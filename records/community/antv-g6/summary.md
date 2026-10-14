---
schema: "library-summary/v1"
id: antv-g6
record: antv-g6
type: summary
updated: "2026-10-14"
---

# AntV G6

|  |  |
|---|---|
| **Type** | repo |
| **Maturity** | implementation |
| **Authors** | AntV contributors |
| **Published** | living repository and documentation; reviewed 2026-10-14 |
| **Identifier** | git: https://github.com/antvis/G6 |
| **Source** | https://github.com/antvis/G6 |
| **Digest** | Not recorded; repository evidence is pinned by commit. |

## Overview

AntV G6 5.1.1 is an MIT-licensed graph-visualization framework. Official documentation covers nodes, edges, combos, states, interactions, multiple layout families and configurable force inputs. RPT-0006 records G6 as an alternative SDK found during completeness review, not as part of the fixed main comparison.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | adjacent | General graph-visualization SDK. |
| Cryptography | none | No cryptographic mechanism. |
| This project | adjacent | Informs graphical objects, grouping, layout and weighting. |

Informs DEC-006, R-014, and R-018 without accepting a decision. Reviewed at commit `bdf6a55cd346afa5429e38083b380081734c6ff9`.

## Implementations

| Name | Kind | License | URL |
|---|---|---|---|
| AntV G6 | graph-visualization framework | MIT | https://g6.antv.antgroup.com/ |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |

## Limits

The report did not prototype G6. Framework capabilities do not establish a complete review workflow, accessibility outcome, or superiority to the fixed candidates.
