---
schema: "library-verification/v1"
id: iso-sae-21434-2021-verification
record: iso-sae-21434-2021
type: verification
updated: "2026-11-13"
by: "Claude Code"
reviewed_by: ""
passes:
  - verify
  - cross-check
scope: full
---

# iso-sae-21434-2021: FX-1 pass 2 (verify) and pass 3 (cross-check)

Both passes ran on 2026-11-13 for tmodel#154, at maximum effort, each in a separate run that took
no part in the passes before it. They worked read-only and reported; the fixes were then applied
to the artifacts and re-checked. ISO/SAE 21434 is a licensed standard, so this page quotes none of
its text; findings point to clause, table and figure ids.

## Pass 2: verify

### Method

- **Source.** The purchased PDF, re-hashed: SHA-256
  `73f990078d3a5b47dec91dd0d2b4e6c24cecd9e4160ae5b143c3b3fa80b7cdf4`, 87 pages, equal to
  `source_digest`. Text from `pdftotext -layout`; the verifier's own extraction of every provision
  kept the NOTE and EXAMPLE paragraphs, so a list that continues after one could not hide. Figures
  and merged-cell tables were read from rendered page images (Figures 2, 3, C.1, D.1, E.1 and H.1 to
  H.3; Tables E.1 to E.4, G.6, G.7 and H.2 to H.11).
- **Meaning, not string equality** (docs/extraction.md, Licensed standards): for each paraphrase,
  the actor, condition, action, objects, list items and force (shall, should, may) against the
  provision.
- **Copy check.** Every string of every new file, and of `requirements.yaml`, against the standard:
  the longest run of words shared with it, and word-sequence (LCS) closeness to the best-matching
  passage, flagged at a run of 6 or more words or a closeness of 0.70 or more, then judged by hand
  (names, labels, clause and table ids and references are allowed). A by-eye hunt looked for
  synonym swaps that keep the standard's word order, which neither measure catches.

### Result: 2 must-fix, 11 should-fix, 28 optional

What held: all 118 paraphrases keep their provision's meaning, including the 13 lists that a NOTE
or EXAMPLE interrupts; all 160 locators, verbs and normativity values; every cross-reference in
`refs`; all 42 work products against their subclauses and Table A.1; the keyword reconciliation
(0 and 0); the 13 edges of Figure 3; about 380 annex values and labels, merged cells included;
the hand-worked test vectors; and the three `not_applicable` reasons.

Findings and how each was resolved:

- **Must-fix.** (M1) The 18 untagged Prerequisites lists, which the Introduction makes mandatory
  inputs, were carried nowhere: `normative.md` §8 now lists the inputs of all 24 activity
  subclauses. (M2) The Table E.4 penetration-testing parameters described the testers; they
  describe the attacker the test assumes, and `annex-e-cal.yaml` now says so.
- **Should-fix.** Source notes added for item and vulnerability (§3); the work-product count in §4
  corrected, and the 56 provisions that feed a subclause-level work product now name it in
  `verification`; the TARA modules described as runnable in any order (§2); scope, Clause 4, the
  objectives of every clause and the figures added (§6, §7, §9); same-order paraphrase removed, the
  annex data now held as structured fields (actor, action, target; level, access, typical case)
  and 13 definitions reframed; the formula comparison labelled unrounded; two state-machine labels
  corrected and Figure 2 cited; the annex EXAMPLE count corrected to 26; Figure 3 no longer called
  normative; 30 `actor` fields corrected (two more in pass 3); the passes recorded.
- **Optional.** Applied, among them: three definitions tightened; the dropped Annex B pairing and
  the Annex G expert trait restored; the out-of-context wording in Annex E; Other ECUs placed
  outside the environment in Annex H; vector sources marked stated or inferred; one more Annex H
  gap and the Figure H.3 word swap recorded; a CVSS test vector in the low band added (59 vectors,
  108 checks); the design notes' Q1, D1, D6 and A2 sharpened; the 6.3.2 work-product id defect
  recorded; tailoring limited to project activities (Clause 5 and RQ-14-01 are not tailorable);
  RQ-05-01 (define, not have) and RQ-11-01 (considering, not done with) corrected; 11 older texts
  whose closeness sat at the 0.70 line reworded; eight bibliography entries completed.

Left open:

- **The closeness bar for older text.** `requirements.yaml` still holds paraphrases from earlier
  work that keep the standard's word order below the 0.70 closeness bar set on 2026-11-08. Whether
  that bar is strict enough is for the record's owner (@Clovier) and the sponsor to decide.

## Pass 3: cross-check

### Method

`requirements.yaml` against its work products in both directions; `requirements.md` against the
YAML row by row; `normative.md` against the catalog (the §2 table, the §4 counts, every work
product in §8, the objectives that provisions cite, the §5 summaries against `examples/`); both
state machines against the provisions and §8; the annex data against the provisions it
illustrates; every claim in `design-notes.md` about tmodel against tmodel `main` at `b0604a4`
(ARCH-0001, the ADRs, the decision register, the schema, RPT-0007, the RPT-0017 extraction file,
and the open engine PR tmodel#229); `record.yaml`, `summary.md` and both READMEs against the files
and each other.

### Result: 5 must-fix, 11 should-fix, 17 optional

What held: the 47 / 56 / 15 split of provisions by work product; every `verification` text that
names a subclause-level work product; `requirements.md` against the YAML; all 24 rows of §8 against
the licensed copy; the state machines' structure, locators and stated labels; the annex data
against RQ-15-04, RQ-15-05, RQ-15-10, RQ-15-16, RC-15-11 to RC-15-14, PM-06-08, RQ-09-10 and
RQ-06-27; tmodel#229's risk table against Table H.8, cell for cell; and the counts repeated across
files.

Findings and how each was resolved:

- **Must-fix.** (M1) The design notes now take tmodel's decisions from ARCH-0001 §8: DEC-001a is
  amended by ADR-0011 and ADR-0012, and DEC-001b is partly accepted by ADR-0013 (the decision
  register lags on both). (M2) RPT-0017 converts 42 of the 49 in-scope provisions on tmodel `main`;
  tmodel#239 adds back the other seven. (M3) A road user is not `RiskScore.for_stakeholder`, which
  names an asset owner; tmodel has no road-user object. (M4) Every catalog entry now carries `kind`
  (all stated) and `testable` (92 yes, 22 partial with a reason, 4 permissions no). (M5) The passes
  are recorded.
- **Should-fix.** §4's model line now uses tmodel's accepted names (`SdlPractice`, `Evidence`); the
  design notes no longer map work products onto `EvidenceKind` and ask how an audit would link them
  (Q6); the summary no longer counts function and cybersecurity requirement as Clause 3.1 terms;
  RQ-05-07 and RQ-05-08 also point to WP-05-01; `requirements.md` shows the subclause-level work
  products, so "none" marks only the 15 that have none; the catalog's provenance records this day's
  changes; the untagged Prerequisites are counted where the tags are; the schema N/A reason says
  tmodel covers only part of Figure 3; the single-valued `realizes_damage` and `realizes_threat` are
  named; `bears_on` gains DEC-001a, DEC-001b, DEC-008, R-013 and R-018; §10 gains rows for Clause
  3.2, the NOTEs and the EXAMPLE notes.
- **Optional.** All applied but one, among them two more Annex H caveats, the §2 table's
  method provisions, the CAL wording (can be set, meant to stay fixed), R-019 for impact, and two
  bibliography URLs.

Left open:

- **On the tmodel side, not in this record.** tmodel's decision register lags ARCH-0001 on DEC-001a
  and DEC-001b, and the schema header and the `AttackPath` and `RiskScore` descriptions still call
  DEC-003 open, although ADR-0006 accepted it.

## Checks after the fixes

- `bin/validate`: 0 errors on this record.
- `bin/check-requirements`: 52 sets, 0 failures. `bin/check-artifacts`: 0 errors, no warning on
  this record. `bin/test_yaml.py`: 15 of 15.
- `examples/run-fixtures.derived.py`: all 108 checks pass.
- Copy check: no sentence of the standard anywhere; the remaining flags are names, labels, ids,
  references, the CVSS formula and lines that predate this work.
- Not done here: pass 4. Each artifact's `reviewed_by` is empty until a person reviews it.
