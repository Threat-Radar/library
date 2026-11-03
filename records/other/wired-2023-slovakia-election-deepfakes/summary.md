---
schema: "library-summary/v1"
id: wired-2023-slovakia-election-deepfakes
record: wired-2023-slovakia-election-deepfakes
type: summary
updated: "2026-11-02"
---

# Slovakia's Election Deepfakes Show AI Is a Danger to Democracy

|  |  |
|---|---|
| **Type** | article (news story) |
| **Maturity** | _unset_ (journalism; no maturity level applies) |
| **Authors** | Morgan Meaker (WIRED) |
| **Published** | 2023-10-03 |
| **Identifier** | URL only |
| **Source** | https://www.wired.com/story/slovakias-election-deepfakes-show-ai-is-a-danger-to-democracy/ |
| **Digest** | `sha256:96e7ed7db712eca635002716f27fd3d21132c00fd9fe6e093ca88cb1cd8e0fb1` (the live HTML page on 2026-11-02, 1,435,418 bytes, including current site navigation) |

## Overview

Two days before Slovakia's 2023 election, an audio recording posted to Facebook seemed to capture Michal Šimečka, leader of Progressive Slovakia, and Monika Tódová
of the daily Denník N discussing how to rig the vote, partly by buying votes from the Roma
minority. Both denounced it as fake, and AFP's fact-checkers found signs of AI manipulation.
Two things made it hard to answer. It appeared during the 48-hour pre-election moratorium,
when media and politicians are meant to stay silent. And as audio it fell outside Meta's
manipulated-media policy, which then covered only faked video. A second fake clip, of Šimečka
promising to double the price of beer, was spreading three days before the vote. The
fact-checking group Demagog, a Meta partner, traced it to an anonymous Instagram account,
consulted experts, ran an ElevenLabs speech classifier, and labelled it as altered after a
few hours. Both clips stayed up on Facebook with fact-check labels, which Meta says also
down-rank them. The
far-right party Republika also posted AI voice impersonations of Šimečka and President
Zuzana Čaputová, with a disclaimer that appears only 15 seconds into a 20-second video.
Progressive Slovakia lost to SMER. Fact-checkers in Slovakia and Poland say they lack
reliable detection tools, and a Polish fact-checker adds that the mere possibility of AI
fakes is already used to discredit genuine material.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | Disinformation built with AI voice cloning against an election, and the gaps in platform policy and detection it exploited; no system is compromised |
| Cryptography | `none` | No cryptographic content (no provenance signing or watermarking is discussed) |
| This project | `adjacent` | The object model has to represent harm to third parties' likeness and reputation from generative-AI misuse, with timing and platform policy as conditions |

`bears_on: DEC-001a` (the core type system, accepted in ADR-0010).

## Implementations

Searched on 2026-11-02. None applies: this is a news story. The one detection tool it names
is ElevenLabs' AI speech classifier, used by Demagog.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this document |

## Limits

- **Fakery is asserted, not shown.** The story relies on the subjects' denials, AFP's
  finding and Demagog's judgement; it gives no forensic detail and does not say who made
  the clips.
- **No measure of reach or effect.** It says nothing on how many people heard the clips or
  whether they changed votes.
- **Written days after the vote.** Later findings are not covered.
- **A live page.** The digest covers today's HTML, so it will not match a capture from
  another day.

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | core | AIT-129 | AIT-129 cites it, and it is the primary source for INC-035. It confirms the three details INC-035 marks as "from recall, not confirmed": release during the 48-hour moratorium, Monika Tódová as the second voice, and the gap in Meta's policy for audio-only fakes. sources.md says wired.com was blocked for WebFetch; the page was fetched on 2026-11-02 |
| Existing AI threat models | none | none | A news story; it models nothing. threat-models.md does not list it |
| Weakness enumerations | none | AML.T0088, LLM09:2025, NISTAML.04 | Not an enumeration, and neither NIST AI 100-2e2025 nor ATLAS 2026.09 mentions the Slovak case (searched 2026-11-02). The ids are RPT-0014's mapping in sources.md |
| Attack → asset mapping | adjacent | C12, A15, A13 | Names the targets (a party leader, a journalist and the president, whose voices were cloned: A15; their reputations: A13), the channels (Facebook, Instagram) and the conditions (the moratorium, the audio gap in Meta's policy), but models no system. The mapping, with C12 as the people targeted and deceived, is ours |
