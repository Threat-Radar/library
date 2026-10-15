#!/usr/bin/env python3
"""Reproduce every recorded result in expected.yaml (ECMA-427 1st edition fixtures).

Library-written helper (hence the .derived. infix); it contains no Ecma text.
Run it from the repository root with an isolated interpreter that has the
pinned tools installed (see README.md in this directory):

    python3 -I records/other/ecma-427/distilled/examples/run-fixtures.derived.py
    python3 -I records/other/ecma-427/distilled/examples/run-fixtures.derived.py --json

Default mode recomputes every tool result and compares it with the `actual`
and `comparison` blocks recorded in expected.yaml, after these self-checks:

  * the validation schema has the pinned SHA-256 and passes the Draft-07
    meta-schema check;
  * every verbatim/ file is the fixture string plus one LF, and occurs in the
    text rendering of the source (when .cache/ecma-427.txt is present);
  * every quoted rule in expected.yaml is a verbatim substring of that text;
  * every quoted Annex A constraint occurs line for line in the schema file;
  * every type-definition fixture other than minimal-valid differs from it at
    exactly the one JSON Pointer its entry names.

Exit status 0 means every recorded result was reproduced. `--json` prints the
recomputed results instead of comparing them. ECMA-262 cross-checks run only
when `node` is on PATH; without it they are reported as skipped.
"""
import argparse
import hashlib
import importlib.metadata as md
import json
import pathlib
import re
import shutil
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
SCHEMA_SHA256 = "b8988773ac628fe97a33fccabaf19bb45262bb4bd56002fa3d0ab3be72dae983"
DEFAULT_SCHEMA = ROOT / ".cache" / "purl-spec" / "schema-1.0-at-v1.0.0.json"
DEFAULT_SOURCE_TEXT = ROOT / ".cache" / "ecma-427.txt"
TOOLS = [("python", None), ("jsonschema", "jsonschema"),
         ("packageurl_python", "packageurl-python"), ("pyyaml", "PyYAML"),
         ("referencing", "referencing"), ("rfc3987", "rfc3987")]


# ---------------------------------------------------------------- helpers

def pointer_get(doc, ptr):
    """Resolve a JSON Pointer (RFC 6901) against a parsed JSON document."""
    if ptr == "":
        return doc
    cur = doc
    for raw in ptr.split("/")[1:]:
        tok = raw.replace("~1", "/").replace("~0", "~")
        cur = cur[int(tok)] if isinstance(cur, list) else cur[tok]
    return cur


def pointer_of(parts):
    return "".join("/" + str(p).replace("~", "~0").replace("/", "~1") for p in parts)


def diff_pointers(a, b, base=""):
    """JSON Pointers at which two JSON values differ (lists compared whole)."""
    if isinstance(a, dict) and isinstance(b, dict):
        out = []
        for k in sorted(set(a) | set(b)):
            p = base + "/" + k.replace("~", "~0").replace("/", "~1")
            if k not in a or k not in b:
                out.append(p)
            else:
                out.extend(diff_pointers(a[k], b[k], p))
        return out
    return [] if a == b and type(a) is type(b) else [base]


def normalise_source(text):
    """Text rendering with page furniture removed and whitespace collapsed."""
    keep = []
    for line in text.splitlines():
        if "\u00a9 Ecma International 2025" in line and re.fullmatch(
                r"\s*(?:[ivx]+|\d+)?\s*\u00a9 Ecma International 2025\s*(?:[ivx]+|\d+)?\s*", line):
            continue
        keep.append(line)
    joined = "\n".join(keep)
    joined = re.sub(r"-\n\s*", "-", joined)  # a word split at its own hyphen
    return re.sub(r"\s+", " ", joined)


def collapse(s):
    return re.sub(r"\s+", " ", s).strip()


def lines_occur(needle_lines, hay_lines):
    """True when the stripped needle lines occur consecutively in the haystack."""
    n = [ln.strip() for ln in needle_lines if ln.strip()]
    h = [ln.strip() for ln in hay_lines if ln.strip()]
    return any(h[i:i + len(n)] == n for i in range(len(h) - len(n) + 1))


def read_fixture_text(rel):
    raw = (HERE / rel).read_bytes()
    if not raw.endswith(b"\n") or raw.endswith(b"\n\n") or b"\r" in raw:
        raise ValueError(f"{rel}: must end with exactly one LF and contain no CR")
    return raw[:-1].decode("utf-8")


def versions():
    out = {"python": sys.version.split()[0]}
    for key, dist in TOOLS:
        if dist:
            try:
                out[key] = md.version(dist)
            except md.PackageNotFoundError:
                out[key] = "not installed"
    return out


# ---------------------------------------------------------- tool runners

def js_errors(validator, instance):
    errs = sorted(validator.iter_errors(instance),
                  key=lambda e: (pointer_of(e.absolute_path), pointer_of(e.absolute_schema_path), e.message))
    return [{"instance_path": pointer_of(e.absolute_path),
             "schema_path": pointer_of(e.absolute_schema_path),
             "keyword": str(e.validator),
             "message": e.message} for e in errs]


def js_result(validator, instance):
    errors = js_errors(validator, instance)
    out = {"result": "valid" if not errors else "invalid"}
    if errors:
        out["errors"] = errors
    return out


def run_packageurl(s):
    from packageurl import PackageURL
    try:
        p = PackageURL.from_string(s)
    except Exception as exc:  # the library signals every rejection with ValueError
        return {"from_string": type(exc).__name__, "error": str(exc)}
    return {"from_string": "ok",
            "components": {"type": p.type, "namespace": p.namespace or "", "name": p.name,
                           "version": p.version or "", "qualifiers": dict(p.qualifiers or {}),
                           "subpath": p.subpath or ""},
            "to_string": p.to_string()}


NODE_JS = r"""
const cases = JSON.parse(require('fs').readFileSync(0, 'utf8'));
process.stdout.write(JSON.stringify(cases.map(c => {
  const r = {};
  for (const [label, flags] of [['no_flags', ''], ['u_flag', 'u']]) {
    try {
      const re = new RegExp(c.pattern, flags);
      r[label] = c.value === null ? 'compiles' : (re.test(c.value) ? 'matches' : 'does not match');
    } catch (e) { r[label] = e.name; }
  }
  return r;
})));
"""


def run_node(cases):
    """ECMA-262 behaviour of each {pattern, value} case, or None without node."""
    node = shutil.which("node")
    if not node or not cases:
        return None
    res = subprocess.run([node, "-e", NODE_JS], input=json.dumps(cases),
                         capture_output=True, text=True, check=True)
    return json.loads(res.stdout)


def node_version():
    node = shutil.which("node")
    if not node:
        return "not available"
    return subprocess.run([node, "--version"], capture_output=True, text=True).stdout.strip()


# ------------------------------------------------------------ computation

def resolve_from(spec, schema, instance):
    """'schema:/ptr' or 'instance:/ptr' to the value it names."""
    where, _, ptr = spec.partition(":")
    return pointer_get(schema if where == "schema" else instance, ptr)


def compute(fx, schema, v_plain, v_fmt, node_cache):
    """Recompute the `actual` and `comparison` blocks of one fixture."""
    from jsonschema import Draft7Validator
    kind = fx["kind"]
    exp = fx.get("expected", {})
    if kind == "purl":
        sub = schema["properties"]["examples"]["items"]
        js = js_result(Draft7Validator(sub), fx["string"])
        js = dict({"subschema": "/properties/examples/items"}, **js)
        pp = run_packageurl(fx["string"])
        actual = {"jsonschema": js, "packageurl_python": pp}
        res = exp["result"]
        if res == "unspecified":
            agree = "n/a"
        elif res == "reject":
            agree = "agrees" if pp["from_string"] != "ok" else "differs"
        else:
            want = {k: v for k, v in exp["components"].items() if k != "scheme"}
            ok = pp["from_string"] == "ok" and pp["components"] == want
            if ok and exp.get("canonical"):
                ok = pp["to_string"] == exp["canonical"]
            agree = "agrees" if ok else "differs"
        return actual, {"packageurl_python": agree}
    if kind in ("type-string", "type-name"):
        ptr = "/properties/type" if kind == "type-string" else "/properties/type_name"
        js = dict({"subschema": ptr}, **js_result(Draft7Validator(pointer_get(schema, ptr)), fx["string"]))
        actual = {"jsonschema": js, "packageurl_python": "n/a (not a purl)"}
        return actual, {"jsonschema": "agrees" if js["result"] == exp["result"] else "differs"}
    if kind == "annex-a-examples-array":
        fragment = json.loads("{" + read_fixture_text(fx["file"]) + "}")["examples"]
        ptr = fx["schema_pointer"]
        sub = pointer_get(schema, ptr.rsplit("/", 1)[0])
        items = [dict({"value": v}, **js_result(Draft7Validator(sub), v)) for v in fragment]
        actual = {"equals_schema_value": "yes" if fragment == pointer_get(schema, ptr) else "no",
                  "jsonschema_items": items, "packageurl_python": "n/a (not a purl)"}
        all_valid = all(i["result"] == "valid" for i in items)
        return actual, {"jsonschema": "agrees" if all_valid == (exp["result"] == "valid") else "differs"}
    if kind == "type-definition":
        inst = json.loads((HERE / fx["file"]).read_text(encoding="utf-8"))
        actual = {"jsonschema": {"without_format_checker": js_result(v_plain, inst),
                                 "with_format_checker": js_result(v_fmt, inst)},
                  "packageurl_python": "n/a (not a purl)"}
        chk = fx.get("ecma262_check")
        if chk:
            key = (fx["id"],)
            if key in node_cache:
                actual["ecma262_node"] = node_cache[key]
        cmp = {name: ("agrees" if actual["jsonschema"][name]["result"] == exp["result"] else "differs")
               for name in ("without_format_checker", "with_format_checker")}
        return actual, cmp
    raise ValueError(f"{fx['id']}: unknown kind {kind!r}")


def node_cases(doc, schema):
    keys, cases = [], []
    for fx in doc["fixtures"]:
        chk = fx.get("ecma262_check")
        if not chk:
            continue
        inst = json.loads((HERE / fx["file"]).read_text(encoding="utf-8"))
        value = resolve_from(chk["test_value_from"], schema, inst) if chk.get("test_value_from") else None
        keys.append((fx["id"],))
        cases.append({"pattern": resolve_from(chk["pattern_from"], schema, inst), "value": value})
    for p in ("/properties/$id/pattern", "/properties/type/pattern", "/properties/examples/items/pattern"):
        keys.append(("schema", p))
        cases.append({"pattern": pointer_get(schema, p), "value": None})
    out = run_node(cases)
    if out is None:
        return None
    res = {}
    for k, r in zip(keys, out):
        if k[0] == "schema":
            res[k] = {"pointer": k[1], "no_flags": r["no_flags"], "u_flag": r["u_flag"]}
        else:
            src = next(f["ecma262_check"] for f in doc["fixtures"] if f["id"] == k[0])
            entry = {"pattern_from": src["pattern_from"]}
            if src.get("test_value_from"):
                entry["test_value_from"] = src["test_value_from"]
            entry.update(no_flags=r["no_flags"], u_flag=r["u_flag"])
            res[k] = entry
    return res


# ------------------------------------------------------------- self-checks

# Keys whose values are quotations of the source: each must occur verbatim
# (whitespace-collapsed) in the text rendering.
VERBATIM_FIELDS = ("rule", "lead", "item", "prose_rule", "prose_lead", "prose_item")


def walk_dicts(node):
    """Every dict nested anywhere in a parsed YAML node, outermost first."""
    if isinstance(node, dict):
        yield node
        for v in node.values():
            yield from walk_dicts(v)
    elif isinstance(node, list):
        for v in node:
            yield from walk_dicts(v)


def self_checks(doc, schema, schema_text, source_text):
    errs = []
    norm = normalise_source(source_text) if source_text is not None else None
    src_lines = source_text.splitlines() if source_text is not None else None
    if norm is not None:
        for r in doc.get("rules", []):
            for field in ("text", "lead", "item"):
                if field in r and collapse(r[field]) not in norm:
                    errs.append(f"rule {r['id']}: {field} is not verbatim in the source text")
        if collapse(doc.get("reject_rule", {}).get("rule", "")) not in norm:
            errs.append("reject_rule: rule is not verbatim in the source text")
    base = None
    for fx in doc["fixtures"]:
        if fx["kind"] == "type-definition" and fx["id"] == "TD-POS-01":
            base = json.loads((HERE / fx["file"]).read_text(encoding="utf-8"))
    for fx in doc["fixtures"]:
        fid, kind = fx["id"], fx["kind"]
        f = fx.get("file", "")
        if f.startswith("verbatim/"):
            content = read_fixture_text(f)
            if kind == "annex-a-examples-array":
                if src_lines is not None and not lines_occur(content.splitlines(), src_lines):
                    errs.append(f"{fid}: {f} lines do not occur in the source text")
                same = [next(g["string"] for g in doc["fixtures"] if g["id"] == i)
                        for i in fx["expected"].get("same_values_as", [])]
                if same != json.loads("{" + content + "}")["examples"]:
                    errs.append(f"{fid}: values differ from the fixtures named in same_values_as")
            else:
                if content != fx["string"]:
                    errs.append(f"{fid}: {f} differs from the entry's string")
                if norm is not None and collapse(content) not in norm:
                    errs.append(f"{fid}: {f} is not verbatim in the source text")
        for v in walk_dicts({k: fx[k] for k in fx if k not in ("actual", "comparison")}):
            if norm is not None:
                for field in VERBATIM_FIELDS:
                    if field in v and collapse(v[field]) not in norm:
                        errs.append(f"{fid}: {field} is not verbatim in the source text")
            if "annex_a" in v:
                if not lines_occur(v["annex_a"].splitlines(), schema_text.splitlines()):
                    errs.append(f"{fid}: annex_a quote does not occur in the schema file")
                val = pointer_get(schema, v["annex_a_pointer"])
                vals = val if isinstance(val, list) else [val]
                if isinstance(val, dict) or not all(json.dumps(x) in v["annex_a"] for x in vals):
                    errs.append(f"{fid}: annex_a_pointer value not in the quoted lines")
        if kind == "type-definition" and fid != "TD-POS-01":
            inst = json.loads((HERE / f).read_text(encoding="utf-8"))
            got = diff_pointers(base, inst)
            if got != [fx["mutation"]]:
                errs.append(f"{fid}: differs from minimal-valid at {got}, entry says {fx['mutation']!r}")
    return errs


# ------------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--schema", default=str(DEFAULT_SCHEMA))
    ap.add_argument("--source-text", default=str(DEFAULT_SOURCE_TEXT))
    ap.add_argument("--expected", default=str(HERE / "expected.yaml"))
    ap.add_argument("--json", action="store_true", help="print recomputed results as JSON")
    args = ap.parse_args()

    import yaml
    from jsonschema import Draft7Validator

    doc = yaml.safe_load(pathlib.Path(args.expected).read_text(encoding="utf-8"))
    schema_path = pathlib.Path(args.schema)
    schema_bytes = schema_path.read_bytes()
    schema_text = schema_bytes.decode("utf-8")
    schema = json.loads(schema_text)
    src_path = pathlib.Path(args.source_text)
    source_text = src_path.read_text(encoding="utf-8") if src_path.exists() else None

    problems, notes = [], []
    env = versions()
    for k, v in env.items():
        want = str(doc.get("tools", {}).get(k, ""))
        if want and want != v:
            notes.append(f"tool {k}: running {v}, expected.yaml was recorded with {want}")
    sha = hashlib.sha256(schema_bytes).hexdigest()
    try:
        Draft7Validator.check_schema(schema)
        meta = "ok"
    except Exception as exc:  # SchemaError
        meta = f"{type(exc).__name__}: {exc}"
    node_cache = node_cases(doc, schema)
    schema_checks = {"sha256": sha, "draft7_check_schema": meta}
    if node_cache is not None:
        schema_checks["ecma262_patterns"] = [v for k, v in node_cache.items() if k[0] == "schema"]
    if sha != SCHEMA_SHA256:
        problems.append(f"schema SHA-256 is {sha}, expected {SCHEMA_SHA256}")
    if source_text is None:
        notes.append(f"{src_path} not found: verbatim-against-source checks skipped")
    if node_cache is None:
        notes.append("node not on PATH: ECMA-262 cross-checks skipped")
    problems += self_checks(doc, schema, schema_text, source_text)

    v_plain = Draft7Validator(schema)
    v_fmt = Draft7Validator(schema, format_checker=Draft7Validator.FORMAT_CHECKER)
    fresh = {}
    for fx in doc["fixtures"]:
        actual, comparison = compute(fx, schema, v_plain, v_fmt, node_cache or {})
        fresh[fx["id"]] = {"actual": actual, "comparison": comparison}

    if args.json:
        for p in problems:
            print("FAIL:", p, file=sys.stderr)
        print(json.dumps({"tools": env, "node": node_version(), "schema_checks": schema_checks,
                          "fixtures": fresh}, indent=2, ensure_ascii=False))
        return 1 if problems else 0

    recorded_checks = dict(doc.get("schema_checks", {}))
    if node_cache is None:
        recorded_checks.pop("ecma262_patterns", None)
    if recorded_checks != schema_checks:
        problems.append("schema_checks differ from the recorded ones")
    differs = 0
    for fx in doc["fixtures"]:
        got = fresh[fx["id"]]
        rec_actual = dict(fx.get("actual", {}))
        if node_cache is None:
            rec_actual.pop("ecma262_node", None)
        if rec_actual != got["actual"]:
            problems.append(f"{fx['id']}: recorded actual result does not match this run")
        if fx.get("comparison") != got["comparison"]:
            problems.append(f"{fx['id']}: recorded comparison does not match this run")
        if any(str(v).startswith("differs") for v in got["comparison"].values()):
            differs += 1
            if not str(fx.get("finding", "")).strip():
                problems.append(f"{fx['id']}: a tool differs from the expected result but no finding is written")
    for n in notes:
        print("note:", n)
    for p in problems:
        print("FAIL:", p)
    total = len(doc["fixtures"])
    print(f"{total} fixtures; {differs} where a tool differs from the expected result "
          f"(each has a finding); {len(problems)} problems")
    print("tools:", ", ".join(f"{k} {v}" for k, v in env.items()), "| node", node_version())
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
