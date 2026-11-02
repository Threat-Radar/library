---
schema: "library-summary/v1"
id: agent-security-systems-problem
record: agent-security-systems-problem
type: summary
updated: "2026-11-02"
---

# Agent Security is a Systems Problem

|  |  |
|---|---|
| **Type** | paper (arXiv preprint); **stub**: pinned, not summarized here |
| **Authors** | Christodorescu, Fernandes, Hooda, Jha, Rehberger, Chaudhuri, Fu, Shams, Amir, Choi, Choudhary, Palumbo, Labunets, Pandya |
| **Published** | arXiv 2605.18991, v1 2026-05-18, v2 2026-05-20 (pinned) |
| **Source** | https://arxiv.org/pdf/2605.18991v2 |
| **Digest** | `eb02d189389663de9e0b4a315ca9f33b07fa1b2e32b23972ea245273134bbadf` |

## Overview

A short position paper by the authors of `systems-security-agentic-computing`,
building on it. Per RPT-0009 §2.6: treat the model that powers an agent as an
untrusted component and enforce security invariants at the system level,
through provable separation of instructions and data, least-privilege
sandboxing with verifiable policy generation, and information-flow control. It
argues that stacking ML guard models is not real defense in depth, because they
share failure modes.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | System-level defenses against prompt injection in agents |
| Cryptography | `none` | |
| This project | `adjacent` | Bears on tmodel's own AI features (RPT-0009 §7) and on modeling defenses |

`bears_on: DEC-001`.

## Status

A stub for tmodel #189 (2026-11-02). RPT-0009 §2.6 reads it. The author list
matches v2 of `systems-security-agentic-computing`, which is the SAGAI'25
report. This paper names no workshop in either version (v1 or v2), so the link
to `sagai-workshop` is `see_also`, not `part_of`.

## Limits

- Only RPT-0009 §2.6's reading is recorded; the paper was not re-read for this
  stub.
