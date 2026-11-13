---
schema: "library-normative/v1"
id: iso-sae-21434-2021-normative
record: iso-sae-21434-2021
type: normative
updated: "2026-11-13"
coverage: "Fig 3 object model, Clause 15 TARA and Table 1, all 40 Clause 3.1 terms, the work-product and audit mapping, and Annexes A to H (informative); scope (§6), objectives (§7), inputs (§8) and figures (§9); every provision is in requirements.yaml (§10)."
reviewed_by: ""
---

# ISO/SAE 21434 — distilled normative content

> Compacted so an implementer can build the model without re-reading the source.
> **Our own wording throughout.** ISO/SAE 21434 is a licensed standard; this page paraphrases
> it and cites clause IDs, and quotes none of its text (sponsor decision:
> tmodel#69 sponsor note, hold 1 (2026-10-02); tmodel#154).
> Requirement ids resolve in `requirements.yaml`. **Coverage baseline:** the standard
> tags every provision, so the baseline is marker count, not a verb grep (the 18 untagged
> Prerequisites lists are obligations too; §8 carries them):
> **118 requirements (101 RQ shall / 13 RC should / 4 PM may) + 42 work products.**
> A distillation missing any marker has failed; all 118+42 are catalogued.
> Annexes A to H (all informative) are in §5, with the tables of Annexes E to H and the worked example as data in
> `examples/`; §10 says where every part of the standard is distilled.

## 1. Object model (Figure 3)

Typed edges (a ready candidate object model for ARCH-0001 / #17), read from Figure 3 tail to head
(checked on a page image on 2026-10-02; an earlier
version had the item and function edge reversed and the wrong source for `contains` and
`allocated to`):

- `item` **implements** `function(s)`; `item` **contains** `asset`; `item` **consists of** `component`
- `cybersecurity property` **attribute of** `asset`
- `cybersecurity goal` **protects** `asset`; **associated with** `item`; **associated with**
  `threat scenario`; **realized by** `cybersecurity requirement`
- `cybersecurity requirement` **allocated to** `item`; **allocated to** `component`
- `threat scenario` **compromises** `cybersecurity property`; **realizes** `damage scenario`
- `damage scenario` **affects** `road user`

## 2. TARA pipeline (Clause 15) — the risk method

In clause order, each step a requirement and a work product (the standard lets the modules run in any
order, at whatever lifecycle stage calls them; 15.1, H.1):

| step | clause | requirement(s) | work product |
|---|---|---|---|
| Damage scenarios | 15.3 | RQ-15-01 | WP-15-01 |
| Asset identification | 15.3 | RQ-15-02 | WP-15-02 |
| Threat scenario identification | 15.4 | RQ-15-03 (targeted asset + compromised property + cause) | WP-15-03 |
| Impact rating | 15.5 | RQ-15-04 (categories **S,F,O,P**), RQ-15-05 (**severe/major/moderate/negligible**), RQ-15-06 (safety ← ISO 26262); PM-15-07 (may skip a category; no work product) | WP-15-04 |
| Attack path analysis | 15.6 | RQ-15-08, RQ-15-09 | WP-15-05 |
| Attack feasibility rating | 15.7 | RQ-15-10 (per **Table 1**); RC-15-11 to RC-15-14 (method; no work product) | WP-15-06 |
| Risk value determination | 15.8 | RQ-15-15, RQ-15-16 | WP-15-07 |
| Risk treatment decision | 15.9 | RQ-15-17 | WP-15-08 |

### Table 1 — Attack feasibility ratings
| rating | effort the attack path needs |
|---|---|
| High | low effort |
| Medium | medium effort |
| Low | high effort |
| Very low | very high effort |

**RC-15-11** (should): pick the rating approach from three: (a) attack potential, (b) CVSS or
(c) attack vector. Annex G gives guidance for each (§5.7).

## 3. Terminology (Clause 3.1, all 40 terms)

Our own definitions. Where the standard adapts a term from another standard it gives a source
note, and we say adapted from (or taken from, for the one it uses unchanged).

- **asset** (3.1.2): something that has value or helps create value; compromising one of its cybersecurity properties can result in damage scenarios.
- **cybersecurity property** (3.1.20): an attribute that might deserve protection, for example confidentiality, integrity or availability.
- **damage scenario** (3.1.22): a harmful outcome for a road user that involves a vehicle or one of its functions.
- **threat scenario** (3.1.33): a possible way one or more assets could have their cybersecurity properties compromised, bringing about a damage scenario.
- **attack path** (3.1.4): the deliberate actions that, taken together, carry out a threat scenario; also called an attack.
- **attack feasibility** (3.1.3): how easily the actions of an attack path can be carried out successfully; a property of the path.
- **item** (3.1.25): what delivers a vehicle-level function: one component, or several working together (adapted from ISO 26262-1).
- **component** (3.1.7): a part that can be separated from the rest, both logically and technically.
- **weakness** (3.1.40): anything about a system, a defect or simply a property, that can make it behave in ways no one wants: a missing requirement or specification, an architecture or design flaw (a badly designed security protocol among them), an implementation defect in hardware or software, a flaw in how it is operated (misuse, poor training), or reliance on outdated or deprecated functions such as old cryptographic algorithms (our note: compare CWE).
- **vulnerability** (3.1.38): a weakness that an attack path can exploit (adapted from ISO/IEC 27000; our note: compare CVE).
- **work product** (described in the Introduction; 3.2 lists only its abbreviation, WP): what a cybersecurity activity produces in meeting one or more of the requirements tied to it; Annex A summarizes them. In this audit model it is the evidence an auditor checks.

The other Clause 3.1 terms, in number order:

- **architectural design** (3.1.1): a description of the structure from which the components can be picked out, together with where each ends, how they connect and how they act on one another.
- **attacker** (3.1.5): whoever executes an attack path: one person, a group or an organization.
- **audit** (3.1.6): checking a process to see how well its objectives are being met (adapted from ISO 26262-1).
- **customer** (3.1.8): the party on the receiving end of a product or service, whether a person or an organization (adapted from ISO 9000).
- **cybersecurity** (3.1.9), in full road vehicle cybersecurity: the condition where assets are protected well enough against threat scenarios aimed at a vehicle's items, their functions and their E/E components.
- **cybersecurity assessment** (3.1.10): an evaluation that reaches a verdict on cybersecurity.
- **cybersecurity case** (3.1.11): the evidence-backed, structured argument that the risks are not unreasonable.
- **cybersecurity claim** (3.1.12): something asserted about a risk; it can justify keeping the risk or sharing it.
- **cybersecurity concept** (3.1.13): the item's cybersecurity requirements plus the requirements placed on its operational environment, with information on the controls that go with them.
- **cybersecurity control** (3.1.14): any measure that changes a risk (adapted from ISO 31000).
- **cybersecurity event** (3.1.15): whatever cybersecurity information turns out to bear on a given item or component.
- **cybersecurity goal** (3.1.16): a requirement at concept level, tied to one or more threat scenarios.
- **cybersecurity incident** (3.1.17): something happening in the field where exploitation of a vulnerability may be in play.
- **cybersecurity information** (3.1.18): information about cybersecurity whose relevance has not yet been decided.
- **cybersecurity interface agreement** (3.1.19): the agreement between customer and supplier on the cybersecurity activities they share out.
- **cybersecurity specification** (3.1.21): cybersecurity requirements together with the architectural design that goes with them.
- **distributed cybersecurity activities** (3.1.23): cybersecurity work on an item or component that customer and supplier divide between them.
- **impact** (3.1.24): the estimated size of the harm, physical or otherwise, that a damage scenario would do.
- **operational environment** (3.1.26): where and how the item is actually used, and what it interacts with there; for an item or component, that use can be inside a vehicle function, on the production line, or in workshop service and repair.
- **out-of-context** (3.1.27): developed without a particular item in view, for example a processing unit built to assumed cybersecurity requirements so that different items can use it.
- **penetration testing** (3.1.28): cybersecurity testing that plays the attacker, using realistic attacks to look for ways the cybersecurity goals could be broken.
- **risk** (3.1.29), in full cybersecurity risk: what uncertainty means for road vehicle cybersecurity, measured by two things, attack feasibility and impact.
- **risk management** (3.1.30): the coordinated set of activities through which an organization directs and controls how it handles risk (taken from ISO 31000).
- **road user** (3.1.31): anyone using a road, such as a passenger, a pedestrian, a cyclist, a driver or a vehicle's owner.
- **tailor** (3.1.32, verb): adapting the standard's activities to a situation by skipping one or doing it another way than described.
- **triage** (3.1.34): sorting incoming cybersecurity information by whether it is relevant to a given item or component.
- **trigger** (3.1.35): a criterion that triage applies.
- **validation** (3.1.36): showing, with objective evidence, that the item's cybersecurity goals are the right goals and that the item meets them (adapted from ISO/IEC/IEEE 15288).
- **verification** (3.1.37): proof, through objective evidence, that what was specified has been achieved (adapted from ISO/IEC/IEEE 15288).
- **vulnerability analysis** (3.1.39): finding and evaluating vulnerabilities in a systematic way.

## 4. Requirement / work-product structure → audit automation (tmodel #15)

Work products are the evidence, and each names what it results from. 47 provisions are listed by
name (e.g. `WP-15-05`, attack paths, from RQ-15-08 and RQ-15-09); 56 more sit in the subclauses that
the 10 subclause-level work products result from as a whole (e.g. WP-06-02, the cybersecurity case,
from 6.4.7), and their `verification` field names that work product; 15 yield no work product
(RQ-07-01, RC-07-02, RQ-07-03, RQ-08-08, RC-10-06, RQ-10-13, RQ-12-03, RQ-13-02, RQ-13-03, RQ-14-02,
PM-15-07 and RC-15-11 to RC-15-14).
Because **conformance is itself audited** (§6.4.8 cybersecurity assessment; §5.4.7 audit),
this structure is the template for automating the mechanical parts of an audit:

- in tmodel's accepted model (ADR-0012, ADR-0013): a `Requirement` is implemented by an
  `SdlPractice`, which produces `Evidence` (`evidence_nature: work_product`), tied to a product
  version by `about_version`; nothing yet says which work product an `Evidence` item is
  (`design-notes.md` A6, Q6);
- **audit = query**: for a scope, enumerate applicable requirements → required work products →
  check evidence exists and is human-reviewed-adequate → emit a coverage/gap report;
- **tailoring** (Clause 6) is recorded with rationale and is itself auditable;
- the KG automates coverage/traceability/gaps; a **human judges adequacy**.

`requirements.yaml` (118 provisions, plus 42 `required_deliverables` with `from_requirements` or
`from_subclauses`) is the seed dataset.

## 5. Annexes A to H (all informative)

No annex adds a requirement: each one illustrates or supports provisions in the body. The
tables and the worked example are carried as data in `examples/`, with test vectors and a script
that recomputes them (`examples/README.md`).

### 5.1 Annex A: activities and work products (Table A.1)

A planning aid that lists, subclause by subclause, the work products each cybersecurity activity
yields, so an organization can check coverage and estimate effort. Because the cybersecurity plan
defines the concept and development activities, their work products fall within the
cybersecurity assessment; the Clause 15 work products are documented within the work
products of other clauses (A.1, 15.1). Four subclauses yield none: 7.4.1 (supplier capability), 7.4.2 (request for quotation),
13.4 (updates) and 14.4 (decommissioning). `requirements.yaml` holds all 42 work products with
the provisions or subclauses they come from.

### 5.2 Annex B: cybersecurity culture (Table B.1)

Paired examples, for 5.4.2, of behaviour that signals a weak culture and of its strong
counterpart. A strong culture keeps cybersecurity decisions traceable to the people who made
them; puts cybersecurity and safety ahead of features, cost and schedule; rewards doing
cybersecurity well and penalizes shortcuts; has security staff who model sensible, practical
judgement instead of rigid rules; keeps enough independence in assessment that the people who
run a process cannot sway those who check it; finds and fixes problems from the start (security
by design) and is ready to react fast to field incidents, instead of testing late and reacting
only to incidents or press attention; staffs cybersecurity with enough competent people; seeks
diverse views and protects dissent, where a weak one shows groupthink, review panels picked for a
desired result, and dissenters labelled or fearing repercussions; encourages self-disclosure and
responsible disclosure of vulnerabilities from inside and outside; keeps hunting and fixing
problems after release, in production and across other products; builds continuous improvement
into every process; and follows defined, traceable, controlled processes rather than ad hoc ones.

### 5.3 Annex C: cybersecurity interface agreement template (Figure C.1)

An example layout for the customer-supplier agreement that RQ-07-04 requires. Each row is
one phase and one work product that touches the interface; the columns give the clause it comes
from, the supplier's and the customer's role by RASIC, the agreed confidentiality level, and a
comment for points settled in negotiation. In RASIC, R carries out the activity, A approves it
when done, S helps R, I is kept up to date on progress and decisions, and C advises without doing
the work. The example confidentiality levels run from the creating organization only, through
customer and supplier both and authorized third parties under 5.4.3, to public. Contacts,
milestones, methods and tools can be added to the template. The figure shows concept-phase
rows for the item definition, the TARA, the cybersecurity concept and its verification report,
then product-development rows starting with the cybersecurity specification. Its TARA row
misspells "threat" (a typo in the source).

### 5.4 Annex D: cybersecurity relevance (Figure D.1)

An example screen for RQ-06-02 a), whether a candidate item or component is relevant to
cybersecurity. Anything that is not an E/E item or component drops out at once. Otherwise it is
relevant if any of three questions is answered yes, asked in this order: does it help the vehicle
operate safely (for example motion control, or modules with an ASIL); does it gather or process
data about users (for example driver or passenger data, or location); does it carry out vehicle
functions over networked components (internal links such as CAN, Ethernet, MOST or TCP/IP;
external ones such as a backend server, the cellular network or the OBD-II port; wireless sensors
and actuators such as keyless entry, NFC or tyre pressure monitoring). Three noes make it not
relevant. Experienced safety and cybersecurity experts can also judge relevance together.

### 5.5 Annex E: cybersecurity assurance levels

A CAL sets how much rigour later engineering has to show; it is not a control. It can be set in the
concept phase from inputs expected to stay stable, and is meant to stay fixed while the risk value
keeps changing (Figure E.1), and
it can ride on a cybersecurity goal down to the requirements refined from it. Table E.1 picks one
of four CALs from the worst impact and the attack vector among the threat scenarios concerned
(none for negligible impact, see PM-06-08); combined goals take the highest CAL. A CAL can steer
development and verification methods, vulnerability-finding methods and assessment
independence (Table E.2), the independence of verification, validation and assessment (Table
E.3, levels I1 to I3) and the depth of functional, scanning, fuzz and penetration testing (Table
E.4, parameter sets T1 and T2). In the concept phase requirements inherit their goal's CAL and a
component takes the highest CAL among its requirements unless it is shown to be protected from
the others (E.3.2, extending RQ-09-10); in development, components that cannot be shown isolated
can be built to the highest CAL of their requirements (E.3.3). Data:
`examples/annex-e-cal.yaml`.

### 5.6 Annex F: impact rating

Four example tables, one per impact category, each defining severe, major, moderate and
negligible for 15.5. Safety uses ISO 26262-3's S3 to S0 classes, optionally with controllability
and exposure if justified; financial is judged by whether the road user can recover from the
loss; operational by whether a core, an important or no vehicle function is lost, impaired or
degraded; privacy by how badly the road user is harmed together with how sensitive the
information is and how easily it ties to the person. Damage reaching many road users at once is
left to organization-specific criteria. Data: `examples/annex-f-impact.yaml`.

### 5.7 Annex G: attack feasibility rating

Guidance for the three approaches of RC-15-11, each ending on the four ratings of Table 1, and
each able to weigh whether an attack scales. **Attack potential** (RC-15-12, after ISO/IEC 18045)
scores five factors (elapsed time, specialist expertise, knowledge of the item or component,
window of opportunity, equipment) with the values of Table G.6, sums them, and maps the sum: 0 to
13 high (two bands, 0 to 9 and 10 to 13), 14 to 19 medium, 20 to 24 low, 25 and above very low
(Table G.7). **CVSS** (RC-15-13) uses only the exploitability metrics: the exploitability value is
8.22 times the four metric values, ranging from 0.12 to 3.89, and Table G.8 cuts that range into
four equal steps; the standard notes this does not strictly follow CVSS, its own impact rating
standing in for CVSS impact. **Attack vector** (RC-15-14) rates a path by how remote the attacker
can be: network high, adjacent medium, local low, physical very low (Table G.9). Data:
`examples/annex-g-feasibility.yaml`.

### 5.8 Annex H: a worked TARA for a headlamp system

An illustrative concept-phase run of 9.3, 9.4 and Clause 15 (Figure H.1). The item is a headlamp
system (switch, body control ECU, camera ECU, power switch actuator, lamps) that follows the
driver's switch and dips from high to low beam while an oncoming car is detected; its
environment is a gateway ECU with an OBD-II port and a navigation ECU with Bluetooth and
cellular, both assumed to be firewalled. Assets are the lamp-request and oncoming-car messages
and the body control ECU's firmware. Three damage scenarios are rated: a night-time crash after
the lamp goes off (safety, severe), a car that cannot be driven at night (operational, major) and
automatic high beam failing (operational, moderate). Three threat scenarios are named (spoofing
or tampering with the lamp request, and denial of service of the oncoming-car information), and
attack paths are worked for the spoofing and the denial of service. Five attack paths run through the
navigation ECU (cellular or Bluetooth), the OBD port or a Bluetooth OBD dongle. Feasibility is
rated by attack vector for the spoofing paths (high, medium, low) and by attack potential for the
denial-of-service paths (20 and 24, both low). With the example risk matrix of Table H.8, or the
formula R = 1 + I × F of Table H.10, the risk values are 5 for the safety scenario and 2 for the
operational one, and both are treated by reducing the risk. Seven inconsistencies inside the annex,
and three caveats, are listed in the data file, among them the spoofed lamp request being off in Table H.5 and
Figure H.3 but on in Table H.6. Data: `examples/annex-h-headlamp-tara.yaml`; test vectors:
`examples/expected.yaml`.

### 5.9 Bibliography

39 entries; `record.yaml` `cites` lists them, by record id where the library holds the source
and by title otherwise.

## 6. Scope and applicability (Clause 1; Clause 4, informative)

**Clause 1.** The standard covers managing cybersecurity risk for the E/E systems of road vehicles,
with their components and interfaces, through every phase from concept to decommissioning. It
gives process requirements and a common vocabulary for talking about and handling that risk. It
applies only to the E/E systems of series-production vehicles whose development or modification
started after it was published, and it prescribes no particular technology or solution.

**Clause 4, in brief.** An item is all the electronics and software in a vehicle that together
realize one vehicle-level function, braking for example, and items and components interact with
their operational environment. The scope covers only items and components that
matter for cybersecurity, in series-production vehicles, aftermarket and service parts included and prototypes
not; systems off the vehicle, such as back-end servers, may be taken into account but are outside
the scope. The standard works one item at a time and does not say how functions are divided into
items; for the whole vehicle, one can look at its E/E architecture or at all its items' cybersecurity
cases together, and carrying out the activities on every item and component deals with
unreasonable vehicle-level risk. Risk management runs through every lifecycle phase (Figure 2: a
loop from concept through product development, production, operations and maintenance back to
concept, with a way out to decommissioning or the end of support) and along the supply
chain, where activities can be tailored (Clause 6) and divided between partners (Clause 7). The
Clause 15 methods are modules that other clauses call on. Analysis imagines abstract, malicious
adversaries and the damage they could do; monitoring, remediation and incident response add the
reactive side as conditions change. Defence in depth is suggested: layers of controls, so that
what gets past one layer can be contained by the next.

## 7. Objectives per clause (5.2 to 15.2)

Some provisions judge work against the standard's objectives (RQ-05-17, RQ-06-14, PM-06-29,
RQ-06-30 d)), so each clause's objectives are listed here, in our words.

| clause | objectives |
|---|---|
| 5 | set a policy, plus the organization's rules and processes; give roles their responsibilities and authority; resource cybersecurity and manage how its processes meet related ones; manage cybersecurity risk; foster a lasting cybersecurity culture through competence and awareness management and continuous improvement; support and manage information sharing; keep management systems that sustain cybersecurity; show that tools do not harm cybersecurity; audit the organization |
| 6 | give the project's activities their owners; plan them, tailoring included; build a cybersecurity case; assess, where applicable; decide on releasing the item or component for post-development |
| 7 | settle how customer and supplier interact on shared activities, what each depends on and who is responsible |
| 8 | watch cybersecurity information for events; evaluate events for weaknesses; find which weaknesses are vulnerabilities; manage the vulnerabilities found |
| 9 | define the item, its environment and how they interact, for cybersecurity; specify goals and claims; specify a concept that meets the goals |
| 10 | define the cybersecurity specifications; check them against the higher-level ones; find weaknesses in the component; show that implementation and integration meet the specifications |
| 11 | validate the goals and claims; confirm the item meets its goals; confirm that no unreasonable risk is left |
| 12 | apply the post-development requirements; keep vulnerabilities from being introduced in production |
| 13 | decide and carry out remedies for incidents; keep the item or component secure through updates after production, until support ends |
| 14 | let customers know when support ends; make decommissioning possible with cybersecurity in mind |
| 15 | find the assets, with their cybersecurity properties and damage scenarios; find threat scenarios; give each damage scenario its impact rating; find the attack paths behind threat scenarios; rate how easily those paths can be carried out; set the threat scenarios' risk values; choose how to treat them |

## 8. Inputs per subclause

Each activity subclause opens with its inputs. The **prerequisites** must be available (the
Introduction calls them mandatory inputs, from earlier phases); the **further supporting
information** is optional, informative input. Work products are given by id; other inputs in
our words.

| subclause | prerequisites | further supporting information |
|---|---|---|
| 5.3 | none | evidence of conforming to quality-management standards (for example IATF 16949 with ISO 9001, ISO 10007, Automotive SPICE, the ISO/IEC 330xx family, ISO/IEC/IEEE 15288 and 12207) |
| 6.3 | none | the organizational audit report (6.3.2 cites it as WP-05-03, but that id is the management-systems evidence; the audit report is WP-05-05); the project plan |
| 7.3 | none: the subclause has no inputs | none |
| 8.3 | the rules and processes in WP-05-01 for developing triggers | WP-09-01, WP-09-04, WP-10-01, WP-15-03, earlier WP-08-05 analyses, and information from the field (for example scan reports, repair records, usage data) |
| 8.4 | WP-08-03; WP-10-02 where applicable; configuration information kept under RQ-05-12 | WP-09-01, WP-10-01, earlier WP-08-05 analyses |
| 8.5 | WP-09-01 when an item is analysed, or WP-10-01 when a component is | WP-08-04, WP-10-05, earlier WP-08-05 analyses, WP-15-05, WP-10-04 and WP-10-07, lessons from earlier incidents |
| 8.6 | WP-08-05 | none |
| 9.3 | none | what is already known about the item and its environment (for example the in-vehicle E/E and network architecture, networks outside the vehicle, reference models, documents from earlier developments) |
| 9.4 | WP-09-01 | WP-08-03 |
| 9.5 | WP-09-01, WP-09-03, WP-09-04 | WP-09-02 |
| 10.3 | WP-10-01 from the higher levels of architectural abstraction, which can be cut down to what the component needs (its allocated requirements, its external interfaces, assumptions about its environment); at the top level, WP-09-06 and WP-09-01 take its place | WP-09-01, WP-09-06, the existing architectural design, controls already in place, known weaknesses and vulnerabilities of reused components |
| 11.3 | WP-09-01, WP-09-03, and WP-09-04 where applicable | WP-09-06, the product-development work products (10.5) |
| 12.3 | WP-06-04, WP-10-02 | none |
| 13.3 | none | cybersecurity information about the vulnerability behind the incident; WP-08-05 |
| 13.4 | WP-06-04 | WP-13-01; the parts of WP-10-02 that concern the update |
| 14.3 | none: the subclause has no inputs | none |
| 14.4 | WP-10-02 | none |
| 15.3 | WP-09-01 | WP-10-01 |
| 15.4 | WP-09-01 | WP-10-01, WP-15-01, WP-15-02 |
| 15.5 | WP-15-01 | WP-09-01, WP-15-02 |
| 15.6 | WP-09-01 for an item or WP-10-01 for a component, and WP-15-03 | WP-08-04, WP-10-05, the architectural design, attack paths found earlier (WP-15-05), WP-08-05 |
| 15.7 | WP-15-05 | the architectural design, WP-08-05 |
| 15.8 | WP-15-03, WP-15-04, WP-15-06 | none |
| 15.9 | WP-09-01, WP-15-03, WP-15-07 | WP-10-01, earlier treatment decisions for this or similar items or components, WP-15-04, WP-15-05, WP-15-06 |

## 9. Figures

| figure | where | what it shows | carried |
|---|---|---|---|
| 1 | Introduction | how the document's clauses are grouped | no: the clause list in `summary.md` and the map in §10 give the same structure |
| 2 | Clause 4 | the risk-management loop over the lifecycle | described in §6; the `item-release` machine in `state-machine.yaml` follows it |
| 3 | Clause 4 | item, function, component and related terms | §1, all 13 edges |
| 4 | 5.4.1 | cybersecurity governance | no: it pictures 5.4.1, whose provisions are in `requirements.yaml` |
| 5 | 6.1 | fitting off-the-shelf and out-of-context components into an item | no: it illustrates 6.4.5 and 6.4.6, whose provisions are in `requirements.yaml` |
| 6 | 6.4.4 | examples of reuse analysis | no: it illustrates 6.4.4 |
| 7 | 6.4.8 | how the cybersecurity assessment relates to other activities | no: it illustrates 6.4.8; the `item-release` machine models the gate |
| 8 | 7.1 | customer and supplier arrangements along the supply chain | no: it illustrates Clause 7 |
| 9 | 10.1 | product development activities on a V-model, as an example | no: it illustrates Clause 10 |
| C.1, D.1, E.1, H.1 to H.3 | Annexes | | §5, with data in `examples/` |

## 10. Where each part of the standard is distilled

| part of ISO/SAE 21434 | where |
|---|---|
| Introduction (how provisions, work products and inputs are tagged and read) | §8 (inputs), §3 (work product); the tags are counted in the `requirements.yaml` header |
| Clause 1 (scope) | §6 |
| Clause 2 (normative references) | `record.yaml` `cites` |
| Clause 3.1 (40 terms) | §3 |
| Clause 3.2 (12 abbreviations, CAL to WP) | not listed; each is spelled out where it is used |
| Clause 4 (general considerations, informative; no provisions) | §6, with Figure 3 in §1 |
| objectives of Clauses 5 to 15 | §7 |
| inputs of every activity subclause | §8 |
| Figures 1 to 9 | §9 |
| NOTEs in Clauses 5 to 15 and the notes to entry in 3.1 (informative) | not carried as text; cited where an artifact relies on one (for example 8.4.2 NOTE 2 and 8.6.2 NOTE 3 in `state-machine.yaml`, RQ-15-04 NOTE 2 and 15.4.2 NOTE 3 in `design-notes.md`) |
| EXAMPLE notes in Clauses 3 to 15 (informative) | not carried; `examples/README.md` says why |
| Clauses 5 to 15, every provision (118 tags: 101 RQ, 13 RC, 4 PM) | `requirements.yaml`, one entry each, with paraphrase, designator, normativity, verb, actor and locator; `requirements.md` is its generated view |
| work products (42 [WP] tags) | `requirements.yaml` `required_deliverables` |
| Figure 3 (object model) | §1 |
| Clause 15 pipeline and Table 1 | §2 |
| Clause 8 and the release gate of 6.4.7 to 6.4.9, as lifecycles | `state-machine.yaml` |
| Annexes A to H | §5, with data and test vectors in `examples/` |
| how the standard bears on tmodel's decisions | `design-notes.md` |
