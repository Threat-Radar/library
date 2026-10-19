---
schema: "library-summary/v1"
id: anchore-nvd-data-overrides
record: anchore-nvd-data-overrides
type: summary
updated: "2026-10-18"
---

# NVD Data Overrides (anchore/nvd-data-overrides)

|  |  |
|---|---|
| **Type** | dataset |
| **Maturity** | _unset_ |
| **Authors** |  |
| **Published** | 2026-10-08 |
| **Identifier** | git: https://github.com/anchore/nvd-data-overrides |
| **Source** | https://raw.githubusercontent.com/anchore/nvd-data-overrides/56fa5a1cc8b7721500beeb17e9c9ce2e679b2205/README.md |
| **Digest** | `fd2a2d6647dd743b28adff9d68e30c4061794b99377631eff8f19ce59527f471` |

## Overview

**A stub: not read in full.** Anchore's repository of enriched vulnerability data in NVD-compatible format, one JSON file per CVE under data/<year>/, generated every hour from Anchore's cve-data-enrichment repository. The files add CPE configurations for CVEs that NVD has not analysed or correct existing ones; both files read also record the reason for the override. Cited by tmodel RPT-0004 (tmodel#38): evidence that the version ranges behind Grype's nvd:cpe matches can come from Anchore's overrides rather than from NVD, which explained a range that NVD's own record did not contain.

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

Not read in full. Read the README and two override files at the reconstructed commit, but not the schema, the scripts or the upstream enrichment repositories.
