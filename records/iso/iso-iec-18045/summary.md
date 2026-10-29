---
schema: "library-summary/v1"
id: iso-iec-18045
record: iso-iec-18045
type: summary
updated: "2026-10-25"
---

# ISO/IEC 18045:2022 / CEM:2022 — Methodology for IT security evaluation

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | _unset — do not guess_ |
| **Authors** | ISO/IEC JTC 1/SC 27; CCRA Common Criteria Maintenance Board |
| **Published** | ISO/IEC 18045:2022 (August 2022); CEM:2022 Release 1 (November 2022) |
| **Identifier** | ISO/IEC 18045:2022 · CEM:2022 R1 |
| **Source** | https://www.commoncriteriaportal.org/files/ccfiles/CEM2022R1.pdf |
| **Digest** | `da5b991a457eb32040a15849bfe6d8da1870aef91f6b7255f767f0b186e89a83` (the CCRA PDF) |

**Which text was read.** The ISO edition is licensed and was not obtained. The CCRA publishes the same methodology free as CEM:2022 Release 1. The CEM:2022 foreword says CC:2022/CEM:2022 were developed first as ISO/IEC standards and then published by the CCRA, and the CCMB errata v1.2 states there is no content-level or technical-wording difference between the core parts. This summary reads the CCRA text and paraphrases it. Locators are CEM clause/table numbers.

## Overview

The CEM is the evaluator's methodology for the Common Criteria (`iso-iec-15408`): work units for each assurance class. For tmodel the important part is **Annex B (informative), vulnerability assessment**, which defines **attack potential**. An attack is scored on five factors — elapsed time, specialist expertise, knowledge of the target, window of opportunity, equipment — each with point values (B.6, Table B.2). The points are **summed**, and the total is banded as Basic (0–9), Enhanced-Basic (10–13), Moderate (14–19), High (20–24) or Beyond High (≥25) (Table B.3). The bands tie to the AVA_VAN assurance components (Table B.1). The CEM says the table values "are not mathematically proven" and may need adjusting for a domain (B.5). The method rates each **attack scenario**, and the least "expensive" combination of factor values is the one that counts (B.6).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | The standard attack-effort metric reused by automotive and telecom risk methods. |
| Cryptography | adjacent | Applies to cryptographic mechanisms like any other TOE function. |
| This project | core | ISO/SAE 21434 Annex G's attack-potential approach follows ISO/IEC 18045 (tmodel RPT-0007 §G.2, which lists this standard as "not read" — this record fills that gap). Common Criteria feasibility is display-only under ADR-0006 (R-013). |

Bears on **DEC-003 / ADR-0006** (feasibility method), **R-011**, **R-013**.

**Implications for tmodel (inference).** (1) Attack potential is rated per *attack scenario*, which matches ADR-0006's path-level feasibility on `AttackPath`. It is not a per-step score, so it fits "no per-step aggregation at MVP". (2) If tmodel ever shows CC points (R-013, display-only), it must show the five factor values with the total, because a total alone hides which factor drives the rating. (3) The ETSI TVRA (`etsi-ts-102-165-1`) and ISO/SAE 21434 Annex G reuse the same factor table with different band labels and an inverted direction (high attack potential = low feasibility). A tmodel display must label which scale it shows.

## Implementations

Not searched. No calculator is held.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata; ISO and CCRA identifiers |
| `summary.md` | this summary |

## Limits

- Read only Annex B and the front matter. The 400+ pages of assurance work units were not read.
- The factor values are examples. The CEM itself says they may need domain adjustment (B.5), and ISO/SAE 21434 uses its own banding (RPT-0007).
- The CEM gives no guidance on composing scores across the steps of a multi-step attack. It rates a whole scenario.
- Text was paraphrased, not copied, even though the CCRA licence grants re-use for CC-related documents. That keeps the record consistent with the ISO edition's licence.
