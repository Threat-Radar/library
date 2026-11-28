---
schema: "library-summary/v1"
id: cosai-risk-map
record: cosai-risk-map
type: summary
updated: "2026-11-20"
lane: catalogs-schema
reviewed_by: ""
---

# CoSAI Risk Map

|  |  |
|---|---|
| **Type** | dataset (YAML with JSON Schemas, in the repository `cosai-oasis/secure-ai-tooling`) |
| **Maturity** | _unset — do not guess_ (an open project's working catalog, revised continuously) |
| **Authors** | Coalition for Secure AI (CoSAI), an OASIS Open Project |
| **Published** | read at commit `622605a1` (2026-10-20). The risk data last changed in `a293592` (2026-10-14). RPT-0014 read `0d8bfc9b5d76` (2026-10-02) |
| **Identifier** | https://github.com/cosai-oasis/secure-ai-tooling |
| **Source** | `risk-map/yaml/risks.yaml` at commit `622605a13fafaa2784acbdbe3f8d23ee22da4be7` (Apache-2.0) |
| **Digest** | `e4d165972d2dce38f569366e6111aa2146e47c364524bf9168f8f6c11b9a878b` (that file); the other YAML digests are in `record.yaml` |

## Overview

A machine-readable catalog of AI security risks, which grew out of Google's SAIF and is now maintained by CoSAI. It has four linked sets, each with a JSON Schema:

| Set | Count | Grouped as |
|---|---|---|
| Components | 42 | infrastructure 14, application 13, model 9, external tools 6 |
| Risks | 36 | deployment and infrastructure 14, supply chain and development 7, runtime input, output and data security 5 each |
| Controls | 37 | infrastructure 11, application 9, data 6, assurance 4, governance 4, model 3 |
| Personas | 10 | model provider, data provider, platform provider, model serving, agentic provider, application developer, governance, end user, model creator, model consumer |

**What a risk record holds:**
- descriptions, examples and external references (every risk has both);
- the controls that mitigate it (1 to 10 each) and the personas it concerns;
- a lifecycle stage (planning to maintenance), impact types (confidentiality to safety and compliance) and actor access (user, API, agent, supply chain, privileged, physical …);
- a "tour" text on where the risk is introduced, exposed and mitigated;
- mappings to other frameworks.

Fifteen risks are SAIF's, and 21 were added. The additions cover:
- side channels and economic denial of wallet;
- PEFT/adapter injection and benchmark manipulation;
- cache and vector-store poisoning, and covert output channels;
- tool registry tampering, MCP transport hijacking and zombie MCP servers;
- delegation confused deputy, stale agent identity, shadow agents and runaway tool loops;
- cross-tenant credential propagation.

**Crosswalks.** Six frameworks are registered: MITRE ATLAS, NIST AI RMF, STRIDE, the OWASP LLM Top 10, ISO 22989 and the EU AI Act. Of the 36 risks, 26 map to STRIDE, 19 to ATLAS and 19 to the OWASP LLM Top 10. Under ADR-027 (accepted 2026-05-22), each mapping is pinned to the edition it was made against, for example `AML.T0020@5.0.1`. The ADR's reason is that frameworks re-version on their own schedules: OWASP's LLM02 changed meaning, ATLAS retires techniques, and the AI Act renumbered articles. The repository also ships a static "Risk Map Explorer" site that browses risks and controls by persona.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | A risk-and-control catalog for AI systems, linked to components and personas |
| Cryptography | none | No cryptographic design; credential and transport risks are named, not specified |
| This project | core | Component → risk → control, with lifecycle, impact and access attributes, is close to tmodel's Component → Threat → Mitigation path. Version-pinned external ids are what `report.md` §7 proposes for catalog references (**DEC-001**, **DEC-008**). It can be imported as a pinned catalog layer, as the report suggests |

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | adjacent | AIT-138, AIT-146 | AIT-138 (shadow agents and MCP servers) and AIT-146 (router manipulation) cite it. Its risks are classes, each with examples and references, not incident or attack records |
| Existing AI threat models | core | TM-041 | TM-041's source. TM-041's counts and fields hold at the newer commit: 42 components, 36 risks, 37 controls and 10 personas, with lifecycle stage, impact type and actor access. Its "version-pinned crosswalks (ADR-027)" are real, but see the next row |
| Weakness enumerations | core | CoSAI risk ids; AML.T*@5.0.1 (37 mappings), LLM01–LLM10:2025, STRIDE | **The ATLAS pins are all still 5.0.1.** On 2026-10-14 `frameworks.yaml` made 2026.09 the current ATLAS edition, but no mapping was re-pinned. Against 2026.09 one mapping has no counterpart: `riskDataPoisoning` → AML.T0019, as `sources.md` noted, which still holds. **Against 2026.10 there are three:** AML.T0024.002, which `riskModelExfiltration` and `riskModelReverseEngineering` cite, was removed in 2026.10. 17 risks have no ATLAS mapping, nearly all of them the agentic, MCP, cache and side-channel additions. `sources.md`'s "first 15 risk titles match SAIF" is close: SAIF's 15 are all there, but "Excessive Data Handling During Inference", an addition, sits fifth and "Rogue Actions" sixteenth |
| Attack → asset mapping | core | C01–C21 (most); A01–A11 | Its 42 components cover most of the report's C01–C21: data sources and stores, training, registry and supply chain, serving, RAG, application, agent, tools and MCP, identity, and MLOps infrastructure. Its impact types and the assets in its risk texts (data, weights, prompts, credentials, compute spend) map to A01–A11. The report's business and human assets (A12–A18) have no direct counterpart. The mapping is ours |

## Implementations

Searched 2026-11-20 (GitHub code and repository search):

| Name | Kind | License | URL |
|---|---|---|---|
| CoSAI Risk Map Explorer | The repository's own static site, built from the YAML (`site/`) | Apache-2.0 | https://github.com/cosai-oasis/secure-ai-tooling |

Other CoSAI repositories (`ws2-defenders`, `ws4-secure-design-agentic-systems`, `project-codeguard`) reference it. No third-party tool importing the YAML was found.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, digest, commit and `cites` |
| `summary.md` | this summary, with the RPT-0014 applicability table |

## Reference expansion

The `externalReferences` of the risks, controls, components and personas list 83 references, checked against `sources.md` and the library on 2026-11-20:
- **In `sources.md` (28)** and **in the library only (2):** the library ones are RFC 6749 (`rfc-6749`), given twice. Several MCP-specification pages are `mcp-spec-security-best-practices`.
- **Covered by another source (5):** news reports of incidents RPT-0014 already holds:
  - Samsung, S-1127 / INC-027;
  - Asana MCP, S-1138 / INC-097;
  - package hallucination, S-0991;
  - stop-sign perturbation, S-0038;
  - Salesforce OAuth, S-1105.
- **Missing, added as stubs (22):**
  - **11 papers:** architectural backdoors, phantom sponges, verbatim-memorization privacy, cache side channels in local LLMs, FedMIA, PETA, selective benchmark attacks, steganographic collusion, semantic-cache key collision, dense-retrieval backdoors, and cryptographic binding for agent tools.
  - **11 web pages, each pinned by a Wayback Machine copy:** ShellTorch, MCP server hosting, multi-modal injection against GPT-4V, ChatGPT plugin source-code theft, the 2021 pickle exploit post, ransomware in ML models, WhatsApp MCP exfiltration, CVE-2026-24779 (vLLM SSRF), Alexa and Google Home skill phishing, and two vendor MCP risk overviews.
- **Out of scope (26):**
  - 18 general security references: NIST SP 800-53/162/190/207 and 800-63C, RFC 7591 and 8693, CIS Controls, the OWASP WSTG, JSON-RPC, gVisor, Kata Containers, AWS IAM, ATT&CK M1037 and CWE-441;
  - 8 that aren't about attacks on AI systems: AI-generated music takedowns, the Clearview settlement, Stanford Alpaca, two face-inference studies, a Gartner press release, an AutoGen bug report and BingBang (an Azure AD misconfiguration).

## Limits

- **Crosswalk pinned to an old ATLAS.** All ATLAS mappings are as of 5.0.1, which is older than 2026.09. ADR-027 itself says it can detect a pin's version but cannot yet detect retirement or renumbering, so one dangling mapping, and three against 2026.10, went unnoticed.
- **A living catalog.** The data changed between RPT-0014's capture and this one, and changes weekly. Only a commit pin is stable.
- **Classes, not evidence.** A risk names a class and gives examples and references. It doesn't rate likelihood or say which risks have been seen in the wild.
- **Gaps for business assets.** Personas and components are about the AI stack. Harms to people, brand and finances appear only as impact types, not as assets.
