---
schema: "library-summary/v1"
id: lenovo-lena-xss-2025
record: lenovo-lena-xss-2025
type: summary
updated: "2026-10-13"
---

# Critical flaw plagues Lenovo AI chatbot: attackers can run malicious code and steal cookies

|  |  |
|---|---|
| **Type** | article (news / research report) |
| **Maturity** | _unset — do not guess_ |
| **Authors** | Cybernews Research team |
| **Published** | 2025-08-18, Cybernews (per `sources.md`) |
| **Identifier** | Cybernews article; MITRE ATLAS case study AML.CS0060 (per `sources.md`) |
| **Source** | https://cybernews.com/security/lenovo-chatbot-lena-plagued-by-critical-vulnerabilities/ |
| **Digest** | `not fetched` (site refuses automated access (HTTP 403); not read in this pass) |

## Overview

**Not yet read** — Cybernews refuses automated access, so this record is a placeholder from the team's round-1 catalog (`incidents.md` INC-113), not verified here. As catalogued: a single ~400-character prompt asked **Lena**, Lenovo's GPT-4-based support chatbot, a product question and told it to format the answer as **HTML with an image tag whose error handler sends cookies** to an attacker. Because the output was rendered unsanitised, the payload ran — including when **support agents** opened the conversation — enabling **session hijacking** (prompt injection → improper output handling → stored XSS). MITRE ATLAS records it as case study AML.CS0060.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | Real-world prompt injection reaching a classic web sink. |
| Cryptography | none | Not about cryptography. |
| This project | core | A clear two-step attack path (injection → unsafe rendering) on a deployed product. |

Bears on **DEC-001**. Status `queued` until the article is read.

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | not assessed | AIT-072 (catalog) | Not read; catalog link only |
| Existing AI threat models | none | — | News report |
| Weakness enumerations | not assessed | CWE-79, CWE-1426, CWE-1427, LLM05:2025, AML.CS0060 (catalog) | Not read |
| Attack → asset mapping | not assessed | C07, C12, C17 (catalog) | Not read |

## Implementations

— Searched 2026-10-13.

| Name | Kind | License | URL |
|---|---|---|---|


## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this summary |

## Limits

- **Not read:** Cybernews blocks automated access; save the page from a browser to complete this record.
- **Secondary report** of Cybernews' own research; Lenovo's response not checked.
