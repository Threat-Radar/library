---
schema: "library-summary/v1"
id: ftc-2025-companion-chatbots-6b
record: ftc-2025-companion-chatbots-6b
type: summary
updated: "2026-11-03"
---

# FTC Launches Inquiry into AI Chatbots Acting as Companions

|  |  |
|---|---|
| **Type** | article (a regulator's press release) |
| **Maturity** | _unset_. A press release announcing a study, not a rule or finding |
| **Authors** | U.S. Federal Trade Commission, Office of Public Affairs. Lead staff are named in the release |
| **Published** | 2025-09-11 |
| **Identifier** | https://www.ftc.gov/news-events/news/press-releases/2025/09/ftc-launches-inquiry-ai-chatbots-acting-companions |
| **Source** | https://web.archive.org/web/20250912065107/https://www.ftc.gov/news-events/news/press-releases/2025/09/ftc-launches-inquiry-ai-chatbots-acting-companions. On 2026-11-03, ftc.gov answered automated clients with 403 or 404, so the Wayback Machine capture from the day after release was used. RPT-0014's fold fetched ftc.gov directly on 2026-10-03 |
| **Digest** | `sha256:10cef210a9af6a401aeedae31a5dd5857b24ebdf765d25690e9e1803559e9107`. This is the capture's HTML after gzip decompression (1,000,070 bytes) |

## Overview

**What the FTC did.** It issued 6(b) orders to seven companies offering consumer AI chatbots: Alphabet, Character Technologies, Instagram, Meta Platforms, OpenAI OpCo, Snap and X.AI. The Commission voted 3–0. A 6(b) study gathers information; it has no specific law-enforcement purpose.

**What it asks.** How the companies:
- make money from user engagement;
- process inputs and generate outputs;
- develop and approve characters;
- measure, test and monitor for negative impacts before and after deployment;
- mitigate harms, especially to children;
- disclose risks and data practices to users and parents;
- enforce age and terms-of-service rules;
- use or share personal information from conversations.

**The stated concern.** Companion chatbots imitate human relationships, which may lead children and teens to trust them and form attachments.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | Consumer safety and privacy regulation, not security attacks |
| Cryptography | `none` | No cryptographic content |
| This project | `adjacent` | Regulatory evidence that consumer-facing chatbot harms are a recognized risk class (RPT-0014's AIT-144). Not a threat-modeling source |

`bears_on: none yet.` The release informs no ARCH-0001 decision or requirement. It is `summarized` because LANES.md requires full summaries for subset-1 sources; no relevance is claimed.

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | adjacent | AIT-144 | **AIT-144 (consumer-facing safety failures with legal exposure):** RPT-0014's catalog lists S-1154 here, and INC-170 is this release. It is a regulatory inquiry, not evidence of an attack or of specific harm; it records questions, not findings |
| Existing AI threat models | none | — | No threat model |
| Weakness enumerations | none | — | No mapping to any weakness enumeration. Neither ATLAS release 2026.09 nor NIST AI 100-2e2025 cites it (checked 2026-11-03) |
| Attack → asset mapping | adjacent | A17, A07, A13; C07, C13 — **ids assigned by us; the concerns are the FTC's** | The FTC names what it is concerned about: children's and teens' wellbeing, personal information from conversations, and providers' compliance with COPPA and their own terms. Our ids: A17 (end-user safety and wellbeing), A07 (user data), A13 (providers' legal standing), C07 (the chatbot application layer), C13 (the model providers) |

## Implementations

Not applicable; this is a regulatory notice. Searched 2026-11-03: nothing to build on.

| Name | Kind | License | URL |
|---|---|---|---|

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | Metadata. `cites` lists the 6(b) orders and the two commissioners' statements linked from the release |
| `summary.md` | This document |

**Reference expansion.** The release links three FTC primary documents.

*Reference-expansion candidates* (1; locator taken from the release page; outcome of the 2026-11-03 review):

| Work | Locator | Outcome |
|---|---|---|
| FTC, 6(b) Orders to File Special Report on advertising, safety and data-handling practices of generative AI companion products | ftc.gov, reports/6b-orders-file-special-report-regarding-advertising-safety-data-handling-practices-companies | created: `ftc-2025-companion-chatbots-6b-orders` |

The two commissioners' statements are kept as `cites` entries only. They are opinions on the same action.

Created stubs are `status: stub` with unwritten summaries; tmodel#81 owns filling them. Candidates marked "not created" were excluded in the consolidated review of 2026-11-03 as unnecessary for RPT-0014: niche, or their attack class is already covered.

## Limits

- **An announcement, not findings.** No company's practices are assessed here, and the study's results, if published, would be a later record.
- **Only seven companies.** Other companion-chatbot operators are not covered.
- **Read from an archived copy.** ftc.gov now refuses automated clients, so the content was read from the Wayback Machine capture of 2025-09-12. It shows the original 2025-09-11 text.
