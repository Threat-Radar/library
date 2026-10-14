---
schema: "library-summary/v1"
id: shavit-2023-openai-governing-agentic
record: shavit-2023-openai-governing-agentic
type: summary
updated: "2026-10-13"
---

# Practices for Governing Agentic AI Systems

|  |  |
|---|---|
| **Type** | paper (white paper; 23 pp.) |
| **Maturity** | _unset — do not guess_ |
| **Authors** | Y. Shavit, S. Agarwal, M. Brundage, and 13 co-authors (OpenAI) |
| **Published** | December 2023, OpenAI |
| **Identifier** | OpenAI white paper |
| **Source** | https://cdn.openai.com/papers/practices-for-governing-agentic-ai-systems.pdf |
| **Digest** | `22b3a8607ed781a848b82b0bfe8e638b16cd027aac90a19b2aecf236063d0e7c` (matches `pdf-manifest.tsv`) |

## Overview

A white paper that **defines agentic AI systems** — systems that pursue complex goals with limited direct supervision — and the **parties** in their life-cycle (model developer, system deployer, user), arguing each needs agreed baseline responsibilities. Its main contribution is an initial set of **seven practices** for keeping agents safe and accountable: evaluating suitability for the task; **constraining the action space and requiring approval**; setting safe default behaviours; **legibility** of agent activity; **automatic monitoring**; **attributability** (tracing actions to an accountable party); and **interruptibility** and maintaining control — each with open questions. It closes with **indirect impacts** of widespread agent adoption: adoption races, labour displacement, shifting offense-defense balances, and correlated failures.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | adjacent | Adjacent: governance and safety practices more than attacks. |
| Cryptography | none | Not about cryptography. |
| This project | core | The seven practices are candidate mitigations, and attributability/legibility match tmodel's review and provenance requirements. |

Bears on **DEC-001** (mitigation types for agents) and **R-018** (human review and traceability).

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | none | — | Describes failure and misuse risks, not attacks |
| Existing AI threat models | adjacent | TM-074 | A responsibility and practice framework rather than a threat model |
| Weakness enumerations | adjacent | LLM06:2025, ASI02, ASI03, ASI08, ASI10 | Its practices address these catalog entries; the paper maps none |
| Attack → asset mapping | adjacent | C08, C11, C12 | Agent runtime, delegation/attribution, human approvers |

## Implementations

Practices, not software. Searched 2026-10-13.

| Name | Kind | License | URL |
|---|---|---|---|


## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this summary |

## Limits

- **Pre-dates most agent attacks** catalogued in 2024–2026; no concrete threat analysis.
- **Explicitly preliminary:** the authors give open questions, not settled recommendations.
- Reference expansion not done in this pass (see PR notes).
