---
schema: "library-distilled/v1"
id: etsi-en-304-223-verification
record: etsi-en-304-223
type: verification
updated: "2026-10-22"
---

# Verification — etsi-en-304-223

## Where this stopped (read first)

**Pass 1 (extract) is complete and committed** (`d6aa69b`, 2026-10-21).
**Passes 2 (verify) and 3 (cross-check) are started, not finished.** They ran as three independent
subagents at maximum effort (one verifier per record, one reviewer for the threat mapping and the
tmodel-decision claims in both records). The account usage limit stopped all three twice
(2026-10-21 ~20:50 and ~22:00 PT); their transcripts are saved and they resume where they stopped.
No defect had been reported when they stopped. Partial results seen:

- threat-mapping reviewer: 234 NIST and ATLAS ids across both records checked; 0 missing; every
  name matches ATLAS 2026.09 or the NIST E2025 index. It had moved on to reading each ATLAS
  description for fit.
- CISA verifier: `bin/bcp14-count` is 0 on every rendering of the PDF; it had started the
  word-by-word comparison of the capture against independent renderings.
- ETSI verifier: had re-derived the source text and was checking headings and pages.

Because passes 2 and 3 are not recorded in `record.yaml`, `bin/validate` reports exactly two
errors for this record ("pass 'verify' / 'cross-check' not recorded"). That is the true state.

**To finish:** resume the three verifiers, apply their must-fix findings, fill in the two pass
sections below, record `verify` and `cross-check` in `distillation.passes`, rerun
`bin/validate`, `bin/check-pr-extraction origin/main`, `bin/check-artifacts` and
`bin/check-requirements` (with and without `--invariants`), commit with `-s`.

## Pass 1 self-checks (extractor, 2026-10-21)

All scripted; scripts are in the session scratchpad, not the repo.

- Source PDF sha256 equals `content.sha256`; text rendered with PyMuPDF, page-marked.
- All 72 provision texts equal the complete source provision (whitespace-normalised), none
  truncated or spliced (`etsi_audit.py`).
- Whole-document modal counts and every exclusion: see `requirements.yaml` `reconciliation`.
- `normative.md` quotes are cut from the source by start/end anchors; the script fails on a
  missing anchor (`etsi_normative.py`).
- `threats.yaml` descriptions checked verbatim; ATLAS ids checked against ATLAS-2026.09.yaml from
  atlas.mitre.org; NIST ids against the E2025 index (`threats_build.py`, `etsi_build_fx1.py`).
- `bin/check-requirements` (LinkML) passes; `bin/check-artifacts` reports nothing for this record.

## Pass 2 — verify

Not finished; see above.

## Pass 3 — cross-check

Not finished; see above.
