---
schema: "library-summary/v1"
id: owasp-pytm
record: owasp-pytm
type: summary
updated: "2026-10-12"
---

# OWASP pytm

|  |  |
|---|---|
| **Type** | repo |
| **Maturity** | established OWASP implementation |
| **Authors** | OWASP pytm project |
| **Published** | v1.4.0 released 2026-07-06; reviewed 2026-10-12 |
| **Identifier** | git: https://github.com/OWASP/pytm |
| **Source** | https://github.com/OWASP/pytm |
| **Digest** | `not fetched` |

## Overview

OWASP pytm is an MIT-licensed Python library and command-line approach for defining a threat model as code. The reviewed repository documents Python model objects, rule-based threat generation, generated data-flow diagrams, sequence diagrams and reports, plus native JSON output and loading. Version 1.4.0 added `Data` decoding needed for round-trip serialization.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | Implements threat generation from a structured system model. |
| Cryptography | none | Does not define a cryptographic protocol. |
| This project | adjacent | Useful model-as-code evidence for DEC-001, DEC-003, and DEC-006. |

Reviewed at commit `381dea05c58055ba218e632510dd3a327d2bf215`. The object model includes `SetOfProcesses` as well as actors, assets, processes, datastores, servers, boundaries, data flows, threats, findings, assumptions and controls.

## Implementations

| Name | Kind | License | URL |
|---|---|---|---|
| OWASP pytm | open-source library/CLI | MIT | https://github.com/OWASP/pytm |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |

## Limits

The JSON format is native to pytm, not a neutral cross-tool format. The reviewed source does not establish built-in issue-tracker integration or a native collaborative review lifecycle. No acceptance test was performed.
