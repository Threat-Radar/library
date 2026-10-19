---
schema: "library-summary/v1"
id: benedetti-2024-sbom-python
record: benedetti-2024-sbom-python
type: summary
updated: "2026-10-18"
---

# The Impact of SBOM Generators on Vulnerability Assessment in Python: A Comparison and a Novel Approach

|  |  |
|---|---|
| **Type** | paper |
| **Maturity** | _unset_ |
| **Authors** | Giacomo Benedetti, Serena Cofano, Alessandro Brighente, Mauro Conti |
| **Published** | 2024-09-10 |
| **Identifier** | arxiv: 2409.06390v1 |
| **Source** | https://arxiv.org/pdf/2409.06390v1 |
| **Digest** | `51d5ab2467a212b89e8bf09235d2b35dd4ab63cffd0cd2c696a473e32c6bcd88` |

## Overview

**A stub: not read in full.** Evaluates Python SBOM generators (cdxgen, GitHub's SBOM export, ORT, Syft and Trivy) by passing their output to a vulnerability scanner and comparing the results with a ground truth, traces the errors to component identification and dependency resolution, and proposes PIP-sbom, a pip-based generator that the authors report as more precise. Cited by tmodel RPT-0004 (tmodel#38): published evidence that the SBOM generator changes vulnerability results for Python packages, mostly through false positives (dimension 5, Q4).

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

Not read in full. I read the arXiv listing, abstract and title page of v1, searched its text for the tool names, and read the Crossref record of the LNCS version; I did not re-check the paper's tables or read the LNCS text.
