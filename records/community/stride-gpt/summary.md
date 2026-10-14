---
schema: "library-summary/v1"
id: stride-gpt
record: stride-gpt
type: summary
updated: "2026-10-13"
---

# STRIDE GPT

|  |  |
|---|---|
| **Type** | repo |
| **Maturity** | _unset — do not guess_ |
| **Authors** | Matthew Adams / STRIDE GPT contributors |
| **Published** | v0.20.0 released 2026-09-26; repository reviewed 2026-10-13 |
| **Identifier** | git: https://github.com/mrwadams/stride-gpt |
| **Source** | https://github.com/mrwadams/stride-gpt |
| **Digest** | `not fetched` |

## Overview

STRIDE GPT is an MIT-licensed application using language models to generate STRIDE threat models, attack trees, DREAD assessments and Gherkin test cases. RPT-0003 uses it only as an active-product coverage check.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | Generates threat-model artifacts. |
| Cryptography | none | Not a cryptographic specification. |
| This project | adjacent | Coverage evidence for automation and review choices. |

Reviewed at commit `4ae531247d698d07bb99400c24c1d13010d400f3`; the source log observed release v0.20.0 on 2026-09-26.

## Implementations

| Name | Kind | License | URL |
|---|---|---|---|
| STRIDE GPT | application | MIT | https://github.com/mrwadams/stride-gpt |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |

## Limits

The research did not acceptance-test generated output or treat model-generated claims as authoritative.
