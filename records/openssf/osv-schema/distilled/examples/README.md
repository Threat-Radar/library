---
record: osv-schema
kind: examples
title: "osv-schema: examples, derived fixtures and expected results"
extracted: "2026-10-18"
reviewed_by: ""
---

# OSV Schema 1.9.2 examples and test vectors

Contains text from the OSV Schema (github.com/ossf/osv-schema, tag v1.9.2), licensed under the Apache License, Version 2.0.

Every example that `docs/schema.md` of OSV Schema 1.9.2 prints, copied byte
for byte (34 fenced blocks and 54 examples written inside sentences), plus 136
records the library derived from the text. Each of the 224 fixtures has an
expected result worked out by hand from the prose, and the actual result of
validating it against the source's own JSON Schema (`validation/schema.json`)
with jsonschema 4.26.0, once without and once with a format checker.
`run-fixtures.derived.py` reproduces every actual result and fails if one
changes.

Source: github.com/ossf/osv-schema at tag `v1.9.2`, commit
`c8a57bdc5b0bc54646e140cabbb7834bd0b5aec9`. `docs/schema.md` is the
specification (2010 lines, SHA-256
`96d82f03d763fb408bc344d01fc271f761a81cc225f6f6a42d318e3ed21cebff`; the
repository's root `schema.md` only points to the published page), and
`validation/schema.json` is its JSON Schema (draft 2020-12, SHA-256
`15b10dbb4c4e31c7aae11d22cdd991a9a374758db7c8389e62b3cc37cac92653`). Line
numbers everywhere are those of `docs/schema.md` at that commit. No expected
result depends on another distilled artifact; the requirement ids that pass 3
added are links to `../requirements.yaml`.

The specification writes its rules in lowercase (must, should, required) and
uses no BCP 14 capitals; the expected results read the lowercase words with
their ordinary force.

## Files

| path | what |
|---|---|
| `expected.yaml` | the index: all 224 fixtures, each with its locator (or the record it was derived from and the JSON Pointers that changed), the expected result and the statements it rests on (cited by rule id and locator, each with a basis, and for a broken rule the `requirements.yaml` ids it breaks), the actual jsonschema results and a comparison. Also the 109 statements the fixtures cite, quoted verbatim, each with its `requirements.yaml` ids; 9 enumerations comparing a list in the prose with the JSON Schema's; the 24 findings; the 15 source issues |
| `verbatim/blocks/` | the 34 fenced blocks of `docs/schema.md`, byte for byte (the lines between the fences, tabs kept), named by fence line and heading: 9 complete records and 2 package objects (`.json`), 7 ranges examples (`.json-fragment`: a `"ranges"` member to wrap in braces), and 16 blocks that are not JSON texts as printed (`.txt`): 13 informal field shapes, the Credits example (a trailing comma), the id regular expression and the evaluation pseudocode |
| `verbatim/inline/` | the 54 examples written inside sentences (7 ids, 28 ecosystem strings, 9 package names, 2 versions, 3 CVSS vectors, 2 event objects, 3 credit names), one per file, named by line, position on the line and kind; each ends in one LF that is not part of the example. `.json` and `.json-fragment` where the text writes the example as JSON |
| `osv-records/` | the 136 derived records (`.derived.json`). `pos-02-base.derived.json` is the base; every other derived record except `pos-01-minimal` is the base (or another fixture) changed only at the JSON Pointers listed in `mutations`, one pointer for most and never more than four |
| `run-fixtures.derived.py` | the reproduction script (library-written, no source text) |

Files the library wrote carry `.derived.` before the extension; files under
`verbatim/` are copies of source text and do not. `README.md` and
`expected.yaml` keep the names the extraction brief gave them.

## Counts

| group | ids | n | expected | jsonschema 4.26.0 |
|---|---|---:|---|---|
| source examples | `SRC-L<line>` (blocks), `SRC-L<line>-<n>` (inline) | 88 | 73 with a validity result: 70 valid; invalid are the two limit examples taken literally and the text's own invalid event. The other 15 are 13 informal shapes, the id regular expression and the pseudocode | agrees on all 73 |
| source examples placed in the base record | `EMB-L<line>` | 10 | 7 valid, 3 invalid | agrees on all |
| positives | `POS-01` to `23` | 23 | valid | agrees |
| negatives | `NEG-01` to `34` | 34 | invalid | agrees |
| the prose forbids, the JSON Schema accepts | `GAP-01` to `41` | 41 | invalid | accepts all 41; the format checker rejects 4 of them (`GAP-12`, `13`, `32`, `33`) |
| the prose allows, the JSON Schema rejects | `OVER-01` to `03` | 3 | valid | rejects all 3 |
| a should broken, otherwise valid | `SHOULD-01` to `10` | 10 | valid | agrees |
| the prose does not decide | `EDGE-01` to `12` | 12 | 10 unspecified; `EDGE-05` invalid (since pass 3) and `EDGE-11` valid | accepts 5 of the 10 and rejects 5; agrees on `EDGE-05` and `EDGE-11` |
| jsonschema against JSON Schema 2020-12 | `TOOL-01` to `03` | 3 | 2 invalid, 1 valid | accepts `TOOL-01` and `02`, which the patterns read as ECMA-262 reject; rejects `TOOL-03` with the format checker |

In 47 fixtures jsonschema differs from the expected result (`GAP-*`, `OVER-*`
and `TOOL-*`); each names its finding.

## How the expected results were derived

Only the prose of `docs/schema.md` decides an expected result; the JSON Schema
is the thing under test. Each fixture's `expected` cites the statements it
rests on by rule id, and `rules` quotes them verbatim with their locators. A
citation carries a basis:

- **must**: a statement with must, must not, required, "only ... is allowed",
  "not allowed" or "is **invalid**" (for example the id character set, the one
  type per event rule, a GIT range's repo).
- **definition**: a statement that defines a field without a modal verb ("is a
  JSON array", "in the form of the `id` field", "full-length Git commit
  hashes", "without the `@version` component"). A record that breaks a
  definition does not have the structure the text defines, so it is expected
  invalid.
- **inference**: a conclusion drawn from one or more statements. Seven
  negatives cite one (`NEG-12`, `GAP-07`, `GAP-10`, `GAP-11`, `GAP-18`,
  `GAP-34`, `GAP-35`); each is a judgement call.

`context` cites statements that explain a verdict without being broken (for
example the Ubuntu example that makes 22.04 an LTS release, in `GAP-26`). A
record that breaks only should or recommended statements is valid, and lists
them in `breaks_should`. Where the text does not decide, the result is
`unspecified` and `readings` gives each alternative with the statement behind
it. Three source blocks are not instances: the informal field shapes (result
`shape`, checked by comparing the field paths they name with the paths the
JSON Schema defines), the id regular expression (`rule`) and the evaluation
pseudocode (`algorithm`).

Pass 3 (cross-check) tied the fixtures to `../requirements.yaml`. Each quoted
rule carries the ids of the entries whose text it quotes (`requirements`; nine
narration and rationale rules have none, and say why), and each rule a fixture
violates carries `breaks`: the entries that the fixture's one change breaks,
including the entry taken from the JSON Schema that states the same constraint
when the JSON Schema also rejects the change (for example `NEG-12` breaks
R-0163 and the type enum R-0226). Pass 3 also added `GAP-41` (a listed prefix
and its hyphen with no entry id) and the rule `purl-recommended`, and changed
`EDGE-05` from unspecified to invalid.

Values written inside sentences are validated against the subschema they
belong to (`validate_as`): an id against `/properties/id`, an ecosystem string
against the package ecosystem schema, a CVSS vector as the score of a severity
item of its type. Seven printed examples are not JSON because of a trailing
comma (source issue S-01); the runner removes those commas, and nothing else,
before validating them.

Derived records use made-up names so they cannot be mistaken for real
advisories: ids use the local `x_` prefix, the package is `osv-fixture`, URLs
use example.com and commit hashes are runs of one digit.

## Where the JSON Schema and the prose disagree

Each row is a `findings` entry in `expected.yaml`, with the JSON Pointer of
the schema keyword involved.

**The JSON Schema accepts what the prose forbids**

| finding | what | fixtures |
|---|---|---|
| F-01 | The id pattern `^(x_\|(ASB-A\|...\|VCPKG)-)` checks only the start: any characters may follow a known prefix, and `x_` alone passes, as does a listed prefix and its hyphen with nothing after them (`GHSA-`). The prose requires the whole id to match `^[a-zA-Z0-9:_.-]+$`, of the form `<DB>-<ENTRYID>`, and names spaces, slashes, backslashes, parentheses and exclamation marks as not allowed | `GAP-01` to `07`, `GAP-41` |
| F-03 | `aliases`, `related` and `upstream` items are plain strings; the prose says ids (aliases in the form of the `id` field), and an id cannot be its own upstream | `GAP-09`, `10`, `11` |
| F-04 | Timestamps: the pattern has no anchors and `format: date-time` is only an annotation by default, so text around a timestamp and 30 February pass; a trailing line feed passes even with the format checker (also a tool issue, below) | `GAP-12`, `13`, `14` |
| F-06 | SEMVER range values are unchecked: `v1.0.2` and `1.0` pass | `GAP-15`, `16` |
| F-07 | The GIT hash pattern allows `0` for every event type, so `fixed: "0"` passes; the prose gives `0` to introduced only | `GAP-17` |
| F-09 | The ecosystem pattern allows any `:suffix`, or none, on every ecosystem. The prose requires a suffix for Alpine (with `v`), Mageia, Photon OS and Red Hat Lightwell (an existing ecosystem), `:LTS` for an LTS Ubuntu release, lists the only Echo values, forbids a trailing slash on a Maven repository URL, and describes no suffix for npm | `GAP-18` to `27` |
| F-10 | Package names are plain strings; the prose allows only `Kernel` for Linux and only the listed SoC vendors after `:linux_kernel:` in Android | `GAP-28`, `29` |
| F-12 | `purl` is a plain string; the prose asks for a Package URL without its version | `GAP-30`, `31` |
| F-13 | `references[].url` has `format: uri`, checked only with a format checker; by default any string passes | `GAP-32`, `33` |
| F-16 | The CVSS_V2 and CVSS_V3 patterns accept any sequence of known metrics, so `AV:N` and `CVSS:3.1/AV:N` pass; both CVSS specifications require every base metric (cited). The CVSS_V4 pattern does require them | `GAP-34`, `35` |
| F-17 | `aliases`, `affected`, `references` and `severity` accept `null` (`type: [array, null]`); `related`, `upstream` and `credits` do not. The prose describes all of them as arrays or lists | `GAP-36` to `39`, `NEG-31` |
| F-21 | A two-line `summary` passes; the prose defines a one-line summary | `GAP-40` |
| F-22 | Nothing stops an id from naming the weakness, package or severity (`x_FIXTURE-RCE-0001`); the prose's must not applies to new identifier schemes | `GAP-08` |

**The JSON Schema rejects what the prose allows**

| finding | what | fixtures |
|---|---|---|
| F-02 | The prefix list is enforced as a hard rule, though the prose asks for a defined prefix with should (line 169). The lists also differ: the prose table prints `CleanStart` where the JSON Schema has `CLEANSTART`, and the JSON Schema accepts `FreeBSD`, which the table does not list | `OVER-02`, `OVER-03`, `SHOULD-08` |
| F-08 | The GIT hash pattern rejects `limit: "*"`, the infinity value the prose defines and the implicit event it says every range has. The text's own `{ "limit": "*" }` is valid as an event item and in a SEMVER range, and invalid in a GIT range | `OVER-01`, `SRC-L1154-1`, `SHOULD-04` |

**The JSON Schema decides what the prose leaves open**

| finding | what | fixtures |
|---|---|---|
| F-11 | `GIT` is accepted as a package ecosystem (the pattern ends in `\|GIT`). The table does not list it, the prose calls GIT a pseudo-ecosystem, and the schema's own unreferenced `ecosystemName` enum leaves it out | `EDGE-01` |
| F-14 | The reference type enum adds `GIT`, which is not among the prose's ten known values, and closes the list, which the prose does not. Under either reading of the prose the schema disagrees with one of the two fixtures | `EDGE-07`, `08` |
| F-15 | The severity source is a closed enum (NVD, CNA, SELF); the prose calls it an optional string and never says the list is closed, unlike severity type and credit type | `EDGE-06` |
| F-18 | `additionalProperties: false` applies at the top level only: an unknown top-level field is rejected, an unknown field in an affected entry or an event object is accepted | `EDGE-02`, `03`, `04` |
| F-19 | The rule against severity at both levels fires on the presence of the top-level member, so a `null` or empty top-level severity next to package-level severity is rejected | `EDGE-05`, `12` |
| F-20 | GIT hashes must be lowercase hexadecimal; the prose does not fix the letter case | `EDGE-09` |
| F-23 | `versions` is optional in every case; the prose calls it generally recommended in one place and a requirement that GIT ranges do not remove in another | `EDGE-10`, `SRC-L1635` |

The enumerations in `expected.yaml` compare each closed or tabled list in the
prose with the JSON Schema: the id prefixes differ (`CleanStart` only in the
prose; `CLEANSTART` and `FreeBSD` only in the schema), the ecosystems differ by
`GIT`, the reference types differ by `GIT`, and severity types, severity
sources, range types and credit types match. The eight Android SoC vendors have
no counterpart in the schema.

## Where jsonschema differs from the JSON Schema itself

JSON Schema 2020-12 specifies ECMA-262 regular expressions and leaves `format`
an annotation unless assertion is asked for. jsonschema 4.26.0 evaluates
`pattern` with Python `re.search` and checks `date-time` with
rfc3339-validator 0.1.4.

| finding | what | fixtures |
|---|---|---|
| F-24 | Python's `$` also matches just before a final line feed, so a commit hash or an ecosystem followed by a line feed passes jsonschema; Node (ECMA-262, with and without the `u` flag) rejects the same value under the same pattern. Every pattern in the schema that ends in `$` has this gap | `TOOL-01`, `02` |
| F-05 | With the format checker, the leap second `2016-12-31T23:59:60Z` is rejected: rfc3339-validator allows seconds up to 59, RFC 3339 up to 60 at a leap second (cited) | `TOOL-03` |
| F-04 | rfc3339-validator also matches with Python's `$`, so a timestamp followed by a line feed passes even with the format checker | `GAP-14` |

jsonschema reports a schema path through a `$ref` without the `$ref` hop:
`/properties/id/pattern` in an error means the pattern of `/$defs/prefix`.
All eleven patterns in the schema compile in Python and in ECMA-262 with and
without the `u` flag (`schema_checks`). `$defs/ecosystemName` and
`$defs/ecosystemSuffix` are never referenced.

## Evaluation of the range examples

Five of the seven ranges examples state what they mean ("everything before
`1.0.2`" is affected, and so on). For each, `evaluation` lists versions with
the verdict that meaning gives, 28 probes in all, including SemVer
pre-release and build-metadata versions (`1.0.2-rc.1` is affected by a fix in
`1.0.2`; `1.0.2+build.5` is not). The runner evaluates them with a literal
transcription of `IncludedInRanges` and `BeforeLimits` from the pseudocode
(`verbatim/blocks/L1247-evaluation.txt`) under SemVer 2.0.0 precedence; it
agrees with every probe. The `last_affected` example's ECOSYSTEM range names no
ecosystem, so SemVer precedence stands in for its ordering. The two GIT limit
examples are not evaluated: their results depend on the commit graph in
`images/git_graph.png`, which is not part of `docs/schema.md` (S-11).

## Where the source is inconsistent or unclear

Each is a `source_issues` entry in `expected.yaml`.

1. **S-01** Seven printed examples are not valid JSON: a trailing comma before
   a closing bracket or brace (RFC 8259, cited) in six of the seven ranges
   examples and in the Credits example.
2. **S-02** The two `last_affected` vs `fixed` examples use different range
   types (ECOSYSTEM at line 1389, SEMVER at line 1405), though the second is
   introduced as looking similar.
3. **S-03** The versions list is "generally recommended" (lines 937 to 939) but
   called a requirement that GIT ranges do not remove and SEMVER ranges do
   (lines 1104 and 1127). The OSV example (line 1635) has a GIT range and no
   versions.
4. **S-04** The Red Hat row says the prefix `cpe/:[oa]:(redhat):` is removed,
   but its example CPE begins `cpe:/a:redhat:`.
5. **S-05** The FreeBSD row calls `'FreeBSD:base:14.3'` a `ranges[].events`
   version, though it has the shape of an ecosystem string, and its last
   sentence ends "a particular FreeBSD release like."
6. **S-06** The openEuler row writes the suffix as `<RELEASE>`, without the
   colon every other row has.
7. **S-07** The CleanStart row prints the prefix `CleanStart` (line 277) while
   its URL template spells `CLEANSTART-YYYY-<ID>` (line 283); the JSON Schema
   accepts only `CLEANSTART`.
8. **S-08** The Haskell GHC example reuses the Hackage example's id
   `HSEC-2023-0006` and modified time, so the later-modification rule cannot
   order the two.
9. **S-09** The GitHub example was modified (16:02:43) before it was
   published (16:06:50); no statement orders the two times.
10. **S-10** The affected fields block (line 890) omits
    `affected[].ranges[].database_specific`, which the Format Overview block and
    the JSON Schema both have.
11. **S-11** The limit examples use placeholder commits X and Y and a picture
    the text does not include, so their stated results cannot be checked.
12. **S-12** The id format is `<DB>-<ENTRYID>` (line 144), but line 169 says the
    prefix is only ideally followed by a hyphen; the JSON Schema requires the
    hyphen after a listed prefix and nothing after `x_`.
13. **S-13** The text speaks of a GIT ecosystem (lines 1065 and 1081) and says
    a Git entry should have no package; the table does not list GIT, the
    schema's pattern accepts it and its unused enum does not.
14. **S-14** `$defs/ecosystemName` and `$defs/ecosystemSuffix` are defined but
    never referenced.
15. **S-15** Several examples break recommendations: the Python example puts
    PyPI and GIT ranges in one entry, and the GitHub, Debian, Hackage and GHC
    examples give ECOSYSTEM ranges without a versions list. None of the nine
    complete examples gives a `purl`, which line 967 recommends (added in pass 3).

## Judgement calls

- **Inline examples are fixtures.** Every value the text gives as an example
  inside a sentence ("For example", "e.g.", "such as", "Examples:") and that
  fills an OSV field has its own file, as do the implicit `{ "limit": "*" }`
  event (line 1154) and the `"GHC"` the GHC example switches to (line 1891).
  Templates, closed lists of allowed values and words inside descriptions do
  not (see Not transcribed).
- **The regular expression and the pseudocode** are transcribed although they
  are not examples: the runner uses the first to check ids and the second is
  what the evaluation probes are checked against.
- **Definitions bind.** A record that breaks a definitional statement ("is a
  JSON array", "in the form of the `id` field") is expected invalid; the
  basis field marks every such citation so a reader can weigh it.
- **Prefixes are a should.** An id with an unlisted prefix is expected valid
  with a broken should (`OVER-02`); line 149's "allowing external records to
  be schema-compliant" describes the JSON Schema, not a rule of the prose.
  `CleanStart-2026-0001` is valid because the table prints that prefix
  (`OVER-03`).
- **The id must not about weaknesses** (`GAP-08`) is read as binding the
  fixture's identifier scheme, although the text scopes it to new schemes.
- **CVSS completeness** (`GAP-34`, `35`) rests on the CVSS v2 and v3.1
  documents (library records `first-cvss` and `first-cvss-v3-1`), cited, not
  quoted.
- **Ubuntu 22.04 is LTS** (`GAP-26`) because the text's own example says so.
- **The OSV example is valid** (`SRC-L1635`), reading the versions list as
  recommended; the other reading is recorded in `readings`.
- **The limit examples are judged on their literal values** (invalid: X and Y
  are not hashes), although they are illustrations.
- **Ten cases are left unspecified** (`EDGE-01` to `04`, `EDGE-06` to `10`,
  `EDGE-12`) rather than forced: GIT as an ecosystem, extra keys in events,
  unknown fields at either level, an empty top-level severity next to
  package-level severity, an unlisted severity source or reference type,
  uppercase hashes, and a Git entry without versions. `EDGE-05`, a null
  top-level severity next to package-level severity, was left unspecified in
  pass 1; pass 3 made it invalid, because a null severity is not a JSON array,
  the reason `GAP-39` is invalid.
- **The purl recommendation is not repeated.** Line 967 recommends a `purl`
  (rule `purl-recommended`, R-0079). The base record has none, so nearly every
  derived record breaks that recommendation; `breaks_should` lists it only for
  the nine complete source examples, none of which has a purl.
- **`FreeBSD:base:14.3`** is validated as an ecosystem string and **`v3.16`**
  as `Alpine:v3.16`, the forms the examples stand for.
- **Trailing commas** are removed mechanically before the seven non-JSON
  examples are validated or embedded; `trailing_commas_removed` records how
  many.
- **The fixed vulnerability example has no record of its own**: its range is
  the base record's npm range, which `POS-02` records with `embeds`.

## Reproduce

From the repository root. The run recorded here used Python 3.13.9; other
versions may word JSON parse errors differently, and the script notes any
version that differs from `tools` in `expected.yaml`.

```sh
python3 -m venv /tmp/osv-examples-venv    # any directory outside the repository
/tmp/osv-examples-venv/bin/pip install jsonschema==4.26.0 referencing==0.37.0 \
  jsonschema-specifications==2025.9.1 rfc3339-validator==0.1.4 rfc3987==1.3.8 PyYAML==6.0.3

# the source, never committed (CLAUDE.md); .cache/ is gitignored
C=c8a57bdc5b0bc54646e140cabbb7834bd0b5aec9
mkdir -p .cache/osv-schema-v1.9.2/docs .cache/osv-schema-v1.9.2/validation
curl -L -o .cache/osv-schema-v1.9.2/docs/schema.md https://raw.githubusercontent.com/ossf/osv-schema/$C/docs/schema.md
curl -L -o .cache/osv-schema-v1.9.2/validation/schema.json https://raw.githubusercontent.com/ossf/osv-schema/$C/validation/schema.json
shasum -a 256 .cache/osv-schema-v1.9.2/docs/schema.md .cache/osv-schema-v1.9.2/validation/schema.json
# 96d82f03d763fb408bc344d01fc271f761a81cc225f6f6a42d318e3ed21cebff  docs/schema.md
# 15b10dbb4c4e31c7aae11d22cdd991a9a374758db7c8389e62b3cc37cac92653  validation/schema.json

/tmp/osv-examples-venv/bin/python -I records/openssf/osv-schema/distilled/examples/run-fixtures.derived.py
/tmp/osv-examples-venv/bin/python -I records/openssf/osv-schema/distilled/examples/run-fixtures.derived.py --json
```

`--schema` and `--source` take other paths to the same two files; the script
refuses bytes whose SHA-256 differs. The first command checks everything and
prints
`224 fixtures; 47 where a tool differs from the expected result (each names a finding); 0 problems`.
Before comparing results it checks that each `verbatim/blocks/` file equals
the lines between its fences, that each `verbatim/inline/` example occurs on
its line, that each quoted rule occurs verbatim at the lines and under the
heading its locator names, that each prose list in `enumerations` is what the
source holds, and that each derived record differs from its parent only where
`mutations` says. Without the source text those checks are skipped and
reported; the JSON Schema is always needed. The second command prints the
recomputed results as JSON. With `node` on `PATH` the ECMA-262 checks run
too; without it they are skipped and reported.

Versions recorded in this run: Python 3.13.9, jsonschema 4.26.0
(referencing 0.37.0, jsonschema-specifications 2025.9.1), rfc3339-validator
0.1.4 (makes `date-time` checkable), rfc3987 1.3.8 (makes `uri` checkable),
PyYAML 6.0.3, Node v22.23.2.

`expected.yaml` parses identically with the library's reader and PyYAML
(every scalar is a quoted string or a block scalar; there are no flow
mappings):

```sh
python3 -I -c "import sys, yaml; sys.path.insert(0, 'bin'); from _yaml import parse; t = open('records/openssf/osv-schema/distilled/examples/expected.yaml', encoding='utf-8').read(); assert parse(t) == yaml.safe_load(t); print('identical')"
```

## Not transcribed

| source | why |
|---|---|
| line 144 `<DB>-<ENTRYID>`, line 1005 `+echo.<N>`, line 1008 `{owner}/{repo}`, line 1012 `_N`, line 1017 `groupId:artifactId`, line 1032 `Root:{BaseDistro}:{Version}`, `Root:{PackageManager}`, `root-{package}`, `@root/{package}`, line 1039 `<publisher>.<name>` | templates with placeholders, not values |
| lines 1135 to 1138, `{"introduced": string}` and its three siblings | informal shapes inside a list, with no values |
| lines 179 to 710, the Source URL and OSV Formatted URL entries of the prefix table | URL templates with `<ID>` placeholders; the prefixes themselves are compared in the `id-prefixes` enumeration |
| line 959 `*`, line 1015 `Kernel` | single values a rule allows (the wildcard name, the only Linux name); exercised by `POS-17` and `GAP-28` |
| line 1006 `:ports`, `:base`, `:kernel`; line 1037 `:LTS`, `:Pro:` | suffix parts named by a rule; the full ecosystem strings the same lines give as examples are transcribed |
| line 160, spaces, slashes, backslashes, parentheses, exclamation marks | examples of forbidden characters, not ids; each became one of `GAP-01` to `05` |
| line 168, `SQLI`, `RCE`, `LOG4J`, `CRITICAL`, `HIGH` | examples of what an id must not describe, not ids; used for `GAP-08` |
| lines 1151 and 1153, `"0"` and `"*"` | special values inside rules; exercised by `POS-13`, `OVER-01`, `SHOULD-04` and the `{ "limit": "*" }` event, which is transcribed |
| line 1005 `Echo:PyPI`, `Echo:Maven`, `Echo:npm`, `Echo:NuGet`; line 1041 `:Core`, `:Plugin`, `:Theme`; lines 2003 to 2010 the SoC vendors; the type and source tables and lists | closed lists of allowed values, not examples; compared in `enumerations` or used by derived records |
| line 1012 `homebrew/core`, line 1017 `https://repo.maven.apache.org/maven2`, line 1025 `https://packagist.org`, line 1038 `microsoft/vcpkg`, line 1039 `https://marketplace.visualstudio.com/vscode` | defaults that apply when a suffix is absent, not examples |
| line 1029 `cpe:/a:redhat:rhel_aus:8.4::appstream` | a CPE, the stated translation of the Red Hat example; kept in the note of `SRC-L1029-1` (S-04) |
| line 1012 `pkg:brew`, line 1038 the vcpkg field `port-version` and the purl qualifiers `port_version`, `repository_url`, `repository_revision`, line 1192 `git clone`, line 1370 `git rev-list X..Y`, line 1454 `app.any.run` | purl names, commands and a site name, not OSV field values |
| lines 1355 to 1356 and 1369, `X, A, B, C, D, E, F` and `X, A, B, C` | stated results of the limit examples; quoted as rules `meaning-git-fixed` and `meaning-git-limit` |
| line 1342 `images/git_graph.png` | a picture outside `docs/schema.md` (S-11) |
| lines 1543 to 1547, Go vulnerability | the section has no example of its own; it points to go.dev |
| line 128 `1.0.0`; lines 131 to 132, 1.2.0 and 1.3.0 | the default schema version and versions inside an illustration, not record examples |
| line 105 TOML, YAML; lines 1439 to 1442 YARA rules, Twitter, Mastodon, Hacker News, Reddit; line 1430 `https://`; names of tools, files, fields and classes inside descriptions (line 1003 `distro-info-data`, line 1006 `pkg(8)`, line 1012 `brew info`, `PkgVersion`, `Version`, line 1022 `LTS`, `SP`, line 1023 `/etc/os-release`, `PRETTY_NAME`, line 1039 `Publisher`, `Id`, `Identity`, `itemName`) | words inside descriptions |
