#!/usr/bin/env python3
"""Reproduce every recorded result in expected.yaml (NISTIR 7695, CPE Naming 2.3 fixtures).

Library-written (hence the .derived. infix). It holds no text of the
specification except the short pseudocode identifiers and the percent-encoding
table it implements. Python 3.9 or later; PyYAML is the only third-party
package. Run it from the repository root with an isolated interpreter:

    python3 -I records/nist/nistir-7695/distilled/examples/run-fixtures.derived.py
    python3 -I records/nist/nistir-7695/distilled/examples/run-fixtures.derived.py --json
    python3 -I records/nist/nistir-7695/distilled/examples/run-fixtures.derived.py \
        --source-text /path/to/nistir7695.txt

What it contains:

  1. An RFC 5234 ABNF engine: a strict parser that reports every syntax error
     (used to show where the printed figures are not valid ABNF) and a
     compiler from a non-recursive grammar to a regular expression.
  2. A check of RFC 5646 section 2.1 Language-Tag well-formedness.
  3. The grammars: the four repaired figures in ../schema/*.derived.abnf,
     the library's prose readings in the same files, and the two pattern
     facets of ../schema/cpe-naming_2.3.xsd.
  4. A reference implementation of the specification's pseudocode: the WFN
     operations of 5.4, bind_to_URI (6.1.2.3), unbind_URI (6.1.3.2),
     bind_to_fs (6.2.2.2), unbind_fs (6.2.3.2) and the conversions of 7.1 and
     7.2. It follows the printed pseudocode line by line. Where the printed
     code cannot run as written (process_quoted_chars, finding F-20) it
     computes both literal readings and the repaired one, and the repaired
     one is the reference.
  5. The fixture runner: it recomputes the `actual` block of every fixture in
     expected.yaml, compares it with the recorded block, recomputes
     `comparison` (expected against actual), and fails on any difference.

Default mode also runs these self-checks first:

  * every grammar file parses as RFC 5234 (derived files with no error; the
    verbatim figure files with exactly the errors recorded in expected.yaml);
  * the derived grammars equal the printed figures token for token, apart
    from the repairs each one lists;
  * the XML schema has its pinned SHA-256;
  * when the text rendering of the source is available (--source-text,
    default .cache/nistir-7695.txt): the lines of each verbatim figure occur,
    in order, in it (runs of spaces collapsed: the text rendering does not
    keep the figures' columns); every verbatim/ file occurs in it line by line; every
    quoted rule, every violates text, every quote field and every quotation
    inside a finding, note, purpose or label occurs in it verbatim;
  * every printed expected output (expected_file) equals the expected value
    written in expected.yaml;
  * the patterns in ../schema/wfn.derived.schema.json equal the ones compiled
    from the ABNF here, and (with node on PATH) compile as ECMA-262 regular
    expressions with the u flag;
  * (with jsonschema installed) the JSON Schema gives the same verdict as
    wfn_checks on every WFN that occurs in the fixtures.

It also reports, as a note, how often the XML schema patterns agree with the
figures over every CPE name in the fixtures. Checks whose inputs are missing
are skipped and reported. Exit status 0 means every recorded result was
reproduced and every self-check passed.
"""
import argparse
import hashlib
import json
import pathlib
import re
import shutil
import subprocess
import sys
import xml.etree.ElementTree as ET

HERE = pathlib.Path(__file__).resolve().parent
SCHEMA_DIR = HERE.parent / "schema"
ROOT = HERE.parents[4]
DEFAULT_SOURCE_TEXT = ROOT / ".cache" / "nistir-7695.txt"
XSD_SHA256 = "d37f813fe223922fb7456751d453482009fc7075a3f5ad5e1999d075d190dd69"


# =========================================================================
# 1. ABNF engine (RFC 5234)
# =========================================================================

# RFC 5234 Appendix B.1 core rules, used when a grammar does not define them.
CORE_RULES = """
ALPHA  = %x41-5A / %x61-7A
BIT    = "0" / "1"
CHAR   = %x01-7F
CR     = %x0D
CRLF   = CR LF
CTL    = %x00-1F / %x7F
DIGIT  = %x30-39
DQUOTE = %x22
HEXDIG = DIGIT / "A" / "B" / "C" / "D" / "E" / "F"
HTAB   = %x09
LF     = %x0A
LWSP   = *(WSP / CRLF WSP)
OCTET  = %x00-FF
SP     = %x20
VCHAR  = %x21-7E
WSP    = SP / HTAB
"""

TOKEN_RE = re.compile(r"""
    (?P<ws>[ \t]+)
  | (?P<charval>"[^"]*")
  | (?P<prose><[^>]*>)
  | (?P<numval>%[xX][0-9A-Fa-f]+(?:(?:\.[0-9A-Fa-f]+)+|-[0-9A-Fa-f]+)?
             |%[dD][0-9]+(?:(?:\.[0-9]+)+|-[0-9]+)?
             |%[bB][01]+(?:(?:\.[01]+)+|-[01]+)?)
  | (?P<repeat>[0-9]*\*[0-9]*|[0-9]+)
  | (?P<name>[A-Za-z][A-Za-z0-9_-]*)
  | (?P<punct>[/()\[\]])
""", re.X)


class AbnfError(Exception):
    pass


def strip_comment(line):
    """The line without its comment; a ';' inside a char-val or prose-val is text."""
    out, i, n = [], 0, len(line)
    while i < n:
        c = line[i]
        if c == '"':
            j = line.find('"', i + 1)
            j = n - 1 if j < 0 else j
            out.append(line[i:j + 1])
            i = j + 1
        elif c == "<":
            j = line.find(">", i + 1)
            j = n - 1 if j < 0 else j
            out.append(line[i:j + 1])
            i = j + 1
        elif c == ";":
            break
        else:
            out.append(c)
            i += 1
    return "".join(out)


def rule_chunks(text):
    """Group the lines of a rulelist into rules: (first line number, [(line number, text)], problem)."""
    chunks, cur = [], None
    for no, raw in enumerate(text.split("\n"), 1):
        body = strip_comment(raw)
        if not body.strip():
            if not raw.strip() or not raw[:1].isspace():
                cur = None          # an empty line or a column-0 comment ends a rule
            continue
        if raw[:1].isspace():
            if cur is None:
                chunks.append((no, [(no, body)], "continuation line without a rule"))
                continue
            cur[1].append((no, body))
        else:
            cur = (no, [(no, body)], None)
            chunks.append(cur)
    return chunks


def tokenize(s, line, errors):
    toks, i = [], 0
    while i < len(s):
        m = TOKEN_RE.match(s, i)
        if not m:
            ch = s[i]
            errors.append((line, f"unexpected character {ch!r} (U+{ord(ch):04X}) where an element must begin"))
            i += 1
            continue
        kind = m.lastgroup
        val = m.group()
        if kind == "charval":
            bad = [c for c in val[1:-1] if not (0x20 <= ord(c) <= 0x21 or 0x23 <= ord(c) <= 0x7E)]
            if bad:
                errors.append((line, "char-val " + val + " holds " + ", ".join(
                    f"U+{ord(c):04X}" for c in bad) + ", outside %x20-21 / %x23-7E"))
        if kind == "name" and "_" in val:
            errors.append((line, f"rule name {val!r} contains '_' (rulename = ALPHA *(ALPHA / DIGIT / \"-\"))"))
        if kind != "ws":
            toks.append((kind, val))
        i = m.end()
    return toks


class Parser:
    def __init__(self, toks, line, errors):
        self.t, self.i, self.line, self.errors = toks, 0, line, errors

    def peek(self):
        return self.t[self.i] if self.i < len(self.t) else (None, None)

    def take(self):
        tok = self.peek()
        self.i += 1
        return tok

    def alternation(self):
        alts = [self.concatenation()]
        while self.peek() == ("punct", "/"):
            self.take()
            alts.append(self.concatenation())
        return alts[0] if len(alts) == 1 else ("alt", alts)

    def concatenation(self):
        items = []
        while True:
            kind, val = self.peek()
            if kind is None or (kind == "punct" and val in "/)]"):
                break
            items.append(self.repetition())
        if not items:
            raise AbnfError("empty concatenation")
        return items[0] if len(items) == 1 else ("cat", items)

    def repetition(self):
        kind, val = self.peek()
        lo, hi = 1, 1
        if kind == "repeat":
            self.take()
            if "*" in val:
                a, b = val.split("*")
                lo = int(a) if a else 0
                hi = int(b) if b else None
            else:
                lo = hi = int(val)
        node = self.element()
        return node if (lo, hi) == (1, 1) else ("rep", lo, hi, node)

    def element(self):
        kind, val = self.take()
        if kind == "name":
            return ("ref", val.lower())
        if kind == "charval":
            return ("str", val[1:-1])
        if kind == "prose":
            return ("prose", val[1:-1])
        if kind == "numval":
            return numval(val)
        if kind == "punct" and val in "([":
            inner = self.alternation()
            close = self.take()
            want = ")" if val == "(" else "]"
            if close != ("punct", want):
                raise AbnfError(f"missing {want!r}")
            return inner if val == "(" else ("rep", 0, 1, inner)
        raise AbnfError(f"unexpected {val!r}")


def numval(v):
    base = {"x": 16, "d": 10, "b": 2}[v[1].lower()]
    body = v[2:]
    if "-" in body:
        a, b = body.split("-")
        return ("range", int(a, base), int(b, base))
    return ("seq", [int(x, base) for x in body.split(".")])


DEFINED_AS = re.compile(r"^([^\s=/]+)\s*(=/|/=|=)\s*(.*)$", re.S)


def parse_rulelist(text, with_core=True):
    """Parse an ABNF rulelist. Returns (rules, errors, order).

    rules maps a lower-case rule name to its node; errors lists (line, message)
    for every departure from RFC 5234 syntax that was found.
    """
    rules, order, errors = {}, [], []
    for no, lines, problem in rule_chunks(text):
        if problem:
            errors.append((no, problem))
            continue
        m = DEFINED_AS.match(lines[0][1])
        if not m:
            errors.append((no, "no defined-as ('=' or '=/') after the rule name"))
            continue
        name, op, rest = m.groups()
        if not re.fullmatch(r"[A-Za-z][A-Za-z0-9_-]*", name):
            errors.append((no, f"invalid rule name {name!r}"))
            continue
        if "_" in name:
            errors.append((no, f"rule name {name!r} contains '_' (rulename = ALPHA *(ALPHA / DIGIT / \"-\"))"))
        if op == "/=":
            errors.append((no, "'/=' is not a defined-as; RFC 5234 section 3.3 writes incremental alternatives '=/'"))
        errs_before = len(errors)
        toks = tokenize(rest, no, errors)
        for ln_no, body in lines[1:]:
            toks += tokenize(body, ln_no, errors)
        try:
            p = Parser(toks, no, errors)
            node = p.alternation()
            if p.i != len(toks):
                raise AbnfError(f"unexpected {p.peek()[1]!r}")
        except AbnfError as exc:
            errors.append((no, str(exc)))
            continue
        if len(errors) > errs_before:
            continue
        key = name.lower()
        if op in ("=/", "/=") and key in rules:
            old = rules[key]
            olds = old[1] if old[0] == "alt" else [old]
            news = node[1] if node[0] == "alt" else [node]
            rules[key] = ("alt", olds + news)
        elif op in ("=/", "/="):
            errors.append((no, f"incremental alternative for undefined rule {name!r}"))
        elif key in rules:
            errors.append((no, f"rule {name!r} defined twice with '='"))
        else:
            rules[key] = node
            order.append(key)
    if with_core:
        core, _, _ = parse_rulelist(CORE_RULES, with_core=False)
        for k, v in core.items():
            rules.setdefault(k, v)
    unique = []
    for e in errors:
        if e not in unique:
            unique.append(e)
    return rules, sorted(unique, key=lambda e: e[0]), order


REGEX_SPECIAL = set("\\^$.|?*+()[]{}/")


def lit_char(c):
    """A character outside a class, escaped the same way in Python and ECMA-262 (u flag)."""
    return "\\" + c if c in REGEX_SPECIAL else c


def class_char(code):
    c = chr(code)
    if c in "\\]^-[":
        return "\\" + c
    if 0x21 <= code <= 0x7E:
        return c
    return f"\\x{code:02X}" if code < 0x100 else f"\\u{code:04X}"


def compile_node(node, rules, cs, hooks, stack):
    kind = node[0]
    if kind == "alt":
        return "(?:" + "|".join(compile_node(n, rules, cs, hooks, stack) for n in node[1]) + ")"
    if kind == "cat":
        return "".join(compile_node(n, rules, cs, hooks, stack) for n in node[1])
    if kind == "rep":
        _, lo, hi, inner = node
        body = "(?:" + compile_node(inner, rules, cs, hooks, stack) + ")"
        if (lo, hi) == (0, None):
            return body + "*"
        if (lo, hi) == (1, None):
            return body + "+"
        if (lo, hi) == (0, 1):
            return body + "?"
        if hi is None:
            return body + "{%d,}" % lo
        return body + ("{%d}" % lo if lo == hi else "{%d,%d}" % (lo, hi))
    if kind == "ref":
        name = node[1]
        if name in stack:
            raise AbnfError(f"recursive rule {name!r}: not a regular grammar")
        if name not in rules:
            raise AbnfError(f"undefined rule {name!r}")
        return "(?:" + compile_node(rules[name], rules, cs, hooks, stack | {name}) + ")"
    if kind == "str":
        out = []
        for c in node[1]:
            if c.isalpha() and c.isascii() and not cs:
                out.append("[" + c.upper() + c.lower() + "]")
            else:
                out.append(lit_char(c))
        return "".join(out)
    if kind == "range":
        return "[" + class_char(node[1]) + "-" + class_char(node[2]) + "]"
    if kind == "seq":
        return "".join(lit_char(chr(x)) if 0x20 <= x <= 0x7E else class_char(x).join("[]") for x in node[1])
    if kind == "prose":
        if hooks and node[1] in hooks:
            return "(?:" + hooks[node[1]] + ")"
        raise AbnfError(f"prose value <{node[1]}> has no implementation")
    raise AbnfError(f"unknown node {kind}")


class Grammar:
    def __init__(self, path, hooks=None):
        self.path = pathlib.Path(path)
        self.text = self.path.read_text(encoding="utf-8")
        self.rules, self.errors, self.order = parse_rulelist(self.text)
        self.hooks = hooks or {}
        self._cache = {}

    def regex(self, rule, case_sensitive=False):
        key = (rule.lower(), case_sensitive)
        if key not in self._cache:
            body = compile_node(("ref", rule.lower()), self.rules, case_sensitive, self.hooks, frozenset())
            self._cache[key] = (body, re.compile(body, re.S))
        return self._cache[key]

    def match(self, rule, s, case_sensitive=False):
        return "valid" if self.regex(rule, case_sensitive)[1].fullmatch(s) else "invalid"


# =========================================================================
# 2. RFC 5646 Language-Tag (section 2.1), well-formedness only
# =========================================================================

IRREGULAR = ["en-GB-oed", "i-ami", "i-bnn", "i-default", "i-enochian", "i-hak", "i-klingon",
             "i-lux", "i-mingo", "i-navajo", "i-pwn", "i-tao", "i-tay", "i-tsu", "sgn-BE-FR",
             "sgn-BE-NL", "sgn-CH-DE"]
REGULAR = ["art-lojban", "cel-gaulish", "no-bok", "no-nyn", "zh-guoyu", "zh-hakka", "zh-min",
           "zh-min-nan", "zh-xiang"]


def language_tag_regex(sep):
    """RFC 5646 Language-Tag as a portable regex; sep is the regex for the separator."""
    a, d, an = "[A-Za-z]", "[0-9]", "[A-Za-z0-9]"
    language = f"(?:{a}{{2,3}}(?:{sep}{a}{{3}}){{0,3}}|{a}{{4}}|{a}{{5,8}})"
    script = f"{a}{{4}}"
    region = f"(?:{a}{{2}}|{d}{{3}})"
    variant = f"(?:{an}{{5,8}}|{d}{an}{{3}})"
    singleton = "[0-9A-WY-Za-wy-z]"
    extension = f"{singleton}(?:{sep}{an}{{2,8}})+"
    privateuse = f"[xX](?:{sep}{an}{{1,8}})+"
    langtag = (f"{language}(?:{sep}{script})?(?:{sep}{region})?(?:{sep}{variant})*"
               f"(?:{sep}{extension})*(?:{sep}{privateuse})?")

    def ci(word):
        return "".join(("[" + c.upper() + c.lower() + "]") if c.isalpha() else sep for c in word)
    grandfathered = "|".join(ci(w) for w in IRREGULAR + REGULAR)
    return f"(?:{langtag}|{privateuse}|{grandfathered})"


LANGTAG_PLAIN = language_tag_regex("-")
LANGTAG_QUOTED = language_tag_regex(r"\\-")
HOOKS = {
    "Language-Tag, RFC 5646 section 2.1": LANGTAG_PLAIN,
    'RFC 5646 Language-Tag, each "-" written as "\\-"': LANGTAG_QUOTED,
}


# =========================================================================
# 3. The grammars and the XML schema patterns
# =========================================================================

GRAMMAR_FILES = {
    "figure_5_1": "figure-5-1-avstring.derived.abnf",
    "figure_6_1": "figure-6-1-uri-v2.2-compatible.derived.abnf",
    "figure_6_2": "figure-6-2-uri-preferred.derived.abnf",
    "figure_6_3": "figure-6-3-formatted-string.derived.abnf",
}
VERBATIM_FILES = {
    "figure_5_1": "figure-5-1-avstring.abnf",
    "figure_6_1": "figure-6-1-uri-v2.2-compatible.abnf",
    "figure_6_2": "figure-6-2-uri-preferred.abnf",
    "figure_6_3": "figure-6-3-formatted-string.abnf",
}
G = {}
XSD = {}


def load_grammars():
    for k, f in GRAMMAR_FILES.items():
        G[k] = Grammar(SCHEMA_DIR / f, HOOKS)
    raw = (SCHEMA_DIR / "cpe-naming_2.3.xsd").read_bytes()
    XSD["sha256"] = hashlib.sha256(raw).hexdigest()
    ns = {"xsd": "http://www.w3.org/2001/XMLSchema"}
    root = ET.fromstring(raw)
    for st in root.findall("xsd:simpleType", ns):
        pat = st.find("xsd:restriction/xsd:pattern", ns)
        XSD[st.get("name")] = re.compile(pat.get("value"))


def xsd_match(type_name, s):
    return "valid" if XSD[type_name].fullmatch(s) else "invalid"


def uri_grammar(u):
    return {
        "figure_6_1": G["figure_6_1"].match("cpe-name", u),
        "figure_6_1_case_sensitive": G["figure_6_1"].match("cpe-name", u, True),
        "figure_6_2": G["figure_6_2"].match("cpe-name", u),
        "figure_6_2_case_sensitive": G["figure_6_2"].match("cpe-name", u, True),
        "xsd_cpe22Type": xsd_match("cpe22Type", u),
    }


def fs_grammar(fs):
    return {
        "figure_6_3": G["figure_6_3"].match("formstring", fs),
        "figure_6_3_case_sensitive": G["figure_6_3"].match("formstring", fs, True),
        "xsd_cpe23Type": xsd_match("cpe23Type", fs),
    }


# =========================================================================
# 4. WFN model and the operations of 5.4
# =========================================================================

class Logical:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


ANY = Logical("ANY")
NA = Logical("NA")
ATTRS = ["part", "vendor", "product", "version", "update", "edition", "language",
         "sw_edition", "target_sw", "target_hw", "other"]


class PseudocodeError(Exception):
    """The pseudocode's own `error` statement was reached."""


class Undefined(Exception):
    """The pseudocode reaches a state it does not define."""


def new():
    """5.4.1: an empty WFN."""
    return {}


def get(w, a):
    """5.4.2: the value of a, or ANY when a is unspecified."""
    return w.get(a.lower(), ANY)


def set_(w, a, v):
    """5.4.3: add or replace a=v; nil (None) deletes a. Pass by value (1.3)."""
    w = dict(w)
    if v is None:
        w.pop(a.lower(), None)
    else:
        w[a.lower()] = v
    return w


# ---- string helpers the pseudocode cites (6.1.2.3, 6.1.3.2) ----

def substr(s, b, e):
    """Characters b to e of s (0-based, inclusive); nil when b >= strlen(s).

    Readings: an end past the last character stops at the last character, and
    a call with b > e or a negative b is undefined ("b must be <= e").
    """
    if s is None:
        raise Undefined("substr called on nil")
    if b >= len(s):
        return None
    if b < 0 or b > e:
        raise Undefined(f"substr({s!r},{b},{e}) breaks 'b must be <= e'")
    return s[b:e + 1]


def strchr(s, ch, off):
    i = s.find(ch, off)
    return None if i < 0 else i


def is_alphanum(c):
    return c is not None and len(c) == 1 and (c.isascii() and (c.isalnum() or c == "_"))


def strcat(*parts):
    if any(p is None for p in parts):
        raise Undefined("strcat with a nil argument")
    return "".join(parts)


# =========================================================================
# 5. The WFN illustration notation (5.1) and value checks (5.2, 5.3)
# =========================================================================

def parse_wfn(text, allow_ellipsis=False):
    """Parse 'wfn:[a=v,...]' into a list of (attribute as written, value).

    Strings keep their backslash quoting; logical values become ANY / NA.
    With allow_ellipsis, a pair written as the ellipsis character is skipped.
    Raises ValueError when the text is not in the notation.
    """
    if not text.startswith("wfn:[") or not text.endswith("]"):
        raise ValueError("not of the form wfn:[...]")
    s, i, pairs = text[5:-1], 0, []
    while i < len(s):
        if allow_ellipsis and s[i] == "\u2026":
            i += 1
        else:
            m = re.match(r"([A-Za-z_][A-Za-z0-9_]*)=", s[i:])
            if not m:
                raise ValueError(f"no attribute name at offset {i}")
            name = m.group(1)
            i += m.end()
            if s.startswith('"', i):
                j, buf = i + 1, []
                while j < len(s) and s[j] != '"':
                    if s[j] == "\\" and j + 1 < len(s):
                        buf.append(s[j:j + 2])
                        j += 2
                    else:
                        buf.append(s[j])
                        j += 1
                if j >= len(s):
                    raise ValueError("unterminated string value")
                pairs.append((name, "".join(buf)))
                i = j + 1
            else:
                m = re.match(r"(ANY|NA)(?=,|$)", s[i:])
                if not m:
                    raise ValueError(f"value of {name} is neither a quoted string nor ANY or NA")
                pairs.append((name, ANY if m.group(1) == "ANY" else NA))
                i += m.end()
        if i < len(s):
            if s[i] != ",":
                raise ValueError(f"expected ',' at offset {i}")
            i += 1
            while i < len(s) and s[i] == " ":
                i += 1
    return pairs


def fmt_value(v):
    return v.name if isinstance(v, Logical) else '"' + v + '"'


def fmt_wfn(w):
    return "wfn:[" + ",".join(f"{a}={fmt_value(v)}" for a, v in w.items()) + "]"


def pairs_to_wfn(pairs):
    w = {}
    for a, v in pairs:
        w[a.lower()] = v
    return w


def avstring_checks(v):
    f = G["figure_5_1"].match("avstring", v)
    p = G["figure_5_1"].match("avstring-prose", v)
    s = G["figure_5_1"].match("avstring-strict", v)
    verdict = "valid" if f == p == "valid" else "invalid" if f == p == "invalid" else "disputed"
    return {"figure_5_1": f, "prose_5_3_2": p, "strict": s, "verdict": verdict}


def wfn_checks(pairs):
    """Check a WFN's pairs against 5.2, 5.3.2 (figure and prose), 5.3.3.1 and 5.3.3.10."""
    failures, seen, disputed = [], set(), False
    for a, v in pairs:
        al = a.lower()
        if al not in ATTRS:
            failures.append({"attribute": a, "check": "permitted_5_2"})
            continue
        if al in seen:
            failures.append({"attribute": a, "check": "at_most_once_5_2"})
        seen.add(al)
        if isinstance(v, Logical):
            continue
        c = avstring_checks(v)
        if c["verdict"] == "invalid":
            failures.append({"attribute": al, "check": "value_5_3_2", "value": v})
        elif c["verdict"] == "disputed":
            disputed = True
            failures.append({"attribute": al, "check": "value_5_3_2_disputed", "value": v,
                             "figure_5_1": c["figure_5_1"], "prose_5_3_2": c["prose_5_3_2"]})
        if al == "part" and G["figure_5_1"].match("part-string", v, True) != "valid":
            failures.append({"attribute": al, "check": "part_5_3_3_1", "value": v})
        if al == "language" and G["figure_5_1"].match("language-string", v, True) != "valid":
            failures.append({"attribute": al, "check": "language_5_3_3_10", "value": v})
    hard = [f for f in failures if f["check"] != "value_5_3_2_disputed"]
    out = {"verdict": "invalid" if hard else "disputed" if disputed else "valid"}
    if failures:
        out["failures"] = failures
    return out


# =========================================================================
# 6. The pseudocode
# =========================================================================

# ---- 6.1.2.3 bind_to_URI and its helpers ----

PCT_ENCODE = {
    "!": "%21", '"': "%22", "#": "%23", "$": "%24", "%": "%25", "&": "%26", "'": "%27",
    "(": "%28", ")": "%29", "*": "%2a", "+": "%2b", ",": "%2c", "-": "-", ".": ".",
    "/": "%2f", ":": "%3a", ";": "%3b", "<": "%3c", "=": "%3d", ">": "%3e", "?": "%3f",
    "@": "%40", "[": "%5b", "\\": "%5c", "]": "%5d", "^": "%5e", "`": "%60", "{": "%7b",
    "|": "%7c", "}": "%7d", "~": "%7e",
}


def pct_encode(c):
    if c is None:
        raise Undefined("pct_encode(nil): a backslash ends the value")
    if c not in PCT_ENCODE:
        raise Undefined(f"pct_encode has no case for {c!r}")
    return PCT_ENCODE[c]


def transform_for_uri(s):
    result, idx = "", 0
    while idx < len(s):
        thischar = substr(s, idx, idx)
        if is_alphanum(thischar):
            result = strcat(result, thischar)
            idx += 1
            continue
        if thischar == "\\":
            idx += 1
            nxtchar = substr(s, idx, idx)
            result = strcat(result, pct_encode(nxtchar))
            idx += 1
            continue
        if thischar == "?":
            result = strcat(result, "%01")
        if thischar == "*":
            result = strcat(result, "%02")
        idx += 1
    return result


def bind_value_for_uri(s):
    if s is ANY:
        return ""
    if s is NA:
        return "-"
    return transform_for_uri(s)


def pack(ed, sw_ed, t_sw, t_hw, oth):
    if sw_ed == "" and t_sw == "" and t_hw == "" and oth == "":
        return ed
    return strcat("~", ed, "~", sw_ed, "~", t_sw, "~", t_hw, "~", oth)


def trim(s):
    s1 = s[::-1]
    idx = 0
    for i in range(0, len(s1) + 1):
        if substr(s1, i, i) == ":":
            idx += 1
        else:
            break
    rest = substr(s1, idx, len(s1) - 1)
    if rest is None:
        raise Undefined("trim: the string is all colons")
    return rest[::-1]


def bind_to_uri(w):
    uri = "cpe:/"
    for a in ["part", "vendor", "product", "version", "update", "edition", "language"]:
        if a == "edition":
            ed = bind_value_for_uri(get(w, "edition"))
            sw_ed = bind_value_for_uri(get(w, "sw_edition"))
            t_sw = bind_value_for_uri(get(w, "target_sw"))
            t_hw = bind_value_for_uri(get(w, "target_hw"))
            oth = bind_value_for_uri(get(w, "other"))
            v = pack(ed, sw_ed, t_sw, t_hw, oth)
        else:
            v = bind_value_for_uri(get(w, a))
        uri = strcat(uri, v, ":")
    return trim(uri)


# ---- 6.1.3.2 unbind_URI and its helpers ----

def get_comp_uri(uri, i):
    """The i'th component (1-based) after 'cpe:/', or '' when there are fewer.

    Reading: the comment's example returns "" for a missing component; the
    prefix is matched without regard to case (RFC 3986 schemes, and an RFC 2234
    quoted string, are case-insensitive).
    """
    if uri[:5].lower() != "cpe:/":
        raise Undefined("get_comp_uri: the URI does not begin with cpe:/")
    if i == 0:
        return uri[:4]
    comps = uri[5:].split(":")
    return comps[i - 1] if i <= len(comps) else ""


def decode(s):
    if s == "":
        return ANY
    if s == "-":
        return NA
    s = s.lower()
    result, idx, embedded = "", 0, False
    while idx < len(s):
        c = substr(s, idx, idx)
        if c in (".", "-", "~"):
            result = strcat(result, "\\", c)
            idx += 1
            embedded = True
            continue
        if c != "%":
            result = strcat(result, c)
            idx += 1
            embedded = True
            continue
        form = substr(s, idx, idx + 2)
        if form == "%01":
            if ((idx == 0 or idx == len(s) - 3)
                    or (not embedded and substr(s, idx - 3, idx - 1) == "%01")
                    or (embedded and len(s) >= idx + 6 and substr(s, idx + 3, idx + 5) == "%01")):
                result = strcat(result, "?")
                idx += 3
                continue
            raise PseudocodeError(f"decode: %01 at offset {idx} is neither at an end nor in a leading or trailing run")
        elif form == "%02":
            if idx == 0 or idx == len(s) - 3:
                result = strcat(result, "*")
            else:
                raise PseudocodeError(f"decode: %02 at offset {idx} is not at the beginning or the end")
        elif form in DECODE:
            result = strcat(result, DECODE[form])
        else:
            raise PseudocodeError(f"decode: illegal percent-encoded form {form!r}")
        idx += 3
        embedded = True
    return result


DECODE = {
    "%21": "\\!", "%22": '\\"', "%23": "\\#", "%24": "\\$", "%25": "\\%", "%26": "\\&",
    "%27": "\\'", "%28": "\\(", "%29": "\\)", "%2a": "\\*", "%2b": "\\+", "%2c": "\\,",
    "%2f": "\\/", "%3a": "\\:", "%3b": "\\;", "%3c": "\\<", "%3d": "\\=", "%3e": "\\>",
    "%3f": "\\?", "%40": "\\@", "%5b": "\\[", "%5c": "\\\\", "%5d": "\\]", "%5e": "\\^",
    "%60": "\\`", "%7b": "\\{", "%7c": "\\|", "%7d": "\\}", "%7e": "\\~",
}


def unpack(s, wfn):
    def field(start):
        end = strchr(s, "~", start)
        if end is None:
            raise Undefined("unpack: strchr finds no further '~' (end := nil)")
        return ("" if start == end else substr(s, start, end - 1)), end
    start = 1
    ed, end = field(start)
    sw_ed, end = field(end + 1)
    t_sw, end = field(end + 1)
    t_hw, end = field(end + 1)
    start = end + 1
    oth = "" if start >= len(s) else substr(s, start, len(s) - 1)
    wfn = set_(wfn, "edition", decode(ed))
    wfn = set_(wfn, "sw_edition", decode(sw_ed))
    wfn = set_(wfn, "target_sw", decode(t_sw))
    wfn = set_(wfn, "target_hw", decode(t_hw))
    wfn = set_(wfn, "other", decode(oth))
    return wfn


def unbind_uri(uri):
    result = new()
    for i in range(1, 8):
        v = get_comp_uri(uri, i)
        if i == 1:
            result = set_(result, "part", decode(v))
        elif i == 2:
            result = set_(result, "vendor", decode(v))
        elif i == 3:
            result = set_(result, "product", decode(v))
        elif i == 4:
            result = set_(result, "version", decode(v))
        elif i == 5:
            result = set_(result, "update", decode(v))
        elif i == 6:
            if v == "" or v == "-" or substr(v, 0, 0) != "~":
                result = set_(result, "edition", decode(v))
            else:
                result = unpack(v, result)
        else:
            result = set_(result, "language", decode(v))
    return result


# ---- 6.2.2.2 bind_to_fs and its helpers ----

def process_quoted_chars(s, reading="repaired"):
    """6.2.2.2. The printed branch for '.', '-' and '_' ends with "idx = idx + 2."
    and no continue, so the loop then also runs "idx := idx + 1" (finding F-20).

    reading = 'assignment': "idx = idx + 2." assigns; the next character is skipped.
              'comparison': "idx = idx + 2." is a comparison with no effect; the
                            quoted character is visited again and copied.
              'repaired':   the branch ends like the else branch: idx := idx + 2,
                            continue (the result every printed example shows).
    """
    result, idx = "", 0
    while idx < len(s):
        c = substr(s, idx, idx)
        if c != "\\":
            result = strcat(result, c)
        else:
            nextchr = substr(s, idx + 1, idx + 1)
            if nextchr in (".", "-", "_"):
                result = strcat(result, nextchr)
                if reading == "assignment":
                    idx = idx + 2
                elif reading == "repaired":
                    idx = idx + 2
                    continue
            else:
                result = strcat(result, "\\", nextchr)
                idx += 2
                continue
        idx += 1
    return result


def bind_value_for_fs(v, reading="repaired"):
    if v is ANY:
        return "*"
    if v is NA:
        return "-"
    return process_quoted_chars(v, reading)


def bind_to_fs(w, reading="repaired"):
    fs = "cpe:2.3:"
    for a in ATTRS:
        v = bind_value_for_fs(get(w, a), reading)
        fs = strcat(fs, v)
        if a != "other":
            fs = strcat(fs, ":")
    return fs


# ---- 6.2.3.2 unbind_fs and its helpers ----

def split_fs(fs, reading="escape-pairs"):
    """Fields of a formatted string (0 = "cpe", 1 = "2.3", 2 = part, ...).

    'escape-pairs': a backslash quotes the next character, so in "\\\\:" the
                    colon is a delimiter (agrees with Figure 6-3).
    'preceded':     a colon right after a backslash is never a delimiter (the
                    comment's words read literally).
    """
    fields, cur, i = [], "", 0
    while i < len(fs):
        c = fs[i]
        if reading == "escape-pairs" and c == "\\" and i + 1 < len(fs):
            cur += fs[i:i + 2]
            i += 2
            continue
        if c == ":" and not (reading == "preceded" and i > 0 and fs[i - 1] == "\\"):
            fields.append(cur)
            cur = ""
        else:
            cur += c
        i += 1
    fields.append(cur)
    return fields


def get_comp_fs(fs, i, reading="escape-pairs"):
    fields = split_fs(fs, reading)
    return fields[i] if i < len(fields) else None


def add_quoting(s):
    if s is None:
        raise Undefined("add_quoting(nil): the formatted string has fewer than eleven fields")
    result, idx, embedded = "", 0, False
    while idx < len(s):
        c = substr(s, idx, idx)
        if is_alphanum(c) or c == "_":
            result = strcat(result, c)
            idx += 1
            embedded = True
            continue
        if c == "\\":
            result = strcat(result, substr(s, idx, idx + 1))
            idx += 2
            embedded = True
            continue
        if c == "*":
            if idx == 0 or idx == len(s) - 1:
                result = strcat(result, c)
                idx += 1
                embedded = True
                continue
            raise PseudocodeError(f"add_quoting: '*' at offset {idx} is not at the beginning or the end")
        if c == "?":
            if ((idx == 0 or idx == len(s) - 1)
                    or (not embedded and substr(s, idx - 1, idx - 1) == "?")
                    or (embedded and substr(s, idx + 1, idx + 1) == "?")):
                result = strcat(result, c)
                idx += 1
                embedded = False
                continue
            raise PseudocodeError(f"add_quoting: '?' at offset {idx} is neither at an end nor in a run")
        result = strcat(result, "\\", c)
        idx += 1
        embedded = True
    return result


def unbind_value_fs(s):
    if s == "*":
        return ANY
    if s == "-":
        return NA
    return add_quoting(s)


def unbind_fs(fs, reading="escape-pairs"):
    result = new()
    for a in range(2, 13):
        v = get_comp_fs(fs, a, reading)
        v = unbind_value_fs(v)
        result = set_(result, ATTRS[a - 2], v)
    return result


# ---- 7.1 and 7.2 ----

def convert_uri_to_fs(u, reading="repaired"):
    return bind_to_fs(unbind_uri(u), reading)


def convert_fs_to_uri(fs):
    return bind_to_uri(unbind_fs(fs))


# =========================================================================
# 7. Fixture computations
# =========================================================================

def outcome(fn, *args, **kw):
    """Run a pseudocode function; return ('ok', value) or ('error'|'undefined', reason)."""
    try:
        return "ok", fn(*args, **kw)
    except PseudocodeError as exc:
        return "error", str(exc)
    except Undefined as exc:
        return "undefined", str(exc)


def value_result(v):
    if isinstance(v, Logical):
        return {"outcome": "logical", "value": v.name}
    return {"outcome": "value", "value": v}


def read_fixture(rel):
    raw = (HERE / rel).read_bytes()
    if not raw.endswith(b"\n") or raw.endswith(b"\n\n") or b"\r" in raw:
        raise ValueError(f"{rel}: must end with exactly one LF and contain no CR")
    return raw[:-1].decode("utf-8")


def joined(text):
    """A printed example that wraps across lines, as one string (no separator)."""
    return "".join(ln.strip() for ln in text.split("\n"))


def fixture_input(fx, key="input"):
    """The input string of a fixture, read from its file when it has one.

    A derived file holds one line taken as written; a verbatim file holds the
    printed lines, joined with nothing between them.
    """
    rel = fx.get(key + "_file")
    if rel is None:
        return fx[key]
    text = read_fixture(rel)
    if fx.get("source") == "derived":
        return text
    if fx.get(key + "_token") == "quoted":
        text = text.strip()
        assert text.startswith('"') and text.endswith('"'), rel
        return text[1:-1]
    return joined(text)


def unbind_uri_result(u):
    st, val = outcome(unbind_uri, u)
    if st != "ok":
        return {"outcome": st, "reason": val}
    pairs = list(val.items())
    return {"outcome": "wfn", "wfn": fmt_wfn(val), "wfn_checks": wfn_checks(pairs)}


def unbind_fs_result(fs):
    st, val = outcome(unbind_fs, fs)
    if st != "ok":
        return {"outcome": st, "reason": val}
    out = {"outcome": "wfn", "wfn": fmt_wfn(val), "wfn_checks": wfn_checks(list(val.items()))}
    naive = outcome(unbind_fs, fs, "preceded")
    if naive[0] != "ok" or fmt_wfn(naive[1]) != out["wfn"]:
        out["get_comp_fs_preceded_reading"] = (fmt_wfn(naive[1]) if naive[0] == "ok"
                                               else naive[0] + ": " + naive[1])
    return out


def bind_uri_result(w):
    st, val = outcome(bind_to_uri, w)
    if st != "ok":
        return {"outcome": st, "reason": val}
    return {"outcome": "uri", "uri": val, "grammar": uri_grammar(val)}


def bind_fs_result(w):
    st, val = outcome(bind_to_fs, w)
    if st != "ok":
        return {"outcome": st, "reason": val}
    out = {"outcome": "fs", "fs": val}
    for reading in ("assignment", "comparison"):
        s2, v2 = outcome(bind_to_fs, w, reading)
        printed = v2 if s2 == "ok" else s2 + ": " + v2
        if printed != val:
            out["as_printed_" + reading] = printed
    out["grammar"] = fs_grammar(val)
    return out


def wfn_from_fixture(fx, key="input"):
    text = fixture_input(fx, key)
    pairs = parse_wfn(text)
    return text, pairs


def compute(fx):
    """Recompute the `actual` block of one fixture."""
    kind = fx["kind"]
    if kind in ("wfn", "wfn-fragment"):
        text = fixture_input(fx)
        out = {"notation": G["figure_5_1"].match("wfn-notation", text)}
        try:
            pairs = parse_wfn(text, allow_ellipsis=(kind == "wfn-fragment"))
        except ValueError as exc:
            out["parse"] = "fails: " + str(exc)
            return out
        out["pairs"] = fmt_wfn(pairs_to_wfn(pairs)) if len({a.lower() for a, _ in pairs}) == len(pairs) \
            else "duplicate attribute: " + ",".join(f"{a}={fmt_value(v)}" for a, v in pairs)
        out["wfn_checks"] = wfn_checks(pairs)
        return out
    if kind == "avstring":
        v = fixture_input(fx)
        out = {"avstring": avstring_checks(v)}
        st, b = outcome(transform_for_uri, v)
        if st == "ok":
            out["uri_component"] = b
            s2, d = outcome(decode, b)
            out["uri_decode"] = value_result(d) if s2 == "ok" else {"outcome": s2, "reason": d}
        else:
            out["uri_component"] = st + ": " + b
        st, b = outcome(process_quoted_chars, v)
        if st == "ok":
            out["fs_field"] = b
            s2, d = outcome(unbind_value_fs, b)
            out["fs_unbind"] = value_result(d) if s2 == "ok" else {"outcome": s2, "reason": d}
        else:
            out["fs_field"] = st + ": " + b
        return out
    if kind == "illustration":
        text = fixture_input(fx)
        return {"notation": G["figure_5_1"].match("wfn-notation", text)}
    if kind == "wfn-op":
        return compute_op(fx)
    if kind == "bind-uri":
        text, pairs = wfn_from_fixture(fx)
        return {"input_checks": wfn_checks(pairs), "bind_to_URI": bind_uri_result(pairs_to_wfn(pairs))}
    if kind == "bind-fs":
        text, pairs = wfn_from_fixture(fx)
        return {"input_checks": wfn_checks(pairs), "bind_to_fs": bind_fs_result(pairs_to_wfn(pairs))}
    if kind == "bind":
        text, pairs = wfn_from_fixture(fx)
        w = pairs_to_wfn(pairs)
        return {"input_checks": wfn_checks(pairs), "bind_to_URI": bind_uri_result(w),
                "bind_to_fs": bind_fs_result(w)}
    if kind == "bind-substring":
        st, val = outcome(transform_for_uri, fx["input"])
        return {"transform_for_uri": val if st == "ok" else st + ": " + val}
    if kind == "unbind-uri":
        u = fixture_input(fx)
        return {"grammar": uri_grammar(u), "unbind_URI": unbind_uri_result(u)}
    if kind == "unbind-fs":
        fs = fixture_input(fx)
        return {"grammar": fs_grammar(fs), "unbind_fs": unbind_fs_result(fs)}
    if kind == "get-comp-uri":
        u = fixture_input(fx)
        return {"components": [get_comp_uri(u, i) for i in range(0, 7)]}
    if kind == "get-comp-fs":
        fs = fixture_input(fx)
        return {"components": [get_comp_fs(fs, i) for i in range(0, 6)]}
    if kind == "convert-uri-to-fs":
        u = fixture_input(fx)
        st, val = outcome(convert_uri_to_fs, u)
        out = {"convert_uri_to_fs": val if st == "ok" else st + ": " + val}
        if st == "ok":
            out["grammar"] = fs_grammar(val)
            for reading in ("assignment", "comparison"):
                s2, v2 = outcome(convert_uri_to_fs, u, reading)
                printed = v2 if s2 == "ok" else s2 + ": " + v2
                if printed != val:
                    out["as_printed_" + reading] = printed
        return out
    if kind == "convert-fs-to-uri":
        fs = fixture_input(fx)
        st, val = outcome(convert_fs_to_uri, fs)
        out = {"convert_fs_to_uri": val if st == "ok" else st + ": " + val}
        if st == "ok":
            out["grammar"] = uri_grammar(val)
        return out
    if kind == "round-trip-uri":
        u = fixture_input(fx)
        st, fs = outcome(convert_uri_to_fs, u)
        if st != "ok":
            return {"to_fs": st + ": " + fs}
        st, back = outcome(convert_fs_to_uri, fs)
        out = {"to_fs": fs, "back": back if st == "ok" else st + ": " + back}
        out["round_trip"] = "same" if back == u else "different"
        return out
    if kind == "round-trip-fs":
        fs = fixture_input(fx)
        st, u = outcome(convert_fs_to_uri, fs)
        if st != "ok":
            return {"to_uri": st + ": " + u}
        st, back = outcome(convert_uri_to_fs, u)
        out = {"to_uri": u, "back": back if st == "ok" else st + ": " + back}
        out["round_trip"] = "same" if back == fs else "different"
        return out
    raise ValueError(f"{fx['id']}: unknown kind {kind!r}")


OP_RE = {
    "new": re.compile(r"^new\(\) \u2192 (?P<out>wfn:\[.*\])$"),
    "get": re.compile(r"^get\((?P<w>wfn:\[.*\]),(?P<a>[a-z_]+)\) \u2192 (?P<out>.*)$"),
    "set": re.compile(r"^set\((?P<w>wfn:\[.*\]),(?P<a>[a-z_]+),(?P<v>\"[^\"]*\"|ANY|NA|nil)\) \u2192 (?P<out>wfn:\[.*\])$"),
}


def compute_op(fx):
    text = " ".join(ln.strip() for ln in read_fixture(fx["input_raw_file"]).split("\n"))
    op = fx["op"]
    m = OP_RE[op].match(text)
    if not m:
        return {"parse": "fails"}
    if op == "new":
        got = fmt_wfn(new())
        printed = fmt_wfn(pairs_to_wfn(parse_wfn(m.group("out"))))
    elif op == "get":
        val = get(pairs_to_wfn(parse_wfn(m.group("w"))), m.group("a"))
        got = fmt_value(val)
        printed = m.group("out")
    else:
        raw = m.group("v")
        v = None if raw == "nil" else ANY if raw == "ANY" else NA if raw == "NA" else raw[1:-1]
        got = fmt_wfn(set_(pairs_to_wfn(parse_wfn(m.group("w"))), m.group("a"), v))
        printed = fmt_wfn(pairs_to_wfn(parse_wfn(m.group("out"))))
    return {"result": got, "printed_result": printed,
            "matches_printed": "yes" if got == printed else "no"}


def subset_equal(exp, act):
    """True when every key of exp is in act with an equal value (recursively); lists compare whole."""
    if isinstance(exp, dict):
        return isinstance(act, dict) and all(k in act and subset_equal(v, act[k]) for k, v in exp.items())
    return exp == act


def compare(expected, actual):
    """Per expected key: 'agrees' when actual holds the same value (extra actual keys are ignored)."""
    out = {}
    for k, v in expected.items():
        if k.endswith("_note") or k in ("violates", "verdict_note"):
            continue
        out[k] = "agrees" if k in actual and subset_equal(v, actual[k]) else "differs"
    # The printed pseudocode, read literally, against the reference (finding F-20, F-25).
    inner = [actual] + [v for v in actual.values() if isinstance(v, dict)]
    if any(k.startswith("as_printed_") for d in inner for k in d):
        out["pseudocode_as_printed"] = "differs"
    if any("get_comp_fs_preceded_reading" in d for d in inner):
        out["get_comp_fs_literal_reading"] = "differs"
    return out


# =========================================================================
# 8. Self-checks
# =========================================================================

def normalise_source(text):
    """Text rendering, page furniture removed, line-end hyphens joined, whitespace collapsed."""
    keep = [ln for ln in text.splitlines()
            if not re.fullmatch(r"\s*(?:[ivx]+|\d+)\s*", ln)
            and "COMMON PLATFORM ENUMERATION: NAMING SPECIFICATION VERSION 2.3" not in ln]
    joined_text = "\n".join(keep).replace("\f", "")
    joined_text = re.sub(r"-\n\s*", "-", joined_text)
    return re.sub(r"\s+", " ", joined_text)


def collapse(s):
    return re.sub(r"\s+", " ", s).strip()


PUA = {"\u2192": "\uf0ae"}  # the arrow of the 5.4 examples is a Symbol-font glyph (U+F0AE) in the text layer


def lines_occur(needle, hay_lines):
    """True when the needle's lines occur, in order, within consecutive source lines."""
    n = ["".join(PUA.get(c, c) for c in ln.strip()) for ln in needle.split("\n") if ln.strip()]
    h = [ln.strip() for ln in hay_lines]
    return any(all(n[k] in h[i + k] for k in range(len(n))) for i in range(len(h) - len(n) + 1))


def figure_tokens(text):
    """The token stream of a grammar text: comments, layout and the library header ignored."""
    toks = []
    for raw in text.split("\n"):
        line = strip_comment(raw)
        toks += re.findall(r'"[^"]*"|<[^>]*>|%[xXdDbB][0-9A-Fa-f.\-]+|[0-9]*\*[0-9]*|=/|/=|[A-Za-z0-9_\-.\[\]]+|[^\s]', line)
    return toks


def grammar_repairs_ok(doc):
    """Each derived figure equals its verbatim figure token for token, after the listed repairs."""
    problems = []
    for key, rec in (doc.get("grammar_files") or {}).items():
        v = (SCHEMA_DIR / VERBATIM_FILES[key]).read_text(encoding="utf-8")
        d = (SCHEMA_DIR / GRAMMAR_FILES[key]).read_text(encoding="utf-8")
        vt = " ".join(figure_tokens(v))
        for rep in rec.get("repairs", []):
            vt = vt.replace(rep["from"], rep["to"])
        dt = " ".join(figure_tokens(d.split(rec["derived_figure_ends_before"])[0]
                                    if rec.get("derived_figure_ends_before") else d))
        if vt != dt:
            problems.append(f"{GRAMMAR_FILES[key]}: tokens differ from {VERBATIM_FILES[key]} after the listed repairs")
    return problems


def self_checks(doc, source_text):
    problems, notes = [], []
    for key, f in VERBATIM_FILES.items():
        rules, errors, _ = parse_rulelist((SCHEMA_DIR / f).read_text(encoding="utf-8"))
        got = [f"line {ln}: {msg}" for ln, msg in errors]
        want = (doc.get("grammar_files") or {}).get(key, {}).get("verbatim_parse_errors", [])
        if got != want:
            problems.append(f"{f}: RFC 5234 parse errors differ from the recorded ones: {got}")
    for key, f in GRAMMAR_FILES.items():
        if G[key].errors:
            problems.append(f"{f}: not valid RFC 5234: {G[key].errors}")
    problems += grammar_repairs_ok(doc)
    if XSD["sha256"] != XSD_SHA256:
        problems.append(f"cpe-naming_2.3.xsd: SHA-256 {XSD['sha256']}, expected {XSD_SHA256}")
    if source_text is None:
        notes.append("source text not found: verbatim-against-source checks skipped")
    else:
        norm = normalise_source(source_text)
        hay = source_text.splitlines()
        # The figure files keep the page's columns and pdftotext -layout widens
        # some runs of spaces, so the lines are compared with runs collapsed.
        solid = [collapse(h) for h in hay if h.strip()]
        for key, f in VERBATIM_FILES.items():
            body = (SCHEMA_DIR / f).read_text(encoding="utf-8").split("\n; " + "=" * 69 + "\n", 2)[-1]
            fig = [collapse(ln) for ln in body.split("\n") if ln.strip()]
            if not any(solid[i:i + len(fig)] == fig for i in range(len(solid) - len(fig) + 1)):
                problems.append(f"{f}: the figure lines do not occur, in order, in the source text")
        for r in doc.get("rules", []):
            if collapse(r["text"]) not in norm:
                problems.append(f"rule {r['id']}: text is not verbatim in the source text")
        for fx in doc["fixtures"]:
            for key in ("input_file", "expected_file", "input_raw_file"):
                rel = fx.get(key)
                if rel and rel.startswith("verbatim/"):
                    if not lines_occur(read_fixture(rel), hay):
                        problems.append(f"{fx['id']}: {rel} does not occur in the source text")
            for v in fx.get("violates", []) or []:
                if collapse(v["text"]) not in norm:
                    problems.append(f"{fx['id']}: a violates text is not verbatim in the source text")
            if fx.get("quote") and collapse(fx["quote"]) not in norm:
                problems.append(f"{fx['id']}: quote is not verbatim in the source text")
        # Quotations of the specification inside library prose: every double-quoted
        # span that reads as text (it holds a space and a letter) must be verbatim.
        prose = [(f["id"], f.get("text", "")) for f in doc.get("findings", [])]
        prose += [(fx["id"], fx.get(k, "")) for fx in doc["fixtures"]
                  for k in ("finding", "expected_note", "purpose", "label")]
        for owner, text in prose:
            for span in quoted_spans(text):
                if collapse(span) not in norm and collapse(span) not in NOT_FROM_SOURCE:
                    problems.append(f"{owner}: quoted text not verbatim in the source: {span!r}")
    for fx in doc["fixtures"]:
        if fx.get("source") == "derived" and "input_file" in fx and fixture_input(fx) != fx.get("input"):
            problems.append(f"{fx['id']}: {fx['input_file']} differs from the inline input")
        if "expected_file" in fx:
            want = printed_output(fx)
            if want is not None and want != expected_output(fx):
                problems.append(f"{fx['id']}: the expected output differs from {fx['expected_file']}")
    rule_ids = {r["id"] for r in doc.get("rules", [])}
    for fx in doc["fixtures"]:
        for v in fx.get("violates", []) or []:
            if v["rule"] not in rule_ids:
                problems.append(f"{fx['id']}: violates cites unknown rule {v['rule']}")
    problems += schema_pattern_checks(notes)
    problems += json_schema_cross_check(doc, notes)
    xsd_agreement_note(doc, notes)
    return problems, notes


def xsd_agreement_note(doc, notes):
    """How often the XML schema patterns agree with the figures, over every CPE name in the fixtures."""
    uris, fss = set(), set()

    def walk(o):
        if isinstance(o, str):
            low = o.lower()
            if low.startswith("cpe:2.3:"):
                fss.add(o)
            elif low.startswith("cpe:/"):
                uris.add(o)
        elif isinstance(o, dict):
            for v in o.values():
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)
    for fx in doc["fixtures"]:
        walk({k: fx[k] for k in ("input", "expected", "actual") if k in fx})
        for key in ("input_file", "expected_file"):
            if key in fx:
                walk(joined(read_fixture(fx[key])))
    u_diff = sum(1 for u in uris if len({uri_grammar(u)[k] for k in
                                         ("xsd_cpe22Type", "figure_6_1", "figure_6_1_case_sensitive")}) > 1)
    f_diff = sum(1 for f in fss if fs_grammar(f)["xsd_cpe23Type"] != fs_grammar(f)["figure_6_3_case_sensitive"])
    notes.append(f"XML schema against the figures: cpe22Type differs from Figure 6-1 (either reading) on "
                 f"{u_diff} of {len(uris)} URIs; cpe23Type differs from Figure 6-3 read case-sensitively on "
                 f"{f_diff} of {len(fss)} formatted strings")


def json_schema_cross_check(doc, notes):
    """Every WFN in the fixtures, written in the JSON shape of wfn.derived.schema.json,
    must get the same verdict from the JSON Schema as from wfn_checks (valid against
    invalid or disputed, since the schema requires Figure 5-1 and the prose both)."""
    try:
        from jsonschema import Draft202012Validator
    except ImportError:
        notes.append("jsonschema not installed: JSON Schema cross-check skipped")
        return []
    v = Draft202012Validator(json.loads((SCHEMA_DIR / "wfn.derived.schema.json").read_text(encoding="utf-8")))
    seen, problems = {}, []
    for fx in doc["fixtures"]:
        texts = []
        if fx["kind"] in ("wfn", "bind", "bind-uri", "bind-fs"):
            try:
                texts.append(fixture_input(fx))
            except (KeyError, ValueError):
                pass
        if fx["kind"] in ("unbind-uri", "unbind-fs") and "expected_file" in fx:
            texts.append(joined(read_fixture(fx["expected_file"])))
        for key in ("unbind_URI", "unbind_fs"):
            w = (fx.get("expected", {}).get(key) or {}).get("wfn")
            if w:
                texts.append(w)
        for text in texts:
            try:
                pairs = parse_wfn(text)
            except ValueError:
                continue
            if len({a.lower() for a, _ in pairs}) != len(pairs):
                continue                     # duplicate attributes have no JSON form
            obj = {a.lower(): ({"logical": x.name} if isinstance(x, Logical) else x) for a, x in pairs}
            seen[text] = (fx["id"], obj, wfn_checks(pairs)["verdict"])
    for text, (fid, obj, verdict) in seen.items():
        ok = not any(True for _ in v.iter_errors(obj))
        if ok != (verdict == "valid"):
            problems.append(f"{fid}: JSON Schema says {'valid' if ok else 'invalid'}, wfn_checks says {verdict}")
    notes.append(f"JSON Schema cross-check: {len(seen)} distinct WFNs, {len(problems)} disagreements")
    return problems


QUOTED = re.compile(r'"((?:[^"\\]|\\.)*)"')
# quoted spans in library prose that quote something other than the specification
NOT_FROM_SOURCE = {"ABNF strings are case-insensitive"}


def quoted_spans(text):
    """Double-quoted spans of library prose that look like quoted sentences."""
    out = []
    for m in QUOTED.finditer(text or ""):
        span = m.group(1)
        if " " in span and re.search(r"[A-Za-z]{3}", span) and len(span) >= 12:
            out.append(span)
    return out


def printed_output(fx):
    """The output a verbatim fixture's expected_file prints, normalised like the actual one."""
    text = joined(read_fixture(fx["expected_file"]))
    if fx["kind"] in ("unbind-uri", "unbind-fs"):
        return fmt_wfn(pairs_to_wfn(parse_wfn(text)))
    return text


def expected_output(fx):
    exp = fx.get("expected", {})
    for key, field in (("bind_to_URI", "uri"), ("bind_to_fs", "fs"), ("unbind_URI", "wfn"), ("unbind_fs", "wfn")):
        if key in exp and field in exp[key]:
            return exp[key][field]
    return None


def schema_patterns():
    """The patterns wfn.derived.schema.json must carry, compiled from the ABNF here."""
    g = G["figure_5_1"]
    return {
        "avstring-figure-5-1": "^" + g.regex("avstring", True)[0] + "$",
        "avstring-prose": "^" + g.regex("avstring-prose", True)[0] + "$",
        "part-string": "^" + g.regex("part-string", True)[0] + "$",
        "language-string": "^" + g.regex("language-string", True)[0] + "$",
    }


def schema_pattern_checks(notes):
    problems = []
    schema = json.loads((SCHEMA_DIR / "wfn.derived.schema.json").read_text(encoding="utf-8"))
    want = schema_patterns()
    for name, pat in want.items():
        got = schema["$defs"][name].get("pattern")
        if got != pat:
            problems.append(f"wfn.derived.schema.json: $defs/{name}/pattern differs from the ABNF compilation")
    node = shutil.which("node")
    if not node:
        notes.append("node not on PATH: ECMA-262 compilation of the schema patterns skipped")
        return problems
    js = ("const p=JSON.parse(require('fs').readFileSync(0,'utf8'));"
          "const r={};for(const[k,v]of Object.entries(p)){try{new RegExp(v,'u');r[k]='ok'}catch(e){r[k]=e.message}}"
          "process.stdout.write(JSON.stringify(r))")
    res = json.loads(subprocess.run([node, "-e", js], input=json.dumps(want), capture_output=True,
                                    text=True, check=True).stdout)
    for k, v in res.items():
        if v != "ok":
            problems.append(f"schema pattern {k} does not compile in ECMA-262 with the u flag: {v}")
    return problems


# =========================================================================
# 9. main
# =========================================================================

def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--source-text", default=str(DEFAULT_SOURCE_TEXT))
    ap.add_argument("--expected", default=str(HERE / "expected.yaml"))
    ap.add_argument("--json", action="store_true", help="print recomputed results as JSON")
    args = ap.parse_args()

    import yaml
    load_grammars()
    doc = yaml.safe_load(pathlib.Path(args.expected).read_text(encoding="utf-8"))
    src = pathlib.Path(args.source_text)
    source_text = src.read_text(encoding="utf-8") if src.exists() else None
    problems, notes = self_checks(doc, source_text)

    fresh = {}
    for fx in doc["fixtures"]:
        try:
            actual = compute(fx)
        except Exception as exc:  # a fixture that cannot even be read is a problem, not a crash
            problems.append(f"{fx['id']}: computation failed: {type(exc).__name__}: {exc}")
            continue
        fresh[fx["id"]] = {"actual": actual, "comparison": compare(fx.get("expected", {}), actual)}

    if args.json:
        for p in problems:
            print("FAIL:", p, file=sys.stderr)
        print(json.dumps({"python": sys.version.split()[0], "fixtures": fresh}, indent=2, ensure_ascii=False))
        return 1 if problems else 0

    differs = 0
    for fx in doc["fixtures"]:
        got = fresh.get(fx["id"])
        if got is None:
            continue
        if fx.get("actual") != got["actual"]:
            problems.append(f"{fx['id']}: recorded actual result does not match this run")
        if fx.get("comparison") != got["comparison"]:
            problems.append(f"{fx['id']}: recorded comparison does not match this run")
        if any(v == "differs" for v in got["comparison"].values()):
            differs += 1
            if not str(fx.get("finding", "")).strip():
                problems.append(f"{fx['id']}: the reference implementation differs from the expected result "
                                f"but no finding is written")
    for n in notes:
        print("note:", n)
    for p in problems:
        print("FAIL:", p)
    print(f"{len(doc['fixtures'])} fixtures; {differs} where the pseudocode differs from the expected "
          f"result (each has a finding); {len(problems)} problems")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
