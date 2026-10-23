---
schema: "library-summary/v1"
id: pillar-2025-rules-file-backdoor
record: pillar-2025-rules-file-backdoor
type: summary
updated: "2026-10-13"
---

# New Vulnerability in GitHub Copilot and Cursor: How Hackers Can Weaponize Code Agents

|  |  |
|---|---|
| **Type** | article (vendor security research blog) |
| **Maturity** | _unset — do not guess_ |
| **Authors** | Ziv Karliner (Pillar Security) |
| **Published** | 2025-03-18, Pillar Security blog |
| **Identifier** | Pillar Security research blog |
| **Source** | https://www.pillar.security/blog/new-vulnerability-in-github-copilot-and-cursor-how-hackers-can-weaponize-code-agents |
| **Digest** | `7005751530518ae23730c08a0addc0cdf798a2996a9c8cd7d4f66aaa56e73e76` (HTML as fetched; living page) |

## Overview

Pillar Security disclosed the **"Rules File Backdoor"**: a supply-chain attack on AI coding assistants (**GitHub Copilot** and **Cursor**) through their **rule/configuration files** (e.g. Cursor's `.cursor/rules`), which developers share widely and trust implicitly. Malicious instructions are hidden with **invisible Unicode** (zero-width joiners, bidirectional markers) and evasive wording, so a human reviewer sees a harmless rule while the model follows hidden instructions to **insert malicious code** into generated output — and stay silent about it. The instructions survive project forking, spreading to downstream users. A Cursor demonstration shows the injected code appearing in generated files. **Disclosure:** Cursor (Feb–Mar 2025) and GitHub (Mar 2025) both answered that reviewing AI suggestions is the **user's responsibility**; on May 1, 2025 GitHub added a warning when a file contains hidden Unicode.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | A real, disclosed attack on widely used coding agents. |
| Cryptography | none | Not about cryptography. |
| This project | core | Rule files are agent configuration components; tmodel needs them as a supply-chain entry point with hidden-text attack steps. |

Bears on **DEC-001** (object model — agent configuration files as components and entry points).

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | core | AIT-095, AIT-067 | Rules-file poisoning; hidden-instruction smuggling with invisible Unicode |
| Existing AI threat models | none | — | Incident research, not a threat model |
| Weakness enumerations | adjacent | AML.T0081, AML.T0068, AML.T0051.001, LLM01:2025, LLM03:2025, ASI04 | Catalog entries for the technique |
| Attack → asset mapping | core | C04, C08, C14 | Shared rule files (supply chain), coding agents, developer environment |

## Implementations

Pillar published a rule-file scanner (linked from the post; not assessed). Searched 2026-10-13.

| Name | Kind | License | URL |
|---|---|---|---|


## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this summary |

## Limits

- **Vendor research** promoting its own product; demonstration, not measured prevalence.
- **No CVE:** both vendors declined to treat it as a vulnerability.
- Incident INC-084 in RPT-0014.
