---
schema: "library-doc/v1"
id: iso-sae-21434-2021-design-notes
record: iso-sae-21434-2021
type: design-notes
updated: "2026-11-13"
reviewed_by: ""
---

# ISO/SAE 21434:2021: design notes for tmodel

Basis: the purchased copy (sha256 `73f99007…cdf4`), all clauses and Annexes A to H, read for
tmodel#154. Our own wording throughout (licensed standard; sponsor decision: tmodel#69 sponsor
note, hold 1 (2026-10-02)). tmodel's decisions are as ARCH-0001 §8 records them on tmodel `main` at
`b0604a4` (read 2026-11-13): accepted DEC-001a (ADR-0010, amended by ADR-0011 and ADR-0012), DEC-001b
in part (ADR-0013: `SdlPractice`, `Evidence`, `RequirementSource`), DEC-002 (ADR-0007), DEC-003
(ADR-0006), DEC-004 (ADR-0008), DEC-005 (ADR-0002), DEC-006 and DEC-010 (ADR-0003, ADR-0009), DEC-007
(ADR-0001) and DEC-011 (ADR-0004); open: the rest of DEC-001b, DEC-008 and DEC-009.
`project/DECISIONS-0001.md` lags behind ARCH-0001 on DEC-001a and DEC-001b. tmodel RPT-0007 §5 and §6 hold an earlier mapping
of this standard onto the object model and the risk metric.

## Adopt

- **A1. The TARA chain is the core attack-path model (DEC-001a; ADR-0010, ADR-0011).** Figure 3 and
  Clause 15 run asset (with its cybersecurity properties), damage scenario, threat scenario,
  attack path, attack feasibility, risk value and treatment. tmodel's core has each link up to the
  risk value: `Asset.security_properties`, `DamageScenario.damages_asset` and `compromised_property`,
  `ThreatInstance` realizing a damage, `AttackPath.attack_feasibility`, and `RiskScore`. Two of those
  links hold one value where the standard allows several: one threat scenario may cause several
  damage scenarios (15.4.2 NOTE 3), but `ThreatInstance.realizes_damage` names one, and an attack path
  can realize several threat scenarios (RQ-15-09), but `AttackPath.realizes_threat` names one.
  Treatment has no link (D2). Annex H runs
  the whole chain on one item, so `examples/annex-h-headlamp-tara.yaml` is a ready test model for it.
- **A2. Impact is a four-by-four vector (DEC-003; ADR-0006).** RQ-15-04 and RQ-15-05 give four
  categories with four levels each; this is tmodel's `ImpactVector` with the `ImpactSeverity` values
  severe, major, moderate and negligible. Annex F's criteria are the guidance a reviewer sees when
  rating impact (R-019: a person sets the real impact); safety follows ISO 26262-3's S classes. The four categories are a
  minimum: the standard allows more (RQ-15-04 NOTE 2), and 15.1 lets an organization use its own
  scales for impact, feasibility and risk if it maps them onto the standard's.
- **A3. Feasibility is the Table 1 scale (DEC-003; ADR-0006).** RQ-15-10's four ratings are the
  `FeasibilityLevel` values high, medium, low and very low, human-rated at the MVP.
- **A4. A risk value from 1 to 5, per threat scenario and impact category (DEC-003; ADR-0006).**
  RQ-15-16 fixes the range, with 1 the least risk, and RQ-15-15 derives the value from impact and
  feasibility; the matrix itself is left to the organization, and Table H.8 is the annex's example.
  ADR-0006's derived risk (one value from 1 to 5 per threat scenario and impact category, folded over
  attack paths by the worst path) matches how Table H.9 works: each value carries its category label,
  and the aggregated feasibility is the worst path's. The 59 test vectors in `examples/expected.yaml`
  are fixtures for tmodel's risk calculation (tmodel#63; the open engine PR tmodel#229 uses Table H.8).
- **A5. Findings move through Clause 8's lifecycle (DEC-009 and DEC-008, both open).** The
  `security-finding` machine in `state-machine.yaml` gives a `Weakness` or `Vulnerability` a status
  path: event, weakness, vulnerability or not (with a recorded reason), then managed by a 15.9
  treatment or a remediation, with incident response when the treatment calls for it; incident
  response can also start without a TARA (8.6.2 NOTE 3). This is input
  for DEC-009's mitigation lifecycle and R-021's mitigation tracking; DEC-008's CWE and NVD feeds
  enter it as cybersecurity information, where triage triggers decide what becomes an event.
- **A6. Provisions are Requirements and work products are their evidence (ADR-0012; ADR-0013, which
  accepted part of DEC-001b).** The 118 provisions map onto the core `Requirement`. The 42 work
  products become `Evidence` items (`evidence_nature: work_product`, mostly `evidence_kind: document`).
  tmodel has no slot saying which work product an item is, and `Evidence` reaches a `Requirement` only
  through an `SdlPractice` (`implements`, `produces`), so the audit query (`normative.md` §4; tmodel
  #15) needs one more link (Q6). tmodel's RPT-0017 converts 42 of the 49 provisions of Clauses 8, 9,
  10 and 15 on `main` (`research/0017-requirements-extraction/iso-sae-21434-2021.yaml`); tmodel#239,
  still open, adds back the other seven. `Requirement.conformance_status`, where conformance would be
  recorded, is still open under DEC-001b.

## Adapt

- **D1. Annex G's three methods, under ADR-0006.** ADR-0006 keeps the Table 1 rating human at the MVP,
  names Table 1 (not CVSS exploitability) as the method, and makes Common Criteria attack potential
  display-only (R-013).
  - *Attack potential* (G.2) is the ISO/IEC 18045 points scheme behind Common Criteria, so it is
    shown beside the rating, never used to set it; the Table G.6 and G.7 data let the app show the
    points a reviewer chose.
  - *Attack vector* (G.4) can seed a proposed rating from where a path enters (network, adjacent,
    local, physical); the annex itself calls this approach suitable in the concept phase (H.2.6,
    NOTE 1). In tmodel it is a suggestion that stays unreviewed until a person accepts it (R-018).
  - *CVSS* (G.3) does not set the rating. Only CVSS v3.x has the exploitability formula the annex
    uses; CVSS v4.0 has none (tmodel RPT-0007 §3), so this route cannot follow CVSS forward.
  - Annex H shows how far the methods can diverge: AP-4 enters through the cellular interface,
    which Table G.9 rates high as a network vector, yet it scores 20, low, by attack potential
    (Table H.7). That is a reason to keep the rating human and to record which method informed it.
- **D2. 15.9 treatment is not `MitigationStatus` (DEC-009).** RQ-15-17's options are avoid, reduce,
  share and retain; tmodel's `MitigationStatus` is planned, in progress, complete, accepted risk and
  not applicable. Retaining maps to accepted risk, and reducing to a mitigation's progress, but
  avoiding (dropping the function) and sharing (for example by contract or insurance) have no value.
  The standard also ties the options to outputs: reducing calls for cybersecurity goals (RQ-09-05),
  and sharing, or retaining because of assumptions, calls for cybersecurity claims (RQ-09-06).
- **D3. A CAL has no home yet.** Annex E's CAL can be set in the concept phase, is meant to stay
  fixed, and is inherited by requirements; it scales rigour (test depth, independence), not risk. It could be a `Requirement`
  attribute (ADR-0012) or part of the governed layer's gates and checkpoints (DEC-001b).
- **D4. Goals, claims and road users.** Figure 3's cybersecurity goal is a concept-level requirement
  tied to threat scenarios (3.1.16), so it fits `Requirement` linked to threats, though `Requirement`
  has no level slot and a new requirement kind would amend the core `RequirementKind` (ADR-0012). A
  cybersecurity claim is an assertion about a risk, which can justify sharing or retaining it
  (3.1.12), so it fits an `Assertion` about a `RiskScore`. A road user has no tmodel object: tmodel
  rates S, F, O and P from the end-beneficiary's side, who is the road user (`ImpactVector`; RPT-0007
  §6.2 item 15), while `RiskScore.for_stakeholder` names an asset owner, a different party, of whom
  ADR-0006 allows one at the MVP. RPT-0007 §5 found no tmodel object for road user, goal, claim or
  CAL.
- **D5. A relevance screen outside vehicles.** Annex D's screen asks about E/E parts and vehicle
  safety, so it fits automotive items only. ADR-0002's products span at least two domains; a
  domain-neutral version (does it affect physical safety, handle user data, run over a network?)
  could decide whether a product enters the model.
- **D6. Lifecycle phases and the release gate.** The standard's phases (concept; product development,
  which includes validation (Table A.1); production; operations and maintenance; end of
  support and decommissioning; Clauses 9 to 14) map onto tmodel's finer `LifecyclePhaseCode` list. Release for post-development (6.4.9; the
  `item-release` machine in `state-machine.yaml`) is a gate, which belongs to the governed layer
  (DEC-001b).
- **D7. The interface agreement.** Annex C's RASIC roles per work product attach `Party` (core) roles
  to `Evidence` and `Requirement`, and its confidentiality levels are a sharing attribute. This is
  governed-layer material (DEC-001b) and outside the MVP (ADR-0002).

## Reject

- **X1. One number for risk.** A single score, or a CVSS base score, as the risk (ADR-0006's scope
  guard). The standard keeps feasibility and impact apart and replaces CVSS impact with its own
  (G.3 NOTE).
- **X2. Folding the four impact categories into one** for the derived value (ADR-0006). Table H.9
  keeps the category with each value.
- **X3. Annex B as model content.** Culture is organizational practice outside the MVP (ADR-0002);
  a security program (DEC-001b) could cite it, nothing more.
- **X4. Treating the Table H.10 formula as the same method as the matrix.** The two agree on the
  annex's two cases but differ in 4 of 16 cells when the formula is left unrounded. Its fractional
  values are allowed (RQ-15-16 sets only the range 1 to 5, and its EXAMPLE names both matrices and
  formulas), so choosing between them is the organization's call; tmodel's derived risk follows the
  matrix (Q1).

## Defects in the source

- **Annex H** has seven inconsistencies, listed under `source_inconsistencies` in
  `examples/annex-h-headlamp-tara.yaml`. The one that matters most is the lamp request: off in
  Table H.5 and Figure H.3, on in Table H.6. tmodel's fixtures should follow off, as RPT-0007 §4.4
  advised.
- **Figure C.1** misspells "threat" in its TARA row.
- **6.3.2** lists the organizational cybersecurity audit report as WP-05-03, but WP-05-03 is the
  evidence of the management systems; the audit report is WP-05-05.
- **Table G.7**'s high rating spans two value bands (0 to 9 and 10 to 13), the two lowest levels of
  ISO/IEC 18045. The mapping is right, but the two rows are easy to misread as two ratings.
- **G.3** gives the privileges-required range as 0.27 to 0.85 without CVSS's scope-changed values
  (0.68 and 0.5); those fall inside the range, so the stated range of results still holds.

## Open questions

- **Q1.** Is Table H.8 tmodel's default risk matrix, or does each product's owner supply one
  (the standard leaves the method to the organization: H.2.7, and the EXAMPLE under RQ-15-16)?
  ADR-0006 says the derived risk follows ISO 21434. tmodel#229 implements Table H.8 but makes the
  caller name it, so there is no default yet; and tmodel's schema still stores `RiskScore.risk` as a
  string "until a DEC-003 ADR", although ADR-0006 has accepted DEC-003.
- **Q2.** Where does a CAL live, if anywhere: on `Requirement` (ADR-0012) or in the governed layer
  (DEC-001b)?
- **Q3.** How does tmodel record avoiding or sharing a risk, which `MitigationStatus` cannot
  express (DEC-009)?
- **Q4.** Do cybersecurity goals and claims become their own classes (DEC-001b) or requirement kinds
  (an amendment to the core `RequirementKind`, ADR-0012), or stay `Requirement` and `Assertion`?
- **Q5.** Should the app propose attack-vector-based feasibility ratings (D1), shown as unreviewed
  until a person accepts them?
- **Q6.** How does an audit query tell which work product an `Evidence` item is, and tie it to the
  provisions it evidences, when `EvidenceKind` is a closed list of forms and `Evidence` reaches a
  `Requirement` only through an `SdlPractice` (A6)?
