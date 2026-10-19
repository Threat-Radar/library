---
schema: "library-summary/v1"
id: rosso-2026-svs-test
record: rosso-2026-svs-test
type: summary
updated: "2026-10-18"
---

# A Practical Solution to Systematically Monitor Inconsistencies in SBOM-based Vulnerability Scanners

|  |  |
|---|---|
| **Type** | paper |
| **Maturity** | _unset_ |
| **Authors** | Martin Rosso, Muhammad Asad Jahangir Jaffar, Alessandro Brighente, Mauro Conti |
| **Published** | 2025-12-19 |
| **Identifier** | arxiv: 2512.17710v1 |
| **Source** | https://arxiv.org/pdf/2512.17710v1 |
| **Digest** | `4ff067220c54a207531af8db5b98442dc833f2a7ffd2e3b0718cde98be94deb0` |

## Overview

**A stub: not read in full.** Introduces SVS-TEST, a method and tool for testing SBOM-based vulnerability scanners against crafted SBOMs with a known ground truth, and applies it to seven scanners with 16 SBOMs. It reports large differences in reliability and error handling, including scanners that fail silently on valid input. Cited by tmodel RPT-0004 (tmodel#38): published evidence on how SBOM-based scanners handle purl and CPE input, including tools that ignore the purl version or fail silently (dimension 5, Q4).

## Applicability

A stub. `bears_on` (DEC-002, DEC-008) comes from RPT-0004's source log and was not re-assessed here.

## Implementations

Not searched.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this summary |

## Limits

Not read in full. I read the arXiv listing, abstract, title page and the tool-version table of v1 and the Crossref record; I did not re-check the results or the Zenodo artifacts.
