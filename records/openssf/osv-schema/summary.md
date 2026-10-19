---
schema: "library-summary/v1"
id: osv-schema
record: osv-schema
type: summary
updated: "2026-10-19"
---

# OSV Schema (OpenSSF), version 1.9.2

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | `best-practice`: an OpenSSF community specification, not a ratified standard. It describes itself as stable but still open to "backwards compatible changes" (Purpose). |
| **Authors** | Oliver Chang and Russ Cox (Google), named in the document as original authors; maintained in the open by contributors to `ossf/osv-schema` |
| **Publisher** | OpenSSF (Open Source Security Foundation), repository `ossf/osv-schema` |
| **Published** | Version 1.9.2, dated October 13, 2026 in the text; GitHub release `v1.9.2` published 2026-10-13 |
| **Identifier** | git tag `v1.9.2`, commit `c8a57bdc5b0bc54646e140cabbb7834bd0b5aec9` |
| **Source** | https://raw.githubusercontent.com/ossf/osv-schema/v1.9.2/docs/schema.md (the specification, `docs/schema.md` at tag `v1.9.2`). https://ossf.github.io/osv-schema/ renders the current `main` branch, not this tag, and the repository's root `schema.md` only points there. |
| **Digest** | SHA-256 `96d82f03d763fb408bc344d01fc271f761a81cc225f6f6a42d318e3ed21cebff` (`docs/schema.md`), `15b10dbb4c4e31c7aae11d22cdd991a9a374758db7c8389e62b3cc37cac92653` (`validation/schema.json`), `1c5a7af863c576398e333358c006d30577dd111c810416cd2f3fc0cecd20a070` (`proto/vulnerability.proto`) |
| **Licence** | Apache-2.0 (repository licence) |

## Overview

OSV defines one JSON record per vulnerability entry that any vulnerability database can serve in the same shape, so that consumers can read every database alike and the databases can cross-check one another. A record names affected software as packages (an ecosystem from a closed list plus the package's name in that ecosystem, with an optional purl that leaves the version out) and gives the affected versions as typed timelines (`SEMVER`, `ECOSYSTEM` or `GIT`) of introduced, fixed, last-affected and limit events, optionally with the full list of affected versions, plus pseudocode (`IsVulnerable`) for deciding whether a given version is affected. Each record belongs to a home database named by its id prefix, and points at other databases' records as `aliases` (the same vulnerability), `upstream` (a vulnerability it derives from) or `related`. The schema deliberately standardises only the fields that "absolutely must be shared between databases" (Format Overview): how to order versions in most ecosystems, which weakness (CWE) a vulnerability is, and whether a product is not affected are all left out or pushed into the open `database_specific` and `ecosystem_specific` objects.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | The advisory format on the vulnerability side of the component-to-vulnerability bridge: GitHub's advisory database, the Go, PyPI and RustSec databases, most Linux distributions and OSV.dev serve it, and OSV-Scanner, Trivy, Dependency-Track and GUAC read it. |
| Cryptography | none | No signatures, digests or keys. Git commit hashes appear only as version identifiers in `GIT` ranges, and a record's integrity rests on the channel it was fetched from. |
| This project | core | It maps onto tmodel's accepted core classes (DEC-001a, ADR-0010): an OSV id is a Vulnerability `catalog_ref`, matches and alias links are Assertions, purls go to Component `identifiers`. It bears most on the open DEC-008 (CWE and NVD integration: cached exports or live lookups, and which copy of a record) and DEC-009 (matching packages to components, version ranges), on RPT-0004's candidate rules R-RANGE-1, R-MATCH-1 and R-CWE-1, and on DEC-002 (accepted, ADR-0007), whose committed import list does not include OSV. |

Bears on DEC-001a, DEC-002 and DEC-003 (accepted) and DEC-008 and DEC-009 (open). Gathered first for RPT-0011 (knowledge graphs and NSF OKN, tmodel #25); extracted to FX-1 for RPT-0004 (product composition, tmodel #38). `distilled/design-notes.md` gives 7 adopt, 8 adapt and 7 reject items, 22 source defects and 14 open questions.

## Implementations

Searched 2026-10-18: GitHub's REST API for the repositories below (licences and latest releases), and tmodel's RPT-0004 notes of 2026-10-08 for how each tool uses OSV. Commercial products were not surveyed.

| Name | Kind | License | URL |
|---|---|---|---|
| `osvschema` and `osvconstants` (in the schema repository, `bindings/go`) | Go library generated from the protobuf | Apache-2.0 | https://github.com/ossf/osv-schema/tree/v1.9.2/bindings/go |
| OSV.dev | aggregator service: per-ecosystem exports and a query API (library record `osv-dev`) | Apache-2.0 (code); record data per source database | https://github.com/google/osv.dev |
| OSV-Scanner | scanner that asks OSV.dev, or reads its exports, for a project's packages (library record `google-osv-scanner` pins v2.6.0; v2.7.0 was released 2026-10-12) | Apache-2.0 | https://github.com/google/osv-scanner |
| Dependency-Track 5.2.0 | SBOM platform; mirrors OSV data and converts OSV ranges to `vers` | Apache-2.0 | https://github.com/DependencyTrack/dependency-track |
| GUAC v1.1.0 | supply-chain graph with an OSV certifier keyed on purls (library record `guac`) | Apache-2.0 | https://github.com/guacsec/guac |
| Trivy (v0.76.0 latest; RPT-0004 checked 0.75.0) | scanner; `osv` is one of its data and severity sources | Apache-2.0 | https://github.com/aquasecurity/trivy |

Producers include the GitHub Advisory Database (library record `github-advisory-database`), Ubuntu (library record `ubuntu-security-notices`) and the other databases in the specification's prefix table.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, labels and relations, and the FX-1 `distillation` block |
| `distilled/README.md` | index of the extracted artifacts, what each one covers, and the Apache-2.0 licence and attribution |
| `distilled/normative.md` | the normative statements of the prose, the JSON Schema and the protobuf, verbatim, with locators |
| `distilled/requirements.yaml` | one entry per requirement (`osv-schema#R-NNNN`), reconciled by line against the document's lowercase keywords, since it uses no uppercase BCP 14 keyword |
| `distilled/schema/` | the tag's JSON Schema and protobuf, byte for byte, and two `.derived.` JSON Schemas for the stated rules and recommendations that neither file enforces |
| `distilled/messages.yaml` | the record structure field by field: type, whether required, constraints, locators and the requirement ids that constrain each field |
| `distilled/state-machine.yaml` | two machines: evaluating a version against a record's ranges, and a record's lifecycle (which copy is authoritative, withdrawal) |
| `distilled/examples/` | the specification's examples as fixtures, plus derived positives, negatives and edge cases, with expected and actual results and a runner |
| `distilled/design-notes.md` | what tmodel adopts, adapts or rejects, mapped to its decisions; an OSV-to-tmodel field mapping; source defects; open questions |
| `distilled/verification.md` | the verify and cross-check record (passes 2 and 3) |

Protocol is not applicable; the reason is in `record.yaml`.

## Limits

- **Version comparison is mostly outside it.** `ECOSYSTEM` range versions are "arbitrary, uninterpreted strings" (§ affected[].ranges[].type field); of 52 ecosystems only four (Echo, Homebrew, openSUSE, SUSE) state an ordering, so evaluating a range needs each ecosystem's own comparator (apk, dpkg, rpm, PEP 440, Maven and others).
- **Matching is underspecified.** `IsVulnerable` does not define package equality, the wildcard name `*`, entries with no `package`, withdrawn records, or the order of two events at the same version; with `introduced` and `last_affected` at one version, the result depends on that order.
- **No weakness, no "not affected", no review state.** CWEs appear only by one database's convention (GitHub's `database_specific.cwe_ids`); a version outside every range is not a not-affected statement; and `withdrawn` names no successor.
- **The JSON Schema and the text disagree.** The schema lacks the `id` character rule that 1.9.2 added (the schema file is byte-identical to 1.9.1's), accepts `GIT` as an ecosystem the text does not list, rejects a `limit` of `"*"` in `GIT` ranges, and rejects unknown top-level fields that the text tells readers to ignore. The protobuf calls itself "*NOT* stable" and marks different fields as required.
- **Copies differ.** OSV.dev re-serialises the records it aggregates (it adds purls, changes `schema_version` and drops versions from purls), so one id can carry different content depending on where it was fetched.
- **A patch release over 1.9.1.** tmodel's RPT-0004 and RPT-0005 quote 1.9.1 (2026-09-24); 1.9.2 changes only the `id` rules, so those quotations still hold. New ecosystems and database prefixes keep arriving by pull request, and `main` moves after the tag.
