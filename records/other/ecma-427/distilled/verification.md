---
schema: "library-verification/v1"
id: ecma-427-verification
record: ecma-427
type: verification
updated: "2026-10-15"
by: "claude (independent verify agent, did not extract); claude (cross-check agent, pass 3)"
reviewed_by: ""
passes:
  - verify
  - cross-check
scope: full
attribution: "Contains text from ECMA-427 1st edition, © Ecma International 2025, reproduced under the Ecma copyright notice; full notice in distilled/README.md"
---

# ecma-427: FX-1 pass 2 (verify) and pass 3 (cross-check)

Contains text from ECMA-427 1st edition, © Ecma International 2025, reproduced under the Ecma copyright notice; full notice in distilled/README.md

By claude, an independent verify agent that took no part in pass 1. Effort: max. Date: 2026-10-15.
Scope: every file under `distilled/` and `summary.md`. The job was to break the extraction: recount
the verbal forms, check every quotation and locator against the PDF, look for dropped statements,
re-run every example and schema check, and test every factual claim about tmodel, purl-spec and the
other sources the files cite.

## Method

- **Source identity.** `.cache/ecma-427.bin` re-hashed: SHA-256
  `037180df99e7d7c26d910dc3adb3fa07c4fb787cc4bd29e43634de3802313825`, 40 pages, as in
  `record.yaml`. `pdftotext -layout` and plain `pdftotext` (poppler 26.07.0) re-run on the PDF
  reproduce `.cache/ecma-427.txt` (1771 lines) and `.cache/ecma-427.raw.txt` byte for byte. The page
  map was re-derived page by page: printed pp. 1 to 18 are PDF pp. 9 to 26, Annex A pp. 19 to 25 are
  PDF pp. 27 to 33, p. v is PDF p. 7, and PDF pp. 8, 34, 36 and 38 are blank.
- **Independence.** Own scripts only, kept in the session scratchpad and not committed. No pass-1
  script, output or artifact was used as evidence; every quotation was compared with the PDF text.
- **Allowed normalisation.** Page footers dropped; a line break inside a sentence joined with one
  space; a break directly after a hyphen (or after a slash inside a URL) joined with no space. Each
  check ran against both renderings in both join modes and reported which mode a match needed; the
  no-space join was needed only at hyphen or URL breaks (for example `Package-URL`,
  `percent-encoding` and the two Annex A strings on p. 20), which the page images confirm.
- **Locators.** A section map built from the clause headings, the eight table captions and the page
  footers of the layout text. A quotation counts as located only if it occurs inside the clause,
  table or Annex A pointer its locator names, on the printed page it names. This is what catches a
  repeated sentence filed under the wrong subclause.
- **Page images.** PDF pp. 11, 13, 14, 15, 18, 24 and 28 (printed pp. 3, 5, 6, 7, 10, 16 and 20)
  rendered at 110 dpi and read. Quote marks are straight wherever the text layer has them straight;
  the text layer's only curly marks are the double quotes around AS IS on p. v and the apostrophe in
  "specification’s" on p. 2. Tables 1, 2 and 8, the two hyphen breaks of Annex A on p. 20, the
  `Package-` / `URL` break of §6.5.5 on p. 10 and the italic "All items shall be unique." on pp. 10
  and 16 were confirmed on the images. Glyph positions on
  printed p. 21 (`pdftotext -bbox`) show both Annex A `examples` arrays indented by one 12 pt step,
  two monospace characters, as the two `.json-fragment` files have them; the layout text shows three
  spaces for one of them, a spacing artifact.
- **Other sources**, fetched 2026-10-15 into the scratchpad: purl-spec tarballs at `v1.0.0`
  (commit `c03cfa02`) and `v1.1.0` (commit `7cd2d344`) and commit, tag, release and contents
  metadata through `gh api`; the schema file again from raw.githubusercontent.com, by tag, by commit
  and from its `$id` URL; CVE schema `v5.2.0`; OSV `docs/schema.md` at `v1.9.1`; RFC 3986 and
  RFC 5234 from rfc-editor.org; RDF 1.1 Concepts (W3C Recommendation, 25 February 2014); Unicode
  16.0.0 and 18.0.0, chapter 3; ECMA-262 16th edition; the IANA URI schemes registry;
  draft-handrews-json-schema-validation-01. tmodel was read only with
  `git show origin/main:<path>` at `9f566281` (2026-10-14); nothing there was fetched or changed.
- **Tools.** Python 3.13.9 with jsonschema 4.26.0, packageurl-python 0.17.6, abnf 2.2.0 and
  PyYAML 6.0.3; Node v22.23.2; poppler 26.07.0.

## Recount of the verbal forms

Case-insensitive, whole words, "X not" counted once as "X not" (also when "not" starts the next
line), by layout-text line:

| Region (layout lines) | shall | shall not | should | should not | may | may not | must | can | cannot | total |
|---|---|---|---|---|---|---|---|---|---|---|
| Front matter, pp. i to v (1-214) | 1 | 0 | 0 | 0 | 2 | 1 | 0 | 1 | 0 | 5 |
| Clause 1 Scope (215-231) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Clause 2 Conformance (232-267) | 8 | 2 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 12 |
| Clause 3 Normative references (268-283) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Clause 4 Overview (284-311) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Clause 5, with Table 1 (312-560) | 21 | 11 | 3 | 0 | 11 | 0 | 0 | 0 | 0 | 46 |
| Clause 6, with Tables 2 to 8 (561-1305) | 37 | 0 | 0 | 0 | 2 | 0 | 0 | 1 | 8 | 48 |
| Annex A (1306-1696) | 3 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 5 |
| Back matter: Bibliography, Colophon, Software License (1697-1771) | 1 | 0 | 0 | 0 | 2 | 0 | 2 | 0 | 0 | 5 |
| **Whole document** | **71** | **13** | **3** | **0** | **20** | **1** | **2** | **2** | **9** | **121** |

The back-matter "shall" is the uppercase SHALL of the BSD disclaimer (line 1759).
`bin/bcp14-count .cache/ecma-427.txt` gives **2**: REQUIRED (line 1744) and SHALL (line 1759), both
in the Software License on p. 31.

| quantity | this recount | where it is recorded | result |
|---|---|---|---|
| shall, shall not, should, may (may not folded into may) | 71, 13, 3, 21: 108 | `requirements.yaml` `source_normative_counts` | equal, in total and in every region |
| forms in the 168 entry texts (recomputed with the file's own matcher) | shall 45, shall not 13, should 3, may 14 | `extracted_normative_counts.in_text` | equal |
| in_text + repeats + excluded | 75 + 26 + 7 = 108 | `extracted_normative_counts` | equal |
| occurrences accounted for by line and form | 108 of 108 | `keyword_accounting` | equal; every "extracted as" entry's text contains its form, every "repeats of" target lists the repeats in `also_at` |
| can, cannot, must | 2 (lines 133, 566), 9 (744, 819, 871, 929, 979, 1036, 1187, 1245, 1375), 2 (1750, 1752) | `reconciliation` | equal (the cannot lines were added in this pass, defect 12) |
| BCP 14 keywords | 2 | `source_keyword_count` 2, `extracted_keyword_count` 0 | equal; the difference of 2 is explained in `reconciliation` |
| normative.md tally (lowercase forms only) | shall 70 plus 1 uppercase SHALL; may 20; may not 1; can 2; cannot 9 | normative.md, "Verbal form tally" | equal; the two conventions are now cross-referenced (defect 14) |
| normative.md statement tags | 291 statements, 292 tag rows | normative.md | all 291 tags equal the forms found in their own quotations |

## Defects found

Severity: **material** = a wrong or dropped requirement, a wrong count, a non-verbatim quote or a
false claim; **minor** = locator, wording or format. Every fix keeps quoted text verbatim; no
quotation was changed.

1. **Material.** `requirements.yaml` R-0024 and R-0063 (normativity, testable, counts). Both "may
   look like a host" sentences were recorded as permissions, although their own notes,
   normative.md U-14 and the file's declared convention (possibility is never extracted as a
   requirement) read them as possibility. Evidence: "may sometimes look like a host" and "may look
   like a host" describe how a namespace can appear; no actor is granted anything (task question c).
   Fix: normativity `informative`, testable `no` with a reason, notes rewritten; `counts`
   updated (permission 14 to 12, informative 2, partial 36 to 34, no 7 to 9); the `note` and
   `reconciliation` now explain the class. Both "may" occurrences stay accounted for.
2. **Material.** normative.md C-8; `requirements.yaml` R-0008 and R-0081 `testable_reason`. They
   called §5.6.6's empty-value sentence a contradiction of Clause 2's rejection duty and said a
   validator "cannot tell" what to do. Judgement (task question a): no conflict. The second half of
   the sentence, "a key=value pair with an empty value is the same as if no key=value pair exists for
   this key", gives such a pair a meaning, so Clause 2 has nothing to reject; what the text leaves
   open is only whether a strict validator may also flag `key=`. `examples/expected.yaml`
   (PURL-NEG-06) and design-notes Adopt-4 already read it this way; `purl.derived.abnf` refuses
   `key=` (its gap G7). Fix: C-8 marked withdrawn and restated as U-16 under "Unclear or
   incomplete" (ids kept stable); R-0008 and R-0081 reasons rewritten; `schema/README.md` G7 now
   says `purl-parser-input` is stricter than the sentence.
3. **Material.** `requirements.yaml` R-0083 `notes` and R-0006 `testable_reason` items (4) and (5);
   design-notes Adopt-4. R-0083 and R-0006 said nothing settles whether a parser lowercases or
   rejects an uppercase key, or decodes a triplet such as `%41`. Evidence: "The key shall be
   composed only of lowercase ASCII letters and numbers, period '.', dash '-' and underscore '_'."
   (§5.6.6) and "The following characters shall not be percent-encoded:" (§5.4) make both strings
   non-conforming, and Clause 2 requires rejection; the record's own grammar (reading R1), fixtures
   PURL-NEG-04 and PURL-NEG-10 and design-notes defect 2 say so. Adopt-4's "fifth" equivalence
   presented such spellings as equal under the edition. Fix: both requirements notes corrected and
   R-0006's list renumbered (8 items to 7); Adopt-4 now says only the hex-digit case can differ
   between two valid spellings and that Adapt-1 step 3 decodes the others on purpose.
4. **Material.** `requirements.yaml` R-0165 `notes`; design-notes.md defect 9. They said a dotted
   type "cannot have a conforming "$id"" and "can never have a valid `$id`". False: nothing in
   Annex A or Clause 6 ties `$id` to `type` (normative.md U-11, `schema/README.md` O5, examples item
   9 and `messages.yaml` all say so), so `foo.bar` can carry a conforming `$id` such as one ending
   `foo-bar-definition.json`. Fix: both now say such a type cannot have an `$id` that embeds its
   type string, a potential mismatch rather than a broken rule.
5. **Material.** design-notes.md defect 2. It said "whether a non-canonical purl may contain, say,
   a raw space is not said" and that "An implementer cannot tell which deviations to reject and
   which to normalise". False and overstated: "Where the space ' ' is permitted, it shall be
   percent-encoded as '%20'." (§5.4) and each component "shall be encoded as defined in the
   Character encoding clause" (§5.6) bind every purl, and each rule's verbal form separates invalid
   from non-canonical input. Fix: the item now states the defect that holds (the line is drawn only
   by the verbal forms, and §5.2's "A canonical PURL" wording misleads); its 2nd-edition status is
   kept.
6. **Material.** design-notes.md E12. It said no key is marked `recommended` at v1.1.0 "although the
   2nd edition's schema allows it". At tag v1.1.0 `schemas/purl-type-definition.schema-1.1.json`
   allows `recommended`, but the 2nd edition's own Annex A text
   (`docs/specification/standard/Annex-A-PURL-Type-Definition.md`) does not: its qualifier key
   `requirement` admits only `optional` and `required`, and the two JSON documents differ. Fix: E12
   names the document that allows it and records the difference.
7. **Material.** design-notes.md, "What ECMA-427 is, for tmodel": "Parsing is fully defined
   (Clause 5)." Contradicted by `examples/README.md` ("gives no parsing algorithm"), by defects 11
   and 12, by grammar reading R5 and by PURL-EDGE-02. Fix: now "defined component by component
   (Clause 5), though without an algorithm and with a few edges left open".
8. **Minor.** `messages.yaml`, structure `purl-qualifier`, field `key`: the locator "§5.6.6; §5.3"
   did not contain the field's `source_phrase`, "The key for the qualifier.", which is in Table 7 and
   §6.8.1.1. Fix: the locator names both. The other 185 text and source_phrase values are at their
   locators.
9. **Minor.** `examples/README.md`, "Where the source is inconsistent or unclear", item 12: "That
   branch now carries later text". The path is gone: HTTP 404 on 2026-10-15 at github.com and
   raw.githubusercontent.com, after purl-spec commit `178ec1aa` renamed it on 2025-10-08. Fix:
   reworded, pointing to `schemas/purl-type-definition.schema-1.0.json` at v1.0.0.
10. **Minor.** `schema/README.md`, the closing "For context only" paragraph: "rewrites each one ...
    and `pkg:np_m/foobar` ... unchanged". Re-run: packageurl-python accepts 19 of the 30 strings,
    rewrites 18 and returns `pkg:np_m/foobar` unchanged. Fix: reworded.
11. **Minor.** design-notes.md, open question 12: said `record.yaml` has `bears_on: DEC-001,
    DEC-002`; it now also lists DEC-009. Fix: updated, still noting DEC-008 and DEC-001a.
12. **Minor.** `distilled/README.md` (requirements row) and `requirements.yaml` `reconciliation`.
    The README said every lowercase verbal form is accounted for by line in `keyword_accounting`;
    that list holds shall, shall not, should and may, while can, cannot and must are in
    `reconciliation`, which gave the cannot occurrences by location but not by line. Fix: README
    reworded; the nine cannot line numbers added.
13. **Minor.** `distilled/README.md` (examples row): "negatives that each break one stated rule".
    PURL-NEG-02 necessarily breaks three rules and PURL-NEG-06 is accepted. Fix: reworded.
14. **Minor.** normative.md, "Verbal form tally": its lowercase-only convention (shall 70) was not
    reconciled with `requirements.yaml`'s case-insensitive count (shall 71, may 21). Fix: one
    sentence added.
15. **Minor, not fixed.** `schema/purl.derived.abnf`: the rules `scheme`, `pct-slash` and
    `pct-octet-no-slash` carry no clause number on the rule line itself (their section headers
    cite 5.6.1 and 5.4, and `segment-pct-encoded` cites 5.4 and R1). Left unchanged because the
    headers make the citation clear and any edit would change the SHA-256 that `schema/README.md`
    records. Every other rule cites the clause it encodes, correctly.

## Judgements asked for

- **(a) Empty qualifier values.** Not a conflict with Clause 2 (defect 2). The sentence prohibits
  writing an empty value and gives a written one a meaning; a reader drops the pair. Open only:
  whether a strict validator may flag it. The files now say this consistently, and
  `purl-parser-input` is documented as stricter.
- **(b) "Shall be one of" items and the "Array" cells.** Classified consistently. All five "Shall
  be one of:" lines are `[shall]` statements in normative.md and `requirement` entries with verb
  shall and a verbatim `enumeration` in `requirements.yaml` (R-0124, R-0137, R-0140, R-0149,
  R-0153), each tied to its Annex A `oneOf`. The nine contradicting "Array" cells (four in Table 2,
  the `requirement` row of Tables 4 to 8) are the same nine in normative.md C-1 and C-2,
  `schema/README.md` D5, design-notes defect 7, examples items 5 and 6, `messages.yaml`
  `json_type_sources` and the table-cell notes; the seven agreeing "Array" cells are excluded
  everywhere. The rendered p. 7 confirms Table 2.
- **(c) "may look like a host".** A statement of possibility, not a permission (defect 1).
  normative.md U-14 already said so; `requirements.yaml` now agrees.

## Checked and clean

- **Verbatim.** `requirements.yaml`: 168 of 168 `text` values and every `enumeration` item; no
  splice (the multi-sentence texts are adjacent sentences, and the four split sentences, R-0046 and
  R-0047, R-0051 and R-0052, R-0081 and R-0082, R-0087 and R-0088, are contiguous pieces).
  normative.md: 344 of 344 quoted paragraphs in 324 blockquotes; 51 of 51 table rows, matched as
  whole rows in order, so every cell is in its own row; the 8 captions match apart from the
  documented replacement of the em dash. `messages.yaml`: 186 of 186 `text` and `source_phrase`
  values. `examples/expected.yaml`: the `reject_rule`, 63 of 63 `rules` and 59 fixture-level
  quotations. `examples/verbatim/`: 10 of 10 files byte-exact against the printed lines (plus one
  LF). design-notes.md: 204 curly quotations; 129 found verbatim in ECMA-427, and each of the other
  75 found in the source it is attributed to: the tmodel files (each in the file and section cited),
  the purl-spec v1.1.0 text, type files and commit messages, CVE 5.2.0, OSV 1.9.1, the IANA
  registry, RFC 3986 §2.1 and §3.1, RFC 5234 §2.3, RDF 1.1 Concepts §3.2, Unicode chapter 3 and
  draft-handrews-json-schema-validation-01 §6.4.2 (a few are search terms such as “sort”, not
  quotations). `summary.md`, `distilled/README.md`,
  `examples/README.md` and `schema/README.md`: every quotation of ECMA-427 verbatim, including the
  Copyright Notice and the Software License. `purl.derived.abnf`: 78 of 78 quoted passages in its
  comments.
- **Locators.** normative.md: 291 of 291 statements in the clause, table or Annex A pointer named,
  on the page named (one sentence occurs in both §5.1 bullets 4 and 5; statement 34 is the bullet 5
  instance, on p. 4 as stated); every JSON Pointer and page in the Annex A keyword tables.
  `requirements.yaml`: 168 locators and 149 `also_at` pointers (317 checks): each Requirement cell
  read from its own table row, each property line in its own subclause, each Annex A pointer
  resolved in the schema. `examples/expected.yaml`: 122 quoted rules in the clause and on the page
  named.
- **Dropped statements.** Walked Clause 2, §3, Table 1, §5 to §5.6.7 bullet by bullet, §6 with every
  subclause and property block, Tables 2 to 8 and Annex A. Every sentence of Clauses 1, 2, 3, 5 and
  6 is in normative.md (Clause 4 is excluded as declared non-normative), and every shall, shall not,
  should and may is in a `requirements.yaml` entry or listed there as a repeat or a licence
  exclusion. The 41 normative.md statements without an entry of their own are lead-ins (carried
  verbatim in `condition`), name-only property descriptions (excluded by the file's stated rule),
  the Clause 3 reference list and the Annex A introduction; none carries a verbal form. Annex A
  recounted from the schema: 38 constraint keywords (required 7, oneOf 5, const 4, format 4,
  uniqueItems 4, allOf 4, additionalProperties 3, pattern 3, default 2, additionalItems 1, minItems
  1), 39 `type` keywords and 37 description strings, 5 with a verbal form: equal to normative.md,
  and each constraint keyword is carried by a requirements entry, its `also_at` or its notes. The
  property types ("Type:" lines and the Type column) have no requirement entries of their own; they
  are carried field by field in `messages.yaml` (`json_type_sources`) and in the table-cell notes.
  Recorded for pass 3, not a defect.
- **Examples.** `run-fixtures.derived.py` reproduces all 54 recorded results: "54 fixtures; 13 where
  a tool differs from the expected result (each has a finding); 0 problems". Each negative breaks
  the rule it cites; PURL-NEG-02 also breaks two more and PURL-NEG-09 is rejected by the type
  characters after the §5.6.1 slash removal, both as documented. Expected results follow the text:
  `pkg://` and `pkg:///` accepted with every slash removed (§5.6.1); the colon written raw in a
  version and in a qualifier value, and `%3A` rejected (§5.4); an empty value dropped (§5.6.6);
  PURL-EDGE-01 and PURL-EDGE-02 recorded as judgement calls. The counts in `examples/README.md`
  (15 agreeing PURL fixtures, 13 differing) hold.
- **Schema.** SHA-256 `b8988773…e983` re-derived from fresh downloads by tag, by commit and from the
  `$id` URL; byte-identical to the committed file and to the v1.1.0 copy; git blob `97819266…` at
  v1.0.0 and on `main`; 10,732 bytes, 327 lines, ASCII, no tabs or trailing spaces. The printed
  Annex A, rebuilt from the layout text (29 joins at a space, 2 after a hyphen), equals the file
  token for token (925 tokens: 541 punctuation, 373 strings, 11 literals), as parsed JSON with key
  order, and with whitespace removed (7,236 characters). `purl.derived.abnf` (SHA-256 `7fecac73…`,
  matching its README) loads with abnf 2.2.0, says "DERIVED" on line 4, and reproduces all 49
  smoke verdicts on all three roots; 20 further adversarial strings behave as readings R1 to R5
  state. The purl-spec v1.0.0 corpus figures reproduce exactly: 497 tests, 200 strings, 129 of 129
  canonical outputs accepted, 114 accepted and 32 rejected parse inputs with the 24, 5, 4, 3 and 1
  breakdown, and 12 of 19 expected failures rejected. Defects D1 to D6 and observations O1 to O9
  hold. Provenance holds: both 404s, commit `178ec1aa` (2025-10-08, rename to `schema-1.1.json`),
  `4899f152` (2025-09-19) and `9c48dff9` (2025-11-10), the lightweight tag on `c03cfa02`, the
  release of 2025-12-19, 33 of 35 v1.0.0 type definitions valid with bazel and julia invalid as
  described, the `LICENSE` SHA-256, the one-token difference of the sibling `schema-1.1.json`, and
  the draft-07 §6.4.2 and §7.2 quotations.
- **Design notes and summary, tmodel.** DECISIONS-0001 v0.1.8 (updated 2026-10-12): DEC-001a,
  002, 003, 004, 005, 006, 007, 010 and 011 accepted by the ADRs named, DEC-001b, 008 and 009 open.
  ADR-0001 to ADR-0010 (there is no ADR-0005) all `accepted` at 1.0.0 with the quoted
  `version_policy`. APP-0001 and ARCH-0001 `draft`, the v0.2.0 proposal `proposed`, RPT-0004
  `draft`. The `identifiers` slot: `range: string`, multivalued, on Product, ProductInstance and
  Component, description ending "Additive DRAFT slot (DEC-001 open); not a new §13 class.".
  Exactly four `oci` purls in `spec/vectors` carry a namespace (mvp-01 one, mvp-03 two,
  tv-software-auth-service one), and the `oci` definition prohibits the namespace at v1.0.0 and at
  v1.1.0, with the quoted note. Every quotation attributed to a tmodel file is in the file and
  section cited (`fanout-identity.md` §1.2, §1.20 to §1.22, §1.25, §1.27, §1.31, §2 dimension 6 Q3
  item 3, §5, §9 and §10; `pilot.md`; `dimensions.md` Table 3; `fanout-vuln-data.md` §7; the ADRs,
  APP-0001, DECISIONS-0001, the LinkML schema and the vectors).
- **Design notes and summary, purl-spec and other sources.** npm and golang namespace and name
  `case_sensitive` false at v1.0.0 and true at v1.1.0, with the quoted notes; required qualifier
  keys only julia `uuid` and swid `tag_id` at both tags; 35 and 42 type definitions; the `oci` and
  `docker` example spellings at both tags; no registered type with one letter or a period; pypi's
  version `case_sensitive` false at both; `main` commit `accf27abf1` (2026-10-09) changed the type
  files. Every quoted 2nd-edition sentence is in `docs/specification` at v1.1.0, and every
  structural claim holds (Clause 2 word for word, the "Array" cells, `$id` 1.1 against the
  `$schema` const 1.0, the `purl-schemas` path in Clause 6.1, §6.9.1.8, the Unicode 16.0.0 link,
  RFC 3629 and RFC 5234 in Clause 3, the unchanged four-entry Bibliography against "Added 6
  references.", the About link text, the release notes' §5.1 rewording, "such as git://" and
  "programming" fixed). CVE 5.2.0 schema SHA-256 `33f75174…de67`, its quoted sentence and
  examples; OSV 1.9.1 sentence; RDF 1.1 §3.2; RFC 3986 §2.1 and §3.1; RFC 5234 §2.3; Unicode
  §3.13.2 "Default Case Conversion" in 16.0.0 and 18.0.0 with no "culture-invariant" in either
  chapter 3; ECMA-262 16th edition Annex A informative; IANA lists `pkg` as Provisional. E11
  reproduces row for row with packageurl-python 0.17.6, including the `normalize_name` list. The
  summary's ISO/IEC DIS 27056 listing is on the cached Ecma page, and the v1.1.0 release text
  confirms TC54's approval for the December 2026 General Assembly.
- **Source-defect lists across files.** After the fixes above, every defect claimed in normative.md
  (C-1 to C-10, U-1 to U-16), the requirements notes, `schema/README.md` (D1 to D6, O1 to O9, G1 to
  G9), design-notes.md (defects 1 to 21), `examples/README.md` (items 1 to 12) and `summary.md`
  ("Limits") holds against the source. Where two files describe the same defect, they now agree:
  the "Array" cells, `$id` and `$schema`, the `use_repository` default, the type length, the
  misplaced uniqueness line, `additionalItems`, the dead Annex A link, the empty qualifier value and
  the `$id` period.
- **YAML parsing.** `bin/_yaml.py` and PyYAML give the same structure and values for
  `requirements.yaml`, `messages.yaml`, `examples/expected.yaml` and `record.yaml`. The only
  differences are scalar types: `bin/_yaml.py` keeps unquoted numbers and booleans as strings, as it
  does for every record. `expected.yaml`, which quotes every scalar, parses identically outright.
- **Validators**, run before and after this pass: `bin/validate` 0 errors, 122 warnings, output
  identical; `bin/check-artifacts` 0 parse failures, 0 structural errors, 38 warnings, output
  identical; `bin/check-requirements` 47 sets including ecma-427, 0 failures (it needs the venv's
  `linkml-validate` on `PATH`). None of the warnings concerns ecma-427.

## Not-applicable declarations

- **protocol: correct, with one wording fix.** ECMA-427 defines a string syntax and a JSON
  document format; nothing in it is exchanged between parties, and Clause 1 only lists where purls
  are used. But "It names no roles" is too strong: the text names implementation roles, "PURL
  parsers" (§5.6.1), "Tools" (§6.5.7) and "A conforming implementation" (Clause 2). Its procedural
  statements are also more than the two given (Clause 2's rejection duty, the lowercasing of §5.6.2
  and §6.5.6, the empty-value reading of §5.6.6). Suggested reason: "ECMA-427 defines an identifier
  syntax (Clause 5) and a JSON document format for type definitions (Clause 6, Annex A). It names
  implementation roles (PURL parsers, §5.6.1; tools, §6.5.7; a conforming implementation, Clause 2)
  but no parties that exchange messages and no sequence of steps between them; Clause 1 lists where
  purls are used (SBOMs, vulnerability databases, advisories) without defining any exchange. Its
  procedural statements are all single-party string rules (for example a parser removing the
  slashes after 'pkg:', §5.6.1, the percent-encoding steps of §5.4, and the rejection duty of
  Clause 2), which requirements.yaml and schema/purl.derived.abnf carry."
- **state-machine: correct as written.** A purl is a string and a type definition is a static
  document; the 1st edition defines no lifecycle, no registration state (registered and
  unregistered types arrive only with the 2nd edition's Clause 5.7) and no parsing or building
  algorithm (the P1 to P9 order in `examples/expected.yaml` is the library's own).

## Not checked, or left open

- The 2nd edition was checked against purl-spec v1.1.0's Markdown, which the design notes define as
  the 2nd edition text; no Ecma-published 2nd edition PDF exists to check against.
- Tool runs and live queries reported in tmodel's research (E1 to E9: Syft, Docker Scout, Grype,
  OSV.dev, NVD) were checked as quotations of those files, not re-run. The CERT-In guidance, the
  firmware SBOM specification, SBOMproof and purl-spec issue #741 were not read directly.
- ISO/IEC Directives Part 2 was not fetched; the reading of shall, should, may, can and cannot
  follows the convention the files state.
- ECMA-262 regular-expression behaviour was confirmed only with Node v22.23.2, through the fixture
  runner; no second engine.
- Judgement calls left for the human reviewer: grammar readings R1 to R5; whether a strict
  validator may flag `key=` (U-16); PURL-EDGE-01 and PURL-EDGE-02; R-0062 ("Use instead a
  repository_url qualifier.") classified as a requirement; R-0132 classified as a recommendation.
- `record.yaml` was not edited: its top metadata is out of scope for this pass and its
  `distillation` block is not yet written.

## Pass 3: cross-check

By claude, a cross-check agent that took no part in passes 1 and 2. Effort: max. Date: 2026-10-15.
Scope: `requirements.yaml`, `messages.yaml`, `schema/` (the verbatim Annex A schema,
`purl.derived.abnf` and `README.md`), `examples/`, `normative.md`, `design-notes.md`,
`distilled/README.md` and `summary.md`. `record.yaml` was not edited; its `distillation` block is
the orchestrator's.

### Method

- **Reading.** Every YAML file was read with PyYAML and compared with `bin/_yaml.py`. Edits to
  `messages.yaml` and `examples/expected.yaml` were made by scratch scripts that insert lines
  (`messages.yaml`: only the 65 `constrained_by: []` lines were replaced), so every other byte is
  unchanged. The scripts stayed in the session scratchpad and are not committed.
- **Wiring rule, per field.** (1) Each entry of `constrained_by_locators` was resolved to the
  requirements whose `locator` or `also_at` sits in that clause, table or Annex A pointer. (2) A
  requirement was kept only where its `object`, `field` and `text` reach the field: a rule on a
  type definition is not wired to a PURL-string component, or the reverse, unless its text names
  that component (R-0117, R-0130 to R-0132, R-0135, R-0138, R-0141 and R-0151 speak of "the PURL
  ... component" and are wired to both sides). (3) The whole-string rules that a component's own
  attributes cite were added: `position` (R-0015), `url_mapping` (R-0026), URL validity (R-0025),
  the ASCII string (R-0041), the separators (R-0033), the encoding rules of §5.2, §5.4 and §5.6
  (R-0032, R-0034 to R-0038, R-0042, R-0043) on every percent-encoded component, and case folding
  (R-0039, R-0040) wherever a component is lowercased. Requirements that bind a structure as a
  whole (a closed set of components or members) went on the structure, in a structure-level
  `constrained_by`.
- **Grammar.** `purl.derived.abnf` (SHA-256 `7fecac73…a695`, unchanged by this pass) loaded with
  abnf 2.2.0; every PURL fixture parsed with the three entry rules; each rejected negative parsed
  again after repairing only the defect it cites.
- **Schema.** Every type-definition fixture validated against the committed verbatim schema
  (SHA-256 `b8988773…e983`) with `pattern` and `format: regex` evaluated by Node v22.23.2
  (`new RegExp`, ECMA-262) and `format: uri` by rfc3987 1.3.8, the reading `expected.yaml`
  declares; `run-fixtures.derived.py` run against the cached copy and against the committed file.
- **normative.md.** The 291 numbered statements parsed and matched to requirement texts and
  `also_at` locators by script, reviewed by hand, and each pair checked again by text or locator.
- **Tools.** Python 3.13.9, PyYAML 6.0.3, jsonschema 4.26.0, rfc3987 1.3.8, abnf 2.2.0,
  packageurl-python 0.17.6, Node v22.23.2.

### Check 1: requirements to messages and schema

All 168 entries checked by `object` and `field`:

| what the label names | entries | resolves to |
|---|---:|---|
| a PURL-string component, part or rule (objects PURL string, canonical PURL string, component string, percent-encoding rules, case folding, and the component lists of R-0004 and R-0005) | 86 | a field of `purl-string` or `purl-qualifier`, or that structure as a whole |
| a type-definition document, object or property | 70 | a field of a `typedef-*` structure, that structure as a whole, or an Annex A definition |
| an implementation duty or a document-level rule (R-0001 to R-0003, R-0006 to R-0014) | 12 | names no field; nothing to resolve |

Labels that name no `messages.yaml` field, and where each resolves:

- R-0023, R-0027 (URL Authority): a component a PURL must not have. Resolves to structure
  `purl-string` as a closed set of seven components.
- R-0099, R-0162, R-0166, R-0167 (whole document; top-level, repository and qualifier-definition
  properties): the structures `typedef-root`, `typedef-repository` and
  `typedef-qualifiers_definition-item`, each closed by Annex A `additionalProperties: false`.
- R-0125, R-0126, R-0127 (Component optional, required, prohibited requirement; "value"): the
  Annex A definitions `/definitions/optional_requirement`, `required_requirement` and
  `prohibited_requirement`, whose `title` is the object label and whose `const` is the value.
  `messages.yaml` carries them as the allowed values of each `requirement` field, where they are
  wired.
- R-0161 (schema dialect): the Annex A `$schema` keyword (draft-07), not the `$schema` member of a
  type definition document. Resolves to structure `typedef-root`, whose `encoding` names draft-07.
- R-0062 (repository_url qualifier): `messages.yaml` named no such key. **Fix:** an `inferred`
  statement on `purl-qualifier.key` names repository_url as the only key the 1st edition names, with
  its basis.

No requirement label was wrong and none was changed. Annex A side: the 38 constraint keywords
(normative.md K1 to K38) are all carried, 31 by an entry's `locator` or `also_at` and 7 by notes
(K10 in R-0164, K15 in R-0113, the `allOf` keywords K19, K22, K25 and K33 in R-0119 to R-0123, K26
in R-0142). Property types (the Type column of Tables 2 to 8, the Type lines of Clause 6 and the 39
Annex A `type` keywords) have no entries; `messages.yaml` carries them as `json_type` with
`json_type_sources`. Pass 2 left this for pass 3. **Fix:** the `requirements.yaml` `note` now says
so (see "What remains open").

### Check 2: constrained_by wired

- **Fields:** 65 of 65 wired, none empty: 344 links to 147 distinct requirements. 23 fields carry a
  `constrained_by_note`: why the requirements at one of their locators bind another structure, or
  how a requirement reaches the field through a type definition. `constrained_by_locators` is kept
  unchanged on all 65 fields, and the file's `note` describes the wiring.
- **Structures:** 4 carry a structure-level `constrained_by` with 7 requirements: `purl-string`
  (R-0023, R-0027), `typedef-root` (R-0099, R-0161, R-0162), `typedef-repository` (R-0166),
  `typedef-qualifiers_definition-item` (R-0167). The `messages` family schema lists
  `constrained_by` on fields; its keys are "a loose superset", and `bin/check-artifacts` output is
  unchanged.
- **Locators:** the 297 locator entries resolve, clause by clause, to 1,122 candidate links (a
  table locator reaches every row of the table, `Clause 2` all 13 duties). 306 were kept and 816
  filtered out by object, field and text; 38 links were added by step (3) of the wiring rule
  (R-0015, R-0025, R-0026, R-0032, R-0036, R-0039, R-0040, R-0041, R-0062 and R-0064 on the PURL
  components, and R-0117, R-0135, R-0138 and R-0151 on the four `requirement` fields). 16 locator
  entries (13 distinct) resolve to no requirement: Clause 1; §6.8.1 (twice), §6.8.1.5 and §6.8.1.6
  (twice), which have no Property line; and 10 Annex A property pointers whose Required or Optional
  status is entered under a table cell, with `/required` in `also_at`.
- **Requirements no field references (14), and why:**
  - R-0001 to R-0003 and R-0006 to R-0013 (11): Clause 2 conformance duties. They bind an
    implementation (support everything, adhere to the syntax, canonicalise, process encoding per
    RFC 3986, reject invalid PURLs, extend or not), not a field. R-0004 and R-0005 name components
    and are wired (R-0005 to qualifiers and subpath, the two it names).
  - R-0014: Clause 3, which edition of an undated reference applies. It governs how R-0039
    (Unicode), R-0128 (ECMA-262) and the URI formats (R-0116, R-0158) are read; those are wired.
  - R-0024, R-0063: informative ("may" as possibility, normative.md U-14); they constrain nothing.
- **Referenced by a structure only (7):** R-0023, R-0027, R-0099, R-0161, R-0162, R-0166, R-0167,
  as listed above.

### Check 3: Clause 5 requirements to the derived grammar

Of the 84 Clause 5 entries (R-0015 to R-0098): 58 are enforced by a rule, 12 are enforced in part
with the rest named by a gap item, 12 are not expressible (9 in the grammar's own GAPS G1 to G9, 3
newly listed in `schema/README.md`: R-0025, R-0038, R-0062), and 2 are informative. Enforcement
holds under the grammar's readings R1 to R5. The authority prohibition is enforced by `purl` but
not after the `pkg://` slash removal of `purl-parser-input`; that is new design-notes open question
13. `schema/README.md` now also gives the requirement ids beside G1 to G9. The grammar file is
unchanged.

| Clause 5 requirement | enforced by (`purl.derived.abnf`, under readings R1 to R5) | not expressible: where it is listed |
|---|---|---|
| R-0015 | `purl`, `purl-remainder`, `canonical-shape` | |
| R-0016 | `purl` (`scheme` first) | |
| R-0017 | `purl-remainder` (`type`) | |
| R-0018 | `purl-path` (namespace optional) | G3: a type may require it |
| R-0019 | `purl-path`, `name` (R3) | |
| R-0020, R-0022 | `purl-remainder` (`@` version and `#` subpath optional) | |
| R-0021 | `purl-remainder` (`?` qualifiers optional) | G3: a type may require keys |
| R-0023, R-0027 | `purl` (no authority part) | a host after `pkg://` survives as a type: schema/README.md (pass 3), design-notes open question 13 |
| R-0024, R-0063 | informative, nothing to enforce | |
| R-0025 | every `purl` string is an RFC 3986 URI (24 checked) | conformance to four documents: schema/README.md (pass 3) |
| R-0026 | `purl-remainder` (path, then `?` query, then `#` fragment) | |
| R-0028, R-0030 | `scheme` (only `pkg`) | G9: the excluded type names are open-ended |
| R-0029, R-0031 | `qualifier-value` admits an encoded URL (smoke 47) | |
| R-0032 | `allowed-char`, `pchar`, the separators of the root rules | |
| R-0033 | root rules, `purl-path`, `qualifiers`, `qualifier`, `canonical-subpath` | |
| R-0034 | | G6: well-formed UTF-8 not checked |
| R-0035, R-0043, R-0088 | `pchar`, `pct-encoded` (R1) | |
| R-0036 | `pct-octet-no-slash` (R1); separators written raw | |
| R-0037 | `pchar` (no raw space; `%20` admitted) | |
| R-0038 | | schema/README.md (pass 3): says which document governs, no syntax |
| R-0039, R-0040 | | G2 |
| R-0041 | every terminal is ASCII | |
| R-0042 | `pchar`, `segment-char` | |
| R-0044 | `scheme` (R4) | |
| R-0045 | `purl` (`scheme ":"`) | |
| R-0046 | `purl-parser-input` | |
| R-0047 | | G5: a transformation |
| R-0048, R-0049, R-0050 | `type` | |
| R-0051 | `type` admits any case | G2: the comparison itself |
| R-0052 | `canonical-type` | |
| R-0053 | `purl-path` (namespace optional) | G3 |
| R-0054, R-0057, R-0059 | `namespace`, `namespace-segment` | |
| R-0055, R-0065, R-0092 | `canonical-shape` (no insignificant slash; shape only, G1) | |
| R-0056, R-0066 | `purl-path` (R5) | |
| R-0058, R-0094 | `segment-char` (no `%2F`; R1) | |
| R-0060, R-0097 | `segment-char` | G3; G6 |
| R-0061 | | G8 |
| R-0062 | `qualifier-key` admits the key | schema/README.md (pass 3): an instruction, not syntax |
| R-0064 | `purl-path`, `canonical-shape` | |
| R-0067 | `name` | |
| R-0068, R-0072 | `pchar` (an encoded `/` allowed) | G3; G6 |
| R-0069, R-0070, R-0071 | `purl-remainder`, `version` (R2) | |
| R-0073, R-0098 | | G8 |
| R-0074, R-0075 | `purl-remainder`, `qualifiers` (R2) | |
| R-0076, R-0077, R-0078 | `qualifiers` | |
| R-0079, R-0080 | `qualifier` | |
| R-0081 | `qualifier-value` (`1*pchar`) | |
| R-0082 | | G7 |
| R-0083, R-0084, R-0085 | `qualifier-key` | |
| R-0086 | | G4 |
| R-0087 | `qualifier-value` | |
| R-0089, R-0090, R-0091 | `purl-remainder`, `subpath`, `canonical-subpath` (R2) | |
| R-0093, R-0095, R-0096 | `subpath-segment`, `canonical-subpath` (R1 makes `%2E` impossible) | |

### Check 4: examples to schema and grammar

- **PURL fixtures (24) against the grammar.** All 12 positives are accepted by
  `purl-parser-input`, the parser's entry rule. `purl` rejects only the two `pkg://` forms
  (PURL-POS-01, 02), which §5.6.1 makes parser input; `canonical-shape` rejects only the uppercase
  type (POS-03) and the doubled slash (POS-07), both valid but not canonical. The 13 canonical strings
  `expected.yaml` gives are all accepted by `canonical-shape`. Of the 10 negatives, 8 are rejected by
  all three rules, and each is accepted once only the defect it cites is repaired, so each fails for
  the requirement it cites. The other 2 are the stated gaps: PURL-NEG-05 (a repeated key, expected
  reject, R-0086) passes the grammar (G4), and PURL-NEG-06 (an empty value, expected accept,
  R-0082) fails it, because all three rules refuse `key=` (G7). PURL-EDGE-01 is accepted by
  `purl-parser-input` with the type `example.com`, as expected; PURL-EDGE-02 (`PKG:`) is rejected,
  which is reading R4 and one of the two readings `expected.yaml` records.
- **Type-definition fixtures.** The 30 schema-checked fixtures (23 type definitions, 7 source
  examples) give exactly the expected result against the committed verbatim schema under the
  declared reading (ECMA-262 patterns and regex format, format asserted). Each of the 17 invalid
  type definitions fails at exactly the Annex A keyword its `violates` cites (TD-NEG-11 and TD-NEG-12
  also at a sibling keyword reached by the same change, as `examples/README.md` says).
- **Runner.** `run-fixtures.derived.py`, before and after the edits, with the cached schema copy and
  with `--schema` set to the committed file: "54 fixtures; 13 where a tool differs from the expected
  result (each has a finding); 0 problems".
- **Trace added to `expected.yaml`.** `requirements` on each of the 63 rules (61 with ids, 56
  distinct; `c1-no-type-definitions` and `c5-separators` have none, with a `requirements_note`) and
  on `reject_rule` (R-0008); and `breaks` beside each broken rule: 34 lists on 31 fixtures (10 PURL
  negatives, 13 TD negatives, 3 TD format, 1 TD pattern and 4 TD gap fixtures), 26 distinct ids. Two
  fixtures break a property type, which has no entry: TD-NEG-11 traces to R-0099 and TD-NEG-12 to
  R-0124 (the oneOf the same change breaks), each with a `breaks_note`. A new `conventions` item
  explains the keys, and PURL-NEG-06's `result_note` names R-0081 and R-0082. The file still parses
  identically with `bin/_yaml.py` and PyYAML.

### Check 5: normative.md statements to requirements

All 291 statements: 219 map to requirement ids (277 pairs, each confirmed by text or by an
`also_at` locator, except statement 225, a `Type: Object` line, mapped to R-0142 by content); 72
have no entry and a reason; **0 have neither**. Of the 72, 29 are quoted in an entry's notes or
`condition`; pass 2's figure of 41 statements "without an entry of their own" used its own grouping.

| clause | statement → requirement ids |
|---|---|
| Clause 2 (1 to 14) | 1 to 5 → R-0001 to R-0005; 6, 7 → R-0006 (two sentences of one entry); 8 to 14 → R-0007 to R-0013 |
| Clause 3 (15 to 18) | 17 → R-0014 |
| Clause 5, Table 1, §5.1 to §5.5 (19 to 46) | 20 → R-0015; 22 → R-0016 to R-0022; 24 to 26 → R-0023 to R-0025; 28 to 29 → R-0026 to R-0027; 30, 31 → R-0028 (two sentences of one entry); 32 → R-0029; 33, 34 → R-0030 (two sentences of one entry); 35 to 37 → R-0031 to R-0033; 39 to 44 → R-0034 to R-0039; 45, 46 → R-0040 (two sentences of one entry) |
| §5.6 to §5.6.7 (47 to 107) | 47 → R-0041; 49 to 50 → R-0042 to R-0043; 53 to 54 → R-0044 to R-0045; 55 → R-0046, R-0047; 56 to 65 → R-0048 to R-0057; 67 to 89 → R-0058 to R-0080; 90 → R-0081, R-0082; 92 to 95 → R-0083 to R-0086; 96 → R-0087, R-0088; 97 to 101 → R-0089 to R-0093; 103 to 107 → R-0094 to R-0098 |
| Clause 6 and Table 2 (108 to 114) | 109 → R-0099; 112 → R-0100 to R-0111; 113 → R-0117 (a repeat, in its also_at); 114 → R-0141 (a repeat, in its also_at) |
| §6.1 to §6.4.3, Table 3 (115 to 129) | 115 → R-0100, R-0112; 117 → R-0101; 119 → R-0102; 121 → R-0103; 123 → R-0113 to R-0115; 124 → R-0113; 126 → R-0114, R-0116; 128 → R-0115 |
| §6.5 to §6.5.9, Table 4 (130 to 162) | 130 → R-0104; 132 → R-0117; 133 → R-0118 to R-0123; 134 → R-0129; 135 to 136 → R-0131 to R-0132; 137 → R-0118; 139 to 140 → R-0124 to R-0125; 142 → R-0126; 144 → R-0127; 146 → R-0119, R-0128; 147, 148 → R-0129; 149 → R-0120, R-0130; 150, 151 → R-0131; 152 → R-0121; 154, 155 → R-0132; 156 to 157 → R-0133 to R-0134; 158 → R-0122; 161 → R-0123 |
| §6.6 to §6.6.7, Table 5 (163 to 191) | 163 → R-0105; 165 → R-0135; 166 → R-0136, R-0119 to R-0123; 167 → R-0129; 168 to 169 → R-0131 to R-0132; 170 → R-0136; 172 → R-0137; 173 → R-0126; 175 → R-0119, R-0128; 176, 177 → R-0129; 178 → R-0120, R-0130; 179, 180 → R-0131; 181 → R-0121; 183, 184 → R-0132; 185 to 186 → R-0133 to R-0134; 187 → R-0122; 190 → R-0123 |
| §6.7 to §6.7.7, Table 6 (192 to 220) | 192 → R-0106; 194 → R-0138; 195 → R-0139, R-0119 to R-0123; 196 → R-0129; 197 to 198 → R-0131 to R-0132; 199 → R-0139; 201 → R-0140; 202 → R-0125; 204 → R-0119, R-0128; 205, 206 → R-0129; 207 → R-0120, R-0130; 208, 209 → R-0131; 210 → R-0121; 212, 213 → R-0132; 214 to 215 → R-0133 to R-0134; 216 → R-0122; 219 → R-0123 |
| §6.8 to §6.8.1.7, Table 7 (221 to 243) | 221 → R-0107; 223 → R-0141; 224, 225 → R-0142 (225 by content: its item Type: Object line); 227 → R-0143 to R-0147; 229 → R-0148 (the inferred entry); 232 → R-0149; 233 → R-0125; 235 → R-0126; 243 → R-0150 |
| §6.9 to §6.9.7, Table 8 (244 to 272) | 244 → R-0108; 246 → R-0151; 247 → R-0152, R-0119 to R-0123; 248 → R-0129; 249 to 250 → R-0131 to R-0132; 251 → R-0152; 253 → R-0153; 254 → R-0125; 256 → R-0119, R-0128; 257, 258 → R-0129; 259 → R-0120, R-0130; 260, 261 → R-0131; 262 → R-0121; 264, 265 → R-0132; 266 to 267 → R-0133 to R-0134; 268 → R-0122; 271 → R-0123 |
| §6.10 to §6.12 (273 to 282) | 273 → R-0109, R-0154; 274 to 276 → R-0155 to R-0157; 277 → R-0110; 279 → R-0111, R-0158; 281 to 282 → R-0159 to R-0160 |
| Annex A (283 to 291) | 285 → R-0161; 287 → R-0129; 288 to 289 → R-0131 to R-0132; 290 → R-0117; 291 → R-0141 |

| reason there is no requirement entry | statements | n |
|---|---|---:|
| lead-in, carried verbatim in the `condition` of the entries after it | 48, 66, 91, 102 | 4 |
| pointer, purpose or rationale sentence, quoted or named in the notes of the entry given | 15 (R-0014), 16 (R-0014), 21 (R-0015), 23 (R-0015), 27 (R-0025), 38 (R-0034), 51 (R-0041), 52 (R-0041), 108 (R-0099), 284 (R-0161), 286 (R-0161) | 11 |
| expansion of the abbreviation PURL; constrains nothing | 19 | 1 |
| the Clause 3 reference list (R-0014 applies to each entry) | 18 | 1 |
| Annex A heading | 283 | 1 |
| property block with only Location and Type lines (property types have no entry; check 1) | 110, 228, 230, 237, 239, 241 | 6 |
| property description that only names or explains a property (excluded by the rule in the `requirements.yaml` note) | 111, 116, 118, 120, 122, 125, 127, 129, 131, 138, 141, 143, 145, 153, 159, 160, 162, 164, 171, 174, 182, 188, 189, 191, 193, 200, 203, 211, 217, 218, 220, 222, 226, 231, 234, 236, 238, 240, 242, 245, 252, 255, 263, 269, 270, 272, 278, 280 | 48 |
| **total** | | **72** |

The 38 Annex A constraint keywords are mapped under check 1.

### Check 6: design notes to requirements

95 edits added 148 requirement-id references (64 distinct ids) beside the clause or table locators
of the rules that `design-notes.md` argues from: the overview, the Adopt, Adapt and Reject items,
the mapping table, the source defects, the evidence table (E7, E10, E11) and open questions 8 and
10. All 202 curly quotations were compared before and after: unchanged. A convention bullet says
that `R-NNNN` is the `requirements.yaml` entry, a different series from RPT-0004's R-ID-n and
R-MERGE-n. Quotations left without an id have no entry: Clause 1, the Introduction, Clause 4, the
two descriptive Clause 5 sentences (statements 21 and 23), Table 1 description cells, the §5.1
rationale bullet (statement 27), the Annex A link (statement 286) and the property types; [2nd ed.]
and non-Ecma quotations get none.

### Check 7: consistency

- **Coverage lines,** recomputed from the files: normative.md 291 statements; requirements.yaml
  168 entries, its `counts` block equal to the entries; messages.yaml 13 structures and 65 fields;
  examples 54 fixtures; 2 schema files and a README. `distilled/README.md` now says that property
  types are not requirement entries, and its messages, examples and design-notes rows describe the
  pass-3 additions. `summary.md` "Artifacts in this record" states no counts and still matches the
  files.
- **Stale text fixed:** `schema/README.md` ("Open for the later passes") and the `messages.yaml`
  `note` still said `constrained_by` was empty; the `expected.yaml` row of `examples/README.md` now
  mentions the ids.
- **Withdrawn claims:** none survives. The C-8 conflict, defect 2's "cannot tell" and raw-space
  claims, "cannot have a conforming $id" (defect 9, R-0165), "nothing settles" (R-0083, R-0006) and
  "Parsing is fully defined" appear only as withdrawn (normative.md C-8) or in the pass 2 log above.
- **One contradiction fixed:** R-0112's notes called the type pattern's lowercase-only class
  inconsistent with §5.6.2, while `schema/README.md` D4, normative.md C-6, design-notes defect 9 and
  TD-NEG-06 treat only the two-character floor as a defect. The note now limits the inconsistency to
  length and says why the case part agrees.
- Every other source defect stated in two or more files agrees: the "Array" cells, `$id` and
  `$schema`, the `use_repository` default, the type length, the misplaced uniqueness line,
  `additionalItems`, the dead Annex A link, the empty qualifier value, the `$id` period, the scheme
  case, `repository_url`, qualifier order and hex-digit case.

### Check 8: source questions recorded

- design-notes open question 13: whether the authority prohibition (R-0023, R-0027) can be enforced
  at all once §5.6.1 removes the slashes after `pkg:` (R-0046, R-0047). Recorded since pass 1 only
  in `examples/README.md` item 2 and PURL-EDGE-01; met again in check 3.
- design-notes open question 14: what a qualifier definition's `default_value` and an absent
  `requirement` mean (R-0146, R-0144). Found in check 2.
- The structure-level note on `purl-string` and the field note on `default_value` point to them.
  Neither was checked against the 2nd edition.

### Fixes, by file

- `messages.yaml`: `constrained_by` on 65 fields and 4 structures; 23 field notes and 4 structure
  notes; the inferred repository_url statement on `purl-qualifier.key`; the `note` sentence about
  `constrained_by` rewritten.
- `examples/expected.yaml`: `requirements` on 63 rules and `reject_rule`; 34 `breaks` lists; 2
  `breaks_note`; 2 `requirements_note`; 1 `conventions` item; PURL-NEG-06 `result_note`.
- `requirements.yaml`: R-0112 `notes`; the header `note` (property types). No entry, text, id or
  count changed.
- `design-notes.md`: 148 requirement ids, the convention bullet, open questions 13 and 14.
- `schema/README.md`: ids beside G1 to G9, the paragraph on the Clause 5 requirements no G item
  covers, the "Open for the later passes" bullet. `schema/purl.derived.abnf` and the verbatim schema
  are unchanged (SHA-256 `7fecac73…a695` and `b8988773…e983`).
- `distilled/README.md`, `examples/README.md`: coverage lines.
- `verification.md`: this section; front matter `passes` now lists verify and cross-check.
- Unchanged: `normative.md`, `summary.md`, `record.yaml`, the fixture files and
  `run-fixtures.derived.py`.

### Validators and YAML

`bin/validate` 0 errors, 122 warnings; `bin/check-artifacts` 0 parse failures, 0 structural errors,
38 warnings; `bin/check-requirements` 47 files, 0 failures. Each output is identical to the run made
before this pass (apart from a temporary directory name), and no warning concerns ecma-427.
`bin/_yaml.py` and PyYAML agree on `messages.yaml`, `requirements.yaml` and `expected.yaml` once
unquoted numbers and booleans are read as strings, the known difference; `expected.yaml` agrees
outright.

### What remains open

- **Property types are not requirement entries.** A reviewer should decide whether to extract the
  Clause 6 Type lines and Annex A `type` keywords (about 30 entries) or keep them in `messages.yaml`
  only. Until then TD-NEG-11 traces only to R-0099.
- **Structure-level `constrained_by`** is an addition to the `messages` family; the migration PR
  for `schema/artifact.schema.yaml` may adopt it or move the 7 ids.
- **Judgement calls for the reviewer:** the whole-string rules (R-0015, R-0025, R-0026, R-0033,
  R-0041) wired to every component, and the §5.4 rules, R-0038 included, to every percent-encoded
  component; the Clause 2 duties left unwired; R-0005 wired to qualifiers and subpath only, as its
  label says; the rules that reach a component through a type definition wired to both sides.
- R-0025 (conformance to four URL definitions) has no single test; `schema/README.md` says so.
- Pass-2 defect 15 (three grammar rules without a clause number on the rule line) stays unfixed,
  so the grammar's SHA-256 is unchanged.
- Open questions 13 and 14 go to purl-spec upstream.
