---
record: mitre-attack-flow
kind: index
title: "Attack Flow — full extraction index"
extracted: "2026-11-09"
reviewed_by: ""
---

# Attack Flow extraction

This extraction covers `docs/language.rst`, the published JSON Schema and the
extension-definition instance at Attack Flow tag `v4.1.0`, resolved to commit
`5c8bf4ca9ff64ef9b55c38a2505db318750cbcda`. It does not extract all Builder code,
corpus flows, every STIX object, or other versions of the language. Sources are
identified by URL and SHA-256; complete source documents remain outside Git.
The extracted schema and example bytes are retained under the upstream license.

| artifact | coverage and limit |
|---|---|
| [normative.md](normative.md) | All 10 language tables, effects semantics and source-schema constraints; exact excerpts with line locators. |
| [requirements.yaml](requirements.yaml) | 109 source-stated entries; all 22 uppercase modal occurrences (20 MUST, 2 MAY) appear exactly once in 20 source blocks. Additional table, datatype, effect, confidence and schema constraints are separately identified. |
| [schema/](schema/) | Published schema and extension instance copied unchanged; all 13 transitive STIX schema dependencies pinned separately for offline resolution, with provenance and licenses. |
| [messages.yaml](messages.yaml) | Seven language object types, all 48 local and 14 inherited common fields, supporting structures and requirement links. Imported STIX definitions are limited to the examined schema closure. |
| [protocol.yaml](protocol.yaml), [protocol.md](protocol.md) | Written N/A finding: a graph data format with no defined transport or exchange protocol. Graph evaluation is kept separate. |
| [state-machine.yaml](state-machine.yaml) | Action effects, conditions and Boolean operator evaluation. Derived state labels are explicit; scheduling and unresolved-input policy are not specified by this source. |
| [examples/](examples/) | Every language JSON block and text example preserved, expected outcomes, and reproducible offline checks. Published examples are never silently repaired. |
| [design-notes.md](design-notes.md) | Adopt/adapt/reject findings routed to tmodel's accepted architecture or new review work; source contradictions remain visible. |

## Source reconciliation

The prose defines seven types; the schema dispatches five. In particular,
`x-detection` and `x-mitigation` lack dedicated schema definitions. The prose
lists five scope values while the schema accepts seven. Execution timestamps
are mislabeled as identifiers in the prose. Several lists have `minItems: 1`
in the schema even though the prose does not settle empty-list semantics.
An extension declaration is schema-required even where custom-object examples
omit it. The imported STIX custom-property pattern also means that
`unevaluatedProperties: false` is not a whitelist of only the documented fields.
The source schema's remote dependencies name mutable OASIS branches; their
snapshot commits and hashes are recorded without changing the published refs.

These are source differences, not tmodel decisions. See each artifact's source
locators and the design notes before using the extraction to implement an
importer. Whole-flow cardinality, graph references, review acceptance and risk
ratings cannot be established by individual-object schema validation.

## Review boundary

Automated extraction, independent verification and cross-check results are
recorded in `record.yaml` when completed. They do not constitute human review.
Every artifact retains an empty `reviewed_by`; a person must review and sign
each artifact before it is treated as buildable-on under FX-1. The report also
remains a draft until its human review and merge.
