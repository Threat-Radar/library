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

`record.schema.yaml` v0.7.0 adds these four values to the enum; v0.8.0 adds four
more for the forward-looking families below (`procedures`, `agents`,
`formal-proofs`, `threats`). Extending that enum is the **only** edit this PR
makes to record data's schema — no `record.yaml` is re-tagged.

### The fields / requirements collision

`library-fields/v1` and the `fields` kind name two different things. The FX-1
field-definition artifact `distilled/fields.yaml` (the one `kind: fields` means)
is mislabelled `schema: library-requirements/v1` in its one real file. The schema
string `library-fields/v1` is instead carried by a *different* artifact — the
verbatim table-registry `crypto-registry.yaml`. Both map to record kind `fields`.
`bin/check-artifacts` resolves the two apart **by filename** and warns on the
schema-string mismatch; choosing a non-colliding schema string for one of them is
left to the migration PR, which can re-tag in one place.

## Forward-looking families (no records yet)

The seven families above are **grounded in real files** (each `derived from` a
record in the corpus). The four below are **grounded design**: the sponsor asked
that every artifact type be formalised, including types we expect to extract but
have **no records for yet** (0 in the corpus on 2026-10-09). Their shapes are
therefore anchored in external standards and the FX-1 intent (`docs/extraction.md`)
rather than lifted from an observed file. They are formalised under
`forward_looking_families` in `schema/artifact.schema.yaml`.

They are **extraction-layer** artifacts — what a *source document* describes —
and stay standalone. Where one touches a downstream knowledge-graph object (a
threat/weakness/vulnerability/mitigation that a consuming project models), the
link is an **opaque reference by id**, carried by the consumer, never a
dependency of this library — exactly like the `tmodel_mapping` notes on
`object-model`. No record is created and nothing is re-tagged; the checker
recognises each by filename stem and, with zero files, runs **zero** checks.

| file | family | schema string | required body | record `kind` | anchor |
|---|---|---|---|---|---|
| `procedures.yaml` | procedures | `library-procedures/v1` | `procedures` | `procedures` | SSDF/ISO process clauses |
| `agents.yaml` | agents | `library-agents/v1` | `agents` | `agents` | agentic-AI / actor models † |
| `formal-proofs.yaml` | formal-proofs | `library-formal-proofs/v1` | `claims` or `proofs` | `formal-proofs` | SACM, CAE/GSN assurance cases |
| `threats.yaml` | threats-vulnerabilities | `library-threats/v1` | one of `threats`/`weaknesses`/`vulnerabilities` | `threats` | CWE/CAPEC/CVE, STRIDE, 21434 |

† **`agents` is a sponsor-named family and its precise scope is open for review**
— see the open question at the end of this section.

The skeletons below are **illustrative**, to show reviewers the intended shape.
They are **not records** — do not copy them into `distilled/`.

### `procedures` — a documented process

Ordered `steps` (order is significant) with the `roles` that perform them and
the entry/exit criteria that bound each procedure. Distinct from `protocol`
(message exchange); a procedure is a work process whose steps need not exchange
a message.

```yaml
schema: library-procedures/v1
record: <record-id>
roles:
  - {id: developer, definition: "writes and commits code"}
  - {id: reviewer,  definition: "approves a change before merge"}
procedures:
  - id: secure-code-review
    name: "Secure code review"
    locator: "§4.2"
    trigger: "a pull request is opened"
    entry_criteria: ["change builds", "automated scan has run"]
    exit_criteria:  ["reviewer approval recorded"]
    steps:
      - {n: 1, actor: developer, action: "open PR with scan results attached",
         outputs: ["pull-request"], locator: "§4.2.1", kind: stated}
      - {n: 2, actor: reviewer,  action: "review diff and scan findings",
         inputs: ["pull-request"], locator: "§4.2.2", kind: stated}
    kind: stated
```

### `agents` — actor/agent roles the source defines

Identity, role, capabilities, autonomy level and the trust assumptions the
source attaches. These are actors the **source** names — **not** our FX-1
extraction agents.

```yaml
schema: library-agents/v1
record: <record-id>
agents:
  - id: orchestrator
    role: "plans and dispatches sub-tasks to tool agents"
    capabilities: ["task decomposition", "tool invocation"]
    autonomy: semi-autonomous        # PROVISIONAL vocabulary — scope under review
    trust_assumptions: ["prompt channel is authenticated", "tools are sandboxed"]
    locator: "§3.1"
    kind: stated
```

### `formal-proofs` — assurance/proof structures

`claims` the source asserts, the `arguments`/strategies linking them to
subclaims and `evidence`, the `assumptions` relied on, and the `obligations`
still to discharge. One case (top-level `claims`) or several (`proofs`).

**Relation to `claim-trees`:** `claim-trees` is the narrow transcription of APC
assurance-claim trees recovered from source **diagrams** (SVG), each node
`{id, text, parent, parent_kind}`, edge geometry lost. `formal-proofs` is the
**general** assurance/proof artifact — arguments, evidence, assumptions and
obligations as first-class lists, independent of any diagram. A claim-tree is a
degenerate formal-proof (claims only); they are kept separate so the
diagram-transcription provenance of claim-trees is not lost.

```yaml
schema: library-formal-proofs/v1
record: <record-id>
claims:
  - {id: C1, statement: "the signing key is never exposed in plaintext",
     supported_by: [A1], locator: "§6", kind: stated}
arguments:
  - {id: A1, statement: "argue over all key-handling paths",
     from_claim: C1, to: [E1, E2], kind: stated}
evidence:
  - {id: E1, description: "static analysis report, 0 plaintext-key flows",
     source_ref: "artifacts/sa-report.json", kind: stated}
  - {id: E2, description: "HSM configuration review", kind: inferred}
assumptions:
  - {id: K1, statement: "the HSM firmware is trusted", kind: stated}
obligations:
  - {id: O1, statement: "discharge side-channel analysis", discharged: false, kind: stated}
```

### `threats` — threats / weaknesses / vulnerabilities described

Threat scenarios (`actor`, `capability`, `attack_vector`, `affected_asset`) and
`weaknesses`/`vulnerabilities` entries carrying an external id (CWE/CAPEC/CVE) as
an **opaque string** plus a description. These are the **extracted descriptions**
of what the source says. A consuming threat-model knowledge graph (its
`ThreatInstance` / `Weakness` / `Vulnerability` / `Mitigation` objects) consumes
them **by opaque id** — the link runs consumer→library and lives in the
consumer. This family models none of the KG: no product instantiation, no risk
vector, no mitigation state.

```yaml
schema: library-threats/v1
record: <record-id>
threats:
  - id: T-spoof-update
    name: "Spoofed software update"
    description: "an attacker serves a forged update package"
    actor: "network adversary"
    capability: "can intercept and modify update traffic"
    attack_vector: "man-in-the-middle on the update channel"
    affected_asset: ["update client", "installed artifact"]
    external_id: "CAPEC-186"          # opaque — not resolved by the checker
    locator: "§5.1"
    kind: stated
weaknesses:
  - {id: W-missing-sig-check, external_id: "CWE-347",
     description: "improper verification of cryptographic signature",
     locator: "§5.2", kind: stated}
vulnerabilities:
  - {id: V-example, external_id: "CVE-2023-00000",
     description: "unauthenticated update endpoint in FooUpdater 1.2",
     affected: "FooUpdater 1.2", weakness_ref: "CWE-347",
     locator: "§5.3", kind: stated}
```

### Open scope question — `agents`

`agents` was **named by the sponsor**, and the precise scope is left open for
review. As drafted it captures an actor/agent role the *source document*
defines (identity, role, capabilities, autonomy, trust assumptions). Two
boundaries need a decision before the first extraction:

- **autonomy vocabulary** — `human-directed` / `supervised` / `semi-autonomous`
  / `autonomous` is a provisional placeholder, not drawn from a ratified source.
- **overlap with `object-model` and `protocol`** — a source that already models
  its actors as object-model objects or protocol roles should not have them
  re-extracted here. Is `agents` only for sources whose *subject* is agents
  (agentic-AI threat docs), or any source that names actors? The draft assumes
  the former; a reviewer should confirm.

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
