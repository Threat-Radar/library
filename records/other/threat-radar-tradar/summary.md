---
schema: "library-summary/v1"
id: threat-radar-tradar
record: threat-radar-tradar
type: summary
updated: "2026-10-18"
---

# Threat Radar (tradar)

|  |  |
|---|---|
| **Type** | repo |
| **Maturity** | `implementation` |
| **Authors** | Threat Radar |
| **Published** | 2026-09-10 |
| **Identifier** | git: https://github.com/Threat-Radar/tradar |
| **Source** | https://github.com/Threat-Radar/tradar/tree/26d9c76e69b8d359d8e7e1192941b8438cad5698 |
| **Digest** | `not fetched` |

## Overview

**A stub: not read in full.** tradar is a Python command-line tool that runs Syft and Grype, saves their results, and builds a NetworkX directed graph of vulnerable packages, their vulnerabilities and fix versions, saved as GraphML. Its repository describes it as a vulnerability-based threat modeler. Cited by tmodel RPT-0004 (tmodel#38): what radar, the composition source under ADR-0001, reads from Syft and Grype output and what it drops (purl, CPE, dependency edges, match details, CWEs) on the way to its graph.

## Applicability

A stub. `bears_on` (DEC-001, DEC-007) comes from RPT-0004's source log and was not re-assessed here.

## Implementations

Not searched.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this summary |

## Limits

Not read in full. I checked the pinned commit, its dates, the licence, the default branch and five cited code locations through the GitHub API and raw files; I did not run tradar or re-check all 19 Phase 1 claims. No digest: Repo record, pinned by commit; no tag exists at this commit and the tree page was not digested. Phase 1 digested the GitHub API response for commits/main (94c0e8de066bdbc69a1a1fd954d565cd0b6673d006b6b645a31f11a71b19c69f, a live API endpoint); the same gh api call on 2026-10-18 returns exactly the same bytes, which also shows main has not moved.
