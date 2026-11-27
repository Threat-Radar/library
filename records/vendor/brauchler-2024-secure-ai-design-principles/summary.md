---
schema: "library-summary/v1"
id: brauchler-2024-secure-ai-design-principles
record: brauchler-2024-secure-ai-design-principles
type: summary
updated: "2026-11-26"
lane: catalogs-schema
reviewed_by: ""
---

# Analyzing Secure AI Design Principles

|  |  |
|---|---|
| **Type** | article (vendor research blog post) |
| **Maturity** | _unset — do not guess_ |
| **Authors** | David Brauchler (NCC Group) |
| **Published** | no date on the page; the Wayback Machine lists the URL from 2024-12-11 |
| **Identifier** | https://www.nccgroup.com/research/analyzing-secure-ai-design-principles/ |
| **Source** | https://web.archive.org/web/20250702003120id_/https://www.nccgroup.com/us/research-blog/analyzing-secure-ai-design-principles/ |
| **Digest** | `54b92faaa6cac27f19ace2f5762841ce4028f7cf7cc0db9c6690115a32708037` (the archived bytes, gzip; see `record.yaml` for the decompressed HTML's digest) |

## Overview

The follow-up to `brauchler-2024-ai-application-threat-models`, turning its threat model into design rules. The problem it starts from is that teams treat content filtering ("guardrails", jailbreak prevention) as if it were secure design. NCC's red teamers keep finding a centralized pattern: one LLM that can call any function in any context.

Its picture of an LLM is "an overenthusiastic, overconfident intern", and its rules are:
- **Data-code separation:** a model with trusted functions reads only trusted data. A model that must read untrusted data has every other capability turned off at prompt time.
- **Least privilege, decided at runtime:** a model's trust changes with what it has read. This "capability shifting" is called a primary control, "not merely a defense-in-depth measure".
- **Data pollution:** a model takes the trust level of the least-trusted source in its prompt. That trust flows "downstream" to any model that reads its output, and through the conversation history.
- **Authorization controls:** pass the user's own session token with the model's function call ("fail-closed"), rather than checking the model's scope after the call.
- **Minimal delegation:** keep work that ordinary code can do, and arguments such as the target user id, away from the model.
- **Human in the loop:** confirm write operations through something the agent does not control.
- **Fault tolerance:** where life is at stake, such as in vehicles or OT, a model must not be the only safeguard. Sensors, plain algorithms and people must be able to override it.

It also names the indirect form of prompt injection **Cross-User Prompt Injection**, by analogy with XSS.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | Architectural controls for LLM agents, framed against prompt injection and excessive agency |
| Cryptography | none | No cryptographic content |
| This project | adjacent | The data-pollution rule is a graph rule: a model node's trust is the minimum over its input edges, and the result flows to downstream models. tmodel could compute it over components and data flows (**DEC-001**), as report.md's TrustBoundary row proposes. The fault-tolerance rule applies directly to the automotive examples: a model must not be the only safeguard of a safety function |

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | none | AIT-091 | No attack is reported. AIT-091 lists S-0742, and this post's cross-user prompt injection and excessive agency are that technique's preconditions. |
| Existing AI threat models | core | TM-027 | The seven principles TM-027 lists come from this post. It has an eighth that TM-027 leaves out, Designing for Fault Tolerance, about safety-critical systems. That one bears most on tmodel's automotive domain |
| Weakness enumerations | none | — | No catalog ids. "Cross-User Prompt Injection" is the author's name for OWASP's indirect prompt injection (LLM01:2025), which a naming crosswalk should record. Neither ATLAS 2026.09 nor NIST AI 100-2e2025 cites it (searched 2026-11-15) |
| Attack → asset mapping | adjacent | C07, C08, C09, C11, C12, C16, A07, A09, A12 | The controls sit on named parts: prompt assembly (C07), the agent loop (C08), function calls (C09), the user's session token passed with them (C11), human confirmation (C12), and the safety-critical edge (C16). They protect user data (A07), credentials (A09) and physical safety (A12). The mapping is ours |

## Implementations

Searched 2026-11-15: none. It promises a successor post with design patterns, which was not searched for.

| Name | Kind | License | URL |
|---|---|---|---|

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata and digest |
| `summary.md` | this summary, with the RPT-0014 applicability table |

## Reference expansion

The post's only cited work is its predecessor, `brauchler-2024-ai-application-threat-models`, which is S-0742's other half. It has no other references.

## Limits

- **Principles, not a method.** Each rule comes from one worked analogy (an intern, a comptroller and a malicious vendor), with no case data and no test of whether a design meets it.
- **Undated.** The page shows no date. 2024 is the Wayback Machine's first listing (2024-12-11), and the post could be older.
- **The successor wasn't checked.** Patterns promised for "later articles" may refine these rules.
- **Read from an archive.** The pinned 2025-07-02 copy is retained. On 2026-11-26 the recorded `/research/analyzing-secure-ai-design-principles/` URL serves the article again; it is no longer a redirect to the general research landing page.
