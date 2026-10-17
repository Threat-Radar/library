---
record: open-threat-model
kind: verification
title: "open-threat-model — FX-1 pass 2 (verify) and pass 3 (cross-check)"
extracted: "2026-10-14"
reviewed_by: ""
---

# Verification: Open Threat Model 0.2.0 extraction

Agent C, independent of the pass-1 extractors (agents A and B and the
coordinator), at maximum effort, 2026-10-14 and 2026-10-16. Sources:
`iriusrisk/OpenThreatModel` at `c88c5a7b`, re-hashed before use, all matching
the recorded digests: `README.md` (`4acfb48b…ef78cf8c0`, 2,034 lines),
`otm_schema.json` (`81e7f5a5…545eef0c`, 308 lines), `EXAMPLE.json`
(`045667cd…387b`), `EXAMPLE.yaml` (`d78f4282…a2761`) and `CONTRIBUTING.md`
(`fa5dbac4…2eefa2`). The clone was clean; its git history was read, never
written. Every check ran from my own scripts (Python 3.14.3 run with `-I`,
PyYAML 6.0.3, jsonschema 4.26.0), not the extractors'. They are scratch files,
not committed. Tools also used: `bin/bcp14-count`, `bin/_bcp14.py`,
`bin/validate`, `bin/check-artifacts`.

The protocol artifact is not applicable (pure data format), as declared.

## Pass 2: verify

### 1. Keyword recount

- **Upper case.** `bin/bcp14-count` on README.md gives 51 (REQUIRED 50,
  RECOMMENDED 1). The schema, CONTRIBUTING.md and both EXAMPLE files give 0.
  LICENSE gives 2, the disclaimer "MAY NOT APPLY TO YOU" at L327 and L337,
  correctly not counted. `_bcp14.count` over all 287 requirement texts gives
  51; no text holds two. The header's 51 = 51 holds.
- **Lower case, rescanned on my own** (case-insensitive, longest match first,
  all twelve keyword forms). README.md: 16 hits (may 4, must 2, optional 1,
  required 3, should 6). otm_schema.json: 20 (`required`, one per required
  array). CONTRIBUTING.md: 2 (should L47, may L60). EXAMPLE.json and
  EXAMPLE.yaml: 1 each.
- **`keyword_accounting`** has 87 rows (67 README, 20 schema). Every row
  matches one of my hits by file, line, 1-based column and word, and none of
  my README or schema hits is missing. I mapped each hit to the requirement
  texts whose source span contains it. For all 67 README rows the
  `as`/`in_text_of` targets equal that set exactly, and each extracted row's
  target carries the keyword as its verb. For all 20 schema rows, `as` lists
  exactly the names of that required array, at its line and column.
- **Defect, fixed** (requirements.yaml `reconciliation`): the lower-case
  paragraph omitted the two EXAMPLE hits. Both are the example value
  `state: required` (EXAMPLE.yaml L164, EXAMPLE.json L220); they are now
  listed as excluded. No count changes.

### 2. Verbatim text and locators

Method for requirements:

- A README text must be a whitespace-normalised, contiguous substring of
  README.md that starts on its locator line. A text inside one line must be
  byte-exact. The locator's heading path and Field cell must equal my own
  README model: heading nesting, plus the first `<td>` of the HTML row or the
  first cell of the markdown row.
- A schema text must be the verbatim member at its JSON pointer, key through
  value, starting on the locator line. I parsed it with my own
  position-tracking JSON parser. The verb must follow from the member: type,
  type-nullable, required, required-in-branch, ref, one-of or dialect. For a
  required entry, the field must be the name at that index.
- I tested both checkers with planted errors. The README checker caught all 7:
  a splice, a wrong line, two tidied quotes, a tidied range, a wrong Field cell
  and a wrong heading path. The schema checker caught all 5: a wrong line, a
  tidied space, a wrong verb, a wrong field name and a tidied multi-line
  member.

Results:

- **requirements.yaml: 287/287 pass.** README texts: 109, five spanning
  lines (R-0021, R-0059, R-0071, R-0094, R-0095). Schema-located texts: 178,
  the `$comment` licence entry R-0111 included; six span lines (R-0250,
  R-0283 to R-0287). These are exactly the 11 multi-line texts the header
  lists.
- **Order and counts.** README entries are in source order (line, column,
  stated before inferred), and schema entries too (line, column, array
  order). Ids run 1 to 287 without a gap. Every figure in `counts` reproduces
  (by form, kind, verb, actor and testable). `testable_reason` is present
  exactly when testable is not yes, and `inferred_rule` exactly when the kind
  is inferred. Every `related` pair is symmetric, and every R- or D-id cited
  in a note resolves.
- **Schema notes.** Every REQUIRED or RECOMMENDED row's note says "Schema:
  required (R-nnnn, otm_schema.json Lnn)" or "not required (… Lnn)". All 51
  claims are right: id, field, array line and `related`.
- **normative.md.** All of these equal the README:
  - 56 bullet quotes, each on its locator line, with the ids and verbs of the
    requirements located in its span;
  - all 118 table rows: 109 field rows (Field, Type and Description cells,
    the Description line or range, and the extracted ids and verbs) and 9
    Data Types rows;
  - 86 Examples-column blocks, dedented as stated;
  - 23 `#### Example` ranges, fences included.

  The schema part also holds: 167 member quotes at their lines with the right
  ids and verbs, every schema requirement id present, and every section's
  line range. The keyword totals are also right: type 119, required 20,
  properties 20, items 21, $ref 10, oneOf 1, definitions 1. The 109
  comparison rows have the right type cell, keyword and required status.
  D-01 to D-32 are identical to `requirements.yaml` `source_defects`. Planted
  errors: 5 of 5 caught. The "README fields by type" tallies match my own
  count of the Type cells.
- **Other files.**
  - state-machine.yaml: 20 quotes, all verbatim at their README or
    CONTRIBUTING locators.
  - design-notes.md: 20 quotes. 7 are from README.md and 9 from the LinkML
    model. One each comes from ADR-0010, ADR-0006 (rendered text, bold
    removed) and the RPT-0005 report. The last is the subject of commit
    06288a0.
  - messages.yaml: the `statement` texts are verbatim.

### 3. Section walk for dropped statements

- **README.** I read all 2,034 lines. Every one of the 51 keyword cells is
  extracted, and so is every lower-case modal that directs an actor. Every
  "Unique identifier" id (11), every range (7) and every reference rule are
  extracted too, as are the default (L1404), the Data Types rules, the
  versioning rule and the licence footer. I also checked coverage
  mechanically: each of the 56 README prose lines outside tables, code and
  headings is inside a normative.md bullet quote. Each of the 86 non-empty
  Examples cells and each of the 23 example blocks has an entry. The version
  block L17–L19 is a bullet. **No dropped statement.**
- **Schema.** My own schema walk tells keywords from property names. It finds
  177 constraint keywords: 58 type, 61 type-nullable, 44 required, 2
  required-in-branch, 10 ref, 1 oneOf and 1 $schema. That is exactly the
  177 schema entries. It raises on any keyword outside that set plus `$id`,
  `title`, `$comment`, `properties`, `items` and `definitions`; none occurs,
  which confirms the absence of `enum`, bounds, `pattern`,
  `additionalProperties` and the rest.

### 4. Source defects and mismatches, re-derived

I re-derived each of D-01 to D-32 from the source and checked every cited
line. These were mechanical:

- the null-admitting required fields (D-03);
- every non-nullable optional property (D-09);
- the EXAMPLE lines of D-19 and D-30;
- the no-break space at L1735 (D-29), the README's only one;
- LICENSE L1 (D-31).

All 32 are real. Two are incomplete:

- **Defect, fixed (D-09)**, in requirements.yaml and normative.md, which are
  identical. D-09 said trust zone `type` and `impactComment` are the only
  optional strings that reject null. It missed the Parent object's
  `trustZone` and `component` (schema L229, L230), which are optional outside
  their oneOf branch and typed "string". It also missed a trust zone's
  optional `parent`, which refs the Parent object typed "object" (L92, L223).
  jsonschema confirms that both nulls fail. The finding and its lines are
  amended. The notes of R-0165, R-0170, R-0253 and R-0254 now say the same.
- **Defect, fixed (D-32)**, in both files. Three typos in normative text were
  missing:
  - "within an OTM files" (L33), which R-0009 quotes verbatim;
  - "Array of mitigation" (L1756);
  - "a very basic information" (L1951).

  One example typo was also missing: "Creditcard … data base" (L1481).

I re-derived M-01 to M-16 the same way. All are real.

- **Defect, fixed (M-10)**, in messages.yaml. It has the same omission as
  D-09; the schema and effect texts are extended.
- **Defect, fixed (M-16)**, in messages.yaml. It counted "11 id-valued
  reference fields (unchecked_references)", but that list has 12 entries: 10
  in-document id references plus the external `cwes` and Repository `url`.
  The text is reworded.

No further defect was found. Candidates I examined and left out are below.

- The bare-URL Examples cell for Repository `url` (L1935) is already recorded
  in messages.yaml and in the field vector FE-082.
- In examples, ids are fragment-local across different README blocks.
- The naming differs between "Open Threat Modeling Format" (L3) and
  "Open Threat Model specification" (L15).

### 5. messages.yaml

- **Structures and fields.** I rebuilt all 26 structures and 120 field
  entries from my own README, schema and EXAMPLE.json models, and every
  attribute matches. For structures that is heading, line, section range
  (to the end of its last example block) and prose lines. For fields:
  - README type (rendered), keyword, name line, keyword line and Description
    lines (`<td>` line to `</td>` line);
  - schema pointer, key line, type after `$ref`, ref and ref line, items,
    required status (yes, oneOf or no) and constraints;
  - EXAMPLE.json of, present, null and lines, with variants selected by
    `type` or by the referenced representation's type.
- **Other claims.** EXAMPLE.json has 22 nulls, as `counts` says; it is ASCII
  only, with LF line ends and 2-space indentation. The identifier-style
  examples sit at the lines cited. The git facts (`last_changed` 355287f and
  06288a0) reproduce.

### 6. Examples

- **Fixture set.** The 49 files on disk are exactly the 49 vectors, and every
  SHA-256 and size matches.
- **Verbatim fixtures.** For the 23 README fixtures, the README byte range
  [start, end) reproduces the fixture, the lines match the bytes, and the
  fences sit at lines start−1 and end+1. EXAMPLE.json and EXAMPLE.yaml are
  byte-identical to the source.
- **Derived fixtures.** For each of the 24, a unified diff against its base
  (n=0) equals the recorded `diff` exactly.
- **Validation.** I re-ran every fixture with a `$ref` mechanism different
  from the extractors': a `referencing` registry keyed by a URN, and
  `{"$ref": "<urn>#<pointer>"}`. Three schemas were used: the source, the
  strict profile and the tag-0.2.0 schema (`git show 0.2.0:otm_schema.json`,
  SHA-256 `bf3a9703…b18a`). Results:
  - every validity, error count and error tuple matches (instance path,
    keyword, schema path and message), every `secondary` check included;
  - source 32 valid / 17 invalid; strict 22 / 27;
  - 42 fixtures match their expectation, as recorded.
- **Undeclared keys.** I re-derived `undeclared_keys_accepted` with my own
  schema walk; it matches on all 49.
- **Derived checks.** I implemented XR-01 to XR-10 from `messages.yaml`
  `derived_checks`. On the 26 whole documents every pass and fail matches,
  with failures exactly where designed: XR-01, XR-02 (`trustZones: null`),
  XR-05, XR-08 and XR-10.
- **Cross-fixture assertions.** X-01 to X-05 hold. X-03's two differing
  fixtures reproduce against the tagged schema. Planted errors in a copy of
  expected.yaml: 4 of 4 caught (a digest, an error message, an XR result and
  a diff line).
- **Field vectors.** All 86 texts equal the README cells, dedented, each
  cell whole, and every SHA-256 matches. 85 parse. FE-023 really is invalid
  YAML. FE-073's only key really is `\xa0threat`. 84 are valid under both
  schemas.
- **examples/README.md.** The 49 table rows (size, lines, results and XR)
  equal expected.yaml. The documented re-run prints "49 fixtures, 0
  differences", and the byte-range command reproduces the TrustZones digest.

### 7. Schema directory

- **Source copy.** `schema/otm_schema.json` is byte-identical to the source
  (`cmp`). The schema/README.md facts reproduce: 11,549 bytes, ASCII only,
  101 property declarations, the history commits, the LICENSE commit d226d5b
  (2024-11-20) and the 302-line tag file.
- **Strict profile.** It passes `Draft7Validator.check_schema`, and its size
  (20,959 bytes), SHA-256 and missing `$id` are as stated. A structural diff
  against the source finds changes at exactly the 36 S-pointers, each with a
  `$comment` naming its id. The 23 type changes all narrow (integer for
  number, null removed), and nothing is relaxed.
- **README support.** Every S-nn cites README lines that carry its basis: the
  integer type, "From 0", "signed 32 bits", "`null` is not supported",
  "array of", "Map", "By default, it is false.", REQUIRED, the three
  representation types, and L15/L55 for semver. The schema/README.md table
  equals `strict_additions` row for row.
- **Defect, fixed** (schema/README.md). It said "Every JSON pointer of the
  source schema exists unchanged", but `/$id` is removed and `/title` and
  `/$comment` are rewritten, all of them annotations. It now says
  "constraint-bearing" and names the three.

### 8. State machine

- **States.** All 17 observed-value citations are right. A scan of every
  `state:` value in README.md, EXAMPLE.json and EXAMPLE.yaml finds no
  occurrence the file omits.
- **Git facts.** These reproduce from the source history:
  - tags 0.1.0 (4147643, 2023-08-29) and 0.2.0 (6bcb2ab, 2023-08-30);
  - commits 355287f and 06288a0, with their subjects;
  - the `$id` before and after 355287f;
  - both schema digests;
  - that only `representations` and `assets` lacked `items` at the tag.

## Pass 3: cross-check

- **Names resolve.** Every object a requirement names is a messages.yaml
  structure, or one of Versions, Format, Data Types, (document) and (schema).
  Every field it names, the variant's included, exists in messages.yaml and
  as a schema property. The four `variant` values are structure names.
- **`constrained_by`.** I recomputed every link from the stated method.
  - It reproduces 275 linked and the same 12 unlinked: R-0001, R-0006 to
    R-0014, R-0109 and R-0111. The reasons are accurate, and all 120 fields
    carry links.
  - No requirement links to the wrong variant. A diagram-element rule never
    reaches the code or threat-model variant.
  - **Defect, fixed**: R-0034 (L480, the code element's "at least one of them
    is required") was linked only to the generic RepresentationElement
    object, never to its own variant. It is now also on Representation
    element for code. The linked count is unchanged.
  - **Defect, fixed**: the method text did not describe the rule the links
    follow. Variant rows also link to the shared field of the structure their
    `object` names. The text is rewritten. With it, the recomputation matches
    every link except the documented whole-document case R-0002 to R-0005.
  - **Defect, fixed**: `conventions.constrained_by` still read "placeholder".
- **Stated or inferred.** messages.yaml marks the references of the
  representation element, data-flow endpoints, asset instances and `cwes` as
  `stated`, and XR-04 to XR-06 too. requirements.yaml marks the same rules
  `inferred` (R-0029, R-0036, R-0040, R-0053, R-0054, R-0081, R-0083,
  R-0088). Both are right under their own meaning. messages.yaml records
  whether the README names the target; requirements.yaml whether the
  must-resolve rule is stated, and it never is.
  - **Defect, fixed**: the two meanings were undefined. They are now written
    into `conventions.references` and the `derived_checks` note. No value
    changed.
- **State machine.** All four events are defined, and every trigger is one of
  them. Every from and to state exists in its machine. The cited fixtures
  exist and fail as stated.
- **Examples against both schemas.** EXAMPLE.json and EXAMPLE.yaml are valid
  under both schemas and under the tag-0.2.0 file, and pass all ten derived
  checks. Every fixture validates or fails exactly as recorded.
- **design-notes.md against the source and tmodel.**
  - The OTM claims and line citations hold, with the exceptions below.
  - The tmodel claims hold against ADR-0010, ADR-0007, ADR-0006, ADR-0004,
    ARCH-0001 (R-005, R-010, R-018, R-020 and R-021; DEC-009 open) and the
    LinkML model. Those files are byte-unchanged from `cd02eff` to
    `9f56628` (`main` on 2026-10-16). The checks covered class and slot
    names, ranges, `MethodFacet`, `MitigationStatus` and every quote.
  - G13's first sentence is verbatim. The converters paragraph matches
    RPT-0005 `fanout-models-requirements.md` §8.1 and §8.2.
  - **No sentence proposes adding a class.** L242 proposes an import policy
    (a warning plus a finding), not a class.
  - The substantive fixes are listed below.
- **Index.** distilled/README.md coverage lines checked against the
  artifacts. **Defect, fixed**: the examples line said "7 README examples are
  invalid as published (D-25 to D-30)". In fact 6 fail the source schema
  (D-25 to D-28) and 1 fails only the strict profile (D-07). The design-notes
  line lacked R-020 and the G13 direction. The passes line is now dated.
- **Pass status.** requirements.yaml (`note`) and normative.md (header) said
  that the verify and cross-check passes had not run. Both now point here.
  normative.md's notation bullet now says that `(L<n>)` is a schema line
  inside the schema sections.

### design-notes.md: substantive changes

1. **G13.** The notes called closing the gap "the sponsor's decision" only.
   The report's G13 row now records the sponsor's direction of 2026-10-14
   (RPT-0005 commit 1db50e7, after the notes were written): add the classes;
   accepting them needs an ADR amending ADR-0010. The notes now record this.
   They still make no proposal. The mapping rows and open question 2 follow.
2. **Open question 4.** The notes said each top-level array lacked `items`
   before 06288a0. Only `representations` and `assets` did. Corrected.
3. **Adopt 2.** "ADR-0010's own rule: never present unreviewed output as
   reviewed" is not ADR-0010's wording. The ADR says "never present AI
   output as reviewed"; the notes now quote it and call the import rule an
   extension of it.
4. **Adapt 5.** The README examples use `required` (L1495) as well as
   `implemented`; the notes said only EXAMPLE.yaml has `required`.
5. **Identifiers.** "Only `Component` has a slot for an external id" is now
   scoped to the classes an import fills (Product and ProductInstance have
   one too). "Cannot carry its OTM id" is now "has no slot for", with
   `Mitigation.external_refs` ("Linked work items, e.g. a Jira key") named.
6. **`attributes`.** The notes said `attributes` is on every object; it is on
   9 structures.
7. **Decisions header.** It now records that the decision files are
   unchanged at `9f56628`.

## Gate

- `bin/validate`: 0 errors over 464 records, and nothing reported for this
  record.
- `bin/check-artifacts`: 0 parse failures and 0 structural errors over 166
  files, and nothing for this record.
- `record.yaml` has no `distillation` block yet, so I simulated `check_full`
  with `profile: full`, protocol declared not applicable and three passes at
  max effort: 0 errors.
- No artifact holds a TODO marker. The library parser reads the folded
  `reconciliation` as its full text, unlike the cwe case.

## Residual issues

- **`distillation` block.** `record.yaml` still needs its `distillation`
  block (profile full, artifacts, protocol not applicable, passes) and a
  status change. That is the coordinator's step, and it should list
  `verification.md`.
- **G13 can go stale.** The sponsor's direction lives on the RPT-0005 topic
  branch, not on tmodel `main`. When the ADR amending ADR-0010 lands,
  design-notes' G13 section, its mapping rows and open question 2 need
  revisiting.
- **Two meanings of "kind".** The two files classify reference rules
  differently. This is now defined, not unified; a reviewer may prefer one
  vocabulary.
- **The 0–100 quote.** design-notes *adapt* 1 quotes "From 0 to 100" for all
  seven risk fields. It is verbatim at five of them; L825 and L1266 read
  "From 0 to a 100" and "From 0 and 100" (D-32).
- **One link text.** The link text "Representation Element object" (L994,
  L1186) differs in spacing from the heading "RepresentationElement object".
  `readme_link_notes` records the case and anchor differences, not this one.
