---
schema: "library-summary/v1"
id: owasp-agentic-threats-mitigations-v1-1
record: owasp-agentic-threats-mitigations-v1-1
type: summary
updated: "2026-10-13"
---

# Agentic AI - Threats and Mitigations

|  |  |
|---|---|
| **Type** | paper (OWASP guide; 53 pp.; CC BY-SA 4.0) |
| **Maturity** | _unset — do not guess_ |
| **Authors** | OWASP GenAI Security Project — Agentic Security Initiative (ASI) |
| **Published** | Version 1.1, December 2025 (v1.0 February 2025) |
| **Identifier** | OWASP ASI, Agentic AI - Threats and Mitigations v1.1 |
| **Source** | https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/ |
| **Digest** | `65e3bd59f99c411b055c6caf2bac96ab361dff8c010e4bef532a593ce10345ff` (v1.1 PDF obtained through OWASP's download form; matches `pdf-manifest.tsv`) |

## Overview

The first guide of the OWASP **Agentic Security Initiative**: a **threat-model-based reference** for agentic AI. It defines agentic terms and capabilities, gives a **reference architecture** (single-agent and multi-agent, with the deployable components to threat-model), and a **reference threat model** of **17 agentic threats**: T1 memory poisoning, T2 tool misuse, T3 privilege compromise, T4 resource overload, T5 cascading hallucination attacks, T6 intent breaking and goal manipulation, T7 misaligned and deceptive behaviours, T8 repudiation and untraceability, T9 identity spoofing and impersonation, T10 overwhelming human-in-the-loop, T11 unexpected remote code execution, T12 agent communication poisoning, T13 rogue agents in multi-agent systems, T14 human attacks on multi-agent systems, T15 human manipulation, T16 insecure inter-agent protocol abuse (e.g. MCP, A2A), T17 supply-chain compromise. A **taxonomy navigator** helps locate threats; **six mitigation playbooks** cover reasoning manipulation, memory poisoning, tool execution, identity and privilege, human-in-the-loop fatigue, and multi-agent trust; **example threat models** apply it to scenarios such as enterprise copilots and smart-home IoT camera agents. It positions itself next to STRIDE/PASTA (which need mapping to AI) and MAESTRO.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | A primary industry catalog of agentic threats with mitigations. |
| Cryptography | none | Not about cryptography. |
| This project | core | Its T1-T17 and playbooks feed tmodel's agentic attack classes, mitigations and worked example threat models. |

Bears on **DEC-001** (object model — agentic threat classes, components and mitigations).

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | adjacent | AIT-102, AIT-091, AIT-101, AIT-111, AIT-093, AIT-140, AIT-106, AIT-099, AIT-139 | Names threat classes (memory poisoning, tool misuse, privilege, overload, HITL overwhelm, inter-agent and protocol abuse, repudiation) with examples, not new attacks |
| Existing AI threat models | core | TM-059 | Is an agentic threat model with a reference architecture and example models |
| Weakness enumerations | core | T1-T17; ASI01-ASI10 (catalog crosswalk) | Its own threat ids; the later OWASP agentic Top 10 (ASI) builds on it |
| Attack → asset mapping | core | C06, C08, C09, C10, C11, C12 | Reference architecture: agent runtime, tools, memory, identity, human-in-the-loop |

## Implementations

OWASP notes intentionally vulnerable agentic samples in its GitHub repository (not assessed here). Searched 2026-10-13.

| Name | Kind | License | URL |
|---|---|---|---|


## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this summary |

## Limits

- **Threat catalog, not measurement:** threats are described with examples, not evidence of frequency.
- **Some threats overlap** (e.g. T6/T7, T12/T16); ids are OWASP-specific and need crosswalking.
- **v1.1 read;** v1.0 (Feb 2025) differs — cite the version.
- Reference expansion not done in this pass (see PR notes).
