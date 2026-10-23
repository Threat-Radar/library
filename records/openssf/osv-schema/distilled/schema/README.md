---
record: osv-schema
kind: schema
title: "osv-schema: schemas (two verbatim, two derived)"
extracted: "2026-10-18"
reviewed_by: ""
---

# osv-schema: schemas

Contains text from the OSV Schema v1.9.2 (https://github.com/ossf/osv-schema, tag v1.9.2), Apache License 2.0.

This README is derived: the library wrote it. Of the files beside it, only
`osv.schema.json` and `vulnerability.proto` carry the source's own bytes.

## What OSV ships, and how the three parts relate

OSV Schema v1.9.2 (git tag `v1.9.2`, commit
`c8a57bdc5b0bc54646e140cabbb7834bd0b5aec9`) states its format three times:

| part | repository path | what the source says it is |
|---|---|---|
| prose | `docs/schema.md` (2010 lines) | "This document defines a standard interchange format for describing vulnerabilities in open source packages." (L19-L20) |
| JSON Schema | `validation/schema.json` | "A JSON Schema for validation is also available" (L43) |
| protobuf | `proto/vulnerability.proto` | "The protobuf representation is *NOT* stable and only used for implementing the JSON based API." (proto L193-L194) |

The repository's root `schema.md` is only a pointer: "Moved to <https://ossf.github.io/osv-schema>."
In this README, `Lnnn` is a line of `docs/schema.md` at v1.9.2, `JSON Lnnn` a
line of `osv.schema.json` and `proto Lnnn` a line of `vulnerability.proto`.

None of the three says which one governs when they disagree. This library
reads the prose as the definition, because it says it defines the format and
calls itself "only about the JSON encoding the database serves to consumers"
(L102-L103), while it offers the JSON Schema "for validation" and the proto
disowns stability. `../messages.yaml` therefore gives the prose value of every
type, required-ness, allowed value and format, and lists each disagreement
with all three values. Two further cautions:

- The prose links the JSON Schema on the `main` branch (L44), and the schema's
  own `$id` also names `main` (JSON L3). Neither names a version, so a reader
  who follows either link gets whatever `main` holds. The copy here is the
  file at tag `v1.9.2`.
- The prose says "This format is stable, but further backwards compatible
  changes may still be made." (L29). The JSON Schema is closed at the top
  level (D1), so a backwards compatible addition of a top-level field makes
  older validators reject newer records.

## Files

| file | verbatim or derived | source | SHA-256 of the file as written | what it is |
|---|---|---|---|---|
| `osv.schema.json` | **verbatim**: bytes unchanged | `validation/schema.json` at tag `v1.9.2` | `15b10dbb4c4e31c7aae11d22cdd991a9a374758db7c8389e62b3cc37cac92653` | JSON Schema (draft 2020-12) for one OSV record |
| `vulnerability.proto` | **verbatim**: bytes unchanged | `proto/vulnerability.proto` at tag `v1.9.2` | `1c5a7af863c576398e333358c006d30577dd111c810416cd2f3fc0cecd20a070` | proto3 messages of package `osv`, the representation behind the OSV JSON API |
| `osv-prose.derived.schema.json` | **derived**: written by this library | `docs/schema.md` prose | `e4889e9aea8224ec16dc4efa4503d741c427db737da29485d60e512629f83a6a` | rules P01 to P12: stated rules that neither verbatim file enforces; a failure is an error |
| `osv-recommended.derived.schema.json` | **derived**: written by this library | `docs/schema.md` prose | `470a7a8b676963287d0b19af2805b42fde4eef881f6c20e0c95dcf8b9c614cd2` | rules S01 to S10: should and recommended statements; a failure is a warning |
| `README.md` | derived (this file) | none | not listed: a file cannot state its own digest | |

Naming. A file in `distilled/schema/` that the library wrote carries the infix
`.derived.` before its extension and says "derived" in its first 12 lines; an
unmarked filename asserts that the file is the source's own bytes. Both derived
files follow it: their line 3 is a `$comment` that begins `DERIVED - not
verbatim`. The verbatim JSON Schema is renamed from `schema.json` to
`osv.schema.json` to follow the `*.schema.json` convention of
`docs/extraction.md`; the proto keeps its name.

Every structure and field these files govern is decomposed in
`../messages.yaml` (13 structures, 47 fields), with the prose, JSON Schema and
proto value of each side by side. `../state-machine.yaml` models the
evaluation of a range and the lifecycle of a record.

## Provenance of the verbatim files

- Copied on 2026-10-18 from the local copies pinned for this extraction at
  tag `v1.9.2`. After copying, the SHA-256 of each file
  equals the pinned digest above and `cmp` finds no difference.
- Git blob ids, computed locally with `git hash-object` (no network):
  `osv.schema.json` `13f42fbea5372ef4a1e43e53993263fdb7b3d396`,
  `vulnerability.proto` `9ed3e4ad78f8ad6a01e94561f0244d15fb0ff3e0`. A later
  pass can compare them with the ids the GitHub API lists for the two paths at
  the tag; this pass did not query it.
- `osv.schema.json`: 16,868 bytes, 584 lines, ASCII only, LF line ends with a
  final newline, no tabs, no trailing spaces. It declares
  `https://json-schema.org/draft/2020-12/schema` (JSON L2);
  `Draft202012Validator.check_schema` passes (jsonschema 4.26.0). All 11 of its
  `pattern` values compile as ECMA-262 regular expressions with and without the
  `u` flag (node 22.23.2).
- `vulnerability.proto`: 7,728 bytes, 234 lines, UTF-8 (the `id` comment, proto
  L198-L201, holds three pairs of curly quotes, U+201C and U+201D), LF line ends
  with a final newline. `protoc` 29.3 compiles it, with the
  `google/protobuf/struct.proto` and `google/protobuf/timestamp.proto` it
  imports; the field numbers, labels, types and JSON names in `../messages.yaml`
  come from that compiled descriptor.
- Licence: the proto keeps its own header, Copyright 2025 Google LLC under the
  Apache License 2.0 (proto L1-L13). A JSON file cannot carry a notice without
  changing its bytes; the attribution line at the top of this README covers
  `osv.schema.json`.

## Validating a record offline

With jsonschema installed (run here with jsonschema 4.26.0, rfc3339-validator
0.1.4 and rfc3987 1.3.8 on Python 3.13.9), from the repository root:

```sh
python3 -I - records/openssf/osv-schema/distilled/schema my-record.json <<'EOF'
import json, os, sys
from jsonschema import Draft202012Validator as V
d = sys.argv[1]
load = lambda n: json.load(open(os.path.join(d, n), encoding="utf-8"))
fc = V.FORMAT_CHECKER
checks = [("ERROR", None, V(load("osv.schema.json"), format_checker=fc))]
for name, level in (("osv-prose.derived.schema.json", "ERROR"),
                    ("osv-recommended.derived.schema.json", "WARN")):
    s = load(name)
    for k, rule in s["$defs"].items():
        if "title" in rule and k[:1] in "PS":
            checks.append((level, rule["title"],
                           V({"$defs": s["$defs"], "$ref": f"#/$defs/{k}"}, format_checker=fc)))
rc = 0
for path in sys.argv[2:]:
    rec = json.load(open(path, encoding="utf-8"))
    for level, title, v in checks:
        for e in v.iter_errors(rec):
            where = "/".join(map(str, e.absolute_path)) or "(root)"
            print(os.path.basename(path), level, where, title or e.message[:100])
            rc |= level == "ERROR"
sys.exit(rc)
EOF
```

It needs no network: every `$ref` is local and jsonschema bundles the 2020-12
metaschema. The exit status is 1 if any record has an error (the verbatim
schema or a P rule); warnings (S rules) do not change it. Output for the
Python example of the prose (L1713-L1755) and for a record built to break
four P rules:

```
ex-L1714.json WARN affected/0/package S06 affected[].package: purl is present
ex-L1714.json WARN affected/0 S09 affected[]: GIT ranges are not mixed with SEMVER or ECOSYSTEM ranges in one entry
bad-record.json ERROR modified 'x 2021-01-01T00:00:00Z' is not a 'date-time'
bad-record.json ERROR id P01 id: only ASCII letters, digits and the characters : _ . -
bad-record.json ERROR modified P02 modified, published, withdrawn: the whole value is an RFC 3339 timestamp in UTC ending in Z
bad-record.json ERROR affected/0/ranges/0/events/0/introduced P03 SEMVER ranges: event versions are SemVer 2.0.0 with no leading v (introduced may be 0; limit may contain *)
bad-record.json ERROR affected/0/package/ecosystem P07 ecosystems whose suffix the prose says must be present
bad-record.json WARN affected/0/package S06 affected[].package: purl is present
```

Cautions for anyone wiring these schemas into a test harness:

- **Format.** In draft 2020-12, `format` is an annotation unless the validator
  asserts it. Without `format_checker`, jsonschema ignores `date-time` and
  `uri`, and `osv.schema.json` then accepts `x 2021-01-01T00:00:00Z y` as a
  `modified` value (D10); P02 rejects it either way. With the checker,
  `date-time` needs rfc3339-validator and `uri` needs rfc3987 or
  rfc3986-validator; if neither is importable the check is skipped silently.
- **Regular expressions.** JSON Schema patterns are ECMA-262; jsonschema runs
  them with Python's `re.search`. Python's `$` also matches before a final
  newline, so `GHSA-1` followed by a newline passes `^[a-zA-Z0-9:_.-]+$` under
  Python and fails under ECMA-262 (checked with node). This affects every
  anchored pattern of both the verbatim and the derived schemas. The derived
  schemas write digits as `[0-9]`, never `\d`, which in Python also matches
  non-ASCII digits.
- **Errors in the verbatim schema's conditions.** The range conditions of
  `osv.schema.json` (JSON L162-L271) test `type` and `events` without requiring
  them, so a range with no `type` also reports the GIT errors (`repo` required)
  and a range with no `events` reports the `last_affected` exclusion. The
  verdict does not change, because both members are required anyway; only the
  error list is longer.

## Where the three sources disagree

36 disagreements, D1 to D36. `../messages.yaml` carries each one, with the
same id and all three values, at the structure or field it concerns. The
category column says what differs: fields and structures, types,
required-ness, defaults, patterns and formats, enumerations, or meaning.
"Derived" names the rule that checks the prose side where a schema can.

| id | category | aspect | prose (docs/schema.md) | JSON Schema (osv.schema.json) | proto (vulnerability.proto) | derived |
|---|---|---|---|---|---|---|
| D1 | structure | closure of the record | clients read newer versions "by ignoring any unexpected fields" (L132) | root `additionalProperties: false` (JSON L583): an unknown top-level field is invalid; nested objects stay open | not expressed in the file | none |
| D2 | required-ness | `schema_version` | required "For schema versions above 1.0.0" (L721-L722) | optional (not in `/required`, JSON L368-L371) | no label (proto L196) | none: not checkable on a record (see gaps) |
| D3 | default | `schema_version` | assumed `1.0.0` when absent (L128-L129) | no `default` | none; proto3 reads an unset string as empty | none |
| D4 | pattern | `schema_version` | SemVer 2.0.0, no leading v (should, L126-L128) | any string | any string | S01 |
| D5 | pattern | `id` character set | must match `^[a-zA-Z0-9:_.-]+$` (L154-L157) | only `$defs/prefix` (JSON L468), anchored at the start only: `x_`, `x_a b/c` and `GHSA-a/b` are valid | any string | P01 |
| D6 | enumeration | `id` prefixes | 59 codes (L179-L710), with `CleanStart`, without `FreeBSD` | 60 prefixes once `SUSE-[SRFO]U` is expanded (JSON L468): `CLEANSTART` instead of `CleanStart`, and `FreeBSD`; case sensitive | no list | none |
| D7 | pattern | separator after the prefix | `<DB>-<ENTRYID>` (L144) but "followed (ideally) by a `-` separator" (L169) | a listed prefix must be followed by `-`; `x_` by nothing | none | none |
| D8 | required-ness | `summary`, `details`, `affected` | optional (L722) | optional | `Required.` (proto L217, L220, L222) | none |
| D9 | pattern | `summary` length | "on the order of no more than 120 characters" (L824-L825), recommended | none | "recommended to keep this under 120 characters" (proto L217-L218) | S02 |
| D10 | type, pattern | `modified`, `published`, `withdrawn` | RFC 3339, UTC, ending in Z (L716-L717, L734-L735, L745-L746) | string, `format: date-time`, pattern without `^` and `$` (JSON L577-L581) | `google.protobuf.Timestamp` (proto L204, L206, L209) | P02 |
| D11 | type | null for arrays | every list is a JSON array | `aliases`, `affected`, `references` and both `severity` arrays also accept `null`; the other arrays do not | `repeated`: no null; empty equals absent | P12 (pass 3) |
| D12 | pattern | `aliases[]` | "in the form of the `id` field" (L758-L759) | any string | any string | P05 |
| D13 | meaning | `related` | similar but different vulnerabilities, or cases outside `aliases` and `upstream` (L807-L810) | no description | "such as the same problem in alternate ecosystems" (proto L212-L213) | none |
| D14 | structure | top-level versus package `severity` | package-level set excludes top-level (L1071-L1073); "set" undefined for `null` or `[]` | a present top-level key, even `null` or `[]`, forbids any non-null package-level `severity` (JSON L372-L393) | not expressible | none |
| D15 | enumeration | `severity[].type` | 4 values (L863-L866) | the same 4 | the same plus `UNSPECIFIED = 0` | none |
| D16 | enumeration | `severity[].source` | 3 values in a table, not declared closed (L876-L886) | closed enum of 3 | enum of 3 plus `SOURCE_UNSPECIFIED = 0` | none |
| D17 | pattern | CVSS scores | CVSS_V3 ">= 3.0 and < 4.0", CVSS_V4 ">= 4.0 and < 5.0" (L864-L865) | only `CVSS:3.0`, `CVSS:3.1` and `CVSS:4.0`; incomplete or repeated v2 and v3 metrics pass | any string | none |
| D18 | enumeration | Ubuntu score | "A lowercased string representing the" Ubuntu priority (L866), no list | enum `negligible`, `low`, `medium`, `high`, `critical` (JSON L559-L565) | any string | none |
| D19 | required-ness | `affected[].ranges` | optional | optional | `Required.` (proto L107) | none |
| D20 | required-ness | `affected[].versions` | generally recommended (L937); "must" where versions cannot be ranges (L945-L946); SEMVER removes, GIT does not remove, "the requirement" (L1104, L1127) | optional | `Optional.` (proto L109) | S03, S04, S05 |
| D21 | enumeration | `GIT` as an ecosystem | not in the table (L988-L1042), yet called a pseudo-ecosystem (L1065, L1081) | accepted, with any suffix (JSON L462) | free string | none |
| D22 | pattern | ecosystem suffixes | per ecosystem: required, forbidden, closed list, numeric, no trailing slash (L990-L1041) | any `:.+` suffix or none, for every ecosystem | free string | P07, P08, P09 |
| D23 | pattern | package name forms | per ecosystem: `Kernel`, `:linux_kernel:` vendors, `groupId:artifactId`, `<publisher>.<name>`, `{owner}/{repo}`, normalized PyPI names, `wordpress` (L993-L1041, L2001-L2010) | any string | any string | P10 |
| D24 | pattern | `package.purl` | a Package URL "without the `@version` component" (L966) | any string | any string | P06 |
| D25 | enumeration | `ranges[].type` | 3 values | the same 3 | the same plus `UNSPECIFIED = 0` | none |
| D26 | meaning | `ranges[].database_specific` | information "about the range" (L1203) | no description | "about the vulnerability" (proto L98-L99) | none |
| D27 | structure | one type per event | "Only **a single type**" (L1159) | `oneOf`: exactly one of the four, other keys allowed (JSON L108-L153) | four independent fields, no `oneof`: several may be set | none needed |
| D28 | pattern | GIT event values | full-length hashes (L1122-L1123); `0` only for `introduced`; `limit` may contain `*` | `^(0\|[a-f0-9]{40}\|[a-f0-9]{64})$` for all four: `limit` `*` and upper-case hex invalid, `0` valid everywhere (JSON L177-L244) | any string | P04 |
| D29 | pattern | SEMVER event values | SemVer 2.0.0, no leading v (L1098-L1099) | any string | any string | P03 |
| D30 | meaning | several `introduced` events | allowed (example L1325-L1333) | at least one, no maximum | comment: "The earliest version/commit where this vulnerability was introduced in." (proto L71-L72) | none |
| D31 | enumeration | `references[].type` | 10 values (L1436-L1455) | 11: also `GIT` | 12: also `GIT = 11` and `NONE = 0` | none |
| D32 | format | `references[].url` | "the fully-qualified URL (including the scheme" (L1429) | `format: uri`, asserted only on request | any string | none (format) |
| D33 | enumeration | `credits[].type` | 10 values (L1496-L1505) | the same 10 | the same plus `UNSPECIFIED = 0`, numbered from `OTHER = 1` | none |
| D34 | pattern | `credits[].contact[]` | "should be a valid, fully qualified, plain-text URL" (L1487) | any string | any string ("Contact methods (URLs).") | S07 |
| D35 | structure | `Commit` message | absent | absent | `message Commit`, deprecated, used by no field (proto L24-L53) | none |
| D36 | required-ness | required fields in the proto | `id`, `modified`, `package.ecosystem`, `package.name`, `ranges[].type`, `references[]` members, `credits[].name`, `severity[]` type and score | the same, as `required` lists | proto3 cannot require; the comments say `Required.` for the package, range and reference members, and nothing for `id`, `modified`, `credits[].name` or the severity members | none |

Not a disagreement but worth knowing: the 52 ecosystem names of the prose
table (L990-L1041) and the `$defs/ecosystemName` enum of the JSON Schema
(JSON L395-L453) are the same list in the same order; the reference types,
credit types, severity types and sources, and range types agree between prose
and JSON Schema except as listed above. Every JSON name in the proto equals the
JSON Schema property name, the deprecated `Commit` aside (six fields set
`json_name` explicitly: proto L79, L100, L113, L116, L197, L229).

## Observations within one source

Pass 3 (cross-check) found each recorded in `../design-notes.md` as a source
defect (O1: 6; O2: 20; O3 and O4: 22; O5: 5; O6 and O8: 16; O7: 10; O9: 7
and 8); none changes a value above.

- **O1.** `$defs/ecosystemName` (JSON L395-L453) and `$defs/ecosystemSuffix`
  (JSON L454-L457) are defined and never referenced; `ecosystem` uses
  `$defs/ecosystemWithSuffix`.
- **O2.** The JSON Schema leaves every nested object open: an event such as
  `{"introduced": "0", "x": 1}` is valid, as are unknown members of
  `package`, `affected`, ranges, severities, references and credits. The prose
  says nothing for or against extra members there.
- **O3.** L1194-L1196 says "The range object defines the fields `type`,
  `events`, `repo`.  `introduced`, `fixed`, and additional type-specific
  fields as needed."; every other passage, both schemas and all examples put
  `introduced` and `fixed` on event objects.
- **O4.** The Format Overview shows `ranges[].database_specific` (L83); the
  block of the affected fields section (L903-L912) leaves it out.
- **O5.** The prefix table asks to be kept alphabetically sorted (comment at
  L177) and is not: ASB-A comes before ALSA, ALSA before ALPINE, MGASA before
  MAL, RHSA before RHLW, RSEC before ROOT, and CLSA is last. The CleanStart
  row has an empty database link (L278).
- **O6.** Six of the seven range snippets (L1302, L1315, L1350, L1364, L1392,
  L1408), the credits block (L1464) and the credits example (L1522) end an
  array or object with a trailing comma, so they are not valid JSON as
  printed. The nine complete example records (L1553 to L1995) parse and are
  valid against `osv.schema.json` and `osv-prose.derived.schema.json`.
- **O7.** L937 only recommends a `versions` list, while L1104-L1105 and
  L1127-L1128 speak of "the requirement" to give one.
- **O8.** The Python example (L1713-L1755) puts a `GIT` range and an
  `ECOSYSTEM` range in one PyPI entry, which L1056 recommends against (S09).
- **O9.** The evaluation pseudocode matches `affected.package == pkg`
  (L1250), so an entry with no `package`, the recommended Git entry (L1059),
  never matches. It also sorts events, which needs a total order; for GIT
  ranges `u < v` is the ancestor relation (L1124-L1125), a partial order. See
  `../state-machine.yaml`, machine `range-evaluation`.

## The derived schemas

Both are JSON Schema draft 2020-12, use only local `$ref`s, and are meant to be
applied **in addition to** `osv.schema.json`: they add checks and never relax
one. Each rule is one entry of `$defs`; its `title` starts with the rule id and
its `$comment` quotes the source lines it enforces, checked character for
character against `docs/schema.md` when the file was generated. Conditions use
`if` with `required`, so an absent member never triggers a rule by accident.

### `osv-prose.derived.schema.json`: stated rules (errors)

| rule | checks | statement it enforces | requirements (pass 3) |
|---|---|---|---|
| P01 | `id` matches `^[a-zA-Z0-9:_.-]+$` | "the `id` field must strictly use ASCII characters matching the regular expression:" (L154), with the expression at L157 | R-0012, R-0013, R-0014 |
| P02 | `modified`, `published`, `withdrawn` match the timestamp pattern of the JSON Schema with `^` and `$` | "as an RFC3339-formatted timestamp in UTC (ending in "Z")." (L716-L717); the same words for `published` (L735, "time stamp") and `withdrawn` (L746) | R-0022, R-0028, R-0029 |
| P03 | in SEMVER ranges, `fixed` and `last_affected` are SemVer 2.0.0 versions; `introduced` is `0` or one; `limit` is one or contains `*` | "The versions `introduced` and `fixed` are semantic versions as defined by [SemVer 2.0.0](https://semver.org), with no leading "v" prefix." (L1098-L1099), L1143-L1144, L1151-L1153 | R-0164, R-0175, R-0177, R-0178 |
| P04 | in GIT ranges, `fixed`, `last_affected` and `limit` are not `0` | "The versions `introduced` and `fixed` are full-length Git commit hashes." (L1122-L1123), with the special value of L1151-L1152 | R-0171, R-0177 |
| P05 | each `aliases[]` item matches the P01 character set | "in the form of the `id` field" (L759) | R-0012, R-0032 |
| P06 | `package.purl` starts with `pkg:` and has no `@` before `?` or `#` | "without the `@version` component" (L966) | R-0078 |
| P07a to P07d | Alpine `:v` suffix; Mageia, Photon OS and Red Hat Lightwell suffix present; Lightwell's suffix is one of the 52 ecosystem names | "The ecosystem string must have a" suffix (L992, L1016, L1026); "The ecosystem **must** have a suffix matching an existing OSV ecosystem" (L1030) | R-0085, R-0113, R-0124, R-0128 |
| P08a to P08h | a suffix is present for Alpaquita, Azure Linux (numeric), BellSoft Hardened Containers, openEuler, openSUSE, Red Hat, SUSE, Ubuntu (`:[Pro:]YY.MM[:LTS]`) | "The ecosystem string has a" suffix (L991, L994, L995, L1022, L1023, L1029, L1034, L1037) | R-0083, R-0088, R-0089, R-0119, R-0120, R-0127, R-0133, R-0136, R-0137, R-0138 |
| P09a to P09i | AlmaLinux, Rocky Linux, TuxCare: an optional numeric suffix; Echo: only `:PyPI`, `:Maven`, `:npm`, `:NuGet`; WordPress: only `:Core`, `:Plugin`, `:Theme`; vcpkg: no suffix; Maven, Packagist, VSCode: no trailing slash | L990, L1031, L1036 ("`<RELEASE>` is a numeric version."); "The supported values are" (L1005); L1041; "The ecosystem string has no release suffix." (L1038); "without a trailing slash" (L1017, L1025, L1039) | R-0082, R-0099, R-0114, R-0122, R-0130, R-0135, R-0139, R-0140, R-0142 |
| P10a to P10g | `name` is `Kernel` for Linux; an Android `:linux_kernel:` name ends in nothing or a listed vendor; Maven `groupId:artifactId`; VSCode `<publisher>.<name>`; GitHub Actions `{owner}/{repo}`; PyPI normalized; `wordpress` for `WordPress:Core`; every form exempts the wildcard name `*` (L959-L960) | "The only supported `name` is `Kernel`." (L1015); L993, L2001-L2010; L1017; L1039; L1008; L1028; L1041 | R-0077, R-0087, R-0104, R-0111, R-0114, R-0126, R-0140, R-0142, R-0224 |
| P11 | `summary` has no line feed or carriage return (added in pass 3; S02a until then) | "The `summary` field gives a one-line, English textual summary of the vulnerability." (L823-L824) | R-0043 |
| P12 | `aliases`, `affected`, `references`, `severity` and `affected[].severity` are not `null` (added in pass 3) | "The `aliases` field gives a list of IDs" (L758); "The `affected` field is a JSON array" (L920); "The `references` field contains a list of JSON objects describing references." (L1427); "The `severity` field is a JSON array" (L851), which L1069 applies to `affected[].severity` | R-0032, R-0050, R-0063, R-0152, R-0205 |

That is 36 checks in 12 rules; P11 and P12, added in pass 3, count one check each.

### `osv-recommended.derived.schema.json`: recommendations (warnings)

| rule | checks | statement it enforces | requirements (pass 3) |
|---|---|---|---|
| S01 | `schema_version` is a SemVer 2.0.0 version, no leading v | "The value should be a string matching the OSV Schema version" (L126-L127) | R-0006 |
| S02 | `summary` has at most 120 characters | "It is recommended that this field be kept short, on the order of no more than 120 characters." (L824-L825); until pass 3 also one line (S02a), now P11 | R-0044 |
| S03 | an affected entry has `versions`, unless it has a SEMVER range | "The `versions` list is generally recommended to always be present" (L937), with the SEMVER exemption of L1104-L1105 | R-0069, R-0167 |
| S04 | an entry with an ECOSYSTEM range has `versions` | "It is recommended that you provide an explicitly enumerated `versions` list when specifying one or more `ECOSYSTEM` ranges" (L1114-L1115) | R-0170 |
| S05 | an entry with a GIT range has `versions` | "Specifying one or more `GIT` ranges does NOT remove the requirement to specify an explicitly enumerated `versions` list" (L1127-L1128) | R-0173 |
| S06 | `package.purl` is present | "This field is optional but recommended." (L967) | R-0079 |
| S07 | each `credits[].contact[]` item is a URI with a scheme | "should be a valid, fully qualified, plain-text URL" (L1487) | R-0217 |
| S08 | SEMVER and ECOSYSTEM ranges have no `limit` event | "`limit` events are typically not necessary for describing numbered (linear) version ranges and should not be used." (L1337-L1338) | R-0202 |
| S09 | no affected entry mixes GIT ranges with SEMVER or ECOSYSTEM ranges | "it is recommended to use separate entries in the `affected` array." (L1056) | R-0145, R-0159 |
| S10 | an affected entry with no `package` has only GIT ranges | "This entry should use **no** `package` field. It should use the `GIT` range type" (L1059) | R-0148, R-0149 |

### Readings (judgement calls for a reviewer)

- **R1.** The rows that say the ecosystem string "has a" suffix (P08) are read
  as requirements, like the rows that say it "must have a" suffix (P07): both
  describe the form of the string, and the rows with an optional suffix say it
  "might optionally have" one. A reviewer who reads "has" as descriptive
  should drop P08.
- **R2.** "in the form of the `id` field" (P05) is read as the character set of
  P01, not the prefix list, which the JSON Schema does not apply to aliases
  either.
- **R3.** Red Hat Lightwell's suffix (P07d) may carry the named ecosystem's own
  suffix (`Red Hat Lightwell:Maven:...`); the prose does not say.
- **R4.** The openEuler suffix (P08d) is written `<RELEASE>` without the colon
  (L1022); P08d requires the colon, as the JSON Schema does for every suffix.
- **R5.** The WordPress (P09e) and Echo (P09d) suffix lists are read as closed.
- **R6.** P10f's pattern is a PEP 508 project name after PEP 503
  normalization, as the prose's link (L1028) suggests; neither PEP is part of
  this source.
- **R7.** P04 reads the special value `0` as reserved for `introduced`
  (L1151-L1152) and GIT `limit` as a hash; the prose also lets `limit` contain
  `*` (L1153), which the JSON Schema rejects in GIT ranges (D28), and a
  derived schema cannot relax the verbatim one.
- **R8.** S08 reads "numbered (linear) version ranges" as SEMVER and ECOSYSTEM,
  as against GIT.
- **R9.** S10 reads an entry with no package as a Git entry.
- **R10.** S02 uses 120 as a hard lint limit where the prose says "on the
  order of".
- **R11.** P10 exempts the wildcard name `*`: "Use the wildcard package name
  `*` to indicate that an advisory affects all packages within the specified
  `ecosystem`." (L959-L960) names no ecosystem, so it is read as an exception
  to each row's name form. For `Linux`, whose row says "The only supported
  `name` is `Kernel`." (L1015), the prose does not reconcile the two rules;
  P10a accepts both `Kernel` and `*` rather than decide. (Added in pass 2,
  2026-10-19: as written in pass 1, P10 rejected `*` for six ecosystems.)
- **R12.** P11 and P12 read definitions as binding, as P05 and P06 do: a
  summary is "a one-line" summary (L823), and `aliases`, `affected`,
  `references` and both `severity` fields are lists or arrays, so `null` is
  not allowed (L758, L851, L920, L1069, L1427). The examples read them the same
  way (GAP-36 to GAP-40). (Added in pass 3, 2026-10-19.)
- **R13.** S05 keeps a warning for R-0173, which `../requirements.yaml`
  records as a requirement: L1127-L1128 call the `versions` list "the
  requirement", but the text states it elsewhere only as a recommendation
  (L937). This is a source defect (`../normative.md` U-2; `../design-notes.md`
  defect 10); the examples leave it open (EDGE-10). (Added in pass 3.)

### What no schema here checks

Rules the prose states that neither verbatim file nor a derived schema
expresses, with the reason:

- `schema_version` required "For schema versions above 1.0.0" (L721-L722, R-0026): a
  record without it reads as 1.0.0 (L128-L129), so the condition is never
  observable on the record.
- IDs "should be semantically neutral" (L166-L168, R-0016, R-0017): an open-ended semantic
  rule, scoped to new identifier schemes.
- `aliases` symmetric and transitive (L768-L769, R-0034), `upstream` transitive and
  not symmetric (L795-L797, R-0039, R-0040), `related` symmetric (L812, R-0042), and the CVE alias
  prohibition for distributions (L773-L776, R-0036): relations across records.
- One affected entry per package (L924-L926, R-0065): uniqueness of a member across
  array items.
- Non-overlapping SEMVER ranges (L1101-L1102, R-0166) and sorted events (L1183-L1184, R-0190):
  need version ordering.
- `versions` required for products whose versions cannot be ranges
  (L945-L946, R-0071): no record says which products those are.
- `fixed` events for every cherry-picked fix (L1175-L1177, R-0186), `fixed` preferred
  over `last_affected` and `limit` (L1164, L1179-L1180, R-0183, R-0188): judgement about the
  repository history.
- `details` as CommonMark without raw HTML or non-http(s) links (L832-L835,
  R-0047, R-0049); Ubuntu's mandatory `:LTS` (L1037, R-0137), which needs the list
  of LTS releases; the validity of a CVSS vector beyond its shape (R-0053 to
  R-0055); the full Package URL syntax (R-0078; see the library record `ecma-427`).
- An entry id after the database prefix, the `<ENTRYID>` of `<DB>-<ENTRYID>`
  (L143-L145, R-0010): `osv.schema.json` checks a listed prefix and its `-`
  (R-0230) and P01 the characters, but not that an entry id follows, because
  the prefix is only "ideally" followed by a `-` separator (L169, R-0018), so
  where the database part ends cannot be told in general (examples GAP-07 and
  GAP-41; source issue S-12). Added in pass 3.

## Smoke tests

Run on 2026-10-18 with the tools below, with format assertion on: 80 cases,
each with an expected verdict for `osv.schema.json`, the prose rules and the
recommendations, and the rule ids expected to fire. 0 unexpected results.

- The nine complete example records of the prose (L1553 to L1995): valid
  against `osv.schema.json` and `osv-prose.derived.schema.json`. Warnings:
  S06 on all nine (no example has a purl); S03 on five (L1554, L1636, L1764,
  L1846, L1894); S04 on four (L1554, L1764, L1846, L1894); S05 on one (L1636,
  a GIT range without versions); S09 on one (L1714, see O8).
- 71 constructed records: each P check rejects its negative case and accepts
  its positive case (for example `GHSA-a/b` and `x_a b` fail P01 while
  `x_CUSTOM-0001` passes; `v1.0.0`, `1.0` and `01.0.0` fail P03 while
  `1.0.0-alpha.1` and `1.0.0+build.5` pass; `Alpine` and `Alpine:3.16` fail
  P07a while `Alpine:v3.16` passes; `Django` and `zope.interface` fail P10f
  while `zope-interface` passes), and each S rule fires on its case and not on
  a clean record.
- All 60 patterns of the prose rules and the 3 of the recommendations compile
  as ECMA-262 regular expressions with and without the `u` flag (node
  22.23.2).

The scripts that ran these checks are scratch files of this pass and are not
committed; the examples artifact (`../examples/`) is where fixtures belong.

Pass 2 (2026-10-19) changed `osv-prose.derived.schema.json` once, to exempt
the wildcard name from P10 (reading R11), and re-ran the checks it could
reproduce: both derived files pass `check_schema`; their 63 patterns compile
under node with and without the `u` flag; their 57 quotations of the prose
are verbatim at the lines cited; the nine example records give the results
listed above; and the name `*` now passes P10 for Linux, Maven, VSCode,
GitHub Actions, PyPI and `WordPress:Core`, while every other P10 verdict is
unchanged. See `../verification.md`.

Pass 3 (cross-check, 2026-10-19) changed both derived files so that they agree
with `../requirements.yaml` and `../examples/`: the one-line check on `summary`
(R-0043, a constraint) moved from the warning S02a to the stated rule P11,
because GAP-40 expects a two-line summary to be invalid; P12 was added, because
D11 had no derived rule while R-0032, R-0050, R-0063 and R-0205 define those
fields as lists or arrays and GAP-36 to GAP-39 expect `null` to be invalid; and
S02 now checks the length only. Re-run after the change: both files pass
`check_schema`; their 63 patterns compile under node 22.23.2 with and without
the `u` flag; every quotation written as `L<line>: '...'` (33, the six new ones
included) is verbatim at the lines cited; the nine example records give the
results listed above; and over the 136 derived records and the nine example
records the only verdicts that changed are GAP-36 to GAP-40 and EDGE-05, now
rejected by P11 or P12, as `../examples/expected.yaml` expects. See
`../verification.md`, pass 3.

## Tools and versions

Python 3.13.9; jsonschema 4.26.0; rfc3339-validator 0.1.4; rfc3987 1.3.8;
PyYAML 6.0.3; node 22.23.2 (ECMA-262 regular expressions); libprotoc 29.3.
Every Python run that read a source file used `python3 -I`.

## Open for the later passes

- Pass 3 (cross-check) wired `constrained_by` in `../messages.yaml`, mapped each
  P and S rule to requirement ids (the requirements column above) and added P11
  and P12 (see Smoke tests).
- Readings R1 to R13 are for a human reviewer; R1 decides whether P08 stays an
  error.
- D5, D6, D10, D21, D28 and D31 are the disagreements most likely to make a
  record valid under one source and invalid under another; they could be
  reported upstream (`https://github.com/ossf/osv-schema/issues`).
