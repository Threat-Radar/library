---
schema: "library-summary/v1"
id: beurer-kellner-2025-design-patterns
record: beurer-kellner-2025-design-patterns
type: summary
updated: "2026-10-13"
---

# Design Patterns for Securing LLM Agents against Prompt Injections

|  |  |
|---|---|
| **Type** | paper (design patterns; 32 pp.) |
| **Maturity** | _unset — do not guess_ |
| **Authors** | L. Beurer-Kellner and 13 co-authors (Invariant Labs, IBM, EPFL, ETH Zurich, Swisscom, Google, Microsoft, Kyutai, and others) |
| **Published** | arXiv v3, 2025-06-27 (no venue stated) |
| **Identifier** | arXiv:2506.08837 |
| **Source** | https://arxiv.org/pdf/2506.08837 |
| **Digest** | `c202a240f8f03c93cfafd157f218ec790c9e503beeaf80e229fb5e1645ab7f9c` (matches `pdf-manifest.tsv`) |

## Overview

Proposes **design patterns that make LLM agents resistant to prompt injection by construction**, instead of relying on detection. The core idea: once an agent has read untrusted input, that input must not be able to trigger consequential actions. Six patterns, each limiting what the agent can do: **action-selector** (the LLM only picks from fixed actions), **plan-then-execute** (the plan is fixed before untrusted data is seen), **LLM map-reduce** (untrusted items processed in isolated sub-calls), **dual LLM** (a privileged LLM never sees untrusted text; a quarantined one does), **code-then-execute** (the LLM writes a program that is then run), and **context-minimization** (remove untrusted content from context before acting). It analyses the utility/security trade-off of each and applies them to **ten case studies**, from OS assistants to software-engineering agents.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | Principled defenses for the dominant agent attack. |
| Cryptography | none | Not about cryptography. |
| This project | core | Gives tmodel concrete, named mitigations to attach to prompt-injection attack paths. |

Bears on **DEC-001** (object model — mitigations attached to attack paths).

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | adjacent | AIT-064, AIT-091 | Defends against indirect injection and tool hijacking; no new attacks |
| Existing AI threat models | adjacent | TM-072 | A defense-pattern framework with an explicit threat model |
| Weakness enumerations | adjacent | LLM01:2025, LLM06:2025, ASI01, ASI02 | Mitigates these catalog entries; the paper maps none |
| Attack → asset mapping | core | C07, C08, C09 | Patterns restructure the app layer, agent runtime and tool calls |

## Implementations

Patterns, not a library; the case studies are design sketches. Searched 2026-10-13.

| Name | Kind | License | URL |
|---|---|---|---|


## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this summary |

## Limits

- **Utility cost.** The patterns deliberately stop agents from solving arbitrary tasks; general-purpose agents remain unprotected.
- **Preprint;** guarantees hold only if the pattern is implemented exactly.
- Reference expansion not done in this pass (see PR notes).
