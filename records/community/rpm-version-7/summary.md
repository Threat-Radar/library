---
schema: "library-summary/v1"
id: rpm-version-7
record: rpm-version-7
type: summary
updated: "2026-10-18"
---

# rpm-version(7): RPM version system

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | _unset_ |
| **Authors** |  |
| **Published** | 2026-08-20 |
| **Identifier** | git: https://github.com/rpm-software-management/rpm |
| **Source** | https://raw.githubusercontent.com/rpm-software-management/rpm/rpm-6.1.0-release/docs/man/rpm-version.7.scd |
| **Digest** | `dd6ebf07fd2139723681cfded24cf1a348c928324747661257235c912e84d741` |

## Overview

**A stub: not read in full.** The rpm-version(7) manual page from RPM 6.1.0, which defines the EVR label (epoch, version, release) RPM uses for package versions and how two labels are compared: segment by segment, numbers numerically and letters lexically, with tilde marking pre-releases, caret marking post-release snapshots, and a list of known quirks. Cited by tmodel RPT-0004 (tmodel#38): RPM's EVR format and comparison rules (numeric segments newer than alphabetic ones, separators not compared, tilde and caret, non-ASCII characters ignored).

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

Not read in full. Checked the file at the release tag and the commit that tag points to, but did not read RPM's other documentation on dependencies or version ranges.
