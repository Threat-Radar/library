---
schema: "library-summary/v1"
id: cccs-itsap-00-041-generative-ai-2025
record: cccs-itsap-00-041-generative-ai-2025
type: summary
updated: "2026-11-15"
lane: catalogs-schema
reviewed_by: ""
---

# Generative artificial intelligence (AI) - ITSAP.00.041

|  |  |
|---|---|
| **Type** | article (government awareness publication, "Awareness series") |
| **Maturity** | _unset — do not guess_ |
| **Authors** | Canadian Centre for Cyber Security |
| **Published** | December 2025 (date modified 2025-12-10); first published July 2023 |
| **Identifier** | ITSAP.00.041; https://www.cyber.gc.ca/en/guidance/generative-artificial-intelligence-ai-itsap00041 |
| **Source** | https://web.archive.org/web/20260908055757id_/https://www.cyber.gc.ca/en/guidance/generative-artificial-intelligence-ai-itsap00041 |
| **Digest** | `cc5530e0ce68a69d54bd655d84cf94571945f2557e25ddf00b5b654bb1d75d91` (the archived page; its body text matches the live page on 2026-11-15) |

## Overview

A one-page awareness note from Canada's national cyber security agency, for organizations and individuals. After a list of uses by sector, it names **eight risks** of generative AI:
1. misinformation and disinformation;
2. phishing;
3. privacy of data put into prompts;
4. malicious code written with AI;
5. buggy code from AI assistance;
6. poisoned training datasets;
7. biased content;
8. loss of intellectual property.

It warns that outputs can be incorrect or biased. The mitigations are general cyber hygiene: MFA, patching, network monitoring and phishing training for organizations, and caution about sharing data and checking content for individuals. Three measures are specific to using generative AI:
- a risk plan with usage policies and security by design across the AI lifecycle;
- choosing a vendor carefully, including asking how its training data was obtained and validated;
- keeping PII and sensitive corporate data out of prompts.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | adjacent | It names risks without mechanisms, mostly AI as the attacker's tool (phishing, malware) and data leakage by users |
| Cryptography | none | No cryptographic content |
| This project | none | Nothing in it shapes tmodel's object model or a decision; it is kept as the source of RPT-0014's TM-056. `bears_on` is empty for that reason |

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | adjacent | AIT-085 | One of AIT-085's three sources (employee disclosure to third-party AI): "Users may unknowingly provide sensitive corporate data or ... PII in their AI queries". It reports no incident |
| Existing AI threat models | adjacent | TM-056 | TM-056's source. TM-056's "eight organizational GenAI risks" and its category list match the page. It is a risk list, not a threat model: there are no assets, actors or paths beyond those names |
| Weakness enumerations | none | LLM02:2025, LLM04:2025, LLM09:2025, NISTAML.04 | It cites no catalog. The ids are `sources.md`'s mapping. Privacy of data, poisoned datasets and content accuracy fit them, but phishing, malicious code and buggy code, three of its eight, are AI-enabled offense or developer error, which those ids don't cover |
| Attack → asset mapping | adjacent | C12, C13, C01, A07, A02, A13 | Read for the user side: employees (C12) sending data to third-party AI (C13), and open-Internet training data (C01). The assets named are corporate data and PII (A07), intellectual property (A02) and reputation (A13). The mapping is ours |

## Implementations

None, searched 2026-11-15: awareness guidance, not software.

| Name | Kind | License | URL |
|---|---|---|---|

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, digest and `cites` |
| `summary.md` | this summary, with the RPT-0014 applicability table |

## Reference expansion

The page's "Learn more" list has six of the Cyber Centre's own publications, checked against `sources.md` and the library on 2026-11-15. None is in `sources.md`.
- **Missing and in scope, added as a stub (1):** *Artificial Intelligence* (ITSAP.00.040), the companion awareness note on AI in general: `cccs-itsap-00-040-artificial-intelligence-2025`.
- **Out of scope (5):** MFA (ITSAP.30.030), network logging and monitoring (ITSAP.80.085), misinformation (ITSAP.00.300), phishing (ITSAP.00.101) and vishing (ITSAP.00.102). These are general cyber hygiene and say nothing AI-specific.

## Limits

- **A refresh, not a rewrite.**
  - Compared with the July 2023 version (Wayback copy of 2023-07-24), the eight risks and the organizational mitigations are unchanged in substance. The sector list grew, and individuals got "Be cautious when sharing data".
  - "Select training datasets carefully" became "Select your vendor carefully": the advice moved from building your own datasets to asking a provider about theirs.
  - The December 2025 text still names Google's LaMDA and Bard among current tools.
- **No mechanisms.** Poisoning is "inject malicious code into the dataset", with no route, scale or evidence. The page cites no sources.
- **Typed as an article, not a standard.** `sources.md` gives S-0846 the type "standard", but an awareness note sets no requirements. So it isn't a `spec` here, and FX-1 doesn't apply.
- **Read from an archive.** The Wayback copy of 2026-09-08 was read and compared with the live page, whose body text matched.
