---
record: cwe
kind: verification
title: "cwe — FX-1 pass 2 (verify) and pass 3 (cross-check)"
extracted: "2026-10-08"
reviewed_by: ""
---

# Verification: CWE XML Schema 7.3 extraction

Agent C, independent of the pass-1 extractors, at maximum effort. Sources:
`cwe_schema_v7.3.xsd` (SHA-256 `690dedee…e45f98`, 1,345 lines) and
`cwec_v4.20.xml` (SHA-256 `1f5a78bd…0912e`), both re-hashed before use. All
checks ran from my own scripts (stdlib Python run with `-I`, expat and
ElementTree; system Ruby only to turn our YAML artifacts into JSON, which also
proves each one parses). The scripts are scratch files, not committed. Tools:
`bin/bcp14-count`, `bin/_bcp14.py`, xmllint (libxml2 2.9.13).

## Pass 2: verify

### 1. Keyword recount

- `bin/bcp14-count` on the XSD gives 0. `_bcp14.count` over all requirement
  texts gives 0. The header's 0 = 0 holds.
- Lower case, rescanned on my own. I used a regex over the raw XSD, longest
  match first and case-insensitive. Each hit's scope comes from character
  regions: documentation, appinfo, markup or comment. Result: 197 hits (must 6,
  must not 1, should 42, should not 5, may 32, required 72, optional 39). Of
  these, 161 are in documentation, 1 in appinfo and 35 in markup. None is
  upper or mixed case.
- `keyword_accounting` has 197 entries. Their positions match mine exactly
  (1-based columns), and so do their scopes. Each of the 89 extracted
  occurrences lies inside the text of its target requirement, on the same
  line. Each keyword inside a prose requirement text is accounted to that
  requirement.
- I read each of the 108 exclusions in context.
  - 75 are labels. I re-derived each target and its declaration from the XSD:
    70 are consistent and 5 contradict their declaration (D-01 to D-05).
  - 16 are may of possibility, 9 definitional, 4 examples, 1 purpose, and
    3 are embedded should / should not (L360, L417, L503).
  - None of the 108 is a directive.
- **Defect, fixed** (requirements.yaml): three consistent labels carried
  `contradicts:`. They were L274:340 (R-0089), L274:661 (R-0090) and L436:385
  (R-0129). All three are now `restates:`.

### 2. Verbatim text and locators

Method for requirements:

- A prose text must be a whitespace-normalised, contiguous substring of the
  documentation block that contains its locator line, and it must start on
  that line.
- An xsd text must be an exact substring of its locator line and must be the
  complete start tag.
- I tested the checker by planting a splice, a wrong line, a tidied quote and
  a truncated tag. It caught all four.

Results:

- **requirements.yaml**: 198/198 pass. Every text is byte-exact and file order
  holds; only the appended R-0198 sits out of order. **Defect, fixed**: the
  note said whitespace normalisation affected some texts. It affects none, and
  the note now says so.
- **normative.md**: all 115 quotes (111 documentation, 4 appinfo) equal the
  full source text. None is missing or duplicated. The other checks against my
  model also pass:
  - 195 structure lines and 4 branch lines: type, declared min/max (with †),
    required/optional, and the line of each R-id
  - the 344 enumeration values and the per-type counts
  - the component line ranges and the banner comments
  - the absence of default, fixed, `xs:key`, `xs:keyref` and other facets
    (checked by grep)
  
  Every prose requirement is listed exactly once, under its quote, with the
  right verb.
- **Other files**: quotes checked in state-machine.yaml, documented-formats.yaml
  and design-notes.md, plus the catalog quotes, give 82 quotes with 0 failures.
  The files follow different text conventions:

  | file | convention |
  |---|---|
  | requirements.yaml, normative.md, design-notes.md | keep `&lt;` and `&gt;` as written |
  | documented-formats.yaml D10 | decodes them |
  | messages.yaml enumeration docs | byte-exact, including double spaces |
  | normative.md | normalises whitespace |

### 3. Component walk for dropped statements

I built my own expat model of the XSD with line numbers, tracking effective
minOccurs through the compositors. It confirms the structural totals the
extraction claims:

| component | count |
|---|---|
| element declarations | 145 (144 local, 1 root) |
| attributes | 55 |
| wildcards | 2 |
| `xs:choice` | 3 |
| `xs:unique` | 5 |
| named simpleTypes | 34, with 342 values (plus 2 anonymous) |
| structures | 60 (31 named, 29 anonymous) |
| `xs:documentation` texts | 111 |

Coverage of the components that must be recorded:

- **All 105 are present**, with the right line and cardinality:
  - 57 required element particles, 4 of them with minOccurs omitted
  - 35 `use="required"` attributes
  - 4 required-in-branch
  - 2 required choices
  - 2 wildcards
  - 5 uniques
- **The other 8 xsd requirements** are 2 namespace, 1 root and 5 bounded.
- **Body_Text and Example_Code** are correctly left out: they sit in an
  optional choice.

Defects found:

- **Wording, fixed** (requirements.yaml note): bounded rule (b), read
  literally, also caught L494 Effectiveness_Notes. The rule now says the leaf
  itself must be enumeration-typed.
- **Consistency, fixed**: R-0140 (Observed_Example/Reference) now carries the
  rule-(a) note that R-0128 already had.
- **Dropped statement, fixed by adding R-0198** (`added_by: verify`, kind
  inferred). L616 says "A "Compound" weakness is … either a Chain or
  Composite." That is a co-constraint between two attributes: Abstraction
  Compound requires Structure Chain or Composite. Pass 1 excluded it as a value
  definition, yet catalog-stats I12 already cites L616 as its XSD basis. I
  updated, consistently:
  - in requirements.yaml: the counts, the reconciliation and the note
  - in normative.md: the "extracted as" line under L616
  - in catalog-stats: the I12 basis

### 4. messages.yaml

- **Structures and fields**: I re-derived all 60 structures and 203 fields
  from my model. Every field matches: line, complex_type_line, node, name,
  type, declared cardinality, required, effective, group, documentation_lines,
  appears_as and the header counts. documented_at also matches when recomputed
  by the file's own stated rule. 0 differences. (My script flagged 4 choice
  branch fields; that was its own simplification. The file's `required: false`
  with `effective` 0..1 or 0..unbounded is right.)
- **Enumerations**: 35 checked, covering values, lines, counts, has_other,
  used_by and documentation texts. 0 differences: 342 named values and 2
  anonymous.
- **4.20 counts**: my own type-directed walk of the catalog resolved every
  element and attribute (0 anomalies). All 203 `observed_4_20` counts, all 60
  `instances_4_20` and every enumeration value count match. XHTML: 20,246 in
  total, 15,025 inside Example_Code, 2,555 + 2,902 direct children, 151 under
  Note.

### 5. Examples

- **Digests and sizes**: all 20 fixtures match on SHA-256 and size.
- **Verbatim fixtures (13)**: for each entry, the catalog byte range gives the
  stated entry SHA-256, size, line range and CRLF flag. I rebuilt each fixture
  from the README wrapper rule plus those bytes, and every one is identical to
  the file.
- **Derived fixtures (7)**: each diff against its base is exactly the change
  described. In the two duplicate negatives, the second copy is verbatim
  except for its Name.
- **README**: the table and the totals (166,585 and 144,386 bytes) match.
- **xmllint, offline catalog** (the W3C schema digests match):
  - 14 fixtures valid (exit 0). 6 invalid (exit 3), each with the recorded
    error count, line, element, message and final line.
  - The full catalog validates against both the cached XSD and the committed
    copy.
  - Without the XHTML catalog, xmllint exits 3 with 5,457 strict-wildcard
    errors.
  - X5 reproduces.
- **Semantic values**: every value in expected.yaml equals both the fixture
  and the same entry parsed from the full catalog. These checks also hold:
  - the selection claims (smallest of each shape; CWE-79 4th largest; only
    22/78/119 have more child kinds)
  - the cross-fixture assertions X1 to X4
- **catalog-stats.yaml**, recomputed in full:
  - Every section and all 32 invariants reproduce.
  - Two lists differ only in order: cwe_ids_in_prose is sorted numerically,
    and "1300" sits last in the list of never-cited references.
  - I13's 944 counts the 934 entries with exactly one Primary ChildOf plus
    the 10 Pillars with none.
- **documented-formats.yaml**: D01 to D12 reproduce. **Defect, fixed**: D03's
  "not listed in the entry's References: 0" holds only if Demonstrative_Example
  References count as the entry's References. Counting only the entry-level
  References element, 15 citations are not listed. D03 now records both
  readings.

### 6. State machine and design notes

**state-machine.yaml**

- Its states are StatusEnumeration values, its guards UsageEnumeration values,
  and its Importance and Contribution values exist.
- Every observed count reproduces. That includes Status by kind, Status ×
  Usage, Abstraction × Usage, the 63 Suggestions with their source Usage and
  the 58 non-deprecated Prohibited weaknesses. It also includes the
  never-modified entries, the 23 Critical modifications with their quotes,
  235 + 48 Contributions, 925 previous names (4 with Version), 63 versions,
  the 4.20 deltas and 641 of 925 aligned.
- The transitions marked stated match the file's own definition: the source
  states the behaviour, and the state names are ours.

Defects, fixed:

- M1 listed Obsolete as terminal, yet it modelled Obsolete → Deprecated, and
  `not_modelled` contradicted that transition. Obsolete is no longer terminal,
  and both the basis and not_modelled are reworded.
- M2 listed mapped and both rejected states as terminal, yet transitions
  leave all three. Now `terminal_states: []`, with `outcome_states` and a
  note.
- M3 said "two release dates", but 4.11 has three. Reworded.

**design-notes.md**

The quotes are verbatim. These claims hold:

- 64 deprecated entries, 2 with Suggestions
- views 1000, 699 and 1194 are Graph views with Status Draft
- no weakness has two Primary relations with the same Nature and View
  (I14: 1193/1193, and no triple is repeated)
- the archive sizes
- the decision-id glosses, which match tmodel's spec

Defects, fixed:

- Mapping_Notes is also required on views (L131, L154).
- Three line ranges were wrong: L291–330 is now L291–357, L481–499 is
  L481–500, and L1071–1081 is L1071–1082.
- "All three graph views" was misleading, since 4.20 has 38 Graph views; it
  now names views 1000, 699 and 1194.
- Added open question 5: 4.20 departs from the documented Ordinal and
  Chain_ID rules (I15, I16).

## Pass 3: cross-check

- **`constrained_by` filled.** The requirements were linked as follows:
  - **By line:** 103 xsd requirements link to the field whose line is their
    locator line. R-0194 also links to the wildcard that Note inherits.
  - **By name:** 88 requirements link through an explicit object/field map:
    - prose requirements, to the fields they name
    - the choices R-0096 and R-0169, to their branch fields
    - the uniques R-0014 to R-0018, to the ID, Name and Reference_ID fields;
      R-0015 links Name on Weakness, Category and View (D-13)
    - value rules, to every field of that enumeration
  - **Result:** 191 of 198 requirements linked, giving 215 links on 128 of the
    203 fields. No requirement names the other 75: 74 are optional and one is
    the simpleContent value of Previous_Entry_Name (L349).
  - **Unlinked, with reasons, in `constrained_by_unlinked`** (7):
    R-0001, R-0002, R-0003, R-0004, R-0005, R-0035, R-0153.
- **Names resolve.** Every element, attribute and type name, and every quoted
  value, in a requirement's object or field exists in the schema.
- **State machine.** All 13 events are defined, and so are all
  triggers, accompanied_by events and states (initial, terminal, outcome,
  error). The fixtures it names exist, and its 20 invariant references match
  catalog-stats.
- **Examples ↔ state machine.** Every positive example validates.
  **Defect, fixed** (expected.yaml): `m2_mapping_decision` used names that are
  not M2 states. It now uses `mapped` (was `mappable`, ×3) and `under-review`
  (was `mappable-after-review`, ×1).
- **Source defects.** D-01 to D-16 are identical in requirements.yaml and
  normative.md. These agree with them:
  - documented-formats D10/D11, with D-09/D-08
  - the uniqueWeaknessName notes in messages.yaml and schema/README, with D-13
  - unchecked_references, with D-14
  - I14 and design-notes Q2, with D-10
  - I21, with D-11

  The data departures I15 and I16 are now cross-referenced in R-0159, R-0161
  and design-notes Q5, and R-0162 notes I14. No contradictions.
- **Index.** README.md still held the scaffold placeholders; it now has coverage lines and a row
  for this file.
- **Gate.** `bin/validate` reports 0 errors and nothing for cwe. I also
  simulated `check_full` with `profile: full`: 0 errors.

## Residual issues

- **L973 (not extracted).** Two of its statements imply co-constraints:
  Requires/RequiredBy denote composite parts, and
  StartsWith/CanPrecede/CanFollow denote chaining. Pass 1 excluded them as
  value definitions. The 4.20 data agrees: Requires appears only on the 4
  composites and StartsWith only on the 3 chains. A human reviewer should
  decide whether they become requirements.
- **R-0159 vs the data.** The inferred rule of R-0159 and the should-only of
  R-0161 are contradicted by MITRE's own data (I16, I15). The requirements
  record the source's rule, not the data.
- **Unverifiable claims.** design-notes' claim about CVE `replacedBy` cannot
  be checked inside the library: record cve-json-5 holds no extraction. The
  verbatim terms-of-use quotes in examples/README were not re-fetched.
- **Folded `reconciliation`.** `bin/_yaml.py` reads a folded
  `reconciliation: >` block as the string ">". That passes the non-empty
  check, but the library parser never reads the text.
- **Key name.** catalog-stats keeps the key `versions_with_two_release_dates`,
  although 4.11 has three dates.
