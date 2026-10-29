---
schema: "library-summary/v1"
id: kohnfelder-garg-1999-threats-to-our-products
record: kohnfelder-garg-1999-threats-to-our-products
type: summary
updated: "2026-10-22"
---

# The threats to our products

|  |  |
|---|---|
| **Type** | article (internal Microsoft article, 8 pages) |
| **Maturity** | `historical` — the origin of STRIDE |
| **Authors** | Loren Kohnfelder, Praerit Garg |
| **Published** | 1999-04-01 (date in the byline); released publicly by Microsoft on its SDL blog on 2009-08-27 |
| **Identifier** | copy hosted by Adam Shostack; Microsoft's 2009 attachment is archived by the Wayback Machine (see `record.yaml`) |
| **Source** | https://shostack.org/files/microsoft/The-Threats-To-Our-Products.docx |
| **Digest** | `7004b8bfdeb52683c75329be9d41b877466393d37b64641cee99d9d07c4cfea8` (identical to the archived Microsoft attachment) |

## Overview

The article that introduced **STRIDE**. It says the Microsoft Security Task Force
"has defined a security threat model that it recommends all Microsoft product
teams adopt", to be used at design time to identify the types of threat a product
is subject to. The original expansion is: **Spoofing of user identity, Tampering
with data, Repudiability, Information disclosure (privacy breach), Denial of
Service, Elevation of privilege** — "Repudiability" where later sources say
"Repudiation". It already notes that some attacks "have several steps" in which
"one minor break-in leads to another".

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | The primary source for STRIDE's origin and original definition. |
| Cryptography | none | Not about cryptography. |
| This project | adjacent | Grounds RPT-0002 §2's history of STRIDE in a source that can be read. |

Bears on **DEC-001** only through RPT-0002 §2.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this summary |

## Limits

- **Attribution conflict:** Shostack (2008) names the first 1999 Microsoft
  threat-modeling document as "Threats to our software" by Jason Garms, Praerit Garg
  and Michael Howard. This record follows the document Microsoft itself released in
  2009; the two may be different documents.
- **Venue:** Shostack (2014, 2019) says it appeared in an internal Microsoft journal
  ("Interface"); the document itself names no venue.
- The `.docx` is never committed; only its digest and locator are recorded.
