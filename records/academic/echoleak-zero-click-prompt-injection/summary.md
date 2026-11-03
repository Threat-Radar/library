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
| **Type** | paper (secondary case study; AAAI Fall Symposium Series 2025); **stub**: pinned, not summarized here |
| **Authors** | Pavan Reddy, Aditya Sanjay Gujral (The George Washington University) |
| **Published** | arXiv 2509.10540v1, 2025-09-06; "Published at AAAI Fall Symposium Series 2025" (arXiv comment) |
| **Source** | https://arxiv.org/pdf/2509.10540v1 |
| **Digest** | `4f0939532c477922ab9d501adbfc3f25433d1df72da7d33e4e7834a2b064969c` |

## Overview

A case study of EchoLeak (CVE-2025-32711) by researchers who did not find it:
"researchers at Aim Security disclosed EchoLeak", and the finders' disclosure is
`aim-labs-echoleak-disclosure`. Per RPT-0009 §5: one email carried hidden
instructions; retrieval later pulled it into Copilot's context; Copilot put the
user's data into a reference-style image link; and the client fetched it
through an allow-listed Teams service to the attacker's server. The abstract
names four steps in the chain: "evading Microsoft's XPIA (Cross Prompt
Injection Attempt) classifier, circumventing link redaction with
reference-style Markdown, exploiting auto-fetched images, and abusing a
Microsoft Teams proxy allowed by the content security policy". Its threat
model lists three defenses that were in place: the XPIA classifier, output
filtering that redacts external links, and the browser content security
policy. The paper recommends prompt partitioning, filtering every link and
image, and strict content security policies.

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

- Secondary. Its Limitations section says it is "based solely on analysis of
  already-public data; we did not reproduce the attack or run any
  experiments". The finders' disclosure (`aim-labs-echoleak-disclosure`) is
  not pinned (HTTP 403 on 2026-11-02), and Microsoft's own write-up is not
  held.
- One vendor's product.
