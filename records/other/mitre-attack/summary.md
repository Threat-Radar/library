---
schema: "library-summary/v1"
id: mitre-attack
record: mitre-attack
type: summary
updated: "2026-10-25"
---

# MITRE ATT&CK — Enterprise v20.0 (STIX 2.1 data)

|  |  |
|---|---|
| **Type** | dataset (best-practice) |
| **Publisher** | The MITRE Corporation |
| **Version** | Enterprise ATT&CK 20.0 (collection `modified` 2026-10-13) |
| **Source** | https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-20.0.json |
| **Digest** | `81113ba98afa2928f3dcff62022539f7ce30c315c32e14422f11ff95ce534352` |

## Overview

ATT&CK is MITRE's knowledge base of adversary tactics and techniques, published as STIX 2.1 bundles (`stix-2-1`) per domain (Enterprise, Mobile, ICS). Techniques are `attack-pattern` objects, tactics are `x-mitre-tactic`, mitigations are `course-of-action`, and edges are STIX `relationship` objects.

**Counts computed from the Enterprise v20.0 bundle (2026-10-25), excluding revoked and deprecated objects:**

| Measure | Count |
|---|---|
| tactics | 15 |
| techniques + sub-techniques | 706 (227 top-level) |
| mitigations (`course-of-action`) | 44 |
| relationships by type (non-revoked) | uses 18,975 · mitigates 1,477 · detects 703 · subtechnique-of 481 · revoked-by 157 · attributed-to 26 |
| live techniques carrying a CAPEC external reference | 0 |

The v20.0 tactic list includes **Stealth** and **Defense Impairment** and has no "Defense Evasion". This is a change from the 14-tactic Enterprise matrix that tmodel's earlier reports assume. Read from the tactic objects; the release notes were not read.

## Applicability to tmodel

| Axis | Rating | Why |
|---|---|---|
| Security | core | The common adversary-behaviour vocabulary. |
| Cryptography | adjacent | Covers credential and crypto abuse only as techniques. |
| This project | core | The terminal hop of the ADR-0002 backbone; `kill_chain_phase` on `AttackStep` (DEC-001a) takes its values from ATT&CK tactics. |

Bears on **DEC-001** and **DEC-008**.

**Implications for tmodel (inference).** (1) No live v20.0 technique points back to CAPEC, which confirms RPT-0005: the ATT&CK→CAPEC direction is gone, and the only bridge is CAPEC's own mappings (`capec`), pinned to old ATT&CK ids. (2) `kill_chain_phase` values must be versioned. A v12-era path labelled "defense-evasion" has no v20 tactic of that name, so any stored phase needs the ATT&CK version alongside it. (3) The `revoked-by` relationships (157) give a mechanical way to forward stale CAPEC→ATT&CK edges to their replacements. That is a cheap importer step and a natural DEC-008 "cached + refresh" check.

## Implementations

Official data: `mitre-attack/attack-stix-data` on GitHub. Other tools were not searched.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata; pinned v20.0 bundle digest |
| `summary.md` | this summary |

## Limits

- Enterprise domain only; the Mobile and ICS bundles were not read.
- Counts come from a short script over the STIX bundle (filtering `revoked` and `x_mitre_deprecated`). They were not reconciled with the ATT&CK website's counts.
- The tactic rename is inferred from the data, not from release notes.
