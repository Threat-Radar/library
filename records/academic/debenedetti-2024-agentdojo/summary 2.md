---
schema: "library-summary/v1"
id: debenedetti-2024-agentdojo
record: debenedetti-2024-agentdojo
type: summary
updated: "2026-10-13"
---

# AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents

|  |  |
|---|---|
| **Type** | paper (benchmark; 26 pp.) |
| **Maturity** | _unset — do not guess_ |
| **Authors** | E. Debenedetti, J. Zhang, M. Balunovic, L. Beurer-Kellner, M. Fischer, F. Tramèr (ETH Zurich, Invariant Labs) |
| **Published** | NeurIPS 2024 Datasets and Benchmarks Track (stated in the PDF); arXiv v3 of 2024-11-24 read |
| **Identifier** | arXiv:2406.13352 |
| **Source** | https://arxiv.org/pdf/2406.13352 |
| **Digest** | `349884fffbf43282591c5accffd57bb651632f38e412fe303114941bdd111b05` (matches `pdf-manifest.tsv`) |

## Overview

An extensible evaluation environment for **prompt-injection attacks and defenses on LLM agents** that call tools over untrusted data. It ships 97 realistic user tasks (email client, e-banking, travel booking, workspace) and 629 security test cases, where injected instructions in tool results try to make the agent perform an attacker's goal. It measures **utility** (task solved without attack), **utility under attack**, and **targeted attack success rate**. Headline results: current models solve under 66% of tasks even without attacks; attacks succeed against the best agents in under 25% of cases; a secondary prompt-injection detector cuts attack success to 8%. Attacks gain little from knowing the system, and rarely succeed when the attacker's goal is unusually security-sensitive. The benchmark is meant to be live: new tasks, attacks and defenses can be added.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | Measures the most important agent attack class with reproducible numbers. |
| Cryptography | none | Not about cryptography. |
| This project | core | Gives tmodel concrete success rates and defense effects for agent attack paths, and a test structure for vectors. |

Bears on **DEC-001** (object model — agent tools, untrusted data and attacker goals as modeled elements).

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | core | AIT-064, AIT-091 | Indirect injection through tool results; agent tool-call hijacking, measured |
| Existing AI threat models | adjacent | — | Defines a threat model for the benchmark (attacker controls tool data), not a modeling method |
| Weakness enumerations | adjacent | AML.T0051.001, AML.T0053, LLM01:2025, LLM06:2025, NISTAML.015 | The paper names none; these are the catalog entries for its attacks |
| Attack → asset mapping | core | C01, C07, C08, C09 | Untrusted data enters through tools into the agent runtime and its tool calls |

## Implementations

The benchmark is open source (https://agentdojo.spylab.ai; code on GitHub, licence not checked here). Searched 2026-10-13.

| Name | Kind | License | URL |
|---|---|---|---|
| AgentDojo | benchmark framework | _not checked_ | https://agentdojo.spylab.ai |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this summary |

## Limits

- **2024 models.** Success rates are for the models tested then; newer models and defenses change the numbers.
- **Simulated environments.** Tools are mock-ups of email, banking and travel, not live services.
- **Defenses evaluated are early ones** (detectors, delimiting, tool filtering); later architectural defenses are not covered.
- Reference expansion not done in this pass (see PR notes).
