---
record: osv-schema
kind: index
title: "osv-schema: distilled artifacts"
extracted: "2026-10-18"
reviewed_by: ""
source_version: "OSV Schema v1.9.2 (October 13, 2026), github.com/ossf/osv-schema tag v1.9.2, commit c8a57bdc5b0bc54646e140cabbb7834bd0b5aec9"
source_digest: "96d82f03d763fb408bc344d01fc271f761a81cc225f6f6a42d318e3ed21cebff"
attribution: "Contains text from the OSV Schema v1.9.2 (github.com/ossf/osv-schema, tag v1.9.2: docs/schema.md, validation/schema.json, proto/vulnerability.proto), licensed under the Apache License, Version 2.0; see Licence and attribution below."
---

# Distilled artifacts

FX-1 (`docs/extraction.md`) for the OSV Schema, the Open Source Vulnerability
format, version 1.9.2 (October 13, 2026), pinned at tag `v1.9.2` (commit
`c8a57bdc5b0bc54646e140cabbb7834bd0b5aec9`) of github.com/ossf/osv-schema. Three
files of that tag were read; none is committed except the two schema files that
`schema/` copies byte for byte:

| file | role | SHA-256 |
|---|---|---|
| `docs/schema.md` | the specification (2010 lines); `Lnnn` in every artifact is a line of this file | `96d82f03d763fb408bc344d01fc271f761a81cc225f6f6a42d318e3ed21cebff` |
| `validation/schema.json` | the JSON Schema (draft 2020-12) the specification offers "for validation" | `15b10dbb4c4e31c7aae11d22cdd991a9a374758db7c8389e62b3cc37cac92653` |
| `proto/vulnerability.proto` | the protobuf definition, which says it is not stable | `1c5a7af863c576398e333358c006d30577dd111c810416cd2f3fc0cecd20a070` |

The repository's root `schema.md` only points to the published page.

How to read the verbal forms: the OSV Schema writes its rules in lowercase
("must", "should", "may", "required") and uses no BCP 14 capitals, so
`bin/bcp14-count` finds 0. `requirements.yaml` therefore reconciles against the
document's own lowercase baseline: 74 occurrences of must, must not, should,
should not, may and required, each accounted for by line.

| kind | file | coverage |
|---|---|---|
| normative | normative.md | 384 numbered statements, verbatim, in source order under the source's headings: 317 from `docs/schema.md` (191 quoted passages and fences, 126 table rows and list items: the 47 prefix rows, the 52 ecosystem rows, the severity type and source rows, the reference and credit types), 31 JSON Schema constraint statements with their JSON Pointers and 36 proto statements; 75 excluded passages with reasons; a verbal-form tally per region; disagreements D-1 to D-25 and unclear points U-1 to U-28. Every statement's `req` names its requirement ids or the reason it has none (pass 3: 319 statements map to 391 links; 65 have none: 36 proto, 12 field blocks, 15 explanatory prose sentences, 2 unreferenced `$defs`). |
| requirements | requirements.yaml | 237 entries `osv-schema#R-0001` to `R-0237` (requirement 26, prohibition 5, recommendation 43, permission 24, constraint 135, informative 4; 1 inferred): 224 from `docs/schema.md` and 13 from `validation/schema.json` where it differs from or adds to the prose. BCP 14: source 0, extracted 0. All 74 lowercase occurrences are accounted for by line (68 in entry texts, 6 excluded as non-normative), and 43 occurrences of recommended, optional, allowed and similar words. Field types are carried in `messages.yaml`; the proto is not extracted (`normative.md` carries it). |
| schema | schema/ | `osv.schema.json` and `vulnerability.proto`: the source's `validation/schema.json` and `proto/vulnerability.proto`, byte-identical. `osv-prose.derived.schema.json`: rules P01 to P12 (36 checks), stated rules neither verbatim file enforces, reported as errors; `osv-recommended.derived.schema.json`: rules S01 to S10, should and recommended statements, reported as warnings. `schema/README.md`: provenance, 36 disagreements D1 to D36 between the three sources, readings R1 to R13, the requirement ids of every P and S rule, and the stated rules no schema here expresses, with reasons. |
| messages | messages.yaml | 13 structures and 47 fields (the record, severity, affected, package, range, event, reference, credit, the four open `*_specific` objects, and the deprecated proto-only `Commit`), with type, required-ness, format, allowed values and locators from the prose, the JSON Schema and the proto side by side, and disagreements D1 to D36 where they concern a field. `constrained_by` (pass 3): 428 links on 44 of the 47 fields and 54 on 12 of the 13 structures, reaching 231 of the 237 requirements; the 6 others and the proto-only `Commit` are explained. |
| protocol | (not applicable) | See `record.yaml` `distillation.not_applicable`. |
| state-machine | state-machine.yaml | Two machines: `range-evaluation`, the `IncludedInRanges` and `BeforeLimits` pseudocode (6 states, 10 transitions, error state `invalid-range`), and `record-lifecycle`, the authority of the later-modified copy and withdrawal (4 states, 14 transitions, each marked stated or inferred). Pass 3 added 8 named events, each tied to the `messages.yaml` structure or field it involves; every transition names its event and its `constrained_by` requirement ids. |
| examples | examples/ | 224 fixtures: the source's 34 fenced blocks and 54 inline examples byte for byte, 10 source examples placed in a record, 23 positives, 34 negatives, 41 records the prose forbids and the JSON Schema accepts, 3 the reverse, 10 broken recommendations, 12 edge cases (10 left unspecified) and 3 tool cases. Expected results come from the prose; actual results from jsonschema 4.26.0 with and without a format checker (47 tool differences, each with a finding). Each of the 109 quoted rules carries the ids of the entries whose text it quotes (9 narration and rationale rules have none, and say why), and every violated rule names the ids the fixture breaks (pass 3). `run-fixtures.derived.py` reproduces every result. |
| design-notes | design-notes.md | How OSV bears on tmodel: 7 adopt, 8 adapt and 7 reject items, each grounded in quotations and mapped to a DEC or ADR with its status; a 30-row mapping table from OSV structures to tmodel's accepted core; 22 source defects; evidence E1 to E13 from tmodel's research and this extraction's probes; 14 open questions routed to their owners. Pass 3 added the requirement id beside each cited passage that has an entry (262 ids, 135 distinct). |
| verification | verification.md | The verify and cross-check record (passes 2 and 3). |

Files the library wrote rather than copied from the source carry `.derived.` in
their name, or say so in their first lines. The other files of this directory
are the library's own text, with quotations from the three source files marked
as such.

## Licence and attribution

Contains text from the OSV Schema v1.9.2: `docs/schema.md`,
`validation/schema.json` and `proto/vulnerability.proto` of
github.com/ossf/osv-schema at tag `v1.9.2` (commit
`c8a57bdc5b0bc54646e140cabbb7834bd0b5aec9`), licensed under the Apache License,
Version 2.0. A copy of the License is at
<https://www.apache.org/licenses/LICENSE-2.0>; the repository's own `LICENSE`
file is that licence.

- `schema/osv.schema.json` and `schema/vulnerability.proto` are unmodified
  copies of `validation/schema.json` and `proto/vulnerability.proto`. The proto
  keeps its own header, reproduced here verbatim:

  ```proto
  // Copyright 2025 Google LLC
  //
  // Licensed under the Apache License, Version 2.0 (the "License");
  // you may not use this file except in compliance with the License.
  // You may obtain a copy of the License at
  //
  //      http://www.apache.org/licenses/LICENSE-2.0
  //
  // Unless required by applicable law or agreed to in writing, software
  // distributed under the License is distributed on an "AS IS" BASIS,
  // WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  // See the License for the specific language governing permissions and
  // limitations under the License.
  ```

- The files under `examples/verbatim/` hold examples printed in
  `docs/schema.md`, byte for byte (an inline example is followed by one line
  feed that is not part of it).
- Every other file quotes the three source files for commentary, analysis and
  testing. Quotations are the source's characters; the only changes are those
  each file states (joining a line the source wrapped, re-serialising a JSON
  value in `normative.md`, removing a trailing comma before validating an
  example). Everything outside the quotations is the library's own work, and
  the files the library derived from the source say so in their name or their
  first lines.
- The repository has no `NOTICE` file at tag `v1.9.2` (checked on 2026-10-19
  against the GitHub listing of the repository root at that tag), so no further
  attribution notice applies.
