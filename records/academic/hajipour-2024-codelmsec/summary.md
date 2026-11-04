---
schema: "library-summary/v1"
id: hajipour-2024-codelmsec
record: hajipour-2024-codelmsec
type: summary
updated: "2026-11-03"
---

# CodeLMSec Benchmark: Systematically Evaluating and Finding Security Vulnerabilities in Black-Box Code Language Models

|  |  |
|---|---|
| **Type** | paper (introduces a benchmark dataset) |
| **Maturity** | _unset_. A peer-reviewed conference paper; no standing is asserted |
| **Authors** | Hossein Hajipour, Keno Hassler, Thorsten Holz, Lea Schönherr, Mario Fritz (CISPA Helmholtz Center for Information Security) |
| **Published** | IEEE SaTML 2024, pp. 684–709 (Crossref, issued 2024-04-09). arXiv v1 2023-02-08, v2 2023-10-23 |
| **Identifier** | doi:10.1109/SaTML59370.2024.00040; arXiv:2302.04012 |
| **Source** | https://arxiv.org/pdf/2302.04012v2. The IEEE version of record was not obtained |
| **Digest** | `sha256:37997e2cbdd820374be40217054fe6048e21ca9ba8e105f859133bc6c425072d` (9,196,368 bytes, 23 pages, retrieved 2026-11-03). The RPT-0014 manifest has no entry for S-0922 |

## Overview

**The argument.** Code models learn insecure patterns from unsanitized training code. Earlier evaluations used a handful of hand-written prompts (§I, §II).

**Method.** The authors find prompts automatically. They give a black-box code model a few examples of vulnerable code paired with the prompts that led to them, and ask it to write new prompts likely to produce the same vulnerability. The paper calls this an approximate inversion of the model (§IV, Fig. 1). GitHub's CodeQL static analyser then flags the generated code against 13 CWEs (Table I), eleven of which are in CWE's Top 25.

**Results.**
- More than 2,000 vulnerable Python and C programs from CodeGen and ChatGPT (Tables II–III).
- The prompts transfer between models (Tables IV–V).
- The benchmark has 280 non-secure prompts: 200 Python and 80 C.
- Run on five models, every one produced vulnerable code; StarCoder-7B and WizardCoder-15B produced the most (Table VI).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Measures how often code models emit known weakness classes, and gives a reusable test |
| Cryptography | `none` | No cryptographic content |
| This project | `adjacent` | Evidence for RPT-0014's AIT-131 (AI-generated insecure code). Its CWE labels tie AI risk to the same weakness ids our model uses. It does not address threat modeling |

`bears_on: none yet.` The CWE labelling is close to R-010 (map weaknesses to CWE), but the paper informs no ARCH-0001 decision: it labels generated code, it does not map threats. It is `summarized` because LANES.md requires full summaries for subset-1 sources; no relevance is claimed.

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | core | AIT-131 | **AIT-131 (AI-generated insecure code reaching production):** it measures at scale how code models produce CWE-classed vulnerable code, and finds the prompts that trigger it (§V, Table VI). RPT-0014's catalog lists S-0922 here. The non-secure prompts are written to elicit insecure code, so they model a careless or adversarial prompt rather than typical use |
| Existing AI threat models | none | — | No threat model is stated. The setting is black-box query access to a code model |
| Weakness enumerations | core | CWE-20, CWE-22, CWE-78, CWE-79, CWE-89, CWE-94, CWE-117, CWE-190, CWE-476, CWE-502, CWE-601, CWE-611, CWE-787 — **the paper's own**; OWASP LLM05:2025, LLM09:2025 — concept-level, our mapping | The benchmark is organized by these 13 CWE ids (Table I, printed with leading zeros, such as CWE-020). Neither ATLAS release 2026.09 nor NIST AI 100-2e2025 cites the paper (checked 2026-11-03) |
| Attack → asset mapping | adjacent | A08, A10; C14 — **assigned by us** | The paper's concern is vulnerable code entering developers' work through tools like Copilot (§I). It gives no asset model. Our ids: A08 (source code and release pipeline), A10 (hosts that run the code), C14 (the developer environment and AI coding tools) |

## Implementations

Searched 2026-11-03. The benchmark and code are at https://github.com/codelmsec/codelmsec, under Apache-2.0. The leaderboard site the paper promised is at codelmsec.github.io.

| Name | Kind | License | URL |
|---|---|---|---|
| codelmsec | open source, benchmark and prompt-generation code | Apache-2.0 | https://github.com/codelmsec/codelmsec |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | Metadata. `cites` lists the prior code-security evaluations and CWE |
| `summary.md` | This document |

**Reference expansion.** The references were screened with the Batch 1 rule. The two central prior works are already in `sources.md`: Pearce et al., "Asleep at the Keyboard" (S-0147), and SVEN (S-0169). **No stubs are proposed.** The other references are code-model papers, static-analysis tools and datasets.

## Limits

- **Static analysis only.** Vulnerabilities are CodeQL findings, with its false positives and negatives (§VI-B), on short, function-level snippets.
- **13 CWEs, two languages.** The CWEs were chosen because CodeQL can detect them (§III-B). Fuzzing and deployment-level weaknesses are out of scope.
- **Seeds were chosen by hand.** The vulnerable examples that drive prompt generation were picked manually, which may bias results (§VI-B).
- **Models as of 2023.** CodeGen, ChatGPT, Code Llama-13B, StarCoder-7B and WizardCoder-15B, plus a Copilot appendix. Newer models are not covered.
- **Counts, not rates.** Table VI reports counts of vulnerable outputs per model, so comparing models also needs their functional quality. The authors make this point themselves.
