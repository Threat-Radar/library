---
schema: "library-summary/v1"
id: google-photos-model-extraction-2025
record: google-photos-model-extraction-2025
type: summary
updated: "2026-11-03"
---

# Google Photos' AI Models: The Secret Sauce That Can Be Stolen

|  |  |
|---|---|
| **Type** | article (vendor research blog post) |
| **Maturity** | _unset_. A vendor blog post; no standing is asserted |
| **Authors** | Mathis Mauvisseau, Victor Guyomard (Skyld) |
| **Published** | Skyld blog, 2025-03-31. Its disclosure timeline gives submission as 2025-02-28 |
| **Identifier** | https://skyld.io/google-photos-model-extraction; MITRE ATLAS case study AML.CS0058 |
| **Source** | Same URL, fetched as HTML on 2026-11-03 |
| **Digest** | `sha256:b0d63e6479e623184a565149b8a52c3f655ee9eff29ecefd24599fa59a53f95f` (45,907 bytes). This is the page as served, so the digest will change when the page template changes |

## Overview

**What was done.** Skyld recovered the TensorFlow Lite models that power Google Photos' on-device AI features (Magic Eraser, Unblur, Portrait light and others) from the Android app. They used three methods:
- searching the APK and the native library for the TFLite file signature;
- parsing the model files from the library's binary;
- using Frida to capture encrypted models when the app decrypts them in memory at runtime. Their keys stay in the Android Keystore's trusted execution environment, but the models must be decrypted to run.

**What was recovered.** Models in four places: 20 decrypted at runtime, 17 in the native library, 2 in app assets and 1 in app files. The recovered models included face detection, age and attribute estimation, segmentation and depth models.

**Implications claimed.** Competitors could reuse the models, and white-box access makes adversarial examples possible.

**Disclosure.** Reported to Google on 2024-12-23 and accepted; a reward decision followed on 2025-02-06.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | A primary, real-world demonstration of on-device model theft against a major app |
| Cryptography | `none` | It notes that runtime decryption defeats TEE-held keys, but contains no cryptographic analysis |
| This project | `adjacent` | Evidence for RPT-0014's on-device extraction class. Not a threat-modeling source |

`bears_on: none yet.` The post informs no ARCH-0001 decision or requirement. It is `summarized` because LANES.md requires full summaries for subset-1 sources; no relevance is claimed.

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | core | AIT-056; AIT-001 | **AIT-056 (on-device or edge model extraction):** demonstrated on a production app. RPT-0014's catalog lists S-1025 here, and its incident INC-082 is this post. **AIT-001 (white-box adversarial examples):** only claimed as a consequence; the post does not demonstrate it |
| Existing AI threat models | none | — | No threat model |
| Weakness enumerations | adjacent | AML.CS0058 (with AML.T0007, AML.T0035, AML.T0044, AML.T0025, AML.T0048.004, AML.T0043.000, AML.T0015); OWASP ML05 | **Verified:** ATLAS release 2026.09 cites this post as the reference for case study AML.CS0058 (checked 2026-11-03). **Concept-level, our mapping:** OWASP ML05 (model theft). NIST AI 100-2e2025 does not cite it. **Where ATLAS goes beyond the post** is listed under Limits |
| Attack → asset mapping | adjacent | A02; C16 — **ids assigned by us** | The post names its asset: Google's proprietary models as intellectual property, deployed on-device. Our ids: A02 (model weights and IP), C16 (mobile and on-device models) |

## Implementations

Searched 2026-11-03. No extraction tool is released. The method uses public tools (Frida and the TFLite flatbuffer schema). Skyld sells model-protection products, which are not listed here as implementations.

| Name | Kind | License | URL |
|---|---|---|---|

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | Metadata. `cites` lists the prior Android model-theft paper and ATLAS AML.CS0058 |
| `summary.md` | This document |

**Reference expansion.** The post cites one in-scope primary paper: Paindavoine, Despres and Sabt, "Your Mind is Mine: How to Automatically Steal DL Models From Android Apps". It is not in `sources.md`, but no stable locator was found, so it stays a `cites` entry. **No stubs are proposed.**

## Limits

- **ATLAS overstates the post.** AML.CS0058's procedure includes AML.T0043.000 (White-Box Optimization) and AML.T0015 (Evade AI Model). The post only says extraction "opens the door" to adversarial examples; it does not craft any.
- **Inconsistent counts.** The findings list four locations totalling 40 models, then the next section says "Among the 20 models identified". The 20 likely refers to the decrypted set.
- **A vendor with an interest.** Skyld sells model protection, and the post ends with a product pitch.
- **No evidence of misuse in the wild.** This is a research demonstration that Google acknowledged through its reward programme. The post does not say what Google changed afterwards.
