---
schema: "library-summary/v1"
id: google-2024-ai-overviews-satire-retrieval
record: google-2024-ai-overviews-satire-retrieval
type: summary
updated: "2026-10-13"
---

# AI Overviews: About last week

|  |  |
|---|---|
| **Type** | article (vendor blog post) |
| **Maturity** | _unset — do not guess_ |
| **Authors** | Elizabeth Reid, VP Search (Google) |
| **Published** | 2024-05-30, Google blog |
| **Identifier** | Google Keyword blog |
| **Source** | https://blog.google/products/search/ai-overviews-update-may-2024/ |
| **Digest** | `7f7a694d476425632bb88605cece8645290992d2f92b7b85e7d38af7ab7e4d96` (HTML as fetched; living page) |

## Overview

Google's explanation of why **AI Overviews** in Search gave odd or wrong answers shortly after their U.S. launch (May 2024). Causes it names: **"data voids"** — queries with little high-quality content, where **satirical** pages (e.g. advice to eat rocks, republished on a company site) became the source — and **sarcastic or troll forum posts** (e.g. glue on pizza) treated as advice; it also notes many shared screenshots were faked. Google describes **more than a dozen technical fixes**: better detection of nonsensical queries, limits on satire and user-generated content, triggering restrictions where overviews were not helpful, and stronger guardrails for news and health topics.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | adjacent | A retrieval-integrity failure at scale, not an attack. |
| Cryptography | none | Not about cryptography. |
| This project | adjacent | Adjacent: shows untrusted retrieved content steering output without an attacker — the same channel attackers exploit. |

Bears on **DEC-001** (object model — retrieval sources and their trust).

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | adjacent | AIT-090, AIT-116 | Untrustworthy retrieval (data voids) and misinformation acted upon — non-adversarial |
| Existing AI threat models | none | — | A vendor post-mortem |
| Weakness enumerations | adjacent | AML.T0070, LLM08:2025, LLM09:2025 | Catalog entries for RAG/misinformation weaknesses |
| Attack → asset mapping | adjacent | C01, C06, C17 | Web sources, retrieval layer, users relying on the answer |

## Implementations

Fixes are inside Google Search. Searched 2026-10-13.

| Name | Kind | License | URL |
|---|---|---|---|


## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this summary |

## Limits

- **The vendor's own account;** no independent measurement of the fixes.
- **Not an attack,** though the same weakness is exploitable.
- Incident INC-055 in RPT-0014.
