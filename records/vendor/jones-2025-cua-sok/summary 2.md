---
schema: "library-summary/v1"
id: jones-2025-cua-sok
record: jones-2025-cua-sok
type: summary
updated: "2026-10-13"
---

# A Systematization of Security Vulnerabilities in Computer Use Agents

|  |  |
|---|---|
| **Type** | paper (systematization / threat analysis; 18 pp.) |
| **Maturity** | _unset — do not guess_ |
| **Authors** | D. Jones, G. Severi, M. Pouliot, G. Lopez, J. de Gruyter, S. Zanella-Beguelin, J. Song, B. Bullwinkel, P. Cortez, A. Minnich (Microsoft) |
| **Published** | arXiv v1, 2025-07-07 (no venue stated) |
| **Identifier** | arXiv:2507.05445 |
| **Source** | https://arxiv.org/pdf/2507.05445 |
| **Digest** | `45f4f3ceb7e19b7dacfb8b951abf0a1519006ecd32386c094ee916235079a956` (matches `pdf-manifest.tsv`) |

## Overview

A systematic threat analysis of **computer-use agents (CUAs)** — agents that operate browsers and operating systems through screenshots, the DOM and system commands. From adversarial testing of real-world CUAs it names **seven risk classes**: UI deception and perceptual mismatch; remote code execution via action composition; chain-of-thought exposure; bypassing human-in-the-loop safeguards; indirect prompt injection; identity ambiguity and over-delegation; and content harms. Three exploits are worked in depth (clickjacking with visual overlays, indirect injection chained to RCE, and CoT-exposure hijacking). The root causes it identifies are architectural: **no input provenance tracking, weak binding between interface and action, and too little control over agent memory and delegation**. It ends with a CUA security evaluation framework and design principles (structured red teaming, provenance-aware audit, memory/intent isolation).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | Covers a fast-growing agent type with tested exploits. |
| Cryptography | none | Not about cryptography. |
| This project | core | Its root causes (provenance, interface-action binding, delegation) map onto tmodel's components, trust boundaries and review model. |

Bears on **DEC-001** (object model — agent perception/action loop, trust boundaries, provenance).

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | core | AIT-104, AIT-093, AIT-064 | Browser/computer-use hijacking; human-approval bypass; indirect injection to RCE |
| Existing AI threat models | core | TM-078 | A CUA-specific threat analysis with a perception → reasoning → action decomposition |
| Weakness enumerations | adjacent | AML.T0051.001, AML.T0100, LLM01:2025, LLM06:2025, ASI01, ASI05, ASI09 | Catalog entries for its risks; the paper maps none |
| Attack → asset mapping | core | C08, C09, C11, C12, C20 | Agent runtime and tools, delegated identity, human approvers, AI browsers |

## Implementations

Describes an evaluation framework; no tool released as far as the PDF states. Searched 2026-10-13.

| Name | Kind | License | URL |
|---|---|---|---|


## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this summary |

## Limits

- **Vendor research, preprint.** Systems tested are not all named; results are case studies rather than measured rates.
- **Mitigations are principles,** not evaluated defenses.
- Reference expansion not done in this pass (see PR notes).
