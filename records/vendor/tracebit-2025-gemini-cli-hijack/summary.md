---
schema: "library-summary/v1"
id: tracebit-2025-gemini-cli-hijack
record: tracebit-2025-gemini-cli-hijack
type: summary
updated: "2026-10-13"
---

# Code Execution Through Deception: Gemini AI CLI Hijack

|  |  |
|---|---|
| **Type** | article (vendor security research blog) |
| **Maturity** | _unset — do not guess_ |
| **Authors** | Sam Cox (Tracebit) |
| **Published** | 2025-07-28, Tracebit blog (page shows a 2026-04-08 update) |
| **Identifier** | Tracebit research blog |
| **Source** | https://tracebit.com/blog/code-exec-deception-gemini-ai-cli-hijack |
| **Digest** | `not fetched` (page content is rendered by JavaScript; read through a web reader, no stable digest) |

## Overview

Tracebit showed how **Google's Gemini CLI** (coding agent in the terminal; default configuration, no sandbox) could be hijacked by a **malicious repository**. A `README.md` holds a hidden **prompt injection** inside licence text that a human skips but the agent reads. The injection first gets the user to approve a harmless `grep`; because the **command allow-list only checked the first word**, a later command that starts with `grep` runs **without asking**. Padding the command with whitespace pushes the malicious part off-screen (**UI deception**), so after two user inputs the environment variables (often secrets) are **sent to an attacker's server**; the payload could equally install a shell or delete files. OpenAI Codex and Anthropic Claude did not appear vulnerable. **Timeline:** reported June 27, 2025; Google raised it to **P1/S1**; fixed in **v0.1.14** (July 25); disclosed July 28.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | A concrete agent RCE chain with a fixed version. |
| Cryptography | none | Not about cryptography. |
| This project | core | Shows a multi-step attack path (injection → approval bypass → deception → exfiltration) of the kind tmodel must model with ordered steps. |

Bears on **DEC-001** (object model — ordered attack steps across agent, human approval and tools).

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | core | AIT-092, AIT-093 | Coding-agent prompt injection to code execution; human-approval bypass |
| Existing AI threat models | none | — | Incident research |
| Weakness enumerations | adjacent | AML.T0051.001, AML.T0050, LLM01:2025, LLM06:2025, ASI01, ASI05, CWE-78 | Catalog entries for the chain |
| Attack → asset mapping | core | C08, C09, C11, C12, C14 | Coding agent and its shell tool, secrets in the environment, the approving user, developer machine |

## Implementations

Fix in Gemini CLI v0.1.14. Searched 2026-10-13.

| Name | Kind | License | URL |
|---|---|---|---|


## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this summary |

## Limits

- **Vendor research;** a single demonstrated chain on an early release.
- **Read through a web reader** (JavaScript-rendered page); no stable digest.
- Incident INC-103 in RPT-0014.
