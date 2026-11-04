---
schema: "library-summary/v1"
id: sharif-2016-accessorize-to-a-crime
record: sharif-2016-accessorize-to-a-crime
type: summary
updated: "2026-11-02"
---

# Accessorize to a Crime: Real and Stealthy Attacks on State-of-the-Art Face Recognition

|  |  |
|---|---|
| **Type** | paper |
| **Maturity** | _unset_. A peer-reviewed conference paper; no standing is asserted |
| **Authors** | Mahmood Sharif, Sruti Bhagavatula, Lujo Bauer (Carnegie Mellon University); Michael K. Reiter (University of North Carolina) |
| **Published** | ACM CCS '16, Vienna, 24–28 October 2016: pp. 1528–1540, published 2016-10-24 (Crossref). Proceedings ISBN 978-1-4503-4139-4 |
| **Identifier** | doi:10.1145/2976749.2978392 |
| **Source** | https://users.ece.cmu.edu/~lbauer/papers/2016/ccs2016-face-recognition.pdf. This is the author-hosted copy, linked from co-author Lujo Bauer's CMU publications page. It carries the ACM permission block and DOI. The ACM Digital Library PDF returned HTTP 403 on 2026-11-02, so byte-identity with the ACM copy is not verified |
| **Digest** | `sha256:e70d28a1fb80015315845de20a551896db6a4a2cb2b0d84994f0e7b6c664750b` (4,429,471 bytes, 13 pages, retrieved 2026-11-02; PDF created 2016-10-20). The RPT-0014 manifest has no entry for S-0012 |

## Overview

**The argument.** Attacks on biometric systems matter only when an attacker can carry them out with the means available in the physical world, without drawing attention. A face-recognition attacker controls their appearance, not the digital image (pp. 1–2).

**Method.** The authors optimise the colour pattern of a printed pair of eyeglass frames, which cover about 6.5% of the face image (p. 5). The pattern is made robust to small pose changes, smoothed by total variation, and restricted to colours the printer can reproduce (§4.3).

**Attack goals.** Two goals are pursued (§4.2):
- *dodging:* being misidentified as anyone else;
- *impersonation:* being recognised as a chosen target.

**Results.**
- *Digital, white-box:* against VGG-Face and two transfer-learned variants, almost every attempt succeeds (Table 1).
- *Physical, white-box:* printed frames worn by three of the authors let each dodge recognition and achieve some impersonations (Table 2).
- *Black-box, digital only:* the attack extends to the commercial Face++ API using particle-swarm search (§6, Table 3).
- *Face detection, digital only:* it also evades the Viola–Jones face detector (§7).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | A primary demonstration of physical-world evasion and impersonation against deployed-class face recognition |
| Cryptography | `none` | No cryptographic content |
| This project | `adjacent` | Evidence for the physical and biometric evasion classes in RPT-0014. It shows that the operator's acceptance threshold changes attack success (Table 2), a product-specific factor. It does not address threat modeling |

`bears_on: none yet.` The paper informs no ARCH-0001 decision or requirement directly. It is kept as RPT-0014 evidence.

**Why `summarized` with an empty `bears_on`.** The `summarize` and `ingest-reference` skills suggest that a source bearing on no decision stay a stub. RPT-0014's LANES.md requires full summaries for every subset-1 source, and `docs/scope.md` treats the bears-on test as a prompt for judgement, not a gate. No architectural relevance is claimed to justify the summary.

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | core | AIT-001, AIT-002, AIT-004, AIT-010 | Evidence for each AIT is listed below the table. All attacks are research demonstrations against the authors' own models and a 10-identity Face++ model the authors trained; no attack on a deployed third-party system is reported |
| Existing AI threat models | none | — | §3.1 scopes the paper's own adversary: inference-time only, no poisoning, knowledge of the feature space and, by default, the model. That is experimental scoping, not a reusable threat model |
| Weakness enumerations | adjacent | NISTAML.022; CWE-1039; AML.T0043.000, AML.T0043.001, AML.T0041, AML.T0015 | The paper defines no enumeration. **Verified:** NIST AI 100-2e2025 cites it as [332] for physically realizable attacks (§2.2.1, p. 13). **Concept-level only, our mapping:** CWE-1039, which does not cite this paper; and the ATLAS ids, confirmed to exist in ATLAS release 2026.09 (2026-11-02), which also does not cite it |
| Attack → asset mapping | adjacent | A12, A15; C05, C13, C16; TB11 — **assigned by us** | The paper names what the attacks target: face-recognition access control to laptops and phones, surveillance, and law enforcement (p. 2), all fed by cameras the attacker cannot control (p. 1). It gives no asset model. The ids are our assignment onto RPT-0014's preliminary vocabularies: A15 (human identity) and A12 (downstream decisions); C16 (camera), C05 (the model), C13 (the Face++ cloud API); TB11 (physical world into sensors) |

**Evidence for each linked AIT:**
- AIT-001: white-box gradient descent on the input (§4.2, Table 1).
- AIT-004: printed physical frames (§5.2, Table 2, Fig. 4).
- AIT-010: biometric impersonation and dodging of face recognition, and evasion of face detection (§5, §7).
- AIT-002: score-based black-box queries against Face++, which returns its top three classes with confidence scores (§6, Table 3).

**Key results:**
- *Digital eyeglass attacks (Table 1):* 100% success, except 91.67% for impersonation against the 2,622-identity VGG-Face model.
- *Physical dodging (Table 2):* 97.22–100% success, except one subject (S_C) against DNN_B. That subject failed completely with the standard frames and reached 80% only with frames enlarged to 10% of the image (p. 8, Fig. 5).
- *Physical impersonation (Table 2):* 87.87–100% for four of the six subject–target pairs, but only 16.13% and 16.22% for the other two.
- *Under an operating threshold* (0.85 for DNN_B, 0.90 for DNN_C), success falls, for example to 48.48% for one pair, and to 0% for the two weakest pairs (Table 2).
- *Face++:* all four impersonation pairs succeeded, averaging 25–134 queries (Table 3).
- *Viola–Jones:* 19 of 20 images evaded detection with perturbation alone, and 20 of 20 with accessories plus perturbation (§7.2).
- *Cost:* printing one frame costs about $0.22 (p. 7). One optimization step takes about 53 seconds on a laptop, and a full 300-step run about 4.4 hours (p. 9).

## Implementations

Searched 2026-11-02. The paper releases no code. It names MatConvNet as the toolbox used (p. 4) and Face++ as the system attacked (§6.1); neither is an implementation of the attack.

| Name | Kind | License | URL |
|---|---|---|---|

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | Metadata. `cites` holds the in-scope subset of the 46 references plus the three systems attacked. S-0003 and the ten stubs below are cited by record id |
| `summary.md` | This document |

**Reference expansion.** All 46 references were reviewed.

*Selection rule:* a reference is proposed as a stub only if all four hold:
1. it is a primary source on an attack, defence or evaluation in RPT-0014's scope;
2. it is not already in `sources.md`;
3. it is not already in the library;
4. its locator was verified.

*Reference-expansion stubs* (10). Each was created with `bin/ingest --stub` under tmodel#81. Bibliographic fields were checked on 2026-11-02, against Crossref for the eight with DOIs, and against the sources named in the last two rows. They are `status: stub` and have not been read. Their `summary.md` files are unwritten scaffolds, and filling them is deferred to a later tmodel#81 pass:

| Ref | Record | Work | Locator |
|---|---|---|---|
| [7] | `erdogmus-2013-3d-mask-spoofing` | Erdogmus and Marcel 2013, 3D-mask face spoofing | doi:10.1109/BTAS.2013.6712688 |
| [10] | `feng-2013-fashion-camouflage` | Feng and Prabhakaran 2013, fashion camouflage | doi:10.1145/2502081.2502121 |
| [12] | `galbally-2010-hill-climbing-face` | Galbally et al. 2010, hill-climbing attacks on face verification | doi:10.1016/j.patcog.2009.08.022 |
| [22] | `li-2014-osn-facial-disclosure` | Li et al. 2014, social-network photos against face authentication | doi:10.1145/2590296.2590315 |
| [23] | `liang-2016-cracking-classifiers-evasion` | Liang et al. 2016, evasion of Google's phishing-page filter | doi:10.1145/2872427.2883060 |
| [32] | `papernot-2016-defensive-distillation` | Papernot et al. 2016, defensive distillation | doi:10.1109/SP.2016.41 |
| [35] | `srndic-2014-practical-evasion` | Šrndić and Laskov 2014, practical evasion of PDF-malware classifiers | doi:10.1109/SP.2014.20 |
| [44] | `yamada-2013-privacy-visor` | Yamada et al. 2013, Privacy Visor | doi:10.1109/SMC.2013.271 |
| [9] | `fawzi-2015-fundamental-limits-adversarial-robustness` | Fawzi, Fawzi and Frossard 2015, an ICML 2015 workshop paper. The title on the PDF matches the printed citation exactly | EPFL Infoscience handle 20.500.14299/122125 |
| [43] | `wittel-2004-attacking-statistical-spam-filters` | Wittel and Wu 2004, attacks on statistical spam filters | CEAS 2004 accepted-papers list; the conference-hosted PDF as archived on 2004-12-21 |

*In scope, kept as a `cites` entry only, with no record created:*
- [14] Harvey 2010, CV Dazzle, a master's thesis. The printed URL now leads to the artist's project page; no catalogued thesis was found, so there is no reliable locator.

*Excluded because already in `sources.md`:* [5] (S-0008), [11] (S-0005), [13] (S-0006), [31] (S-0010) and [39] (S-0003, now this library's `szegedy-2013-intriguing-properties`).

*Excluded as out of scope:* architectures, datasets, optimizers, product pages, a policy survey [18], a human–robot overtrust study [36], and the attacked systems themselves ([25], [33], [42]), which are cited for context only.

## Limits

- **A very small, controlled physical study.**
  - Three subjects, all authors, photographed in a windowless room with neutral expressions and only slight pose changes (§5.2).
  - The authors say outdoor or street surveillance conditions are untested (§8).
- **Inconspicuousness is asserted, not measured.** There was no human-subject study (§8). The enlarged frames used for one subject are explicitly less inconspicuous (p. 8).
- **The black-box and face-detection results are digital only.**
  - The Face++ attack was not physically realized, and it targets a 10-identity model the authors trained themselves (§6).
  - The Viola–Jones evasion's physical realizability is deferred to future work (§7).
- **The white-box results depend on model access.** DNN_B and DNN_C reuse VGG-Face's first 37 layers through transfer learning (§4.1), so the white-box setting includes full knowledge of the shared layers.
- **Defences are not evaluated.** An attribute-based classifier is proposed as future work (§8).
- **Confirmed internal inconsistencies:**
  - p. 8 gives the mean target probability for S_C impersonating Carson Daly as 0.99; Table 2 gives 0.90.
  - The introduction says frames let all three subjects dodge at least 80% of the time (p. 2). Table 2 and p. 8 show that one subject needed enlarged frames for that, and failed completely with the standard ones.
  - Reference [31] is printed as Euro S&P 2015; its DOI (10.1109/EuroSP.2016.36) and `sources.md` S-0010 place it at EuroS&P 2016.
- **Possible discrepancy:** frame coverage is given as about 6.5% of pixels (p. 5) but as 6% in the Table 2 caption, probably rounding.
- **Unverified links.** Image-credit and frame-design links use `goo.gl` short links (pp. 5–9); they were not checked individually.
