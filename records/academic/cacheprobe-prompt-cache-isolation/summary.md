---
schema: "library-summary/v1"
id: cacheprobe-prompt-cache-isolation
record: cacheprobe-prompt-cache-isolation
type: summary
updated: "2026-11-02"
---

# CacheProbe: Auditing Prompt Cache Isolation in Gateway APIs

|  |  |
|---|---|
| **Type** | paper (SAGAI '26; arXiv preprint); **stub**: pinned, partly read |
| **Authors** | Fahey (Northeastern University) |
| **Published** | arXiv 2605.30613v1, 2026-05-28; "Accepted at SAGAI '26 (Workshop on Secure Agents for Generative AI), co-located with IEEE Symposium on Security and Privacy 2026" (arXiv comment) |
| **Source** | https://arxiv.org/pdf/2605.30613v1 |
| **Digest** | `3a756ca946b65d2f2d5c9205fe3677b6ada72d12a897a33eb25c7f0b9553a4e2` |

## Overview

Asks whether an LLM API gateway (OpenRouter) breaks the prompt-cache isolation
that inference providers give each account. The paper detects cache hits two
ways, from timing differences and from the cached-token counts some providers
report. It concludes that OpenRouter's "use of shared organizational
credentials enables cross-account cache sharing that would not occur when
accessing providers directly": all three providers tested showed cache
sharing in OpenRouter's default mode, and isolated caches when called
directly or through OpenRouter's bring-your-own-key mode (§VIII). Its
recommendation is per-user cache isolation at the gateway.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | A privacy attack on shared LLM infrastructure, through timing and metadata side channels |
| Cryptography | `none` | |
| This project | `adjacent` | An AI threat that sits in the serving infrastructure, not in the model or the application |

`bears_on: DEC-001`. RPT-0009 attack classes it touches: privacy (other users'
prompts become observable), carried by a conventional side channel in the
gateway.

## Status

A stub for tmodel #189 (2026-11-02), added because the RPT-0009 Phase 4
review (finding F-07) found the SAGAI'26 papers missing. The abstract, the
section headings, the results (§VI) and the conclusion (§VIII) were read.

## Limits

- One gateway and three providers, measured at one point in time. The
  providers' and the gateway's behavior may have changed since.
- The methodology and statistics (§IV to §VI) were not checked.
