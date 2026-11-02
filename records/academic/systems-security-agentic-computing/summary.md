---
schema: "library-summary/v1"
id: systems-security-agentic-computing
record: systems-security-agentic-computing
type: summary
updated: "2026-11-02"
---

# Systems Security Foundations for Agentic Computing

|  |  |
|---|---|
| **Type** | paper (systematization of knowledge) |
| **Maturity** | _unset_ — preprint |
| **Authors** | Christodorescu, Fernandes, Hooda, Jha, Rehberger, Chaudhuri, Fu, Shams, Amir, Choi, Choudhary, Palumbo, Labunets, Pandya |
| **Published** | 2025-12-01 (arXiv v1); v2 2026-02-19 |
| **Identifier** | arXiv:2512.01295 |
| **Source** | https://arxiv.org/pdf/2512.01295v2 |
| **Digest** | `sha256:a6afdd4020ac8007ea062fe5c7e6aab1e5200d969a416999282c7a6a63d9d4df` |

## Overview

Argues that agent security needs the systems-security view of the whole system, not only a
more robust model (§1). It names four frictions when classic principles meet agents: a
**probabilistic** trusted computing base, **dynamic, task-specific** security policies, a
**fuzzy** security boundary (no layers between a prompt and a tool call), and instruction
following that is sometimes a feature rather than an attack (§2). Eleven real attacks
(Copilot, Devin, ChatGPT memory, Claude Code, Cursor, …) are mapped to the principles they
violate — least privilege, TCB tamper resistance, complete mediation, secure information
flow, human weak link (§3, Table 1). Open problems: separating instructions from data,
least-privilege access control and information-flow control (§5); separation alone "is
unlikely to fully solve the prompt injection problem" (§5.1).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Agent attack classes, principles and defenses |
| Cryptography | `none` | — |
| This project | `adjacent` | Attack-to-principle mapping is input to AI threat types in the object model (DEC-001) |

`bears_on: DEC-001`. It is the SAGAI'25 research-challenges document, so `part_of:
sagai-workshop` (tmodel #189, 2026-11-02). Version 1 (2025-12-01, 7 pages, by Christodorescu,
Fernandes, Hooda, Jha, Rehberger and Shams) opens: "The IEEE Secure Generative AI Agents 2025
workshop (SAGAI; co-located with the IEEE Symposium on Security and Privacy) set out to
explore how computer-security research and practice can help inform and advance agentic
computing security. This report captures those discussions and distills key lessons, open
research problems and recommendations". Four of its authors are four of the five SAGAI'25
organizers, and Rehberger spoke at the workshop. Version 2, pinned here, is the expanded SoK
with eight more authors, and drops that sentence, which is why an earlier search of v2 found
no mention of the workshop.

## Implementations

Surveyed by the paper itself (Table 2, §4) — e.g. CaMeL, FIDES, Progent, ceLLMate,
NeMo Guardrails. Not independently searched.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this document |

## Limits

- **Problems, not solutions.** Most mechanisms are open research; the authors doubt that
  provable defenses can be built on a probabilistic component at all (§2.1, §5.4).
- **Follow-up exists.** A shorter position paper by the same authors, *Agent Security is a
  Systems Problem* (arXiv 2605.18991), is record `agent-security-systems-problem` (a stub).
- **Two versions differ.** This summary reads v2. v1, the workshop report as first issued,
  is not pinned as its own record; its digest is in `record.yaml`'s header.
