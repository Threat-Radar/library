---
record: ecma-427
kind: schema
title: "ecma-427: schemas (one verbatim, one derived)"
extracted: "2026-10-15"
reviewed_by: ""
---

# ecma-427: schemas

Contains text from ECMA-427 1st edition, © Ecma International 2025, reproduced under the Ecma copyright notice; full notice in distilled/README.md

This README is derived: the library wrote it. Of the files beside it, only
`purl-type-definition.schema-1.0.json` carries the source's own bytes.

## What ECMA-427 ships, and what it does not

ECMA-427 1st edition (December 2025) contains exactly one formal artifact: the
**Annex A (normative)** JSON Schema for *PURL type definition* documents (JSON
Schema draft-07, printed pp. 19 to 25). It has **no grammar for the PURL
string**: Clause 5 gives the syntax as prose bullets (§5.1 to §5.6.7), with no
ABNF, BNF or regular expression. This directory therefore holds the Annex A
schema verbatim, and an ABNF for the PURL string that this library derived
from the prose.

## Files

| file | verbatim or derived | source | locator | SHA-256 of the file as written |
|---|---|---|---|---|
| `purl-type-definition.schema-1.0.json` | **verbatim**: bytes unchanged | ECMA-427 Annex A; bytes as published in purl-spec tag `v1.0.0` | Annex A (pp. 19 to 25) | `b8988773ac628fe97a33fccabaf19bb45262bb4bd56002fa3d0ab3be72dae983` |
| `purl.derived.abnf` | **derived**: RFC 5234 ABNF written for this library | ECMA-427 Clause 5 prose | Clause 5 (Table 1), §5.1 to §5.6.7 | `7fecac7342830b59b2d32e353cfc25b3b0a0f0fcebffe7fcfba5edf9bc1ca695` |
| `README.md` | derived (this file) | none | none | not listed: a file cannot state its own digest |

Naming. Upstream m-of-n/library adopted on 2026-10-13 a rule this fork has not
synced yet: a file in `distilled/schema/` that the library wrote carries the
infix `.derived.` before its extension and says "derived" in its first 12
lines, and an unmarked filename asserts that the file is the source's own
bytes. Both files above follow it: the schema is unmarked because it is the
source's bytes; the grammar is marked, and its line 4 reads `DERIVED - not
verbatim; ECMA-427 1st edition defines no grammar`. This README keeps the
conventional index name the scaffold gave it (a judgement call); its title and
its opening lines say it is derived.

The structures and fields these files govern are decomposed one by one in
`../messages.yaml` (13 structures, 65 fields).

## Provenance of `purl-type-definition.schema-1.0.json`

### The link printed in Annex A is dead

Annex A (p. 19) says: "The schema shown below is available in electronic form
at: https://github.com/package-url/purl-spec/blob/main/schemas/purl-type-definition.schema.json"

On 2026-10-15 that URL returned HTTP 404, as did its raw form
(`https://raw.githubusercontent.com/package-url/purl-spec/main/schemas/purl-type-definition.schema.json`)
and the same path at tag `v1.0.0`. The repository history says why: commit
`178ec1aadd72036d201cb84febd39c0321c439a7` (2025-10-08, "Update schema files
filenames and ids #699") renamed that file to
`schemas/purl-type-definition.schema-1.1.json`. The path had already left
`main` when the standard "was adopted by the General Assembly of December
2025" (p. iii). The frozen 1st-edition schema lives at
`schemas/purl-type-definition.schema-1.0.json`, added by commit
`4899f1528f60a3ac13c2bede49f3c202e700f823` (2025-09-19, "Freeze purl-type
schemas for Ecma standard") and last changed by commit
`9c48dff9a56cd977acc4c4ab6ca4eeaccd6738a4` (2025-11-10, "Update must to shall
for ISO standard").

### Where the bytes came from

- Downloaded on 2026-10-15 from
  `https://raw.githubusercontent.com/package-url/purl-spec/v1.0.0/schemas/purl-type-definition.schema-1.0.json`:
  SHA-256 `b8988773ac628fe97a33fccabaf19bb45262bb4bd56002fa3d0ab3be72dae983`,
  byte-identical (`cmp`) to the cached `.cache/purl-spec/schema-1.0-at-v1.0.0.json`.
  The file here is a copy of those bytes.
- Tag `v1.0.0` is a lightweight tag on commit
  `c03cfa02e1c740ab5ff3c54305a950eb32cbff17`; the GitHub release `v1.0.0` was
  published on 2025-12-19. The same path fetched by that commit id gives the
  same SHA-256.
- The git blob id of these bytes, computed locally, is
  `978192667ffbc6dcea4439ef092cff68e5b9577c`, which is the id the GitHub API
  lists for this path both at `v1.0.0` and on `main` (2026-10-15): `main`
  still holds exactly these bytes.
- The schema's own `$id`, `https://packageurl.org/schemas/purl-type-definition.schema-1.0.json`,
  served byte-identical content (same SHA-256) on 2026-10-15.
- `.cache/purl-spec/schema-1.0-at-v1.1.0.json`, the same path at tag `v1.1.0`,
  has the same SHA-256.
- At tag `v1.0.0` the sibling file `schemas/purl-type-definition.schema-1.1.json`
  differs from the 1.0 file in one token only, the root `$id`. Annex A prints
  the `schema-1.0.json` `$id`, so the 1.0 file is the only match.

File facts: 10,732 bytes, 327 lines, ASCII only, LF line ends with a final
newline, no tabs, no trailing spaces. It is a valid draft-07 schema:
`Draft7Validator.check_schema` passes and the full `iter_errors` list against
the draft-07 metaschema is empty (jsonschema 4.26.0).

### Proof that it equals the printed Annex A, token for token

Method. Lines 1316 to 1691 of `.cache/ecma-427.txt` (`pdftotext -layout`)
hold the printed schema. The six page-footer lines (pp. 19 to 24) and the form
feeds are page furniture and are dropped. A PDF wrap inside a string puts the
rest of the string at column 0, while every JSON line of the print is
indented, so a wrap is joined with nothing after a hyphen and with one space
otherwise. The two hyphen wraps, `purl-type-` / `definition.schema-1.0.json`
(in `/properties/$schema/const`) and `[a-z0-9-]+-` / `definition\\.json$` (in
`/properties/$id/pattern`), were checked on the rendered image of printed
p. 20: each line breaks after a hyphen that belongs to the text.

| check | result |
|---|---|
| token for token (925 tokens each: 541 punctuation, 373 strings, 11 literals) | identical, 0 mismatches |
| PDF wraps inside strings | 31: 29 at a space, 2 after a hyphen; no continuation line is indented |
| parsed values, key order kept (`object_pairs_hook=list`) | equal |
| all whitespace removed, character for character | equal (7,236 characters each) |
| negative controls: `minItems` 1 changed to 2; a period added to one description; the sibling `schema-1.1.json` at tag `v1.0.0` | each one detected (exactly one mismatching token) |

The non-layout rendering `.cache/ecma-427.raw.txt` cannot be used for this
check: it deletes hyphens at line ends (`purl-typedefinition.schema-1.0.json`)
and reorders lines on printed pp. 24 and 25.

To reproduce (from the repository root; Python 3 standard library only):

```sh
python3 -I - .cache/ecma-427.txt records/other/ecma-427/distilled/schema/purl-type-definition.schema-1.0.json <<'EOF'
import json, re, sys
foot = re.compile(r"^\s*(\d+\s+)?© Ecma International 2025(\s+\d+)?\s*$")
lines = open(sys.argv[1], encoding="utf-8").read().split("\n")[1315:1691]
pdf = "\n".join(l for l in (x.replace("\f", "") for x in lines) if not foot.match(l))
src = open(sys.argv[2], encoding="utf-8").read()
# A PDF wrap puts the rest of a string at column 0, while JSON lines are
# indented: rejoin with nothing after '-', otherwise with one space.
joined = re.sub(r"\n(?=\S)", " ", re.sub(r"-\n(?=\S)", "-", pdf))
tok = re.compile(r'"(?:[^"\\]|\\.)*"|[{}\[\]:,]|-?\d+(?:\.\d+)?|true|false|null')
a, b = tok.findall(joined), tok.findall(src)
print("1. token for token:", a == b, f"({len(a)} and {len(b)} tokens)")
print("2. equal as parsed JSON, key order kept:",
      json.loads(joined, object_pairs_hook=list) == json.loads(src, object_pairs_hook=list))
nows = lambda s: re.sub(r"\s+", "", s)
print("3. equal with all whitespace removed:", nows(pdf) == nows(src))
EOF
```

Output on 2026-10-15:

```
1. token for token: True (925 and 925 tokens)
2. equal as parsed JSON, key order kept: True
3. equal with all whitespace removed: True
```

Run against the `schema-1.1.json` sibling, all three print `False`.

### Licence of the verbatim file

The schema is "Software" in the sense of the Software License printed on p. 31:
"All Software contained in this document ("Software") is protected by
copyright and is being made available under the "BSD License", included
below." Its condition 1 requires that redistributions of source code retain
the copyright notice, the list of conditions and the disclaimer. A JSON file
cannot carry a comment without changing its bytes, so they are reproduced
here, beside the file.

Copyright notice, as printed in the page footers of ECMA-427, p. 31
included: © Ecma International 2025

The Software License of p. 31, verbatim (lines the PDF wrapped are joined):

```text
Software License
Ecma International
Rue du Rhone 114
CH-1204 Geneva
Tel: +41 22 849 6000
Fax: +41 22 849 6001
Web: https://ecma-international.org/

All Software contained in this document ("Software") is protected by copyright and is being made available under the "BSD License", included below. This Software may be subject to third party rights (rights from parties other than Ecma International), including patent rights, and no licenses under such third party rights are granted under this license even if the third party concerned is a member of Ecma International. SEE THE ECMA CODE OF CONDUCT IN PATENT MATTERS AVAILABLE AT https://ecma-international.org/memento/codeofconduct.htm FOR INFORMATION REGARDING THE LICENSING OF PATENT CLAIMS THAT ARE REQUIRED TO IMPLEMENT ECMA INTERNATIONAL STANDARDS.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
3. Neither the name of the authors nor Ecma International may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE ECMA INTERNATIONAL "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL ECMA INTERNATIONAL BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
```

The bytes themselves were fetched from the purl-spec repository, which
distributes the same file under the MIT License. Its notice, from `LICENSE` at
tag `v1.0.0` (SHA-256 `24fb7204fd3c9396c9d83533448cb988e8e86d6f598d1ab51c6d2e5d7e42bcb1`),
verbatim:

```text
# SPDX-License-Identifier: MIT
# Copyright (c) the purl authors
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
# Visit https://github.com/package-url/purl-spec and https://packageurl.org for support
```

## Validating a type definition offline

With `jsonschema` installed (this was run with jsonschema 4.26.0, Python
3.13.9), from the repository root:

```sh
python3 -I - records/other/ecma-427/distilled/schema/purl-type-definition.schema-1.0.json my-type-definition.json <<'EOF'
import json, sys
from jsonschema import Draft7Validator
schema = json.load(open(sys.argv[1], encoding="utf-8"))
Draft7Validator.check_schema(schema)
v = Draft7Validator(schema, format_checker=Draft7Validator.FORMAT_CHECKER)
rc = 0
for path in sys.argv[2:]:
    errors = sorted(v.iter_errors(json.load(open(path, encoding="utf-8"))),
                    key=lambda e: list(e.absolute_path))
    print(path.rsplit("/", 1)[-1], "VALID" if not errors else "INVALID")
    for e in errors:
        print("  ", "/".join(map(str, e.absolute_path)) or "(root)", e.message)
    rc |= bool(errors)
sys.exit(rc)
EOF
```

It needs no network: every `$ref` in the schema is local
(`#/definitions/...`) and jsonschema bundles the draft-07 metaschema. The exit
status is 0 only if every file is valid.

Two cautions about `format`:

- Draft-07 makes format checking optional: "Implementations MAY support the
  "format" keyword as a validation assertion." (draft-handrews-json-schema-validation-01
  §7.2, the JSON Schema reference in the Bibliography). Without
  `format_checker`, jsonschema ignores `format` entirely. With it, `uri` is
  checked only when `rfc3987` (here 1.3.8) or `rfc3986-validator` is
  importable, and is silently skipped otherwise.
- `format: regex` is checked with Python's `re`, not the ECMA-262 dialect that
  §6.5.5 names. A pattern can pass here and fail in ECMA-262, or the reverse.

Example run on 2026-10-15, over the 35 type definitions in purl-spec `v1.0.0`
(`types/*-definition.json`; purl-spec data, not part of ECMA-427): 33 valid,
2 invalid. Output for three of them:

```
maven-definition.json VALID
bazel-definition.json INVALID
   $schema 'https://packageurl.org/schemas/purl-type-definition.schema-1.0.json' was expected
   version_definition/requirement 'required' is not valid under any of the given schemas
julia-definition.json INVALID
   version_definition 'requirement' is a required property
```

`bazel-definition.json` gives `$schema` as
`https://packageurl.org/schemas/purl-type.schema-1.0.json` and sets
`version_definition.requirement` to `required`, which §6.7.1 and Annex A do
not allow; `julia-definition.json` has a `version_definition` with no
`requirement`.

## Annex A schema defects (confirmed)

All six candidates set for this pass were checked against the text and the
page images, and all six hold. Each was also probed with jsonschema 4.26.0
against the verbatim schema. Numbers D1 to D6 are the ones `../messages.yaml`
cites in its `flags`.

**D1. `$id` is required by Annex A but absent from Clause 6.**
Annex A, `/required`: `"required": [ "$id", "type", "type_name",
"description", "repository", "namespace_definition", "name_definition",
"examples" ]`, and `/properties/$id` has `"pattern":
"^https:\\/\\/packageurl\\.org/types/[a-z0-9-]+-definition\\.json$"`. Table 2
(p. 7) lists twelve properties, from `type` to `reference_urls`, and neither
`$id` nor `$schema`; no subclause of Clause 6 has a `Location: /$id`. Effect:
a type definition written from Clause 6 alone fails Annex A. Probe: dropping
`$id` from a valid document gives `'$id' is a required property`.

**D2. `additionalItems` is used with a single-schema `items`, so it does
nothing.** Annex A, `/properties/qualifiers_definition`: `"type": "array",
"additionalItems": false, "uniqueItems": true, "items": {` an object schema `}`.
Draft-07 (draft-handrews-json-schema-validation-01 §6.4.2): "If "items" is an
array of schemas, validation succeeds if every instance element at a position
greater than the size of "items" validates against "additionalItems"." and
"Otherwise, "additionalItems" MUST be ignored, as the "items" schema (possibly
the default value of an empty schema) is applied to all elements." Probe:
with and without the keyword, two good items are valid and one bad item is
invalid; the verdicts never change. Harmless, but a reader may think it
restricts something.

**D3. `use_repository` has a default in Annex A and none in Clause 6.**
Annex A, `/properties/repository/properties/use_repository`: `"type":
"boolean", "default": false`. §6.4.1 prints "Location:
/repository/use_repository", "Property: use_repository (Required)", "Type:
Boolean" and "true if this PURL type uses a public package repository.", and
no `Default Value` line, while §6.5.6, §6.6.4, §6.7.4 and §6.9.4 print
"Default Value: true" for `case_sensitive`. The property is also required
(Table 3; Annex A `/properties/repository/required`), so the default can never
apply to a valid document.

**D4. The `type` pattern needs two characters; §5.6.2 allows one.**
§6.1: "Pattern Constraint: ^[a-z][a-z0-9-\.]+$" (Annex A: `"pattern":
"^[a-z][a-z0-9-\\.]+$"`), and the `examples` item pattern of §6.10 and Annex A
is `^pkg:[a-z][a-z0-9-\.]+/.*$`. §5.6.2 says only "The package type shall be
composed only of ASCII letters and numbers, period '.', and dash '-'." and
"The type shall start with an ASCII letter.", with no minimum length. So a
one-letter type such as `pkg:a/foobar` is a valid PURL (the grammar here
accepts it), but no type definition can exist for it. Probe: `"type": "a"`
gives `'a' does not match '^[a-z][a-z0-9-\\.]+$'`, and the example
`pkg:a/name` fails the items pattern.

**D5. The property tables say "Array" where the subclauses and Annex A say
object or string.** Nine cells, each confirmed on the page image (pp. 7, 9,
11, 13, 15, 16):

| table, row | table says | subclause says | Annex A says |
|---|---|---|---|
| Table 2, `namespace_definition` | Array | Object (§6.5) | `"type": "object"` |
| Table 2, `name_definition` | Array | Object (§6.6) | `"type": "object"` |
| Table 2, `version_definition` | Array | Object (§6.7) | `"type": "object"` |
| Table 2, `subpath_definition` | Array | Object (§6.9) | `"type": "object"` |
| Table 4, `requirement` | Array | String (§6.5.1) | `"type": "string"` |
| Table 5, `requirement` | Array | String (§6.6.1) | `"type": "string"` |
| Table 6, `requirement` | Array | String (§6.7.1) | `"type": "string"` |
| Table 7, `requirement` | Array | String (§6.8.1.2) | `"type": "string"` |
| Table 8, `requirement` | Array | String (§6.9.1) | `"type": "string"` |

The other "Array" cells (`qualifiers_definition`, `examples` and
`reference_urls` in Table 2, `normalization_rules` in Tables 4, 5, 6 and 8)
agree with their subclauses and Annex A. Probe: a `namespace_definition`
written as an array, as Table 2 says, fails with `is not of type 'object'`;
a `requirement` written as an array fails with `is not of type 'string'`.

**D6. §6.8.1.7 says "All items shall be unique." under a string property.**
§6.8.1.7 prints "Location: /qualifiers_definition/[]/native_name", "Type:
String", "The equivalent native name for this qualifier key." and then "All
items shall be unique." (p. 16). A string has no items. Annex A puts
`"uniqueItems": true` on the `qualifiers_definition` array, and §6.8 itself
has no uniqueness sentence, so the sentence most likely belongs to §6.8
(inferred: the other array properties, §6.5.7, §6.10 and §6.12, end with the
same sentence in the same italic style).

## Other observations (not contradictions)

Recorded for the cross-check pass; none is a source defect.

- **O1.** The `$schema` property (optional; `"const":
  "https://packageurl.org/schemas/purl-type-definition.schema-1.0.json"`,
  `"format": "uri"`) exists only in Annex A.
- **O2.** Annex A closes three objects (`additionalProperties: false` at the
  root, in `repository` and in each `qualifiers_definition` item); Clause 6
  never says so. The four component definitions stay open, so a misspelt
  property validates silently: `{"requirement": "optional", "case_sensitve":
  false}` is a valid `namespace_definition`.
- **O3.** `uniqueItems` on `qualifiers_definition` compares whole objects: two
  items with the same `key` and different descriptions are valid.
- **O4.** `qualifiers_definition[].key` has no pattern, although §5.6.6 limits
  keys to lower-case ASCII letters, digits, period, dash and underscore,
  starting with a letter: a definition with the key `Not A Key!` is valid.
- **O5.** The `$id` pattern allows `[a-z0-9-]` before `-definition.json`,
  while the `type` pattern also allows a period; nothing ties `$id` to `type`.
  A type `foo.bar` is valid, but its natural `$id` is not.
- **O6.** `examples` has `"minItems": 1` in Annex A only; Clause 6 makes the
  property required but sets no minimum.
- **O7.** Annex A spells the `default_repository_url` description without the
  final period that Table 3 and §6.4.2 print (editorial).
- **O8.** `version_definition.requirement` and `subpath_definition.requirement`
  must be present but may only be `optional`, and
  `name_definition.requirement` may only be `required`: no type definition can
  make the version or subpath required, or the name optional.
- **O9.** "If provided, this shall be a subset of the 'Permitted characters'
  defined in the PURL specification." (§6.5.5, §6.6.3, §6.7.3, §6.9.3) is not
  checkable by the schema; `format: regex` only checks regular-expression
  syntax, and only when format checking is on.

## The derived grammar: `purl.derived.abnf`

RFC 5234 ABNF, pure ASCII (RFC 5234 allows only ASCII in comments, so the
copyright sign in its attribution line is written `(c)`). Every rule cites the
clause it encodes, and every passage the comments attribute to a clause is
verbatim. Three root rules:

| rule | what it accepts |
|---|---|
| `purl` | a PURL string: every Clause 5 rule a context-free grammar can enforce, plus what Clause 5 calls non-canonical rather than invalid (upper-case letters in the type; leading or trailing slashes around namespace, name and subpath) |
| `canonical-shape` | the part of `purl` with the canonical shape: lower-case type, no insignificant slash. Necessary, **not sufficient**, for canonical form |
| `purl-parser-input` | `purl` plus the `pkg:/` and `pkg://` forms §5.6.1 obliges parsers to accept |

`canonical-shape` is contained in `purl`, which is contained in
`purl-parser-input` (checked: no violation in any test below).

### Readings (judgement calls)

- **R1 Strict percent-encoding.** §5.6 says each component "shall be encoded
  as defined in the Character encoding clause", and §5.4 says "The following
  characters shall not be percent-encoded", naming the Alphanumeric and
  Punctuation Characters and "the colon ':', whether used as a Separator
  Character or otherwise". A triplet such as `%41`, `%2E` or `%3A` cannot come
  out of that encoding, so the grammar rejects it. The lenient alternative is
  one line away (define `pct-octet-no-slash` as `2HEXDIG`).
- **R2 Nothing empty after a separator.** No `@`, `?` or `#` unless a
  non-empty component follows: the converse of "The version is prefixed by a
  '@' separator when not empty." (§5.6.5) and the matching bullets of §5.6.6
  and §5.6.7. Implied, not stated.
- **R3 The name is non-empty**, from Table 1 ("Required") and Clause 2 ("All
  required components of a PURL, such as the scheme, type, and name, shall be
  present").
- **R4 Lower-case scheme only.** §5.6.1 gives the constant "pkg" and never
  calls the scheme case insensitive; RFC 3986 section 3.1 (invoked by §5.1)
  does. Not imported.
- **R5 Where an insignificant slash may stand.** After the type, at the
  namespace and name boundary, after the name (so also just before `@`, `?`
  or `#`) and at both ends of the subpath; never inside the namespace or
  subpath, where a run of slashes makes an empty segment. The purl-spec
  `v1.0.0` tests (not part of ECMA-427) read the slash before `@` differently:
  they expect `pkg:swift/github.com/Alamofire/@5.4.3` to fail for want of a
  name. The 1st edition text does not decide it.

### What the grammar cannot express

The grammar's own GAPS section (items G1 to G9) gives each in full, with the
governing text. In short:

- **Canonical form (G1; R-0006, R-0055, R-0065, R-0092, R-0131, R-0132).** Only the case of the type and the insignificant
  slashes are checked. Type-specific case folding and `normalization_rules`
  are out of reach, and two things a canonical form needs are not defined by
  the 1st edition at all: an order for the qualifiers (no clause orders them)
  and the case of hex digits in a triplet. Clause 2 nevertheless requires that
  "equivalent PURLs are consistently resolved to the same canonical
  representation".
- **Case folding (G2; R-0039, R-0040, R-0051).** §5.5 defines "lowercase" as the Unicode full case
  mapping; a grammar does not fold case, it only admits or refuses upper case.
- **Type-specific rules (G3; R-0018, R-0021, R-0053, R-0060, R-0068, R-0072, R-0097):** a required or prohibited namespace, required
  qualifier keys, narrower character sets. They live in type definitions
  validated by the Annex A schema.
- **Uniqueness of qualifier keys (G4; R-0086):** "Each key shall be unique among all
  the keys of the qualifiers component." (§5.6.6) is not context-free.
- **The `pkg://` leniency of §5.6.1 (G5; R-0047).** `purl-parser-input` states what to
  accept; the duty to "ignore and remove" the slashes is a transformation.
- **Decoded segments (G6; R-0034, R-0058, R-0094).** That a percent-decoded namespace or subpath
  segment is non-empty and holds no `/` (§5.6.3, §5.6.7) is enforced on the
  encoded form, which is exact under R1 (no `%2F` in a segment, at least one
  character). Not checked: that the decoded octets are well-formed UTF-8, as
  §5.4 requires.
- **Empty qualifier values (G7; R-0081, R-0082):** "a key=value pair with an empty value is
  the same as if no key=value pair exists for this key" (§5.6.6) is an
  equivalence, not syntax; all three roots refuse `key=`. For
  `purl-parser-input` that is stricter than the sentence's own second half,
  which gives such a pair a meaning: a reader that follows it accepts `key=`
  and drops the pair, as `../examples/expected.yaml` expects (PURL-NEG-06).
  Added in pass 2; see `../normative.md` U-16.
- **Meaning (G8; R-0061, R-0073, R-0098):** host versus namespace, the opaque version, the subpath
  relative to the package root.
- **Type names (G9; R-0028, R-0030):** the special and VCS URL schemes that §5.1 says "are not
  valid PURL types" are open-ended lists, so no name is excluded.
- **Also outside the grammar, found in pass 3 (cross-check).** Three Clause 5
  requirements are in no G item. R-0025: a PURL "is a valid URL and URI that
  conforms to the URL definitions or specifications at:" four documents that do
  not agree with each other; every string `purl` accepts is an RFC 3986 URI
  (checked with `rfc3987` on the 24 distinct smoke and fixture strings it
  accepts), but conformance to all four is not one test. R-0038, which says which document
  defines the percent-encoding rules and has no syntax. R-0062, "Use instead a
  repository_url qualifier.", an instruction that `qualifier-key` admits but
  cannot require. R-0024 and R-0063 are informative. The authority prohibition
  (R-0023, R-0027) holds for `purl`, which has no authority part, but a host
  written after `pkg://` survives the slash removal of §5.6.1 as a type
  (`../examples/expected.yaml`, PURL-EDGE-01). `../verification.md` (pass 3)
  maps each of the 84 Clause 5 requirements to the rule that enforces it or to
  the item that explains why it cannot.

## Smoke tests of the grammar

All runs on 2026-10-15 with the Python package `abnf` 2.2.0 (a generalised
RFC 5234 parser that explores every match, so ambiguous optional parts are
safe). The grammar loads with `Rule.from_file`, which also enforces that the
file is ASCII.

Command (from the repository root; one line of output per string: one letter
per root rule, in the order `purl`, `canonical-shape`, `purl-parser-input`,
`A` accept and `R` reject):

```sh
python3 -I -c '
import sys
from abnf import Rule
from abnf.parser import ParseError
class P(Rule): pass
P.from_file(sys.argv[1])
for s in sys.argv[2:]:
    r = ""
    for root in ("purl", "canonical-shape", "purl-parser-input"):
        try:
            P(root).parse_all(s); r += "A"
        except ParseError:
            r += "R"
    print(r, s)
' records/other/ecma-427/distilled/schema/purl.derived.abnf \
  'pkg:deb/debian/curl@7.50.3-1?arch=i386&distro=jessie' \
  'pkg:maven/org.apache.xmlgraphics/batik-anim@1.9.1?packaging=sources' \
  'pkg:npm/foobar@12.3.1' \
  'pkg:1abc/foobar' 'pkg:np%6D/foobar' 'pkg:npm/foobar?Arch=x86' 'pkg:npm/foobar?arch=' \
  'pkg:maven/org//apache/batik' 'pkg:maven/org%2Fapache/batik' 'pkg:npm/foobar#src/../lib' \
  'pkg:npm/foo bar' 'pkg:npm/foobar@1.0+build' 'pkg:npm/fooba%72' \
  'pkg:NPM/foobar@12.3.1' 'pkg://npm/foobar@12.3.1' 'pkg:npm/foobar?arch=x86&arch=arm64'
```

Output (about 10 seconds):

```
AAA pkg:deb/debian/curl@7.50.3-1?arch=i386&distro=jessie
AAA pkg:maven/org.apache.xmlgraphics/batik-anim@1.9.1?packaging=sources
AAA pkg:npm/foobar@12.3.1
RRR pkg:1abc/foobar
RRR pkg:np%6D/foobar
RRR pkg:npm/foobar?Arch=x86
RRR pkg:npm/foobar?arch=
RRR pkg:maven/org//apache/batik
RRR pkg:maven/org%2Fapache/batik
RRR pkg:npm/foobar#src/../lib
RRR pkg:npm/foo bar
RRR pkg:npm/foobar@1.0+build
RRR pkg:npm/fooba%72
ARA pkg:NPM/foobar@12.3.1
RRA pkg://npm/foobar@12.3.1
AAA pkg:npm/foobar?arch=x86&arch=arm64
```

The full smoke set, 49 strings, each as expected (the three Clause 5 examples
are accepted by all three roots; every string that breaks a stated rule is
rejected by all three):

| # | string | `purl` | `canonical-shape` | `purl-parser-input` | rule exercised |
|---|---|---|---|---|---|
| 1 | `pkg:deb/debian/curl@7.50.3-1?arch=i386&distro=jessie` | accept | accept | accept | Clause 5 Example 1 |
| 2 | `pkg:maven/org.apache.xmlgraphics/batik-anim@1.9.1?packaging=sources` | accept | accept | accept | Clause 5 Example 2 |
| 3 | `pkg:npm/foobar@12.3.1` | accept | accept | accept | Clause 5 Example 3 |
| 4 | `pkg:1abc/foobar` | reject | reject | reject | §5.6.2 type shall start with an ASCII letter |
| 5 | `pkg:np_m/foobar` | reject | reject | reject | §5.6.2 type: only letters, numbers, '.', '-' |
| 6 | `pkg:np%6D/foobar` | reject | reject | reject | §5.6.2 type shall not be percent-encoded |
| 7 | `pkg:npm/foobar?Arch=x86` | reject | reject | reject | §5.6.6 key only lowercase letters, numbers, '.', '-', '_' |
| 8 | `pkg:npm/foobar?1arch=x86` | reject | reject | reject | §5.6.6 key shall start with an ASCII letter |
| 9 | `pkg:npm/foobar?ar%63h=x86` | reject | reject | reject | §5.6.6 key shall not be percent-encoded |
| 10 | `pkg:npm/foobar?arch=` | reject | reject | reject | §5.6.6 value shall not be an empty string |
| 11 | `pkg:npm/foobar?arch` | reject | reject | reject | §5.6.6 key and value separated by '=' |
| 12 | `pkg:npm/foobar?arch=x86&` | reject | reject | reject | §5.6.6 pairs separated by '&' (no empty pair) |
| 13 | `pkg:maven/org//apache/batik` | reject | reject | reject | §5.6.3 namespace segment shall not be empty |
| 14 | `pkg:maven/org%2Fapache/batik` | reject | reject | reject | §5.6.3 decoded segment shall not contain '/' |
| 15 | `pkg:npm/foobar#src/../lib` | reject | reject | reject | §5.6.7 segment shall not be '..' |
| 16 | `pkg:npm/foobar#src/./lib` | reject | reject | reject | §5.6.7 segment shall not be '.' |
| 17 | `pkg:npm/foobar#src//lib` | reject | reject | reject | §5.6.7 segment shall not be empty |
| 18 | `pkg:npm/foo bar` | reject | reject | reject | §5.4 space shall be percent-encoded as '%20' |
| 19 | `pkg:npm/foobar@1.0+build` | reject | reject | reject | §5.4 '+' is outside the allowed set |
| 20 | `pkg:npm/@angular/core` | reject | reject | reject | §5.4 '@' in data is outside the allowed set |
| 21 | `pkg:npm/foobar@1.0%` | reject | reject | reject | §5.4 '%' only as the start of a triplet |
| 22 | `pkg:npm/foobar@1.0%zz` | reject | reject | reject | §5.4 triplet is '%' and two hex digits |
| 23 | `pkg:npm/fooba%72` | reject | reject | reject | §5.4 alphanumerics shall not be percent-encoded (R1) |
| 24 | `pkg:deb/debian/curl@1%3A7.50.3-1` | reject | reject | reject | §5.4 the colon shall not be percent-encoded (R1) |
| 25 | `pkg:npm/foo%7Ebar` | reject | reject | reject | §5.4 punctuation shall not be percent-encoded (R1) |
| 26 | `pkg:npm` | reject | reject | reject | Table 1 name Required (R3) |
| 27 | `pkg:npm/` | reject | reject | reject | Table 1 name Required (R3) |
| 28 | `pkg:npm/foobar@` | reject | reject | reject | §5.6.5 '@' only when the version is not empty (R2) |
| 29 | `pkg:npm/foobar?` | reject | reject | reject | §5.6.6 '?' only when not empty (R2) |
| 30 | `pkg:npm/foobar#` | reject | reject | reject | §5.6.7 '#' only when not empty (R2) |
| 31 | `pkg//npm/foobar` | reject | reject | reject | §5.6.1 scheme followed by an unencoded colon |
| 32 | `PKG:npm/foobar` | reject | reject | reject | §5.6.1 scheme constant pkg (R4) |
| 33 | `npm/foobar@1.0` | reject | reject | reject | Clause 5: no scheme |
| 34 | `pkg:NPM/foobar@12.3.1` | accept | reject | accept | §5.6.2 type case insensitive; canonical lowercase |
| 35 | `pkg:npm//foobar@12.3.1` | accept | reject | accept | §5.6.4 leading slash not significant |
| 36 | `pkg:npm/foobar/@12.3.1` | accept | reject | accept | §5.6.4 trailing slash not significant |
| 37 | `pkg:maven//org.apache.xmlgraphics//batik-anim` | accept | reject | accept | §5.6.3 leading/trailing slashes |
| 38 | `pkg:npm/foobar#/lib/index.js/` | accept | reject | accept | §5.6.7 leading/trailing slashes |
| 39 | `pkg://npm/foobar@12.3.1` | reject | reject | accept | §5.6.1 parsers shall accept 'pkg://' |
| 40 | `pkg:/npm/foobar@12.3.1` | reject | reject | accept | §5.6.1 one or more slashes |
| 41 | `pkg:npm/foobar?arch=x86&arch=arm64` | accept | accept | accept | GAP G4: duplicate key not detectable |
| 42 | `pkg:a/foobar` | accept | accept | accept | §5.6.2 sets no minimum length (Annex A needs 2) |
| 43 | `pkg:npm/%40angular/core@12.3.1` | accept | accept | accept | §5.4 '@' in data encoded as %40 |
| 44 | `pkg:npm/foobar@1.0%2Bbuild` | accept | accept | accept | §5.4 '+' encoded |
| 45 | `pkg:npm/foo%2fbar` | accept | accept | accept | §5.6.4 a name may hold an encoded '/' |
| 46 | `pkg:deb/debian/curl@1:7.50.3-1` | accept | accept | accept | §5.4 colon never encoded |
| 47 | `pkg:generic/x?download_url=https:%2F%2Fexample.com%2Fx.tgz` | accept | accept | accept | §5.4 '/' in a value encoded |
| 48 | `pkg:npm/foobar#lib/.hidden/..x` | accept | accept | accept | §5.6.7 '.hidden' and '..x' are not '.' or '..' |
| 49 | `pkg:npm/fo%c3%b6bar` | accept | accept | accept | §5.4 non-ASCII as UTF-8 triplets, lower-case hex |

The right-hand column is our label for the rule exercised, not a quotation.

### Two further checks, run with scratch scripts that are not committed

- **Differential test against an independent checker.** A second
  implementation of the same reading, written as string splitting (not
  derived from the grammar), was compared with the grammar on random strings
  biased towards the edge of validity: 2,998 distinct strings (seed 20261015;
  829 accepted by `purl`, 365 by `canonical-shape`, 1,007 by
  `purl-parser-input`) and 8,985 distinct strings (seed 427; 2,560, 1,132 and
  3,042 accepted). **0 disagreements, 0 containment violations.** Controls:
  copies of the grammar with one rule broken (a segment that admits `%2F`; a
  subpath segment that admits `..`) produced 4 and 58 disagreements.
- **The purl-spec `v1.0.0` test corpus** (497 tests in `tests/spec` and
  `tests/types`; informative, not part of ECMA-427; 200 distinct strings):
  - all **129** canonical outputs of the build and roundtrip tests are
    accepted by `canonical-shape` and by `purl`;
  - of 146 inputs the tests expect to parse, `purl-parser-input` accepts 114
    and rejects 32. Each of the 32 breaks §5.4 or §5.6.6 as written (some
    break two): 24 have an unencoded `/` in a qualifier value
    (`repository_url=https://...`), 5 write a colon as `%3A`, 4 have an
    upper-case letter in a qualifier key, 3 have an unencoded `+`, 1 has an
    unencoded `@` in the namespace. purl-spec's own canonical outputs repair
    exactly these (`%2F` in values, a literal colon), and one test calls its
    input "wrongly percent encoded". The 1st edition states no parser leniency
    beyond §5.6.1, so the grammar does not model one;
  - of 19 inputs the tests expect to fail, the grammar rejects 12 and accepts
    7: six fail for type-specific reasons the grammar cannot see (`cpan`,
    `julia`, `otp`, `swift`), and one is the R5 case
    `pkg:swift/github.com/Alamofire/@5.4.3`.

For context only: packageurl-python 0.17.6 accepts 19 of the 30 smoke strings
the grammar's `purl-parser-input` rejects. It rewrites 18 of them, for example
`pkg:maven/org%2Fapache/batik` to `pkg:maven/org/apache/batik` (one namespace
segment becomes two) and `pkg:npm/foobar#src/../lib` to `pkg:npm/foobar#src/lib`,
and returns the 19th, `pkg:np_m/foobar` (a type §5.6.2 forbids), unchanged. Clause 2 says
"Invalid PURLs that fail to conform to the specification shall be identified
and rejected by any conforming implementation."

## Tools and versions

Python 3.13.9; jsonschema 4.26.0; rfc3987 1.3.8; abnf 2.2.0;
packageurl-python 0.17.6; PyYAML 6.0.3; poppler `pdftotext` and `pdftoppm`
for the text and the page images. Every Python run that read a downloaded
file used `python3 -I`.

## Open for the later passes

- Pass 3 (cross-check) wired `constrained_by` on every field of
  `../messages.yaml` from its `constrained_by_locators`; `../verification.md`
  records the method and the counts.
- Readings R1 to R5 are judgement calls for a human reviewer. R1 and R5 are
  the ones where real-world data (purl-spec tests, packageurl-python) reads
  the text differently.
- Defects D1 to D6 could be reported to Ecma TC54 (`https://github.com/Ecma-TC54/ECMA-427`).
