---
schema: "library-summary/v1"
id: osv-dev
record: osv-dev
type: summary
updated: "2026-10-18"
---

# OSV.dev vulnerability database: data exports and query API

|  |  |
|---|---|
| **Type** | dataset |
| **Maturity** | _unset_ |
| **Authors** |  |
| **Published** | 2026-10-18 |
| **Identifier** | git: https://github.com/google/osv.dev |
| **Source** | https://storage.googleapis.com/osv-vulnerabilities/Alpine/all.zip |
| **Digest** | `7a48aafb7ca0d81d1c50d3080522ea66edb64573c43de2e94636bcfb956a59d7` |

## Overview

**A stub: not read in full.** OSV.dev aggregates vulnerability records in the OSV format from many source databases, converts some other data (Debian, Alpine and NVD) into OSV, and serves the result through a query API and a public Cloud Storage bucket holding a full zip, per-ecosystem zips and CSV lists of records ordered by last modification. On import it may enumerate affected versions, compute Package URLs and recompute aliases. Cited by tmodel RPT-0004 (tmodel#38): evidence that osv.dev adds version-less purls to the records it imports, that its query API matches versions fuzzily, and per-ecosystem export counts (Alpine, Debian, PyPI, Maven, Go, crates.io, Red Hat).

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

Not read in full. Read the data, FAQ and API documents at commit 16b340c7 and checked one export file's structure, but did not re-download the other six exports or re-run any live API query.
