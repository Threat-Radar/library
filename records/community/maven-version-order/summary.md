---
schema: "library-summary/v1"
id: maven-version-order
record: maven-version-order
type: summary
updated: "2026-10-18"
---

# POM Reference: Version Order Specification

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | _unset_ |
| **Authors** |  |
| **Published** | 2026-08-05 |
| **Identifier** | git: https://github.com/apache/maven-site |
| **Source** | https://raw.githubusercontent.com/apache/maven-site/15c4fdd29825c316056b20b07d9da4653ffe8e3b/content/markdown/pom.md |
| **Digest** | `25ad4e818ac5c73814c2f4d0a5296677e7e5b5c6c3a0383c1ede77def3594312` |

## Overview

**A stub: not read in full.** The Apache Maven POM Reference, which describes Maven's pom.xml project model; its Version Order Specification subsection defines how Maven splits version strings into tokens, trims and pads them and orders numbers and qualifiers (alpha, beta, milestone, rc, snapshot, release, sp), and states where this order departs from Semantic Versioning 2.0.0. Cited by tmodel RPT-0004 (tmodel#38): Maven's version order and its stated differences from SemVer 2.0.0 (case-insensitive comparison, no special handling of the plus sign or build identifiers).

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

Not read in full. Read the Version Order Specification and the version range syntax in the source at a pinned commit, but not the rest of the POM Reference or Maven's comparison code.
