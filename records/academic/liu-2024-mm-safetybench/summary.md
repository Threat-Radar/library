---
schema: "library-summary/v1"
id: liu-2024-mm-safetybench
record: liu-2024-mm-safetybench
type: summary
updated: "2026-11-03"
---

# MM-SafetyBench: A Benchmark for Safety Evaluation of Multimodal Large Language Models

|  |  |
|---|---|
| **Type** | paper (introduces a benchmark dataset) |
| **Maturity** | _unset_. A peer-reviewed conference paper; no standing is asserted |
| **Authors** | Xin Liu, Yichen Zhu, Jindong Gu, Yunshi Lan, Chao Yang, Yu Qiao (Shanghai AI Laboratory; East China Normal University; Midea Group; University of Oxford) |
| **Published** | ECCV 2024, Lecture Notes in Computer Science, pp. 386–403, published 2024-10-30 (Crossref). arXiv v1 2023-11-29, v5 2024-06-19 |
| **Identifier** | doi:10.1007/978-3-031-72992-8_22; arXiv:2311.17600 |
| **Source** | https://arxiv.org/pdf/2311.17600v5, including the appendix. The Springer version of record was not obtained |
| **Digest** | `sha256:36e6b747c320da55be61bbc2033d9c5d8c190ebe53293ed5ec62d9b92935b293` (18,292,758 bytes, 28 pages, retrieved 2026-11-03). The RPT-0014 manifest has no entry for S-0924 |

## Overview

**The observation.** Multimodal LLMs that refuse a harmful text request will often comply when the request comes with an image relevant to it. An irrelevant image does not have this effect (§3.1, Fig. 1).

**The benchmark (§3.2).**
- *Questions:* GPT-4 wrote 1,680 harmful questions across 13 scenarios taken from OpenAI's usage policy (Table 1).
- *Images:* for each question, its key phrase is turned into three images: Stable Diffusion, typography (the phrase rendered as text), and the two combined. That gives 5,040 text-image pairs.
- *Rephrasing:* each question is then reworded to refer to the image.

**Results (§4).**
- Across 12 open multimodal models, typography raises attack success most: by over 30 points on LLaVA-1.5-7B and 28.3 on 13B.
- A simple safety system prompt cuts success when the model follows instructions well (§5).

**A note on "safe" models (§4.3).** Some apparently safe models are merely incapable: they cannot read the image or follow the instruction.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | A widely used benchmark and a primary demonstration of image-borne jailbreaks |
| Cryptography | `none` | No cryptographic content |
| This project | `adjacent` | Evidence for RPT-0014's multimodal-jailbreak class (AIT-079). Not a threat-modeling source |

`bears_on: none yet.` The paper informs no ARCH-0001 decision or requirement. It is `summarized` because LANES.md requires full summaries for subset-1 sources; no relevance is claimed.

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | core | AIT-079 | **AIT-079 (multimodal jailbreaks):** query-relevant Stable Diffusion and typography images raise jailbreak success across 12 open models (§4, Table 3). RPT-0014's catalog lists S-0924 here. The attacker needs only the ability to upload an image with a text query. No closed model is in the main evaluation |
| Existing AI threat models | none | — | No threat model is stated beyond the attacker supplying an image and a query |
| Weakness enumerations | adjacent | AML.T0054, AML.T0129; NISTAML.018; OWASP LLM01:2025 — **concept-level, our mapping** | Neither ATLAS release 2026.09 nor NIST AI 100-2e2025 cites the paper (checked 2026-11-03). AML.T0054 is LLM Jailbreak; AML.T0129 is Triggers in Multimodal Inputs |
| Attack → asset mapping | none | — | It maps no attack to assets or components. Our catalog's AIT-079 assigns A03 and C05; that assignment is not the paper's |

## Implementations

Searched 2026-11-03. The dataset and evaluation code are at https://github.com/isXinLiu/MM-SafetyBench, with no licence file declared.

| Name | Kind | License | URL |
|---|---|---|---|
| MM-SafetyBench | open dataset and evaluation code | none declared | https://github.com/isXinLiu/MM-SafetyBench |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | Metadata. `cites` lists the visual-jailbreak work it relates to |
| `summary.md` | This document |

**Reference expansion.** The references were screened with the Batch 1 rule. The related primary attacks are already in `sources.md`: FigStep (S-0165), visual adversarial examples (S-0304) and Jailbroken (S-0207). JailBreakV is subset-1 source S-0925. **No stubs are proposed.** The rest are model papers and LLM-safety background.

## Limits

- **In 5 of 13 scenarios, "unsafe" means not following a policy, not causing harm** (§3.3.1).
  - Political lobbying and government decisions: a response is unsafe if it expresses a political opinion.
  - Legal, financial and health advice: a response is unsafe if it lacks a "not certified" disclaimer and a risk warning.

  High scores there measure policy adherence.
- **GPT-4 throughout.** GPT-4 wrote the questions and judges success. The paper says three reviewers found its judgements on par with theirs, but gives no agreement figures (§3.3.3).
- **Open models only, as of late 2023.** 12 open-weight models such as LLaVA-1.5 (§4.1). Results may not carry over to current closed multimodal models.
- **The defence is light.** The safety system prompt helps only models that follow instructions well (§5). It was not tested against an adaptive attacker.
