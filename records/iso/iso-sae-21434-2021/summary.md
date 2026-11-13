---
schema: "library-summary/v1"
id: iso-sae-21434-2021
record: iso-sae-21434-2021
type: summary
updated: "2026-11-13"
---

# Road vehicles — Cybersecurity engineering (ISO/SAE 21434:2021)

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | standard (ratified ISO/SAE, first edition 2021-08) |
| **Authors** | ISO/TC 22/SC 32 · SAE |
| **Published** | 2021-08 |
| **Identifier** | ISO/SAE 21434:2021 |
| **Source** | https://www.iso.org/standard/70918.html (purchased; bytes held locally, never committed) |
| **Digest** | `73f990078d3a5b47dec91dd0d2b4e6c24cecd9e4160ae5b143c3b3fa80b7cdf4` |

## Overview

ISO/SAE 21434 is the reference standard for **cybersecurity engineering of road-vehicle
electrical/electronic systems** across the whole lifecycle (concept → development →
production → operations → maintenance → decommissioning). It cancels and supersedes
SAE J3061:2016. Its core method is **TARA — Threat Analysis and Risk Assessment**
(Clause 15): identify damage scenarios and assets, derive threat scenarios, rate
impact in four categories (Safety, Financial, Operational, Privacy), analyse attack
paths, rate **attack feasibility** (Table 1), determine a **risk value**, and decide a
risk treatment. It also draws an **object model** (Figure 3, in the informative Clause 4: item, function,
component, asset, cybersecurity goal and requirement, threat scenario, damage scenario; 3.1 defines
most of these, though not function or cybersecurity requirement) and
tags every provision as a **requirement** (`[RQ-CC-NN]` shall / `[RC-]`
should / `[PM-]` may) that produces auditable **work products** (`[WP-CC-NN]`).

## Why it matters here

Two things make this the core doc to iterate on:
1. **A ready object model + risk pipeline** we can adopt/adapt for tmodel (feeds ARCH-0001,
   the schema #17, and the metrics work #14).
2. **Its requirement/work-product structure is the template for automating conformance
   audits** — a work product is the unit of evidence, so an audit becomes a coverage +
   traceability query over the knowledge graph, with a human judging adequacy (tmodel #15).

## Requirements

**118 requirements** (101 shall / 13 should / 4 may) and **42 work products**, catalogued with clause locators, cross-references and produced work products. Each provision's text is **our own paraphrase**, not the standard's wording: this is a licensed standard, and the sponsor's decision (tmodel#69 sponsor note, hold 1 (2026-10-02); tmodel#154) is paraphrase plus clause IDs, never verbatim text.

- Full structured catalog: [`distilled/requirements.yaml`](distilled/requirements.yaml) (cite as `iso-sae-21434-2021#RQ-CC-NN`)
- Viewable list (designator + short title, per clause): [`distilled/requirements.md`](distilled/requirements.md)

| clause | area | requirements | work products |
|---|---|---|---|
| 5 | Organizational mgmt | 17 | 5 |
| 6 | Project-dependent mgmt | 34 | 4 |
| 7 | Distributed activities | 8 | 1 |
| 8 | Continual activities | 8 | 6 |
| 9 | Concept | 11 | 7 |
| 10 | Product development | 13 | 7 |
| 11 | Validation | 2 | 1 |
| 12 | Production | 3 | 1 |
| 13 | Operations & maintenance | 3 | 1 |
| 14 | End of support | 2 | 1 |
| 15 | TARA methods | 17 | 8 |
| **all** | | **118** | **42** |

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | The normative method for automotive threat modeling & risk |
| Cryptography | adjacent | Uses crypto controls; does not specify primitives |
| This project | core | Object model, TARA pipeline, and audit template all map directly |

Bears on `DEC-003` (risk metric), `DEC-005` (MVP scope), `DEC-009` (product/mitigation
mapping), `DEC-001a` (core object model), `DEC-001b` (governed layer: evidence, gates, CAL),
`DEC-008` (CWE and NVD feeds), `R-011`, `R-012` (ISO 21434 support), `R-013` (Common Criteria
display), `R-018` (human review), `R-021` (mitigation lifecycle).

## Implementations

Tooling exists (e.g. IriusRisk, medini analyze, itemis SECURE, Ansys medini) but not yet
surveyed as build-on-it options — see the products survey (tmodel #7). searched: 2026-09-25.

| Name | Kind | License | URL |
|---|---|---|---|

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `distilled/requirements.yaml` | 118 requirements + 42 work products, paraphrased text, refs, `#RQ-CC-NN` referenceable |
| `distilled/requirements.md` | viewable per-clause table: designator + short title |
| `distilled/normative.md` | object model (Fig 3), TARA pipeline and Table 1, all 40 terms, audit mapping, Annexes A to H, scope, objectives, inputs, figures, coverage map |
| `distilled/examples/` | Annexes E to H as data; 59 test vectors and a script that recomputes them |
| `distilled/state-machine.yaml` | the Clause 8 finding lifecycle and the 6.4.9 release gate to decommissioning |
| `distilled/design-notes.md` | how the standard bears on tmodel's DEC and ADR decisions |
| `distilled/README.md` | index of distilled artifacts + coverage |

## Limits

- Annexes A to H are distilled in our own words (`distilled/normative.md` §5), with the tables of
  Annexes E to H and the worked headlamp TARA as data and test vectors (`distilled/examples/`), on 2026-11-13
  (tmodel#154). The 55 EXAMPLE notes in Clauses 3 to 15 are not carried.
- Requirement statements are **our own paraphrases** (rewritten 2026-11-05), not the
  standard's wording, and are **not yet reviewed line by line** (`reviewed_by` empty). The
  designator, normativity, verb and locator of each entry are kept beside the paraphrase; the
  `verb` field is authoritative for force. Read the standard before relying on any entry.
- A check against the source (tmodel RPT-0007 §7, 2026-10-02) found 16 of the 118 extracted
  texts defective: 5 held annex text instead of the provision (RQ-07-04, RQ-09-03, RQ-09-04,
  RQ-10-08, RQ-11-01), and 11 lost the list items that follow an interrupting NOTE or EXAMPLE
  (RQ-05-11, RQ-06-02, RQ-06-15, RQ-06-16, RQ-06-30, RQ-09-01, RQ-10-01, RQ-10-04, RQ-12-02,
  RQ-13-01, RQ-15-17). On 2026-11-07 all 16 were paraphrased in full from the licensed copy
  (tmodel#154), and each one's `notes` says what the earlier extract had lost or held instead.
  A human pass is still required before any requirement is treated as authoritative.
- Work-product links (22 were missing), locators (5 provision, 14 work product) and three
  work-product titles were corrected against the source on 2026-10-02 (RPT-0007 §7). The
  derived `nature` and `verification` fields follow the links: 47 provisions are now
  deliverable-producing. The 10 work products that the standard ties to subclauses rather than
  provisions list those subclauses in `from_subclauses` (2026-10-03).
- 21434 defines a *method*, not machine-readable schemas; the object model is ours to encode.
