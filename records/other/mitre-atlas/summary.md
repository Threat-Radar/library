---
schema: "library-summary/v1"
id: mitre-atlas
record: mitre-atlas
type: summary
updated: "2026-11-20"
lane: catalogs-schema
reviewed_by: ""
---

# MITRE ATLAS (Adversarial Threat Landscape for AI Systems)

|  |  |
|---|---|
| **Type** | dataset (summarized, not extracted) |
| **Maturity** | best-practice |
| **Authors** | The MITRE Corporation (ATLAS team) |
| **Published** | 2026.09, data format 6.0.0 (collection `modified-date` 2026-09-15; tag `v2026.09`) |
| **Identifier** | https://atlas.mitre.org/; https://github.com/mitre-atlas/atlas-data |
| **Source** | `dist/v6/ATLAS-2026.09.yaml` at the tag (Apache-2.0, repository `LICENSE` at the tag) |
| **Digest** | `935efa93e28294432d3e2f537eb94991ef8d1f8c58341cd360ea3321ddb66688` |

## Overview

ATT&CK's counterpart for attacks on AI systems. It is a matrix of tactics and techniques, plus mitigations and case studies of real attacks and exercises, with each case study coded step by step to techniques. The pinned file holds:
- 16 tactics;
- 208 techniques, 88 of them sub-techniques. 101 are rated Realized, 83 Demonstrated and 24 Feasible;
- 40 mitigations;
- 73 case studies: 23 Incidents and 50 Exercises;
- 1,355 relationship items under 322 source objects (counted from the YAML on 2026-11-02; 0.3.1 of this record wrongly called the 322 source objects relationships).

The techniques, mitigations and case studies cite 206 distinct references between them.

**A newer release exists.** ATLAS v2026.10 (collection `modified-date` 2026-10-28, data format 6.1.0) came out before this record was pinned. This record keeps 2026.09, the version RPT-0009's and RPT-0014's mappings use. The changes that touch those mappings were checked against `dist/v6/ATLAS-2026.10.yaml` (sha256 `ac41ee9f99a47084ba5fdfc77ae83a28687e12390240fffeb37df7914ffe142d`, downloaded from the v2026.10 tag; not pinned here):
- **Removed (5):**
  - AML.T0024.000 (Infer Training Data Membership), .001 (Invert AI Model) and .002 (Extract AI Model). The parent AML.T0024 (Exfiltration via AI Inference API) remains;
  - AML.T0056 (Extract LLM System Prompt), which 0.3.2 of this record left out;
  - AML.T0057 (LLM Data Leakage).

  The 2026.10 file never mentions the removed ids, so it gives no pointer to a successor. The closest new techniques are AML.T0137 (Training Data Information from AI Models, with .000 to .003), AML.T0144 (Recover AI Model Internals), AML.T0085.003 (System Instructions) and AML.T0136 (Exfiltration via AI User Interface).
- **Added (18 techniques).** Among them:
  - AML.T0017.003 (Malware);
  - AML.T0085.002 and .003;
  - AML.T0135 to AML.T0145, for example LLM Prompt Propagation, Centralized AI Service Request Routing, Event Triggered Execution and Poison AI Agent Learning Environment;
  - AML.T0137's four sub-techniques.
- **Renamed:** AML.T0010 "AI Supply Chain Compromise" becomes "Supply Chain Compromise", with .001 "AI Software" becoming "Software", .002 "Data" becoming "Data Repository" and .003 "Model" becoming "Model Repository". AML.M0026 "Privileged AI Agent Permissions Configuration" becomes "Manage AI Agent Service Access", and AML.M0027 "Single-User AI Agent Permissions Configuration" becomes "Manage User-Delegated AI Agent Access".
- **AML.CS0059 (EchoLeak):** the 2026.09 field `actor: Aim Labs` is gone. 2026.10 links the case study `attributed-to` the new entity AML.E0016, Cato Networks ("activity-purpose: Security Evaluation"), which the entity's description says acquired Aim Security in September 2025. The case study's own description still says "Aim Security researchers discovered EchoLeak".
- **New sections:** 2026.10 adds top-level `entities` (44) and `software` (37). It has 221 techniques, 44 mitigations, 77 case studies and 1,750 relationship items.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | The technique catalog for AI attacks |
| Cryptography | none | |
| This project | core | Technique ids in RPT-0009 and RPT-0014. Case study AML.CS0059 is the source of RPT-0009's EchoLeak model |

`bears_on: DEC-008`: like ATT&CK ids, ATLAS ids are catalog references that need a version pin and, per RPT-0009 §5 item 3, a level (parent technique or sub-technique) and a fit grade (RPT-0009 G4).

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | core | 141 of 146 AIT entries; INC-* with AML.CS ids | 141 of the catalog's 146 attack entries carry ATLAS ids. ATLAS case studies are the coded source for 69 of the 179 incidents (`incidents.md` P1). **18 AIT entries cite an id that 2026.10 removed:** AIT-024, 046 to 054, 056 to 058, 083 to 085, 103 and 137. A re-pin to 2026.10 needs a by-hand alias table for them, since the release gives no successor ids |
| Existing AI threat models | adjacent | — | Not a threat model. Its case studies are reference attack paths (tactic-ordered steps), which `report.md` §7 proposes as the coarse ordering tag for AttackPath |
| Weakness enumerations | core | AML.TA*, AML.T*, AML.M*, AML.CS* | The attack layer of every crosswalk in `enumerations.md`. It isn't weakness-oriented (CWE AI WG slides, 2026-06-26). Each technique carries a maturity (Feasible / Demonstrated / Realized), which the AIT catalog copies as `atlas_maturity` |
| Attack → asset mapping | adjacent | — | Techniques name tactics and targets, not assets or components. A case study's `target` is the victim system. The mapping to C01–C21 and A01–A18 is the report's own work |

## Implementations

Searched 2026-11-20:

| Name | Kind | License | URL |
|---|---|---|---|
| mitre-atlas/atlas-data | The data, per release: YAML, STIX 2.1, Navigator layers and spreadsheets | Apache-2.0 | https://github.com/mitre-atlas/atlas-data |
| mitre-atlas/atlas-navigator-data | ATLAS layers for the ATT&CK Navigator | not stated in the GitHub metadata | https://github.com/mitre-atlas/atlas-navigator-data |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, digest and `cites` |
| `summary.md` | this summary, with the RPT-0014 applicability table |

## Reference expansion

The 206 distinct references were checked against `sources.md` (by id, title and URL) and the library on 2026-11-20:
- **In `sources.md` (85):** 69 by id or title, and 16 more by URL. Seven also have library records: `apruzzese-2023-real-attackers`, `echoleak-zero-click-prompt-injection`, `google-photos-model-extraction-2025`, `lenovo-lena-xss-2025`, `mcp-spec-security-best-practices`, `pillar-2025-rules-file-backdoor` and `pytorch-2022-torchtriton-dependency-confusion`.
- **Covered by another source (48):** another write-up of an incident or finding RPT-0014 already holds, for example:
  - AgentFlayer, S-1006; LLMjacking, S-1000; LameHug, S-1036;
  - OpenClaw, S-0560/S-0774/S-1148; the Amazon Q extension, S-1095;
  - ShadowRay, S-0990; EchoLeak, S-0456; Storm-2139, S-1141;
  - Clearview, S-1122; ID.me, S-1123; Cylance, S-0869; Tay, S-0864; Proof Pudding, S-0871;
  - package hallucination, S-0991; abliteration, S-0227.
- **Missing, added as stubs (33):**
  - 2 papers: JailbreakZoo, and ROME (model editing);
  - 31 web pages, each pinned by a Wayback Machine copy:
    - 9 AI-enabled voice-fraud incidents, 8 of them from the AI Incident Database and 1 from the OECD monitor;
    - Google's 2026 census of prompt injections on the web, and Mandiant on AI voice spoofing;
    - prompt-injection and agent attacks by Embrace The Red (3), Zenity (2), NCC Group, Backslash and Vulcan;
    - LLM abuse news (2 GBHackers, 1 Cyber Security News) and GreyNoise on actors targeting LLMs;
    - three OWASP guides (MCP security, Agent Memory Guard, GenAI red teaming), the DAN jailbreak prompts and Promptfoo's jailbreak guide;
    - the Colab, OpenGPT-2 and swyx case-study sources.
- **Missing, not stubbed (1):** the SPIE paper "An AI Red Team Playbook" (DOI 10.1117/12.3021906). It has no archived copy to pin.
- **Out of scope or duplicate (39):**
  - MCP server directories and product, help or vendor documentation (guardrails, alignment explainers, ID.me help pages, OpenClaw's own pages);
  - datasets (MATH, GSM8K) and training-method papers;
  - the target models in the 2018–2019 detector case studies;
  - general container-registry articles;
  - social-media posts, videos and a Shodan search;
  - one duplicated URL.

## Limits

- Case studies are ordered steps (`step-id`, tactic, `leads-to`), an exception to RPT-0005 G2 (RPT-0009 G2). That structure isn't described here; it is WAVE 2's extraction (`CAT-mitre-atlas-2026-09`, #84).
- ATLAS covers well under half of RPT-0014's incident log (69 of 179 incidents carry a case-study id; RPT-0014 `incidents.md` P1).
- **Releases remove ids without leaving aliases.** 2026.10 drops five techniques and doesn't say what replaced them, so every consumer's mappings have to be re-pinned by hand. CoSAI's Risk Map, for example, still pins 5.0.1.
- **The references are uneven.** Exercises often cite one vendor blog or social-media post, and the AI-enabled-fraud technique (AML.T0052.001) leans on AI Incident Database entries, which are secondary.
