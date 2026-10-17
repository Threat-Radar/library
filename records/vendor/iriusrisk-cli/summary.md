---
schema: "library-summary/v1"
id: iriusrisk-cli
record: iriusrisk-cli
type: summary
updated: "2026-10-13"
---

# IriusRisk CLI

|  |  |
|---|---|
| **Type** | repo |
| **Maturity** | _unset — do not guess_ |
| **Authors** | IriusRisk |
| **Published** | repository reviewed 2026-10-13 |
| **Identifier** | git: https://github.com/iriusrisk/iriusrisk-cli |
| **Source** | https://github.com/iriusrisk/iriusrisk-cli |
| **Digest** | `not fetched` |

## Overview

First-party command-line tooling for IriusRisk and Open Threat Model. Its documentation covers OTM import, export and schema validation, making it implementation evidence for OTM portability rather than a separate interchange specification.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | Operates on structured threat models. |
| Cryptography | none | Does not specify cryptography. |
| This project | core | Informs DEC-001, DEC-002 and automation requirements. |

Reviewed at commit `a7d5aafcbb887bb180dbd5f3ee89c315218e3232`.

## Implementations

| Name | Kind | License | URL |
|---|---|---|---|
| IriusRisk CLI | CLI | MIT | https://github.com/iriusrisk/iriusrisk-cli |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |

## Limits

Tool documentation does not prove lossless interchange with every OTM consumer; no round-trip acceptance test was performed.
