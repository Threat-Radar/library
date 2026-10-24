---
schema: "library-summary/v1"
id: react-flow
record: react-flow
type: summary
updated: "2026-10-14"
---

# React Flow

|  |  |
|---|---|
| **Type** | repo |
| **Maturity** | implementation |
| **Authors** | xyflow contributors |
| **Published** | living repository; reviewed 2026-10-14 |
| **Identifier** | git: https://github.com/xyflow/xyflow |
| **Source** | https://github.com/xyflow/xyflow |
| **Digest** | Not recorded; repository evidence is pinned by commit. |

## Overview

React Flow is an MIT-licensed React library for node-based editors. RPT-0006 uses official accessibility, save/restore and subflow documentation as follow-up evidence for keyboard and screen-reader primitives, persisted editor state, and parent/child grouping.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | adjacent | General node-editor prior art. |
| Cryptography | none | No cryptographic mechanism. |
| This project | adjacent | Informs editing, grouping and accessibility evaluation. |

Informs DEC-006 and R-014 without accepting a decision. Reviewed at commit `3d35b57317576b0916c0bfeaaedd573aaacc2839`.

## Implementations

| Name | Kind | License | URL |
|---|---|---|---|
| React Flow | React node-editor library | MIT | https://reactflow.dev/ |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |

## Limits

Documented primitives and examples do not prove an accessible tmodel console, coordinated canonical views, or a proposal-review workflow. Pro examples are not treated as open-source core features.
