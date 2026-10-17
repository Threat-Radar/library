---
record: open-threat-model
kind: examples
title: "open-threat-model — examples and test vectors"
extracted: "2026-10-13"
reviewed_by: ""
---

# Examples and test vectors: Open Threat Model 0.2.0

The source has no test vectors as such. Its examples are of three kinds: one fenced block under every `#### Example` heading of README.md (22 headings and 23 blocks, because Parent object has two), the complete documents EXAMPLE.json and EXAMPLE.yaml (README L11), and a snippet in the Examples column of 86 of the 109 field-table rows. All of them are here, verbatim. Beside them are derived negative fixtures, and the actual result of validating every one.

| file | what |
|---|---|
| `readme-*.yaml` (23) | every README `#### Example` block, verbatim, one file per block, named after its section |
| `EXAMPLE.json`, `EXAMPLE.yaml` | the source's complete example documents, verbatim (their digests are the source digests) |
| `neg-*` (11, excluding the two groups below) | derived, category A: each breaks exactly one constraint the source schema enforces |
| `neg-strict-*` (9) | derived, category B: each breaks one README rule the source schema does not enforce; valid under the source schema, invalid under the strict profile |
| `neg-xref-*` (4) | derived, category C: each breaks one README rule no draft-07 schema can express; valid under both schemas, caught by one derived check (XR) |
| `readme-field-examples.yaml` | the 86 Examples-column snippets as vectors FE-001 to FE-086, each with its README lines, exact text, SHA-256 and results |
| `expected.yaml` | for every fixture: its source locator and byte range, or its derivation and diff; SHA-256; expected and actual results under both schemas, with every error (instance path, keyword, schema path, message); the derived-check results for whole documents; the undeclared keys accepted; and the cross-fixture assertions X-01 to X-05 |

## Fixtures

Results are source schema / strict profile; a number in brackets is the error count. XR is the outcome of the derived checks, run on whole documents only.

| file | origin | source | bytes | result | what it shows |
|---|---|---|---|---|---|
| `readme-project-object.yaml` | verbatim | README L172-180 (Project object) | 230 | valid / valid | Project object, with attributes |
| `readme-representations-object.yaml` | verbatim | README L274-293 (Representations object) | 463 | valid / valid | a diagram and a code representation |
| `readme-representation-type-diagram.yaml` | verbatim | README L313-323 (Diagram) | 274 | valid / invalid (1) | a diagram representation; attributes value `transparent: 40` is a number |
| `readme-representation-type-code.yaml` | verbatim | README L339-347 (Code) | 202 | valid / valid | a code representation with repository |
| `readme-representation-type-threat-model.yaml` | verbatim | README L359-365 (Threat-Model) | 186 | valid / valid | a threat-model representation |
| `readme-representation-element-for-diagram.yaml` | verbatim | README L463-475 (Representation element for diagram) | 209 | invalid (1) / invalid (1) | one element written as a mapping, not an array item; `size` has `with`; `attributes` at column 0 |
| `readme-representation-element-for-code.yaml` | verbatim | README L589-605 (Representation element for code) | 441 | invalid (1) / invalid (1) | one element written as a mapping, not an array item; valid as an element |
| `readme-representation-element-for-threat-model.yaml` | verbatim | README L675-680 (Representation element for threat-model) | 169 | invalid (1) / invalid (1) | one element written as a mapping, not an array item; valid as an element |
| `readme-assets-object.yaml` | verbatim | README L757-777 (Assets object) | 736 | valid / valid | two assets; the second has `attributes:` empty (null) |
| `readme-asset-instance-object.yaml` | verbatim | README L897-902 (Asset Instance object) | 160 | valid / valid | processed and stored asset ids |
| `readme-components-object.yaml` | verbatim | README L1034-1096 (Components object) | 1,567 | invalid (2) / invalid (2) | `attributes` as a list; `represetation` for `representation` |
| `readme-trustzones-object.yaml` | verbatim | README L1211-1247 (TrustZones object) | 837 | invalid (4) / invalid (4) | `trustzones` for `trustZones`; `representations` as mappings; `parent: internet` a string; `postion`, `with` |
| `readme-trustzonerisk-object.yaml` | verbatim | README L1278-1279 (TrustZoneRisk object) | 24 | valid / valid | trustRating 20 |
| `readme-parent-object-1.yaml` | verbatim | README L1327-1328 (Parent object) | 29 | valid / valid | parent by trustZone |
| `readme-parent-object-2.yaml` | verbatim | README L1332-1333 (Parent object) | 32 | valid / valid | parent by component |
| `readme-dataflows-object.yaml` | verbatim | README L1478-1498 (Dataflows object) | 578 | invalid (1) / invalid (1) | `target` for `destination` |
| `readme-threats-object.yaml` | verbatim | README L1619-1639 (Threats object) | 930 | valid / valid | a threat; `expirationDate: 2021-05-17` is a date only for a YAML 1.1 loader |
| `readme-threatrisk-object.yaml` | verbatim | README L1708-1712 (ThreatRisk object) | 326 | valid / valid | likelihood, impact and both comments |
| `readme-threat-instance-object.yaml` | verbatim | README L1764-1769 (Threat instance object) | 178 | valid / valid | state exposed, one mitigation implemented |
| `readme-mitigations-object.yaml` | verbatim | README L1854-1866 (Mitigations object) | 375 | valid / valid | two mitigations |
| `readme-mitigation-instance-object.yaml` | verbatim | README L1911-1913 (Mitigation instance object) | 89 | valid / valid | state implemented |
| `readme-repository-object.yaml` | verbatim | README L1945-1946 (Repository object) | 49 | valid / valid | repository url |
| `readme-position-object.yaml` | verbatim | README L2027-2029 (Position object) | 24 | valid / valid | x 0, y 0 |
| `EXAMPLE.json` | verbatim | EXAMPLE.json at c88c5a7 | 8,115 | valid / valid, XR: pass | the complete example; all derived checks pass |
| `EXAMPLE.yaml` | verbatim | EXAMPLE.yaml at c88c5a7 | 5,975 | valid / valid, XR: pass | the complete example in YAML; same data as EXAMPLE.json |
| `neg-missing-otmversion.yaml` | derived A | EXAMPLE.yaml | 5,957 | invalid (1) / invalid (1), XR: pass | its first line (otmVersion: 0.2.0) deleted — breaks root required ["otmVersion", "project"] (schema L7) |
| `neg-component-missing-parent.json` | derived A | EXAMPLE.json | 8,046 | invalid (1) / invalid (1), XR: pass | /components/0/parent deleted — breaks components items required [..., "parent"] (schema L105) |
| `neg-parent-both-trustzone-and-component.json` | derived A | EXAMPLE.json | 8,150 | invalid (1) / invalid (1), XR: pass | "component": "web-client" added to /components/1/parent beside its trustZone — breaks definitions/parent oneOf (schema L224-227): the value matches both branches |
| `neg-parent-miscased-key.json` | derived A | EXAMPLE.json | 8,115 | invalid (1) / invalid (1), XR: pass | /components/2/parent key trustZone written trustzone — breaks definitions/parent oneOf (schema L224-227): the value matches neither branch (field names are case sensitive, README L25) |
| `neg-asset-risk-confidentiality-string.json` | derived A | EXAMPLE.json | 8,117 | invalid (1) / invalid (1), XR: pass | /assets/0/risk/confidentiality the string "100" — breaks type number (schema L65) |
| `neg-threat-risk-impact-null.json` | derived A | EXAMPLE.json | 8,116 | invalid (1) / invalid (1), XR: pass | /threats/0/risk/impact null — breaks type number (schema L184); unlike likelihood (schema L182), impact is not nullable |
| `neg-trustzones-null.json` | derived A | EXAMPLE.json | 6,972 | invalid (1) / invalid (1), XR: XR-02 fail | /trustZones null — breaks type array (schema L76); unlike most root collections, trustZones is not nullable |
| `neg-dataflow-target-instead-of-destination.json` | derived A | EXAMPLE.json | 8,110 | invalid (1) / invalid (1), XR: pass | /dataflows/1 key destination written target, as the README Dataflows example writes it (README L1484) — breaks dataflows items required [..., "destination"] (schema L135) |
| `neg-representation-element-misspelled-representation.json` | derived A | EXAMPLE.json | 8,114 | invalid (1) / invalid (1), XR: pass | /components/2/representations/0 key representation written represetation, as the README Components example writes it (README L1077) — breaks definitions/representationElement required ["representation", "id"] (schema L243) |
| `neg-size-missing-height.json` | derived A | EXAMPLE.json | 8,091 | invalid (1) / invalid (1), XR: pass | /representations/0/size/height deleted — breaks definitions/size required ["width", "height"] (schema L216) |
| `neg-threat-instance-missing-state.json` | derived A | EXAMPLE.json | 8,085 | invalid (1) / invalid (1), XR: pass | /components/1/threats/0/state deleted — breaks definitions/threat required ["threat", "state"] (schema L258) |
| `neg-strict-asset-risk-out-of-range.json` | derived B | EXAMPLE.json | 8,116 | valid / invalid (1), XR: pass | /assets/1/risk/availability 150 — breaks strict S-06 maximum 100 |
| `neg-strict-trustrating-negative.json` | derived B | EXAMPLE.json | 8,115 | valid / invalid (1), XR: pass | /trustZones/0/risk/trustRating -5 — breaks strict S-07 minimum 0 |
| `neg-strict-likelihood-fraction.json` | derived B | EXAMPLE.json | 8,117 | valid / invalid (1), XR: pass | /threats/0/risk/likelihood 50.5 — breaks strict S-08 type integer |
| `neg-strict-diagram-without-size.json` | derived B | EXAMPLE.json | 8,044 | valid / invalid (1), XR: pass | /representations/0/size (a diagram representation) deleted — breaks strict S-03 if type diagram then size required |
| `neg-strict-representation-type-unknown.json` | derived B | EXAMPLE.json | 8,121 | valid / invalid (1), XR: pass | /representations/1/type "repository" — breaks strict S-02 enum diagram, code, threat-model |
| `neg-strict-attributes-non-string-value.json` | derived B | EXAMPLE.json | 8,108 | valid / invalid (1), XR: pass | /project/attributes/cmdbId the number 123 — breaks strict S-27 attributes values are strings |
| `neg-strict-otmversion-not-semver.yaml` | derived B | EXAMPLE.yaml | 5,976 | valid / invalid (1), XR: pass | its first line changed to otmVersion: v0.2.0 — breaks strict S-01 semver pattern |
| `neg-strict-mitigation-state-null.json` | derived B | EXAMPLE.json | 8,109 | valid / invalid (1), XR: pass | /dataflows/1/threats/0/mitigations/0/state null — breaks strict S-18 type string (REQUIRED) |
| `neg-strict-tag-null-item.json` | derived B | EXAMPLE.json | 8,129 | valid / invalid (1), XR: pass | /components/0/tags ["external", null] — breaks strict S-19 array of strings |
| `neg-xref-duplicate-component-id.json` | derived C | EXAMPLE.json | 8,110 | valid / valid, XR: XR-01 fail | /components/3/id "customer-database", the id of /components/2 — breaks XR-01 unique ids |
| `neg-xref-dangling-dataflow-destination.json` | derived C | EXAMPLE.json | 8,109 | valid / valid, XR: XR-05 fail | /dataflows/1/destination "customer-db", which no component has as id — breaks XR-05 |
| `neg-xref-dangling-threat-reference.json` | derived C | EXAMPLE.json | 8,095 | valid / valid, XR: XR-08 fail | /components/1/threats/0/threat "LOSS-CONTROL_ENV" (the README's example threat id), which is not a root threat of this document — breaks XR-08 |
| `neg-xref-diagram-element-without-position.json` | derived C | EXAMPLE.json | 8,035 | valid / valid, XR: XR-10 fail | /trustZones/0/representations/0/position deleted; that element is on architecture-diagram, a diagram representation — breaks XR-10 |

**How a fixture is made.**
- **README block**: the exact bytes of the lines between its fences. `expected.yaml` gives the README lines and the byte range [start, end) in README.md, and the SHA-256 of that range is the fixture's.
- **EXAMPLE.json, EXAMPLE.yaml**: byte-identical copies.
- **Derived JSON fixture**: EXAMPLE.json parsed, one edit applied, and the result written with `json.dumps(indent=2, ensure_ascii=False)` plus a final LF. With no edit, that reproduces EXAMPLE.json byte for byte (X-02), so each derived file differs from EXAMPLE.json only in the lines its `diff` lists.
- **Derived YAML fixture**: one line of EXAMPLE.yaml edited as text.

**What is validated.**
- **A whole document**: against the root schema.
- **A README block**: a fragment whose top-level key names a field. The value under that key is validated against the property subschema the key names, in the context of the section's structure; `instance` and `schema_pointer` in `expected.yaml` give both. For example, the TrustZoneRisk block's `risk` is checked against `/properties/trustZones/items/properties/risk`.
- **A single element written as a mapping where an array belongs**: three README element examples and the TrustZones example do this. Each such mapping is also checked as a `representationElement` (`secondary`).

**Results.** 42 of 49 fixtures give the expected result.
- **All 24 derived fixtures do exactly what they were built to do** (X-04).
- **The 7 that do not are README examples.** Each fails because of a defect in the README text, and `expected.yaml` explains each from the source lines: `readme-components-object.yaml`, `readme-dataflows-object.yaml`, `readme-representation-element-for-code.yaml`, `readme-representation-element-for-diagram.yaml`, `readme-representation-element-for-threat-model.yaml`, `readme-representation-type-diagram.yaml`, `readme-trustzones-object.yaml`.
- **EXAMPLE.json and EXAMPLE.yaml are valid** under both schemas, and pass all ten derived checks.
- **Field snippets**: 84 of the 86 validate under both schemas. Two cannot be validated: FE-023 (`codeSnippet`, README L557-564) is not valid YAML as written, and FE-073 (`threat`, L1735) has a U+00A0 NO-BREAK SPACE before its key, so the key is not `threat`.

## Re-run

From the library root, with `jsonschema` and `PyYAML` installed (tested: Python 3.14.3, jsonschema 4.26.0, PyYAML 6.0.3; run on 2026-10-14):

```sh
# digests: compare with sha256 in expected.yaml
shasum -a 256 records/vendor/open-threat-model/distilled/examples/*.json records/vendor/open-threat-model/distilled/examples/*.yaml

# a README block against the README itself, e.g. the TrustZones example: lines 1211-1247, bytes [27220, 28057)
tail -c +27221 .cache/otm-src/README.md | head -c 837 | shasum -a 256    # = sha256 of readme-trustzones-object.yaml

# every fixture against both schemas; prints "49 fixtures, 0 differences"
python3 - <<'EOF'
import json, pathlib, yaml
from jsonschema import Draft7Validator
D = pathlib.Path('records/vendor/open-threat-model/distilled')
src = json.load(open(D / 'schema/otm_schema.json'))
strict = json.load(open(D / 'schema/otm-0.2.0.derived-strict.schema.json'))

class JsonModelLoader(yaml.SafeLoader):   # YAML scalars onto JSON types: no YAML 1.1 timestamps
    pass
JsonModelLoader.yaml_implicit_resolvers = {
    k: [(t, r) for t, r in v if t != 'tag:yaml.org,2002:timestamp']
    for k, v in yaml.SafeLoader.yaml_implicit_resolvers.items()}

def at(doc, ptr):                          # RFC 6901 pointer into a parsed document
    for t in ptr.split('/')[1:]:
        t = t.replace('~1', '/').replace('~0', '~')
        doc = doc[int(t)] if isinstance(doc, list) else doc[t]
    return doc

def errors(schema, ptr, inst):             # validate inst against the subschema at ptr
    if ptr:
        schema = dict(schema, **{'$ref': '#' + ptr})
        schema.pop('$id', None)
    return sorted(('/' + '/'.join(map(str, e.absolute_path)) if e.absolute_path else '', e.validator)
                  for e in Draft7Validator(schema).iter_errors(inst))

exp = yaml.safe_load(open(D / 'examples/expected.yaml', encoding='utf-8'))
diffs = 0
for v in exp['vectors']:
    text = open(D / 'examples' / v['file'], encoding='utf-8').read()
    doc = json.loads(text) if v['format'] == 'json' else yaml.load(text, Loader=JsonModelLoader)
    inst = at(doc, v['instance'])
    for label, schema in (('source_schema', src), ('strict_schema', strict)):
        want = sorted((e['instance_path'], e['keyword']) for e in v['actual'][label]['errors'])
        got = errors(schema, v['schema_pointer'], inst)
        if got != want:
            diffs += 1
            print('DIFFERS', v['file'], label, got, want)
print(len(exp['vectors']), 'fixtures,', diffs, 'differences')
EOF
```

The script compares (instance path, keyword) pairs, which are stable across validators. The error messages in `expected.yaml` are jsonschema's wording. No committed tool runs the derived checks XR-01 to XR-10: they are defined in `../messages.yaml` (`derived_checks`), and their results here are in `expected.yaml` (`xref`).

## Licence and attribution

The README examples, the field snippets and EXAMPLE.json / EXAMPLE.yaml are from the Open Threat Model, published by IriusRisk and contributors at https://github.com/iriusrisk/OpenThreatModel (commit `c88c5a7b4115f0f025e28d5682a2b0d790b389e4`). They are licensed under the Creative Commons Attribution-ShareAlike 4.0 International License, https://creativecommons.org/licenses/by-sa/4.0/. The README ends with that notice: "This work is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License" (README.md L2033, as rendered; the line carries HTML link markup). The source carries no copyright line of its own. The material is provided as-is, without warranties; see the licence.

- `readme-*.yaml`, `EXAMPLE.json` and `EXAMPLE.yaml` are unmodified copies.
- `readme-field-examples.yaml` quotes the field snippets. The only change to each is the removal of its 4-space code-block indentation (or, for the one inline-code snippet, of its backticks).
- The `neg-*` files are adaptations, each a single change to EXAMPLE.json or EXAMPLE.yaml, recorded in `expected.yaml` (`change`, `diff`). As adaptations of CC BY-SA 4.0 material they are licensed under CC BY-SA 4.0.

The schemas in `../schema/` carry their own terms; see `../schema/README.md`.
