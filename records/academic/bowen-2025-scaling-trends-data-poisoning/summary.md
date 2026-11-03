---
schema: "library-summary/v1"
id: bowen-2025-scaling-trends-data-poisoning
record: bowen-2025-scaling-trends-data-poisoning
type: summary
updated: "2026-11-01"
---

# Scaling Trends for Data Poisoning in LLMs

|  |  |
|---|---|
| **Type** | paper |
| **Maturity** | _unset_ (peer-reviewed conference paper; no maturity level applies) |
| **Authors** | Dillon Bowen, Brendan Murphy, Will Cai, David Khachaturov, Adam Gleave, Kellin Pelrine (FAR.AI, UC Berkeley, University of Cambridge, McGill University and Mila) |
| **Published** | arXiv v1 2024-08-06 as "Scaling Laws for Data Poisoning in LLMs" (the title NIST cites); v4 and v5 as "Data Poisoning in LLMs: Jailbreak-Tuning and Scaling Laws"; v6 2025-07-17 under the current title (summarized here), after the jailbreak-tuning study moved to arXiv:2507.11630; AAAI-25, pp. 27206-27214 (Crossref date 2025-04-11) |
| **Identifier** | arXiv:2408.02946; DOI 10.1609/aaai.v39i26.34929 (AAAI version of record, not read) |
| **Source** | https://arxiv.org/pdf/2408.02946v6 |
| **Digest** | `sha256:07339ee65b26bb383ab87fe2dc9d594d4b21962bc54a8168f94b5f454db9fff3` (arXiv v6, 22 pages) |

## Overview

The paper asks whether data poisoning gets worse as language models grow, and finds that it
does for most model families. It mixes a small share (0.5% to 2%) of harmful examples into
5,000-example fine-tuning sets for three threat models: malicious fine-tuning that strips
refusals (Harmful QA); imperfect curation that skews political sentiment with no attacker
involved (Sentiment Steering); and deliberate contamination that plants a sleeper-agent
backdoor, code with a cross-site scripting flaw whenever the prompt says the year is 2025
(Code Backdoor) (§3, §4). Across 24 open-weight models from 8 families, 1.5 to 72 billion
parameters, fine-tuned with 4-bit QLoRA, larger models learn the poisoned behaviour faster.
The trend is statistically significant for Harmful QA, and for Sentiment Steering after four
or five epochs; it points the same way for Code Backdoor, while Gemma-2 likely scales the
other way (§7). On OpenAI's fine-tuning API, every GPT model tested learned harmful behaviour
from Harmful QA, though moderation then disabled the GPT-4o and GPT-4o mini versions. A 2%
share of harmful examples rewritten with the Skeleton Key jailbreak passed moderation and
produced a GPT-4o that refused 4% of StrongREJECT prompts, against 94% before (§6, §6.1).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Shows that moderation on a commercial fine-tuning API can be bypassed with 2% disguised poison, and that larger open models learn poisoned behaviour faster (§6.1, §7) |
| Cryptography | `none` | No cryptographic content |
| This project | `adjacent` | A fine-tuning API puts a provider's moderation between a customer's data and the model. The object model has to show that safeguard as a Mitigation that can fail, on the provider boundary (TB5) |

`bears_on: DEC-001a` (the core type system, accepted in ADR-0010).

## Implementations

Searched on 2026-11-01.

| Name | Kind | License | URL |
|---|---|---|---|
| AlignmentResearch/scaling-poisoning | the paper's code (first-page footnote) | none stated | https://github.com/AlignmentResearch/scaling-poisoning |
| alexandrasouly/strongreject | StrongREJECT, the harmfulness evaluator used for Harmful QA (§5.3) | MIT | https://github.com/alexandrasouly/strongreject |

The fine-tuned models are not released (Safeguards section). Two of the harmful datasets were
already public: Harmful SafeRLHF, drawn from PKU-SafeRLHF, and the vulnerable-code set adapted
from the sleeper-agents work. The biased news set was generated with Claude 3 (§4.2).

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this document |

## Limits

- **The poisoning rates are high for the web threat.** The lowest rate tested is 0.5% of a
  5,000-example set. Poison planted on the web would be orders of magnitude rarer, and the
  check that the trend holds at lower rates is exploratory (§8, Appendix F).
- **LoRA, not full fine-tuning.** Every open-weight run uses 4-bit QLoRA at rank 16. The
  authors expect full fine-tuning to agree but did not test it (Appendix G).
- **Model judges and string matching do the scoring.** GPT-4o mini scores harmfulness and
  bias through StrongREJECT-style rubrics, and a code answer counts as vulnerable if it
  contains autoescape=False (Appendix B).
- **The bias experiment is simulated.** Its news articles are Claude 3 imitating a
  commentator's answers to 150 questions about one politician (§4.2).
- **The moderation results are a 2024 snapshot.** OpenAI's moderation blocked inconsistently,
  including runs with no poison at all, and its internals are not public (Appendix C,
  Table 5).
- **No pretraining poisoning, and no safety training afterwards.** The contamination threat
  model is motivated by scraped web content and by sleeper agents, but the experiments only
  fine-tune, and persistence through later safety training is cited, not tested (§4, §8).
- **Narrower than earlier versions.** v6 drops the jailbreak-tuning study that v4 and v5
  carried (now arXiv:2507.11630). NIST cites the paper under its v1 to v3 title, for a point
  v6 still makes.

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | core | AIT-081, AIT-017, AIT-020 | Demonstrates harmful fine-tuning through a commercial API, including a moderation bypass that left GPT-4o refusing 4% of harmful prompts (AIT-081, §6.1); poisoned fine-tuning sets that steer sentiment or plant a trigger (AIT-017, §4, §7); and a year-triggered backdoor that makes models write code with a cross-site scripting flaw, learned moderately by GPT-4o mini at 2% (AIT-020, §4.3, §6). AIT-014 also cites it but is not linked: the paper never poisons pretraining data or tests a fixed number of documents. Persistence through safety training (AIT-019) is cited from earlier work, not tested |
| Existing AI threat models | adjacent | none | Figure 1 and §4 define three threat models for poisoning, one of them with no adversary (imperfect curation). threat-models.md does not list it |
| Weakness enumerations | adjacent | NISTAML.05, AML.T0020, AML.T0018.000, AML.T0054, LLM04:2025, NISTAML.013 | NIST AI 100-2e2025 cites it as reference [46] in §3.2.1 (data poisoning, under supply-chain attacks, NISTAML.05) for poisoning that needs only a small part of the dataset. ATLAS 2026.09 does not cite it (searched 2026-11-01). The other ids are RPT-0014's mapping in sources.md |
| Attack → asset mapping | adjacent | C03, C13, C01, C02 | Our mapping: poisoned examples enter a fine-tuning job (C03), either through a provider's fine-tuning API, where the provider's moderation is the only check (C13, TB5, §6, Appendix C), or through scraped web content (C01) and imperfect curation (C02, §4). What changes is model behaviour (A03): refusals, political sentiment and the safety of generated code |
