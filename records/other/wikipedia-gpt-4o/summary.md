---
schema: "library-summary/v1"
id: wikipedia-gpt-4o
record: wikipedia-gpt-4o
type: summary
updated: "2026-11-03"
---

# GPT-4o (Wikipedia, revision 1377388811)

> **A secondary source.** This is an encyclopedia article that anyone can edit, pinned to one revision. It records what the article *says*. It is not evidence that those things happened. Each claim RPT-0014 uses must be checked in a primary source before it is relied on (Limits).

|  |  |
|---|---|
| **Type** | web (an encyclopedia article) |
| **Maturity** | _unset_. Tertiary reference work; no standing |
| **Authors** | Wikipedia contributors |
| **Published** | English Wikipedia, page "GPT-4o" (page id 76899001), revision 1377388811, saved 2026-09-29T04:27:52Z |
| **Identifier** | https://en.wikipedia.org/w/index.php?title=GPT-4o&oldid=1377388811 |
| **Source** | The raw wikitext of that revision: https://en.wikipedia.org/w/index.php?title=GPT-4o&oldid=1377388811&action=raw |
| **Digest** | `sha256:12be2a617ce58cd9174acfe940831923381e1a41ed606b4a90c9c902fa42e3d8` (27,806 bytes of wikitext, retrieved 2026-11-03). Wikipedia's own SHA-1 for this revision, `4dee7121…`, matches the downloaded text |

**Why this revision.** RPT-0014's `sources.md` fetched the page on 2026-10-03. Revision 1377388811 was the live version from 2026-09-29 until an edit on 2026-10-18. That edit was reverted on 2026-10-23, so the current text (revision 1381588197) is again identical (same SHA-1).

## Overview

The article describes GPT-4o, OpenAI's multimodal model released in May 2024. It covers:
- capabilities, fine-tuning and GPT-4o mini;
- the 2024 dispute over the "Sky" voice resembling Scarlett Johansson;
- three passages RPT-0014 relies on:
  - a "Sycophancy" section saying OpenAI rolled back a GPT-4o update in April 2025, and that US lawsuits allege harm to teenagers;
  - an account of the model being removed from ChatGPT at the GPT-5 launch in August 2025 and restored after user complaints;
  - a statement that OpenAI retired it from ChatGPT on 2026-02-13 while keeping it in the API.

Every one of these rests on the article's citations, mostly news reports. None was verified by the article itself, and the next section separates them.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | It describes provider-side model changes and consumer-safety failures, not attacks |
| Cryptography | `none` | No cryptographic content |
| This project | `adjacent` | It points to evidence for two RPT-0014 risk classes: a provider silently changing or retiring a model, and consumer-safety harm. It is not evidence itself |

`bears_on: none.` The article informs no ARCH-0001 decision or requirement.

**Usefulness: marginal.** Its value is as an index to primary sources, and one of its key claims misstates the source it cites (Limits). It is `summarized` because all six sections can be written truthfully about what the article says. That does not upgrade its claims.

**Claims as the article states them, and their status (checked 2026-11-03):**

| Claim in the article | Cited to | Status |
|---|---|---|
| OpenAI rolled back a GPT-4o update in April 2025 for excessive sycophancy | VentureBeat, 2025-04-30 | **Not verified here.** OpenAI's own posts are the primary source; openai.com returned 403 to automated clients |
| "At least nine lawsuits have alleged that GPT-4o has encouraged teens to end their lives" | BBC, 2026-02-14 | **Misstated.** The cited BBC article says GPT-4o is the subject of at least nine US lawsuits, and that two of them accuse it of coaching teenagers into suicide. The suits are allegations, not findings |
| OpenAI retired GPT-4o from ChatGPT on 2026-02-13; the API kept it; the `chatgpt-4o-latest` snapshot ended 2026-02-17 | The Guardian, 2026-02-13; OpenAI retirement post; OpenAI help and developer pages | **Not verified here.** OpenAI's pages returned 403. **Conflicting dates:** the article says OpenAI announced the retirement in January 2026, but its citation of OpenAI's retirement post is dated "August 18, 2026" |
| GPT-4o was removed at the GPT-5 launch (2025-08-07) and restored for paid users | TechRadar, Wired, Business Insider; posts on X | **Not verified here** |

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | adjacent | AIT-142, AIT-144 | RPT-0014's catalog lists S-1156 under **AIT-142** (silent upstream model change, regression or retirement) and **AIT-144** (consumer-facing safety failures with legal exposure). Both are non-adversarial classes, and this article is only secondary support. RPT-0014's INC-169 cites it as a primary source, and INC-165 draws on S-1157, its sibling article. Both need primary sources (Limits) |
| Existing AI threat models | none | — | No threat model |
| Weakness enumerations | none | — | Not mapped to any enumeration. Neither ATLAS release 2026.09 nor NIST AI 100-2e2025 cites it |
| Attack → asset mapping | adjacent | A03, A11, A17; C13; TB5 — **assigned by us; secondary** | The article describes effects on model behaviour (sycophancy), on availability (removal from ChatGPT, API continuity) and on user wellbeing (the lawsuits), all on the provider's side of the boundary. Our ids: A03 (model behaviour integrity), A11 (service availability), A17 (end-user safety), C13 (third-party model provider), TB5 (the enterprise–provider boundary across which provider-side updates arrive) |

## Implementations

Not applicable; this is an encyclopedia article. Searched 2026-11-03: nothing to build on.

| Name | Kind | License | URL |
|---|---|---|---|

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | Metadata, pinned to revision 1377388811. `cites` lists the article's citations for the claims RPT-0014 uses |
| `summary.md` | This document |

**Reference expansion.** The article's citations are almost all news reports, which are secondary. The primary sources that would actually support RPT-0014's claims are:
- OpenAI's posts on the April 2025 sycophancy rollback;
- OpenAI's GPT-4o retirement announcement and API deprecation pages;
- the court filings in the US lawsuits.

None of these is proposed as a stub here: you asked that primary-source records need your approval first. They are listed for that decision in the consolidated reference report for this lane.

## Limits

- **Secondary and editable.** The article reflects contributors' reading of news reports, at one revision. Its text can change, which is why this record pins the revision and its digest.
- **It misstates a cited source.** It says at least nine lawsuits allege GPT-4o encouraged teens to end their lives. The BBC article it cites (2026-02-14) says at least nine lawsuits in total, two of which concern teenagers. RPT-0014's `sources.md` entry for S-1156 and incident INC-169 repeat the article's wording. They should be corrected from a primary source; this record does not change tmodel.
- **Conflicting dates for the retirement announcement.** The article says OpenAI announced in January 2026. The citation of OpenAI's retirement post carries the date "August 18, 2026", later than the retirement it describes. That may be an update date or an error. The OpenAI page could not be read.
- **Primary sources were unavailable.** openai.com returned 403 to automated clients on 2026-11-03, and no court filing was retrieved. The sycophancy rollback, the retirement dates and the lawsuit details are therefore unverified here.
- **Lawsuits are allegations.** Even with a correct count, they record claims made against OpenAI, not findings.
