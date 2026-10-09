---
schema: "library-doc/v1"
id: requirements-schema
title: "The requirements LinkML schema and its v2->v3 normalization loader"
type: policy
status: draft
version: "0.1.0"
updated: "2026-10-09"
needs_review: true
reviewed: false
---

# The requirements schema, and how the real corpus loads into it

`schema/requirements.linkml.yaml` (`library_requirements` v3.1, LinkML, CC0) is
the machine schema for extracted requirement sets. `docs/requirements.md` is the
human spec; this file explains the **shape contract** between the two and the
loader that bridges them.

## The design decision: schema describes the NORMALIZED shape; a loader bridges

The 44 on-disk `records/<body>/<id>/distilled/requirements.yaml` files are **raw
`library-requirements/v2`** (3 are v1). In the raw files:

- document-specific long-tail keys sit as **top-level siblings** of the modeled
  fields (no file nests an `attributes:` or `taxonomy:` bag);
- the version key is **`schema:`**, the whole-set note is **`note:`**;
- `maps_to` entries use publisher spellings (`source`, `relationship`,
  `target_edition`, `kind`) and some entries are **bare strings**;
- YAML parses `testable: yes` / `tailorable: no` as **booleans**;
- a few multivalued fields (`actor`, `context`, `inherits_from`, some
  `footnotes`) appear as **scalars**;
- the `aliases:` in the schema are **documentation, not alternate parse keys** —
  LinkML does not read them on input.

Rather than bend the schema into the raw shape (which would make it an un-typed
bag) or rewrite 44 files now (a separate migration PR), the schema describes the
**normalized v3 shape**, and a **normalization loader** is the bridge:

```
raw v2 file  --->  bin/_requirements.normalize_set(doc)  --->  v3-conformant dict  --->  linkml-validate
(unchanged on disk)        (the bridge)                        (ephemeral)              (the gate)
```

The loader (`bin/_requirements.py`, stdlib + PyYAML) **mutates nothing on disk.**
It is pure data: `normalize_set(raw_dict) -> normalized_dict`.

## What the loader does

| Transform | Detail |
|---|---|
| **Header renames** | `schema` -> `conforms_to` (verbatim, no default — the 3 v1 records keep `v1`); `note` -> `set_note` |
| **Fold parallel taxonomies** | header `practices` / `security_levels` / `requirement_areas` / `principles` / `tasks` / `sources` / `reference_schemes` become `TaxonomyNode`s in one `taxonomy` list, each tagged with `taxonomy_kind` |
| **Header extension bag** | every other non-slot header key (`source`, `source_normative_counts`, `extracted_normative_counts`, `source_scope`, `source_files`, `source_url`, …) relocates into `RequirementSet.attributes` (symmetry with `Requirement.attributes`) |
| **Per-req renames** | `note`/`additional_notes` -> `notes`; `testable_note` -> `testable_reason`; `refs` -> `external_refs` |
| **Per-req attribute bag** | every per-req key that is not a declared slot (~100-key long tail: `playbook`, `chapter_name`, `responsible_roles`, `obligated_party`, `business_function`, `stream`, `baselines`, `levels`, `primarily_applies_to`, …) relocates into `Requirement.attributes` |
| **Bool coercion** | `testable` and `contributes_to_assurance` booleans -> `"yes"`/`"no"` strings (`tailorable` stays a real boolean) |
| **Scalar -> 1-list** | `actor`, `context`, `inherits_from` (and other multivalued slots) wrap a scalar into a 1-element list |
| **`maps_to` key remap** | per entry: `source`/`source_ref` -> `mapping_source`, `relationship` -> `relation`, `target_edition` -> `edition`, `kind` -> `xref_kind`, `published_by_source` -> `published_by`, `note`/`target_note` -> `xref_note`, `record` -> `xref_record`, `id` -> `xref_id`, `basis` -> `xref_basis`; a **bare-string** entry becomes `{ref: <string>}`; leftover keys relocate into the entry's `attributes` |
| **`level` tier** | a numeric `level` (BSIMM 1/2/3) is stringified onto the `StructuralLevel` string arm (migrates to `attributes.tier` later) |
| **Derived `verb_bcp14`** | set to the canonical BCP 14 keyword when `verb` is one; **never overwrites** the verbatim `verb` |
| **Nested objects** | examples -> `NormativeExample{example_id,text}`; deliverables keep `{deliverable_id,designator,title,from_*}` and relocate extras (`deliverable`, `clause`, `audit_check`, …) to `attributes`; bare-string footnotes -> `{text}` |

Nothing is dropped: a coverage check confirms **every raw key is preserved** as a
renamed slot or an `attributes` entry (`bin/check-requirements` is the gate; the
coverage assertion is in the PR description).

## The acceptance gate

```sh
pip install -r requirements-dev.txt        # linkml + pyyaml (dev/CI only)
bin/check-requirements                      # normalize all 44, then linkml-validate
```

`bin/check-requirements` normalizes every raw file through `normalize_set` and
runs:

```
linkml-validate -s schema/requirements.linkml.yaml -C RequirementSet \
  --allow-null-for-optional-enums <44 normalized files>
```

Current result: **44 files validated, 0 failures.** (`gen-json-schema
schema/requirements.linkml.yaml` also generates cleanly.) The gate is wired into
`.github/workflows/ci.yml`. The library's record/topic tooling stays stdlib-only;
these two deps exist solely for this gate.

`bin/check-requirements --invariants` additionally runs the **cross-field
invariants** that are not schema shape and stay in Python, never SHACL:
count reconciliation, `kind=inferred` needs a note, `provenance=ours` needs a
`rationale`. These are warn-only here (they are enforced by `bin/validate`).

## Adversarial findings, resolved

- **C1** (unknown keys dropped) — the loader relocates them into `attributes`
  bags; the schema declares the normalized shape it targets.
- **C2** (`aliases` are not parse keys) — the loader renames the data's dominant
  spellings to the canonical slots (header `note`, `maps_to` `source`/
  `relationship`/`target_edition`/`kind`).
- **C3** (`schema:` vs `conforms_to` + `ifabsent`) — loader renames `schema` ->
  `conforms_to`; the `ifabsent` default is **dropped** so the 3 v1 records keep
  `library-requirements/v1`.
- **C4** (`applies_to` is a scalar scope string) — `applies_to` stays a scalar
  `string`; the KG-edge concept is a **new** slot `scopes_to` (range
  `ContextLink`).
- **C5** (header taxonomies/metrics unmodeled) — folded into `taxonomy`;
  `RequirementSet.attributes` is the `Any` header extension bag.
- **M1** — `ReferenceEdition` has a key slot `scheme_key` (`key: true`) so the
  scheme-keyed map validates natively.
- **M2** — `verb`/`actor` demoted to `recommended` (108/48 real rows lack them).
  `condition` is **recommended, not required**: §1 lists it mandatory but only
  **984/6274** rows carry one. **RESOLVED (sponsor, 2026-10-09) → hybrid:** keep
  `recommended` in the schema so the corpus loads; the gate emits a warn-only finding
  for a missing `condition`; the extract skill + §1 are tightened so **every newly
  extracted or re-touched requirement states `condition`** (explicit "unconditional"
  allowed); old rows are backfilled **as records are revisited**, not in a mass
  inference pass. The requirements schema may keep resolving toward required as
  coverage rises.
- **M3** — `verbs` (multivalued) added for the 72 rows that bundle verbs.
- **M4** — `maps_to` gains `xref_record` (`record`), `xref_id` (`id`),
  `xref_basis` (`basis`), and reuses `title`; `id` is renamed so it never
  collides with the Requirement identifier.
- **M5** — the `LifecyclePhase` enum is widened to **every** value observed
  across the corpus (incl. `operations/response`, the top value) so it is
  honest; the string arm still carries any future family-specific phase.

## Open-question resolutions applied

`any_of:[enum,string]` kept with **honest** enums; derived optional `verb_bcp14`
(loader-populated, never hand-authored); `actor`/`context` forced plain
`multivalued` (scalars wrapped on load); one wide `CrossReference` kept (names
fixed, not subclassed); the top ~14 long-tail keys promoted to real optional
slots (`section`, `section_title`, `section_name`, `chapter`, `role`, `verifier`,
`variant`, `requirement_type`, `maturity_level`, `question`, `answer_set`,
`track`, `family`, `basis`) with the true tail in `attributes`; KG targets
opaque (`uriorcurie`); the `id` pattern kept (0 of 6274 violate it); cross-field
invariants in Python, not SHACL.

## tmodel-independence (preserved)

The schema imports only `linkml:types`. No prefix resolves to the threat model;
`satisfied_by`/`scopes_to` targets are opaque `uriorcurie` the consumer resolves.
The dependency points consumer -> library, never the reverse.

## Status of the raw files

The 44 files stay **raw v2** until the separate data-migration PR. This PR
changes only the schema, the loader, the gate, and this doc.
