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
| **Type** | article (news report of Cybernews' own research) |
| **Maturity** | _unset — do not guess_ |
| **Authors** | Ernestas Naprys (Senior Journalist); research by the Cybernews Research team |
| **Published** | 2025-08-18, Cybernews (updated 2025-08-21) |
| **Identifier** | Cybernews article; MITRE ATLAS case study AML.CS0060 (per RPT-0014 catalog, not stated in the article) |
| **Source** | https://cybernews.com/security/lenovo-chatbot-lena-plagued-by-critical-vulnerabilities/ |
| **Digest** | `1e9dd34aaffcec2748079821285cbb325a19f6a2bd233a41994459e3e99d48e6` (browser 'Save as PDF' copy of the page (10 pp., saved 2026-10-14); the site refuses automated access) |

## Overview

Cybernews researchers found **critical XSS flaws in Lena**, Lenovo's customer-support chatbot built on **OpenAI's GPT-4**. A **single ~400-character prompt** did it in four parts: a harmless product question; instructions to return the answer in **HTML** (plus JSON and plain text in the order the web server expected); an **HTML image with a non-existent URL whose error handler sends the page's cookies** to an attacker's server; and insistence that the image be shown. Lena complied; the page rendered the HTML unsanitised and **leaked the session cookie**. When the conversation is handed to a **human support agent**, their browser renders the same HTML and **leaks the agent's cookie**, opening the support platform and a possible path to lateral movement. Root causes named: missing input and **output sanitisation**, the server not verifying chatbot content, running unverified code, and loading arbitrary resources. **Disclosure:** reported 2025-07-22, acknowledged 2025-08-06, mitigated before publication on 2025-08-18; Lenovo confirmed and thanked the researchers.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | Real-world prompt injection reaching a classic web sink. |
| Cryptography | none | Not about cryptography. |
| This project | core | A clear multi-step attack path (injection → unsafe rendering → session theft → support platform) on a deployed product. |

Bears on **DEC-001** (object model — output handling and downstream consumers as attack-path steps).

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | core | AIT-072, AIT-063 | Prompt injection to a classic sink (stored XSS); direct injection by the user |
| Existing AI threat models | none | — | A news report of disclosed research |
| Weakness enumerations | core | CWE-79, CWE-1426, CWE-1427, LLM05:2025, LLM01:2025, AML.CS0060 | XSS from unvalidated model output, as catalogued |
| Attack → asset mapping | core | C07, C12, C17 | Chatbot app layer, human support agents, browsers rendering the output |

## Implementations

Fixed by Lenovo (details not public). Searched 2026-10-13.

| Name | Kind | License | URL |
|---|---|---|---|


## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this summary |

## Limits

- **Journalistic write-up** of the publisher's own research; the full prompt and Lenovo's fix are not published.
- **Digest is of a browser-saved PDF,** not a publisher file; the live page may differ.
- Incident INC-113 in RPT-0014.
