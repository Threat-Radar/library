---
schema: "library-summary/v1"
id: iso-iec-15408
record: iso-iec-15408
type: summary
updated: "2026-10-25"
---

# ISO/IEC 15408:2022 / CC:2022 — Common Criteria for IT security evaluation

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | _unset — do not guess_ |
| **Authors** | ISO/IEC JTC 1/SC 27; CCRA Common Criteria Maintenance Board |
| **Published** | ISO/IEC 15408-1..5:2022 (August 2022); CC:2022 Release 1 (November 2022) |
| **Identifier** | ISO/IEC 15408:2022 · CC:2022 R1 (Part 1: CCMB-2022-11-001) |
| **Source** | https://www.commoncriteriaportal.org/files/ccfiles/CC2022PART1R1.pdf |
| **Digest** | `62cccce618919ea3458fa4bf701cbff5ecf908a6f89f43f9c87cfbf2563452f2` (Part 1, CCRA PDF) |

**Which text was read.** The ISO edition is licensed and was not obtained. The CCRA text is free. The CC:2022 Part 1 foreword says CC:2022 was developed first as ISO/IEC 15408:2022 and then published by the CCRA, and the CCMB errata v1.2 states the core parts do not differ in content or technical wording. Only **Part 1** (introduction and general model) was read for this summary. Parts 2–5 are named, not summarised. The text is paraphrased, and locators are clause numbers.

## Overview

The Common Criteria let IT products be evaluated against a stated security problem so that results are comparable. Part 1 defines the general model. A **security problem definition** (threats, organisational security policies, assumptions) is the axiomatic input; the CC does not say how to derive it (7.1.1). A **threat** is an adverse action by a **threat agent** on an **asset** (7.1.2; terms 3.x). Security objectives and functional/assurance requirements follow from it. **Attack potential** is defined as the effort needed to exploit a vulnerability, as a function of attacker and vulnerability properties (3.8). Its calculation lives in the methodology (`iso-iec-18045`, Annex B). CC:2022 has five parts: general model, functional components, assurance components, and two new ones — a framework for evaluation methods and activities (Part 4) and predefined packages (Part 5).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | International product-evaluation standard. |
| Cryptography | adjacent | Covers crypto modules through protection profiles, not directly. |
| This project | adjacent | Supplies the vocabulary for R-013, which ADR-0006 makes display-only. The scoring tmodel would show is in 18045. |

Bears on **DEC-003 / ADR-0006**, **R-011**, **R-013**.

**Implications for tmodel (inference).** CC's threat triple (agent, adverse action, asset) maps onto ThreatInstance + Party (threat-agent role) + the asset a DamageScenario damages. The SPD being "axiomatic" is the same stance ADR-0010 takes on human-supplied impact (R-019). The SPD is the input a human reviews and asserts, not something derived. The new Part 4 "evaluation methods/activities" is analogous to DEC-001b's `Gate`/`Requirement`, but this record does not establish any mapping.

## Implementations

Not searched.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata; ISO and CCRA identifiers |
| `summary.md` | this summary |

## Limits

- Only Part 1 was read. Parts 2–5 (SFR/SAR catalogs, evaluation-method framework, packages) were not.
- The ISO edition was not seen. Equivalence rests on the CCRA's own statements cited above.
- CC evaluates a product against a claimed problem. It does not produce attack paths or a risk number, so it cannot replace a TARA.
