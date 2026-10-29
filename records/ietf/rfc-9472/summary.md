---
schema: "library-summary/v1"
id: rfc-9472
record: rfc-9472
type: summary
updated: "2026-10-22"
---

# A YANG Data Model for Reporting Software Bills of Materials (SBOMs) and Vulnerability Information

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | `standard` |
| **Authors** | E. Lear, S. Rose |
| **Published** | 2023-10 |
| **Identifier** | rfc: 9472 |
| **Source** | https://www.rfc-editor.org/rfc/rfc9472.txt |
| **Digest** | `64a6b305c6fcb81a129fe0ac2d4658e70ec3bfc4e05d95d1edcf27bb98886bf3` |

## Overview

**A stub: not read in full.** RFC 9472 extends the YANG model of Manufacturer Usage Description (MUD) files (RFC 8520) with a transparency schema, so that a device's MUD file can give the locations of its software bill of materials (SBOM) and of its vulnerability information. It also defines a well-known URI, `/.well-known/sbom`, from which management tools can retrieve a device's SBOM from the device itself; the response's format follows its Content-Type. It names SPDX and CycloneDX as examples of SBOM formats, and CycloneDX, CVRF and CSAF for vulnerability information. Cited by tmodel RPT-0004 (tmodel#38): in section 6, as the discovery route that leads from a device, not from an artifact's digest, to its bill, and in Table 2 (Distribution and Delivery).

## Applicability

A stub. `bears_on` (DEC-007) is RPT-0004's use: its section 6 is about the radar to tmodel input contract (ADR-0001). Not re-assessed here.

## Implementations

Not searched.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this summary |

## Limits

Not read in full. On 2026-10-22 the abstract, section 2 (the well-known endpoint) and the references were read, and the RFC Editor's metadata was checked: Proposed Standard, 18 pages, updates nothing and is updated by nothing, no errata. The YANG module was not read.
