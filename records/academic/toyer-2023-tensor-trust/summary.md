---
schema: "library-summary/v1"
id: toyer-2023-tensor-trust
record: toyer-2023-tensor-trust
type: summary
updated: "2026-10-13"
---

# Tensor Trust: Interpretable Prompt Injection Attacks from an Online Game

|  |  |
|---|---|
| **Type** | paper (game-derived dataset + benchmark; 34 pp.) |
| **Maturity** | _unset — do not guess_ |
| **Authors** | S. Toyer, O. Watkins, and 10 co-authors (UC Berkeley, Georgia Tech, Harvard) |
| **Published** | arXiv v1, 2023-11-02; `sources.md` gives ICLR 2024 'per memory; not re-verified' — not stated in the PDF read |
| **Identifier** | arXiv:2311.01011 |
| **Source** | https://arxiv.org/pdf/2311.01011 |
| **Digest** | `7f815c7caa9bd24db98aa02ec13ad612d496898838efad4bf56e49f71c6a123f` (not in `pdf-manifest.tsv`; computed on the arXiv copy) |

## Overview

Presents **Tensor Trust**, an online game where players write *defenses* (system prompts guarding an access code) and *attacks* against other players' defenses, yielding **over 126,000 prompt-injection attacks and 46,000 defenses** — the largest human-generated set of adversarial examples for instruction-following LLMs at the time. The attacks have clearly interpretable structure. From it the authors build two **robustness benchmarks**: **prompt extraction** (making the model reveal its hidden instructions) and **prompt hijacking** (making it act against them), and find many models vulnerable. Some attack strategies **generalise to deployed LLM applications**. Data and code are released (tensortrust.ai/paper).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | Evidence for two core injection outcomes. |
| Cryptography | none | Not about cryptography. |
| This project | adjacent | Adjacent: chat-level injection; supports system-prompt extraction as an attack step. |

Bears on **DEC-001** (object model — prompt extraction and hijacking as attack steps).

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | core | AIT-063, AIT-083 | Direct injection (hijacking); system-prompt extraction |
| Existing AI threat models | none | — | A dataset and benchmark |
| Weakness enumerations | adjacent | AML.T0051.000, AML.T0056, LLM01:2025, LLM07:2025 | Catalog entries for its two attack types |
| Attack → asset mapping | adjacent | C07 | System prompt and configuration in the LLM application layer |

## Implementations

Data and code released (tensortrust.ai/paper; licence not checked). Searched 2026-10-13.

| Name | Kind | License | URL |
|---|---|---|---|


## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this summary |

## Limits

- **Game setting with GPT-3.5 backend;** transfer to agents is shown only anecdotally.
- **Venue unverified;** not in the team PDF manifest (digest computed here).
- Reference expansion not done in this pass (see PR notes).
