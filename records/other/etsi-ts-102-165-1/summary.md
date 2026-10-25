---
schema: "library-summary/v1"
id: etsi-ts-102-165-1
record: etsi-ts-102-165-1
type: summary
updated: "2026-10-25"
---

# ETSI TS 102 165-1 V5.3.1 — Threat, Vulnerability, Risk Analysis (TVRA)

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | _unset — do not guess_ (ETSI Technical Specification) |
| **Authors** | ETSI TC CYBER |
| **Published** | 2025-02 (V5.3.1); earlier versions from 2003 in the same deliverable directory |
| **Identifier** | ETSI TS 102 165-1 V5.3.1 |
| **Source** | https://www.etsi.org/deliver/etsi_ts/102100_102199/10216501/05.03.01_60/ts_10216501v050301p.pdf |
| **Digest** | `aa1efd2c8dc0145b111901f980ad8c86a4d8cd84f410ecb333ae79966213afbb` |

## Overview

TVRA is ETSI's systematic risk-analysis method for ICT systems. The analyst inventories the **assets** and their relationships, identifies **weaknesses** and the **vulnerabilities** they create (a weakness that a threat can exploit), and identifies **threat agents** and attack methods (clause 6). The analyst then rates each attack and selects countermeasures with a cost-benefit step (6.9–6.10). Likelihood is built in three stages:

1. **Attack potential** is computed by summing five factors — time, expertise, knowledge, opportunity, equipment — using the CEM B.6 values (Table 10; an Opportunity of "None" scores 999).
2. That sum is banded into a **vulnerability rating**, Basic to Beyond High (Table 11).
3. The rating is combined with a **threat level** from attacker motivation × capability (Tables 7–9) to give an **occurrence likelihood** of 1–3 (Table 12, 6.7).

**Risk = likelihood × impact.** Impact is also 1–3 (Table 3), and attack intensity can raise it (Tables 6, 13). The product is classed as Minor (1–2), Major (3–4) or Critical (6, 9) (5a.1, 6.8.2, Table 15). V5.3.1 adds informative annexes on AI/ML as attacker or attack determinant (Annex J) and on applying TVRA to AI/ML systems, including systems whose behaviour changes after deployment (Annex K).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | A complete, free threat-and-risk-analysis method. |
| Cryptography | adjacent | Notes that CEM metrics can misjudge long-term cryptanalytic risk (5a.1). |
| This project | core | It is a free TARA to compare with ADR-0006. ISO/SAE 21434 lists TVRA as an example threat-scenario method (RPT-0007 §15.4), and RPT-0007 lists TVRA as "not read" — this record fills that gap. |

Bears on **DEC-003 / ADR-0006**, **DEC-005**, **R-011**.

**Implications for tmodel (inference).**
- **Same input, different output.** TVRA and ISO/SAE 21434 Annex G both start from the CEM attack-potential factors (`iso-iec-18045`). TVRA multiplies likelihood by impact and outputs a single class. ADR-0006 keeps impact as a 4-category S/F/O/P vector and derives risk per category. A TVRA import or crosswalk must keep the vector and must not adopt the product.
- **Adds attacker intent.** TVRA's threat level (motivation × capability) has no slot in ADR-0006, which rates feasibility from the attack alone. It could be a Party (threat-agent) property that informs, but does not change, the human feasibility rating.
- **Cumulative impact.** TVRA asks the analyst to consider cumulative impact across several assets (5a.2). That corresponds to tmodel's worst-path fold plus composition, and should be noted for R-020/DEC-009.
- **Agentic threats.** Annex K's point that an AI system's behaviour can change after deployment argues for re-review triggers on AI-related ThreatInstances (#71/#78).

## Implementations

Annex G describes a risk-calculation template and tool. That tool was not obtained or checked. No other implementations were searched.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this summary |

## Limits

- Read clauses 4–6, 5a, the tables and Annexes J/K. Annex A (pro forma), the Annex B motivation discussion and Annexes G/H (templates) were not read in detail.
- **Internal cross-reference slip.** 6.8.2.1 says to multiply likelihood "from table 15" by impact "from table 14", but in this version Table 14 is occurrence likelihood, Table 15 is the risk classes, and impact is Table 3/13. Cite the tables by content, not by number.
- Equal values for "very unlikely/unlikely" and "likely/very likely" (Table 4 note) leave a 3-point likelihood scale. The product therefore takes only the values 1, 2, 3, 4, 6, 9.
- TVRA is not limited to telecom, but its examples and history are ETSI/telecom. It has no automotive S/F/O/P impact categories.
