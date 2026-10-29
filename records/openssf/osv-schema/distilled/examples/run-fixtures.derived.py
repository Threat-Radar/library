#!/usr/bin/env python3
"""Reproduce every recorded result in expected.yaml (OSV Schema v1.9.2 fixtures).

Library-written helper (hence the .derived. infix). It contains no source text
apart from the pinned digests. Run it from the repository root with an
isolated interpreter that has the pinned tools installed (README.md in this
directory gives the setup):

    python -I records/openssf/osv-schema/distilled/examples/run-fixtures.derived.py
    python -I records/openssf/osv-schema/distilled/examples/run-fixtures.derived.py --json

Default mode recomputes every tool result and compares it with the `actual`
and `comparison` blocks recorded in expected.yaml, after these self-checks:

  * the JSON Schema has the pinned SHA-256, names the 2020-12 dialect and
    passes its meta-schema check;
  * when the source text is present (it is never committed): it has the
    pinned SHA-256; every verbatim/blocks/ file equals the lines between its
    fences; every verbatim/inline/ example occurs on its line; every quoted
    rule occurs in the source at the lines and under the heading its locator
    names; every prose list in `enumerations` is what the source holds;
  * every derived record differs from the fixture named in derived_from only
    at or below the JSON Pointers listed in mutations, and a record that embeds
    a source example carries that example's values;
  * every rule a fixture cites exists and is cited with its own locator; every
    finding and source issue names fixtures that exist; every fixture on which
    a tool differs from the expected result names a finding; the counts match.

Exit status 0 means every recorded result was reproduced. `--json` prints the
recomputed results instead of comparing them. ECMA-262 checks run only when
`node` is on PATH; without it they are reported as skipped.
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
CACHE = ROOT / ".cache" / "osv-schema-v1.9.2"
DEFAULT_SCHEMA = CACHE / "validation" / "schema.json"
DEFAULT_SOURCE = CACHE / "docs" / "schema.md"
SCHEMA_SHA256 = "15b10dbb4c4e31c7aae11d22cdd991a9a374758db7c8389e62b3cc37cac92653"
SOURCE_SHA256 = "96d82f03d763fb408bc344d01fc271f761a81cc225f6f6a42d318e3ed21cebff"
DIALECT = "https://json-schema.org/draft/2020-12/schema"
TOOLS = [("jsonschema", "jsonschema"), ("referencing", "referencing"),
         ("jsonschema_specifications", "jsonschema-specifications"),
         ("rfc3339_validator", "rfc3339-validator"), ("rfc3987", "rfc3987"),
         ("pyyaml", "PyYAML")]
RANGES_PTR = "/properties/affected/items/properties/ranges"
CREDITS_PTR = "/properties/credits"
PACKAGE_PTR = "/properties/affected/items/properties/package"
REGEX_FIXTURE = "SRC-L0156"          # the fenced regular expression for ids
GROUPS = ("SRC", "EMB", "POS", "NEG", "GAP", "OVER", "SHOULD", "EDGE", "TOOL")


# ---------------------------------------------------------------- helpers

def esc(token):
    return str(token).replace("~", "~0").replace("/", "~1")


def pointer_of(parts):
    return "".join("/" + esc(p) for p in parts)


def pointer_get(doc, ptr):
    """Resolve a JSON Pointer (RFC 6901)."""
    if ptr == "":
        return doc
    cur = doc
    for raw in ptr.split("/")[1:]:
        tok = raw.replace("~1", "/").replace("~0", "~")
        cur = cur[int(tok)] if isinstance(cur, list) else cur[tok]
    return cur


def resolve_from(spec, schema, instance):
    """'schema:/ptr' or 'instance:/ptr' to the value it names."""
    where, _, ptr = spec.partition(":")
    return pointer_get(schema if where == "schema" else instance, ptr)


def diff_pointers(a, b, base=""):
    """JSON Pointers at which two JSON values differ.

    Objects are compared key by key and arrays of equal length item by item;
    an array whose length changed is reported as a whole."""
    if isinstance(a, dict) and isinstance(b, dict):
        out = []
        for k in sorted(set(a) | set(b)):
            p = base + "/" + esc(k)
            if k not in a or k not in b:
                out.append(p)
            else:
                out.extend(diff_pointers(a[k], b[k], p))
        return out
    if isinstance(a, list) and isinstance(b, list) and len(a) == len(b):
        out = []
        for i, (x, y) in enumerate(zip(a, b)):
            out.extend(diff_pointers(x, y, f"{base}/{i}"))
        return out
    return [] if (a == b and type(a) is type(b)) else [base]


def under(p, m):
    return p == m or p.startswith(m + "/")


def collapse(s):
    return re.sub(r"\s+", " ", s).strip()


def repair_trailing_commas(text):
    """Remove each comma that is followed, after optional whitespace, by ] or }."""
    return re.subn(r",(\s*[\]}])", r"\1", text)


def json_attempt(text):
    try:
        json.loads(text)
        return {"result": "ok"}
    except json.JSONDecodeError as exc:
        return {"result": "error", "message": exc.msg, "line": str(exc.lineno), "column": str(exc.colno)}


def read_text(rel):
    raw = (HERE / rel).read_bytes()
    if b"\r" in raw:
        raise ValueError(f"{rel}: contains a carriage return")
    return raw.decode("utf-8")


def read_inline(rel):
    """An inline example file: the example text plus exactly one LF."""
    text = read_text(rel)
    if not text.endswith("\n") or text.endswith("\n\n"):
        raise ValueError(f"{rel}: must end with exactly one LF")
    return text[:-1]


def versions():
    out = {"python": sys.version.split()[0]}
    for key, dist in TOOLS:
        try:
            out[key] = md.version(dist)
        except md.PackageNotFoundError:
            out[key] = "not installed"
    return out


# ------------------------------------------------------------- the source

class Source:
    """docs/schema.md: its lines, the heading path in force on each line, and
    a whitespace-collapsed copy with a map back to line numbers."""

    def __init__(self, text):
        self.text = text
        self.lines = text.split("\n")
        if self.lines and self.lines[-1] == "":
            self.lines.pop()
        self.paths = {}
        stack, in_fence, start = [], False, 0
        if self.lines and self.lines[0] == "---":
            start = self.lines.index("---", 1) + 1
        for n, ln in enumerate(self.lines, 1):
            if n <= start:
                self.paths[n] = ""
                continue
            if ln.lstrip().startswith("```"):
                in_fence = not in_fence
            elif not in_fence:
                m = re.match(r"^(#{1,6})\s+(.*?)\s*$", ln)
                if m:
                    level = len(m.group(1))
                    while stack and stack[-1][0] >= level:
                        stack.pop()
                    stack.append((level, m.group(2)))
            self.paths[n] = " > ".join(t for _, t in stack)
        chars, owner, prev_space = [], [], False
        for n, ln in enumerate(self.lines, 1):
            for ch in ln + "\n":
                if ch.isspace():
                    if not prev_space and chars:
                        chars.append(" ")
                        owner.append(n)
                    prev_space = True
                else:
                    chars.append(ch)
                    owner.append(n)
                    prev_space = False
        self.flat = "".join(chars)
        self.owner = owner

    def locate(self, quote):
        """Every (first line, last line) at which a collapsed quote occurs."""
        q = collapse(quote)
        out, i = [], self.flat.find(q)
        while i >= 0 and q:
            out.append((self.owner[i], self.owner[i + len(q) - 1]))
            i = self.flat.find(q, i + 1)
        return out


def locator(path, first, last):
    span = f"L{first}" if first == last else f"L{first}-{last}"
    return f"§ {path} / {span}"


# ------------------------------------------------------------ JSON Schema

class Ctx:
    def __init__(self, schema, source, node):
        from jsonschema import Draft202012Validator, validators
        from referencing import Registry, Resource
        self.schema = schema
        self.source = source
        self.cls = validators.validator_for(schema)
        self.uri = schema["$id"]
        self.registry = Registry().with_resource(self.uri, Resource.from_contents(schema))
        self.fc = Draft202012Validator.FORMAT_CHECKER
        self.plain = self.cls(schema)
        self.fmt = self.cls(schema, format_checker=self.fc)
        self.node = node
        self.node_results = {}
        self._subs = {}

    def sub(self, ptr, fmt):
        key = (ptr, fmt)
        if key not in self._subs:
            kw = {"registry": self.registry}
            if fmt:
                kw["format_checker"] = self.fc
            self._subs[key] = self.cls({"$ref": self.uri + "#" + ptr}, **kw)
        return self._subs[key]


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


def both_modes(ctx, instance, ptr=None):
    if ptr is None:
        return {"without_format_checker": js_result(ctx.plain, instance),
                "with_format_checker": js_result(ctx.fmt, instance)}
    return {"subschema": ptr,
            "without_format_checker": js_result(ctx.sub(ptr, False), instance),
            "with_format_checker": js_result(ctx.sub(ptr, True), instance)}


def compare_modes(expected, js):
    if expected not in ("valid", "invalid"):
        return {"without_format_checker": "n/a", "with_format_checker": "n/a"}
    return {m: ("agrees" if js[m]["result"] == expected else "differs")
            for m in ("without_format_checker", "with_format_checker")}


def schema_patterns(node, base=""):
    out = []
    if isinstance(node, dict):
        for k, v in node.items():
            p = base + "/" + esc(k)
            if k == "pattern" and isinstance(v, str):
                out.append((p, v))
            else:
                out.extend(schema_patterns(v, p))
    elif isinstance(node, list):
        for i, v in enumerate(node):
            out.extend(schema_patterns(v, f"{base}/{i}"))
    return out


def schema_refs(node):
    out = set()
    if isinstance(node, dict):
        for k, v in node.items():
            if k == "$ref" and isinstance(v, str):
                out.add(v)
            else:
                out |= schema_refs(v)
    elif isinstance(node, list):
        for v in node:
            out |= schema_refs(v)
    return out


def schema_field_paths(schema):
    """Dotted field paths the JSON Schema defines ('[]' marks array items),
    gathering properties from allOf/anyOf/oneOf members and if/then/else."""
    def deref(n):
        while isinstance(n, dict) and "$ref" in n:
            n = pointer_get(schema, n["$ref"][1:])
        return n

    def props(n):
        n = deref(n)
        found, items = {}, []
        if not isinstance(n, dict):
            return found, items
        for k, v in n.get("properties", {}).items():
            found.setdefault(k, []).append(v)
        if isinstance(n.get("items"), dict):
            items.append(n["items"])
        for key in ("allOf", "anyOf", "oneOf"):
            for m in n.get(key, []):
                f2, i2 = props(m)
                for k, v in f2.items():
                    found.setdefault(k, []).extend(v)
                items.extend(i2)
        for key in ("if", "then", "else"):
            if isinstance(n.get(key), dict):
                f2, i2 = props(n[key])
                for k, v in f2.items():
                    found.setdefault(k, []).extend(v)
                items.extend(i2)
        return found, items

    def walk(nodes, prefix):
        out = set()
        found, items = {}, []
        for n in nodes:
            f2, i2 = props(n)
            for k, v in f2.items():
                found.setdefault(k, []).extend(v)
            items.extend(i2)
        for k, subs in found.items():
            p = prefix + ("." if prefix else "") + k
            out.add(p)
            out |= walk(subs, p)
        if items:
            out |= walk(items, prefix + "[]")
        return out

    return walk([schema], "")


def shape_to_json(text):
    """An informal shape block as JSON: the placeholder string becomes "",
    { see description } becomes {}, trailing commas are removed."""
    t = text.replace("{ see description }", "{}")
    t = re.sub(r'(?<!")\bstring\b(?!")', '""', t)
    t, _ = repair_trailing_commas(t)
    return json.loads(t)


def shape_field_paths(value, prefix=""):
    out = set()
    if isinstance(value, dict):
        for k, v in value.items():
            p = prefix + ("." if prefix else "") + k
            out.add(p)
            out |= shape_field_paths(v, p)
    elif isinstance(value, list):
        for v in value:
            out |= shape_field_paths(v, prefix + "[]")
    return out


# --------------------------------------------------------------- ECMA-262

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


# ------------------------------------------------- evaluation (pseudocode)
# A literal transcription of IncludedInRanges and BeforeLimits from the
# source's Evaluation pseudocode (verbatim/blocks/L1247-evaluation.txt), with
# versions ordered by SemVer 2.0.0 precedence, "0" (introduced) before every
# version and "*" (limit) after every version.

SEMVER = re.compile(
    r"^(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)"
    r"(?:-((?:0|[1-9][0-9]*|[0-9]*[a-zA-Z-][0-9a-zA-Z-]*)"
    r"(?:\.(?:0|[1-9][0-9]*|[0-9]*[a-zA-Z-][0-9a-zA-Z-]*))*))?"
    r"(?:\+([0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$")


def semver_key(v):
    m = SEMVER.match(v)
    if not m:
        raise ValueError(f"not a SemVer 2.0.0 version: {v!r}")
    major, minor, patch, pre = int(m.group(1)), int(m.group(2)), int(m.group(3)), m.group(4)
    if pre is None:
        pk = (1,)
    else:
        pk = (0,) + tuple((0, int(p), "") if p.isdigit() else (1, 0, p) for p in pre.split("."))
    return (major, minor, patch, pk)


def event_value(evt):
    for k in ("introduced", "fixed", "last_affected", "limit"):
        if k in evt:
            return k, evt[k]
    raise ValueError(f"event without a version: {evt!r}")


def order_key(kind, value):
    if kind == "introduced" and value == "0":
        return (0,)
    if kind == "limit" and value == "*":
        return (2,)
    return (1, semver_key(value))


def cmp_versions(v, kind, value):
    a, b = (1, semver_key(v)), order_key(kind, value)
    return (a > b) - (a < b)


def before_limits(v, rng):
    if not any("limit" in e for e in rng["events"]):
        return True                      # implicit "*" entry is assumed
    for evt in rng["events"]:
        if "limit" in evt and cmp_versions(v, "limit", evt["limit"]) < 0:
            return True
    return False


def included_in_ranges(v, ranges):
    for rng in ranges:
        if before_limits(v, rng):
            vulnerable = False
            for evt in sorted(rng["events"], key=lambda e: order_key(*event_value(e))):
                if "introduced" in evt and cmp_versions(v, "introduced", evt["introduced"]) >= 0:
                    vulnerable = True
                elif "fixed" in evt and cmp_versions(v, "fixed", evt["fixed"]) >= 0:
                    vulnerable = False
                elif "last_affected" in evt and cmp_versions(v, "last_affected", evt["last_affected"]) > 0:
                    vulnerable = False
            if vulnerable:
                return True
    return False


# ------------------------------------------------------------ computation

def get_inline_value(fx):
    text = fx["example_text"]
    syntax = fx.get("syntax", "text")
    if syntax == "text":
        return text
    if syntax == "json":
        return json.loads(text)
    if syntax == "json-member":
        obj = json.loads("{" + text + "}")
        (only,) = obj.values()
        return only
    raise ValueError(f"{fx['id']}: unknown syntax {syntax!r}")


def node_check_entry(fx, ctx):
    chk = fx.get("ecma262_check")
    if not chk:
        return None
    key = fx["id"]
    if ctx.node_results.get(key) is None:
        return None
    r = ctx.node_results[key]
    return {"pattern_from": chk["pattern_from"], "test_value_from": chk["test_value_from"],
            "no_flags": r["no_flags"], "u_flag": r["u_flag"]}


def compare_parse(exp, parse):
    """Whether the bytes as printed are a JSON text, against `printed_json`."""
    want = exp.get("printed_json", "valid")
    return "agrees" if (parse["result"] == "ok") == (want == "valid") else "differs"


def compute(fx, ctx, prose_regex):
    """Recompute the `actual` and `comparison` blocks of one fixture."""
    kind = fx["kind"]
    exp = fx.get("expected", {})
    want = exp.get("result")
    if kind == "record":
        text = read_text(fx["file"])
        parse = json_attempt(text)
        if parse["result"] != "ok":
            return {"json_parse": parse}, {"json_parse": compare_parse(exp, parse)}
        inst = json.loads(text)
        js = both_modes(ctx, inst)
        actual = {"json_parse": parse, "jsonschema": js}
        if isinstance(inst, dict) and isinstance(inst.get("id"), str):
            actual["prose_id_regex"] = "matches" if re.fullmatch(prose_regex, inst["id"]) else "does not match"
        else:
            actual["prose_id_regex"] = "n/a (no string id)"
        cmp = dict({"json_parse": compare_parse(exp, parse)}, **compare_modes(want, js))
        nd = node_check_entry(fx, ctx)
        if nd is not None:
            actual["ecma262_node"] = nd
            reading = "invalid" if nd["no_flags"] == "does not match" else "valid"
            cmp["schema_read_as_ecma262"] = ("n/a" if want not in ("valid", "invalid")
                                             else "agrees" if reading == want else "differs")
        return actual, cmp
    if kind == "informal-shape":
        text = read_text(fx["file"])
        shape = shape_to_json(text)
        paths = shape_field_paths(shape)
        scope = {k for k in shape}
        defined = {p for p in schema_field_paths(ctx.schema) if re.split(r"[.\[]", p)[0] in scope}
        actual = {"json_parse": json_attempt(text),
                  "field_paths": sorted(paths),
                  "missing_from_schema": sorted(paths - defined),
                  "missing_from_shape": sorted(defined - paths)}
        ok = (actual["missing_from_schema"] == exp.get("missing_from_schema", [])
              and actual["missing_from_shape"] == exp.get("missing_from_shape", []))
        return actual, {"field_paths": "agrees" if ok else "differs"}
    if kind == "rule-regex":
        text = read_text(fx["file"]).rstrip("\n")
        try:
            re.compile(text)
            py = "compiles"
        except re.error as exc:
            py = f"error: {exc}"
        actual = {"python_re": py}
        r = ctx.node_results.get(fx["id"])
        if r is not None:
            actual["ecma262_node"] = {"no_flags": r["no_flags"], "u_flag": r["u_flag"]}
        return actual, {"compiles": "agrees" if py == "compiles" else "differs"}
    if kind == "algorithm":
        return {"note": "pseudocode, not executed; run-fixtures.derived.py transcribes IncludedInRanges and BeforeLimits"}, {}
    if kind == "package-object":
        text = read_text(fx["file"])
        parse = json_attempt(text)
        js = both_modes(ctx, json.loads(text), PACKAGE_PTR)
        actual = {"json_parse": parse, "jsonschema": js}
        return actual, dict({"json_parse": compare_parse(exp, parse)}, **compare_modes(want, js))
    if kind in ("ranges-fragment", "partial-record"):
        text = read_text(fx["file"])
        wrapped = "{" + text + "}" if kind == "ranges-fragment" else text
        repaired, n = repair_trailing_commas(wrapped)
        member = "ranges" if kind == "ranges-fragment" else "credits"
        value = json.loads(repaired)[member]
        ptr = RANGES_PTR if member == "ranges" else CREDITS_PTR
        js = both_modes(ctx, value, ptr)
        parse = json_attempt(wrapped)
        actual = {"json_parse_as_printed": parse,
                  "trailing_commas_removed": str(n),
                  "jsonschema": js}
        cmp = dict({"json_parse": compare_parse(exp, parse)}, **compare_modes(want, js))
        ev = fx.get("evaluation")
        if ev and ev.get("probes"):
            got = [{"version": p["version"], "affected": "yes" if included_in_ranges(p["version"], value) else "no"}
                   for p in ev["probes"]]
            actual["evaluation"] = got
            same = all(g["affected"] == p["affected"] for g, p in zip(got, ev["probes"]))
            cmp["evaluation"] = "agrees" if same else "differs"
        return actual, cmp
    if kind in ("id", "ecosystem", "package-name", "version", "credit-name", "cvss-vector", "event"):
        text = read_inline(fx["file"])
        value = get_inline_value(fx)
        va = fx["validate_as"]
        inst = value
        if "compose" in va:
            inst = va["compose"].replace("{value}", value)
        if "severity_type" in va:
            inst = {"type": va["severity_type"], "score": value}
        js = both_modes(ctx, inst, va["subschema"])
        actual = {"jsonschema": js}
        if inst is not value:
            actual["validated_instance"] = json.dumps(inst, ensure_ascii=False)
        if kind == "id":
            actual["prose_id_regex"] = "matches" if re.fullmatch(prose_regex, value) else "does not match"
        if text != fx["example_text"]:
            actual["file_matches_example_text"] = "no"
        return actual, compare_modes(want, js)
    raise ValueError(f"{fx['id']}: unknown kind {kind!r}")


def compute_schema_checks(ctx):
    pats = []
    for ptr, pat in schema_patterns(ctx.schema):
        try:
            re.compile(pat)
            py = "compiles"
        except re.error as exc:
            py = f"error: {exc}"
        entry = {"pointer": ptr, "python_re": py}
        r = ctx.node_results.get(("schema", ptr))
        if r is not None:
            entry["ecma262_no_flags"] = r["no_flags"]
            entry["ecma262_u_flag"] = r["u_flag"]
        pats.append(entry)
    refs = {r for r in schema_refs(ctx.schema)}
    defs = sorted(ctx.schema.get("$defs", {}))
    unref = [d for d in defs if f"#/$defs/{d}" not in refs]
    try:
        ctx.cls.check_schema(ctx.schema)
        meta = "ok"
    except Exception as exc:  # SchemaError
        meta = f"{type(exc).__name__}: {exc}"
    return {"dialect": ctx.schema.get("$schema", ""),
            "validator": ctx.cls.__name__,
            "check_schema": meta,
            "format_assertion_by_default": "no (format is an annotation unless a format checker is passed)",
            "format_checkers": {"date-time": "available" if "date-time" in ctx.fc.checkers else "missing",
                                "uri": "available" if "uri" in ctx.fc.checkers else "missing"},
            "unreferenced_defs": unref,
            "patterns": pats}


# ----------------------------------------------------------- enumerations

def extract_prose(source, rule, lines):
    a, b = (int(x) for x in lines.split("-"))
    rows = source.lines[a - 1:b]
    out = []
    if rule == "first-td-codes":
        for i, ln in enumerate(rows):
            if ln.strip() == "<tr>" and i + 1 < len(rows):
                out.extend(re.findall(r"<code>(.*?)</code>", rows[i + 1]))
    elif rule == "md-table-first-cell":
        for ln in rows:
            m = re.match(r"^\|\s*`([^`]+)`\s*\|", ln)
            if m:
                out.append(m.group(1))
    elif rule == "bullet-code":
        for ln in rows:
            m = re.match(r"^\s*- `([^`]+)`:", ln)
            if m:
                out.append(m.group(1))
    elif rule == "bullet-text":
        for ln in rows:
            m = re.match(r"^- (\S.*?)\s*$", ln)
            if m:
                out.append(m.group(1))
    else:
        raise ValueError(f"unknown prose extraction rule {rule!r}")
    return out


def extract_schema(schema, rule, ptr):
    if rule == "enum":
        return list(pointer_get(schema, ptr))
    if rule == "none":
        return []
    pat = pointer_get(schema, ptr)
    if rule == "pattern-alternatives":
        inner = re.search(r"\^\((.*)\)\(:\.\+\)\?\$$", pat).group(1)
        return [a.replace("\\.", ".") for a in inner.split("|")]
    if rule == "prefix-alternatives":
        m = re.match(r"^\^\((x_)\|\((.*)\)-\)$", pat)
        out = [m.group(1)]
        for alt in m.group(2).split("|"):
            cls = re.match(r"^(.*)\[([A-Z]+)\](.*)$", alt)
            if cls:
                out.extend(cls.group(1) + c + cls.group(3) for c in cls.group(2))
            else:
                out.append(alt)
        return out
    raise ValueError(f"unknown schema extraction rule {rule!r}")


def compute_enumeration(en, ctx):
    schema_values = extract_schema(ctx.schema, en["schema_extract"], en["schema_pointer"]) \
        if en["schema_extract"] != "none" else []
    prose = list(en["prose_values"])
    return {"schema_values": schema_values,
            "only_in_prose": [v for v in prose if v not in schema_values],
            "only_in_schema": [v for v in schema_values if v not in prose]}


# ------------------------------------------------------------- self-checks

def walk_dicts(node):
    if isinstance(node, dict):
        yield node
        for v in node.values():
            yield from walk_dicts(v)
    elif isinstance(node, list):
        for v in node:
            yield from walk_dicts(v)


def self_checks(doc, ctx):
    errs = []
    src = ctx.source
    rules = {r["id"]: r for r in doc.get("rules", [])}
    fixtures = {f["id"]: f for f in doc["fixtures"]}
    if len(fixtures) != len(doc["fixtures"]):
        errs.append("duplicate fixture ids")
    # rules: verbatim, at their lines, under their heading
    for r in doc.get("rules", []):
        if src is None:
            break
        hits = src.locate(r["text"])
        if not hits:
            errs.append(f"rule {r['id']}: text is not verbatim in the source")
            continue
        locs = [locator(src.paths[a], a, b) for a, b in hits]
        if r["locator"] not in locs:
            errs.append(f"rule {r['id']}: locator {r['locator']!r} is not where the text is ({locs})")
    # citations, wherever they sit in a fixture
    for fx in doc["fixtures"]:
        for d in walk_dicts({k: v for k, v in fx.items() if k not in ("actual", "comparison")}):
            if "rule" in d:
                rid = d["rule"]
                if rid not in rules:
                    errs.append(f"{fx['id']}: cites unknown rule {rid!r}")
                elif d.get("locator") != rules[rid]["locator"]:
                    errs.append(f"{fx['id']}: cites {rid} with locator {d.get('locator')!r}")
    # verbatim files
    for fx in doc["fixtures"]:
        f = fx.get("file", "")
        if f.startswith("verbatim/blocks/"):
            body = read_text(f)
            if src is not None:
                o, c = int(fx["fence"]["open"]), int(fx["fence"]["close"])
                want = "\n".join(src.lines[o:c - 1]) + "\n"
                if body != want:
                    errs.append(f"{fx['id']}: {f} differs from source lines {o + 1}-{c - 1}")
                if src.lines[o - 1] != "```" + fx["fence"]["info"] or src.lines[c - 1] != "```":
                    errs.append(f"{fx['id']}: fence lines or info string differ from the source")
                path = src.paths[o]
                if fx["locator"] != locator(path, o + 1, c - 1):
                    errs.append(f"{fx['id']}: locator should be {locator(path, o + 1, c - 1)!r}")
        elif f.startswith("verbatim/inline/"):
            text = read_inline(f)
            if text != fx["example_text"]:
                errs.append(f"{fx['id']}: {f} is not example_text plus one LF")
            if src is not None:
                n = int(fx["line"])
                if fx["example_text"] not in src.lines[n - 1]:
                    errs.append(f"{fx['id']}: example text does not occur on line {n}")
                if fx["locator"] != locator(src.paths[n], n, n):
                    errs.append(f"{fx['id']}: locator should be {locator(src.paths[n], n, n)!r}")
    # derived records: one stated change from their parent; embedded examples
    for fx in doc["fixtures"]:
        if fx.get("source") != "derived":
            continue
        b = json.loads(read_text(fx["file"]))
        parent = fx.get("derived_from")
        if parent and parent != "none":
            if parent not in fixtures:
                errs.append(f"{fx['id']}: derived_from {parent!r} is not a fixture")
                continue
            a = json.loads(read_text(fixtures[parent]["file"]))
            got = diff_pointers(a, b)
            muts = fx.get("mutations", [])
            stray = [p for p in got if not any(under(p, m) for m in muts)]
            idle = [m for m in muts if not any(under(p, m) for p in got)]
            if stray or idle or not got:
                errs.append(f"{fx['id']}: differs from {parent} at {got}, entry says {muts}")
        emb = fx.get("embeds")
        if emb:
            src_fx = fixtures.get(emb["fixture"])
            if src_fx is None:
                errs.append(f"{fx['id']}: embeds unknown fixture {emb['fixture']!r}")
            else:
                if src_fx["kind"] in ("ranges-fragment",):
                    val = json.loads(repair_trailing_commas("{" + read_text(src_fx["file"]) + "}")[0])["ranges"]
                elif src_fx["kind"] == "partial-record":
                    val = json.loads(repair_trailing_commas(read_text(src_fx["file"]))[0])["credits"]
                elif src_fx["kind"] == "package-object":
                    val = json.loads(read_text(src_fx["file"]))
                else:
                    val = get_inline_value(src_fx)
                if pointer_get(b, emb["at"]) != val:
                    errs.append(f"{fx['id']}: value at {emb['at']} is not the embedded example")
    # findings, issues, counts
    fids = {f["id"] for f in doc.get("findings", [])}
    for group in ("findings", "source_issues"):
        for item in doc.get(group, []):
            for x in item.get("fixtures", []):
                if x not in fixtures:
                    errs.append(f"{group} {item['id']}: unknown fixture {x!r}")
            for x in item.get("rules", []):
                if x not in rules:
                    errs.append(f"{group} {item['id']}: unknown rule {x!r}")
    for fx in doc["fixtures"]:
        for x in fx.get("finding", []):
            if x not in fids:
                errs.append(f"{fx['id']}: unknown finding {x!r}")
    counts = {}
    for fid in fixtures:
        g = fid.split("-")[0]
        counts[g] = counts.get(g, 0) + 1
    want = {k: int(v) for k, v in doc.get("counts", {}).items()}
    if want != counts:
        errs.append(f"counts say {want}, fixtures give {counts}")
    if int(doc.get("fixture_count", -1)) != len(fixtures):
        errs.append(f"fixture_count says {doc.get('fixture_count')}, there are {len(fixtures)}")
    # enumerations: the recorded prose lists are what the source holds
    if src is not None:
        for en in doc.get("enumerations", []):
            got = extract_prose(src, en["prose_extract"], en["prose_lines"])
            extra = list(en.get("prose_extra", []))
            if got + extra != list(en["prose_values"]):
                errs.append(f"enumeration {en['id']}: source gives {got + extra}")
    return errs


def gather_node_cases(doc, ctx, prose_regex):
    keys, cases = [], []
    for ptr, pat in schema_patterns(ctx.schema):
        keys.append(("schema", ptr))
        cases.append({"pattern": pat, "value": None})
    keys.append(REGEX_FIXTURE)
    cases.append({"pattern": prose_regex, "value": None})
    for fx in doc["fixtures"]:
        chk = fx.get("ecma262_check")
        if not chk:
            continue
        inst = json.loads(read_text(fx["file"]))
        keys.append(fx["id"])
        cases.append({"pattern": resolve_from(chk["pattern_from"], ctx.schema, inst),
                      "value": resolve_from(chk["test_value_from"], ctx.schema, inst)})
    out = run_node(cases)
    if out is None:
        return False
    for k, r in zip(keys, out):
        ctx.node_results[k] = r
    return True


# ------------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--schema", default=str(DEFAULT_SCHEMA), help="validation/schema.json at v1.9.2")
    ap.add_argument("--source", default=str(DEFAULT_SOURCE), help="docs/schema.md at v1.9.2")
    ap.add_argument("--expected", default=str(HERE / "expected.yaml"))
    ap.add_argument("--json", action="store_true", help="print recomputed results as JSON")
    args = ap.parse_args()

    import yaml

    doc = yaml.safe_load(pathlib.Path(args.expected).read_text(encoding="utf-8"))
    schema_bytes = pathlib.Path(args.schema).read_bytes()
    schema = json.loads(schema_bytes.decode("utf-8"))
    src_path = pathlib.Path(args.source)
    source = None
    problems, notes = [], []
    if src_path.exists():
        src_bytes = src_path.read_bytes()
        if hashlib.sha256(src_bytes).hexdigest() != SOURCE_SHA256:
            problems.append(f"source SHA-256 is {hashlib.sha256(src_bytes).hexdigest()}, expected {SOURCE_SHA256}")
        else:
            source = Source(src_bytes.decode("utf-8"))
    else:
        notes.append(f"{src_path} not found: checks against the source text skipped")
    sha = hashlib.sha256(schema_bytes).hexdigest()
    if sha != SCHEMA_SHA256:
        problems.append(f"schema SHA-256 is {sha}, expected {SCHEMA_SHA256}")
    if schema.get("$schema") != DIALECT:
        problems.append(f"schema names {schema.get('$schema')!r}, expected {DIALECT}")

    env = versions()
    for k, v in env.items():
        want = str(doc.get("tools", {}).get(k, ""))
        if want and want != v:
            notes.append(f"tool {k}: running {v}, expected.yaml was recorded with {want}")
    nv = node_version()
    if str(doc.get("tools", {}).get("node", "")) not in ("", nv):
        notes.append(f"tool node: running {nv}, expected.yaml was recorded with {doc['tools']['node']}")

    prose_regex = read_text(next(f["file"] for f in doc["fixtures"] if f["id"] == REGEX_FIXTURE)).rstrip("\n")
    ctx = Ctx(schema, source, shutil.which("node"))
    have_node = gather_node_cases(doc, ctx, prose_regex)
    if not have_node:
        notes.append("node not on PATH: ECMA-262 checks skipped")
    problems += self_checks(doc, ctx)

    schema_checks = compute_schema_checks(ctx)
    schema_checks = dict({"sha256": sha}, **schema_checks)
    fresh = {}
    for fx in doc["fixtures"]:
        actual, comparison = compute(fx, ctx, prose_regex)
        fresh[fx["id"]] = {"actual": actual, "comparison": comparison}
    enums = {en["id"]: compute_enumeration(en, ctx) for en in doc.get("enumerations", [])}

    if args.json:
        for p in problems:
            print("FAIL:", p, file=sys.stderr)
        print(json.dumps({"tools": dict(env, node=nv), "schema_checks": schema_checks,
                          "enumerations": enums, "fixtures": fresh}, indent=2, ensure_ascii=False))
        return 1 if problems else 0

    def strip_node(d):
        """Drop ECMA-262 results from a recorded block when node is absent."""
        if have_node or not isinstance(d, dict):
            return d
        out = {}
        for k, v in d.items():
            if k in ("ecma262_node", "ecma262_no_flags", "ecma262_u_flag", "schema_read_as_ecma262"):
                continue
            if isinstance(v, list):
                v = [strip_node(x) for x in v]
            elif isinstance(v, dict):
                v = strip_node(v)
            out[k] = v
        return out

    if strip_node(doc.get("schema_checks", {})) != strip_node(schema_checks):
        problems.append("schema_checks differ from the recorded ones")
    for en in doc.get("enumerations", []):
        if en.get("actual") != enums[en["id"]]:
            problems.append(f"enumeration {en['id']}: recorded actual does not match this run")
    differs = 0
    for fx in doc["fixtures"]:
        got = fresh[fx["id"]]
        if strip_node(fx.get("actual", {})) != strip_node(got["actual"]):
            problems.append(f"{fx['id']}: recorded actual result does not match this run")
        if strip_node(fx.get("comparison", {})) != strip_node(got["comparison"]):
            problems.append(f"{fx['id']}: recorded comparison does not match this run")
        if any(str(v) == "differs" for v in got["comparison"].values()):
            differs += 1
            if not fx.get("finding"):
                problems.append(f"{fx['id']}: a tool differs from the expected result but no finding is named")
    for n in notes:
        print("note:", n)
    for p in problems:
        print("FAIL:", p)
    print(f"{len(doc['fixtures'])} fixtures; {differs} where a tool differs from the expected result "
          f"(each names a finding); {len(problems)} problems")
    print("tools:", ", ".join(f"{k} {v}" for k, v in env.items()), "| node", nv)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
