---
schema: "library-summary/v1"
id: gtig-adversarial-misuse-2025
record: gtig-adversarial-misuse-2025
type: summary
updated: "2026-11-03"
---

# Adversarial Misuse of Generative AI

|  |  |
|---|---|
| **Type** | paper (a threat-intelligence report) |
| **Maturity** | _unset_. A vendor threat-intelligence report; no standing is asserted |
| **Authors** | Google Threat Intelligence Group (GTIG): Mandiant Intelligence and the Threat Analysis Group. No individual authors are named |
| **Published** | Report dated January 2025, published 2025-01-29 with a companion Google Cloud blog post (`datePublished` 2025-01-29) |
| **Identifier** | Blog post (the RPT-0014 URL): https://cloud.google.com/blog/topics/threat-intelligence/adversarial-misuse-generative-ai |
| **Source** | https://services.google.com/fh/files/misc/adversarial-misuse-generative-ai.pdf, the full report linked from the blog post |
| **Digest** | `sha256:6eaf9782e628ed2c444153f4a25d76ab4ae1235127ca2c1d97418e1f6dfc44eb` (921,995 bytes, 32 pages, retrieved 2026-11-03). The blog post as served hashed to `f6a53404…` on the same date |

## Overview

**What it studies.** How government-backed hacking groups (APT) and influence-operation (IO) actors used the Gemini web app. GTIG identified them through its own threat-actor tracking, and analysed their prompts with analysts plus an LLM.

**Main conclusion.** Generative AI made these actors faster, but gave them no new capability.

**Key findings.**
- *Jailbreaks:* actors made only a few low-effort attempts using public jailbreak prompts, and all failed. There were no original or persistent prompt attacks.
- *APT use:* groups from more than 20 countries, used for research, troubleshooting code, reconnaissance, vulnerability research and post-compromise help.
  - Iran: over 10 groups, the heaviest users; APT42 focused on phishing content.
  - China: over 20 groups.
  - North Korea: included drafting cover letters, likely to place clandestine IT workers.
  - Russia: limited use.
- *IO use:* research, personas, translation and content. Iranian IO actors account for about three-quarters of IO use.
- *Abuse of Google itself:* attempts at Gmail phishing, a Chrome infostealer and account-verification bypass all failed.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Primary in-the-wild evidence of how state actors use a frontier LLM |
| Cryptography | `none` | No cryptographic content |
| This project | `adjacent` | Calibrates likelihood for misuse classes in RPT-0014. It shows observed uplift is modest. Not a threat-modeling source |

`bears_on: none yet.` The report informs no ARCH-0001 decision or requirement. It is `summarized` because LANES.md requires full summaries for subset-1 sources; no relevance is claimed.

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | core | AIT-129; AIT-126, AIT-122, AIT-128; AIT-073 | **AIT-129 (AI-generated influence operations):** IO actors used Gemini for content, personas and translation. RPT-0014's catalog lists S-1027 here, and INC-073 is this report. **AIT-126 (AI-written phishing), AIT-122 (AI-accelerated vulnerability research) and AIT-128 (North Korea's IT-worker cover letters):** observed APT uses. **AIT-073 (manual jailbreaks):** only failed attempts with public prompts. All of this is in-the-wild, but it is AI used as a tool; the report found no attack on the model itself |
| Existing AI threat models | none | — | It refers to Google's Secure AI Framework (SAIF) risk taxonomy for AI-focused threats but does not apply it as a threat model |
| Weakness enumerations | adjacent | AML.T0054 — **concept-level, our mapping** | Neither ATLAS release 2026.09 nor NIST AI 100-2e2025 cites the report (checked 2026-11-03). Most activity is misuse of AI as a tool, which these catalogs barely enumerate |
| Attack → asset mapping | none | — | The targets are third parties and Google's other products, reached through ordinary cyber operations. The report maps nothing to AI system assets |

## Implementations

Searched 2026-11-03. Nothing to build on: this is a threat-intelligence report. Google points to SAIF and its responsible-AI toolkits.

| Name | Kind | License | URL |
|---|---|---|---|

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | Metadata. `cites` lists the SAIF taxonomy the report refers to |
| `summary.md` | This document |

**Reference expansion.** The report cites few primary sources: SAIF (already in `sources.md`, S-0260 and related), other threat-intelligence reports, and Google product pages. **No stubs are proposed.**

## Limits

- **One vendor, one product, about its own model.** It covers only the Gemini web app, as seen by Google. Its conclusion that Gemini's safeguards held is the vendor's own assessment.
- **Visibility is limited to known actors.** Activity is tied to actors GTIG already tracks; unattributed or unknown actors are not counted.
- **Few numbers.** Counts are given as "more than" or "over" by country, with no prompt volumes or success rates.
- **A point in time** (late 2024). GTIG itself expects the picture to change as agentic systems spread. Later GTIG reports should be checked before relying on this one.
