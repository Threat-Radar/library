---
schema: "library-summary/v1"
id: sagai-workshop
record: sagai-workshop
type: summary
updated: "2026-11-02"
---

# SAGAI — IEEE Security and Privacy workshop series on securing generative AI

|  |  |
|---|---|
| **Type** | hierarchy (workshop series) |
| **Maturity** | _unset_ — a venue, not a document |
| **Organizers** | Mihai Christodorescu, John Mitchell, Somesh Jha, Khawaja Shams; Earlence Fernandes from 2025 |
| **Editions** | 2024, 2025, 2026 — co-located with IEEE S&P, San Francisco |
| **Identifier** | sites.google.com/view/sagai2024 · sites.google.com/ucsd.edu/sagai25-ieee-sp · sites.google.com/view/sagai-2026 |
| **Source** | https://sites.google.com/view/sagai2024/home |
| **Digest** | none — web pages |

## Overview

A workshop series at the IEEE Symposium on Security and Privacy on the security of
systems built on generative AI. **SAGAI'24** (*Security Architectures for GenAI Systems*,
May 23 2024) accepted peer-reviewed papers, published in the IEEE SPW 2024 proceedings.
**SAGAI'25** (*Secure Generative AI Agents Workshop*, May 15 2025) ran as invited talks and
panels with no papers; its stated output is a joint research-challenges document.
**SAGAI'26** (*Secure Agents for Generative Artificial Intelligence*, May 21 2026) is listed
by IEEE S&P; its program page was not available (404) on 2026-09-29. Three of its papers
were found on arXiv on 2026-11-02 by their authors' acceptance notes and are members:
`pentest-lessons-agent-systems`, `cacheprobe-prompt-cache-isolation` and
`agentic-reverse-engineering-challenges`.

The series' through-line is that GenAI security is a property of the **whole system**, not
only the model: its 2024 topics include input sanitization, prompt-injection defenses,
output validation and secure composition of GenAI components.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Security of GenAI-based systems is the whole subject |
| Cryptography | `none` | Not a topic of the series |
| This project | `adjacent` | Confirmed target of tmodel #13; its papers bear on DEC-001 (AI threat types) |

This record is a **container**: it bears on nothing itself. Members point here with
`part_of`; see `has_part` in `index/crosswalk.md`.

## Implementations

Not applicable to a workshop series; see the member papers.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this document |

## Limits

- **SAGAI'25's output is a member since 2026-11-02.** `systems-security-agentic-computing`
  is the research-challenges document: its v1 introduces itself as the report of "the IEEE
  Secure Generative AI Agents 2025 workshop (SAGAI ...)" (tmodel #189). Its follow-up,
  `agent-security-systems-problem`, names no workshop and stays `see_also`.
- **SAGAI'26 is only partly held.** Three papers are members (2026-11-02, tmodel #189,
  RPT-0009 Phase 4 review F-07), found by an arXiv search for "SAGAI" in the comment field;
  membership rests on each paper's own "accepted at SAGAI 2026" note. The full program is
  still unpublished, so other SAGAI'26 papers may exist.
- **Name clash.** Fraunhofer IESE runs an unrelated "SAGAI" workshop (*Software
  Architecture and Generative AI*, at ICSA); it is out of scope here.
