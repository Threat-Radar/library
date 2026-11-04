---
schema: "library-summary/v1"
id: microsoft-2016-learning-from-tay
record: microsoft-2016-learning-from-tay
type: summary
updated: "2026-11-02"
---

# Learning from Tay's introduction

|  |  |
|---|---|
| **Type** | article (corporate blog post) |
| **Maturity** | _unset_ (a blog post; no maturity level applies) |
| **Authors** | Peter Lee, Microsoft (the byline now reads Corporate Vice President, Microsoft Healthcare) |
| **Published** | 2016-03-25, Official Microsoft Blog |
| **Identifier** | URL only |
| **Source** | https://blogs.microsoft.com/blog/2016/03/25/learning-tays-introduction/ |
| **Digest** | `sha256:aa1c9483cf09bfda13e569bc5c8039ae90e7d549fdcc4d902542bcb4784e4abe` (the live HTML page on 2026-11-02, 124,665 bytes, including current site navigation) |

## Overview

Two days after launching Tay, a chatbot for 18- to 24-year-olds in the US, on Twitter,
Microsoft apologises for its offensive tweets and explains that Tay is offline. Tay followed
XiaoIce, a chatbot used by some 40 million people in China, and was meant to test whether
such an AI would be as engaging in a very different culture. Microsoft says it built a lot
of filtering, ran user studies with diverse groups and stress-tested Tay before inviting a
wider audience, expecting the AI to improve through interaction. Within the first 24 hours,
a coordinated attack by a subset of users "exploited a vulnerability in Tay", and Tay tweeted
grossly offensive words and images. Microsoft calls this a critical
oversight for this specific attack, takes full responsibility, and says it is fixing the
vulnerability and will bring Tay back only when it can better anticipate malicious intent.
The closing lesson is that AI systems feed off both positive and negative interactions, so
the challenges are as much social as technical, and that doing AI right requires iterating
in public, with caution.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | The vendor's account of an in-the-wild attack that turned a public AI chatbot against its owner, though with no technical detail |
| Cryptography | `none` | No cryptographic content |
| This project | `adjacent` | The object model has to represent an attack by ordinary users through a public channel on a system that changes with interaction, with reputational harm as the impact |

`bears_on: DEC-001a` (the core type system, accepted in ADR-0010).

## Implementations

Searched on 2026-11-02. None applies: this is an incident statement.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this document |

## Limits

- **The vulnerability is never named.** The post does not say what was exploited, how, or
  whether Tay's model was changed by the abuse; it mentions no "repeat after me" feature and
  no learning mechanism beyond expecting the AI to get better through interaction.
- **An apology, not a post-mortem.** It gives no timeline beyond "the first 24 hours", no
  numbers and no description of the fix.
- **A live page.** The digest covers today's HTML, which wraps the 2016 text in current site
  navigation, so it will not match a capture from another day.

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | core | AIT-027 | AIT-027 cites it, and it is the primary source for INC-001, whose quoted sentence matches the post. The post does not say the attack worked by poisoning what Tay learned: AIT-027's online-learning reading rests on secondary accounts such as ATLAS AML.CS0009, which says Tay's machine learning let its conversations influence it directly, and sources.md's "repeat after me" detail is likewise not in the post |
| Existing AI threat models | none | none | An incident statement; it models nothing. threat-models.md does not list it |
| Weakness enumerations | adjacent | AML.CS0009, AML.T0020, AML.T0048, LLM04:2025, ML02, ML08 | ATLAS 2026.09's case study AML.CS0009 (Tay Poisoning) cites it as one of four references, beside the AI Incident Database's incident 6 and AVID-2022-v013. NIST AI 100-2e2025 does not cite it (searched 2026-11-02). The ids are RPT-0014's mapping in sources.md |
| Attack → asset mapping | adjacent | A03, A13 | Names the channel (Twitter) and the harm (offensive tweets and images: model behaviour, A03, and reputation, A13) but no component or mechanism. Mapping it to AIT-027's components (C03, C05) would rest on the secondary accounts, not this post |
