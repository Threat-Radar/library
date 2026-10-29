---
record: open-threat-model
kind: normative
title: "open-threat-model — normative statements"
extracted: "2026-10-13"
reviewed_by: ""
---

# Open Threat Model (OTM) 0.2.0 — normative content

Source: the Open Threat Model specification in the repository <https://github.com/iriusrisk/OpenThreatModel> at commit `c88c5a7b4115f0f025e28d5682a2b0d790b389e4` (2025-12-11). `README.md` is the specification text: 2034 lines, SHA-256 `4acfb48b04423a6abecf805673890e38edf4df6340dc1269d6ac2e1ef78cf8c0`, licensed CC BY-SA 4.0 (L2033). `otm_schema.json` is its JSON Schema: 308 lines, JSON Schema draft-07, `$id` `https://iriusrisk.com/schema/otm-0.2.0.schema.json`, SHA-256 `81e7f5a52a0a7d66b44cc4e0c15f21b5d60e1ca945c810e39622a730545eef0c`, Apache License 2.0 by its own `$comment`. Specification version 0.2.0 (README L18). Pass-1 extraction (agent A), 2026-10-13; verify and cross-check passes by agent C, 2026-10-14 (`verification.md`).

How to read this file:

- Order: the README in source order (Introduction to Position object, then the licence footer), then `otm_schema.json`, then a field-by-field README ↔ schema comparison, then the source defects. Only the last two sections, the *Extractor's note* paragraphs and the requirement column of each table are ours; everything else is source text.
- Headings keep the README's own nesting, one level down (README `#` is `##` here). The README puts every object section under `# Schema` and `### Position object` under `## Size object` (D-24); this file keeps that.
- `(L<n>)` is a README.md line, except inside the otm_schema.json sections, where it is a schema line; `(schema L<n>)` an otm_schema.json line, with a JSON pointer where useful.
- Quotations are verbatim: spelling, grammar and typography uncorrected. Markdown and HTML markup is kept as written (`**REQUIRED**`, `<b>REQUIRED</b>`, `<br/>`, `&lt;string, string&gt;`, links). Inside a quoted table cell, line breaks and whitespace runs show as one space.
- Field tables: every row of every table, the Field, Type and Description cells verbatim, with the README line of the Description cell and the requirements extracted from it. The Examples column follows each table as code blocks, verbatim except that the indentation common to the cell's lines is removed. The `#### Example` blocks are informative: each is listed by line range with the result of a pass-1 check against the matching schema location; the fixtures themselves are in `examples/`.
- `R-NNNN` is `open-threat-model#R-NNNN` in `requirements.yaml` (verb in brackets). A keyword row's requirement quotes the whole Description cell; further rules inside the same cell have their own ids. `requirements.yaml` also accounts for every keyword-like word, upper- and lower-case (`keyword_accounting`).

## Introduction (L1–L7)

*Informative: purpose and use cases. No requirement is extracted.*

- (L3) The Open Threat Modeling Format (OTM) defines a platform independent way to define the threat model of any system.

- (L5) OTM allows both humans and computers to understand what are the components of a system, how are they distributed, the security risks that could be exposed to attackers and the mitigations that could be implemented to avoid those vulnerabilities.

- (L7) OTM can be used to document your system and threat model, to keep you threat model aware of the changes that happens in the system and many other use cases.

## Complete example (L9–L11)

- (L11) For a complete example see [EXAMPLE.yaml](EXAMPLE.yaml) or [EXAMPLE.json](EXAMPLE.json).

  *Extractor's note:* `EXAMPLE.yaml` (232 lines, SHA-256 `d78f4282…a2761`) and `EXAMPLE.json` (320 lines, SHA-256 `045667cd…387b`) are the complete example; both validate against `otm_schema.json`, and both use members that neither the README nor the schema defines (D-30). They are fixtures in `examples/`.

## Versions (L13–L19)

- (L15) The Open Threat Model specification is versioned using [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html) (semver) and follows the semver specification.  → R-0001 (versioning)

- (L17–L19)

  ```
  Current schema version: 0.2.0
  ```

## Format (L21–L27)

- (L23) An OTM document is itself a JSON object, which may be represented either in JSON or YAML format.  → R-0002 (may), R-0003 (data-model, inferred)

- (L25) All field names in the specification are **case sensitive**. This includes all fields that are used as keys in a map.  → R-0004 (case-sensitive)

- (L27) The specification follows the same approach to JSON formats as the OpenAPI specification. See https://swagger.io/specification/ for more information.  → R-0005 (normative-reference)

  *Extractor's note:* L23-L31 follow the wording of the OpenAPI Specification 3.0 sections *Format* and *Data Types*, which L27 points to; the `nullable` of L31 is an OpenAPI 3.0 Schema Object field that OTM does not define (D-04).

## Data Types (L29–L45)

- (L31) Primitive data types in the OTM are based on the types supported by the [JSON Schema Specification Wright Draft 00](https://datatracker.ietf.org/doc/html/draft-wright-json-schema-00#section-4.2). Note that `integer` as a type is also supported and is defined as a JSON number without a fraction or exponent part. `null` is not supported as a type (see `nullable` for an alternative solution).  → R-0006 (normative-reference), R-0007 (defines), R-0008 (not-supported)

- (L33) The formats available to be used within an OTM files are:  → R-0009 (closed)

Table (L35–L45):

| Type | Comment | Line | Extracted as |
|---|---|---|---|
| `integer` | signed 32 bits | L37 | R-0010 (format) |
| `long` | signed 64 bits (a.k.a long) | L38 | R-0011 (format) |
| `float` |  | L39 | — |
| `double` |  | L40 | — |
| `string` |  | L41 | — |
| `richText` | Rich text fields are noted as supporting CommonMark markdown formatting. | L42 | R-0012 (format) |
| `boolean` |  | L43 | — |
| `date` | As defined by full-date - [RFC3339](https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14) | L44 | R-0013 (format) |
| `datetime` | As defined by date-time - [RFC3339](https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14) | L45 | R-0014 (format) |

*Extractor's note — README fields by type (from the field tables):*

- string (41): OTM object `otmVersion` (L55), Project object `name` (L80), Project object `id` (L92), Project object `owner` (L116), Project object `ownerContact` (L128), Representations object `name` (L208), Representations object `id` (L220), Representations object `type` (L232), Representation element for diagram `representation` (L395), Representation element for diagram `name` (L407), Representation element for diagram `id` (L419), Representation element for code `representation` (L493), Representation element for code `name` (L505), Representation element for code `id` (L517), Representation element for code `file` (L529), Representation element for threat-model `representation` (L623), Representation element for threat-model `name` (L635), Representation element for threat-model `id` (L647), Assets object `id` (L696), Assets object `name` (L708), Components object `name` (L921), Components object `id` (L933), Components object `type` (L945), TrustZones object `name` (L1114), TrustZones object `id` (L1126), TrustZones object `type` (L1138), Parent object `trustZone` (L1300), Parent object `component` (L1313), Dataflows object `name` (L1351), Dataflows object `id` (L1363), Dataflows object `source` (L1416), Dataflows object `destination` (L1428), Threats object `name` (L1516), Threats object `id` (L1528), Threat instance object `threat` (L1730), Threat instance object `state` (L1743), Mitigations object `name` (L1787), Mitigations object `id` (L1799), Mitigation instance object `mitigation` (L1884), Mitigation instance object `state` (L1896), Repository object `url` (L1931)
- richText (12): Project object `description` (L104), Representations object `description` (L243), Representation element for code `codeSnippet` (L553), Assets object `description` (L720), AssetRisk object `comment` (L837), Components object `description` (L971), TrustZones object `description` (L1150), Dataflows object `description` (L1375), Threats object `description` (L1540), ThreatRisk object `likelihoodComment` (L1669), ThreatRisk object `impactComment` (L1693), Mitigations object `description` (L1811)
- integer (12): Representation element for code `line` (L541), AssetRisk object `confidentiality` (L800), AssetRisk object `integrity` (L812), AssetRisk object `availability` (L824), TrustZoneRisk object `trustRating` (L1265), ThreatRisk object `likelihood` (L1657), ThreatRisk object `impact` (L1681), Mitigations object `riskReduction` (L1823), Size object `width` (L1964), Size object `height` (L1976), Position object `x` (L2001), Position object `y` (L2013)
- boolean (1): Dataflows object `bidirectional` (L1401)
- array of strings (9): Project object `tags` (L140), Asset Instance object `processed` (L864), Asset Instance object `stored` (L879), Components object `tags` (L957), Dataflows object `tags` (L1387), Dataflows object `assets` (L1440), Threats object `categories` (L1552), Threats object `cwes` (L1566), Threats object `tags` (L1588)
- Map [string, string] (8): Project object `attributes` (L155), Representations object `attributes` (L255), Assets object `attributes` (L740), Components object `attributes` (L1018), TrustZones object `attributes` (L1194), Dataflows object `attributes` (L1462), Threats object `attributes` (L1602), Mitigations object `attributes` (L1836)
- Map <string, string> (3): Representation element for diagram `attributes` (L447), Representation element for code `attributes` (L572), Representation element for threat-model `attributes` (L659)
- Asset instance object (1): Components object `assets` (L1002)
- AssetRisk object (1): Assets object `risk` (L732)
- Assets object (1): OTM object `assets` (L58)
- Components object (1): OTM object `components` (L59)
- DataFlows object (1): OTM object `dataflows` (L60)
- Mitigations object (1): OTM object `mitigations` (L63)
- Parent object (2): Components object `parent` (L983), TrustZones object `parent` (L1175)
- Position object (1): Representation element for diagram `position` (L431)
- Project object (1): OTM object `project` (L56)
- Repository object (1): Code `repository` (L334)
- Representations object (1): OTM object `representations` (L57)
- Size object (2): Diagram `size` (L308), Representation element for diagram `size` (L439)
- ThreatRisk object (1): Threats object `risk` (L1580)
- Threats object (1): OTM object `threats` (L62)
- TrustZoneRisk object (1): TrustZones object `risk` (L1167)
- TrustZones object (1): OTM object `trustZones` (L61)
- array of Mitigation instance object (1): Threat instance object `mitigations` (L1755)
- array of Representation Element object (2): Components object `representations` (L994), TrustZones object `representations` (L1186)
- array of Threat instance object (2): Components object `threats` (L1010), Dataflows object `threats` (L1454)
- long, float, double, date, datetime: no field.

## Schema (L47–L2030)

- (L49) [JSON Schema](otm_schema.json)

  *Extractor's note:* the link names `otm_schema.json`, rendered in its own section below. Every object section that follows has a field table (Field, Type, Description, Examples).

### OTM object (L51–L63)

Table (L53–L63):

| Field | Type | Description | Line | Extracted as |
|---|---|---|---|---|
| otmVersion | string | **REQUIRED** This field states the OTM version used in the current file. It is an important field in order to ensure backwards compatibility. | L55 | R-0015 (REQUIRED), R-0016 (format, inferred) |
| project | [Project object](#project-object) | **REQUIRED** The project node represents the entity within all the other elements are grouped. It's the unit of work. | L56 | R-0017 (REQUIRED) |
| representations | [Representations object](#representations-object) | Representations define different ways in which the project may be represented. Representation is an abstract concept and there might be several implementations. | L57 | — |
| assets | [Assets object](#assets-object) | Assets are the different kinds of sensible information that take part in our threat model. | L58 | — |
| components | [Components object](#components-object) | Components are the different pieces of software / hardware that make up our project. | L59 | — |
| dataflows | [DataFlows object](#dataflows-object) | Data flows are the elements that describe the movement of relevant information (assets) across our architecture. | L60 | — |
| trustZones | [TrustZones object](#trustzones-object) | Trust zones are the different areas within which components are located. They define how trustworthy an area is, based on how accessible it is: the more accessible, the less trustworthy. | L61 | — |
| threats | [Threats object](#threats-object) | Threats are the undesirable outcomes that can occur in our system and that we want to prevent. | L62 | — |
| mitigations | [Mitigations object](#mitigations-object) | Mitigations are the actions that we can take (or controls that we can put in place) in order to prevent a threat from taking place. | L63 | — |

Examples column:

- `otmVersion` (L55): `otmVersion: 0.1.0`

### Project object (L65–L181)

- (L67) The project node represents the entity within all the other elements are grouped. Its the unit of work.

Table (L69–L166):

| Field | Type | Description | Line | Extracted as |
|---|---|---|---|---|
| name | string | <b>REQUIRED</b> Name of the project | L81 | R-0018 (REQUIRED) |
| id | string | <b>REQUIRED</b> Unique identifier for the project. | L93 | R-0019 (REQUIRED), R-0020 (unique) |
| description | richText | Short description for the project. | L105 | — |
| owner | string | Name of the project's owner. This is the person responsible for the project. | L117 | — |
| ownerContact | string | Project's owner contact email. | L129 | — |
| tags | array of strings | Array of labels to tag the project | L142 | — |
| attributes | Map [string, string] | This is a free-form map of attributes that complete the information about the project. | L156 | — |

Examples column:

`name` (L84):

```yaml
name: Project name
```

`id` (L96):

```yaml
id: project-example-id
```

`description` (L108):

```yaml
description: This is the threat model for the app 'MuCustomApp123
```

`owner` (L120):

```yaml
owner: John Doe
```

`ownerContact` (L132):

```yaml
ownerContact: email@email.com
```

`tags` (L145–L147):

```yaml
tags:
    - microservice
    - spring
```

`attributes` (L159–L161):

```yaml
attributes:
    filePath: “file.xml”
    cmdbId: MyApp123
```

- **Example** (L171–L181), informative; pass-1 check: valid against `/properties/project`.

### Representations object (L183–L294)

- (L185) This node can define several ways on which the project can be represented.

- (L187) Representation is an abstract concept and there might be several implementations.

- (L189) These are the currently supported representation types:  → R-0021 (supported-values)
  - (L191) `diagram`
  - (L192) `code`
  - (L193) `threat-model`

- (L195) Each representation has these fields:

Table (L197–L268):

| Field | Type | Description | Line | Extracted as |
|---|---|---|---|---|
| name | string | <b>REQUIRED</b> Name for the representation. | L209 | R-0022 (REQUIRED) |
| id | string | <b>REQUIRED</b> Unique identifier for the representation. | L221 | R-0023 (REQUIRED), R-0024 (unique) |
| type | string | <b>REQUIRED</b> Type of representation. | L233 | R-0025 (REQUIRED) |
| description | richText | Short description of the representation content and usage. | L244 | — |
| attributes | Map [string, string] | This is a free-form list of attributes that complete the description of the representation. | L257 | — |

Examples column:

`name` (L212):

```yaml
name: Architecture diagram
```

`id` (L224):

```yaml
id: architecture-diagram-id
```

`type` (L236):

```yaml
type: diagram
```

`description` (L247):

```yaml
description: This is a diagram of the project's architecture
```

`attributes` (L260–L263):

```yaml
attributes:
    language: java
    platform: github
    vcs: git
```

- **Example** (L273–L294), informative; pass-1 check: valid against `/properties/representations`.

### Representation supported types (L296–L366)

- (L298) Depending on the type selected, some extra fields must be included in the representation. The supported representation types are:  → R-0026 (must)

#### Diagram (L300–L324)

- (L302) Represents a diagram with very basic information.

- (L304) Under the type “diagram“ we have the following extra fields:

Table (L306–L308):

| Field | Type | Description | Line | Extracted as |
|---|---|---|---|---|
| size | [Size object](#size-object) | **REQUIRED** Object that contains the information regarding the diagram size | L308 | R-0027 (REQUIRED) |

- **Example** (L312–L324), informative; pass-1 check: valid against `/properties/representations`; its attributes value `transparent: 40` is an integer in a Map [string, string] (D-07).

#### Code (L326–L348)

- (L328) Represents a repository of code.

- (L330) Under the type “code“ we have the following extra fields:

Table (L332–L334):

| Field | Type | Description | Line | Extracted as |
|---|---|---|---|---|
| repository | [Repository object](#repository-object) | Contains information about the Repository where the referenced code is located | L334 | — |

- **Example** (L338–L348), informative; pass-1 check: valid against `/properties/representations`.

#### Threat-Model (L350–L366)

- (L352) Represents a threat model.

- (L354) Under the type “threat-model“ we have no extra fields.

- **Example** (L358–L366), informative; pass-1 check: valid against `/properties/representations`.

### RepresentationElement object (L368–L681)

- (L370) The representation element stated how an element is represented with the available representations.

- (L372) In the current version we support three types of representation types as was mentioned here [OTM version 0.1.0 | Representations-object](#representations-object):
  - (L374) diagram
  - (L375) code
  - (L376) threat-model

- (L378) Therefore, there can be also three types of representation instances:

#### Representation element for diagram (L380–L476)

- (L382) Represents an element of a diagram.

Table (L384–L457):

| Field | Type | Description | Line | Extracted as |
|---|---|---|---|---|
| representation | string | <b>REQUIRED</b> Id of the representation on which this element is represented | L396 | R-0028 (REQUIRED), R-0029 (references, inferred) |
| name | string | Name for the representation element. | L408 | — |
| id | string | <b>REQUIRED</b> Unique identifier of the current representation instance | L420 | R-0030 (REQUIRED), R-0031 (unique) |
| position | <a href="#position-object">Position object</a> | <b>REQUIRED</b> This node contains all the information about the location of the element within the diagram. | L432 | R-0032 (REQUIRED) |
| size | <a href="#size-object">Size object</a> | <b>REQUIRED</b> This node contains all the information regarding the size of the shape. | L440 | R-0033 (REQUIRED) |
| attributes | Map &lt;string, string&gt; | This is a free-form map of attributes that complete the description of the representation. | L448 | — |

Examples column:

`representation` (L399):

```yaml
representation: architecture-diagram
```

`name` (L411):

```yaml
name: Component Box
```

`id` (L423):

```yaml
id: component-box-id
```

`attributes` (L451–L453):

```yaml
attributes:
  color: red
  shape: square
```

- **Example** (L462–L476), informative; pass-1 check: one element under `representations:` as a mapping, `with:` for width (L471), `attributes:` at column 0 (L473); the element fails `/definitions/representationElement` (size lacks width) (D-26).

#### Representation element for code (L478–L606)

- (L480) Despite all fields being optional, at least one of them is required.  → R-0034 (required)

Table (L482–L583):

| Field | Type | Description | Line | Extracted as |
|---|---|---|---|---|
| representation | string | <b>REQUIRED</b> Id of the representation on which this element is represented | L494 | R-0035 (REQUIRED), R-0036 (references, inferred) |
| name | string | Name for the representation element. | L506 | — |
| id | string | <b>REQUIRED</b> Unique identifier of the current representation instance | L518 | R-0037 (REQUIRED), R-0038 (unique) |
| file | string | File where the representative code is located | L530 | — |
| line | integer | Number of the code line that represents the element | L542 | — |
| codeSnippet | richText | Code that represents the element | L554 | — |
| attributes | Map &lt;string, string&gt; | This is a free-form list of attributes that complete the description of the representation. | L573 | — |

Examples column:

`representation` (L497):

```yaml
representation: code-repository
```

`name` (L509):

```yaml
name: Example Class
```

`id` (L521):

```yaml
id: org.example.class
```

`file` (L533):

```yaml
file: path/to/class.java
```

`line` (L545):

```yaml
line: 324
```

`codeSnippet` (L557–L564):

```yaml
codeSnippet: |
  public void createOTM(String[] args) {
    Scanner reader = new Scanner(System.in);
    System.out.print("Enter a number: ");

    int number = reader.nextInt()
    System.out.println("You entered: " + number);
}
```

`attributes` (L576–L578):

```yaml
attributes:
  source: sonar
  author: John Doe
```

- **Example** (L588–L606), informative; pass-1 check: the element is valid against `/definitions/representationElement`, but it sits under `representations:` as a mapping, not in an array (D-26).

#### Representation element for threat-model (L608–L681)

- (L610) Represents an element of a threat model.

Table (L612–L669):

| Field | Type | Description | Line | Extracted as |
|---|---|---|---|---|
| representation | string | <b>REQUIRED</b> Id of the representation on which this element is represented | L624 | R-0039 (REQUIRED), R-0040 (references, inferred) |
| name | string | Name for the representation element. | L636 | — |
| id | string | <b>REQUIRED</b> Unique identifier of the current representation instance | L648 | R-0041 (REQUIRED), R-0042 (unique) |
| attributes | Map &lt;string, string&gt; | This is a free-form list of attributes that complete the description of the representation. | L660 | — |

Examples column:

`representation` (L627):

```yaml
representation: architecture-threat-model
```

`name` (L639):

```yaml
name: Threat model representation
```

`id` (L651):

```yaml
id: threat-model-representation-id
```

`attributes` (L663–L664):

```yaml
attributes:
  author: John Doe
```

- **Example** (L674–L681), informative; pass-1 check: the element is valid against `/definitions/representationElement`, but it sits under `representations:` as a mapping, not in an array (D-26).

### Assets object (L683–L778)

- (L685) Assets are the different kinds of sensible information that take part in our threat model.

Table (L687–L751):

| Field | Type | Description | Line | Extracted as |
|---|---|---|---|---|
| id | string | <b>REQUIRED</b> Unique identifier for the asset | L697 | R-0043 (REQUIRED), R-0044 (unique) |
| name | string | <b>REQUIRED</b> Name for the defined assets | L709 | R-0045 (REQUIRED) |
| description | richText | Short description for the asset | L721 | — |
| risk | <a href="#assetrisk-object">AssetRisk object</a> | <b>REQUIRED</b> AssetRisk influences impact with regard to a threat. | L733 | R-0046 (REQUIRED) |
| attributes | Map [string, string] | This is a free-form map of attributes that complete the description of the asset. | L741 | — |

Examples column:

`id` (L700):

```yaml
id: cc-data
```

`name` (L712):

```yaml
name: Credit card data
```

`description` (L724):

```yaml
description: This is our customer’s credit card numbers
```

`attributes` (L744–L746):

```yaml
attributes:
  attr1: value1
  attr2: value2
```

- **Example** (L756–L778), informative; pass-1 check: valid against `/properties/assets`; the second asset's empty `attributes:` (L777) is null (D-03).

### AssetRisk object (L780–L846)

- (L782) AssetRisk influences impact with regard to a threat.

- (L784) Those values are passed through OTM into the IR rules engine which performs the calculation for inherent risk.

- (L786) More information - [https://support.iriusrisk.com/hc/en-us/articles/4412644787345-How-is-inherent-risk-calculated-](https://support.iriusrisk.com/hc/en-us/articles/4412644787345-How-is-inherent-risk-calculated-)

  *Extractor's note:* IR is IriusRisk; the sentence describes one consumer's processing and binds no producer.

Table (L789–L846):

| Field | Type | Description | Line | Extracted as |
|---|---|---|---|---|
| confidentiality | integer | <b>REQUIRED</b> From 0 to 100. How bad would it be to have an attacker see this information? | L801 | R-0047 (REQUIRED), R-0048 (range) |
| integrity | integer | <b>REQUIRED</b> From 0 to 100. How bad would it be to have an attacker modify this information? | L813 | R-0049 (REQUIRED), R-0050 (range) |
| availability | integer | <b>REQUIRED</b> From 0 to a 100. How bad would it be to lose this information or have it inaccessible in our system? | L825 | R-0051 (REQUIRED), R-0052 (range) |
| comment | richText | Short explanation on why we have selected the different risk values | L838 | — |

Examples column:

`confidentiality` (L804):

```yaml
confidentiality: 50
```

`integrity` (L816):

```yaml
integrity: 50
```

`availability` (L829):

```yaml
availability: 50
```

`comment` (L841):

```yaml
comment: We have decided that the values are a 100 for all values since this highly-sensitive information
```

### Asset Instance object (L848–L903)

- (L850) Object that describes the relationship between the component and the different assets.

Table (L852–L891):

| Field | Type | Description | Line | Extracted as |
|---|---|---|---|---|
| processed | array of strings | Array of ids that represent the assets that are processed in this component. | L865 | R-0053 (references, inferred) |
| stored | array of strings | Array of ids that represent the assets that are stored within the described component. | L880 | R-0054 (references, inferred) |

Examples column:

`processed` (L868–L871):

```yaml
assets:
  processed:
    - asset1
    - asset2
```

`stored` (L883–L886):

```yaml
assets:
  stored:
    - asset1
    - asset2
```

- **Example** (L896–L903), informative; pass-1 check: valid against `/definitions/assetInstance`.

### Components object (L905–L1097)

- (L907) Components are the different pieces of software / hardware that make our project. These are the fields for them:

Table (L909–L1029):

| Field | Type | Description | Line | Extracted as |
|---|---|---|---|---|
| name | string | <b>REQUIRED</b> Name for the defined component | L922 | R-0055 (REQUIRED) |
| id | string | <b>REQUIRED</b> Unique identifier for the component | L934 | R-0056 (REQUIRED), R-0057 (unique) |
| type | string | <b>REQUIRED</b> The kind of the described component | L946 | R-0058 (REQUIRED) |
| tags | array of strings | List of tags related to the component. | L958 | — |
| description | richText | Short description for the components | L972 | — |
| parent | <a href="#parent-object">Parent object</a> | <b>REQUIRED</b> Element in which this component is currently enclosed. It can be either a trust zone or another component. It should contain an attribute name stating the component type to avoid ambiguity. <br/>A component must have just <b>one parent</b>: another component or a trust zone. | L984–L986 | R-0059 (REQUIRED), R-0060 (should), R-0061 (must) |
| representations | array of <a href="#representations-object">Representation Element object</a> | Array of the representations that this component has. | L995 | — |
| assets | <a href="#asset-instance-object">Asset instance object</a> | Object that describes the relationship between the component and the different assets | L1003 | — |
| threats | array of <a href="#threat-instance-object">Threat instance object</a> | Array of threats that are related to the current component. | L1011 | — |
| attributes | Map [string, string] | This is a free-form map of attributes that complete the description of the component. | L1019 | — |

Examples column:

`name` (L925):

```yaml
name: Payments service
```

`id` (L937):

```yaml
id: payment-service
```

`type` (L949):

```yaml
type: ec2-instance
```

`tags` (L961–L963):

```yaml
tags:
  - web
  - server
```

`description` (L975):

```yaml
description: This is the server in charge of processing the payments in the platform
```

`attributes` (L1022–L1024):

```yaml
attributes:
  attr1: value1
  attr2: value2
```

- **Example** (L1033–L1097), informative; pass-1 check: invalid against `/properties/components`: attributes as a list of maps (L1065-L1067), `represetation` (L1077) (D-27).

### TrustZones object (L1099–L1248)

- (L1101) Trust zones are the different areas within which components are located. They define how trustworthy an area is, based on how accessible it is: the more accessible, the less trustworthy.

Table (L1103–L1205):

| Field | Type | Description | Line | Extracted as |
|---|---|---|---|---|
| name | string | <b>REQUIRED</b> Name for the defined trust zone | L1115 | R-0062 (REQUIRED) |
| id | string | <b>REQUIRED</b> Unique identifier for the trust zone | L1127 | R-0063 (REQUIRED), R-0064 (unique) |
| type | string | <b>RECOMMENDED (required in the next major version)</b> Type for the trust zone | L1139 | R-0065 (RECOMMENDED) |
| description | richText | Short description for the trust zone | L1151 | — |
| risk | <a href="#trustzonerisk-object">TrustZoneRisk object</a> | <b>REQUIRED</b> This is the object that describes the different aspects of risk associated with the trust zone | L1168 | R-0066 (REQUIRED) |
| parent | <a href="#parent-object">Parent object</a> | Unique identifier of the component or trust zone enclosing this trust zone. It should contain an attribute name stating the element type.<br /> A trust zone can have <b>zero or one parent</b>: another component or a trust zone. | L1177–L1178 | R-0067 (should), R-0068 (cardinality) |
| representations | array of <a href="#representationelement-object">Representation Element object</a> | Array of the representations that this trust zone has | L1187 | — |
| attributes | Map [string, string] | This is a free-form map of attributes that complete the description of the trust zone. | L1195 | — |

Examples column:

`name` (L1118):

```yaml
name: Internet
```

`id` (L1130):

```yaml
id: 730df42e-69a4-11ed-bd69-9b318e4f98c5
```

`type` (L1142):

```yaml
type: internet
```

`description` (L1154–L1159):

```yaml
description: >
  This is the world
  wide web accesible
  for every one with
  an internet
  connection
```

`attributes` (L1198–L1200):

```yaml
attributes:
  attr1: value1
  attr2: value2
```

- **Example** (L1210–L1248), informative; pass-1 check: `trustzones` (L1211) is not the field `trustZones`; under the intended key it fails at representations (a mapping) and parent (a string), with `postion` and `with` typos (D-25).

### TrustZoneRisk object (L1250–L1280)

- (L1252) This is the object that describes the different aspects of risk associated with the trust zone.

Table (L1254–L1273):

| Field | Type | Description | Line | Extracted as |
|---|---|---|---|---|
| trustRating | integer | <b>REQUIRED</b> From 0 and 100. How trustworthy is this trust zone? | L1266 | R-0069 (REQUIRED), R-0070 (range) |

Examples column:

`trustRating` (L1269):

```yaml
trustRating: 10
```

- **Example** (L1277–L1280), informative; pass-1 check: valid against `/properties/trustZones/items/properties/risk`.

### Parent object (L1282–L1334)

- (L1284) Element that encloses another element. It can be either a trust zone or a component. Currently, we have two supported types of parents:  → R-0071 (supported-values)
  - (L1286) trustZone
  - (L1287) component

Table (L1289–L1321):

| Field | Type | Description | Line | Extracted as |
|---|---|---|---|---|
| trustZone | string | Id of the element in which this component is currently enclosed. It can be either a trust zone or another component. It should contain an attribute name stating the component type to avoid ambiguity | L1302 | R-0072 (references, inferred), R-0073 (should) |
| component | string | Id of the element in which this component is currently enclosed. It can be either a trust zone or another component. It should contain an attribute name stating the component type to avoid ambiguity | L1314 | R-0074 (references, inferred), R-0075 (should) |

Examples column:

`trustZone` (L1305):

```yaml
trustZone: private
```

`component` (L1317):

```yaml
component: web-server
```

- **Example** (L1326–L1329), informative; pass-1 check: valid against `/definitions/parent`.

- **Example** (L1331–L1334), informative; pass-1 check: valid against `/definitions/parent`.

### Dataflows object (L1336–L1499)

- (L1338) Data flows are the elements that describe the movement of relevant information (assets) across our architecture.

Table (L1340–L1472):

| Field | Type | Description | Line | Extracted as |
|---|---|---|---|---|
| name | string | <b>REQUIRED</b> Name for the defined dataflow. | L1352 | R-0076 (REQUIRED) |
| id | string | <b>REQUIRED</b> Unique identifier for the dataflow. | L1364 | R-0077 (REQUIRED), R-0078 (unique) |
| description | richText | Short description of the dataflow content and usage. | L1376 | — |
| tags | array of strings | Array of tags related to the dataflow. | L1388 | — |
| bidirectional | boolean | States if the information flows both ways. By default, it is false. | L1402–L1404 | R-0079 (default) |
| source | string | <b>REQUIRED</b> Unique identifier for the source component of the dataflow. | L1417 | R-0080 (REQUIRED), R-0081 (references, inferred) |
| destination | string | <b>REQUIRED</b> Unique identifier for the destination component of the dataflow. | L1429 | R-0082 (REQUIRED), R-0083 (references, inferred) |
| assets | array of strings | Array of assets that are transported by the dataflow. | L1441 | R-0084 (references, inferred) |
| threats | array of <a href="#threat-instance-object">Threat instance object</a> | Array of threats that are related to the current dataflow. | L1455 | — |
| attributes | Map [string, string] | This is a free-form map of attributes that complete the description of the dataflow. | L1463 | — |

Examples column:

`name` (L1355):

```yaml
name: Credit card reporting
```

`id` (L1367):

```yaml
id: credit-card-reporting
```

`description` (L1379):

```yaml
description: Credit card information being exchanged in between the web app and the database
```

`tags` (L1391–L1393):

```yaml
tags:
  - http
  - https
```

`bidirectional` (L1408):

```yaml
bidirectional: true
```

`source` (L1420):

```yaml
source: web-service
```

`destination` (L1432):

```yaml
destination: psotgress-db
```

`assets` (L1444–L1446):

```yaml
assets:
  - cc-data
  - public-info
```

`attributes` (L1466–L1468):

```yaml
attributes:
  attr1: value1
  attr2: value2
```

- **Example** (L1477–L1499), informative; pass-1 check: invalid against `/properties/dataflows`: `target` (L1484) instead of the required `destination` (D-28).

### Threats object (L1501–L1640)

- (L1503) Threats are the undesirable outcomes that can occur in our system and that we want to prevent. These are its fields:

Table (L1505–L1613):

| Field | Type | Description | Line | Extracted as |
|---|---|---|---|---|
| name | string | <b>REQUIRED</b> This is the name for the threat | L1517 | R-0085 (REQUIRED) |
| id | string | <b>REQUIRED</b> Unique identifier for the threat | L1529 | R-0086 (REQUIRED), R-0087 (unique) |
| description | richText | Short description of the threat | L1541 | — |
| categories | array of strings | Array of categories that are applicable to the threat | L1553 | — |
| cwes | array of strings | Array of CWE identifiers of weaknesses associated with the threat | L1567 | R-0088 (references, inferred) |
| risk | <a href="#threatrisk-object">ThreatRisk object</a> | <b>REQUIRED</b> This object describes different aspects of risk (likelihood and impact) posed by the threat | L1581 | R-0089 (REQUIRED) |
| tags | array of strings | Array of tags related to the threat | L1589 | — |
| attributes | Map [string, string] | This is a free-form map of attributes that complete the description of the threat. | L1603 | — |

Examples column:

`name` (L1520):

```yaml
name: Attackers gain unauthorized access to the control of the environment
```

`id` (L1532):

```yaml
id: LOSS-CONTROL_ENV
```

`description` (L1544):

```yaml
description: Attackers could potentially gain unauthorized access to the control of the environment, due to user accounts - or role groups - not being well-defined and configured. As a consequence, attackers may be able to make changes without root approval.
```

`categories` (L1556–L1558):

```yaml
categories:
  - Spoofing
  - Authentication
```

`cwes` (L1570–L1572):

```yaml
cwes:
  - CWE-79
  - CWE-787
```

`tags` (L1592–L1594):

```yaml
tags:
  - unauthorized-access
  - loss-control
```

`attributes` (L1606–L1608):

```yaml
attributes:
  expirationDate: “2021-05-17”
  cmdbId: MyApp123
```

- **Example** (L1618–L1640), informative; pass-1 check: valid against `/properties/threats`; the unquoted `expirationDate: 2021-05-17` (L1635) is a YAML 1.1 timestamp (D-29).

### ThreatRisk object (L1642–L1713)

- (L1644) Risk information for the associated threat.

Table (L1646–L1702):

| Field | Type | Description | Line | Extracted as |
|---|---|---|---|---|
| likelihood | integer | <b>REQUIRED</b> From 0 to 100. How likely is it that this threat will take place? | L1658 | R-0090 (REQUIRED), R-0091 (range) |
| likelihoodComment | richText | Short explanation of why we have selected such a value for the likelihood | L1670 | — |
| impact | integer | <b>REQUIRED</b> From 0 to 100. How bad would it be if this threat took place? | L1682 | R-0092 (REQUIRED), R-0093 (range) |
| impactComment | richText | Short explanation of why we have selected such a value for the impact | L1694 | — |

Examples column:

`likelihood` (L1661):

```yaml
likelihood: 50
```

`likelihoodComment` (L1673):

```yaml
likelihoodComment: It is reasonable to think that this might happen, but it requires that the attacker has a deep knowledge of cryptography
```

`impact` (L1685):

```yaml
impact: 100
```

`impactComment` (L1697):

```yaml
impactComment: If this threat becomes a reality, the company will struggle to keep customers and the monetary loss would jeopardize the business
```

- **Example** (L1707–L1713), informative; pass-1 check: valid against `/properties/threats/items/properties/risk`.

### Threat instance object (L1715–L1770)

- (L1717) This object stores a reference to a threat and add additional data enclosed in a particular scope.

Table (L1719–L1759):

| Field | Type | Description | Line | Extracted as |
|---|---|---|---|---|
| threat | string | <b>REQUIRED</b> Unique identifier of the related threat. It should be one of the threats described in the root node threats. | L1731–L1732 | R-0094 (REQUIRED), R-0095 (should) |
| state | string | <b>REQUIRED</b> Describes the state in which the threat currently is. | L1744 | R-0096 (REQUIRED) |
| mitigations | array of <a href="#mitigation-instance-object">Mitigation instance object</a> | Array of mitigation that can prevent the threat from taking place. | L1756 | — |

Examples column:

`threat` (L1735):

```yaml
 threat: 22724267-be7e-44c0-8b1f-d7d33e9a34ec
```

`state` (L1747):

```yaml
state: mitigated
```

- **Example** (L1763–L1770), informative; pass-1 check: valid against `/properties/components/items/properties/threats`.

### Mitigations object (L1772–L1867)

- (L1774) Mitigations are the actions that we can take (or controls that we can put in place) in order to prevent a threat from taking place.

Table (L1776–L1848):

| Field | Type | Description | Line | Extracted as |
|---|---|---|---|---|
| name | string | <b>REQUIRED</b> Name for the mitigation | L1788 | R-0097 (REQUIRED) |
| id | string | <b>REQUIRED</b> Unique identifier for the mitigation | L1800 | R-0098 (REQUIRED), R-0099 (unique) |
| description | richText | Short descriptions of how to implement the mitigation | L1812 | — |
| riskReduction | integer | <b>REQUIRED</b> From 0 to 100. How much will the threat risk decrease once this mitigation is implemented? | L1824 | R-0100 (REQUIRED), R-0101 (range) |
| attributes | Map [string, string] | This is a free-form list of attributes that complete the description of the threat. | L1838 | — |

Examples column:

`name` (L1791):

```yaml
name: Use strong passwords
```

`id` (L1803):

```yaml
id: use-strong-passwords
```

`description` (L1815):

```yaml
description: Force users to use passwords over 10 characters, containing letters numbers and symbols
```

`riskReduction` (L1827):

```yaml
riskReduction: 75
```

`attributes` (L1841–L1843):

```yaml
attributes:
  standard: OWASP-ASVS
  cmdbId: MyApp123
```

- **Example** (L1853–L1867), informative; pass-1 check: valid against `/properties/mitigations`.

### Mitigation instance object (L1869–L1914)

- (L1871) Mitigation that can prevent the threat from taking place.

Table (L1873–L1905):

| Field | Type | Description | Line | Extracted as |
|---|---|---|---|---|
| mitigation | string | <b>REQUIRED</b> Unique identifier of the related mitigation. It should be declared in the root node mitigation. | L1885 | R-0102 (REQUIRED), R-0103 (should) |
| state | string | <b>REQUIRED</b> State of the mitigation | L1897 | R-0104 (REQUIRED) |

Examples column:

`mitigation` (L1888):

```yaml
mitigation: fd6136f4-e2ff-11eb-ba80-0242ac130004
```

`state` (L1900):

```yaml
state: implemented
```

- **Example** (L1910–L1914), informative; pass-1 check: valid against `/definitions/threat/properties/mitigations`.

### Repository object (L1916–L1947)

- (L1918) Contains information about the Repository where the referenced code is located.

Table (L1920–L1939):

| Field | Type | Description | Line | Extracted as |
|---|---|---|---|---|
| url | string | Connection URL of the described repository | L1932 | — |

Examples column:

`url` (L1935):

```yaml
https://github.com/my-project
```

- **Example** (L1944–L1947), informative; pass-1 check: valid against `/properties/representations/items/properties/repository`.

### Size object (L1949–L2030)

- (L1951) Represents a very basic information about a size of an element.

Table (L1953–L1984):

| Field | Type | Description | Line | Extracted as |
|---|---|---|---|---|
| width | integer | <b>REQUIRED</b> Width in pixels | L1965 | R-0105 (REQUIRED) |
| height | integer | <b>REQUIRED</b> Height in pixels | L1977 | R-0106 (REQUIRED) |

Examples column:

`width` (L1968):

```yaml
width: 400
```

`height` (L1980):

```yaml
height: 300
```

#### Position object (L1986–L2030)

- (L1988) Represents very basic information about the position of an element.

Table (L1990–L2021):

| Field | Type | Description | Line | Extracted as |
|---|---|---|---|---|
| x | integer | <b>REQUIRED</b> This is the position of the element in the X-axis in units | L2002 | R-0107 (REQUIRED) |
| y | integer | <b>REQUIRED</b> This is the position of the element in the Y-axis in units | L2014 | R-0108 (REQUIRED) |

Examples column:

`x` (L2005):

```yaml
x: 200
```

`y` (L2017):

```yaml
y: 100
```

- **Example** (L2026–L2030), informative; pass-1 check: valid against `/definitions/position`.

## Licence footer (L2032–L2034) — not under a heading in the source

- (L2033) This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>  → R-0109 (licence)

  *Extractor's note:* L2033 opens with the Creative Commons badge image link, not reproduced; the repository's `LICENSE` is the CC BY-SA 4.0 legal code. `otm_schema.json` states Apache-2.0 for itself (D-31).

## otm_schema.json — normative content (schema L1–L308)

Header members, verbatim:

- (schema L2) `"$schema": "http://json-schema.org/draft-07/schema#"`  → R-0110 (dialect)
- (schema L3) `"$id": "https://iriusrisk.com/schema/otm-0.2.0.schema.json"` — identifies the schema; constrains nothing
- (schema L4) `"title": "Open Threat Model Specification"` — a label; constrains nothing
- (schema L5) `"$comment" : "Open Threat Model JSON schema is published under the terms of the Apache License 2.0."`  → R-0111 (licence)

Keywords the schema uses: `type` (119), `required` (20 arrays, 46 names), `properties` (20), `items` (21), `$ref` (10), `oneOf` (1), `definitions` (1). Keywords it never uses: `enum`, `const`, `minimum`, `maximum`, `exclusiveMinimum`, `exclusiveMaximum`, `multipleOf`, `minLength`, `maxLength`, `pattern`, `format`, `minItems`, `maxItems`, `uniqueItems`, `contains`, `additionalProperties`, `patternProperties`, `propertyNames`, `dependencies`, `if`/`then`/`else`, `allOf`, `anyOf`, `not`, `default`.

*Extractor's note:* so the content model is open (an undeclared member validates at every level, D-30); no value has a vocabulary, a bound or a string format (D-18, D-19, D-06); no requirement depends on another value (D-10, D-11); nullability is a type array that includes "null" (D-03, D-09). Of the 119 `type` keywords 58 name one type and 61 are type arrays, every one with "null".

### `/` — OTM object, the document root (schema L1–L308)

- (L6) `"type": "object"`  → R-0112 (type)
- (L7) `"required": ["otmVersion", "project"]`  → otmVersion R-0113, project R-0114
- properties (L8):
  - `otmVersion` (L9): (L10) `"type": "string"`  → R-0115 (type)
  - `project` (L12): (L13) `"type": "object"`  → R-0116 (type); see `/properties/project`
  - `representations` (L30): (L31) `"type": ["array", "null"]`  → R-0127 (type-nullable); items (L33) `"type": "object"`  → R-0128 (type); items: see `/properties/representations/items`
  - `assets` (L52): (L53) `"type": ["array", "null"]`  → R-0141 (type-nullable); items (L55) `"type": "object"`  → R-0142 (type); items: see `/properties/assets/items`
  - `trustZones` (L75): (L76) `"type": "array"`  → R-0158 (type); items (L78) `"type": "object"`  → R-0159 (type); items: see `/properties/trustZones/items`
  - `components` (L101): (L102) `"type": ["array", "null"]`  → R-0174 (type-nullable); items (L104) `"type": "object"`  → R-0175 (type); items: see `/properties/components/items`
  - `dataflows` (L131): (L132) `"type": "array"`  → R-0193 (type); items (L134) `"type": "object"`  → R-0194 (type); items: see `/properties/dataflows/items`
  - `threats` (L161): (L162) `"type": ["array", "null"]`  → R-0212 (type-nullable); items (L164) `"type": "object"`  → R-0213 (type); items: see `/properties/threats/items`
  - `mitigations` (L198): (L199) `"type": ["array", "null"]`  → R-0234 (type-nullable); items (L201) `"type": "object"`  → R-0235 (type); items: see `/properties/mitigations/items`

### `/properties/project` — Project object (schema L12–L29)

- (L13) `"type": "object"`  → R-0116 (type)
- (L14) `"required": ["name", "id"]`  → name R-0117, id R-0118
- properties (L15):
  - `name` (L16): (L16) `"type": "string"`  → R-0119 (type)
  - `id` (L17): (L17) `"type": "string"`  → R-0120 (type)
  - `description` (L18): (L18) `"type": ["string", "null"]`  → R-0121 (type-nullable)
  - `owner` (L19): (L19) `"type": ["string", "null"]`  → R-0122 (type-nullable)
  - `ownerContact` (L20): (L20) `"type": ["string", "null"]`  → R-0123 (type-nullable)
  - `tags` (L21): (L22) `"type": ["array", "null"]`  → R-0124 (type-nullable); items (L24) `"type": "string"`  → R-0125 (type)
  - `attributes` (L27): (L27) `"type": ["object", "null"]`  → R-0126 (type-nullable)

### `/properties/representations/items` — Representations object (schema L32–L50)

- (L33) `"type": "object"`  → R-0128 (type)
- (L34) `"required": ["name", "id", "type"]`  → name R-0129, id R-0130, type R-0131
- properties (L35):
  - `name` (L36): (L36) `"type": "string"`  → R-0132 (type)
  - `id` (L37): (L37) `"type": "string"`  → R-0133 (type)
  - `type` (L38): (L38) `"type": "string"`  → R-0134 (type)
  - `description` (L39): (L39) `"type": ["string", "null"]`  → R-0135 (type-nullable)
  - `size` (L40): (L40) `"$ref": "#/definitions/size"`  → R-0136 (ref)
  - `repository` (L41): (L42) `"type": ["object", "null"]`  → R-0137 (type-nullable); see `/properties/representations/items/properties/repository`
  - `attributes` (L48): (L48) `"type": ["object", "null"]`  → R-0140 (type-nullable)

### `/properties/representations/items/properties/repository` — Repository object (schema L41–L47)

- (L42) `"type": ["object", "null"]`  → R-0137 (type-nullable)
- (L43) `"required": ["url"]`  → url R-0138
- properties (L44):
  - `url` (L45): (L45) `"type": ["string", "null"]`  → R-0139 (type-nullable)

### `/properties/assets/items` — Assets object (schema L54–L73)

- (L55) `"type": "object"`  → R-0142 (type)
- (L56) `"required": ["name", "id", "risk"]`  → name R-0143, id R-0144, risk R-0145
- properties (L57):
  - `name` (L58): (L58) `"type": "string"`  → R-0146 (type)
  - `id` (L59): (L59) `"type": "string"`  → R-0147 (type)
  - `description` (L60): (L60) `"type": ["string", "null"]`  → R-0148 (type-nullable)
  - `risk` (L61): (L62) `"type": "object"`  → R-0149 (type); see `/properties/assets/items/properties/risk`
  - `attributes` (L71): (L71) `"type": ["object", "null"]`  → R-0157 (type-nullable)

### `/properties/assets/items/properties/risk` — AssetRisk object (schema L61–L70)

- (L62) `"type": "object"`  → R-0149 (type)
- (L63) `"required": ["confidentiality", "integrity", "availability"]`  → confidentiality R-0150, integrity R-0151, availability R-0152
- properties (L64):
  - `confidentiality` (L65): (L65) `"type": "number"`  → R-0153 (type)
  - `integrity` (L66): (L66) `"type": "number"`  → R-0154 (type)
  - `availability` (L67): (L67) `"type": "number"`  → R-0155 (type)
  - `comment` (L68): (L68) `"type": ["string", "null"]`  → R-0156 (type-nullable)

### `/properties/trustZones/items` — TrustZones object (schema L77–L99)

- (L78) `"type": "object"`  → R-0159 (type)
- (L79) `"required": ["id", "name", "risk"]`  → id R-0160, name R-0161, risk R-0162
- properties (L80):
  - `id` (L81): (L81) `"type": "string"`  → R-0163 (type)
  - `name` (L82): (L82) `"type": "string"`  → R-0164 (type)
  - `type` (L83): (L83) `"type": "string"`  → R-0165 (type)
  - `description` (L84): (L84) `"type": ["string", "null"]`  → R-0166 (type-nullable)
  - `risk` (L85): (L86) `"type": "object"`  → R-0167 (type); see `/properties/trustZones/items/properties/risk`
  - `parent` (L92): (L92) `"$ref": "#/definitions/parent"`  → R-0170 (ref)
  - `representations` (L93): (L94) `"type": ["array", "null"]`  → R-0171 (type-nullable); items (L95) `"$ref": "#/definitions/representationElement"`  → R-0172 (ref)
  - `attributes` (L97): (L97) `"type": ["object", "null"]`  → R-0173 (type-nullable)

### `/properties/trustZones/items/properties/risk` — TrustZoneRisk object (schema L85–L91)

- (L86) `"type": "object"`  → R-0167 (type)
- (L87) `"required": ["trustRating"]`  → trustRating R-0168
- properties (L88):
  - `trustRating` (L89): (L89) `"type": "number"`  → R-0169 (type)

### `/properties/components/items` — Components object (schema L103–L129)

- (L104) `"type": "object"`  → R-0175 (type)
- (L105) `"required": ["id", "name", "type", "parent"]`  → id R-0176, name R-0177, type R-0178, parent R-0179
- properties (L106):
  - `id` (L107): (L107) `"type": "string"`  → R-0180 (type)
  - `name` (L108): (L108) `"type": "string"`  → R-0181 (type)
  - `type` (L109): (L109) `"type": "string"`  → R-0182 (type)
  - `description` (L110): (L110) `"type": ["string", "null"]`  → R-0183 (type-nullable)
  - `parent` (L111): (L111) `"$ref": "#/definitions/parent"`  → R-0184 (ref)
  - `representations` (L112): (L113) `"type": ["array", "null"]`  → R-0185 (type-nullable); items (L114) `"$ref": "#/definitions/representationElement"`  → R-0186 (ref)
  - `assets` (L116): (L116) `"$ref": "#/definitions/assetInstance"`  → R-0187 (ref)
  - `threats` (L117): (L118) `"type": ["array", "null"]`  → R-0188 (type-nullable); items (L119) `"$ref": "#/definitions/threat"`  → R-0189 (ref)
  - `tags` (L121): (L122) `"type": ["array", "null"]`  → R-0190 (type-nullable); items (L124) `"type": ["string", "null"]`  → R-0191 (type-nullable)
  - `attributes` (L127): (L127) `"type": ["object", "null"]`  → R-0192 (type-nullable)

### `/properties/dataflows/items` — Dataflows object (schema L133–L159)

- (L134) `"type": "object"`  → R-0194 (type)
- (L135) `"required": ["id", "name", "source", "destination"]`  → id R-0195, name R-0196, source R-0197, destination R-0198
- properties (L136):
  - `id` (L137): (L137) `"type": "string"`  → R-0199 (type)
  - `name` (L138): (L138) `"type": "string"`  → R-0200 (type)
  - `description` (L139): (L139) `"type": ["string", "null"]`  → R-0201 (type-nullable)
  - `bidirectional` (L140): (L140) `"type": ["boolean", "null"]`  → R-0202 (type-nullable)
  - `source` (L141): (L141) `"type": "string"`  → R-0203 (type)
  - `destination` (L142): (L142) `"type": "string"`  → R-0204 (type)
  - `assets` (L143): (L144) `"type": ["array", "null"]`  → R-0205 (type-nullable); items (L145) `"type": ["string", "null"]`  → R-0206 (type-nullable)
  - `threats` (L147): (L148) `"type": ["array", "null"]`  → R-0207 (type-nullable); items (L149) `"$ref": "#/definitions/threat"`  → R-0208 (ref)
  - `tags` (L151): (L152) `"type": ["array", "null"]`  → R-0209 (type-nullable); items (L154) `"type": ["string", "null"]`  → R-0210 (type-nullable)
  - `attributes` (L157): (L157) `"type": ["object", "null"]`  → R-0211 (type-nullable)

### `/properties/threats/items` — Threats object (schema L163–L196)

- (L164) `"type": "object"`  → R-0213 (type)
- (L165) `"required": ["id", "name", "risk"]`  → id R-0214, name R-0215, risk R-0216
- properties (L166):
  - `id` (L167): (L167) `"type": "string"`  → R-0217 (type)
  - `name` (L168): (L168) `"type": "string"`  → R-0218 (type)
  - `description` (L169): (L169) `"type": ["string", "null"]`  → R-0219 (type-nullable)
  - `categories` (L170): (L171) `"type": ["array", "null"]`  → R-0220 (type-nullable); items (L172) `"type": ["string", "null"]`  → R-0221 (type-nullable)
  - `cwes` (L174): (L175) `"type": ["array", "null"]`  → R-0222 (type-nullable); items (L176) `"type": ["string", "null"]`  → R-0223 (type-nullable)
  - `risk` (L178): (L179) `"type": "object"`  → R-0224 (type); see `/properties/threats/items/properties/risk`
  - `tags` (L188): (L189) `"type": ["array", "null"]`  → R-0231 (type-nullable); items (L191) `"type": ["string", "null"]`  → R-0232 (type-nullable)
  - `attributes` (L194): (L194) `"type": ["object", "null"]`  → R-0233 (type-nullable)

### `/properties/threats/items/properties/risk` — ThreatRisk object (schema L178–L187)

- (L179) `"type": "object"`  → R-0224 (type)
- (L180) `"required": ["likelihood", "impact"]`  → likelihood R-0225, impact R-0226
- properties (L181):
  - `likelihood` (L182): (L182) `"type": ["number", "null"]`  → R-0227 (type-nullable)
  - `likelihoodComment` (L183): (L183) `"type": ["string", "null"]`  → R-0228 (type-nullable)
  - `impact` (L184): (L184) `"type": "number"`  → R-0229 (type)
  - `impactComment` (L185): (L185) `"type": "string"`  → R-0230 (type)

### `/properties/mitigations/items` — Mitigations object (schema L200–L210)

- (L201) `"type": "object"`  → R-0235 (type)
- (L202) `"required": ["id", "name", "riskReduction"]`  → id R-0236, name R-0237, riskReduction R-0238
- properties (L203):
  - `id` (L204): (L204) `"type": "string"`  → R-0239 (type)
  - `name` (L205): (L205) `"type": "string"`  → R-0240 (type)
  - `description` (L206): (L206) `"type": ["string", "null"]`  → R-0241 (type-nullable)
  - `riskReduction` (L207): (L207) `"type": "number"`  → R-0242 (type)
  - `attributes` (L208): (L208) `"type": ["object", "null"]`  → R-0243 (type-nullable)

### `/definitions/size` — Size object (schema L214–L221)

- (L215) `"type": ["object", "null"]`  → R-0244 (type-nullable)
- (L216) `"required": ["width", "height"]`  → width R-0245, height R-0246
- properties (L217):
  - `width` (L218): (L218) `"type": "number"`  → R-0247 (type)
  - `height` (L219): (L219) `"type": "number"`  → R-0248 (type)

### `/definitions/parent` — Parent object (schema L222–L232)

- (L223) `"type": "object"`  → R-0249 (type)
- (L224) `"oneOf": [ {"required": ["trustZone"]}, {"required":["component"]} ]`  → R-0250 (one-of)
  - branch 1: (L225) `"required": ["trustZone"]`  → trustZone R-0251
  - branch 2: (L226) `"required":["component"]`  → component R-0252
- properties (L228):
  - `trustZone` (L229): (L229) `"type": "string"`  → R-0253 (type)
  - `component` (L230): (L230) `"type": "string"`  → R-0254 (type)

### `/definitions/position` — Position object (schema L233–L240)

- (L234) `"type": ["object", "null"]`  → R-0255 (type-nullable)
- (L235) `"required": ["x", "y"]`  → x R-0256, y R-0257
- properties (L236):
  - `x` (L237): (L237) `"type": "number"`  → R-0258 (type)
  - `y` (L238): (L238) `"type": "number"`  → R-0259 (type)

### `/definitions/representationElement` — RepresentationElement object (schema L241–L255)

- (L242) `"type": "object"`  → R-0260 (type)
- (L243) `"required": ["representation", "id"]`  → representation R-0261, id R-0262
- properties (L244):
  - `representation` (L245): (L245) `"type": "string"`  → R-0263 (type)
  - `name` (L246): (L246) `"type": ["string", "null"]`  → R-0264 (type-nullable)
  - `id` (L247): (L247) `"type": "string"`  → R-0265 (type)
  - `position` (L248): (L248) `"$ref": "#/definitions/position"`  → R-0266 (ref)
  - `size` (L249): (L249) `"$ref": "#/definitions/size"`  → R-0267 (ref)
  - `file` (L250): (L250) `"type": ["string", "null"]`  → R-0268 (type-nullable)
  - `line` (L251): (L251) `"type": ["number", "null"]`  → R-0269 (type-nullable)
  - `codeSnippet` (L252): (L252) `"type": ["string", "null"]`  → R-0270 (type-nullable)
  - `attributes` (L253): (L253) `"type": ["object", "null"]`  → R-0271 (type-nullable)

### `/definitions/threat` — Threat instance object (schema L256–L274)

- (L257) `"type": "object"`  → R-0272 (type)
- (L258) `"required": ["threat", "state"]`  → threat R-0273, state R-0274
- properties (L259):
  - `threat` (L260): (L260) `"type": "string"`  → R-0275 (type)
  - `state` (L261): (L261) `"type": "string"`  → R-0276 (type)
  - `mitigations` (L262): (L263) `"type": "array"`  → R-0277 (type); items (L265) `"type": ["object", "null"]`  → R-0278 (type-nullable); items: see `/definitions/threat/properties/mitigations/items`

### `/definitions/threat/properties/mitigations/items` — Mitigation instance object (schema L264–L271)

- (L265) `"type": ["object", "null"]`  → R-0278 (type-nullable)
- (L266) `"required": ["mitigation", "state"]`  → mitigation R-0279, state R-0280
- properties (L267):
  - `mitigation` (L268): (L268) `"type": ["string", "null"]`  → R-0281 (type-nullable)
  - `state` (L269): (L269) `"type": ["string", "null"]`  → R-0282 (type-nullable)

### `/definitions/assetInstance` — Asset Instance object (schema L275–L306)

- (L276) `"type": [ "object", "null" ]`  → R-0283 (type-nullable)
- properties (L280):
  - `processed` (L281): (L282) `"type": [ "array", "null" ]`  → R-0284 (type-nullable); items (L287) `"type": [ "string", "null" ]`  → R-0285 (type-nullable)
  - `stored` (L293): (L294) `"type": [ "array", "null" ]`  → R-0286 (type-nullable); items (L299) `"type": [ "string", "null" ]`  → R-0287 (type-nullable)

## README ↔ schema, field by field (extractor's comparison)

One table per README field table. *README* gives the Type cell and the keyword that opens the Description cell; *schema* gives the property's `type` (one `$ref` followed, array items after *of*) and whether the container's `required` lists it. Every schema property has a README row and every README row a schema property; the disagreements are the defects cited.

### OTM object (README L53–L63; schema `/`, required at schema L7)

| Field | README type | README keyword | schema type | schema required | agreement |
|---|---|---|---|---|---|
| otmVersion | string (L55) | REQUIRED (L55) | `"string"` (L10) | yes | agree |
| project | Project object (L56) | REQUIRED (L56) | `"object"` (L13) | yes | agree |
| representations | Representations object (L57) | — | `["array", "null"] of "object"` (L31) | — | README object, schema array (D-08); schema admits null (D-03) |
| assets | Assets object (L58) | — | `["array", "null"] of "object"` (L53) | — | README object, schema array (D-08); schema admits null (D-03) |
| components | Components object (L59) | — | `["array", "null"] of "object"` (L102) | — | README object, schema array (D-08); schema admits null (D-03) |
| dataflows | DataFlows object (L60) | — | `"array" of "object"` (L132) | — | README object, schema array (D-08) |
| trustZones | TrustZones object (L61) | — | `"array" of "object"` (L76) | — | README object, schema array (D-08) |
| threats | Threats object (L62) | — | `["array", "null"] of "object"` (L162) | — | README object, schema array (D-08); schema admits null (D-03) |
| mitigations | Mitigations object (L63) | — | `["array", "null"] of "object"` (L199) | — | README object, schema array (D-08); schema admits null (D-03) |

### Project object (README L69–L166; schema `/properties/project`, required at schema L14)

| Field | README type | README keyword | schema type | schema required | agreement |
|---|---|---|---|---|---|
| name | string (L80) | REQUIRED (L81) | `"string"` (L16) | yes | agree |
| id | string (L92) | REQUIRED (L93) | `"string"` (L17) | yes | agree |
| description | richText (L104) | — | `["string", "null"]` (L18) | — | schema admits null (D-03) |
| owner | string (L116) | — | `["string", "null"]` (L19) | — | schema admits null (D-03) |
| ownerContact | string (L128) | — | `["string", "null"]` (L20) | — | schema admits null (D-03) |
| tags | array of strings (L140) | — | `["array", "null"] of "string"` (L22) | — | schema admits null (D-03) |
| attributes | Map [string, string] (L155) | — | `["object", "null"]` (L27) | — | Map vs object with any values (D-07); schema admits null (D-03) |

### Representations object (README L197–L268; schema `/properties/representations/items`, required at schema L34)

| Field | README type | README keyword | schema type | schema required | agreement |
|---|---|---|---|---|---|
| name | string (L208) | REQUIRED (L209) | `"string"` (L36) | yes | agree |
| id | string (L220) | REQUIRED (L221) | `"string"` (L37) | yes | agree |
| type | string (L232) | REQUIRED (L233) | `"string"` (L38) | yes | agree |
| description | richText (L243) | — | `["string", "null"]` (L39) | — | schema admits null (D-03) |
| attributes | Map [string, string] (L255) | — | `["object", "null"]` (L48) | — | Map vs object with any values (D-07); schema admits null (D-03) |

### Diagram (README L306–L308; schema `/properties/representations/items`, required at schema L34)

| Field | README type | README keyword | schema type | schema required | agreement |
|---|---|---|---|---|---|
| size | Size object (L308) | REQUIRED (L308) | `$ref size → ["object", "null"]` (L40) | — | README REQUIRED, schema optional (D-10); schema admits null (D-03) |

### Code (README L332–L334; schema `/properties/representations/items`, required at schema L34)

| Field | README type | README keyword | schema type | schema required | agreement |
|---|---|---|---|---|---|
| repository | Repository object (L334) | — | `["object", "null"]` (L42) | — | schema admits null (D-03) |

### Representation element for diagram (README L384–L457; schema `/definitions/representationElement`, required at schema L243)

| Field | README type | README keyword | schema type | schema required | agreement |
|---|---|---|---|---|---|
| representation | string (L395) | REQUIRED (L396) | `"string"` (L245) | yes | agree |
| name | string (L407) | — | `["string", "null"]` (L246) | — | schema admits null (D-03) |
| id | string (L419) | REQUIRED (L420) | `"string"` (L247) | yes | agree |
| position | Position object (L431) | REQUIRED (L432) | `$ref position → ["object", "null"]` (L248) | — | README REQUIRED, schema optional (D-11); schema admits null (D-03) |
| size | Size object (L439) | REQUIRED (L440) | `$ref size → ["object", "null"]` (L249) | — | README REQUIRED, schema optional (D-11); schema admits null (D-03) |
| attributes | Map <string, string> (L447) | — | `["object", "null"]` (L253) | — | Map vs object with any values (D-07); schema admits null (D-03) |

### Representation element for code (README L482–L583; schema `/definitions/representationElement`, required at schema L243)

| Field | README type | README keyword | schema type | schema required | agreement |
|---|---|---|---|---|---|
| representation | string (L493) | REQUIRED (L494) | `"string"` (L245) | yes | agree |
| name | string (L505) | — | `["string", "null"]` (L246) | — | schema admits null (D-03) |
| id | string (L517) | REQUIRED (L518) | `"string"` (L247) | yes | agree |
| file | string (L529) | — | `["string", "null"]` (L250) | — | schema admits null (D-03) |
| line | integer (L541) | — | `["number", "null"]` (L251) | — | integer vs number (D-05); schema admits null (D-03) |
| codeSnippet | richText (L553) | — | `["string", "null"]` (L252) | — | schema admits null (D-03) |
| attributes | Map <string, string> (L572) | — | `["object", "null"]` (L253) | — | Map vs object with any values (D-07); schema admits null (D-03) |

### Representation element for threat-model (README L612–L669; schema `/definitions/representationElement`, required at schema L243)

| Field | README type | README keyword | schema type | schema required | agreement |
|---|---|---|---|---|---|
| representation | string (L623) | REQUIRED (L624) | `"string"` (L245) | yes | agree |
| name | string (L635) | — | `["string", "null"]` (L246) | — | schema admits null (D-03) |
| id | string (L647) | REQUIRED (L648) | `"string"` (L247) | yes | agree |
| attributes | Map <string, string> (L659) | — | `["object", "null"]` (L253) | — | Map vs object with any values (D-07); schema admits null (D-03) |

### Assets object (README L687–L751; schema `/properties/assets/items`, required at schema L56)

| Field | README type | README keyword | schema type | schema required | agreement |
|---|---|---|---|---|---|
| id | string (L696) | REQUIRED (L697) | `"string"` (L59) | yes | agree |
| name | string (L708) | REQUIRED (L709) | `"string"` (L58) | yes | agree |
| description | richText (L720) | — | `["string", "null"]` (L60) | — | schema admits null (D-03) |
| risk | AssetRisk object (L732) | REQUIRED (L733) | `"object"` (L62) | yes | agree |
| attributes | Map [string, string] (L740) | — | `["object", "null"]` (L71) | — | Map vs object with any values (D-07); schema admits null (D-03) |

### AssetRisk object (README L789–L846; schema `/properties/assets/items/properties/risk`, required at schema L63)

| Field | README type | README keyword | schema type | schema required | agreement |
|---|---|---|---|---|---|
| confidentiality | integer (L800) | REQUIRED (L801) | `"number"` (L65) | yes | integer vs number (D-05) |
| integrity | integer (L812) | REQUIRED (L813) | `"number"` (L66) | yes | integer vs number (D-05) |
| availability | integer (L824) | REQUIRED (L825) | `"number"` (L67) | yes | integer vs number (D-05) |
| comment | richText (L837) | — | `["string", "null"]` (L68) | — | schema admits null (D-03) |

### Asset Instance object (README L852–L891; schema `/definitions/assetInstance`, no required list)

| Field | README type | README keyword | schema type | schema required | agreement |
|---|---|---|---|---|---|
| processed | array of strings (L864) | — | `["array", "null"] of ["string", "null"]` (L282) | — | schema admits null (D-03) |
| stored | array of strings (L879) | — | `["array", "null"] of ["string", "null"]` (L294) | — | schema admits null (D-03) |

### Components object (README L909–L1029; schema `/properties/components/items`, required at schema L105)

| Field | README type | README keyword | schema type | schema required | agreement |
|---|---|---|---|---|---|
| name | string (L921) | REQUIRED (L922) | `"string"` (L108) | yes | agree |
| id | string (L933) | REQUIRED (L934) | `"string"` (L107) | yes | agree |
| type | string (L945) | REQUIRED (L946) | `"string"` (L109) | yes | agree |
| tags | array of strings (L957) | — | `["array", "null"] of ["string", "null"]` (L122) | — | schema admits null (D-03) |
| description | richText (L971) | — | `["string", "null"]` (L110) | — | schema admits null (D-03) |
| parent | Parent object (L983) | REQUIRED (L984) | `$ref parent → "object"` (L111) | yes | agree |
| representations | array of Representation Element object (L994) | — | `["array", "null"] of $ref representationElement` (L113) | — | schema admits null (D-03); README link targets the wrong section (D-22) |
| assets | Asset instance object (L1002) | — | `$ref assetInstance → ["object", "null"]` (L116) | — | schema admits null (D-03) |
| threats | array of Threat instance object (L1010) | — | `["array", "null"] of $ref threat` (L118) | — | schema admits null (D-03) |
| attributes | Map [string, string] (L1018) | — | `["object", "null"]` (L127) | — | Map vs object with any values (D-07); schema admits null (D-03) |

### TrustZones object (README L1103–L1205; schema `/properties/trustZones/items`, required at schema L79)

| Field | README type | README keyword | schema type | schema required | agreement |
|---|---|---|---|---|---|
| name | string (L1114) | REQUIRED (L1115) | `"string"` (L82) | yes | agree |
| id | string (L1126) | REQUIRED (L1127) | `"string"` (L81) | yes | agree |
| type | string (L1138) | RECOMMENDED (L1139) | `"string"` (L83) | — | RECOMMENDED vs optional: consistent |
| description | richText (L1150) | — | `["string", "null"]` (L84) | — | schema admits null (D-03) |
| risk | TrustZoneRisk object (L1167) | REQUIRED (L1168) | `"object"` (L86) | yes | agree |
| parent | Parent object (L1175) | — | `$ref parent → "object"` (L92) | — | described as an identifier (D-14) |
| representations | array of Representation Element object (L1186) | — | `["array", "null"] of $ref representationElement` (L94) | — | schema admits null (D-03) |
| attributes | Map [string, string] (L1194) | — | `["object", "null"]` (L97) | — | Map vs object with any values (D-07); schema admits null (D-03) |

### TrustZoneRisk object (README L1254–L1273; schema `/properties/trustZones/items/properties/risk`, required at schema L87)

| Field | README type | README keyword | schema type | schema required | agreement |
|---|---|---|---|---|---|
| trustRating | integer (L1265) | REQUIRED (L1266) | `"number"` (L89) | yes | integer vs number (D-05) |

### Parent object (README L1289–L1321; schema `/definitions/parent`, no required list; the oneOf at schema L224 requires exactly one of trustZone, component)

| Field | README type | README keyword | schema type | schema required | agreement |
|---|---|---|---|---|---|
| trustZone | string (L1300) | — | `"string"` (L229) | — | agree |
| component | string (L1313) | — | `"string"` (L230) | — | agree |

### Dataflows object (README L1340–L1472; schema `/properties/dataflows/items`, required at schema L135)

| Field | README type | README keyword | schema type | schema required | agreement |
|---|---|---|---|---|---|
| name | string (L1351) | REQUIRED (L1352) | `"string"` (L138) | yes | agree |
| id | string (L1363) | REQUIRED (L1364) | `"string"` (L137) | yes | agree |
| description | richText (L1375) | — | `["string", "null"]` (L139) | — | schema admits null (D-03) |
| tags | array of strings (L1387) | — | `["array", "null"] of ["string", "null"]` (L152) | — | schema admits null (D-03) |
| bidirectional | boolean (L1401) | — | `["boolean", "null"]` (L140) | — | schema admits null (D-03) |
| source | string (L1416) | REQUIRED (L1417) | `"string"` (L141) | yes | agree |
| destination | string (L1428) | REQUIRED (L1429) | `"string"` (L142) | yes | agree |
| assets | array of strings (L1440) | — | `["array", "null"] of ["string", "null"]` (L144) | — | schema admits null (D-03) |
| threats | array of Threat instance object (L1454) | — | `["array", "null"] of $ref threat` (L148) | — | schema admits null (D-03) |
| attributes | Map [string, string] (L1462) | — | `["object", "null"]` (L157) | — | Map vs object with any values (D-07); schema admits null (D-03) |

### Threats object (README L1505–L1613; schema `/properties/threats/items`, required at schema L165)

| Field | README type | README keyword | schema type | schema required | agreement |
|---|---|---|---|---|---|
| name | string (L1516) | REQUIRED (L1517) | `"string"` (L168) | yes | agree |
| id | string (L1528) | REQUIRED (L1529) | `"string"` (L167) | yes | agree |
| description | richText (L1540) | — | `["string", "null"]` (L169) | — | schema admits null (D-03) |
| categories | array of strings (L1552) | — | `["array", "null"] of ["string", "null"]` (L171) | — | schema admits null (D-03) |
| cwes | array of strings (L1566) | — | `["array", "null"] of ["string", "null"]` (L175) | — | schema admits null (D-03) |
| risk | ThreatRisk object (L1580) | REQUIRED (L1581) | `"object"` (L179) | yes | agree |
| tags | array of strings (L1588) | — | `["array", "null"] of ["string", "null"]` (L189) | — | schema admits null (D-03) |
| attributes | Map [string, string] (L1602) | — | `["object", "null"]` (L194) | — | Map vs object with any values (D-07); schema admits null (D-03) |

### ThreatRisk object (README L1646–L1702; schema `/properties/threats/items/properties/risk`, required at schema L180)

| Field | README type | README keyword | schema type | schema required | agreement |
|---|---|---|---|---|---|
| likelihood | integer (L1657) | REQUIRED (L1658) | `["number", "null"]` (L182) | yes | integer vs number (D-05); schema admits null (D-03) |
| likelihoodComment | richText (L1669) | — | `["string", "null"]` (L183) | — | schema admits null (D-03) |
| impact | integer (L1681) | REQUIRED (L1682) | `"number"` (L184) | yes | integer vs number (D-05) |
| impactComment | richText (L1693) | — | `"string"` (L185) | — | agree |

### Threat instance object (README L1719–L1759; schema `/definitions/threat`, required at schema L258)

| Field | README type | README keyword | schema type | schema required | agreement |
|---|---|---|---|---|---|
| threat | string (L1730) | REQUIRED (L1731) | `"string"` (L260) | yes | agree |
| state | string (L1743) | REQUIRED (L1744) | `"string"` (L261) | yes | agree |
| mitigations | array of Mitigation instance object (L1755) | — | `"array" of ["object", "null"]` (L263) | — | schema admits null (D-03) |

### Mitigations object (README L1776–L1848; schema `/properties/mitigations/items`, required at schema L202)

| Field | README type | README keyword | schema type | schema required | agreement |
|---|---|---|---|---|---|
| name | string (L1787) | REQUIRED (L1788) | `"string"` (L205) | yes | agree |
| id | string (L1799) | REQUIRED (L1800) | `"string"` (L204) | yes | agree |
| description | richText (L1811) | — | `["string", "null"]` (L206) | — | schema admits null (D-03) |
| riskReduction | integer (L1823) | REQUIRED (L1824) | `"number"` (L207) | yes | integer vs number (D-05) |
| attributes | Map [string, string] (L1836) | — | `["object", "null"]` (L208) | — | Map vs object with any values (D-07); schema admits null (D-03) |

### Mitigation instance object (README L1873–L1905; schema `/definitions/threat/properties/mitigations/items`, required at schema L266)

| Field | README type | README keyword | schema type | schema required | agreement |
|---|---|---|---|---|---|
| mitigation | string (L1884) | REQUIRED (L1885) | `["string", "null"]` (L268) | yes | schema admits null (D-03) |
| state | string (L1896) | REQUIRED (L1897) | `["string", "null"]` (L269) | yes | schema admits null (D-03) |

### Repository object (README L1920–L1939; schema `/properties/representations/items/properties/repository`, required at schema L43)

| Field | README type | README keyword | schema type | schema required | agreement |
|---|---|---|---|---|---|
| url | string (L1931) | — | `["string", "null"]` (L45) | yes | schema requires it, README does not (D-12); schema admits null (D-03) |

### Size object (README L1953–L1984; schema `/definitions/size`, required at schema L216)

| Field | README type | README keyword | schema type | schema required | agreement |
|---|---|---|---|---|---|
| width | integer (L1964) | REQUIRED (L1965) | `"number"` (L218) | yes | integer vs number (D-05) |
| height | integer (L1976) | REQUIRED (L1977) | `"number"` (L219) | yes | integer vs number (D-05) |

### Position object (README L1990–L2021; schema `/definitions/position`, required at schema L235)

| Field | README type | README keyword | schema type | schema required | agreement |
|---|---|---|---|---|---|
| x | integer (L2001) | REQUIRED (L2002) | `"number"` (L237) | yes | integer vs number (D-05) |
| y | integer (L2013) | REQUIRED (L2014) | `"number"` (L238) | yes | integer vs number (D-05) |

## Extractor notes — source inconsistencies (not source text)

Recorded while extracting, not corrected. The schema governs validation; the README governs meaning. Also in `requirements.yaml` › `source_defects`, with the same numbers.

1. **D-01** (reference-mismatch; README.md L31; otm_schema.json L2) Data Types bases OTM's primitive types on the 'JSON Schema Specification Wright Draft 00' (draft-wright-json-schema-00, section 4.2; L31); the schema that ships with the specification declares JSON Schema draft-07 ("$schema": "http://json-schema.org/draft-07/schema#", L2). Validation semantics are draft-07's.
2. **D-02** (stale-version; README.md L18 L55 L372; otm_schema.json L3) The current version is 0.2.0 (README L18; schema $id otm-0.2.0, L3; EXAMPLE.yaml L1 otmVersion: 0.2.0), but the OTM object table's Examples cell gives otmVersion: 0.1.0 (L55) and the RepresentationElement section links '[OTM version 0.1.0 | Representations-object]' (L372).
3. **D-03** (null-contradiction; README.md L31 L777 L1247; otm_schema.json L45 L182 L265 L268 L269 and 56 others) README: '`null` is not supported as a type' (L31). The schema admits null at 61 of its 119 type keywords (every type array includes "null"): optional fields, the array items of tags, categories, cwes, assets, processed and stored, the mitigation-instance items (L265), and four required fields: repository url (L45), threat risk likelihood (L182), mitigation instance mitigation and state (L268, L269). The README's own examples leave attributes empty (L777, L1247), which YAML reads as null.
4. **D-04** (undefined-term; README.md L27 L31) L31 points to '`nullable` for an alternative solution', but neither the README nor the schema defines nullable. (Extractor's note: it is the OpenAPI 3.0 Schema Object field behind L27's OpenAPI reference; the OTM schema expresses nullability with draft-07 type arrays instead.)
5. **D-05** (type-mismatch; README.md L31 L37 L541 L800 L812 L824 L1265 L1657 L1681 L1823 L1964 L1976 L2001 L2013; otm_schema.json L65-L67 L89 L182 L184 L207 L218 L219 L237 L238 L251) Twelve fields are typed integer in the README (line, confidentiality, integrity, availability, trustRating, likelihood, impact, riskReduction, width, height, x, y) and number in the schema. The schema accepts 50.5, which the README's integer (a JSON number without a fraction or exponent part, L31; signed 32 bits, L37) excludes.
6. **D-06** (bounds-not-encoded; README.md L37 L801 L813 L825 L1266 L1658 L1682 L1824; otm_schema.json L65-L67 L89 L182 L184 L207) Seven fields carry 'From 0 to 100' (or 'From 0 to a 100', 'From 0 and 100'): confidentiality, integrity, availability, trustRating, likelihood, impact, riskReduction. The schema declares no minimum or maximum anywhere, nor the signed 32-bit range of integer (L37); 150 or -5 validates.
7. **D-07** (type-mismatch; README.md L155 L255 L323 L447 L572 L659 L740 L1018 L1194 L1462 L1602 L1836; otm_schema.json L27 L48 L71 L97 L127 L157 L194 L208 L253) Every attributes field is typed Map [string, string] in the README (written Map &lt;string, string&gt; in the representation-element tables); the schema declares ["object", "null"] with no constraint on member values, so numbers, arrays or objects validate. The README's own Diagram example gives an integer value (transparent: 40, L323).
8. **D-08** (collection-typing; README.md L57-L63; otm_schema.json L31 L53 L76 L102 L132 L162 L199) The OTM object table types representations, assets, components, dataflows, trustZones, threats and mitigations as '... object' (L57-L63) and the README never says they are arrays; the schema declares each an array of objects, and the README examples use YAML sequences (e.g. L757, L1034).
9. **D-09** (nullability-inconsistent; otm_schema.json L24 L76 L83 L92 L132 L182 L184 L185 L223 L229 L230 L263) Nullability is applied unevenly: root trustZones (L76) and dataflows (L132) are "array" while the other five root collections are ["array", "null"]; trust zone type (L83), threat risk impactComment (L185) and the Parent object's trustZone and component (L229, L230; each optional outside its oneOf branch) are "string" while every other optional string admits null (likelihoodComment, L183); a trust zone's optional parent refs the Parent object, typed "object" (L92, L223), while a component's optional assets refs a nullable assetInstance (L116, L276); project tags items (L24) are "string" while all other tags items admit null; likelihood admits null (L182) but impact does not (L184); threat-instance mitigations is "array" (L263) while its items admit null. A producer that writes null for every absent optional value fails at these places.
10. **D-10** (required-mismatch; README.md L298 L304 L308 L334 L354; otm_schema.json L34 L40) 'Depending on the type selected, some extra fields must be included' (L298); the Diagram type marks size REQUIRED (L308), the Code type's repository is not marked REQUIRED (L334) and Threat-Model has none (L354). The schema requires only name, id and type of a representation (L34), declares size optional (L40) and has no conditional (if/then) on type.
11. **D-11** (required-mismatch; README.md L432 L440; otm_schema.json L243 L248 L249) A representation element for a diagram has position (L432) and size (L440) REQUIRED; the schema's representationElement requires only representation and id (L243). Which variant applies depends on the type of the representation the element names, which a schema of the element alone cannot see.
12. **D-12** (required-mismatch; README.md L1930-L1932; otm_schema.json L43 L45) Repository url carries no REQUIRED in the README (L1932); the schema requires it whenever repository is present (L43) and at the same time admits null for it (L45).
13. **D-13** (internal-contradiction; README.md L480 L494 L518) 'Despite all fields being optional, at least one of them is required.' (L480) opens a table that marks representation (L494) and id (L518) REQUIRED, so the fields are not all optional, and 'at least one of them' names no field set. The schema has no anyOf or minProperties for it.
14. **D-14** (type-description-mismatch; README.md L1175 L1177 L1236; otm_schema.json L92 L223) TrustZones parent is typed Parent object (L1175; schema L92 refs definitions/parent, an object, L223) but described as 'Unique identifier of the component or trust zone enclosing this trust zone' (L1177). The README's TrustZones example writes parent: internet (L1236), a bare string, which the schema rejects.
15. **D-15** (ambiguous-semantics; README.md L1175 L1284-L1287 L1302 L1314) The trustZone row (L1302) and the component row (L1314) of the Parent object share one description: 'Id of the element in which this component is currently enclosed. It can be either a trust zone or another component.' Each key-specific row thus says its id may name either kind, and both say 'this component' although trust zones use the Parent object too (L1175). That the key names the kind of the parent is implied (L1284-L1287) but not stated.
16. **D-16** (strength-mismatch; README.md L985 L1177 L1302 L1314; otm_schema.json L224-L227) The README says a parent 'should contain an attribute name stating the component type' (L985, L1177, L1302, L1314), a recommendation; the schema's oneOf (L224-L227) makes exactly one of trustZone or component mandatory in every Parent object, so a parent without that attribute is invalid.
17. **D-17** (integrity-not-enforced; README.md L93 L221 L396 L420 L494 L518 L624 L648 L697 L865 L880 L934 L1127 L1302 L1314 L1364 L1417 L1429 L1441 L1529 L1731 L1800 L1885) The README's identifier rules are prose-only: eleven ids are each a 'Unique identifier' (scope not stated: per collection or document-wide), and representation elements, parents, dataflow endpoints and assets, asset instances, threat instances and mitigation instances name other objects by id. JSON Schema draft-07 has no keys or references between instance values, and the schema declares no uniqueItems; validation checks none of it.
18. **D-18** (enumeration-not-encoded; README.md L189-L193 L298 L372-L376; otm_schema.json L38) The README lists the 'currently supported representation types' diagram, code, threat-model (L189-L193, restated L372-L376); the schema types representation type as a plain string (L38) with no enum. Whether another value is invalid is not stated.
19. **D-19** (unspecified-vocabulary; README.md L946 L1139 L1744 L1897) Four fields have no value set: component type (L946; examples ec2-instance, web-service, database, code-class at L949, L1037, L1073, L1088; EXAMPLE.yaml uses CD-V2-WEB-CLIENT and similar at L52), trust zone type (L1139; examples internet, private at L1142, L1232; EXAMPLE.yaml uses UUIDs at L170, L186), threat-instance state (L1744; examples exposed, mitigated at L1747, L1766) and mitigation-instance state (L1897; examples implemented, required at L1769, L1495). The two state fields are REQUIRED.
20. **D-20** (default-not-encoded; README.md L1404; otm_schema.json L140) Dataflows bidirectional defaults to false (L1404); the schema declares no default for it and admits null (L140).
21. **D-21** (wrong-field-name; README.md L63 L1885; otm_schema.json L198) The mitigation instance's mitigation 'should be declared in the root node mitigation' (L1885); the root field is mitigations (L63; schema L198), and field names are case sensitive (L25). The parallel threat-instance rule names 'the root node threats' correctly (L1731-L1732).
22. **D-22** (wrong-link; README.md L994 L1186) Components representations is typed 'array of <a href="#representations-object">Representation Element object</a>' (L994): the link targets the Representations object, not the RepresentationElement object that TrustZones links correctly (#representationelement-object, L1186).
23. **D-23** (copy-paste; README.md L1838) Mitigations attributes is described as 'This is a free-form list of attributes that complete the description of the threat.' (L1838): the Threats row's wording, in the Mitigations table.
24. **D-24** (heading-level; README.md L1949 L1986) '### Position object' (L1986) is a level-3 heading under '## Size object' (L1949), while every other object section is level 2, so the README's own heading path places Position inside Size. Locators in this record keep that path.
25. **D-25** (example-invalid; README.md L1210-L1248) TrustZones example: the key is trustzones (L1211), not trustZones (L61; schema L75), and field names are case sensitive (L25); representations is a single mapping, not an array (L1218, L1238); parent is the string internet (L1236), not a Parent object; postion (L1241) and with (L1245) for position and width. Against the schema the block is not a trust-zone list at all, and under the intended key it fails at representations and parent.
26. **D-26** (example-invalid; README.md L462-L476 L588-L606 L674-L681) The three representation-element examples put one element mapping under representations: (L463, L589, L675) where the field is an array of elements. The diagram example writes with: 100 (L471) for width, so the size lacks its required width (schema L216), and its attributes: (L473) sits at column 0, outside the element.
27. **D-27** (example-invalid; README.md L1033-L1097) Components example: the first component's attributes is a list of single-key maps (L1065-L1067), not a map (Map [string, string]; schema L127 object); the second component's representation element writes represetation (L1077), so its required representation is missing (schema L243).
28. **D-28** (example-invalid; README.md L1477-L1499) Dataflows example: target: customer-database (L1484) where the field is destination (L1429), which is required (schema L135); the example fails validation.
29. **D-29** (example-value; README.md L160 L179 L1607 L1635 L1735) Example values that are not what they look like: expirationDate: 2021-05-17 (L1635) is unquoted, which a YAML 1.1 loader reads as a timestamp, a value with no JSON equivalent (L23); the table cell writes the same value with typographic quotes, “2021-05-17” (L1607), as do filePath: “file.xml” (L160, L179), so the curly quotes become part of the string; the threat-instance example cell indents with a no-break space (U+00A0, L1735), which YAML does not treat as indentation.
30. **D-30** (example-undeclared-fields; EXAMPLE.yaml L124 L145 L158; EXAMPLE.json L177 L195 L212) The complete example (README L11) uses members that neither the README nor the schema defines: package in a representation element (EXAMPLE.yaml L124; EXAMPLE.json L177) and representations in dataflows (EXAMPLE.yaml L145, L158; EXAMPLE.json L195, L212). Both files validate only because the schema sets no additionalProperties (an open content model).
31. **D-31** (licence-split; README.md L2033; otm_schema.json L5; LICENSE L1) The repository's LICENSE is the CC BY-SA 4.0 legal code and the README footer licenses 'This work' under it (L2033); the schema's $comment says it 'is published under the terms of the Apache License 2.0' (schema L5). The schema file thus carries two candidate licences: Apache-2.0 by its own statement, CC BY-SA 4.0 by the repository licence.
32. **D-32** (typos; README.md L7 L33 L56 L58 L67 L257 L304 L330 L354 L370 L573 L660 L685 L825 L1266 L1717 L1756 L1812 L1838 L1951) Kept verbatim, not corrected. In normative text: 'From 0 to a 100' (L825) and 'From 0 and 100' (L1266) for the 0-100 range; 'within all the other elements are grouped' (L56, L67) lacks 'which'; 'Its the unit of work' (L67) beside 'It's' (L56); 'sensible information' for sensitive (L58, L685); 'The representation element stated how' (L370); 'add additional data' (L1717); 'Short descriptions' (L1812); 'free-form list of attributes' (L257, L573, L660, L1838) beside 'free-form map' for the same Map type; typographic quotes opened on both sides, “diagram“ (L304), “code“ (L330), “threat-model“ (L354); 'keep you threat model aware of the changes that happens' (L7); 'within an OTM files' (L33); 'Array of mitigation' (L1756); 'a very basic information' (L1951). In examples: attakers (L776), represetation (L1077), postgress (L1078), Managages (L1087), accesible (L1156), postion (L1241), psotgress-db (L1432), Creditcard and data base (L1481), attaketr and cyprografy (L1631), rallity, strruggle and monetory (L1633), with for width (L471, L1245), an unbalanced quote in 'MuCustomApp123 (L108).
