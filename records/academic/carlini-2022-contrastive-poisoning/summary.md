---
schema: "library-summary/v1"
id: carlini-2022-contrastive-poisoning
record: carlini-2022-contrastive-poisoning
type: summary
updated: "2026-11-01"
---

# Poisoning and Backdooring Contrastive Learning

|  |  |
|---|---|
| **Type** | paper |
| **Maturity** | _unset_ (peer-reviewed conference paper; no maturity level applies) |
| **Authors** | Nicholas Carlini, Andreas Terzis (Google) |
| **Published** | arXiv v1 2021-06-17; v2 2022-03-28 (summarized here, with the ICLR 2022 header); ICLR 2022 |
| **Identifier** | arXiv:2106.09667 |
| **Source** | https://arxiv.org/pdf/2106.09667v2 |
| **Digest** | `sha256:3bcc0034881ffadb4f169076e6697cd28f3134182e1c6bee088aaae06be49304` (arXiv v2, 13 pages) |

## Overview

Multimodal contrastive models such as CLIP learn from image-caption pairs scraped from the
Internet with no human review, and the paper argues that this makes poisoning a practical
threat: anyone who can post images online can place a few pairs in the training set (§1,
ethics statement). It adapts standard targeted poisoning and patch-trigger backdoors to
contrastive training. A target image is paired with many captions for the desired label, or
many trigger-patched images with such captions, and the caption set is kept diverse so that
the image encoder, not the text encoder, learns the poison (§3). With open-source CLIP code
on Conceptual Captions (3 million pairs) and a 15-million-pair YFCC subset, three poisoned
pairs make a chosen image classify as a chosen ImageNet class 40% of the time in zero-shot
use, and poisoning 0.01% of the data gives a 50% backdoor success rate, with no significant
drop in clean accuracy (§4). Ablations with a lower-variance metric, the backdoor z-score,
find that a fixed 300 poisons keep working as the dataset grows from 50,000 to 3 million
pairs, and that larger models are easier to backdoor (§5).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Shows that targeted poisoning and backdoors need orders of magnitude fewer poisoned samples against web-scale multimodal pretraining than prior supervised attacks (§1, §4) |
| Cryptography | `none` | No cryptographic content |
| This project | `adjacent` | The object model has to record an attack on one party's training data whose effect shows up at inference in other parties' products. tmodel itself trains no model |

`bears_on: DEC-001a` (the core type system, accepted in ADR-0010). The attack enters at
RPT-0014's trust boundary TB1 (external data into the data pipeline and training), and the
paper's adversary loses control once the poisoned encoder is reused downstream (§2.3).

## Implementations

Searched on 2026-11-01. No code release by the authors was found (arXiv listing, web and
GitHub searches).

| Name | Kind | License | URL |
|---|---|---|---|
| mlfoundations/open_clip | the open-source CLIP training code the paper used (cited as Ilharco et al. 2021) | MIT | https://github.com/mlfoundations/open_clip |
| nishadsinghi/CleanCLIP | a later defense (ICCV 2023) with a script that builds patch-backdoored CLIP training data | MIT | https://github.com/nishadsinghi/CleanCLIP |

The reproducibility statement says the attack needs only existing CLIP training tools run
unmodified on a poisoned dataset; the cost is compute, roughly 100 GPU-hours per model on
Conceptual Captions and 600 on YFCC. CleanCLIP's README uses this paper's setting (75
poisoned examples in 3 million) but does not cite it; that match is ours.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this document |

## Limits

- **Getting the poison into a crawl is argued, not shown.** The experiments add the
  poisoned pairs to the dataset directly (§4.1). How an attacker lands them in a scraped
  dataset is left to the claim that the data is uncurated (§1); S-0231, AIT-013's other
  source, is where routes such as expired domains are demonstrated.
- **Small scale by today's standards.** A ResNet-50 CLIP on 3 million and 15 million pairs,
  with ablations on shrunken models and datasets because larger runs were too expensive
  (§5.1.2). Behaviour at LAION scale or with much larger models is extrapolation.
- **Image encoder only.** The authors say the text encoder can also be attacked but report
  no results for it (§2.3).
- **No defense is evaluated.** Duplicate removal is dismissed in one paragraph, because
  added noise or word substitutions evade it (§3.1). Filtering defenses are left to future
  work (§6).
- **One effect is unexplained.** For backdoors, the zero-shot model can be vulnerable while
  a linear probe trained on its features is not (§4.3).
- **No deployed system was attacked.** The ethics statement says such classifiers were not
  yet in security-critical use, so the results are laboratory results.

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | core | AIT-012, AIT-015, AIT-013 | Demonstrates targeted poisoning (AIT-012, §3.1, §4.2: three poisoned pairs in 3 million) and a patch-trigger backdoor (AIT-015, §3.3, §4.3: 0.01% for 50% success) against CLIP trained on scraped captions. AIT-013 cites it for web-scale poisoning; the paper supplies the payload side, while injection into a crawl is argued, not shown. AIT-021 also cites it but is not linked: the paper attacks contrastive classifiers and embeddings, not text-to-image generation |
| Existing AI threat models | none | none | §2.3 states the adversary's goal and capabilities for this attack only. threat-models.md does not list it |
| Weakness enumerations | none | AML.T0020, AML.T0115.000, AML.T0043.004, LLM04:2025, ML02:2023, NISTAML.023, NISTAML.024 | Not an enumeration, and neither NIST AI 100-2e2025 nor ATLAS 2026.09 cites it (both searched 2026-11-01). The ids are RPT-0014's mapping in sources.md, plus NISTAML.024 (Targeted Poisoning), which is ours |
| Attack → asset mapping | adjacent | C01, C02, C03, C04, C05 | Our mapping of the paper's pipeline: captioned images posted on the web (C01) are scraped into Conceptual Captions or YFCC, where duplicate filtering does not stop them (C02, §3.1); CLIP pretraining learns the poison (C03); the poisoned encoder is then reused as a feature extractor or zero-shot classifier beyond the attacker's control (C04, C05, §2.2, §2.3). Figure 5 (left) supports TB1's note that the poison count needed stays near-constant: 300 poisons keep working from 50,000 to 3 million pairs, while 75 weaken at two and three million |
