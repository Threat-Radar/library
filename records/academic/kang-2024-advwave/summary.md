---
schema: "library-summary/v1"
id: kang-2024-advwave
record: kang-2024-advwave
type: summary
updated: "2026-11-03"
---

# AdvWave: Stealthy Adversarial Jailbreak Attack against Large Audio-Language Models

|  |  |
|---|---|
| **Type** | paper |
| **Maturity** | _unset_. A peer-reviewed conference paper; no standing is asserted |
| **Authors** | Mintong Kang, Chejian Xu, Bo Li (University of Illinois Urbana-Champaign) |
| **Published** | ICLR 2025, proceedings pp. 27819–27835, publication date 2025-05-01 (proceedings.iclr.cc). arXiv v1 2024-12-11 |
| **Identifier** | arXiv:2412.08608 |
| **Source** | https://proceedings.iclr.cc/paper_files/paper/2025/file/45673dbf3f331fbd911b0689872de396-Paper-Conference.pdf (the camera-ready proceedings PDF) |
| **Digest** | `sha256:e1611922b83a8823577a7d64e0841e0ea8cc80f1eafcc516f828b95645ea9dd6` (735,136 bytes, 17 pages, retrieved 2026-11-03). The RPT-0014 manifest has no entry for S-0278 |

## Overview

**The argument.** Large audio-language models (ALMs) are LLMs with an audio encoder in front. Text jailbreaks do not carry over to them well, for three reasons (§1, §3.1):
- the audio tokenizer snaps features to the nearest learned cluster, which blocks gradients ("gradient shattering");
- ALMs respond in varied ways, so a fixed target answer such as "Sure!" is a poor optimization target;
- the adversarial audio must sound natural.

**Method.** AdvWave answers each problem in turn:
- *Two-phase optimization (§3.2):* it first optimizes the discrete audio tokens, then optimizes the waveform so its features land on those tokens.
- *Per-query target search (§3.3):* it asks GPT-4o to rewrite the harmful query as a benign one, records how the ALM answers that, and builds the target answer from the pattern.
- *Stealth (§3.4):* the attack appends a short suffix that an audio classifier steers towards sounding like urban noise, such as a car horn.

**Results.** The attack was run white-box on SpeechGPT, Qwen2-Audio and Llama-Omni, using 520 spoken AdvBench queries (§4, Table 1).
- AdvWave averages 0.838 success by refusal keywords and 0.746 by an LLM judge, with a stealthiness score of 0.713.
- The best baseline, a text jailbreak (AutoDAN) converted to speech, averages 0.436 and 0.470.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | A primary white-box jailbreak attack on a new input modality of deployed-class models |
| Cryptography | `none` | No cryptographic content |
| This project | `adjacent` | Evidence for the adversarial-audio and multimodal-jailbreak classes in RPT-0014. Not a threat-modeling source |

`bears_on: none yet.` The paper informs no ARCH-0001 decision or requirement. As with the earlier subset-1 records, it is `summarized` rather than a stub because LANES.md requires full summaries for subset-1 sources; no relevance is claimed.

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | core | AIT-006, AIT-079; AIT-074 | **AIT-006 (adversarial audio)** and **AIT-079 (multimodal jailbreaks):** a gradient-optimized audio suffix makes the model answer harmful spoken queries (§3, Table 1). RPT-0014's catalog already lists S-0278 under both. **AIT-074 (optimization-based jailbreaks):** the method is a GCG-style adversarial suffix carried into audio, and text GCG, BEAST and AutoDAN are its baselines (§4.1). All results are digital, on open models with full weight access |
| Existing AI threat models | none | — | §3.1 states the attack's own assumptions: the attacker submits audio, and the attack is white-box. That is experimental scoping, not a reusable threat model |
| Weakness enumerations | adjacent | AML.T0054, AML.T0043; NISTAML.018 — **concept-level, our mapping** | The paper defines no enumeration, and none of the catalogs checked cites it: not ATLAS release 2026.09 and not NIST AI 100-2e2025 (both checked 2026-11-03). The ATLAS ids (LLM Jailbreak; Craft Adversarial Data) and NISTAML.018 (prompt injection, which NIST uses for jailbreaks) match the attack class |
| Attack → asset mapping | none | — | It maps no attack to assets or components. Our catalog's AIT-079 entry assigns A03 and C05; that assignment is not the paper's |

## Implementations

Searched 2026-11-03. The authors' code is at https://github.com/kangmintong/AdvWave, with no licence file declared. The paper itself names no repository.

| Name | Kind | License | URL |
|---|---|---|---|
| AdvWave | open source, authors' code | none declared | https://github.com/kangmintong/AdvWave |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | Metadata. `cites` lists the jailbreak and audio-attack work the paper builds on, with the screened candidates below |
| `summary.md` | This document |

**Reference expansion.** The references were screened with the Batch 1 rule: a primary in-scope source, not in `sources.md`, not in the library, with a verified locator. These were checked against `sources.md`, the library and the arXiv API on 2026-11-03.

*Reference-expansion candidates* (3; outcome of the 2026-11-03 review):

| Work | Locator | Outcome |
|---|---|---|
| Sadasivan et al. 2024, BEAST: fast beam-search jailbreaks (a baseline) | arXiv:2402.15570 | not created |
| Alzantot et al. 2017, adversarial examples against speech recognition | arXiv:1801.00554 | not created |
| Cisse et al. 2017, Houdini: attacks on structured prediction, including speech | arXiv:1707.05373 | not created |

*Excluded because already in `sources.md`:* GCG (S-0220), AutoDAN (S-0181) and CommanderSong (S-0051). The other references are model papers, datasets and visual jailbreaks covered by other subset-1 sources.

The candidates above were excluded in the consolidated review of 2026-11-03 as unnecessary for RPT-0014: niche, or their attack class is already covered. No stub was created from this source.

## Limits

- **Strong attacker, small test.** White-box gradient access to three open models (§4.1). No closed or API-only ALM is attacked, and the audio is never played over the air.
- **One baseline model was barely aligned.** Llama-Omni answers 92.8% of the harmful spoken queries with no attack at all, by refusal keywords (Table 1, Vanilla). Average gains are inflated by including it.
- **The stealth score is partly self-defined.** It averages a noise ratio, spectrogram similarity and a human rating (§4.1). The human rating's procedure is in Appendix A.5, and its rater count was not checked.
- **Success is judged on text output only** (§4.1). The audio channel's own harms are not measured.
- **Possible table error.** In Table 1, the AutoDAN-Trans results for Llama-Omni (0.453, 0.485, 0.289) are identical to those for SpeechGPT, which looks like a copied row. The averages are computed from the duplicated values.
- **Comparison claims vary.** The abstract claims a 40% higher average success rate and §4.2 says over 50%. The text's "closest baseline" on SpeechGPT (GCG-Trans) is not the strongest baseline in Table 1 (AutoDAN-Trans).
