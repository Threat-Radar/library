---
schema: "library-summary/v1"
id: mitre-atlas
record: mitre-atlas
type: summary
updated: "2026-11-02"
---

# MITRE ATLAS (Adversarial Threat Landscape for AI Systems)

|  |  |
|---|---|
| **Type** | dataset; **stub**: pinned, not extracted |
| **Publisher** | The MITRE Corporation |
| **Version** | 2026.09, data format 6.0.0 (collection `modified-date` 2026-09-15; tag `v2026.09`) |
| **Source** | https://github.com/mitre-atlas/atlas-data, `dist/v6/ATLAS-2026.09.yaml` at the tag |
| **Digest** | `935efa93e28294432d3e2f537eb94991ef8d1f8c58341cd360ea3321ddb66688` |
| **Licence** | Apache-2.0 (repository `LICENSE` at the tag) |

## Overview

ATT&CK's counterpart for attacks on AI systems: a matrix of tactics and
techniques, mitigations, and case studies of real attacks and exercises, each
case study coded step by step to techniques. The pinned file holds 16 tactics,
208 techniques (88 of them sub-techniques), 40 mitigations, 73 case studies and
322 relationships (counted from the YAML on 2026-11-02).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | The technique catalog for AI attacks |
| Cryptography | `none` | |
| This project | `core` | Technique ids in RPT-0009 and RPT-0014; case study AML.CS0059 is the source of RPT-0009's EchoLeak model |

`bears_on: DEC-008`: like ATT&CK ids, ATLAS ids are catalog references that need
a version pin and, per RPT-0009 §5 item 3, a level (parent technique or
sub-technique) and a fit grade (RPT-0009 G4).

## Status

A stub for tmodel #189 (2026-11-02), shared with RPT-0014 (tmodel #71). The
digest matches the one RPT-0009's source log recorded. Not extracted.

## Limits

- Case studies are ordered steps (`step-id`, tactic, `leads-to`), an exception
  to RPT-0005 G2 (RPT-0009 G2); that structure is not described here.
- ATLAS covers well under half of RPT-0014's incident log (69 of 179 incidents
  carry a case-study id; RPT-0014 `incidents.md` P1).
