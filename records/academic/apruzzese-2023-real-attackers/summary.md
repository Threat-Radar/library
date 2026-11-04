---
schema: "library-summary/v1"
id: apruzzese-2023-real-attackers
record: apruzzese-2023-real-attackers
type: summary
updated: "2026-11-02"
---

# "Real Attackers Don't Compute Gradients": Bridging the Gap Between Adversarial ML Research and Practice

|  |  |
|---|---|
| **Type** | paper (a position paper with case studies and a literature review) |
| **Maturity** | _unset_. A peer-reviewed conference paper; no standing is asserted |
| **Authors** | Giovanni Apruzzese (University of Liechtenstein), Hyrum S. Anderson (Robust Intelligence), Savino Dambra (Norton Research Group), David Freeman (Meta), Fabio Pierazzi (King's College London), Kevin Roundy (Norton Research Group) |
| **Published** | IEEE SaTML 2023, Raleigh, NC, 8–10 February 2023, pp. 339–364 (Crossref, issued 2023-02). arXiv v1 2022-12-29 is the only arXiv version |
| **Identifier** | doi:10.1109/SaTML54575.2023.00031; arXiv:2212.14315 |
| **Source** | https://arxiv.org/pdf/2212.14315v1. The IEEE PDF was not obtained. The authors' SaTML copy (real-gradients.github.io, digest `c023dcd7…`) has the same text, apart from the arXiv stamp, two one-word edits and the symbol encoding in Table IV. Both have 26 pages, matching the IEEE page range |
| **Digest** | `sha256:c946a01f8d97aadd801294e87f98b855b911898be296b79994ec81ebdf8a640c` (1,626,079 bytes, 26 pages, retrieved 2026-11-02). The RPT-0014 manifest has no entry for S-0685 |

## Overview

**The argument.** Adversarial-ML research and security practice have drifted apart. Researchers study one model and gradient-based perturbations. Practitioners defend whole ML systems against economically motivated attackers who mostly use cheap tricks, so they rank adversarial-ML defences low (§I, §II). The paper's thesis is that research would matter more in practice if threat models covered the entire system and counted costs.

**Evidence.** The paper offers three original case studies, a fourth in an appendix, and a literature review.
- *Facebook's abuse-fighting funnel (§III-A, Fig. 3):* an attacker must pass four layers (automation, access, activity, application) before any content classifier is reached. A blocked attacker cannot tell which layer stopped them.
- *A commercial phishing detector's logs (§III-B, Table II, Fig. 4):* July 2022, a vendor's image-classifier ensemble. The authors reviewed 4,600 of 9,174 pages the detector was uncertain about, stopping once they had 100 pages they judged possibly adversarial. Those pages used simple tricks such as styling the company name, blurring, cropping or replacing the logo. None looked gradient-derived, but the authors say they cannot prove it.
- *The MLSEC 2021 anti-phishing competition (§III-C, Fig. 5):* query counts alone misjudge attack cost. The winner used the fewest queries but two people and 42 days; the third-placed entrant used one person and 12 days.
- *The MLSEC 2020 malware competition (App. A-D):* the winning attack simply embedded the malware payload in another binary, and evaded every detector.
- *Literature review (§IV, App. B, Table IV):* all 88 adversarial-ML papers at the four top security venues in 2019–2021. 89% consider only deep learning and 63% evaluate on images. About 80% attack a single model rather than a pipeline, only 20% test a real deployed system, 27% never mention cost and 51% release code. Threat-model terms such as "white-box", "black-box" and "access" are used inconsistently (§IV-D).

**Positions (§V).** Four positions follow:
- threat models must define the attacker's goal, knowledge, capabilities and strategy against every component of the ML system;
- threat models must include cost-driven assessments for both attacker and defender (Fig. 6: attack likelihood from benefit and cost, risk from likelihood and damage, deploy a countermeasure only if its cost suits the risk);
- industry and academia must collaborate;
- source-code disclosure should be encouraged through a "just culture" rather than a culture of blame.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Primary practitioner evidence on how deployed ML systems are actually evaded, and a critique of how adversarial-ML threat models are written |
| Cryptography | `none` | No cryptographic content |
| This project | `core` | A method for writing AI threat models: system-wide attacker elements, cost-driven likelihood and risk, and a countermeasure decision. RPT-0014 already lists it as TM-023. It bears on two ARCH-0001 items, below |

**What it bears on.**
- **R-011 / DEC-003 (risk metric).** The paper wants likelihood derived from attacker benefit and cost, risk from likelihood and damage (Fig. 6), and attacker cost to include human time and expertise, not only queries (§III-C, §V-B). That speaks to how a feasibility-based risk metric should weigh attacker effort.
- **R-020 / DEC-009, the generic-to-product half only.** The paper argues that a generic attack on a model behaves differently once the model sits inside a product's pipeline, layers and response logic (§III-A, §V-A). Mapping a generic threat onto a specific product is that problem. The mitigation-lifecycle half of DEC-009 is not addressed.

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | core | AIT-007; AIT-002 | **AIT-007 (problem-space evasion of security classifiers):** primary evidence from production logs of a commercial phishing detector (§III-B, Table II, Fig. 4), and the two MLSEC competitions (§III-C, App. A-D). RPT-0014's catalog already lists S-0685 as an AIT-007 source. **AIT-002 (query-based black-box evasion):** secondary evidence. MLSEC 2021 contestants queried seven closed detectors that returned a probability, and the winners were ranked by query count (§III-C). The two MLSEC cases are competitions, not attacks on deployed products |
| Existing AI threat models | core | TM-023 | RPT-0014's TM-023 is this paper. It proposes extending the goal, knowledge, capability and strategy elements to every component of the ML system (§V-A), cost-driven threat modeling (Fig. 6) and stricter terminology (§V-A). It also audits the threat models of 88 papers (App. B-H). It is a method, not a machine-readable catalog |
| Weakness enumerations | adjacent | AML.CS0032 (with AML.T0015, AML.T0043.003, AML.T0048.003, AML.T0052); NISTAML.022; NISTAML.025; CWE-1039 | The paper defines no enumeration. **Verified:** ATLAS release 2026.09 (checked 2026-11-02) cites this paper as ref-1 of case study AML.CS0032, which uses AML.T0015, AML.T0043.003, AML.T0048.003 and AML.T0052. NIST AI 100-2e2025 cites it as [17] in §2.2.4, real-world evasion attacks (p. 16), within the evasion section NISTAML.022. **Concept-level only, our mapping:** NISTAML.025 (black-box evasion, which `sources.md` lists), and CWE-1039, which does not cite it. **Where both catalogs go beyond the paper** is listed under Limits |
| Attack → asset mapping | adjacent | A16; C01, C05, C17 — **assigned by us** | The paper argues that attacks must be mapped to every component of the ML system (Fig. 1: input, preprocessing, model, post-processing; Fig. 3: the four-layer funnel). It does not map attacks to assets. Our ids: A16 (security detection: the phishing, spam and malware detectors attacked); C01 (attacker-supplied content arriving from outside); C05 (the models); C17 (security tooling acting on the verdicts) |

## Implementations

Searched 2026-11-02. The paper ships no attack or defence tool. Its website, real-gradients.github.io, releases supporting material: screenshots of the 100 evasive phishing pages, a notebook with data for the MLSEC 2021 analysis, the submissions, and a list of the 43 excluded papers. These are research artifacts, not something to build on.

| Name | Kind | License | URL |
|---|---|---|---|

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | Metadata. `cites` holds the in-scope subset of the 197 references: those the paper uses as evidence, the sources of its case studies, and the proposed stubs below. Two are cited by record id |
| `summary.md` | This document |

**Reference expansion.** All 197 references were screened.

*Selection rule:* the same rule as Batch 1. A reference is a candidate only if all four hold:
1. it is a primary source on an attack, defence or evaluation in RPT-0014 scope;
2. it is not in `sources.md`;
3. it is not in the library;
4. its locator was verified.

This paper adds a fifth rule. Only references it uses as evidence in its argument (§II–§V and Appendix A) are candidates. Papers that appear only as data points in the Table IV survey are not proposed.

*Reference-expansion candidates* (20; locators checked on 2026-11-02 against Crossref, arXiv or the USENIX paper page). After the consolidated review on 2026-11-03, 9 were created as stubs and 11 were not:

| Ref | Work | Locator | Outcome |
|---|---|---|---|
| [10] | Apruzzese et al. 2022, adversarial examples against 5G network ML | doi:10.1109/TNSM.2022.3188930 | not created |
| [12] | Tramèr et al. 2019, AdVersarial: attacks on perceptual ad blocking | doi:10.1145/3319535.3354222 | created: `tramer-2019-adversarial-ad-blocking` |
| [22] | Xiao et al. 2019, camouflage attacks on image scaling | usenix.org, usenixsecurity19/presentation/xiao | created: `xiao-2019-image-scaling-camouflage` |
| [32] | Pajola and Conti 2021, simple evasion of text-based MLaaS | doi:10.1109/EuroSP51992.2021.00023 | created: `pajola-2021-fall-of-giants` |
| [42] | Apruzzese et al. 2022, realistic threat models for attacks on network intrusion detection | doi:10.1145/3469659 | created: `apruzzese-2022-realistic-nids-attacks` |
| [44] | Demontis et al. 2019, why adversarial attacks transfer | usenix.org, usenixsecurity19/presentation/demontis; arXiv:1809.02861 | not created |
| [50] | Li, Guo and Chen 2020, no-box adversarial attacks | arXiv:2012.02525 | not created |
| [66] | Gilmer et al. 2018, the rules of the game for adversarial-example research (the closest prior position paper, §II-D) | arXiv:1807.06732 | created: `gilmer-2018-rules-of-the-game` |
| [82] | Shan et al. 2022, poison forensics | usenix.org, usenixsecurity22/presentation/shan; arXiv:2110.06904 | created: `shan-2022-poison-forensics` |
| [83] | Shan et al. 2022, post-breach recovery for leaked models | doi:10.1145/3548606.3560561 | not created |
| [89] | Nasr et al. 2021, blind adversarial perturbations against network traffic analysis | usenix.org, usenixsecurity21/presentation/nasr | not created |
| [91] | Chen et al. 2021, attacks on speaker recognition | doi:10.1109/SP40001.2021.00004 | created: `chen-2021-real-bob` |
| [92] | Zheng et al. 2021, black-box attacks on commercial speech platforms | doi:10.1145/3460120.3485383 | created: `zheng-2021-commercial-speech-platforms` |
| [112] | Rakin et al. 2021, Deep-Dup weight duplication on multi-tenant FPGAs | usenix.org, usenixsecurity21/presentation/rakin; arXiv:2011.03006 | not created |
| [132] | Ling et al. 2019, DEEPSEC evaluation platform | doi:10.1109/SP.2019.00023 | not created |
| [133] | Carlini 2019, a critique of DEEPSEC | arXiv:1905.07112 | not created |
| [134] | Pintor et al. 2022, indicators of attack failure | doi:10.52202/068431-1676 | not created |
| [139] | Quiring et al. 2020, the winning defence in the MLSEC 2020 malware competition | arXiv:2010.09569 | not created |
| [140] | Ceschin et al. 2020, the winning attack in the MLSEC 2020 malware competition | doi:10.1145/3433667.3433669 | created: `ceschin-2020-mlsec-xor-evasion` |
| [150] | Lovisotto et al. 2021, SLAP short-lived physical perturbations | arXiv:2007.04137 | not created |

*Already held, cited by record id:* [38] `szegedy-2013-intriguing-properties` and [43] `srndic-2014-practical-evasion`.

*Excluded because already in `sources.md`:* [3] S-0675, [13] S-0058, [25] S-0095, [28] S-0125, [39] S-0672, [40] S-0002, [45] S-0013, [47] S-0001, [48] S-0026, [49] S-0098, [52] S-0076, [95] S-0110, [107] S-0089, [110] S-0062 and [111] S-0054. Each match was checked in `sources.md` itself.

*Not proposed:*
- **Web pages for the MLSEC case studies ([84]–[87]):** kept as `cites` entries with their printed URLs, which were not checked.
- **Table IV survey data points:** the remaining papers among the 88.
- **Out of scope:** practitioner surveys and interview studies, economics and risk-management literature, ML background, and software-engineering references.

Created stubs are `status: stub` with unwritten summaries; tmodel#81 owns filling them. Candidates marked "not created" were excluded in the consolidated review of 2026-11-03 as unnecessary for RPT-0014: niche, or their attack class is already covered.

## Limits

- **Thin quantitative evidence for the headline claim.**
  - The phishing case study is a judgement study: two authors stopped reviewing after finding 100 pages they thought could be adversarial, from one vendor, one month and the 40 most-targeted domains (§III-B).
  - The authors say they cannot prove whether any page was gradient-derived (§III-B, §VI).
  - The title is therefore a hypothesis the paper does not test.
- **Competitions, not deployments.** The MLSEC results (§III-C, App. A-D) come from contestants, most of them security enthusiasts, attacking competition detectors. The human-effort reading of Fig. 5 is the authors' inference from submission timestamps (App. A-C).
- **Two catalogs overstate the case study:**
  - ATLAS AML.CS0032 says the logo-edited pages evaded the brand-impersonation model but that other components flagged them. The paper says only that these pages left the system uncertain and went to manual triage (§III-B, Table II caption). It does not say whether other components flagged them.
  - NIST AI 100-2e2025 (p. 16) says the authors identified 100 adversarial examples among 4,600 uncertain samples. The paper found 100 possible adversarial examples by judgement, in 4,600 of 9,174 uncertain samples, and does not confirm that any is one.
- **Confirmed defects:**
  - §V-B points to "Fig. 9" for the cost-driven threat-modeling overview (p. 11), but that figure is Fig. 6. Fig. 9 is the G4 cost chart in Appendix B.
  - The Table IV key labels the output and training-data questions "T11" instead of T3 and T4. It also says "the answer to T2 is 'poisoning'", where the attack family is question G2 (p. 25).
  - Reference [38] cites Szegedy et al. as ICML 2013. The paper appeared at ICLR 2014 (record `szegedy-2013-intriguing-properties`).
- **Possible discrepancies** (we could not reproduce the arithmetic):
  - The winning MLSEC 2021 team is said to have needed an "8x increase in absolute time" over the third-placed entrant (p. 7). The stated figures give 3.5x in calendar days (42 against 12), or 7x in person-days (84 against 12).
  - App. A-C says the second-placed team took "at least 19 days", but its first and last submissions are on days 31 and 41.
  - The share of attack papers is 72% in §IV-A and 75% in App. B-C. Our count of Table IV gives 64 of 88, or 72.7%.
  - Deep-learning-only papers are 89% in §I and §IV-A, and 90% in §V-C.
- **A narrow venue sample.** The review covers four security venues for 2019–2021, and excludes workshops. 43 candidate papers were left out, among them work on federated learning, secure computation and high-level analyses (App. B-A). Machine-learning venues are not covered.
- **Facebook's architecture is described, not evaluated.** The funnel (§III-A) is an account by one of its practitioners, with no data on how often each layer stops attackers.
