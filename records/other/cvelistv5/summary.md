---
schema: "library-summary/v1"
id: cvelistv5
record: cvelistv5
type: summary
updated: "2026-10-18"
---

# CVE List V5 (CVEProject/cvelistV5)

|  |  |
|---|---|
| **Type** | dataset |
| **Maturity** | _unset_ |
| **Authors** |  |
| **Published** | 2026-10-08 |
| **Identifier** | git: https://github.com/CVEProject/cvelistV5 |
| **Source** | https://github.com/CVEProject/cvelistV5/releases/download/cve_2026-10-08_1700Z/2026-10-08_all_CVEs_at_midnight.zip.zip |
| **Digest** | `affae4d6b70a956a6699d0e811449e11605effeff964a6647f78e68bc5072015` |

## Overview

**A stub: not read in full.** The official CVE List, published by the CVE Program as a GitHub repository of CVE records in CVE Record Format 5 JSON, refreshed about every seven minutes from the CVE Services API, with GitHub releases that carry a daily midnight baseline zip of all records and hourly delta zips. Each record has a CNA container and may add the CVE Program container and ADP containers such as CISA's. Cited by tmodel RPT-0004 (tmodel#38): the 2026-10-08 snapshot used to count how CVE records name affected products (packageURL, cpeApplicability, vendor and product given as n/a, versionType values) and which ADP containers they carry.

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

Not read in full. Checked the release, its tag commit and the asset's size and GitHub-listed digest through the GitHub API and read the README at the tag commit, but did not download or parse the archive, so all record counts rest on Phase 1.
