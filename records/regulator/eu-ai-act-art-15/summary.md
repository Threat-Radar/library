---
schema: "library-summary/v1"
id: eu-ai-act-art-15
record: eu-ai-act-art-15
type: summary
updated: "2026-11-20"
lane: catalogs-schema
reviewed_by: ""
---

# EU AI Act Article 15: Accuracy, robustness and cybersecurity

|  |  |
|---|---|
| **Type** | spec (binding EU law; **stub**: summarized for WAVE 1, not FX-1 extracted) |
| **Maturity** | _unset — do not guess_ (a regulation, not a standards-track document) |
| **Authors** | European Parliament and Council of the European Union |
| **Published** | Regulation (EU) 2024/1689 of 13 June 2024, OJ L 12.7.2024. Application dates amended by Regulation (EU) 2026/1744 of 8 July 2026 (OJ L 24.7.2026) |
| **Identifier** | ELI http://data.europa.eu/eli/reg/2024/1689/oj; CELEX 32024R1689; Article 15 |
| **Source** | https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=OJ:L_202401689 (text read from the EUR-Lex HTML of the same act) |
| **Digest** | `bba630444b3278e881066774002a1d7824308934f49ccfa203e65be43692f55e` (the whole regulation, 144 pages) |

## Overview

Article 15 is one of the requirements for **high-risk AI systems** in Chapter III, Section 2. It has five paragraphs:
1. Such systems are to "achieve an appropriate level of accuracy, robustness, and cybersecurity" and "perform consistently in those respects throughout their lifecycle".
2. The Commission is to encourage benchmarks and measurement methods.
3. Accuracy levels and metrics are to be declared in the instructions for use.
4. Systems are to be "as resilient as possible regarding errors, faults or inconsistencies", for example through redundancy and fail-safe plans. Systems that keep learning after release must limit "feedback loops", where biased outputs influence later inputs.
5. **The AI-specific attack list.** Systems "shall be resilient against attempts by unauthorised third parties to alter their use, outputs or performance by exploiting system vulnerabilities". The measures are to "prevent, detect, respond to, resolve and control for attacks" against:
   - "the training data set (data poisoning)";
   - "pre-trained components used in training (model poisoning)";
   - "inputs designed to cause the AI model to make a mistake (adversarial examples or model evasion)";
   - "confidentiality attacks";
   - "model flaws".

**When it applies.** Regulation (EU) 2026/1744 (the "Digital Omnibus on AI", 8 July 2026) moved Chapter III Sections 1 to 3, this article included, from 2 August 2026 to:
- **2 December 2027** for systems that are high-risk under Article 6(2) and Annex III;
- **2 August 2028** for systems that are high-risk under Article 6(1) and Annex I.

The same act adds Article 42(3): a high-risk AI system within the Cyber Resilience Act (Regulation (EU) 2024/2847) that meets its Article 12(1) conditions "shall be deemed to comply with the cybersecurity requirements set out in Article 15". Article 15's own text is unchanged.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | A legal duty to resist named AI attack classes, for every high-risk system on the EU market |
| Cryptography | none | No cryptographic content |
| This project | adjacent | A source of Requirements that a TARA-like AI threat model must trace to (**DEC-001**: Requirement in the core, ADR-0012). It gives no method, so it tells tmodel what must be covered, not how |

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | adjacent | AIT-027 (and the poisoning, evasion and extraction classes) | AIT-027 (online-learning and feedback-loop poisoning) cites it, for 15(4). 15(5)'s five classes cover the poisoning, evasion and privacy groups of the catalog. Prompt injection, jailbreaks, agents and supply-chain code execution are not named, so they fall only under the general "exploiting system vulnerabilities" |
| Existing AI threat models | none | — | A legal requirement, not a threat model |
| Weakness enumerations | adjacent | Art. 15(5) classes; ~ NISTAML.013/.011/.022/.03; AML.T0020, AML.T0018, AML.T0015, AML.T0024 | The ids are `sources.md`'s mapping; the article cites no catalog. **AML.T0024's sub-techniques, which "confidentiality attacks" would map to, were removed in ATLAS 2026.10.** **`sources.md`'s open point is settled:** the later dates come from Regulation (EU) 2026/1744, now verified. prEN 18282, which `sources.md` expects to fill the gaps, wasn't checked here |
| Attack → asset mapping | adjacent | C02, C03, C04, C05; A01, A02, A03, A07 | The classes sit on training data and pipelines (C02, C03: poisoning), pre-trained components (C04: model poisoning) and inference inputs (C05: evasion). The assets are training data (A01), the model (A02), behaviour integrity (A03) and data that confidentiality attacks expose (A07). The mapping is ours |

## Implementations

None, searched 2026-11-20: a legal requirement. Conformity is to be shown through harmonised standards, which weren't checked here.

| Name | Kind | License | URL |
|---|---|---|---|

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, digest and relations |
| `summary.md` | this summary, with the RPT-0014 applicability table |

## Reference expansion

Article 15 cites no external work. Checking `sources.md`'s statement about its dates found one in-scope document missing from both `sources.md` and the library:
- **Added as a stub (1):** `eu-2026-1744-digital-omnibus-ai`, the amending regulation that sets the new dates and adds Article 42(3).
- **Already in the library:** the Cyber Resilience Act that Article 42(3) points to, `eu-cra-2024-2847`.

## Limits

- **A stub for FX-1.** This record summarizes the article for WAVE 1. The regulation is a `spec`, so moving it past stub needs the full FX-1 extraction of its requirements, recitals and cross-references.
- **"Where appropriate".** 15(5) requires the measures only "where appropriate" and "appropriate to the relevant circumstances and the risks". What counts is left to harmonised standards and conformity assessment.
- **Only high-risk systems.** General-purpose models fall under Chapter V instead (see the Code of Practice, S-0851), and other systems under transparency rules such as Article 50.
- **The list is short and dated.** Five classes, written before agentic systems were common. "Model flaws" is not defined.
