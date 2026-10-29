---
schema: "library-summary/v1"
id: first-cvss
record: first-cvss
type: summary
updated: "2026-10-25"
---

# FIRST CVSS — specification family

|  |  |
|---|---|
| **Type** | hierarchy (one record for the family; versions are their own records) |
| **Maturity** | _unset — do not guess_ |
| **Authors** | FIRST CVSS Special Interest Group |
| **Published** | v4.0 announced November 2023 (FIRST CVSS page); v3.1, v3.0, v2 and v1 archived on the same site |
| **Identifier** | https://www.first.org/cvss/ |
| **Source** | https://www.first.org/cvss/ (web page; retrieved 2026-10-25; can change) |
| **Digest** | `8ee54bdaf17941f9329407c96f402c46a61743d0ae03e5d13df2c436d9239b4d` (HTML bytes as retrieved; the page changes) |

## Overview

The FIRST CVSS SIG maintains the Common Vulnerability Scoring System. On 2026-10-25 its landing page said CVSS "is currently at version 4.0" and that the SIG keeps revising the v4.0 user guide, FAQ and examples. It listed archives for v3.1, v3.0, v2 and v1 and announced a new CVSS **Consumer Implementation Guide** on tailoring scores to deployment environments. The version texts tmodel holds are `first-cvss-v3-1` and `first-cvss-v4-0`. This record is their family parent, because a CVSS score only means something together with its version.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | The de facto severity score on CVE/NVD records. |
| Cryptography | none | — |
| This project | core | Every imported Vulnerability carries CVSS. ADR-0006 refuses CVSS as the risk number, so tmodel must say exactly where CVSS appears. |

Bears on **DEC-003 / ADR-0006** and **R-011**.

**What tmodel takes from CVSS (from ADR-0006 and the version records; our position, not FIRST's):**
- **Display and evidence only.** A Vulnerability's CVSS vector and score are shown with their version and source (CNA or NVD/ADP; see `cve-json-5`). They are never the RiskScore and never folded into it (ADR-0006 scope guard).
- **Not feasibility by default.** ISO/SAE 21434 Annex G allows a CVSS-based feasibility rating written for v3.1 (RPT-0007). `first-cvss-v4-0` records that v4.0 defines no exploitability subscore, so that route does not carry over to v4.0 vectors as they stand. ADR-0006 rates feasibility with Table-1 and a human, not CVSS.
- **Do not sum.** `bron` shows how summed CVSS ranks products by version count. NVD assigns 10 to CVEs with no information (bron §5.1.1). Aggregate views must not add scores.

## Implementations

FIRST publishes official calculators for v4.0 and v3.1 (landing-page links). They were not reviewed. Nothing else was searched.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata; `see_also` to the version records |
| `summary.md` | this summary |

## Limits

- A landing page, not a specification. All technical detail belongs to the version records.
- The version records (`first-cvss-v3-1`, `first-cvss-v4-0`) are stubs by another contributor and were not edited here. Linking them back with `part_of` is left to their owner.
- EPSS and SSVC (other FIRST/CISA prioritisation schemes) are separate records (`first-epss`, `ssvc`), currently in library#21.
