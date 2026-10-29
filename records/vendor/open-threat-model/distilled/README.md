---
record: open-threat-model
kind: index
title: "open-threat-model — distilled artifacts"
extracted: "2026-10-13"
reviewed_by: ""
---

# Distilled artifacts

FX-1 (`docs/extraction.md`). One line per artifact: what it covers, and what
it does not.

**Sources.** `iriusrisk/OpenThreatModel` at commit `c88c5a7b` (2025-12-11):
- the specification `README.md` (SHA-256 `4acfb48b…ef78cf8c0`, CC BY-SA 4.0);
- the schema `otm_schema.json` (SHA-256 `81e7f5a5…545eef0c`, Apache-2.0,
  `$id` otm-0.2.0);
- `EXAMPLE.json` and `EXAMPLE.yaml`, plus `CONTRIBUTING.md` for versioning.

**Passes.**
- Pass 1 (extract), 2026-10-13/14, two parallel agents and the coordinator:
  - A: normative text and requirements;
  - B: schema, messages, state machine and examples;
  - coordinator: design notes and `constrained_by` linking.
- Passes 2 (verify) and 3 (cross-check), 2026-10-14/16, by an independent agent C (`verification.md`).

Nothing here is human-reviewed yet.

| kind | file | coverage |
|---|---|---|
| normative | normative.md | The README's normative text, verbatim with line locators, in source order: Versions, Format, Data Types, and every object's field table, all rows, with REQUIRED cells. The schema's normative content by JSON pointer. A README-vs-schema comparison for every field. Source defects D-01 to D-32. The README's introduction is purpose text and is not extracted as rules. |
| requirements | requirements.yaml | 287 requirements: 110 prose (97 stated, 13 inferred) and 177 schema (every `type`, every `required` entry, `$ref`, `oneOf`, `$schema`). BCP 14 count 51 = 51 (REQUIRED 50, RECOMMENDED 1). Every lower-case keyword and every schema `required` is accounted for in `keyword_accounting`. Defects D-01 to D-32. |
| schema | schema/ | `otm_schema.json` byte-identical to the source, keeping its Apache-2.0 notice. A **derived** strict profile, `otm-0.2.0.derived-strict.schema.json`, adds 36 README rules (S-01 to S-36), each citing its README line. Offline validation commands and results. Notes that a different, weaker schema text carried the same 0.2.0 `$id` before 2024-01-31. |
| messages | messages.yaml | 26 structures named as their README headings, 120 field entries: README and schema type, required in each, constraints, references, JSON pointer and lines, and occurrence in EXAMPLE.json. Also encodings, identifier scheme, 12 unchecked references, derived cross-reference checks XR-01 to XR-10, extension points, and README-vs-schema mismatches M-01 to M-16. `constrained_by` links 275 of 287 requirements, and all 120 fields; the other 12 are listed with reasons. |
| protocol | — | Not applicable: a pure data format; the source defines no exchange between parties. |
| state-machine | state-machine.yaml | No lifecycle is defined in the source. M1 is threat-instance `state` and M2 mitigation-instance `state`: values observed only in examples, transitions inferred and flagged. M3 is the specification's version lifecycle (semver, stated; the next-major change announced at L1139; releases from git history). |
| examples | examples/ | 49 fixtures: 23 README `#### Example` blocks verbatim, `EXAMPLE.json` and `EXAMPLE.yaml` verbatim, and 24 derived negatives (11 the source schema catches, 9 only the strict profile catches, 4 only the XR checks catch). The 86 Examples-column snippets as vectors. Actual jsonschema 4.26.0 results under both schemas. 7 README examples fail as published: 6 under the source schema (D-25 to D-28), 1 only under the strict profile (D-07). |
| design-notes | design-notes.md | Adopt, adapt or reject against tmodel ADR-0010 (DEC-001a classes), ADR-0007 (OTM import), ADR-0006, ADR-0004 and R-005/010/018/020/021. G13: no target class for `assets`, `trustZones` or `dataflows` (the report records the sponsor's 2026-10-14 direction to add them, pending an ADR amending ADR-0010); related gaps listed, no classes proposed. Open questions. |
| verification | verification.md | Passes 2 and 3: every check, how it was run, counts, defects fixed and residual issues. |
