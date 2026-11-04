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
208 techniques (88 of them sub-techniques), 40 mitigations, 73 case studies,
and 1,355 relationship items under 322 source objects (counted from the YAML on
2026-11-02; 0.3.1 of this stub wrongly called the 322 source objects
relationships).

**A newer release exists.** ATLAS v2026.10 (collection `modified-date`
2026-10-28, data format 6.1.0) came out before this record was pinned. This
record keeps 2026.09, the version RPT-0009's and RPT-0014's mappings use. The
changes that touch those mappings, checked against
`dist/v6/ATLAS-2026.10.yaml` (sha256
`ac41ee9f99a47084ba5fdfc77ae83a28687e12390240fffeb37df7914ffe142d`, the copy
the review downloaded from the v2026.10 tag; not pinned here):
- **Removed:** AML.T0024.000 (Infer Training Data Membership), .001 (Invert AI
  Model) and .002 (Extract AI Model), and AML.T0057 (LLM Data Leakage). The
  parent AML.T0024 (Exfiltration via AI Inference API) remains.
- **Renamed:** AML.T0010 "AI Supply Chain Compromise" becomes "Supply Chain
  Compromise", with .001 "AI Software" becoming "Software", .002 "Data" becoming
  "Data Repository" and .003 "Model" becoming "Model Repository". AML.M0026
  "Privileged AI Agent Permissions Configuration" becomes "Manage AI Agent
  Service Access", and AML.M0027 "Single-User AI Agent Permissions
  Configuration" becomes "Manage User-Delegated AI Agent Access".
- **AML.CS0059 (EchoLeak):** the 2026.09 field `actor: Aim Labs` is gone. 2026.10
  links the case study `attributed-to` the new entity AML.E0016, Cato Networks
  ("activity-purpose: Security Evaluation"), which the entity's description says
  acquired Aim Security in September 2025. The case study's own description
  still says "Aim Security researchers discovered EchoLeak".
- 2026.10 adds top-level `entities` (44) and `software` (37), and has 221
  techniques, 44 mitigations, 77 case studies and 1,750 relationship items.

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
