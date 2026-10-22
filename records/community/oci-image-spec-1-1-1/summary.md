---
schema: "library-summary/v1"
id: oci-image-spec-1-1-1
record: oci-image-spec-1-1-1
type: summary
updated: "2026-10-18"
---

# OCI Image Format Specification

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | _unset_ |
| **Authors** |  |
| **Published** | 2025-03-03 |
| **Identifier** | git: https://github.com/opencontainers/image-spec |
| **Source** | https://raw.githubusercontent.com/opencontainers/image-spec/147f9c13cedb47a0c4d9a11a222961073d585877/spec.md |
| **Digest** | `4f700f4549e4c25faa806075bc3e6b4571d0400595cf73f4a142d38cd9d6586e` |

## Overview

**A stub: not read in full.** The OCI Image Format Specification defines how a container image is built from content-addressed parts: content descriptors identified by digest, an image manifest, an optional image index for several platforms, filesystem layers and an image configuration, together with annotations and guidance for storing other artifacts in the same structures. Cited by tmodel RPT-0004 (tmodel#38): the digest, image index, image config (ImageID) and subject rules behind candidate rules R-ID-1 and R-BUILD-1, the build-identity annotations, and the dropped artifact manifest (PR #999).

## Applicability

A stub. `bears_on` (DEC-001, DEC-009) comes from RPT-0004's source log and was not re-assessed here.

## Implementations

Not searched.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this summary |

## Limits

Not read in full. spec.md and the files Phase 1 cited, at the v1.1.1 tag, checked 2026-10-18; not read in full.
