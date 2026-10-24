---
schema: "library-summary/v1"
id: khodayari-2026-ipi-in-the-wild
record: khodayari-2026-ipi-in-the-wild
type: summary
updated: "2026-10-13"
---

# Indirect Prompt Injection in the Wild: An Empirical Study of Prevalence, Techniques, and Objectives

|  |  |
|---|---|
| **Type** | paper (web measurement study; 18 pp.) |
| **Maturity** | _unset — do not guess_ |
| **Authors** | S. Khodayari, X. Zhang, B. Acharya, G. Pellegrino (CISPA and others) |
| **Published** | arXiv v1, 2026-04-29 (no venue stated) |
| **Identifier** | arXiv:2604.27202 |
| **Source** | https://arxiv.org/pdf/2604.27202 |
| **Digest** | `3f2430963a1dd7164fcb473330cf607f10a76ecc5c82b73b6277a44d404f212d` (matches `pdf-manifest.tsv`) |

## Overview

A large-scale measurement of **indirect prompt injections already present on the public web**. Scanning 1.2 billion URLs from 24.8 million hosts (Common Crawl and HTTP responses), it validates 15.3K injection instances on 11.7K pages, most coming from a few recurring templates. It classifies their **objectives** (disruption, reputation manipulation, content-protection directives, AI-bot detection), **delivery**, **visibility** and **persistence**, and the systems they target (crawlers, search pipelines, customer-support agents, hiring workflows). About 70% sit in non-rendered HTML (headers, comments, metadata) — aimed at machines, not people. In 5,200 controlled runs across 13 models and four page representations, compliance is limited but real (up to 8% for smaller models on plain text), and structured page representations reduce it.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | Real-world evidence for the most common agent attack class. |
| Cryptography | none | Not about cryptography. |
| This project | core | Shows where untrusted content enters agent pipelines in practice, and how often it works — inputs to likelihood/feasibility. |

Bears on **DEC-001** (object model — untrusted web content as an attack-path entry point).

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | core | AIT-064, AIT-067, AIT-090, AIT-133 | In-the-wild indirect injection; hidden instructions; SEO-style manipulation |
| Existing AI threat models | none | — | A measurement, not a threat model |
| Weakness enumerations | adjacent | AML.T0051.001, AML.T0068, LLM01:2025, NISTAML.015 | Catalog entries for the observed attacks; the paper maps none |
| Attack → asset mapping | core | C01, C06, C07, C08, C12 | Web sources feed retrieval/search, apps and agents, and human workflows such as hiring |

## Implementations

No tool released as far as the PDF states. Searched 2026-10-13.

| Name | Kind | License | URL |
|---|---|---|---|


## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this summary |

## Limits

- **Preprint** (v1), not yet peer-reviewed.
- **Lower bound.** Detection depends on the authors' templates and validation; injections in other channels are missed.
- **Compliance tests are controlled,** not observed attacks on deployed agents.
- Reference expansion not done in this pass (see PR notes).
