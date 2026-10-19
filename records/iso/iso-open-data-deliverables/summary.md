---
schema: "library-summary/v1"
id: iso-open-data-deliverables
record: iso-open-data-deliverables
type: summary
updated: "2026-10-18"
---

# ISO Deliverables Metadata

|  |  |
|---|---|
| **Type** | dataset |
| **Maturity** | _unset_ |
| **Authors** |  |
| **Published** | 2026-10-14 |
| **Identifier** | dataset: iso_deliverables_metadata |
| **Source** | https://isopublicstorageprod.blob.core.windows.net/opendata/_latest/iso_deliverables_metadata/csv/iso_deliverables_metadata.csv |
| **Digest** | `36aad5a43316f54fe327601a0ef032d131eea873597f64dc7866307219c0ad62` |

## Overview

**A stub: not read in full.** ISO Open Data's ISO Deliverables Metadata dataset gives one row per ISO deliverable, published or in development, with its reference, titles, publication date, edition, ICS codes, owner committee, current harmonized stage code, replaces and replacedBy links, languages, page count and scope text, in CSV, JSON Lines and Parquet. ISO publishes it under the ODC Attribution License (ODC-By) v1.0, and its separate stage-codes page gives the meaning of each stage code. Cited by tmodel RPT-0004 (tmodel#38): the ISO status and stage of the standards RPT-0004 cites (ISO/IEC 5962, DIS 27055, DIS 27056, 19770-2, 19770-6 and 18670), with stage meanings from ISO's stage-codes page.

## Applicability

A stub. `bears_on` (DEC-001, DEC-002) comes from RPT-0004's source log and was not re-assessed here.

## Implementations

Not searched.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this summary |

## Limits

Not read in full. CSV and JSONL snapshot of 2026-10-14 downloaded and filtered for the cited references on 2026-10-18, and the dataset page read through its Wayback capture of 2026-09-15 (iso.org returns 403); the dataset was not otherwise analysed.
