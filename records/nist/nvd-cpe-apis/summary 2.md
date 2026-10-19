---
schema: "library-summary/v1"
id: nvd-cpe-apis
record: nvd-cpe-apis
type: summary
updated: "2026-10-18"
---

# NVD Products APIs 2.0: CPE API and CPE Match Criteria API

|  |  |
|---|---|
| **Type** | dataset |
| **Maturity** | _unset_ |
| **Authors** |  |
| **Published** |  |
| **Identifier** | api_cpe: https://services.nvd.nist.gov/rest/json/cpes/2.0 |
| **Source** | https://csrc.nist.gov/schema/nvd/api/2.0/cpe_api_json_2.0.schema |
| **Digest** | `102ae482c48e8edfdd56ebae4e9d487675bf6499c4ee5479732a6b1b9e81df36` |

## Overview

**A stub: not read in full.** NIST's National Vulnerability Database serves the Official CPE Dictionary and CVE match criteria through two version 2.0 REST endpoints: the CPE API, which returns dictionary records with NVD-assigned identifiers, dates and deprecation flags, and the CPE Match Criteria API, which returns the match strings and match string ranges used in CVE applicability statements. The record also covers NVD's 2025 and 2026 notices that removed the legacy CPE feeds and limited which CVEs NVD enriches. Cited by tmodel RPT-0004 (tmodel#38): pilot CPE dictionary lookups, CVE match criteria with version ranges, the removal of the legacy CPE dictionary feeds on 2025-08-20, and the enrichment prioritization of 2026-04-15.

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

Not read in full. Documentation text, both response schemas, the news page and one live query per API checked 2026-10-18; the dictionary and match feeds were not downloaded.
