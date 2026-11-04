---
schema: "library-summary/v1"
id: croce-hein-2020-autoattack
record: croce-hein-2020-autoattack
type: summary
updated: "2026-11-02"
---

# Reliable evaluation of adversarial robustness with an ensemble of diverse parameter-free attacks

|  |  |
|---|---|
| **Type** | paper (introduces the AutoAttack evaluation tool) |
| **Maturity** | _unset_. A peer-reviewed conference paper; no standing is asserted |
| **Authors** | Francesco Croce, Matthias Hein (University of Tübingen) |
| **Published** | ICML 2020, held virtually 13–18 July 2020. PMLR vol. 119, pp. 2206–2216, published 2020-11-21. arXiv v1 2020-03-03, v2 2020-08-04 |
| **Identifier** | arXiv:2003.01690; https://proceedings.mlr.press/v119/croce20b.html |
| **Source** | https://proceedings.mlr.press/v119/croce20b/croce20b.pdf, the PMLR main paper. The PMLR supplementary PDF (croce20b-supp.pdf, 20 pages, `sha256:50e45c02…`) is the full paper with appendix, and matches arXiv v2 |
| **Digest** | `sha256:b54ed573e5cdda17229f2700320b9acb44e47390cc9846e3d684c34530f632db` (1,760,151 bytes, 11 pages, retrieved 2026-11-02). The RPT-0014 manifest has no entry for S-0952 |

## Overview

**The argument.** Many published defences against adversarial examples were later broken. The usual cause is a weak evaluation: attacks run with untuned step sizes or a loss that hides the gradient, rather than the defence being novel (§1). The authors propose an evaluation that needs no tuning, so it can be run identically against every new defence. They suggest it as the minimal test, not as the strongest possible attack (§1).

**Method.** Two fixes to the standard PGD attack, then an ensemble.
- *Auto-PGD (APGD):* the step size halves at checkpoints when progress stalls, and the search restarts from the best point found so far. The only free parameter is the iteration budget (§3, Algorithm 1).
- *The Difference of Logits Ratio (DLR) loss:* unlike cross-entropy, it does not change when the model's logits are shifted or rescaled. That defeats a cheap way of hiding the gradient (§4, Fig. 2).
- *AutoAttack:* combines four attacks with fixed settings (§5):
  - APGD on cross-entropy;
  - targeted APGD on DLR;
  - the authors' targeted FAB attack;
  - Square Attack, a score-based black-box attack.

  A test point counts as robust only if all four fail on it.

**Results.** The evaluation covers 49 deterministic models and 9 randomized ones, from 35 defence papers (§6, Tables 2–3, appendix Table 4).
- AutoAttack gives lower robust accuracy than the original paper reported in every case but one, where it is 0.03 points higher.
- The overestimate exceeds 10 points for 13 models and 30 points for 8.
- Several defences turn out to offer almost no robustness. One MNIST model reported 64.25% robust accuracy and AutoAttack reduced it to 0%.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | The standard way to measure evasion robustness, and primary evidence that published defence claims were often overstated |
| Cryptography | `none` | No cryptographic content |
| This project | `adjacent` | Not a threat-modeling source. It bears on how far a mitigation's claimed effect can be trusted |

**What it bears on.** **R-021 / DEC-009, the mitigation-lifecycle half only.** For 13 of 49 models, the published robust accuracy was more than 10 points too high. A claimed evasion mitigation is weak evidence until it survives an independent, untuned evaluation such as this one. That bears on what it takes to record a threat as mitigated. The paper does not address product mapping (the generic-to-product half of DEC-009).

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | core | AIT-001; AIT-002 | **AIT-001 (white-box gradient-based crafting):** APGD-CE and targeted APGD-DLR are new white-box attacks, and FAB-T is a white-box minimum-norm attack. Together they find the lowest robust accuracy for most models (§3–§6, Table 2). RPT-0014's catalog already lists S-0952 as an AIT-001 source. **AIT-002 (query-based black-box evasion):** Square Attack is the score-based black-box member of the ensemble, and it is the strongest attack on the MNIST models (§6). All results come from research attacks on published research models; no deployed system is attacked |
| Existing AI threat models | none | — | The paper's "threat model" is a perturbation budget (an l∞ or l2 ball of radius ε, §2). That is an evaluation constraint, not a model of attackers, assets or systems |
| Weakness enumerations | adjacent | NISTAML.022; AML.T0043.000, AML.T0042, AML.T0015; CWE-1039 — **all concept-level, our mapping** | No catalog checked cites this paper: not NIST AI 100-2e2025, not ATLAS release 2026.09 and not CWE-1039 (each checked 2026-11-02). NIST cites RobustBench [97], a benchmark built on AutoAttack, for rigorous evaluation of mitigations. It does so in §2.2, Evasion (NISTAML.022, p. 11), and again in §4.1 (p. 57). The ATLAS ids are concept matches: AML.T0043.000 (White-Box Optimization) for the attacks, AML.T0042 (Verify Attack) for using AutoAttack to test a model, and AML.T0015 (Evade AI Model) |
| Attack → asset mapping | none | — | It maps no attack to assets or components. Our catalog's AIT-001 assigns A03, A12 and C05, but that assignment is not the paper's |

## Implementations

Searched 2026-11-02; licences read from GitHub.

| Name | Kind | License | URL |
|---|---|---|---|
| auto-attack | open source, reference implementation by the authors (named in the paper, §5 footnote 1) | MIT | https://github.com/fra31/auto-attack |
| RobustBench | open source benchmark; its evaluation code imports AutoAttack | MIT for the code; some model-zoo weights carry other licences | https://github.com/RobustBench/robustbench |
| Adversarial Robustness Toolbox (ART) | open source library with an AutoAttack class | MIT | https://github.com/Trusted-AI/adversarial-robustness-toolbox |
| torchattacks | open source PyTorch library with an AutoAttack class | MIT | https://github.com/Harry24k/adversarial-attacks-pytorch |

No commercial product was found that is built specifically on AutoAttack.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | Metadata. `cites` holds the in-scope subset of the references: the attacks AutoAttack combines or builds on, the evaluation-methodology work it answers, and the defences it found most overestimated |
| `summary.md` | This document |

**Reference expansion.** All references were screened, about 60 of them.

*Selection rule:* the same four conditions as before:
1. a primary source on an attack, defence or evaluation in RPT-0014 scope;
2. not in `sources.md`;
3. not in the library;
4. a verified locator.

*Reference-expansion candidates* (3; outcome of the 2026-11-03 review):

| Work | Why | Locator | Outcome |
|---|---|---|---|
| Croce and Hein 2020, FAB: minimally distorted adversarial examples with a fast adaptive boundary attack | One of the four attacks in AutoAttack | PMLR v119 pp. 2196–2205; arXiv:1907.02044 | created: `croce-hein-2020-fab` |
| Mosbach et al. 2018, logit pairing methods can fool gradient-based attacks | Primary evidence that PGD fails and robustness is overestimated (§1) | arXiv:1810.12042 | not created |
| Croce, Rauber and Hein 2019, a scaled-up gradient-free attack reveals overestimated robustness | Same, as an IJCV journal paper | doi:10.1007/s11263-019-01213-0 | not created |

*Further candidates:* six defence papers whose robustness AutoAttack showed was overstated by more than 30 points. All six were excluded on 2026-11-03, because this record already carries the evidence.

| Work | Overstatement | Locator | Outcome |
|---|---|---|---|
| Wang and Zhang 2019, bilateral adversarial training | 39.97 | doi:10.1109/ICCV.2019.00673 | not created |
| Mustafa et al. 2019, restricting the hidden space | 32.04 | doi:10.1109/ICCV.2019.00348 | not created |
| Pang et al. 2020, rethinking softmax cross-entropy | 31.40 | arXiv:1905.10626 | not created |
| Xiao et al. 2020, k-winners-take-all | 33.90 | arXiv:1905.10510 | not created |
| Taghanaki et al. 2019, kernelized manifold mapping | 64.25 | doi:10.1109/CVPR.2019.01160 | not created |
| Pang et al. 2019, promoting ensemble diversity | 30.40 and 32.98 | PMLR v97; arXiv:1901.08846 | not created |

*Not proposed:*
- **Zhang and Xu 2020, adversarial interpolation training** (overstated by 32.25 points): a rejected ICLR submission. OpenReview returned a bot-verification challenge, so its locator was not verified.
- **Already in `sources.md`:** Square Attack S-0078, Madry et al. S-0044, Goodfellow et al. S-0006, Kurakin et al. S-0021, Carlini and Wagner S-0015 and S-0016, Athalye et al. S-0032, Carlini et al. S-0058, and Cohen et al. S-0060.
- **Not proposed for other reasons:** the remaining defence papers, with smaller or no overestimates; the certified-defence background; and software libraries.

Created stubs are `status: stub` with unwritten summaries; tmodel#81 owns filling them. Candidates marked "not created" were excluded in the consolidated review of 2026-11-03 as unnecessary for RPT-0014: niche, or their attack class is already covered.

## Limits

- **Image classifiers and lp-norm budgets only.** All models are CIFAR-10/100, MNIST or ImageNet classifiers attacked within l∞ or l2 balls (§6). The paper says nothing about problem-space attacks, physical attacks, other data types or LLMs.
- **A lower bound, not a guarantee.** AutoAttack's robust accuracy is an upper bound on true robustness. The authors present it as a minimal test, not the final word (§1). On one defence, Square Attack with a larger budget cut robust accuracy from 20.44% to 8.0% (appendix D), so the fixed budget can leave robustness overestimated.
- **The model set depends on author cooperation.** Some models were retrained from released code rather than obtained from the authors, and several authors did not respond (§6, §6.1).
- **Confirmed internal inconsistencies:**
  - The final introduction says AutoAttack beat the reported figures in all except two cases, and mentions a slightly more expensive "AutoAttack+". The abstract, §6 and the tables say all except one, and AutoAttack+ is defined nowhere in the final paper. Both phrases survive from arXiv v1, which did define AutoAttack+.
  - §3.2 says APGD always reaches the lowest robust accuracy in this comparison. The Figure 1 caption says "almost always".
- **Possible reading issue:** in the PMLR main PDF, Greek symbols (α, η, ε) render as blanks under macOS PDFKit, in both the text layer and the rendered page. The supplementary PDF renders them. This may be a property of this renderer, not the file.
- **Numbers that do reconcile:** the 13 models over 10 points and 8 over 30 points need the three appendix models (Table 4) as well as Table 2. With them included, both counts are correct.
