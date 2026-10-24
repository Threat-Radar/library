---
schema: "library-summary/v1"
id: oasis-stix-visualizer
record: oasis-stix-visualizer
type: summary
updated: "2026-10-14"
---

# OASIS STIX Visualizer

|  |  |
|---|---|
| **Type** | repo |
| **Maturity** | implementation |
| **Authors** | OASIS Open CTI contributors |
| **Published** | living repository and deployment; reviewed 2026-10-14 |
| **Identifier** | git: https://github.com/oasis-open/cti-stix-visualization |
| **Source** | https://github.com/oasis-open/cti-stix-visualization |
| **Digest** | Not recorded; repository evidence is pinned by commit. |

## Overview

The OASIS STIX Visualizer is a BSD-3-Clause browser application for loading STIX 2.x JSON and displaying objects and relationships as an interactive graph. It provides type visibility controls, selected and linked-object details, and timeline filtering. RPT-0006 uses it as security-graph prior art.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | Visualizes structured cyber-threat intelligence. |
| Cryptography | none | No cryptographic mechanism. |
| This project | adjacent | Informs security-object inspection, filtering and temporal focus. |

Informs DEC-006 and R-014 without accepting a decision. Reviewed at commit `ac8d5ba946422273a754b23b9054b3ee57c47454`.

## Implementations

| Name | Kind | License | URL |
|---|---|---|---|
| OASIS STIX Visualizer | browser application | BSD-3-Clause | https://oasis-open.github.io/cti-stix-visualization/ |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |

## Limits

The visualizer is not a general-purpose review-console SDK. Its input, legend, detail and timeline behavior does not establish editing, saved collaborative views, semantic importance or proposal verdicts.
