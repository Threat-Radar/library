---
schema: "library-summary/v1"
id: shostack-2008-experiences-threat-modeling-microsoft
record: shostack-2008-experiences-threat-modeling-microsoft
type: summary
updated: "2026-10-22"
---

# Experiences Threat Modeling at Microsoft

|  |  |
|---|---|
| **Type** | paper (workshop paper, 11 pages) |
| **Maturity** | `peer-reviewed` (workshop) |
| **Authors** | Adam Shostack |
| **Published** | Workshop on Modeling Security (MODSEC08) at MODELS 2008, Toulouse; CEUR Workshop Proceedings Vol-413, 2008-11-03 |
| **Identifier** | CEUR-WS Vol-413, paper 12 (no DOI) |
| **Source** | https://ceur-ws.org/Vol-413/paper12.pdf |
| **Digest** | `afc5f5cb642a28ddaa8af16f9e27f249ff61a7cf35fa918244194f278ad37fbf` (retrieved 2026-10-22) |

## Overview

Describes "a decade of experience" threat modeling Microsoft products, and the
method used in the **Security Development Lifecycle (SDL)**: a practical approach,
"usable by non-experts", centred on **data-flow diagrams** with added **trust
boundaries** and a threat-enumeration technique of **"STRIDE per element"**. The
method has four steps — **diagramming, threat enumeration, mitigation and
verification** — and uses the DFD elements process, data store, data flow and
external entity. It states that Microsoft "has had documented threat modeling
methodologies since 1999", lists the published Microsoft versions of the method,
reports lessons learned, and closes with questions for academic research.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | Microsoft's own peer-reviewed account of STRIDE per element in the SDL. |
| Cryptography | none | Not about cryptography. |
| This project | core | The readable, peer-reviewed source for how STRIDE is applied to DFD elements (RPT-0002 §2), which ARCH-0001-PROPOSAL §2 builds on. |

Bears on **DEC-001** (object model — STRIDE as a per-element method facet).

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this summary |

## Limits

- Its history section credits the first 1999 document to Garms, Garg and Howard
  ("Threats to our software"); the document Microsoft released in 2009 is
  Kohnfelder and Garg's "The threats to our products" (see
  `kohnfelder-garg-1999-threats-to-our-products`).
- A practitioner's experience report, not an evaluation of the method's
  effectiveness.
