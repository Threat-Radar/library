---
schema: "library-summary/v1"
id: cursor-curxecute-mcpoison-2025
record: cursor-curxecute-mcpoison-2025
type: summary
updated: "2026-10-13"
---

# CVE-2025-54135, CVE-2025-54136: Frequently Asked Questions About Vulnerabilities in Cursor IDE (CurXecute and MCPoison)

|  |  |
|---|---|
| **Type** | article (vendor FAQ on two CVEs) |
| **Maturity** | _unset — do not guess_ |
| **Authors** | Satnam Narang (Tenable Research Special Operations) |
| **Published** | 2025-08-05, Tenable blog |
| **Identifier** | CVE-2025-54135; CVE-2025-54136 |
| **Source** | https://www.tenable.com/blog/faq-cve-2025-54135-cve-2025-54136-vulnerabilities-in-cursor-curxecute-mcpoison |
| **Digest** | `c5017280a03228e4a5eadb1e92721912962e5f40958681b3d8cd45a06a504098` (HTML as fetched; living page) |

## Overview

Tenable's FAQ on two vulnerabilities in **Cursor** (AI code editor) in how it handles **MCP servers**. **CurXecute (CVE-2025-54135, CVSS 8.5)**, disclosed by AIM Security: through **prompt injection** — e.g. a crafted message read via a Slack MCP server — the agent rewrites the global `mcp.json` and so runs attacker commands. **MCPoison (CVE-2025-54136, CVSS 7.2)**, disclosed by Check Point Research: once a user **approves** a project's MCP server, later changes to its configuration are trusted because approval is bound to the server's **name, not its contents**, so a malicious contributor can swap in a command. Both were reported in July 2025 through coordinated disclosure and fixed in Cursor 1.3.x (per Tenable's version table).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | Real, CVE-scored MCP vulnerabilities. |
| Cryptography | none | Not about cryptography. |
| This project | core | Two distinct MCP attack steps (config tampering via injection; trust bound to name not content) for tmodel's MCP components. |

Bears on **DEC-001** (object model — MCP configuration as a component) and **R-010** (CVE linkage).

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | core | AIT-092, AIT-094 | Coding-agent injection to code execution; agent configuration tampering |
| Existing AI threat models | none | — | Vulnerability FAQ |
| Weakness enumerations | core | CVE-2025-54135, CVE-2025-54136, CWE-78, AML.T0051.001, LLM01:2025, LLM03:2025, ASI04, ASI05 | Real CVE ids plus catalog entries |
| Attack → asset mapping | core | C08, C09, C14 | Coding agent, MCP servers and their config, developer environment |

## Implementations

Fixed in Cursor releases (versions per Tenable's table). Searched 2026-10-13.

| Name | Kind | License | URL |
|---|---|---|---|


## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this summary |

## Limits

- **Secondary source:** Tenable summarises AIM Security's and Check Point's primary disclosures (not ingested here).
- **Fixed-version numbers** were read from Tenable's table; check them there before relying on them.
- Incident INC-110 in RPT-0014.
