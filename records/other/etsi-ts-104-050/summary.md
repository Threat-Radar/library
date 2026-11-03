---
schema: "library-summary/v1"
id: etsi-ts-104-050
record: etsi-ts-104-050
type: summary
updated: "2026-11-02"
---

# ETSI TS 104 050 V1.1.1: AI Threat Ontology and definitions

|  |  |
|---|---|
| **Type** | spec (ETSI Technical Specification); **stub**: pinned, not extracted |
| **Publisher** | ETSI, TC Securing Artificial Intelligence (SAI) |
| **Version** | V1.1.1, 2025-03 (first published January 2022 as ETSI GR SAI 001) |
| **Source** | https://www.etsi.org/deliver/etsi_ts/104000_104099/104050/01.01.01_60/ts_104050v010101p.pdf |
| **Digest** | `7a49a0c77b9bf766d2b198f5adac420d364de10c23a7cf69b208d98ffb0485c4` |

## Overview

ETSI's definition of an AI threat. Its scope (clause 1) says it "defines what
an Artificial Intelligence (AI) threat is and defines how it can be
distinguished from any non-AI threat", and presents the model "in the form of
an ontology to give a view of the relationships between actors representing
threats, threat agents, assets and so forth". The ontology extends the threat
and threat-agent taxonomy of ETSI TS 102 165-1, and it "applies to AI both as a
threat agent and as an attack target" (clause 1, NOTE 1). The outline covers
the move from taxonomy to ontology (clause 4), a threat landscape with
adversarial goals, attack surface and a trust model (clause 5), and the core
SAI ontology relationships (clause 6).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | A standards body's model of AI threats and threat agents |
| Cryptography | `none` | |
| This project | `core` | Evidence for what tmodel's object model must represent for AI threats, including AI used as a tool by an attacker |

`bears_on: DEC-001`.

## Status

A stub for tmodel #189 (2026-11-02), added because the RPT-0009 Phase 4
review (finding F-08) found it missing. Its History table gives two
publications, "V1.1.1 January 2022 Publication as ETSI GR SAI 001" and
"V1.1.1 March 2025 Publication", and the Foreword says it "updates and extends
ETSI GR SAI 001". The library holds no GR SAI 001 record, so no `supersedes`
link is made. Only the scope, foreword, history and outline were read.

## Limits

- Not extracted. Its ontology has not been compared with tmodel's object
  model or with RPT-0009's gaps G1 to G10.
- It points to ETSI TR 104 221 (problem statement) and TR 104 222 (mitigation
  strategies) as essential to its scope. Neither is held.
