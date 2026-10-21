---
record: cwe
kind: design-notes
title: "cwe — bearing on our design"
extracted: "2026-10-08"
reviewed_by: ""
---

How CWE bears on tmodel. Quotes are from `cwe_schema_v7.3.xsd` (SHA-256
`690dedee…e45f98`) by line; data facts are from `cwec_v4.20.xml` (CWE List 4.20,
2026-04-30) and can be re-derived from `examples/catalog-stats.yaml`. Decision ids
are tmodel's: ARCH-0001 §3 (object model), R-010 (map Weakness→CWE), R-018
(review), R-021/R-022, DEC-001a (core object model, accepted as ADR-0010), DEC-001b
(governed layer, open), DEC-002 (encoding and imports, accepted as ADR-0007), DEC-003
(risk, accepted as ADR-0006), DEC-008 (CWE/NVD integration, open), DEC-009
(generic→product, open), ADR-0004 (file canonical store, typed edges with properties).

CWE is a **catalog**, not a protocol: one authority (MITRE) publishes a versioned
XML file, and everyone else reads it. So the design question is not "do we
implement CWE" but "how do we import it, cite it, and keep citations honest".

## What we adopt

1. **The CWE id as the external key of a tmodel Weakness** (R-010, DEC-001). The
   id is an integer shared by weaknesses, categories and views, and it is stable:
   "It is considered static for the lifetime of the entry. If this entry becomes
   deprecated, the identifier will not be reused." (L83). A tmodel Weakness
   stores `cwe_id` as an integer plus the catalog version it was read from
   (`Weakness_Catalog/@Version`, `@Date`), never the name, which changes
   (`Previous_Entry_Name`, L293).
2. **`Mapping_Notes/Usage` as an import gate** (R-010, R-018). Every weakness,
   category and view must carry `Mapping_Notes` (L106, L131, L154; minOccurs 1)
   with a `Usage` of
   Allowed, Allowed-with-Review, Discouraged or Prohibited (L420, L1287). A
   tmodel Weakness that cites a Discouraged or Prohibited id is a **finding to
   review**, not a mapping: Discouraged means "this CWE ID should not be used to
   map to real-world vulnerabilities" (L1294). Allowed-with-Review creates a
   Review task (R-018). `Mapping_Notes/Suggestions` (L424, L566) gives the
   alternative ids to offer the reviewer.
3. **Relations as typed edges with properties** (ADR-0004). A `Related_Weakness`
   requires `Nature`, `CWE_ID` and `View_ID` (L545–547) and may carry
   `Chain_ID` and `Ordinal` (L548–549). Import each as one edge with all five as
   properties. Dropping `View_ID` would merge hierarchies that CWE keeps
   separate (Research Concepts view 1000, Simplified Mapping view 1003,
   Hardware Design 1194).
4. **The XSD as the import validator** (DEC-002). The 4.20 catalog is checked
   against the pinned XSD on every import (`schema/README.md` has the
   command). The schema is closed (no `xs:any` outside XHTML text), so a new
   element in a future catalog fails validation loudly instead of being
   dropped silently.
5. **`Modification_Importance = Critical` as a re-review trigger** (R-018,
   R-021). The schema says changes that alter meaning "should be marked with an
   importance of critical to bring it to the attention of anyone previously
   dependent on the weakness" (L293). On a catalog upgrade, every tmodel
   Review attached to a Weakness whose CWE entry gained a Critical modification
   is flagged stale.

## What we adapt, and how

1. **`ChildOf` is specialization, not `part_of`** (DEC-001a, ADR-0010). "A ChildOf nature
   denotes a related weakness at a higher level of abstraction" (L973): it
   means "is a kind of". Neither ARCH-0001's edge list nor the core accepted in
   ADR-0010 has a Weakness-to-Weakness edge, so either propose one (`specializes`)
   in a follow-up ADR or carry it as an imported, view-scoped edge.
   Category and view membership (`Has_Member` / `Member_Of`, L556–563, scoped by
   `View_ID`) is the CWE relation closest to `part_of`.
2. **Chains are ordered weaknesses, not attack paths** (ARCH-0001 §3
   AttackPath). A Chain is "a set of weaknesses that must be reachable
   consecutively in order to produce an exploitable vulnerability" and a
   Composite "a set of weaknesses that must all be present simultaneously in
   order to produce an exploitable vulnerability" (L1050). Import `StartsWith` /
   `CanPrecede` / `CanFollow` (with `Chain_ID`) as ordering edges between
   Weakness nodes and `Requires` / `RequiredBy` as an AND group. Attack patterns
   (tmodel `AttackPattern`) come from CAPEC through `Related_Attack_Pattern/@CAPEC_ID`
   (L533), not from CWE; the CWE↔CAPEC link is a reviewed Assertion (ADR-0010 core).
3. **Deprecation → `supersedes` is derived, and reviewed** (ARCH-0001 §3
   `supersedes`). A deprecated entry keeps its id with `Status="Deprecated"`
   and `Usage` Prohibited, and names its successor in prose. CWE-1187: "This
   entry has been deprecated because it was a duplicate of CWE-908." Of 64
   deprecated entries in 4.20, only 2 carry `Mapping_Notes/Suggestions` with a
   machine-readable id. The importer parses the Description for `CWE-\d+`,
   emits a `supersedes` edge marked inferred, and queues it for human Review.
   CVE's `replacedBy` (record `cve-json-5`) needs no such step.
4. **Fit-graded mapping for local weaknesses** (DEC-001, DEC-002). CWE cannot be
   extended (see Reject 2), so a weakness tmodel finds that CWE lacks lives in
   a tmodel namespace with its own id, linked to the nearest CWE entry by a
   mapping edge. Reuse CWE's own fit vocabulary from `Taxonomy_Mapping`
   (L589, L1071–1082): Exact, CWE More Abstract, CWE More Specific, Imprecise,
   Perspective.
5. **Provenance is per entry; tmodel needs it per edge** (ARCH-0001 PROPOSAL
   v0.2.0, reified Assertion). `Content_History` records who submitted and
   modified the whole entry (L291–357); it does not say who asserted any one
   relation or mitigation. Imported edges therefore get one provenance:
   asserted by MITRE CWE, catalog version N, never an individual.
6. **Mitigations are generic templates** (DEC-009). `Potential_Mitigations`
   gives Phase, Strategy, Effectiveness and Description per weakness (L481–500).
   Import them as generic Mitigation nodes; per-product mitigation *state*
   (R-021) is tmodel's own and has no CWE source. `Mitigation_ID` (MIT-n) is
   "used by the internal CWE team" (L484) and optional, so it is a dedupe hint,
   not a key.
7. **Observed examples are a sample, not an index** (R-010). `Observed_Examples`
   (L465–480) lists CVE ids that illustrate a weakness. Import them as
   Vulnerability → Weakness links marked *example*; the forward direction for a
   given CVE comes from the CVE record's `problemTypes`. `instance_of` is
   ARCH-0001 §3's working name: the accepted core (ADR-0010) has no
   Vulnerability-to-Weakness edge yet, so until one is added the link is an
   Assertion (a proposed `Vulnerability.instance_of` is in tmodel#130).

## What we reject, and why

1. **The XSD as tmodel's own schema** (DEC-002, ADR-0004). It is
   catalog-shaped (one root, everything nested in entries) and closed. tmodel's
   canonical form is YAML/JSON objects plus link records; CWE stays an
   import.
2. **Extending CWE in place.** There is no extension point: the only `xs:any`
   admits XHTML inside structured text (L1332, L1340), and the list of external
   taxonomies a weakness may map to is a closed enumeration
   (`TaxonomyNameEnumeration`, L1083). A local weakness inside the CWE
   namespace would collide with MITRE's future ids.
3. **Categories as mapping targets.** "A Category is used primarily as an
   organizational mechanism for CWE and should not be mapped to by external
   sources." (L122). A tmodel Weakness never maps to a category; categories
   import as grouping only.
4. **CWE's likelihood and consequences as a RiskScore** (DEC-003, ARCH-0001 §6).
   `Likelihood_Of_Exploit` (L95) and `Common_Consequences` (L96) are generic
   and qualitative; tmodel's risk is per asset and environment. They may
   seed a default, never stand in for the score.

## Mapping to our decisions

The edge rows use ARCH-0001 §3's working names. The accepted LinkML schema
(ADR-0010) has no `part_of`, `instance_of` or `supersedes` slot, so those rows
are proposals against it, not mappings onto it.

| tmodel item | CWE construct | verdict |
|---|---|---|
| ARCH-0001 §3 Weakness | `Weakness` (Pillar/Class/Base/Variant/Compound; Simple/Chain/Composite) | adopt as external key |
| §3 Mitigation | `Potential_Mitigations/Mitigation` | adapt: generic template |
| §3 AttackPath / ThreatChain | `Structure="Chain"` + `StartsWith`/`CanPrecede` | adapt: weakness ordering only |
| AttackPattern (ADR-0010) | `Related_Attack_Pattern/@CAPEC_ID` | link out to CAPEC as a reviewed Assertion |
| §3 Review | `Status`, `Mapping_Notes` (editorial, not a decision record) | no equivalent; tmodel's own |
| edge `part_of` | `Has_Member` / `Member_Of` (view-scoped) | adapt |
| edge `instance_of` | `Observed_Example` (CVE ids) | adapt: example only |
| edge `supersedes` | deprecated entry, successor in prose | adapt: inferred + reviewed |
| (new) specialization | `ChildOf` / `ParentOf` (view-scoped) | not in the accepted core (DEC-001a, ADR-0010); needs a follow-up ADR |
| (new) causal order | `CanPrecede` / `CanFollow` | not in the accepted core (DEC-001a, ADR-0010); needs a follow-up ADR |
| R-010 | `CWE-<int>`, `Mapping_Notes/Usage` | adopt id + gate |
| R-018 | `Allowed-with-Review`, Critical modifications | adopt as review triggers |
| DEC-002 (accepted, ADR-0007) | XML + closed XSD 7.3 | import only, validated; adding it to ADR-0007's import set needs a MAP-NNNN crosswalk and a vector |
| DEC-008 | bulk XML per release (zip ~2 MB; XML ~18 MB) | cached mirror pinned by version |
| ADR-0004 | `Related_Weakness` with Nature/View_ID/Chain_ID/Ordinal | edges with properties |

**DEC-008 (live lookup vs cached mirror).** The pinned source defines a file
that MITRE publishes whole, once per release. A pinned, cached mirror (catalog
version + digest, validated against the XSD) fits that, and lets an old threat
model be re-read against the catalog it was written with. Any MITRE web API is
outside this record and was not checked. A mirror redistributed inside tmodel
must keep MITRE's licence header ("When distributing copies of the CWE Schema,
this license header must be included", L10).

## Open questions

1. **Which view is canonical for hierarchy?** Research Concepts (1000) is the
   most complete graph; Hardware Design (1194) matters for R-022's hardware
   domain. Views 1000, 699 and 1194 (three of the 38 Graph views in 4.20) all
   have `Status="Draft"`. Proposal: import all, store `View_ID` on every edge,
   and let queries choose.
2. **The Primary-ordinal rule is ambiguous as written.** "For each unique triple
   of &lt;Nature, CWE_ID, View_ID&gt;, there should be only one relationship that is
   given a "Primary" ordinal." (L540). Read literally, a triple occurs once per
   entry anyway, so the rule constrains nothing. The likely intent is one
   Primary per (Nature, View_ID) within an entry. 4.20 satisfies that stricter
   reading: no weakness has two Primary relations with the same Nature and
   View. tmodel should check the stricter reading on import.
3. **Mapping guidance is a separate document.** MITRE's root-cause mapping
   guidance (which prefers Base and Variant over Class) is not in the XSD. It
   should become its own library record before tmodel encodes its rules.
4. **Content licence for a redistributed mirror.** The terms of use allow it
   with the header; whether tmodel ships the mirror or fetches it at install
   time is a DEC-008 choice.
5. **MITRE's own data departs from two documented relation rules.** The
   documentation ties `Ordinal` to "the primary ChildOf relationship" and
   `Chain_ID` to "a CanFollow or CanPrecede relationship" (L540), but 4.20 puts
   `Ordinal="Primary"` on 27 PeerOf/CanPrecede relations and `Chain_ID` on the 3
   StartsWith relations of the named chains (`examples/catalog-stats.yaml` I15,
   I16; requirements `cwe#R-0159`, `cwe#R-0161`). An importer that enforced the
   documented rules would reject MITRE's own catalog, so tmodel should keep both
   properties on any nature and report the departures as warnings, not errors.
