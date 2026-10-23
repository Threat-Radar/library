---
schema: "library-doc/v1"
id: cisa-ai-in-ot-principles-distilled-index
record: cisa-ai-in-ot-principles
type: index
audience: human   # orientation for people; the machine source is requirements.yaml
updated: "2026-10-21"
---

# Distilled artifacts — Principles for the Secure Integration of AI in OT

FX-1 (`docs/extraction.md`), `distillation.profile: full`. Source: the CISA PDF revision
`508cV2`, sha256 `1fde3cba…1560`, 25 pp. Extracted 2026-10-21 for tmodel#39 part B. All text comes
from the gitignored capture `.cache/cisa-ai-in-ot-principles.capture.txt` (PyMuPDF text blocks;
the normalisation rules are in `verification.md`).

Nothing here is reviewed line by line yet (`reviewed_by` is empty on each artifact).

| artifact | kind | coverage |
|---|---|---|
| `requirements.yaml` | requirements | **machine source.** 136 statements in source order, ids `R-0001`…`R-0136`. Verbatim text, page locator, verb, actor, `kind`, `testable`, `bears_on` (tmodel decisions), `maps_to` (frameworks the source names, and our threat mapping to NIST AI 100-2 E2025 and MITRE ATLAS ids, stated or inferred). Header reconciles every normative form in the source. |
| `normative.md` | normative | the regulatory status, the definitions the statements rely on, Tables 1 and 2 cell by cell, and all 136 statements under their section headings |
| `threats.yaml` | threats | 32 threats and risks (all of Table 2 plus §1.3, §2.2, §2.3, §2.4, §3.4, §4.1, §4.2) and 4 weaknesses, quoted, with NIST and ATLAS ids and the statements that address each |
| `examples/` | examples | the §2.1 business-case assessment and the §4.1 monitoring setup as verbatim fixtures |
| `design-notes.md` | design-notes | how each statement bears on tmodel (ADR-0006, ADR-0007, ADR-0010, tmodel#130, DEC-001b, DEC-008, DEC-009, R-018) and which AI attack class it defends against |
| `verification.md` | verification | FX-1 passes 2 (verify) and 3 (cross-check), the capture rules, and every excluded occurrence of every normative form |

Not applicable, with reasons in `record.yaml` `distillation.not_applicable`: schema, messages,
protocol, state machine. The guidance is prose: it defines no format, no exchange, and no transitions
between the states it names.

## Checks (after the verify pass, 2026-10-22)

| check | result |
|---|---|
| `bin/bcp14-count` | 0 (lower-case recommendation forms and imperatives) |
| verbatim | 136 / 136 texts found in the capture by the build script; no overlapping spans. The verify pass re-checked the 123 pass-1 texts against three independent renderings and found the capture lossless; the 13 entries added in that pass are checked against the same capture |
| own-form baseline vs extracted | should 40 → 40 · must 5 → 4 · may 37 → 9 · can 53 → 23 · encourage* 2 → 2 · recommend* 9 → 4 · essential 4 → 4 · critical 10 → 7 · vital 3 → 2 · crucial 2 → 1 · necessary 2 → 1 · imperative entries 60 |
| ATLAS ids | all present in ATLAS 2026.09 (the data file atlas.mitre.org loads) |
| `bin/check-requirements` (LinkML) | passes |

Derived fields to review: `actor`, `phase`, `nature`, `testable`, `bears_on`, and every `maps_to`
entry with `provenance: ours`.
