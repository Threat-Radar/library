---
schema: "library-summary/v1"
id: mitre-attack-flow
record: mitre-attack-flow
type: summary
updated: "2026-10-22"
---

# Attack Flow — Language

|  |  |
|---|---|
| **Type** | spec (a STIX 2.1 extension, plus open-source tools) |
| **Maturity** | `best-practice` — maintained open project with a published schema; not a standards-body specification |
| **Authors** | MITRE Center for Threat-Informed Defense |
| **Published** | Language 2.0.0, extension definition created 2022-08-02; the text read is the docs at release v4.1.0 (2026-10-14) |
| **Identifier** | https://center-for-threat-informed-defense.github.io/attack-flow/language/ |
| **Source** | https://raw.githubusercontent.com/center-for-threat-informed-defense/attack-flow/v4.1.0/docs/language.rst |
| **Digest** | `85ae7b7f367b57c935328276a412e5b2f051e4d48f2ab622276359d49615fa49` (the language page at tag v4.1.0, retrieved 2026-10-22) |

## Overview

Attack Flow is a machine-readable language for **sequences of adversary
behaviour**, defined as an extension to **STIX 2.1** so that flows interoperate
with existing threat-intelligence tools. A flow document has exactly one
**`attack-flow`** object (name, description, `start_refs`, and a `scope`:
`incident`, `campaign`, `threat-actor`, `malware`, `emulation-plan`,
`attack-tree` or `other`). Its building blocks are:

- **`attack-action`**: one execution of a technique (`technique_id`,
  `tactic_id`, optional refs to the ATT&CK objects, a command, the assets it
  touches), linked to what follows through **`effect_refs`**;
- **`attack-condition`**: a state or outcome after an action, with optional
  STIX pattern, branching with **`on_true_refs` / `on_false_refs`**;
- **`attack-operator`**: **`AND` / `OR`**, joining several paths;
- **`attack-asset`**: the subject or target of an action;
- custom `x-detection` and `x-mitigation` objects for ATT&CK detection
  strategies and mitigations.

The key idea is the **effect**: an arrow from one action to another means a
**dependency** — the second action needs the effect (state, knowledge, access)
the first produced — which the documentation stresses is "not equivalent to
saying that one action happened before another". Confidence uses a fixed
verbal scale mapped to STIX's 0–100. Techniques usually come from ATT&CK but
need not: custom collections (e.g. VERIS) and ad-hoc actions are allowed.

The tools (Attack Flow Builder, visualisations, a corpus of example flows) moved
to **v4.0/4.1 in October 2026**, adding AI-assisted flow generation from
incident reports, technique recommendations, tags, mitigation and detection
support, and the ATLAS, D3FEND and Fight Fraud frameworks; the language schema
remains **2.0.0**.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | MITRE's format for how ATT&CK techniques combine into attacks. |
| Cryptography | none | Not about cryptography. |
| This project | core | The closest existing format to tmodel's AttackStep/AttackPath: actions, AND/OR operators, conditions and assets (RPT-0002 §9; #63). |

Bears on **DEC-001** (object model — attack steps, gates, ordering vs dependency)
and **DEC-005** (MVP scope — the attack-path graph). A STIX 2.1 import is already
committed by ADR-0007, so Attack Flow documents are a candidate interchange.

## Implementations

Searched 2026-10-22.

| Name | Kind | License | URL |
|---|---|---|---|
| Attack Flow (language, Builder, corpus) | open-source format + tools | Apache-2.0 | https://github.com/center-for-threat-informed-defense/attack-flow |
| JSON schema 2.0.0 | schema | Apache-2.0 | https://center-for-threat-informed-defense.github.io/attack-flow/stix/attack-flow-schema-2.0.0.json |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this summary |

## Limits

- **Summary bar only:** this `spec` record is summarised, not extracted; the
  schema's objects and properties are listed above, but no FX-1 extraction was
  done.
- **Describes attacks, not systems:** a flow records adversary behaviour; it has
  no model of the system under design (no DFD, components or trust boundaries)
  and no risk scoring.
- **Dependency, not order:** connecting two actions states a dependency on
  effects; it does not encode a time order, which a tool must not assume.
- **Tool features are not the language:** the v4.x AI generation, tags and
  extra frameworks are Builder features; their persistence in the 2.0.0 schema
  was not checked.
