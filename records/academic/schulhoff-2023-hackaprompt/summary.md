---
schema: "library-summary/v1"
id: schulhoff-2023-hackaprompt
record: schulhoff-2023-hackaprompt
type: summary
updated: "2026-10-13"
---

# Ignore This Title and HackAPrompt: Exposing Systemic Vulnerabilities of LLMs through a Global Scale Prompt Hacking Competition

|  |  |
|---|---|
| **Type** | paper (competition dataset + taxonomy; 33 pp.) |
| **Maturity** | _unset — do not guess_ |
| **Authors** | S. Schulhoff, J. Pinto, and 8 co-authors (University of Maryland, Mila, and others) |
| **Published** | arXiv v3, 2024-03-03; `sources.md` gives EMNLP 2023 'from memory' — not stated in the PDF read |
| **Identifier** | arXiv:2311.16119 |
| **Source** | https://arxiv.org/pdf/2311.16119 |
| **Digest** | `a0c34dd3ee11d34758a22fe29259c2773f942b0ea12788bab1fb5822303c6b19` (matches `pdf-manifest.tsv`) |

## Overview

Reports a **global prompt-hacking competition**: over 2,800 participants submitted **600K+ adversarial prompts** trying to make three models (GPT-3 text-davinci-003, ChatGPT gpt-3.5-turbo, FlanT5-XXL) ignore their instructions and output a target phrase across graded levels. The resulting dataset (released on Hugging Face) empirically confirms that deployed LLMs can be manipulated by **prompt injection and jailbreaking** ("prompt hacking"), and the paper derives a **taxonomical ontology of prompt-hacking techniques** (for example context ignoring, refusal suppression, obfuscation, payload splitting), discussing harms such as training-data leakage, arbitrary content generation and token-wasting denial of service.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | Large-scale evidence of direct prompt manipulation. |
| Cryptography | none | Not about cryptography. |
| This project | adjacent | Adjacent: direct (user-side) injection on chat models; gives technique vocabulary but no agent/tool setting. |

Bears on **DEC-001** (object model — attack technique vocabulary).

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | core | AIT-063, AIT-073 | Direct prompt injection; manual jailbreak techniques, at scale |
| Existing AI threat models | none | — | A dataset and taxonomy, not a threat model |
| Weakness enumerations | adjacent | AML.T0051.000, AML.T0054, LLM01:2025, NISTAML.018 | Catalog entries for its attacks; its own technique ontology |
| Attack → asset mapping | adjacent | C07 | The LLM application layer (system prompt vs user input) |

## Implementations

Dataset on Hugging Face (licence not checked here). Searched 2026-10-13.

| Name | Kind | License | URL |
|---|---|---|---|


## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this summary |

## Limits

- **2023 models and a game setting** (make the model say a phrase), far from agentic tool use.
- **Venue unverified** in this pass; cite the arXiv version.
- Reference expansion not done in this pass (see PR notes).
