---
schema: "library-summary/v1"
id: etsi-tr-104-128
record: etsi-tr-104-128
type: summary
updated: "2026-11-02"
---

# ETSI TR 104 128 V1.1.1: Guide to Cyber Security for AI Models and Systems

|  |  |
|---|---|
| **Type** | spec (ETSI Technical Report, informative); **stub**: pinned, not extracted |
| **Publisher** | ETSI, TC Securing Artificial Intelligence (SAI) |
| **Version** | V1.1.1, 2025-05 |
| **Source** | https://www.etsi.org/deliver/etsi_tr/104100_104199/104128/01.01.01_60/tr_104128v010101p.pdf |
| **Digest** | `824c2ef6720ea30e38c0b64ec7ac46e2d5a5ea6e597f0b69029e4e2605900e05` |

## Overview

The implementation guide that accompanies the baseline requirements (TS 104 223,
now EN 304 223). Clause 6 gives examples for meeting each provision, one
subclause per principle (6.1 to 6.13), often per example application ("Chatbot
App", "ML Fraud Detection", "Open-Access LLM Model"). An annex maps design and
organization principles to SAI. Clause 6 is keyed to TS 104 223's provision
numbers. EN 304 223 keeps them: the text of 5.1.2-2, 5.2.1-4.1 and 5.2.5-4.1
is the same in both. The pinned UK Code of Practice page says the UK government
"plan to submit the Code and Implementation Guide in ETSI so that the future
standard is accompanied by a guide".

**What clause 6 says about the attacks in RPT-0009** (read 2026-11-02 for the
RPT-0009 Phase 4 review, finding F-01; PDF pages):

| Clause | Provision | What the guide adds |
|---|---|---|
| 6.2.3 (p. 23) | 5.1.2-2 | "implementing input validation to prevent prompt injection attacks to the LLM it uses" |
| 6.2.4 (p. 24) | 5.1.2-3 | "For RAG workflows, track the embeddings generated, log metadata about retrieved data (e.g. query terms, document IDs)" |
| 6.2.8 (p. 27) | 5.1.2-6 | "The actions taken by an AI system are not fully predictable, and can be coerced by an attacker. This risk introduces the potential for unauthorized access, data exfiltration, and privilege escalation", answered by "Least-privilege access to data and systems accessed by AI System" |
| 6.3.4 (p. 31) | 5.1.3-1.3 | "Chatbot App: Indirect Prompt Injections and Bias are rated as High when the app is used for recruitment" |
| 6.3.5 (p. 32) | 5.1.3-2 | "If the app performs document summarization, the application maybe vulnerable to indirect prompt injection" |
| 6.5.6 (p. 41) | 5.2.1-4.1 | "Chatbot App: Apply data sanitisation in incoming user prompts to reduce the risk of prompt injections" |
| 6.9.6 (p. 59) | 5.2.5-4.1 | "apply prompt engineering and guardrails to constraint prevent output manipulation and abuse the app using prompt injection attacks" |

So the guide names prompt injection, retrieval (RAG) and exfiltration against
provisions whose normative text in EN 304 223 does not. It never mentions
output rendering, markdown or content security policies (0 matches each in the
extracted text).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | How to meet AI security provisions |
| Cryptography | `none` | |
| This project | `adjacent` | Where to look for how an EN 304 223 provision is met |

`bears_on: R-018`.

## Status

A stub for tmodel #189 (2026-11-02). Cited by EN 304 223 as [i.1] and named by
CISA's AI-in-OT guidance (§3.4). Not extracted. Only the seven subclauses above
were read, for the RPT-0009 Phase 4 review.

## Limits

- Informative, so it adds no requirements. Its examples are guidance on how a
  provision may be met, not what the provision requires.
- Only the seven subclauses in the table were read. The rest of clause 6 and
  the annex were not, so other provisions may also gain attack links from it.
- `etsi-en-304-223`'s mappings were made from the EN's normative text, and are
  not updated from this guide.
