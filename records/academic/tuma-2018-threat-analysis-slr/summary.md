---
schema: "library-summary/v1"
id: tuma-2018-threat-analysis-slr
record: tuma-2018-threat-analysis-slr
type: summary
updated: "2026-10-22"
---

# Threat analysis of software systems: A systematic literature review

|  |  |
|---|---|
| **Type** | paper (journal article; systematic literature review) |
| **Maturity** | `peer-reviewed` |
| **Authors** | Katja Tuma, Gul Calikli, Riccardo Scandariato |
| **Published** | Journal of Systems and Software 144, 275–294, October 2018 (Elsevier) |
| **Identifier** | DOI 10.1016/j.jss.2018.06.073 |
| **Source** | Read as Paper A (chapter 2) of the first author's PhD thesis, *Efficiency and Automation in Threat Analysis of Software Systems* (University of Gothenburg, 2021), https://research.chalmers.se/publication/520907/file/520907_Fulltext.pdf |
| **Digest** | `430fb7e7064e604da1abc79223bb08ccdc7eaae7e4e2da88e1bbbae6ea93fcdd` — of the thesis PDF as fetched 2026-10-22. The repository serves a differently stamped copy on every download (same 4,338,577 bytes, different digest), so the digest identifies our copy, not the publication |

## Overview

A systematic literature review of **architectural threat-analysis techniques**,
written to help practitioners choose one. The authors searched ACM, IEEE Xplore and
Google Scholar in **January 2017** (top 5,000 results by relevance), kept venues
ranked by CORE, and added backward snowballing, ending with **38 primary studies
covering 26 techniques**. They group the techniques as risk-centric (e.g. CORAS),
attack-centric and software-centric, plus goal-oriented requirements engineering,
security-requirements engineering and privacy approaches; named examples include
STRIDE, CORAS, PASTA, DREAD, Trike, LINDDUN, attack trees and misuse cases.

Each technique is compared on **applicability, required input, analysis procedure
(including precision and whether it has a stopping condition), outcomes (type,
representation, assurance of quality, granularity) and ease of adoption**. In
their description of attack trees, an **attack path** is "a single path starting at
leaf node leading to the root node". Their findings: the analysis procedure is
not precisely defined, the quality of outcomes is not assured, and **tool support
and validation are limited** — 9 techniques have no tool, 13 have a tool and 4 a
prototype, about a third (9) were validated only by illustrations, and the
existing tools "typically only aid the graphical representation of threats,
rather than the analysis of threats".

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | A peer-reviewed survey of threat-analysis techniques with explicit comparison criteria. |
| Cryptography | none | Not about cryptography. |
| This project | core | Evidence for RPT-0002's comparison: its criteria (procedure, stopping condition, outcome assurance, tool support) and its findings on manual, weakly tooled analysis bear directly on what tmodel automates. |

Bears on **DEC-001** (object model) and the RPT-0002 gap analysis.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this summary |

## Limits

- **Literature up to January 2017**, software design level only: OCTAVE, the Cyber
  Kill Chain and ATT&CK are not covered.
- **Read in the thesis reprint:** section and page numbers are the thesis's, not the
  journal's.
