---
record: mitre-attack-flow
kind: normative
title: "Attack Flow — normative language and schema constraints"
extracted: "2026-11-09"
reviewed_by: ""
text_origin: verbatim
source_digest: "85ae7b7f367b57c935328276a412e5b2f051e4d48f2ab622276359d49615fa49"
---

# Attack Flow — normative language and schema constraints

Source attribution: MITRE Center for Threat-Informed Defense, Attack Flow, repository tag `v4.1.0`. Copyright 2021 MITRE. Approved for public release. Document number CT0040. Source code and documentation are licensed under the [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0). This artifact extracts selected provisions and records constraints; it does not reproduce the complete language source document.

Pinned sources:

- [Language](https://raw.githubusercontent.com/center-for-threat-informed-defense/attack-flow/v4.1.0/docs/language.rst): `docs/language.rst`, 684 lines, SHA-256 `85ae7b7f367b57c935328276a412e5b2f051e4d48f2ab622276359d49615fa49`.
- [Normative JSON Schema](https://raw.githubusercontent.com/center-for-threat-informed-defense/attack-flow/v4.1.0/stix/attack-flow-schema-2.0.0.json): `stix/attack-flow-schema-2.0.0.json`, 430 lines, SHA-256 `fff896f5e1bdc39d9b387c0d3571307037cf9be1059de9cd94d066d1da2997cc`.
- [Extension definition](https://raw.githubusercontent.com/center-for-threat-informed-defense/attack-flow/v4.1.0/stix/attack-flow-extension-2.0.0.json): extension version `2.0.0`, extension identifier `extension-definition--fb9c968a-745b-4ade-9b25-c324172197f4` (lines 6–18); SHA-256 `afdbac65edc9805ea2f3b2b84b4ae4908644e7f4190f28e8e836659d74d87e70`.

Locators below name the source section and inclusive lines of the pinned source, not rendered HTML lines. Every fenced `rst` block is a contiguous, unchanged source excerpt, including source markup, spelling and whitespace. The source's object-section order is preserved. Headings, coverage notes, the schema inventory and discrepancy discussion outside quoted blocks are extraction commentary. JSON fragments in the schema inventory preserve the source's exact key and value spellings; fragments joined with prose or semicolons are separate quotations, not a claim that they are adjacent in the source.

Coverage: all 22 uppercase modal occurrences in the language source (20 obligation occurrences and 2 permission occurrences), all 10 tables, all seven object definitions and their 48 property rows, all eight common-property rows, eight datatype rows, seven confidence mappings, and the effects semantics. Of the 56 common/object property rows, 28 are marked required and 28 optional. Lowercase recommendations and permissions are retained too. Object examples are fixtures in the examples artifact; their instance values do not create additional constraints. The confidence conversion examples are retained beside their mapping table. The schema inventory covers every property constraint and required list in the supplied normative schema, including constraints absent from the language tables. External STIX schemas are referenced dependencies; their contents are not silently substituted for the pinned sources.

## Language source

### Overview

Locator: `docs/language.rst`, §Overview, lines 7–24. Context and the source's declaration of its formal specification.

```rst
Attack Flow is a machine-readable language that is defined as an extension to the
`Structured Threat Information Expression (STIX) 2.1 Standard.
<https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html>`__ STIX is a
machine-readable standard for cyber threat intelligence that is expressed in JSON for
easy parsing and processing across a variety of programming languages and computer
architectures. STIX 2.1 has `a formal extension mechanism
<https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_32j232tfvtly>`__ that
allows STIX to be augmented with new features and capabilities.

As a result of extending STIX, the Attack Flow language is interoperable with a broad
ecosystem of STIX content, tools, and vendors. A flow can reference external STIX
objects (e.g. an identity or a threat actor) and external STIX objects can also refer
back to an attack flow. Attack Flow extends STIX by defining several new STIX Domain
Objects (SDOs) that are described below.

The formal specification for the Attack Flow language is represented as `a JSON schema,
<https://github.com/center-for-threat-informed-defense/attack-flow/stix/attack-flow-schema-2.0.0.json>`__
but this page summarizes the extension objects and attributes that make up the language.
```

### STIX Datatypes

Locator: `docs/language.rst`, §STIX Datatypes, lines 29–56. The full datatype table is retained; the source delegates the complete datatype definitions to STIX Chapter 2.

```rst
STIX has built-in datatypes that are used in Attack Flow. The datatypes that are most
relevant to Attack Flow are summarized below.

.. list-table::
  :widths: 30 70
  :header-rows: 1

  * - Datatype
    - Description
  * - **boolean**
    - A value of true or false.
  * - **enum**
    - A value from a STIX Enumeration.
  * - **external-reference**
    - A non-STIX identifier or reference to other related external content.
  * - **float**
    - An IEEE 754 [IEEE 754-2008] double-precision number.
  * - **identifier**
    - An identifier (ID) is for STIX Objects.
  * - **integer**
    - A whole number.
  * - **string**
    - A series of Unicode characters.
  * - **timestamp**
    - A time value (date and time).

For the full list of data types, see `the STIX Standard Chapter 2.
<https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_gv21fm9t1qgx>`__
```

### STIX Common Properties

Locator: `docs/language.rst`, §STIX Common Properties, lines 61–114. All eight property rows are retained, including required/optional status, timestamp precision, confidence bounds, and external-reference placement. The source explicitly describes this as an incomplete list of STIX common properties.

```rst
All STIX objects, including Attack Flow objects, share a set of common properties. The
most important common properties are described in the table below. (See the STIX
specification for the complete list of `common properties.
<https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_ble33ropuhb8>`__)

.. list-table::
  :widths: 25 25 50
  :header-rows: 1

  * - Property Name
    - Type
    - Description
  * - **type** *(required)*
    - ``string``
    - Identifies the type of STIX object. It must be a valid object type as defined in
      the STIX 2.1 standard or in an extension (such as Attack Flow).
  * - **spec_version** *(required)*
    - ``string``
    - The version of the STIX specification used to represent this object. The value
      must be ``2.1`` for all Attack Flow objects.
  * - **id** *(required)*
    - ``identifier``
    - Uniquely identifies each object.
  * - **created_by_ref** *(optional)*
    - ``identifier``
    - Specifies the ``id`` property of the ``identity`` object that describes the entity
      that created this object.
  * - **created** *(required)*
    - ``timestamp``
    - Represents the time at which the object was originally created. The object creator
      can use the time it deems most appropriate as the time the object was created. The
      minimum precision MUST be milliseconds (three digits after the decimal place in
      seconds), but MAY be more precise.
  * - **modified** *(required)*
    - ``timestamp``
    - The modified property is only used by STIX Objects that support versioning and
      represents the time that this particular version of the object was last modified.
      The object creator can use the time it deems most appropriate as the time this
      version of the object was modified. The minimum precision MUST be milliseconds
      (three digits after the decimal place in seconds), but MAY be more precise.
  * - **confidence** *(optional)*
    - ``integer``
    - The confidence property identifies the confidence that the creator has in the
      correctness of their data. The confidence value MUST be a number in the range of
      0-100. Attack Flow uses a :ref:`confidence scale <confidence>` to convert from
      numerical confidence to human terms.
  * - **external_references** *(optional)*
    - ``list`` of ``external-reference``
    - Citing the intelligence sources consulted for creating an Attack Flow is an
      important part of producing informative and trustworthy flows. You can include
      this property on the ``attack-flow`` object to cite the sources used for creating
      the flow, or you can include references on ``attack-action`` objects for
      fine-grained sourcing. For the STIX standard, see `STIX Chap. 2.5.
      <https://docs.oasis-open.org/cti/stix/v2.1/cs02/stix-v2.1-cs02.html#_72bcfr3t79jx>`__
```

### Attack Flow SDOs

Locator: `docs/language.rst`, §Attack Flow SDOs, lines 119–122. The source identifies the extension objects and links to their schema.

```rst
This section describes the STIX Domain Objects (SDOs) defined in the Attack Flow
extension. The complete extension, schema, and example flow can be found on `the Attack
Flow GitHub.
<https://github.com/center-for-threat-informed-defense/attack-flow/stix/>`__
```

#### Attack Flow

Locator: `docs/language.rst`, §Attack Flow SDOs → Attack Flow, lines 131–162. Document cardinality and the complete six-row object table.

```rst
Every Attack Flow document **MUST** contain exactly one ``attack-flow`` object.
It provides metadata for name and description, starting points for the flow of
actions, and can be referenced from other STIX objects.

.. list-table::
   :widths: 20 30 50
   :header-rows: 1

   * - Property Name
     - Type
     - Description
   * - **type** *(required)*
     - ``string``
     - The type **MUST** be ``attack-flow``.
   * - **spec_version** *(required)*
     - ``string``
     - The version **MUST** be ``2.1``.
   * - **name** *(required)*
     - ``string``
     - The name of the Attack Flow.
   * - **description** *(optional)*
     - ``string``
     - A description of the overall Attack Flow.
   * - **scope** *(required)*
     - ``enum``
     - Indicates what type of behavior the Attack Flow describes: a specific incident,
       a campaign, etc.

       The value of this property **MUST** be one of: "incident", "campaign", "threat-actor", "malware", "other".
   * - **start_refs** *(required)*
     - ``list`` of type ``identifier`` (of type ``attack-action`` or ``attack-condition``)
     - A list of objects that start the flow.
```

#### Attack Action

Locator: `docs/language.rst`, §Attack Flow SDOs → Attack Action, lines 207–266. Object meaning and the complete thirteen-row object table.

```rst
An ``attack-action`` object represents the execution of a particular technique,
i.e. a discrete unit of adverary behavior.

.. list-table::
   :widths: 20 30 50
   :header-rows: 1

   * - Property Name
     - Type
     - Description
   * - **type** *(required)*
     - ``string``
     - The type **MUST** be ``attack-action``.
   * - **spec_version** *(required)*
     - ``string``
     - The version **MUST** be ``2.1``.
   * - **name** *(required)*
     - ``string``
     - The name of the technique, or if a specific technique is not known, then the
       name of the tactic.
   * - **tactic_id** *(optional)*
     - ``string``
     - A tactic identifier or shortname that may reference an authoritative collection
       of tactics, e.g. ATT&CK.
   * - **tactic_ref** *(optional)*
     - ``identifier``
     - A reference to the tactic's STIX representation. For ATT&CK, this should be an
       ``x-mitre-tactic`` object.
   * - **technique_id** *(optional)*
     - ``string``
     - A technique identifier or shortname that may reference an authoritative
       collection of techniques, e.g. ATT&CK.
   * - **technique_ref** *(optional)*
     - ``identifier`` (of type ``attack-pattern``)
     - A reference to the technique's STIX representation.
   * - **description** *(optional)*
     - ``string``
     - A description of the adversary behavior, e.g. what they did, how they did it,
       and why. This field may contain prose as well as technical information, but
       consider using ``command_ref`` for providing technical details about technique
       execution.
   * - **execution_start** *(optional)*
     - ``identifier``
     - Timestamp indicating when the execution of this action began.
   * - **execution_end** *(optional)*
     - ``identifier``
     - Timestamp indicating when the execution of this action ended.
   * - **command_ref** *(optional)*
     - ``identifier`` (of type ``process``)
     - Describe tools or commands executed by the attacker by referring to a STIX
       Process object, which can represent commands, environment variables, process
       image, etc.
   * - **asset_refs** *(optional)*
     - ``list`` of type ``identifier`` (of type ``attack-asset``)
     - The assets involved in this action, i.e. where this action modifies or depends
       on the state of the asset.
   * - **effect_refs** *(optional)*
     - ``list`` of type ``identifier`` (of type ``attack-action`` or ``attack-operator`` or ``attack-condition``)
     - The potential effects that result from executing this action. (See:
       :ref:`effects`.)
```

#### Attack Asset

Locator: `docs/language.rst`, §Attack Flow SDOs → Attack Asset, lines 297–331. Asset meaning, contextual-use recommendation, and the complete five-row object table.

```rst
An asset is any object that is the subject or target of an action. Assets can be
technical assets (such as machines and data) or non-technical assets such as
people and physical systems. Actions typically either modify or depend upon the
*state* of an asset in some way.

Note that assets are not applicable in all
contexts. For example, public threat reports may not include enough detail to
represent the assets in a flow, or the flow might represent aggregate behavior
(at the campaign or actor level) for which it does not make sense to specify an
asset. Assets should be used to add context to a flow when the underlying
intelligence contains sufficient detail to do so.

.. list-table::
   :widths: 20 30 50
   :header-rows: 1

   * - Property Name
     - Type
     - Description
   * - **type** *(required)*
     - ``string``
     - The type **MUST** be ``attack-asset``.
   * - **spec_version** *(required)*
     - ``string``
     - The version **MUST** be ``2.1``.
   * - **name** *(required)*
     - ``string``
     - An name for the asset.
   * - **description** *(optional)*
     - ``string``
     - A description of the asset.
   * - **object_ref** *(optional)*
     - ``identifier``
     - A reference to any STIX data object (i.e. SDO) or observable (i.e. SCO) that
       contains structured data about this asset.
```

#### Attack Condition

Locator: `docs/language.rst`, §Attack Flow SDOs → Attack Condition, lines 358–401. Condition meaning, experimental pattern fields, branch behavior, and the complete eight-row object table.

```rst
An ``attack-condition`` object represents some possible condition, outcome, or
state that could occur. Conditions can be used to split flows based on the
success or failure of an action, or to provide further description of an
action's results.

.. list-table::
   :widths: 20 30 50
   :header-rows: 1

   * - Property Name
     - Type
     - Description
   * - **type** *(required)*
     - ``string``
     - The type **MUST** be ``attack-condition``.
   * - **spec_version** *(required)*
     - ``string``
     - The version **MUST** be ``2.1``.
   * - **description** *(required)*
     - ``string``
     - The condition that is evaluated, usually based on the success or failure of the
       preceding action.
   * - **pattern** *(optional)*
     - ``string``
     - *(This is an experimental feature.)* The detection pattern for this condition
       may be expressed as a STIX Pattern or another appropriate language such as
       SNORT, YARA, etc.
   * - **pattern_type** *(optional)*
     - ``string``
     - *(This is an experimental feature.)* The pattern langauge used in this
       condition. The value for this property should come from the STIX
       ``pattern-type-ov`` open vocabulary.
   * - **pattern_version** *(optional)*
     - ``string``
     - *(This is an experimental feature.)* The version of the pattern language used
       for the data in the ``pattern`` property. For the STIX Pattern language, the
       default value is determined by the ``spec_version`` of the condition object.
   * - **on_true_refs** *(optional)*
     - ``list`` of type ``identifier`` (of type ``attack-action`` or ``attack-operator`` or ``attack-condition``)
     - When the condition is ``true``, the flow continues to these objects.
   * - **on_false_refs** *(optional)*
     - ``list`` of type ``identifier`` (of type ``attack-action`` or ``attack-operator`` or ``attack-condition``)
     - When the condition is ``false``, the flow continues to these objects. (If there
       are no objects, then the flow halts at this node.)
```

#### Attack Operator

Locator: `docs/language.rst`, §Attack Flow SDOs → Attack Operator, lines 429–454. Boolean join meaning, closed operator values, effect/halt behavior, and the complete four-row object table.

```rst
An ``attack-operator`` object joins multiple attack paths together using boolean
logic.

.. list-table::
   :widths: 20 30 50
   :header-rows: 1

   * - Property Name
     - Type
     - Description
   * - **type** *(required)*
     - ``string``
     - The type **MUST** be ``attack-operator``.
   * - **spec_version** *(required)*
     - ``string``
     - The version **MUST** be ``2.1``.
   * - **operator** *(required)*
     - ``enum``
     - The logical operator to apply to the input effects.

        The value of this property **MUST** be one of: "AND", "OR".
   * - **effect_refs** *(optional)*
     - ``list`` of type ``identifier`` (of type ``attack-action`` or ``attack-operator`` or ``attack-condition``)
     - The effects, outcomes, or states that result when this operator evaluates to
       ``true``. If the operator evaluates to ``false``, then the flow halts. (See:
       :ref:`effects`.)
```

#### Detection

Locator: `docs/language.rst`, §Attack Flow SDOs → Detection, lines 482–509. Custom detection meaning and the complete six-row object table, including the required label content.

```rst
A ``x-detection`` object represents an ATT&CK Detection Strategy and are custom STIX objects. An ATT&CK Detection Strategy can be defined as a method or technique that can be used
to identify adversary activity.

.. list-table::
   :widths: 20 30 50
   :header-rows: 1

   * - Property Name
     - Type
     - Description
   * - **type** *(required)*
     - ``string``
     - The type **MUST** be ``x-detection``.
   * - **spec_version** *(required)*
     - ``string``
     - The version **MUST** be ``2.1``.
   * - **detection_id** *(optional)*
     - ``string``
     - A unique identifier for the detection (e.g., "DET0516").
   * - **name** *(optional)*
     - ``string``
     - A human-readable name for the detection.
   * - **description** *(optional)*
     - ``string``
     - A description of the detection method.
   * - **labels** *(required)*
     - ``list`` of type ``string``
     - A list containing the string ``x-detection``.
```

#### Mitigation

Locator: `docs/language.rst`, §Attack Flow SDOs → Mitigation, lines 532–559. Custom mitigation meaning and the complete six-row object table, including the required label content.

```rst
A ``x-mitigation`` object represents an ATT&CK mitigation and is a custom STIX object. An ATT&CK mitigation can be defined as a strategy or control that can be used
to prevent or reduce the impact of adversary activity.

.. list-table::
   :widths: 20 30 50
   :header-rows: 1

   * - Property Name
     - Type
     - Description
   * - **type** *(required)*
     - ``string``
     - The type **MUST** be ``x-mitigation``.
   * - **spec_version** *(required)*
     - ``string``
     - The version **MUST** be ``2.1``.
   * - **mitigation_id** *(optional)*
     - ``string``
     - A unique identifier for the mitigation (e.g., "M1021").
   * - **name** *(optional)*
     - ``string``
     - A human-readable name for the mitigation.
   * - **description** *(optional)*
     - ``string``
     - A description of the mitigation strategy.
   * - **labels** *(required)*
     - ``list`` of type ``string``
     - A list containing the string ``x-mitigation``.
```

### Effects

Locator: `docs/language.rst`, §Effects, lines 584–615. Effect definition, dependency examples, indeterminate execution state, success-dependent action chaining, exclusive condition-branch selection, and operator aggregation. The examples within this prose explain the meaning of effects; they do not add field constraints.

```rst
One of the key ideas behind Attack Flow is understanding how individual adversary
techniques relate to each other. The concept of *effect* is critical for understanding
these relationships between techniques. An effect is the outcome, result, or change in
state that occurs when an adversary executes a technique. Examples of effects include:

1. The attacker modifies the state of an asset, e.g. opening a port on the firewall.
2. The attacker gains some knowledge, e.g. a password.
3. The attacker achieves code execution.

Actions can produce effects, and subsequent actions may *depend* on those effects:

1. The attacker wants to connect to an internal service, which requires opening a port
   on the firewall.
2. The attacker wants to log in remotely, which depends on knowing the password.
3. The attacker wants to run a C2 implant, which depends on having code execution.

While an *action* is being executed, it's effect is an *indeterminate* state, i.e. we
cannot make any statement about the outcome or result. Once the action concludes, then
we can evaluate its effects, whether it succeeded or failed, etc. When one action is
chained to another, the latter depends on the effects of the former, i.e. the second one
can only execute when the first one completes successfully.

A *condition* splits a flow into multiple paths based on evaluating an effect, e.g. if
the action is a privilege escalation exploit, then the condition can test whether the
attacker has obtained elevated privileges (i.e. the exploit succeeded) or still has
regular privileges (i.e. the exploit failed.) A condition always selects one path to
follow, either the ``on_true_refs`` or the ``on_false_refs``.

On the other hand, an *operator* joins multiple attack paths together by aggregating
multiple effects. Conditions and operators can be used to encode complex behavior into
an attack flow that represents how attackers coordinate multiple behaviors to achieve a
desired outcome, as well as how they handle individual technique failure.
```

### Confidence

Locator: `docs/language.rst`, §Confidence, lines 622–684. Inclusive numerical range, the complete seven-row confidence table, and both conversion examples.

```rst
The ``confidence`` property is STIX common property that establishes the confidence in
the correctness of the data in a particular object, e.g. in a particular
``attack-action``. In STIX, the value is defined as a number from 0 to 100 (inclusive),
i.e. a percentage. It is often difficult or impossible to estimate confidence to that
level of precision, because Attack Flow typically describes real-world behavior that may
have been observed only a few times, which is not a large enough sample to compute
precise statistics.

To make ``confidence`` easier to reason about, Attack Flow uses the following confidence
scale to map confidence terms to numbers, and vice-versa.

.. list-table:: Confidence Terms
  :widths: 15 55 15 15
  :header-rows: 1

  * - Term
    - Description
    - Confidence Value
    - Confidence Range
  * - Speculation
    - Information that is purely speculative or hypothetical, e.g. the author imagines a
      what-if scenario.
    - 0
    - 0-0
  * - Very Doubtful
    - Information that is very unlikely to be true. All of the available evidence is
      against it, or it may have bias in its reporting, e.g. an adversary providing
      attribution information.
    - 10
    - 1-20
  * - Doubtful
    - Information that is unlikely to be true. Most of the available evidence is against
      it.
    - 30
    - 21-40
  * - Even Odds
    - Information that is equally like to be true as not true; a coin flip. The
      available evidence is equally weighted in support and against.
    - 50
    - 41-60
  * - Probable
    - Information that is likely to be true. Most of the available evidence supports it.
    - 70
    - 61-80
  * - Very Probable
    - Information that is very likely to be true. All of the available evidence supports
      it.
    - 90
    - 81-99
  * - Certainty
    - Information that is unquestionably true.
    - 100
    - 100-100

Example usage of the table:

* Convert "Very Probable" to a confidence number:
    * Look up "Very Probable" in the table: it is in row 6.
    * Read off the Confidence Value for row 6: it is 90.
* Convert 38 to a confidence term.
    * Go down the Confidence Range column to find the range containing 38: it is in the
      21-40 range, which is row 3.
    * Read off the term from row 3: "Doubtful".
```

## Normative JSON Schema constraint inventory

The language source calls the JSON Schema its formal specification (§Overview, lines 22–24). The schema independently identifies itself as the normative definition (schema line 5). The inventory below distinguishes schema constraints from the quoted language; it does not rewrite either source to reconcile differences. JSON pointers identify the exact constrained locations. Schema annotations (`title`, descriptions, comments and `x-exampleObject`) do not themselves add JSON Schema assertions; descriptions that duplicate language provisions are already quoted above. The document-cardinality statement in a schema description remains a prose requirement even though the schema validates individual objects.

### Schema identity and root constraints

Locator: `stix/attack-flow-schema-2.0.0.json`, root, lines 2–11.

```json
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "https://center-for-threat-informed-defense.github.io/attack-flow/schema/attack-flow-schema-2.0.0.json",
    "title": "Attack Flow STIX 2.1 Extension",
    "description": "This schema is the normative definition of the STIX 2.1 extension `extension-definition--fb9c968a-745b-4ade-9b25-c324172197f4`. It extends STIX with additional STIX Data Objects (SDOs) that model Attack Flow concepts.",
    "type": "object",
    "unevaluatedProperties": false,
    "allOf": [
        {
            "$comment": "All Attack Flow SDOs implement the required common properties.",
            "$ref": "http://raw.githubusercontent.com/oasis-open/cti-stix2-json-schemas/stix2.1/schemas/common/core.json"
```

The root applies `allOf` to the common-core reference, the extension-envelope constraints below, and the object-type dispatch. Thus the common-core reference applies in addition to the selected object definition. The root is an object with unevaluated properties disallowed; this is not a separate per-definition `additionalProperties` declaration.

### Extension-envelope constraints

Locator: schema `/allOf/1`, lines 14–40. The top-level `extensions` property, this extension identifier within it, and `extension_type` within that entry are all required. Every level shown is typed as an object; `extension_type` is a string with the literal value `new-sdo`.

```json
            "$comment": "Attack Flow SDOs must reference the extension definition.",
            "type": "object",
            "properties": {
                "extensions": {
                    "type": "object",
                    "properties": {
                        "extension-definition--fb9c968a-745b-4ade-9b25-c324172197f4": {
                            "type": "object",
                            "properties": {
                                "extension_type": {
                                    "type": "string",
                                    "const": "new-sdo"
                                }
                            },
                            "required": [
                                "extension_type"
                            ]
                        }
                    },
                    "required": [
                        "extension-definition--fb9c968a-745b-4ade-9b25-c324172197f4"
                    ]
                }
            },
            "required": [
                "extensions"
            ]
```

### Type dispatch

Locator: schema `/allOf/2`, lines 43–112. Each `if` tests an object whose `type` is a string with the indicated constant. The selected `then` uses the exact definition reference shown. The chain terminates in the literal `"else": true` at line 108; this leaves the other root `allOf` constraints in force.

| `type` constant | Selected `$ref` | Schema lines |
|---|---|---|
| `attack-flow` | `#/$defs/attack-flow` | 44–54 |
| `attack-action` | `#/$defs/attack-action` | 57–67 |
| `attack-condition` | `#/$defs/attack-condition` | 70–80 |
| `attack-operator` | `#/$defs/attack-operator` | 83–93 |
| `attack-asset` | `#/$defs/attack-asset` | 96–108 |

No dispatch case or `$defs` entry for `x-detection` or `x-mitigation` appears in the supplied schema.

### Referenced STIX schemas

These are the source's exact reference targets, retained without URL normalization. The symbolic names in the inventory tables below are local abbreviations for these references, not new schema definitions.

| Inventory name | Literal source `$ref` | Use and schema lines |
|---|---|---|
| Common core | `http://raw.githubusercontent.com/oasis-open/cti-stix2-json-schemas/stix2.1/schemas/common/core.json` | Root common properties, line 11 |
| Identifier | `http://raw.githubusercontent.com/oasis-open/cti-stix2-json-schemas/stix2.1/schemas/common/identifier.json` | `start_refs` item, line 157; `tactic_ref`, line 202; `technique_ref`, line 214; `command_ref`, line 237; `asset_refs` item, line 250; action `effect_refs` item, line 265; asset `object_ref`, line 306; `on_true_refs` item, line 352; `on_false_refs` item, line 367; operator `effect_refs` item, line 412 |
| Timestamp | `https://raw.githubusercontent.com/oasis-open/cti-stix2-json-schemas/master/schemas/common/timestamp.json` | `execution_start`, line 227; `execution_end`, line 231 |

The timestamp references target `master`; the other references use `stix2.1`. These are the reference strings present in the pinned schema, not a claim that all remote dependencies are independently pinned by its tag.

### Reference-prefix patterns containing alternatives

These two inventory names preserve the following literal source fragments. The same Effect pattern also occurs at schema lines 355, 370 and 415.

Start pattern, locator `/$defs/attack-flow/properties/start_refs/items/allOf/1/pattern`, schema line 160:

```json
                                "pattern": "^(attack-action|attack-condition)--"
```

Effect pattern, locator `/$defs/attack-action/properties/effect_refs/items/allOf/1/pattern`, schema line 268:

```json
                                "pattern": "^(attack-action|attack-operator|attack-condition)--"
```

### `attack-flow` constraints

Locator: schema `/$defs/attack-flow`, lines 116–175. The definition itself has `"type": "object"` (line 118).

| Property pointer under `/$defs/attack-flow/properties` | Literal assertion fragments and reference composition | Schema lines |
|---|---|---|
| `/type` | `"type": "string"`; `"const": "attack-flow"` | 120–124 |
| `/spec_version` | `"type": "string"`; `"const": "2.1"` | 125–129 |
| `/name` | `"type": "string"` | 130–133 |
| `/description` | `"type": "string"` | 134–137 |
| `/scope` | `"type": "string"`; exact `enum` below | 138–150 |
| `/start_refs` | `"type": "array"`; each item is `allOf` Identifier and the Start pattern below; `"minItems": 1` | 151–165 |

Closed `scope` values, locator `/$defs/attack-flow/properties/scope/enum`, schema lines 141–149:

```json
                    "enum": [
                        "incident",
                        "campaign",
                        "threat-actor",
                        "malware",
                        "emulation-plan",
                        "attack-tree",
                        "other"
                    ]
```

Required properties, locator `/$defs/attack-flow/required`, schema lines 167–173:

```json
            "required": [
                "type",
                "spec_version",
                "name",
                "start_refs",
                "scope"
            ],
```

### `attack-action` constraints

Locator: schema `/$defs/attack-action`, lines 176–281. The definition itself has `"type": "object"` (line 178).

| Property pointer under `/$defs/attack-action/properties` | Literal assertion fragments and reference composition | Schema lines |
|---|---|---|
| `/type` | `"type": "string"`; `"const": "attack-action"` | 180–184 |
| `/spec_version` | `"type": "string"`; `"const": "2.1"` | 185–189 |
| `/name` | `"type": "string"` | 190–193 |
| `/tactic_id` | `"type": "string"` | 194–197 |
| `/tactic_ref` | `allOf` containing Identifier; no additional type-prefix `pattern` in this property | 198–205 |
| `/technique_id` | `"type": "string"` | 206–209 |
| `/technique_ref` | `allOf` Identifier and `"pattern": "^attack-pattern--"` | 210–220 |
| `/description` | `"type": "string"` | 221–224 |
| `/execution_start` | Timestamp reference | 225–228 |
| `/execution_end` | Timestamp reference | 229–232 |
| `/command_ref` | `allOf` Identifier and `"pattern": "^process--"` | 233–243 |
| `/asset_refs` | `"type": "array"`; each item is `allOf` Identifier and `"pattern": "^(attack-asset)--"`; `"minItems": 1` | 244–258 |
| `/effect_refs` | `"type": "array"`; each item is `allOf` Identifier and the Effect pattern below; `"minItems": 1` | 259–273 |

Required properties, locator `/$defs/attack-action/required`, schema lines 275–279:

```json
            "required": [
                "type",
                "spec_version",
                "name"
            ],
```

### `attack-asset` constraints

Locator: schema `/$defs/attack-asset`, lines 282–315. The definition itself has `"type": "object"` (line 284).

| Property pointer under `/$defs/attack-asset/properties` | Literal assertion fragments and reference composition | Schema lines |
|---|---|---|
| `/type` | `"type": "string"`; `"const": "attack-asset"` | 286–290 |
| `/spec_version` | `"type": "string"`; `"const": "2.1"` | 291–295 |
| `/name` | `"type": "string"` | 296–299 |
| `/description` | `"type": "string"` | 300–303 |
| `/object_ref` | Identifier reference | 304–307 |

Required properties, locator `/$defs/attack-asset/required`, schema lines 309–313:

```json
            "required": [
                "type",
                "spec_version",
                "name"
            ],
```

### `attack-condition` constraints

Locator: schema `/$defs/attack-condition`, lines 316–383. The definition itself has `"type": "object"` (line 318).

| Property pointer under `/$defs/attack-condition/properties` | Literal assertion fragments and reference composition | Schema lines |
|---|---|---|
| `/type` | `"type": "string"`; `"const": "attack-condition"` | 320–324 |
| `/spec_version` | `"type": "string"`; `"const": "2.1"` | 325–329 |
| `/description` | `"type": "string"` | 330–333 |
| `/pattern` | `"type": "string"` | 334–337 |
| `/pattern_type` | `"type": "string"` | 338–341 |
| `/pattern_version` | `"type": "string"` | 342–345 |
| `/on_true_refs` | `"type": "array"`; each item is `allOf` Identifier and the Effect pattern below; `"minItems": 1` | 346–360 |
| `/on_false_refs` | `"type": "array"`; each item is `allOf` Identifier and the Effect pattern below; `"minItems": 1` | 361–375 |

Required properties, locator `/$defs/attack-condition/required`, schema lines 377–381:

```json
            "required": [
                "type",
                "spec_version",
                "description"
            ],
```

### `attack-operator` constraints

Locator: schema `/$defs/attack-operator`, lines 384–428. The definition itself has `"type": "object"` (line 386).

| Property pointer under `/$defs/attack-operator/properties` | Literal assertion fragments and reference composition | Schema lines |
|---|---|---|
| `/type` | `"type": "string"`; `"const": "attack-operator"` | 388–392 |
| `/spec_version` | `"type": "string"`; `"const": "2.1"` | 393–397 |
| `/operator` | `"type": "string"`; exact `enum` below | 398–405 |
| `/effect_refs` | `"type": "array"`; each item is `allOf` Identifier and the Effect pattern below; `"minItems": 1` | 406–420 |

Closed `operator` values, locator `/$defs/attack-operator/properties/operator/enum`, schema lines 401–404:

```json
                    "enum": [
                        "AND",
                        "OR"
                    ]
```

Required properties, locator `/$defs/attack-operator/required`, schema lines 422–426:

```json
            "required": [
                "type",
                "spec_version",
                "operator"
            ],
```

## Source discrepancies and limits

These findings preserve the two source representations. They do not introduce replacement requirements or silently choose an interpretation.

1. **Different closed scope sets.** The language's object table says the value is one of `incident`, `campaign`, `threat-actor`, `malware`, or `other` (Language §Attack Flow, line 159). The normative schema's enum additionally includes `emulation-plan` and `attack-tree` (`/$defs/attack-flow/properties/scope/enum`, schema lines 141–149). Both sets are retained exactly. The same extension version is used despite the different published sets.
2. **Execution-time type disagreement.** The language marks `execution_start` and `execution_end` as `identifier`, while their descriptions call them timestamps (Language §Attack Action, lines 248–253). The schema uses Timestamp references for these properties (schema lines 225–231). The extraction does not convert the quoted table's type or invent an identifier-valued timestamp encoding.
3. **Custom objects exist only in the language tables.** Detection and mitigation define `x-detection` and `x-mitigation`, their property types, and required `labels` containing the corresponding string (Language §Detection, lines 482–509; §Mitigation, lines 532–559). The schema has only five dispatch routes (lines 43–112) and five definitions (lines 115–428), with no definitions for these custom objects. The fallback `"else": true` (line 108) still combines with the root common-core, extension-envelope and unevaluated-property constraints. Absence of dedicated definitions is not treated as proof that arbitrary custom-object instances validate. The two language examples also omit the extension envelope (Language lines 515–525 and 565–575); the schema root requires it (schema lines 14–40).
4. **Nonempty arrays are specified by the schema.** All six reference-list properties use `"minItems": 1`: flow `start_refs` (schema line 164), action `asset_refs` and `effect_refs` (257, 272), condition `on_true_refs` and `on_false_refs` (359, 374), and operator `effect_refs` (419). The language tables do not state that minimum (Language lines 160–162, 259–266, 395–401, 450–454). The prose's false-condition halt when there are no objects (Language lines 400–401) does not clarify whether absence or an empty array expresses that case; the schema makes those branch lists optional but disallows an empty array when one is present. No new requirement is inferred for the absent true branch.
5. **Envelope and closed-property validation are not in the common-property table.** The language lists its most important common properties rather than a complete set (Language lines 61–64). The schema explicitly requires the extension identifier and `extension_type: new-sdo`, and sets root `"unevaluatedProperties": false` (schema lines 7, 14–40). These are retained as schema constraints rather than added to the quoted table. The quoted language examples for the five extension SDOs include the extension entry (Language lines 195–199, 285–289, 346–350, 417–421, 470–474).
6. **Document and graph rules exceed object validation.** The exact-one-flow rule is explicit in the language and repeated in a schema description (Language line 131; schema line 117), but the schema root has `"type": "object"` and does not validate a whole bundle's object count. Likewise, reference patterns constrain identifier strings, not whether the referenced objects exist or whether action/condition/operator execution semantics hold. The Effects section supplies the indeterminate-state, success-chaining and branch-selection semantics (Language lines 600–615); the schema supplies structural validation. No additional evaluation order, scheduling rule, cycle policy, or truth table for indeterminate operator inputs is specified in these sources.
7. **Reference recommendations are narrower than structural checks.** The language recommends an `x-mitre-tactic` target for ATT&CK `tactic_ref` (Language lines 231–234); its schema applies only the Identifier reference with no tactic-prefix pattern (schema lines 198–205). The experimental `pattern_type` recommendation and `pattern_version` default are prose provisions (Language lines 385–394); the schema types both as strings without an enum or JSON Schema default (schema lines 338–345). These recommendations and defaults are retained without strengthening them into validation assertions.
8. **Inherited constraints require separate STIX sources.** The language delegates full datatypes and common properties to STIX (Language lines 55–56, 61–64). The supplied schema references external core, identifier and timestamp schemas rather than embedding their full definitions (schema lines 11, 157, 227 and the reference inventory above). This extraction records those dependencies and preserves its directly stated precision and confidence rules. It does not claim to have extracted every inherited STIX rule from the language summary alone.

Human review is outstanding: `reviewed_by` is intentionally blank.
