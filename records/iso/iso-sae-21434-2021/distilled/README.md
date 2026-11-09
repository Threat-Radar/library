---
schema: "library-doc/v1"
id: iso-sae-21434-2021-distilled-index
record: iso-sae-21434-2021
type: index
audience: human   # orientation for people; the machine source is requirements.yaml
updated: "2026-11-08"
---

# Distilled artifacts — ISO/SAE 21434:2021

**Audience of each file:** `requirements.yaml` is the **machine/AI** source of truth (canonical, queryable, audit-typed). `requirements.md` is the **human** view, *generated* from the YAML (do not hand-edit). `normative.md` is human + AI reading. This `README` orients people.

Progressive distillation. Nothing here is reviewed line-by-line yet (`reviewed_by`
empty on each artifact); a human pass is required before treating any requirement
as authoritative.

| artifact | what it is | coverage |
|---|---|---|
| `requirements.yaml` | **machine source.** 118 requirements + 42 required deliverables, audit-typed: normativity, actor, nature (process vs deliverable-producing), expects_deliverables, verification, tailorable, refs, external_refs | all normative statements; text is our paraphrase, never the standard's wording (licensed standard); derived fields need review |
| `requirements.md` | **human view, generated.** Per-clause table: designator, normativity, nature, actor, short title, deliverables | all 118 + 42 |
| `normative.md` | TARA pipeline (Clause 15), Fig 3 object model, Table 1 feasibility, key Clause 3 terms, audit-automation mapping | overview; **Annexes not distilled** (impact tables F, feasibility methods) |

## Not yet done (next passes)
- Line-by-line human review of `requirements.yaml` (set `reviewed_by`, fix any truncation/verb drift).
- Done 2026-11-08: 52 entries whose paraphrase still followed a sentence of the standard are reworded: every entry that reused 70% or more of its provision's words in the same order, unless the overlap was only names or references, plus a few with a near-copied opening. `normative.md` §3 is rewritten in our own words. The decision citations now point to where the decision is written: hold 1 of the tmodel#69 sponsor note (2026-10-02), which the sponsor confirmed for the library's ISO/SAE 21434 material in tmodel#202 item 7 (2026-11-04) and on tmodel#154 (2026-11-05). That comment and library#44 call it the "#38 Q3 decision", but on tmodel#38 it is question 4 of the 2026-10-19 comment, and no answer was posted there.
- Done 2026-11-07: the 16 defective entries listed in `summary.md` Limits are paraphrased in full from the licensed copy (tmodel#154). Each one's `notes` says what the earlier extract had lost or held instead.
- Done 2026-11-05: every provision `text` and `short_title` is now our own paraphrase, under the sponsor's licensed-text decision (paraphrase plus clause IDs, never verbatim; tmodel#69 sponsor note, hold 1 (2026-10-02); tmodel#154). Designator, normativity, verb and locator sit beside each paraphrase; the `verb` field is authoritative for force. Policy: `docs/requirements.md` §3a and the licensed-standards section of `docs/extraction.md`.
- Done 2026-10-02: every provision and work-product locator points to the subclause that holds it, and every provision-to-work-product link the standard names is recorded (RPT-0007 §7).
- Done 2026-10-03: the 10 work products that the standard ties to subclauses rather than provisions list them in `from_subclauses`, so every work product now records what it results from. The provisions in those subclauses do not list these work products; find them by locator.
- Annex distillation: impact-rating criteria (Annex F) and attack-feasibility methods (attack-potential / CVSS / attack-vector). tmodel RPT-0007 §3 and §4 summarize Annexes E to H in its own words.
- `fields.yaml` + a `schema/` encoding of the object model, once the model is chosen (#17).
