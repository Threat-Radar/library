---
schema: "library-summary/v1"
id: owasp-nhi-top10-2025
record: owasp-nhi-top10-2025
type: summary
updated: "2026-11-15"
lane: catalogs-schema
reviewed_by: ""
---

# OWASP Top 10 Non-Human Identities Risks - 2025

|  |  |
|---|---|
| **Type** | web (an OWASP Top 10 list, published as a MkDocs site from GitHub) |
| **Maturity** | _unset — do not guess_ |
| **Authors** | OWASP Non-Human Identities Top 10 project |
| **Published** | released 2024-12-09, live 2024-12-24 (release notes); read at repository commit `16f8b793` (2026-07-02) |
| **Identifier** | https://owasp.org/www-project-non-human-identities-top-10/ (the 2025 list is served at owasp.github.io) |
| **Source** | `2025/docs/top-10-2025.md` at commit `16f8b79394662c6467eb7a1907b6af7e209b1fd9` (CC BY-SA 4.0) |
| **Digest** | `772f6f8c259320124b7780d6aa8d365e38ee3f24af21a48c631c8e7000f4e46d` (that file) |

## Overview

A ranked list of the ten most serious risks of **non-human identities (NHIs)**: the service accounts, roles, API keys, tokens and OAuth apps that software uses to reach other software. The ten:
1. NHI1 Improper Offboarding;
2. NHI2 Secret Leakage;
3. NHI3 Vulnerable Third-Party NHI;
4. NHI4 Insecure Authentication;
5. NHI5 Overprivileged NHI;
6. NHI6 Insecure Cloud Deployment Configurations;
7. NHI7 Long-Lived Secrets;
8. NHI8 Environment Isolation;
9. NHI9 NHI Reuse;
10. NHI10 Human Use of NHI.

Each risk page has the same parts: a rating row, a description, example attack scenarios, prevention, references and "data points".

**How it ranks.** The team drafted 12 risks from incidents of the previous three years, NVD CVSS scores and surveys (CSA's 2024 NHI report, Datadog, Verizon DBIR). It rated each on OWASP's Risk Rating Methodology: exploitability, prevalence, detectability and technical impact, each 1–3. Then it took a weighted average. The weights and scores are in a Google spreadsheet. NHI1 and NHI2 rate Easy / Widespread or Common / Hard / Severe. NHI9 and NHI10 have Low technical impact.

The list was released in December 2024 and is still edited. NHI3 gained the Salesloft Drift OAuth-token case on 2026-01-13, and a detection-resources page appeared in June 2026.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | An identity and credential risk list, with incidents and controls for each item |
| Cryptography | none | Keys and tokens appear only as secrets to manage. There is no cryptographic design |
| This project | adjacent | An agent's tool credentials and OAuth grants are NHIs, so these ten are weakness types tmodel would attach to an agent or integration Component and its credential asset (**DEC-001**). The list itself never discusses AI |

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | adjacent | AIT-100, AIT-113, AIT-138 | A source for all three: credential harvesting from agent configs, LLMjacking with stolen keys, and orphaned agents and NHIs. Its own incidents are mostly not AI. The AI ones are the Microsoft AI researchers' SAS token (INC-037), Hugging Face Space secrets, the Rabbit R1 keys, and Salesloft Drift's AI chat-agent tokens (INC-111) |
| Existing AI threat models | none | — | A risk list with no system model. `threat-models.md` doesn't list it |
| Weakness enumerations | core | NHI1–NHI10; AML.T0055, AML.T0083, AML.T0098, ASI03, CWE-798, CWE-522 | An enumeration of 10 ids (`NHIn:2025`), as `enumerations.md` records. The ATLAS, OWASP agentic and CWE ids are `sources.md`'s mapping: Unsecured Credentials, Credentials from AI Agent Configuration, AI Agent Tool Credential Harvesting, hard-coded credentials and unprotected credentials. The list itself cites no catalog ids. Neither ATLAS 2026.09 nor NIST AI 100-2e2025 cites it (searched 2026-11-15) |
| Attack → asset mapping | core | C11, C14, C15, C09, A09, A10, A07 | Every risk sits on the identity layer (C11). The scenarios name the places NHIs live: CI/CD and IDE extensions (C14), cloud and Kubernetes control planes (C15), and third-party SaaS integrations (C09). The asset is the credential (A09), and through it hosts (A10) and data (A07). The mapping is ours |

## Implementations

Searched 2026-11-15. Its detection-resources page lists one tool:

| Name | Kind | License | URL |
|---|---|---|---|
| abhishek20c/gh-iga | GitHub identity-governance scanner: GitHub Apps, deploy keys and Actions secrets, mapped to NHI1, NHI3, NHI5 and NHI7 | MIT | https://github.com/abhishek20c/gh-iga |

The prevention text points to secret managers, such as HashiCorp Vault, AWS Secrets Manager and Azure Key Vault, and to OWASP WrongSecrets. These are general tools, not built for this list.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, digest, commit and `cites` |
| `summary.md` | this summary, with the RPT-0014 applicability table |

## Reference expansion

The ten risk pages and the method pages have 63 unique links, checked against `sources.md` and the library on 2026-11-15. RPT-0014's scope is AI, so only the AI-related ones are in scope:
- **In `sources.md` (3):** Wiz on the 38 TB exposed by Microsoft AI researchers (S-0977), Hugging Face's Space secrets disclosure (S-1092), and GTIG on Salesloft Drift (S-1105).
- **Covered by another source (1):** Unit 42's Salesloft Drift threat brief, the same incident as S-1105 (INC-111).
- **Missing, added as a stub (1):** Doppler's running list of 2024 breaches from leaked secrets, `doppler-2024-data-breaches-caused-by-leaks`. NHI7 cites it for the Rabbit Inc. (R1) API key leak, its only AI-product entry.
- **The tool (1):** gh-iga, under Implementations.
- **Not works to stub (4):** a link to the list's own NHI2 page, the NVD home page, and the project's two Google working documents (a breach list and the score spreadsheet).
- **Out of scope (53):**
  - non-AI incidents: Midnight Blizzard, Okta, Internet Archive, CircleCI, Uber, Cloudflare, Snowflake, Sisense, the `.env` extortion, JetBrains, VS Code extensions, Verkada, Azure Site Recovery, Chronicle and others;
  - vendor documentation and OWASP cheat sheets;
  - the IETF OAuth security draft;
  - cloud-security surveys: Datadog, CSA, Verizon DBIR, Orca and Anetac.

## Limits

- **Not about AI.** No page discusses AI, LLMs or agents. The only mention is a link title ("Microsoft AI researchers"), and NHI3 never says Drift is an AI chat agent. Its use to RPT-0014 depends on treating agents as NHIs, which RPT-0014 does (AIT-100, AIT-138) and the list doesn't.
- **The ranking can't be checked.** The weights and scores are in a Google spreadsheet, and the breach list in a Google document. Neither is archived with the site. The four ratings on each page are visible, but not how they combine.
- **Mostly vendor sources.** Many incident write-ups are one project member's Medium posts or vendor blogs. Several data points come from a single 2024 survey (CSA's).
- **A living page under a fixed name.** "2025" content changed in 2026, for example NHI3's Drift case and the detection page. The commit pin fixes what was read; the site will drift.
