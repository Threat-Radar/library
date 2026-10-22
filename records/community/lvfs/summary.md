---
schema: "library-summary/v1"
id: lvfs
record: lvfs
type: summary
updated: "2026-10-18"
---

# Linux Vendor Firmware Service (LVFS) documentation

|  |  |
|---|---|
| **Type** | web |
| **Maturity** | _unset_ |
| **Authors** | Richard Hughes |
| **Published** |  |
| **Identifier** | git: https://gitlab.com/fwupd/lvfs-website |
| **Source** | https://lvfs.readthedocs.io/en/latest/claims.html |
| **Digest** | `0dbd0b83d3a9eeaf4daaacc505f3cbec0447a39c339614a8acf9abb45263becc` |

## Overview

**A stub: not read in full.** Documentation for the Linux Vendor Firmware Service, the firmware distribution service used by fwupd. Its Claims page explains the attributes added to every uploaded firmware, including a scan for CoSWID data embedded in SBOM sections of COFF binaries and for uSWID metadata, with external metadata expected for blobs such as microcode; its SBOM Generation Helper builds uSWID, CoSWID, SWID XML or INI files for components without native SBOM metadata. Cited by tmodel RPT-0004 (tmodel#38): firmware-update service practice: every uploaded firmware is scanned for embedded CoSWID and uSWID SBOM data (dimension 2, firmware bills in practice).

## Applicability

A stub. `bears_on` (DEC-002) comes from RPT-0004's source log and was not re-assessed here.

## Implementations

Not searched.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this summary |

## Limits

Not read in full. Read the Claims page, the SBOM Specification page and the helper form; no per-firmware SBOM export was inspected and nothing was uploaded.
