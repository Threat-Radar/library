---
schema: "library-summary/v1"
id: uefi-firmware-sbom-proposal-2023
record: uefi-firmware-sbom-proposal-2023
type: summary
updated: "2026-10-18"
---

# Firmware SBOM Proposal

|  |  |
|---|---|
| **Type** | article |
| **Maturity** | _unset_ |
| **Authors** | Richard Hughes, Martin Fernandez |
| **Published** | 2023-10-04 |
| **Identifier** | https://uefi.org/blog/firmware-sbom-proposal |
| **Source** | https://uefi.org/blog/firmware-sbom-proposal |
| **Digest** | `185f11b4b7810c3141c3443dff1066b0f270dbccf00bbab4d53313e9054cae24` |

## Overview

**A stub: not read in full.** UEFI Forum blog post in which the authors present for feedback a possible solution, arising from the UEFI SBOM sub-team's work on recommendations, for how firmware that conforms to the UEFI standard could carry SBOM data. It sorts firmware into four kinds of component (immutable space-critical blobs, immutable large blobs, precompiled PE binaries, PE binaries built from source) and recommends for each a way to attach CoSWID tags: detached metadata, a uSWID header, or a .sbom COFF section, combined into a composite firmware SBOM. Cited by tmodel RPT-0004 (tmodel#38): context: the proposal to the UEFI ecosystem that became the Firmware Embedded SBOM Specification.

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

Not read in full. Read the post's byline, date, section headings and recommendations; did not follow the linked tools or examples, and the 2024 Plugfest deck was only identified and digested, not read in full.
