---
schema: "library-summary/v1"
id: tcg-dice-attestation-architecture-1-2
record: tcg-dice-attestation-architecture-1-2
type: summary
updated: "2026-10-18"
---

# DICE Attestation Architecture

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | `standard` |
| **Authors** |  |
| **Published** | 2025-04-24 |
| **Identifier** | https://trustedcomputinggroup.org/wp-content/uploads/DICE-Attestation-Architecture-v1.2_pub.pdf |
| **Source** | https://trustedcomputinggroup.org/wp-content/uploads/DICE-Attestation-Architecture-v1.2_pub.pdf |
| **Digest** | `a930c341a65493e87d42207ac485da0b97fe0eb2c0ce0c7642316e7825759f2d` |

## Overview

**A stub: not read in full.** TCG specification that defines an attestation architecture for DICE layering and X.509 certificate extensions that carry attestation Evidence and Endorsements. Its DiceTcbInfo extension describes each layer's target environment (vendor, model, version, security version number, layer, index, firmware digests, operational flags and related fields), and other extensions cover multiple TcbInfo structures and device identity. TCG lists an errata, v1.0 r1 of January 29, 2026, for this version. Cited by tmodel RPT-0004 (tmodel#38): DiceTcbInfo measurement fields and DICE device identity in certificates (Table 4b; measured evidence as an Assertion by the device).

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

Not read in full. Checked the cover, page footers, scope, reference list and the DiceTcbInfo ASN.1 in the 1.2 PDF; the 2026-01-29 errata could not be fetched or read.
