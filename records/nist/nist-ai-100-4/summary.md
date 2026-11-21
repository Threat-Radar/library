---
schema: "library-summary/v1"
id: nist-ai-100-4
record: nist-ai-100-4
type: summary
updated: "2026-11-20"
lane: catalogs-schema
reviewed_by: ""
---

# NIST AI 100-4: Reducing Risks Posed by Synthetic Content

|  |  |
|---|---|
| **Type** | spec (a NIST AI report; **stub**: summarized for WAVE 1, not FX-1 extracted) |
| **Maturity** | informational |
| **Authors** | National Institute of Standards and Technology |
| **Published** | November 2024 (approved by the NIST Editorial Review Board 2024-11-18) |
| **Identifier** | NIST AI 100-4; DOI 10.6028/NIST.AI.100-4 |
| **Source** | https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-4.pdf |
| **Digest** | `a387a4977db70d65cdbc178c8b0cb8aa5dedb85fa80d6f473c244e2767a4fd54` (81 pages; matches `pdf-manifest.tsv`) |

## Overview

An overview, written under Executive Order 14110, of technical approaches to **digital content transparency**: recording and revealing where content came from, labelling and detecting AI-generated content, and limiting AI-generated child sexual abuse material (CSAM) and non-consensual intimate imagery (NCII). It frames harms along a pipeline of creation, publication and consumption. Most measures act at creation and consumption.

**The main sections:**
- **Provenance tracking (§3.1).** Covert and overt watermarking for images, video, audio and text, and metadata recording with digital signatures (C2PA manifests, IPTC, EXIF, XMP).
- **Synthetic content detection (§3.2).** Detection from provenance signals, automated content-based classifiers, and human-assisted detection, each discussed by modality.
- **Labels and user perception (§3.3).**
- **Testing and evaluation (§4).**
- **CSAM and NCII safeguards (§5).** Filtering training data, inputs and outputs, hashing confirmed material, provenance tracking, and red-teaming.
- **Mapping to the AI RMF lifecycle (§6).**

The appendices list current standards, tools and detection methods.

**On security (§3.1.1.3 and §3.2).** NIST is explicit about the weaknesses:
- **Scrubbing.** Overt watermarks "can easily be edited out", and covert ones are often straightforward to remove too.
- **Paraphrasing.** A second model can paraphrase text and remove a text watermark "with only minor degradation", and targeted paraphrasing works even on long texts. Theoretical results show any text watermark can in principle be defeated.
- **Audio.** Audio watermarks are robust to perturbations they were trained on, but "not secure against adversarial perturbation".
- **Spoofing.** Adversaries can also forge a watermark, which undermines trust in genuine marks.
- **Detectors** can be evaded or optimized against, and they show bias.

The conclusion is that "none of these techniques can be considered as a comprehensive solution" and that they work only alongside social measures. Many approaches "may be years away from widespread deployment on mobile devices".

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | The control layer for AI-enabled impersonation, fraud and abuse imagery, with the attacks on those controls stated plainly |
| Cryptography | adjacent | Signed metadata (C2PA, FIPS 186-5), perceptual and cryptographic hashing, and cryptographic watermarks, described but not specified |
| This project | adjacent | Mitigations, and their weaknesses, for threats against content-integrity and identity assets (**DEC-001**: Mitigation and its evidence). It has no object model of its own |

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | core | AIT-118, AIT-120, AIT-127, AIT-129 | AIT-118 (watermark and detector removal or spoofing) cites it. Its scrubbing, paraphrasing, spoofing and detector-evasion passages are the control-side evidence for deepfake impersonation (AIT-127) and election deepfakes (AIT-129). §5's hashing of confirmed CSAM is the control that AIT-120's perceptual-hash collisions attack. It reports no incidents of its own beyond news cited in §5 |
| Existing AI threat models | adjacent | — | The creation, publication and consumption pipeline, with actors at each stage, is a harm model for synthetic content, not a system threat model |
| Weakness enumerations | adjacent | AML.T0088; NISTAML.04 | The mapping is `sources.md`'s ("AML.T0088 Generate Deepfakes?"); the report cites no catalog ids. **`sources.md` read only the front matter and contents;** the security findings above come from the body |
| Attack → asset mapping | adjacent | C12, C17, C13; A13, A15, A17, A18 | Deepfakes target people (C12) and downstream consumers and platforms (C17), through third-party generators (C13). The assets are reputation and content provenance (A13), human identity (A15), user safety (A17) and the people depicted (A18). The mapping is ours |

## Implementations

The report's Appendix B lists tools, among them C2PA tooling and SDKs, IPTC metadata, and watermarking such as Google DeepMind's SynthID. It endorses none. This record lists none separately (searched 2026-11-20); C2PA is the library's `c2pa-2-4`.

| Name | Kind | License | URL |
|---|---|---|---|

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, digest and `cites` |
| `summary.md` | this summary, with the RPT-0014 applicability table |

## Reference expansion

The bibliography is arranged by section and repeats entries. It has 148 entries, about 133 distinct works, checked against `sources.md` and the library on 2026-11-20. RPT-0014 is about attacks, so a watermarking or detection paper is in scope when it is about the **security** of these controls: an attack, a robustness benchmark, an impossibility result or a detector failure.
- **In `sources.md` (15):** S-0151, S-0164, S-0171, S-0175, S-0197, S-0208, S-0276, S-0279, S-0280, S-0300, S-0311, S-0354, S-0356, S-0783 and S-0858 (C2PA, also the library's `c2pa-2-4`).
- **In the library only (1):** FIPS 186-5 (`fips-186-5`), which is general cryptography.
- **Missing, added as stubs (15):**
  - 11 papers:
    - limits of AI-text detection (Chakraborty; Ghosal's survey);
    - undetectable LLM watermarks;
    - AudioMarkBench;
    - color-aware watermark bypass;
    - open challenges in synthetic-speech detection;
    - flawed human heuristics;
    - detector bias against non-native writers;
    - CNN-image detectability;
    - adversarial-robustness evaluation;
    - LM detectors "easily optimized against", from a Wayback copy of the ICLR PDF.
  - 4 incident reports: the Taylor Swift deepfakes, AI-generated abuse imagery, the FBI's sextortion alert, and the Stanford finding of abuse images in a training set.
- **Missing, in scope, not stubbed (2):** Quiring et al., *Adversarial ML against digital watermarking* (EUSIPCO 2018), and RevHashNet (2018). Neither has an open copy to pin.
- **Out of scope (100):**
  - 37 papers that only propose a watermark or detector method, without a security evaluation. This report is the record for that engineering;
  - 63 other references: standards and specifications (C2PA harms modelling, ISO, IPTC, EXIF, S/MIME, FIPS-related), US policy, vendor and tool pages, explainers, a perception study of labels, CSAM and NCII statistics and support services, and non-AI image, signature and hashing security.

## Limits

- **A stub for FX-1.** It is a `spec`, so moving it past stub needs full extraction. It is mostly a survey, with no normative requirements.
- **Written for EO 14110.** That order was revoked in January 2025. The report's technical content stands, but its policy framing is dated.
- **An overview, not an evaluation.** It says "the efficacy of many of these technical approaches are not fully examined yet". Its security claims summarize the literature rather than test anything.
- **Detection is fragile by design.** Its own sources show watermarks being removed and forged, and detectors being evaded. Its recommendation is defense in depth, not any one control.
