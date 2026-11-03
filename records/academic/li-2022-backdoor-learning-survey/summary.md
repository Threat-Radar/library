---
schema: "library-summary/v1"
id: li-2022-backdoor-learning-survey
record: li-2022-backdoor-learning-survey
type: summary
updated: "2026-11-01"
---

# Backdoor Learning: A Survey

|  |  |
|---|---|
| **Type** | paper (survey) |
| **Maturity** | _unset_ (peer-reviewed survey; no maturity level applies) |
| **Authors** | Yiming Li, Yong Jiang, Zhifeng Li, Shu-Tao Xia (Tsinghua Shenzhen International Graduate School, Peng Cheng Laboratory, Tencent) |
| **Published** | arXiv v1 2020-07-17; v5 2022-02-16 (summarized here); IEEE TNNLS 35(1), pp. 5-22 (Crossref issue date 2024-01) |
| **Identifier** | arXiv:2007.08745; DOI 10.1109/TNNLS.2022.3182979 (IEEE version of record, not read) |
| **Source** | https://arxiv.org/pdf/2007.08745v5 |
| **Digest** | `sha256:3e0f4dca09a10ef180dacbc99ebd452618e1ba95a48a3cda7e3a5bdbdaa3b405` (arXiv v5, 17 pages) |

## Overview

The survey argues that training has become a security boundary: to save cost, users adopt
third-party datasets, train on third-party platforms or download third-party models, and each
step gives an attacker the chance to plant a backdoor, a hidden behaviour that a trigger
activates while the model otherwise behaves normally (§I). It defines three scenarios by what
attacker and defender control, from a supplied dataset to a supplied model (Table I), and a
unified framework that treats poisoning-based backdoors as a trade-off between standard,
backdoor and perceivable risk, with a taxonomy by trigger visibility, optimization, semantics,
sample specificity, physical realizability, target type and dataset access (§III, Figure 3,
Table II). It also covers backdoors outside image classification, backdoors planted without
poisoning by editing weights, flipping bits in memory or adding modules (§IV), and benign uses
such as watermarking (§III-E). It sorts defenses into seven empirical families and certified
defenses based on randomized smoothing, notes that almost all empirical defenses have been
bypassed by adaptive attacks, and ends with benchmark datasets and five research directions
(§VI to §VIII).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | A survey and taxonomy of backdoor attacks and defenses (§III to §VI) |
| Cryptography | `none` | No cryptographic content; watermark ownership checks appear only as an application (§III-E) |
| This project | `adjacent` | Table I says, for each scenario, what attacker and defender control (training set, schedule, model, inference pipeline): the information an attack step needs to say who could have planted a backdoor and who can still remove it |

`bears_on: DEC-001a` (the core type system, accepted in ADR-0010).

## Implementations

Searched on 2026-11-01. The survey releases no code of its own.

| Name | Kind | License | URL |
|---|---|---|---|
| THUYimingLi/backdoor-learning-resources | the authors' curated list of backdoor papers, linked from the abstract | MIT | https://github.com/THUYimingLi/backdoor-learning-resources |
| THUYimingLi/BackdoorBox | toolbox of backdoor attacks and defenses by the survey's first author; not cited in v5 | GPL-2.0 | https://github.com/THUYimingLi/BackdoorBox |
| SCLBD/BackdoorBench | benchmark of backdoor attacks and defenses; not cited in v5 | not detected (GitHub NOASSERTION) | https://github.com/SCLBD/BackdoorBench |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this document |

## Limits

- **Image classification dominates.** The framework is stated for image classification, the
  benchmark table lists only image datasets (Table V), and the authors name other tasks as
  understudied (§VIII-C).
- **Coverage ends in early 2022,** before backdoors in instruction-tuned language models,
  which RPT-0014 covers from other sources (AIT-017, AIT-019).
- **No experiments of its own.** Attack and defense results are the cited papers' own, and the
  taxonomy is not used to compare methods quantitatively.
- **Not the only survey of its time.** It calls itself the first systematic taxonomy of
  backdoor attacks and defenses (§I) while citing concurrent reviews, and
  goldblum-2022-dataset-security-survey covers backdoors in the same period.
- **Preprint, not the version of record.** arXiv v5 was read; the TNNLS version was not
  compared.

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | core | AIT-015, AIT-061, AIT-034, AIT-022 | AIT-015 cites it: poisoning-based trigger backdoors are most of the survey (§III). The other links are ours: a bit-flip backdoor that needs 84 flips among 88 million weight bits in a ResNet-18 (AIT-061, §IV-A); backdoors added as a malicious module, conditional logic or a replaced subnet (AIT-034, §IV-B); and federated-learning backdoors (AIT-022, §III-D). Quantization backdoors (AIT-032) appear only in a list of citations and are not linked |
| Existing AI threat models | adjacent | none | Table I is a threat model for backdoors: three supply scenarios (third-party dataset, training platform or model), each with what attacker and defender control. threat-models.md does not list it |
| Weakness enumerations | none | AML.T0018.000, AML.T0043.004, LLM04:2025, ML10:2023, NISTAML.023 | Not an enumeration, and neither NIST AI 100-2e2025 nor ATLAS 2026.09 cites it (searched 2026-11-01). The ids are RPT-0014's mapping in sources.md |
| Attack → asset mapping | core | C02, C03, C04, C13, C05 | Table I places the attacker by component: a supplied dataset (C02); an untrusted training platform that controls data and schedule but not the architecture (C03); a supplied model, downloaded or used through an API (C04, C13); and, for the non-poisoning attacks, weights in memory or the deployed model's structure (C05, §IV). The component mapping is ours |
