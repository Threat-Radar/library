---
schema: "library-summary/v1"
id: mbaka-tuma-2024-stride-replication
record: mbaka-tuma-2024-stride-replication
type: summary
updated: "2026-10-22"
---

# On the Measures of Success in Replication of Controlled Experiments with STRIDE

|  |  |
|---|---|
| **Type** | paper (journal article; controlled experiment, replication) |
| **Maturity** | `peer-reviewed` |
| **Authors** | Winnie Mbaka, Katja Tuma |
| **Published** | International Journal of Software Engineering and Knowledge Engineering 34(04), 623–650, 2024, World Scientific |
| **Identifier** | DOI 10.1142/s0218194023500651; arXiv 2208.01524 |
| **Source** | preprint "A replication of a controlled experiment with two STRIDE variants", https://arxiv.org/pdf/2208.01524 |
| **Digest** | `10d23f6041f1305b141e0174a42cfa26ffed0e4beffc4c3d104e755e3f499c86` (the preprint, retrieved 2026-10-22) |

## Overview

A replication of an earlier controlled experiment comparing two variants of
STRIDE: **per element** (threats enumerated for each DFD element) and **per
interaction** (threats enumerated for each interaction between elements). **45
student participants** in teams, with about two hours for the analysis, measured
on **productivity** (correct threats per hour) and **precision**. In the preprint's
tables, per-element teams averaged 2.5 correct threats per hour at 0.40 precision,
and per-interaction teams 3.57 at 0.43. Per-interaction teams "performed better
(albeit, not significantly)", contradicting the original study's claim that this
variant suits expert analysts better. Both groups reported many false positives.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | Controlled evidence on STRIDE's variants. |
| Cryptography | none | Not about cryptography. |
| This project | adjacent | Neither enumeration strategy clearly wins, and manual precision is low — evidence for the RPT-0002 gap analysis on automating threat elicitation. |

Bears on **DEC-001** through RPT-0002 §11.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this summary |

## Limits

- **Preprint read, not the journal version:** the numbers above come from the
  preprint's tables; the journal text may differ.
- Students, a single system, about two hours (the original allowed about four).
