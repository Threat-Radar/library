---
schema: "library-summary/v1"
id: github-advisory-database
record: github-advisory-database
type: summary
updated: "2026-10-18"
---

# GitHub Advisory Database (github/advisory-database)

|  |  |
|---|---|
| **Type** | dataset |
| **Maturity** | _unset_ |
| **Authors** |  |
| **Published** | 2026-10-08 |
| **Identifier** | git: https://github.com/github/advisory-database |
| **Source** | https://codeload.github.com/github/advisory-database/tar.gz/0d77cdb5998b6b9c4c13738926d555c877e8e5af |
| **Digest** | `0c227c744d0593be639b7f121527e44ab181b58a58017c2e5156fa5ac6734a24` |

## Overview

**A stub: not read in full.** GitHub's public repository of security advisories, one OSV-format JSON file per advisory in github-reviewed and unreviewed folders, drawn from GitHub repository advisories, NVD and other advisory databases, with GitHub's own fields (severity, CWE ids, review state, extra version ranges) under database_specific. GitHub's REST API lists these global security advisories through /advisories endpoints whose schema also keys packages by ecosystem and name. Cited by tmodel RPT-0004 (tmodel#38): evidence that GitHub advisories name packages by ecosystem and name with no purl or CPE (in the files and the REST API schema), use only ECOSYSTEM ranges, carry GitHub-assigned CWE ids, and that unreviewed advisories are NVD copies without packages.

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

Not read in full. Verified the commit tarball, README, two advisories and the REST API description against Phase 1 digests and re-read the moved docs page, but did not recompute the record counts (382,210 files, 67,514 affected entries).
