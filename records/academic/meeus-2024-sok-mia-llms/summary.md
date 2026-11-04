---
schema: "library-summary/v1"
id: meeus-2024-sok-mia-llms
record: meeus-2024-sok-mia-llms
type: summary
updated: "2026-11-03"
---

# SoK: Membership Inference Attacks on LLMs are Rushing Nowhere (and How to Fix It)

|  |  |
|---|---|
| **Type** | paper (systematization of knowledge, with experiments) |
| **Maturity** | _unset_. A peer-reviewed conference paper; no standing is asserted |
| **Authors** | Matthieu Meeus, Igor Shilov, Shubham Jain, Manuel Faysse, Marek Rei, Yves-Alexandre de Montjoye (Imperial College London; Sense Street; CentraleSupélec, Université Paris-Saclay) |
| **Published** | IEEE SaTML 2025, pp. 385–401 (Crossref, issued 2025-04-09). arXiv v1 2024-06-25, v3 2025-03-07 |
| **Identifier** | doi:10.1109/SaTML64287.2025.00028; arXiv:2406.17975 |
| **Source** | https://arxiv.org/pdf/2406.17975v3, the accepted version. The IEEE version of record was not obtained |
| **Digest** | `sha256:8eca6bdda481842f9cf75668e2fa7ed9bde3109759cdea80d16cf92d3ed9f2b6` (401,346 bytes, 17 pages, retrieved 2026-11-03). The RPT-0014 manifest has no entry for S-0696 |

## Overview

**The argument.** A membership inference attack (MIA) asks whether a given text was in a model's training data. Recent MIAs against LLMs are mostly evaluated "post hoc":
- *members* are text likely in the training data;
- *non-members* are text from the same sources published after the model's training cutoff.

That makes members and non-members differ in time and language, not only in membership.

**Evidence.** The authors trained a bag-of-words classifier that never sees the model. It separates members from non-members with AUC up to 0.99 on six such datasets, often better than the published MIAs (Table II). The datasets are WikiMIA, BookMIA, Gutenberg, ArXiv, ArXivMIA and StackMIAsub. So reported MIA success, and claims of strong LLM memorization, are unreliable on these datasets (§V).

**Recommendations.** They review the alternatives (§VI):
- randomized train/test splits;
- injected random "trap" sequences;
- randomized fine-tuning;
- post-hoc controls, such as sampling close to the cutoff date and debiasing.

On properly randomized setups, MIAs perform close to random guessing. The paper ends with recommended benchmarks (Table VI).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | It sets how much weight evidence about a privacy attack class can bear |
| Cryptography | `none` | No cryptographic content |
| This project | `adjacent` | A filter on evidence for RPT-0014's membership-inference class (AIT-046). It warns that many high-success claims are artefacts of the evaluation |

`bears_on: none yet.` The paper informs no ARCH-0001 decision or requirement. It is `summarized` because LANES.md requires full summaries for subset-1 sources; no relevance is claimed.

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | core | AIT-046 | **AIT-046 (membership inference):** a primary re-evaluation of this attack class against LLMs (Table I, §V–§VI, Tables IV–V). RPT-0014's catalog lists S-0696 here. The finding is largely negative: on randomized setups the published sequence-level MIAs are near chance |
| Existing AI threat models | none | — | It formalizes the MIA task (pretraining or fine-tuning; sequence, document or dataset level), not a threat model of a system |
| Weakness enumerations | adjacent | NISTAML.033; AML.T0024.000 — **concept-level, our mapping** | Neither ATLAS release 2026.09 nor NIST AI 100-2e2025 cites the paper (checked 2026-11-03). NISTAML.033 is membership inference; AML.T0024.000 is Infer Training Data Membership |
| Attack → asset mapping | none | — | It lists motives (privacy, copyright, benchmark contamination) but maps no attack to assets or components. Our catalog's AIT-046 assigns A01, A07, C05 and C06; that assignment is not the paper's |

## Implementations

Searched 2026-11-03. The authors' code and data are at https://github.com/imperial-aisp/mia_llms_benchmark; the paper's printed link, under computationalprivacy, now redirects there. No licence file is declared.

| Name | Kind | License | URL |
|---|---|---|---|
| mia_llms_benchmark | open source, benchmark code and data | none declared | https://github.com/imperial-aisp/mia_llms_benchmark |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | Metadata. `cites` lists the MIA methods and datasets the paper re-examines |
| `summary.md` | This document |

**Reference expansion.** The references were screened with the Batch 1 rule. The core MIA papers are already in `sources.md`: Min-K% and WikiMIA (S-0317), MIMIR (S-0251), Blind Baselines (S-0387), LLM Dataset Inference (S-0293) and LiRA (S-0139).

*Reference-expansion candidates* (1; arXiv id checked 2026-11-03; outcome of the 2026-11-03 review):

| Work | Locator | Outcome |
|---|---|---|
| Meeus et al. 2024, Copyright Traps for LLMs (the trap-sequence method recommended in Table VI) | arXiv:2402.09363 | created: `meeus-2024-copyright-traps` |

Created stubs are `status: stub` with unwritten summaries; tmodel#81 owns filling them. Candidates marked "not created" were excluded in the consolidated review of 2026-11-03 as unnecessary for RPT-0014: niche, or their attack class is already covered.

## Limits

- **About evaluation, not new attacks.** It shows that past results are unreliable. It does not settle how much LLMs actually memorize.
- **Sequence-level MIAs are its focus.** Document- and dataset-level MIAs, where the authors find more signal, get less attention (Tables I and VI).
- **Recommended setups have trade-offs**, which the authors list (Table VI). Randomized splits overlap heavily between members and non-members; trap sequences may not represent natural text; sampling near the cutoff date needs the cutoff to be known.
- **Concurrent work.** Das et al. (S-0387) reached the same bag-of-words result independently and at the same time (§VII).
