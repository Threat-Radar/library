---
schema: "library-summary/v1"
id: scandariato-2015-stride-descriptive-study
record: scandariato-2015-stride-descriptive-study
type: summary
updated: "2026-10-22"
---

# A descriptive study of Microsoft's threat modeling technique

|  |  |
|---|---|
| **Type** | paper (journal article; empirical study) |
| **Maturity** | `peer-reviewed` |
| **Authors** | Riccardo Scandariato, Kim Wuyts, Wouter Joosen |
| **Published** | Requirements Engineering 20(2), 163–180 (online December 2013, issue June 2015), Springer |
| **Identifier** | DOI 10.1007/s00766-013-0195-2 |
| **Source** | authors' manuscript, https://lirias.kuleuven.be/retrieve/245643 |
| **Digest** | `a24e2856c088aa6649ce419858ee15d1b356ccbc9483369345b26343800dc9f1` (retrieved 2026-10-22) |

## Overview

The first empirical study of **STRIDE's cost and effectiveness**, by its own
account: a descriptive study with **57 final-year master's students** in computer
science. It measures how many valid threats are found per hour, how many of the
reported threats are incorrect (false positives) and how many are missed (false
negatives). The headline result: the average number of incorrect threats is low,
**19–24% of the threats produced**, but the average number of overlooked threats is
very high, **64–69% of all threats**.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | Measured evidence on how well the most used threat-modeling method performs by hand. |
| Cryptography | none | Not about cryptography. |
| This project | core | Evidence for the RPT-0002 gap analysis: manual STRIDE misses most threats, which is the case for tool support and for engine-computed paths. |

Bears on **DEC-001** (object model) through RPT-0002 §11.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this summary |

## Limits

- Students, not practitioners, on a given system; the authors discuss the threats
  to validity.
- Read in the authors' manuscript; the published version may differ in wording.
