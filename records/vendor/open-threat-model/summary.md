---
schema: "library-summary/v1"
id: open-threat-model
record: open-threat-model
type: summary
updated: "2026-10-13"
---

# Open Threat Model specification and JSON Schema

|  |  |
|---|---|
| **Type** | repo (specification text + JSON Schema), maturity draft |
| **Publisher** | IriusRisk (vendor; no external governance body) |
| **Version** | OTM 0.2.0: "Current schema version: 0.2.0" (README L18); schema `$id` `https://iriusrisk.com/schema/otm-0.2.0.schema.json`, JSON Schema draft-07. 0.2.0 introduced 2023-08-29 (`355287f5`); schema last changed 2024-01-31 (`06288a0d`) with no version bump. |
| **Source** | https://github.com/iriusrisk/OpenThreatModel at commit `c88c5a7b4115f0f025e28d5682a2b0d790b389e4` (2025-12-11, the repository head when read) |
| **Schema** | `otm_schema.json` — SHA-256 `81e7f5a5…545eef0c` |
| **Specification** | `README.md` — SHA-256 `4acfb48b…ef78cf8c0` |
| **Licence** | Split. The repository, including the specification text and examples, is CC BY-SA 4.0 (`LICENSE`, added 2024-11-20). The schema file's `$comment` says it "is published under the terms of the Apache License 2.0". |

## Overview

OTM is a JSON (or YAML) document format for exchanging one system's threat
model between tools. A document has a required `otmVersion` and `project`,
and lists of `assets` (with confidentiality, integrity and availability
scores), `trustZones` (nested, each with a `trustRating`), `components` (each
inside exactly one trust zone or component), `dataflows` (`source` to
`destination`), `threats` (with `categories`, `cwes` and likelihood/impact)
and `mitigations` (with `riskReduction`). A component or data flow holds
threat *instances*, each a reference to a root threat plus a free-string
`state` and its mitigation instances. `representations` carry diagram layout
and code locations. Nine object types carry a free-form `attributes` map,
and no object is closed, so unknown keys validate.

The README marks fields **REQUIRED** and gives ranges ("From 0 to 100") and
reference rules that the schema does not enforce: the schema has no numeric
bounds, allows `null` where the README forbids it, and checks no id
uniqueness or reference. `distilled/` records both views and a derived strict
schema that adds the README's rules.

## Applicability

- **Security: core.** A security-model format: assets, trust zones, threats,
  mitigations and their per-component state.
- **Cryptography: none.** Defines no cryptographic mechanism.
- **This project: core.** ADR-0007 (DEC-002) commits tmodel to importing
  OTM, with a crosswalk and a round-trip vector. Components, threats,
  mitigations and `cwes` map onto ADR-0010's `Component`, `ThreatInstance`,
  `Mitigation` and `Weakness`. OTM's assets, trust zones and data flows have
  no target class in the accepted schema (RPT-0005 gap G13), and OTM has no
  attack steps, paths, vulnerabilities, products or review records. Details
  in `distilled/design-notes.md`.

## Implementations

| Name | Kind | Licence | URL |
|---|---|---|---|
| IriusRisk | commercial; imports and exports OTM | commercial | https://www.iriusrisk.com/ |
| iriusrisk-cli | open-source CLI; OTM import, export and validation | see repository | https://github.com/iriusrisk/iriusrisk-cli |
| StartLeft | open source (Apache-2.0); generates OTM from IaC, diagrams and other tools' exports | Apache-2.0 | https://github.com/iriusrisk/startleft |

Searched 2026-10-04 (RPT-0003); StartLeft added from RPT-0005 (2026-10-05).
RPT-0005's Table 4 lists further producers and consumers (threatcl, Devici,
Threat Dragon `main`, tmac) and §8 of its fan-out notes records what each
converter loses; those are research notes, not checked again here.

## Artifacts in this record

- `record.yaml` — metadata, digests, relations, FX-1 distillation block.
- `distilled/` — the FX-1 artifact set; `distilled/README.md` indexes each
  file and its coverage: normative text and requirements from the README and
  schema, the verbatim schema plus a derived strict schema, every object and
  field, the instance-state lifecycle, every README example as a fixture with
  actual validation results, design notes for tmodel, and the verification
  record.

## Limits

- Pins one commit of one repository. IriusRisk's product documentation, the
  StartLeft code and any OTM features specific to IriusRisk were not examined.
- The README and the schema disagree in places; both are extracted and every
  disagreement is recorded (`source_defects` in
  `distilled/requirements.yaml`). Neither is declared authoritative by the
  source.
- The schema text changed in 2024 under the same 0.2.0 id, so "0.2.0" names
  two different schema texts; this record pins the later one.
- Vendor-controlled and still 0.x. CONTRIBUTING.md says semver is intended,
  but "the policy for versioning could change in the future".
- Gathered for RPT-0003 (tmodel threat-modeling products); fully extracted
  for RPT-0005 (tmodel #39).
