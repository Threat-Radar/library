---
schema: "library-summary/v1"
id: nist-ai-100-2-e2025
record: nist-ai-100-2-e2025
type: summary
updated: "2026-11-02"
---

# NIST AI 100-2 E2025: Adversarial Machine Learning

|  |  |
|---|---|
| **Type** | spec (NIST Trustworthy and Responsible AI report); **stub**: pinned, not extracted |
| **Authors** | Apostol Vassilev, Alina Oprea, Alie Fordyce, Hyrum Anderson, Xander Davies, Maia Hamin |
| **Published** | March 2025 (NIST's page notes a corrected PDF uploaded 2025-04-01) |
| **Identifier** | doi:10.6028/NIST.AI.100-2e2025 |
| **Source** | https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-2e2025.pdf |
| **Digest** | `4811fb6ad73f9c9121843ab77e029b5adc6f2c86d33c2fc5b2099ef133847646` |

## Overview

NIST's taxonomy and terminology for adversarial machine learning. Per its
abstract, it arranges attacks by type of ML method, life-cycle stage, and the
attacker's goals, objectives, capabilities and knowledge, describes mitigations
for each, and adds a glossary, so that later standards share one vocabulary.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | A reference taxonomy of attacks on AI systems |
| Cryptography | `none` | |
| This project | `adjacent` | Supplies the attack classes and `NISTAML.*` ids in RPT-0009 Table 2 |

`bears_on: DEC-008`: RPT-0009 maps every ETSI EN 304 223 and CISA AI-in-OT
entry onto its classes, and those ids resolve to this record (RPT-0009 G12).

## Status

A stub for tmodel #189 (2026-11-02). The digest matches the one RPT-0009's
source log recorded. The class names and ids used in `etsi-en-304-223` and
`cisa-ai-in-ot-principles` were checked against its index by the session
recorded in RPT-0009 §10; the document itself is not extracted.

## Limits

- Not read critically here. Whether its classes fit tmodel's object model
  (a single class per attack, or several) is open (RPT-0009 G9).
- EN 304 223 cites the earlier E2023 edition ([i.17]), not this one; no record
  of E2023 is held.
- **Index erratum.** NIST's "Errata (Potential Updates)" list, last updated
  June 3, 2025
  (https://csrc.nist.gov/files/pubs/ai/100/2/e2025/final/docs/nist.ai.100-2e2025_potential_updates.pdf,
  sha256 `ac73cb5fe5e5c6dfaef566866d92ad5c9887176480f620112cc6a997d7d624d8`
  as downloaded 2026-11-02, not pinned here), corrects the taxonomy index on
  page x. Under Generative AI Attacks, Availability Violations (NISTAML.01), the
  index lists Data Poisoning (NISTAML.013), Indirect Prompt Injection
  (NISTAML.015) and Prompt Injection (NISTAML.018). These "should be replaced
  with" Manipulate Resources (NISTAML.016) and Time-Consuming Tasks
  (NISTAML.017). NIST says these "are not official changes to the document".
  No mapping in `etsi-en-304-223` or `cisa-ai-in-ot-principles` depends on the
  error: the one availability mapping (ETSI 5.2.2-2) uses NISTAML.01 itself
  (checked 2026-11-02, RPT-0009 Phase 4 review, F-22).
