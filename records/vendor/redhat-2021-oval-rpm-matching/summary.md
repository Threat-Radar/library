---
schema: "library-summary/v1"
id: redhat-2021-oval-rpm-matching
record: redhat-2021-oval-rpm-matching
type: summary
updated: "2026-10-18"
---

# How to accurately match OVAL security data to installed RPMs

|  |  |
|---|---|
| **Type** | article |
| **Maturity** | _unset_ |
| **Authors** | Jason Shepherd |
| **Published** | 2021-05-05 |
| **Identifier** | https://www.redhat.com/en/blog/how-accurately-match-oval-security-data-installed-rpms |
| **Source** | https://www.redhat.com/en/blog/how-accurately-match-oval-security-data-installed-rpms |
| **Digest** | `9cdd799abe31cc6eadf21537d7770d1220258f50d77f54872078c615ee45ab47` |

## Overview

**A stub: not read in full.** A Red Hat blog post on choosing which Red Hat OVAL stream files to scan a system or container image against: find the repositories the installed RPMs came from, then use Red Hat's repository-to-CPE mapping file to find the matching product streams, including Extended Update Support streams. Cited by tmodel RPT-0004 (tmodel#38): the point that matching an installed RPM to Red Hat security data needs the repository it came from, through Red Hat's repository-to-CPE mapping.

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

Not read in full. Read the article text and its page metadata, but did not fetch the repository-to-CPE mapping file or the OVAL files it links.
