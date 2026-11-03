---
schema: "library-summary/v1"
id: vero-2025-baxbench
record: vero-2025-baxbench
type: summary
updated: "2026-11-01"
---

# BaxBench: Can LLMs Generate Correct and Secure Backends?

|  |  |
|---|---|
| **Type** | paper (benchmark) |
| **Maturity** | _unset_ (peer-reviewed conference paper; no maturity level applies) |
| **Authors** | Mark Vero, Niels Mündler, Victor Chibotaru, Veselin Raychev, Maximilian Baader, Nikola Jovanović, Jingxuan He, Martin Vechev (ETH Zurich, LogicStar.ai, UC Berkeley, INSAIT Sofia) |
| **Published** | arXiv v1 2025-02-17; v3 2025-05-30 (summarized here, with the ICML 2025 header); ICML 2025, PMLR 267 |
| **Identifier** | arXiv:2502.11844 |
| **Source** | https://arxiv.org/pdf/2502.11844v3 |
| **Digest** | `sha256:fbabce80c3094bde4b10da9c2c0f557aaa41315669bd192cc78c623595c9e9ed` (arXiv v3, 47 pages) |

## Overview

BaxBench asks whether language models can write a whole, deployable application module,
choosing web backends because they are common, take several functions and files, and face
untrusted users (§1). It combines 28 scenarios specified in OpenAPI with 14 frameworks in six
languages into 392 tasks, and checks each generated backend with functional tests and with
expert-written end-to-end exploits, rather than static analysis, against 13 CWEs (§2, §3,
Table 5). Across 11 models the best correctness is 62% (OpenAI o1) and the best rate of correct
and secure code is 37% (OpenAI o3-mini); the exploits succeed against about half of the correct
programs, and models do worse in less popular frameworks such as Rust-Actix and PHP-Lumen
(§1, §4, Figures 1, 3 and 5). A generic security reminder helps reasoning models but not
others, a reminder that names every expected vulnerability raises security at some cost to
correctness, and a coding agent improves security only with that reminder (§4, Table 2).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Measures, with working exploits, how often LLM-generated backends are insecure, across 14 frameworks and 13 CWEs (§2 to §4) |
| Cryptography | `adjacent` | Its CWE-522 exploits check whether generated code stores passwords and secrets unprotected, for example with a dictionary attack on the stored database (§2.1) |
| This project | `adjacent` | tmodel has to record a weakness that entered a product through AI-generated code, as a CWE-typed Weakness with that origin. The project is also built with AI assistance, and the finding that about half of correct generated backends are exploitable supports reviewing generated code |

`bears_on: DEC-001a` (the core type system, accepted in ADR-0010).

## Implementations

Searched on 2026-11-01.

| Name | Kind | License | URL |
|---|---|---|---|
| logic-star-ai/baxbench | the benchmark's scenarios, functional tests and exploits; leaderboard at https://baxbench.com/ | MIT | https://github.com/logic-star-ai/baxbench |

Golden solutions are not released, to limit contamination (§5).

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this document |

## Limits

- **Security is an upper bound.** A program counts as secure when none of the exploits
  succeeds, so the score depends on the exploit set. Compared with Snyk Code on o1's 237 correct
  programs, the exploits caught 64 vulnerable programs Snyk missed, while Snyk raised 7 valid
  flags the exploits did not confirm (§4).
- **Mostly single-shot generation.** Ten samples per task for non-reasoning models and one for
  reasoning models; the only agent experiment is OpenHands with Claude 3.5 Sonnet on 351 tasks
  (§4).
- **Small applications.** About two endpoints per scenario; the authors present the tasks as
  simpler real-world backends (§3, §5).
- **Contamination is possible** once the benchmark is public, though golden solutions are
  withheld (§5).
- **The numbers changed between versions.** v1 reported o1 at 60% correct, more than half of
  correct programs exploitable and a best correct-and-secure rate of 35%; v3 reports 62%, about
  half and 37%. v3's Figure 3 caption still says 35%.
- **Early-2025 models,** since superseded.

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | core | AIT-131 | AIT-131 cites it, and it is that entry's measured evidence: on 392 backend tasks the best correctness is 62% (o1) and the best correct-and-secure rate 37% (o3-mini), and expert exploits succeed against about half of the correct programs (§4, Figures 1 and 3). report.md §3.14 says o1 is correct and secure about 38% of the time; in v3 o1 is about 31%, 6 points below o3-mini, and in v1 no model passed 35%, so that figure needs correcting in the next integration pass |
| Existing AI threat models | none | none | A benchmark, with no threat model beyond backends facing untrusted users (§1). threat-models.md does not list it |
| Weakness enumerations | adjacent | CWE-20, CWE-22, CWE-78, CWE-79, CWE-89, CWE-94, CWE-117, CWE-284, CWE-400, CWE-434, CWE-522, CWE-703, CWE-863, LLM09:2025, LLM05:2025 | Its exploits are organized under 13 CWEs, 9 of them in the 2024 CWE Top 25 and 10 within the OWASP Top 10 web risks of 2025 (Table 5). Neither NIST AI 100-2e2025 nor ATLAS 2026.09 cites it (searched 2026-11-01). The OWASP LLM ids are RPT-0014's mapping in sources.md, which also lists four of the CWEs |
| Attack → asset mapping | adjacent | C14, C08 | The weakness originates in an AI coding assistant or agent (C14, C08), the components AIT-131 also names, and lands in application code (A08). The backends themselves sit outside RPT-0014's AI reference architecture. The mapping is ours |
