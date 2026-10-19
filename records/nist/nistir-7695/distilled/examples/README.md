---
record: nistir-7695
kind: examples
title: "nistir-7695: examples, derived fixtures and expected results"
extracted: "2026-10-18"
reviewed_by: ""
---

# NISTIR 7695 (CPE Naming 2.3): examples and test vectors

Every example that NIST IR 7695, "Common Platform Enumeration: Naming
Specification Version 2.3" (August 2011) prints, copied character for
character, plus 112 fixtures the library derived from the text. Each fixture
has an expected result worked out by hand from the specification and the
actual result of `run-fixtures.derived.py`, the library's reference
implementation of the specification's own pseudocode and grammars. The script
reproduces every actual result and fails if one changes.

Source: `.cache/nistir-7695.bin`, SHA-256
`01553a4638b21eda10018690b71162e91605d78eb15850f881bd0b2b691ac3f6`, 49 pages,
read through `pdftotext -layout` (`.cache/nistir-7695.txt`, 2443 lines). Every
example was checked against the rendered PDF page. NIST published NISTIR 7695
with no copyright or licence notice; works of NIST employees are not subject to
copyright in the United States (17 U.S.C. 105), but two of its three authors
were not NIST staff (Acknowledgments, p. iii).
Locators give the section, the printed page with the PDF page in parentheses
(PDF page = printed page + 6) and the line in the text rendering.

## Files

| path | what |
|---|---|
| `expected.yaml` | the index: all 177 fixtures, each with its locator (or what it was derived from), the statements a negative breaks (`violates`: rule id, locator, verbatim text, and `breaks`, the `requirements.yaml` ids it breaks), the expected result, the actual result, a comparison and, where it matters, a finding. It also holds the 78 rules it cites, quoted verbatim, each with the `requirements.yaml` ids that hold it (`requirements`; both id keys were added in pass 3, cross-check), the 28 findings, and `grammar_files`, which pins the RFC 5234 parse errors of the four printed figures and the repairs that turn them into `../schema/*.derived.abnf` |
| `verbatim/` | the printed examples, 84 files, named `sec-<section>-<what>.txt`; each holds the printed characters plus one LF |
| `derived/` | the 112 derived inputs, one file per fixture, named `<fixture id>.derived.txt`; each holds one line plus one LF, taken as written (`AV-NEG-07`, the empty value, is the empty line). `expected.yaml` repeats each input inline as `input` for reading, and the runner checks the two are equal |
| `run-fixtures.derived.py` | the reference implementation and runner (library-written; Python 3.9 or later, standard library plus PyYAML) |

Files the library wrote carry `.derived.` before the extension; files under
`verbatim/` are copies of source text and do not. `README.md` and
`expected.yaml` keep the names the scaffold gave them.

What a verbatim file holds. A wrapped example keeps its printed lines; joined
with nothing between them they give the string (every wrap falls after a
comma, except §6.2.3.3.3, whose formatted string wraps after a hyphen).
Labels (`URI: `, `FS: `), list bullets, the pseudocode comment marker `;; `
and the explanation in parentheses that follows 12 of the 13 value strings of
§5.3.2 are not part of an example and are left out. The arrow of the §5.4 examples is
a Symbol-font glyph (U+F0AE in the text layer) and is written U+2192. The 13
value strings of §5.3.2 keep their surrounding quotation marks, which §5.3.2
says "are, of course, not considered part of the string values themselves";
`input_token: quoted` in `expected.yaml` marks them.

## Counts

| group | ids | n | what |
|---|---|---:|---|
| source examples | `SRC-*` | 65 | §1: a WFN and its two bindings (3); §5: an attribute=value set (1); §5.1: attribute-value pairs (4); §5.3.1 and §5.3.2: notation fragments (4); §5.3.2: allowable value strings (13); §5.4: `new`, `get`, `set` (7); §5.5: WFNs (5); §6.1.2.1.2: the two inline binding examples (2); §6.1.2.4: WFN to URI (5); §6.1.3.2 and §6.2.3.2: the comment examples of `get_comp_uri` and `get_comp_fs` (2); §6.1.3.3: URI to WFN (8, two of them errors); §6.2.2.3: WFN to formatted string (6); §6.2.3.3: formatted string to WFN (5, one an error) |
| value strings, positive | `AV-POS-01` to `07` | 7 | valid under Figure 5-1 and the prose |
| value strings, disputed | `AV-DSP-01` to `05` | 5 | Figure 5-1 and the prose of §5.3.2 disagree |
| value strings, negative | `AV-NEG-01` to `11` | 11 | invalid under both |
| WFNs | `WFN-POS-01` to `06`, `WFN-NEG-01` to `08` | 14 | §5.2, §5.3.1, §5.3.3.1, §5.3.3.10 |
| URIs | `URI-POS-01` to `07`, `URI-NEG-01` to `12`, `URI-EDGE-01` to `04` | 23 | Figures 6-1 and 6-2, the XML schema, and `unbind_URI` |
| formatted strings | `FS-POS-01` to `07`, `FS-NEG-01` to `15` | 22 | Figure 6-3, the XML schema, and `unbind_fs` |
| bindings | `BIND-01` to `10`, `BIND-NEG-01`, `02` | 12 | one WFN through `bind_to_URI` and `bind_to_fs` |
| conversions | `CONV-01` to `07` | 7 | §7.1 and §7.2 on §6 examples |
| round trips | `RT-01` to `11` | 11 | the §7 round-trip claim |
| **total** | | **177** | 65 printed, 112 derived |

The edge cases the extraction brief asked for: quoting (`AV-POS-03` to `07`,
`FS-POS-03`, `FS-POS-04`, `FS-NEG-09`, `FS-NEG-13`, `BIND-05`, which binds
every quoted character of Table 6-1), percent-encoding (`URI-POS-04`,
`URI-POS-06`, `URI-NEG-01`, `02`, `05`, `11`, `BIND-05`), ANY and NA
(`WFN-POS-04`, `05`, `URI-POS-01`, `03`, `07`, `URI-NEG-08`, `URI-EDGE-04`,
`FS-POS-01`, `02`, `BIND-01`, `02`, `RT-10`, `11`), wildcards (`AV-POS-01`,
`02`, `07`, `AV-DSP-01` to `05`, `AV-NEG-02` to `04`, `URI-NEG-09` to `11`,
`URI-EDGE-03`, `FS-POS-05`, `06`, `FS-NEG-04`, `05`, `11`, `12`, `BIND-04`,
`10`) and the packed edition (`URI-POS-03`, `URI-NEG-06`, `07`, `URI-EDGE-02`,
`04`, `BIND-01`, `07`, `CONV-02`, `05`, `06`, `RT-05`, `08`, `10`).

## How the expected results were derived

- **Printed examples**: the expected result is what the specification prints
  ("This WFN binds to the following URI:", "Unbinds to this WFN:", "An error
  is raised when this URI is unbound"). The runner checks that the expected
  output in `expected.yaml` equals the printed one in `verbatim/`.
- **Derived fixtures**: worked out by hand from the cited statements and by
  running the pseudocode by hand. Only after that was the reference
  implementation run; where the two first disagreed the derivation and the
  code were both re-read (one hand error was found and fixed: `WFN-NEG-01`,
  where the library's notation grammar itself rejects the attribute).
- **Where the specification disagrees with itself** the expected block keeps
  each authority's answer under its own key instead of choosing: for a value
  string `figure_5_1` and `prose_5_3_2`; for a URI `figure_6_1`,
  `figure_6_2` and the `unbind_URI` outcome. A `finding` then names the
  disagreement.
- **Values that are not well formed** have no expected binding: 6.1.2 says
  "The behavior of bind_to_URI is undefined if its input is not well formed."
  Their actual results are recorded anyway, because they show what an
  implementation that follows the pseudocode does (for example,
  `transform_for_uri` drops an unquoted hyphen without a word: `AV-NEG-05`).

## The reference implementation

`run-fixtures.derived.py` follows the printed pseudocode line by line:
`new`, `get` and `set` (§5.4), `bind_to_URI` with `bind_value_for_URI`,
`transform_for_uri`, `pct_encode`, `pack` and `trim` (§6.1.2.3),
`unbind_URI` with `get_comp_uri`, `decode` and `unpack` (§6.1.3.2),
`bind_to_fs` with `process_quoted_chars` (§6.2.2.2), `unbind_fs` with
`get_comp_fs`, `unbind_value_fs` and `add_quoting` (§6.2.3.2), and
`convert_uri_to_fs` and `convert_fs_to_uri` (§7). Each run ends in a result,
in `error` (the pseudocode's own error statement) or in `undefined` (a state
the pseudocode does not define, such as nil where a string is needed).

It needs these readings, each also stated in the code:

1. **`process_quoted_chars` (finding F-20).** As printed it cannot produce the
   printed examples. The script computes both literal readings
   (`as_printed_assignment`, `as_printed_comparison`) and uses the repaired
   one (`idx := idx + 2. continue.`) as the reference; the comparison key
   `pseudocode_as_printed: differs` marks the 14 fixtures where the literal
   readings give a different string, and each carries the finding.
2. **`get_comp_fs` (F-25)** is a comment, not code. The reference splits on
   colons with a backslash quoting the next character, as Figure 6-3 and
   `add_quoting` do; the literal reading ("unless prefixed by a" backslash)
   is computed too and differs on `FS-POS-04`.
3. **`get_comp_uri`** is a comment too: components after `cpe:/`, and `""`
   for a missing one (its own example says so); the prefix is matched without
   regard to case (RFC 3986 schemes are case-insensitive). A missing
   formatted string field is nil, so `unbind_fs` is undefined for fewer than
   eleven fields.
4. **`substr(s,b,e)`** with `e` past the end returns the characters up to the
   end; with `b > e` or a negative `b` it is undefined ("b must be <= e").
   `is_alphanum` is ASCII letters, digits and the underscore.
5. **Grammar checks** use the repaired grammars of `../schema/` in two
   readings: RFC 2234's case-insensitive quoted strings (`figure_6_1`, ...)
   and case-sensitive ones (`..._case_sensitive`), plus the XML schema's two
   patterns (`xsd_cpe22Type`, `xsd_cpe23Type`).
6. **Value checks** use Figure 5-1, the library's prose reading of §5.3.2
   (readings P1 to P4 in `../schema/figure-5-1-avstring.derived.abnf`), §5.2,
   §5.3.3.1 and RFC 5646 well-formedness for §5.3.3.10.

## Findings

Full text, quotations and fixture lists are under `findings:` in
`expected.yaml`. Every printed example is reproduced by the reference
implementation; the findings are about the specification.

| id | finding | fixtures |
|---|---|---|
| F-01 | Figures 6-1 and 6-2 write incremental alternatives `/=`; ABNF spells them `=/` | grammar files |
| F-02 | Figure 6-2's `pct-encoded` continuation lines begin with `=` | grammar files |
| F-03 | rule names with underscores in Figures 5-1, 6-2, 6-3 | grammar files |
| F-04 | Figure 6-1 prints U+02DC SMALL TILDE where `~` is meant | `SRC-6.1.3.3.7`, `CONV-04`, `RT-03` |
| F-05 | Figure 6-1's `LANGTAG = cf. [RFC5646]` is prose | grammar files |
| F-06 | ABNF strings are case-insensitive: the figures accept `CPE:2.3:`, part `A`, `%2A`; the XML schema does not; `unbind_URI` lower-cases, `unbind_fs` does not | `URI-POS-05`, `06`, `URI-NEG-12`, `FS-NEG-06`, `07`, `RT-02`, `06`, `09` |
| F-07 | Figure 6-1 is not a copy of the CPE 2.2 grammar it says it shows (bare `%`, part alone) | see `../schema/README.md` |
| F-08 | the XML schema §6 calls authoritative differs from Figure 6-1 on 6 of 53 URIs; `cpe23Type` equals case-sensitive Figure 6-3 on all 73 formatted strings | `URI-NEG-02`, `08`, `12`, `BIND-02` |
| F-10 | Figure 5-1 accepts `*`, `**`, `?*`, `*?`, which §5.3.2 forbids | `AV-DSP-01` to `04`, `URI-NEG-10`, `FS-NEG-11`, `BIND-10` |
| F-11 | Figure 5-1 rejects `\-?`, which the prose allows and both bindings round-trip | `AV-DSP-05`, `FS-POS-06`, `BIND-09` |
| F-12 | §5.3 item 2 cites "Section 5.5.3", which does not exist | none |
| F-13 | reading: logical values stay allowed for part | `WFN-POS-04` |
| F-14 | §5.3.3.10 allows any valid RFC 5646 tag; Figures 6-2 and 6-3 do not | `WFN-POS-06`, `BIND-03`, `FS-NEG-08` |
| F-15 | `bind_to_URI` writes `-` for language NA, which Figures 6-1 and 6-2 reject | `BIND-02`, `URI-NEG-08`, `RT-11` |
| F-16 | a lone `?` is a valid value that Figures 6-2 and 6-3 cannot express | `AV-POS-01`, `BIND-04`, `URI-EDGE-03`, `FS-NEG-12` |
| F-17 | quoted underscore: `process_quoted_chars` handles it, Figure 5-1 and `pct_encode` do not | `AV-NEG-10`, `BIND-NEG-02` |
| F-20 | `process_quoted_chars` cannot run as printed (`idx = idx + 2.` without `continue`) | 14 fixtures, among them every printed WFN to formatted string example with a quoted period |
| F-21 | `add_quoting` accepts `a??b`; `decode` rejects `a%01%01b` | `AV-NEG-03`, `FS-NEG-05`, `URI-NEG-11` |
| F-22 | `unbind_URI` rejects URIs Figure 6-1 allows, against §6.1.1's MUST; the printed examples 6.1.3.3.6 and 6.1.3.3.8 are such URIs | `SRC-6.1.3.3.6`, `SRC-6.1.3.3.8`, `URI-NEG-01`, `05`, `06` |
| F-23 | the asterisk rules are not enforced on unbinding; a lone `*` string collides with ANY | `AV-DSP-01`, `02`, `URI-NEG-10`, `FS-NEG-11`, `BIND-10`, `RT-07` |
| F-24 | limited checking: unbinding returns WFNs that break §5 (part `x`, extra or missing fields) | `URI-NEG-03`, `04`, `FS-NEG-01`, `02`, `09`, `10`, `15` |
| F-25 | `get_comp_fs` is an ambiguous comment ("forward slash"; escaped backslash before a colon) | `SRC-6.2.3.2-GET-COMP-FS`, `FS-POS-04` |
| F-26 | the §7 round trip fails for URIs Figure 6-1 allows and formatted strings with upper case | `RT-02` to `07`, `RT-09` |
| F-27 | the error example of 6.2.3.3.3 has ten fields, not eleven | `SRC-6.2.3.3.3-VARIANT` |
| F-28 | 6.1.3.3.5 prints `target_HW` | `SRC-6.1.3.3.5` |
| F-29 | §7 calls `unbind_uri` and `bind_to_uri`; §6.1 defines `unbind_URI` and `bind_to_URI` | none |
| F-35 | the same-result MUST of §6.1.3 and §6.2.3 against the SHOULD to add syntax checks | `URI-NEG-09`, `FS-NEG-03` |
| F-36 | an empty formatted string field becomes an empty value, which §5.3.2 forbids | `FS-NEG-14` |

The numbering has gaps on purpose (F-09, F-18, F-19, F-30 to F-34 are
unused) so that the grammar findings, the value findings and the pseudocode
findings keep their own ranges.

For a consumer of CPE names the practical upshot: compare names after
unbinding, never as strings (`RT-02` to `RT-07` and `RT-09` show seven ways a
name changes on a round trip); treat the pseudocode as a definition of
results, not as a validator (F-24); validate with the derived grammars and
decide, explicitly, how to read case (F-06) and the two §5.3.2 disputes
(F-10, F-11).

## Judgement calls

- **The repaired `process_quoted_chars` is the reference.** Both literal
  readings are recorded; neither reproduces a single printed example with a
  quoted period, while the repair reproduces all of them.
- **Readings P1 to P4** of §5.3.2 (`../schema/README.md`); the most
  consequential is P2, that a value made only of special characters is
  allowed only when it is a run of `?`.
- **`part` may be ANY or NA** (F-13).
- **Language checks are RFC 5646 well-formedness** only.
- **§5 and §5.1 illustrations are fixtures** of kind `illustration`: they
  are examples in the text, but of attribute=value pairs in general, not of
  WFNs, so the expected result is only that they are not in the WFN notation.
- **The §5.3.1 and §5.3.2 notation fragments** contain the ellipsis
  character; the runner checks only the pairs they show.
- **Section 7 prints no examples.** The conversion and round-trip fixtures
  are derived from the §6 examples and from URIs and formatted strings that
  the figures allow.

## Reproduce

From the repository root, with Python 3.9 or later and PyYAML (listed in
`requirements-dev.txt`):

```sh
# the source, never committed (CLAUDE.md); needed only for the verbatim checks
mkdir -p .cache
curl -L -o .cache/nistir-7695.bin https://nvlpubs.nist.gov/nistpubs/Legacy/IR/nistir7695.pdf
shasum -a 256 .cache/nistir-7695.bin   # 01553a4638b21eda10018690b71162e91605d78eb15850f881bd0b2b691ac3f6
pdftotext -layout .cache/nistir-7695.bin .cache/nistir-7695.txt

python3 -I records/nist/nistir-7695/distilled/examples/run-fixtures.derived.py
python3 -I records/nist/nistir-7695/distilled/examples/run-fixtures.derived.py --json
python3 -I records/nist/nistir-7695/distilled/examples/run-fixtures.derived.py --source-text /other/path/nistir7695.txt
```

The first command checks everything and ends with
`177 fixtures; 15 where the pseudocode differs from the expected result (each has a finding); 0 problems`.
Before comparing results it checks that the four printed figures parse with
exactly the RFC 5234 errors recorded in `expected.yaml` and that their lines
occur, in order, in the text rendering (runs of spaces collapsed, because the
figure files keep the page's columns); that the four derived grammars parse
with none and equal the printed figures token for token after the listed
repairs; that the XML schema has its pinned SHA-256; that every `derived/`
file equals its inline input; that every `verbatim/` file, every quoted rule, every `violates` text and every quotation inside a
finding or note occurs verbatim in the text rendering; that each printed
expected output equals the expected value in `expected.yaml`; that the
patterns of `../schema/wfn.derived.schema.json` equal the ones compiled from
the ABNF and compile as ECMA-262 regular expressions with the `u` flag (with
`node` on `PATH`); and that the JSON Schema gives the same verdict as the
ABNF-based check on all 84 distinct WFNs in the fixtures (with jsonschema
installed). Without the source text, `node` or jsonschema those checks are
skipped and reported. `--json` prints the recomputed results instead of
comparing them.

Versions in the recorded run: Python 3.13.9, PyYAML 6.0.3, jsonschema 4.26.0,
Node v22.23.2; the text rendering came from pdftotext (Poppler) 26.07.0.

`expected.yaml` parses identically with the library's reader and PyYAML
(every scalar is a quoted string or a block scalar; there are no flow
collections):

```sh
python3 -I -c "import sys, yaml; sys.path.insert(0, 'bin'); from _yaml import parse; t = open('records/nist/nistir-7695/distilled/examples/expected.yaml', encoding='utf-8').read(); assert parse(t) == yaml.safe_load(t); print('identical')"
```

## Not transcribed

| source | why |
|---|---|
| §5.1, `wfn:[a1=v1, a2=v2, …, an=vn]` (p. 9, L571) | the notation template, not an example; it has no values |
| §6.2, the field template that begins `cpe:2.3: part : vendor :` (p. 31, L1811-1812) | a template of the formatted string, not an example |
| Tables 6-1 and 6-2 (p. 19) | mapping tables, implemented in the script (`PCT_ENCODE`, `DECODE`), bound in full by `BIND-05`, and checked against `pct_encode`, `decode` and Figure 6-2 (`../schema/README.md`) |
| §1.3, `[CPE22:7]` and `(cf. 5.3.1)` (p. 2) | examples of citation style, not of CPE names |
| words given as examples inside prose: the platforms and devices of §2.1, "Lenovo ThinkPad X61" (§5), the attribute names Foo, foo and FOO (§5.1, L560), x86 (§5.3.3.9), instance data (§5.3.3.11) | not names or values in any CPE form; the §5.1 case rule they illustrate is exercised by `WFN-POS-03` |
| the pseudocode itself | implemented, not transcribed; `normative.md` carries the text |
