---
schema: "library-summary/v1"
id: goldstein-2023-influence-operations
record: goldstein-2023-influence-operations
type: summary
updated: "2026-11-21"
lane: catalogs-schema
reviewed_by: ""
---

# Generative Language Models and Automated Influence Operations: Emerging Threats and Potential Mitigations

|  |  |
|---|---|
| **Type** | paper (a policy research report, informed by an expert workshop) |
| **Maturity** | _unset — do not guess_ (arXiv preprint) |
| **Authors** | Josh A. Goldstein, Girish Sastry, Micah Musser, Renée DiResta, Matthew Gentzel, Katerina Sedova (Georgetown CSET, OpenAI, Stanford Internet Observatory) |
| **Published** | arXiv v1, 2023-01-10 (dated January 2023; the only version on 2026-11-21) |
| **Identifier** | arXiv:2301.04246 |
| **Source** | https://arxiv.org/pdf/2301.04246 |
| **Digest** | `5b79c714add31173517ac63fc1f0f12c66eb16691648103c71a8545d22a526a3` (84 pages) |

## Overview

The report asks how generative language models could change **influence operations**, meaning covert attempts to shape opinion, and what could mitigate that. It draws on a workshop of 30 experts held in October 2021, and says it is "inherently speculative".

**The ABC framework.** Using Camille François's "Disinformation ABC", it predicts changes along three axes (Table 1):
- **Actors:** more and more diverse propagandists, and outsourced firms for hire;
- **Behaviour:** automated scale, cheaper existing tactics such as cross-platform testing, and new ones such as personalised real-time chatbots;
- **Content:** more credible and persuasive messages, and less discoverable ones, because no copy-pasted text gives them away.

It makes "a high confidence judgment that language models will be useful for influence operations". It names critical unknowns: emergent capabilities, purpose-built models, investment, norms, and when easy tools arrive.

**The mitigation pipeline.** Mitigations attach to a four-stage kill chain of what propagandists need (Table 2):
1. **A capable model** (model design and construction): more fact-sensitive models, radioactive training data, data-collection limits, and controls on AI hardware.
2. **Reliable access to it** (model access): stricter usage rules and release norms.
3. **Infrastructure to distribute content** (dissemination): platform and AI-provider coordination, proof of personhood, and provenance standards.
4. **A susceptible audience** (belief formation): media literacy and consumer AI tools.

It concludes there is "no silver bullet". It calls for a whole-of-society response and for mitigations that address demand as well as supply.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | A structured threat analysis of AI-enabled influence operations, with mitigations by stage |
| Cryptography | none | Provenance is named as a mitigation without any design |
| This project | adjacent | It supports the brand-impersonation and disinformation threats a company model needs, with mitigations attached per stage (**DEC-001**). It is societal rather than system-specific |

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | adjacent | AIT-129 (and AIT-126) | AIT-129 (AI-generated influence operations and election deepfakes) cites it. Its chatbot and personalised-content tactics also fit AI-automated social engineering (AIT-126). It reports the threat as expected, with few 2022 incidents (fake faces in influence operations, the Zelenskyy deepfake) |
| Existing AI threat models | core | TM-108 | TM-108's source. TM-108's "pipeline stage" decomposition matches the four stages. TM-108 could also note the ABC dimensions, which are the threat side of the model |
| Weakness enumerations | none | NISTAML.04; LLM09:2025? | The mapping is `sources.md`'s; the report cites no catalog. LLM09 (misinformation) covers a model producing false content, which is an application weakness, not the deliberate misuse this report studies, so `sources.md`'s question mark is apt |
| Attack → asset mapping | adjacent | C13, C12, C17; A13, A15 | Attackers use third-party or open models (C13) to reach people (C12) through platforms (C17). The assets are brand and reputation (A13) and human trust (A15). The mapping is ours |

## Implementations

None, searched 2026-11-21: a policy analysis.

| Name | Kind | License | URL |
|---|---|---|---|

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, digest and `cites` |
| `summary.md` | this summary, with the RPT-0014 applicability table |

## Reference expansion

208 references, checked against `sources.md` and the library on 2026-11-21. 90 mention AI, and 17 of those are in scope: AI-enabled influence operations and deepfake incidents, model spinning, the limits of AI-text detection, threat models and security primers, and misuse-aware release research.
- **In `sources.md` (2):** S-0027 (Shokri) and S-0013 (Tramèr).
- **Covered by another source or stub (4):**
  - the $35M voice-clone fraud, which is the stub `aiid-147-hong-kong-bank-voice-clone-fraud`;
  - two news stories on GPT-4chan, covered by the new `kurenkov-2022-gpt-4chan-controversy` stub;
  - Tay (S-0864).
- **Missing, added as stubs (16):**
  - **5 arXiv papers:** model spinning ("propaganda-as-a-service"), detection is easiest when humans are fooled, the cost analysis of LMs for influence operations, release practices for synthetic media, and OpenAI's release-strategies study;
  - **11 web documents, pinned by Wayback copies:** the Zelenskyy deepfake, a deepfake harassment plot, AI-generated fake faces in influence operations, the CSET reports (*Truth, Lies, and Automation*; *Hacking AI*; *Cyber Swords or Shields*; *AI and the Future of Disinformation Campaigns, Part 2: A Threat Model*), Farid on deepfakes, Wired on AI-written public comments, and Nightingale and Farid on synthetic faces.
- **Not stubbed (3):**
  - two references cited as unpublished working papers (Goldstein et al. on AI propaganda; Kreps and Kriner's field experiment);
  - DeepAttest (ISCA 2019), which has no open copy.
- **Out of scope (the other 183):**
  - general model and capability papers, vendor API pages and model announcements;
  - detection and marking methods without a security evaluation (GLTR, feature-based detection, radioactive data);
  - perception studies and opinion pieces;
  - non-AI disinformation research.

## Limits

- **Speculative by design, and from 2021–2022.** It predates ChatGPT's release by weeks and reasons from GPT-3-era capability. Later evidence, such as the 2025 *Science* study of AI persuasion (`hackenburg-2025-levers-political-persuasion`), tests what it forecast.
- **No measurement.** It predicts effects on actors, behaviour and content without data on reach or persuasion. The cited working papers are the evidence it leans on.
- **Mitigations aren't evaluated.** It catalogues them by stage and judges them only qualitatively for feasibility and downside risk.
- **A conflict to note.** One author's institution, OpenAI, is a model provider, and model access is one of the stages it analyses.
