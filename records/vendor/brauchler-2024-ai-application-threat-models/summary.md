---
schema: "library-summary/v1"
id: brauchler-2024-ai-application-threat-models
record: brauchler-2024-ai-application-threat-models
type: summary
updated: "2026-11-26"
lane: catalogs-schema
reviewed_by: ""
---

# Analyzing AI Application Threat Models

|  |  |
|---|---|
| **Type** | article (vendor research blog post) |
| **Maturity** | _unset — do not guess_ |
| **Authors** | David Brauchler (NCC Group) |
| **Published** | 2024-02-07, NCC Group research blog |
| **Identifier** | https://www.nccgroup.com/research/analyzing-ai-application-threat-models/ (the `sources.md` link under `/us/research-blog/` redirects there) |
| **Source** | https://web.archive.org/web/20250702003120id_/https://www.nccgroup.com/us/research-blog/analyzing-ai-application-threat-models/ |
| **Digest** | `ebe2ce14816f912060c06240227074ad0b183417a700f7d79af641e2e5499cf2` (the archived bytes, gzip; see `record.yaml` for the decompressed HTML's digest) |

## Overview

NCC Group's threat model for applications that build in machine learning, mostly LLMs. Its central claim is that a model sits in the threat model as an asset, a control and a **threat actor** at once. Since anyone who gets data into a model can steer it, the model should be designed as a potential attacker. NCC calls this the Models-As-Threat-Actors (**MATA**) methodology.

The post works through four attack scenarios on a generic architecture, in which a user reaches a frontend API, the frontend feeds an LLM, and the LLM can call a backend API in front of protected data:
1. privileged access through the model;
2. response poisoning in a "persistent world", where one user's data reaches another user's session;
3. poisoned training data, which it calls Water Table Attacks;
4. compromise of what the model can reach: secrets in the prompt or the training data, the model itself, its APIs and its compute.

It then lists **25 threat vectors** "that can emerge organically ... by default". Some are standard (prompt injection, extraction, adversarial input, malicious pickled models). Many are its own names: Oracle Attacks, Entropy Injection, Format Corruption, Parameter Smuggling and Parameter Cracking, Token Overrun, Control Token Injection, Cross-Plugin Request Forgery, Cross-Modal Data Leakage and Offline Environment Replication.

On controls, it calls canary nonces and watchdog models "none ... foolproof, or even particularly strong". Its alternative is a **trustless function** split: a "code model" takes trusted user requests, a separate "data model" handles untrusted content, and the application, not the first model, puts the second one's output in front of the user. It ends with advice for AI penetration tests: whitebox access, architecture documents and a subject-matter expert.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | A threat model and attack list for LLM-integrated applications, from a security consultancy's testing practice |
| Cryptography | none | No cryptographic content |
| This project | adjacent | It gives the rule behind report.md's TrustBoundary proposal: an AI component is untrusted, and anything it can reach is exposed to whoever feeds it data. That is a label tmodel could carry on a Component and propagate along edges (**DEC-001**). It is a method, not a schema |

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | adjacent | AIT-091 | One of AIT-091's nine sources (tool-call hijacking with the user's privileges, its Excessive Agency and API Abuse). It reports no attack of its own. Its in-the-wild examples are others': Tay, the Bard exfiltration (S-0974), the "Glorbo" news-bot prank and GPT-4 output used to train other models |
| Existing AI threat models | core | TM-027 | TM-027's source, with the second post. TM-027 lists seven threat categories. The post has four scenarios and 25 vectors, and the vectors with local names (Parameter Smuggling and Cracking, Token Overrun, Control Token Injection, Format Corruption, Cross-Modal Data Leakage, Offline Environment Replication) are not in TM-027. The "code models vs data models" split TM-027 credits is in this post; the seven principles are in the second |
| Weakness enumerations | adjacent | AML.T0051.001, AML.T0053, LLM01:2025, LLM06:2025, ASI02, ASI03 | It cites no catalog ids; its 25 vectors are its own list. Neither ATLAS 2026.09 nor NIST AI 100-2e2025 cites it (searched 2026-11-15). ATLAS's AML.CS0016 cites a different NCC post (2022, prompt injection). The ids are `sources.md`'s mapping |
| Attack → asset mapping | core | C07, C09, C05, C06, C03, C04, C17, A07, A04, A09, A02, A01, A11 | The generic architecture names the parts: the frontend and prompt (C07), the backend API the model calls (C09), the model and its compute (C05), persistent-world sources (C06), continuously trained models (C03), pickled model files (C04), and systems that parse its output, for Format Corruption (C17). The assets are backend data (A07), the initialization prompt (A04) and secrets in it (A09), model IP for extraction (A02), training data (A01) and compute (A11). The component and asset mapping is ours |

## Implementations

Searched 2026-11-15: none. The post describes a method and names no tool. The code-model and data-model split is a pattern, not software.

| Name | Kind | License | URL |
|---|---|---|---|

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, digest and `cites` |
| `summary.md` | this summary, with the RPT-0014 applicability table |

## Reference expansion

The post cites inline, with 15 links. Each was checked against `sources.md` and the library on 2026-11-15, by arXiv id and title, then by author and keyword:
- **In `sources.md` (4):** Shokri et al., membership inference (S-0027); Tramèr et al., model stealing (S-0013); Akhtar and Mian's survey (S-0671); Rehberger's Bard exfiltration (S-0974).
- **Covered by another source (1):** Ars Technica's 2017 report on stop-sign stickers, which reports Eykholt et al. (S-0038).
- **Missing, added as `status: stub` with forward `cites` from this record (6):**
  - `wang-2022-variational-model-inversion` (arXiv 2201.10787, cited for "model inversions");
  - `elsayed-2018-adversarial-reprogramming` (arXiv 1806.11146);
  - `machado-2020-adversarial-ml-image-classification-survey` (arXiv 2009.03728);
  - `openai-2021-multimodal-neurons` (typographic attacks on CLIP);
  - `edwards-2023-glorbo-ai-news-prank` (Ars Technica);
  - `ong-2023-ethnically-ambiguous-homer` (The Chainsaw).

  The three web pages are pinned by Wayback Machine copies.
- **Out of scope (4):**
  - SALMONN (arXiv 2310.13289), cited only as an example of a speech-to-LLM architecture;
  - Computerphile's "Glitch Tokens" video, an explainer (S-0632 covers glitch tokens);
  - a Hugging Face model card, cited as evidence of training on GPT-4 output, which is not a single work;
  - NPR's 2023 Bing chatbot story, cited for model unreliability, not an attack.

## Limits

- **No evidence of its own.** The scenarios are hypothetical, and the examples come from others. Several vectors are named here and nowhere else, so readers cannot check them against other sources.
- **Attributions go beyond the sources.**
  - Cross-Modal Data Leakage says "OpenAI appears to inject" anti-bias terms into image prompts. The article it cites names only "an unspecified AI art generator", then tries the prompt on "Bing Image Generator".
  - Glorbo is presented as an Adversarial Input attack exploited in the wild. The Ars Technica report describes a fake Reddit post that a news site scraping Reddit turned into a bot-written article. That is closer to the post's own persistent-world corruption than to an input that makes a model fail its task.
- **2024 state.** Plugins, canaries and watchdog models are discussed as they stood in early 2024. MCP, agents with browsers, and today's guard models came later.
- **Read from an archive.** The 2025-07-02 copy was read. The page now lives at a new URL. Its live copy, fetched 2026-11-15, has word-for-word the same body text, with the byline "David Brauchler" in place of "nccdavid".
