---
schema: "library-summary/v1"
id: huang-2024-harmful-finetuning-survey
record: huang-2024-harmful-finetuning-survey
type: summary
updated: "2026-11-03"
---

# Harmful Fine-tuning Attacks and Defenses for Large Language Models: A Survey

|  |  |
|---|---|
| **Type** | paper (survey) |
| **Maturity** | _unset_. A peer-reviewed journal survey; no standing is asserted |
| **Authors** | Tiansheng Huang, Sihao Hu, Fatih Ilhan, Selim Furkan Tekin, Ling Liu (Georgia Institute of Technology) |
| **Published** | ACM Computing Surveys, vol. 58, no. 13, pp. 1–39, 2026-06-23 (Crossref). arXiv v1 2024-09-26; the authors keep updating the arXiv version (v6 2026-04-23) |
| **Identifier** | doi:10.1145/3817114; arXiv:2409.18169 |
| **Source** | https://arxiv.org/pdf/2409.18169v6. Its page header still reads "Manuscript submitted to ACM". The ACM version of record was not obtained |
| **Digest** | `sha256:c23302761c3d5d48a333a6edc887da01710d67315a171d84c8dfd143bb94e20c` (2,832,467 bytes, 45 pages, retrieved 2026-11-03). The RPT-0014 manifest has no entry for S-0695 |

## Overview

**The problem.** Fine-tuning-as-a-service lets a customer upload data to fine-tune a provider's aligned model. A small fraction of harmful examples, or even benign data, can undo the model's safety alignment (§1, §2.3).

**Threat model (§2.2).**
- *Attacker:* a user who controls only the uploaded data, not the training process.
- *Defender:* the provider, who controls training and can filter data.
- *Motive:* either deliberate (for example, to make the provider liable for harmful output) or accidental (unfiltered data).

**Taxonomy (§3, Fig. 8).**
- *Attacks:* vanilla harmful-data attacks, benign-data attacks, and stealthier variants using steganography or data designed to slip past guardrails.
- *Defences:* well over 100, grouped by when they act: pre-training, alignment, fine-tuning or post-fine-tuning.

**Also covered.** A small experiment of the authors' own on Llama2-7B, measuring how harmful-data ratio affects harmfulness (§2.3); evaluation datasets and metrics (§4); and research directions (§5).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | The reference map of a major LLM attack class against hosted fine-tuning APIs, and its defences |
| Cryptography | `none` | No cryptographic content |
| This project | `adjacent` | Evidence for RPT-0014's AIT-081. Its threat model covers one service type, not a system |

`bears_on: none yet.` The paper informs no ARCH-0001 decision or requirement. It is `summarized` because LANES.md requires full summaries for subset-1 sources; no relevance is claimed.

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | core | AIT-081; AIT-017 | **AIT-081 (harmful fine-tuning to remove safety):** the survey's subject (§3.2). RPT-0014's catalog lists S-0695 here. **AIT-017 (fine-tuning data poisoning):** it overlaps, since the attack works through the uploaded data. The survey counts benign-data attacks and backdoor-style variants as extensions (Fig. 8). The evidence is research results on open models and fine-tuning APIs, not in-the-wild abuse |
| Existing AI threat models | adjacent | — | It states an explicit threat model for one service type: attacker and defender capabilities, goals and motives (§2.2). It is narrower than a system threat model, and RPT-0014 assigns it no TM id |
| Weakness enumerations | adjacent | AML.T0018.000, AML.T0020; NISTAML.037; OWASP LLM04:2025 — **concept-level, our mapping** | Neither ATLAS release 2026.09 nor NIST AI 100-2e2025 cites the survey (checked 2026-11-03). AML.T0018.000 is Poison AI Model; AML.T0020 is Training Data Poisoning; NISTAML.037 is training data attacks |
| Attack → asset mapping | adjacent | A03, A13; C03, C13; TB5 — **assigned by us** | The survey names what is harmed: the deployed model's safety behaviour and the provider's legal exposure (§2.2). Our ids: A03 (model behaviour integrity), A13 (provider liability), C03 (the fine-tuning service), C13 (third-party model providers), TB5 (the enterprise–provider boundary over which fine-tuning data crosses) |

## Implementations

Searched 2026-11-03. The survey ships no tool. It maintains a curated paper list at https://github.com/git-disl/awesome_LLM-harmful-fine-tuning-papers, which has no licence file declared. Defence code lives with the individual surveyed papers.

| Name | Kind | License | URL |
|---|---|---|---|
| awesome_LLM-harmful-fine-tuning-papers | curated reading list | none declared | https://github.com/git-disl/awesome_LLM-harmful-fine-tuning-papers |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | Metadata. `cites` lists the seed attack papers and the main defences |
| `summary.md` | This document |

**Reference expansion.** The references were screened with the Batch 1 rule. The seed attack papers are already in `sources.md`: Qi et al. (S-0303), Shadow Alignment (S-0209), Lermen et al. (S-0177), Zhan et al. (S-0215) and TAR (S-0471).

*Reference-expansion candidates* (5 widely cited defences; arXiv ids checked 2026-11-03; outcome of the 2026-11-03 review):

| Work | Locator | Outcome |
|---|---|---|
| Huang et al., Vaccine: perturbation-aware alignment | arXiv:2402.01109 | created: `huang-2024-vaccine` |
| Rosati et al., Representation Noising | arXiv:2405.14577 | created: `rosati-2024-repnoise` |
| Huang et al., Booster | arXiv:2409.01586 | not created |
| Hsu et al., Safe LoRA | arXiv:2405.16833 | not created |
| Huang et al., Lisa: lazy safety alignment | arXiv:2405.18641 | not created |

The other 100-plus defences were not proposed; this survey is the index to them.

Created stubs are `status: stub` with unwritten summaries; tmodel#81 owns filling them. Candidates marked "not created" were excluded in the consolidated review of 2026-11-03 as unnecessary for RPT-0014: niche, or their attack class is already covered.

## Limits

- **Narrow threat model.** Only fine-tuning-as-a-service, where the provider controls training. Attackers who download open weights and fine-tune them freely, the RPT-0014 AIT-081 open-weights case, sit outside its defence assumptions (§2.2).
- **The authors evaluate their own defences.** Vaccine, Booster, Lisa and others in the taxonomy are the authors' own, which may shape the framing.
- **A one-author collection process.** One author collected and first categorized the papers, and the others checked (§3.1). The stated search end date (2024-09-20) does not match v6, which includes papers from 2025 and 2026.
- **Version uncertainty.** v6 was read, and the authors say the arXiv version keeps changing. The ACM version of record (2026) may differ.
