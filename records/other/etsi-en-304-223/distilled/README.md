---
schema: "library-doc/v1"
id: etsi-en-304-223-distilled-index
record: etsi-en-304-223
type: index
audience: human   # orientation for people; the machine source is requirements.yaml
updated: "2026-10-21"
---

# Distilled artifacts — ETSI EN 304 223 V2.1.1

FX-1 (`docs/extraction.md`), `distillation.profile: full`. Source: the ETSI PDF, sha256
`1ef542ac…d21a`, 16 pp. The first pass (2026-10-01, library#8) left `requirements.yaml`,
`requirements.md` and a paraphrased `normative.md`; the FX-1 pass (2026-10-21, tmodel#39 part B)
checked those against the source, fixed them and added the rest.

Nothing here is reviewed line by line yet (`reviewed_by` is empty on each artifact).

| artifact | kind | coverage |
|---|---|---|
| `requirements.yaml` | requirements | **machine source.** 73 entries: the 72 clause 5 provisions keyed by ETSI's designator (`#5.1.2-3`) and C4-1 (clause 4). Verbatim text, page locator, verbs, actor, `kind`, `testable`, `bears_on` (tmodel decisions) and `maps_to` (threat mapping to NIST AI 100-2 E2025 and MITRE ATLAS ids, stated or inferred). Header reconciles every modal verb in the source. |
| `requirements.md` | requirements (generated) | **human view** of the YAML: one table per principle |
| `normative.md` | normative | every normative statement verbatim with clause and page: verbal forms, scope, terms, clause 4 and Table 4-1, all 72 provisions with their headings |
| `threats.yaml` | threats | the 14 threats and 3 weaknesses the EN describes, with candidate CWE ids for the weaknesses,, quoted, with NIST and ATLAS ids and the provisions that address each |
| `design-notes.md` | design-notes | how each provision bears on tmodel (ADR-0006, ADR-0007, ADR-0010, tmodel#130, DEC-001b, DEC-008, DEC-009, R-018) and which AI attack class it defends against |
| `verification.md` | verification | FX-1 passes 2 (verify) and 3 (cross-check): method, results, defects found and fixed |

Not applicable, with reasons in `record.yaml` `distillation.not_applicable`: schema, messages,
protocol, state machine, examples. The EN is a requirements standard in prose: it defines no
format, exchange, lifecycle states or worked example.

## Checks (after verify and cross-check, 2026-10-22)

| check | result |
|---|---|
| `bin/bcp14-count` | 0 (the EN uses lower-case ETSI verbal forms) |
| own-form baseline vs extracted, whole source | shall 61 → 59 · should 32 → 29 · can 22 → 6 · will 7 → 6 · cannot 5 → 2 · may 9 → 0 · must 2 → 0 · shall not 4 → 0 · should not, will not, need not 1 → 0; each exclusion itemised in `requirements.yaml` `reconciliation` |
| clause 5 provisions vs source | 72 / 72 texts equal the full source provision; confirmed by the independent verifier on two fresh renderings |
| ATLAS ids | all present in ATLAS 2026.09 (the data file atlas.mitre.org loads) |
| `bin/check-requirements` (LinkML) | passes |
| `bin/validate`, `bin/check-pr-extraction`, `bin/check-artifacts` | clean for this record |

Derived fields to review: `actor` (five `(implied)`, incl. 5.1.2-1.1 fixed in this pass), `short_title`,
`nature`, `expects_deliverables`, `verification`, `testable`, `bears_on`, and every `maps_to`
entry with `provenance: ours`.
