---
schema: "library-summary/v1"
id: iso-sae-21434-2021
record: iso-sae-21434-2021
type: summary
updated: "2026-09-25"
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
risk treatment. It also defines a normative **object model** (Figure 3: item, function,
component, asset, cybersecurity goal/requirement, threat scenario, damage scenario) and
structures every obligation as a tagged **requirement** (`[RQ-CC-NN]` shall / `[RC-]`
should / `[PM-]` may) that produces auditable **work products** (`[WP-CC-NN]`).

## Why it matters here

Two things make this the core doc to iterate on:
1. **A ready object model + risk pipeline** we can adopt/adapt for tmodel (feeds ARCH-0001,
   the schema #17, and the metrics work #14).
2. **Its requirement/work-product structure is the template for automating conformance
   audits** — a work product is the unit of evidence, so an audit becomes a coverage +
   traceability query over the knowledge graph, with a human judging adequacy (tmodel #15).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | The normative method for automotive threat modeling & risk |
| Cryptography | adjacent | Uses crypto controls; does not specify primitives |
| This project | core | Object model, TARA pipeline, and audit template all map directly |

Bears on `DEC-003` (risk metric), `DEC-005` (MVP scope), `DEC-009` (product/mitigation
mapping), `R-011`, `R-012` (ISO 21434 support), `R-021` (mitigation lifecycle).

## Implementations

Tooling exists (e.g. IriusRisk, medini analyze, itemis SECURE, Ansys medini) but not yet
surveyed as build-on-it options — see the products survey (tmodel #7). searched: 2026-09-25.

| Name | Kind | License | URL |
|---|---|---|---|

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `distilled/requirements.yaml` | 118 requirements (RQ/RC/PM) + 42 work products, `#RQ-CC-NN` referenceable |
| `distilled/normative.md` | TARA pipeline, object model (Fig 3), Table 1 feasibility, terminology, audit mapping |
| `distilled/README.md` | index of distilled artifacts + coverage |

## Limits

- Distilled from the document body; **Annexes not distilled** — impact criteria (Annex F),
  attack-feasibility methods (attack-potential / CVSS / attack-vector, Annexes G/H), and the
  worked example are referenced but not extracted.
- Requirement statements are **verbatim prefixes** (≤320 chars) and **not yet reviewed
  line-by-line** against the source (`reviewed_by` empty). A human pass is required before
  any requirement is treated as authoritative.
- 21434 defines a *method*, not machine-readable schemas; the object model is ours to encode.
