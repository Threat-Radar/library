---
schema: "library-summary/v1"
id: dependencytrack-dependency-track
record: dependencytrack-dependency-track
type: summary
updated: "2026-10-18"
---

# OWASP Dependency-Track

|  |  |
|---|---|
| **Type** | repo |
| **Maturity** | `implementation` |
| **Authors** | OWASP Dependency-Track |
| **Published** | 2026-10-08 |
| **Identifier** | git: https://github.com/DependencyTrack/dependency-track |
| **Source** | https://github.com/DependencyTrack/dependency-track/releases/tag/5.2.0 |
| **Digest** | `not fetched` |

## Overview

**A stub: not read in full.** Dependency-Track is a server platform that keeps CycloneDX SBOMs per project, analyses their components for known vulnerabilities through internal and external analyzers, and stores findings with per-analyzer attribution. Its v5 line accepts only CycloneDX for SBOM upload, in all CycloneDX versions. Cited by tmodel RPT-0004 (tmodel#38): how a multi-project SBOM platform identifies components (one CPE, one purl, a SWID tag id and hashes per component), which data sources need which identifier, how findings carry analyzer attribution and review history, and its CycloneDX-only, no-SPDX-3 status.

## Applicability

A stub. `bears_on` (DEC-001, DEC-002, DEC-008) comes from RPT-0004's source log and was not re-assessed here.

## Implementations

Not searched.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this summary |

## Limits

Not read in full. I checked the 5.2.0 tag and release, the README, the full file tree and seven cited source files at 5.2.0, the file-formats documentation page and issue #1746; I did not run Dependency-Track or re-fetch the other v5 documentation pages of row L229. No digest: Repo record, pinned by commit; the release page itself was not digested. README.md at 5.2.0 (70b38a18097a812ccd495d827377a2e005bef787b5faa9eb0acd59b65bb79c63), the seven Java files of rows L165 and L230, and the v5 documentation page Reference, File formats (f0f5435b6ff16044dfa6c765d5ac1a2c4ceb904683701a03fbe97bb6968d150c) all match their Phase 1 digests.
