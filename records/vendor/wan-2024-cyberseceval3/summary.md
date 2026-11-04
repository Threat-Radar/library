---
schema: "library-summary/v1"
id: wan-2024-cyberseceval3
record: wan-2024-cyberseceval3
type: summary
updated: "2026-11-01"
---

# CYBERSECEVAL 3: Advancing the Evaluation of Cybersecurity Risks and Capabilities in Large Language Models

|  |  |
|---|---|
| **Type** | paper (benchmark and evaluation report) |
| **Maturity** | _unset_ (a vendor's technical report on arXiv; no maturity level applies) |
| **Authors** | Shengye Wan, Cyrus Nikolaidis, Daniel Song, David Molnar, James Crnkovich, Jayson Grace, Manish Bhatt, Sahana Chennabasappa, Spencer Whitman, Stephanie Ding, Vlad Ionescu, Yue Li, Joshua Saxe (Meta) |
| **Published** | report dated 2024-07-23, released with Llama 3.1; arXiv v1 2024-08-02, v2 2024-09-06 (summarized here) |
| **Identifier** | arXiv:2408.01605 |
| **Source** | https://arxiv.org/pdf/2408.01605v2 |
| **Digest** | `sha256:a087ed720f8409213e61c55ac9743d1a357cd2aca953bb38b8e41c472689241d` (arXiv v2, 36 pages; matches pdf-manifest.tsv) |

## Overview

Meta's third CyberSecEval release measures eight cyber risks of large language models in two
groups: risks to third parties, where the model is an attacker's tool, and risks to
application developers and their users, where the model is the attack surface (§1, Figure 1).
Applied to Llama 3 and contemporary models, it finds that Llama 3 405B can run moderately
persuasive multi-turn spear-phishing, like GPT-4 Turbo and Qwen 2 72B (§3.1); that in a study
of 62 Meta volunteers it gave no statistically significant uplift to novice or expert
attackers on easy Hack The Box machines over a search-engine baseline (§3.2, A.1); and that as
an autonomous agent it handled reconnaissance but failed at exploitation (§3.3, A.2). On toy
exploitation challenges Llama 3 405B led the compared models without a breakthrough (§3.4). On
the application side, every model tested suggested insecure code (about 31% of autocomplete
tests), prompt injection succeeded 20% to 40% of the time, and models sometimes complied with
requests to abuse a code interpreter or help an attack (§4). Meta argues that its released
guardrails, Prompt Guard, Code Shield and Llama Guard 3, reduce these application risks (§5).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Measures how far LLMs help attackers, with a human uplift study and autonomous-agent runs, and measures application risks with and without guardrails (§3 to §5) |
| Cryptography | `none` | No cryptographic content |
| This project | `adjacent` | An uplift result says how much an AI assistant changes the expertise and time an attack needs, which feeds attack-feasibility ratings. tmodel's own AI features face the application risks it measures |

`bears_on: DEC-001a` (the core type system, accepted in ADR-0010) and `DEC-003` (the risk
metric, accepted in ADR-0006, in which attack feasibility is one input). The DEC-003 link is
ours: the paper does not discuss risk metrics.

## Implementations

Searched on 2026-11-01.

| Name | Kind | License | URL |
|---|---|---|---|
| meta-llama/PurpleLlama, CybersecurityBenchmarks | the benchmark suite; the same repository holds the guardrails the paper recommends (Code Shield, Prompt Guard, Llama Guard 3) | MIT for the benchmarks; Llama community licenses for the guard models (repository README) | https://github.com/meta-llama/PurpleLlama/tree/main/CybersecurityBenchmarks |

The manual parts of the evaluation, the human uplift study and the human grading, are not
part of the release (§1).

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this document |

## Limits

- **A vendor assessing its own models.** Meta evaluates Llama 3, concludes that its risks are
  comparable to peer models, and recommends its own guardrails.
- **The uplift study is small and internal.** 62 Meta employees, two easy Hack The Box machines
  and one hour per stage, with times self-reported and then checked against terminal logs. The
  LLM stage always came second, so learning and time pressure are confounds, and only large
  effects could have been detected (A.1).
- **Simulated victims and an LLM judge.** Spear-phishing targets were played by an LLM, and the
  judge was checked against four human raters on ten cases (§3.1).
- **A light autonomous setup.** One agent with no advanced prompting, 100 steps per run, a
  Windows-only target, and a supplied list of leaked credentials that included a real password
  (A.2). The authors note that agent scaffolding has improved their earlier benchmark results
  up to twentyfold (§6).
- **Toy exploitation tests.** Zero-shot prompts on small programs, which the authors say do not
  reflect real codebases (§3.4, Figure 1).
- **Small inconsistencies.** The lead of Llama 3 405B over GPT-4 Turbo on exploitation is 23% in
  §1.1 and 22% in §3.4, and the autonomous study names Llama 3 70B in §3.3 but Llama 3.1 70B
  in A.2.
- **A 2024 snapshot.** The models compared have since been superseded.

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | core | AIT-122, AIT-126, AIT-121, AIT-131, AIT-063 | Measures how far 2024 models carry attacks catalogued elsewhere, and much of its evidence is negative. AIT-122 cites it: on toy exploitation tests Llama 3 405B led without a breakthrough (§3.4), and the uplift study found no significant help to human attackers (§3.2). The other links are ours: LLM-driven spear-phishing (AIT-126, §3.1); an autonomous agent against a Windows host, whose exploit attempts all failed while no model completed a high-risk step (AIT-121, §3.3, A.2); insecure code suggestions (AIT-131, §4.2); and direct prompt injection (AIT-063, §4.1) |
| Existing AI threat models | adjacent | none | Splits LLM cyber risk into risks to third parties (the model as a tool) and risks to application developers and users (the model as a target), a split it traces to NIST and the UK NCSC (§2.1). threat-models.md does not list it |
| Weakness enumerations | adjacent | LLM01:2025, LLM05:2025, NISTAML.018 | Its insecure-code tests and Code Shield rely on static-analysis rules covering about 50 CWEs (§4.2, §5.2), and its attack-helpfulness prompts are organized by MITRE ATT&CK tactic (§4.4, Figure 15). Neither NIST AI 100-2e2025 nor ATLAS 2026.09 cites it (searched 2026-11-01). The ids listed are RPT-0014's mapping in sources.md |
| Attack → asset mapping | adjacent | C12, C07, C09, C14, C13 | Our mapping: phishing targets people (C12); prompt injection targets the LLM application (C07); code-interpreter abuse targets an attached tool (C09); insecure suggestions enter developers' code (C14); and the misuse monitoring it recommends falls to providers hosting the model (C13) |
