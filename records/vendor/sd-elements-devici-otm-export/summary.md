---
schema: "library-summary/v1"
id: sd-elements-devici-otm-export
record: sd-elements-devici-otm-export
type: summary
updated: "2026-10-13"
---

# SD Elements — Exporting an OTM from Devici

|  |  |
|---|---|
| **Type** | web |
| **Maturity** | _unset — do not guess_ |
| **Authors** | Security Compass |
| **Published** | living documentation; retrieved 2026-10-11 |
| **Identifier** | https://docs.sdelements.com/master/guide/docs/import_from_devici/exporting_otm_from_devici.html |
| **Source** | https://docs.sdelements.com/master/guide/docs/import_from_devici/exporting_otm_from_devici.html |
| **Digest** | `not fetched` |

## Overview

First-party instructions for exporting OTM 0.2.0 from Devici through the canvas or REST API. The export carries elements, data flows, attributes, threats, mitigations, trust boundaries, layout and methodology metadata.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | Concrete threat-model interchange evidence. |
| Cryptography | none | Not cryptographic guidance. |
| This project | core | Informs DEC-001, DEC-002 and DEC-003. |

Bears on DEC-001, DEC-002, DEC-003 and R-014.

## Implementations

| Name | Kind | License | URL |
|---|---|---|---|
| Devici / SD Elements | commercial integration | commercial | https://www.securitycompass.com/devici/ |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |

## Limits

Documentation establishes exported fields, not lossless import by every OTM consumer; no round-trip test was performed.
