---
schema: "library-summary/v1"
id: etsi-tr-104-048
record: etsi-tr-104-048
type: summary
updated: "2026-11-02"
---

# ETSI TR 104 048 V1.1.1: Data Supply Chain Security

|  |  |
|---|---|
| **Type** | spec (ETSI Technical Report, informative); **stub**: pinned, not extracted |
| **Publisher** | ETSI, TC Securing Artificial Intelligence (SAI) |
| **Version** | V1.1.1, 2025-01 |
| **Source** | https://www.etsi.org/deliver/etsi_tr/104000_104099/104048/01.01.01_60/tr_104048v010101p.pdf |
| **Digest** | `a91b1fed1edb296c95dcb2e1a2464ae4761eb9bdfaac41b55708051af76ad40a` |

## Overview

ETSI's technical report on data supply chain security for AI. Its scope
(clause 1) "addresses the security problems arising from data supply chains in
in [sic] the development of Artificial Intelligence (AI) and Machine Learning
(ML) systems", noting that "Compromising the integrity of data has been
demonstrated to be a viable attack vector". It summarizes how training data is
sourced, reviews data-sharing initiatives, and gives a gap analysis to scope
possible standards requirements. Clause 4 covers why data integrity matters:
consequences, methods of compromise, case studies. It names the poisoning of
training data as "the most likely outcome" of such an attack. It "relates
primarily to the security of data, rather than the security of models
themselves" (clause 1).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Data supply chain attacks on AI, including poisoning |
| Cryptography | `none` | |
| This project | `adjacent` | Supply chain is one of RPT-0009's attack classes (Table 2: 8 ETSI and 6 CISA entries) |

`bears_on: R-018`.

## Status

A stub for tmodel #189 (2026-11-02). Named by CISA's AI-in-OT guidance (§3.4)
as one of the top AI technical standards. Not extracted.

## Limits

- Only the scope and clause 4's outline and poisoning sentences were read (for
  the RPT-0009 Phase 4 review, F-25, 2026-11-02). Whether it gives the data
  supply chain a model tmodel could use (RPT-0009 G10, training data as Asset
  or Component) is unknown.
