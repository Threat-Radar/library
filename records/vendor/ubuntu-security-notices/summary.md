---
schema: "library-summary/v1"
id: ubuntu-security-notices
record: ubuntu-security-notices
type: summary
updated: "2026-10-18"
---

# Ubuntu Vulnerability Data (canonical/ubuntu-security-notices)

|  |  |
|---|---|
| **Type** | dataset |
| **Maturity** | _unset_ |
| **Authors** |  |
| **Published** | 2026-10-08 |
| **Identifier** | git: https://github.com/canonical/ubuntu-security-notices |
| **Source** | https://raw.githubusercontent.com/canonical/ubuntu-security-notices/650493ddcf7c54881148acfafc8a67edb8415e0e/README.md |
| **Digest** | `36a09fbf5f1e70dd86d2104627e181477e747625629a21342286e8f3b62f2f04` |

## Overview

**A stub: not read in full.** Canonical's repository of Ubuntu vulnerability data from the Ubuntu Security Team in three JSON formats: the team's own USN/LSN notice format, which it advises against relying on, OSV records and OpenVEX documents. Companion documentation pages explain the OSV and VEX fields and how the team's patch states map onto them. Cited by tmodel RPT-0004 (tmodel#38): how Ubuntu's OSV records name source packages and list binaries, carry versioned purls, write ECOSYSTEM ranges that always start at 0, and fold several triage states into affected.

## Applicability

A stub. `bears_on` (DEC-008, DEC-009) comes from RPT-0004's source log and was not re-assessed here.

## Implementations

Not searched.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this summary |

## Limits

Not read in full. Matched the README, three OSV records and both documentation pages to Phase 1 at a reconstructed commit, but did not read the OpenVEX files or the rest of the repository.
