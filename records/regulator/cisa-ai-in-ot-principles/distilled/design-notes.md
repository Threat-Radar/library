---
record: cisa-ai-in-ot-principles
kind: design-notes
title: "cisa-ai-in-ot-principles — bearing on our design"
extracted: "2026-10-21"
reviewed_by: ""
---

# CISA et al., Secure Integration of AI in OT — bearing on tmodel

**What this is.** For every statement in `requirements.yaml`: (a) which tmodel decisions it bears
on, as they stand on tmodel `main` at `e1ae8c3` (2026-10-21), and (b) which AI attack class it
defends against, in NIST AI 100-2 E2025 terms (index ids `NISTAML.*`) and, where one fits, a MITRE
ATLAS technique id. Evidence for RPT-0009, not a decision: nothing here accepts a `DEC-*`. The
guidance itself binds nobody ("does not create policies, impose requirements, mandate actions",
Disclaimer p. 22).

**How to read the threat mapping.** Same conventions as `etsi-en-304-223/distilled/design-notes.md`:

- **stated** — the statement's own words name the risk (kept as `source_text`); the NIST class and
  ATLAS id are our translation, since the source prints neither.
- **inferred** — our reading, with a one-line rationale in `requirements.yaml`.
- Labels of ours outside the NIST attack taxonomy: **non-adversarial** (drift, hallucination,
  error rates), **conventional** (ordinary cyber means: network paths into OT, exfiltration,
  account abuse), **general** (names attacks on the AI system without a class).
- **ATLAS ids** were checked against ATLAS release 2026.09, the data file atlas.mitre.org itself
  loads (`/atlas-data/dist/v6/ATLAS-2026.09.yaml`, sha256 `935efa93…6688`); the technique pages
  are a JavaScript app and return HTTP 404 to a plain fetch. **NIST ids** are from the E2025
  taxonomy index (pp. x–xi, `https://doi.org/10.6028/NIST.AI.100-2e2025`).

**Two directions**, as for the EN: (1) **content** a tmodel user needs to model an AI-enabled OT
system; (2) **requirements on tmodel itself**, which proposes threats with AI. Most of this
guidance is (1); its human-in-the-loop and logging advice is also (2).

## Summary

136 entries; 50 carry a threat mapping, 22 of them to a NIST AI 100-2 attack class. An entry is counted once per class (as stated if any of its mappings to that class is stated).

| attack class | entries | stated | inferred | NIST AI 100-2 E2025 ids | ATLAS ids |
|---|---|---|---|---|---|
| Evasion | 4 | 1 | 3 | NISTAML.022 Evasion | AML.T0015, AML.T0041, AML.T0043 |
| Poisoning | 7 | 2 | 5 | NISTAML.013 Data Poisoning, NISTAML.026 Model Poisoning | AML.T0018, AML.T0018.000, AML.T0020, AML.T0059 |
| Privacy | 7 | 2 | 5 | NISTAML.031 Model Extraction, NISTAML.032 Reconstruction, NISTAML.034 Property Inference, NISTAML.036 Leaking information from user interactions, NISTAML.038 Data Extraction | AML.T0024, AML.T0024.000, AML.T0024.001, AML.T0024.002, AML.T0057 |
| Direct prompt injection | 4 | 0 | 4 | NISTAML.018 Prompt Injection | AML.T0051.000, AML.T0054 |
| Indirect prompt injection | 4 | 0 | 4 | NISTAML.015 Indirect Prompt Injection | AML.T0051.001, AML.T0053 |
| Supply chain | 6 | 0 | 6 | NISTAML.05 Supply Chain Attacks | AML.T0010, AML.T0010.001, AML.T0010.003 |
| Conventional (outside NIST AI 100-2: access, theft, tampering, network paths) | 16 | 4 | 12 | — | AML.T0012, AML.T0025, AML.T0035, AML.T0036, AML.T0122 |
| Non-adversarial (not an attack) | 18 | 8 | 10 | — | — |
| General (attacks on the AI system, no class) | 5 | 4 | 1 | — | — |

The pattern differs from the EN's. This guidance is mostly about **safety and reliability**: of its
ten Table 2 risks, one is an attack class (Cybersecurity Risks) and one has an adversarial part
(Data Quality: centralised operational data that "threat actors can use"); drift,
explainability, cognitive load, compliance, dependency, interoperability, complexity and
reliability are not attacks. Its
security advice is weighted to **conventional OT defences** around the AI system (segmentation,
push-based architectures, egress control, access control), which NIST AI 100-2 leaves out of
scope and ATLAS covers only partly. It names four AI attack classes itself: prompt injection and
guardrail bypass (Table 2), data poisoning (§2.2, §4.1) and adversarial inputs (§4.1).

## By decision

### ADR-0010 — core classes (accepted)

- **Inventory of AI components** (§4.1, "taking inventory of any AI components, as well as other
  components reliant on the AI"): `Component` plus the accepted `depends_on` / `uses_component`
  edges cover "reliant on the AI". The AI component itself needs a kind; tmodel#130 proposes
  `component_kind: machine_learning_model`.
- **ATLAS alongside ATT&CK** (§3.2, stated): ATLAS techniques are generic attack patterns, so they
  fit `AttackPattern.catalog_ref` beside ATT&CK and CAPEC ids. Adopt: a threat model of an
  AI-enabled OT system should carry both. **Gap:** `catalog_ref` is single-valued, while every
  mapping here pairs a NIST taxonomy class with one or more ATLAS techniques (open question 4).
- **Roles** (§1.2 "must clearly define and communicate these roles and responsibilities with the AI
  system manufacturer, OT supplier, and any system integrator or managed service provider"; §3.1
  roles list). **Gap:** the accepted core has no role slot. Its Party-ranged edges are
  `manufactured_by`, `supplied_by`, `owned_by`, `reported_by`, `assigned_by`,
  `implementation_owner`, `for_stakeholder`, `reviewer` and `owner`; system integrator and managed
  service provider (and, from the EN, Data Custodian, End-user, Affected entity) have no edge.
  They would need new typed edges, which means amending DEC-001a.
- **SBOM for AI** (§2.3, footnote 6: the minimum elements of an SBOM for AI software are the same
  as for all software): AI components take the same opaque `identifiers` (purl, SBOM ids) as any
  component. No new identity scheme is needed for MVP.
- **AI identity in logs** (§4.1, "so the logged AI identity is distinct from any typical machine
  or user identifiers"): the accepted `PartyKind` values are `organization` and `person`. An AI
  acting in the system is neither. tmodel#130 proposes `software_agent`, defined as "A tool or AI
  agent that makes Assertions"; this statement is about an AI acting inside the modelled system,
  so it is evidence for widening that proposed value, not for the value as written.
- **Phases**: part of the advice maps to `LifecyclePhaseCode` (`concept` for the §2.1 business
  case; `design`; `verification_validation` for §3.3; `deployment`; `operation`; `maintenance`).
  **Gap:** `LifecyclePhaseCode` has no procurement, governance, training or response value, and
  42 of the 136 entries here sit in those phases (`phase` in `requirements.yaml` uses the library's
  own phase vocabulary, not tmodel's).

### tmodel#130 — Asset, TrustBoundary, DataFlow (proposed, not accepted)

This guidance is the strongest source in RPT-0009 for tmodel#130, because OT security is
zone-and-conduit security:

| statement | needs | tmodel#130 element |
|---|---|---|
| Table 1 (Purdue levels 0–5); §2.4 DMZ or jump host | zones that nest | `TrustBoundary` with `within_boundary`, `trust_level` |
| §2.4 and §4.1 push-based or brokered architectures; one-way transfer; "not a persistent attack path into OT" | direction and boundary crossing of each flow | `DataFlow` (`flow_from`, `flow_to`, `bidirectional: false`, `crosses_boundary`) |
| §2.2 Data Assurance, Exposure of Sensitive Information; Prioritizing OT Data Protection | data worth protecting, and where it is stored | `Asset` (`stored_in`, `processed_by`, `security_properties`) |
| §2.2 "the data may become accessible or stored (statistically) … in the model" | training data that persists inside a model | `Asset.stored_in` a `machine_learning_model` component |
| §4.1 inventory of AI components | kind of component | `component_kind: machine_learning_model`, `data` |
| §4.1 distinct AI identity | an agent that is not a person or organization | `PartyKind: software_agent`, widened (see ADR-0010 above) |

### ADR-0006 — risk composite vector (accepted)

- **Impact categories.** Table 2's OT Impacts column maps onto the ISO 21434 S/F/O/P vector:
  "functional safety risks", "unsafe operating conditions" → safety; "financial losses",
  "increased maintenance costs" → financial; "impacted system availability", "production halts",
  "loss of productivity" → operational. Privacy appears only as a compliance concern (Regulatory
  Compliance row) and in §2.2, not as an impact. Several impacts have **no slot**:
  "reputational damage" (three rows: Cybersecurity Risks, Operator Cognitive Load, Regulatory
  Compliance), and also "network/OT compromise", "cascading compromise", "complexity in
  troubleshooting", "dependence on technology" and "increased documentation costs". ADR-0006
  keeps `business_impact` as a post-MVP axis with no slot and does not say what it covers, so
  filing reputational damage there is our inference; the others are consequences or costs the
  S/F/O/P vector does not try to carry.
- **Humans rate safety** (Table 2: LLMs "almost certainly should not be used to make safety
  decisions for OT environments"). ADR-0006 already makes impact human-supplied and feasibility
  human-rated at MVP. Adopt as stated support for that choice, and as a rule for tmodel itself
  (direction 2): its AI must not set a safety impact.
- **Feasibility.** §2.4 and §4.1's architecture advice (no persistent inbound access, one-way
  transfer, DMZ) lowers the feasibility of reaching OT through the AI system, which is the 21434
  "window of opportunity" factor (inferred).
- **False positives and negatives** (§4.1, understand error rates against the base rate) are an
  input to how much weight a human gives an AI-proposed finding, not a risk component.

### ADR-0007 — LinkML; OTM and STIX import (accepted)

The guidance defines no data format (record.yaml `not_applicable`). For the import mappings:
OTM `trustZones` and `dataflows` are exactly what the Purdue-level advice needs, and they land
nowhere in the accepted core without tmodel#130 (OTM schema at `c88c5a7`); an AI threat imported
from OTM has no dedicated slot for its ATLAS id (OTM threats carry `cwes`, `categories`, `tags`).

### DEC-001b — governed layer (open)

§3.1 is a governance program in miniature: a governance structure with named stakeholders,
leadership commitment, regular audits and compliance testing, continuous validation; §4.1 adds
KPIs and regular review sessions; §3.3 a test-before-production gate ("Operators should only move
the AI system into production for additional testing after sufficient testing in a
non-production environment"). These are inputs to `SecurityProgram`, `Gate` and `Checkpoint`.
The guidance gives no states or transitions, so no state machine was extracted.

### DEC-008 — CWE/NVD integration (open)

- §3.2: "traditional cybersecurity requirements, vulnerability management, and critical
  infrastructure regulations must be factored in when integrating AI systems." AI components are
  in scope of the CVE/NVD pipeline like any software (footnote 6, SBOM).
- §2.3 *Vendor Notifications* asks AI vendors to disclose when "the AI can provide improper advice
  or take inappropriate action": a behavioural defect that has no CVE form today.
- AI weaknesses partly in CWE 4.20: CWE-1426 *Improper Validation of Generative AI Output* (GenAI
  only) is the weakness the "should not make safety decisions" and validate-AI-output statements
  address for LLMs;
  CWE-1427 *Improper Neutralization of Input Used for LLM Prompting* is the weakness behind the
  prompt injection Table 2 names. Both links inferred.
- Mirror ATLAS with CWE/NVD if DEC-008 picks a cached mirror (see the EN's notes).

### DEC-009 — generic threat → product; mitigation lifecycle (open)

- **Vendor-embedded AI** (§2.3): AI arrives inside OT products ("Some OT devices now come with
  built-in AI technology"). A generic AI threat therefore maps onto a product family through the
  vendor, and members can differ: *Disabling AI Features* ("Specify conditions under which
  certain AI features can be disabled or enabled") makes AI presence a per-instance property, so
  the same threat applies to one instance and not another.
- **Lifecycle of the mitigation**: failsafe fallback to non-AI operation (§2.4, §3.4 thresholds,
  §4.2); drift monitoring and known good state (§4.1); retraining on new OT data (§4.1); incident
  response for AI failure states (§4.2).

### R-018 — human review (draft requirement)

- **Content (1).** Human-in-the-loop decision-making (§4.1), limiting active AI control without a
  human in the loop (§2.4), intervention points where AI updates control logic (§4.1), failsafes.
- **tmodel itself (2).** "Ultimately, humans are responsible for functional safety" (§4) and the
  audit-trail item (§4.1, "Logging of all AI system operating data (including timestamps, inputs,
  and outputs)") are R-018 and its provenance: tmodel's AI proposals should be logged with inputs
  and outputs, under an AI identity distinct from the human reviewer, and stay proposed until a
  `Review`.

## Weaknesses, threats and vulnerabilities (the sponsor's framing)

- **Threats.** `threats.yaml` lists the 32 risks and threats the guidance describes (all ten
  Table 2 rows, the §1.3 consequences, the §2.2 and §2.3 data and vendor risks, the §2.4 and §3.4
  challenges, the §4.1 attack vectors and the §4.2 failure and attack statements), in source order, each quoted, mapped where a class fits, with the
  statements that address it.
- **Weaknesses.** Two stated (an LLM in a safety decision path; lack of AI vendor transparency,
  moved from the threats after review) and three read as the negation of a recommendation
  (persistent inbound access into OT, an AI identity that logs cannot tell apart, active AI
  control without a human in the loop). Candidate CWE 4.20 ids, all inferred: CWE-1426 (GenAI
  only), CWE-653, CWE-778 and CWE-223; none fits vendor opacity or human-in-the-loop.
- **Vulnerabilities.** None: no product or CVE is named.

## Open questions for the sponsor

1. **Scope of "AI threat".** The guidance excludes misuse of AI and harmful content from its scope
   (Appendix, Risks) and spends most of Table 2 on non-adversarial risks. Should RPT-0009 count
   safety and reliability risks (drift, hallucination) as threats in the object model, or keep
   them out as non-adversarial?
2. **AI-enabled attacks** (§4.2: "so will the number of AI-enabled attacks on existing IT and OT
   systems") are attacks that *use* AI, outside NIST AI 100-2. Does tmodel model the attacker's
   use of AI at all (e.g. ATLAS AML.T0102 *Generate Malicious Commands*), or only attacks on AI?
3. **Continuous retraining on OT data** (§4.1) is also a poisoning exposure; the guidance does not
   say so. Flag it in RPT-0009 as a gap in the source?
4. **One attack, several ids.** `AttackPattern.catalog_ref` holds one id, but each mapping here is a
   NIST class (a taxonomy node, not a technique) plus one or more ATLAS techniques. Multivalued
   `catalog_ref`, one AttackPattern per ATLAS id with the NIST class as a classification, or
   something else?
5. **CWE ids for AI weaknesses.** `threats.yaml` gives candidate CWE 4.20 ids for the weaknesses
   (inferred, with each id's mapping-usage value); there is no CWE entry for predictive-ML
   weaknesses. Adopt these, or leave AI weaknesses without CWE?
6. **AI defects with no CVE.** *Vendor Notifications* (§2.3) asks vendors to disclose when "the AI
   can provide improper advice or take inappropriate action". Where does such a report live in
   the object model if it has no CVE?
7. **Mapping rule.** The inferred mappings follow our reading. ATLAS publishes which mitigations
   (`AML.M*`) address which techniques; should RPT-0009 derive or check the inferred mappings from
   those relations, which would also feed `Mitigation.catalog_ref`?
8. **Library records** for NIST AI 100-2 E2025 and ATLAS 2026.09 do not exist yet, so the ids here
   resolve only by citation. Add them (tmodel RPT-0014 already lists both as sources)?

## Source notes (kept as printed; not decisions)

- **Version.** The PDF file is the January 2026 revision (`508cV2`) but its Version History lists
  only "December 3, 2025: Initial version." What changed between versions is not stated.
- **Principle 4 title** differs between the Introduction and Conclusion ("Embed Safety and
  Security Practices") and the body and contents ("Embed Oversight and Failsafe Practices").
- The §3.2 ATLAS sentence ends with a comma at the end of the section (p. 17).

## Decision index

| decision | entries |
|---|---|
| ADR-0006 | 15: R-0001, R-0012, R-0014, R-0032, R-0034, R-0035, R-0036, R-0037, R-0080, R-0082, R-0086, R-0098, R-0107, R-0117, R-0120 |
| ADR-0007 | 5: R-0043, R-0051, R-0086, R-0087, R-0100 |
| ADR-0010 | 16: R-0011, R-0013, R-0015, R-0016, R-0039, R-0046, R-0051, R-0060, R-0071, R-0077, R-0083, R-0086, R-0087, R-0100, R-0109, R-0120 |
| DEC-001b | 27: R-0005, R-0011, R-0016, R-0017, R-0018, R-0030, R-0058, R-0059, R-0063, R-0067, R-0070, R-0071, R-0072, R-0074, R-0075, R-0077, R-0078, R-0080, R-0088, R-0089, R-0093, R-0096, R-0104, R-0114, R-0118, R-0119, R-0120 |
| DEC-008 | 7: R-0021, R-0051, R-0052, R-0081, R-0082, R-0087, R-0115 |
| DEC-009 | 29: R-0015, R-0019, R-0021, R-0022, R-0023, R-0025, R-0026, R-0038, R-0040, R-0045, R-0049, R-0050, R-0052, R-0060, R-0061, R-0066, R-0069, R-0079, R-0091, R-0097, R-0102, R-0108, R-0112, R-0121, R-0127, R-0128, R-0129, R-0132, R-0133 |
| R-018 | 29: R-0006, R-0010, R-0014, R-0028, R-0029, R-0031, R-0055, R-0065, R-0066, R-0068, R-0073, R-0084, R-0098, R-0099, R-0101, R-0104, R-0105, R-0106, R-0107, R-0109, R-0113, R-0114, R-0115, R-0118, R-0122, R-0123, R-0124, R-0126, R-0127 |
| tmodel#130 | 21: R-0020, R-0036, R-0039, R-0041, R-0042, R-0046, R-0047, R-0048, R-0053, R-0054, R-0056, R-0062, R-0064, R-0067, R-0076, R-0084, R-0095, R-0100, R-0116, R-0125, R-0126 |

## Mapping, statement by statement

Decisions: `bears_on` in `requirements.yaml`. Threat: attack class, **s** = stated, *i* = inferred.
A dash means a governance or process statement with no single attack class.

| id | provision | decisions | threat | NIST | ATLAS |
|---|---|---|---|---|---|
| `R-0001` | Despite the many benefits, integrating AI into operational technology … | ADR-0006 | non-adversarial (**s**); general (**s**) | — | — |
| `R-0002` | This guidance outlines four key principles critical infrastructure owners … | — | — | — | — |
| `R-0003` | Understand AI. Understand the unique risks and potential impacts … | — | — | — | — |
| `R-0004` | Consider AI Use in the OT Domain. Assess the … | — | — | — | — |
| `R-0005` | Establish AI Governance and Assurance Frameworks. Implement robust governance … | DEC-001b | — | — | — |
| `R-0006` | Embed Safety and Security Practices Into AI and AI-Enabled … | R-018 | — | — | — |
| `R-0007` | The authoring agencies encourage critical infrastructure owners and operators … | — | — | — | — |
| `R-0008` | The scope of this guidance focuses on ML- and … | — | — | — | — |
| `R-0009` | However, this guidance may also be applied to systems … | — | — | — | — |
| `R-0010` | Implementing error-checking can improve AI agent’s performance by avoiding … | R-018 | — | — | — |
| `R-0011` | Table 2 provides a broad overview of known AI … | ADR-0010, DEC-001b | evasion (*i*); poisoning (*i*); direct prompt injection (*i*); indirect prompt injection (*i*); supply chain (*i*); non-adversarial (*i*) | NISTAML.013, NISTAML.015, NISTAML.018, NISTAML.022, NISTAML.026, NISTAML.05 | AML.T0010.001, AML.T0015, AML.T0018, AML.T0020, AML.T0041, AML.T0043, AML.T0051.000, AML.T0051.001, AML.T0054 |
| `R-0012` | critical infrastructure owners and operators should investigate risks specific … | ADR-0006 | — | — | — |
| `R-0013` | Table 2, row Cybersecurity Risks | ADR-0010 | conventional (**s**) | — | AML.T0012, AML.T0035 |
| `R-0014` | Table 2, row Reliability | R-018, ADR-0006 | non-adversarial (*i*) | — | — |
| `R-0015` | To address the unique challenges of integrating AI into … | DEC-009, ADR-0010 | — | — | — |
| `R-0016` | Similar to hybrid ownership models used with cloud systems, … | ADR-0010, DEC-001b | — | — | — |
| `R-0017` | NCSC-UK and CISA’s joint Guidelines for Secure AI System … | DEC-001b | — | — | — |
| `R-0018` | Secure Design | DEC-001b | — | — | — |
| `R-0019` | Secure Procurement or Development | DEC-009 | supply chain (*i*) | NISTAML.05 | AML.T0010 |
| `R-0020` | Secure Deployment | tmodel#130 | conventional (*i*) | — | AML.T0122 |
| `R-0021` | Secure Operation and Maintenance | DEC-008, DEC-009 | — | — | — |
| `R-0022` | Critical infrastructure owners and operators should also carefully evaluate … | DEC-009 | supply chain (*i*) | NISTAML.05 | AML.T0010 |
| `R-0023` | Procure an AI System | DEC-009 | — | — | — |
| `R-0024` | Develop an AI System | — | — | — | — |
| `R-0025` | Customize an Existing AI System | DEC-009 | — | — | — |
| `R-0026` | Where possible, critical infrastructure owners and operators should demand … | DEC-009 | — | — | — |
| `R-0027` | Critical infrastructure owners and operators should consult CISA’s Secure … | — | — | — | — |
| `R-0028` | Critical infrastructure owners and operators may mitigate these risks … | R-018 | — | — | — |
| `R-0029` | Training OT teams on AI fundamentals and threat modeling … | R-018 | evasion (*i*); non-adversarial (**s**) | NISTAML.022 | AML.T0015 |
| `R-0030` | Developing clear standard operating procedures (SOPs) for all operations … | DEC-001b | — | — | — |
| `R-0031` | Leveraging explainable AI by having operators request that AI … | R-018 | — | — | — |
| `R-0032` | Before incorporating an AI system into their OT environment, … | ADR-0006 | — | — | — |
| `R-0033` | Critical infrastructure owners and operators should further consider whether … | — | — | — | — |
| `R-0034` | While AI comes with unique benefits, it is an … | ADR-0006 | — | — | — |
| `R-0035` | This assessment should incorporate various factors—including security, performance, complexity, … | ADR-0006 | — | — | — |
| `R-0036` | Critical infrastructure owners and operators should understand the organization’s … | ADR-0006, tmodel#130 | — | — | — |
| `R-0037` | If the assessment indicates an AI system is the … | ADR-0006 | — | — | — |
| `R-0038` | When integrating AI into OT environments, critical infrastructure owners … | DEC-009 | — | — | — |
| `R-0039` | Data Assurance | tmodel#130, ADR-0010 | poisoning (*i*); conventional (*i*) | NISTAML.013 | AML.T0020, AML.T0025, AML.T0035 |
| `R-0040` | Data Sovereignty | DEC-009 | — | — | — |
| `R-0041` | Exposure of Sensitive Information | tmodel#130 | privacy (**s**); conventional (**s**) | NISTAML.038 | AML.T0057 |
| `R-0042` | Data Privacy and Security | tmodel#130 | poisoning (**s**); conventional (**s**); non-adversarial (**s**) | NISTAML.013 | AML.T0012, AML.T0020 |
| `R-0043` | Data Silos | ADR-0007 | — | — | — |
| `R-0044` | Data Quality and Availability | — | non-adversarial (**s**) | — | — |
| `R-0045` | Data Quality and Availability | DEC-009 | poisoning (*i*) | NISTAML.013 | AML.T0020, AML.T0059 |
| `R-0046` | Prioritizing OT Data Protection | tmodel#130, ADR-0010 | — | — | — |
| `R-0047` | Engineering Configuration Data | tmodel#130 | conventional (**s**) | — | AML.T0036 |
| `R-0048` | Ephemeral OT Data | tmodel#130 | privacy (**s**) | NISTAML.032, NISTAML.034, NISTAML.038 | AML.T0024.000, AML.T0024.001, AML.T0057 |
| `R-0049` | Critical infrastructure owners and operators should demand transparency and … | DEC-009 | supply chain (*i*) | NISTAML.05 | AML.T0010 |
| `R-0050` | Contractual Agreements | DEC-009 | — | — | — |
| `R-0051` | Software Supply Chain and Software Bill of Materials (SBOM) | ADR-0010, ADR-0007, DEC-008 | supply chain (*i*) | NISTAML.05 | AML.T0010, AML.T0010.003 |
| `R-0052` | Vendor Notifications | DEC-008, DEC-009 | general (**s**) | — | — |
| `R-0053` | Explicit Data Usage Policy Review and Enforcement | tmodel#130 | privacy (*i*) | NISTAML.032, NISTAML.034, NISTAML.038 | AML.T0024.000, AML.T0024.001, AML.T0057 |
| `R-0054` | Increased Connectivity | tmodel#130 | supply chain (*i*) | NISTAML.05 | AML.T0010 |
| `R-0055` | Disabling AI Features | R-018 | — | — | — |
| `R-0056` | When integrating AI into OT environments, critical infrastructure owners … | tmodel#130 | — | — | — |
| `R-0057` | To mitigate these challenges, critical infrastructure owners and operators … | — | — | — | — |
| `R-0058` | Integrate AI systems into their overall security and cybersecurity … | DEC-001b | — | — | — |
| `R-0059` | Add AI security considerations to a comprehensive security strategy … | DEC-001b | conventional (*i*) | — | AML.T0012, AML.T0035 |
| `R-0060` | Critical infrastructure owners and operators should define and validate … | DEC-009, ADR-0010 | — | — | — |
| `R-0061` | Cloud providers should provide detailed documentation that outlines security … | DEC-009 | — | — | — |
| `R-0062` | Consider existing OT infrastructure and assess and develop an … | tmodel#130 | — | — | — |
| `R-0063` | Consider using test infrastructure before deployment to production systems, … | DEC-001b | — | — | — |
| `R-0064` | Encourage push-based architectures where data is pushed out of … | tmodel#130 | conventional (*i*) | — | AML.T0012, AML.T0122 |
| `R-0065` | Prioritize the organization’s control over critical functions that AI … | R-018 | — | — | — |
| `R-0066` | Ensure there are failsafe mechanisms that revert to traditional … | R-018, DEC-009 | non-adversarial (*i*) | — | — |
| `R-0067` | Integrate AI systems the same as any new OT … | tmodel#130, DEC-001b | conventional (*i*) | — | AML.T0122 |
| `R-0068` | Limit active control of OT infrastructure by AI without … | R-018 | — | — | — |
| `R-0069` | Regularly update and validate AI models for accuracy and … | DEC-009 | non-adversarial (*i*) | — | — |
| `R-0070` | Effective governance structures are essential for the safe and … | DEC-001b | — | — | — |
| `R-0071` | An AI governance structure should include the key stakeholders … | DEC-001b, ADR-0010 | — | — | — |
| `R-0072` | Leadership | DEC-001b | — | — | — |
| `R-0073` | OT/IT Subject Matter Experts | R-018 | — | — | — |
| `R-0074` | Cybersecurity Teams | DEC-001b | — | — | — |
| `R-0075` | Other key components of governance structures may include: … | DEC-001b | — | — | — |
| `R-0076` | Enforcing strict data governance policies that protect sensitive OT … | tmodel#130 | conventional (*i*) | — | AML.T0012, AML.T0035 |
| `R-0077` | Establishing clear roles and responsibilities that ensure everyone involved … | ADR-0010, DEC-001b | — | — | — |
| `R-0078` | Implementing regular audits and compliance testing to help identify … | DEC-001b | — | — | — |
| `R-0079` | Continuously validate and verify the performance of AI systems … | DEC-009 | non-adversarial (*i*) | — | — |
| `R-0080` | When integrating AI into OT environments, critical infrastructure owners … | ADR-0006, DEC-001b | — | — | — |
| `R-0081` | This means that traditional cybersecurity requirements, vulnerability management, and … | DEC-008 | — | — | — |
| `R-0082` | Regular Security Audits and Risk Assessments | ADR-0006, DEC-008 | — | — | — |
| `R-0083` | Robust Security Controls | ADR-0010 | conventional (*i*) | — | AML.T0012, AML.T0035 |
| `R-0084` | Collect flow logs and access logs for AI endpoints … | R-018, tmodel#130 | privacy (*i*); conventional (*i*) | NISTAML.031 | AML.T0024, AML.T0025 |
| `R-0085` | Integrate with data loss prevention for prompts and output … | — | privacy (*i*) | NISTAML.036, NISTAML.038 | AML.T0057 |
| `R-0086` | AI-Tailored Security Information | ADR-0010, ADR-0006, ADR-0007 | — | — | — |
| `R-0087` | AI-Tailored Security Information | ADR-0010, ADR-0007, DEC-008 | — | — | — |
| `R-0088` | Thorough testing and evaluation (T&E) are crucial when introducing … | DEC-001b | — | — | — |
| `R-0089` | Operators should initially conduct tests of the AI system … | DEC-001b | — | — | — |
| `R-0090` | Low fidelity testing can allow for faster iterations of … | — | — | — | — |
| `R-0091` | Alternatively, work with vendors to understand their testing and … | DEC-009 | — | — | — |
| `R-0092` | As the system matures, operators can test with more … | — | — | — | — |
| `R-0093` | Operators should only move the AI system into production … | DEC-001b | — | — | — |
| `R-0094` | Virtualized controllers can speed up this testing process when … | — | — | — | — |
| `R-0095` | Critical infrastructure owners and operators should also comply with … | tmodel#130 | conventional (*i*) | — | AML.T0035 |
| `R-0096` | Critical infrastructure owners and operators should evaluate the applicability … | DEC-001b | — | — | — |
| `R-0097` | Critical infrastructure owners and operators should continuously validate and … | DEC-009 | non-adversarial (*i*) | — | — |
| `R-0098` | Critical infrastructure owners and operators should also identify and … | ADR-0006, R-018 | general (**s**) | — | — |
| `R-0099` | Ultimately, humans are responsible for functional safety. Humans make … | R-018 | — | — | — |
| `R-0100` | Critical infrastructure owners and operators should implement oversight of … | tmodel#130, ADR-0010, ADR-0007 | — | — | — |
| `R-0101` | Log and monitor inputs and outputs for these components. … | R-018 | privacy (*i*); direct prompt injection (*i*); indirect prompt injection (*i*) | NISTAML.015, NISTAML.018, NISTAML.031 | AML.T0024.002, AML.T0051.000, AML.T0051.001 |
| `R-0102` | Also, establish and maintain a known good state or … | DEC-009 | poisoning (*i*) | NISTAML.013, NISTAML.026 | AML.T0018.000, AML.T0020 |
| `R-0103` | Consider the following points when embedding safety processes into … | — | — | — | — |
| `R-0104` | Human-in-the-Loop Decision-Making | R-018, DEC-001b | — | — | — |
| `R-0105` | Human-in-the-Loop Decision-Making | R-018 | — | — | — |
| `R-0106` | Human-in-the-Loop Decision-Making | R-018 | evasion (*i*); non-adversarial (*i*) | NISTAML.022 | AML.T0015 |
| `R-0107` | Understand the correctness of AI system results to support … | ADR-0006, R-018 | non-adversarial (**s**) | — | — |
| `R-0108` | Implement anomaly detection and behavioral analytics. Establish safe operating … | DEC-009 | poisoning (*i*); non-adversarial (**s**) | NISTAML.026 | AML.T0018 |
| `R-0109` | Configure logging so AI decisions can be tracked for … | R-018, ADR-0010 | indirect prompt injection (*i*) | NISTAML.015 | AML.T0053 |
| `R-0110` | The example below demonstrates how operators and engineers should … | — | — | — | — |
| `R-0111` | AI System Output | — | — | — | — |
| `R-0112` | Anomaly Detection Algorithm | DEC-009 | non-adversarial (*i*) | — | — |
| `R-0113` | Monitoring Tools | R-018 | non-adversarial (*i*) | — | — |
| `R-0114` | Audit Trail | R-018, DEC-001b | privacy (*i*); direct prompt injection (*i*); indirect prompt injection (*i*) | NISTAML.015, NISTAML.018, NISTAML.031 | AML.T0024.002, AML.T0051.000, AML.T0051.001 |
| `R-0115` | Offensive Security Assessments/AI Red Teaming | DEC-008, R-018 | general (*i*) | — | — |
| `R-0116` | Network and Egress Security | tmodel#130 | conventional (*i*) | — | AML.T0025 |
| `R-0117` | Establish key performance indicators (KPIs) that measure AI effectiveness … | ADR-0006 | — | — | — |
| `R-0118` | Critical infrastructure owners and operators should schedule regular review … | R-018, DEC-001b | — | — | — |
| `R-0119` | Continuously validate and refine AI models in simulated environments … | DEC-001b | — | — | — |
| `R-0120` | Regularly update threat models with AI-specific attack vectors (such … | ADR-0010, DEC-001b, ADR-0006 | evasion (**s**); poisoning (**s**); direct prompt injection (*i*) | NISTAML.013, NISTAML.018, NISTAML.022 | AML.T0015, AML.T0020, AML.T0043, AML.T0051.000, AML.T0054 |
| `R-0121` | Continuously update and refine AI models with new OT … | DEC-009 | non-adversarial (**s**) | — | — |
| `R-0122` | Explore new AI explainability and transparency tools. … | R-018 | — | — | — |
| `R-0123` | Critical infrastructure owners and operators should, where possible, explore … | R-018 | — | — | — |
| `R-0124` | Such transparency is critical for safety and regulatory compliance … | R-018 | — | — | — |
| `R-0125` | Prefer push-based or brokered architectures that move required features … | tmodel#130 | conventional (*i*) | — | AML.T0012, AML.T0122 |
| `R-0126` | Where data must traverse to business networks, use one-way … | tmodel#130, R-018 | conventional (*i*) | — | AML.T0012, AML.T0122 |
| `R-0127` | Establish failsafe mechanisms that enable AI systems to fail … | DEC-009, R-018 | non-adversarial (*i*) | — | — |
| `R-0128` | Incorporate new AI system failure states, including how to … | DEC-009 | — | — | — |
| `R-0129` | Therefore, operators responsible for revising the existing functional safety … | DEC-009 | — | — | — |
| `R-0130` | Design functional safety procedures that account for the AI … | — | — | — | — |
| `R-0131` | Per Principle 2 – Consider AI Use in the … | — | — | — | — |
| `R-0132` | Incorporate AI considerations into the cybersecurity incident response plan. … | DEC-009 | — | — | — |
| `R-0133` | To account for this, critical infrastructure owners and operators … | DEC-009 | non-adversarial (**s**); general (**s**) | — | — |
| `R-0134` | While AI can enhance efficiency, productivity, and decision-making, it … | — | — | — | — |
| `R-0135` | For successful mitigation of the risks of integrating AI … | — | — | — | — |
| `R-0136` | However, as definitions of AI and OT may vary … | — | — | — | — |

## ATLAS techniques used (all verified in ATLAS 2026.09)

| ATLAS id | name (2026.09) | used by |
|---|---|---|
| AML.T0010 | AI Supply Chain Compromise | 5 entries |
| AML.T0010.001 | AI Software | 1 entries |
| AML.T0010.003 | Model | 1 entries |
| AML.T0012 | Valid Accounts | 8 entries |
| AML.T0015 | Evade AI Model | 4 entries |
| AML.T0018 | Manipulate AI Model | 2 entries |
| AML.T0018.000 | Poison AI Model | 1 entries |
| AML.T0020 | Training Data Poisoning | 6 entries |
| AML.T0024 | Exfiltration via AI Inference API | 1 entries |
| AML.T0024.000 | Infer Training Data Membership | 2 entries |
| AML.T0024.001 | Invert AI Model | 2 entries |
| AML.T0024.002 | Extract AI Model | 2 entries |
| AML.T0025 | Exfiltration via Cyber Means | 3 entries |
| AML.T0035 | AI Artifact Collection | 6 entries |
| AML.T0036 | Data from Information Repositories | 1 entries |
| AML.T0041 | Physical Environment Access | 1 entries |
| AML.T0043 | Craft Adversarial Data | 2 entries |
| AML.T0051.000 | Direct | 4 entries |
| AML.T0051.001 | Indirect | 3 entries |
| AML.T0053 | AI Agent Tool Invocation | 1 entries |
| AML.T0054 | LLM Jailbreak | 2 entries |
| AML.T0057 | LLM Data Leakage | 4 entries |
| AML.T0059 | Erode Dataset Integrity | 1 entries |
| AML.T0122 | Exploitation of Remote Services | 5 entries |
