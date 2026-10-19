---
schema: "library-summary/v1"
id: osfw-firmware-embedded-sbom-0-10
record: osfw-firmware-embedded-sbom-0-10
type: summary
updated: "2026-10-18"
---

# Firmware Embedded SBOM Specification

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | `draft` |
| **Authors** | Richard Hughes, Martin Fernandez, Adam Williamson |
| **Published** | 2024-02-21 |
| **Identifier** | git: https://github.com/open-source-firmware/sbom |
| **Source** | https://sbomspec.osfw.foundation/ |
| **Digest** | `52dcd10bcec2ac09cd44a3ae8982f415e0abc2507f8b0d2804f4a5dd59305e9e` |

## Overview

**A stub: not read in full.** Prerelease specification (revision 0.10) for embedding SBOM metadata in firmware images and their components. It requires CoSWID tags in CBOR (RFC 9393), carried in a .sbom section of PE binaries or behind a uSWID header in other binaries, lists the attributes each tag must hold (identifier, vendor entity, component relationships), and describes how firmware and platform SBOMs are assembled, converted, signed and read back. Cited by tmodel RPT-0004 (tmodel#38): the only written firmware SBOM profile found: its required CoSWID attributes and where the SBOM sits in the image (dimension 2, firmware bills in practice).

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

Not read in full. Checked the metadata, revision history, licence, section headings and the CoSWID and uSWID requirements in the sources at the pinned commit; the requirements were not extracted or counted here.
