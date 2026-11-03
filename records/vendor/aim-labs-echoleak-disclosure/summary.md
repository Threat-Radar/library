---
schema: "library-summary/v1"
id: aim-labs-echoleak-disclosure
record: aim-labs-echoleak-disclosure
type: summary
updated: "2026-11-02"
---

# Aim Labs: EchoLeak Vulnerability Found in Microsoft 365 Copilot

|  |  |
|---|---|
| **Type** | web (vendor research disclosure); **stub**: NOT pinned, not read |
| **Authors** | Aim Labs, Aim Security |
| **Published** | June 2025 (public disclosure on 2025-06-11, per the timeline in `echoleak-zero-click-prompt-injection`) |
| **Source** | https://www.aim.security/lp/aim-labs-echoleak-m365 |
| **Digest** | none: the page returned HTTP 403 to `bin/ingest --fetch` on 2026-11-02 |

## Overview

The finders' primary disclosure of EchoLeak (CVE-2025-32711), the zero-click
prompt injection in Microsoft 365 Copilot that RPT-0009's worked example
(em-01) models. This stub records where it is and how other sources rely on
it; its content has not been read. The CVE record's CVE Program (ADP)
container lists this URL as a reference. The secondary case study
`echoleak-zero-click-prompt-injection` says "researchers at Aim Security
disclosed EchoLeak", cites this disclosure as "Aim Labs 2025", and draws its
timeline from it: discovery and a proof of concept in January 2025, disclosure
to Microsoft's MSRC, a server-side fix in May 2025, and public disclosure with
the CVE on 2025-06-11.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | The primary account of a real indirect prompt injection that exfiltrated data |
| Cryptography | `none` | |
| This project | `adjacent` | Primary evidence for em-01 and RPT-0009 §5 |

`bears_on: DEC-001`, as the secondary case study does.

## Status

A stub for tmodel #189 (2026-11-02), added because the RPT-0009 Phase 4
review (finding F-09) found that the report treated the secondary case study
as the finders' write-up, and that the primary disclosure was not held.

## Limits

- Not pinned and not read. The page refused the fetch (HTTP 403), so no claim
  in RPT-0009 can rest on this record's content until it is pinned.
- The title is the one the secondary case study's bibliography gives ("Aim
  Labs. 2025. EchoLeak Vulnerability Found in Microsoft 365 Copilot."), not
  one read from the page.
