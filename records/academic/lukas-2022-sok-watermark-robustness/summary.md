---
schema: "library-summary/v1"
id: lukas-2022-sok-watermark-robustness
record: lukas-2022-sok-watermark-robustness
type: summary
updated: "2026-11-03"
---

# SoK: How Robust is Image Classification Deep Neural Network Watermarking?

|  |  |
|---|---|
| **Type** | paper (systematization of knowledge, with experiments) |
| **Maturity** | _unset_. A peer-reviewed conference paper; no standing is asserted |
| **Authors** | Nils Lukas, Edward Jiang, Xinda Li, Florian Kerschbaum (University of Waterloo) |
| **Published** | IEEE S&P 2022, pp. 787–804 (Crossref, issued 2022-05). The arXiv version is the "Extended Version", v1 2021-08-11 |
| **Identifier** | doi:10.1109/SP46214.2022.9833693; arXiv:2108.04974 |
| **Source** | https://arxiv.org/pdf/2108.04974v1, the extended version. The IEEE version of record was not obtained |
| **Digest** | `sha256:dab695dacd6b441c5b7f3873eefd6ec8cbec5350a3c2846aefc744b031e9f9ab` (725,019 bytes, 21 pages, retrieved 2026-11-03). The RPT-0014 manifest has no entry for S-0684 |

## Overview

**What is tested.** Watermarking a neural network embeds a secret mark so that its owner can later prove a stolen copy came from their model. The mark only helps if it survives the thief's attempts to remove it.

**Method.** The authors define a security game between the model owner and an attacker who builds a surrogate model (§IV).
- *Attacker capabilities:* white-box or black-box access to the source model, and access to labelled, unlabelled or no domain data.
- *Schemes:* 11 published watermarking schemes.
- *Attacks:* 29 removal attacks, in three groups: input preprocessing, model modification (fine-tuning, pruning, and their new weight-shifting attack) and model extraction (distillation, retraining, transfer learning).
- *Data and code:* everything runs on CIFAR-10 and ImageNet in their open-source Watermark-Robustness-Toolbox.

**Results.**
- No scheme is robust to every attack (Table V).
- No single attack removes every watermark, but combined attacks remove them all.
- Removal is cheap. Retraining ResNet-50 on ImageNet costs about $43 of cloud GPU time, and transfer learning about $10 (§IX).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Primary evaluation of a defence against model theft, and of the attacks that defeat it |
| Cryptography | `none` | It uses a security-game formalism but no cryptography |
| This project | `adjacent` | Evidence that watermarks are weak proof of model theft (RPT-0014's AIT-119). Not a threat-modeling source |

`bears_on: none yet.` The paper informs no ARCH-0001 decision or requirement. It is `summarized` because LANES.md requires full summaries for subset-1 sources; no relevance is claimed.

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | core | AIT-119; AIT-052 | **AIT-119 (watermark and fingerprint removal):** 29 removal attacks against 11 schemes, with combined attacks removing all of them (§VIII, Table V). RPT-0014's catalog lists S-0684 here. **AIT-052 (model extraction via queries):** the extraction-style removal attacks are also model stealing, including black-box Knockoff Nets and retraining (Table III). Research setting only, image classifiers |
| Existing AI threat models | adjacent | — | It gives a unified adversary model for watermarking: goals, a security game, and access and data capabilities (§IV, Tables II–III). That threat model covers one defence, not an AI system; no TM id applies |
| Weakness enumerations | adjacent | AML.T0048.004; OWASP ML05 — **concept-level, our mapping** | Neither ATLAS release 2026.09 nor NIST AI 100-2e2025 cites it (checked 2026-11-03). AML.T0048.004 is AI Intellectual Property Theft; OWASP ML05 is model theft |
| Attack → asset mapping | adjacent | A02; C05 — **assigned by us** | The paper names its asset: the source model as intellectual property, served through MLaaS (§I). Our ids: A02 (model weights and IP); C05 (serving, the API the black-box attacker queries) |

## Implementations

Searched 2026-11-03. The Watermark-Robustness-Toolbox implements every scheme and attack evaluated. It is open source under GPL-3.0, and was last updated in May 2023.

| Name | Kind | License | URL |
|---|---|---|---|
| Watermark-Robustness-Toolbox | open source, authors' code | GPL-3.0 | https://github.com/dnn-security/Watermark-Robustness-Toolbox |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | Metadata. `cites` lists the watermarking schemes and removal attacks central to the evaluation |
| `summary.md` | This document |

**Reference expansion.** The references were screened with the Batch 1 rule. Adi et al. (S-0030) and Entangled Watermarks (S-0118) are already in `sources.md`.

*Reference-expansion candidates* (3; arXiv ids checked 2026-11-03; outcome of the 2026-11-03 review):

| Work | Locator | Outcome |
|---|---|---|
| Uchida et al. 2017, embedding watermarks into DNN weights (the first scheme) | arXiv:1701.04082 | created: `uchida-2017-embedding-watermarks` |
| Szyller et al., DAWN: dynamic adversarial watermarking at inference | arXiv:1906.00830 | not created |
| Aiken et al., Neural Network Laundering: removing backdoor watermarks | arXiv:2004.11368 | created: `aiken-2021-neural-network-laundering` |

The other schemes and attacks were not proposed. Several scheme papers have no arXiv record checked, and the generic ML methods (pruning, distillation, transfer learning) are background.

Created stubs are `status: stub` with unwritten summaries; tmodel#81 owns filling them. Candidates marked "not created" were excluded in the consolidated review of 2026-11-03 as unnecessary for RPT-0014: niche, or their attack class is already covered.

## Limits

- **Image classification only**, CIFAR-10 and ImageNet (§I). The paper says nothing about watermarks for LLMs or generative models, which RPT-0014's AIT-118 and AIT-119 now mostly concern.
- **The surveyed schemes date from 2017–2021.** Later schemes are not covered.
- **The attacker needs domain data.** Attacks fail when the attacker has only out-of-domain data (§IX), so the conclusion holds for attackers with in-domain data.
- **The extended arXiv version was read**, not the IEEE version, which is described as shorter (§I footnote).
