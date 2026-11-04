---
schema: "library-summary/v1"
id: unit42-2024-deceptive-delight
record: unit42-2024-deceptive-delight
type: summary
updated: "2026-11-03"
---

# Deceptive Delight: Jailbreak LLMs Through Camouflage and Distraction

|  |  |
|---|---|
| **Type** | article (vendor threat research) |
| **Maturity** | _unset_. A vendor research post; no standing is asserted |
| **Authors** | Royce Lu (Palo Alto Networks Unit 42) |
| **Published** | Unit 42 Threat Research Center, 2024-10-23 (byline and page metadata) |
| **Identifier** | https://unit42.paloaltonetworks.com/jailbreak-llms-through-camouflage-distraction/ |
| **Source** | Same URL, fetched as HTML on 2026-11-03 |
| **Digest** | `sha256:351f07007f500397cb063a4cd5baf41781fad8658cf308a46800d426c77dcf64` (301,888 bytes). This is the page as served, so the digest will change when the page template changes |

## Overview

**The technique.** Deceptive Delight is a short multi-turn jailbreak.
- *Turn 1:* ask the model for a story linking two benign topics and one unsafe topic.
- *Turn 2:* ask it to expand on each topic.
- *Turn 3 (optional):* ask it to expand on the unsafe one.

The author attributes success to the model's limited "attention" being drawn to the benign content.

**Evaluation.**
- *Setup:* 40 hand-written unsafe topics in six categories, 5 variants each, 5 repeats, on 8 anonymized models: 8,000 cases.
- *Filters:* the providers' content filters were disabled.
- *Judge:* an unnamed LLM scored harmfulness and quality from 0 to 5. A case counts as a success when both scores are at least 3.

**Results.**
- Average success rises from 5.8% with no jailbreak to 64.6% with it.
- Success peaks at turn 3.
- Violence topics succeed most, sexual and hate topics least.

**Mitigations.** Content filters and system-prompt hardening.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | A primary description and measurement of a multi-turn jailbreak |
| Cryptography | `none` | No cryptographic content |
| This project | `adjacent` | Evidence for RPT-0014's multi-turn jailbreak class. Not a threat-modeling source |

`bears_on: none yet.` The post informs no ARCH-0001 decision or requirement. It is `summarized` because LANES.md requires full summaries for subset-1 sources; no relevance is claimed.

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | core | AIT-075 | **AIT-075 (multi-turn escalation and context-poisoning jailbreaks):** a two-to-three-turn camouflage jailbreak measured over 8,000 cases. RPT-0014's catalog lists S-1003 here. It is research on anonymized models with their filters off, not observed abuse |
| Existing AI threat models | none | — | No threat model |
| Weakness enumerations | adjacent | AML.T0054; NISTAML.018; OWASP LLM01:2025 — **concept-level, our mapping** | Neither ATLAS release 2026.09 nor NIST AI 100-2e2025 cites the post (checked 2026-11-03) |
| Attack → asset mapping | none | — | It maps no attack to assets. Our catalog's AIT-075 assigns A03, C07 and C13; that assignment is not the post's |

## Implementations

Searched 2026-11-03. No code or dataset is released. The post lists commercial and open content filters as mitigations: OpenAI Moderation, Azure, Vertex AI, Bedrock Guardrails, Llama Guard and NeMo Guardrails.

| Name | Kind | License | URL |
|---|---|---|---|

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | Metadata. `cites` lists the multi-turn jailbreak and judge work the post builds on |
| `summary.md` | This document |

**Reference expansion.** The post's references were screened with the Batch 1 rule. Crescendo (S-0310) and JailbreakBench (S-0920) are already in `sources.md`. The judge-selection study (arXiv:2406.18403) is evaluation background and is not proposed.

*Reference-expansion candidates* (1; arXiv id checked 2026-11-03; outcome of the 2026-11-03 review):

| Work | Locator | Outcome |
|---|---|---|
| Sun et al. 2024, Multi-Turn Context Jailbreak Attack from first principles (the "Context Fusion Attack") | arXiv:2408.04686 | not created |

The candidates above were excluded in the consolidated review of 2026-11-03 as unnecessary for RPT-0014: niche, or their attack class is already covered. No stub was created from this source.

## Limits

- **Filters were off.** Content filters were deliberately disabled, so the 64.6% figure measures model alignment alone, not deployed products.
- **Models are anonymized and the judge is unnamed.** Results cannot be tied to products or reproduced. The judge is justified by citing other studies, not validated here.
- **Hand-written topics.** The authors say category results may be biased by the 40 topics they wrote.
- **Small inconsistencies.** The summary says the judge scores "on a scale of one to five", but the metric section uses 0–5. The method is described as unfolding over two turns, but the headline counts three.
