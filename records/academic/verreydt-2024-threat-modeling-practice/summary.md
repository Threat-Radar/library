---
schema: "library-summary/v1"
id: verreydt-2024-threat-modeling-practice
record: verreydt-2024-threat-modeling-practice
type: summary
updated: "2026-10-22"
---

# Threat modeling state of practice in Dutch organizations

|  |  |
|---|---|
| **Type** | paper (conference; interview study) |
| **Maturity** | `peer-reviewed` |
| **Authors** | Stef Verreydt, Koen Yskout, Laurens Sion, Wouter Joosen |
| **Published** | SOUPS 2024, Philadelphia, August 2024, USENIX Association |
| **Identifier** | https://www.usenix.org/conference/soups2024/presentation/verreydt (no DOI) |
| **Source** | https://www.usenix.org/system/files/soups2024-verreydt.pdf |
| **Digest** | `2c1aba24e4a2a0bc4d4072fc3724e33c8e96fff9bc8294d359cef8b781927366` (retrieved 2026-10-22) |

## Overview

Semi-structured interviews on how **large Dutch organizations** practise threat
modeling: **13 participants from 7 organizations** (each with thousands of
employees), in 10 interviews. Threat modeling is valued both for finding threats
and for raising developers' security awareness, and motivating developers matters
more than enforcing it as compliance. The challenges named are managing scope,
getting architectural documentation, scaling, and following up on results.
Participants see the opportunity for tooling such as CI/CD integration to trigger
reassessment when a change may introduce new threats, but **none of the
organizations do so, "mostly due to the lack of tool support"**, so threat modeling
"remains mostly a one-time activity" and models are rarely updated.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | Recent evidence on threat modeling in practice. |
| Cryptography | none | Not about cryptography. |
| This project | core | Evidence for the RPT-0002 gap analysis: models that are not kept current, for lack of tools, are what tmodel's engine and re-computation address. |

Bears on **DEC-001** through RPT-0002 §11.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this summary |

## Limits

- Seven large organizations in one country; interview data.
