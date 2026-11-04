---
schema: "library-summary/v1"
id: cnn-2024-deepfake-cfo-hong-kong
record: cnn-2024-deepfake-cfo-hong-kong
type: summary
updated: "2026-11-02"
---

# Finance worker pays out $25 million after video call with deepfake 'chief financial officer'

|  |  |
|---|---|
| **Type** | article (news story) |
| **Maturity** | _unset_ (journalism; no maturity level applies) |
| **Authors** | Heather Chen, Kathleen Magramo (CNN) |
| **Published** | 2024-02-04 |
| **Identifier** | URL only |
| **Source** | https://www.cnn.com/2024/02/04/asia/deepfake-cfo-scam-hong-kong-intl-hnk |
| **Digest** | `sha256:05dbbbff34398557da45720e0c0f3a8364b6e934d748ecac3a5aa69d66ac22ba` (the live HTML page on 2026-11-02, 4,599,229 bytes, including current site navigation) |

## Overview

CNN reports what Hong Kong police said at a briefing on Friday 2 February 2024. A finance
worker at a multinational firm received a message, purportedly from the company's UK-based
chief financial officer, about a secret transaction, and at first suspected phishing. He set
his doubts aside after a video conference in which the other participants looked and
sounded like colleagues he knew; according to Senior Superintendent Baron Chan
Shun-ching, every one of them was a deepfake. He remitted a total of HK$200 million, about
US$25.6 million, and the fraud came to light only when he later checked with head office.
The police named neither the company nor the worker. At the same briefing they reported six
arrests linked to such scams and, separately, that eight stolen Hong Kong identity cards were
used for 90 loan applications and 54 bank-account registrations between July and September
2023, with AI deepfakes fooling facial recognition at least 20 times by imitating the card
holders. The story closes with wider concern about deepfakes, citing the AI-generated
explicit images of Taylor Swift that spread in late January 2024.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Social engineering with real-time deepfake video that defeated a payment process, plus deepfakes that fooled facial recognition |
| Cryptography | `none` | No cryptographic content |
| This project | `adjacent` | The object model has to represent people and payment processes as targets of synthetic likenesses, with the out-of-band check that finally exposed the fraud as the missing control |

`bears_on: DEC-001a` (the core type system, accepted in ADR-0010).

## Implementations

Searched on 2026-11-02. None applies: this is a news story.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this document |

## Limits

- **Second-hand.** It reports the police briefing and an RTHK interview; it has no
  independent sources and no account from the company.
- **No technique.** It does not say how the deepfakes were made, whether they were live or
  pre-recorded, or whether the worker spoke with them.
- **The company is not named.** RPT-0014 records that Arup was named as the victim in May
  2024, after this story.
- **A live page.** The digest covers today's HTML, so it will not match a capture from
  another day.

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | core | AIT-127, AIT-010 | AIT-127 cites S-1130, and this story is the press source named in INC-041 (S-1130 also counts the police briefing, Arup's confirmation and a PRMIA case study). It supports INC-041's account of the message, the all-deepfake call and the HK$200 million (about US$25.6 million). It does not name Arup, give INC-041's "15 transfers to 5 local accounts", or say this case's deepfakes were built from public footage: it says that of several recent episodes in general. AIT-010 is ours: deepfakes that fooled facial recognition with stolen identity cards, from the same briefing |
| Existing AI threat models | none | none | A news story; it models nothing. threat-models.md does not list it |
| Weakness enumerations | none | AML.T0052, AML.T0048, ASI09 | Not an enumeration, and neither NIST AI 100-2e2025 nor ATLAS 2026.09 cites it (searched 2026-11-02); ATLAS's AML.T0052.001 (Deepfake-Assisted Phishing) cites the same case through the AI Incident Database's incident 634. The ids are RPT-0014's mapping in sources.md |
| Attack → asset mapping | adjacent | C12, A14, A15 | Names the target (a finance worker authorising transfers: C12 and A14), the impersonated executives' likenesses (A15), the channel (a message, then a video conference) and the control that worked late (checking with head office), but models no system. The mapping is ours |
