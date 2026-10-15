---
record: ecma-427
kind: examples
title: "ecma-427: examples, derived fixtures and expected results"
extracted: "2026-10-15"
reviewed_by: ""
---

# ECMA-427 examples and test vectors

Contains text from ECMA-427 1st edition, © Ecma International 2025, reproduced under the Ecma copyright notice; full notice in distilled/README.md

Every example that ECMA-427 1st edition (December 2025) prints, copied byte for
byte, plus 44 fixtures the library derived from the text. Each fixture has an
expected result worked out by hand from the standard and the actual result of
two tools, jsonschema 4.26.0 and packageurl-python 0.17.6.
`run-fixtures.derived.py` reproduces every actual result and fails if one
changes.

Source: `.cache/ecma-427.bin`, SHA-256
`037180df99e7d7c26d910dc3adb3fa07c4fb787cc4bd29e43634de3802313825`, 40 pages,
read through `pdftotext -layout` (`.cache/ecma-427.txt`). Every example was
checked against the rendered PDF pages (printed pp. 3, 7, 8, 21). The
validation schema is the Annex A schema as published at purl-spec tag v1.0.0
(SHA-256 `b8988773ac628fe97a33fccabaf19bb45262bb4bd56002fa3d0ab3be72dae983`),
the bytes the schema artifact (`distilled/schema/`) is to commit and compare
with the printed Annex A. Nothing here depends on that artifact.

All the examples in Clauses 5 and 6 are labelled "(Informative)". The
standard never states the parse of any of them, so every expected parse here
is derived: the normative rules of Clause 5 applied to an informative example.

## Files

| path | what |
|---|---|
| `expected.yaml` | the index: all 54 fixtures, each with its source locator (or how it was derived), the rule a negative breaks (verbatim, with locator, and since pass 3 the `requirements.yaml` ids it breaks, in `breaks`), the expected result, the actual jsonschema and packageurl-python results, and a comparison. Also holds the 63 rules it cites by id, quoted verbatim, each with its `requirements.yaml` ids (pass 3), and the parsing procedure P1 to P9. Derived PURL strings live here, inline |
| `verbatim/` | the 10 source examples, byte for byte, each file ending in one LF that is not part of the example: Clause 5 Examples 1 to 3 (PURL strings), 6.1 Examples 1 to 3 (type strings), 6.2 Examples 1 and 2 (type names), and the two `examples` arrays inside Annex A as `.json-fragment` files (the printed lines with their common indentation removed) |
| `type-definitions/` | 23 library-made PURL type definitions. `minimal-valid.derived.json` uses only what Annex A requires; each of the other 22 is that file with exactly one change, named by the JSON Pointer in its `mutation` field |
| `run-fixtures.derived.py` | the reproduction script (library-written, no Ecma text) |

Files the library wrote carry `.derived.` before the extension; files under
`verbatim/` are copies of source text and do not. `README.md` and
`expected.yaml` keep the names the extraction brief gave them.

## Counts

| group | ids | n | expected |
|---|---|---:|---|
| source examples | `SRC-*` | 10 | PURLs accept; type strings, type names and Annex A arrays valid |
| derived PURL positives | `PURL-POS-01` to `09` | 9 | accept |
| derived PURL negatives | `PURL-NEG-01` to `10` | 10 | reject, except `NEG-06` (empty qualifier value: accept, pair treated as absent) |
| PURL edge cases | `PURL-EDGE-01`, `02` | 2 | accept (judgement call); unspecified |
| type definition, positive | `TD-POS-01` | 1 | valid |
| type definitions, one Annex A constraint broken | `TD-NEG-01` to `13` | 13 | invalid |
| regex and URI formats | `TD-FMT-01` to `04` | 4 | invalid, except `FMT-03` (valid) |
| pattern semantics | `TD-PAT-01` | 1 | invalid |
| schema-valid but in conflict with the prose | `TD-GAP-01` to `04` | 4 | valid under Annex A |

## How the expected results were derived

The 1st edition defines seven components and their separators but gives no
parsing algorithm and no procedure for building a canonical string.
`expected.yaml` therefore states an ordering of the stated rules (P1 to P9)
and cites, for every step of every parse, the rule ids it applies. The
ordering is safe because 5.4 requires every separator character used as data
to be percent-encoded; the colon is the one character 5.4 never encodes, and a
type may not contain one.

A string that breaks a rule is expected to be rejected, because Clause 2 says
"Invalid PURLs that fail to conform to the specification shall be identified
and rejected by any conforming implementation." The text grants exactly two
leniencies: slashes after `pkg:` are removed (5.6.1), and an empty qualifier
value is the same as no pair (5.6.6). Nothing else is forgiven, so an
uppercase qualifier key, a duplicate key, a `..` subpath segment, an empty
namespace segment and a percent-encoded colon are all expected rejections.

The canonical form is fully fixed by the text only for some strings. The type
is lowercase (5.6.2), leading and trailing slashes "should be stripped"
(5.6.3, 5.6.4, 5.6.7), and 5.4 fixes which characters are encoded. The text
states **no qualifier order**, and although Clause 2 requires "normalisation
and equivalence rules", no clause states them. So the canonical string of any
PURL with two or more qualifiers is not determined (`SRC-C5-EX1` is
"defined, except qualifier order"; `PURL-POS-04` is "not defined"). The case
of percent-encoding hex digits is not stated either (`PURL-POS-08`).

Type-definition fixtures are judged against Annex A read the way the prose
describes it: regular expressions in the ECMA-262 dialect (6.5.5, 6.6.3 and
the other "Permitted characters" subclauses) and `format` asserted (6.4.2,
6.12). Each was run through `Draft7Validator` twice, without and with
`format_checker=Draft7Validator.FORMAT_CHECKER`.

## Where a tool differs from the expected result (13 fixtures)

Each row has a `finding` in `expected.yaml`. packageurl-python tracks the
purl-spec repository, whose main branch carries the 2nd edition text, so
these are findings about the 1st edition and the tool, not fixture errors.

**packageurl-python 0.17.6** (`PackageURL.from_string`, then `to_string`)

| fixture | string | expected | packageurl-python |
|---|---|---|---|
| `PURL-NEG-03` | `pkg:my_type/foobar@12.3.1` | reject (5.6.2 has no underscore in a type) | accepts; its type check allows `_` |
| `PURL-NEG-04` | `...?Arch=i386&distro=jessie` | reject (keys are lowercase, 5.6.6) | lowercases the key, accepts |
| `PURL-NEG-05` | `...?arch=i386&distro=jessie&arch=amd64` | reject (keys unique, 5.6.6) | accepts, keeps the last value, drops `arch=i386` silently |
| `PURL-NEG-07` | `...#lib/../index.js` | reject (no `..` segment, 5.6.7) | drops the `..`, giving `#lib/index.js`, which is not even what resolving it would give |
| `PURL-NEG-08` | `pkg:maven/org.apache//xmlgraphics/...` | reject (no empty segment, 5.6.3) | drops the empty segment, accepts |
| `PURL-NEG-10` | `...@1%3A7.50.3-1...` | reject (colon never encoded, 5.4) | decodes `%3A`, accepts |
| `PURL-POS-08` | `...?repository_url=https:%2F%2Frepo.example.com%2Fmaven2` | canonical keeps `%2F` (5.4) | parses correctly, but `to_string` writes the slashes unencoded |
| `PURL-POS-09` | `pkg:npm/FooBar@12.3.1` | name keeps its case (Clause 5 alone) | lowercases npm names, a purl-spec type-definition rule outside this edition |

It agrees on the other 15 PURL fixtures that have a defined result. Worth knowing
even so: on `PURL-POS-04` it sorts qualifier keys, one possible canonical
order that the 1st edition does not choose; on `PURL-EDGE-01` it reads
`pkg://example.com/npm/...` as type `example.com`, as derived here; on
`PURL-EDGE-02` it rejects `PKG:` (the text allows either reading).

**jsonschema 4.26.0** (`Draft7Validator`; `uri` checked through rfc3987
1.3.8, `regex` through Python `re.compile`)

| fixture | expected | without format checker | with format checker |
|---|---|---|---|
| `TD-FMT-01` `default_repository_url` without a scheme | invalid | valid (format not asserted) | invalid |
| `TD-FMT-02` `permitted_characters` `[a-z` | invalid | valid (format not asserted) | invalid |
| `TD-FMT-03` `permitted_characters` `(?<name>[a-z]+)` | valid (ECMA-262 named group) | valid | **invalid**: Python `re` does not know the syntax |
| `TD-FMT-04` `permitted_characters` `(?i)^[a-z0-9.-]+$` | invalid (not ECMA-262) | **valid** | **valid**: Python accepts inline flags |
| `TD-PAT-01` type `fixture` plus a newline | invalid (ECMA-262 `$` is end of input) | **valid** | **valid**: Python `re.search` lets `$` match before a final newline |

The ECMA-262 side of every regex claim was confirmed with Node v22.23.2
(`ecma262_node` in `expected.yaml`); the schema's own three patterns compile
in ECMA-262 with and without the `u` flag. Two smaller observations:
jsonschema reports a `$ref` reached through `allOf` at the referenced keyword
(schema path `/properties/namespace_definition/allOf/0/type`), and
`TD-NEG-11` and `TD-NEG-12` each produce two errors for one change.

As a cross-check every PURL fixture was also validated against the Annex A
`examples` item schema. Its pattern, `^pkg:[a-z][a-z0-9-\.]+/.*$`, looks only
at the scheme and type: it rejects valid non-canonical forms (`pkg://`, an
uppercase type) and accepts most invalid strings (`PURL-NEG-04`, `05`, `07`,
`08` and `10`).

## For consumers that compare PURLs as strings

tmodel keeps PURLs as opaque strings (ADR-0010). The fixtures show strings
that name the same package under the 1st edition but are not equal as
strings: `pkg://` and `pkg:///` (`PURL-POS-01`, `02`), an uppercase type
(`POS-03`), reordered qualifiers (`POS-04`, where the standard does not even
say which order is canonical), a doubled slash (`POS-07`), and an empty
qualifier value (`NEG-06`). Two implementations can also disagree on the
canonical string itself: name case once type definitions apply (`POS-09`)
and encoding of URL-valued qualifiers (`POS-08`).

## Where the source is inconsistent or unclear

1. **No parsing algorithm, no qualifier order, no equivalence rules.**
   Clause 2 requires "strict adherence to normalisation and equivalence
   rules", but no clause states them, and 5.6.6 says nothing about order.
2. **Authority prohibition against the `pkg://` leniency.** Clause 5: "A PURL
   shall not contain a URL Authority, i.e. there is no support for username,
   password, host and port components." 5.6.1: parsers "shall ignore and
   remove all such '/' characters". After the removal no authority is left to
   detect: `pkg://example.com/npm/foobar@12.3.1` parses with type
   `example.com` (`PURL-EDGE-01`), and `pkg://user@example.com/...` is rejected
   only because `@` is not a type character (`PURL-NEG-09`).
3. **Scheme case.** 5.6.1: "The scheme is a constant with the value "pkg"."
   5.1: "A PURL is a valid URL and URI that conforms to the URL definitions or
   specifications at:", and URI schemes compare without regard to case
   (RFC 3986 section 3.1, cited, not quoted). Nothing says which governs
   `PKG:` (`PURL-EDGE-02`).
4. **Type length.** 5.6.2 sets no minimum, but 6.1 gives "Pattern
   Constraint: ^[a-z][a-z0-9-\.]+$", which needs two characters; the examples
   pattern has the same floor (`TD-NEG-07`).
5. **Table 2 against 6.5 to 6.9.** Table 2 types `namespace_definition`,
   `name_definition`, `version_definition` and `subpath_definition` as
   "Array"; 6.5, 6.6, 6.7 and 6.9 say "Type: Object", as does Annex A
   (`TD-NEG-11`).
6. **Tables 4 to 8 against the subclauses.** Each table types `requirement`
   as "Array"; 6.5.1 and its siblings say "Type: String", as does Annex A
   (`TD-NEG-12`).
7. **`$id` and `$schema` are absent from Clause 6.** Annex A requires `$id`
   and fixes `$schema` to one value; Table 2 lists neither (`TD-NEG-01`,
   `TD-NEG-04`).
8. **A misplaced sentence.** "All items shall be unique." for the
   `qualifiers_definition` array is printed under 6.8.1.7 Native name, a
   string property (`TD-NEG-13`).
9. **`$id` pattern excludes the period** that 5.6.2 and the type pattern
   allow, so a dotted type cannot use the obvious `$id` (`TD-NEG-08`;
   an observation, since nothing says the `$id` must contain the type).
10. **`additionalItems: false`** sits beside a single-schema `items` in
    `qualifiers_definition` (Annex A, p. 23); Draft-07 ignores it there.
11. **The schema cannot check what the prose asks** of examples ("valid,
    canonical PURLs for this package type", 6.10) or of qualifier keys (5.6.6
    syntax): `TD-GAP-01` to `04`.
12. **Annex A points at a moving copy:** "available in electronic form at:
    https://github.com/package-url/purl-spec/blob/main/schemas/purl-type-definition.schema.json"
    (the print wraps the URL after `main/`; rejoined here). The link names a
    branch, and the path no longer exists on it: purl-spec commit `178ec1aa`
    (2025-10-08) renamed the file, and the URL returned HTTP 404 on 2026-10-15
    (see `../schema/README.md`). The stable copy is
    `schemas/purl-type-definition.schema-1.0.json` at the v1.0.0 tag.

## Judgement calls

- **Strict reading.** Non-conforming strings are rejected (Clause 2) except
  under the two stated leniencies; each such negative records the lenient
  alternative in `lenient_reading`.
- **`PURL-EDGE-01`** expected accept (type `example.com`), and
  **`PURL-EDGE-02`** recorded as unspecified rather than forced either way.
- **`PURL-POS-07`**: the doubled slash between namespace and name is read as
  a not-significant leading or trailing slash (5.6.3, 5.6.4), not an empty
  segment; its canonical form rests on a "should". `PURL-NEG-08` puts the
  doubled slash inside the namespace, where the empty-segment rule applies.
- **`PURL-NEG-02`** cannot break only one rule: a percent-encoded type also
  breaks the type character rule and 5.4. All three agree.
- **`PURL-NEG-09`** is rejected by the type character rule, because 5.6.1
  removes the slashes before an authority could be recognised.
- **`PURL-POS-08`**: 5.4 read as requiring a slash inside a qualifier value
  to be encoded (it is data, outside the allowed set); uppercase hex follows
  the RFC 3986 recommendation, which this edition does not state. RFC 3986 is
  not held in this library, so it is cited, not quoted.
- **`PURL-POS-09`**: with no type definitions in this edition, the name keeps
  its case; `case_sensitive` defaults to true (6.6.4).
- **`TD-GAP-01` to `04`** and **`TD-NEG-08`**: where the prose has no rule
  for type definitions, the conflict is marked as inference in
  `prose_agrees`.
- **Annex A is quoted from the electronic v1.0.0 copy**, whose lines equal
  the printed ones apart from display wraps inside long strings.
- The made-up type `fixture` keeps the definitions from being mistaken for
  real ones.

## Reproduce

From the repository root, with Python 3.9 or later:

```sh
python3 -m venv /tmp/ecma427-venv    # any directory outside the repository
/tmp/ecma427-venv/bin/pip install jsonschema==4.26.0 packageurl-python==0.17.6 PyYAML==6.0.3 rfc3987==1.3.8

# the source, never committed (CLAUDE.md); needed for the verbatim checks
mkdir -p .cache/purl-spec
curl -L -o .cache/ecma-427.bin https://ecma-international.org/wp-content/uploads/ECMA-427_1st_edition_december_2025.pdf
shasum -a 256 .cache/ecma-427.bin   # 037180df99e7d7c26d910dc3adb3fa07c4fb787cc4bd29e43634de3802313825
pdftotext -layout .cache/ecma-427.bin .cache/ecma-427.txt

# the Annex A schema as published at purl-spec tag v1.0.0 goes in
# .cache/purl-spec/schema-1.0-at-v1.0.0.json, or pass any copy with --schema;
# the script refuses bytes whose SHA-256 is not b8988773...dae983

/tmp/ecma427-venv/bin/python -I records/other/ecma-427/distilled/examples/run-fixtures.derived.py
/tmp/ecma427-venv/bin/python -I records/other/ecma-427/distilled/examples/run-fixtures.derived.py --json
```

The first command checks everything and prints
`54 fixtures; 13 where a tool differs from the expected result (each has a finding); 0 problems`.
Before comparing results it checks that each `verbatim/` file and each quoted
rule occurs verbatim in `.cache/ecma-427.txt`, that each Annex A quote occurs
line for line in the schema, and that each type-definition fixture differs
from `minimal-valid` only at its stated pointer. The second prints the
recomputed results as JSON. With `node` on `PATH` the ECMA-262 cross-checks
run too; without it they are skipped and reported.

Versions recorded in this run: Python 3.13.9, jsonschema 4.26.0 (referencing
0.37.0, jsonschema-specifications 2025.9.1), rfc3987 1.3.8 (makes the `uri`
format checkable), packageurl-python 0.17.6, PyYAML 6.0.3, Node v22.23.2.
The cached text rendering came with the brief; pdftotext (Poppler) 26.07.0 is
the version installed here.
The brief named jsonschema 4.23.0, but the shared environment was upgraded to
4.26.0 before any result was recorded, so every result here is from 4.26.0.
The script notes any version that differs from `tools` in `expected.yaml`.

`expected.yaml` parses identically with the library's reader and PyYAML
(every scalar is a quoted string or a block scalar; there are no flow
mappings):

```sh
python3 -I -c "import sys, yaml; sys.path.insert(0, 'bin'); from _yaml import parse; t = open('records/other/ecma-427/distilled/examples/expected.yaml', encoding='utf-8').read(); assert parse(t) == yaml.safe_load(t); print('identical')"
```

## Not transcribed

| source | why |
|---|---|
| Clause 5, `scheme:type/namespace/name@version?qualifiers#subpath` (p. 2) | the syntax template, not an example; it has no values |
| 5.6.1, `'pkg://'` (p. 5) | a fragment inside the rule; used to derive `PURL-POS-01` and `02` |
| 5.1, `file://`, `https://`, `http://`, `ftp://`, `git://`, `svn://`, `hg://` (pp. 3 to 4) | URL schemes the text says are not PURL types; fragments, not PURLs |
| Table 1 ("maven, npm, nuget, gem, pypi, etc."), Clause 1 ("maven, pypi or npm"), 6.5.8 ('groupId', 'scope') | words inside descriptions, not labelled examples; the labelled type examples are 6.1 and 6.2 |
| the Annex A schema itself | it is the schema artifact (`distilled/schema/`), not an example; it is used here only to validate |
