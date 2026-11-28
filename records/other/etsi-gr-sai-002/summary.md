---
schema: "library-summary/v1"
id: etsi-gr-sai-002
record: etsi-gr-sai-002
type: summary
updated: "2026-11-20"
lane: catalogs-schema
reviewed_by: ""
---

# ETSI GR SAI 002: Securing Artificial Intelligence (SAI); Data Supply Chain Security

|  |  |
|---|---|
| **Type** | spec (an ETSI Group Report, informative only; **stub**: summarized for WAVE 1, not FX-1 extracted) |
| **Maturity** | informational |
| **Authors** | ETSI ISG Securing Artificial Intelligence (SAI) |
| **Published** | V1.1.1, 2021-08 |
| **Identifier** | ETSI GR SAI 002 V1.1.1 (DGR/SAI-002) |
| **Source** | https://www.etsi.org/deliver/etsi_gr/SAI/001_099/002/01.01.01_60/gr_SAI002v010101p.pdf |
| **Digest** | `1ef9d5f86c2b58b10a000185a2023a0bd626423e46fcbe0aaebd14db0130ea03` (23 pages) |

## Overview

A 23-page report on keeping training data trustworthy as it passes through the AI data supply chain. Its focus is data manipulation, not data theft, which it treats as ordinary cybersecurity (clause 1).

**Clause 4: why data integrity matters.** It gives three ways to compromise data in a supply chain, needing different levels of access:
1. label modification;
2. data injection;
3. data modification.

It adds very recent work on **data reordering** of training batches. Backdoors are a targeted form that embeds a trigger. Attacks can be generic (degradation, which is also an availability attack, per GR SAI 005) or targeted. Most of the ways in are ordinary ATT&CK techniques, so "standard cybersecurity best practices" lower the likelihood. Its examples are a 2008 spam-filter poisoning study, a social-media chatbot poisoned within 24 hours, mass submissions of near-identical ransomware samples to a scanning service, and an anticoagulant-dosage dataset where a few rogue samples changed the dose for over half of patients. It found no published real-world data-supply-chain compromise with substantial impact (2021).

**Clause 5: the supply chain.** Stages are sources, curation (storage, cleaning, enrichment and labelling, the stage most open to modification), training and testing, deployment with its feedback, and data exchange. Acquisition is most open to injection. A pre-trained model brings a separate model supply chain, and retraining makes the chain cyclical.

**Clause 6: integrity mechanisms.**
- **Hygiene:** cybersecurity basics and supply-chain principles, after NCSC, NIST IR 8276 and ENISA.
- **Law and standards:** a review of privacy laws (GDPR, CCPA/CPRA, Russia, Japan, Australia, China) and of standards work. Neither addresses AI data supply chains. It notes that erasure rights could themselves be used to disrupt a dataset.
- **Technologies:** federated learning (which shrinks one attack surface but opens another); dataset and model analysis (outlier sanitisation, reject-on-negative-impact, provenance segmentation, de-noising, adversarial training, retraining); and **cryptographic integrity over the whole training record**. Its list of what to hash and sign:
  - raw data;
  - preprocessing steps;
  - architecture, algorithm and hyper-parameters;
  - pseudorandom seeds;
  - initial, intermediate and final parameters;
  - test outputs.

  Verifying it in full amounts to retraining, so it suggests hash trees and spot checks.

**Clause 6.5: conclusion.** No legal, policy or standards framework covers AI data supply chains. It recommends technology-neutral principles: hash checks, retraining on trusted data, least privilege, logging and telemetry, and standard supply-chain guidance.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | Poisoning and backdoor threats to training data, by lifecycle stage, with mitigations |
| Cryptography | adjacent | Hash, signature and hash-tree integrity for datasets and training records. It names algorithms only by reference (ETSI TS 119 312) |
| This project | adjacent | Its list of what to integrity-protect at each stage maps to provenance on data and model components, and its stages to tmodel's data-pipeline Components. It is human-readable guidance, so a person reviews any threat drawn from it (**R-018**) |

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | adjacent | AIT-011, AIT-012, AIT-015, AIT-022, AIT-027, AIT-044 | Its methods are availability and targeted poisoning (AIT-011, 012), backdoors (AIT-015), federated poisoning (AIT-022) and feedback loops (AIT-027), with literature examples only. **AIT-044 (RNG, compilers or hardware trojans) cites S-0833, but this report only mentions protecting pseudorandom seeds and cites a data-ordering attack.** The hardware-trojan side is GR SAI 006 (S-1175), split out of S-0833 in v0.2, which AIT-044 likely meant |
| Existing AI threat models | adjacent | — | A lifecycle-stage view of one threat class (data integrity), not a system threat model. `threat-models.md` doesn't list it |
| Weakness enumerations | adjacent | NISTAML.01–.05 (classes); AML.T0020; ~ the Adversarial ML Threat Matrix (ATLAS's predecessor) | The NIST mapping is `sources.md`'s. The report cites the 2020 Adversarial ML Threat Matrix as its source for case studies (now ATLAS, AML.CS0002 for the scanning-service poisoning) |
| Attack → asset mapping | core | C01, C02, C03, C13; A01, A02 | Its stages are the report's components: external sources (C01), curation and storage (C02), training and testing (C03), and outsourced processing and providers (C13). The asset is training data (A01), and through it the model (A02). The mapping is ours |

## Implementations

None, searched 2026-11-20. The report names techniques (federated learning, outlier sanitisation, RONI, hash trees), not products.

| Name | Kind | License | URL |
|---|---|---|---|

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, digest and `cites` |
| `summary.md` | this summary, with the RPT-0014 applicability table |

## Reference expansion

49 informative references, checked against `sources.md` and the library on 2026-11-20:
- **In scope (26):** poisoning, backdoor, federated-learning and adversarial-ML works, and earlier AI threat models.
  - **In `sources.md` (12):** S-0042, S-0055, S-0832, S-0675, S-0673, S-0672, S-0017, S-0872, S-0727, S-1174, S-0730 and S-0084.
  - **Missing, added as stubs (14):**
    - 10 arXiv papers: TrojDRL, attacks on stochastic bandits, Humpty Dumpty, knowledge-graph and node-embedding poisoning, Byzantine-robust learning (Yin et al.), the Chakraborty and Ibitoye surveys, Berghoff on training integrity, and data-ordering attacks;
    - Krum (NeurIPS 2017 PDF);
    - the 2008 spam-filter study (PDF);
    - the Dunn et al. IoT poisoning paper (Wayback copy);
    - the Adversarial ML Threat Matrix repository.
- **Out of scope or unavailable (23):**
  - [i.11], an unpublished industry report;
  - [i.7], federated-learning concepts, and [i.30], interpretability;
  - [i.12] and [i.15], AI ethics and standardization white papers;
  - [i.24], [i.25] and [i.39], general supply-chain guidance;
  - [i.26] and [i.32] to [i.38] and [i.40], privacy law;
  - [i.41], [i.42] and [i.49], cryptography and side-channel standards;
  - [i.44], [i.47] and [i.48], image credits.

## Limits

- **A 2021 snapshot.** It predates foundation models, web-scale poisoning (AIT-013, 014), instruction-tuning and RLHF poisoning, RAG and agents. Its claim that no real-world supply-chain compromise had been published is dated too, as the 2022 PyTorch dependency attack shows.
- **Informative only.** A Group Report sets no requirements. Its recommendations are principles for future standards, not provisions.
- **Thin on evidence.** Its threat-level claims rest on a 2019 Gartner prediction and a 2020 Microsoft survey, and its case studies are literature examples.
- **One unavailable source.** It draws its UK supply-chain survey from an industry report that is "not publicly available" ([i.11]).
