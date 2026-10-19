---
schema: "library-verification/v1"
id: osv-schema-verification
record: osv-schema
type: verification
updated: "2026-10-19"
by: "claude (independent verify agent, did not extract); claude (cross-check agent, pass 3)"
reviewed_by: ""
passes:
  - verify
  - cross-check
scope: full
attribution: "Contains text from the OSV Schema v1.9.2 (github.com/ossf/osv-schema, tag v1.9.2: docs/schema.md, validation/schema.json, proto/vulnerability.proto), licensed under the Apache License, Version 2.0"
---

# osv-schema: FX-1 verification

Contains text from the OSV Schema v1.9.2 (github.com/ossf/osv-schema, tag v1.9.2), licensed under the
Apache License, Version 2.0.

## Pass 2: verify

By claude, an independent verify agent that took no part in pass 1. Effort: max. Begun 2026-10-18,
finished 2026-10-19. Scope: every file under `distilled/`; `record.yaml` and `summary.md` were read, not
edited. The job was to break the extraction: recount the verbal forms, check every quotation and locator
against the three source files, look for dropped statements, check the classification of every
requirement, re-run every schema and example check, and test every claim about tmodel.

### Method

- **Source identity.** The three pinned files were hashed before and after the pass and did not change:
  `docs/schema.md` SHA-256 `96d82f03…cebff` (2010 lines), `validation/schema.json` `15b10dbb…2653`
  (584 lines), `proto/vulnerability.proto` `1c5a7af8…a070` (234 lines), all at tag `v1.9.2`.
- **Independence.** Own scripts only, kept in the session scratchpad and not committed. No pass-1
  script, working file or output was used as evidence. The fixture runner was run as its README says,
  and its results were then recomputed separately.
- **Allowed normalisation.** A line break inside a passage, with the spaces or tabs around it, is
  joined as one space; spaces inside a line are kept (the source has double spaces after some full
  stops). Under this join a quotation cannot run across a blank line, so two spliced paragraphs cannot
  match. Proto comments are joined with their `//` markers removed, as `normative.md` and
  `messages.yaml` declare.
- **Locators.** A heading map built from the 63 headings of `docs/schema.md`, fenced code skipped. A
  quotation counts as located only if it occurs inside the lines its locator names, under the heading
  path it names. JSON Pointers were resolved with a position-tracking parser that gives each value's
  key line and last line.
- **tmodel.** Read only with `git show` at `1cb85b74` (`origin/main`, 2026-10-18 22:25 -0700), the
  commit the design notes cite; nothing was fetched or changed. The `docs/schema.md` of tag `v1.9.1`
  that pass 1 downloaded for the design notes was read as data (SHA-256 `e5b87d62…307e`, as stated).
- **Tools.** Python 3.13.9 with jsonschema 4.26.0, rfc3339-validator 0.1.4, rfc3987 1.3.8, PyYAML 6.0.3
  and linkml 1.12.1; Node v22.23.2; libprotoc 29.3.

### Recount of the verbal forms

Case-insensitive, between non-letters, longest form first. Between the two words of "must not",
"should not" and "may not" a line break or Markdown emphasis is allowed, so `should **not**` (L771)
counts once, as should not. An occurrence belongs to the line of its first letter. Regions are those of
`requirements.yaml` `source_normative_counts`.

| region (docs/schema.md lines) | must | must not | should | should not | may | may not | required | shall | total |
|---|---|---|---|---|---|---|---|---|---|
| front matter, version line, authors, # Purpose (1-36) | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 |
| # Format Overview, with the informal schema (37-112) | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| # Field Details, ## schema_version field (113-133) | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 2 |
| ## id, modified fields, with the prefix table and ### modified field (134-725) | 1 | 1 | 4 | 0 | 0 | 0 | 2 | 0 | 8 |
| ## published field (726-736) | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 |
| ## withdrawn field (737-749) | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 2 |
| ## aliases field (750-779) | 0 | 1 | 2 | 1 | 0 | 0 | 0 | 0 | 4 |
| ## upstream field (780-798) | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 2 |
| ## related field (799-813) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| ## summary, details fields (814-838) | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 |
| ## severity field, with the type and source tables (839-887) | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| ## affected fields, introduction (888-947) | 1 | 0 | 1 | 0 | 2 | 0 | 0 | 0 | 4 |
| ### affected[].package field and the ecosystem table (948-1049) | 6 | 0 | 2 | 0 | 2 | 0 | 2 | 0 | 12 |
| ### Depicting multiple ecosystems in the same record (1050-1066) | 0 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 4 |
| ### affected[].severity field, ### affected[].versions field (1067-1084) | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 2 |
| ### affected[].ranges[] field, ### affected[].ranges[].type field (1085-1130) | 0 | 0 | 1 | 1 | 1 | 2 | 1 | 0 | 6 |
| ### affected[].ranges[].events fields (1131-1187) | 2 | 0 | 2 | 0 | 3 | 0 | 1 | 0 | 8 |
| ### repo, ranges database_specific, ecosystem_specific, affected database_specific (1188-1241) | 0 | 0 | 3 | 0 | 1 | 0 | 1 | 0 | 5 |
| ### Evaluation (1242-1293) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| ### Examples under affected fields (1294-1415) | 0 | 0 | 0 | 1 | 3 | 0 | 0 | 0 | 4 |
| ## references field (1416-1456) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| ## credits fields (1457-1526) | 2 | 0 | 3 | 0 | 0 | 0 | 1 | 0 | 6 |
| ## database_specific field (1527-1540) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| # Examples (1541-1996) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| # Appendix, ## Android SoC Vendors (1997-2010) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **whole document (1-2010)** | **14** | **3** | **29** | **3** | **15** | **2** | **8** | **0** | **74** |

`bin/bcp14-count` on `docs/schema.md` gives **0**: the source has no uppercase BCP 14 keyword. The
uppercase "NOT" of "does NOT remove" (L1127) is emphasis, not a keyword.

| quantity | this recount | where it is recorded | result |
|---|---|---|---|
| must, must not, should, should not, may (may not folded in), required, shall | 14, 3, 29, 3, 17, 8, 0: 74 | `requirements.yaml` `source_normative_counts` | equal, in total and in each of the 25 regions |
| the same words counted plainly | must 17, should 32, may 17, required 8 | `source_normative_counts.total.plain_word_count`, and the brief | equal |
| occurrences by line and form | 74 of 74 | `keyword_accounting` | equal, line for line and form for form; each "extracted as" entry's located text contains that occurrence |
| forms inside entry texts, recomputed from the located text spans | must 13, must not 3, should 29, should not 3, may 12, required 8: 68 | `extracted_normative_counts.in_text` | equal |
| excluded occurrences | must at L110; may at L29, L791, L1146, L1371 and L1379: 6 | `extracted_normative_counts.excluded`, `keyword_accounting` | equal; each exclusion is right (the format's change policy, a design rationale, two example sentences and two statements of possibility) |
| repeats | 0 | `repeats_listed_in_also_at` | equal: no sentence that carries a form occurs twice in the source |
| BCP 14 keywords | 0 | `source_keyword_count` 0, `extracted_keyword_count` 0 | equal |
| `normative.md` tally | must 14, must not 3, should 29, should not 3, may 15 (11 in statements, 4 excluded), may not 2, required 8 (one of them "not required"): 74 | `normative.md`, Verbal form tally | equal; the form tags of all 317 prose statements equal my matcher's, statement by statement |
| recommended, optional, optionally, allowed, permitted, mandatory, encouraged, invalid, preferable, preferred, cannot | 43 | `supplementary_wordings` | equal, line for line |

Both pass-1 tallies therefore equal this recount. They differ only in where one "may" sits:
`normative.md` numbers "This may be useful if the scope of a vulnerability entry is limited to a small
set of linear branches." (L1371) as statement N-0273 and so excludes four occurrences, while
`requirements.yaml` excludes that sentence as a statement of possibility and so excludes five
occurrences (68 + 6 = 74). Each file is consistent with itself; neither is a counting error.

### The four JSON Schema readings the coordinator asked about

All four are source defects, disagreements between `docs/schema.md` and `validation/schema.json`,
confirmed with jsonschema 4.26.0 on the pinned file:

- **CLEANSTART.** The prefix table prints `CleanStart` (L277), the same row's OSV Formatted URL spells
  `CLEANSTART-YYYY-<ID>.json` (L283), and `/$defs/prefix/pattern` lists only `CLEANSTART`. An id
  `CleanStart-2026-1` fails the schema; `CLEANSTART-2026-1` passes.
- **FreeBSD.** The pattern accepts the prefix `FreeBSD`, and the table (L179-L710) has no FreeBSD row;
  FreeBSD is only an ecosystem (L1006). `FreeBSD-2026-1` passes. Apart from these two names, the 59
  prefixes of the table equal the 60 of the pattern once `SUSE-[SRFO]U` is expanded.
- **GIT.** `/$defs/ecosystemWithSuffix/pattern` ends `|GIT)(:.+)?$`, so `GIT`, and `GIT:` with any
  suffix, pass as `package.ecosystem`. The table (L988-L1042) does not list GIT, the ecosystem "must be
  one of the strings in the table below" (L954-L955), and a Git entry "should use **no** `package`
  field" (L1059); yet the prose also speaks of entries using `GIT` "ecosystem" (L1065) and of "the
  `GIT` pseudo-ecosystem" (L1081), so the prose itself is unsettled. The unreferenced
  `/$defs/ecosystemName` enum equals the 52 table names, in order.
- **limit "*".** In a GIT range `allOf/1` applies `^(0|[a-f0-9]{40}|[a-f0-9]{64})$` to every event
  value, so `{"limit": "*"}` fails, although "`limit` allows versions containing the string `"*"` to
  represent "infinity"." (L1153) and an implicit `{ "limit": "*" }` is assumed (L1154-L1155). The same
  event passes in a SEMVER range. The pattern also admits `"0"` for `fixed`, `last_affected` and
  `limit`, where the prose gives `"0"` a meaning for `introduced` only (L1151-L1152).

Every artifact that states these defects states them as above: `normative.md` D-3, D-4 and D-10;
`requirements.yaml` R-0019, R-0227, R-0229 and R-0230; `schema/README.md` D6, D21 and D28;
`messages.yaml`; the examples' findings F-02, F-08 and F-11; and design-notes defects 5, 6 and 9.

### Defects found

Severity: **material** means a wrong or dropped requirement, a wrong count, a non-verbatim quotation,
a wrong verdict or a false claim; **minor** means a locator, wording or format. Every fix keeps the
source's text verbatim, and no requirement `text` changed.

1. **Material. `examples/`: 180 stray copies.** 176 files named like `pos-02-base.derived 2.json` and
   `edge-01-ecosystem-git.derived 3.json` sat beside the fixtures in `examples/osv-records/` (311 files
   where the README counts 135 records), and four empty folders `verbatim/blocks 2`, `blocks 3`,
   `inline 2` and `inline 3` beside `verbatim/blocks` and `verbatim/inline`. All were dated 23:53 with
   owner-only permissions, apparently copies left by file synchronisation while pass 1 rewrote its
   files. Each copy was byte-identical to its original and no artifact referred to one, but
   `distilled/` is untracked, so committing the folder would have added them. Fix: moved, not deleted,
   to the session scratchpad with their paths kept. The record now holds 239 files, 135 of them
   derived records.
2. **Material. `requirements.yaml` R-0019: a dropped value set.** The lead-in "The defined database
   prefixes and their "home" databases are:" gave the 47 Prefix cells only as a paraphrased list in its
   notes, while every other value-set lead-in (R-0052, R-0081, R-0163, R-0209, R-0220, R-0224) carries
   its values as a verbatim `enumeration`, and R-0018 ("from the defined database prefixes below") and
   R-0230 depend on this set. Fix: an `enumeration` of the 47 cells, verbatim (the inner HTML of each
   row's first cell, L189 to L695: 59 prefixes in all, `CleanStart` included), the locator widened from
   L174 to L174-704 as for the other lead-ins, and the notes rewritten.
3. **Material. `schema/osv-prose.derived.schema.json`: a wrong verdict.** P10 belongs to the profile
   whose failures are errors ("stated rules"), yet it rejected the wildcard name `*` for PyPI, Linux,
   Maven, VSCode, GitHub Actions and `WordPress:Core`, although "Use the wildcard package name `*` to
   indicate that an advisory affects all packages within the specified `ecosystem`." (L959-L960) names
   no ecosystem. The examples' wildcard fixture, POS-17, uses npm, which P10 does not constrain, so
   nothing had caught it. Fix: every P10 name form now exempts `*` (P10b needed no change), and P10
   carries a `$comment` that quotes L959-L960. For Linux, whose row says "The only supported `name` is
   `Kernel`." (L1015), the prose does not reconcile the two rules (`normative.md` U-24), and P10a now
   accepts both rather than decide. Every other P10 verdict I tested is unchanged, and the nine example
   records give the same results as before. `schema/README.md`: the new SHA-256
   `fdcf554fe30f6632e0717439cca7674ca059145f207196706fda9eec0f8f41be`, the P10 row, reading R11, a
   paragraph on this change, and "Readings R1 to R11".
4. **Material. `requirements.yaml`: a claim the entries did not keep.** The `source_files` entry for
   the proto said "where its comments disagree with docs/schema.md, the entry notes say so", but only
   R-0027 and R-0228 mentioned the proto. Fix: notes that quote the proto were added to R-0025 (no
   "Required." marker on `id` or `modified`), R-0041 ("such as the same problem in alternate
   ecosystems"), R-0044 ("It is recommended to keep this under 120 characters."), R-0160
   (`Affected.ranges` "Required. Range information."), R-0174 (`introduced` "The earliest
   version/commit where this vulnerability was introduced in."), R-0181 (`Event` has four independent
   fields and no `oneof`) and R-0195 (`Range.database_specific` "about the vulnerability"), and the
   header now names the nine entries. A parse of both versions shows that nothing else in those
   entries changed.
5. **Material. `messages.yaml`: library text under a key declared verbatim.** The file's note says that
   every `description` value is verbatim from `docs/schema.md`, but 7 `allowed_values` items for values
   the prose does not define (the proto zero values `UNSPECIFIED` three times, `SOURCE_UNSPECIFIED` and
   `NONE` once each, and `GIT` as an ecosystem and as a reference type) carried the
   library's own words there ("proto3 zero value", "not defined by the prose"). Fix: those 7 keys
   renamed `note`; all 82 remaining `description` values are verbatim.
6. **Material, in notes only. 12 near-quotations.** Source words in quotation marks, with backticks or
   link markup dropped or a capital lowered: 11 edits in `requirements.yaml` notes and header (for
   example 'in the form of the id field' for 'in the form of the `id` field', 'the defined types' for
   'The defined types', 'has a suffix' for 'has a `:<RELEASE>` suffix', 'display code' and 'programs'
   for 'Display code' and 'Programs') and one in `examples/expected.yaml` ("The known reference type
   values" for "The known reference `type` values"). Fix: each made exact. `expected.yaml` still reads
   identically with `bin/_yaml.py` and PyYAML, and the runner still reports 0 problems.
7. **Minor. `requirements.yaml` R-0018** was `testable: "yes"`, but whether an id's prefix is the
   "correctly scoped" one, that of the publishing database, cannot be seen in the record. Fix:
   `partial`, with a reason; `counts.by_testable` updated (yes 108, partial 98).
8. **Minor. `requirements.yaml` R-0097 and the header note.** The header said `verb: imperative` marks
   "the one imperative sentence", but the Debian row, a constraint, ends with an imperative ("use the
   the string in the `series` column ..."). Fix: R-0097's notes say so and why the sentence is not
   split; the header sentence now names R-0077 as the one entry stated only as an imperative and
   points to R-0097, R-0017 and R-0018.
9. **Minor. The prefix table's order.** `normative.md` U-7 lists the rows that break the table's
   alphabetical order but missed `RSEC` before `ROOT` (L607, L618); R-0019's notes, `schema/README.md`
   O5 and the `messages.yaml` note on `id` gave shorter lists in the same form. Fix: all four now list
   ASB-A before ALSA, ALSA before ALPINE, MGASA before MAL, RHSA before RHLW, RSEC before ROOT, and CLSA
   last, the complete set by script.
10. **Minor. `design-notes.md`:** its one two-level locator used "›" between headings, where every
    other artifact uses " > ". Fix: " > ".

### Checked and clean

- **requirements.yaml.** 237 of 237 `text` values verbatim and inside the lines their locators name:
  224 from `docs/schema.md`, each under the heading path named, and 13 from `validation/schema.json`, at
  the pointer and lines named; no splice. 9 enumerations with 140 items and 2 code blocks verbatim. 80
  JSON Pointer references (in the 13 schema locators and in `also_at`) resolve to the lines cited.
  Every table-row locator names the row on its line. `counts` equals the entries; ids run R-0001 to
  R-0237 with no gap; every entry that is not fully testable gives a reason. The statements in notes
  about what `validation/schema.json` accepts or rejects were re-run and hold.
- **Classification.** All 237 entries were read in full for `normativity`, `verb`, `actor`,
  `condition`, `testable` and `kind`. The file applies its declared conventions consistently, apart
  from defects 7 and 8. R-0023 is rightly inferred: no sentence says that a producer must update
  `modified`, though R-0022's definition and R-0024's rule imply it, and its notes say so. No stated
  entry rests on an inference.
- **Dropped statements.** A coverage map shows that `normative.md`'s 384 statements and 75 exclusions
  cover every non-blank, non-structural character of `docs/schema.md`. Of its 317 prose statements,
  74 had no requirement entry before this pass: the 47 prefix rows, which were a gap (defect 2), and
  27 that the requirements file leaves out by its stated rule (2 pointers, the informal schema and 12
  field blocks, 8 explanatory or rationale sentences, the source's invalid example, and the three
  notes that a `*_specific` object is "a single field"). After defect 2, those 27 remain. A
  character-level map of the requirement texts
  over `docs/schema.md` finds nothing else normative left out. Every constraint keyword of the JSON
  Schema is reached by an entry or an `also_at`, apart from bare `"type": "string"` keywords and the two
  unreferenced `$defs`. The proto is not extracted into `requirements.yaml`, by a stated choice;
  `normative.md` carries its 36 statements.
- **normative.md.** 384 of 384 statements: 317 prose statements (191 quoted passages and fences, and
  126 table rows with every cell verbatim within its lines), 31 JSON Schema statements whose values
  equal the parsed schema at their pointers and lines, and 36 proto statements whose lines equal the
  source lines. All 75 exclusions quote verbatim. All 256 short quotations in notes and in the D and U
  lists are verbatim. The 25 D items and 27 U items were tested against the files (D-2, D-3, D-4, D-9,
  D-10, D-11, D-13 and D-15 with jsonschema), and the N-numbers they cite point at the statements
  meant; only U-7 needed a change (defect 9). N-0317 omits the level-1 heading "Appendix" from its
  locator, as the file's own convention says it should.
- **messages.yaml.** 13 structures and 47 fields, as stated. 106 `text`, 44 `source_phrase` and 82
  `description` values verbatim at their locators; 54 `proto_comment` values verbatim in the proto
  comments; 129 double-quoted fragments elsewhere verbatim. 266 JSON Schema and 122 proto line
  references resolve. The allowed values equal the JSON Schema enums and the proto enums with their
  numbers (severity type and source, range type, reference type, credit type, the deprecated commit's
  repo type) and the 52 table names plus GIT. The type, required-ness and proto label of all 47 fields
  agree with the sources.
- **Schema bytes.** `schema/osv.schema.json` and `schema/vulnerability.proto` are byte-identical to the
  pinned files (`cmp`; SHA-256 `15b10dbb…2653` and `1c5a7af8…a070`; git blob ids `13f42fbe…` and
  `9ed3e4ad…`, as the README states). The README's sizes, line counts and character checks hold, and
  libprotoc 29.3 compiles the proto. Both derived schemas pass `check_schema`; their 63 patterns and the
  verbatim schema's 11 compile as ECMA-262 with and without the `u` flag; their 57 quotations of the
  prose are verbatim at the lines cited; the nine complete example records give exactly the README's
  results (valid against both, S06 on all nine, S03 on five, S04 on four, S05 and S09 on one each); the
  sampled smoke cases behave as stated; and the README's 73 quotations are verbatim.
- **Examples.** `run-fixtures.derived.py`, run with `$PY -I` against the scratch copies and again with
  `--schema` set to the committed `schema/osv.schema.json`: "223 fixtures; 46 where a tool differs from
  the expected result (each names a finding); 0 problems", before and after this pass. Recomputed
  separately: the 416 recorded jsonschema results of 208 fixtures, with and without a format checker,
  with their error lists, and every `comparison` label against its expected result. 34 of 34 fenced
  blocks byte for byte, 54 of 54 inline examples on their lines and in order, 133 derived records that
  differ from their parents exactly at the listed pointers, and 108 quoted rules verbatim at their
  lines and headings. The expected verdicts of the 135 derived records follow the prose; the judgement
  calls are the ones the examples README lists.
- **Design notes.** 149 curly quotations, each verbatim in the source it names: 103 in `docs/schema.md`
  1.9.2 (98 of them also in 1.9.1), 9 in the JSON Schema or the proto, 47 in tmodel files at `1cb85b74`,
  and 1 in `record.yaml`; each citation's file, section or line range checked. The decision status
  matches `DECISIONS-0001` v0.1.8 (updated 2026-10-12): DEC-001a, 002, 003, 004, 005, 006, 007, 010 and
  011 accepted by the ADRs named, DEC-001b, 008 and 009 open. ADR-0001 to ADR-0010 (there is no
  ADR-0005) are `accepted` at 1.0.0; APP-0001, ARCH-0001, RPT-0004 and RPT-0005 are drafts; tmodel's
  `CLAUDE.md` does still say "**Every `DEC-*` is open.**". The 40 E11 probes, re-run, give the table's
  results. E12 holds: 1.9.1 differs from 1.9.2 only in the version line, two sections and two
  headings, and RPT-0004 and RPT-0005 both record `15b10dbb…` for the 1.9.1 schema. The tmodel tables,
  rows and vectors the notes cite exist as described (Table 6b's Upstream row, Table 6d's rows, Table
  6f, `mapping.md` §3 with pilot finding 5, `mvp-01`'s `CVE-2026-30111`, `mvp-18`'s
  `vex_not_affected`).
- **state-machine.yaml.** 14 quotations verbatim at their locators; the range-evaluation transitions
  follow the pseudocode branch by branch; the note on comparing timestamps as strings is right
  (`2021-01-01T00:00:00Z` sorts after `2021-01-01T00:00:00.5Z`).
- **YAML.** `requirements.yaml`, `messages.yaml` and `state-machine.yaml` read the same with
  `bin/_yaml.py` and PyYAML once unquoted numbers and booleans are read as strings, the known
  difference; `examples/expected.yaml` reads identically.
- **Validators**, after this pass: `bin/validate` 0 errors, 122 warnings; `bin/check-artifacts` 0 parse
  failures, 0 structural errors, 40 warnings; `PATH="$VENV/bin:$PATH" bin/check-requirements` 47 files,
  0 failures, with no cross-field invariant warning for this record. This record's warnings concern
  `record.yaml` (no content digest, no publisher) and the `protocol.yaml` scaffold.

### Files changed in this pass

`requirements.yaml` (defects 2, 4, 6, 7, 8, 9), `messages.yaml` (5, 9), `normative.md` (9),
`schema/osv-prose.derived.schema.json` and `schema/README.md` (3, 9), `design-notes.md` (10),
`examples/expected.yaml` (6), the stray copies moved out of `examples/` (1), and this file. Unchanged:
the verbatim schema and proto, `state-machine.yaml`, `examples/README.md`, `run-fixtures.derived.py`,
every fixture file, `protocol.yaml`, `protocol.md`, `README.md`, `record.yaml` and `summary.md`.

### Not-applicable declaration

- **protocol.** Not applicable is right, and the coordinator records it. A possible reason: "OSV Schema
  1.9.2 defines one JSON document, the vulnerability record, and no exchange between parties. It names
  producers (databases), consumers, clients and display code and says what each does with a record:
  serve it only as JSON (L105-L107), read a newer minor version by ignoring unexpected fields
  (L129-L132), sanitize details (L833-L834). These are single-party rules, carried by R-0004, R-0008
  and R-0048. The document defines no messages, sequences or error paths between parties; the OSV.dev
  API it links to is outside it; state-machine.yaml models the evaluation of a range and the lifecycle
  of a record."

### Not checked, or left open

- `protocol.yaml` and `protocol.md` are still the scaffold, on purpose. `distilled/README.md` still has
  TODO coverage lines; this pass did not fill them, because they belong with the `distillation` block
  of `record.yaml`.
- No fixture covers an id that is a listed prefix and a hyphen with nothing after it (`GHSA-`): the
  JSON Schema accepts it, and the format `<DB>-<ENTRYID>` (L144) rules it out. Recorded for pass 3;
  this pass added no fixture.
- The `validation/schema.json` of tag `v1.9.1` was not fetched: E12's statement that it equals the
  1.9.2 file rests on the digest RPT-0004 and RPT-0005 recorded. E13's release facts and the tool runs
  behind E1 to E10 were checked as quotations of tmodel's files, not re-run.
- The schema README's 80 smoke cases were not re-run one by one (their scripts were not kept); the
  sampled cases, the nine example records and every pattern were.
- Judgement calls for the human reviewer: the "should" of R-0007, R-0034, R-0039, R-0184 and R-0185
  read as recommendations to consumers, while the "should" inside the definitions of R-0028 and R-0029
  is read as a constraint; R-0173 classified as a requirement, although the "requirement" it refers to
  is stated elsewhere only as a recommendation (`normative.md` U-2); R-0023 kept inferred; the proto
  left out of `requirements.yaml`; the derived schemas' readings R1 to R11 (R1 decides whether P08 stays
  an error, R11 is this pass's); and the examples' judgement calls (GAP-08, definitions read as
  binding, the eleven unspecified EDGE fixtures).
- `record.yaml` and `summary.md` were not edited.

## Pass 3: cross-check

By claude, a cross-check agent that took no part in passes 1 and 2. Effort: max. Date: 2026-10-19.
Scope: `requirements.yaml`, `messages.yaml`, `normative.md`, `schema/` (the two derived schemas and
`README.md`), `examples/` (`expected.yaml`, `README.md` and one new derived record), `design-notes.md`,
`state-machine.yaml`, `distilled/README.md` and this file. `record.yaml`, `summary.md`, `protocol.yaml`
and `protocol.md` were not edited; protocol is not applicable, and the coordinator records it.

### Method

- **Source identity.** The three pinned files were hashed before and after the pass and did not change
  (`96d82f03…cebff`, `15b10dbb…2653`, `1c5a7af8…a070`); `schema/osv.schema.json` and
  `schema/vulnerability.proto` are still byte-identical to them (`cmp`).
- **Independence.** Own scripts only, kept in the session scratchpad and not committed; no pass-1 or
  pass-2 script or working file was used.
- **Edits.** Made by scripts that change only the targeted lines, staged outside the record and written
  into place once (no file deleted). Each edited YAML file was compared before and after with PyYAML:
  every value outside the keys this pass fills is unchanged. `normative.md` was compared with its `req`
  slots masked: only the slots, the `req` convention and the new U-28 differ. `bin/_yaml.py` and PyYAML
  read every edited YAML file the same way, `expected.yaml` outright and the others once unquoted
  booleans are read as strings, as before this pass.
- **Tools.** Python 3.13.9, PyYAML 6.0.3, jsonschema 4.26.0 (referencing 0.37.0), rfc3339-validator
  0.1.4, rfc3987 1.3.8, Node v22.23.2. One unauthenticated request to the GitHub API listed the
  repository root at tag `v1.9.2`, for the licence section of `distilled/README.md`; it carried no
  personal data.

### Check 1: requirements to messages and schema

All 237 entries were checked by their `object` and `field` labels:

| what the labels name | entries | resolves to |
|---|---:|---|
| `messages.yaml` fields, directly | 175 | the field or fields named; R-0004's `encoding` is the encoding of structure `vulnerability` |
| part of a field: an ecosystem suffix, the id prefix, a version ordering or the range events | 33 | `package.ecosystem`, `vulnerability.id`, `range.events` or `range.type` |
| a structure as a whole, every field of a kind, or a relation across records (R-0001, R-0002, R-0008, R-0027, R-0034, R-0039, R-0040, R-0042, R-0145, R-0159) | 10 | the structure, every field of that kind, or the list field that holds the relation |
| the JSON Schema (R-0225 to R-0237) | 13 | their JSON Pointers; all 71 pointers of their locators and of every `also_at` resolve in `schema/osv.schema.json` |
| nothing a record carries (R-0003, R-0020), or informative (R-0150, R-0151, R-0176, R-0221) | 6 | nothing; see check 2 |

No label is wrong and none was changed. In the other direction, every `messages.yaml` field except the
three of the proto-only `Commit` is reached by at least one requirement.

### Check 2: constrained_by wired

- **Rule**, now stated in the `messages.yaml` note. Field level: the requirements whose object and field
  labels name the field (paths into other structures resolved), whose text one of its `rules` items
  quotes, or that are the `description` of one of its allowed values (the ecosystem rows, the severity
  type rows, the range types), kept only where the text reaches the field. A requirement that makes one
  field depend on another is wired on both (R-0031, R-0147, R-0149, R-0154, R-0167, R-0170, R-0173,
  R-0194, R-0202). R-0002 (UTF-8 strings) is on every string-valued field and R-0027 on the twelve
  optional top-level fields. Structure level: the requirements that bind a structure as a whole (its
  definition, member set, one-of rule or entry shape), and R-0008 (unknown members) on every structure
  with defined members.
- **Counts.** 482 links: 428 on 44 of the 47 fields (228 distinct requirements) and 54 on 12 of the 13
  structures (45 distinct); 231 of the 237 requirements are wired. R-0001, R-0004 and R-0237 are on a
  structure only. 25 `constrained_by_note` values explain links that cross structures and candidates
  left out. `constrained_by_locators` is unchanged.
- **Locators.** The pass-1 `constrained_by_locators` give 594 candidate links (requirements whose lines
  lie inside a target's locators): 340 were kept and 254 filtered out (a sibling field's or a member's
  rule, such as the range type rules inside the event fields' locators). 142 links come from outside the
  locators: R-0002 and R-0027, rules in other sections that a label names (R-0143, R-0154, R-0201 and
  others), and the ecosystem rows that speak of versions, purls, `ecosystem_specific` or range events.
- **Requirements that constrain nothing in `messages.yaml` (6).** R-0003 binds a database's internal
  storage, which the document leaves free. R-0020 binds which vulnerabilities a publisher chooses to
  publish, a scope the text does not define and no record shows. R-0150, R-0151, R-0176 and R-0221 are
  informative.
- **`Commit`** (the structure and its three fields) keeps an empty `constrained_by`, with a note: it is a
  deprecated, proto-only message that no field uses (D35), and `requirements.yaml` does not extract the
  proto.

### Check 3: normative.md statements to requirements

Every statement's `req` slot is filled. Prose statements were matched to entries by text (either
contains the other) with an overlap of the cited lines, which removed 11 false matches (a type name such
as `Ubuntu`, `GIT` or `Qualcomm` inside another row, and the "meaning of the values" sentence the source
repeats in four sections). JSON Schema statements were matched by pointer (`locator` or `also_at`).
Nine links were added by hand: N-0234 to R-0174 (its second sentence and list); N-0325 to R-0227 and
N-0341 to N-0344 to R-0232 to R-0235 (the patterns under each `allOf` item); N-0346 to R-0022, R-0028 and
R-0029 (the `format` inside `/$defs/timestamp`, which their `also_at` cite); N-0318 to R-0076 and N-0332
to R-0216 (the same rule in prose).

| outcome | statements |
|---|---:|
| mapped to requirement ids (391 links); 123 table rows and list items carry `(item)`: one item of an entry's `enumeration` | 319 |
| none: a proto statement, since the proto is not extracted; 34 name the prose entry they agree with, add to or differ from, N-0349 (`Commit`) has no counterpart, and N-0373 is the sentence `requirements.yaml` gives as its reason | 36 |
| none: a field block; the types are carried in `messages.yaml` | 12 |
| none: an explanation, rationale, pointer, example or statement of possibility, each quoted or named in the notes or the keyword accounting of the entry given (N-0002, N-0004, N-0005, N-0009, N-0089, N-0134, N-0230, N-0235, N-0243, N-0248, N-0249, N-0266, N-0270, N-0273, N-0316) | 15 |
| none: an unreferenced `$defs` that validates nothing (N-0335, N-0336) | 2 |
| **total** | **384** |

The 27 prose statements with no entry (15 and 12) match the 27 pass 2 counted, category by category. In the other direction,
236 of the 237 requirements are reached by a statement; R-0225 (`"type": ["array", "null"]`) has no
numbered statement and is carried by the table of `type` keywords and by D-11.

### Check 4: examples to requirements

- **Rules.** 109 quoted rules (the 108 of pass 1 and the new `purl-recommended`): 100 carry the ids of
  the entries whose text they quote (103 distinct ids); 9 have none, each with a `requirements_note`:
  the Format Overview rationale (`customizations`) and eight narrations of the range examples, which
  `requirements.yaml` does not extract. `modified-format` carries R-0022 and the inferred R-0023, which
  rests on the same sentence.
- **Negatives.** Each of the 96 `violates` items of the 84 fixtures expected invalid (34 NEG, 41 GAP, 3
  EMB, 3 SRC, 2 TOOL and EDGE-05) carries `breaks` (120 links, 59 distinct ids): the rule's own ids, and
  the JSON Schema entry that states the same constraint when the JSON Schema also rejects the change (17
  links: R-0226 once, R-0227 six times, R-0229 three, R-0230 two, R-0233 one, R-0235 one, R-0236 three).
  Each of the 17 was confirmed against the error jsonschema records for that fixture, or, for TOOL-01
  and TOOL-02, against the recorded ECMA-262 result. 5 `breaks_note` values explain a list.
- **Positives.** Of the 115 fixtures expected valid, every record (the positives, the broken
  recommendations, the reverse gaps, the valid source examples, EDGE-11 and TOOL-03) is valid under
  `osv-prose.derived.schema.json` (P01 to P12) and under checks of my own for stated rules no schema
  expresses: the id format, the neutral id, list items in the form of an id, an id that names itself as
  upstream, a one-line summary, and a `versions` list beside a GIT range. The one exception is SRC-L1635
  under the reading that R-0173 is a requirement, which its `readings` record (F-23). `osv.schema.json`
  rejects only the three OVER fixtures (F-02, F-08), and TOOL-03 with a format checker (F-05). The 37
  inline id, ecosystem and version examples pass the stated rules that apply to them; the other inline
  values, package objects and range fragments agree with the subschemas the runner validates them
  against.
- **Added and changed.** GAP-41 (`GHSA-`, a listed prefix and its `-` with no entry id; it breaks R-0010
  and the JSON Schema accepts it, finding F-01), as pass 2 suggested; the rule `purl-recommended` (L967,
  R-0079); EDGE-05 changed from unspecified to invalid (check 7, item 5); `purl-recommended` in the
  `breaks_should` of the nine complete source examples (check 7, item 6); two conventions added and the
  `requirements` convention rewritten; F-01 and S-15 extended; `examples/README.md` updated to match.
- **Runner.** `run-fixtures.derived.py`, run with `$PY -I` and `--schema` and `--source` set to the
  pinned copies, and again with `--schema` set to the committed `schema/osv.schema.json`: "224 fixtures;
  47 where a tool differs from the expected result (each names a finding); 0 problems".

### Check 5: design notes to requirements

262 requirement ids (135 distinct; 210 counting the ranges in the mapping table) were added on 191 lines,
beside the locators of the passages the text rests on: the Adopt, Adapt and Reject items, the mapping
table, the source defects, the E11 probe table and open questions 8, 9 and 13. The convention bullet now
says what an id beside a locator means. A script checked that every id exists and that its lines
overlap the lines cited with it; the five ids written after a bare line reference were checked by hand.
All 149 curly quotations are unchanged, and one was added (open question 13). Quotations without an id
have no entry of their own: the Format Overview rationale (L109-L111), the sentence that explains
aliases (L759-L761), the tooling sentence (L943-L944), "may be normalized, or have build metadata
stripped" (L1146-L1147), the prefix table's description cells and invitation row, the example records,
and text from the proto and from tmodel.

### Check 6: state machine

Every trigger now names a defined event. `state-machine.yaml` gained an `events` list of 8 events, each
with a definition, the `messages.yaml` structure or field it involves (all 8 resolve), a locator, a
kind and the requirements that define it: `evaluate-range` (`range`); `next-event-introduced`,
`next-event-fixed` and `next-event-last_affected` (the three event members); `next-event-no-branch`
(`event`); `events-exhausted` (`range.events`); `receive-copy` (`vulnerability`, inferred); and
`withdrawn-time-reached` (`vulnerability.withdrawn`, a time event, inferred). All 24 transitions keep
their trigger text and gained `event` and `constrained_by` (the requirements their guard and effect rest
on). No trigger is a message: OSV defines no exchange, and `protocol.yaml` stays a scaffold.
`bin/check-artifacts` reports no state-machine warning for this record.

### Check 7: consistency between artifacts

Each inconsistency found, and its fix:

1. **Optional nested members.** `messages.yaml` gave "optional (L722)" as the prose basis for
   `affected[].ecosystem_specific`, `affected[].database_specific` and `ranges[].database_specific`, while
   `requirements.yaml` labels R-0027 ("All other fields are optional") for top-level fields, the reading
   that does not contradict the mandatory members of nested objects. Fix: the three values now say that
   no sentence requires the member and that L722 is read for top-level fields, with a note on each field.
   The source's own unclarity is recorded (check 8).
2. **One-line summary.** `osv-recommended.derived.schema.json` checked "one-line" as the warning S02a,
   while R-0043 is a constraint and GAP-40 expects a two-line summary to be invalid. Fix: the check moved
   to a new stated rule, P11 of `osv-prose.derived.schema.json`; S02 now checks the length only.
3. **`null` arrays.** No derived rule rejected `null` for `aliases`, `affected`, `references` and both
   `severity` arrays (D11: none), and `schema/README.md` did not list it among the stated rules no schema
   expresses, while R-0032, R-0050, R-0063 and R-0205 define these fields as lists or arrays and GAP-36 to
   GAP-39 expect `null` to be invalid. Fix: a new stated rule, P12.
4. **The entry id.** `schema/README.md` did not list the `<ENTRYID>` part of R-0010 among the stated
   rules no schema expresses, though GAP-07, and now GAP-41, rest on it. Fix: listed, with the reason (the
   prefix is only "ideally" followed by a `-`, so where the database part ends cannot be told in general).
5. **EDGE-05.** It was left unspecified (a `null` top-level severity next to package-level severity),
   while GAP-39 holds a `null` top-level severity invalid by R-0050. Fix: EDGE-05 is invalid
   (`severity-array`, R-0050); its two readings now concern only the rule on severity at two levels, and
   its comparison is recomputed as `agrees`.
6. **The purl recommendation.** The examples' convention says that a valid record lists the should
   statements it breaks in `breaks_should`, but every derived record whose affected entries have a
   package lacks the recommended `purl` (except POS-20, GAP-30 and GAP-31), as do all nine complete
   source examples (S06 fires on them), and no rule quoted L967. Fix: the rule `purl-recommended`
   (R-0079), listed in the `breaks_should` of the nine source examples, and a convention saying that
   derived records inherit the base record's missing purl and do not repeat it; S-15 extended.
7. **Stale pass-1 text.** The `messages.yaml` note ("constrained_by is empty in pass 1"), the `req`
   convention of `normative.md` ("All read `(pass 3)` now"), the `rules` convention of `expected.yaml`,
   the design-notes convention ("Requirement ids ... are not cited in this pass") and `schema/README.md`
   ("Recorded for the cross-check pass", "Open for the later passes") are rewritten, and the examples
   README's "Nothing here depends on the other distilled artifacts" now says that no expected result
   depends on another artifact and that the ids are links.

Checked and consistent, not changed:

- S05 (a warning) and R-0173 (a requirement) differ because the source does: it calls the `versions` list
  "the requirement" (L1127-L1128) and states it elsewhere only as a recommendation (L937). U-2, design-notes
  defect 10 and EDGE-10 record this, and `schema/README.md` now names it as reading R13.
- R-0076 and R-0216 state the same rule as the JSON Schema `required` keywords that R-0073 and R-0213
  list in `also_at`; `requirements.yaml` assigns each keyword to one entry, and `normative.md` N-0318 and
  N-0332 name both entries.
- The other source defects stated in two or more files agree: `CleanStart` and `FreeBSD`, `GIT` as an
  ecosystem and as a reference type, `limit: "*"` in GIT ranges and `"0"` for the other event types, the
  required fields of the three sources, the unanchored id and timestamp patterns, and
  `additionalProperties`.

### Check 8: source questions recorded

- **What "All other fields" covers** (L722-L723): read for every field, it would contradict the members
  other sentences make mandatory. Recorded as `normative.md` U-28 and in design-notes open question 13.
- **An id with no entry part.** `GHSA-` passes the JSON Schema; design-notes defect 3 now says so, beside
  the existing "ideally" ambiguity (U-25; examples S-12).
- **No complete source example gives a purl**, though L967 recommends one: design-notes defect 16 and
  examples S-15.
- **A `null` top-level severity** is not a JSON array (L851): design-notes defect 11 now says so, beside
  the rule on severity at two levels.

### Fixes, by file

- `messages.yaml`: `constrained_by` on 47 fields and 13 structures (482 links; `Commit` left empty with a
  note); 25 `constrained_by_note`; three `required_sources.prose` values (check 7, item 1); `derived_rules`
  naming P11 and P12 on six fields; the file note.
- `normative.md`: the `req` slot of all 384 statements; the `req` convention; U-28.
- `examples/expected.yaml`: `requirements` on 108 rules and 12 `requirements_note`; the rule
  `purl-recommended`; `breaks` beside 96 violated rules and 5 `breaks_note`; GAP-41; EDGE-05; nine
  `breaks_should` items; F-01 and S-15; two new conventions and one rewritten; `pass`, `fixture_count`
  and `counts`.
- `examples/osv-records/gap-41-id-prefix-hyphen-only.derived.json`: new, the base record with `/id` set
  to `GHSA-`. `examples/README.md`: counts, F-01, S-15, judgement calls, a pass-3 paragraph and the
  reproduce line.
- `schema/osv-prose.derived.schema.json`: P11 and P12 (SHA-256 now `e4889e9a…3a6a`).
  `schema/osv-recommended.derived.schema.json`: S02 narrowed to the length (now `470a7a8b…4cd2`).
  Re-run after the change: both files pass `check_schema`; their 63 patterns compile under node with and
  without the `u` flag; their 33 quotations written as `L<line>: '...'` are verbatim at the lines cited;
  the nine example records give the results `schema/README.md` lists; and over the 136 derived and nine
  example records the only verdicts that changed are GAP-36 to GAP-40 and EDGE-05, now rejected by P11 or
  P12. `schema/README.md`: the digests, P11 and P12, S02, a requirements column for every P and S rule,
  D11, readings R12 and R13, requirement ids in "What no schema here checks" and the entry-id item, the
  observations sentence, a pass-3 paragraph and the open items.
- `design-notes.md`: 262 requirement ids; the convention bullet; defects 3, 11 and 16; open question 13.
- `state-machine.yaml`: the `events` list; `event` and `constrained_by` on 24 transitions; the note.
- `distilled/README.md`: written, with the artifact index and the licence and attribution section.
- This file: this section and the front matter.
- Unchanged: `requirements.yaml`, `schema/osv.schema.json`, `schema/vulnerability.proto`,
  `examples/run-fixtures.derived.py`, every other fixture file, `protocol.yaml`, `protocol.md`,
  `record.yaml` and `summary.md`.

### Validators

`bin/validate` 0 errors, 122 warnings; `bin/check-artifacts` 0 parse failures, 0 structural errors, 40
warnings; `PATH="$VENV/bin:$PATH" bin/check-requirements` 47 files, 0 failures. Each output is identical
to the run made before this pass, apart from a temporary directory name. This record's warnings concern
`record.yaml` (no content digest, no publisher) and the `protocol.yaml` scaffold.

### What remains open

- **Judgement calls for the reviewer:** the wiring rule of check 2 (R-0002 on every string-valued field;
  a row that describes an allowed value wired on that field too; both fields of a dependency); R-0020
  left unwired; L722 read for top-level fields; P11 and P12 (reading R12) and reading R13; EDGE-05 made
  invalid; JSON Schema entries in `breaks`; the purl convention; the `(item)` marks; the two inferred
  events of the record lifecycle.
- **Not checked:** the 80 smoke cases of `schema/README.md` were not re-run, as their scripts were not
  kept; pass 2's checks of every quotation and locator were not repeated beyond the text this pass
  added; the tmodel claims in `design-notes.md` were not re-checked; `protocol.yaml` and `protocol.md`
  remain scaffolds.
- `record.yaml` still needs its `distillation` block, which is the coordinator's; the coverage lines of
  `distilled/README.md` are written for it.

## Recording (coordinator, after pass 3)

- `record.yaml` now carries the `distillation` block (one coverage line per artifact, from pass 3's
  report), the not-applicable reason for protocol, the three passes at effort `max`, and the labels
  and metadata the extraction showed were missing or stale: `version`, `date`, `authors`, `publisher`,
  `identifiers.git` and `identifiers.commit`, `content.url` and `content.sha256` for `docs/schema.md`
  at tag `v1.9.2` (the digest was re-checked against that URL on 2026-10-19), `topic`, `bears_on`,
  `applicability.cryptography` and `implementations`.
- The `protocol.yaml` and `protocol.md` scaffolds that the passes above mention were removed: protocol
  is not applicable, and `record.yaml` says why.
- `summary.md` was rewritten from a proposal written in pass 1 by the design-notes agent, with its
  notes about stale record metadata dropped once `record.yaml` was updated.
