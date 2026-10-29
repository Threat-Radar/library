---
record: open-threat-model
kind: schema
title: "open-threat-model — schemas"
extracted: "2026-10-13"
reviewed_by: ""
---

# Schema — Open Threat Model 0.2.0 JSON Schema

| file | what | status |
|---|---|---|
| `otm_schema.json` | The OTM JSON Schema that README.md links as its schema (L49): draft-07, `$id` `https://iriusrisk.com/schema/otm-0.2.0.schema.json`. | **source, verbatim**: a byte-identical copy (SHA-256 below), its Apache-2.0 notice intact |
| `otm-0.2.0.derived-strict.schema.json` | A stricter profile: the source schema plus 36 constraints that README.md states and the source schema does not enforce (S-01 to S-36, below). Each addition carries a `$comment` naming its README lines. 20,959 bytes, SHA-256 `1ffdbbaae740ba3d6148fdce3324be6f28f0c3e21e2cf277d6d3b0b8d676c235`. | **derived, ours**: said so in its top-level `$comment` and `title`; it has no `$id`, so it cannot be mistaken for the source |

An implementer can validate with either. The source schema is what OTM tools built on it accept; the strict profile adds what the README says. Neither can check that identifiers are unique or that references between objects resolve, which draft-07 cannot express: those are the derived checks XR-01 to XR-10 in `../messages.yaml` (`derived_checks`). Field-by-field structure with line numbers is in `../messages.yaml`; fixtures and actual results are in `../examples/`.

## Source

| | |
|---|---|
| Repository | https://github.com/iriusrisk/OpenThreatModel at commit `c88c5a7b4115f0f025e28d5682a2b0d790b389e4` (2025-12-11) |
| URL | https://github.com/iriusrisk/OpenThreatModel/blob/c88c5a7b4115f0f025e28d5682a2b0d790b389e4/otm_schema.json (raw: https://raw.githubusercontent.com/iriusrisk/OpenThreatModel/c88c5a7b4115f0f025e28d5682a2b0d790b389e4/otm_schema.json) |
| `$schema`, `$id`, `title` | `http://json-schema.org/draft-07/schema#` (L2), `https://iriusrisk.com/schema/otm-0.2.0.schema.json` (L3), "Open Threat Model Specification" (L4) |
| Version | 0.2.0, from the `$id` and README L18 ("Current schema version: 0.2.0") |
| Size | 11,549 bytes, 308 lines, ASCII only, LF line ends |
| SHA-256 | `81e7f5a52a0a7d66b44cc4e0c15f21b5d60e1ca945c810e39622a730545eef0c` |
| History | added 2023-05-10 (6ff9169); copied from the StartLeft repository 2023-06-01 (2bd87d8); `$id` raised to 0.2.0 by 355287f (2023-08-29); **last changed by 06288a0 (2024-01-31, "define objects for all arrays"), after the `0.2.0` tag** |
| Copy | made from `.cache/otm-src/otm_schema.json`; `cmp` reports the files identical and the digests match |

### Two different files carry the `$id` otm-0.2.0

The git tag `0.2.0` (commit 6bcb2ab, 2023-08-30) holds a different `otm_schema.json`: 302 lines, SHA-256 `bf3a9703787b942ca81d08dd7e4288c4b6396258e8e117b181009c4e0c25b18a` (not held here; `git show 0.2.0:otm_schema.json` in the source repository). In it, `representations` and `assets` carry `required` and `properties` directly on the array schema, where draft-07 ignores them, so representation and asset items are not validated at all. Commit 06288a0 moved both under `items` and changed neither the `$id` nor the README. Run over the fixtures in `../examples/`, two documents change result: `neg-asset-risk-confidentiality-string.json` and `neg-size-missing-height.json` are valid under the tagged file and invalid under this one (`../examples/expected.yaml` X-03). A consumer that fetches "the 0.2.0 schema" can get either file; compare digests. The copy here is the pinned commit's file.

### Licence

The schema's own notice (`$comment`, L5), retained in the copy:

> Open Threat Model JSON schema is published under the terms of the Apache License 2.0.

The licence text is at https://www.apache.org/licenses/LICENSE-2.0. The repository's `LICENSE` file, added later (d226d5b, 2024-11-20), is CC BY-SA 4.0 and goes with the specification text (README.md L2032-2034); that commit did not change the schema's notice, and this copy follows the file's own notice. The derived profile is a modified version of the schema. Its top-level `$comment` says so, as Apache-2.0 section 4(b) asks of modified files, and its added `$comment`s cite and quote README.md, which is CC BY-SA 4.0.

## What the source schema declares

- **The root**: an object that requires `otmVersion` and `project` (L7), with 9 properties: `otmVersion`, `project`, `representations`, `assets`, `trustZones`, `components`, `dataflows`, `threats` and `mitigations` (L8-212).
- **6 definitions**: `size` (L214), `parent` (L222), `position` (L233), `representationElement` (L241), `threat`, which is the threat instance (L256), and `assetInstance` (L275).
- **101 property declarations, 20 `required` lists, 10 `$ref` sites and 1 `oneOf`.** Of the `required` lists, 18 sit on objects and 2 are the branches of the `oneOf` (`parent`, L224-227). 61 `type` declarations include `"null"`.
- **Keywords used**: `type`, `required`, `properties`, `items`, `$ref`, `oneOf` and `definitions`, plus the annotations `$schema`, `$id`, `title` and `$comment`. Nothing else appears: no `enum`, `const`, `pattern`, `format`, `minimum`, `maximum`, `additionalProperties`, `uniqueItems`, `minItems`, `maxItems`, `minLength`, `maxLength`, `default`, `if`/`then`/`else`, `allOf`, `anyOf`, `not` or `dependencies`.

## What it enforces, and what it does not

It enforces the JSON type of every declared property, with null wherever a type list names it. It enforces the required keys of each object: every field the README marks REQUIRED is required by the schema except Diagram `size` (README L308) and the diagram element's `position` and `size` (L432, L440). The schema also requires one field the README leaves optional, Repository `url` (L43; README L1930-1932). It enforces exactly one of `trustZone` and `component` in a Parent object (`oneOf`, L224-227) and the shape of array items through `$ref`.

What it does not enforce, with the M-numbers of `../messages.yaml` `mismatches`:

| README says | where | source schema | strict profile | otherwise |
|---|---|---|---|---|
| integer, signed 32 bits (L37), for 12 fields | M-01 | `number` | S-04 to S-15 | |
| "From 0 to 100" for 7 fields | M-02 | no range | S-04 to S-10 | |
| representation types diagram, code, threat-model (L189-193) | M-03 | free string | S-02 | |
| a diagram representation must have `size` (L308) | M-04 | optional | S-03 | |
| a diagram element must have `position` and `size` (L432, L440) | M-05 | optional | not expressible: the variant is known only through the representation's type | XR-10 |
| a code element needs "at least one" field (L480) | M-06 | no rule | not added: the rule contradicts its own table | |
| REQUIRED fields set to null (likelihood, mitigation instance) | M-09 | null allowed | S-08, S-16 to S-18 | |
| `attributes` is "Map [string, string]" | M-11 | any object | S-27 to S-35 | |
| `bidirectional` defaults to false (L1404) | M-12 | no default | S-36 (an annotation) | |
| `otmVersion` is a semver version (L15, L55) | M-13 | any string | S-01 | |
| identifiers are unique | M-16 | not checked | not expressible | XR-01 |
| id-valued fields name objects of the document | M-16 | not checked | not expressible | XR-02 to XR-09 |
| threat and mitigation states, component and trust zone types, threat categories | | free strings | not added: the README gives no closed list | |
| `ownerContact` an email, `url` a URL, `cwes` CWE ids | | free strings | not added: described, not stated as rules | |
| unknown keys | | every object accepts and ignores them (no `additionalProperties` anywhere) | not added: the README never says objects are closed | |

One behaviour of the `oneOf` to know: its two branches are `required`-only, and `required` passes anything that is not an object. A non-object `parent` therefore satisfies both branches. jsonschema then reports `oneOf` ("is valid under each of") beside the `type` error, as the README TrustZones example shows (`parent: internet`, README L1236).

## The derived strict profile

1. **It adds only what the README states.** Each addition is a README rule the source does not enforce, or (marked inferred) what follows from stated lines. Each carries its own `$comment`.
2. **It never relaxes.** Every constraint-bearing JSON pointer of the source schema exists unchanged, only `type` lists are narrowed, so the pointers in `../messages.yaml` apply to both files. The annotations alone differ: `$id` is removed and `title` and `$comment` are rewritten (see the table above). Over all 49 fixtures it accepted nothing the source schema rejected (`../examples/expected.yaml` X-05).
3. **Nullability is kept where the source has it**, except on README-REQUIRED fields (S-08, S-17, S-18) and array items (S-16, S-19 to S-26), and those are marked inferred. README L31 says "`null` is not supported as a type", but the source schema and EXAMPLE.json use null for absent optional values (22 nulls in EXAMPLE.json). Removing null everywhere would reject the project's own complete example.
4. **`integer` is draft-07's**: 1.0 is an integer. README L31's lexical definition ("a JSON number without a fraction or exponent part") would reject it (M-14).
5. **Integers without a 0-100 range get the 32-bit bounds of L37.**

| id | pointer | rule | README | kind |
|---|---|---|---|---|
| S-01 | `/properties/otmVersion` | pattern: a Semantic Versioning 2.0.0 version string (the regular expression published on semver.org) | L15, L55 | inferred |
| S-02 | `/properties/representations/items/properties/type` | enum: diagram, code, threat-model | L189, L191, L192, L193, L298 | stated |
| S-03 | `/properties/representations/items` | if type is "diagram" then size is required and is an object (not null) | L298, L308 | stated |
| S-04 | `/properties/assets/items/properties/risk/properties/confidentiality` | type integer (was number); minimum 0; maximum 100 | L800, L801 | stated |
| S-05 | `/properties/assets/items/properties/risk/properties/integrity` | type integer (was number); minimum 0; maximum 100 | L812, L813 | stated |
| S-06 | `/properties/assets/items/properties/risk/properties/availability` | type integer (was number); minimum 0; maximum 100 | L824, L825 | stated |
| S-07 | `/properties/trustZones/items/properties/risk/properties/trustRating` | type integer (was number); minimum 0; maximum 100 | L1265, L1266 | stated |
| S-08 | `/properties/threats/items/properties/risk/properties/likelihood` | type integer (was ["number","null"]: null removed because the field is REQUIRED and its README type is integer); minimum 0; maximum 100 | L1657, L1658, L31 | inferred |
| S-09 | `/properties/threats/items/properties/risk/properties/impact` | type integer (was number); minimum 0; maximum 100 | L1681, L1682 | stated |
| S-10 | `/properties/mitigations/items/properties/riskReduction` | type integer (was number); minimum 0; maximum 100 | L1823, L1824 | stated |
| S-11 | `/definitions/representationElement/properties/line` | type ["integer","null"] (was ["number","null"]; null kept, the field is optional); int32 bounds | L541, L37 | stated |
| S-12 | `/definitions/size/properties/width` | type integer (was number); int32 bounds | L1964, L37 | stated |
| S-13 | `/definitions/size/properties/height` | type integer (was number); int32 bounds | L1976, L37 | stated |
| S-14 | `/definitions/position/properties/x` | type integer (was number); int32 bounds | L2001, L37 | stated |
| S-15 | `/definitions/position/properties/y` | type integer (was number); int32 bounds | L2013, L37 | stated |
| S-16 | `/definitions/threat/properties/mitigations/items` | item type object (was ["object","null"]) | L1755, L31 | inferred |
| S-17 | `/definitions/threat/properties/mitigations/items/properties/mitigation` | type string (was ["string","null"]) | L1884, L1885, L31 | inferred |
| S-18 | `/definitions/threat/properties/mitigations/items/properties/state` | type string (was ["string","null"]) | L1896, L1897, L31 | inferred |
| S-19 | `/properties/components/items/properties/tags/items` | item type string (was ["string","null"]) | L957, L31 | inferred |
| S-20 | `/properties/dataflows/items/properties/tags/items` | item type string (was ["string","null"]) | L1387, L31 | inferred |
| S-21 | `/properties/dataflows/items/properties/assets/items` | item type string (was ["string","null"]) | L1440, L31 | inferred |
| S-22 | `/properties/threats/items/properties/categories/items` | item type string (was ["string","null"]) | L1552, L31 | inferred |
| S-23 | `/properties/threats/items/properties/cwes/items` | item type string (was ["string","null"]) | L1566, L31 | inferred |
| S-24 | `/properties/threats/items/properties/tags/items` | item type string (was ["string","null"]) | L1588, L31 | inferred |
| S-25 | `/definitions/assetInstance/properties/processed/items` | item type string (was ["string","null"]) | L864, L31 | inferred |
| S-26 | `/definitions/assetInstance/properties/stored/items` | item type string (was ["string","null"]) | L879, L31 | inferred |
| S-27 | `/properties/project/properties/attributes` | additionalProperties {type: string}: every value of the map is a string (the map itself stays ["object","null"]) | L155 | stated |
| S-28 | `/properties/representations/items/properties/attributes` | additionalProperties {type: string}: every value of the map is a string (the map itself stays ["object","null"]) | L255 | stated |
| S-29 | `/properties/assets/items/properties/attributes` | additionalProperties {type: string}: every value of the map is a string (the map itself stays ["object","null"]) | L740 | stated |
| S-30 | `/properties/trustZones/items/properties/attributes` | additionalProperties {type: string}: every value of the map is a string (the map itself stays ["object","null"]) | L1194 | stated |
| S-31 | `/properties/components/items/properties/attributes` | additionalProperties {type: string}: every value of the map is a string (the map itself stays ["object","null"]) | L1018 | stated |
| S-32 | `/properties/dataflows/items/properties/attributes` | additionalProperties {type: string}: every value of the map is a string (the map itself stays ["object","null"]) | L1462 | stated |
| S-33 | `/properties/threats/items/properties/attributes` | additionalProperties {type: string}: every value of the map is a string (the map itself stays ["object","null"]) | L1602 | stated |
| S-34 | `/properties/mitigations/items/properties/attributes` | additionalProperties {type: string}: every value of the map is a string (the map itself stays ["object","null"]) | L1836 | stated |
| S-35 | `/definitions/representationElement/properties/attributes` | additionalProperties {type: string}: every value of the map is a string (the map itself stays ["object","null"]) | L447, L572, L659 | stated |
| S-36 | `/properties/dataflows/items/properties/bidirectional` | default false (an annotation: validation results do not change) | L1404 | stated |

**Not added, and why.**
- `additionalProperties: false`: the README never says an object is closed.
- Identifier uniqueness and references: draft-07 cannot express them (XR-01 to XR-09).
- The diagram element's `position` and `size`: they need the referenced representation's type (XR-10).
- The code element's "at least one" rule: ambiguous and self-contradictory (M-06).
- Trust zone `type`: RECOMMENDED, so optional in 0.2.0 (L1139).
- Email, URL or CWE formats: the README describes these fields but states no format rule.
- Pinning `otmVersion` to 0.2.0: the README does not say a consumer must reject other versions. A consumer that wants that adds `"const": "0.2.0"` itself.

## Validate offline

Nothing is fetched. Every `$ref` is a local `#/definitions/…` fragment, jsonschema bundles the draft-07 meta-schema, and `$id` is never dereferenced.

```sh
pip install jsonschema pyyaml          # tested: Python 3.14.3, jsonschema 4.26.0, PyYAML 6.0.3
S=records/vendor/open-threat-model/distilled/schema/otm_schema.json      # or otm-0.2.0.derived-strict.schema.json
python3 - "$S" path/to/model.json <<'EOF'
import json, sys
from jsonschema import Draft7Validator
schema = json.load(open(sys.argv[1]))
Draft7Validator.check_schema(schema)
errs = sorted(Draft7Validator(schema).iter_errors(json.load(open(sys.argv[2]))), key=lambda e: list(map(str, e.absolute_path)))
for e in errs:
    print('/' + '/'.join(map(str, e.absolute_path)), e.validator, e.message)
print('valid' if not errs else f'{len(errs)} error(s)')
sys.exit(1 if errs else 0)
EOF
```

The exit code is 0 for a valid document and 1 otherwise, with one line per error (instance path, keyword, message).

**YAML.** An OTM document in YAML is the same JSON object (README L23), so load it with every scalar mapped onto a JSON type, then validate the result as above:

```python
import yaml
class JsonModelLoader(yaml.SafeLoader):
    pass
JsonModelLoader.yaml_implicit_resolvers = {
    k: [(t, r) for t, r in v if t != 'tag:yaml.org,2002:timestamp']
    for k, v in yaml.SafeLoader.yaml_implicit_resolvers.items()}
doc = yaml.load(open('model.yaml', encoding='utf-8'), Loader=JsonModelLoader)
```

A stock YAML 1.1 loader turns an unquoted date into a date object, which is not a JSON value. The README Threats example writes `expirationDate: 2021-05-17` (L1635): the strict profile rejects the date object as a non-string attribute and accepts the string. An empty value (`attributes:`) loads as null either way.

**A fragment.** To validate a fragment against one structure, keep the whole schema so that the `#/definitions/…` refs resolve, add `"$ref": "#<pointer>"` at the top and drop `$id`; draft-07 ignores the siblings of `$ref`. `../examples/README.md` does exactly this.

## Results (2026-10-14, jsonschema 4.26.0)

| input | source schema | strict profile | schema at tag 0.2.0 | derived checks XR-01 to XR-10 |
|---|---|---|---|---|
| EXAMPLE.json (SHA-256 `045667cd46ff8755a877f0af6104362bd438da3ca68e961ca9e3e1b969a5387b`) | valid | valid | valid | all pass |
| EXAMPLE.yaml (SHA-256 `d78f42824cc7eec1a1f767aba29d8c0bc3081af6c05149130bb9f7df492a2761`) | valid | valid | valid | all pass |
| the 49 fixtures of `../examples/` | 32 valid, 17 invalid | 22 valid, 27 invalid | 2 whole documents differ from the source schema (X-03) | per document in `../examples/expected.yaml` |

EXAMPLE.yaml parses to data identical to EXAMPLE.json (X-01). Both carry three keys that no schema declares: `package` on the code element (EXAMPLE.json L177), and `representations: null` on both dataflows (L195, L212). They are accepted because no object is closed.
