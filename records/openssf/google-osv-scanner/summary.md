---
schema: "library-summary/v1"
id: google-osv-scanner
record: google-osv-scanner
type: summary
updated: "2026-10-18"
---

# OSV-Scanner

|  |  |
|---|---|
| **Type** | repo |
| **Maturity** | `implementation` |
| **Authors** | Google |
| **Published** | 2026-09-14 |
| **Identifier** | git: https://github.com/google/osv-scanner |
| **Source** | https://github.com/google/osv-scanner/releases/tag/v2.6.0 |
| **Digest** | `not fetched` |

## Overview

**A stub: not read in full.** OSV-Scanner is the officially supported command-line front end to the OSV.dev vulnerability database, published in Google's GitHub organisation. It lists a project's dependencies from lockfiles, SBOMs, git repositories and container images and asks the OSV.dev API, or a local copy of its per-ecosystem exports, which OSV records affect them. Cited by tmodel RPT-0004 (tmodel#38): what an OSV-based scanner records about a match (package coordinates plus the returned OSV records, with no match-method or confidence field) and what data it sends to OSV.dev.

## Applicability

A stub. `bears_on` (DEC-008) comes from RPT-0004's source log and was not re-assessed here.

## Implementations

Not searched.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this summary |

## Limits

Not read in full. I checked the v2.6.0 tag and release and the four cited files at v2.6.0; I did not run OSV-Scanner or review v2.7.0. No digest: Repo record, pinned by commit; the release page itself was not digested. The four files of row L167 at v2.6.0 (pkg/models/results.go, docs/output.md, README.md, docs/offline-mode.md) match their Phase 1 digests exactly.
