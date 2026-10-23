---
schema: "library-distilled/v1"
id: etsi-en-304-223-verification
record: etsi-en-304-223
type: verification
updated: "2026-10-22"
---

# Verification — etsi-en-304-223

FX-1 passes 2 (verify) and 3 (cross-check), run 2026-10-21/22 by independent subagents at maximum
effort that did not extract: one verifier for this record, and one reviewer for the threat
mapping and the tmodel-decision claims (shared with `cisa-ai-in-ot-principles`). The account
usage limit interrupted them twice; they resumed from their saved transcripts. Every finding was
applied by the main session, and the checks were rerun after the fixes.

## Pass 1 self-checks (extractor, 2026-10-21)

All scripted (session scratchpad, not the repo): the source PDF sha256 equals `content.sha256`;
all 72 provision texts equal the complete source provision; whole-document modal counts with
every exclusion itemised in `requirements.yaml` `reconciliation`; `normative.md` cut from the
source by anchors; `threats.yaml` descriptions checked verbatim; ATLAS ids checked against
ATLAS-2026.09.yaml from atlas.mitre.org and NIST ids against the E2025 index.

## Pass 2 — verify

**Method.** The verifier re-derived the text from the PDF twice with PyMuPDF (`text` and
`words`), dropped page furniture, and compared with the extractor's rendering: pages 2–16 are
identical in all three, page 1 differs only in title-block order (no modal verbs). Its scripts
check every entry (verbatim, complete provision span, page, locator, principle, phase, parent,
verbs, normativity), every quoted item in `normative.md`, `threats.yaml`, the design-notes
tables and `requirements.md` row by row.

**Results.**

| check | result |
|---|---|
| `bin/bcp14-count` | 0, equals the header |
| source forms (verifier / header) | shall 61/61 · shall not 4/4 · should 32/32 · should not 1/1 · may 9/9 · can 22/22 · cannot 5/5 · will 7/7 · will not 1/1 · need not 1/1 · must 2/2, on all three renderings |
| extracted forms | shall 59 · should 29 · can 6 · cannot 2 · will 6 · others 0, equal to the header; clause 5 alone equals `verb_baseline` |
| exclusions | 43 occurrences outside the entry texts, all itemised in `reconciliation`, all non-normative |
| verbatim / complete provision | 73/73 verbatim; 72/72 complete provisions, C4-1 a whole sentence |
| designators, locators, pages | 72/72 designators; 73/73 locators and pages |
| normativity, actor, phase, parent | 73/73 (the 5.1.2-1.1 actor fix confirmed) |
| `normative.md` | 145/145 quoted items verbatim; 7 pages wrong (fixed, below) |
| `threats.yaml` | 17/17 descriptions verbatim, locators right, `addressed_by` equal to the set derived from `maps_to` |
| stated `source_text` | 24/24 occur in their entry's text |
| design-notes and `requirements.md` | every generated row matches the YAML |

**Defects found and fixed.**

| # | defect | fix |
|---|---|---|
| 1 | `normative.md`: 7 'Primarily applies to' lines (5.2.2–5.5.1) carried the page of the first identical line | generator now searches forward from the previous line; all 12 pages right |
| 2 | `verbs` missed `will` / `cannot` in 8 entries (5.1.1-2.1, 5.1.2-6, 5.1.3-2, 5.1.3-4, 5.2.4-2.1, 5.3.1-1, 5.4.1-1.1, 5.5.1-1) | lists completed; the note now says `verbs` lists every ETSI verbal form |
| 3 | `summary.md` described *should* provisions (5.1.3-1's threat-modelling clause, 5.1.4-1, 5.2.4-3) as requirements | rewritten to separate shall from should |
| 4 | `design-notes.md` said 5.2.4-3 "requires" a system-prompt audit log (it is a *should*) | corrected |
| 5 | the note's rule for `(implied)` actors was wrong for 3 of 5 entries; summary and README said "four" | rule restated per entry; "five" |
| 6 | design-notes said the EN describes two weaknesses; `threats.yaml` marks three stated | "three" |
| 7 | `threats.yaml` note defined `inferred` too narrowly | definition widened (requirement or recommendation negated, or the attack behind a named effect) |
| 8 | stated threat missing: unauthorized access to sensitive data (5.2.1-4) | added as T-14; counts updated to 14 |
| 9 | examples `not_applicable` reason missed 5.4.1-3's "for example" | added |
| 10 | four source defects not recorded in design-notes (5.2.1-4 cross-reference to 5.2.3; 5.2.1-4.1 cross-reference to 5.2.2 on open source; no 'Primarily applies to' for Principle 10; no References for Principles 10 and 13) | added to open question 4 |
| 11 | coverage text claimed every entry has `bears_on` and `maps_to` | now 60/73 and 33/73 |
| 12 | `normative.md` called §6 verbatim; C4-1 called a requirement | wording fixed |
| 13 | design-notes overstated 5.2.2-2 (rate limits are its example) and Principle 4 (oversight is 5.1.4-1 to 5.1.4-3) | wording fixed |
| 14 | 5.2.2-5 `testable_reason` named one of its two plans | both named |

**Checked and found correct** (things a reader might doubt): every itemised exclusion is real
and non-normative; the 5.3.1 NOTE ("is to be considered") is informative under the ETSI drafting
rules and rightly not a requirement; 5.3.1 has no 'Primarily applies to' and 5.5.1 no References
line; all five `not_applicable` reasons are true; the CISA guidance does list "ETSI TS 104 223".

## Pass 3 — cross-check

Every id cited in the record's ten files resolves; every count quoted in `README.md`,
`summary.md`, `record.yaml` and `design-notes.md` matches the files after the fixes;
`requirements.md` matches the YAML row by row (73 rows, 14 section headers); `addressed_by` in
`threats.yaml` equals the derived set. Schema, messages, protocol and state machine are not
applicable (reasons in `record.yaml`), so the FX-1 field-by-field cross-checks between them have
nothing to compare; the cross-check is between requirements, normative text, threats and design
notes.

## Threat-mapping and design-notes review

**Not finished.** The reviewer checked all 234 NIST and ATLAS ids in both records (0 missing; every
name matches ATLAS 2026.09 or the NIST E2025 index) and was reading each ATLAS description for fit
when the usage limit stopped it a third time (2026-10-22). Its findings are applied when it
reports; until then `verify` and `cross-check` are not recorded in `record.yaml`.

## Checks after the fixes

After the verifier fixes (2026-10-22): `bin/check-requirements` (with and without
`--invariants`) 47/47 valid, no warnings for this record; `bin/check-artifacts` no warnings for
this record; `bin/validate` reports only the two unrecorded passes.
