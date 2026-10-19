---
schema: "library-summary/v1"
id: cisa-vulnrichment
record: cisa-vulnrichment
type: summary
updated: "2026-10-18"
---

# CISA Vulnrichment

|  |  |
|---|---|
| **Type** | dataset |
| **Maturity** | _unset_ |
| **Authors** |  |
| **Published** | 2026-10-08 |
| **Identifier** | git: https://github.com/cisagov/vulnrichment |
| **Source** | https://raw.githubusercontent.com/cisagov/vulnrichment/776f3efcb14b2d86cdb6246b3eddb7ab0da5f1a2/README.md |
| **Digest** | `ffec1da10bdea8a98458362f7136d31b4143ef21875b6aa4b5d7bd9041164ba9` |

## Overview

**A stub: not read in full.** CISA's public repository of its enrichment of CVE records through the CISA ADP container: SSVC decision points for the CVEs it assesses, a KEV block for CVEs in the Known Exploited Vulnerabilities catalog, and CWE and CVSS data where the originating CNA gave none. CPE strings were added only until 10 December 2024, and the results also flow back into the CVE records themselves. Cited by tmodel RPT-0004 (tmodel#38): CISA's stated rules for the CISA ADP container: it fills fields the CNA left empty, never overwrites the CNA container, and the CNA's data takes precedence when both give a value.

## Applicability

A stub. `bears_on` (DEC-008) comes from RPT-0004's source log and was not re-assessed here.

## Implementations

Not searched.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this summary |

## Limits

Not read in full. Read the README at the cited commit, but not the enriched record files or the flowcharts, so the counts of CISA-ADP containers still come from Phase 1's cvelistV5 snapshot.
