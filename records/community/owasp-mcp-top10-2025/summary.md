---
schema: "library-summary/v1"
id: owasp-mcp-top10-2025
record: owasp-mcp-top10-2025
type: summary
updated: "2026-10-13"
---

# OWASP MCP Top 10

|  |  |
|---|---|
| **Type** | web (OWASP project page, beta list) |
| **Maturity** | _unset — do not guess_ |
| **Authors** | OWASP Foundation — MCP Top 10 project (project lead listed on the page) |
| **Published** | 2025, **beta** release (roadmap phase 3: 'beta release and pilot testing'); licensed CC BY-NC-SA 4.0 |
| **Identifier** | https://owasp.org/www-project-mcp-top-10/ |
| **Source** | https://owasp.org/www-project-mcp-top-10/ |
| **Digest** | `335b03198c4daa360f1a9df537b8005151a63e7b11bd8792b6f6476f1ebb1387` (HTML as fetched; living page) |

## Overview

OWASP's top-ten list of security risks in systems built on the **Model Context Protocol (MCP)**, published as a **beta** living document. The ten: **MCP01** token mismanagement and secret exposure; **MCP02** privilege escalation via scope creep; **MCP03** tool poisoning; **MCP04** software supply-chain attacks and dependency tampering; **MCP05** command injection and execution; **MCP06** prompt injection via contextual payloads; **MCP07** insufficient authentication and authorization; **MCP08** lack of audit and telemetry; **MCP09** shadow MCP servers; **MCP10** context injection and over-sharing. Each item has a short description and recommendations for design, implementation and auditing.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | A community risk list for MCP. |
| Cryptography | none | Not about cryptography. |
| This project | core | Gives tmodel a named, ordered set of MCP risks to crosswalk with attack ids. |

Bears on **DEC-001** (object model — MCP-specific threat classes).

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | adjacent | AIT-096, AIT-097, AIT-138, AIT-139 | Tool poisoning; malicious/rug-pull servers; shadow servers; audit gaps — as risk categories, not demonstrated attacks |
| Existing AI threat models | adjacent | TM-089 | A risk list rather than a modeling method |
| Weakness enumerations | core | MCP01:2025–MCP10:2025 | Is the enumeration |
| Attack → asset mapping | core | C08, C09, C11, C19 | MCP servers and tools, credentials and scopes, telemetry |

## Implementations

Content maintained on GitHub (linked from the page). Searched 2026-10-13.

| Name | Kind | License | URL |
|---|---|---|---|


## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this summary |

## Limits

- **Beta:** items and numbering may change; cite as 2025 beta.
- **Thin entries:** short descriptions, little evidence per item.
- **Non-commercial licence** (CC BY-NC-SA 4.0) — check before reusing text in a commercial product.
