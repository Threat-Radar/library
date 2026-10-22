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
| **Published** | Extension labelled 2.0.0: defined 2022-08-02, released with the tools' v2.0 on 2022-10-27; the schema has since been widened in place. Read at tag v4.1.0 (2026-10-14) |
| **Identifier** | https://center-for-threat-informed-defense.github.io/attack-flow/language/ |
| **Source** | https://raw.githubusercontent.com/center-for-threat-informed-defense/attack-flow/v4.1.0/docs/language.rst |
| **Digest** | `85ae7b7f367b57c935328276a412e5b2f051e4d48f2ab622276359d49615fa49` (the raw `docs/language.rst` source at tag v4.1.0, retrieved 2026-10-22; the rendered page at the identifier differs, because its object section is regenerated from the schema). Also read: `docs/introduction.rst` (`0325405cc98e764ca836e6647df70637cb2e3e7e3cc106d9fd401c20a4f32588`) and `stix/attack-flow-schema-2.0.0.json` (`fff896f5e1bdc39d9b387c0d3571307037cf9be1059de9cd94d066d1da2997cc`), same tag |

## Overview

Attack Flow is a machine-readable language for **how adversary actions combine
into an attack**, defined as an extension to **STIX 2.1** so that flows
interoperate with existing threat-intelligence tools. A flow document has
exactly one **`attack-flow`** object (name, description, `start_refs`, and a
`scope` label). Its building blocks, as defined in the JSON schema, are:

- **`attack-action`**: one execution of a behaviour (only `name` is required;
  usually `technique_id` and `tactic_id`, optional refs to the ATT&CK objects,
  `execution_start` / `execution_end`, a command, the assets it touches), linked
  to what follows through **`effect_refs`**;
- **`attack-condition`**: a state or outcome after an action, with an optional
  (experimental) detection pattern of any type, branching with
  **`on_true_refs` / `on_false_refs`**;
- **`attack-operator`**: **`AND`** (all incoming paths must succeed) or **`OR`**
  (any one is enough);
- **`attack-asset`**: the subject or target of an action.

An arrow from one action to another is a **dependency**: "the second action
cannot be executed until the first action completes successfully"
(`introduction.rst`), which the documentation calls a more powerful concept
than one action happening before another. The graph therefore gives a partial
order; independent branches stay unordered, and timestamps are optional.

`scope` values in the schema: `incident`, `campaign`, `threat-actor`,
`malware`, `emulation-plan`, `attack-tree`, `other` (`attack-tree` added in
2024 and `emulation-plan` in 2025 without a version change; `language.rst`
still lists five). Attack trees are drawn with the same blocks: goals as actions
without techniques, joined bottom-up through operators. Flows can be
hypothetical (emulation plans, attack trees, "what-if" scenarios at the
"Speculation" confidence level) as well as observed. Techniques usually come
from ATT&CK, but Workbench collections, other knowledge bases (e.g. VERIS) and
ad-hoc actions are allowed.

The tools (Attack Flow Builder, visualisations, a corpus of example flows)
added ATLAS, D3FEND and Fight Fraud in v3.1 (April 2026), AI-assisted drafting
from incident reports, technique recommendations and tags in v4.0, and D3FEND
countermeasures and red-team tests in v4.1 (October 2026).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | MITRE's format for how ATT&CK techniques combine into attacks. |
| Cryptography | none | Not about cryptography. |
| This project | core | The closest existing format to tmodel's AttackStep/AttackPath: actions, AND/OR operators, dependency, shared steps, hypothetical flows (RPT-0002 §9; #63). |

Bears on **DEC-001** (object model — attack steps, gates, dependency vs order)
and **DEC-005** (MVP scope — the attack-path graph). A STIX 2.1 import is already
committed by ADR-0007, so Attack Flow documents are a candidate interchange.

## Implementations

Searched 2026-10-22.

| Name | Kind | License | URL |
|---|---|---|---|
| Attack Flow (language, Builder, corpus) | open-source format + tools | Apache-2.0 (bundled ATT&CK content under the ATT&CK Terms of Use) | https://github.com/center-for-threat-informed-defense/attack-flow |
| JSON schema (labelled 2.0.0) | schema | Apache-2.0 | https://github.com/center-for-threat-informed-defense/attack-flow/blob/v4.1.0/stix/attack-flow-schema-2.0.0.json |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this summary |

## Limits

- **Summary bar only:** this `spec` record is summarised, not extracted; no FX-1
  extraction was done.
- **Describes attacks, not systems:** no DFD, components or trust boundaries, and
  no risk scoring.
- **Schema versioning:** the schema labelled 2.0.0 was widened in place, so an
  older copy rejects newer flows; its published URL (`$id` and the extension's
  `schema` field) currently returns 404.
- **Builder conventions outside the schema:** detections, mitigations,
  countermeasures and red-team tests are custom `x-` objects linked by generic
  `related-to` relationships, and published flows carry an undefined
  `ttp_frameworks` property; a STIX importer must allow custom objects, read
  `related-to` edges as well as `effect_refs`, and cannot learn the ATT&CK
  version from a flow.
- **Confidence:** the Builder's scale adds "AI Generated" at 0, the documented
  value for "Speculation", so exported STIX cannot tell AI-drafted content from
  a human's what-if.
