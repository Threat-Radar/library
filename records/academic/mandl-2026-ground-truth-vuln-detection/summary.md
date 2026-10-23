---
schema: "library-summary/v1"
id: mandl-2026-ground-truth-vuln-detection
record: mandl-2026-ground-truth-vuln-detection
type: summary
updated: "2026-10-22"
---

# A Ground-Truth-Based Evaluation of Vulnerability Detection Across Multiple Ecosystems

|  |  |
|---|---|
| **Type** | paper |
| **Maturity** | _unset_ |
| **Authors** | Peter Mandl, Paul Mandl, Martin Häusl, Maximilian Auch |
| **Published** | 2026-04-22 |
| **Identifier** | arxiv: 2604.21111v1 |
| **Source** | https://arxiv.org/pdf/2604.21111v1 |
| **Digest** | `a0c93a1c41137c88e613d975731c81801c837410bc0d6c745f4e22cdaa52ea0b` |

## Overview

**A stub: not read in full.** A preprint that evaluates vulnerability detection tools and services across several software ecosystems against a curated ground-truth dataset derived from the Open Source Vulnerabilities (OSV) database, which maps vulnerabilities to concrete package versions. Because OSV changes daily, the dataset is a snapshot, and the authors publish an open-source tool that rebuilds it from the current OSV database. It reports systematic differences between detection systems. Cited by tmodel RPT-0004 (tmodel#38), section 5, as a study that measures several tools, Trivy v0.69.1 among them, against a ground truth derived from OSV rather than validated by hand.

## Applicability

A stub. `bears_on` (DEC-008) is RPT-0004's use: evidence on how far scanner output can be trusted (section 5). Not re-assessed here.

## Implementations

Not searched.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this summary |

## Limits

Not read in full. On 2026-10-22 the arXiv listing and abstract of v1 were read, and the PDF was checked for the passages RPT-0004 cites (the OSV-derived ground truth and the Trivy version). A preprint, not peer reviewed as far as the listing shows.
