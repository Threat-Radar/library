---
schema: "library-summary/v1"
id: buildkit-attestations
record: buildkit-attestations
type: summary
updated: "2026-10-18"
---

# BuildKit attestations: image attestation storage, SBOMs and SLSA provenance (docs/attestations)

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | _unset_ |
| **Authors** |  |
| **Published** | 2026-10-07 |
| **Identifier** | git: https://github.com/moby/buildkit |
| **Source** | https://raw.githubusercontent.com/moby/buildkit/f5b59a1f2fb25a0cb7072c398cab9aed7835da4e/docs/attestations/attestation-storage.md |
| **Digest** | `9103a45463fbfdacfc34ccf365f8036179b628ccd4762ffc8cdd1125cdbeee9d` |

## Overview

**A stub: not read in full.** BuildKit's attestation documentation specifies how BuildKit creates SBOM and SLSA provenance attestations in the in-toto format and stores them with an image: as attestation manifests inside the image index, marked by reference annotations and, in OCI artifact mode, linked to the image manifest by a subject descriptor. SBOMs are SPDX JSON, and provenance can be SLSA v0.2 or v1, with v1 the default. Cited by tmodel RPT-0004 (tmodel#38): where image attestations are stored (attestation manifests in the image index, subject descriptor in OCI artifact mode), the SPDX JSON SBOM format, and SLSA provenance v0.2 or v1.

## Applicability

A stub. `bears_on` (DEC-001) comes from RPT-0004's source log and was not re-assessed here.

## Implementations

Not searched.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this summary |

## Limits

Not read in full. The six docs/attestations files at v0.34.0 checked 2026-10-18 (storage, SBOM and provenance pages read in part); BuildKit source code was not checked.
