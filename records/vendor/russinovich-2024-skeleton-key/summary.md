---
schema: "library-summary/v1"
id: russinovich-2024-skeleton-key
record: russinovich-2024-skeleton-key
type: summary
updated: "2026-11-03"
---

# Mitigating Skeleton Key, a new type of generative AI jailbreak technique

|  |  |
|---|---|
| **Type** | article (a vendor research blog post) |
| **Maturity** | _unset_. A vendor blog post; no standing is asserted |
| **Authors** | Mark Russinovich (Chief Technology Officer, Microsoft Azure) |
| **Published** | Microsoft Security Blog, 2024-06-26 (`datePublished` in the page metadata) |
| **Identifier** | https://www.microsoft.com/en-us/security/blog/2024/06/26/mitigating-skeleton-key-a-new-type-of-generative-ai-jailbreak-technique/ |
| **Source** | Same URL, fetched as HTML on 2026-11-03 |
| **Digest** | `sha256:d6344137dcc97dd402be96c65b3b983632f61560424f89cb2ecb150e7f4ea29a` (297,016 bytes). This is the page as served, so the digest will change when the page template changes |

## Overview

**The technique.** Skeleton Key does not ask a model to drop its safety guidelines. It asks the model to *augment* them: answer every request, adding a warning where the content might be harmful. The attacker frames the request as safe, for example a researcher trained in safety. Once the model accepts the "updated guidelines", the user can ask directly for any forbidden content.

**Testing (April–May 2024).** It worked on seven models:
- Llama 3 70B and Gemini Pro (base models);
- GPT-3.5 Turbo, GPT-4o, Mistral Large, Claude 3 Opus and Command R+ (hosted).

GPT-4 resisted unless the instruction was placed in a user-defined system message.

**Response.** Microsoft disclosed to the affected vendors, updated its own models and Prompt Shields, added the technique to PyRIT, and recommends layered defences: input filtering, system messages, output filtering and abuse monitoring.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | A primary disclosure of a cross-vendor jailbreak, with mitigation guidance |
| Cryptography | `none` | No cryptographic content |
| This project | `adjacent` | Evidence for RPT-0014's manual-jailbreak class. Its explicit scoping of impact is useful for asset mapping |

`bears_on: none yet.` The post informs no ARCH-0001 decision or requirement. It is `summarized` because LANES.md requires full summaries for subset-1 sources; no relevance is claimed.

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | core | AIT-073 | **AIT-073 (manual jailbreaks):** the post describes a jailbreak that reframes the model's guidelines and was tested on seven production and open models. RPT-0014's catalog lists S-0998 here. The post calls it multi-turn, but its example is a single framing prompt followed by direct requests. The evidence is a vendor's own testing, not observed abuse |
| Existing AI threat models | none | — | It names the threat-model position (the attacker already has legitimate access to the model) but offers no threat model |
| Weakness enumerations | adjacent | AML.T0054; NISTAML.018; OWASP LLM01:2025 — **concept-level, our mapping** | Neither ATLAS release 2026.09 nor NIST AI 100-2e2025 cites the post (checked 2026-11-03) |
| Attack → asset mapping | adjacent | A03; C07, C13 — **ids assigned by us; the scoping is the post's** | The post scopes the impact itself. The attack narrows the gap between what the model can do and what it will do. It does not by itself expose other users' data, take control of the system or exfiltrate data. Our ids: A03 (model behaviour integrity), C07 (application-layer filters and system messages, the mitigations named), C13 (hosted model providers) |

## Implementations

Searched 2026-11-03. Microsoft says PyRIT, its open-source red-teaming toolkit, now includes Skeleton Key. Azure AI Content Safety Prompt Shields is a commercial mitigation.

| Name | Kind | License | URL |
|---|---|---|---|
| PyRIT | open source red-teaming toolkit | MIT | https://github.com/Azure/PyRIT |
| Azure AI Content Safety, Prompt Shields | commercial filter | — | https://learn.microsoft.com/azure/ai-services/content-safety/ |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | Metadata. `cites` lists the related jailbreak work the post links to |
| `summary.md` | This document |

**Reference expansion.** The post's references were screened with the Batch 1 rule. Crescendo is already in `sources.md` (S-0310).

*Reference-expansion candidates* (1; arXiv id checked 2026-11-03; outcome of the 2026-11-03 review):

| Work | Locator | Outcome |
|---|---|---|
| Dong et al., Attacks, Defenses and Evaluations for LLM Conversation Safety: A Survey (NAACL 2024) | arXiv:2402.09283 | not created |

The candidates above were excluded in the consolidated review of 2026-11-03 as unnecessary for RPT-0014: niche, or their attack class is already covered. No stub was created from this source.

## Limits

- **No numbers.** The post publishes no success rates, prompts or test sets, only that all affected models "complied fully" across the tested categories.
- **Vendor-framed.** It promotes Azure mitigations alongside the disclosure.
- **A point in time.** Models were tested in April–May 2024, and the affected vendors were told before publication. Current models may not be vulnerable.
- **Prior naming.** The technique was first shown at Microsoft Build 2024 as "Master Key".
