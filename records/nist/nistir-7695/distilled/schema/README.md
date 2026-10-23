---
record: nistir-7695
kind: schema
title: "nistir-7695: schemas (four ABNF figures verbatim, their repairs, derived rules, a WFN JSON Schema and the NIST XML schema)"
extracted: "2026-10-18"
reviewed_by: ""
---

# nistir-7695: schemas

This README is derived: the library wrote it. Files whose names carry
`.derived.` are the library's; the four `figure-*.abnf` files carry the
figures as the specification prints them under a header the library added;
`cpe-naming_2.3.xsd` is NIST's file, bytes unchanged.

Source: NIST Interagency Report 7695, "Common Platform Enumeration: Naming
Specification Version 2.3" (August 2011), PDF SHA-256
`01553a4638b21eda10018690b71162e91605d78eb15850f881bd0b2b691ac3f6`, read
through `pdftotext -layout` (2443 lines). NIST published NISTIR 7695 with no
copyright or licence notice; works of NIST employees are not subject to
copyright in the United States (17 U.S.C. 105), but two of its three authors
were not NIST staff (Acknowledgments, p. iii). Locators
give the section, the printed page with the PDF page in parentheses (PDF page
= printed page + 6) and the line in the text rendering.

## What NISTIR 7695 prints, and what it does not

- **Four ABNF grammars**, each in a boxed figure: Figure 5-1 "ABNF Grammar for
  Attribute-Value Strings" (§5.3.2, p. 11), Figure 6-1 "ABNF for
  v2.2-Compatible URI Binding" (§6.1.1, p. 16), Figure 6-2 "ABNF for
  Preferred URI Binding" (§6.1.1, p. 17) and Figure 6-3 "ABNF for Formatted
  String Binding" (§6.2.1, p. 32). All four are here verbatim. **None of the
  four is valid RFC 2234 ABNF as printed** (findings F-01 to F-05), so each
  has a repaired twin that is.
- **Two mapping tables**, Table 6-1 (quoted characters to percent-encodings)
  and Table 6-2 (unquoted special characters to `%01` and `%02`), p. 19. They
  are data, not grammars. `../examples/run-fixtures.derived.py` implements
  them, and they agree entry for entry with the pseudocode's `pct_encode` and
  `decode` and with Figure 6-2's `pct-encoded` list: 31 table entries, of
  which 29 are percent forms (the hyphen and the period pass unencoded).
- **Pseudocode** for binding and unbinding (§6.1.2.3, §6.1.3.2, §6.2.2.2,
  §6.2.3.2) and conversion (§7.1, §7.2). Implemented, line by line, in
  `../examples/run-fixtures.derived.py`.
- **No grammar or schema for the WFN itself.** §5.1: "The WFN is a logical
  construct only." The rules for a WFN are prose (§5.2, §5.3) plus Figure 5-1
  for one value string. The derived files below express them.
- **A pointer to an XML schema.** §6: "The XML schema implementation of these
  format requirements, which is the authoritative XML binding definition, can
  be found at http://scap.nist.gov/schema/cpe/2.3/cpe-naming_2.3.xsd." It is
  not printed in the report; the file is here (provenance below).

## Files

| file | verbatim or derived | what it is | locator | SHA-256 |
|---|---|---|---|---|
| `figure-5-1-avstring.abnf` | **verbatim** figure + library header | Figure 5-1 | §5.3.2 / p. 11 (PDF p. 17) / L675-695 | `700967cf0d4adf91b3a63305b3a58463c7f73e6efbef50ceedae83160fa88438` |
| `figure-6-1-uri-v2.2-compatible.abnf` | **verbatim** figure + library header | Figure 6-1 | §6.1.1 / p. 16 (PDF p. 22) / L934-960 | `d1b9d9d5d6d5308503d94664117da69f27dab1019b73f5090e152f78a878221f` |
| `figure-6-2-uri-preferred.abnf` | **verbatim** figure + library header | Figure 6-2 | §6.1.1 / p. 17 (PDF p. 23) / L980-1018 | `d31429d1324db5529e724058900cba82e4e20d9c0ba6281c41cbca9d90df2dbb` |
| `figure-6-3-formatted-string.abnf` | **verbatim** figure + library header | Figure 6-3 | §6.2.1 / p. 32 (PDF p. 38) / L1834-1868 | `f0019a839ff3c966f9b3010134eba1b825f9534a030b84b790844fdac7c3ae4a` |
| `figure-5-1-avstring.derived.abnf` | **derived** | Figure 5-1 repaired (PART 1), plus the prose of §5.3.2 as a grammar (`avstring-prose`), their intersection (`avstring-strict`), `part-string` (§5.3.3.1), `language-string` (§5.3.3.10) and the `wfn:[...]` notation (`wfn-notation`, §5.1) | §5.1, §5.3, Figure 5-1 | `a56b7cc872a5b9a62337c3d627ba5c0b2e9b2c84932dae8e0ca635c40d0a0c40` |
| `figure-6-1-uri-v2.2-compatible.derived.abnf` | **derived** | Figure 6-1 repaired (R1 to R3) | §6.1.1 | `c0b81f7e945b20b78f2a7345e7a983d290505e475d454880798fb1ba589a167c` |
| `figure-6-2-uri-preferred.derived.abnf` | **derived** | Figure 6-2 repaired (R1 to R3) | §6.1.1 | `be2a89dfccdfe39de157e019f9115c905adf62de3a34dc2c1fc48ffa5e4c2117` |
| `figure-6-3-formatted-string.derived.abnf` | **derived** | Figure 6-3 repaired (R1) | §6.2.1 | `d1cbc8145da0abbc8e67263b81a91c960f6dae2b2a8254ca832534e23cbb5b0f` |
| `wfn.derived.schema.json` | **derived** | JSON Schema (draft 2020-12) for a WFN written as a JSON object, a shape the library defined | §5.2, §5.3, Figure 5-1 | `b9f680546199b1fadbe4dce8f338abdcd0264602298786e31a7dc5d3dcf06998` |
| `cpe-naming_2.3.xsd` | **verbatim** bytes (NIST's file) | the XML schema §6 calls "the authoritative XML binding definition": two simple types, `cpe22Type` and `cpe23Type`, each one `xsd:pattern` | §6 / p. 16 (PDF p. 22) / L916-918 | `d37f813fe223922fb7456751d453482009fc7075a3f5ad5e1999d075d190dd69` |
| `README.md` | derived (this file) | | | not listed: a file cannot state its own digest |

Naming. As in the library's other FX-1 records, a file the library wrote
carries `.derived.` before its extension and says "derived" in its first 12
lines; an unmarked name says the content is the source's. The four figure
files are the one compromise: their bodies are the source's characters, their
headers are the library's. Each header says so on its fourth line, and the
runner checks that every figure line occurs, in order, in the text rendering
(runs of spaces collapsed).

How the verbatim figures were made and checked. Each figure line is placed
at the columns the page prints it in: the glyph runs of the PDF's content
stream, at 6.0 pt per character of the figures' Courier New (Figure 5-1
holds explicit space characters; Figures 6-1 to 6-3 also position runs
across gaps). Two layout changes only: the indentation common to the whole
figure removed (6 columns in Figure 5-1, which sits in a box; none in the
others) and trailing spaces dropped. The bodies equal the figure code blocks
of `../normative.md` line for line. `pdftotext -layout` widens some runs of
spaces, so compare against `nistir7695.txt` with runs of spaces collapsed;
ABNF treats any run of spaces alike. (Pass 1 had taken the spacing from the
text rendering; pass 2 rebuilt it from the content stream, which changed
spaces only.) Every figure was compared with the page rendered at 300 dpi
(PDF pages 17, 22, 23 and 38). The comparison confirmed two things a reader would otherwise
doubt: the four `=` that begin the continuation lines of Figure 6-2's
`pct-encoded` are printed, and the last alternative of Figure 6-1's
`unreserved` is a raised small tilde, U+02DC in the text layer.

## How to use the grammars

**Which grammar for which job.**

| job | use | why |
|---|---|---|
| validate one WFN value string | `avstring-strict` in `figure-5-1-avstring.derived.abnf` (or `avstring` for Figure 5-1 alone, `avstring-prose` for the prose alone) | the figure and the prose disagree on two families of strings (F-10, F-11); `avstring-strict` accepts only what both accept |
| accept a URI as input | `cpe-name` in `figure-6-1-uri-v2.2-compatible.derived.abnf` | §6.1.1: conforming consumers "MUST accept as valid input any URI that obeys the full syntax shown in Figure 6-1" |
| produce or lint a URI | `cpe-name` in `figure-6-2-uri-preferred.derived.abnf` | §6.1.1: "CPE URIs SHOULD obey the more restricted syntax shown in Figure 6-2" |
| accept or produce a formatted string | `formstring` in `figure-6-3-formatted-string.derived.abnf` | section 4 items 2 and 4(a) |
| check a WFN held as JSON | `wfn.derived.schema.json` | its `$comment` lists the statements it enforces |
| match what XML tools accept | the patterns in `cpe-naming_2.3.xsd` | see F-08 for where they differ from the figures |

**Running them.** The derived files are plain RFC 5234 and load into any
ABNF tool, with two cautions. First, RFC 2234 and RFC 5234 quoted strings are
case-insensitive (RFC 2234 section 2.3: "ABNF strings are case-insensitive"),
so these grammars accept `CPE:2.3:` and a part `A` (finding F-06); to get the
case-sensitive reading the XML schema uses, read every quoted string as RFC
7405 `%s"..."`. Second, two rules are prose values that a tool must supply:
`LANGTAG` in the Figure 6-1 grammar (the RFC 5646 section 2.1 `Language-Tag`
production) and `language-string` in the Figure 5-1 grammar (the same, with
each hyphen quoted as `\-`).

The library's own engine needs only Python 3.9 or later and no package. From
the repository root:

```sh
python3 -I - 'cpe:2.3:a:hp:insight:7.4.0.1570:-:*:*:online:win2003:x64:*' 'cpe:/a:foo%2dbar' <<'EOF'
import importlib.util, sys
spec = importlib.util.spec_from_file_location(
    "rf", "records/nist/nistir-7695/distilled/examples/run-fixtures.derived.py")
rf = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rf)
rf.load_grammars()
for name in sys.argv[1:]:
    if name.lower().startswith("cpe:2.3:"):
        print(name, rf.fs_grammar(name), rf.unbind_fs_result(name)["outcome"])
    else:
        print(name, rf.uri_grammar(name), rf.unbind_uri_result(name)["outcome"])
print(rf.G["figure_5_1"].match("avstring-strict", "8\\.*"))
EOF
```

Output on 2026-10-19:

```
cpe:2.3:a:hp:insight:7.4.0.1570:-:*:*:online:win2003:x64:* {'figure_6_3': 'valid', 'figure_6_3_case_sensitive': 'valid', 'xsd_cpe23Type': 'valid'} wfn
cpe:/a:foo%2dbar {'figure_6_1': 'valid', 'figure_6_1_case_sensitive': 'valid', 'figure_6_2': 'invalid', 'figure_6_2_case_sensitive': 'invalid', 'xsd_cpe22Type': 'valid'} error
valid
```

The second line shows finding F-22 in one row: a URI that Figure 6-1 allows
(and so a conforming consumer must accept) is one the pseudocode's `decode`
rejects.

The engine parses a grammar with a strict RFC 5234 parser (`parse_rulelist`)
and compiles a root rule to a regular expression (`Grammar.regex`); it
refuses recursive rules, which none of these grammars has. The same compiler
writes the four `pattern` values of `wfn.derived.schema.json`, and the runner
fails if the file and the compiler disagree or if a pattern does not compile
as an ECMA-262 regular expression with the `u` flag (checked with Node
v22.23.2 when `node` is on `PATH`).

**The JSON Schema.** A WFN is an object whose keys are the eleven attribute
names in lower case; an absent key is unspecified (ANY by §5.2 item 2); a
value is either the attribute-value string as written between the quotation
marks of the `wfn:[...]` notation (so `version="8\.0\.6001"` is the JSON
string `"8\\.0\\.6001"`) or `{"logical": "ANY"}` or `{"logical": "NA"}`.
When jsonschema is installed, the runner validates every WFN that occurs in
the fixtures (84 distinct WFNs: the printed examples, the derived ones and
every expected unbinding result, valid, invalid and disputed) against this
schema and fails unless the schema's verdict equals the ABNF-based check;
with jsonschema 4.26.0 (`Draft202012Validator`) all 84 agree. It
enforces §5.2 items 1 to 3, §5.3, §5.3.1, §5.3.2 (figure and prose),
§5.3.3.1 and RFC 5646 well-formedness for §5.3.3.10. It does not enforce the
case-insensitivity of attribute names (§5.1; the JSON form requires lower
case), duplicate JSON keys (a parser matter), the SHOULD rules of §5.3.3 or
RFC 5646 registry validity.

## The repairs

Every derived figure equals its verbatim figure token for token after these
replacements, and nothing else (the runner checks it; `grammar_files` in
`../examples/expected.yaml` lists them):

| figure | repair | why |
|---|---|---|
| 5-1 | `spec_chrs` to `spec-chrs` | F-03 |
| 6-1 | R1 `/=` to `=/`; R2 `"˜"` (U+02DC) to `"~"`; R3 `cf. [RFC5646]` to the prose value `<Language-Tag, RFC 5646 section 2.1>` | F-01, F-04, F-05 |
| 6-2 | R1 `/=` to `=/`; R2 the four `=` at the start of `pct-encoded`'s continuation lines removed; R3 `str_wo_special`, `str_w_special`, `spec_chrs` to hyphenated names | F-01, F-02, F-03 |
| 6-3 | R1 `sw_edition`, `target_sw`, `target_hw`, `spec_chrs` to hyphenated names | F-03 |

A strict RFC 5234 parse of the verbatim files reports 2 errors in Figure 5-1,
9 in Figure 6-1, 17 in Figure 6-2 and 8 in Figure 6-3 (each listed with its
line in `grammar_files.*.verbatim_parse_errors`); the derived files parse with
none.

## Where the printed ABNF, the prose and the pseudocode disagree

Finding numbers are the ones `../examples/expected.yaml` and
`../examples/README.md` use; each names the fixtures that show it.

**The figures are not valid ABNF as printed.**

- **F-01.** Figures 6-1 and 6-2 introduce seven alternatives of
  `component-list` with `/=`. RFC 2234 section 3.3 spells incremental
  alternatives `=/` (its own grammar: `defined-as = *c-wsp ("=" / "=/")
  *c-wsp`).
- **F-02.** Figure 6-2's `pct-encoded` has four continuation lines that
  begin with `=` (L1010-1013, p. 17). No ABNF element begins with `=`.
- **F-03.** Rule names with underscores (`spec_chrs`, `str_wo_special`,
  `str_w_special`, `sw_edition`, `target_sw`, `target_hw`); RFC 2234 section
  2.1 allows letters, digits and hyphens.
- **F-04.** Figure 6-1's `unreserved` ends with `"˜"`, U+02DC SMALL TILDE,
  not the ASCII tilde; a char-val may hold only %x20-21 and %x23-7E. The
  ASCII tilde is meant: §6.1.3.3.7 says "The original v2.2 URI syntax allows
  tildes to appear without encoding", and the CPE 2.2 grammar lists `"~"`
  (F-07). A tool built from the printed figure would reject §6.1.3.3.7's own
  URI `cpe:/a:foo~bar:big%7emoney_2010`.
- **F-05.** Figure 6-1's `LANGTAG = cf. [RFC5646]` is a reference, not a rule.

**Figure 5-1 against the prose of §5.3.2** (the two differ in exactly two
families of strings; `figure-5-1-avstring.derived.abnf` PART 3 proves it by
writing the intersection out):

- **F-10.** Figure 5-1 accepts values made only of special characters:
  `*`, `**`, `?*`, `*?`, `??*`, `*??`. The prose forbids them: "A single
  asterisk MUST NOT be used by itself as an attribute value." "The asterisk
  MUST NOT be used more than once in sequence." and a special character only
  "at the beginning of an otherwise non-empty value string, and/or at the end
  of the string". (Fixtures AV-DSP-01 to 04.)
- **F-11.** Figure 5-1 rejects a quoted hyphen followed by special characters
  (`\-?`, `\-*`) because its `body` excludes one quoted hyphen even when
  something follows; it accepts `?\-`. The prose forbids only "A quoted
  hyphen MUST NOT be used by itself as a value string." (AV-DSP-05.)

**The figures against the prose elsewhere.**

- **F-14.** §5.3.3.10 allows any valid RFC 5646 tag ("Although any valid
  language tag MAY be used, only tags containing language and region codes
  SHOULD be used."); Figures 6-2 and 6-3 admit only `language ["-" region]`
  with a 2 or 3 letter language. A valid WFN with `zh\-Hant\-TW` binds to a
  formatted string Figure 6-3 rejects. (BIND-03, FS-NEG-08.)
- **F-16.** §5.3.2 item 4: "A single question mark MAY be used by itself as
  an attribute value." Figure 6-2 (`str_w_special` needs a character that is
  not special) and Figure 6-3 (`avstring` likewise) cannot express it.
  (BIND-04, URI-EDGE-03, FS-NEG-12.)
- **F-12.** §5.3 item 2 points to "the per-attribute value restrictions
  specified in Section 5.5.3"; there is no 5.5.3, the restrictions are in
  5.3.3.
- **F-13** (a reading, not a contradiction in the grammar). §5.3.3.1: "The
  part attribute SHALL have one of these three string values:". Figure 6-1
  allows an empty part and Figure 6-3 a logical one, so the library reads the
  sentence as restricting string values only.

**The figures against the pseudocode.**

- **F-15.** `bind_to_URI` writes `-` for `language=NA`, but `lang = LANGTAG /
  empty` in Figures 6-1 and 6-2 excludes it, so the procedure produces URIs
  that break section 4 item 3 ("it MUST produce URIs that adhere to the
  syntax rules specified in Figure 6-1"). (BIND-02, URI-NEG-08.)
- **F-16** (above): `bind_to_URI` writes `%01` and `bind_to_fs` writes `?`
  for a lone question mark, forms the preferred grammars reject.
- **F-17.** `process_quoted_chars` has a case for a quoted underscore; Figure
  5-1 does not allow `\_` and `pct_encode` has no case for `_`.
  (AV-NEG-10, BIND-NEG-02.)
- **F-21.** `add_quoting` accepts an embedded run of question marks (`a??b`)
  that Figures 5-1 and 6-3 reject; `decode` rejects the URI form. (AV-NEG-03,
  FS-NEG-05, URI-NEG-11.)
- **F-22.** `decode` raises an error on percent forms that Figure 6-1 allows
  (`%2d`, `%07`, an embedded `%01` or `%02`), and `unbind_URI` reads any
  edition that starts with an unencoded tilde as packed (undefined for
  `~a~b`), against §6.1.1's MUST to accept every Figure 6-1 URI. The
  specification's own examples §6.1.3.3.6 and §6.1.3.3.8 are Figure 6-1 URIs
  that it says raise errors.
- **F-23.** Both unbinding procedures return `*` and `**` (which Figure 5-1
  accepts and the prose forbids); a lone `*` string then reads back as ANY.
- **F-11** (above): Figures 6-2 and 6-3 accept the bound forms `-%01` and
  `-?`, and both unbinding procedures produce `\-?`, which Figure 5-1 rejects.
- **F-24 and F-35.** Neither unbinding procedure enforces the field count, the
  prefix, the part values or the quoting that Figures 6-1 to 6-3 require; the
  text calls its checking limited, yet also requires implementations to give
  the pseudocode's result.

**Case (F-06).** RFC 2234 makes quoted strings case-insensitive, so every
figure accepts `CPE:/`, `CPE:2.3:`, a part `A` and upper-case hex. The XML
schema is case-sensitive; `unbind_URI` lower-cases every component (Appendix
B, Release 2: "Ensured that uppercase letters are transformed to lowercase in
unbind_URI."), `unbind_fs` does not, so `cpe:2.3:A:...` unbinds to a part
`A` that §5.3.3.1 forbids. The figures' authors most likely meant the
case-sensitive reading; the text never says so.

**The XML schema against the figures (F-08).** §6 calls the XML schema "the
authoritative XML binding definition". Its `cpe23Type` agrees with a
case-sensitive reading of Figure 6-3 on all 73 formatted strings in the
fixtures. Its `cpe22Type`,
`[c][pP][eE]:/[AHOaho]?(:[A-Za-z0-9\._\-~%]*){0,6}`, differs from Figure 6-1
on 6 of the 53 URIs: it accepts a bare `%` (`cpe:/a:foo%7`), a `-` in the
language component, and `cPE:/` but not `CPE:/`, and it never checks the
language tag. The report does not say which governs when they disagree.

**Figure 6-1 against the CPE 2.2 grammar it reproduces (F-07).** §6.1.1:
"The syntax of legal CPE v2.2 URIs is specified in Appendix A of [CPE22]. For
ease of reference it is shown in Figure 6-1, using ABNF notation
[RFC2234]." Appendix A of the CPE 2.2 specification is a BNF, not ABNF, and
differs in substance: its string is `( ALPHA | DIGIT | PUNC ) +` with
`PUNC ::= ( "." | "_" | "-" | "~" | "%" )`, so a bare `%` is a legal 2.2
character where Figure 6-1 allows `%` only before two hex digits; and its
`component-list` has no alternative with the part alone (`cpe:/a`), which
Figure 6-1 adds. Read from the archived copy
`https://web.archive.org/web/20110727091530id_/http://cpe.mitre.org/files/cpe-specification_2.2.pdf`
(38 pages, SHA-256
`e3a3a806b9ac0b7d6dc941ea741519c8669ff8b944e341bb4179ae1b4745a61d`; the
archive's SHA-1 matches its captures from 2009 to 2011), Appendix A p. 28.
That copy is © The MITRE Corporation and is not held here; the two grammar
lines are quoted for comparison only.

**Other observations (not contradictions).** Figure 6-2 defines `special` and
never uses it. Figures 5-1, 6-1 and 6-3 redefine the core rules `ALPHA`,
`DIGIT`, `DQUOTE` and (6-1) `HEXDIG` with the meaning RFC 2234 gives them.
Figure 6-3's `ALPHA` is commented `; a-z` but covers A to Z too. §5.3.2's
"printable Unicode Transformation Format-8 (UTF-8) characters with
hexadecimal values between x00 and x7F" names a range that includes code
points that are not printable; Figure 5-1 admits only %x21-7E.

## Judgement calls for the reviewer

1. **The XML schema is committed.** It is not printed in the report, but §6
   names it as the authoritative definition of acceptable bound names, which
   makes it the specification's own schema in the FX-1 sense. Provenance:
   the URL §6 prints redirected to
   `https://csrc.nist.gov/schema/cpe/2.3/cpe-naming_2.3.xsd`, which returned
   HTTP 200 on 2026-10-19: 2254 bytes, ASCII, CRLF line ends, its `appinfo`
   giving version 2.3 and date 2011-07-29. The bytes are unchanged (CRLF
   kept). The file carries no licence or copyright statement; it is published
   by NIST with the SCAP schemas. If the library prefers not to hold it, delete
   it and record the URL and digest instead; the runner then needs a copy in
   `.cache/` (a one-line change of path).
2. **Readings P1 to P4** of the §5.3.2 prose
   (`figure-5-1-avstring.derived.abnf`, PART 2): a leading or trailing group
   of special characters is a run of `?` or one `*`; a value made only of
   special characters is allowed only when it is one or more `?` (`??` by
   itself is not explicitly addressed); item 6 forbids `\-` only as the whole
   value; and the escape character may precede only punctuation, itself or a
   special character, as in Figure 5-1 (the prose does not say).
3. **Language checks are RFC 5646 well-formedness** (the section 2.1
   production). RFC 5646 "valid" also requires the IANA subtag registry, which
   is not consulted.
4. **Repairs are minimal**: no repair changes what a grammar means except
   F-04's tilde, which restores the evident intent. In particular the
   case-insensitivity of quoted strings is kept, and the derived files carry
   the figures' gaps (F-14, F-15, F-16) unchanged.
5. **The WFN JSON shape is the library's.** §5.1 says the WFN "is not intended
   to be a data format"; the JSON Schema exists for test harnesses only and
   must never be cited as a CPE format.
