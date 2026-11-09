# Attack Flow source examples and expected results

Extracted: 2026-11-09

Reviewed by: ""

The fixtures preserve every JSON code example in Attack Flow v4.1.0
[`docs/language.rst`](https://github.com/center-for-threat-informed-defense/attack-flow/blob/5c8bf4ca9ff64ef9b55c38a2505db318750cbcda/docs/language.rst),
plus its Effects illustrations, confidence table, and both worked confidence
conversions. The source commit is `5c8bf4ca9ff64ef9b55c38a2505db318750cbcda`.
The language file SHA256 is
`85ae7b7f367b57c935328276a412e5b2f051e4d48f2ab622276359d49615fa49`.

`manifest.json` records source URLs, line ranges, transformations, byte counts,
digests, and expected-result selectors. The seven JSON fixtures are byte-for-byte
source blocks after removing exactly four leading RST indentation spaces from
each code line. Their remaining whitespace and final newline are preserved.
All seven blocks parse as JSON; none contains a pseudoellipsis or omitted block.
The three RST fixtures are unchanged line slices.

| Fixture | Source lines | Published Attack Flow root schema |
|---|---:|---|
| `attack-flow.json` | 168–200 | valid |
| `attack-action.json` | 272–290 | valid |
| `attack-asset.json` | 337–351 | valid |
| `attack-condition.json` | 407–422 | valid |
| `attack-operator.json` | 460–475 | valid |
| `x-detection.json` | 515–525 | invalid; source preserved |
| `x-mitigation.json` | 565–575 | invalid; source preserved |

`effects.rst` preserves the Effects section (lines 581–615), including all three
effect illustrations and all three dependency illustrations. `expected-results.json`
adds ten explicitly derived behavioral cases, each with verbatim source evidence.
The checker checks that evidence and coverage; it does not execute a flow engine
or infer a policy for unresolved operator inputs.

`confidence-scale.rst` preserves the complete seven-row table (lines 633–674).
`confidence-examples.rst` preserves both worked examples (lines 676–684):
“Very Probable” converts to 90, and 38 converts to “Doubtful”. The expected-results
file separately marks twelve range-boundary cases as derived. The checker reads
the preserved table, checks its complete integer partition of 0–100, and verifies
the worked and boundary conversions.

## Source defects and validation limits

Each `x-*` fixture has an invalid STIX identifier containing nonhexadecimal UUID
characters and invalid UUID version/variant components. Each fails the published
STIX common/core schema on that identifier alone. Each also omits the Attack Flow
extension declaration and has no type-specific definition in the published Attack
Flow schema. Applied diagnostically to these custom objects, the root schema reports
three errors each: identifier pattern, required `extensions`, and
`unevaluatedProperties`. The last error includes cascading unannotated common
fields because the common/core branch failed. Exact errors are retained in
`expected-results.json`; the examples have not been repaired. Rejection by this
Attack Flow root schema does not establish that arbitrary custom STIX objects must
declare the Attack Flow extension.

The related published extension-definition bundle is preserved once at
`../schema/attack-flow-extension-2.0.0.json`. Its source hash and locator are in this
manifest. The checker verifies its JSON structure, definition id/type/version,
creator identity references, and consistency with the five Attack Flow example
extension declarations and schema example selectors. The extension's schema URL
uses `/stix/`, while the schema document's `$id` uses `/schema/`; both published
strings are recorded without rewriting. Full STIX bundle, identity, and
extension-definition schema validation is not run because that schema closure is
not included. The Attack Flow SDO root is not a bundle schema.

The seven JSON examples are separate object fragments. Schema validation here
does not establish reference resolution across a complete flow or the document
rule requiring exactly one `attack-flow` object. The source provides illustrative
examples, not a formal conformance suite.

## Reproduce

From the repository root, using Python with `jsonschema` and `referencing`:

```sh
.cache/extraction-venv/bin/python records/other/mitre-attack-flow/distilled/examples/check_examples.py --source-root .cache/attack-flow-v4.1.0
```

The optional `--source-root` enables whole-source SHA256 checks and independent
discovery of all seven JSON blocks, followed by byte equality checks for all ten
source fixtures and the related extension instance. Without it, fixture digests,
confidence expectations, Effects evidence, and schema outcomes are still checked.
`--report PATH` writes the JSON report.

Schema loading uses `../schema/offline_validate.py:load_validator` and its hashed
snapshot manifest. Exact original reference URLs map to preserved STIX dependency
snapshots; an unknown reference raises an error instead of retrieving content.
Format assertions are enabled by the helper. No network access is required.

`validation-report.json` records the source-equality run: 10/10 source fixtures
match, the related extension instance matches, five JSON examples validate, and
the two published `x-*` failures reproduce. Exit status zero means the recorded
expected outcomes match, including those failures; it does not mean every source
example validates. Human review remains unsigned.
