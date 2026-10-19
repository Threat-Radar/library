---
schema: "library-summary/v1"
id: alpine-secdb
record: alpine-secdb
type: summary
updated: "2026-10-18"
---

# Alpine Linux security database (secdb)

|  |  |
|---|---|
| **Type** | dataset |
| **Maturity** | _unset_ |
| **Authors** |  |
| **Published** | 2026-10-18 |
| **Identifier** | https://secdb.alpinelinux.org/v3.24/main.json |
| **Source** | https://secdb.alpinelinux.org/v3.24/main.json |
| **Digest** | `de67bce768b8c3d10860f833a070baca8b38b55627422167240058090404dc99` |

## Overview

**A stub: not read in full.** Alpine Linux's security database, published as one JSON and one YAML file per release branch and repository, listing for each package the package versions that fix given vulnerability ids, mostly CVEs, with no severity, weakness or date fields. This record tracks the v3.24 main file. Cited by tmodel RPT-0004 (tmodel#38): the structure of Alpine's feed and which of the pilot's CVEs it did or did not list on the dates checked, which explains why Grype fell back to NVD CPE matches and Trivy reported nothing.

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

Not read in full. Fetched and parsed the v3.24 main JSON and read the site index and licence file, but could not read Alpine's own format description, so the meaning of a 0 key still rests on the tool code Phase 1 read.
