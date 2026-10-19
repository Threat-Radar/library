---
schema: "library-summary/v1"
id: rfc-9393
record: rfc-9393
type: summary
updated: "2026-10-18"
---

# Concise Software Identification Tags

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | `standard` |
| **Authors** | H. Birkholz, J. Fitzgerald-McKay, C. Schmidt, D. Waltermire |
| **Published** | 2023-06 |
| **Identifier** | rfc: 9393 |
| **Source** | https://www.rfc-editor.org/rfc/rfc9393.txt |
| **Digest** | `6708be37258615edb39de76e32b11439967885d6792f4e2f0ee02de1a0864ebc` |

## Overview

**A stub: not read in full.** RFC 9393 defines Concise SWID (CoSWID) tags, a CBOR encoding, specified in CDDL, of the software identification information that ISO/IEC 19770-2:2015 SWID tags carry in XML. It covers the tag data model (tag identifier and version, entities and their roles, links, software metadata, and payload and evidence resources with hashes), IANA registries for its index values, the swid and swidpath URI schemes, and COSE-signed tags. Cited by tmodel RPT-0004 (tmodel#38): SWID and CoSWID as the third format in RPT-0004 section 1.3: tag-id uniqueness, hash entries, link relations, and the absence of hardware, completeness and vulnerability fields.

## Applicability

A stub. `bears_on` (DEC-001, DEC-002) comes from RPT-0004's source log and was not re-assessed here.

## Implementations

Not searched. The implementations RPT-0004 cites are listed in `record.yaml`: python-uswid 0.6.0; coreboot 26.09 SBOM support, src/sbom.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this summary |

## Limits

Not read in full. RFC text, RFC Editor metadata and the errata page checked on 2026-10-18; Phase 1 read the text and counted its BCP 14 keywords, but it was not read in full in this phase.
