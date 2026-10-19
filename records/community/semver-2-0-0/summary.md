---
schema: "library-summary/v1"
id: semver-2-0-0
record: semver-2-0-0
type: summary
updated: "2026-10-18"
---

# Semantic Versioning 2.0.0

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | _unset_ |
| **Authors** | Tom Preston-Werner |
| **Published** | 2013-06-18 |
| **Identifier** | git: https://github.com/semver/semver |
| **Source** | https://semver.org/spec/v2.0.0.html |
| **Digest** | `f9d4b8b1a5e9a0de6621dbbc70d69fdf05310b7a737509317b94a7bddfb9409e` |

## Overview

**A stub: not read in full.** Semantic Versioning 2.0.0, a specification for MAJOR.MINOR.PATCH version numbers that says when each part is incremented, how pre-release and build metadata labels are written, and how precedence between two versions is worked out, with build metadata left out of precedence. Cited by tmodel RPT-0004 (tmodel#38): SemVer precedence rules, in particular that build metadata does not count in version precedence, set against Maven and Python ordering.

## Applicability

A stub. `bears_on` (DEC-002) comes from RPT-0004's source log and was not re-assessed here.

## Implementations

Not searched.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this summary |

## Limits

Not read in full. Checked the semver.org page against Phase 1 and traced one changed rule back through the source repositories, but did not compare the page with the 2013 tag text in full. The semver.org page differs from the 2013 v2.0.0 tag: commit a27ac08e (2013-08-11) changed build metadata from SHOULD to MUST be ignored, and RPT-0004 quotes the page.
