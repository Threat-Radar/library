---
schema: "library-summary/v1"
id: owasp-threat-dragon
record: owasp-threat-dragon
type: summary
updated: "2026-10-13"
---

# OWASP Threat Dragon

|  |  |
|---|---|
| **Type** | repo |
| **Maturity** | established OWASP implementation |
| **Authors** | OWASP Threat Dragon project |
| **Published** | v2.6.2 released 2026-05-10; reviewed 2026-10-11 |
| **Identifier** | git: https://github.com/OWASP/threat-dragon |
| **Source** | https://github.com/OWASP/threat-dragon |
| **Digest** | `not fetched` |

## Overview

OWASP Threat Dragon is an Apache-2.0 threat-modeling application available in web, desktop, and self-hosted forms. Its repository documents diagram-based modeling, threat and mitigation editing, reports, and repository-backed model storage. RPT-0003 reviewed commit `1753ad0fae42d65c56e754fa8faf8fb57179f9f5`.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | Directly implements threat-model creation and review. |
| Cryptography | none | Cryptographic design is not the project’s subject. |
| This project | core | Evidence for DEC-001, DEC-002, DEC-003, DEC-006, and R-018. |

Its inspectable model and diagram workflow provide implementation evidence; its project-specific JSON also demonstrates a portability limitation.

## Implementations

| Name | Kind | License | URL |
|---|---|---|---|
| OWASP Threat Dragon | open-source application | Apache-2.0 | https://github.com/OWASP/threat-dragon |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |

## Limits

The repository evidence does not establish neutral cross-tool round trips or a complete lifecycle/approval model. Release history was checked for maturity evidence but does not receive a separate library record. No acceptance test was performed.
