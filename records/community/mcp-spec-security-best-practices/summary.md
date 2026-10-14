---
schema: "library-summary/v1"
id: mcp-spec-security-best-practices
record: mcp-spec-security-best-practices
type: summary
updated: "2026-10-13"
---

# Model Context Protocol — Security Best Practices

|  |  |
|---|---|
| **Type** | spec (security section of the MCP specification, draft) |
| **Maturity** | _unset — do not guess_ |
| **Authors** | Model Context Protocol maintainers |
| **Published** | Draft page of the MCP specification (it refers to its 2025-11-25 version); retrieved 2026-10-13 |
| **Identifier** | modelcontextprotocol.io — specification/draft/basic/security_best_practices |
| **Source** | https://modelcontextprotocol.io/specification/draft/basic/security_best_practices |
| **Digest** | `d2aa765d51a39a470ecbb44738766cfe75323c26f9db3edc2336933671e393dc` (HTML of the draft page as fetched; living page, the digest will drift) |

## Overview

The security companion to the **MCP Authorization** specification, for developers of MCP authorization flows, server operators and security reviewers. It describes **attacks on MCP implementations** and their mitigations: the **confused-deputy problem** in MCP proxy servers (static client ids, dynamic client registration and consent cookies letting an attacker obtain tokens without the user's consent), **token passthrough** (servers accepting tokens not issued for them), **server-side request forgery** through OAuth metadata discovery (including against authorization servers), **session hijacking**, **local MCP server compromise** (malicious startup commands), and **scope minimization**. Mitigations are normative — the page contains 20 **MUST** statements (e.g. per-client consent storage, consent-page requirements, redirect-URI and OAuth state validation).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | The authoritative MCP threat catalog. |
| Cryptography | adjacent | Adjacent: relies on OAuth 2.0, tokens and cookie security. |
| This project | core | Gives tmodel MCP-specific attack steps and mitigations for the agentic lane. |

Bears on **DEC-001** (object model — MCP components, authorization trust boundaries). **Summary bar only:** this `spec` record is summarised, not extracted; FX-1 extraction belongs to WAVE 2 (#84).

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | core | AIT-099 | Agent-protocol authorization flaws (confused deputy, token passthrough, SSRF via OAuth metadata) |
| Existing AI threat models | core | TM-088 | A protocol-level threat model with attack flows |
| Weakness enumerations | core | CWE-441, CWE-918, CWE-352, CWE-79, CWE-78, AML.T0083, ASI03, ASI04 | Confused deputy, SSRF, CSRF, injection classes as catalogued |
| Attack → asset mapping | core | C09, C11, C13 | MCP servers and clients, OAuth tokens and delegation, third-party APIs |

## Implementations

Applies to all MCP SDKs and servers; not assessed here. Searched 2026-10-13.

| Name | Kind | License | URL |
|---|---|---|---|


## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this summary |

## Limits

- **Draft and living:** the page changes between protocol revisions; the digest will not match later fetches.
- **Authorization-centric:** tool-description poisoning and prompt injection through tools are mostly out of its scope.
- **Not FX-1 extracted** (20 MUSTs not yet extracted as requirements) — WAVE 2.
