---
schema: "library-summary/v1"
id: gdm-fsf-v3-2025
record: gdm-fsf-v3-2025
type: summary
updated: "2026-11-13"
lane: catalogs-schema
reviewed_by: ""
---

# Frontier Safety Framework, Version 3.0

|  |  |
|---|---|
| **Type** | article (company framework) |
| **Maturity** | _unset — do not guess_ |
| **Authors** | Google DeepMind |
| **Published** | Version 3.0, 2025-09-22; 16 pages |
| **Identifier** | none (PDF on Google DeepMind's storage) |
| **Source** | https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/strengthening-our-frontier-safety-framework/frontier-safety-framework_3.pdf |
| **Digest** | `87ebf40b747b98468226b2198442b45ff54854975f6e9882d9ece2d009082fe5` (matches `sources.md` S-0805) |

## Overview

Google DeepMind's framework for severe risks from frontier models. It is built on **Critical Capability Levels (CCLs)** in three sets:
- **misuse:** CBRN, cyber and harmful manipulation;
- **machine-learning R&D:** acceleration, and automation of AI research;
- **misalignment:** exploratory, about instrumental reasoning that could undermine human control.

Early-warning "alert thresholds" trigger a closer assessment. A model at a CCL gets a response plan and a safety case before deployment.

Mitigations come in two kinds. **Deployment mitigations** act against misuse of a served model. **Security mitigations** act against exfiltration of the weights, and each CCL comes with a recommended **security level**. "Security level N" means controls generally aligned with the security goals and principles of RAND's SL N, not RAND's concrete benchmarks. Misuse CCLs get level 2, and the ML R&D CCLs get levels 3 and 4.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | A frontier developer's mapping from model capability to the level of protection its weights need. |
| Cryptography | none | No cryptographic content. |
| This project | adjacent | Like the RSP, it ties how hard an attacker must work to what the asset is worth, which is the kind of input **DEC-003**'s feasibility rating needs. It is policy, not a model tmodel can import. |

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | adjacent | AIT-055 | One of AIT-055's five sources (weight exfiltration). It reports no attack. |
| Existing AI threat models | core | TM-101 | It is TM-101's source. Its only attacker model is the RAND-aligned security-level tiering, as `sources.md` says; the CCLs are capability governance. |
| Weakness enumerations | adjacent | AML.T0025 | The framework cites no catalog ids. `sources.md` gives S-0805 AML.T0024.002 and AML.T0025. AML.T0025 (Exfiltration via Cyber Means) fits. AML.T0024.002 ("Extract AI Model", extraction by querying) does not: the framework's concern is exfiltration of the weights. |
| Attack → asset mapping | core | A02 | The asset is the weights (A02). The misuse CCLs point at downstream harm (A12) but rate capability, not assets. No components are named. |

## Implementations

None, searched 2026-11-13: a policy, not software.

| Name | Kind | License | URL |
|---|---|---|---|

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, digest and `cites` |
| `summary.md` | this summary, with the RPT-0014 applicability table |

## Reference expansion

The framework cites in footnotes. Each link was checked against `sources.md` and the library on 2026-11-13:
- **In `sources.md`:**
  - RAND, *Securing AI Model Weights* (S-0793), which defines the security levels;
  - *An Approach to Technical AGI Safety and Security*, arXiv 2504.01849 (S-0763);
  - OpenAI's updated Preparedness Framework (S-0814);
  - Anthropic's RSP announcement, which is S-0798, this lane's `anthropic-rsp-v2-2-2025`.
- **Missing and in scope, added as a stub (1):** *Evaluating Frontier Models for Stealth and Situational Awareness*, arXiv 2505.01420, cited for safety cases: `phuong-2025-stealth-situational-awareness`.
- **Not single works (2):** METR's list of frontier AI safety policies, and the Frontier Model Forum's publications page. Both are index pages.
- **Out of scope (1):** the UK government's *Emerging processes for frontier AI safety* (2023), which is governance practice, not an attacker or threat model.

## Limits

- **The attacker model is borrowed.** What a level-2 or level-4 attacker can do is RAND's definition, so this framework adds the capability-to-level mapping and nothing about attack vectors.
- **Goals, not controls.** It aligns with RAND's goals and principles, explicitly not its benchmark controls, so it does not say which measures are in place.
- **Misalignment is exploratory.** Those CCLs are illustrative, with no committed security level.
- **No newer version was found** at the source on 2026-11-13. The URL is version-specific, and DeepMind's site was not searched for a v4.
- **Read in part.** Read: §1 (scope, CCLs, the assessment process), §2.1 on security mitigations with the RAND footnote, the per-domain CCL tables with their recommended security levels, and the footnotes. The deployment-mitigation and safety-case procedure passages were skimmed.
