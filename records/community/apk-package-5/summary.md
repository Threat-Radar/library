---
schema: "library-summary/v1"
id: apk-package-5
record: apk-package-5
type: summary
updated: "2026-10-18"
---

# apk-package(5): apk package metadata fields

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | _unset_ |
| **Authors** |  |
| **Published** | 2026-08-31 |
| **Identifier** | git: https://gitlab.alpinelinux.org/alpine/apk-tools |
| **Source** | https://gitlab.alpinelinux.org/alpine/apk-tools/-/raw/v3.0.8/doc/apk-package.5.scd |
| **Digest** | `36d6b46a87064e41cc469eedaf7a90629473241a07275d0d030a18fe86e6c164` |

## Overview

**A stub: not read in full.** The apk-package(5) manual page from apk-tools 3.0.8, which describes the metadata fields of an apk package, including the package name, the APK version format (numbers, an optional letter, ordered suffixes, an optional hash and a package release number) and the origin field that names the source package. Cited by tmodel RPT-0004 (tmodel#38): the APK version format and suffix order, and the origin field that Syft writes into purls and Grype uses to search Alpine's feed.

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

Not read in full. Checked the file at tag v3.0.8 on both GitLab and the GitHub mirror and the commit the tag points to, but did not read apk-tools' version comparison code.
