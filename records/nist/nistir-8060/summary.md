---
schema: "library-summary/v1"
id: nistir-8060
record: nistir-8060
type: summary
updated: "2026-10-18"
---

# Guidelines for the Creation of Interoperable Software Identification (SWID) Tags

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | _unset_ |
| **Authors** | David Waltermire, Brant A. Cheikes, Larry Feldman, Greg Witte |
| **Published** | 2016-04 |
| **Identifier** | nist: NIST IR 8060 |
| **Source** | https://nvlpubs.nist.gov/nistpubs/ir/2016/NIST.IR.8060.pdf |
| **Digest** | `9aff60d8aecab8cc6143476867a1ea8a1faf45bbed89d73492c7f77c238a6de8` |

## Overview

**A stub: not read in full.** NIST IR 8060 explains how SWID tags, as defined in ISO/IEC 19770-2, are created, deployed and used across the software lifecycle, and gives numbered guidelines for creating interoperable tags: which elements to provide in corpus, primary, patch and supplemental tags, how authoritative and non-authoritative tag creators differ, and how to list files with hashes. It also describes usage scenarios, including inventory monitoring and identifying vulnerable endpoints by forming CPE names from tag data. Cited by tmodel RPT-0004 (tmodel#38): the SWID tag rules RPT-0004 section 1.3 relies on in place of the paywalled ISO standard: required elements (§3.1), authoritative and non-authoritative tags (§4.2), file listing with hashes (GEN-16, PRI-8) and CPE name generation (§5.2.4, §6.1.3).

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

Not read in full. PDF title pages, abstract, contents and the usage-scenario passages, and the CSRC landing page, checked on 2026-10-18; Phase 1 read the text with pdftotext, but it was not read in full in this phase.
