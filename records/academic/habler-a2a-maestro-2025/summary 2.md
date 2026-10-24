---
schema: "library-summary/v1"
id: habler-a2a-maestro-2025
record: habler-a2a-maestro-2025
type: summary
updated: "2026-10-13"
---

# Building A Secure Agentic AI Application Leveraging Google's A2A Protocol

|  |  |
|---|---|
| **Type** | paper (threat model of a protocol; 13 pp.) |
| **Maturity** | _unset — do not guess_ |
| **Authors** | I. Habler, K. Huang, P. Kulkarni, V. S. Narajala (authors write in a personal capacity) |
| **Published** | arXiv v2, 2025-05-02 (no venue stated) |
| **Identifier** | arXiv:2504.16902 |
| **Source** | https://arxiv.org/pdf/2504.16902 |
| **Digest** | `477a283542cfe2b15c6b639fce1aca288489b7fc19870a7e6047e8330080e6cf` (not in `pdf-manifest.tsv`; computed on the arXiv copy) |

## Overview

A security analysis of **Google's Agent2Agent (A2A) protocol** for agent-to-agent communication. It explains A2A's elements (Agent Cards that advertise an agent's capabilities, tasks, messages, authentication) and applies the **MAESTRO** agentic-AI threat-modeling framework to A2A deployments. Threats identified include **Agent Card spoofing and tampering, task replay and injection, cross-agent privilege escalation, authentication weaknesses and prompt injection** between agents. Each is paired with mitigations — signed Agent Cards, mutual TLS, certificate pinning and DNSSEC, strict authentication and authorization on every call, replay protection, monitoring — and secure-development practices. It also discusses how A2A and the Model Context Protocol (MCP) complement each other.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | A threat model for multi-agent communication. |
| Cryptography | adjacent | Adjacent: relies on signatures, certificates and TLS for agent identity. |
| This project | core | An applied MAESTRO example — useful as a worked threat-model vector for agentic products. |

Bears on **DEC-001** (object model — agent identity, inter-agent trust boundaries).

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | adjacent | AIT-106, AIT-099 | Inter-agent injection and session issues; agent-protocol authorization flaws (described, not demonstrated) |
| Existing AI threat models | core | TM-080 | A MAESTRO-based threat model of A2A |
| Weakness enumerations | adjacent | ASI07, ASI03 | OWASP agentic entries for its threats; the paper maps none |
| Attack → asset mapping | core | C08, C09, C11 | Agents, A2A peers and tools, agent credentials and delegation |

## Implementations

Builds on Google's A2A protocol (specification and SDKs from Google; not assessed here). Searched 2026-10-13.

| Name | Kind | License | URL |
|---|---|---|---|


## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this summary |

## Limits

- **Analysis, not measurement.** Threats and mitigations are reasoned, not tested against deployments.
- **Early protocol version.** A2A has evolved since 2025; details may be out of date.
- **Not in the team PDF manifest;** digest computed on the arXiv copy.
- Reference expansion not done in this pass (see PR notes).
