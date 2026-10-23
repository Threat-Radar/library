---
schema: "library-summary/v1"
id: zhou-2025-sbom-reality-check
record: zhou-2025-sbom-reality-check
type: summary
updated: "2026-10-22"
---

# A Reality Check on SBOM-based Vulnerability Management: An Empirical Study and A Path Forward

|  |  |
|---|---|
| **Type** | paper |
| **Maturity** | _unset_ |
| **Authors** | Li Zhou, Marc Dacier, Charalambos Konstantinou |
| **Published** | 2026-04-17 |
| **Identifier** | arxiv: 2511.20313v2 |
| **Source** | https://arxiv.org/pdf/2511.20313v2 |
| **Digest** | `b18cbc4f41190867f2330acd2e3b1b071b223dff2bd5bae9c70a07f0728dfc45` |

## Overview

**A stub: not read in full.** An empirical study of 2,414 open-source repositories. It finds that lock files used with strong package managers give accurate and consistent SBOMs, but that on such SBOMs the downstream vulnerability scanners still produced a 92.0% false positive rate in its case study, mostly by flagging vulnerabilities in unreachable code; function call analysis pruned 61.9% of those false alarms. Cited by tmodel RPT-0004 (tmodel#38), section 5: from the same accurate SBOM, Grype and Trivy agreed almost perfectly, yet manual inspection of four repositories confirmed only 9 of the 113 vulnerabilities in the union of their findings (the paper names Trivy 0.66.0 and Syft 1.33.0).

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

Not read in full. On 2026-10-22 the arXiv listing and abstract of v2 were read, and the passages RPT-0004 cites (the tool versions, the four repositories and the 9 of 113) were checked in the PDF. The ACM version (DOI 10.1145/3800506.3803490) was not read.
