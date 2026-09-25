---
schema: "library-doc/v1"
id: iso-sae-21434-2021-distilled-index
record: iso-sae-21434-2021
type: index
updated: "2026-09-25"
---

# Distilled artifacts — ISO/SAE 21434:2021

Progressive distillation. Nothing here is reviewed line-by-line yet (`reviewed_by`
empty on each artifact); a human pass is required before treating any requirement
as authoritative.

| artifact | what it is | coverage |
|---|---|---|
| `requirements.yaml` | 118 requirements + 42 work products, `#RQ-CC-NN`, with clause + locator + short_title + full text + produces(WP) + refs + external_refs | all marked normative statements, **full text**; not reviewed line-by-line |
| `requirements.md` | viewable per-clause table: designator + short title (HTML version will be expandable) | all 118 + 42 |
| `normative.md` | TARA pipeline (Clause 15), Fig 3 object model, Table 1 feasibility, key Clause 3 terms, audit-automation mapping | overview; **Annexes not distilled** (impact tables F, feasibility methods) |

## Not yet done (next passes)
- Line-by-line human review of `requirements.yaml` (set `reviewed_by`, fix any truncation/verb drift).
- Precise sub-clause locators for every requirement (currently section-level).
- Annex distillation: impact-rating criteria (Annex F) and attack-feasibility methods (attack-potential / CVSS / attack-vector).
- `fields.yaml` + a `schema/` encoding of the object model, once the model is chosen (#17).
