---
schema: "library-summary/v1"
id: debian-security-tracker
record: debian-security-tracker
type: summary
updated: "2026-10-18"
---

# Debian Security Tracker, JSON export

|  |  |
|---|---|
| **Type** | dataset |
| **Maturity** | _unset_ |
| **Authors** |  |
| **Published** |  |
| **Identifier** | git: https://salsa.debian.org/security-tracker-team/security-tracker |
| **Source** | https://security-tracker.debian.org/tracker/data/json |
| **Digest** | `cde6e255b8faa3d535af3799726de4d64b1d78e40f03ab2a5494e26899a54341` |

## Overview

**A stub: not read in full.** The Debian Security Team's tracker of how vulnerabilities affect Debian: the team edits text files in a Git repository, and scripts publish them as web pages and as one JSON export giving, for each source package and vulnerability id, the status, fixed version, urgency and triage notes in each supported Debian release. Its documentation says entries come from research on Debian's own packages and imply nothing about other systems. Cited by tmodel RPT-0004 (tmodel#38): Debian's per-release status and fixed versions (a fixed version of 0 for not affected), triage outcomes such as postponed, and the example of a backported fix that an upstream version range would misjudge.

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

Not read in full. Fetched and parsed the JSON export (4,102 source packages, 75,868 entries, releases bookworm, trixie, forky and sid) and read the documentation page, but found no published definition of the JSON format and did not read the tracker code. A live feed: the server reported Last-Modified 2026-10-19 (UTC) when it was fetched on 2026-10-18 (local).
