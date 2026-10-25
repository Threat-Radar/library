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

**Method.** An independent reviewer read every `provenance: ours` mapping in both records against
the entry text, the NIST AI 100-2 E2025 definitions (`.cache/nist-ai-100-2e2025.txt`) and the
ATLAS 2026.09 technique descriptions, using ATLAS's own mitigation relations (`AML.M*`) as a
cross-check on fit; recomputed every design-notes table; and checked every claim about tmodel
(`origin/main` = `e1ae8c3`, tmodel#130 = `f57386c`), the OTM schema (`c88c5a7`) and CWE 4.20.
Across both records: 240 id occurrences (49 distinct: 34 ATLAS, 15 NIST), 0 missing, 0 name
mismatches; 155 mappings read; 0 stated `source_text` outside its entry (the 10 found at pass 1
had already been fixed by the verify pass). Findings: 2 wrong, 21 weak, 11 notes, all applied
except where noted below.

**Applied to this record.**

| finding | change |
|---|---|
| wrong: 5.1.4-5 mapped to NISTAML.04 although informing users of prohibited uses is not an attack defence | now non-adversarial; the Misuse row is gone |
| wrong: 5.4.2-4 paired AML.T0031 (adversarial inputs) with poisoning | AML.T0020 + AML.T0018.000 (ATLAS M0008), plus a non-adversarial drift mapping |
| 5.2.1-4.1 is training-data hygiene (ATLAS M0007), not a prompt-injection control | prompt-injection mappings removed; CWE-1427 link dropped from the notes |
| 5.2.1-4 names its risk | `inferred` → `stated` ("against unauthorized access") |
| 5.5.1-1 → NISTAML.038 was a stretch | conventional, AML.T0035 only |
| 5.2.2-2 parses two ways; AML.T0040 is the access route, not the attack; rate limits also counter DoS | extraction mapping `inferred` with the ambiguity stated; T0040 dropped; availability (NISTAML.01; AML.T0029, AML.T0034) added |
| unmapped named risks: 5.2.1-3 "specific attacks aimed at AI systems"; 5.3.1-2.1 "failure modes" | `general` and non-adversarial, both stated |
| W-04 (residual risk) is not a weakness | removed; three weaknesses, each with a candidate CWE id (inferred) |
| 5.1.3-1.2, 5.1.2-6, 5.1.2-2, 5.4.2-1 missed direct prompt injection | added (inferred) |
| 5.2.3-3 carried a poisoning id under supply chain | NISTAML.023 dropped (NISTAML.051 covers it) |
| 5.2.5-4 `source_text` named no attack; 5.5.1-2 used an agent-only technique | wording fixed; AML.T0055 in place of AML.T0083 |
| design notes: CWE "no entry"; C1 misread; CVE claim stated as the EN's; 5.4.1-1.1 called `accepted_risk`; roles "on the relation" (no such slot); `catalog_ref` single-valued; M5 conflated; permissions slot | each corrected; open questions split from source notes, three added (catalog_ref, CWE ids, ThreatInstances for non-adversarial items) plus library records for NIST and ATLAS |

**Not applied, and why.** The reviewer asked for one class per ATLAS id across both records (e.g.
AML.T0018 is supply-chain in one mapping, poisoning in another). The class here belongs to the
mapping, not to the id: the same technique is a supply-chain attack when it arrives through a
supplier and a poisoning attack when it happens in-house. Recorded as open question 7 (derive
mappings from ATLAS mitigation relations) instead of forced.

**Survived review** (selection): 5.1.3-1 (model inversion → NISTAML.032 per §2.4.1), 5.1.2-2
evasion, 5.1.2-3, 5.1.2-4/-7, 5.2.1-2, 5.2.3-*, 5.2.4-*, 5.2.5-4.1, 5.4.2-2, and every claim about
ADR-0006, ADR-0010, DEC-008, R-018, tmodel#130, OTM and the CWE entries.

## Checks after the fixes

Run 2026-10-22 on the final state of this commit:

| check | result |
|---|---|
| `bin/validate` | 0 errors; no warning names this record |
| `bin/check-pr-extraction origin/main` | "FX-1: every record this PR extracts is complete" |
| `bin/check-artifacts` | 0 parse failures, 0 structural errors; no warning names this record |
| `bin/check-requirements` | 47 / 47 sets valid, 0 failures |
| `bin/check-requirements --invariants` | 47 / 47 valid; no invariant warning names this record |

