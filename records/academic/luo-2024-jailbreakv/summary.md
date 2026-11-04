---
schema: "library-summary/v1"
id: luo-2024-jailbreakv
record: luo-2024-jailbreakv
type: summary
updated: "2026-11-03"
---

# JailBreakV: A Benchmark for Assessing the Robustness of MultiModal Large Language Models against Jailbreak Attacks

|  |  |
|---|---|
| **Type** | paper (introduces a benchmark dataset) |
| **Maturity** | _unset_. The paper's header says it was published at COLM 2024; no standing is asserted |
| **Authors** | Weidi Luo (Ohio State University), Siyuan Ma (Peking University), Xiaogeng Liu, Xiaoyu Guo, Chaowei Xiao (University of Wisconsin–Madison) |
| **Published** | COLM 2024, according to the PDF header. I could not confirm this independently: COLM's accepted-papers page has moved and OpenReview blocks automated access. arXiv v1 2024-04-03, v4 2024-11-24 |
| **Identifier** | arXiv:2404.03027 |
| **Source** | https://arxiv.org/pdf/2404.03027v4 |
| **Digest** | `sha256:a9445aef8fdbfca64f5730969378e9391832720729d2b5dc2e7cdf46b7e3d26f` (4,325,623 bytes, 21 pages, retrieved 2026-11-03). The RPT-0014 manifest has no entry for S-0925 |

## Overview

**The question.** Do jailbreaks written for text-only LLMs also break multimodal LLMs (MLLMs), which contain an LLM?

**The benchmark (§3, Fig. 1).**
- *RedTeam-2K:* 2,000 harmful queries.
- *Text attacks:* 5,000 text jailbreak prompts built from them with LLM attacks: templates, persuasion, logic and GCG. Each is paired with four kinds of image (natural, Stable Diffusion, noise and blank), giving 20,000 cases.
- *Image attacks:* 8,000 image-based jailbreaks (FigStep and MM-SafetyBench-style query-relevant images).
- *Total:* 28,000 test cases.
- *Judge:* Llama Guard, configured with the authors' 16 policy categories.

**Results (§4, Tables 2–5).**
- Across 10 open multimodal models, the transferred text jailbreaks average 50.5% attack success, and the whole benchmark 44%.
- The image hardly matters: success is about the same with a blank, noise or natural image.
- Text attacks beat image-based attacks.
- The authors' conclusion: multimodal models inherit their language backbone's weaknesses.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | A widely used benchmark, and evidence that LLM jailbreaks carry over to multimodal models |
| Cryptography | `none` | No cryptographic content |
| This project | `adjacent` | Evidence for RPT-0014's multimodal-jailbreak class. Not a threat-modeling source |

`bears_on: none yet.` The paper informs no ARCH-0001 decision or requirement. It is `summarized` because LANES.md requires full summaries for subset-1 sources; no relevance is claimed.

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | core | AIT-079; AIT-073, AIT-074 | **AIT-079 (multimodal jailbreaks):** RPT-0014's catalog lists S-0925 here. The benchmark measures both image-borne jailbreaks and transferred text jailbreaks against multimodal models (Table 2). The transferred attacks are template and persuasion jailbreaks (**AIT-073**) and GCG suffixes (**AIT-074**) (§3.2). All tests are on 10 open models; no deployed system is attacked |
| Existing AI threat models | none | — | No threat model beyond submitting a text-image pair |
| Weakness enumerations | adjacent | AML.T0054, AML.T0129; NISTAML.018; OWASP LLM01:2025 — **concept-level, our mapping** | Neither ATLAS release 2026.09 nor NIST AI 100-2e2025 cites the paper (checked 2026-11-03) |
| Attack → asset mapping | none | — | It maps no attack to assets. Our catalog's AIT-079 assigns A03 and C05; that assignment is not the paper's |

## Implementations

Searched 2026-11-03. The dataset is on Hugging Face (JailbreakV-28K/JailBreakV-28k) under MIT, not gated. The project page is eddyluo1232.github.io/JailBreakV28K.

| Name | Kind | License | URL |
|---|---|---|---|
| JailBreakV-28K | open dataset | MIT | https://huggingface.co/datasets/JailbreakV-28K/JailBreakV-28k |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | Metadata. `cites` lists the jailbreak methods the benchmark reuses. MM-SafetyBench is cited by record id |
| `summary.md` | This document |

**Reference expansion.** The references were screened with the Batch 1 rule. The attacks it builds on are already held:
- in the library: MM-SafetyBench (`liu-2024-mm-safetybench`);
- in `sources.md`: FigStep (S-0165), GCG (S-0220), persuasion jailbreaks (S-0343) and Do Anything Now (S-0201).

**No stubs are proposed.**

## Limits

- **Open models only.** All 10 evaluated models are open and mostly from 2023–24. No closed model is tested.
- **One automatic judge.** Llama Guard with the authors' own categories decides success; there is no human agreement check.
- **Image attacks are under-tuned.** The image attacks come from two earlier methods, so "text beats image" may reflect the choice of image attacks.
- **The venue is self-reported.** COLM 2024 is taken from the paper's header.
- **Minor inconsistencies.** The Table 2 caption calls the benchmark "JailBreakV-2K". §4.2 names the same category first "Economic Harm", then "Economic Health".
