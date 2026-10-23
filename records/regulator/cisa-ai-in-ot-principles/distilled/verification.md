---
schema: "library-distilled/v1"
id: cisa-ai-in-ot-principles-verification
record: cisa-ai-in-ot-principles
type: verification
updated: "2026-10-22"
---

# Verification — cisa-ai-in-ot-principles

FX-1 passes 2 (verify) and 3 (cross-check), run 2026-10-21/22 by independent subagents at maximum
effort that did not extract: one verifier for this record, and one reviewer for the threat
mapping and the tmodel-decision claims (shared with `etsi-en-304-223`). The account usage limit
interrupted them twice; they resumed from their saved transcripts. Every finding was applied by
the main session, and the checks were rerun after the fixes. The fixes renumbered entries (123 →
136) and threats (24 → 32); none of these ids had been published.

## The capture

All text comes from `.cache/cisa-ai-in-ot-principles.capture.txt` (gitignored), built from
PyMuPDF text blocks because sorted-line text interleaves table columns. Rules: page header and
footer dropped; footnote bodies moved to the end; superscript footnote markers removed from
inside text (including the one inline marker, footnote 11 on p. 24) — three markers PyMuPDF
emits as their own blocks (fn 2 and 3 on p. 5, fn 6 on p. 14) stay as one-character lines and
touch no extracted text; bullet glyphs and the "o" sub-bullet glyph dropped; line breaks joined
with one space, except a hyphen that joins a compound across a break ("AI-driven",
"non-production"), and a suspended hyphen before "and"/"or" keeps its space ("machine- and");
whitespace collapsed; quotes and dashes kept as printed.

## Pass 1 self-checks (extractor, 2026-10-21)

The source PDF sha256 equals `content.sha256`; every text found verbatim in the capture with no
overlapping spans (build script); `normative.md`, `threats.yaml` and the example fixtures cut from
the capture by block id or checked verbatim; ATLAS ids checked against ATLAS-2026.09.yaml from
atlas.mitre.org and NIST ids against the E2025 index.

## Pass 2 — verify

**Method.** The verifier rebuilt the capture (byte-identical) and compared it with four
independent renderings (PyMuPDF `text`, `sort=True`, `words`, `dict`; pypdf): word multisets per
page are identical on all 25 pages apart from footnote markers and the "o" glyphs, so the capture
lost, added or altered nothing; the 7 hyphen joins are real compounds. It then checked every
entry exactly against its own rendering and whitespace-free against the others, recounted every
form, printed every stretch of source outside an extracted text and read all of it, rebuilt
Tables 1 and 2 from the ruling lines, and used font colour and indentation to recover the list
structure.

**Results (on the 123 pass-1 entries).**

| check | result |
|---|---|
| `bin/bcp14-count` | 0 on three renderings and the capture |
| forms, source / extracted | should 40/40 · must 5/4 · may 37/9 · can 53/17 · encourage* 2/2 · recommend* 9/4 · essential 4/4 · critical 10/7 · vital 3/2 · crucial 2/1 · necessary 2/1, all equal to the header; itemised exclusions identical to the verifier's own list |
| verbatim / order / overlap | 123/123 exact and unique; strictly in source order; 0 overlaps |
| locator page, section | 123/123 |
| Table 1 / Table 2 cells | 15/15 and 30/30 match the PDF's rows and columns |
| examples, threats | all strings verbatim; `addressed_by` equal to the derived set |
| published `maps_to` | 14/14 name a framework the source names at that statement |
| stated `source_text` | 19 right, 10 wrong (fixed, below) |

**Defects found and fixed.**

| # | defect | fix |
|---|---|---|
| 1 | 10 threat mappings on old R-0008 and R-0010 marked `stated` with words that are in Table 2, not in the entry's own text (one was a splice of three row labels) | now `inferred`, rationale names the Table 2 row and page |
| 2 | 4 described risks missing from `threats.yaml` (Forward and Reverse Compatibility, §2.4; the three §3.4 challenges) | added; 4 more described risks the verifier listed also added (overreliance on automation §1.3, built-in AI needing internet connectivity §2.3, vendors training on operational data §2.3, new failure states §4.2); ids renumbered into source order; 32 threats |
| 3 | `reconciliation` claimed every imperative was extracted unless navigation; three are not (two in the §2.1 example, the §2.3 "expect …" forecast) | claim amended and the three named |
| 4 | imperative count 53 should be 57 (four lower-case imperatives missed) | counting rule fixed; 60 after the fixes below (57 + the three sourcing options now split out) |
| 5 | summary said "twelve subsections"; there are thirteen | fixed |
| 6 | `normative.md` and the `cites` comment claimed all bibliography is held in `cites` | reworded: `cites` is a selection |
| 7 | state-machine `not_applicable` reason said no states are named; the source names several | reason rewritten (states and triggers named, no transitions or guards); conclusion unchanged |
| 8 | schema reason claimed CISA's 2025 SBOM Minimum Elements is held; it is not | reworded, held SBOM records named; the three log-content items acknowledged |
| 9 | §4.1: points 4–7 of the "Consider the following points" list had no parent | parent added to all eleven entries under those points |
| 10 | §3.2 lead-in "These processes include:" in no entry | appended to its sentence's entry (contiguous) |
| 11 | three lists merged lead-in and items, against the record's own rule | split: Introduction lead-in added as an entry; sourcing options and the two OT data types are now items |
| 12 | the anomaly-detection item dropped its middle sentence | sentence kept (contiguous) |
| 13 | six "may (…)" list items typed `recommendation` | `permission` |
| 14 | `normative.md` flattened six sub-bullets | indented to their depth |
| 15 | actors: the six monitoring-example items, the cloud-contract clause and the vendor-transparency lead-in | corrected |
| 16 | `testable_reason` missing on the four lifecycle stages; two lead-ins had a placeholder reason | reasons written |
| 17 | seven candidate dropped statements (scope focus, error-checking, Table 2 "security measures … still apply", "requires continuous evaluation of risks", low-fidelity testing, virtualized controllers, the Conclusion's "require careful management") | all seven extracted (statement, scope or consideration) |
| 18 | header note omitted Secure by Design and Secure by Demand from the published frameworks; design-notes left Data Quality out of the adversarial rows; examples README ids | fixed; Secure by Demand linked to `cisa-secure-by-demand-ot-2025` |

**Checked and found correct** (things a reader might doubt): R-texts that run across a page
break have no footnote spliced in; the Table 2 AI Dependency row, which PyMuPDF merges into one
block, is split correctly; a sentence that starts in lower case is a contiguous clause of a
"(Note: …)" sentence, not a splice; the §3.2 ATLAS sentence ends with a comma in the source; the
Principle 4 title really differs between pages 2/18 and 3/21; both example fixtures' derived
checks are labelled as ours.

## Pass 3 — cross-check

Every id cited anywhere in the record resolves; every count quoted in `README.md`, `summary.md`,
`record.yaml`, `normative.md` and `design-notes.md` matches the files after the fixes; the
generated design-notes tables recompute exactly; the monitoring fixture's ids point at the right
entries; `addressed_by` equals the derived set. Schema, messages, protocol and state machine are
not applicable (reasons in `record.yaml`), so the cross-check is between requirements, normative
text, threats, examples and design notes.

## Threat-mapping and design-notes review

**Method.** An independent reviewer read every `provenance: ours` mapping in both records against
the entry text, the NIST AI 100-2 E2025 definitions (`.cache/nist-ai-100-2e2025.txt`) and the
ATLAS 2026.09 technique descriptions, using ATLAS's own mitigation relations (`AML.M*`) as a
cross-check on fit; recomputed every design-notes table; and checked every claim about tmodel
(`origin/main` = `e1ae8c3`, tmodel#130 = `f57386c`), the OTM schema (`c88c5a7`) and CWE 4.20.
Across both records: 240 id occurrences (49 distinct: 34 ATLAS, 15 NIST), 0 missing, 0 name
mismatches; 155 mappings read; 0 stated `source_text` outside its entry (the 10 found at pass 1
had already been fixed by the verify pass). Findings: 2 wrong, 21 weak, 11 notes, all applied
except where noted below.

**Applied to this record.**

| finding | change |
|---|---|
| R-0011 (Table 2): NISTAML.04 conflicts with the guidance's own scope (it excludes misuse of AI) | guardrail bypass mapped as a jailbreak (NISTAML.018, AML.T0054); evasion (AML.T0015/T0043/T0041) and AI-software supply chain (AML.T0010.001) added for "AI data, models, and deployment software can be manipulated" |
| named but unmapped: "safety-process bypasses" (R-0001), "AI system failure" (R-0133), "inadvertent data poisoning" and "dependency on synthetic, generated data" (R-0042) | mapped (general / non-adversarial, stated); a threat added for safety-process bypasses |
| R-0041: NISTAML.036 is an indirect-injection technique, not this risk | dropped; stated privacy + conventional (disclosure to the host) |
| R-0109: NISTAML.039 is a data leak, not attribution | NISTAML.015 |
| R-0048, R-0053: "patterns of activity" is property inference; T0057 is LLM-only while OT data trains mostly predictive ML | NISTAML.034 / AML.T0024.000 (and T0024.001) added |
| near-identical statements mapped inconsistently (audit trail vs log-and-monitor; strategy vs controls; two failsafe and three re-validation statements; monitoring tools; control-logic thresholds) | made consistent |
| R-0052, R-0098 labelled non-adversarial but rationale says "whatever the cause"; R-0044 `source_text` named a goal | `general`; wording fixed |
| AML.T0122 set: reuse of standing access is also AML.T0012; vendor connectivity is initial access through the supplier | T0012 added to three; R-0054 → AML.T0010 |
| R-0120 adversarial inputs to LLMs are prompting attacks | direct prompt injection added (inferred) |
| threats.yaml: T-14 (foreign government) is legal, not conventional; T-20 missing AML.T0132; AI Vendor Transparency is a weakness | `general`; T0132 added; moved to W-05 |
| design notes: roles (no role slot), `catalog_ref` single-valued, `software_agent` "direct evidence" overstated, impacts with no S/F/O/P slot beyond reputational damage, phases tmodel has no code for (42 entries), `stored_in`, CWE-1426 GenAI-only | each corrected; open questions split from source notes, four added |

**Not applied, and why.** One class per ATLAS id across records: see the same note in
`etsi-en-304-223/distilled/verification.md`; recorded as open question 7.

**Survived review** (selection): R-0001 drift, R-0029 and R-0106 evasion (ATLAS M0009), R-0042
access abuse, R-0045, R-0047, R-0083, R-0085, R-0101 (M0024), R-0102, R-0108 (M0008), R-0115
(M0035), R-0116, R-0120 stated, and every tmodel, OTM and CWE claim.

## Checks after the fixes

Run 2026-10-22 on the final state of this commit:

| check | result |
|---|---|
| `bin/validate` | 0 errors; no warning names this record |
| `bin/check-pr-extraction origin/main` | "FX-1: every record this PR extracts is complete" |
| `bin/check-artifacts` | 0 parse failures, 0 structural errors; no warning names this record |
| `bin/check-requirements` | 47 / 47 sets valid, 0 failures |
| `bin/check-requirements --invariants` | 47 / 47 valid; no invariant warning names this record |

## Every excluded occurrence of each normative form (after the fixes)

Block ids are `p<page>.b<block>` in the capture. Counts are by inclusion in an extracted text.

### should: source 40 → extracted 40 (0 excluded)


### must: source 5 → extracted 4 (1 excluded)

- p11.b12: …ional safety and security requirements that technology must meet in order for critical infrast…

### may: source 37 → extracted 9 (28 excluded)

- p1.b1: …s marked TLP:CLEAR. Disclosure is not limited. Sources may use TLP:CLEAR when information car…
- p1.b1: …ect to standard copyright rules, TLP:CLEAR information may be distributed without restriction…
- p5.b13: …with physical processes. OT data source: Field devices may generate OT data that can be used …
- p6.b8: …ty control: AI models (primarily predictive ML models) may be used for analyzing data from th…
- p6.b8: …t anomalies and alert operators that corrective action may be required. Level 3: Site-Wide Su…
- p6.b11: …aintenance: AI models (primarily predictive ML models) may be used for analyzing aggregated h…
- p6.b12: …uirements. Support operator decision-making: AI models may also be integrated into local supe…
- p6.b15: …ptimization: AI systems (including AI agents and LLMs) may be used for improving business pro…
- p8.b3: …nment OT Impacts Mitigations AI Model Drift: AI models may become less accurate over time due…
- p8.b6: …y: Understanding an AI model’s decision-making process may be difficult; this makes it challe…
- p8.b10: …T Operator Cognitive Load and Unnecessary Downtime: AI may generate alarm errors that could c…
- p8.b14: …cing a robust audit trail of AI-driven decision-making may be difficult, it may be required f…
- p8.b14: …rail of AI-driven decision-making may be difficult, it may be required for regulatory complia…
- p9.b3: …n be complicated by interoperability challenges, which may arise from differences in OT commu…
- p9.b13: …Challenges in AI-OT System Integration Reliability: AI may not be reliable enough to independ…
- p9.b14: …s for OT environments. Decisions made by AI developers may pose OT safety and reliability ris…
- p10.b14: …pendency Risks and Skill Erosion. Heavy reliance on AI may cause OT personnel to lose manual …
- p10.b15: …I failures or system outages. Skill Gaps. OT personnel may misinterpret AI outputs, leading t…
- p10.b15: …AI outputs, leading to incorrect actions; OT personnel may also lack expertise for managing o…
- p13.b11: …OT devices now come with built-in AI technology, which may require internet connectivity to f…
- p14.b14: …-OT System Integration Some challenges an organization may face when integrating AI into OT s…
- p14.b16: …sory control and data acquisition (SCADA) environments may introduce additional cybersecurity…
- p15.b2: … and Reverse Compatibility. OT system design evolution may be necessary to accommodate the se…
- p15.b3: …nalysis. Latency and Real-Time Constraints. AI systems may not meet the strict timing require…
- p18.b6: …e regulatory audits. Safety Certifications. AI systems may not meet the rigorous safety stand…
- p21.b5: … that control vital public services. Resources Readers may find additional information on AI,…
- footnote: …ion from 15 U.S.C. 9401(3); however, definitions of AI may vary among groups and jurisdiction…
- footnote: …ecurity also uses this definition. Other jurisdictions may use their own definition for AI. S…

### can: source 53 → extracted 23 (30 excluded)

- p3.b3: …. For critical infrastructure owners and operators, AI can potentially be used to increase ef…
- p3.b11: …overs how critical infrastructure owners and operators can help ensure the safety and securit…
- p4.b3: … environment. OT systems control physical systems that can harm people or property, such as s…
- p4.b9: …utions and that the relationships are either linear or can be approximated by linear models. …
- p4.b10: …ions without being explicitly programmed. The ML model can handle complex relationships and n…
- p5.b3: …al language prompt and generate a response that humans can understand. LLMs use patterns in l…
- p5.b3: …ays produce the same response to the same inputs. LLMs can power generative AI applications t…
- p5.b5: …in operations. 2 AI agents are a type of software that can process data, perform decision-mak…
- p5.b5: …s, and autonomous action capabilities. Like LLMs, they can enhance decision-making, automate …
- p5.b13: …T data source: Field devices may generate OT data that can be used for training AI models (pr…
- p6.b16: …havioral analytics and profiling of OT and IT data: AI can be used for analyzing OT data in c…
- p7.b8: …curity Risks: AI data, models, and deployment software can be manipulated to cause incorrect …
- p7.b13: …ough AI Testing and Evaluation Data Quality: AI models can only be as effective as the qualit…
- p7.b13: … data. Collecting high-quality, normalized sensor data can be difficult, especially in distri…
- p7.b13: …operational data creates its own risk as threat actors can use it to create a more targeted e…
- p8.b3: …ial training data. Alterations to production processes can affect model performance. Increase…
- p8.b14: …ements, such as those related to OT safety or privacy, can be challenging due to the evolving…
- p8.b19: … Failsafe Mechanisms AI Dependency: Overreliance on AI can lead to operators missing critical…
- p9.b3: …Integrating AI systems with existing OT infrastructure can be complicated by interoperability…
- p9.b13: …make critical decisions in industrial environments. AI can also hallucinate (i.e., fabricate …
- p10.b13: …te Personnel on AI Integrating AI into OT environments can lead to personnel relying too much…
- p10.b13: …educed human oversight and situational awareness. This can have significant consequences, inc…
- p14.b10: … vendors, critical infrastructure owners and operators can better manage the risks associated…
- p14.b15: …ack surfaces and vulnerabilities that malicious actors can exploit—this is a particularly imp…
- p18.b5: …ents. Auditability. Tracing or explaining AI decisions can be difficult, which can complicate…
- p18.b5: …ing or explaining AI decisions can be difficult, which can complicate regulatory audits. Safe…
- p21.b3: …I models, critical infrastructure owners and operators can achieve a balanced integration of …
- p23.b4: …ble to this guidance. Artificial Intelligence (AI). AI can be defined as: A machine-based sys…
- p23.b5: …AI). AI can be defined as: A machine-based system that can, for a given set of human-defined …
- p24.b2: …ontext of OT security as “freedom from conditions that can cause death, injury, occupational …

### encourage*: source 2 → extracted 2 (0 excluded)


### recommend*: source 9 → extracted 4 (5 excluded)

- p4.b2: …s machine- and human-based inputs to make predictions, recommendations, or decisions influencing real or …
- p6.b12: …rated into local supervisory systems to provide system recommendations that support operator decision-mak…
- p11.b12: …er for critical infrastructure owners and operators to recommend using AI in the OT environment. Us…
- p22.b3: …r otherwise, does not constitute or imply endorsement, recommendation, or favoring by CISA and the autho…
- p23.b5: …ven set of human-defined objectives, make predictions, recommendations, or decisions influencing real or …

### essential: source 4 → extracted 4 (0 excluded)


### critical (not "critical infrastructure"): source 10 → extracted 7 (3 excluded)

- p8.b19: …ency: Overreliance on AI can lead to operators missing critical safety-related information if the …
- p9.b13: …y: AI may not be reliable enough to independently make critical decisions in industrial environmen…
- p19.b5: …nce; oversight also maintains human training, which is critical in an emergency. Increased Trust. …

### vital: source 3 → extracted 2 (1 excluded)

- p21.b3: …ntegration of AI into the OT environments that control vital public services. Resources Readers…

### crucial: source 2 → extracted 1 (1 excluded)

- p13.b11: …Role of OT Vendors in AI Integration OT vendors play a crucial role in advancing AI integration i…

### necessary: source 2 → extracted 1 (1 excluded)

- p15.b2: …verse Compatibility. OT system design evolution may be necessary to accommodate the secure integrat…
