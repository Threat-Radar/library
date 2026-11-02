---
schema: "library-summary/v1"
id: echoleak-zero-click-prompt-injection
record: echoleak-zero-click-prompt-injection
type: summary
updated: "2026-11-02"
---

# EchoLeak: zero-click prompt injection in Microsoft 365 Copilot

|  |  |
|---|---|
| **Type** | paper (arXiv preprint); **stub**: pinned, not summarized here |
| **Authors** | Pavan Reddy, Aditya Sanjay Gujral |
| **Published** | arXiv 2509.10540v1, 2025-09-06 |
| **Source** | https://arxiv.org/pdf/2509.10540v1 |
| **Digest** | `4f0939532c477922ab9d501adbfc3f25433d1df72da7d33e4e7834a2b064969c` |

## Overview

The researchers' account of EchoLeak (CVE-2025-32711). Per RPT-0009 §5: one
email carried hidden instructions; retrieval later pulled it into Copilot's
context; Copilot put the user's data into a reference-style image link; and
the client fetched it through an allow-listed Teams service to the attacker's
server. The chain bypassed an injection classifier, link redaction, image
auto-fetch controls and a content-security-policy allowlist. The paper
recommends prompt partitioning, filtering every link and image, and strict
content security policies.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | A documented, patched, zero-click attack on a production LLM system |
| Cryptography | `none` | |
| This project | `core` | The source of RPT-0009's worked example (`example-models/em-01`) |

`bears_on: DEC-001`: the model built from it produced RPT-0009's gaps G1 to G7,
evidence for the object model (#64).

## Status

A stub for tmodel #189 (2026-11-02). RPT-0009's em-01 follows ATLAS case study
AML.CS0059 and was checked against this paper and the CVE record (RPT-0009 §5).
This record pins the PDF; the abstract and HTML digests RPT-0009 recorded are of
other renderings.

## Limits

- One vendor's product, as reported by its finders; Microsoft's own write-up is
  not held.
