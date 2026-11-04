---
schema: "library-summary/v1"
id: openai-2023-chatgpt-redis-outage
record: openai-2023-chatgpt-redis-outage
type: summary
updated: "2026-11-02"
---

# March 20 ChatGPT outage: Here's what happened

|  |  |
|---|---|
| **Type** | article (vendor incident report on the company blog) |
| **Maturity** | _unset_ (an incident report; no maturity level applies) |
| **Authors** | OpenAI |
| **Published** | 2023-03-24 |
| **Identifier** | URL only: https://openai.com/blog/march-20-chatgpt-outage |
| **Source** | https://web.archive.org/web/20230326020730id_/https://openai.com/blog/march-20-chatgpt-outage (the Internet Archive's copy of 2023-03-26, original bytes) |
| **Digest** | `sha256:66b92d3b419ebbed42371af8496ed0de160136400b9e8938a351769dda086c0d` (that archived HTML, 68,998 bytes) |

## Overview

OpenAI explains why it took ChatGPT offline on Monday, 20 March 2023. A bug in redis-py,
the open-source Python client for Redis, let some users see the titles of another active
user's chat history, and possibly the first message of a new conversation. The same bug may
have exposed payment details of 1.2% of ChatGPT Plus subscribers active during a nine-hour
window: name, email address, payment address, the last four digits of a card number and its
expiry date, though never a full card number. That could happen through subscription
confirmation emails sent to the wrong users between 1 a.m. and 10 a.m. Pacific time, or on
the "Manage my subscription" page in the same window. OpenAI caches user information in
Redis Cluster and reaches it through redis-py from an asyncio Python server. The client
shares a pool of connections. If a request was cancelled after it was sent but before its
response was read, the connection was left corrupted, and the next, unrelated request on it
could receive the leftover data. Usually that caused a server error, but sometimes the data
had the expected type and was returned as valid. A server change at 1 a.m. on 20 March
caused a spike in cancellations. OpenAI sent the maintainers a patch and lists its own
actions: testing the fix, redundant checks that cached data belongs to the requesting user,
a programmatic log review, identifying and notifying affected users, better logging, and a
sturdier Redis cluster. Chat history was restored except for a few hours.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | A confidentiality failure across users of an AI service, caused by a bug in an open-source dependency, with the mechanism explained |
| Cryptography | `none` | No cryptographic content |
| This project | `adjacent` | The object model has to represent a failure with no attacker: a provider-side bug in a shared cache that hands one user's data to another, traced to a third-party library |

`bears_on: DEC-001a` (the core type system, accepted in ADR-0010).

## Implementations

Searched on 2026-11-02. None applies: this is an incident report. The bug was in redis-py
(MIT, https://github.com/redis/redis-py). NVD tracks it as CVE-2023-28858 (redis-py before
4.5.3; releases 4.3.6, 4.4.3 and 4.5.3 changed pipeline behaviour), whose record cites this
post and says it was first created in response to reports about ChatGPT, and as
CVE-2023-28859 (fixed in 4.4.4 and 4.5.4), which addresses data leakage across asyncio
connections in general. The post itself names no CVE or version.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this document |

## Limits

- **Read from an archive.** openai.com returned HTTP 403 to scripted requests on 2026-11-02.
  The digest is of the Internet Archive's copy from two days after publication; the live
  page may have changed.
- **Hedged numbers.** OpenAI believes very few users' data "was actually revealed to someone
  else" but gives no count beyond the 1.2% share; exposure before 20 March is called possible
  but unconfirmed.
- **The provider's own account.** No independent investigation is cited.
- **"Outage" undersells it.** The title names the downtime; the substance is a data exposure.

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | core | AIT-141 | AIT-141 cites it, and it is the primary source for INC-029. There was no attacker: AIT-141 covers provider bugs that expose prompts and outputs. INC-029 says cancelled requests returned another user's data; per the post, the cancelled request corrupted the connection and the next, unrelated request received the leftover data. INC-029's source note ("fetch returned 403; content confirmed through press") can now point to the archived primary text |
| Existing AI threat models | none | none | An incident report; it models nothing. threat-models.md does not list it |
| Weakness enumerations | adjacent | LLM02:2025, LLM03:2025, CWE-362, CVE-2023-28858, CVE-2023-28859 | Not an enumeration, and neither NIST AI 100-2e2025 nor ATLAS 2026.09 cites it (searched 2026-11-02). NVD's CVE-2023-28858 cites it, and NVD classes the two CVEs as CWE-193 (off-by-one error) and CWE-459 (incomplete cleanup), where RPT-0014's sources.md maps the incident to CWE-362 (race condition). The other ids are RPT-0014's mapping; the CVE ids are ours |
| Attack → asset mapping | core | C07, C13, A07, A14 | Traces the failure through named parts: the asyncio Python server, redis-py's shared connection pool and the Redis Cluster cache of user information (C07 for ChatGPT as an application; C13 from a customer's side, as in AIT-141), and lists exactly what leaked: chat titles and first messages (A07) and payment details (A14). The component and asset mapping is ours |
