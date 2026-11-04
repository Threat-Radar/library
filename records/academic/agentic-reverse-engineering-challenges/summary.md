---
schema: "library-summary/v1"
id: agentic-reverse-engineering-challenges
record: agentic-reverse-engineering-challenges
type: summary
updated: "2026-11-02"
---

# Challenges and Future Directions in Agentic Reverse Engineering Systems

|  |  |
|---|---|
| **Type** | paper (SAGAI 2026; arXiv preprint); **stub**: pinned, partly read |
| **Authors** | Radey, West, Fawaz (University of Wisconsin-Madison) |
| **Published** | arXiv 2604.14317v1, 2026-04-15; "accepted at SAGAI 2026" (arXiv comment) |
| **Source** | https://arxiv.org/pdf/2604.14317v1 |
| **Digest** | `0133f777a0e76a74c50150c8dcaac9d550cd2ee83e342a7c9a598426b3363f11` |

## Overview

A position paper on LLM agents that reverse-engineer binaries, with static,
dynamic and hybrid analysis. It names their limits: token constraints,
obfuscation, timeouts, reliance on emulation, and "a lack of program
guardrails" (abstract). On the security side, the existing systems it reviewed
"commonly allow models to execute any command the agent deems necessary", and
since agents can be tricked into running malicious code, the authors argue "it
may be possible to craft a binary that tricks a model into executing malicious
code" (§1). They propose research on such adversarial binaries and on
guardrails for dynamic analysis.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | Mostly about the capability of AI as a security tool; the security point is an agent's missing execution guardrails |
| Cryptography | `none` | |
| This project | `none` | Bears on no decision yet; relevant only to RPT-0009's open question on whether attacks that use AI as a tool are in scope |

Bears on no `DEC-*` or `R-*` yet. RPT-0009 attack classes it touches: not one
class. It is AI used as a tool, plus a conventional code-execution risk to the
agent's host when a crafted input (the binary) steers it.

## Status

A stub for tmodel #189 (2026-11-02), added because the RPT-0009 Phase 4
review (finding F-07) found the SAGAI'26 papers missing. The abstract and §1
were read.

## Limits

- The adversarial-binary attack is proposed, not shown.
- The survey of agentic reverse-engineering tools (§2 on) was not read.
