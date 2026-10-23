---
record: etsi-en-304-223
kind: design-notes
title: "etsi-en-304-223 — bearing on our design"
extracted: "2026-10-21"
reviewed_by: ""
---

# ETSI EN 304 223 — bearing on tmodel

**What this is.** For every provision: (a) which tmodel decisions it bears on, as they stand on
tmodel `main` at `e1ae8c3` (2026-10-21), and (b) which AI attack class it defends against, in the
terms of NIST AI 100-2 E2025 (its index ids, `NISTAML.*`) and, where one fits, a MITRE ATLAS
technique id. Evidence for RPT-0009, not a decision: nothing here accepts a `DEC-*`.

**How to read the threat mapping.**

- **stated** — the provision's own words name the attack (the words are kept as `source_text`
  in `requirements.yaml`). The NIST class and the ATLAS id are still our translation of those
  words: the EN prints neither.
- **inferred** — the provision names no attack; the link is our reading, with a one-line
  rationale in `requirements.yaml`.
- Three labels of ours sit outside the NIST attack taxonomy: **non-adversarial** (drift, failure,
  unexpected inputs), **conventional** (an attack on AI assets by ordinary cyber means, which NIST
  AI 100-2 leaves out of scope; ATLAS still has ids for some), and **unclear** (named but undefined).
- **ATLAS ids.** Every id was checked against ATLAS release 2026.09 (2026-09-15), the data file
  that atlas.mitre.org itself loads (`/atlas-data/dist/v6/ATLAS-2026.09.yaml`, sha256
  `935efa93…6688`). The technique pages are a JavaScript app and return HTTP 404 to a plain
  fetch, so the ids were verified against that file, not a rendered page.
- **NIST ids** are from the E2025 "Predictive AI and Generative AI Taxonomy Index" (pp. x–xi,
  `https://doi.org/10.6028/NIST.AI.100-2e2025`; PDF sha256 `4811fb6a…7646`). The EN itself cites
  the older E2023 edition ([i.17]).

**Two directions.** The EN bears on tmodel twice. (1) As **content**: a tmodel user threat-modelling
an AI system needs these parties, assets, threats and controls to be expressible. (2) As
**requirements on tmodel itself**: tmodel proposes threats with AI (ARCH-0001 §2), so tmodel is an
"AI system" and the project is its Developer and System Operator. Where a note is about (2) it
says so.

## Summary

73 entries; 33 carry a threat mapping, 27 of them to a NIST AI 100-2 attack class. An entry is counted once per class (as stated if any of its mappings to that class is stated).

| attack class | entries | stated | inferred | NIST AI 100-2 E2025 ids | ATLAS ids |
|---|---|---|---|---|---|
| Evasion | 1 | 1 | 0 | NISTAML.022 Evasion | AML.T0015, AML.T0043 |
| Poisoning | 10 | 5 | 5 | NISTAML.013 Data Poisoning, NISTAML.026 Model Poisoning | AML.T0010.002, AML.T0018.000, AML.T0020, AML.T0031 |
| Privacy | 6 | 3 | 3 | NISTAML.031 Model Extraction, NISTAML.032 Reconstruction, NISTAML.033 Membership Inference, NISTAML.038 Data Extraction | AML.T0024.000, AML.T0024.001, AML.T0024.002, AML.T0035, AML.T0040, AML.T0057 |
| Misuse | 1 | 0 | 1 | NISTAML.04 Misuse Violations | — |
| Direct prompt injection | 2 | 0 | 2 | NISTAML.018 Prompt Injection | AML.T0051.000 |
| Indirect prompt injection | 3 | 0 | 3 | NISTAML.015 Indirect Prompt Injection, NISTAML.039 Compromising connected resources | AML.T0051.001, AML.T0053, AML.T0129 |
| Supply chain | 8 | 0 | 8 | NISTAML.023 Backdoor Poisoning, NISTAML.05 Supply Chain Attacks, NISTAML.051 Model Poisoning | AML.T0010, AML.T0010.001, AML.T0010.002, AML.T0010.003, AML.T0011.000, AML.T0018, AML.T0018.000 |
| Conventional (outside NIST AI 100-2: access, theft, tampering, network paths) | 6 | 0 | 6 | — | AML.T0012, AML.T0018.003, AML.T0025, AML.T0035, AML.T0048.004, AML.T0081, AML.T0083 |
| Non-adversarial (not an attack) | 2 | 2 | 0 | — | — |

The pattern: the EN names few attacks (data poisoning, model inversion, membership inference and
reverse engineering in provisions; adversarial attacks via the clause 3.1 definition; indirect
prompt injection and model obfuscation only in the Introduction). Most provisions are
governance and lifecycle controls that defend against no single class. That is why so many rows
in the table at the end have no threat mapping: it is a finding, not a gap in the work.

## By decision

### ADR-0010 — core classes (accepted)

**Adopt.**
- **Parties.** Table 4-1's five stakeholder groups (Developer, System Operator, Data Custodian,
  End-user, Affected entity) are roles, not kinds of party: one entity can hold several (§4). They
  fit `Party` plus a role on the relation, not new `PartyKind` values (`organization`, `person`).
- **AttackPattern.** ATLAS techniques are generic attack patterns, the same layer as CAPEC and
  ATT&CK. `AttackPattern.catalog_ref` ("CWE, CAPEC, ATT&CK, CVE, D3FEND"; scheme "not pinned")
  can carry an ATLAS id unchanged. 5.1.3-1 asks threat models to address named AI attacks, so a
  model built to the EN needs ATLAS (or NIST) ids on AttackPattern.
- **Mitigation.** Each provision is a candidate `Mitigation`; `applies_in_phase` takes the EN's
  phase. Phase mapping to `LifecyclePhaseCode`: secure design → `design`; secure development →
  `implementation`, `verification_validation`; secure deployment → `deployment`; secure
  maintenance → `operation`, `maintenance`; secure end of life → `decommission`.
- **Identifiers.** 5.2.4-1.2 (release cryptographic hashes of model components) fits the opaque
  `identifiers` slot as a component digest, alongside purl/SBOM ids.

**Gap.** 5.1.3-1.2 names a weakness the core can hold only loosely: *superfluous functionality*
(a multimodal model used for one modality). `Weakness` is "catalogued as CWE"; CWE 4.20 has no
entry for it.

### tmodel#130 — Asset, TrustBoundary, DataFlow (proposed, not accepted)

Principle 5 is titled *Identify, track and protect the assets* and 5.2.1-1 requires an inventory
of assets "including their interdependencies/connectivity". The accepted core has no `Asset`, so
a model built to the EN cannot say what an AI attack damages. tmodel#130 proposes what is
missing, and these provisions are evidence for it:

| provision | needs | tmodel#130 element |
|---|---|---|
| 5.2.1-1, 5.2.1-2 | asset inventory with dependencies and connectivity; version control | `Asset`; `Component` with `component_kind: machine_learning_model`, `data`; `DataFlow` |
| 5.2.1-4, 5.2.1-4.2 | sensitive training/test data, confidential weights | `Asset.security_properties` (confidentiality) |
| 5.1.2-6, 5.2.2-1, 5.2.2-3 | permissions on other systems; access control on APIs, models, data, pipelines; separated environments | `TrustBoundary` zones, `DataFlow.crosses_boundary` |
| 5.5.1-1, 5.5.1-2 | disposal of data and models on transfer or decommissioning | `Asset` lifecycle (no proposed slot) |

Open choice the EN does not settle: is a training dataset or a set of model weights an `Asset`,
a `Component` (`component_kind: data` / `machine_learning_model`), or both? The EN treats them as
assets (Principle 5) that are also parts of the system (5.1.2-3 "models, datasets and prompts
incorporated into the system").

### ADR-0006 — risk composite vector (accepted)

**Adopt.** The EN requires risk assessment (5.1.2-1, 5.1.2-4, 5.1.3-1, 5.2.3-2.1) but prescribes
no method or metric, so it does not conflict with the composite vector.

**Adapt.** AI attacks need feasibility inputs ISO/SAE 21434 Table 1 does not name, and the EN
gives one: 5.2.2-2 requires controls against attacks via an API and gives model-access rate
limits as its example against reverse engineering and rapid poisoning. That control lowers
**feasibility** (model extraction needs many queries), not impact. The
NIST E2025 attacker-knowledge levels (white-, grey-, black-box, §2.1.4) read naturally as the
21434 "knowledge of the item" factor. Both are inferred; feasibility stays human-rated at MVP.

**Consistent.** 5.1.3-4 says risk "will remain in AI systems despite the application of
controls". ADR-0006 forbids mitigation-status from silently lowering derived risk; the EN says
the same thing from the other side.

**Gap.** 5.1.3-1.3 (controls "in line with their corporate risk tolerance") and 5.1.3-4 ("risk
appetite") assume a risk-acceptance threshold. ADR-0006 has `accepted_risk` as a status but no
threshold; that belongs to the governed layer (DEC-001b).

### ADR-0007 — LinkML; OTM and STIX import (accepted)

The EN defines no data format, so there is nothing to import from it. Three findings for the
import mappings:

- **OTM has no slot for ATLAS ids.** In the OTM schema (`otm_schema.json` at `c88c5a7`, cached
  for RPT-0005), a threat has `attributes, categories, cwes, description, id, name, risk, tags`.
  `cwes` takes CWE ids; an ATLAS technique id would have to ride in `categories`, `tags` or
  `attributes`. The OTM MAP-NNNN has to pick one, or AI threats imported from OTM lose their
  technique id.
- **OTM `assets`, `trustZones`, `dataflows` land nowhere** in the accepted core. The EN's
  Principle 5 makes assets central for AI systems, which adds weight to tmodel#130.
- **STIX 2.1** carries technique ids as `external_references` on `attack-pattern` objects (the
  mechanism ATT&CK uses). Whether MITRE publishes ATLAS as a STIX bundle was **not checked**.

The EN's only field-level content is the documentation list in 5.2.4-1.1 and 5.2.4-2.1 (training
data sources incl. URL and date/time obtained, scope and limitations, guardrails, retention time,
review frequency, failure modes). If tmodel models AI components, that list is a candidate
LinkML extension (inferred).

### DEC-001b — governed layer (open)

- **Requirement.** Each provision is a candidate `Requirement`. This `requirements.yaml` already
  validates against the library's LinkML requirements schema, so a DEC-001b `Requirement` can
  reference `etsi-en-304-223#5.1.3-1` by id rather than copy the text.
- **Gates and checkpoints.** The EN gives triggers, not states: re-run threat modelling when a
  setting or configuration option changes (5.1.3-1.1); test before release (5.2.5-1) and before
  deployment (5.2.5-2); treat a major update as a new version and re-test (5.4.1-2); review the
  threat model regularly (5.1.3-1). These are inputs to `Gate`/`Checkpoint`, and the reason no
  state machine was extracted (record.yaml `not_applicable`).
- **C1 (automatable conformance).** EN conformance is assessed under ETSI TS 104 216, which is
  still a draft work item. C1 cannot be closed from this source.
- **M5 (author/origin of AI-authored artifacts).** 5.1.2-3 requires an audit trail of prompts
  (shall), and 5.2.4-3 recommends an audit log of changes to system prompts (should). Applied to tmodel itself (direction 2), the prompts
  and configuration that produced an AI-proposed threat are provenance; tmodel#130's proposed
  `Assertion.generated_by` and `evidence` are where they would go.

### DEC-008 — CWE/NVD integration (open)

- AI **vulnerabilities** in products still arrive as CVEs (5.1.1-2 awareness, 5.2.2-4 disclosure
  policy, 5.4.1-1 patches, 5.2.3-1 supply chain). AI **attack techniques** do not: they are in
  ATLAS. AI **weaknesses** are partly in CWE: CWE 4.20 (2026-04-30) has CWE-1426 *Improper
  Validation of Generative AI Output*, CWE-1427 *Improper Neutralization of Input Used for LLM
  Prompting* and CWE-1434 *Insecure Setting of Generative AI/ML Model Inference Parameters*.
- If DEC-008 settles on a cached mirror (the register says it leans that way), ATLAS can be
  mirrored the same way: atlas.mitre.org serves a release manifest
  (`/atlas-data/dist/manifest.yaml`) with dated, versioned YAML releases (2026.09 is the latest,
  2026-09-15). Pinning a release keeps every ATLAS id in the library resolvable.

### DEC-009 — generic threat → product; mitigation lifecycle (open)

- **Generic → specific.** 5.1.3-2: threats a Developer cannot resolve go to System Operators
  "so they can threat model their systems", and on to End-users. That is the EN's own path from a
  generic threat to a deployment, and it runs along the supply chain, as vulnerability
  propagation along composition does in the accepted core.
- **Mitigation lifecycle events** the EN names: re-run evaluations on released models before use
  (5.2.3-3); tell End-users before a model update (5.2.3-4); provide patches (5.4.1-1); keep
  contingency plans where updates cannot be provided (5.4.1-1.1, an `accepted_risk` case); a
  major update is a new version (5.4.1-2); monitor for drift and poisoning (5.4.2-2, 5.4.2-4);
  dispose on transfer or decommissioning (5.5.1-1, 5.5.1-2).

### R-018 — human review (draft requirement)

- **Content (1).** 5.1.4-1 to 5.1.4-3 make human oversight a control in the user's AI system
  (5.1.4-4 and 5.1.4-5, also in Principle 4, are about Data Custodian controls and prohibited
  uses). Oversight maps to `Mitigation`, with oversight as the kind of control.
- **tmodel itself (2).** 5.1.4-3: "Where human oversight is a risk control, Developers and/or
  System Operators shall design, develop, verify and maintain technical measures to reduce the
  risk through such oversight." R-018 is exactly that for tmodel: human review is the control on
  AI-proposed threats. Under the EN, tmodel would have to **verify** it, i.e. test that nothing
  machine-proposed shows as final without a `Review`. 5.1.4-2 (outputs humans can assess) asks
  that a proposed threat carry why it was proposed: evidence and source.
- 5.4.2-1 (log system and user actions) gives the audit side of the same requirement.

## Weaknesses, threats and vulnerabilities (the sponsor's framing)

- **Threats.** `threats.yaml` lists the 14 threats the EN describes, each quoted with its
  locator and mapped to NIST and ATLAS ids, with the provisions that address it.
- **Weaknesses.** The EN describes three directly (superfluous functionality, 5.1.3-1.2; models
  or components that are not well documented or secured, 5.2.3-2; risk that remains after
  controls, 5.1.3-4) and implies more; `threats.yaml` lists four. CWE-1427 is the weakness behind prompt injection, which 5.2.1-4.1 (sanitise inputs)
  addresses; CWE-1426 is the weakness 5.2.5-4 and 5.2.5-4.1 (evaluate model outputs) address.
  Both links are inferred.
- **Vulnerabilities.** None: the EN names no product or CVE.

## Open questions for the sponsor

1. **"Model obfuscation"** (Introduction) is named as an AI security risk and never defined. It
   matches no class in NIST AI 100-2 E2025 or ATLAS 2026.09, so it has no id here. Should
   RPT-0009 read it as obfuscated malicious models (e.g. ATLAS AML.T0018.002 *Embed Malware*), as
   prompt obfuscation (AML.T0068), or leave it open?
2. **Where AI artifacts live** in the object model: training data, weights and system prompts as
   `Asset`, as `Component` (`component_kind: data`, `machine_learning_model`), or both
   (tmodel#130)?
3. **ATLAS mitigations.** The EN cites ATLAS *Mitigations* ([i.12]). A provision → ATLAS
   mitigation (`AML.M*`) map would feed `Mitigation.catalog_ref` directly. Not done here; worth a
   follow-up?
4. **Source defects to note** (kept as printed): Table 4-1 defines Affected entities as those
   "that are not directly affected by AI systems", which reads as a drafting slip for "not
   directly using"; and the End-users row refers to "the voluntary Code", a code the EN does not
   cite (its origin is not stated in the EN). Also: 5.2.1-4 says "see clause 5.2.3 for details on
   securing data", but 5.2.3 (supply chain) has no provision on securing data; 5.2.1-4.1 says "See
   clause 5.2.2 for relevant provisions for open source", but 5.2.2 never mentions open source;
   clause 4 says an indication of the primarily responsible stakeholders "is given for each
   principle", but Principle 10 (5.3.1) has none; and the Introduction says standards are
   "signposted at the start of each principle", but Principles 10 and 13 have no References line.
5. **Predecessor.** ETSI TS 104 223 V1.1.1 (April 2025, History) is not a record, so there is no
   `supersedes` link. CISA's AI-in-OT guidance cites the TS, not the EN.

## Mapping, provision by provision

Decisions: the tmodel decisions the provision bears on (`bears_on` in `requirements.yaml`).
Threat: attack class, **s** = stated, *i* = inferred. A dash means the provision is a governance or
lifecycle control with no single attack class.

| id | provision | decisions | threat | NIST | ATLAS |
|---|---|---|---|---|---|
| `C4-1` | Note possible data protection obligations | ADR-0010 | — | — | — |
| `5.1.1-1` | Include AI security content in cyber security training | DEC-001b | — | — | — |
| `5.1.1-1.1` | Tailor AI security training to staff roles | DEC-001b | — | — | — |
| `5.1.1-2` | Keep all staff aware of AI-related threats and mitigations | DEC-008 | — | — | — |
| `5.1.1-2.1` | Share AI threat updates through multiple channels | — | — | — | — |
| `5.1.1-2.2` | Train developers in secure AI coding and design | — | — | — | — |
| `5.1.2-1` | Assess business need, AI security risks and mitigations before building | ADR-0006, DEC-001b | — | — | — |
| `5.1.2-1.1` | Include the Data Custodian in requirements discussions | ADR-0010 | — | — | — |
| `5.1.2-2` | Design AI systems to withstand adversarial attacks and failures | ADR-0010 | evasion (**s**); non-adversarial (**s**) | NISTAML.022 | AML.T0015, AML.T0043 |
| `5.1.2-3` | Keep an audit trail of models, datasets and prompts | R-018, DEC-001b, ADR-0010 | poisoning (*i*) | NISTAML.013 | AML.T0020 |
| `5.1.2-4` | Risk-assess external components for AI-specific risks | ADR-0006, DEC-009 | supply chain (*i*) | NISTAML.05 | AML.T0010, AML.T0010.001, AML.T0010.003 |
| `5.1.2-5` | Match intended use to the sensitivity of training data | tmodel#130 | privacy (*i*) | NISTAML.032, NISTAML.033, NISTAML.038 | AML.T0024.000, AML.T0024.001, AML.T0057 |
| `5.1.2-5.1` | Encourage staff to report AI security risks | — | — | — | — |
| `5.1.2-6` | Give the AI system only the permissions it needs on other systems | tmodel#130, ADR-0010 | indirect prompt injection (*i*) | NISTAML.015, NISTAML.039 | AML.T0051.001, AML.T0053 |
| `5.1.2-7` | Do due diligence on external providers | DEC-009 | supply chain (*i*) | NISTAML.05 | AML.T0010 |
| `5.1.3-1` | Threat-model and manage risks, including AI-specific attacks | ADR-0010, ADR-0006, DEC-001b | poisoning (**s**); privacy (**s**) | NISTAML.013, NISTAML.032, NISTAML.033 | AML.T0020, AML.T0024.000, AML.T0024.001 |
| `5.1.3-1.1` | Re-run threat modelling when settings or configuration change | DEC-001b | — | — | — |
| `5.1.3-1.2` | Manage risks of superfluous model functionality | ADR-0010, ADR-0006 | indirect prompt injection (*i*) | NISTAML.015 | AML.T0129 |
| `5.1.3-1.3` | Apply controls in line with corporate risk tolerance | ADR-0006 | — | — | — |
| `5.1.3-2` | Pass unresolved AI threats on to System Operators and End-users | DEC-009, ADR-0007 | — | — | — |
| `5.1.3-3` | Get assurance from external parties responsible for AI risks | ADR-0006, DEC-009 | — | — | — |
| `5.1.3-4` | Continuously monitor and review infrastructure against risk appetite | ADR-0006, DEC-009 | — | — | — |
| `5.1.4-1` | Build in capabilities for human oversight | R-018 | — | — | — |
| `5.1.4-2` | Make outputs easy for humans to assess | R-018 | — | — | — |
| `5.1.4-3` | Build technical measures where human oversight is a risk control | R-018, ADR-0006 | — | — | — |
| `5.1.4-4` | Verify Data Custodian security controls are built in | R-018 | — | — | — |
| `5.1.4-5` | Tell End-users about prohibited use cases | — | misuse (*i*) | NISTAML.04 | — |
| `5.2.1-1` | Maintain an inventory of assets and their interdependencies | tmodel#130, ADR-0010, ADR-0007 | — | — | — |
| `5.2.1-2` | Track, authenticate, version-control and secure AI assets | tmodel#130, ADR-0010 | supply chain (*i*) | NISTAML.051 | AML.T0010.003, AML.T0018 |
| `5.2.1-3` | Tailor disaster recovery plans to attacks on AI systems | DEC-009 | — | — | — |
| `5.2.1-3.1` | Be able to restore a known good state | DEC-009 | poisoning (*i*) | NISTAML.013, NISTAML.026 | AML.T0018.000, AML.T0020 |
| `5.2.1-4` | Protect sensitive data such as training and test data | tmodel#130 | conventional (*i*) | — | AML.T0025, AML.T0035 |
| `5.2.1-4.1` | Check and sanitise data and inputs, and repeat on model revisions | — | poisoning (*i*); direct prompt injection (*i*); indirect prompt injection (*i*) | NISTAML.013, NISTAML.015, NISTAML.018 | AML.T0020, AML.T0051.000, AML.T0051.001 |
| `5.2.1-4.2` | Protect confidential training data and model weights | tmodel#130 | conventional (*i*) | — | AML.T0035, AML.T0048.004 |
| `5.2.2-1` | Secure access to APIs, models, data and pipelines | tmodel#130 | conventional (*i*) | — | AML.T0012, AML.T0035 |
| `5.2.2-2` | Protect externally offered APIs, e.g. with rate limits | ADR-0006 | poisoning (**s**); privacy (**s**) | NISTAML.013, NISTAML.031 | AML.T0020, AML.T0024.002, AML.T0040 |
| `5.2.2-3` | Use separate, least-privilege development and tuning environments | tmodel#130 | conventional (*i*) | — | AML.T0035 |
| `5.2.2-4` | Publish a vulnerability disclosure policy | DEC-008 | — | — | — |
| `5.2.2-5` | Maintain an AI incident management plan and recovery plan | DEC-009 | — | — | — |
| `5.2.2-6` | Make cloud contracts support these requirements | — | — | — | — |
| `5.2.3-1` | Follow secure software supply chain processes | DEC-008, ADR-0007 | supply chain (*i*) | NISTAML.05 | AML.T0010, AML.T0010.001, AML.T0010.002, AML.T0010.003 |
| `5.2.3-2` | Justify using poorly documented or unsecured models or components | DEC-008, DEC-009 | supply chain (*i*) | NISTAML.05 | AML.T0010.003, AML.T0011.000 |
| `5.2.3-2.1` | Mitigate and risk-assess such models or components | ADR-0006 | supply chain (*i*) | NISTAML.05 | AML.T0010.003, AML.T0011.000 |
| `5.2.3-2.2` | Share that justification with End-users | — | — | — | — |
| `5.2.3-3` | Re-run evaluations on released models before using them | DEC-009 | supply chain (*i*) | NISTAML.023, NISTAML.051 | AML.T0010.003, AML.T0018.000 |
| `5.2.3-4` | Tell End-users before models are updated | DEC-009 | — | — | — |
| `5.2.4-1` | Document an audit trail of design and maintenance plans | DEC-001b, R-018 | — | — | — |
| `5.2.4-1.1` | Include security-relevant information in the documentation | ADR-0007 | poisoning (*i*) | NISTAML.013 | AML.T0020 |
| `5.2.4-1.2` | Release cryptographic hashes of shared model components | ADR-0010, ADR-0007 | supply chain (*i*) | NISTAML.051 | AML.T0010.003, AML.T0018 |
| `5.2.4-2` | Document the source and use of public training data | ADR-0007, DEC-009 | poisoning (**s**) | NISTAML.013 | AML.T0010.002, AML.T0020 |
| `5.2.4-2.1` | Record the source URL and date of training data | ADR-0007 | poisoning (**s**) | NISTAML.013 | AML.T0010.002, AML.T0020 |
| `5.2.4-3` | Keep an audit log of system prompt and configuration changes | R-018, DEC-001b | conventional (*i*) | — | AML.T0018.003, AML.T0081 |
| `5.2.5-1` | Security-test all released models, applications and systems | DEC-001b | — | — | — |
| `5.2.5-2` | Test before deployment, with Developer support | DEC-001b | — | — | — |
| `5.2.5-2.1` | Use independent security testers | R-018 | — | — | — |
| `5.2.5-3` | Share test findings with System Operators | DEC-009 | — | — | — |
| `5.2.5-4` | Check outputs do not allow reverse engineering of the model or data | — | privacy (**s**) | NISTAML.031, NISTAML.032, NISTAML.038 | AML.T0024.001, AML.T0024.002, AML.T0057 |
| `5.2.5-4.1` | Check outputs do not give unintended influence over the system | — | direct prompt injection (*i*) | NISTAML.018 | AML.T0051.000 |
| `5.3.1-1` | Tell End-users how their data is used, accessed and stored | — | — | — | — |
| `5.3.1-2` | Give End-users guidance on use and configuration | — | — | — | — |
| `5.3.1-2.1` | Cover appropriate use, limitations and failure modes in guidance | — | — | — | — |
| `5.3.1-2.2` | Proactively inform End-users of security-relevant updates | DEC-009 | — | — | — |
| `5.3.1-3` | Support End-users and Affected Entities during incidents | DEC-009 | — | — | — |
| `5.4.1-1` | Provide security updates and deliver them to End-users | DEC-009, DEC-008 | — | — | — |
| `5.4.1-1.1` | Have contingency plans where updates cannot be provided | DEC-009, ADR-0006 | — | — | — |
| `5.4.1-2` | Treat major updates as a new model and re-test | DEC-001b, DEC-009 | — | — | — |
| `5.4.1-3` | Help System Operators evaluate model changes | DEC-009 | — | — | — |
| `5.4.2-1` | Log system and user actions | R-018 | privacy (*i*) | NISTAML.031 | AML.T0024.002 |
| `5.4.2-2` | Analyse logs for anomalies, drift and poisoning | DEC-009 | poisoning (**s**); non-adversarial (**s**) | NISTAML.013 | AML.T0020 |
| `5.4.2-3` | Monitor internal states of the AI system | — | — | — | — |
| `5.4.2-4` | Monitor model performance over time | DEC-009 | poisoning (*i*) | NISTAML.013 | AML.T0031 |
| `5.5.1-1` | Involve Data Custodians and dispose securely when transferring ownership | tmodel#130, DEC-009 | privacy (*i*) | NISTAML.038 | AML.T0035 |
| `5.5.1-2` | Involve Data Custodians and delete data when decommissioning | tmodel#130, DEC-009 | conventional (*i*) | — | AML.T0035, AML.T0083 |

## ATLAS techniques used (all verified in ATLAS 2026.09)

| ATLAS id | name (2026.09) | used by |
|---|---|---|
| AML.T0010 | AI Supply Chain Compromise | 3 entries |
| AML.T0010.001 | AI Software | 2 entries |
| AML.T0010.002 | Data | 3 entries |
| AML.T0010.003 | Model | 7 entries |
| AML.T0011.000 | Unsafe AI Artifacts | 2 entries |
| AML.T0012 | Valid Accounts | 1 entries |
| AML.T0015 | Evade AI Model | 1 entries |
| AML.T0018 | Manipulate AI Model | 2 entries |
| AML.T0018.000 | Poison AI Model | 2 entries |
| AML.T0018.003 | Modify Prompt Construction Logic | 1 entries |
| AML.T0020 | Training Data Poisoning | 9 entries |
| AML.T0024.000 | Infer Training Data Membership | 2 entries |
| AML.T0024.001 | Invert AI Model | 3 entries |
| AML.T0024.002 | Extract AI Model | 3 entries |
| AML.T0025 | Exfiltration via Cyber Means | 1 entries |
| AML.T0031 | Erode AI Model Integrity | 1 entries |
| AML.T0035 | AI Artifact Collection | 6 entries |
| AML.T0040 | AI Model Inference API Access | 1 entries |
| AML.T0043 | Craft Adversarial Data | 1 entries |
| AML.T0048.004 | AI Intellectual Property Theft | 1 entries |
| AML.T0051.000 | Direct | 2 entries |
| AML.T0051.001 | Indirect | 2 entries |
| AML.T0053 | AI Agent Tool Invocation | 1 entries |
| AML.T0057 | LLM Data Leakage | 2 entries |
| AML.T0081 | Modify AI Agent Configuration | 1 entries |
| AML.T0083 | Credentials from AI Agent Configuration | 1 entries |
| AML.T0129 | Triggers in Multimodal Inputs | 1 entries |
