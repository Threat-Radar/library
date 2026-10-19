---
schema: "library-summary/v1"
id: anchore-syft
record: anchore-syft
type: summary
updated: "2026-10-18"
---

# Syft

|  |  |
|---|---|
| **Type** | repo |
| **Maturity** | `implementation` |
| **Authors** | Anchore, Inc. |
| **Published** | 2026-10-06 |
| **Identifier** | git: https://github.com/anchore/syft |
| **Source** | https://github.com/anchore/syft/releases/tag/v1.54.1 |
| **Digest** | `not fetched` |

## Overview

**A stub: not read in full.** Syft is Anchore's command-line tool and Go library for generating a software bill of materials from container images, filesystems and archives. It writes CycloneDX, SPDX (2.x, and SPDX 3 in JSON since v1.46.0) and its own JSON format, and generates CPE identifiers by a dictionary lookup with a heuristic fallback. Cited by tmodel RPT-0004 (tmodel#38): what an SBOM generator actually fills in CycloneDX and SPDX output (purl, CPE candidates, hashes, suppliers, dependency edges, image digest), its SPDX 3 support, and its CPE generation rules; it is the SBOM producer that radar wraps.

## Applicability

A stub. `bears_on` (DEC-001, DEC-002, DEC-007) comes from RPT-0004's source log and was not re-assessed here.

## Implementations

Not searched.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this summary |

## Limits

Not read in full. I checked the v1.54.1 tag and release, the checksums file, the five cited source files, the CPE generation README and the SPDX 3 release note, pull request and issue through the GitHub API; I did not run Syft or reproduce the Phase 1 and Table 6 tool runs. No digest: Repo record, pinned by commit; the release page itself was not digested. I checked the release asset syft_1.54.1_checksums.txt instead: SHA-256 7577f0d0b3fb16f65a2e56b413862f69aa5eaa2379d5760cb73d691ca7986059, and its line for syft_1.54.1_darwin_arm64.tar.gz gives b4319c3abaa87a0170ab76ee83ea2260ca34b53aecfa3ab0dd5428d2319d744f; both match Phase 1. The five source files of row L222 at v1.54.1 also match their Phase 1 digests.
