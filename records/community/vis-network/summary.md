---
schema: "library-summary/v1"
id: vis-network
record: vis-network
type: summary
updated: "2026-10-14"
---

# vis-network

|  |  |
|---|---|
| **Type** | repo |
| **Maturity** | implementation |
| **Authors** | Vis.js contributors |
| **Published** | living repository; reviewed 2026-10-14 |
| **Identifier** | git: https://github.com/visjs/vis-network |
| **Source** | https://github.com/visjs/vis-network |
| **Digest** | Not recorded; repository evidence is pinned by commit. |

## Overview

vis-network is a Canvas network-visualization library dual-licensed under Apache-2.0 or MIT. Its node and physics documentation distinguishes node mass, value-based visual scaling, central gravity, repulsion and spring parameters. RPT-0006 uses it to clarify that layout physics and visual prominence are not semantic importance or risk.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | adjacent | General visualization prior art. |
| Cryptography | none | No cryptographic mechanism. |
| This project | adjacent | Informs weighting/gravity terminology. |

Informs DEC-006 and R-018 without accepting a decision. Reviewed at commit `c93000c5e308bfa0253930e16227bb7d17dbff85`.

## Implementations

| Name | Kind | License | URL |
|---|---|---|---|
| vis-network | browser network renderer | Apache-2.0 OR MIT | https://visjs.github.io/vis-network/ |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |

## Limits

Physics parameters are presentation mechanics. The record does not interpret mass, gravity, degree or node value as threat severity, confidence or business importance.
