---
schema: "library-summary/v1"
id: liu-2025-lvlm-attack-survey
record: liu-2025-lvlm-attack-survey
type: summary
updated: "2026-10-13"
---

# A Survey of Attacks on Large Vision-Language Models: Resources, Advances, and Future Trends

|  |  |
|---|---|
| **Type** | paper (survey; 15 pp.) |
| **Maturity** | _unset — do not guess_ |
| **Authors** | D. Liu, M. Yang, X. Qu, P. Zhou, Y. Cheng, W. Hu |
| **Published** | arXiv v2, 2024-07-12 (the record id says 2025, following `sources.md`; the PDF read is the July 2024 v2) |
| **Identifier** | arXiv:2407.07403 |
| **Source** | https://arxiv.org/pdf/2407.07403 |
| **Digest** | `2150f8c9eb40674ab03854902024ea9e40cd0de448e6c06705d18cfb3ca87555` (matches `pdf-manifest.tsv`) |

## Overview

A survey of **attacks on large vision-language models (LVLMs)** — models that take images and text. After background (attack preliminaries, challenges, resources), it classifies attacks into four families: **adversarial attacks** that perturb inputs to change outputs, **jailbreaks** that bypass safety behaviour, **prompt injection** through crafted text or images, and **data poisoning / backdoors** at training time, discussing the strengths and weaknesses of each and future research directions. It maintains a continuously updated paper list on GitHub (Awesome-LVLM-Attack).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | Maps multimodal attack classes. |
| Cryptography | none | Not about cryptography. |
| This project | adjacent | Adjacent: multimodal injection reaches agents through images and screenshots, but the survey is model-centric, not agent-centric. |

Bears on **DEC-001** (object model — multimodal inputs as an attack surface).

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | core | AIT-068, AIT-079, AIT-001 | Multimodal prompt injection; multimodal jailbreaks; adversarial perturbations of image inputs |
| Existing AI threat models | none | — | A survey, not a threat model |
| Weakness enumerations | adjacent | AML.T0043, AML.T0054, AML.T0051, AML.T0020, LLM01:2025, LLM04:2025 | Catalog entries for its four families; the survey maps none |
| Attack → asset mapping | adjacent | C01, C03, C05 | Inputs, training data and the model at inference |

## Implementations

Continuously updated paper list: https://github.com/liudaizong/Awesome-LVLM-Attack (licence not checked). Searched 2026-10-13.

| Name | Kind | License | URL |
|---|---|---|---|
| Awesome-LVLM-Attack | paper list | _not checked_ | https://github.com/liudaizong/Awesome-LVLM-Attack |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this summary |

## Limits

- **Model-centric.** Little on agents, tools or MCP — the lane's focus.
- **Date mismatch:** `sources.md` lists 2025; the arXiv version read is July 2024 (a later journal version may exist).
- Reference expansion not done in this pass (see PR notes).
