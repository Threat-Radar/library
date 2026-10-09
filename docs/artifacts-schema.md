# Distilled artifact schemas

`schema/record.schema.yaml` governs `record.yaml`. **`schema/artifact.schema.yaml`
governs the files under `records/<body>/<id>/distilled/`** — the artifact set
FX-1 produces (`docs/extraction.md`). This note is the human-facing companion to
that schema and to `bin/check-artifacts`, which enforces it.

## Why YAML-shape, not LinkML

Only `requirements.yaml` is LinkML (library#16): requirement ids are externally
referenceable identifiers other repos import, so a generated class model earns
its keep. The other families' real checks are **cross-reference rules** — "every
edge endpoint names a declared object", "every protocol step names a declared
message", "every claim's parent is another claim" — which a validator does
directly over the parsed YAML. A class model would add nothing those checks do
not already give and would couple this standalone library to a toolchain it does
not otherwise need. So these families stay YAML-shape, in the same style as
`record.schema.yaml` and `topic.schema.yaml`, and `bin/check-artifacts` is the
enforcement.

The library stays **standalone** (`CLAUDE.md`): nothing here references tmodel.
The `tmodel_mapping` strings inside `object-model.yaml` are extractor notes, not
dependencies; the schema does not define them and the checker does not resolve
them.

## The families

| file | family | schema string | required body | record `kind` |
|---|---|---|---|---|
| `object-model.yaml` | object-model | `library-object-model/v1` | `objects` + `edges` | `object-model` |
| `requirements.yaml` | requirements | `library-requirements/v2` | `requirements` (LinkML) | `requirements` |
| `state-machine.yaml` | state-machine | `library-state-machine/v1` | `machines`, or `states`+`transitions` | `state-machine` |
| `protocol.yaml` | protocol | `library-protocol/v1` | `roles` or `flows` | `protocol` |
| `messages.yaml` | messages | `library-messages/v1` | `messages`/`structures`/`exchanges` | `messages` |
| `crosswalk.yaml` | crosswalk | `library-crosswalk/v1` | one of five layouts (below) | `crosswalk` |
| `fields.yaml` | field-definitions | `library-requirements/v1` † | `fields` | `fields` |
| `crypto-registry.yaml` | table-registry | `library-fields/v1` † | `tables` | `fields` |
| `*-claim-trees.yaml` | claim-trees | `library-claim-trees/v1` | `trees` | `claim-trees` |
| `verification.md` | verification | `library-verification/v1` ‡ | front matter (below) | `verification` |

† the fields/requirements collision — see below. ‡ going-forward; existing files
diverge — see below.

The **envelope** (`schema` / `record` / `reviewed_by` / `note` / `source_version`
/ `source_digest` / `extracted` / `extracted_by`) is shared. Only `record` is
present on all 155 files and is the one structurally required key; the free-text
"why" key appears as `note` / `notes` / `method` / `finding` / `source` depending
on the lane, and `schema` is missing on 7 files (a data gap, warned). Every
statement, object, edge, field and claim carries a `kind` provenance:
`stated` / `inferred` / `inferred-from-heading`.

### Crosswalk layouts

Six real `crosswalk.yaml` files use five distinct body shapes; `layout` is the
discriminator (inferred from the body today — the re-tagging PR adds it
explicitly):

- **pivot-by-scheme** — `schemes[]`, each with both a forward `rows` and an
  inverse `by_id` (nist/sp-800-218).
- **inverse-index** — one grouped list (`targets`/`frameworks`) mapping an
  external ref to this record's own ids (bsi-tr-03185, etsi-ts-104-219).
- **row-table** — `rows[]`, one row per own activity with several framework
  columns side by side (owasp-dsomm).
- **pair-list** — `pairs[]`, one flat row per (own id, target id) pair
  (owasp-samm-2).
- **transcribed-tables** — top-level blocks named after the source's own tables
  (`table_1`, `appendix_a`, …), verbatim (esf-sscs-developers-2022).

### Verification

`verification.md` is the pass-2/3 evidence log and now a first-class artifact
with its own kind. It is **Markdown**, so it is outside the `distilled/*.yaml`
gate. `schema/artifact.schema.yaml` documents the going-forward front-matter
schema (`library-verification/v1`: `schema`/`id`/`record`/`type`/`updated`/`by`/
`reviewed_by`, optional `passes[verify|cross-check]` and `scope[full|verify-only]`).
The 41 existing files use three divergent conventions (a `library-distilled/v1`
header, or `kind`+`verified`/`verified_by`, or `kind`+`date`/`by`) — only
`record` is universal today. Normalising them is part of the migration PR.

## The `kind` reconciliation

`record.yaml`'s `distillation.artifacts[].kind` enum had no value for four
families, so they were filed under nearest-neighbour kinds:

| family | was filed under | now |
|---|---|---|
| object-model | `diagram` | `object-model` |
| crosswalk | `requirements` | `crosswalk` |
| claim-trees | `diagram` | `claim-trees` |
| verification | *(no kind)* | `verification` |

`record.schema.yaml` v0.7.0 adds these four values to the enum. **This is the
only data-schema edit in this PR.**

### The fields / requirements collision

`library-fields/v1` and the `fields` kind name two different things. The FX-1
field-definition artifact `distilled/fields.yaml` (the one `kind: fields` means)
is mislabelled `schema: library-requirements/v1` in its one real file. The schema
string `library-fields/v1` is instead carried by a *different* artifact — the
verbatim table-registry `crypto-registry.yaml`. Both map to record kind `fields`.
`bin/check-artifacts` resolves the two apart **by filename** and warns on the
schema-string mismatch; choosing a non-colliding schema string for one of them is
left to the migration PR, which can re-tag in one place.

## `bin/check-artifacts`

```sh
pip install -r requirements-dev.txt   # PyYAML — the in-repo _yaml.py drops flow collections
bin/check-artifacts
```

For every `records/*/*/distilled/*.yaml` it parses the file, checks the envelope,
checks the family's required body keys (family resolved by filename), and runs
referential integrity. **The gate is: 0 parse failures and 0 structural errors.**
Referential-integrity mismatches — an edge endpoint, transition endpoint or step
message that does not resolve — are **warnings**, because they are data issues for
the re-tagging/migration PR, not schema defects, and because the real data
legitimately uses descriptive, list-valued, union (`A|B`) and wildcard (`any`)
endpoints. The checker splits unions on `|`, flattens list endpoints, and ignores
the state-machine wildcards (`any`, `any_lower`, `level-n`, …). It is wired into
CI after `bin/validate`.

## Follow-up: data re-tagging (separate PR)

This PR is **schema + validator only**. It does not change any `record.yaml`'s
`distillation.artifacts[].kind` values and does not add `schema:` to the 7 files
that lack it, add `layout:` to crosswalk files, or normalise `verification.md`
front matter. That migration — re-tagging object-model/crosswalk/claim-trees/
verification to their new kinds, resolving the fields schema-string collision,
and clearing the warnings `bin/check-artifacts` reports — is a separate later PR.
