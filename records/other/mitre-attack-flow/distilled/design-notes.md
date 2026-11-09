---
record: mitre-attack-flow
kind: design-notes
title: "mitre-attack-flow — bearing on our design"
date: "2026-11-09"
extracted: "2026-11-09"
reviewed_by: ""
---

## Basis and authority

Pass-1 design extraction from the cached `v4.1.0` repository, read independently
of the other distilled artifacts. Repository release `v4.1.0` and extension
version `2.0.0` are distinct. Locators below use these primary files:

| Key | Cached file | SHA-256 |
|---|---|---|
| L | `docs/language.rst` | `85ae7b7f367b57c935328276a412e5b2f051e4d48f2ab622276359d49615fa49` |
| S | `stix/attack-flow-schema-2.0.0.json` | `fff896f5e1bdc39d9b387c0d3571307037cf9be1059de9cd94d066d1da2997cc` |
| E | `stix/attack-flow-extension-2.0.0.json` | `afdbac65edc9805ea2f3b2b84b4ae4908644e7f4190f28e8e836659d74d87e70` |
| I | `docs/introduction.rst` | `0325405cc98e764ca836e6647df70637cb2e3e7e3cc106d9fd401c20a4f32588` |

`ARCH-0001-threat-model-architecture.md` §§3, 5, 8–9 is the architecture
authority. Core names come from accepted ADR-0010, amended by ADR-0011 and
ADR-0012; its older working labels and proposal documents do not supersede
those ADRs. The dispositions here are reference-use and mapping recommendations,
not acceptance of a new DEC, schema change, import implementation, or runtime.

## Adopt as reference

| Source and exact locator | Reference use | Accepted decision bearing |
|---|---|---|
| L §Effects, lines 584–615; I §Action Objects, lines 33–40; §Operator Objects, lines 96–133 | Explain an action edge as a dependency on an effect, including success/failure branches and AND/OR joins. Chronological order alone loses this meaning; ambiguous joins remain visibly ambiguous. | ADR-0010 §Decision accepts AND/OR attack structure; ARCH-0001 §§2, 7 requires reviewable attack paths. This supports authoring and explanation, without accepting an evaluator. |
| L §STIX Common Properties, `created_by_ref`, `created`, `modified`, `external_references` (lines 84–114) | Cite sources at flow or action granularity and distinguish source authorship/version dates from the importer's own provenance. | ADR-0010 §Decision, Assertion/Review split; ADR-0011 §Decision A5, Assertion provenance. Source authorship is evidence, not a human verdict on applicability. |
| E `/objects/0` (`id`, `schema`, `version`, `extension_types`); S `/allOf/1` | Use the named `new-sdo` Extension Definition as the explicit boundary of any future Attack Flow adapter. | ADR-0007 §Decision commits STIX 2.1 import through a MAP and vector. Draft MAP-0002 §STIX 2.1 records that consumers may refuse content or ignore an unknown extension; baseline STIX import is not proof of extension support. |

## Adapt through a proposed crosswalk

These are candidate routes for a new `MAP-NNNN` and round-trip vector under
ADR-0007 §Decision/§Scope guard. They do not add slots or claim lossless
conversion. Imported applicability and inferred links remain hypotheses:
machine-proposed links are `proposed` Assertions until a human Review accepts
them (ARCH-0001 §2; ADR-0010 §Decision; ADR-0012 §Decision, Review rule).

| Source structure and locator | Candidate mapping and bounded loss | Decision route |
|---|---|---|
| L §Attack Flow, `scope`, `start_refs`; S `/$defs/attack-flow` | Candidate AttackPath grouping and metadata. Multiple starts and branches need an explicit membership/dependency mapping; one flow need not equal one linear path. CTI `scope` does not identify a Product, ProductInstance, deployment, or lifecycle phase. | ADR-0010 core AttackPath/ThreatInstance; ADR-0002 §Architectural considerations requires generic-to-instance context across domains. DEC-009 remains open. |
| L §Attack Action, `technique_id`, `technique_ref`, `tactic_id`, `tactic_ref`, `command_ref`; S `/$defs/attack-action` | An execution is a candidate AttackStep; its catalog technique is a separate candidate AttackPattern/reference. Tactics are not automatically `MethodFacet` or `kill_chain_phase`. Process commands and execution timestamps need a documented preservation/loss rule, not new implicit core slots. | ADR-0010 §Decision accepts the distinct types; ADR-0007 owns the field crosswalk. |
| L §Attack Operator, `operator`, `effect_refs`; I §Operator Objects, lines 96–133 | `AND`/`OR` can inform AttackStep `gate`, but a separate operator object and a gate on a step are not identical shapes. A vector must show preservation of incoming groups, outgoing effects, and ambiguous joins. | ADR-0010 §Decision, AttackGate/AND–OR core structure; ADR-0007 MAP/vector route. |
| L §Attack Condition, `description`, experimental `pattern*`, `on_true_refs`, `on_false_refs`; §Effects | No accepted standalone Condition class or typed pre/postcondition shape supplies a direct equivalent. Candidate Assertions may record dependencies, but `precedes` alone cannot encode predicates or false branches. Preserve unresolved source semantics in the mapping's loss account; do not silently flatten them. | ADR-0010 core AttackStep/Assertion; a new logical shape would require a DEC-001a amendment. Pattern evaluation is not accepted by importing its text. |
| L §Attack Asset, opening paragraphs and `object_ref`; S `/$defs/attack-asset` | Candidate Asset only when it is something worth protecting. The source also includes any action subject/target, technical or nontechnical; content may instead describe a Component or Party. `object_ref` alone establishes neither ownership nor `stored_in`/`processed_by`, and missing asset detail supplies no product context. | ADR-0011 §Decision B1/B5; ADR-0002 generic/instance split. |
| L §§Detection, Mitigation; I §Detections and Mitigations Objects, lines 202–208 | `x-mitigation` content may describe a candidate Mitigation. A detection is not an accepted Detection class, and neither object is automatically a Requirement, an implemented control, or evidence of effectiveness. Relationships and extension handling need their own mapping. | ADR-0010 Mitigation; ADR-0012 §Decision requires a distinct obligation and reviewed `stated_as`/`satisfied_by` links. Draft MAP-0002 §STIX 2.1 maps standard `course-of-action`, not these custom types. |

## Reject automatic assumptions

- **Confidence is not feasibility, impact, risk, or acceptance.** L §Confidence
  (lines 622–684) measures correctness of object data with its own seven-term
  scale; L §STIX Common Properties constrains its numeric range to 0–100.
  Neither that percentage nor a source claim of certainty sets path feasibility
  or a human Review. ADR-0006 §Decision requires human-rated feasibility and
  human-supplied S/F/O/P impact at MVP, with mitigation status a separate peer.
  Preserve source confidence explicitly in a future mapping; no target scale
  conversion is decided here. MAP-0002's draft STIX confidence discussion does
  not ratify this different seven-term conversion.
- **A CTI flow is not proof of applicability or a completed review.** A reported
  action, creator, timestamp, detection, or mitigation does not establish a
  target product's exposure, control state, or real damage. ARCH-0001 §§2, 7,
  ADR-0002 §Decision, and ADR-0012's Review rule retain the human decision.
- **Do not replace the canonical model or narrow it to ATT&CK.** L §Overview
  defines a STIX JSON extension; I §Action Objects, lines 18–22, also permits
  other technique collections and ad hoc actions. ADR-0007 keeps LinkML
  canonical and exports derived; ADR-0002 requires multiple product domains.
- **Do not infer transport or executable workflow.** The read source set defines
  data structures and described effects, not a request/response protocol,
  acknowledgement, retry, or error exchange. E is a data bundle, not a transport.
  L §Effects gives indeterminate action effects and branch selection, but no
  complete evaluation rule for AND/OR inputs mixing true, false, and
  indeterminate states. I §Parallel Attack Paths, lines 70–91, also warns that
  incident and campaign branches carry different meanings. No scheduler,
  operational state machine, or mitigation-lifecycle automation follows from
  this format (ADR-0002 §Scope; ADR-0007 §Scope guard).

## Independently observed source discrepancies and limits

| Finding and exact locator | Consequence for a future adapter/vector |
|---|---|
| L §Attack Flow SDOs describes seven types, including `x-detection` and `x-mitigation`; S `/$defs` and `/allOf/2` dispatch define only `attack-flow`, `attack-action`, `attack-asset`, `attack-condition`, `attack-operator`. | Record both surfaces. The two custom descriptions do not acquire typed schema validation from their appearance in the prose. |
| L §Attack Flow, `scope` (line 159), lists five values; S `/$defs/attack-flow/properties/scope/enum` lists seven, adding `emulation-plan` and `attack-tree`. | Schema-led acceptance and prose-led acceptance differ. Preserve the discrepancy and decide the adapter profile explicitly. |
| L §Attack Action labels `execution_start` and `execution_end` as `identifier` (lines 248–253), while their descriptions say timestamp; S `/$defs/attack-action/properties/execution_start` and `/execution_end` reference a timestamp schema. | Treat this as a prose/schema type conflict; the schema is identified as normative by L §Overview and S `/description`. Do not silently rewrite the source extract. |
| L §Detection example (lines 515–525) and §Mitigation example (lines 565–575) use non-UUID identifier suffixes and omit the extension declaration required by S `/allOf/1`. | These are not positive fixtures for the five-type extension schema. Keep original examples and their defects distinct from any corrected, derived fixtures. |
| S `/allOf/2`, nested final `else: true` (line 108), does not reject an unrecognized type through dispatch; common-property, extension, and `unevaluatedProperties` constraints still apply. | A successful root validation does not prove one of the five typed subschemas was applied. Do not describe the root as a closed five-type union. |
| S `/allOf/0/$ref` and identifier `$ref`s use the `stix2.1` branch; execution timestamp `$ref`s use `master`. E `/objects/0/schema` and S `/$id` also use different published paths (`/stix/` versus `/schema/`). | The local file digests do not pin transitive remote dependencies. Reproducible validation needs a recorded dependency/resolution set; no remote URL's equivalence or continued content is established here. |
| L §Attack Flow and S `/$defs/attack-flow/description` require exactly one flow per document, but S validates individual objects. Reference properties validate identifier syntax/prefixes, not target existence or whole-graph consistency. | Schema validation alone cannot establish document cardinality, reference resolution, branch meaning, or graph integrity. Those checks need a separate documented validation profile/vector under ADR-0007. |
| I §Action Objects, lines 42–43, attributes confidence to connecting lines; S `effect_refs`/`on_true_refs`/`on_false_refs` contain identifiers, while L defines common object confidence. | No structured per-edge confidence carrier is established by this schema. Do not invent one from the introductory wording. |

## Open questions

1. Which extension-aware STIX import profile, including unknown/custom object
   behavior and discrepancy handling, should the new MAP and vector exercise?
2. Can existing AttackStep gates/Assertions preserve conditions, false branches,
   multiple starts and operator groups, or is a separately reviewed core
   amendment needed? What source information must survive an explicit lossy
   round trip?
3. Which pinned STIX schema dependencies and graph-level checks define the
   validation result? How are unresolved external references represented?
4. If runtime evaluation is desired, who defines indeterminate-input handling,
   ambiguous joins and incident-versus-aggregate interpretation? The source does
   not settle these rules or target-product applicability.

**Human review pending for this artifact.** `reviewed_by` intentionally remains
blank. Passes 2–3 and per-artifact human sign-off are separate FX-1 gates; these
notes neither certify the other artifacts nor promote imported hypotheses to
reviewed model facts.
