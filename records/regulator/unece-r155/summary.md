---
schema: "library-summary/v1"
id: unece-r155
record: unece-r155
type: summary
updated: "2026-11-02"
---

# UN Regulation No. 155: Uniform provisions concerning the approval of vehicles with regards to cyber security and cyber security management system

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | `standard` |
| **Authors** |  |
| **Published** | 2021-03-04 (in force as an annex to the 1958 Agreement since 22 January 2021) |
| **Identifier** | un_symbol: E/ECE/TRANS/505/Rev.3/Add.154 |
| **Source** | https://documents.un.org/doc/undoc/gen/g21/054/90/pdf/g2105490.pdf |
| **Digest** | `c41424c6f17784aa7cf8d3de79491e6bce142a674748039f1235dc8c37ea9654` |

## Overview

UN Regulation No. 155 makes cyber security a condition of vehicle type approval. It applies to vehicles of categories M and N, to category O with at least one electronic control unit, and to L6 and L7 with automated driving from level 3 (§1). It asks for two things.

- **A Cyber Security Management System for the manufacturer**, certified by an approval authority for up to three years (§6). Its processes must cover development, production and post-production, and must consider the threats in Annex 5 when identifying, assessing, treating and monitoring risks (§7.2).
- **Per vehicle type:**
  - a risk assessment of the type's critical elements and their interactions that considers every Annex 5 Part A threat (§7.3.3);
  - proportionate mitigations (§7.3.4);
  - testing before approval, attack detection and prevention, and forensic data (§7.3.6, §7.3.7);
  - management of supplier risks, protected environments for aftermarket software, and cryptographic modules in line with consensus standards (§7.3.2, §7.3.5, §7.3.8).

The manufacturer then reports monitoring results to the approval authority at least once a year (§7.4).

Annex 5 is the regulation's catalogue:

- **Part A** lists 67 example attacks and vulnerabilities under 30 high-level threats.
- **Parts B and C** pair those examples with 23 numbered mitigations, for vehicles (Part B) and for systems outside the vehicle such as back-ends (Part C).
- Under §7.3.4, every Part B or C mitigation relevant to an identified risk must be implemented, or replaced by another appropriate measure.

The regulation never mentions software bills of materials, which is why RPT-0004 (tmodel#38) cites it.

## Applicability

- **Security: core.** It is a binding type-approval regime for vehicle cyber security: a management system, plus a risk-based threat and mitigation catalogue.
- **Cryptography: adjacent.** §7.3.8 asks for cryptographic modules in line with consensus standards and for a justification otherwise. Annex 5 covers key storage (M11) and cryptographic weaknesses (threats 26.1 to 26.3), but sets no algorithm or key-length requirements.
- **This project: core.** Annex 5 is the "generic mitigation becomes a requirement" case that ADR-0012 adds to the core object model (DEC-001a). It also gives a regulator-defined product scope for DEC-009 (generic threat to product family). tmodel#172 extracts it into `research/0017-requirements-extraction/unece-r155.yaml`: 26 Requirements, 23 Mitigation stubs, 70 ThreatInstance stubs and the annex's pairings as proposed links.

## Implementations

A regulation, not software.

- **Open source.** A GitHub search for "UNECE R155" on 2026-11-02 found only small personal projects: an explorer, a 2022 test interface, translations and concept repositories. None is a base to build on.
- **Commercial.** Commercial TARA and CSMS tools were not surveyed.
- **Related standard.** The regulation itself names ISO/SAE 21434 (`iso-sae-21434-2021`) as an example of the knowledge approval-authority staff should have (footnote to §5.3.1).

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this summary |

## Limits

- **One version.** Only the original version (Add.154) was read. Later supplements and amendments were not, so changes to the threat or mitigation lists after 2021 are not reflected.
- **Outcomes, not methods.** The regulation sets outcomes. It names no risk method, metric or test depth. The interpretation document its footnotes refer to (§5.3.3, §5.3.5) was not read.
- **Annex 5 inconsistencies:**
  - Table C3 cites threats 30.1 to 30.3, which Table A1 does not list.
  - Table A1 has no threat 14 and no example 22.1.
  - M17 is not used.
  - The M7 cell (rows 20.3 to 20.5) and the M23 cell (rows 28.1 to 29.2) carry extra, unnumbered measures.
- **Merged cells.** Several Part B and C rows share one mitigation through merged cells, which plain text extraction loses. The tmodel extraction read the pairings from the rendered pages.
- **Annexes 1 to 4** (information document, communication form, approval mark, CSMS certificate model) were not read beyond their titles.
