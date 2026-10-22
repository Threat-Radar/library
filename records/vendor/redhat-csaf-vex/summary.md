---
schema: "library-summary/v1"
id: redhat-csaf-vex
record: redhat-csaf-vex
type: summary
updated: "2026-10-18"
---

# Red Hat Product Security CSAF VEX files

|  |  |
|---|---|
| **Type** | dataset |
| **Maturity** | _unset_ |
| **Authors** |  |
| **Published** | 2026-10-15 |
| **Identifier** | https://security.access.redhat.com/data/csaf/v2/vex/2026/cve-2026-54873.json |
| **Source** | https://security.access.redhat.com/data/csaf/v2/vex/2026/cve-2026-54873.json |
| **Digest** | `85c1f06bb74f8ef2b5d77f2ae539c4475c7cca98f9b220aad4ec340e730701d2` |

## Overview

**A stub: not read in full.** Red Hat Product Security's directory of CSAF 2.0 VEX documents, one file per CVE in yearly folders, alongside an index, change and deletion lists and a daily archive, listed in Red Hat's CSAF provider metadata. The document examined gives a product tree of Red Hat product streams and packages, named by CPE and purl, with a status and remediations per product. Cited by tmodel RPT-0004 (tmodel#38): how Red Hat names products (CPE for product streams, purl for packages and images), its per-product status and remediation categories, and its single CWE per vulnerability.

## Applicability

A stub. `bears_on` (DEC-008, DEC-009) comes from RPT-0004's source log and was not re-assessed here.

## Implementations

Not searched.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this summary |

## Limits

Not read in full. Read one VEX document, the directory listing and the provider metadata, but did not read the archive or any other document, and compared the regenerated document with Phase 1's notes only for its counts.
