---
schema: "library-summary/v1"
id: bron
record: bron
type: summary
updated: "2026-10-25"
---

# Linking Threat Tactics, Techniques, and Patterns with Defensive Weaknesses, Vulnerabilities and Affected Platform Configurations for Cyber Hunting (BRON)

|  |  |
|---|---|
| **Type** | paper |
| **Maturity** | white-paper (arXiv preprint; the PDF's ACM block is an unfilled template, p. 1) |
| **Authors** | Erik Hemberg, Jonathan Kelly, Michal Shlapentokh-Rothman, Bryn Reinstadler, Katherine Xu, Nick Rutar, Una-May O'Reilly (MIT CSAIL; Perspecta Labs) |
| **Published** | 2020-10-01 (v1); 2021-02-10 (v2, the version held) |
| **Identifier** | arxiv: 2010.00533v2 |
| **Source** | https://arxiv.org/pdf/2010.00533v2 |
| **Digest** | `00879ac47493bdc27f7ed3e5406a8f7dfe164dbec9f8c1bca0aecfe1e2a0d4c3` |

## Overview

The paper builds BRON, one graph that joins ATT&CK tactics and techniques, CAPEC attack patterns, CWE weaknesses, CVE vulnerabilities and the CPE-named affected product configurations from NVD. Each catalog entry is kept as a node with its verbatim properties, and every cross-catalog link is stored so it can be walked in both directions (§3, p. 3; Fig. 1, p. 2). The authors use it for threat hunting in two directions: top-down from a tactic to the affected products, and bottom-up from a product's CVEs to the tactics (§4, pp. 3-4; worked example §4.1, p. 4). Their main finding is about the data, not the tool. The chain is often broken: 28% of the CVEs counted and 25% of the 519 CAPEC patterns link to nothing, 74% of techniques have no CAPEC pattern, and only 10% of CAPEC patterns reach both a technique and a weakness (§5.1-5.1.1, pp. 7-8). Only 4 of the 2016-2019 "top 10 exploited" CVEs reach any tactic (§4.3.1, Table 2, pp. 5-6). The authors cannot tell whether a missing link means the attack does not exist or that nobody has curated it yet (pp. 6, 8).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | Built from the catalogs tmodel imports, and it measures how complete their cross-links are. |
| Cryptography | none | Has no cryptographic content. |
| This project | core | It is an existing build of the CVE→CWE→CAPEC→ATT&CK backbone in ADR-0002, which tmodel's KG reuses (RPT-0011). |

Bears on **DEC-001** (core types: Weakness / Vulnerability / AttackPattern and the `instance_of` Assertion), **DEC-003** (shows the trouble with summed CVSS, which supports ADR-0006's composite vector), **DEC-008** (snapshot currency vs live sources), **DEC-009** (version noise when mapping a threat to a product), **R-010** and **R-020**. The full analysis and the tmodel implications are in `distilled/design-notes.md`.

## Implementations

| Name | Kind | License | URL |
|---|---|---|---|
| BRON (ALFA group, MIT CSAIL): Python build scripts, ArangoDB graph, Jupyter tutorials | open source | MIT | https://github.com/ALFA-group/BRON |
| Public BRON ArangoDB instance (the paper says it is "updated daily", p. 12; reachability not checked 2026-10-25) | hosted service | n/a | http://bron.alfa.csail.mit.edu:8529 |

Searched 2026-10-25 for BRON itself only. The repo's last commit is 2025-11-09. Its README now also links MITRE Engage, D3FEND, CAR and ATLAS, which the paper does not cover. The related knowledge graphs the paper names (STUCCO, SEPSES, UCO; §7, p. 12) are listed in `cites`. No commercial product was searched.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, `cites` (from the paper's reference list), relations, `bears_on`, distillation block |
| `summary.md` | this summary |
| `quotes.md` | the few verbatim passages relied on, each with a page/section locator |
| `distilled/README.md` | index of the distilled artifacts and what they cover |
| `distilled/design-notes.md` | analysis of the paper and its implications for tmodel (object model, attack paths, risk metric, KG, agentic threats, DEC-001b/008/009), plus draft follow-up issues |

## Limits

- **A snapshot from 2020.** The data is the March 2020 sources, with CVEs refreshed in June 2020 (p. 3). The paper models 12 ATT&CK tactics. Every count describes 2020 catalogs, not today's. tmodel's RPT-0005 later found that the CAPEC→ATT&CK links are pinned to ATT&CK 12.0 and that ATT&CK v13 dropped the reverse direction (`research/0005-schema-representations/fanout-attack-composition.md`). So BRON's top layers are probably staler than this paper suggests.
- **The numbers in the text and tables disagree in places.** CWE-200 has 6,624 CVEs in §2 and §5.1.1 but 6,824 in Table 3. It is the target of 57 CAPEC patterns in §5.1.1 but 58 in Table 3. CWE-79 "connects to the most Vulnerabilities at 1,292" (p. 8), but Table 3 gives 12,629. "71,715 Vulnerabilities" (p. 7) sits beside Table 4's 144,594 with no explanation; it may be the 2015-2020 subset in Fig. 6. Cite the tables, and treat the prose figures with care.
- **No attack semantics.** BRON's "paths" walk links between catalogs. They have no AND/OR structure, preconditions, feasibility or environment. A Tactic→CPE path says an attack is possible in principle, not that it is feasible against a given system.
- **Risk is a sum of CVSS scores.** The "riskiest software" query and the operational vs non-demonstrated severity split add up CVSS scores (§5.3, §6, pp. 10-11). The paper itself notes that CNAs score differently and that NVD gives 10 to CVEs with no information (p. 8).
- **Weak evaluation.** Usability is measured only as query time and memory against a JSON baseline (Table 5, p. 12). There is no study with users. The authors say practitioner utility "needs to be further evaluated" (§9, p. 13).
- **Inherited bias.** It uses public NVD data only. CVEs without IDs and every bias in the sources carry straight through (§8, p. 12).
