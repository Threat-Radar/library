---
schema: "library-summary/v1"
id: sbomproof-2025
record: sbomproof-2025
type: summary
updated: "2026-10-18"
---

# SBOMproof: Beyond Alleged SBOM Compliance for Supply Chain Security of Container Images

|  |  |
|---|---|
| **Type** | paper |
| **Maturity** | _unset_ |
| **Authors** | Jacopo Bufalino, Mario Di Francesco, Agathe Blaise, Stefano Secci |
| **Published** | 2025-10-07 |
| **Identifier** | arxiv: 2510.05798 |
| **Source** | https://arxiv.org/pdf/2510.05798v1 |
| **Digest** | `df6ea23bf601372f61c785889e0208a002f2d5f46c33a5460766e9873ade4a4f` |

## Overview

**A stub: not read in full.** An empirical study of SBOM generators and vulnerability scanners, both open source tools and cloud provider services, applied to operating system packages in widely used Linux container base images. The authors find the tools largely incompatible, with package URLs that differ between tools and depart from the purl specification, which leads to missed vulnerabilities; they call the resulting problem SBOM confusion. Cited by tmodel RPT-0004 (tmodel#38): evidence that SBOM tools write different, often non-conforming purls for the same container packages.

## Applicability

A stub. `bears_on` (DEC-002) comes from RPT-0004's source log and was not re-assessed here.

## Implementations

Not searched.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this summary |

## Limits

Not read in full. Abstract page and v1 PDF (18 pages) checked 2026-10-18; the paper was not read in full and its results were not reproduced.
