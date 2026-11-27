---
schema: "library-doc/v1"
id: catalogs-schema-review-285
title: "Catalogs-schema review-partner source sample (#285)"
type: assessment
status: draft
version: "0.1.1"
updated: "2026-11-26"
needs_review: true
reviewed: false
---

# Catalogs-schema five-record source sample

Task: [tmodel#285](https://github.com/Threat-Radar/tmodel/issues/285), reviewing
library#51 at `8fc3878`. This sample verifies source identity and the claims
below. On 2026-11-26, @paria03 explicitly accepted the eight-summary checklist
(three calibration summaries and these five library records) and authorized
their `reviewed_by` signatures. The five sampled library summaries now record
`reviewed_by: "paria03"`. This does not review every record or cited work.

All five recorded source captures were fetched again on 2026-11-26 and match
their SHA-256 values. NCC and Cyber Centre archive captures are hashed as
received, before decompression. Live-page comparisons do not replace the pins.

## OCCULT

Record: `kouremetis-2025-occult`.
[Pinned primary source](https://arxiv.org/pdf/2502.15797), arXiv v1,
SHA-256 `6b6a747c91b4672c4091a3c918c11377395ae35a4a1c5c1f4c45d4f73376c215`.

- Section 3.2 and Fig. 1 classify evaluations by offensive capability, use
  case and reasoning power. Section 4 describes TACTL, BloodHound Equivalency
  and CyberLayer as three distinct prototypes.
- Section 6.2 / Table X reports 183 TACTL questions and DeepSeek-R1's 91.8%
  result. This is a knowledge benchmark result, not a live intrusion rate.
- Section 6.3 reports 52.5% average correctness for two Mixtral models over
  12 queries and five trials per model. The following paragraph switches to
  ten queries when counting returned objects; do not silently equate these
  denominators. The summary's 12-query figure follows the stated accuracy test.

Result: sampled claims supported. Preserve the preliminary/simulated-result
limitations and the distinction between capability evidence and an incident.

## NCC: application threat models

Record: `brauchler-2024-ai-application-threat-models`.
[Pinned archive](https://web.archive.org/web/20250702003120id_/https://www.nccgroup.com/us/research-blog/analyzing-ai-application-threat-models/),
SHA-256 `ebe2ce14816f912060c06240227074ad0b183417a700f7d79af641e2e5499cf2`.

- Abstract / Inferences: MATA treats a model as an asset, control and potential
  threat actor within the same application architecture.
- Threat Model Analysis contains four numbered attack scenarios. Threat
  Vectors contains 25 named entries, independently recounted in the capture.
- Security Controls distinguishes the trusted code model from a model handling
  untrusted data; ordinary application code delivers the latter's output.

Result: sampled claims supported. These are architectural scenarios, not
independently measured attacks. The component/catalog crosswalk is the lane's
interpretation, not a catalog mapping authored by NCC.

## NCC: secure design principles

Record: `brauchler-2024-secure-ai-design-principles`.
[Pinned archive](https://web.archive.org/web/20250702003120id_/https://www.nccgroup.com/us/research-blog/analyzing-secure-ai-design-principles/),
SHA-256 `54b92faaa6cac27f19ace2f5762841ce4028f7cf7cc0db9c6690115a32708037`.

- Data Pollution sets trust from the least-trusted input and propagates it to
  downstream model outputs.
- Human-In-The-Loop recommends confirmation of write operations through
  functionality outside the agent's control.
- Designing for Fault Tolerance requires independent fallbacks in systems
  where model errors could cause injury or loss.

Result: sampled claims supported. On 2026-11-26 the recorded
[live article](https://www.nccgroup.com/research/analyzing-secure-ai-design-principles/)
serves content again. Correct the summary's stale landing-page redirect claim,
while retaining its original archive and digest.

## Canadian Cyber Centre: ITSAP.00.041

Record: `cccs-itsap-00-041-generative-ai-2025`.
[Pinned archive](https://web.archive.org/web/20260908055757id_/https://www.cyber.gc.ca/en/guidance/generative-artificial-intelligence-ai-itsap00041),
SHA-256 `cc5530e0ce68a69d54bd655d84cf94571945f2557e25ddf00b5b654bb1d75d91`.

- The risks section lists eight categories, from misinformation through
  intellectual-property loss; the summary preserves all eight.
- Security measures cover an AI risk plan, careful vendor selection and
  avoiding sensitive information in prompts.
- The source is an awareness publication with general guidance, not a
  conformance specification or a worked product attack-path model.

Result: sampled claims supported. Applicability ratings and the mapped ids
remain lane judgments; the source does not author those relationships.

## OWASP: NHI Top 10 2025

Record: `owasp-nhi-top10-2025`.
[Pinned source file](https://raw.githubusercontent.com/OWASP/www-project-non-human-identities-top-10/16f8b79394662c6467eb7a1907b6af7e209b1fd9/2025/docs/top-10-2025.md),
SHA-256 `772f6f8c259320124b7780d6aa8d365e38ee3f24af21a48c631c8e7000f4e46d`.
Related pages were checked from the same commit, not the moving live branch.

- `top-10-2025.md` lists NHI1 through NHI10 with the names in the summary.
- `ranking-criteria.md` defines four criteria with three numerical levels.
  `methodology-and-data.md` describes weighted averaging and links its scores.
- Those pages concern software identities. Applying their controls to agent
  credentials is an explicit lane interpretation, not an AI-specific taxonomy
  claimed by the source. This check does not reproduce the external score sheet.

Result: sampled claims supported within that scope.

## Citation policy correction and checks

Following `docs/references.md`, remove 261 reverse library `cited_by` links
from the 256 new reference stubs. Every one has a matching forward `cites`
entry. Preserve those citations and all other parsed metadata. Correct the
OCCULT and NCC source summaries that describe those inverse fields.

Run the library CI steps locally: YAML reader, records/topics, requirements,
artifacts, generated views, bibliography completeness, extraction gate,
dangling references, forbidden third-party documents and DCO. Hosted Actions
remain separately blocked until the repository pause is lifted.

No source review is claimed for the unselected records, the 256 reference
stubs or the unpublished score spreadsheet. The source checks do not themselves
establish human approval. The five signatures record @paria03's separate,
explicit acceptance: "Accept and sign these eight summaries". The corresponding
three calibration signatures are recorded in tmodel#228.

Local validation on the review follow-up: 967 records and bibliography entries,
zero errors, the same 99 record warnings, 15/15 YAML-reader tests, 53 requirement
sets with zero failures, and 181 artifact files with zero parse or structural
errors (38 existing warnings). Export/reindex report no dangling references;
the full-extraction gate passes. Generated views remain untracked. Every
removed inverse edge was checked against its preserved forward citation.
