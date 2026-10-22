---
schema: "library-summary/v1"
id: sigstore-bundle-v0-3
record: sigstore-bundle-v0-3
type: summary
updated: "2026-10-18"
---

# Sigstore Bundle (sigstore_bundle.proto), media type version 0.3

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | _unset_ |
| **Authors** | The Sigstore Authors |
| **Published** | 2026-08-21 |
| **Identifier** | git: https://github.com/sigstore/protobuf-specs |
| **Source** | https://raw.githubusercontent.com/sigstore/protobuf-specs/0342fe5797edd558c58098033220fb27a2542a28/protos/sigstore_bundle.proto |
| **Digest** | `bf8d01cc4a52f8485f5eb795f499396f2e05cc4e0e45d131375b4c780b190792` |

## Overview

**A stub: not read in full.** The Sigstore bundle is a protobuf message (sigstore_bundle.proto in sigstore/protobuf-specs) for a single file that carries either a message signature or a DSSE envelope together with its verification material: a public key hint or X.509 certificates, transparency log entries and timestamp data. At protobuf-specs v0.5.2 the current media type is application/vnd.dev.sigstore.bundle.v0.3+json, and a DSSE envelope in a bundle must hold exactly one signature. Cited by tmodel RPT-0004 (tmodel#38): the bundle media type (v0.3) and the rule that a DSSE envelope in a bundle carries exactly one signature.

## Applicability

A stub. `bears_on` (DEC-001) comes from RPT-0004's source log and was not re-assessed here.

## Implementations

Not searched. The implementations RPT-0004 cites are listed in `record.yaml`: cosign v3.1.3; actions/attest v4.2.2; actions/attest-sbom v4.1.0.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this summary |

## Limits

Not read in full. sigstore_bundle.proto at v0.5.2 checked 2026-10-18 for version, media type and signature rules; the imported protos were not read.
