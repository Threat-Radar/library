---
schema: "library-summary/v1"
id: debian-policy-version
record: debian-policy-version
type: summary
updated: "2026-10-18"
---

# Debian Policy Manual, chapter 5: Control files and their fields

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | _unset_ |
| **Authors** |  |
| **Published** | 2026-03-31 |
| **Identifier** | https://www.debian.org/doc/debian-policy/ch-controlfields.html |
| **Source** | https://www.debian.org/doc/debian-policy/ch-controlfields.html |
| **Digest** | `4d526c151f0a7dfcbe190f7b6fe4de5cc1a0f2208fb83e3ea40d60c7db9f8e15` |

## Overview

**A stub: not read in full.** Chapter 5 of the Debian Policy Manual, version 4.7.4.1, which defines the syntax of Debian control files and each of their fields. Its Version field section sets out the epoch, upstream version and Debian revision parts and the comparison algorithm, in which a tilde sorts lower than any other character and lower than the end of a part. Cited by tmodel RPT-0004 (tmodel#38): the dpkg version format and ordering (epoch compared numerically, tilde sorting first), as when a Debian backport version sorts below the plain release.

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

Not read in full. Checked the page, its stated version and release date and the Version section, but read neither the rest of chapter 5 nor the other chapters.
