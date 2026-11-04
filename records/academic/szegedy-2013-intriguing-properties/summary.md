---
schema: "library-summary/v1"
id: szegedy-2013-intriguing-properties
record: szegedy-2013-intriguing-properties
type: summary
updated: "2026-11-03"
---

# Intriguing properties of neural networks

|  |  |
|---|---|
| **Type** | paper |
| **Maturity** | _unset_. A peer-reviewed conference paper; the RFC 2026 scale does not apply and no standing is asserted |
| **Authors** | Christian Szegedy (Google), Wojciech Zaremba (NYU), Ilya Sutskever (Google), Joan Bruna (NYU), Dumitru Erhan (Google), Ian Goodfellow (Université de Montréal), Rob Fergus (NYU and Facebook) |
| **Published** | ICLR 2014, listed in the ICLR 2014 conference proceedings at iclr.cc (checked 2026-11-02). arXiv v1 2013-12-21, v4 2014-02-19 |
| **Identifier** | arXiv:1312.6199 |
| **Source** | https://arxiv.org/pdf/1312.6199v4 |
| **Digest** | `sha256:c4e3bd872ef20b7d2c4d77a63cd8f37cb8ff518609ae09acaf0fd5dd9e76c54c` (6,565,323 bytes, 10 pages, retrieved 2026-11-02; matches the RPT-0014 `pdf-manifest.tsv` entry for S-0003, whose unversioned URL currently serves v4) |

## Overview

The paper reports two counter-intuitive properties of deep networks.

**Units carry no special meaning (§3).** Random directions in a layer's activation space are as semantically interpretable as individual units (Figs. 1–4). The meaning therefore lives in the space, not in single neurons.

**Adversarial examples (§4).** This is the property that matters for security. The authors find tiny, deliberately computed perturbations of correctly classified images that make the network misclassify them. They name these "adversarial examples".
- *Method:* the perturbation is the smallest input change that forces a chosen target label, found with box-constrained L-BFGS (§4.1).
- *Coverage:* such examples were found for every network studied: MNIST models, AlexNet and QuocNet (Figs. 5–7).
- *Transfer:* examples made for one model also fool models with different hyperparameters (Table 2), and models trained on a disjoint half of MNIST (Tables 3–4).

**Interpretation and next steps.** The authors read this as evidence of dense "blind spots" in the learned input–output mapping (§5). They give per-layer Lipschitz upper bounds as a measure of instability (§4.3, Table 5). They also report that feeding adversarial examples back into training reduced MNIST test error, an early form of adversarial training (pp. 5–6).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | The primary source for adversarial examples and their transferability: evasion of ML at inference time |
| Cryptography | `none` | No cryptographic content |
| This project | `adjacent` | Foundational evidence for the evasion attack class in RPT-0014. The paper does not address threat modeling, products or risk |

`bears_on: none yet.` The paper informs no ARCH-0001 decision or requirement directly. It is kept as RPT-0014 evidence. It is the work CWE cites for CWE-1039 (REF-16), but a mapping to CWE would be our inference, not the paper's claim.

**Why `summarized` with an empty `bears_on`.** The `summarize` and `ingest-reference` skills suggest that a source bearing on no decision stay a stub. RPT-0014's LANES.md requires full summaries for every subset-1 source, and `docs/scope.md` treats the bears-on test as a prompt for judgement, not a gate. No architectural relevance is claimed to justify the summary.

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | core | AIT-001, AIT-003 | It defines and demonstrates white-box, optimization-based adversarial examples (§4.1, Figs. 5–7), which is AIT-001. It shows they transfer across models and disjoint training sets (Tables 2, 4), the basis of AIT-003. It is research only: no deployed system is attacked |
| Existing AI threat models | none | — | No threat model. The attacker is implicitly white-box with full gradient access, but this is never stated as a threat model |
| Weakness enumerations | adjacent | CWE-1039; NISTAML.022; AML.T0043, AML.T0043.000, AML.T0043.002, AML.T0015 | The paper defines no enumeration, but it is the cited evidence for one weakness entry. **Verified:** CWE-1039, CWE 5.0 (2026-11-02), lists it as REF-16; NIST AI 100-2e2025 cites it as [362] for evasion (§2.2, pp. 11–12). **Concept-level only, our mapping:** the ATLAS ids, confirmed to exist in ATLAS release 2026.09 (2026-11-02); ATLAS does not cite this paper |
| Attack → asset mapping | none | — | It maps no attack to assets or components. Our catalog's AIT-001 assigns A03, A12 and C05, but that assignment is not the paper's |

## Implementations

Searched 2026-11-02. The paper ships no code. The full-resolution adversarial images it points to (a `goo.gl` link on pp. 5–6) are gone: the short link now resolves to a retired Google+ photo album, and following the redirect ends on an unrelated Google blog page. Later attack libraries reimplement this attack, but the paper names none.

| Name | Kind | License | URL |
|---|---|---|---|

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | Metadata. `cites` lists only the four models and datasets the paper attacks or uses |
| `summary.md` | This document |

**Reference expansion.** All 13 references were reviewed. None is a source on attacks, AI threat models or weakness catalogs: they are deep-learning architectures, datasets, feature visualization and word embeddings. No stub records are proposed.

## Limits

- **Small, dated test bed.**
  - The quantitative transfer results cover only non-convolutional MNIST models (Tables 1–4).
  - For convolutional networks the authors say they have no MNIST results yet, and give only qualitative AlexNet examples (p. 6).
  - QuocNet is tested only as a binary car classifier on frozen features (Fig. 6).
- **Transfer is weaker than the prose suggests.**
  - Cross-model error at the original distortion ranges from 2% to 87.1% (Table 2).
  - Transfer from the linear (softmax) models to the two sigmoid networks depends on the source model (Table 2). Examples crafted on FC10(10⁻⁴) fool FC100-100-10 and FC200-200-10 only 2% and 3.9% of the time. Those crafted on FC10(10⁻²) fool them 35.9% and 27.3% of the time, and those on FC10(1) 48.1% and 47%. These two models' examples are also larger: average distortion 0.1 and 0.14, against 0.062 for FC10(10⁻⁴).
  - Across the disjoint training sets the effect drops to 5.1–8.2% (Table 4). From the two P₁ models to the P₂ model it is 5.9% and 5.1%; from the P₂ model to each P₁ model it is 8.2%. Gaussian noise of similar size causes 2.2–2.6%. After the authors amplify the perturbations to stddev 0.1, by what they call about 40% (p. 8), it rises to 22–50%: 43% and 22% from P₁ to P₂, and 27% and 50% from P₂ to P₁. Gaussian noise at stddev 0.1 causes 2.6–2.8%.
  - The prose concedes a considerable drop, but its headline is that examples generalize.
- **The noise comparison is overstated.** On p. 7 the text says Gaussian noise of standard deviation 0.1 exceeds the adversarial noise for every model except one. Table 2's distortion column shows two models at or above 0.1 (FC10(10⁻²) at 0.1 and FC10(1) at 0.14).
- **Typographical ambiguity.** On p. 8 the prime that distinguishes the P₂-trained network `FC100-100-10'` is dropped in the prose, which reads "Models FC100-100-10 and FC100-100-10". Table 3 keeps the prime.
- **The defence is preliminary.** Adversarial training is reported for one MNIST network and is not compared systematically (pp. 5–6). The Lipschitz bounds are upper bounds only; large bounds do not prove that adversarial examples exist (§4.3).
- **No threat model or deployment setting.** The attack needs full white-box gradient access. It is not shown physically or through an API.
