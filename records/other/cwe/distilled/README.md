---
record: cwe
kind: index
title: "cwe — distilled artifacts"
extracted: "2026-10-08"
reviewed_by: ""
---

# Distilled artifacts

FX-1 (`docs/extraction.md`). One line per artifact: what it covers, and what
it does not. Source: CWE XML Schema 7.3 (`cwe_schema_v7.3.xsd`, SHA-256
`690dedee…e45f98`), with the CWE List 4.20 XML (`cwec_v4.20.xml`) as observed
data. Pass 1 (extract) by two parallel agents (A: normative, requirements;
B: schema, messages, state machine, examples) and the coordinator (design
notes), 2026-10-08; passes 2 (verify) and 3 (cross-check) by an independent
agent C, 2026-10-08/09. Nothing here is human-reviewed yet.

| kind | file | coverage |
|---|---|---|
| normative | normative.md | All 111 `xs:documentation` texts and the `xs:appinfo` content, verbatim, with locators; every declaration rendered with type and cardinality; all 344 enumeration values; the source inconsistencies (D-01 to D-16). |
| requirements | requirements.yaml | 198 requirements: 85 prose (76 stated, 9 inferred) and 113 structural (every `use="required"`, every required particle, both required choices, 5 `xs:unique`, 2 wildcards). BCP 14 count 0 = 0; all 197 lower-case keyword occurrences accounted one by one. `cwe#R-0198` was added by the verify pass. |
| schema | schema/ | The source XSD, byte-identical, with its licence header; offline validation commands and results. No derived schema: the source is machine-checkable. |
| messages | messages.yaml | All 60 structures and 203 fields with type, cardinality, line and 4.20 counts; 35 enumerations; identity constraints; unchecked references. `constrained_by` links 191 of 198 requirements; the other 7 are listed with reasons. |
| protocol | protocol.yaml, protocol.md | Not applicable: a pure data format; the XSD defines no exchange. |
| state-machine | state-machine.yaml | Entry Status lifecycle (M1), the Mapping_Notes/Usage guard (M2), Content_History as an event log (M3); states, triggers, guards, with stated / inferred / observed marked. |
| examples | examples/ | 20 fixtures (13 verbatim from 4.20, 7 derived: 1 positive control, 6 negatives) with digests and actual xmllint results; 12 vectors for the formats the documentation gives; whole-catalog figures and 32 invariants for 4.20. |
| design-notes | design-notes.md | Adopt, adapt or reject against ARCH-0001, ADR-0004, DEC-001/002/003/008/009 and R-010/018/021/022, with open questions. |
| verification | verification.md | Passes 2 and 3: every check, how it was run, counts, defects fixed and residual issues. |
