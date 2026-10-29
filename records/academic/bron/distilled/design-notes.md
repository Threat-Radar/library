---
schema: "library-doc/v1"
id: bron-design-notes
record: bron
type: design-notes
updated: "2026-10-25"
reviewed_by: ""
---

# Design notes: BRON (arXiv:2010.00533v2) against tmodel

Targets: ADR-0002 (MVP backbone CVE → CWE → CAPEC → ATT&CK "via the BRON backbone"), ADR-0006 (composite risk vector), ADR-0010 (DEC-001a core types; DEC-001b held), DEC-008, DEC-009, R-010, R-020, PLAN-0002 §5, RPT-0011, RPT-0004 `mapping.md`, RPT-0005 `fanout-attack-composition.md`. Locators like (p. 7) are PDF pages of v2. **Inference** marks a conclusion we draw that the paper does not state.

## 1. Analysis

### 1.1 What BRON is

- **Six node layers**, one per source: Tactic, Technique (ATT&CK), Attack Pattern (CAPEC), Weakness (CWE), Vulnerability (CVE), Affected Product Configuration (CPE strings from the NVD CVE entry). CVSS is a property of the CVE, not a layer (Table 1, p. 3; Fig. 1, p. 2).
- **Edges exist only between adjacent layers:** Tactic-Technique, Technique-CAPEC, CAPEC-CWE, CWE-CVE, CVE-CPE (§1, p. 2). The source links mostly point one way. BRON stores them so they can be walked both ways and tags which way the source pointed (§3, p. 3; quote 2).
- **Node properties are the verbatim source entry**, standardised across types. CPE notation is kept as-is (§3, p. 3).
- **Two query modes** for hunting: top-down from a tactic or APT goal to products, and bottom-up from a product's CVEs to tactics (§4, pp. 3-4). The worked path is TA0003 → T1574.010 → CAPEC-17 → CWE-264 → CVE-2011-1185 → Chrome before 10.0.648.127 (§4.1, p. 4; Fig. 2, p. 5).
- **Implementation:** ArangoDB ("BRON-Graph-DB") against a JSON-in-memory baseline. The graph DB is about 4× faster on the small query and about 2× on the medium one, but about 10 s slower on the large "riskiest software" aggregation. It uses far less memory (Table 5, p. 12).

### 1.2 Findings that matter

| Finding | Locator |
|---|---|
| 28% of the 71,715 CVEs counted and 25% of the 519 CAPEC patterns link to nothing ("Floating Entries"); 1 of 266 techniques floats | §5.1, p. 7 |
| 74% of techniques have no CAPEC pattern; only 10% of CAPEC patterns reach both a technique and a weakness; the three most-linked CAPEC patterns (13 links each) link only to weaknesses | §5.1.1, p. 8 |
| About 45% of CWEs are the target of some CAPEC pattern | §5.1.1, p. 8 |
| Only 4 of the US-CERT "top 10 exploited 2016-2019" CVEs reach any tactic. CVE-2017-0143 has no CWE and no CPE in BRON. CVE-2017-11882 reaches CWE-119 and 12 CAPEC patterns, but none of those patterns has a technique | §4.3.1, Table 2, pp. 5-6 |
| 4 of the 2020 CWE Top 25 have no CAPEC pattern; the Top 25 involve 8 distinct tactics | §4.3.2, Table 3, pp. 6-7 |
| Keeping only the latest version of each product cuts the CPE nodes by about 80% (219,767 → 42,061) | §5.1, pp. 7-8 |
| CVEs with no link tend to have low CVSS scores; nearly 25% of "non-demonstrated" CVEs score 0 | §5.3, p. 10 |
| CVSS varies between CNAs; NVD gives 10 to CVEs with no information | §5.1.1, p. 8 |
| The share of CVEs with no CWE fell from 87% (2006) to 18% (2008); the ratios have been fairly stable since 2008 | §5.2-5.3, p. 10 |

### 1.3 Critique

- **Breaks are measured, but their meaning is unknown.** The authors say several times that they cannot tell "no attack known" from "not curated yet" (pp. 6, 8; quote 3). This is the paper's most useful result for us. A consumer that reads a missing link as safety is wrong.
- **The numbers in the text and tables disagree** (CWE-200: 6,624 vs 6,824 CVEs and 57 vs 58 CAPEC patterns; CWE-79: 1,292 vs 12,629; 71,715 vs 144,594 CVEs). See `summary.md` § Limits. Prefer the tables.
- **A link is not an attack path.** Edges are catalog cross-references. Nothing models conjunction, preconditions, reachability, deployment or the attacker's capability. "Path" in the paper means graph traversal (§4.1).
- **Risk means summed CVSS.** The paper's "riskiest software" and its severity sums add CVSS scores (§5.3, p. 10; §6, p. 11) while also showing why CVSS is noisy (p. 8). It does not reconcile the two.
- **Currency.** The data is a 2020 snapshot (p. 3), and the authors name staleness as the risk that BRON itself adds (quote 7). tmodel's own RPT-0005 found the CAPEC→ATT&CK links pinned to ATT&CK 12.0, 15 of 272 pointing at revoked techniques, and the ATT&CK → CAPEC direction dropped in ATT&CK v13. A rebuilt BRON inherits all of that.
- **Evaluation** covers performance only. The value to practitioners is still unmeasured (§9, p. 13).

## 2. Implications for tmodel

### 2.1 Object model (DEC-001a, accepted; ADR-0010)

| BRON layer | tmodel target | Adopt / adapt / reject |
|---|---|---|
| Tactic | `AttackStep.kill_chain_phase` (coarse order), not a node | **adapt.** ADR-0010 keeps the kill-chain phase on AttackStep. A Tactic node is only needed if the KG view (PLAN-0002 B3) must draw it. |
| Technique (ATT&CK) | `AttackPattern` with an ATT&CK `catalog_ref` | **adopt.** The schema already lets AttackPattern stand for both CAPEC and ATT&CK. BRON's Technique and CAPEC links become Assertions between two AttackPatterns. |
| Attack Pattern (CAPEC) | `AttackPattern` with a CAPEC `catalog_ref` | **adopt** |
| Weakness (CWE) | `Weakness` | **adopt.** The CWE↔CAPEC link stays a reviewed Assertion, as ADR-0010 has it. |
| Vulnerability (CVE) | `Vulnerability`; CVE→CWE is an Assertion `instance_of` (DL-0022) | **adopt** |
| Affected Product Configuration (CPE) | the `identifiers` slot on `Product` / `ProductInstance`; `Vulnerability.affects` | **adapt.** BRON makes each CPE string a node. tmodel keeps CPE as an opaque identifier on an identity-bearing instance (ADR-0010). This keeps 219k version nodes out of the model graph. |
| Bidirectional storage, source direction tagged | the Assertion's subject/predicate/object, with the direction kept | **adopt.** Store each link once with the source's direction. Walking it in reverse is a query concern, as ADR-0004 and ADR-0008 have it. |
| CVSS as a node property | evidence only; never a `RiskScore` input | **reject as risk** (see 2.3) |

**Inference:** BRON's edges carry no provenance beyond which catalog they came from. tmodel needs more on every imported link: the catalog release and the authority (CNA vs NVD/ADP for CVE→CWE). That is exactly what RPT-0004 `mapping.md` finding 5 says the Assertion class cannot hold yet. BRON shows this is needed at scale, because the same chain changes between releases (RPT-0005).

### 2.2 Attack paths (AND/OR steps)

- A BRON traversal is **candidate context** for an `AttackPath`, not an AttackPath. BRON has no AND/OR `gate`, no `precedes`, no feasibility. **Inference:** use top-down queries to *propose* AttackSteps for a ThreatInstance, with the matching AttackPattern as `catalog_ref`. Use bottom-up queries to *propose* which ThreatInstances a product's CVEs could serve. Both come in as `proposed` Assertions that need a Review (R-018).
- The break rates (§1.2) mean **most real chains will stop before ATT&CK.** The KG view and the path builder must show a truncated chain as "chain ends here (no catalog link)". They must not drop it, and they must not draw a default technique.

### 2.3 Risk metric (DEC-003 → ADR-0006)

- The paper is **evidence for ADR-0006's scope guard** ("no single-number CVSS substituted for the vector"). Its own data shows that CVSS varies by CNA, is set to 10 when information is missing, and that sums are dominated by version counts (pp. 8, 10). Summing CVSS by product would rank whatever has the most CPE versions.
- **Inference:** BRON's "operational vs non-demonstrated" split (has a CPE vs has none; §5.3) is a useful *evidence* flag beside the 21434 Table-1 feasibility rating. A Vulnerability with no affected-product evidence should not raise path feasibility by itself. Keep it as an annotation, not a component, unless the sponsor adds a vector component (ADR-0006 needs a further decision for that).

### 2.4 Knowledge graph

- **Confirms RPT-0011's "reuse the BRON backbone",** but with a narrower meaning: reuse the *shape* (six layers, edges only between adjacent layers, verbatim properties, source direction kept). Do not reuse the 2020 *data*. Whether to reuse BRON's *code* (MIT license; an ArangoDB stack against tmodel's Oxigraph, ADR-0008) is a separate question that has not been evaluated.
- **Coverage is a first-class output.** BRON's inventory of floating and super entries (§5) is exactly the report a tmodel model should produce about its own imports: how many Vulnerabilities have no Weakness, how many AttackPatterns have no technique, which edges come from which release.
- **Version noise:** filter by product version before counting or displaying anything (an 80% reduction, p. 8). Otherwise the hubs in the graph are old Debian and Windows releases, not the system under analysis.

### 2.5 Agentic threats

- **The paper says nothing about AI or agents.** It predates LLM agents. The BRON *repo* now links MITRE ATLAS (README, last commit 2025-11-09). That suggests ATLAS techniques could be attached to the same backbone for the AI Threat Model lane (tmodel #73-#75), but this record has not checked how ATLAS is linked.
- **Inference:** if a tmodel agent walks a BRON-shaped graph to propose threats, the gaps become agent behaviour. An agent will either stay silent where links are missing or fill the gaps with guesses. Every agent proposal therefore needs (a) the catalog release it walked, (b) any "chain ends here" points it crossed, and (c) `proposed` status until Reviewed. This is ADR-0010's "never present AI output as reviewed" applied to KG traversal.
- **Inference:** the catalogs and their cross-links become part of the input an agent trusts. If the catalog mirror is poisoned or stale, the agent proposes wrong threats. This is a reason for DEC-008 to favour a pinned, digested mirror.

### 2.6 Open decisions

- **DEC-001b (governed layer): indirect.** **Inference:** for "reproducible approval" (DL-0020 C2, `approval_digest`) to be reproducible, an approved ThreatModel must bind the catalog snapshot it was built on (CWE/CAPEC/ATT&CK/NVD releases and digests). BRON's own stated risk is an unpinned snapshot (quote 7). M5 (author/origin) also applies to imported links. The paper does not address governance.
- **DEC-008 (CWE/NVD live vs cached): supports a cached mirror with pinned versions, plus a refresh job.** The paper's model (download, build, refresh by script, p. 12) is a cached mirror. Its stated risk is staleness, and its numbers move with the snapshot date (pp. 3, 10). **Inference:** cache, pin, digest and date every catalog release, as the library does with `library@<commit>`. Refresh on purpose, and diff the coverage report across refreshes. This fits A-043 (offline core loop).
- **DEC-009 (generic threat → product / family):** BRON's product mapping uses the vendor-product fields of the CPE string (3rd and 4th fields, p. 4) and pools every version of a product. The browser comparison, for example, "included any version of the browser" (§4.2, p. 4). **Inference:** for tmodel, map a generic threat to a family by vendor-product, but to a `ProductInstance` only by version range (CPE match criteria). Treat any link from a generic threat to a product as a `proposed` Assertion. Family members can differ per path (R-021).

## 3. Draft follow-up issues (not opened)

1. **Catalog-link provenance on Assertion** (DEC-001a follow-up / #17): record the source catalog, its release and the authority (CNA, NVD, ADP) on each imported CVE→CWE, CWE→CAPEC and CAPEC→ATT&CK Assertion. Extends RPT-0004 `mapping.md` finding 5.
2. **Coverage report for imports** (#61, B3): for each model, count Vulnerabilities with no Weakness, Weaknesses with no AttackPattern, and AttackPatterns with no technique, and show truncated chains in the KG view. Modelled on BRON §5.
3. **DEC-008 ADR input:** a pinned, digested catalog mirror with a dated refresh and a coverage diff; cite this record together with `anwar-2020-cleaning-nvd`.
4. **Version-aware product matching** (DEC-009 / R-020): CPE version-range matching for ProductInstance, with a test that vendor-product-only matching is never used for an instance.
5. **Evaluate reusing BRON code** against our own loader: check the currency of ATT&CK↔CAPEC links after v13 (RPT-0005 open item 9) and how ATLAS is linked, and weigh an ArangoDB dependency against ADR-0008.
6. **Library stubs** for the related work the paper cites but the library does not hold: STUCCO, SEPSES, UCO, Xiao 2019 link prediction, Feutrill 2018 (CVSS and exploit delay). See `cites`.

## 4. Open questions

- Is the 71,715 in §5.1 the 2015-2020 subset in Fig. 6? The paper does not say.
- Does the current BRON still carry CAPEC→ATT&CK links that ATT&CK has revoked, and does it mark them?
