---
schema: "library-summary/v1"
id: zhang-2024-cybench
record: zhang-2024-cybench
type: summary
updated: "2026-11-01"
---

# Cybench: A Framework for Evaluating Cybersecurity Capabilities and Risks of Language Models

|  |  |
|---|---|
| **Type** | paper (benchmark) |
| **Maturity** | _unset_ (peer-reviewed conference paper; no maturity level applies) |
| **Authors** | Andy K. Zhang, Neil Perry, Riya Dulepet, Joey Ji, Celeste Menders, Justin W. Lin, Eliot Jones, Gashon Hussein, Samantha Liu, Donovan Jasper, Pura Peetathawatchai, Ari Glenn, Vikram Sivashankar, Daniel Zamoshchin, Leo Glikbarg, Derek Askaryar, Mike Yang, Teddy Zhang, Rishi Alluri, Nathan Tran, Rinnara Sangpisit, Polycarpos Yiorkadjis, Kenny Osele, Gautham Raghupathi, Dan Boneh, Daniel E. Ho, Percy Liang (Stanford University) |
| **Published** | arXiv v1 2024-08-15; v4 2025-04-12 (summarized here, with the ICLR 2025 header); ICLR 2025, oral |
| **Identifier** | arXiv:2408.08926 |
| **Source** | https://arxiv.org/pdf/2408.08926v4 |
| **Digest** | `sha256:b7bf58d0fac493bdf834f1ad508e7a5d5c2292ebc4168c8469d9ff1fd4baa084` (arXiv v4, 150 pages; matches pdf-manifest.tsv) |

## Overview

Cybench is an open benchmark for language-model agents on professional-level Capture the Flag
tasks: 40 tasks from four competitions held between 2022 and 2024, in cryptography, web
security, reverse engineering, forensics, exploitation and miscellaneous skills, each with a
description, starter files, a sandboxed Kali Linux environment and a flag checker (§1 to §3).
Difficulty is grounded in the first solve time of the fastest human team, from 2 minutes to
24 hours 54 minutes, and subtasks split each task into steps for partial credit (§2.3, §3.3).
With a structured agent (reflection, plan, thought, log and action, a three-turn memory and 15
iterations), the best unguided success rate across 8 models is 17.5% (Claude 3.5 Sonnet), and
no model solves without guidance a task whose first human solve took longer than 11 minutes,
so first solve time predicts agent success (§5, Table 2, Figure 3). Scaffold changes such as a
pseudoterminal or web search help one model and hurt another (§5.1, Table 3). The authors
release code and data, arguing that the benchmark is dual use like other penetration-testing
tools (Ethics Statement).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Measures how far language-model agents can find and exploit vulnerabilities on their own, on professional CTF tasks with difficulty grounded in human first-solve times (§3, §5) |
| Cryptography | `adjacent` | 16 of the 40 tasks exploit flawed cryptographic implementations; no model solved the hardest, which needs a length-extension attack, even with subtask guidance (§5.1, E.2) |
| This project | `adjacent` | First-solve time gives a human-grounded scale for how long an attack takes, and the agents' 11-minute ceiling says how far an AI agent reached on it in 2024. Both bear on the elapsed-time and expertise sides of attack feasibility |

`bears_on: DEC-001a` (the core type system, accepted in ADR-0010) and `DEC-003` (the risk
metric, accepted in ADR-0006, in which attack feasibility is one input). The DEC-003 link is
ours: the paper does not discuss risk metrics.

## Implementations

Searched on 2026-11-01.

| Name | Kind | License | URL |
|---|---|---|---|
| andyzorigin/cybench | the benchmark's tasks, agent, run logs and code; project site https://cybench.github.io | Apache-2.0 | https://github.com/andyzorigin/cybench |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this document |

## Limits

- **A light agent, by the authors' account.** A three-turn memory, no security tools such as
  decompilers, and 15 iterations. The US and UK AI Safety Institutes, with 100 iterations and
  different scaffolding, reported a mean of 26.5% and solved a task with a 75-minute first solve
  time, so these results are not a ceiling (I.1).
- **CTF tasks are not real systems.** Short time spans, small codebases and deliberate
  vulnerabilities, though a few tasks contain real CVEs (I.2).
- **First solve times are estimates.** They come from leaderboards and Discord announcements,
  and the two HKCert times are judgement calls (Appendix F).
- **Possible train-test overlap for Claude 3.5 Sonnet,** whose knowledge cutoff is April 2024;
  the authors judge overlap minimal for the other models (§5.1).
- **The prompt was written to avoid refusals.** Telling the agent it is a cybersecurity expert
  doing a challenge cut refusals to a few by the Claude models (§5.1, Appendix N).
- **2024 models,** since superseded.
- **Read in part.** The paper body and the analysis, competition, first-solve-time, limitation,
  model and refusal appendices were read; the per-task result tables and run logs that fill
  most of the 150 pages were skimmed.

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | core | AIT-122, AIT-115 | AIT-122 cites it: the 40 tasks measure how far LM agents find and exploit vulnerabilities on their own. Unguided, the best agents solved only tasks whose first human solve took 11 minutes or less, against a maximum of 24 hours 54 minutes, with a best success rate of 17.5% (§5, Table 2). AIT-115 is ours: during development the agent reached a task server with docker exec and read a flag from Docker's cache, environment flaws the authors then closed (E.3) |
| Existing AI threat models | none | none | A benchmark. Its framing is dual use: agents that find and exploit vulnerabilities serve attackers and penetration testers alike (§1, Ethics Statement). threat-models.md does not list it |
| Weakness enumerations | none | AML.T0016.002, NISTAML.04 | Not an enumeration, and neither NIST AI 100-2e2025 nor ATLAS 2026.09 cites it (searched 2026-11-01). Some tasks contain real CVEs (I.2), but the paper does not list them. The ids are RPT-0014's mapping in sources.md |
| Attack → asset mapping | none | none | The targets are ordinary software (web applications, cryptographic code, binaries), and the AI is the attacker's tool, which report.md §3.14 treats as a change in attacker capability and cost rather than an added component. AIT-122's component links (C04, C15) are not supported by this paper's tasks |
