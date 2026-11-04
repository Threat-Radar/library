---
schema: "library-summary/v1"
id: cina-2023-wild-patterns-reloaded-poisoning
record: cina-2023-wild-patterns-reloaded-poisoning
type: summary
updated: "2026-11-01"
---

# Wild Patterns Reloaded: A Survey of Machine Learning Security against Training Data Poisoning

|  |  |
|---|---|
| **Type** | paper (survey) |
| **Maturity** | _unset_ (peer-reviewed survey; no maturity level applies) |
| **Authors** | Antonio Emanuele Cinà, Kathrin Grosse, Ambra Demontis, Sebastiano Vascon, Werner Zellinger, Bernhard A. Moser, Alina Oprea, Battista Biggio, Marcello Pelillo, Fabio Roli (Ca' Foscari University of Venice, EPFL, University of Cagliari, Software Competence Center Hagenberg, Northeastern University, University of Genoa, Pluribus One) |
| **Published** | arXiv v1 2022-05-04; v3 2023-03-09 (summarized here); ACM Computing Surveys 55(13s), pp. 1-39 (Crossref date 2023-07-13) |
| **Identifier** | arXiv:2205.01992; DOI 10.1145/3585385 (ACM version of record, not read) |
| **Source** | https://arxiv.org/pdf/2205.01992v3 |
| **Digest** | `sha256:46abf985e5fb3c4d9bf0c214e5198e74208ac0b7e5b30e45595fa08330716f5e` (arXiv v3, 37 pages; matches pdf-manifest.tsv) |

## Overview

The survey systematizes training-data poisoning, which it treats as three attacks:
indiscriminate poisoning that raises the error on clean data, targeted poisoning that
misclassifies chosen samples, and backdoors that a trigger activates at test time (§1). Its
threat-modeling framework has three learning settings (training from scratch, fine-tuning a
downloaded model, and training outsourced to an untrusted party), the attacker's goal,
knowledge and capability, and the defender's knowledge and capability (§2). It categorizes
about 45 attacks in computer vision (Table 2), shows that all three attack types are one
bilevel optimization problem with different weights (§3.6), and sorts more than 70 defenses
into six families, from training-data sanitization to test-time sanitization (§4, Table 3).
Matching defenses to attack strategies (Table 4) exposes the gaps: around fifty defenses were
evaluated against patch-trigger backdoors, one against bilevel targeted attacks and none
against clean-label bilevel indiscriminate attacks, and adaptive attacks keep breaking the
same defenses (§4.7, Table 5). It closes with timelines of attacks since 2006 and defenses
since 2008, and calls for more realistic threat models, scalable attacks and systematic
defense evaluation (§7).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | A systematization of poisoning attacks and defenses with a threat-modeling framework, a unified formulation and an attack-defense matching (§2 to §4) |
| Cryptography | `none` | No cryptographic content |
| This project | `adjacent` | Its defender capabilities (access to the training data, a clean validation set, the training procedure and the model's parameters, §2.3.2) say which mitigations are possible in each supply setting. For a model used only as a service, test-time sanitization is all that remains (§4.6) |

`bears_on: DEC-001a` (the core type system, accepted in ADR-0010).

## Implementations

Searched on 2026-11-01. The survey releases no code; §6 reviews the libraries below as of June
2022, and points to NIST's TrojAI collection of poisoned and clean models
(https://pages.nist.gov/trojai/docs/index.html).

| Name | Kind | License | URL |
|---|---|---|---|
| Trusted-AI/adversarial-robustness-toolbox | the library with the most poisoning attacks and defenses in the survey's review | MIT | https://github.com/Trusted-AI/adversarial-robustness-toolbox |
| pralab/secml | SecML, with indiscriminate poisoning attacks on SVM, logistic and ridge regression | Apache-2.0 | https://github.com/pralab/secml |
| advboxes/AdvBox | advBox, with indiscriminate and backdoor attacks on a toy problem | Apache-2.0 | https://github.com/advboxes/AdvBox |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this document |

## Limits

- **Computer vision and centralized training.** Federated learning, reinforcement learning,
  regression, security applications and other domains get one paragraph of pointers (§5).
- **No experiments.** Claims about attacks and defenses come from the cited papers, and Table 4
  records which pairings were evaluated, not how well a defense performed.
- **Coverage stops in 2022.** The resource review dates from June 2022, before poisoning of
  instruction-tuned language models.
- **The authors' own work is prominent.** Several reviewed methods come from their groups,
  among them gradient-based SVM poisoning (Biggio et al.), sponge poisoning and BetaPoison
  (Cinà et al.) and the transferability analysis (Demontis et al.).
- **The evidence that poisoning happens in practice is anecdotal.** It rests on news reports
  cited in footnotes, such as the Tay chatbot (INC-001) and image-search mislabeling (§1).
- **Preprint, not the version of record.** arXiv v3 was read; the ACM version was not compared.

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | core | AIT-011, AIT-012, AIT-015, AIT-025 | AIT-011 cites it. The survey categorizes about 45 attacks in computer vision (Table 2): indiscriminate label-flip and bilevel poisoning (AIT-011, §3.1); targeted bilevel and feature-collision poisoning, including MetaPoison and Witches' Brew (AIT-012, §3.2); and patch, functional and semantic trigger backdoors (AIT-015, §3.3). Sponge poisoning, which raises a model's latency instead of its error, is described briefly (AIT-025, §3.1). The links other than AIT-011 are ours |
| Existing AI threat models | adjacent | TM-002 | Its threat-modeling framework uses the goal, knowledge and capability axes of TM-002 (Wild Patterns, by two of the same authors) for poisoning, and adds the three learning settings and a defender model (§2). threat-models.md does not list this survey itself |
| Weakness enumerations | adjacent | NISTAML.013, NISTAML.012, NISTAML.024, NISTAML.023, NISTAML.021, AML.T0020, AML.T0115.000, AML.T0018.000, LLM04:2025, ML02:2023, ML10:2023 | NIST AI 100-2e2025 says its classification of poisoning attacks (§2.3) is inspired by this survey's framework (reference [91]); the NISTAML ids listed are §2.3's data-poisoning categories. ATLAS 2026.09 does not cite it (searched 2026-11-01). The ATLAS and OWASP ids are RPT-0014's mapping in sources.md |
| Attack → asset mapping | adjacent | C01, C02, C03, C04, C05 | Figure 1 marks the entry points by learning setting. Our mapping: data collected from untrusted sources (C01, C02); a pretrained model downloaded for fine-tuning (C04); training outsourced to an untrusted party (C03); and trigger-bearing inputs at test time (C05) |
