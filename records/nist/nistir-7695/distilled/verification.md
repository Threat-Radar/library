---
schema: "library-verification/v1"
id: nistir-7695-verification
record: nistir-7695
type: verification
updated: "2026-10-19"
by: "claude (independent verify agent, did not extract); claude (cross-check agent, pass 3)"
reviewed_by: ""
passes:
  - verify
  - cross-check
scope: full
attribution: "Contains text from NIST IR 7695 (August 2011), published by NIST with no copyright or licence notice; works of NIST employees are not subject to copyright in the United States (17 U.S.C. 105), but two of the three authors were not NIST staff (Acknowledgments, p. iii), so the text is not claimed to be wholly a U.S. Government work."
---

# nistir-7695: FX-1 pass 2 (verify) and pass 3 (cross-check)

Contains text from NIST IR 7695 (August 2011); provenance as in the front matter.

By claude, an independent verify agent that took no part in pass 1. Effort: max. Date: 2026-10-19.
Scope: every file under `distilled/` (`normative.md`, `requirements.yaml`, `messages.yaml`,
`schema/`, `examples/`, `design-notes.md`). `record.yaml`, `summary.md` and the `protocol.*` and
`state-machine.yaml` scaffolds were read, not edited. The job was to break the extraction: recount
the verbal forms, check every quotation and locator against the PDF, look for dropped statements,
re-run every example and grammar, and test every claim about tmodel and the other sources the files
cite.

## Pass 2: verify

### Method

- **Source identity.** `nistir7695.pdf` re-hashed: SHA-256
  `01553a4638b21eda10018690b71162e91605d78eb15850f881bd0b2b691ac3f6`, 49 pages, as in
  `record.yaml`. `pdftotext -layout` (poppler 26.07.0) re-run on it reproduces `nistir7695.txt`
  (2443 lines) byte for byte. The page map was re-derived from the page breaks and footers: PDF pages
  3 to 6 are printed ii to v, and PDF pages 7 to 49 are printed 1 to 43 (PDF page = printed page
  plus 6).
- **Independence.** Own scripts only, kept in the session scratchpad (`fx1/cpe/verify/`) and not
  committed. No pass-1 script or output was used as evidence; every check compared an artifact with
  the PDF, its text rendering or a source fetched in this pass.
- **Allowed normalisation (prose).** Page header and footer dropped; a line break inside a sentence
  joined with one space; a break after a hyphen inside a word joined with no space (the seven such
  breaks are `valid-values` L771, `percent-encoding` L973, `non-normative` L1050, `percent-encoded`
  L1724, `round-trip` L2307, `800-126` L2378 and `otherwise-proscribed` L2419); runs of spaces
  collapsed; `{U+2014}` read as U+2014; the Symbol-font bullet U+F0B7 read as `•` or as absent, and
  the Symbol-font arrow U+F0AE as U+2192, as each file documents. A match had to be one contiguous
  run of the source, so a splice of non-adjacent text fails.
- **Locators.** A section map built from the headings of the layout text. A quotation counts as
  located only if it starts on the first line and ends on the last line its locator gives, inside
  the section the locator names, on the page it names. `normative.md`, `messages.yaml` and
  `design-notes.md` give the PDF page; `requirements.yaml`, `schema/` and `examples/` give the
  printed page with the PDF page in parentheses; each file states its convention.
- **Columns of code.** The four figures and every pseudocode listing were rebuilt from the PDF's
  content streams (decompressed with zlib; each text run placed at its `Tm` position, at 6.0 pt per
  character for the 9.96 pt Courier New of the figures and 6.6 pt for the 11.04 pt pseudocode; runs
  in the CID font decoded by glyph id, in the standard Macintosh order; glyph 215 is the one the
  text layer gives as U+02DC). This gives the columns the page prints, independently of
  `pdftotext`.
- **Pages rendered.** PDF page 17 (Figure 5-1, which sits in a box) and a 200 dpi crop of PDF page
  22 (the last alternative of Figure 6-1's `unreserved`, a raised small tilde).
- **Other sources**, fetched 2026-10-19 into the scratchpad (`fx1/cpe/dl-v/`): the XSD from the
  address §6 prints; RFC 2234 from rfc-editor.org (SHA-256 `dcaf7799…b9ca`); NIST IR 7697 (SHA-256
  `3e5b36aa…a592`, equal to library record `nistir-7697`); the archived CPE 2.2 specification that
  `schema/README.md` cites (SHA-256 `e3a3a806…a61d`, 38 pages, as the README says). tmodel was read
  only with `git show 1cb85b74:<path>` (origin/main, 2026-10-18, the commit `design-notes.md` cites).
- **Tools.** Python 3.13.9, PyYAML 6.0.3, jsonschema 4.26.0, poppler 26.07.0, Node v22.23.2 (used
  by the runner for its ECMA-262 check).

### Recount of the verbal forms

Uppercase keywords as `bin/_bcp14.py` matches them (longest first, so "MUST NOT" counts once, also
across a line break: "MUST" ends L654 and "NOT" starts L655); lowercase forms case-sensitive and
whole-word, "may not" counted once as "may not". By layout-text line:

| Region (layout lines) | MUST | MUST NOT | SHALL | SHALL NOT | SHOULD | SHOULD NOT | MAY | OPTIONAL | BCP 14 | must | should | may | may not | required | lowercase |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Front matter, pp. i to v (1-180) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 2 |
| §1 to §3 (181-457) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 3 | 1 | 0 | 6 |
| §4 Conformance (458-500) | 4 | 0 | 0 | 0 | 4 | 0 | 0 | 1 | 9 | 1 | 0 | 2 | 0 | 0 | 3 |
| §5 WFN data model (501-909) | 3 | 4 | 9 | 2 | 25 | 2 | 28 | 0 | 73 | 0 | 1 | 0 | 0 | 3 | 4 |
| §6 introduction and §6.1 (910-1795) | 6 | 0 | 4 | 0 | 2 | 0 | 1 | 2 | 15 | 3 | 2 | 1 | 0 | 2 | 8 |
| §6.2 (1796-2302) | 4 | 0 | 2 | 0 | 0 | 0 | 0 | 2 | 8 | 5 | 1 | 4 | 0 | 0 | 10 |
| §7 (2303-2340) | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 1 |
| Appendices A and B (2341-2443) | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 2 | 1 | 1 | 1 | 0 | 0 | 3 |
| **Whole document** | **18** | **4** | **15** | **2** | **33** | **2** | **29** | **5** | **108** | **12** | **6** | **12** | **1** | **6** | **37** |

The §1.3 key-words sentence (L252 to L254) holds 10 more uppercase keywords; `bin/bcp14-count`
strips it as boilerplate, and without the strip the count is 118 (the common brief's statement that
108 includes it is wrong, as the coordinator noted). No uppercase keyword stands in an example, a
figure, a table or a caption. There is no lowercase "shall", "shall not", "must not" or "should not".

| quantity | this recount | where it is recorded | result |
|---|---|---|---|
| BCP 14 keywords, `bin/bcp14-count` | 108 (SHOULD 33, MAY 29, MUST 18, SHALL 15, OPTIONAL 5, MUST NOT 4, SHALL NOT 2, SHOULD NOT 2); 118 without the strip | `requirements.yaml` `source_keyword_count`, `reconciliation` | equal |
| uppercase keywords in the 240 entry texts (`_bcp14.count` on the joined texts, as `bin/validate` does) | 106 | `extracted_keyword_count` | equal; the other 2 are the "MUST" and "SHOULD" of the Appendix B change log, L2405, as `reconciliation` says |
| occurrences accounted for by line and form | 145 of 145 (108 uppercase, 37 lowercase), plus the boilerplate sentence as one row of 10 | `keyword_accounting` | equal; each "extracted as" row's entry contains its form and its locator covers the line, and each entry holds exactly as many uppercase keywords as rows point at it |
| lowercase forms, by region | must 12, should 6, may 12, may not 1, required 6 (37) | `source_normative_forms` | equal in total and in every region |
| lowercase forms in entry texts, and excluded | 16 in texts (must 8, may 2, required 6), 21 excluded | `extracted_normative_forms` | equal |
| `normative.md` uppercase tally | 108 by section: 106 in statements, 2 excluded | "Verbal form tally" | equal in every section row |
| `normative.md` lowercase tally | must, should, may and may not: 31 (20 in statements, 11 excluded) | "Verbal form tally" | equal; it leaves out "required", so it now says how its 31 relate to the 37 of `requirements.yaml` (defect 16) |
| `normative.md` statements | 466, N-0001 to N-0466; 88 with uppercase keywords | "Statements by kind" | equal; every tag equals the forms in its own quotation, in order |
| `requirements.yaml` counts block | 240 entries; normativity, verb, kind, testable, text kind, 10 two-keyword entries, 15 also_at, 38 excluded | `counts` | equal |

### Defects found

Severity: **material** = a wrong or dropped requirement, a wrong count, a non-verbatim quotation or
a false claim; **minor** = locator, wording or format. Every fix keeps quoted text verbatim; no
requirement text, id or count changed.

1. **Material.** `schema/figure-5-1-avstring.abnf`, `figure-6-1-uri-v2.2-compatible.abnf`,
   `figure-6-2-uri-preferred.abnf`, `figure-6-3-formatted-string.abnf`. The headers said the bodies
   were the figures "character for character, checked against the rendered PDF page", but the runs
   of spaces inside each line were those of `pdftotext -layout`, not the page's: 118 of the 122
   figure lines (every non-blank line; only the 4 blank lines agreed) differed from the content
   stream.
   Evidence: Figure 5-1's `spec_chrs` line carries exactly five space characters before `=` in the
   PDF (runs of four and one at x 161.66 and 185.66), the file had nine; the figure lines at the
   page's columns are the code blocks `normative.md` already had. The non-space characters were
   identical. Fix: the four bodies rebuilt at the page's columns (now equal to `normative.md`'s
   figure blocks line for line); the header sentence corrected within the same number of lines, so
   the line numbers of `grammar_files.*.verbatim_parse_errors` in `examples/expected.yaml` still
   hold; the runner's figure check compares with runs of spaces collapsed; `schema/README.md`
   (method paragraph and the four SHA-256 values) and `examples/README.md` updated. ABNF meaning is
   unchanged.
2. **Material.** `requirements.yaml` R-0007, R-0104 and R-0173 said that every URI the binding
   procedure produces matches Figure 6-1. False when part or language is NA: NA binds to a hyphen
   (R-0151) that Figure 6-1 does not admit in those components (`part = "h" / "o" / "a" / empty`,
   `lang = LANGTAG / empty`), so `cpe:/-:foo` and `cpe:/a:foo:::::-` result (normative.md D-3;
   `messages.yaml` flags; design-notes defect 6; `schema/README.md` F-15; fixtures BIND-02 and
   URI-NEG-08, all of which said so). R-0151 and R-0144 did not mention it. Fix: the three notes
   corrected; a note added to R-0151; R-0144's list of failures extended.
3. **Material.** `requirements.yaml` R-0103 said the XSD "is an external document this record does
   not hold, so its patterns cannot be checked here" and that whether the URL resolves "was not
   checked". The record holds the file (`schema/cpe-naming_2.3.xsd`) and the address resolves (see
   judgement b). Fix: `testable_reason` and `notes` rewritten; `testable` stays partial because the
   text does not say which governs where the XSD and the figures disagree.
4. **Material.** `requirements.yaml` R-0159 and R-0168 said `bind_to_URI()` is "the only place" the
   order of the seven URI components is given. Figures 6-1 and 6-2 (`component-list`) and
   `unbind_URI()` give it too. Fix: both notes say "the only place in §6.1.2" and name the others.
5. **Material.** Twelve statements in eleven files (`normative.md`, `requirements.yaml`,
   `design-notes.md`, `messages.yaml`, `schema/README.md`, the four `figure-*.abnf` headers,
   `examples/README.md` and two in `examples/expected.yaml`) called NIST IR 7695 "a work of the
   U.S. Government, not subject to copyright in the United States". The PDF carries no copyright or
   licence notice, but the Acknowledgments (p. iii) place two of the three authors outside NIST
   (The MITRE Corporation and Scarfone Cybersecurity), so the whole text cannot be claimed as a U.S.
   Government work (17 U.S.C. 105 covers works of federal employees), and p. iii says "CPE is a
   trademark of The MITRE Corporation." Fix: each statement now says what is true, in the terms of
   the coordinator's updated brief; the `.abnf` headers keep two lines, so their line numbers hold.
6. **Minor (check 8a).** `messages.yaml` (3 quotations, 5 em dashes) and `design-notes.md` (1
   quotation, 2 em dashes) wrote the source's em dash as U+2014, while `normative.md` writes
   `{U+2014}`. Fix: see judgement c.
7. **Minor.** `requirements.yaml` R-0112: "Because Figure 6-1's unreserved includes the tilde, a
   packed edition matches here too", true only when the printed U+02DC is read as the ASCII tilde
   (R-0116). Fix: the note names the reading.
8. **Minor.** `requirements.yaml` R-0232 ("is copied from the URI version") and design-notes defect
   17 ("A helper documented with the other helper's words"): `get_comp_uri`'s comment does not
   contain the words "the string to the left of the first forward slash", so the claim of copying
   is unsupported. The defect itself holds (the words fit a URI, not a formatted string). Fix:
   wording.
9. **Minor.** `requirements.yaml` R-0102 ("an unbound WFN names every attribute") and the `wfn`
   flag in `messages.yaml` ("unbinding always returns the explicit form ... examples list ANY for
   every attribute"): a URI whose edition is not packed unbinds to seven attributes, and the
   §6.1.3.3 examples list seven. Fix: both say which attributes each procedure sets.
10. **Minor.** `requirements.yaml` R-0027: Figure 5-1 "admits only letters, digits, underscore,
    backslash and the listed punctuation" left out `*` and `?`. Fix: added.
11. **Minor.** `design-notes.md` (Reject-2, defect 13, evidence row P1) and the
    `formatted-string-binding` flag of `messages.yaml` gave `8..001` as "the" result of the printed
    `process_quoted_chars`. That is the reading of `idx = idx + 2.` as an assignment; read as a
    comparison, as `=` is used elsewhere in the pseudocode, the result is `8..0..6001`.
    `normative.md` D-9, `requirements.yaml` R-0222 and the examples give both. Fix: both readings
    stated.
12. **Minor.** `requirements.yaml` `excluded`, §6.2 paragraph 2 sentence 2: locator L1804-L1806,
    sentence on L1804-L1805. Fix.
13. **Minor.** `examples/expected.yaml`: four rule locators were not the lines of their text:
    `s5.3.2-asterisk-run` L655 (text on L655-656, and its three copies under `violates`),
    `s6.1.3-same-result` L1448-1451 (L1449-1451), `s6.2.2-same-result` L1879-1882 (L1880-1882),
    `s6.2.3-same-result` L2070-2073 (L2071-2073). Fix.
14. **Minor.** `normative.md`: the excluded-example ranges of §6.2.2.3 and §6.2.3.3 started after
    the sentence that introduces the examples (L1968, L2223-L2224), the only lines of the body no
    locator covered. Fix: ranges now L1968-L2051 and L2223-L2293.
15. **Minor.** `examples/README.md` and the first convention of `examples/expected.yaml` listed what
    the verbatim files leave out (labels, bullets, the comment marker) but not the explanation in
    parentheses after 12 of the 13 value strings of §5.3.2. Fix: added.
16. **Minor.** `normative.md`, "Verbal form tally": its lowercase total (31) was not reconciled with
    `requirements.yaml`'s (37, which also counts "required"). Fix: one sentence with the six lines.
17. **Minor, not fixed.** `distilled/README.md` is still the scaffold (TODO markers, and its title
    holds an em dash), and so is the title of `protocol.md`. README is pass 3's to write;
    `protocol.*` and `state-machine.yaml` stay scaffolds by instruction.

### Judgements asked for

- **(a) The `process_quoted_chars` reading.** The artifacts treat the defect consistently. The
  reference reading everywhere is the repaired one (`idx := idx + 2.` followed by `continue.`),
  which reproduces every printed example; the two literal readings are recorded beside it:
  `normative.md` D-9 (traced), `requirements.yaml` R-0222, and `run-fixtures.derived.py`, which
  computes `as_printed_assignment` and `as_printed_comparison` and marks the 14 fixtures where they
  differ (`pseudocode_as_printed: differs`, finding F-20; the 15th differing fixture, FS-POS-04, is
  the `get_comp_fs` reading, F-25). My own port of the pseudocode gives the same strings under all
  three readings. After defect 11 the design notes and `messages.yaml` state both literal readings
  too.
- **(b) NIST's XSD.** It is the file §6 points to: `http://scap.nist.gov/schema/cpe/2.3/cpe-naming_2.3.xsd`
  answered 301 to `https://scap.nist.gov/...`, then 301 to
  `https://csrc.nist.gov/schema/cpe/2.3/cpe-naming_2.3.xsd`, which returned 200 with 2254 bytes,
  SHA-256 `d37f813fe223922fb7456751d453482009fc7075a3f5ad5e1999d075d190dd69`, byte-identical to
  `schema/cpe-naming_2.3.xsd` (CRLF line ends; `appinfo` version 2.3, date 2011-07-29; server
  Last-Modified 2024-09-29). Its two patterns, XML entities decoded, equal the ones `messages.yaml`
  quotes. Recommendation: it belongs in the record, as the specification's own machine-readable
  schema: §6 calls it "the authoritative XML binding definition", FX-1 asks for a specification's
  own schema verbatim, and ECMA-427 holds its Annex A schema the same way. Three points for the
  human reviewer: it is not part of the PDF, so the record's content digest does not cover it and
  its provenance lives in `schema/README.md`; it carries no copyright or licence statement, and its
  `appinfo` names an author whom the PDF's Acknowledgments place at Booz Allen Hamilton, not NIST;
  and if the library prefers not to hold it, the URL and digest suffice and the runner can read a
  cached copy (`schema/README.md`, judgement call 1).
- **(c) Special characters (check 8a).** The library's convention, as ECMA-427's `normative.md`
  states it, is that the em dash is never written ("House style forbids that character in this
  library"): the source's dash is replaced by a documented substitute, and that replacement is the
  only deliberate departure from the source's characters. `normative.md`'s `{U+2014}` is such a
  substitute, and reversible, so all four artifacts now use it: `messages.yaml` and
  `design-notes.md` changed, with the convention stated in `messages.yaml`'s `note` and in the
  design notes' conventions; `requirements.yaml`'s `note` states it too (no entry text has an em
  dash). The verbatim checks read `{U+2014}` as U+2014 and still pass. The other special characters
  were already consistent and documented in each file: U+02DC kept as printed everywhere; curly
  quotes, U+2019 and U+2026 kept; the Symbol-font bullet U+F0B7 written `•` in `normative.md` and
  omitted in the list texts of `requirements.yaml` and `messages.yaml`; the Symbol-font arrow
  U+F0AE written U+2192 in `examples/` (and named in `messages.yaml`'s `note`).

### Checked and clean

- **Verbatim.** `requirements.yaml`: 240 of 240 texts, 55 enumeration items, 15 `also_at` and 38
  `excluded` texts (348 checks), each found as one run of the source, with its first and last line
  equal to its locator, in the section and on the page named; multi-line pseudocode and ABNF texts
  are consecutive source lines, so no splice. `normative.md`: 518 quoted paragraphs and fenced
  blocks; 194 of the 195 code blocks equal the PDF's columns exactly (176 at absolute columns, the
  18 Figure 5-1 rules relative to the figure's box), the other being N-0438, whose superscript
  ordinals are written on the line as its conventions say; the 33 rows of Tables 6-1 and 6-2 equal
  the printed pairs. `messages.yaml`: 164 `text` values with locators, the 31 and 2 table rows,
  and the two XSD patterns. `design-notes.md`: 68 quotations of NIST IR 7695, verbatim and located;
  55 quotations attributed to tmodel files, each in the file and section cited (`mapping.md`
  introduction, §2, §5, Table 6d, §10; `fanout-identity.md` headline 3, §1.5, §1.6, §1.7, §1.21,
  §2 dimension 7 Q5, §5, §10; `pilot.md` §2, §3; `report.md` §3, §4, §5; the LinkML schema;
  ADR-0004, 0007, 0008, 0010; APP-0001; PLAN-0002 §1; DECISIONS-0001; `spec/vectors/README.md`),
  and the unquoted claims citing `report.md` §1.2 and `fanout-tools.md` §1.4 hold; RFC 2234 §2.3 and §3.3 quotations verbatim. `schema/README.md`,
  `examples/README.md` and the comments of the eight `.abnf` files: every quotation of NIST IR 7695
  verbatim. `examples/expected.yaml`: 78 rules and 77 `violates` texts verbatim and, after defect
  13, exactly located.
- **Dropped statements.** Walked §1 to Appendix B, with every table, figure, caption, listing and
  example. Every line of the body (L181 to L2443) is now inside a `normative.md` statement, an
  excluded sentence, an excluded block or an excluded example range. 318 of the 466 statements map
  to a requirement entry or enumeration item, and every requirement text maps back to a statement
  (240 of 240). The 148 statements without an entry are definitions other than Bind and Unbind,
  scope, pointer and rationale sentences, lead-ins carried in `condition`, and pseudocode lines that
  restate extracted rules, which `requirements.yaml`'s stated rule leaves out; none carries an
  uppercase keyword, and every lowercase form among them is accounted for by line. Tables 6-1 and
  6-2 are enumerations of R-0155 and R-0156; all six captions are verbatim headings in
  `normative.md`; every sentence of the eleven §5.3.3 subsections has an entry (R-0065 to R-0099);
  the helpers `substr`, `is_alphanum`, `strchr`, `get_comp_uri` and `get_comp_fs` have entries and
  `strcat`, `strlen`, `reverse` and `to_lowercase` are excluded with reasons; the 89 ABNF rules of
  the four figures are 74 entries plus 15 `also_at`. Recorded for pass 3, not defects: N-0034 (the
  identifier and description decisions left to users, a stated non-requirement like R-0015 and
  R-0017) and the scope limits N-0037 and N-0038 have no entry; decode()'s pass-through of other
  unencoded characters (N-0346), the escape and special-character branches of transform_for_uri()
  (N-0299 to N-0301, which restate Tables 6-1 and 6-2) and process_quoted_chars' pass-through of
  unquoted characters (N-0420) are carried only by notes.
- **Classification.** `verb` is the first uppercase keyword of each text and `verbs` lists both
  where there are two (10 entries); `normativity` follows the verb in all 97 entries that have one;
  the 143 verb-none entries are constraint, definition, exemption or informative; every `testable`
  of no or partial has a reason (65); no entry is `inferred`, and none presents an inference as
  source text (readings sit in `notes`). Every cross-reference R-NNNN resolves.
- **Grammars.** The verbatim figures now equal the page (defect 1). Figure 6-1's last alternative is
  U+02DC in the text layer and glyph 215 of the CID font, and the page shows a raised small
  tilde; the four `=` that begin Figure 6-2's `pct-encoded` continuation lines are printed.
  Each derived file says DERIVED in its header, names the figure and sections it comes from and
  lists its repairs; the runner confirms each equals its verbatim figure token for token after the
  repairs, and that the verbatim files give exactly the recorded RFC 5234 parse errors.
  `wfn.derived.schema.json` is a valid draft 2020-12 schema and behaves as its README says on probe
  WFNs. The ten digests in `schema/README.md` equal the files. The CPE 2.2 claims of F-07 hold
  against the archived copy (Appendix A on PDF page 28: `string ::= ( ALPHA | DIGIT | PUNC ) +`,
  `PUNC` with `%` and `~`, no alternative with the type alone).
- **Structures.** `messages.yaml` against §5, §6 and the tables: the eleven attributes with their
  positions (URI components 1 to 7, the four extended attributes packed as parts 2 to 5 of the
  edition; formatted-string fields 2 to 12); the logical values (ANY as an empty component or `*`,
  NA as `-`); the character classes (28 punctuation characters, 31 characters allowed after the
  escape, one per row of Table 6-1, 29 of them percent-encoded and equal to Figure 6-2's list; the
  26 `punc` characters of Figure 6-3); the packed-edition layout; the language-tag subset; 8
  structures and 46 fields. Two wording defects fixed (9, 11).
- **Examples.** `run-fixtures.derived.py`, before and after the fixes, with `--source-text` on the
  text rendering: "177 fixtures; 15 where the pseudocode differs from the expected result (each has
  a finding); 0 problems", and 84 of 84 distinct WFNs agree with the JSON Schema. Independently, my
  own port of the pseudocode reproduces all 453 recorded binding, unbinding, conversion,
  round-trip and value-string results checked (both literal readings included), the 4 `undefined`
  outcomes differing only in the wording of their reasons; my own regular-expression translations
  of Figures 6-1 (ASCII tilde), 6-2 and 6-3 (case-insensitive and case-sensitive) and of the two
  XSD patterns reproduce all 405 recorded grammar verdicts, and of Figure 5-1 all 36 value-string
  verdicts. The 84 verbatim files reproduce their examples: 72 equal consecutive source lines after
  the documented removal of labels, bullets and the comment marker and the arrow substitution, and
  the other 12 (value strings of §5.3.2) equal the quoted part of their lines, the explanation in
  parentheses left out (defect 15). Derived expected
  results spot-checked against the text hold (for example URI-NEG-02, URI-NEG-08, URI-EDGE-02,
  FS-NEG-10, FS-NEG-13, FS-NEG-14, BIND-06, BIND-08, RT-04, RT-10).
- **Design notes, tmodel.** At `1cb85b74`: DECISIONS-0001 v0.1.8 (updated 2026-10-12) lists
  DEC-001a, 002, 003, 004, 005, 006, 007, 010 and 011 accepted by the ADRs the notes name, and
  DEC-001b, 008 and 009 open; ADR-0001 to ADR-0004 and ADR-0006 to ADR-0010 are `accepted` (there
  is no ADR-0005); APP-0001 is `draft`, the ARCH-0001 proposal `0.2.0-proposed.15`, RPT-0004
  `draft`. The LinkML `identifiers` slot (`range: string`, multivalued, on Product, ProductInstance
  and Component) carries the quoted description; `manufactured_by` and `supplied_by` are on Product
  only; `affects` ranges over Product. The six vectors carry 16 CPE strings (15 distinct), on 6
  Products and 10 Components and no ProductInstance, all double-quoted, 7 distinct ones with
  version NA; the Products, their purls, the ECU compositions and the log4j-core CPE are as
  stated.
- **Design notes, other sources and probes.** The NIST IR 7697 §6.2 sentence is verbatim in that
  PDF (the notes said "not checked"; they now say it was). Probes P1 to P9 reproduce with my own
  port, E9 with my own regular expressions for the XSD and Figure 6-3, E10 with PyYAML 6.0.3.
- **YAML parsing.** `bin/_yaml.py` and PyYAML give the same structure for `requirements.yaml` and
  `messages.yaml` apart from unquoted numbers read as strings (the known difference), and identical
  results for `expected.yaml`. A loader that rejects duplicate keys finds none in the three files;
  a structural diff against the pass-1 snapshot shows only the fields listed under the defects.
- **Validators**, before and after this pass: `bin/validate` 0 errors, 122 warnings, output
  identical; `bin/check-artifacts` 0 parse failures, 0 structural errors, 41 warnings, output
  identical (the three nistir-7695 warnings concern the `protocol.yaml` and `state-machine.yaml`
  scaffolds); `bin/check-requirements` 47 sets, 0 failures.

### Fixes, by file

- `requirements.yaml`: `attribution`; the TEXT convention in `note` (em dash); `notes` of R-0007,
  R-0027, R-0102, R-0103, R-0104, R-0112, R-0144, R-0159, R-0168, R-0232; a new `notes` on R-0151;
  `testable_reason` of R-0103 and R-0173; one `excluded` locator. No text, id, count or keyword
  changed.
- `normative.md`: `attribution`; two excluded-example ranges; one sentence in the lowercase tally.
  No quotation changed.
- `messages.yaml`: header comment; `note` (em dash convention); 3 quotations written with
  `{U+2014}`; the `wfn` flag on lossy bound forms; the `process_quoted_chars` flag.
- `design-notes.md`: `attribution`; the quotation convention; 1 quotation written with `{U+2014}`;
  Reject-2, defect 13 and evidence row P1 (both readings); defect 17's title; Reject-1's NIST IR
  7697 note.
- `schema/`: the bodies and two header passages of the four `figure-*.abnf` files (same line
  counts); `README.md` (provenance sentence, method paragraph, runner sentence, four digests). The
  derived files, `wfn.derived.schema.json` and `cpe-naming_2.3.xsd` are unchanged.
- `examples/`: `run-fixtures.derived.py` (figure-line check and its docstring); `README.md`
  (provenance sentence, value-string explanations, figure check); `expected.yaml` (header comment,
  `licence`, first convention, four rule locators and three `violates` copies). No fixture input,
  expected or actual result changed.
- `verification.md`: this section.

### Not-applicable declarations

As drafted for `record.yaml` (`fx1/cpe/not-applicable.md`; the coordinator records them):

- **protocol: correct.** NIST IR 7695 defines a logical name and two string bindings with
  single-party procedures; no parties, transport, sequence of messages or error path between
  parties. The quoted phrases are verbatim; one locator is loose: "for machine interchange and
  processing" is on L308, the second line of the Bind definition (L307-L308).
- **state-machine: correct as written.** "The WFN is a logical construct only." (L544); the
  pass-by-value bullet is L278; the `embedded` flags are L1533 and L2162; "deprecated" occurs once,
  L766.

### Not checked, or left open

- tmodel's tool runs (Syft, Grype, the NVD API, Dependency-Track) were checked only as quotations
  of its research files; the arXiv paper and Anchore's guidance were read only as those files relay
  them.
- RFC 5646 registry validity is not checked anywhere (well-formedness only, as the files say); the
  ECMA-262 compilation of the JSON Schema patterns rests on the runner's Node check, with no second
  engine; the PDF was read through one library (poppler) and the content streams.
- Judgement calls for the human reviewer: the repaired `process_quoted_chars` as the reference;
  readings P1 to P4 of §5.3.2 (`schema/`); F-13, that part may be ANY or NA; R-0197's lowercase
  "may" read as a permission; R-0020 (a MAY with "at most once") classed as a permission; keeping
  the XSD in `schema/` (judgement b); the `{U+2014}` notation (judgement c).
- Left for the coordinator and pass 3: `distilled/README.md` (scaffold, defect 17); the em dash in
  `protocol.md`'s scaffold title; `record.yaml` (`status: stub`, `bears_on`; design-notes open
  question 13); `constrained_by` in `messages.yaml` and the "Requirement ids: pending (pass 3)"
  lines of `normative.md`.
- No stray copies from file sync: `find records/nist/nistir-7695 -name '* [0-9].*' -o -name '* [0-9]'`
  found nothing.

## Pass 3: cross-check

By claude, a cross-check agent that took no part in passes 1 and 2. Effort: max. Date: 2026-10-19.
Scope: `requirements.yaml`, `messages.yaml`, `schema/`, `examples/`, `normative.md`, `design-notes.md`
and `distilled/README.md`. `record.yaml`, `summary.md` and the `protocol.yaml`, `protocol.md` and
`state-machine.yaml` scaffolds were not edited: protocol and state machine are not applicable, and the
coordinator records the reasons in `record.yaml` and removes the scaffolds.

### Method

- **Snapshot.** `distilled/` copied and the SHA-256 of all 219 files taken before any edit. After
  the pass, seven files differ (listed under "Fixes, by file"); `requirements.yaml`, every file of
  `schema/`, `run-fixtures.derived.py` and the 196 fixture files under `examples/verbatim/` and
  `examples/derived/` are byte-identical, so no verbatim text and no byte of the copied schema
  changed.
- **Edits by script.** Each edit was made by a scratch script that replaces whole placeholder lines or
  exact substrings, each asserted to occur once, and every file was written in place (same inode)
  except `examples/README.md`, edited through the editing tool. Scripts and intermediate files stayed
  in the session scratchpad (`fx1/cpe/xcheck/`) and are not committed.
- **Matching.** A `normative.md` statement maps to an entry when their line ranges overlap (the
  entry's locator or an `also_at` locator) and one text contains the other after whitespace is
  collapsed (`{U+2014}` read as U+2014, the bullet dropped); list items and the IN/OUT pairs of
  Tables 6-1 and 6-2 were matched to `enumeration` items one by one. Every statement whose lines
  overlap an entry without a text match was reviewed by hand.
- **Tools.** Python 3.13.9, PyYAML 6.0.3, jsonschema 4.26.0, Node v22.23.2, and the text rendering
  of the PDF (`pdftotext -layout`, poppler 26.07.0) for the few locators checked again.

### Check 1: requirements to messages and schema

Every entry's `object` and `field` were resolved:

| what the label names | entries | resolves to |
|---|---:|---|
| the WFN, its attributes, operations and notation (objects WFN, WFN operations, WFN notation, implementation internals, and R-0001's pseudocode semantics) | 52 | structure `wfn` and its eleven fields, `wfn-attribute-value-pair`, `logical-value` |
| a WFN attribute-value string and the Figure 5-1 rules (five of them also Figure 6-3, one, DIGIT, all four figures) | 40 | structure `wfn-value-string` and its three fields; `schema/figure-5-1-avstring.abnf` |
| the URI binding, its figures, its procedures and their inputs and results | 82 | `uri-binding` and its eight fields, `uri-packed-edition`; the Figure 6-1 and 6-2 files |
| rules shared by Figures 6-2 and 6-3 (unreserved, LANGTAG, language, region) | 4 | fields of both bindings and `binding-language-tag` |
| the formatted string binding, Figure 6-3, its procedures and results | 47 | `formatted-string-binding` and its thirteen fields; the Figure 6-3 file |
| both bindings at once: Bind and Unbind (§2.1), the two conversions and the round trip | 9 | `uri-binding` and `formatted-string-binding` |
| the XML binding of bound names | 1 | the `external_xsd_*` keys of both bindings; `schema/cpe-naming_2.3.xsd` |
| no structure: end-user documentation (R-0005), the GNU C pointer (R-0002), three pseudocode helpers (R-0171, R-0172, R-0191) | 5 | nothing to resolve |

Mechanically: all 74 ABNF entries name a rule that the verbatim file of each figure in their
`object` defines (89 checks with the 15 `also_at` copies), and each entry's `field` equals the rule
name of its text; every attribute named by a WFN entry is a field of structure `wfn`. No label was
wrong and none was changed.

### Check 2: constrained_by wired

- **Slots:** all 54 wired, none empty: 8 structures and 46 fields, 961 links (865 on fields, 96 on
  structures) to 229 of the 240 entries. 23 slots carry a `constrained_by_note`, which says where the
  entries at one of the slot's `constrained_by_locators` are wired when they bind another structure,
  or why an entry outside the locators was added. `constrained_by_locators` is unchanged, and the
  file's `note` now states the wiring rule.
- **Wiring rule.** The entries at the sections in `constrained_by_locators`, kept where the entry's
  object, field and text reach the slot; plus the entries that the field's own keys cite
  (`allowed_values`, `permitted_characters`, `encoding`, `case`, `logical_value_forms`,
  `binding_forms`, `required_source`). A binding or unbinding step is wired to every component whose
  permitted values it can act on (so Tables 6-1 and 6-2 are not wired to the URI part component,
  whose values are h, o and a). The §5.3.2 value-string rules sit on `wfn-value-string`, and each
  attribute field carries only the two lead-ins (R-0027, R-0028) that send its values there.
  Structure-level lists hold what binds a structure as a whole: grammar roots, order and
  separators, conformance and same-result requirements, and the conversions between the bindings.
- **Self-check.** Every requirement text that `messages.yaml` quotes inside a structure or a field
  is wired to that structure (or one of its fields) or to that field, with two expected exceptions:
  `uri-binding` quotes R-0152 and R-0153 as the context of §6.1.2.1.2, and they are wired to
  `wfn-value-string`, whose subject they are (the `uri-binding` note says so); and the quoted
  permissions R-0012, R-0147, R-0177, R-0219 and R-0224 constrain nothing (below).
- **Entries that constrain no structure (11), and why:**
  - R-0002: points to the GNU C library for the meaning of helper functions; names no structure.
  - R-0005: a duty on an implementation's documentation (the conformance claim).
  - R-0012: permits an implementation to offer the §7.2 conversion; whether a tool offers it is not
    a property of a name.
  - R-0136: Figure 6-2 defines `special = spec1 / spec2`, and no rule of the figure refers to it
    (`schema/README.md`, other observations), so it constrains no component.
  - R-0147, R-0177, R-0219, R-0224: it is OPTIONAL to follow the pseudocode; the results, which
    bind (R-0148, R-0178, R-0220, R-0225), are wired.
  - R-0171 (`substr`), R-0172 (`is_alphanum`), R-0191 (`strchr`): helpers observable only through
    the procedures' results, which are wired (R-0170 carries the effect of `is_alphanum`, R-0190 that
    of `strchr`).
- **Structure-level `constrained_by`** is an addition to the `messages` family, as in ECMA-427; the
  family's item keys are a loose superset, and `bin/check-artifacts` output is unchanged.

### Check 3: normative.md statements to requirements

All 466 statements: **321 map to entries** (332 statement-entry pairs), **145 give a reason**, and
**0 have neither**. Every one of the 240 entries holds at least one statement. The conventions
paragraph of `normative.md` now describes the lines.

| statements | how a statement maps |
|---:|---|
| 195 | the statement is the whole text of one entry |
| 54 | an `enumeration` item (§5.2 item 1, §5.3, §5.3.1, §5.3.3.1, §6.1.2.1, and the 33 pairs of Tables 6-1 and 6-2) |
| 36 | one of several statements that one entry holds (for example N-0160 to N-0164, R-0102) |
| 15 | a rule printed again in another figure, in the entry's `also_at` |
| 10 | the entry quotes part of the statement (a pseudocode step whose excerpt is shorter, the Bind definition, the §6.2 field template) |
| 8 | one sentence split into several entries (§4 items 3 and 4, §5.3.2 item 2, §5.3.3.10, §6.1.2.1.2, §6.1.2.2 step 3, §6.1.3 error checks) |
| 3 | a pseudocode step that shares one source line with an entry (N-0338 with R-0183, N-0361 with R-0190, N-0421 with R-0222) |

| reason there is no entry | statements | n |
|---|---|---:|
| the BCP 14 keyword-definition sentence | N-0001 | 1 |
| §2.1 definitions other than Bind and Unbind, and the abbreviation list | N-0009, N-0011 to N-0019, N-0021, N-0022 | 12 |
| other definitions and second names | N-0032, N-0045, N-0068, N-0087, N-0135 | 5 |
| notation conventions of the wfn:[...] illustrations | N-0047 to N-0050, N-0078, N-0080, N-0081 | 7 |
| lead-ins (carried or restated in the `condition` of the entries after them) | N-0005, N-0023, N-0024, N-0275, N-0279, N-0330, N-0457, N-0461 | 8 |
| structure of a summary ("END LOOP.") | N-0284 | 1 |
| pseudocode steps that restate an entry or only scaffold a loop; each binds through R-0148, R-0178, R-0220 or R-0225, which the reason names | N-0286, N-0289 to N-0297, N-0299 to N-0317, N-0319, N-0334, N-0339, N-0342, N-0344, N-0346, N-0347, N-0350 to N-0359, N-0363, N-0409 to N-0420, N-0424, N-0425, N-0437 to N-0441, N-0443 to N-0449, N-0454 | 74 |
| descriptive, scope, pointer and rationale sentences | N-0002 to N-0004, N-0031, N-0033 to N-0038, N-0041 to N-0043, N-0155, N-0165, N-0167, N-0169, N-0170, N-0188, N-0216, N-0219, N-0220, N-0229, N-0234, N-0235, N-0271, N-0274, N-0321 to N-0323, N-0364, N-0366, N-0373, N-0427, N-0430, N-0465, N-0466 | 37 |
| **total** | | **145** |

Pass 2 counted 318 statements with an entry; the 3 more are the line-sharing pseudocode steps.
Two reasons point at behaviour that no entry states but that binds through a same-result
requirement: `decode()`'s pass-through of other unencoded characters (N-0346, R-0178) and
`process_quoted_chars`' pass-through of unquoted characters (N-0420, R-0220). One reason records a
judgement call: N-0034 ("leaves all decisions about what distinguishes identifiers and descriptions
to the users") is a stated non-requirement like R-0015 and R-0017 but has no entry.

### Check 4: examples to requirements, and the runner

- **`requirements` on the 78 rules** of `expected.yaml`: 69 carry ids (88 links, 86 distinct
  ids); 9 have no entry and carry a `requirements_note` instead (`s5.1-logical-construct`,
  `s5.1-notation`, `s5.3.1-uppercase`, `s5.5-well-formed`, the four example sentences
  `s6.1.3.3.6-error`, `s6.1.3.3.7-tilde`, `s6.1.3.3.8-error` and `s6.2.3.3.3-error`, each naming the
  entries it illustrates, and the lead-in `s7.1-conforms`). Eight more notes explain partial
  matches (for example `s5.3-item2`, enumeration item 2 of R-0023).
- **`breaks` on the 77 `violates` entries** of 65 fixtures: 76 carry ids (78 links, 37 distinct);
  WFN-NEG-07 breaks only a notation convention, which has no entry, and says so. Where a rule spans
  several entries, `breaks` names the one the fixture's change reaches (AV-NEG-06, a space, breaks
  R-0032 of R-0030 to R-0032; AV-NEG-09 and AV-NEG-10 break quoted1, R-0055, BIND-NEG-02 quoted2,
  R-0056; URI-NEG-02 breaks R-0117 and URI-NEG-09 R-0116 of the four `fig-6-1-unreserved` rules).
  Every `breaks` id is one of its rule's `requirements`, and every break agrees with the fixture's
  expected verdicts. 14 `breaks_note`s mark a break that holds only under a stated reading (P1, P2
  and P4 of `schema/figure-5-1-avstring.derived.abnf`, the case-sensitive reading of finding F-06,
  the language-string reading) or that falls outside a permission (R-0020, R-0038).
- **Positives.** 112 fixtures have no `violates`. 101 expect only valid verdicts and successful
  outcomes. The other 11 are explained in the file: the five illustrations of §5 and §5.1, which are
  not WFNs (`expected_note`); SRC-6.1.3.3.7, valid under Figure 6-1, which R-0121 makes every consumer
  accept, and invalid under Figure 6-2, as the example's own text says (finding F-04); FS-POS-06 and
  BIND-09 (finding F-11); BIND-02, whose valid input binds through the report's own procedure to a URI
  that breaks R-0007 (finding F-15, normative.md D-3); BIND-03 (F-14) and BIND-04 (F-16). None
  breaks a requirement on its input; each non-valid verdict is a recorded source defect.
- **Runner.** `run-fixtures.derived.py` with `$PY -I` and `--source-text` on the text rendering, before
  the pass, on the new `expected.yaml` through `--expected`, and after it was installed: "177
  fixtures; 15 where the pseudocode differs from the expected result (each has a finding); 0
  problems", with 84 of 84 distinct WFNs agreeing with the JSON Schema. Without `--source-text` (no
  `.cache/` in this worktree) the result line is the same and the verbatim checks are reported as
  skipped. The runner reads only `id`, `rule` and `text` of the keys it checks, so the new keys
  change no result. `bin/_yaml.py` `parse` and PyYAML `safe_load` give identical objects for the new
  file, the check `examples/README.md` prints.
- **New conventions item** in `expected.yaml` explains the two keys and their notes; the old
  bullet's "Pass 3 (cross-check) is to add requirement ids" was removed. `examples/README.md` now
  mentions the keys.

### Check 5: protocol and state machine

Not done, by instruction: both are not applicable (no parties exchanging messages, no lifecycle),
the coordinator records the reasons in `record.yaml` and removes the three scaffolds, which this pass
did not edit.

### Check 6: design notes to requirements

96 edits put 201 requirement-id references (148 distinct ids, ranges counted in full) beside the
rules that `design-notes.md` argues from: every Adopt, Adapt and Reject item but Reject-4, which rests
only on scope statements that have no entry, 16 rows of the mapping table, the 21 source defects, the probe table of E8 and open
questions 11 and 12. The 51 ids placed beside a line locator were checked against the entry's section
and lines; all match. The scope and provenance bullet now states the convention. The quotations
were compared before and after: unchanged. Quotations left without an id have no entry: the §1.1
scope sentence, §3.2, the §5 scope statements and out-of-scope list, §5.1's "not intended to be a
data format", §6.1's "for backward compatibility with prior CPE versions", the lowercase advice of
§6.1.2.1.3, §6.2's rationale sentences (L1799, L1804), the example sentences, the change log, and
the quotations of NIST IR 7697 and of tmodel.

### Check 7: consistency between artifacts

- **Stale text fixed:** the `messages.yaml` `note` ("constrained_by is left empty in pass 1"), the
  `normative.md` conventions paragraph ("Each statement ends with "Requirement ids: pending (pass
  3)""), the `expected.yaml` conventions bullet ("Pass 3 (cross-check) is to add requirement ids"),
  the `design-notes.md` bullet ("Requirement ids ... are wired into both files in pass 3"), and
  `distilled/README.md`, which was still the scaffold (pass 2, defect 17): rewritten in full, with
  the coverage of every artifact and the provenance of NIST IR 7695, the XML schema, the two CPE 2.2
  grammar lines and the RFC 2234 quotations.
- **Coverage lines recomputed from the files:** normative.md 466 statements (89 ABNF rules, 33 table
  pairs, 106 pseudocode steps), D-1 to D-14, DEF-1 to DEF-22; requirements.yaml 240 entries, its
  `counts` block equal to the entries; messages.yaml 8 structures, 46 fields; examples 177 fixtures
  (65 printed, 112 derived), 84 verbatim files, 28 findings, 78 rules; design-notes 6, 6 and 6
  items, a 21-row table, 21 defects, E1 to E11, now 20 open questions.
- **Claims compared across files and found consistent:** the parse-error counts of the four figures
  (`schema/README.md` and `grammar_files`: 2, 9, 17, 8); Table 6-1's 31 entries and 29 percent forms;
  the 26 `punc` and 28 punctuation characters; the NA forms of part and language (normative.md D-3,
  design-notes defect 6, messages flags, findings F-15); both literal readings of
  `process_quoted_chars` in every file that states them; the `{U+2014}` convention; the XSD's digest
  and redirect chain; the 28 findings of `examples/README.md`.
- **Missing from the design notes:** six source disagreements that the other artifacts recorded and
  `design-notes.md` did not. Added as open questions 15 to 20 (check 8). No contradiction between two
  artifacts was found.

### Check 8: source questions recorded

Open questions added to `design-notes.md`, each routed to NIST and naming its requirement ids:

- 15: may `part` be ANY or NA (R-0065 against R-0021, R-0024, R-0107, R-0201; normative.md D-4,
  finding F-13).
- 16: a quoted hyphen followed by special characters, and a quoted underscore (R-0045, R-0051,
  R-0055, R-0222; findings F-11, F-17).
- 17: the robust-checking SHOULD against the same-result MUST (R-0176 against R-0178; R-0196 against
  R-0225; findings F-24, F-35, F-36).
- 18: Figure 6-1 against the CPE 2.2 grammar it says it shows (R-0121; finding F-07).
- 19: the prose summaries against the pseudocode (R-0163, R-0169, R-0180, R-0186, R-0187, R-0221,
  R-0222; normative.md D-13).
- 20: whether the lowercase forms bind (R-0197, R-0226, R-0234 to R-0236; normative.md DEF-22).

Defect 17 also gains the escaped-backslash ambiguity of `get_comp_fs` (R-0226, finding F-25).

### Fixes, by file

- `messages.yaml`: `constrained_by` on 54 slots (961 links), 23 `constrained_by_note`s, and the last
  sentence of the `note`. No other byte changed.
- `normative.md`: the 466 "Requirement ids" lines and the conventions paragraph. No quotation
  changed.
- `examples/expected.yaml`: `requirements` on 69 rules, 17 `requirements_note`s, `breaks` on 76
  `violates` entries, 14 `breaks_note`s, one conventions bullet trimmed and one added. No fixture
  input, expected or actual result changed.
- `examples/README.md`: the `expected.yaml` row of the file table.
- `design-notes.md`: 201 requirement-id references, the id convention, the escaped-backslash
  sentence of defect 17 and open questions 15 to 20.
- `distilled/README.md`: rewritten in full.
- `verification.md`: this section; the front matter's `by` and `passes` and the title.
- Unchanged: `requirements.yaml`, all of `schema/`, `run-fixtures.derived.py`, the fixture files,
  `record.yaml`, `summary.md` and the scaffolds.

### Validators and YAML

`bin/validate` 0 errors, 122 warnings; `"$PY" bin/check-artifacts` 0 parse failures, 0 structural
errors, 41 warnings (the three nistir-7695 warnings concern the `protocol.yaml` and
`state-machine.yaml` scaffolds, which the coordinator removes); `PATH="$VENV/bin:$PATH"
bin/check-requirements` 47 files, 0 failures. Each output is identical to the run made before this
pass (apart from a temporary directory name). `bin/_yaml.py` and PyYAML agree on `messages.yaml`,
`requirements.yaml` and `expected.yaml` once unquoted numbers and booleans are read as strings, the
known difference; `expected.yaml` agrees outright.

### What remains open

- **Judgement calls for the reviewer:** the wiring rule (binding and unbinding steps on every
  component they can act on; the §5.3.2 rules on `wfn-value-string` only; R-0001 on `wfn`, where
  `messages.yaml` quotes it under operations; the exemptions R-0015 and R-0017 and the informative
  claims R-0104, R-0144, R-0145 and R-0238 on the structures they describe; R-0092, R-0094 and R-0095
  on the bound language fields as well as on `wfn.language`); N-0034 left without an entry; the
  `breaks` that hold only under a stated reading or outside a permission.
- **Not checked:** the expected results of the 101 clean positive fixtures were not re-derived by
  hand; this pass relied on the runner and on pass 2's independent port. The PDF was re-read only
  where a locator was in doubt (L1938 to L1965 for defect 13, p. iii for the README). RFC 5646
  registry validity is not checked anywhere, as the files say.
- **Open questions 15 to 20** go to NIST, like questions 10 to 12; none was checked against a later
  revision, because none exists on the CSRC page (open question 10).

## Recording (coordinator, after pass 3)

- `record.yaml` now carries the `distillation` block (one coverage line per artifact, from pass 3's
  report), the not-applicable reasons for protocol and state machine (written in pass 1 by the
  messages and design-notes agent), the three passes at effort `max`, and `status: distilled` in place
  of the stub. It also adds the labels the extraction showed were missing: `bears_on` gains DEC-001a,
  DEC-005 and DEC-009 beside DEC-002 and DEC-008; `applicability`, `usefulness` and `implementations`
  are filled; and the role tag is `normative` in place of `prior-art`.
- The `protocol.yaml`, `protocol.md` and `state-machine.yaml` scaffolds that the passes above mention
  were removed: both are not applicable, and `record.yaml` says why.
- `summary.md` was rewritten from the stub by the coordinator, from the source's front matter and
  these artifacts.
