---
record: open-threat-model
kind: design-notes
title: "open-threat-model — bearing on our design"
extracted: "2026-10-13"
reviewed_by: ""
---

How Open Threat Model (OTM) 0.2.0 bears on tmodel.

**Sources.** OTM quotes are from the specification `README.md` (SHA-256
`4acfb48b…ef78cf8c0`) and the schema `otm_schema.json` (SHA-256
`81e7f5a5…545eef0c`), both at commit `c88c5a7b` of `iriusrisk/OpenThreatModel`,
cited by line. Requirement ids are `open-threat-model#R-NNNN`
(`requirements.yaml`); D-nn are source defects (`requirements.yaml`
`source_defects`, `normative.md`).

**Decisions.** tmodel decisions are read from tmodel `main` at `cd02eff`
(2026-10-12; the ADRs and the LinkML model are unchanged at `9f56628`, `main`
on 2026-10-16):

- **ADR-0010** accepts DEC-001a, the core object model. Its class names
  supersede ARCH-0001 §3's working labels. Class descriptions are quoted from
  `spec/schema/tmodel-object-model.linkml.yaml`.
- **DEC-001b**, the governed layer, is held open. It includes `ThreatModel`.
- **ADR-0007** accepts DEC-002. It commits tmodel to importing OTM, with a
  `MAP-NNNN` crosswalk and a `spec/vectors/` round trip. Its committed exports
  are JSON-LD, Turtle, GraphML and CSV, not OTM.
- **ADR-0006** accepts DEC-003, the composite risk vector.
- **ADR-0004** sets storage: files in git, stable ids and typed edges.
- **DEC-009** is open.
- Requirements cited: R-005 (import, round trip proven by a vector), R-010
  (Weakness→CWE), R-018 (human Review), R-020 and R-021 (generic → product,
  mitigation over the lifecycle).

OTM is an **interchange file format**, not a protocol and not a catalog: one
JSON or YAML document carries one project's threat model ("An OTM document is
itself a JSON object, which may be represented either in JSON or YAML
format.", L23). ADR-0007 has already decided that tmodel imports it. So the
questions here are what an import can put into ADR-0010's classes, what has
nowhere to go, and what the importer must check that the OTM schema does not.

## What we adopt

1. **OTM 0.2.0 as the committed import** (ADR-0007, R-005). tmodel pins 0.2.0:
   `otmVersion` is required at the root (L55; schema L7), and the schema `$id`
   is `…/otm-0.2.0.schema.json` (schema L3). Every file is validated before it
   is mapped (*adapt* 1).
2. **Imported content enters as unreviewed claims** (ADR-0010, R-018). Every
   imported node and edge is recorded as an `Assertion`, with provenance
   pointing at the OTM file and its digest. Its `assertion_status` stays short
   of accepted until a `Review` exists. This extends ADR-0010's rule, "never
   present AI output as reviewed", to imported content. The OTM file says
   nothing about who decided what.
3. **Component → `Component`, with care.** ADR-0010's `Component` is an
   "Authoritative deployed artifact (service, container, dependency, chip,
   core) — not an OTM diagram node (§0)". An OTM component is a diagram-level
   element with a free-string `type`. So an imported component is a candidate
   `Component`, to be confirmed by review. A component whose `parent` is
   another component becomes `composed_of` on the parent. A component whose
   parent is a trust zone has no target (G13, below).
4. **Root threat → `ThreatInstance`.** ADR-0010 defines `ThreatInstance` as
   "A threat in a model, not the generic catalog entry". An OTM root
   `threats[]` entry is exactly that: a model-scoped threat that components
   and data flows reference. ADR-0010's generic level is `AttackPattern`
   (CAPEC, ATT&CK). OTM threats carry no CAPEC or ATT&CK reference, so they do
   not map to `AttackPattern`.
5. **Root mitigation → `Mitigation`; mitigation instance → `mitigates`.** A
   mitigation instance under a threat instance (L1869) becomes `mitigates`
   (range `ThreatInstance`) on the `Mitigation`, with its state mapped to
   `mitigation_status` (*adapt* 5).
6. **`threats[].cwes` → `Weakness`** (R-010). `cwes` is an "Array of CWE
   identifiers of weaknesses associated with the threat" (L1567). The importer
   parses `CWE-<n>` into a `Weakness` with `catalog_ref`. `ThreatInstance` has
   no slot pointing at a `Weakness`, so the link is an `Assertion` (its
   `predicate` is an open string). The CWE id is resolved against the pinned
   catalog (record `cwe`), and that record's `Mapping_Notes/Usage` gate
   applies.

## What we adapt, and how

1. **Validate against the README, not only the schema.** The schema enforces
   less than the README states.
   - *Range.* The README gives every risk value "From 0 to 100" as an integer
     (L801, L813, L825, L1266, L1658, L1682, L1824). The schema types them
     `number`, with no bounds (schema L65–L67, L89, L182, L184, L207; D-05,
     D-06).
   - *Null.* The README says "`null` is not supported as a type" (L31). The
     schema allows `null` for most optional fields and arrays, for
     `likelihood` (schema L182), and even for the two required fields of a
     mitigation instance (schema L268–L269; D-03).
   - *References.* The schema checks no uniqueness and no reference (D-17).

   The importer runs two checks: the source schema (pinned and verbatim,
   `schema/otm_schema.json`), then the derived strict schema in `schema/`,
   which adds the README's rules. A file that passes the first and fails the
   second is imported with a finding, not rejected, because real producers
   emit such files.
2. **Identifiers** (ADR-0004). OTM ids are free strings with no namespace,
   unique only by description ("Unique identifier for the …"). tmodel mints a
   stable `Node.id` for every imported object. It records the OTM id, scoped
   to the source file (`project.id` plus file digest), in the import's
   provenance. Of the classes an import fills, only `Component` has a slot
   for an external id (`identifiers`); see *gaps*.
3. **Referential integrity.** Instance references are prose rules with
   *should*. A threat instance's id "should be one of the threats described in
   the root node threats" (L1731–L1732). A mitigation instance's "should be
   declared in the root node mitigation" (L1885). `parent`, data-flow
   `source`/`destination` and asset-instance ids are plain strings. The
   importer resolves every reference and reports each dangling one. It does
   not invent the missing target.
4. **`categories` → `method_facet` / `violates_property`.** `categories` has
   no vocabulary in the source; the README's example is `Spoofing`,
   `Authentication`. ADR-0010 has `method_facet` (enum: `stride`, plus
   post-MVP `linddun` and `maestro`) and `violates_property` ("STRIDE sketch,
   not a closed enum: S authentication, T integrity, …"). A STRIDE category
   name maps to `method_facet: stride` plus the matching property. Any other
   category has no slot (*gaps*).
5. **Mitigation instance `state` → `mitigation_status`.** OTM's state is a
   required free string (L1897), and the source enumerates no values (D-19).
   The README examples use `implemented` (L1900) and `required` (L1495), as
   does `EXAMPLE.yaml` (L95, L164).
   ADR-0010's `MitigationStatus` is closed: `planned`, `in_progress`,
   `complete`, `accepted_risk`, `not_applicable`. The OTM `MAP-NNNN` needs a
   table, for example `implemented` → `complete` and `required` → `planned`.
   That table is a candidate for its author to confirm, not a mapping this
   note fixes. A value outside the table has no slot.
6. **Risk numbers** (ADR-0006). These OTM values are 0–100 numbers:
   - threat `likelihood` and `impact`;
   - asset C/I/A;
   - zone `trustRating`;
   - mitigation `riskReduction`.

   The accepted vector is different. Feasibility is the ISO/SAE 21434 Table-1
   4-point scale, human-rated at MVP. Impact is the S/F/O/P `ImpactVector`,
   human-supplied. No OTM number converts into either, and none has a slot.
   At most they can be shown to the human rater as imported evidence.
   `riskReduction` also cuts against ADR-0006: mitigation status is "not an
   input that silently lowers the derived risk", and `riskReduction` is
   exactly such an input.

## What we reject, and why

1. **OTM as canonical store or export format** (ADR-0004, ADR-0007). The
   canonical form is tmodel's own LinkML-shaped files. ADR-0007's committed
   exports are JSON-LD, Turtle, GraphML and CSV, so tmodel does not write OTM.
   An earlier draft of this note proposed `attributes` as an export carrier;
   that is withdrawn.
2. **Reading OTM `state` as a Review** (ADR-0010 `Review`, R-018). A state
   string records no reviewer, date, verdict or justification. An imported
   threat or mitigation arrives unreviewed, whatever its state says.
3. **`representations` as model data.** ADR-0010's `View` is a "Derived
   presentation lens … rendered geometry is transient and out of this schema".
   OTM diagram positions and sizes (Representation element, Size, Position)
   and code locations are not imported into the graph.

## Gaps: OTM content with no target class

**G13** (RPT-0005 report, §6 and gap table): "The committed OTM import has no
target for three of OTM's core entity types." The accepted schema has no
`Asset`, `TrustBoundary` or `DataFlow` class, so an import drops all three:

| OTM | What it carries | Nearest thing in the accepted schema, and why it is not a target |
|---|---|---|
| `assets[]` | id, name, description; AssetRisk `confidentiality` / `integrity` / `availability` 0–100; per-component Asset instance `processed` / `stored`; data-flow `assets` | None. The schema says so itself: "Asset is not a §13 class; the slot is on Product, ProductInstance, and Component as the structural stand-in" (`owned_by`). `ImpactVector` is S/F/O/P, not C/I/A. |
| `trustZones[]` | id, name, `type`, `trustRating` 0–100, nesting through `parent`; the trust zone that encloses a component | None. A component's `parent` chain ends at a trust zone (barring cycles, which the schema does not prevent), so any OTM file with components carries trust zones. |
| `dataflows[]` | `source`, `destination`, `bidirectional`, carried `assets`, and threat instances on the flow | None. `depends_on` ("Dependency edge") and `uses_component` ("Use edge along which vuln/finding propagation is sound") relate components, but neither is a data flow. Recording a flow as either would change what the edge means. |

Consequence: ADR-0007 requires a round-trip vector for the OTM import. For any
OTM file that uses these types, the vector cannot pass until the gap is
closed. The report records the sponsor's direction (2026-10-14): add them,
shaped by iterative example models of published automotive attacks; accepting
the added classes still needs an ADR amending ADR-0010. Until that ADR, the
accepted schema has no target for them. This note makes no proposal of its
own.

**Related gaps, of the same kind.** These are not part of G13 as the report
words it, and are recorded so the OTM mapping can count them:

- **`project`.** The nearest class, `ThreatModel`, is DEC-001b and not
  accepted, so a file's project (name, id, owner) has no accepted container.
  `owner` can become a `Party`, but `owned_by` exists only on `Product`,
  `ProductInstance` and `Component`.
- **Where a threat instance applies, and its `state`.** `ThreatInstance` has
  no slot naming the component or data flow it is on, and no state slot. The
  link can only be an `Assertion`. The state string (`exposed`, `mitigated`)
  has no target.
- **One mitigation, many states.** OTM lets one root mitigation be
  `implemented` under one threat instance and `required` under another.
  ADR-0010's `Mitigation` has one `mitigation_status`; the schema says status
  sits there "until a separate MitigationInstance class is accepted". The
  same holds for R-021's per-product tracking.
- **External ids.** Only `Product`, `ProductInstance` and `Component` have
  `identifiers`. An imported `ThreatInstance` or `Mitigation` has no slot for
  its OTM id (`Mitigation`'s `external_refs` is for "Linked work items, e.g. a
  Jira key"). The round trip then depends on provenance records.
- **No slot at all.** `attributes` (on 9 structures), `tags`, component `type`,
  non-STRIDE `categories`, and `representations` (rejected above).

## Mapping to our decisions

| tmodel (accepted unless noted) | OTM construct | verdict |
|---|---|---|
| ADR-0010 `Component` | `components[]` | adopt as candidate, confirmed by review |
| `composed_of` | `parent.component` | adopt |
| none (G13) | `assets[]`, AssetRisk, Asset instance | no target until an ADR amends ADR-0010 |
| none (G13) | `trustZones[]`, `parent.trustZone` | no target until an ADR amends ADR-0010 |
| none (G13) | `dataflows[]` | no target until an ADR amends ADR-0010 |
| `ThreatInstance` | root `threats[]` | adopt |
| `AttackPattern` | none (no CAPEC / ATT&CK field) | not mapped |
| `method_facet`, `violates_property` | `threats[].categories` | adapt: STRIDE names only |
| `Weakness` (`catalog_ref`) + `Assertion` | `threats[].cwes[]` | adapt: parse, resolve via `cwe` |
| `Mitigation`, `mitigates` | root `mitigations[]`, Mitigation instance | adopt |
| `mitigation_status` (`MitigationStatus`) | Mitigation instance `state` | adapt: table; one status per Mitigation |
| none | Threat instance placement and `state` | gap |
| `RiskScore`, `ImpactVector` (ADR-0006) | ThreatRisk, AssetRisk, TrustZoneRisk, `riskReduction` | no conversion; evidence only |
| `Assertion`, `Review` | none | every import is an unreviewed Assertion |
| `Party` | `project.owner` | adapt: name only |
| `ThreatModel` (DEC-001b, open) | `project` | no accepted target |
| `View` | `representations` | reject: geometry out of schema |
| `identifiers` | OTM `id` | Component only; others via provenance |
| ADR-0007 import + vector | OTM 0.2.0 file | adopt; vector blocked by G13 |
| ADR-0004 | file-local string ids | adapt: tmodel ids authoritative |

**What the existing converters teach.** These come from RPT-0005
`fanout-models-requirements.md` §8, read from the converters' code on
2026-10-05; none of them is in the pinned source.

- Threat Dragon `main` imports OTM threats with `status` forced to `Open` and
  does not carry `cwes`.
- Threat Dragon v2.6.2 refuses OTM import outright.

The OTM vector should therefore check that `cwes` and the instance states
survive import, or declare their loss.

## Open questions

1. **State vocabulary.** The source gives no list for either instance
   `state`. Which values do IriusRisk exports actually use? The
   `MitigationStatus` table needs real exports, not only the README
   examples.
2. **G13 and the related gaps.** The sponsor has directed that the three G13
   types be added (2026-10-14), but until an ADR amending ADR-0010 accepts
   them, should the OTM `MAP-NNNN` and its vector declare `assets`,
   `trustZones`, `dataflows`, threat-instance placement and state as dropped,
   or should the vector wait? That is the sponsor's call, not this note's.
3. **Strict or lenient import.** If a file passes the source schema but breaks
   a README rule (a range, a null, a dangling reference), is that a warning or
   a rejection? This note proposes a warning plus a finding, for the OTM
   `MAP-NNNN` to settle.
4. **Version churn.** The schema has said 0.2.0 since 2023-08-29, yet it
   changed on 2024-01-31 without a version bump (commit `06288a0d`, "define
   objects for all arrays"). Before that commit, the `representations` and
   `assets` arrays carried `required` and `properties` on the array itself,
   where JSON Schema ignores them, so the 2023 text did not check
   representation or asset items at all (the other five root arrays already
   had `items`). The pinned 2024 text wraps them in `items` and does. A file that says `otmVersion: 0.2.0`
   may have been checked only against the weaker text. So tmodel validates
   against the pinned text and treats the result as its own finding, not the
   producer's claim. A later OTM version gets a new library record linked by
   `supersedes`. RPT-0005 also notes that CycloneDX TM-BOM may replace OTM as
   the cross-vendor format (gap G12).
