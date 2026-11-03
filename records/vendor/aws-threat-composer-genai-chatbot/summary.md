---
schema: "library-summary/v1"
id: aws-threat-composer-genai-chatbot
record: aws-threat-composer-genai-chatbot
type: summary
updated: "2026-11-02"
---

# Sample Generative AI Chatbot Application (Threat Composer example threat model)

|  |  |
|---|---|
| **Type** | dataset (one JSON workspace file) |
| **Maturity** | _unset_ (an example published in an open-source repository; no maturity level applies) |
| **Authors** | Amazon Web Services |
| **Published** | added to the repository 2023-11-22; updated 2024-02-14, 2025-04-02 and 2025-09-02 (the content summarized here); pinned at repository commit 3d4ed92f96a2 (2026-09-23) |
| **Identifier** | git: https://github.com/awslabs/threat-composer, file `packages/threat-composer/src/data/workspaceExamples/GenAIChatbot.tc.json` |
| **Source** | https://raw.githubusercontent.com/awslabs/threat-composer/3d4ed92f96a29605a74795d8df103e068f11ed70/packages/threat-composer/src/data/workspaceExamples/GenAIChatbot.tc.json |
| **Digest** | `sha256:604bc44003fa894b0397b61f17fc491892ab1b01c2bd6b1b4e5fa1d73e129912` (425,849 bytes) |

## Overview

This is the example threat model AWS ships with Threat Composer, for a retrieval-augmented
chatbot on Amazon Bedrock. One JSON workspace holds the application description, a reference
architecture and a data-flow model. The architecture covers data preparation with S3, Lambda
and Titan embeddings; a front end behind Cognito, WAF and a load balancer; OpenSearch
Serverless as the vector store; and Bedrock with Guardrails. The data-flow model has nine
entities, nine flows (DF1 to DF9, each listing the assets it carries) and six trust
boundaries (TB1 to TB6). On top of that sit 13 assumptions, 37 threat statements and 84
mitigations. Each threat is written in Threat Composer's grammar (source, prerequisites,
action, impact, impacted goal and assets) and tagged with an OWASP Top 10 for LLM
Applications 2025 category, STRIDE letters and a priority. Every threat links to at least one
mitigation, and 95 further links tie assumptions to threats and mitigations. The disclaimer
presents it as an informational starting point: a hypothetical operator ranks confidentiality
of the retrieval data first, integrity of answers second and availability last, and readers
should set their own priorities.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | A complete worked threat model of an LLM retrieval application: architecture, data flows, trust boundaries, threats, assumptions and mitigations |
| Cryptography | `none` | Only two one-line mitigations touch it: encryption mechanisms (M-83) and code signing on training tools (M-24) |
| This project | `core` | A real threat model in a published, machine-readable format, with typed links between threats, mitigations and assumptions: a ready input for testing an import and for checking that the core types can carry these statements |

`bears_on: DEC-001a` (the core type system, accepted in ADR-0010) and `R-005` (import at least
one existing threat-model format, with a round-trip vector). ADR-0007 commits tmodel to
importing OTM and STIX 2.1, not Threat Composer's format, so this file would test an additional
importer or a conversion.

## Implementations

Searched on 2026-11-02.

| Name | Kind | License | URL |
|---|---|---|---|
| awslabs/threat-composer | the open-source tool that opens and edits this workspace; the library's `aws-threat-composer` record covers it | Apache-2.0 | https://github.com/awslabs/threat-composer |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this document |

## Limits

- **An example, by its own disclaimer.** It is informational, provided as is, a proof of
  concept for one reference architecture, and not a complete end-to-end solution.
- **Nothing is validated.** All 37 threats are in the identified state and all 84 mitigations
  in the identified state; none is marked resolved or tested.
- **Assets are free text.** The impacted assets have no controlled vocabulary, as RPT-0014's
  TM-026 entry also notes.
- **Some tags look misassigned.** T-14, a supplier providing poisoned training data, carries
  STRIDE E and R rather than T, and T-15, a deprecated inference API, carries E and S. The
  text has small errors ("can can", "egitimate", "leads to leads to"), and the numbering skips
  T-8 and T-27.
- **Specific to AWS services.** Bedrock, OpenSearch Serverless, Cognito and the rest are named
  throughout; mapping the model to another stack is left to the reader.
- **A file that changes.** Earlier versions differ, for example before the 2025-04-02 update;
  the digest pins this content.

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | adjacent | AIT-063, AIT-064, AIT-068, AIT-072, AIT-017, AIT-026, AIT-112, AIT-037, AIT-048, AIT-046, AIT-101, AIT-114, AIT-116, AIT-055, AIT-084, AIT-086, AIT-050, AIT-083, AIT-033, AIT-052 | Names threats but demonstrates none, and no AIT entry cites S-0950. The mapping is ours, by threat statement: direct, indirect and multimodal prompt injection (AIT-063 T-1, AIT-064 T-2, AIT-068 T-33); output reaching classic sinks (AIT-072, T-4 to T-6); poisoning by insiders or data suppliers (AIT-017 T-7, T-14; AIT-026 T-9); cost and denial-of-wallet attacks (AIT-112, T-10 to T-12); compromised open-source dependencies (AIT-037, T-13); training-data leakage and membership inference (AIT-048, AIT-046, T-16 to T-18); over-privileged tools (AIT-101, T-21) and excessive agency (AIT-114, T-22, T-24); acting on wrong outputs (AIT-116, T-23, T-25, T-26); model and data exfiltration (AIT-055, T-28, T-29); sensitive retrieval (AIT-084, T-30); knowledge-base poisoning (AIT-086, T-31); embedding inversion (AIT-050, T-34); system-prompt extraction (AIT-083, T-36); backdoored adapters and model merging (AIT-033, T-37, T-38); and distillation (AIT-052, T-39) |
| Existing AI threat models | core | TM-026 | It is TM-026. The counts in threat-models.md (13 assumptions, 37 threats, 84 mitigations, 95 and 122 links) match the file at this commit |
| Weakness enumerations | adjacent | LLM01:2025, LLM02:2025, LLM03:2025, LLM04:2025, LLM05:2025, LLM06:2025, LLM07:2025, LLM08:2025, LLM09:2025, LLM10:2025 | Every threat carries an OWASP Top 10 for LLM Applications 2025 tag, and all ten categories are used (six threats each under LLM02, LLM03 and LLM06), with STRIDE letters as extra metadata. It uses no CWE or ATLAS ids, and neither NIST AI 100-2e2025 nor ATLAS 2026.09 cites it |
| Attack → asset mapping | core | C12, C07, C11, C06, C13, C19, C02 | Its data flows list the assets each carries, and its trust boundaries sit between named entities. Our mapping: users (C12); the web app, API gateway, Lambda functions and Guardrail (C07); Cognito (C11); OpenSearch Serverless and the embedding pipeline (C06); Bedrock as the model provider (C13); DynamoDB holding questions, answers and audit logs (C19); and the S3 knowledge-base store (C02) |
