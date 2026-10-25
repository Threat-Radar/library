---
schema: "library-doc/v1"
id: tmodel-bibliography-review
title: "tmodel bibliography review: relevance and impact of every item"
type: assessment
status: draft
version: "0.1.0"
updated: "2026-10-25"
needs_review: true
reviewed: false
---

# tmodel bibliography review: relevance and impact

Tracking issue: Threat-Radar/tmodel#165 (part of Threat-Radar/tmodel#86; follows Threat-Radar/tmodel#164). Owner: @nymble. Drafted by Grok Bot for Paul.

This is one row per entry in tmodel's `docs/publishing/bibliography.yaml` (414 entries, as of tmodel `main` on 2026-10-25). Each row gives the record's level in this library on `main`, what this review did, whether the source is free, and a short **relevance** (high / medium / low) and **impact** judgement against tmodel's model: ADR-0002 backbone, DEC-001a object model (ADR-0010), attack paths, the ADR-0006 risk vector, the knowledge graph, agentic threats, and DEC-001b / DEC-008 / DEC-009.

## How to read the columns

- **Record on `main`**: `stub` (metadata only), `scaffold` (summary template unwritten), `thin` (summary written but missing a digest, publisher, or substance), `complete` (summary bar met), `complete (FX-1)` (full extraction). Computed by script from `record.yaml` and `summary.md`; this is a heuristic, not a review verdict.
- **This review**: `upgraded → library#NN` is a summary-bar upgrade in that PR. `in open PR …` means a student's in-flight work; it was assessed here but not edited.
- **Availability**: `free` unless the source is a licensed standard. Licensed texts are paraphrased with clause IDs only, never quoted.
- **Related**: `#NN` means a Threat-Radar/tmodel issue; `library#NN` means a pull request in this repo; `DEC-`/`ADR-`/`R-` ids are tmodel decisions and requirements.
- **Relevance / Impact**: a judgement (inference), not a fact taken from the source. Items in the m-of-n part of the bibliography are mostly out of tmodel's scope and are rated low as a group, with exceptions noted.

## Totals

| | Count |
|---|---|
| Bibliography entries | 414 (132 tmodel topics, 282 inherited m-of-n topics) |
| Level on `main` | complete 50 · complete (FX-1) 32 · scaffold 61 · stub 213 · thin 58 |
| Relevance | high 25 · medium 62 · low 327 |
| Upgraded in this review | 10 (library#34, #35, #36) |
| In open student PRs (assessed, not edited) | 7 |
| Licensed or not checked | 20 |

## Remaining high-relevance work

High relevance, still stub/scaffold/thin on `main`, and not in an open PR:

- `csa-maestro-2025` (thin; free; student-authored, left for its author) — #78, #71, #36
- `cve-json-5` (thin; free) — #61, #17, DEC-008, DEC-009
- `first-cvss-v3-1` (stub; free; student-authored, left for its author) — #14, #63, ADR-0006
- `first-cvss-v4-0` (stub; free; student-authored, left for its author) — #14, #63, ADR-0006
- `linkml` (thin; free) — #64, #104
- `prov-o` (thin; free) — #50, #52, DEC-001b
- `schneier-attack-trees-1999` (thin; free; student-authored, left for its author) — #63, #36
- `systems-security-agentic-computing` (thin; free; student-authored, left for its author) — #71, #78, #39

High relevance and in an open student PR (left to the author):

- `cwe` — library#21
- `cyclonedx-1-7` — library#33
- `etsi-en-304-223` — library#32
- `open-threat-model` — library#21
- `osv-schema` — library#28
- `spdx-3-0-1` — library#33

## tmodel-topic items (132)

| Item | Record on `main` | This review | Availability | Relevance | Impact | Related |
|---|---|---|---|---|---|---|
| `bron` — BRON — Linking ATT&CK, CAPEC, CWE, CVE, CPE (Hemberg et al., 2020) | thin | upgraded → library#34 | free | **high** | Existing build of the CVE→CWE→CAPEC→ATT&CK backbone, with measured chain-break rates (28% of CVEs floating, 74% of techniques with no CAPEC). Shape to reuse; the 2020 data is not. | #164, #17, #59, DEC-008, DEC-009 |
| `capec` — MITRE CAPEC — Common Attack Pattern Enumeration and Classification | thin | upgraded → library#36 | free | **high** | Source of AttackPattern (CAPEC) nodes and CWE↔CAPEC links in the ADR-0002 backbone; its ATT&CK links are pinned to ATT&CK 12.0 (RPT-0005), so DEC-008 must pin and date the release. | #17, #61, #59, DEC-008 |
| `csa-maestro-2025` — Agentic AI Threat Modeling Framework: MAESTRO | thin |  | free | **high** | Agentic-AI threat-modeling layers; the post-MVP `method_facet` named in ThreatInstance. Student-authored record. | #78, #71, #36 |
| `cve-json-5` — CVE JSON Record Format v5 | thin |  | free | **high** | Shape of every imported Vulnerability: affected products, CWE problemTypes, CVSS metrics, CNA vs ADP containers (the provenance Assertion must keep). | #61, #17, DEC-008, DEC-009 |
| `cwe` — MITRE CWE — Common Weakness Enumeration | thin | in open PR library#21 (not edited) | free | **high** | Catalog behind `Weakness`; its typed relations and views drive the lossless CWE import. Owned by the CWE lane (library#21). | #61, #143–#146, #157, DEC-008 |
| `cyclonedx-1-7` — CycloneDX Bill of Materials Specification | stub | in open PR library#33 (not edited) | free | **high** | SBOM input format for product composition and VEX; in student PR library#33. | #38, DEC-009 |
| `etsi-en-304-223` — Securing Artificial Intelligence (SAI); Baseline Cyber Security Requirements for AI Models | complete | in open PR library#32 (not edited) | free | **high** | AI security baseline (13 principles, 72 provisions); requirement content for AI threats. In student PR library#32. | #39, #71, DEC-001b |
| `etsi-ts-102-165-1` — ETSI TS 102 165-1, CYBER; Methods and protocols; Part 1: Method and proforma for Threat, V | scaffold | upgraded → library#35 | free | **high** | ETSI TVRA: a threat-vulnerability-risk method with attack-potential likelihood × impact; an alternative TARA to compare against ADR-0006. | #63, #14, DEC-003 |
| `first-cvss` — FIRST, Common Vulnerability Scoring System (CVSS) | scaffold | upgraded → library#35 | free | **high** | Umbrella record for CVSS. ADR-0006 rejects CVSS as the risk number, so CVSS is evidence/display only; needed to say exactly what is shown and what is never folded in. | #14, #63, ADR-0006 |
| `first-cvss-v3-1` — FIRST, Common Vulnerability Scoring System v3.1: Specification Document | stub |  | free | **high** | The CVSS version on most NVD history; its exploitability subscore is what reviewers will be tempted to reuse as 21434 feasibility (ADR-0006 forbids). Student-authored stub. | #14, #63, ADR-0006 |
| `first-cvss-v4-0` — FIRST, Common Vulnerability Scoring System v4.0: Specification Document | stub |  | free | **high** | Current CVSS; adds attack requirements and supplemental metrics; display-only under ADR-0006. Student-authored stub. | #14, #63, ADR-0006 |
| `iso-iec-15408` — ISO/IEC 15408 (all parts), Evaluation criteria for IT security (Common Criteria) | scaffold | upgraded → library#35 | licensed; free CC:2022 read | **high** | Common Criteria: R-013 attack-feasibility display (ADR-0006: CC is display-only). The ISO text is licensed; CC:2022 is free from the CCRA portal and is used as the readable equivalent. | #14, R-013, ADR-0006 |
| `iso-iec-18045` — ISO/IEC 18045, Methodology for IT security evaluation (attack potential) | scaffold | upgraded → library#35 | licensed; free CEM:2022 read | **high** | CEM attack-potential method (elapsed time, expertise, knowledge, window of opportunity, equipment), the basis that ISO/SAE 21434 uses for attack-potential feasibility. | #14, #63, R-013, ADR-0006 |
| `iso-sae-21434-2021` — Road vehicles — Cybersecurity engineering | complete |  | licensed | **high** | Normative source of the ADR-0006 vector (Table-1 feasibility, S/F/O/P impact, risk matrix) and TARA flow. Licensed text: paraphrase and clause IDs only. FX-1 owned by #154. | #154, #63, ADR-0006, DEC-009 |
| `linkml` — LinkML — Linked Data Modeling Language | thin |  | free | **high** | The accepted schema IDL (ADR-0007); generators for JSON Schema/SHACL/OWL. | #64, #104 |
| `mitre-attack` — MITRE ATT&CK (knowledge base + STIX 2.1 data) | thin | upgraded → library#36 | free | **high** | Technique and tactic layer of the backbone (AttackPattern + kill_chain_phase); STIX 2.1 bundles give the uses/mitigates edges. ATT&CK dropped its CAPEC direction in v13 (RPT-0005). | #17, #59, #75, DEC-008 |
| `mulval` — MulVAL: A Logic-based Network Security Analyzer (Ou et al., USENIX Security 2005) | thin | upgraded → library#36 | free | **high** | Logic-based attack-graph generation from vulnerabilities, configuration and reachability: the precondition semantics tmodel attack paths lack (ADR-0010 leaves pre/postconditions unshaped). | #63, #17 |
| `open-threat-model` — Open Threat Model specification and JSON Schema | thin | in open PR library#21 (not edited) | free | **high** | Interchange format ADR-0007 imports; in student PR library#21. | #64, #79 |
| `osv-schema` — OSV Schema (OpenSSF) | thin | in open PR library#28 (not edited) | free | **high** | Version-precise package-to-vulnerability format; the version-range matching DEC-009 needs for ProductInstance. In student PR library#28. | #38, DEC-009 |
| `prov-o` — PROV-O: The PROV Ontology | thin |  | free | **high** | Provenance vocabulary for the Assertion spine (wasGeneratedBy/wasAttributedTo); the gap DL-0020 M5 (author/origin) needs for DEC-001b. | #50, #52, DEC-001b |
| `schneier-attack-trees-1999` — Attack Trees | thin |  | free | **high** | Origin of AND/OR attack trees, which are the semantics of `AttackStep.gate`. Student-authored record. | #63, #36 |
| `spdx-3-0-1` — System Package Data Exchange (SPDX) Specification Version 3.0.1 | stub | in open PR library#33 (not edited) | free | **high** | SBOM graph model with vulnerability assessments; in student PR library#33. | #38, DEC-009 |
| `spotlighting-indirect-prompt-injection` — Defending Against Indirect Prompt Injection Attacks With Spotlighting | complete |  | free | **high** | Indirect prompt injection and the spotlighting mitigation; core agentic threat for the AI model lane. | #71, #78 |
| `stix-2-1` — STIX Version 2.1 (OASIS Standard) | thin | upgraded → library#36 | free | **high** | Interchange target named in ADR-0007; its SDO/SRO graph (Attack Pattern, Vulnerability, Course of Action, Relationship, Opinion) maps onto AttackPattern/Vulnerability/Mitigation/Assertion/Review. | #64, #53, #17 |
| `systems-security-agentic-computing` — Systems Security Foundations for Agentic Computing | thin |  | free | **high** | Systems-security view of agents (probabilistic TCB, dynamic policy); frames agentic threats as system threats. Student-authored record. | #71, #78, #39 |
| `aws-threat-composer` — AWS Threat Composer | thin |  | free | **medium** | Structured threat statements with AI/MCP-assisted workflow; agentic prior art. | #58, #78 |
| `cisa-ai-in-ot-principles` — Principles for the Secure Integration of Artificial Intelligence in Operational Technology | complete | in open PR library#32 (not edited) | free | **medium** | AI-in-OT risks incl. prompt injection. In student PR library#32. | #39, #71 |
| `cisa-framing-software-component-transparency` — Framing Software Component Transparency: Establishing a Common Software Bill of Materials  | complete |  | free | **medium** | Baseline attributes for SBOM ingest. | #38, DEC-009 |
| `cncf-supply-chain-best-practices-v2` — Software Supply Chain Best Practices v2 | complete |  | free | **medium** | Supply-chain stages and threats; RPT-0013 and supply-chain lane. | #67, #80 |
| `cytoscape-js` — Cytoscape.js documentation and project | thin |  | free | **medium** | Candidate KG renderer for the GUI lane (RPT-0006). | #59 |
| `d3fend` — MITRE D3FEND — defensive countermeasures knowledge graph (OWL) | thin | upgraded → library#36 | free | **medium** | OWL graph of countermeasures linked to ATT&CK techniques: a candidate source for typed `Mitigation` nodes and mitigates edges in the KG. | #17, #50, #59 |
| `deng-linddun-2011` — A privacy threat analysis framework: supporting the elicitation and fulfillment of privacy | complete |  | free | **medium** | LINDDUN privacy threat categories; post-MVP `method_facet` on ThreatInstance. | #36, DEC-005 |
| `esf-sscs-developers-2022` — Securing the Software Supply Chain: Recommended Practices Guide for Developers | complete (FX-1) |  | free | **medium** | Pairs threat scenarios with mitigations across the supply chain; worked threat→mitigation content. | #67, #80 |
| `evita-d2-3` — EVITA Deliverable D2.3: Security requirements for automotive on-board networks based on da | stub |  | free | **medium** | Automotive dark-side scenarios and attack trees cited by 21434; a worked automotive example for vectors. Student-authored stub. | #38, #63 |
| `fda-premarket-cybersecurity-guidance` — Cybersecurity in Medical Devices: Quality Management System Considerations and Content of  | complete (FX-1) |  | free | **medium** | Medical-device SPDF expects threat models and SBOMs; a regulated consumer of tmodel output. | #67, DEC-001b |
| `graphrag-ms` — GraphRAG (Microsoft Research, 2024) | thin |  | free | **medium** | LLM-built KG with community summaries; option for agentic report/extraction. | #75, #73 |
| `guac` — GUAC — Graph for Understanding Artifact Composition (OpenSSF) | thin |  | free | **medium** | Supply-chain graph (SBOM, SLSA, OSV, VEX) with pURL software trees; closest prior art for vulnerability propagation along composition (DEC-009). | #38, #80, DEC-009 |
| `hogan-kg-survey` — Knowledge Graphs (Hogan et al., ACM Computing Surveys 54(4), 2021) | thin |  | free | **medium** | Reference for RDF vs property-graph trade-offs behind ADR-0004/0008. | #25, #50 |
| `iec-62443-4-1-2018` — Security for industrial automation and control systems – Part 4-1: Secure product developm | complete |  | licensed | **medium** | Product-supplier SDL requirements; DEC-001b Requirement/Gate content. Licensed: paraphrase only. | #67, DEC-001b |
| `iso-iec-27034-1` — Information technology — Security techniques — Application security — Part 1: Overview and | complete |  | licensed | **medium** | ONF/ASC model: a governed control library, analogue of DEC-001b Requirement. Licensed. | #67, DEC-001b |
| `iso-iec-29147-2018` — Information technology — Security techniques — Vulnerability disclosure | complete |  | licensed (preview read) | **medium** | Vulnerability disclosure roles; the reporter/CNA side of Vulnerability provenance. Licensed. | #67, DEC-008 |
| `iso-iec-30111-2019` — Information technology — Security techniques — Vulnerability handling processes | complete |  | licensed (preview read) | **medium** | Vendor vulnerability handling; mitigation lifecycle (R-021). Licensed. | #67, DEC-009 |
| `iso-sae-pas-8475` — ISO/SAE PAS 8475, Road vehicles: Cybersecurity Assurance Levels (CAL) and Targeted Attack  | stub |  | licensed | **medium** | CAL and targeted attack feasibility (TAF); would refine ADR-0006 feasibility. Licensed and not yet published; stays a stub. | #38, #14, ADR-0006 |
| `linddun-org` — LINDDUN privacy threat modeling framework (linddun.org) | thin |  | free | **medium** | Current LINDDUN catalog for a privacy method facet. | #36 |
| `llm-programmatic-dual-use` — Exploiting Programmatic Behavior of LLMs: Dual-Use Through Standard Security Attacks | complete |  | free | **medium** | LLM misuse via program-like prompts; AI threat catalog content. | #71, #78 |
| `lockheed-kill-chain-2011` — Intelligence-Driven Computer Network Defense Informed by Analysis of Adversary Campaigns a | complete |  | free | **medium** | Kill-chain phases; source for `kill_chain_phase` on AttackStep. | #63, #36 |
| `mitre-attack-design-philosophy` — MITRE ATT&CK: Design and Philosophy | complete |  | free | **medium** | Defines tactic/technique/procedure semantics, which justify keeping kill-chain phase on AttackStep rather than as a node. | #17, #36 |
| `nist-sp-800-160` — NIST SP 800-160, Systems Security Engineering (Ross et al., 2018) | scaffold |  | free | **medium** | Systems security engineering lifecycle; context for DEC-001b gates and the SDL crosswalk. | #67, #19, DEC-001b |
| `ntia-sbom-minimum-elements` — The Minimum Elements For a Software Bill of Materials (SBOM) | complete |  | free | **medium** | SBOM data fields that feed Product/Component identity (DEC-009). | #38, DEC-009 |
| `owasp-asvs-5` — OWASP Application Security Verification Standard 5.0.0 | complete (FX-1) |  | free | **medium** | Verifiable requirements; candidate `Requirement` content for DEC-001b. | #67, DEC-001b |
| `owasp-pytm` — OWASP pytm | thin |  | free | **medium** | Threat-model-as-code with rule-based threat generation; prior art for the engine. | #63 |
| `owasp-threat-dragon` — OWASP Threat Dragon | thin |  | free | **medium** | Reference OSS app (diagram, threats, mitigations); UX baseline. | #58, #59 |
| `owasp-threat-model-library` — OWASP Threat Model Library and TM-BOM | thin |  | free | **medium** | TM-BOM interchange direction; relevant to ADR-0007 export. | #64 |
| `rdf-1-1-concepts` — RDF 1.1 Concepts and Abstract Syntax | thin |  | free | **medium** | Triple and named-graph model under Oxigraph (ADR-0008). | #50, #52 |
| `securechain-okn` — SecureChain — Knowledge Graph for Resilient, Trustworthy, Secure Software Supply Chains (P | thin |  | free | **medium** | Supply-chain KG; prior art for product composition graphs. | #25, #38 |
| `sei-threat-modeling-methods-2018` — Threat Modeling: A Summary of Available Methods | complete |  | free | **medium** | Survey of 12 methods; cited by BRON; a quick comparison table for RPT-0002. | #36 |
| `shacl` — Shapes Constraint Language (SHACL) | thin |  | free | **medium** | Validation of graph shapes; the §13 integrity gate for reviewed Assertions may use it. | #50, DEC-001b |
| `sigma-js` — Sigma.js documentation and project | thin |  | free | **medium** | WebGL renderer for larger graphs (RPT-0006). | #59 |
| `sp-800-161r1` — Cybersecurity Supply Chain Risk Management Practices for Systems and Organizations | stub |  | free | **medium** | C-SCRM practices; supply-chain threat sources for DEC-009 and the supply-chain lane. | #80, #38 |
| `sp-800-218a` — Secure Software Development Practices for Generative AI and Dual-Use Foundation Models: An | complete (FX-1) |  | free | **medium** | SSDF profile for AI models; agentic/AI SDL requirements. | #67, #71 |
| `sparql-1-1` — SPARQL 1.1 Query Language | thin |  | free | **medium** | Query language of the working store (Oxigraph); property paths for backbone traversal. | #50, #59 |
| `spml-image-prompt-injection` — Defending Language Models Against Image-Based Prompt Attacks via User-Provided Specificati | complete |  | free | **medium** | Image-based prompt injection and spec-driven defense; AI attack + mitigation pair. | #71, #78 |
| `threagile` — Threagile | thin |  | free | **medium** | YAML architecture model with risk rules and tracking; prior art for R-021 mitigation lifecycle. | #63, DEC-009 |
| `threattree-help` — ThreatTree Help Center | thin |  | free | **medium** | Commercial DFD + AND/OR attack trees with likelihood×impact register; closest product to the tmodel model. | #58, #63 |
| `trike-v1-2005` — Trike v.1 Methodology Document [Draft] | complete |  | free | **medium** | Requirements-model-driven, automatable threat generation with a risk model; prior art for engine-proposed threats. | #36, #63 |
| `ucedavelez-pasta-owasp-2012` — Real World Threat Modeling Using the PASTA Methodology | complete |  | free | **medium** | PASTA seven-stage, risk-centric method; attack-simulation stage parallels tmodel attack paths. | #36 |
| `unifying-llm-kg` — Unifying Large Language Models and Knowledge Graphs: A Roadmap (Pan et al., IEEE TKDE 2024 | thin |  | free | **medium** | KG-grounded LLM patterns; relevant to agentic extraction into the KG. | #75, #73 |
| `bsi-tr-03183-1` — BSI TR-03183-1 Cyber Resilience Requirements for Manufacturers and Products, Part 1: Gener | complete (FX-1) |  | free | **low** | CRA reading for manufacturers; RPT-0013. | #67 |
| `bsi-tr-03185` — BSI TR-03185 Secure Software Lifecycle | complete (FX-1) |  | free | **low** | Secure lifecycle requirements; RPT-0013. | #67 |
| `bsimm-16` — BSIMM16 — Building Security In Maturity Model (Report 2026) | complete (FX-1) |  | free | **low** | Observed practice data; RPT-0013. | #67 |
| `cis-safecode-sbd-assessment-1-1` — Secure by Design v1.1: A Guide to Assessing Software Security Practices | stub |  | free | **low** | SDL assessment guide; RPT-0013 input. | #67 |
| `cisa-secure-by-demand-guide-2024` — Secure by Demand Guide: How Software Customers Can Drive a Secure Technology Ecosystem | complete (FX-1) |  | free | **low** | Buyer questions; RPT-0013. | #67 |
| `cisa-secure-by-demand-ot-2025` — Secure by Demand: Priority Considerations for Operational Technology Owners and Operators  | complete |  | free | **low** | OT buyer priorities; RPT-0013. | #67 |
| `cisa-secure-by-design-2023` — Shifting the Balance of Cybersecurity Risk: Principles and Approaches for Secure by Design | complete (FX-1) |  | free | **low** | SbD principles; RPT-0013. | #67 |
| `cisa-secure-by-design-pledge-2024` — Secure by Design Pledge | complete (FX-1) |  | free | **low** | SbD pledge goals; RPT-0013. | #67 |
| `cisa-ssdf-attestation-form-2024` — Secure Software Development Attestation Form (with Instructions) | complete (FX-1) |  | free | **low** | Attestation form; DEC-001b evidence model analogue. | #67, DEC-001b |
| `d3-js` — D3.js documentation and project | thin |  | free | **low** | Visualization toolkit without a graph model. | #59 |
| `devici-sd-elements-integration` — Devici–SD Elements integration generally available | stub |  | free | **low** | Vendor release note; OTM in use. | #64 |
| `enisa-sbd-playbook-2026` — ENISA Secure by Design and Default Playbook: A Practical Guide to Secure by Design and Def | complete (FX-1) |  | free | **low** | SbD playbook; RPT-0013. | #67 |
| `etsi-ts-104-219` — Cyber Security (CYBER); Software Security Development and Implementation Framework (SSDIF) | complete (FX-1) |  | free | **low** | SSDIF; RPT-0013. | #67 |
| `fips-140-2` — FIPS 140-2, Security Requirements for Cryptographic Modules (superseded by FIPS 140-3) | scaffold |  | free | **low** | Superseded crypto-module standard; m-of-n scope. | — |
| `frink-fabric` — FRINK — FabRic Integrating Networked Knowledge (RENCI, Proto-OKN Theme 2) | thin |  | free | **low** | Federated SPARQL fabric; context for federation, not MVP. | #25 |
| `gephi` — Gephi desktop documentation and project | thin |  | free | **low** | Desktop analysis tool; not embeddable. | #59 |
| `iec-81001-5-1-2021` — Health software and health IT systems safety, effectiveness and security – Part 5-1: Secur | complete |  | licensed | **low** | Health-software SDL; licensed. | #67 |
| `iriusrisk-creating-threat-model` — IriusRisk — Creating a threat model | thin |  | free | **low** | Vendor docs; IaC and AI inputs. | #58 |
| `iso-24089-2023` — ISO 24089:2023, Road vehicles: Software update engineering | stub |  | licensed | **low** | Vehicle software-update engineering; licensed; stays a stub. | #38 |
| `iso-26262-3-2018` — ISO 26262-3:2018, Road vehicles — Functional safety — Part 3: Concept phase | scaffold |  | licensed | **low** | Functional-safety HARA; analogue for the S in S/F/O/P. Licensed; stays a stub. | #38 |
| `iso-iec-19790` — ISO/IEC 19790:2012, Security requirements for cryptographic modules | scaffold |  | licensed | **low** | Crypto module requirements; licensed; outside tmodel scope except as a product-family example. | — |
| `iso-iec-24759` — ISO/IEC 24759:2017, Test requirements for cryptographic modules | scaffold |  | licensed | **low** | Crypto module test requirements; licensed. | — |
| `iso-iec-29100-2024` — ISO/IEC 29100:2024, Information technology: Security techniques: Privacy framework | stub |  | not checked | **low** | Privacy framework terms (PII); availability of the 2024 edition not checked. | #36 |
| `iso-iec-5962-2021` — Information technology — SPDX Specification V2.2.1 | scaffold |  | licensed; SPDX text free | **low** | ISO adoption of SPDX 2.2.1; the free SPDX text is equivalent. | #38 |
| `iso-pas-5112-2022` — ISO/PAS 5112:2022, Road vehicles: Guidelines for auditing cybersecurity engineering | stub |  | licensed | **low** | Audit of cybersecurity engineering; governance-adjacent (DEC-001b); licensed; stays a stub. | #38, DEC-001b |
| `iso-sae-tr-8477` — ISO/SAE TR 8477, Road vehicles: Cybersecurity verification and validation | stub |  | licensed | **low** | Cybersecurity V&V for vehicles; licensed; stays a stub. | #38 |
| `kuzu` — Kùzu graph database | thin |  | free | **low** | Archived embedded graph DB. | #59 |
| `kuzu-explorer` — Kùzu Explorer | thin |  | free | **low** | Explorer UI for Kùzu. | #59 |
| `mcp-okn` — mcp-okn — Model Context Protocol access to NSF OKN graphs | thin |  | free | **low** | MCP access to OKN graphs; pattern for agent access to the KG. | #25, #78 |
| `memgraph-lab` — Memgraph Lab documentation | thin |  | free | **low** | Memgraph UI. | #59 |
| `microsoft-sdl` — Microsoft Security Development Lifecycle (SDL) Practices | complete (FX-1) |  | free | **low** | Current SDL practices incl. threat modeling; RPT-0013. | #67 |
| `microsoft-sdl-5-2` — Microsoft Security Development Lifecycle (SDL) Process Guidance – Version 5.2 | complete (FX-1) |  | free | **low** | SDL 5.2 process; RPT-0013. | #67 |
| `microsoft-sdl-simplified-2010` — Simplified Implementation of the Microsoft SDL | complete (FX-1) |  | free | **low** | Minimum SDL bar; RPT-0013. | #67 |
| `microsoft-threat-modeling-tool-features` — Microsoft Threat Modeling Tool feature overview | thin |  | free | **low** | Vendor docs; STRIDE per element. | #58 |
| `microsoft-threat-modeling-tool-overview` — Microsoft Threat Modeling Tool overview | thin |  | free | **low** | Vendor docs. | #58 |
| `neo4j-bloom` — Neo4j Bloom user guide | thin |  | free | **low** | Neo4j UI; reference for exploration UX. | #59 |
| `nsf-23-571` — NSF 23-571: Building the Prototype Open Knowledge Network (Proto-OKN) | thin |  | free | **low** | Proto-OKN solicitation; context. | #25 |
| `nsf-okn-launch` — NSF Open Knowledge Network (NSF OKN) — public launch | thin |  | free | **low** | OKN context for RPT-0011. | #25 |
| `okn-roadmap-2022` — Open Knowledge Network Roadmap: Powering the Next Data Revolution (NSF/OSTP, 2022) | thin |  | free | **low** | OKN vision; context. | #25 |
| `omb-m-22-18` — M-22-18: Enhancing the Security of the Software Supply Chain through Secure Software Devel | complete (FX-1) |  | free | **low** | Federal attestation policy; RPT-0013. | #67 |
| `omb-m-23-16` — M-23-16: Update to Memorandum M-22-18, Enhancing the Security of the Software Supply Chain | complete (FX-1) |  | free | **low** | Update to M-22-18; RPT-0013. | #67 |
| `omb-m-26-05` — M-26-05: Adopting a Risk-based Approach to Software and Hardware Security | complete (FX-1) |  | free | **low** | Rescinds M-22-18/23-16; RPT-0013. | #67 |
| `openssf-concise-guide-secure-software` — Concise Guide for Developing More Secure Software | complete |  | free | **low** | Developer guide; RPT-0013. | #67 |
| `openssf-osps-baseline` — Open Source Project Security Baseline (OSPS Baseline) v2026.08.28 | complete (FX-1) |  | free | **low** | OSS project baseline; RPT-0013. | #67 |
| `openssf-scorecard-checks` — OpenSSF Scorecard — Check Documentation (v5.5.0) | complete |  | free | **low** | Repo checks; possible evidence source for Review. | #67 |
| `owasp-dsomm` — OWASP DevSecOps Maturity Model (DSOMM) | complete |  | free | **low** | DevSecOps maturity; RPT-0013. | #67 |
| `owasp-samm-2` — OWASP Software Assurance Maturity Model (SAMM) v2 | complete (FX-1) |  | free | **low** | Maturity model; RPT-0013. | #67 |
| `owasp-threat-dragon-guide` — OWASP Developer Guide — Threat Dragon | thin |  | free | **low** | User guide for Threat Dragon. | #58 |
| `owl-2-primer` — OWL 2 Web Ontology Language Primer | thin |  | free | **low** | OWL reasoning; tmodel uses LinkML→OWL only as an export. | #53 |
| `pasta-risk-centric-threat-modeling` — Risk Centric Threat Modeling: Process for Attack Simulation and Threat Analysis | stub |  | free | **low** | PASTA book; paywalled, stays a stub. The free walkthrough record covers the method. | #36 |
| `pci-secure-slc-2` — PCI Secure Software Lifecycle (Secure SLC) Standard v2.0 | complete |  | free | **low** | Payment SDL; RPT-0013. | #67 |
| `pretrained-encoders-secure-learning` — Pre-trained Encoders in Self-Supervised Learning Improve Secure and Privacy-preserving Sup | complete |  | free | **low** | Image-classifier certified defenses; not GenAI apps. | #81 |
| `sae-j3061` — SAE J3061, Cybersecurity Guidebook for Cyber-Physical Vehicle Systems (superseded by ISO/S | scaffold |  | licensed | **low** | Superseded by ISO/SAE 21434; SAE paywall; stays a stub. | #38 |
| `safecode-fpssd-3` — Fundamental Practices for Secure Software Development: Essential Elements of a Secure Deve | complete (FX-1) |  | free | **low** | SDL practices; RPT-0013. | #67 |
| `sagai-workshop` — SAGAI — IEEE Security and Privacy workshop series on securing generative AI (2024–) | thin |  | free | **low** | Venue record. | #39 |
| `sd-elements-threat-modeling-datasheet` — SD Elements Threat Modeling Datasheet | thin |  | free | **low** | Vendor datasheet. | #58 |
| `sei-octave-allegro-2007` — Introducing OCTAVE Allegro: Improving the Information Security Risk Assessment Process | complete |  | free | **low** | Organisational risk assessment (assets, areas of concern); little bearing on product attack paths. | #36 |
| `sp-800-204d` — SP 800-204D: Strategies for the Integration of Software Supply Chain Security in DevSecOps | complete (FX-1) |  | free | **low** | CI/CD supply-chain controls; RPT-0013. | #67 |
| `sp-800-218r1` — Secure Software Development Framework (SSDF) Version 1.2: Recommendations for Mitigating t | complete (FX-1) |  | free | **low** | SSDF 1.2 draft; RPT-0013. | #67 |
| `sp-800-53r5` — SP 800-53 Rev. 5: Security and Privacy Controls for Information Systems and Organizations | complete |  | free | **low** | Control catalog; mitigation vocabulary. | #67 |
| `sudokn-okn` — SUDOKN — Supply and Demand Open Knowledge Network (Arizona State U., Proto-OKN) | thin |  | free | **low** | Manufacturing supply/demand KG; tangential. | #25 |
| `threat-dragon-tmf-format` — Threat Dragon Threat Model File format and TM-BOM direction | thin |  | free | **low** | Tool format note. | #64 |
| `threatmodeler-vast` — VAST (Visual, Agile, and Simple Threat) modeling — ThreatModeler | thin |  | free | **low** | Vendor description of VAST; marketing-level. | #36 |
| `uk-software-security-code-of-practice` — Software Security Code of Practice | complete (FX-1) |  | free | **low** | Voluntary code; RPT-0013. | #67 |
| `yfiles-html` — yFiles for HTML developer documentation | thin |  | free | **low** | Commercial diagramming SDK. | #59 |

## Inherited m-of-n items (282)

| Item | Record on `main` | This review | Availability | Relevance | Impact | Related |
|---|---|---|---|---|---|---|
| `cisa-2026-sbom-minimum` — 2026 Minimum Elements for a Software Bill of Materials (SBOM) | stub |  | free | **medium** | 2026 SBOM minimum elements; current SBOM ingest baseline. | #38, DEC-009 |
| `cox-2024-xz-timeline` — Timeline of the xz open source attack | stub |  | free | **medium** | xz attack timeline; step order for a worked attack path. | #80, #63 |
| `crowdstrike-sunspot` — SUNSPOT: An Implant in the Build Process | stub |  | free | **medium** | Build-process implant; build-stage attack step. | #80, #63 |
| `cve-2024-3094` — CVE-2024-3094 (xz-utils backdoor, CVSS 10.0) | stub |  | free | **medium** | The xz CVE (CVSS 10.0); a backbone example where CVE→CWE→CAPEC may break. | #80, #61 |
| `draft-asor-wimse-agent-delegation-chain` — Verifiable Attenuated Delegation for AI Agent Chains | stub |  | free | **medium** | Attenuated delegation for agent chains; agentic mitigation. | #78 |
| `draft-hamr-oauth-agent-delegation` — An Attenuated Delegation Profile for Automated Agents | stub |  | free | **medium** | OAuth delegation profile for agents; agentic mitigation. | #78 |
| `draft-mih-scitt-agent-action-capsule` — An Agent Action Capsule Profile for SCITT | scaffold |  | free | **medium** | Signed record of agent actions; evidence for reviewing AI-proposed Assertions. | #78, DEC-001b |
| `draft-niyikiza-oauth-attenuating-agent-tokens` — Attenuating Authorization Tokens for Agentic Delegation Chains | stub |  | free | **medium** | Attenuating tokens for agent chains; agentic mitigation. | #78 |
| `eu-cra-2024-2847` — Regulation (EU) 2024/2847 of the European Parliament and of the Council of 23 October 2024 | complete (FX-1) |  | free | **medium** | CRA essential requirements incl. vulnerability handling and SBOM; regulatory consumer of tmodel output (DEC-001b gates). | #67, DEC-001b |
| `fireeye-sunburst` — Highly Evasive Attacker Leverages SolarWinds Supply Chain with SUNBURST Backdoor | stub |  | free | **medium** | SUNBURST analysis; multi-stage supply-chain attack path. | #80, #63 |
| `freund-2024-xz` — backdoor in upstream xz/liblzma leading to ssh server compromise | stub |  | free | **medium** | xz backdoor disclosure; canonical multi-step supply-chain attack for a worked vector. | #80, #63 |
| `hardy-1988-confused-deputy` — The Confused Deputy (or why capabilities might have been invented) | stub |  | free | **medium** | Confused-deputy problem; the classic shape of agent tool-misuse threats. | #78 |
| `in-toto-2019` — in-toto: Providing farm-to-table guarantees for bits and bytes | stub |  | free | **medium** | Supply-chain layout/attestation threat model; supply-chain attack steps for the supply-chain lane. | #80 |
| `ohm-2020-backstabbers` — Backstabber's Knife Collection: A Review of Open Source Software Supply Chain Attacks | stub |  | free | **medium** | Taxonomy of OSS supply-chain attacks (typosquatting, injection); attack-path content for the supply-chain lane. | #80, #38 |
| `prakash-2026-aip` — AIP: Agent Identity Protocol for Verifiable Delegation Across MCP and A2A | stub |  | free | **medium** | Agent identity/delegation across MCP and A2A; agentic trust boundary threats. | #78 |
| `sigstore-threat-model` — Sigstore Threat Model | stub |  | free | **medium** | Published threat model of a real system; a worked example to encode as tmodel vectors. | #80, #63 |
| `slsa-1-2` — SLSA Specification v1.2 | complete (FX-1) |  | free | **medium** | Supply-chain threat diagram (source/build/dependency threats) and levels; mitigations and threats for the supply-chain lane. | #80, #67 |
| `slsa-2026-mini-shai-hulud` — Mini Shai-Hulud: Where SLSA's Boundaries Fall | stub |  | free | **medium** | Where SLSA does not cover a real worm; a worked supply-chain attack path. | #80 |
| `tuf-2010` — Survivable key compromise in software update systems | stub |  | free | **medium** | Update-system key-compromise threats; worked supply-chain threat model. | #80 |
| `veski-2026-capmas` — CAPMAS: Capability-Based Delegation of Privileges in Multi-Agent Systems | stub |  | free | **medium** | Capability delegation in multi-agent systems; agentic privilege threats/mitigations. | #78 |
| `aclu-fahrenheit-451-2` — Fahrenheit 451.2: Is Cyberspace Burning? | stub |  | free | **low** | Why trust infrastructures fail to be adopted (m-of-n scope). | — |
| `android-key-attestation` — Android Key and ID Attestation | stub |  | free | **low** | Hardware/TEE attestation (m-of-n scope); possible future evidence for hardware ProductInstance identity. | — |
| `apple-app-attest` — DCAppAttestService / App Attest | stub |  | free | **low** | Hardware/TEE attestation (m-of-n scope); possible future evidence for hardware ProductInstance identity. | — |
| `arm-cca-den0125` — Learn the architecture: Introducing Arm Confidential Compute Architecture | stub |  | free | **low** | Hardware/TEE attestation (m-of-n scope); possible future evidence for hardware ProductInstance identity. | — |
| `aws-snp-attestation` — Attest an Amazon EC2 instance with AMD SEV-SNP | stub |  | free | **low** | Hardware/TEE attestation (m-of-n scope); possible future evidence for hardware ProductInstance identity. | — |
| `biscuit-spec-3-3` — Biscuit Specification v3.3 | stub |  | free | **low** | Capability/delegation authorization (m-of-n scope). | — |
| `brickell-2004-daa` — Direct Anonymous Attestation | stub |  | free | **low** | Hardware/TEE attestation (m-of-n scope); possible future evidence for hardware ProductInstance identity. | — |
| `c2pa-2-4` — Content Credentials: C2PA Technical Specification 2.4 | stub |  | free | **low** | Content-provenance display (m-of-n scope). | — |
| `c2pa-conformance-program` — C2PA Conformance Program and Trust List | stub |  | free | **low** | Content-provenance display (m-of-n scope). | — |
| `c2pa-ux-2-2` — C2PA User Experience Guidance for Implementers 2.2 | stub |  | free | **low** | Content-provenance display (m-of-n scope). | — |
| `ca-sb-942` — California AI Transparency Act SB 942, as amended by AB 853 | stub |  | free | **low** | Why trust infrastructures fail to be adopted (m-of-n scope). | — |
| `cabforum-sc063` — Ballot SC-063v4: Make OCSP Optional, Require CRLs | stub |  | free | **low** | PKI naming/revocation governance (m-of-n scope); no bearing on tmodel model or risk. | — |
| `cabforum-smime-br` — CA/Browser Forum Baseline Requirements for S/MIME Certificates | stub |  | free | **low** | PKI naming/revocation governance (m-of-n scope); no bearing on tmodel model or risk. | — |
| `cabforum-tls-br` — CA/Browser Forum Baseline Requirements for TLS Server Certificates | stub |  | free | **low** | PKI naming/revocation governance (m-of-n scope); no bearing on tmodel model or risk. | — |
| `cawg-identity-1-2` — CAWG Identity Assertion 1.2 | stub |  | free | **low** | Content-provenance display (m-of-n scope). | — |
| `ccadb` — Common CA Database (CCADB) public reports | stub |  | free | **low** | PKI naming/revocation governance (m-of-n scope); no bearing on tmodel model or risk. | — |
| `chung-2018-must-staple` — Is the Web Ready for OCSP Must-Staple? | stub |  | free | **low** | PKI naming/revocation governance (m-of-n scope); no bearing on tmodel model or risk. | — |
| `cisa-ed-21-01` — Emergency Directive 21-01: Mitigate SolarWinds Orion Code Compromise | stub |  | free | **low** | SolarWinds emergency directive. | #80 |
| `cnsa-2-0` — Commercial National Security Algorithm Suite 2.0 (CNSA 2.0) Algorithms and FAQ | stub |  | free | **low** | PQC migration (m-of-n scope). | — |
| `cscw-2023-provenance-trust` — Examining the Impact of Provenance-Enabled Media on Trust and Accuracy Perceptions | stub |  | free | **low** | Content-provenance display (m-of-n scope). | — |
| `cve-2019-13050` — CVE-2019-13050: SKS keyserver certificate spamming attack | stub |  | free | **low** | Why trust infrastructures fail to be adopted (m-of-n scope). | — |
| `dennis-vanhorn-1966` — Programming Semantics for Multiprogrammed Computations | stub |  | free | **low** | Capability/delegation authorization (m-of-n scope). | — |
| `did-key-method` — The did:key Method v0.9 | stub |  | free | **low** | PKI naming/revocation governance (m-of-n scope); no bearing on tmodel model or risk. | — |
| `diffie-hellman-1976` — New Directions in Cryptography | stub |  | free | **low** | Signature-scheme history (m-of-n scope). | — |
| `draft-ffm-rats-cca-token` — Arm CCA Reference Attestation Token | stub |  | free | **low** | Hardware/TEE attestation (m-of-n scope); possible future evidence for hardware ProductInstance identity. | — |
| `draft-ietf-cbor-cddl-modules` — CDDL Module Structure | scaffold |  | free | **low** | CBOR/COSE encoding (m-of-n scope); tmodel interchange is LinkML/JSON/RDF (ADR-0007). | — |
| `draft-ietf-cbor-cde` — CBOR Common Deterministic Encoding (CDE) | scaffold |  | free | **low** | Deterministic encoding (m-of-n scope). | — |
| `draft-ietf-cbor-edn-literals` — Concise Diagnostic Notation (CDN) | scaffold |  | free | **low** | CBOR/COSE encoding (m-of-n scope); tmodel interchange is LinkML/JSON/RDF (ADR-0007). | — |
| `draft-ietf-cbor-packed` — Packed CBOR | scaffold |  | free | **low** | CBOR/COSE encoding (m-of-n scope); tmodel interchange is LinkML/JSON/RDF (ADR-0007). | — |
| `draft-ietf-cbor-serialization` — CBOR Serialization and Determinism | scaffold |  | free | **low** | Deterministic encoding (m-of-n scope). | — |
| `draft-ietf-lamps-pq-composite-sigs` — Composite ML-DSA for use in X.509 Public Key Infrastructure | stub |  | free | **low** | PQC migration (m-of-n scope). | — |
| `draft-ietf-rats-corim` — Concise Reference Integrity Manifest (CoRIM) | stub |  | free | **low** | Hardware/TEE attestation (m-of-n scope); possible future evidence for hardware ProductInstance identity. | — |
| `draft-ietf-scitt-scrapi` — SCITT Reference APIs (SCRAPI) | stub |  | free | **low** | SCITT API; m-of-n scope. | — |
| `draft-ietf-spki-cert-structure` — Simple Public Key Certificate (expired, never published) | stub |  | free | **low** | PKI naming/revocation governance (m-of-n scope); no bearing on tmodel model or risk. | — |
| `draft-ietf-vcon-vcon-core-04` — The JSON format for vCon - Conversation Data Container | complete |  | free | **low** | Signed-statement formats (m-of-n scope). | — |
| `draft-mcnally-deterministic-cbor` — dCBOR: Deterministic CBOR | scaffold |  | free | **low** | Deterministic encoding (m-of-n scope). | — |
| `ecma-424` — ECMA-424 CycloneDX Bill of Materials Specification, 2nd Edition | stub |  | free | **low** | Pointer to cyclonedx-1-7. | #38 |
| `eff-2010-ssliverse` — An Observatory for the SSLiverse | stub |  | free | **low** | PKI naming/revocation governance (m-of-n scope); no bearing on tmodel model or risk. | — |
| `elgamal-1985` — A Public Key Cryptosystem and a Signature Scheme Based on Discrete Logarithms | stub |  | free | **low** | Signature-scheme history (m-of-n scope). | — |
| `ellison-schneier-2000-ten-risks` — Ten Risks of PKI: What You're not Being Told about Public Key Infrastructure | stub |  | free | **low** | Why trust infrastructures fail to be adopted (m-of-n scope). | — |
| `eo-14028` — Executive Order 14028: Improving the Nation's Cybersecurity | complete (FX-1) |  | free | **low** | US supply-chain policy; RPT-0013. | #67 |
| `eo-14144` — Executive Order 14144: Strengthening and Promoting Innovation in the Nation's Cybersecurit | complete |  | free | **low** | US cyber EO; RPT-0013. | #67 |
| `eo-14306` — Executive Order 14306: Sustaining Select Efforts To Strengthen the Nation's Cybersecurity  | complete |  | free | **low** | US cyber EO; RPT-0013. | #67 |
| `eu-ai-act-art-50` — EU AI Act Article 50: Transparency Obligations | stub |  | free | **low** | Why trust infrastructures fail to be adopted (m-of-n scope). | — |
| `eu-code-of-practice-marking` — EU Code of Practice on marking and labelling AI-generated content | stub |  | free | **low** | Why trust infrastructures fail to be adopted (m-of-n scope). | — |
| `event-stream-issue-116` — event-stream issue #116: I don't know what to say. | stub |  | free | **low** | event-stream incident thread. | #80 |
| `fips-140-3` — FIPS 140-3, Security Requirements for Cryptographic Modules | complete |  | free | **low** | Crypto-module standard; m-of-n scope. | — |
| `fips-180-4` — Secure Hash Standard (SHS) | complete |  | free | **low** | NIST crypto standards (m-of-n scope). | — |
| `fips-186` — FIPS 186: Digital Signature Standard (DSS), 1994 | stub |  | free | **low** | Signature-scheme history (m-of-n scope). | — |
| `fips-186-1` — FIPS 186-1: Digital Signature Standard (DSS), 1998 | stub |  | free | **low** | Signature-scheme history (m-of-n scope). | — |
| `fips-186-2` — FIPS 186-2: Digital Signature Standard (DSS), 2000 | stub |  | free | **low** | Signature-scheme history (m-of-n scope). | — |
| `fips-186-3` — FIPS 186-3: Digital Signature Standard (DSS), 2009 | stub |  | free | **low** | Signature-scheme history (m-of-n scope). | — |
| `fips-186-4` — Digital Signature Standard (DSS), FIPS 186-4 | stub |  | free | **low** | NIST crypto standards (m-of-n scope). | — |
| `fips-186-5` — Digital Signature Standard (DSS) | complete |  | free | **low** | NIST crypto standards (m-of-n scope). | — |
| `fips-202` — SHA-3 Standard: Permutation-Based Hash and Extendable-Output Functions | complete |  | free | **low** | NIST crypto standards (m-of-n scope). | — |
| `fips-203` — Module-Lattice-Based Key-Encapsulation Mechanism Standard | complete |  | free | **low** | NIST crypto standards (m-of-n scope). | — |
| `fips-204` — Module-Lattice-Based Digital Signature Standard | complete |  | free | **low** | PQC migration (m-of-n scope). | — |
| `fips-205` — Stateless Hash-Based Digital Signature Standard | complete |  | free | **low** | PQC migration (m-of-n scope). | — |
| `foxit-2012-black-tulip` — Black Tulip: Report of the investigation into the DigiNotar CA breach | stub |  | free | **low** | PKI naming/revocation governance (m-of-n scope); no bearing on tmodel model or risk. | — |
| `ghsa-event-stream` — GHSA-mh6f-8j2x-4483 (event-stream / flatmap-stream) | stub |  | free | **low** | GHSA advisory for event-stream; OSV/GHSA shape. | #80 |
| `gittuf-2025` — Rethinking Trust in Forge-Based Git Security (gittuf) | stub |  | free | **low** | Git forge trust; supply-chain mitigation. | #80 |
| `gmr-1984-paradoxical` — A Paradoxical Solution to The Signature Problem | stub |  | free | **low** | Signature-scheme history (m-of-n scope). | — |
| `gmr-1988-adaptive` — A Digital Signature Scheme Secure Against Adaptive Chosen-Message Attacks | stub |  | free | **low** | Signature-scheme history (m-of-n scope). | — |
| `gmy-1983-strong-signatures` — Strong Signature Schemes | stub |  | free | **low** | Signature-scheme history (m-of-n scope). | — |
| `gnupg-key-management` — GnuPG manual: OpenPGP Key Management (tsign, trustspec) | stub |  | free | **low** | PKI naming/revocation governance (m-of-n scope); no bearing on tmodel model or risk. | — |
| `go-nameconstraint-cves` — Go crypto/x509 name-constraint defects (five CVEs, 2025-2026) | stub |  | free | **low** | PKI naming/revocation governance (m-of-n scope); no bearing on tmodel model or risk. | — |
| `golang-61963` — TUBITAK Kamu SM root should be constrained (golang/go#61963) | stub |  | free | **low** | PKI naming/revocation governance (m-of-n scope); no bearing on tmodel model or risk. | — |
| `google-2016-wosign` — Distrusting WoSign and StartCom Certificates | stub |  | free | **low** | PKI naming/revocation governance (m-of-n scope); no bearing on tmodel model or risk. | — |
| `google-2017-symantec` — Chrome's Plan to Distrust Symantec Certificates | stub |  | free | **low** | PKI naming/revocation governance (m-of-n scope); no bearing on tmodel model or risk. | — |
| `google-open-dice` — Open Profile for DICE | stub |  | free | **low** | Hardware/TEE attestation (m-of-n scope); possible future evidence for hardware ProductInstance identity. | — |
| `gutmann-2002-pki-not-dead` — PKI: It's Not Dead, Just Resting | stub |  | free | **low** | Why trust infrastructures fail to be adopted (m-of-n scope). | — |
| `gvu-1998-webmaster-survey` — GVU 10th WWW User Survey: webmaster PICS labelling rates | stub |  | free | **low** | Why trust infrastructures fail to be adopted (m-of-n scope). | — |
| `iana-cbor-simple-values` — IANA Concise Binary Object Representation (CBOR) Simple Values Registry | scaffold |  | free | **low** | CBOR working-group context (m-of-n scope). | — |
| `iana-cbor-tags` — IANA Concise Binary Object Representation (CBOR) Tags Registry | scaffold |  | free | **low** | CBOR working-group context (m-of-n scope). | — |
| `iana-cose-algorithms` — IANA COSE Algorithms registry | complete |  | free | **low** | PKI naming/revocation governance (m-of-n scope); no bearing on tmodel model or risk. | — |
| `ide-2025-signals-of-provenance` — Signals of Provenance: Navigating Indicators in AI-Generated Media for Sighted and Blind I | stub |  | free | **low** | Content-provenance display (m-of-n scope). | — |
| `ietf-cbor-wg` — IETF Concise Binary Object Representation Maintenance and Extensions (CBOR) Working Group | scaffold |  | free | **low** | CBOR working-group context (m-of-n scope). | — |
| `ietf-cose-wg` — IETF CBOR Object Signing and Encryption (COSE) Working Group | scaffold |  | free | **low** | CBOR working-group context (m-of-n scope). | — |
| `ietf-spki-wg` — IETF SPKI Working Group charter and documents | stub |  | free | **low** | Why trust infrastructures fail to be adopted (m-of-n scope). | — |
| `ietf-vcon-wg` — IETF vCon Working Group | stub |  | free | **low** | Signed-statement formats (m-of-n scope). | — |
| `in-toto-attestation-v1` — in-toto Attestation Framework v1 | scaffold |  | free | **low** | Signed-statement formats (m-of-n scope). | — |
| `in-toto-envelope-v1` — in-toto Attestation Framework: Envelope | stub |  | free | **low** | PQC migration (m-of-n scope). | — |
| `intel-sgx-dcap-quotelib` — Intel SGX ECDSA QuoteLibReference (DCAP API) | stub |  | free | **low** | Hardware/TEE attestation (m-of-n scope); possible future evidence for hardware ProductInstance identity. | — |
| `intel-tdx-dcap-quoting` — Intel TDX DCAP Quoting Library API | stub |  | free | **low** | Hardware/TEE attestation (m-of-n scope); possible future evidence for hardware ProductInstance identity. | — |
| `intel-tdx-whitepaper` — Intel Trust Domain Extensions (white paper) | stub |  | free | **low** | Hardware/TEE attestation (m-of-n scope); possible future evidence for hardware ProductInstance identity. | — |
| `iso-iec-11889-2015` — ISO/IEC 11889:2015 Trusted Platform Module Library | stub |  | licensed (TCG TPM 2.0 Library is free) | **low** | TPM library (ISO adoption; licensed); m-of-n scope. | — |
| `iso-iec-5962` — ISO/IEC 5962:2021 SPDX Specification V2.2.1 | stub |  | licensed; SPDX text free | **low** | ISO adoption of SPDX 2.2.1. | #38 |
| `itu-x509` — ITU-T X.509: The Directory - Public-key and attribute certificate frameworks | stub |  | free | **low** | PKI naming/revocation governance (m-of-n scope); no bearing on tmodel model or risk. | — |
| `itu-x509-1988` — ITU-T X.509 (1988): The Directory - Authentication framework | stub |  | free | **low** | PKI naming/revocation governance (m-of-n scope); no bearing on tmodel model or risk. | — |
| `keys-openpgp-org-faq` — keys.openpgp.org FAQ: third-party certification policy | stub |  | free | **low** | Why trust infrastructures fail to be adopted (m-of-n scope). | — |
| `kitchenham-charters-2007` — Guidelines for performing Systematic Literature Reviews in Software Engineering | stub |  | free | **low** | SLR method used for research reports. | #86 |
| `lamport-1979-one-way` — Constructing Digital Signatures from a One Way Function | stub |  | free | **low** | Signature-scheme history (m-of-n scope). | — |
| `langley-2011-revocation` — Revocation doesn't work | stub |  | free | **low** | PKI naming/revocation governance (m-of-n scope); no bearing on tmodel model or risk. | — |
| `langley-2014-revchecking` — No, don't enable revocation checking | stub |  | free | **low** | PKI naming/revocation governance (m-of-n scope); no bearing on tmodel model or risk. | — |
| `larisch-2017-crlite` — CRLite: A Scalable System for Pushing All TLS Revocations to All Browsers | stub |  | free | **low** | PKI naming/revocation governance (m-of-n scope); no bearing on tmodel model or risk. | — |
| `letsencrypt-ocsp-eol` — OCSP Service Has Reached End of Life | stub |  | free | **low** | PKI naming/revocation governance (m-of-n scope); no bearing on tmodel model or risk. | — |
| `liu-2015-revocation` — An End-to-End Measurement of Certificate Revocation in the Web's PKI | stub |  | free | **low** | PKI naming/revocation governance (m-of-n scope); no bearing on tmodel model or risk. | — |
| `macaroons-2014` — Macaroons: Cookies with Contextual Caveats for Decentralized Authorization in the Cloud | stub |  | free | **low** | Capability/delegation authorization (m-of-n scope). | — |
| `merkle-1979-thesis` — Secrecy, Authentication, and Public Key Systems | stub |  | free | **low** | Signature-scheme history (m-of-n scope). | — |
| `merkle-1980-protocols` — Protocols for Public Key Cryptosystems | stub |  | free | **low** | Signature-scheme history (m-of-n scope). | — |
| `merkle-1989-certified` — A Certified Digital Signature | stub |  | free | **low** | Signature-scheme history (m-of-n scope). | — |
| `moruzzi-2025-content-authenticities` — Content Authenticities: A Discussion on the Values of Provenance Data for Creatives and Th | stub |  | free | **low** | Content-provenance display (m-of-n scope). | — |
| `mozilla-2013-anssi` — Revoking Trust in one ANSSI Certificate | stub |  | free | **low** | PKI naming/revocation governance (m-of-n scope); no bearing on tmodel model or risk. | — |
| `mozilla-2013-turktrust` — Revoking Trust in Two TurkTrust Certificates | stub |  | free | **low** | PKI naming/revocation governance (m-of-n scope); no bearing on tmodel model or risk. | — |
| `mozilla-bug-856060` — Name Constraints ignored by libPKIX verification engine | stub |  | free | **low** | PKI naming/revocation governance (m-of-n scope); no bearing on tmodel model or risk. | — |
| `nist-sp-800-140` — NIST SP 800-140, FIPS 140-3 Derived Test Requirements (DTR): CMVP updates to ISO/IEC 24759 | complete |  | free | **low** | CMVP test documents (m-of-n scope). | — |
| `nist-sp-800-140a` — NIST SP 800-140A, CMVP Documentation Requirements | thin |  | free | **low** | CMVP test documents (m-of-n scope). | — |
| `nist-sp-800-140b` — NIST SP 800-140B, CMVP Security Policy Requirements | complete |  | free | **low** | CMVP test documents (m-of-n scope). | — |
| `nist-sp-800-140c` — NIST SP 800-140C, CMVP Approved Security Functions | complete |  | free | **low** | CMVP test documents (m-of-n scope). | — |
| `nist-sp-800-140d` — NIST SP 800-140D, CMVP Approved Sensitive Security Parameter Generation and Establishment  | thin |  | free | **low** | CMVP test documents (m-of-n scope). | — |
| `nist-sp-800-140e` — NIST SP 800-140E, CMVP Approved Authentication Mechanisms | thin |  | free | **low** | CMVP test documents (m-of-n scope). | — |
| `nist-sp-800-140f` — NIST SP 800-140F, CMVP Approved Non-Invasive Attack Mitigation Test Metrics | thin |  | free | **low** | CMVP test documents (m-of-n scope). | — |
| `nistir-8547` — NIST IR 8547 ipd: Transition to Post-Quantum Cryptography Standards | stub |  | free | **low** | PQC migration (m-of-n scope). | — |
| `nistir-8610` — NIST IR 8610: Status Report on the Second Round of the Additional Digital Signature Scheme | stub |  | free | **low** | PQC migration (m-of-n scope). | — |
| `npm-event-stream` — Details about the event-stream incident | stub |  | free | **low** | npm incident write-up. | #80 |
| `nsa-2025-content-credentials` — Content Credentials: Strengthening Multimedia Integrity in the Generative AI Era | stub |  | free | **low** | Content-provenance display (m-of-n scope). | — |
| `ntia-2021-sbom-minimum` — The Minimum Elements For a Software Bill of Materials (SBOM) | stub |  | free | **low** | Duplicate of the NTIA minimum elements record. | #38 |
| `openssl-2022-email-overflow` — CVE-2022-3786 and CVE-2022-3602: X.509 Email Address Buffer Overflows | stub |  | free | **low** | PKI naming/revocation governance (m-of-n scope); no bearing on tmodel model or risk. | — |
| `pics-1-1-labels` — PICS 1.1 Label Distribution: Label Syntax and Communication Protocols | stub |  | free | **low** | Content-provenance display (m-of-n scope). | — |
| `pics-1-1-services` — PICS 1.1 Rating Services and Rating Systems and Their Machine Readable Descriptions | stub |  | free | **low** | Content-provenance display (m-of-n scope). | — |
| `pics-censorship-faq` — PICS, Censorship, and Intellectual Freedom FAQ | stub |  | free | **low** | Why trust infrastructures fail to be adopted (m-of-n scope). | — |
| `pics-dsig-1-0` — PICS Signed Labels (DSig) 1.0 Specification | stub |  | free | **low** | Content-provenance display (m-of-n scope). | — |
| `powder-description-resources` — POWDER: Description Resources | stub |  | free | **low** | Content-provenance display (m-of-n scope). | — |
| `prisma-2020` — The PRISMA 2020 statement: an updated guideline for reporting systematic reviews | stub |  | free | **low** | Systematic-review reporting guideline. | #86 |
| `psscrm-v1` — Proactive Software Supply Chain Risk Management Framework (P-SSCRM) Version 1 | stub |  | free | **low** | Why trust infrastructures fail to be adopted (m-of-n scope). | — |
| `ptacek-2024-macaroons` — Macaroons Escalated Quickly | stub |  | free | **low** | Capability/delegation authorization (m-of-n scope). | — |
| `pypi-trusted-publishers` — Trusted Publishers for PyPI | stub |  | free | **low** | OIDC publishing mitigation. | #80 |
| `rabin-1979-tr212` — Digitalized Signatures and Public-Key Functions as Intractable as Factorization | stub |  | free | **low** | Signature-scheme history (m-of-n scope). | — |
| `rfc-1422` — PEM Part II: Certificate-Based Key Management | stub |  | free | **low** | PKI naming/revocation governance (m-of-n scope); no bearing on tmodel model or risk. | — |
| `rfc-1952` — GZIP | stub |  | free | **low** | Signed-statement formats (m-of-n scope). | — |
| `rfc-2692` — SPKI Requirements | stub |  | free | **low** | Authorization reduction (m-of-n scope). | — |
| `rfc-2693` — SPKI Certificate Theory | scaffold |  | free | **low** | Authorization reduction (m-of-n scope). | — |
| `rfc-3280` — Internet X.509 PKI Certificate and CRL Profile (2002) | stub |  | free | **low** | PKI naming/revocation governance (m-of-n scope); no bearing on tmodel model or risk. | — |
| `rfc-3339` — Timestamps | stub |  | free | **low** | Signed-statement formats (m-of-n scope). | — |
| `rfc-3820` — Internet X.509 PKI Proxy Certificate Profile | stub |  | free | **low** | Authorization reduction (m-of-n scope). | — |
| `rfc-3966` — tel URI | stub |  | free | **low** | Signed-statement formats (m-of-n scope). | — |
| `rfc-4119` — GEOPRIV | stub |  | free | **low** | Signed-statement formats (m-of-n scope). | — |
| `rfc-4122` — UUID | stub |  | free | **low** | Signed-statement formats (m-of-n scope). | — |
| `rfc-4880` — OpenPGP Message Format | stub |  | free | **low** | PKI naming/revocation governance (m-of-n scope); no bearing on tmodel model or risk. | — |
| `rfc-5280` — Internet X.509 Public Key Infrastructure Certificate and CRL Profile | stub |  | free | **low** | PKI naming/revocation governance (m-of-n scope); no bearing on tmodel model or risk. | — |
| `rfc-5321` — SMTP | stub |  | free | **low** | Signed-statement formats (m-of-n scope). | — |
| `rfc-5914` — Trust Anchor Format | stub |  | free | **low** | PKI naming/revocation governance (m-of-n scope); no bearing on tmodel model or risk. | — |
| `rfc-5937` — Using Trust Anchor Constraints during Certification Path Processing | stub |  | free | **low** | PKI naming/revocation governance (m-of-n scope); no bearing on tmodel model or risk. | — |
| `rfc-6068` — mailto URI | stub |  | free | **low** | Signed-statement formats (m-of-n scope). | — |
| `rfc-6749` — The OAuth 2.0 Authorization Framework | stub |  | free | **low** | Capability/delegation authorization (m-of-n scope). | — |
| `rfc-6750` — The OAuth 2.0 Authorization Framework: Bearer Token Usage | stub |  | free | **low** | Capability/delegation authorization (m-of-n scope). | — |
| `rfc-6818` — Updates to the Internet X.509 PKI Certificate and CRL Profile | stub |  | free | **low** | PKI naming/revocation governance (m-of-n scope); no bearing on tmodel model or risk. | — |
| `rfc-6960` — X.509 Internet PKI Online Certificate Status Protocol (OCSP) | stub |  | free | **low** | PKI naming/revocation governance (m-of-n scope); no bearing on tmodel model or risk. | — |
| `rfc-6962` — Certificate Transparency | stub |  | free | **low** | PKI naming/revocation governance (m-of-n scope); no bearing on tmodel model or risk. | — |
| `rfc-7049` — Concise Binary Object Representation (CBOR) | scaffold |  | free | **low** | CBOR/COSE encoding (m-of-n scope); tmodel interchange is LinkML/JSON/RDF (ADR-0007). | — |
| `rfc-7515` — JWS | stub |  | free | **low** | Signed-statement formats (m-of-n scope). | — |
| `rfc-7516` — JWE | stub |  | free | **low** | Signed-statement formats (m-of-n scope). | — |
| `rfc-7633` — X.509v3 TLS Feature Extension (OCSP Must-Staple) | stub |  | free | **low** | PKI naming/revocation governance (m-of-n scope); no bearing on tmodel model or risk. | — |
| `rfc-7800` — Proof-of-Possession Key Semantics for JSON Web Tokens (JWTs) | stub |  | free | **low** | Capability/delegation authorization (m-of-n scope). | — |
| `rfc-8032` — Edwards-Curve Digital Signature Algorithm (EdDSA) | stub |  | free | **low** | Signature-scheme history (m-of-n scope). | — |
| `rfc-8152` — CBOR Object Signing and Encryption (COSE) | scaffold |  | free | **low** | CBOR/COSE encoding (m-of-n scope); tmodel interchange is LinkML/JSON/RDF (ADR-0007). | — |
| `rfc-8230` — Using RSA Algorithms with CBOR Object Signing and Encryption (COSE) Messages | scaffold |  | free | **low** | CBOR/COSE encoding (m-of-n scope); tmodel interchange is LinkML/JSON/RDF (ADR-0007). | — |
| `rfc-8259` — JSON | stub |  | free | **low** | Signed-statement formats (m-of-n scope). | — |
| `rfc-8391` — XMSS: eXtended Merkle Signature Scheme | stub |  | free | **low** | PQC migration (m-of-n scope). | — |
| `rfc-8392` — CBOR Web Token (CWT) | scaffold |  | free | **low** | CBOR/COSE encoding (m-of-n scope); tmodel interchange is LinkML/JSON/RDF (ADR-0007). | — |
| `rfc-8550` — S/MIME Version 4.0 Certificate Handling | stub |  | free | **low** | PKI naming/revocation governance (m-of-n scope); no bearing on tmodel model or risk. | — |
| `rfc-8551` — S/MIME Version 4.0 Message Specification | stub |  | free | **low** | PKI naming/revocation governance (m-of-n scope); no bearing on tmodel model or risk. | — |
| `rfc-8554` — Leighton-Micali Hash-Based Signatures | stub |  | free | **low** | PQC migration (m-of-n scope). | — |
| `rfc-8555` — Automatic Certificate Management Environment (ACME) | stub |  | free | **low** | Why trust infrastructures fail to be adopted (m-of-n scope). | — |
| `rfc-8610` — Concise Data Definition Language (CDDL): A Notational Convention to Express Concise Binary | scaffold |  | free | **low** | CBOR/COSE encoding (m-of-n scope); tmodel interchange is LinkML/JSON/RDF (ADR-0007). | — |
| `rfc-8620` — JMAP | stub |  | free | **low** | Signed-statement formats (m-of-n scope). | — |
| `rfc-8742` — Concise Binary Object Representation (CBOR) Sequences | scaffold |  | free | **low** | CBOR/COSE encoding (m-of-n scope); tmodel interchange is LinkML/JSON/RDF (ADR-0007). | — |
| `rfc-8746` — Concise Binary Object Representation (CBOR) Tags for Typed Arrays | scaffold |  | free | **low** | CBOR/COSE encoding (m-of-n scope); tmodel interchange is LinkML/JSON/RDF (ADR-0007). | — |
| `rfc-8747` — Proof-of-Possession Key Semantics for CBOR Web Tokens (CWTs) | scaffold |  | free | **low** | CBOR/COSE encoding (m-of-n scope); tmodel interchange is LinkML/JSON/RDF (ADR-0007). | — |
| `rfc-8769` — Cryptographic Message Syntax (CMS) Content Types for Concise Binary Object Representation  | scaffold |  | free | **low** | CBOR working-group context (m-of-n scope). | — |
| `rfc-8778` — Use of the HSS/LMS Hash-Based Signature Algorithm with CBOR Object Signing and Encryption  | scaffold |  | free | **low** | CBOR/COSE encoding (m-of-n scope); tmodel interchange is LinkML/JSON/RDF (ADR-0007). | — |
| `rfc-8812` — CBOR Object Signing and Encryption (COSE) and JSON Object Signing and Encryption (JOSE) Re | scaffold |  | free | **low** | CBOR working-group context (m-of-n scope). | — |
| `rfc-8943` — Concise Binary Object Representation (CBOR) Tags for Date | scaffold |  | free | **low** | CBOR/COSE encoding (m-of-n scope); tmodel interchange is LinkML/JSON/RDF (ADR-0007). | — |
| `rfc-8949` — Concise Binary Object Representation (CBOR) | complete (FX-1) |  | free | **low** | CBOR/COSE encoding (m-of-n scope); tmodel interchange is LinkML/JSON/RDF (ADR-0007). | — |
| `rfc-9021` — Use of the Walnut Digital Signature Algorithm with CBOR Object Signing and Encryption (COS | scaffold |  | free | **low** | CBOR/COSE encoding (m-of-n scope); tmodel interchange is LinkML/JSON/RDF (ADR-0007). | — |
| `rfc-9052` — CBOR Object Signing and Encryption (COSE): Structures and Process | complete (FX-1) |  | free | **low** | CBOR/COSE encoding (m-of-n scope); tmodel interchange is LinkML/JSON/RDF (ADR-0007). | — |
| `rfc-9053` — CBOR Object Signing and Encryption (COSE): Initial Algorithms | complete |  | free | **low** | CBOR/COSE encoding (m-of-n scope); tmodel interchange is LinkML/JSON/RDF (ADR-0007). | — |
| `rfc-9054` — CBOR Object Signing and Encryption (COSE): Hash Algorithms | scaffold |  | free | **low** | CBOR/COSE encoding (m-of-n scope); tmodel interchange is LinkML/JSON/RDF (ADR-0007). | — |
| `rfc-9068` — JSON Web Token (JWT) Profile for OAuth 2.0 Access Tokens | stub |  | free | **low** | Capability/delegation authorization (m-of-n scope). | — |
| `rfc-9090` — Concise Binary Object Representation (CBOR) Tags for Object Identifiers | scaffold |  | free | **low** | CBOR/COSE encoding (m-of-n scope); tmodel interchange is LinkML/JSON/RDF (ADR-0007). | — |
| `rfc-9110` — HTTP Semantics | stub |  | free | **low** | Signed-statement formats (m-of-n scope). | — |
| `rfc-9162` — Certificate Transparency Version 2.0 | stub |  | free | **low** | PKI naming/revocation governance (m-of-n scope); no bearing on tmodel model or risk. | — |
| `rfc-9164` — Concise Binary Object Representation (CBOR) Tags for IPv4 and IPv6 Addresses and Prefixes | scaffold |  | free | **low** | CBOR/COSE encoding (m-of-n scope); tmodel interchange is LinkML/JSON/RDF (ADR-0007). | — |
| `rfc-9165` — Additional Control Operators for the Concise Data Definition Language (CDDL) | scaffold |  | free | **low** | CBOR/COSE encoding (m-of-n scope); tmodel interchange is LinkML/JSON/RDF (ADR-0007). | — |
| `rfc-9254` — Encoding of Data Modeled with YANG in the Concise Binary Object Representation (CBOR) | scaffold |  | free | **low** | CBOR working-group context (m-of-n scope). | — |
| `rfc-9277` — On Stable Storage for Items in Concise Binary Object Representation (CBOR) | scaffold |  | free | **low** | CBOR/COSE encoding (m-of-n scope); tmodel interchange is LinkML/JSON/RDF (ADR-0007). | — |
| `rfc-9334` — Remote ATtestation procedureS (RATS) Architecture | stub |  | free | **low** | RATS architecture; possible hardware evidence; m-of-n scope. | — |
| `rfc-9338` — CBOR Object Signing and Encryption (COSE): Countersignatures | scaffold |  | free | **low** | CBOR/COSE encoding (m-of-n scope); tmodel interchange is LinkML/JSON/RDF (ADR-0007). | — |
| `rfc-9360` — CBOR Object Signing and Encryption (COSE): Header Parameters for Carrying and Referencing  | scaffold |  | free | **low** | CBOR/COSE encoding (m-of-n scope); tmodel interchange is LinkML/JSON/RDF (ADR-0007). | — |
| `rfc-9396` — OAuth 2.0 Rich Authorization Requests | stub |  | free | **low** | Capability/delegation authorization (m-of-n scope). | — |
| `rfc-9421` — HTTP Message Signatures | stub |  | free | **low** | Capability/delegation authorization (m-of-n scope). | — |
| `rfc-9449` — OAuth 2.0 Demonstrating Proof of Possession (DPoP) | stub |  | free | **low** | Capability/delegation authorization (m-of-n scope). | — |
| `rfc-9459` — CBOR Object Signing and Encryption (COSE): AES-CTR and AES-CBC | scaffold |  | free | **low** | CBOR/COSE encoding (m-of-n scope); tmodel interchange is LinkML/JSON/RDF (ADR-0007). | — |
| `rfc-9528` — Ephemeral Diffie-Hellman Over COSE (EDHOC) | scaffold |  | free | **low** | CBOR working-group context (m-of-n scope). | — |
| `rfc-9529` — Traces of Ephemeral Diffie-Hellman Over COSE (EDHOC) | scaffold |  | free | **low** | CBOR working-group context (m-of-n scope). | — |
| `rfc-9549` — Internationalization Updates to RFC 5280 | stub |  | free | **low** | PKI naming/revocation governance (m-of-n scope); no bearing on tmodel model or risk. | — |
| `rfc-9580` — OpenPGP | stub |  | free | **low** | PKI naming/revocation governance (m-of-n scope); no bearing on tmodel model or risk. | — |
| `rfc-9581` — Concise Binary Object Representation (CBOR) Tags for Time, Duration, and Period | scaffold |  | free | **low** | CBOR/COSE encoding (m-of-n scope); tmodel interchange is LinkML/JSON/RDF (ADR-0007). | — |
| `rfc-9596` — CBOR Object Signing and Encryption (COSE) "typ" (type) Header Parameter | scaffold |  | free | **low** | CBOR/COSE encoding (m-of-n scope); tmodel interchange is LinkML/JSON/RDF (ADR-0007). | — |
| `rfc-9597` — CBOR Web Token (CWT) Claims in COSE Headers | scaffold |  | free | **low** | CBOR/COSE encoding (m-of-n scope); tmodel interchange is LinkML/JSON/RDF (ADR-0007). | — |
| `rfc-9598` — Internationalized Email Addresses in X.509 Certificates | stub |  | free | **low** | PKI naming/revocation governance (m-of-n scope); no bearing on tmodel model or risk. | — |
| `rfc-9608` — No Revocation Available for X.509 Public Key Certificates | stub |  | free | **low** | PKI naming/revocation governance (m-of-n scope); no bearing on tmodel model or risk. | — |
| `rfc-9618` — Updates to X.509 Policy Validation | stub |  | free | **low** | PKI naming/revocation governance (m-of-n scope); no bearing on tmodel model or risk. | — |
| `rfc-9668` — Using Ephemeral Diffie-Hellman Over COSE (EDHOC) with the Constrained Application Protocol | scaffold |  | free | **low** | CBOR working-group context (m-of-n scope). | — |
| `rfc-9679` — CBOR Object Signing and Encryption (COSE) Key Thumbprint | scaffold |  | free | **low** | CBOR/COSE encoding (m-of-n scope); tmodel interchange is LinkML/JSON/RDF (ADR-0007). | — |
| `rfc-9682` — Updates to the Concise Data Definition Language (CDDL) Grammar | scaffold |  | free | **low** | CBOR/COSE encoding (m-of-n scope); tmodel interchange is LinkML/JSON/RDF (ADR-0007). | — |
| `rfc-9711` — The Entity Attestation Token (EAT) | stub |  | free | **low** | Hardware/TEE attestation (m-of-n scope); possible future evidence for hardware ProductInstance identity. | — |
| `rfc-9741` — Concise Data Definition Language (CDDL): Additional Control Operators for the Conversion a | scaffold |  | free | **low** | CBOR/COSE encoding (m-of-n scope); tmodel interchange is LinkML/JSON/RDF (ADR-0007). | — |
| `rfc-9781` — A Concise Binary Object Representation (CBOR) Tag for Unprotected CBOR Web Token Claims Se | scaffold |  | free | **low** | CBOR/COSE encoding (m-of-n scope); tmodel interchange is LinkML/JSON/RDF (ADR-0007). | — |
| `rfc-9804` — Simple Public Key Infrastructure (SPKI) S-Expressions | complete (FX-1) |  | free | **low** | Deterministic encoding (m-of-n scope). | — |
| `rfc-9864` — Fully-Specified Algorithms for JSON Object Signing and Encryption (JOSE) and CBOR Object S | scaffold |  | free | **low** | CBOR/COSE encoding (m-of-n scope); tmodel interchange is LinkML/JSON/RDF (ADR-0007). | — |
| `rfc-9921` — CBOR Object Signing and Encryption (COSE) Header Parameter for Timestamp Tokens as Defined | scaffold |  | free | **low** | CBOR/COSE encoding (m-of-n scope); tmodel interchange is LinkML/JSON/RDF (ADR-0007). | — |
| `rfc-9942` — CBOR Object Signing and Encryption (COSE) Receipts | complete |  | free | **low** | CBOR/COSE encoding (m-of-n scope); tmodel interchange is LinkML/JSON/RDF (ADR-0007). | — |
| `rfc-9943` — An Architecture for Trustworthy and Transparent Digital Supply Chains | complete |  | free | **low** | SCITT architecture; transparency for statements; possible DEC-001b approval evidence. | DEC-001b |
| `rfc-9964` — ML-DSA for JSON Object Signing and Encryption (JOSE) and CBOR Object Signing and Encryptio | complete |  | free | **low** | CBOR/COSE encoding (m-of-n scope); tmodel interchange is LinkML/JSON/RDF (ADR-0007). | — |
| `rfc-9995` — CBOR Object Signing and Encryption (COSE) Hash Envelope | scaffold |  | free | **low** | CBOR/COSE encoding (m-of-n scope); tmodel interchange is LinkML/JSON/RDF (ADR-0007). | — |
| `rfc-9997` — YANG-CBOR: Allocating SID Ranges for Private Enterprise Number (PEN) Holders | scaffold |  | free | **low** | CBOR working-group context (m-of-n scope). | — |
| `rsa-1978` — A Method for Obtaining Digital Signatures and Public-Key Cryptosystems | stub |  | free | **low** | Signature-scheme history (m-of-n scope). | — |
| `schnorr-1989-smartcards` — Efficient Identification and Signatures for Smart Cards | stub |  | free | **low** | Signature-scheme history (m-of-n scope). | — |
| `schnorr-1991-jcryptology` — Efficient Signature Generation by Smart Cards | stub |  | free | **low** | Signature-scheme history (m-of-n scope). | — |
| `sdsi-1-1` — SDSI — A Simple Distributed Security Infrastructure, version 1.1 | stub |  | free | **low** | PKI naming/revocation governance (m-of-n scope); no bearing on tmodel model or risk. | — |
| `secure-systems-lab-dsse` — Dead Simple Signing Envelope (DSSE) | complete |  | free | **low** | Deterministic encoding (m-of-n scope). | — |
| `sev-snp-primer-2026` — AMD SEV-SNP: A Confidential Computing Primer | stub |  | free | **low** | Hardware/TEE attestation (m-of-n scope); possible future evidence for hardware ProductInstance identity. | — |
| `shor-1994` — Algorithms for Quantum Computation: Discrete Logarithms and Factoring | stub |  | free | **low** | PQC migration (m-of-n scope). | — |
| `shor-1997` — Polynomial-Time Algorithms for Prime Factorization and Discrete Logarithms on a Quantum Co | stub |  | free | **low** | PQC migration (m-of-n scope). | — |
| `sigstore-2022` — Sigstore: Software Signing for Everybody | stub |  | free | **low** | Signing infrastructure; supply-chain mitigation context. | #80 |
| `solarwinds-8k` — SolarWinds Form 8-K, Item 8.01, 14 December 2020 | stub |  | free | **low** | SolarWinds disclosure filing. | #80 |
| `sp-1800-38` — SP 1800-38: Migration to Post-Quantum Cryptography | stub |  | free | **low** | PQC migration (m-of-n scope). | — |
| `sp-800-186` — Recommendations for Discrete Logarithm-based Cryptography: Elliptic Curve Domain Parameter | complete |  | free | **low** | NIST crypto standards (m-of-n scope). | — |
| `sp-800-208` — Recommendation for Stateful Hash-Based Signature Schemes | complete |  | free | **low** | NIST crypto standards (m-of-n scope). | — |
| `sp-800-218` — SP 800-218: Secure Software Development Framework (SSDF) Version 1.1: Recommendations for  | complete (FX-1) |  | free | **low** | SSDF 1.1; RPT-0013. | #67 |
| `sp-800-57pt1r5` — Recommendation for Key Management: Part 1 - General | complete |  | free | **low** | NIST crypto standards (m-of-n scope). | — |
| `survey-2026-nameconstraints-measurement` — Name-constraint prevalence among CCADB-disclosed intermediate CA certificates (original me | stub |  | free | **low** | PKI naming/revocation governance (m-of-n scope); no bearing on tmodel model or risk. | — |
| `tcg-dice-cert-profiles` — DICE Certificate Profiles r01 | stub |  | free | **low** | Hardware/TEE attestation (m-of-n scope); possible future evidence for hardware ProductInstance identity. | — |
| `tcg-dice-hw-requirements` — Hardware Requirements for a Device Identifier Composition Engine r78 | stub |  | free | **low** | Hardware/TEE attestation (m-of-n scope); possible future evidence for hardware ProductInstance identity. | — |
| `tcg-dice-implicit-identity` — Implicit Identity Based Device Attestation v1 r0.93 | stub |  | free | **low** | Hardware/TEE attestation (m-of-n scope); possible future evidence for hardware ProductInstance identity. | — |
| `tcg-dice-layering` — DICE Layering Architecture v1.0 r0.19 | stub |  | free | **low** | Hardware/TEE attestation (m-of-n scope); possible future evidence for hardware ProductInstance identity. | — |
| `tcg-dice-symmetric` — Symmetric Identity Based Device Attestation v1 r0p94 | stub |  | free | **low** | Hardware/TEE attestation (m-of-n scope); possible future evidence for hardware ProductInstance identity. | — |
| `tcg-integrity-event-log` — TCG Guidance on Integrity Measurements and Event Log Processing v1 r0p118 | stub |  | free | **low** | Hardware/TEE attestation (m-of-n scope); possible future evidence for hardware ProductInstance identity. | — |
| `tcg-pc-client-pfp` — TCG PC Client Platform Firmware Profile Specification r1.05 | stub |  | free | **low** | Hardware/TEE attestation (m-of-n scope); possible future evidence for hardware ProductInstance identity. | — |
| `tcg-pc-client-ptp` — TCG PC Client Platform TPM Profile (PTP) for TPM 2.0 v1.06 r32 | stub |  | free | **low** | Hardware/TEE attestation (m-of-n scope); possible future evidence for hardware ProductInstance identity. | — |
| `tcg-tpm-1-2-main` — TPM Main Specification Version 1.2, Level 2, Revision 116 | stub |  | free | **low** | Hardware/TEE attestation (m-of-n scope); possible future evidence for hardware ProductInstance identity. | — |
| `tcg-tpm-2-0-library-184` — TPM 2.0 Library Specification, Parts 0-4, Version 184 | stub |  | free | **low** | Hardware/TEE attestation (m-of-n scope); possible future evidence for hardware ProductInstance identity. | — |
| `tcg-tpm-2-0-library-185` — TPM 2.0 Library Specification v1.85 (PQC: ML-KEM, ML-DSA) | stub |  | free | **low** | PQC migration (m-of-n scope). | — |
| `tcg-tpm2-keys-device-identity` — TPM 2.0 Keys for Device Identity and Attestation v1 r12 | stub |  | free | **low** | Hardware/TEE attestation (m-of-n scope); possible future evidence for hardware ProductInstance identity. | — |
| `tuf-spec` — The Update Framework Specification v1.0.36 | stub |  | free | **low** | TUF spec; m-of-n scope. | #80 |
| `tuf-tap-21` — TAP 21: ML-DSA signing scheme for TUF metadata | stub |  | free | **low** | PQC migration (m-of-n scope). | — |
| `tukaani-xz-backdoor` — XZ Utils backdoor (upstream project statement) | stub |  | free | **low** | Upstream xz statement. | #80 |
| `ucan-1-0` — User Controlled Authorization Network (UCAN) Specification v1.0.0 | stub |  | free | **low** | Capability/delegation authorization (m-of-n scope). | — |
| `ulrich-2011-openpgp-wot` — Investigating the OpenPGP Web of Trust | stub |  | free | **low** | Why trust infrastructures fail to be adopted (m-of-n scope). | — |
| `vu-2020-typosquatting` — Typosquatting and Combosquatting Attacks on the Python Ecosystem | stub |  | free | **low** | PyPI typosquatting measurement; supply-chain attack example. | #80 |
| `w3-org-pics` — W3C Platform for Internet Content Selection (PICS) | scaffold |  | free | **low** | Content-provenance display (m-of-n scope). | — |
| `w3c-did-1-1` — Decentralized Identifiers (DIDs) v1.1 | stub |  | free | **low** | PKI naming/revocation governance (m-of-n scope); no bearing on tmodel model or risk. | — |
| `w3c-did-core` — Decentralized Identifiers (DIDs) v1.0 | stub |  | free | **low** | Signed-statement formats (m-of-n scope). | — |
| `w3c-did-extensions-methods` — DID Extensions: Methods registry | stub |  | free | **low** | PKI naming/revocation governance (m-of-n scope); no bearing on tmodel model or risk. | — |
| `w3c-tag-obsolete-powder` — W3C TAG proposal to obsolete CC/PP and POWDER (issue 86) | stub |  | free | **low** | Why trust infrastructures fail to be adopted (m-of-n scope). | — |
| `wang-2006-reducing-spki` — Reducing the Dependence of SPKI/SDSI on PKI | stub |  | free | **low** | Why trust infrastructures fail to be adopted (m-of-n scope). | — |
| `wohlin-2014-snowballing` — Guidelines for snowballing in systematic literature studies and a replication in software  | stub |  | free | **low** | Snowballing method for citation chasing in #86. | #86 |
| `zcap-ld` — Authorization Capabilities (ZCAP-LD) v0.4.0-rc.6 | stub |  | free | **low** | Capability/delegation authorization (m-of-n scope). | — |
| `zhang-2014-heartbleed` — Analysis of SSL Certificate Reissues and Revocations in the Wake of Heartbleed | stub |  | free | **low** | PKI naming/revocation governance (m-of-n scope); no bearing on tmodel model or risk. | — |
| `zooko-2001-names` — Names: Decentralized, Secure, Human-Meaningful: Choose Two | stub |  | free | **low** | PKI naming/revocation governance (m-of-n scope); no bearing on tmodel model or risk. | — |
| `zoom-keybase-2020` — Zoom Acquires Keybase | stub |  | free | **low** | Why trust infrastructures fail to be adopted (m-of-n scope). | — |

## Records in open PRs that are not yet in the bibliography

These records exist only on open student PR branches, so they are not in the 414 above. They are assessed here so the index is complete when those PRs merge.

| Item | Relevance | Impact | Related |
|---|---|---|---|
| `lallie-2018-attack-graphs-fault-trees` | **medium** | Survey of attack-graph and fault-tree notations; evidence for how tmodel draws AND/OR paths. In student PR library#30. | #36, #63, #59 |
| `karpati-2014-attack-trees-misuse-cases` | **medium** | Comparison of attack trees and misuse cases. In student PR library#30. | #36 |
| `mitre-attack-flow` | **high** | Sequenced ATT&CK actions with AND/OR operators and conditions; the closest public schema to tmodel `AttackPath`. In student PR library#30. | #36, #63, #64 |
| `shostack-threat-modeling-2014` | **medium** | STRIDE-per-element and DFD practice; baseline method facet. In student PR library#30. | #36 |
| `shostack-2008-experiences-threat-modeling-microsoft` | **low** | Practice report. In student PR library#30. | #36 |
| `kohnfelder-garg-1999-threats-to-our-products` | **medium** | STRIDE origin. In student PR library#30. | #36 |
| `scandariato-2015-stride-descriptive-study` | **low** | Empirical STRIDE study. In student PR library#30. | #36 |
| `mbaka-tuma-2024-stride-replication` | **low** | Empirical STRIDE replication. In student PR library#30. | #36 |
| `tuma-2018-threat-analysis-slr` | **low** | SLR of threat analysis. In student PR library#30. | #36 |
| `verreydt-2024-threat-modeling-practice` | **low** | Practice study. In student PR library#30. | #36 |
| `xiong-2019-threat-modeling-slr` | **low** | SLR of threat modeling. In student PR library#30. | #36 |
| `lenovo-lena-xss-2025` | **medium** | Agent incident; in student PR library#22. | #78 |
