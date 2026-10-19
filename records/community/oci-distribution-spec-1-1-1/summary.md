---
schema: "library-summary/v1"
id: oci-distribution-spec-1-1-1
record: oci-distribution-spec-1-1-1
type: summary
updated: "2026-10-18"
---

# Open Container Initiative Distribution Specification

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | _unset_ |
| **Authors** |  |
| **Published** | 2025-01-29 |
| **Identifier** | git: https://github.com/opencontainers/distribution-spec |
| **Source** | https://raw.githubusercontent.com/opencontainers/distribution-spec/a139cc423184af6078077b9b7ee336eddbd03f8f/spec.md |
| **Digest** | `360b29820869bfaac5f73ebfa30669c9172c069ef619f8c6689acc3bcef6f719` |

## Overview

**A stub: not read in full.** The OCI Distribution Specification defines the HTTP API between registries and clients for pushing, pulling and discovering content by tag or digest, including tag listing, content management and the referrers API for finding artifacts that refer to a given manifest. It derives from the Docker Registry HTTP API V2 protocol. Cited by tmodel RPT-0004 (tmodel#38): the definitions of digest and tag, the client duty to verify a manifest pulled by digest, and the referrers API with its tag-schema fallback.

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

Not read in full. spec.md at the v1.1.1 tag checked 2026-10-18 (introduction, definitions and structure); not read in full.
