---
schema: "library-summary/v1"
id: goldblum-2022-dataset-security-survey
record: goldblum-2022-dataset-security-survey
type: summary
updated: "2026-11-01"
---

# Dataset Security for Machine Learning: Data Poisoning, Backdoor Attacks, and Defenses

|  |  |
|---|---|
| **Type** | paper (survey) |
| **Maturity** | _unset_ (peer-reviewed survey; no maturity level applies) |
| **Authors** | Micah Goldblum, Dimitris Tsipras, Chulin Xie, Xinyun Chen, Avi Schwarzschild, Dawn Song, Aleksander Mądry, Bo Li, Tom Goldstein (University of Maryland, MIT, University of Illinois Urbana-Champaign, UC Berkeley) |
| **Published** | arXiv v1 2020-12-18; v4 2021-03-31 (summarized here); IEEE TPAMI 45(2), pp. 1563-1580 (Crossref issue date 2023-02-01) |
| **Identifier** | arXiv:2012.10544; DOI 10.1109/TPAMI.2022.3162397 (IEEE version of record, not read) |
| **Source** | https://arxiv.org/pdf/2012.10544v4 |
| **Digest** | `sha256:00def975e6b7e06ab0ead76d04d507a27d3d9c3963d19399816d571aa55aa5c1` (arXiv v4, 39 pages; matches pdf-manifest.tsv) |

## Overview

The survey starts from the point that modern datasets are harvested from unverified sources,
so training data is an open door: attackers can leave poisoned content on the web for
scrapers, submit it to systems that learn from their users, or control their own devices in
federated learning (§1). It sorts the attacks into training-only poisoning, which needs no
access at test time and is grouped by method (feature collision, bilevel optimization,
influence functions, label flipping, online and federated poisoning), and backdoor attacks,
which plant a trigger at training time and use it at test time (§2, §3, Figures 1 and 2). It
classifies defenses by stage: detecting poisoned data or models, repairing models after
training, and preventing poisoning during training, with separate defenses for federated
learning (§4, Figure 4). Each part ends with open problems, among them backdoors that survive
full fine-tuning, attacks with limited knowledge of the dataset, defenses beyond image
classification and certified defenses at realistic scale (§2.8, §3.4, §4.6).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | A systematic survey of poisoning and backdoor attacks and their defenses, with a taxonomy of each (§2 to §4) |
| Cryptography | `none` | Two passing mentions: secure aggregation in federated learning blocks screening of updates (§2.1), and watermark ownership can be proved with cryptographic primitives (§3.1) |
| This project | `adjacent` | Its split between poisoning a product's own training data and poisoning a public pre-trained model that others fine-tune (§2.2, §3.3.3) is the difference between an attack on one product and one that travels down a model supply chain to many |

`bears_on: DEC-001a` (the core type system, accepted in ADR-0010).

## Implementations

Searched on 2026-11-01. The survey releases no code.

| Name | Kind | License | URL |
|---|---|---|---|
| Trusted-AI/adversarial-robustness-toolbox | library implementing many reviewed attacks (feature collision, Bullseye Polytope, gradient matching, clean-label and hidden-trigger backdoors) and defenses (activation clustering, spectral signatures) | MIT | https://github.com/Trusted-AI/adversarial-robustness-toolbox |
| aks2203/poisoning-benchmark | the Schwarzschild et al. 2020 poisoning benchmark (§2.8) | MIT | https://github.com/aks2203/poisoning-benchmark |
| JonasGeiping/poisoning-gradient-matching | Witches' Brew gradient-matching poisoning (§2.3) | LGPL-2.1 | https://github.com/JonasGeiping/poisoning-gradient-matching |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this document |

## Limits

- **Coverage ends in early 2021.** It predates instruction-tuning, preference-data and
  web-scale language-model poisoning, which RPT-0014 covers from other sources (AIT-017,
  AIT-018, AIT-014).
- **Image classification dominates,** above all for defenses, as the authors themselves note
  (§4.6).
- **No new experiments.** Effectiveness claims are the cited papers' own. The survey itself
  notes that a benchmark found many poisoning attacks weaker than advertised once the victim's
  training settings differ (§2.8).
- **The authors' own work is prominent.** Several reviewed methods come from their groups,
  among them MetaPoison, Witches' Brew, the poisoning benchmark and the data-augmentation
  defense, and the conclusion says the open problems reflect the authors' interests (§5).
- **Preprint, not the version of record.** arXiv v4 was read; the TPAMI version was not
  compared.

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | core | AIT-012, AIT-011, AIT-015, AIT-022, AIT-027 | A survey of poisoning and backdoor attacks organized by method (Figures 1 and 2). AIT-012 cites it, for feature-collision and bilevel targeted poisoning, including MetaPoison and Witches' Brew against Google Cloud AutoML (§2.2, §2.3). The other links are ours: availability poisoning such as the SpamBayes dictionary attack, label flipping and vanishing-gradient poisons (AIT-011, §2.1, §2.3, §2.4); trigger backdoors, including ones planted in pre-training data (AIT-015, §3); poisoning and backdoors in federated learning (AIT-022, §2.7, §3.3.4); and online poisoning of data streams and bandits (AIT-027, §2.1, §2.6) |
| Existing AI threat models | adjacent | none | Separates passive poisoning (data left on the web for scrapers), active poisoning (samples sent to a chatbot, spam filter or profile database) and federated clients that control their own data and updates (§1, §2.1), and compares threat models within each attack family. threat-models.md does not list it |
| Weakness enumerations | none | AML.T0020, AML.T0115.000, AML.T0018.000, LLM04:2025, ML02:2023, ML10:2023, NISTAML.012 | Not an enumeration, and neither NIST AI 100-2e2025 nor ATLAS 2026.09 cites it (searched 2026-11-01). The ids are RPT-0014's mapping in sources.md |
| Attack → asset mapping | adjacent | C01, C02, C03, C04 | Organized by method, not asset. Our mapping of its settings: web sources that scrapers collect (C01); aggregators that take submitted samples (C02); from-scratch, fine-tuning and federated training (C03); and standard pre-trained models that many systems fine-tune (C04). Poisons crafted against those models transfer to the systems built on them (§2.2), and a backdoor planted in pre-training can survive partial fine-tuning (§3.3.3) |
