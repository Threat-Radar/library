---
schema: "library-normative/v1"
id: iso-sae-21434-2021-normative
record: iso-sae-21434-2021
type: normative
updated: "2026-11-08"
coverage: "Clause 15 TARA, the Fig 3 object model, Table 1 feasibility, key Clause 3 terms, audit mapping. Annexes NOT distilled."
reviewed_by: ""
---

# ISO/SAE 21434 — distilled normative content

> Compacted so an implementer can build the model without re-reading the source.
> **Our own wording throughout.** ISO/SAE 21434 is a licensed standard; this page paraphrases
> it and cites clause IDs, and quotes none of its text (sponsor decision:
> tmodel#69 sponsor note, hold 1 (2026-10-02); tmodel#154).
> Requirement ids resolve in `requirements.yaml`. **Coverage baseline:** the standard
> tags every obligation, so the baseline is marker count, not a verb grep —
> **118 requirements (101 RQ shall / 13 RC should / 4 PM may) + 42 work products.**
> A distillation missing any marker has failed; all 118+42 are catalogued.

## 1. Object model (Figure 3 — item, function, component and related terms)

Typed edges (a ready candidate object model for ARCH-0001 / #17), read from Figure 3 tail to head
(checked on a page image on 2026-10-02; an earlier
version had the item and function edge reversed and the wrong source for `contains` and
`allocated to`):

- `item` **implements** `function(s)`; `item` **contains** `asset`; `item` **consists of** `component`
- `cybersecurity property` **attribute of** `asset`
- `cybersecurity goal` **protects** `asset`; **associated with** `item`; **associated with**
  `threat scenario`; **realized by** `cybersecurity requirement`
- `cybersecurity requirement` **allocated to** `item`; **allocated to** `component`
- `threat scenario` **compromises** `cybersecurity property`; **realizes** `damage scenario`
- `damage scenario` **affects** `road user`

## 2. TARA pipeline (Clause 15) — the risk method

Ordered, each step a requirement + a work product:

| step | clause | requirement(s) | work product |
|---|---|---|---|
| Damage scenarios | 15.3 | RQ-15-01 | WP-15-01 |
| Asset identification | 15.3 | RQ-15-02 | WP-15-02 |
| Threat scenario identification | 15.4 | RQ-15-03 (targeted asset + compromised property + cause) | WP-15-03 |
| Impact rating | 15.5 | RQ-15-04 (categories **S,F,O,P**), RQ-15-05 (**severe/major/moderate/negligible**), RQ-15-06 (safety ← ISO 26262) | WP-15-04 |
| Attack path analysis | 15.6 | RQ-15-08, RQ-15-09 | WP-15-05 |
| Attack feasibility rating | 15.7 | RQ-15-10 (per **Table 1**), RC-15-11 (method) | WP-15-06 |
| Risk value determination | 15.8 | RQ-15-15, RQ-15-16 | WP-15-07 |
| Risk treatment decision | 15.9 | RQ-15-17 | WP-15-08 |

### Table 1 — Attack feasibility ratings
| rating | effort the attack path needs |
|---|---|
| High | low effort |
| Medium | medium effort |
| Low | high effort |
| Very low | very high effort |

**RC-15-11** — feasibility method is one of: (a) attack-potential-based; (b) CVSS-based;
(c) attack-vector-based. (Detailed criteria are in the Annexes, not distilled here.)

## 3. Key terminology (Clause 3, selected)

- **asset** (3.1.2): something that has value or helps create value; its cybersecurity properties, if compromised, can lead to damage scenarios.
- **cybersecurity property** (3.1.20): an attribute that might deserve protection, for example confidentiality, integrity or availability.
- **damage scenario** (3.1.22): a harmful outcome for a road user that involves a vehicle or one of its functions.
- **threat scenario** (3.1.33): a possible way one or more assets could have their cybersecurity properties compromised, bringing about a damage scenario.
- **attack path** (3.1.4): the deliberate actions that, taken together, carry out a threat scenario; also called an attack.
- **attack feasibility** (3.1.3): how easily the actions of an attack path can be carried out successfully; a property of the path.
- **item** (3.1.25): what delivers a vehicle-level function: one component, or several working together.
- **component** (3.1.7): a part that can be separated from the rest, both logically and technically.
- **weakness** (3.1.40): a flaw or trait that can cause unwanted behaviour, such as a missing requirement, a design flaw or an implementation defect (cf. CWE).
- **vulnerability** (3.1.38): a weakness that an attack path can exploit (cf. CVE).
- **work product** (described in the Introduction; 3.2 lists only its abbreviation, WP): what a cybersecurity activity produces in meeting one or more of the requirements tied to it; Annex A summarizes them. In this audit model it is the evidence an auditor checks.

## 4. Requirement / work-product structure → audit automation (tmodel #15)

Every `[RQ]` produces one or more `[WP]` (e.g. `WP-15-05 = Attack paths, from RQ-15-08/09`).
Because **conformance is itself audited** (§6.4.8 cybersecurity assessment; §5.4.7 audit),
this structure is the template for automating the mechanical parts of an audit:

- model **Requirement → produces → WorkProduct → evidenced_by → Evidence → for_product → Product@version**;
- **audit = query**: for a scope, enumerate applicable requirements → required work products →
  check evidence exists and is human-reviewed-adequate → emit a coverage/gap report;
- **tailoring** (Clause 6) is recorded with rationale and is itself auditable;
- the KG automates coverage/traceability/gaps; a **human judges adequacy**.

`requirements.yaml` (RQ/RC/PM + work_products with `resulting_from`) is the seed dataset.
