---
schema: "library-summary/v1"
id: graphology
record: graphology
type: summary
updated: "2026-10-14"
---

# Graphology

|  |  |
|---|---|
| **Type** | repo |
| **Maturity** | implementation |
| **Authors** | Guillaume Plique and contributors |
| **Published** | living repository; reviewed 2026-10-14 |
| **Identifier** | git: https://github.com/graphology/graphology |
| **Source** | https://github.com/graphology/graphology |
| **Digest** | Not recorded; repository evidence is pinned by commit. |

## Overview

Graphology is an MIT-licensed JavaScript and TypeScript graph data model supporting directed, undirected, mixed and multi-graphs. Its standard-library documentation covers subgraph operators, weighted metrics, centralities, layouts and paths. RPT-0006 uses this evidence for data/model and analysis behavior around Sigma, not as evidence of Sigma rendering capability.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | adjacent | General graph model and algorithms. |
| Cryptography | none | No cryptographic mechanism. |
| This project | core | Informs presentation separation, subgraphs, weighting and ranking. |

Informs DEC-006, R-014, and R-018 without accepting a decision. Reviewed at commit `65e278f0075de97bee3fce12d10e423752ed395a`.

## Implementations

| Name | Kind | License | URL |
|---|---|---|---|
| Graphology | graph model and algorithms | MIT | https://github.com/graphology/graphology |
| Sigma.js | renderer using Graphology | MIT | https://www.sigmajs.org/ |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |

## Limits

Graphology does not render graphs or provide a review console. Centrality and weighted metrics are not semantic risk or importance unless tmodel supplies a separate domain warrant.
