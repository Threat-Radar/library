---
schema: "library-summary/v1"
id: anchore-grype
record: anchore-grype
type: summary
updated: "2026-10-18"
---

# Grype

|  |  |
|---|---|
| **Type** | repo |
| **Maturity** | `implementation` |
| **Authors** | Anchore, Inc. |
| **Published** | 2026-10-06 |
| **Identifier** | git: https://github.com/anchore/grype |
| **Source** | https://github.com/anchore/grype/releases/tag/v0.120.1 |
| **Digest** | `not fetched` |

## Overview

**A stub: not read in full.** Grype is Anchore's vulnerability scanner for container images, filesystems and SBOMs. It matches packages against its own vulnerability database, built by vunnel providers from distribution feeds, GitHub advisories, NVD and other sources, and records for each match the matcher, the match type (exact direct, exact indirect or CPE) and what was searched and found. Cited by tmodel RPT-0004 (tmodel#38): how a scanner matches components to vulnerabilities and what it records per match (match type, matcher, namespace, version constraint, database provenance, CWEs), its CPE matching defaults, and the apk matcher's use of NVD data; it is the matcher that radar wraps.

## Applicability

A stub. `bears_on` (DEC-001, DEC-002, DEC-007, DEC-008) comes from RPT-0004's source log and was not re-assessed here.

## Implementations

Not searched.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this summary |

## Limits

Not read in full. I checked the v0.120.1 and v0.119.0 tags, the release checksums, ten Grype source files at both tags, five vunnel files, the grype-db configuration, two Anchore documentation pages and the cited issues and pull requests; I did not run Grype or download its vulnerability database. No digest: Repo record, pinned by commit; the release page itself was not digested. The release asset grype_0.120.1_checksums.txt has SHA-256 c25b6095265b44fd9bbb9dbe76aca8daa394c5f0490793d2b52b16be4f5b71b1 and lists grype_0.120.1_darwin_arm64.tar.gz at cf97957fa467d25575ec2cc3228289f391ea51cf88b9cffc5f83dc03d4cbc732; both match Phase 1. vex/processor.go at v0.120.1 matches Phase 1 (ffe6f17f4c8569f31b62277da454f72e24653baa4e4a05192eb022403bfb3963), and the vunnel v0.64.0 and grype-db files of row L161 match exactly.
