---
schema: "library-summary/v1"
id: cwe-4-21
record: cwe-4-21
type: summary
updated: "2026-11-22"
---

# MITRE CWE: Common Weakness Enumeration 4.21

|  |  |
|---|---|
| **Type** | dataset (best-practice) |
| **Publisher** | The MITRE Corporation (CWE Program) |
| **Version** | CWE List 4.21, catalog dated 2026-10-28; XML schema 7.4 (October 27, 2026), namespace `http://cwe.mitre.org/cwe-7` |
| **Source** | https://cwe.mitre.org/data/xml/cwec_v4.21.xml.zip, SHA-256 `5225e2b4…7e718862`; unzipped `cwec_v4.21.xml`, 18,571,978 bytes, SHA-256 `3bd5b7f8…2756bdeb` |
| **Schema** | https://cwe.mitre.org/data/xsd/cwe_schema_v7.4.xsd, SHA-256 `8ce16831…f5aa384e` |
| **Licence** | CWE terms of use (https://cwe.mitre.org/about/termsofuse.html); a copy of CWE content keeps MITRE's copyright designation and licence |
| **Supersedes** | `cwe` (CWE 4.20, schema 7.3, fully extracted) |

## Overview

CWE 4.21 is MITRE's October 2026 catalog of software and hardware weakness
types, in the same XML format as 4.20 (schema 7.x). MITRE released it beside
CWE 5.0, which moves to schema 8.0 (namespace `http://cwe.mitre.org/cwe-8`,
Categories become Groupings). The two carry the same 984 weaknesses, with
identical IDs and names, so 4.21 is the newest list a schema 7.x reader can
take. It is not a clean 7.x file: it carries some of 5.0's new content in
places schema 7.4 does not allow (see below).

## Changes from 4.20

| | 4.20 | 4.21 |
|---|---|---|
| Weaknesses | 969 | 984 (28 deprecated) |
| Categories | 422 | 431 |
| Views | 59 | 62 |
| External references | 1,026 | 1,081 |

Nothing was removed: every 4.20 ID is still in 4.21.

**15 new weaknesses**, all with status Incomplete:

| ID | Name |
|---|---|
| CWE-1461 | Hardware Simulation / Synthesis Mismatch |
| CWE-1462 | Improper Session Management |
| CWE-1463 | Insufficient Session Timeout Value |
| CWE-1464 | Improper Session Invalidation |
| CWE-1465 | Improper Session Invalidation after User Logout |
| CWE-1466 | Improper Session Invalidation after Authentication Credential Change |
| CWE-1467 | Use of Singular Authentication Artifact for Multiple User Sessions |
| CWE-1469 | Improper Check for Credential Expiration |
| CWE-1470 | Improper External Identity Verification |
| CWE-1471 | Insufficiently Controlled Parser Differential |
| CWE-1472 | Generation of Credential with Long Expiration |
| CWE-1473 | Improper Expiration of Cached Data |
| CWE-1474 | Non-Equivalent Data Transformation |
| CWE-1475 | Incomplete Data/State Propagation |
| CWE-1476 | Improper Request Propagation before Data Reception in Write Transactions in a Bus Architecture |

**3 weaknesses deprecated**, now with mapping usage `Prohibited`: CWE-377
(Insecure Temporary File), CWE-391 (Unchecked Error Condition) and CWE-613
(Insufficient Session Expiration). For CWE-613, MITRE points to CWE-1462 and
its descendants instead.

**9 new categories** (CWE-1451 to CWE-1459) for the OpenSSF Secure Coding
Guide for Python (2026), and **3 new views**: CWE-1449 (that guide), CWE-1460
(Top 20 Secure PLC Coding Practices) and CWE-1468 (OWASP Golang Secure Coding
Practices Guide).

## Schema 7.4, and where 4.21 departs from it

Schema 7.4 declares the same elements and attributes as 7.3, less one:
`Demonstrative_Example` no longer has a `References` child. It also makes the
three children of `Content_History/Modification` required and rewords some
documentation.

**The 4.21 file does not validate against schema 7.4.** Checked with xmllint
(libxml2 2.13.9) offline, using the W3C catalog recipe in
`../cwe/distilled/schema/README.md`; the 4.20 file still validates against
7.3 the same way. Every one of the 81 errors is content schema 8.0 adds:

| Departure from 7.4 | Errors | In schema 8.0 |
|---|---|---|
| `Taxonomy_Mapping/@Taxonomy_Name` values `OWASP Golang Secure Coding Practices Guide` and `PLC Top 20` | 47 | enumeration values |
| `External_Reference` children `Rationale`, `Alt_URL`, `Media_Type` and `Access_Restrictions`, plus `Alt_URL_Date` (xmllint reports only the first unexpected child of each reference) | 19 | declared fields |
| `Phase` text such as `(Custom AI) Training` and `(Custom Hardware) Hardware Architecture` | 10 | a new `Custom_Phase` element, domain `AI` or `Hardware` |
| `Related_Weakness/@Nature` value `Overlaps` | 3 | enumeration value |
| `Impact` value `DoS: Prevent Access` | 2 | enumeration value |

## Applicability

- **Security: core.** The same vocabulary as `cwe`; CVE records and NVD cite
  CWE IDs.
- **Cryptography: adjacent.** Covers cryptographic weaknesses as entries; not
  a cryptographic specification.
- **This project: core.** The CWE release tmodel's engine serves and its app
  ships, pinned by this record's digest (DEC-008; tmodel ADR-0014, a cached
  pinned mirror). It keys tmodel's Weakness type (ARCH-0001 §3, R-010). Its
  departures bear on DEC-002 (import formats): a reader that rejects files
  failing their declared schema would reject this release.

## Implementations

Not searched for this release (2026-11-22). Consumers already held in this
library: CVE Record Format 5.x (`cve-json-5`) and Open Threat Model
(`open-threat-model`). tmodel's importer (`engine/engine/load/cwe.py`) reads
the whole file without loss: 984 weaknesses, 431 categories and 62 views.

## Artifacts in this record

- `record.yaml`: metadata, digests and relations (`supersedes: cwe`).
- `summary.md`: this page.

There is no `distilled/`. The schema 7.x extraction lives in `cwe` and still
describes this file's structure, apart from the departures above.

## Limits

- Summary bar, not FX-1: the full extraction stays with `cwe` (4.20, schema
  7.3). Extracting the CWE line again, for schema 8.0 and CWE 5.0, belongs to
  tmodel #61.
- The record pins the XML distribution only. CSV and HTML views, and MITRE's
  web pages, were not examined.
- 4.21 and 5.0 were compared on weakness IDs and names only. Categories
  (Groupings in 5.0), views and relationships were not compared.
- Deprecated entries stay in the file, so links made before 4.21 can point at
  a retired entry. The `owasp-asvs-5` record links 8 requirements to CWE-613,
  as inferred legacy mappings (OWASP dropped CWE mappings in ASVS 5.0). Those
  links are left as they are; whether to remap them is that record's call.
- Added so tmodel can move its CWE pin to 4.21 (tmodel #61, question 3).
