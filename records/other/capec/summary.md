---
schema: "library-summary/v1"
id: capec
record: capec
type: summary
updated: "2026-10-25"
---

# MITRE CAPEC 3.9 — Common Attack Pattern Enumeration and Classification

|  |  |
|---|---|
| **Type** | dataset (best-practice) |
| **Publisher** | The MITRE Corporation |
| **Version** | CAPEC List 3.9 (catalog date 2023-01-24) |
| **Source** | https://capec.mitre.org/data/xml/capec_v3.9.xml (same bytes as `capec_latest.xml` on 2026-10-25) |
| **Digest** | `70279a2dff0cb0ad79e546adb07828335a704ad5210e047e09e986172fc9e34d` |

## Overview

CAPEC is MITRE's catalog of attack patterns. Each entry describes how an adversary exploits a class of weakness. Entries link down to CWE (`Related_Weaknesses`) and across to ATT&CK (`Taxonomy_Mappings`, taxonomy `ATTACK`). Version 3.9 is still the current release; `capec_latest.xml` and `capec_v3.9.xml` had the same digest when this record was written.

**Counts computed from the 3.9 XML (2026-10-25):**

| Measure | Count |
|---|---|
| Attack_Pattern entries | 615 |
| by status | Draft 402 · Stable 154 · Deprecated 56 · Usable 2 · Obsolete 1 |
| non-deprecated (matches the site's "Total Attack Patterns: 559") | 559 |
| non-deprecated with ≥1 related CWE | 450 |
| non-deprecated with ≥1 ATT&CK mapping | 177 |
| CAPEC→ATT&CK mappings | 272, to 189 distinct ATT&CK ids |

**Currency against ATT&CK Enterprise v20.0** (`mitre-attack`): 16 of the 272 mappings no longer resolve to a live Enterprise technique. 15 point to revoked techniques: 14 under T1562 (Impair Defenses) sub-techniques plus T1574.002, which together affect CAPEC-13, 268, 571, 578 and 641. One (CAPEC-648 → T1513) is not in the Enterprise bundle at all; T1513 is a Mobile-domain id. This is consistent with tmodel RPT-0005, which pins CAPEC→ATT&CK to ATT&CK 12.0.

## Applicability to tmodel

| Axis | Rating | Why |
|---|---|---|
| Security | core | The standard attack-pattern vocabulary. |
| Cryptography | adjacent | Some patterns cover crypto misuse. |
| This project | core | The CWE→CAPEC→ATT&CK hop of the ADR-0002 backbone and the `AttackPattern` node of DEC-001a (ADR-0010). |

Bears on **DEC-001** (AttackPattern covers CAPEC+ATT&CK), **DEC-008** (cached vs live: CAPEC has been frozen since 2023-01, so caching it costs nothing), and **DEC-009** (generic patterns → product).

**Implications for tmodel (inference).** (1) Only 177 of 559 live patterns map to ATT&CK at all. A CVE→CWE→CAPEC→ATT&CK walk will dead-end for most CWEs, so the importer must treat a missing ATT&CK hop as normal, not as an error. (2) The CAPEC→ATT&CK edge must carry an ATT&CK version and a resolution status (live, revoked→replacement, other-domain). With v20.0, 16 of 272 edges need that handling. (3) Most entries (402) are Draft; status is worth keeping as an attribute on the imported node so reviewers can weight it.

## Implementations

Not searched beyond the BRON pipeline (`bron`), which already ingests CAPEC.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata; pinned 3.9 XML digest |
| `summary.md` | this summary |

## Limits

- Counts are from one XML snapshot and a short script (XPath over `Attack_Pattern`, `Related_Weakness`, `Taxonomy_Mapping[@Taxonomy_Name="ATTACK"]`). They were not cross-checked against MITRE's own view files.
- Revocation status was checked only against the Enterprise v20.0 bundle, not Mobile or ICS.
- No reading of individual pattern prose; this is a dataset-level summary.
