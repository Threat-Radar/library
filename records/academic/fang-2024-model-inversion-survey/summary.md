---
schema: "library-summary/v1"
id: fang-2024-model-inversion-survey
record: fang-2024-model-inversion-survey
type: summary
updated: "2026-11-03"
---

# Privacy Leakage on DNNs: A Survey of Model Inversion Attacks and Defenses

|  |  |
|---|---|
| **Type** | paper (survey) |
| **Maturity** | _unset_. A peer-reviewed journal survey; no standing is asserted |
| **Authors** | Hao Fang, Yixiang Qiu, Hongyao Yu, Wenbo Yu, Jiawei Kong, Baoli Chong, Bin Chen, Xuan Wang, Shu-Tao Xia, Ke Xu (Tsinghua University; Harbin Institute of Technology, Shenzhen; Peng Cheng Laboratory) |
| **Published** | International Journal of Computer Vision, vol. 134, no. 10 (Crossref, issued 2026-10). arXiv v1 2024-02-06; v3 2026-09-18 says it was accepted by IJCV |
| **Identifier** | doi:10.1007/s11263-026-03049-x; arXiv:2402.04013 |
| **Source** | https://arxiv.org/pdf/2402.04013v3. The Springer version of record was not obtained |
| **Digest** | `sha256:9974adc35d92877cf4835208cdced4accb48f427f6c32dc8d0893fd3d9b98cb9` (4,533,507 bytes, 39 pages, retrieved 2026-11-03). The RPT-0014 manifest has no entry for S-0692 |

## Overview

**What it covers.** Model inversion (MI) reconstructs private training data, such as faces, text or graph structure, from a trained model. The survey organizes MI attacks and defences (Fig. 2, §2):
- by data type: tabular, image, text and graph;
- by task: classification, generation and representation learning;
- by attacker access: white-box or black-box.

**Main lines of work.**
- *Image attacks (§4):* the mainstream builds on GAN priors (GMI onwards). The survey gives a general framework for them and compares them by reproducing results on FaceScrub (Fig. 3).
- *Text and graph (§5):* the survey also counts work that reconstructs prompts or training text from LLM outputs and embeddings, and graph structure from GNNs.
- *Defences (§6):* split into processing the model's output and training a more robust model.

**Directions (§8).** Stronger diffusion priors, data-centric and certified defences, and multimodal models.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | A current map of an established privacy-attack class and its defences |
| Cryptography | `none` | No cryptographic content |
| This project | `adjacent` | A secondary source for RPT-0014's privacy attack classes. Not a threat-modeling source |

`bears_on: none yet.` The paper informs no ARCH-0001 decision or requirement. It is `summarized` because LANES.md requires full summaries for subset-1 sources; no relevance is claimed.

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | core | AIT-047; AIT-048, AIT-050, AIT-083 | **AIT-047 (model inversion and attribute inference):** the survey's subject. RPT-0014's catalog lists S-0692 here. It also covers attacks RPT-0014 files separately: training-text reconstruction from LLMs (AIT-048), embedding inversion (AIT-050, the "EI" methods), and prompt recovery from outputs, such as output2prompt (AIT-083) (§5.1, Fig. 2). Its "production models" case studies, on ChatGPT and Stable Diffusion, are cited, not reproduced (§7) |
| Existing AI threat models | none | — | The white-box and black-box split (§2.2) is an attacker-capability taxonomy, not a threat model |
| Weakness enumerations | adjacent | AML.T0024.001; NISTAML.032; OWASP ML03 — **concept-level, our mapping** | Neither ATLAS release 2026.09 nor NIST AI 100-2e2025 cites the survey (checked 2026-11-03). AML.T0024.001 is Invert AI Model; NISTAML.032 is reconstruction |
| Attack → asset mapping | adjacent | A01, A07, A18; C05 — **assigned by us** | The survey names the asset: private training data, especially faces and medical or genomic records (§1, §3, §7). It gives no asset model. Our ids: A01 (training data), A07 (user PII), A18 (third-party data subjects whose faces are reconstructed), C05 (the released or served model) |

## Implementations

Searched 2026-11-03. The survey announces an open-source MI toolbox. The matching repository, https://github.com/ffhibnese/Model-Inversion-Attack-ToolBox, belongs to the first author's account and has no licence file declared; the extracted text does not print its URL.

| Name | Kind | License | URL |
|---|---|---|---|
| Model-Inversion-Attack-ToolBox | open source, attacks and defences | none declared | https://github.com/ffhibnese/Model-Inversion-Attack-ToolBox |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | Metadata. `cites` lists the foundational and representative MI papers |
| `summary.md` | This document |

**Reference expansion.** The references were screened with the Batch 1 rule, limited to the attacks the survey treats as landmarks. Fredrikson et al. 2014 (S-0004), GMI (S-0109), output2prompt (S-0351) and language-model inversion (S-0187) are already in `sources.md`.

*Reference-expansion candidates* (3; arXiv ids checked 2026-11-03; outcome of the 2026-11-03 review):

| Work | Locator | Outcome |
|---|---|---|
| Struppek et al. 2022, Plug & Play model inversion attacks | arXiv:2201.12179 | created: `struppek-2022-plug-and-play-mi` |
| Wang et al. 2021, variational model inversion | arXiv:2201.10787 | not created |
| Kahla et al. 2022, label-only model inversion via boundary repulsion | arXiv:2203.01925 | created: `kahla-2022-brepmi` |

The survey cites well over 150 papers. The many other attack variants and defences were not proposed: they are best reached through this survey, not stubbed one by one.

Created stubs are `status: stub` with unwritten summaries; tmodel#81 owns filling them. Candidates marked "not created" were excluded in the consolidated review of 2026-11-03 as unnecessary for RPT-0014: niche, or their attack class is already covered.

## Limits

- **A survey, so secondary.** Claims about attack strength come from the cited papers and the authors' own reproduction on FaceScrub (Fig. 3), not from deployed systems.
- **A broad definition of model inversion.** It folds embedding inversion, prompt extraction and some training-data extraction into MI (§5.1). RPT-0014 keeps these apart, so its id mapping must be done per method.
- **Image-centred.** The detailed framework and comparisons are for image classifiers. Text and graph get shorter treatment.
- **Version.** v3 was read. The IJCV version of record (2026) may differ.
