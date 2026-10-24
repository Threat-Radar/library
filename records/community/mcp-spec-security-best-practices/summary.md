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
| **Type** | spec (security best-practices page of the MCP 2025-11-25 release, which files it under docs/tutorials rather than the specification tree) |
| **Maturity** | _unset — do not guess_ |
| **Authors** | Model Context Protocol maintainers |
| **Published** | MCP 2025-11-25 release; retrieved 2026-10-21 (first read as the living draft page on 2026-10-13) |
| **Identifier** | modelcontextprotocol.io — specification/2025-11-25/basic/security_best_practices |
| **Source** | https://modelcontextprotocol.io/docs/2025-11-25/tutorials/security/security_best_practices |
| **Digest** | `95beaace4d676d89e92d94751bab1ad4c9870e1458bc5f6f7eae8dd8bbc75bec` (HTML of the dated 2025-11-25 page; identical on two fetches) |

## Overview

The security companion to the **MCP Authorization** specification, for developers of MCP authorization flows, server operators and security reviewers. It describes **attacks on MCP implementations** and their mitigations: the **confused-deputy problem** in MCP proxy servers (static client ids, dynamic client registration and consent cookies letting an attacker obtain tokens without the user's consent), **token passthrough** (servers accepting tokens not issued for them), **server-side request forgery** through OAuth metadata discovery (including against authorization servers), **session hijacking**, **local MCP server compromise** (malicious startup commands), **OAuth authorization-URL validation**, **stdio transport security in proxy setups**, and **scope minimization**. Mitigations are normative — the page contains about 21 **MUST** statements (a rough count; FX-1 extraction will give the exact one) (e.g. per-client consent storage, consent-page requirements, redirect-URI and OAuth state validation).

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

- **Dated release, not the draft:** pinned to the 2025-11-25 page. The living draft has since moved on (it adds mix-up attacks, localhost redirect-URI impersonation and CIMD trust policies, and has a "state handle hijacking" section where the release has "session hijacking"); a later release needs a new record or an update.
- **Authorization-centric:** tool-description poisoning and prompt injection through tools are mostly out of its scope.
- **Not FX-1 extracted** (its MUSTs are not yet extracted as requirements) — WAVE 2.
