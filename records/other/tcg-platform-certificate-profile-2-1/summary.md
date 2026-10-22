---
schema: "library-summary/v1"
id: tcg-platform-certificate-profile-2-1
record: tcg-platform-certificate-profile-2-1
type: summary
updated: "2026-10-18"
---

# TCG Platform Certificate Profile

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | _unset_ |
| **Authors** |  |
| **Published** | 2026-01-27 |
| **Identifier** | https://trustedcomputinggroup.org/wp-content/uploads/TCG_Platform_Certificate_Profile_2.1_Pub_v2.pdf |
| **Source** | https://trustedcomputinggroup.org/wp-content/uploads/TCG_Platform_Certificate_Profile_2.1_Pub_v2.pdf |
| **Digest** | `not fetched` |

## Overview

**A stub: not read in full.** TCG specification for Platform Certificates: RFC 5280 public-key certificates or RFC 5755 attribute certificates in which a platform manufacturer, or a later party such as an integrator or reseller, asserts that a platform contains given roots of trust (TPM, DICE and others), trusted building blocks and a list of components with attributes such as manufacturer, model, serial number and MAC addresses. Delta Platform Certificates record changes made after the platform leaves the factory, and component class registries say how component data was collected. Cited by tmodel RPT-0004 (tmodel#38): Platform Certificate component traits, origin and part-number traits and Delta certificates, read as a signed hardware bill (Table 4b; mapping rows on component kind, supply-chain origin and post-manufacture changes).

## Applicability

A stub. `bears_on` (DEC-001, DEC-002, DEC-009) comes from RPT-0004's source log and was not re-assessed here.

## Implementations

Not searched. The implementations RPT-0004 cites are listed in `record.yaml`: NSA PACCOR v2.0r16; NSA HIRS v3.2.0, implementing Platform Certificate profile 1.1 r15 with 2.0 in development, not 2.1.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this summary |

## Limits

Not read in full. Title, version, date and description come from TCG's resource page as archived on 2026-09-02; the PDF itself could not be fetched or read on 2026-10-18. No digest: Not digested: on 2026-10-18 trustedcomputinggroup.org answered every automated request (curl and WebFetch, PDFs and pages, even robots.txt) with HTTP 429 and a 'Vercel Security Checkpoint' JavaScript challenge; the Internet Archive holds no capture of any TCG_Platform_Certificate PDF; the Claude in Chrome extension was not connected. Phase 1 recorded SHA-256 077676d51348c973bf94ac0c8842c975be36f096b4b4854e8cf3efa4b81adaa7 (67 pages) from a direct download on 2026-10-08; not re-verified.
