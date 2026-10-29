---
record: cwe
kind: normative
title: "cwe — normative statements"
extracted: "2026-10-08"
reviewed_by: ""
---

# CWE XML Schema 7.3 — normative content

Source: `cwe_schema_v7.3.xsd` — CWE Schema version 7.3, dated December 11, 2025, target namespace `http://cwe.mitre.org/cwe-7`, 1345 lines, SHA-256 `690dedeed4e12eb8ba7244bbab90176afac549cfd6403de37000de7481e45f98`, <https://cwe.mitre.org/data/xsd/cwe_schema_v7.3.xsd>. It validates the CWE List 4.20 XML. Pass-1 extraction (agent A), 2026-10-08; verify and cross-check passes (agent C), 2026-10-08, recorded in `verification.md`.

How to read this file:

- One `##` section per top-level schema component, in file order. The `#` headings that follow the first are the source's own banner comments.
- `(L<line> › <path>)` locates a quotation: the line on which it starts and the declaration it documents.
- All 111 `xs:documentation` texts and the `xs:appinfo` content are quoted verbatim, in full. Whitespace runs (line breaks, tabs, double spaces) are normalised to one space. XML character references (`&lt;`, `&gt;`) are kept as written in the file, so they render as `<` and `>`. Spelling and grammar are the source's own.
- Structure lines are renderings of the declaration on the cited line, not quotations: `name : type [minOccurs..maxOccurs]`. † marks a value the source omits (XSD default 1). *required* means effective minOccurs ≥ 1 for an element or `use="required"` for an attribute; a required child of an optional element is required whenever its parent is present. The children of an `xs:sequence` must appear in the order listed. The schema declares no `default` or `fixed` values, no `xs:key` or `xs:keyref`, and no facets other than `xs:enumeration`.
- `cwe#R-NNNN` points to `requirements.yaml`, which lists every requirement extracted from this text and structure, with an occurrence-by-occurrence account of the lower-case keywords. The last section lists source inconsistencies found while extracting; it is the only text here that is not the source's.

## Schema — `xs:schema`, `xs:import` and header annotation (L2–L12)

Declaration (L2): `targetNamespace="http://cwe.mitre.org/cwe-7"`, `elementFormDefault="qualified"`, `attributeFormDefault="unqualified"`, `version="7.3"`; namespace prefixes `xs` (XML Schema), `cwe` (the target namespace) and `xhtml`. (cwe#R-0001, cwe#R-0002)

Import (L3): `<xs:import namespace="http://www.w3.org/1999/xhtml" schemaLocation="http://www.w3.org/2002/08/xhtml/xhtml1-strict.xsd"/>` — the XHTML 1.0 Strict schema, against which the two `xs:any` wildcards (L1332, L1340) validate.

**Documentation**

- (L5 › xs:schema) The CWE Schema is maintained by The MITRE Corporation and developed in partnership with the public CWE Community. For more information, including how to get involved in the project and how to submit change requests, please visit the CWE website at https://cwe.mitre.org.

**Appinfo** (verbatim; the terms of use require this header to accompany distributed copies of the schema)

- (L7 › xs:schema › xs:appinfo › schema) Core Definition
- (L8 › xs:schema › xs:appinfo › version) 7.3
- (L9 › xs:schema › xs:appinfo › date) December 11, 2025
- (L10 › xs:schema › xs:appinfo › terms_of_use) Copyright (c) 2006-2025, The MITRE Corporation. All rights reserved. The contents of this file are subject to the terms of the CWE License located at https://cwe.mitre.org/about/termsofuse.html. See the CWE License for the specific language governing permissions and limitations for use of this schema. When distributing copies of the CWE Schema, this license header must be included.
  - extracted as: cwe#R-0003 (indicative), cwe#R-0004 (must)

## Weakness_Catalog — root element (L16–L75) (cwe#R-0005)

**Documentation**

- (L18 › Weakness_Catalog) The Weakness_Catalog root element is used to describe a collection of security issues known as weaknesses (e.g., flaws, faults, bugs). Each catalog can be organized by optional Views and Categories. The catalog also contains a list of all External_References that may be shared throughout the individual weaknesses. The required Name and Version attributes are used to uniquely identify the catalog. The required Date attribute identifies the date when this catalog was created or last updated.
  - extracted as: cwe#R-0006 (unique)

**Structure** — anonymous complexType (L20): xs:sequence (L21), children in this order; then attributes

- L22 `Weaknesses` [0..1] — optional; anonymous complexType (L23) — xs:sequence (L24), children in this order:
  - L25 `Weakness` : cwe:WeaknessType [1..unbounded] — required (cwe#R-0007)
- L29 `Categories` [0..1] — optional; anonymous complexType (L30) — xs:sequence (L31), children in this order:
  - L32 `Category` : cwe:CategoryType [1..unbounded] — required (cwe#R-0008)
- L36 `Views` [0..1] — optional; anonymous complexType (L37) — xs:sequence (L38), children in this order:
  - L39 `View` : cwe:ViewType [1..unbounded] — required (cwe#R-0009)
- L43 `External_References` [0..1] — optional; anonymous complexType (L44) — xs:sequence (L45), children in this order:
  - L46 `External_Reference` : cwe:ExternalReferenceType [1..unbounded] — required (cwe#R-0010)
- L51 `@Name` : xs:string — required (cwe#R-0011)
- L52 `@Version` : xs:string — required (cwe#R-0012)
- L53 `@Date` : xs:date — required (cwe#R-0013)

**Identity constraints** (`xs:unique`; a selected node lacking the field is not constrained)

- L55 `<xs:unique name="uniqueWeaknessID">` — selector `./cwe:Weaknesses/cwe:Weakness` (L56), field `@ID` (L57) (cwe#R-0014)
- L59 `<xs:unique name="uniqueWeaknessName">` — selector `./cwe:*/cwe:*` (L60), field `@Name` (L61) (cwe#R-0015)
- L63 `<xs:unique name="uniqueCategoryID">` — selector `./cwe:Categories/cwe:Category` (L64), field `@ID` (L65) (cwe#R-0016)
- L67 `<xs:unique name="uniqueViewID">` — selector `./cwe:Views/cwe:View` (L68), field `@ID` (L69) (cwe#R-0017)
- L71 `<xs:unique name="uniqueReferenceID">` — selector `./cwe:External_References/cwe:External_Reference` (L72), field `@Reference_ID` (L73) (cwe#R-0018)

# WEAKNESS

_Source banner comment, L77._

## WeaknessType — complexType (L79–L116)

**Documentation**

- (L81 › WeaknessType) A weakness is a mistake or condition that, if left unaddressed, could under the proper conditions contribute to a cyber-enabled capability being vulnerable to attack, allowing an adversary to make items function in unintended ways. This complexType is used to describe a specific type of weakness and provide a variety of information related to it.
- (L82 › WeaknessType) The required Description should be short and limited to the key points that define this weakness. The optional Extended_Description element provides a place for additional details important to this weakness, but that are not necessary to convey the fundamental concept behind the weakness. A number of other optional elements are available, each of which is described in more detail within the corresponding complexType that it references.
  - extracted as: cwe#R-0019 (should)
- (L83 › WeaknessType) The required ID attribute provides a unique identifier for the entry. It is considered static for the lifetime of the entry. If this entry becomes deprecated, the identifier will not be reused. The required Name attribute is a string that identifies the entry. The name should focus on the weakness being described and should avoid mentioning the attack that exploits the weakness or the consequences of exploiting the weakness. All words in the entry name should be capitalized except for articles and prepositions, unless they begin or end the name. Subsequent words in a hyphenated chain are also not capitalized. The required Abstraction attribute defines the abstraction level for this weakness. The required Structure attribute defines the structural nature of the weakness. The required Status attribute defines the maturity of the information for this weakness.
  - extracted as: cwe#R-0020 (unique), cwe#R-0021 (static), cwe#R-0022 (will not), cwe#R-0023 (should), cwe#R-0024 (should), cwe#R-0025 (should), cwe#R-0026 (indicative)

**Structure** — xs:sequence (L85), children in this order; then attributes

- L86 `Description` : xs:string [1..1] — required (cwe#R-0027)
- L87 `Extended_Description` : cwe:StructuredTextType [0..1] — optional
- L88 `Related_Weaknesses` : cwe:RelatedWeaknessesType [0..1] — optional
- L89 `Weakness_Ordinalities` : cwe:WeaknessOrdinalitiesType [0..1] — optional
- L90 `Applicable_Platforms` : cwe:ApplicablePlatformsType [0..1] — optional
- L91 `Background_Details` : cwe:BackgroundDetailsType [0..1] — optional
- L92 `Alternate_Terms` : cwe:AlternateTermsType [0..1] — optional
- L93 `Modes_Of_Introduction` : cwe:ModesOfIntroductionType [0..1] — optional
- L94 `Exploitation_Factors` : cwe:ExploitationFactorsType [0..1] — optional
- L95 `Likelihood_Of_Exploit` : cwe:LikelihoodEnumeration [0..1] — optional
- L96 `Common_Consequences` : cwe:CommonConsequencesType [0..1] — optional
- L97 `Detection_Methods` : cwe:DetectionMethodsType [0..1] — optional
- L98 `Potential_Mitigations` : cwe:PotentialMitigationsType [0..1] — optional
- L99 `Demonstrative_Examples` : cwe:DemonstrativeExamplesType [0..1] — optional
- L100 `Observed_Examples` : cwe:ObservedExampleType [0..1] — optional
- L101 `Functional_Areas` : cwe:FunctionalAreasType [0..1] — optional
- L102 `Affected_Resources` : cwe:AffectedResourcesType [0..1] — optional
- L103 `Taxonomy_Mappings` : cwe:TaxonomyMappingsType [0..1] — optional
- L104 `Related_Attack_Patterns` : cwe:RelatedAttackPatternsType [0..1] — optional
- L105 `References` : cwe:ReferencesType [0..1] — optional
- L106 `Mapping_Notes` : cwe:MappingNotesType [1..1] — required (cwe#R-0028)
- L107 `Notes` : cwe:NotesType [0..1] — optional
- L108 `Content_History` : cwe:ContentHistoryType [1..1] — required (cwe#R-0029)
- L110 `@ID` : xs:integer — required (cwe#R-0030)
- L111 `@Name` : xs:string — required (cwe#R-0031)
- L112 `@Abstraction` : cwe:AbstractionEnumeration — required (cwe#R-0032)
- L113 `@Structure` : cwe:StructureEnumeration — required (cwe#R-0033)
- L114 `@Status` : cwe:StatusEnumeration — required (cwe#R-0034)
- L115 `@Diagram` : xs:string — optional

# CATEGORY

_Source banner comment, L118._

## CategoryType — complexType (L120–L138)

**Documentation**

- (L122 › CategoryType) A category is a collection of weaknesses based on some common characteristic or attribute. The shared attribute may be any number of things including, but not limited to, environment (J2EE, .NET), functional area (authentication, cryptography) and the relevant resource (credentials management, certificate issues). A Category is used primarily as an organizational mechanism for CWE and should not be mapped to by external sources.
  - extracted as: cwe#R-0035 (should not)
- (L123 › CategoryType) The required Summary element contains the key points that define the category and helps the user understand what the category is attempting to be. The optional Relationships element is used to define relationships (Member_Of and Has_Member) with other weaknesses, categories, and views. The optional Taxonomy_Mappings element is used to relate this category to similar categories in taxomomies outside of CWE. The optional References element is used to provide further reading and insight into this category. This element should be used when the category is based on external sources or projects. The optional Notes element is used to provide additional comments or clarifications that cannot be captured using the other elements of the category. The optional Content_History element is used to keep track of the original author of the category and any subsequent modifications to the content. This provides a means of contacting the authors and modifiers for clarifying ambiguities, or in merging overlapping contributions.
  - extracted as: cwe#R-0036 (should)
- (L124 › CategoryType) The required ID attribute provides a unique identifier for the category. It is meant to be static for the lifetime of the category. If the category becomes deprecated, the ID should not be reused, and a placeholder for the deprecated category should be left in the catalog. The required Name attribute provides a descriptive title used to give the reader an idea of what characteristics this category represents. All words in the name should be capitalized except for articles and prepositions unless they begin or end the name. The required Status attribute defines the maturity of the information for this category. Please refer to the StatusEnumeration simple type for a list of valid values and their meanings.
  - extracted as: cwe#R-0037 (unique), cwe#R-0038 (static), cwe#R-0039 (should not), cwe#R-0040 (should), cwe#R-0041 (should)

**Structure** — xs:sequence (L126), children in this order; then attributes

- L127 `Summary` : cwe:StructuredTextType [1..1] — required (cwe#R-0042)
- L128 `Relationships` : cwe:RelationshipsType [0..1] — optional
- L129 `Taxonomy_Mappings` : cwe:TaxonomyMappingsType [0..1] — optional
- L130 `References` : cwe:ReferencesType [0..1] — optional
- L131 `Mapping_Notes` : cwe:MappingNotesType [1..1] — required (cwe#R-0043)
- L132 `Notes` : cwe:NotesType [0..1] — optional
- L133 `Content_History` : cwe:ContentHistoryType [1..1] — required (cwe#R-0044)
- L135 `@ID` : xs:integer — required (cwe#R-0045)
- L136 `@Name` : xs:string — required (cwe#R-0046)
- L137 `@Status` : cwe:StatusEnumeration — required (cwe#R-0047)

# VIEW

_Source banner comment, L140._

## ViewType — complexType (L142–L162)

**Documentation**

- (L144 › ViewType) A view represents a perspective with which one might look at the weaknesses in the catalog. There are three different types of views as defined by the type attribute: graphs, explicit slices, and implicit slices. The members of a view are either defined externally through the members element (in the case of a graph or an explicit slice) or by the optional filter element (in the case of an implicit slice).
  - extracted as: cwe#R-0048 (indicative)
- (L145 › ViewType) The required Objective element describes the perspective from which the view has been constructed. The optional Audience element provides a reference to the target stakeholders or groups for whom the view is most relevant. The optional Members element is used to define Member_Of relationships with categories. The optional Filter element is only used for implicit slices (see the Type attribute) and holds an XSL query for identifying which entries are members of the view. The optional References element is used to provide further reading and insight into this view. This element should be used when the view is based on external sources or projects. The optional Notes element is used to provide any additional comments that cannot be captured using the other elements of the view. The optional Content_History element is used to keep track of the original author of the view and any subsequent modifications to the content. This provides a means of contacting the authors and modifiers for clarifying ambiguities, or in merging overlapping contributions.
  - extracted as: cwe#R-0049 (only), cwe#R-0050 (should)
- (L146 › ViewType) The required ID attribute provides a unique identifier for the view. It is meant to be static for the lifetime of the view. If the view becomes deprecated, the ID should not be reused, and a placeholder for the deprecated view should be left in the catalog. The required Name attribute provides a descriptive title used to give the reader an idea of what perspective this view represents. All words in the name should be capitalized except for articles and prepositions, unless they begin or end the name. The required Type attribute describes how this view is being constructed. Please refer to the ViewTypeEnumeration simple type for a list of valid values and their meanings. The required Status attribute defines the maturity of the information for this view. Please refer to the StatusEnumeration simple type for a list of valid values and their meanings.
  - extracted as: cwe#R-0051 (unique), cwe#R-0052 (static), cwe#R-0053 (should not), cwe#R-0054 (should), cwe#R-0055 (should)

**Structure** — xs:sequence (L148), children in this order; then attributes

- L149 `Objective` : cwe:StructuredTextType [1..1] — required (cwe#R-0056)
- L150 `Audience` : cwe:AudienceType [0..1] — optional
- L151 `Members` : cwe:RelationshipsType [0..1] — optional
- L152 `Filter` : xs:string [0..1] — optional
- L153 `References` : cwe:ReferencesType [0..1] — optional
- L154 `Mapping_Notes` : cwe:MappingNotesType [1..1] — required (cwe#R-0057)
- L155 `Notes` : cwe:NotesType [0..1] — optional
- L156 `Content_History` : cwe:ContentHistoryType [1..1] — required (cwe#R-0058)
- L158 `@ID` : xs:integer — required (cwe#R-0059)
- L159 `@Name` : xs:string — required (cwe#R-0060)
- L160 `@Type` : cwe:ViewTypeEnumeration — required (cwe#R-0061)
- L161 `@Status` : cwe:StatusEnumeration — required (cwe#R-0062)

# EXTERNAL REFERENCE

_Source banner comment, L164._

## ExternalReferenceType — complexType (L166–L185)

**Documentation**

- (L168 › ExternalReferenceType) The ExternalReferenceType complex type defines a collection of elements that provide a pointer to where more information and deeper insight can be obtained. Examples would be a research paper or an excerpt from a publication.
- (L169 › ExternalReferenceType) Not all of the elements need to be used, since some are designed for web references and others are designed for book references. The Author and Title elements should be filled out for all references if possible; Author is optional, but Title is required. The optional Edition element identifies the edition of the material being referenced in the event that multiple editions of the material exist. If the reference is part of a magazine or journal, the Publication element should be used to identify the name. The optional Publication_Year, Publication_Month, Publication_Day, and Publisher elements should be used to more specifically identify the book or publication via its date and publisher. The year must follow the YYYY format while the month must follow the --MM format and the day must follow the ---DD format. The URL and URL_Date elements are used to capture a URL for the material being referenced, if one exists, and the date when the URL was validated to exist.
  - extracted as: cwe#R-0063 (should), cwe#R-0064 (required), cwe#R-0065 (should), cwe#R-0066 (should), cwe#R-0067 (must), cwe#R-0068 (must), cwe#R-0069 (must)
- (L170 › ExternalReferenceType) The required Reference_ID attribute exists to provide a globally unique identifier for the reference (e.g., REF-1). The ID is used by other entities to link to this external reference.
  - extracted as: cwe#R-0070 (unique)

**Structure** — xs:sequence (L172), children in this order; then attributes

- L173 `Author` : xs:string [0..unbounded] — optional
- L174 `Title` : xs:string [1..1] — required (cwe#R-0071)
- L175 `Edition` : xs:string [0..1] — optional
- L176 `Publication` : xs:string [0..1] — optional
- L177 `Publication_Year` : xs:gYear [0..1] — optional
- L178 `Publication_Month` : xs:gMonth [0..1] — optional
- L179 `Publication_Day` : xs:gDay [0..1] — optional
- L180 `Publisher` : xs:string [0..1] — optional
- L181 `URL` : xs:anyURI [0..1] — optional
- L182 `URL_Date` : xs:date [0..1] — optional
- L184 `@Reference_ID` : xs:string — required (cwe#R-0072)

# GLOBAL TYPES

_Source banner comment, L187._

## AffectedResourcesType — complexType (L189–L196)

**Documentation**

- (L191 › AffectedResourcesType) The AffectedResourcesType complex type is used to identify system resources that can be affected by an exploit of this weakness. If multiple resources could be affected, then each should be defined by its own Affected_Resource element.
  - extracted as: cwe#R-0073 (should)

**Structure** — xs:sequence (L193), children in this order

- L194 `Affected_Resource` : cwe:ResourceEnumeration [1..unbounded] — required (cwe#R-0074)

## AlternateTermsType — complexType (L197–L211)

**Documentation**

- (L199 › AlternateTermsType) The AlternateTermsType complex type indicates one or more other names used to describe this weakness. The required Term element contains the actual alternate term. The required Description element provides context for each alternate term by which this weakness may be known.

**Structure** — xs:sequence (L201), children in this order

- L202 `Alternate_Term` [1..unbounded] — required (cwe#R-0075); anonymous complexType (L203) — xs:sequence (L204), children in this order:
  - L205 `Term` : xs:string [1..1] — required (cwe#R-0076)
  - L206 `Description` : cwe:StructuredTextType [0..1] — optional

## ApplicablePlatformsType — complexType (L212–L248)

**Documentation**

- (L214 › ApplicablePlatformsType) The ApplicablePlatformsType complex type specifies the languages, operating systems, architectures, and technologies in which a given weakness could appear. A technology represents a generally accepted feature of a system and often refers to a high-level functional component within a system. The required Prevalence attribute identifies the regularity with which the weakness is applicable to that platform. When providing an operating system name, an optional Common Platform Enumeration (CPE) identifier can be used to a identify a specific OS.

**Structure** — xs:sequence (L216), children in this order

- L217 `Language` [0..unbounded] — optional; anonymous complexType (L218) — attributes only:
  - L219 `@Name` : cwe:LanguageNameEnumeration — optional
  - L220 `@Class` : cwe:LanguageClassEnumeration — optional
  - L221 `@Prevalence` : cwe:PrevalenceEnumeration — required (cwe#R-0077)
- L224 `Operating_System` [0..unbounded] — optional; anonymous complexType (L225) — attributes only:
  - L226 `@Name` : cwe:OperatingSystemNameEnumeration — optional
  - L227 `@Version` : xs:string — optional
  - L228 `@CPE_ID` : xs:string — optional
  - L229 `@Class` : cwe:OperatingSystemClassEnumeration — optional
  - L230 `@Prevalence` : cwe:PrevalenceEnumeration — required (cwe#R-0078)
- L233 `Architecture` [0..unbounded] — optional; anonymous complexType (L234) — attributes only:
  - L235 `@Name` : cwe:ArchitectureNameEnumeration — optional
  - L236 `@Class` : cwe:ArchitectureClassEnumeration — optional
  - L237 `@Prevalence` : cwe:PrevalenceEnumeration — required (cwe#R-0079)
- L240 `Technology` [0..unbounded] — optional; anonymous complexType (L241) — attributes only:
  - L242 `@Name` : cwe:TechnologyNameEnumeration — optional
  - L243 `@Class` : cwe:TechnologyClassEnumeration — optional
  - L244 `@Prevalence` : cwe:PrevalenceEnumeration — required (cwe#R-0080)

## AudienceType — complexType (L249–L263)

**Documentation**

- (L251 › AudienceType) The AudienceType complex type provides a reference to the target stakeholders or groups for a view. For each stakeholder, the required Type element specifies the type of members that might be interested in the view. The required Description element provides some text describing what properties of the view this particular stakeholder might find useful.

**Structure** — xs:sequence (L253), children in this order

- L254 `Stakeholder` [1..unbounded] — required (cwe#R-0081); anonymous complexType (L255) — xs:sequence (L256), children in this order:
  - L257 `Type` : cwe:StakeholderEnumeration [1..1] — required (cwe#R-0082)
  - L258 `Description` : xs:string [0..1] — optional

## BackgroundDetailsType — complexType (L264–L271)

**Documentation**

- (L266 › BackgroundDetailsType) The BackgroundDetailsType complex type contains one or more Background_Detail elements, each of which contains information that is relevant but not related to the nature of the weakness itself.

**Structure** — xs:sequence (L268), children in this order

- L269 `Background_Detail` : cwe:StructuredTextType [1..unbounded] — required (cwe#R-0083)

## CommonConsequencesType — complexType (L272–L290)

**Documentation**

- (L274 › CommonConsequencesType) The CommonConsequencesType complex type is used to specify individual consequences associated with a weakness. The required Scope element identifies the security property that is violated. The optional Impact element describes the technical impact that arises if an adversary succeeds in exploiting this weakness. The optional Likelihood element identifies how likely the specific consequence is expected to be seen relative to the other consequences. For example, there may be high likelihood that a weakness will be exploited to achieve a certain impact, but a low likelihood that it will be exploited to achieve a different impact. The optional Note element provides additional commentary about a consequence.
- (L275 › CommonConsequencesType) The optional Consequence_ID attribute is used by the internal CWE team to uniquely identify examples that are repeated across any number of individual weaknesses. To help make sure that the details of these common examples stay synchronized, the Consequence_ID is used to quickly identify those examples across CWE that should be identical. The identifier is a string and should match the following format: CC-1.
  - extracted as: cwe#R-0084 (should), cwe#R-0085 (should)

**Structure** — xs:sequence (L277), children in this order

- L278 `Consequence` [1..unbounded] — required (cwe#R-0086); anonymous complexType (L279) — xs:sequence (L280), children in this order; then attributes:
  - L281 `Scope` : cwe:ScopeEnumeration [1..unbounded] — required (cwe#R-0087)
  - L282 `Impact` : cwe:TechnicalImpactEnumeration [1..unbounded] — required (cwe#R-0088)
  - L283 `Likelihood` : cwe:LikelihoodEnumeration [0..1] — optional (cwe#R-0089)
  - L284 `Note` : cwe:StructuredTextType [0..1] — optional (cwe#R-0090)
  - L286 `@Consequence_ID` : xs:string — optional

## ContentHistoryType — complexType (L291–L357)

**Documentation**

- (L293 › ContentHistoryType) The ContentHistoryType complex type provides elements to keep track of the original author of an entry and any subsequent modifications to the content. The required Submission element is used to identify the submitter and/or their organization, the date on which the submission was made, the CWE version and release date in which the new CWE entry was added, and any optional comments related to an entry. The optional Modification element is used to identify a modifier's name, organization, the date on which the Modification was made or suggested, the CWE version and release date in which the modification first appeared, and any related comments. A new Modification element should exist for each change made to the content. Modifications that change the meaning of the entry, or how it might be interpreted, should be marked with an importance of critical to bring it to the attention of anyone previously dependent on the weakness. The optional Contribution element is used to identify a contributor's name, organization, the date, the CWE version and release date in which the contribution first appeared, and any related comments. This element has a single Type attribute, which indicates whether the contribution was part of general feedback given or actual content that was donated. The optional Previous_Entry_Name element is used to describe a previous name that was used for the entry. This should be filled out whenever a substantive name change occurs. The required Date attribute lists the date on which this name was no longer used, typically the date of the first CWE release that changed the previous name. A Previous_Entry_Name element should align with a corresponding Modification element.
  - extracted as: cwe#R-0091 (should), cwe#R-0092 (should), cwe#R-0093 (should), cwe#R-0094 (should)

**Structure** — xs:sequence (L295), children in this order

- L296 `Submission` [1†..1†] — required (cwe#R-0095); anonymous complexType (L297) — xs:sequence (L298), children in this order:
  - L299 xs:choice [1†..1†] — one branch per occurrence (cwe#R-0096):
    - branch 1: L300 xs:sequence [1†..1†] — children in this order:
      - L301 `Submission_Name` : xs:string [1..1†] — required in this branch (cwe#R-0097)
      - L302 `Submission_Organization` : xs:string [0..1†] — optional
    - branch 2: L304 `Submission_Organization` : xs:string [1..1†] — required in this branch (cwe#R-0098)
  - L306 `Submission_Date` : xs:date [1†..1†] — required (cwe#R-0099)
  - L307 `Submission_Version` : xs:string [1†..1†] — required (cwe#R-0100)
  - L308 `Submission_ReleaseDate` : xs:date [1†..1†] — required (cwe#R-0101)
  - L309 `Submission_Comment` : xs:string [0..1] — optional
- L313 `Modification` [0..unbounded] — optional; anonymous complexType (L314) — xs:sequence (L315), children in this order:
  - L316 `Modification_Name` : xs:string [0..1] — optional
  - L317 `Modification_Organization` : xs:string [0..1] — optional
  - L318 `Modification_Date` : xs:date [1..1] — required (cwe#R-0102)
  - L319 `Modification_Version` : xs:string [0..1] — optional
  - L320 `Modification_ReleaseDate` : xs:date [0..1] — optional
  - L321 `Modification_Importance` : cwe:ImportanceEnumeration [0..1] — optional
  - L322 `Modification_Comment` : xs:string [0..1] — optional
- L326 `Contribution` [0..unbounded] — optional; anonymous complexType (L327) — xs:sequence (L328), children in this order; then attributes:
  - L329 `Contribution_Name` : xs:string [0..1] — optional
  - L330 `Contribution_Organization` : xs:string [0..1] — optional
  - L331 `Contribution_Date` : xs:date [1..1] — required (cwe#R-0103)
  - L332 `Contribution_Version` : xs:string [0..1] — optional
  - L333 `Contribution_ReleaseDate` : xs:date [0..1] — optional
  - L334 `Contribution_Comment` : xs:string [0..1] — optional
  - L336 `@Type` — required (cwe#R-0104); anonymous simple type (L337): restriction of `xs:string` (L338), closed enumeration of 2 values:
    - L339 `Content`
    - L340 `Feedback`
- L346 `Previous_Entry_Name` [0..unbounded] — optional; anonymous complexType (L347) — simple content (L348): extension of `xs:string` (L349) adding attributes:
  - L350 `@Date` : xs:date — required (cwe#R-0105)
  - L351 `@Version` : xs:string — optional

## DemonstrativeExamplesType — complexType (L358–L379)

**Documentation**

- (L360 › DemonstrativeExamplesType) The DemonstrativeExamplesType complex type contains one or more Demonstrative_Example elements, each of which contains an example illustrating how a weakness may look in actual code. The optional Title_Text element provides a title for the example. The Intro_Text element describes the context and setting in which this code should be viewed, summarizing what the code is attempting to do. The Body_Text and Example_Code elements are a mixture of code and explanatory text about the example. The References element provides additional information.
- (L361 › DemonstrativeExamplesType) The optional Demonstrative_Example_ID attribute is used by the internal CWE team to uniquely identify examples that are repeated across any number of individual weaknesses. To help make sure that the details of these common examples stay synchronized, the Demonstrative_Example_ID is used to quickly identify those examples across CWE that should be identical. The identifier is a string and should match the following format: DX-1.
  - extracted as: cwe#R-0106 (should), cwe#R-0107 (should)

**Structure** — xs:sequence (L363), children in this order

- L364 `Demonstrative_Example` [1..unbounded] — required (cwe#R-0108); anonymous complexType (L365) — xs:sequence (L366), children in this order; then attributes:
  - L367 `Title_Text` : xs:string [0..1] — optional
  - L368 `Intro_Text` : cwe:StructuredTextType [1..1] — required (cwe#R-0109)
  - L369 xs:choice [0..unbounded] — one branch per occurrence:
    - branch 1: L370 `Body_Text` : cwe:StructuredTextType [1†..1†] — optional (inside an optional xs:choice)
    - branch 2: L371 `Example_Code` : cwe:StructuredCodeType [1†..1†] — optional (inside an optional xs:choice)
  - L373 `References` : cwe:ReferencesType [0..1] — optional
  - L375 `@Demonstrative_Example_ID` : xs:string — optional

## DetectionMethodsType — complexType (L380–L398)

**Documentation**

- (L382 › DetectionMethodsType) The DetectionMethodsType complex type is used to identify methods that may be employed to detect this weakness, including their strengths and limitations. The required Method element identifies the particular detection method being described. The required Description element is intended to provide some context of how this method can be applied to a specific weakness. The optional Effectiveness element says how effective the detection method may be in detecting the associated weakness. This assumes the use of best-of-breed tools, analysts, and methods. There is limited consideration for financial costs, labor, or time. The optional Effectiveness_Notes element provides additional discussion of the strengths and shortcomings of this detection method.
- (L383 › DetectionMethodsType) The optional Detection_Method_ID attribute is used by the internal CWE team to uniquely identify methods that are repeated across any number of individual weaknesses. To help make sure that the details of these common methods stay synchronized, the Detection_Method_ID is used to quickly identify those Detection_Method elements across CWE that should be identical. The identifier is a string and should match the following format: DM-1.
  - extracted as: cwe#R-0110 (should), cwe#R-0111 (should)

**Structure** — xs:sequence (L385), children in this order

- L386 `Detection_Method` [1..unbounded] — required (cwe#R-0112); anonymous complexType (L387) — xs:sequence (L388), children in this order; then attributes:
  - L389 `Method` : cwe:DetectionMethodEnumeration [1..1] — required (cwe#R-0113)
  - L390 `Description` : cwe:StructuredTextType [1..1] — required (cwe#R-0114)
  - L391 `Effectiveness` : cwe:DetectionEffectivenessEnumeration [0..1] — optional
  - L392 `Effectiveness_Notes` : cwe:StructuredTextType [0..1] — optional
  - L394 `@Detection_Method_ID` : xs:string — optional

## ExploitationFactorsType — complexType (L399–L406)

**Documentation**

- (L401 › ExploitationFactorsType) The ExploitationFactorsType complex type points out conditions or factors that could increase the likelihood of exploit for this weakness.

**Structure** — xs:sequence (L403), children in this order

- L404 `Exploitation_Factor` : cwe:StructuredTextType [1..unbounded] — required (cwe#R-0115)

## FunctionalAreasType — complexType (L407–L414)

**Documentation**

- (L409 › FunctionalAreasType) The FunctionalAreasType complex type contains one or more functional_area elements, each of which identifies the functional area in which the weakness is most likely to occur. For example, CWE-23: Relative Path Traversal may occur in functional areas of software related to file processing. Each applicable functional area should have a new Functional_Area element, and standard title capitalization should be applied to each area.
  - extracted as: cwe#R-0116 (should), cwe#R-0117 (should)

**Structure** — xs:sequence (L411), children in this order

- L412 `Functional_Area` : cwe:FunctionalAreaEnumeration [1..unbounded] — required (cwe#R-0118)

## MappingNotesType — complexType (L415–L426)

**Documentation**

- (L417 › MappingNotesType) The MappingNotesType complex type provides guidance for when (and whether) to map an issue to this CWE entry or to suggest alternatives. The Usage element describes whether the CWE should be used for mapping vulnerabilities to their underlying weaknesses as part of root cause analysis. The Rationale element provides context for the Usage. The Comments element provides further clarification to the reader. The Reasons element uses a limited vocabulary to summarize the Usage. The Suggestions element includes suggestions for additional CWEs that might be more appropriate for the mapping task.
  - extracted as: cwe#R-0119 (closed)

**Structure** — xs:sequence (L419), children in this order

- L420 `Usage` : cwe:UsageEnumeration [1..1] — required (cwe#R-0120)
- L421 `Rationale` : cwe:StructuredTextType [1..1] — required (cwe#R-0121)
- L422 `Comments` : cwe:StructuredTextType [1..1] — required (cwe#R-0122)
- L423 `Reasons` : cwe:ReasonsType [1..1] — required (cwe#R-0123)
- L424 `Suggestions` : cwe:SuggestionsType [0..1] — optional

## MemberType — complexType (L427–L433)

**Documentation**

- (L429 › MemberType) The MemberType complex type may be used to establish a Has_Member or Member_Of type relationship within the designated View_ID. This type will establish a relationship between the container Category/View ID and the target CWE_ID.

**Structure** — attributes only

- L431 `@CWE_ID` : xs:integer — required (cwe#R-0124)
- L432 `@View_ID` : xs:integer — required (cwe#R-0125)

## ModesOfIntroductionType — complexType (L434–L448)

**Documentation**

- (L436 › ModesOfIntroductionType) The ModeOfIntroductionType complex type is used to provide information about how and when a given weakness may be introduced. If there are multiple possible introduction points, then a separate Introduction element should be included for each. The required Phase element identifies the point in the product life cycle at which the weakness may be introduced. The optional Note element identifies the typical scenarios under which the weakness may be introduced during the given phase.
  - extracted as: cwe#R-0126 (should)

**Structure** — xs:sequence (L438), children in this order

- L439 `Introduction` [1..unbounded] — required (cwe#R-0127); anonymous complexType (L440) — xs:sequence (L441), children in this order:
  - L442 `Phase` : cwe:PhaseEnumeration [1..1] — required (cwe#R-0128)
  - L443 `Note` : cwe:StructuredTextType [0..1] — optional (cwe#R-0129)

## NotesType — complexType (L449–L464)

**Documentation**

- (L451 › NotesType) The NotesType complex type contains one or more Note elements, each of which is used to provide any additional comments about an entry that cannot be captured using other elements.

**Structure** — xs:sequence (L453), children in this order

- L454 `Note` [1..unbounded] — required (cwe#R-0130); anonymous complexType (L455) — complex content (L456): extension of `cwe:StructuredTextType` (L457) adding attributes:
  - L458 `@Type` : cwe:NoteTypeEnumeration — required (cwe#R-0131)

## ObservedExampleType — complexType (L465–L480)

**Documentation**

- (L467 › ObservedExampleType) The ObservedExampleType complex type specifies references to a specific observed instance of a weakness in real-world products. Typically this will be a CVE reference. Each Observed_Example element represents a single example. The required Reference element should contain the identifier for the example being cited. For example, if a CVE is being cited, it should be of the standard CVE identifier format, such as CVE-2005-1951 or CVE-1999-0046. The required Description element should contain a brief description of the weakness being cited, without including irrelevant details such as the product name or attack vectors. The description should present an unambiguous correlation between the example being described and the weakness(es) that it is meant to exemplify. It should also be short and easy to understand. The Link element should provide a valid URL where more information regarding this example can be obtained.
  - extracted as: cwe#R-0132 (indicative), cwe#R-0133 (should), cwe#R-0134 (should), cwe#R-0135 (should), cwe#R-0136 (should), cwe#R-0137 (should), cwe#R-0138 (should)

**Structure** — xs:sequence (L469), children in this order

- L470 `Observed_Example` [1..unbounded] — required (cwe#R-0139); anonymous complexType (L471) — xs:sequence (L472), children in this order:
  - L473 `Reference` : xs:string [1..1] — required (cwe#R-0140)
  - L474 `Description` : cwe:StructuredTextType [1..1] — required (cwe#R-0141)
  - L475 `Link` : xs:anyURI [1..1] — required (cwe#R-0142)

## PotentialMitigationsType — complexType (L481–L500)

**Documentation**

- (L483 › PotentialMitigationsType) The PotentialMitigationsType complex type is used to describe potential mitigations associated with a weakness. It contains one or more Mitigation elements, which each represent individual mitigations for the weakness. The Phase element indicates the development life cycle phase during which this particular mitigation may be applied. The Strategy element describes a general strategy for protecting a system to which this mitigation contributes. The Effectiveness element summarizes how effective the mitigation may be in preventing the weakness. The Description element contains a description of this individual mitigation including any strengths and shortcomings of this mitigation for the weakness.
  - extracted as: cwe#R-0143 (indicative)
- (L484 › PotentialMitigationsType) The optional Mitigation_ID attribute is used by the internal CWE team to uniquely identify mitigations that are repeated across any number of individual weaknesses. To help make sure that the details of these common mitigations stay synchronized, the Mitigation_ID is used to quickly identify those mitigation elements across CWE that should be identical. The identifier is a string and should match the following format: MIT-1.
  - extracted as: cwe#R-0144 (should), cwe#R-0145 (should)

**Structure** — xs:sequence (L486), children in this order

- L487 `Mitigation` [1..unbounded] — required (cwe#R-0146); anonymous complexType (L488) — xs:sequence (L489), children in this order; then attributes:
  - L490 `Phase` : cwe:PhaseEnumeration [0..unbounded] — optional
  - L491 `Strategy` : cwe:MitigationStrategyEnumeration [0..1] — optional (cwe#R-0147)
  - L492 `Description` : cwe:StructuredTextType [1..1] — required (cwe#R-0148)
  - L493 `Effectiveness` : cwe:EffectivenessEnumeration [0..1] — optional (cwe#R-0149)
  - L494 `Effectiveness_Notes` : cwe:StructuredTextType [0..1] — optional
  - L496 `@Mitigation_ID` : xs:string — optional

## ReasonsType — complexType (L501–L512)

**Documentation**

- (L503 › ReasonsType) The ReasonsType complex type is used to identify the different reasons to why a CWE should not be considered.

**Structure** — xs:sequence (L505), children in this order

- L506 `Reason` [1..unbounded] — required (cwe#R-0150); anonymous complexType (L507) — attributes only:
  - L508 `@Type` : cwe:ReasonEnumeration — required (cwe#R-0151)

## ReferencesType — complexType (L513–L525)

**Documentation**

- (L515 › ReferencesType) The ReferencesType complex type contains one or more reference elements, each of which is used to link to an external reference defined within the catalog. The required External_Reference_ID attribute represents the external reference entry being linked to (e.g., REF-1). Text or quotes within the same CWE entity can cite this External_Reference_ID similar to how a footnote is used, and should use the format [REF-1]. The optional Section attribute holds any section title or page number that is specific to this use of the reference.
  - extracted as: cwe#R-0152 (references, inferred), cwe#R-0153 (should)

**Structure** — xs:sequence (L517), children in this order

- L518 `Reference` [1..unbounded] — required (cwe#R-0154); anonymous complexType (L519) — attributes only:
  - L520 `@External_Reference_ID` : xs:string — required (cwe#R-0155)
  - L521 `@Section` : xs:string — optional

## RelatedAttackPatternsType — complexType (L526–L537)

**Documentation**

- (L528 › RelatedAttackPatternsType) The RelatedAttackPatternsType complex type contains references to attack patterns associated with this weakness. The association implies those attack patterns may be applicable if an instance of this weakness exists. Each related attack pattern is identified by a CAPEC identifier.

**Structure** — xs:sequence (L530), children in this order

- L531 `Related_Attack_Pattern` [1..unbounded] — required (cwe#R-0156); anonymous complexType (L532) — attributes only:
  - L533 `@CAPEC_ID` : xs:integer — required (cwe#R-0157)

## RelatedWeaknessesType — complexType (L538–L553)

**Documentation**

- (L540 › RelatedWeaknessesType) The RelatedWeaknessesType complex type is used to refer to other weaknesses that differ only in their level of abstraction. It contains one or more Related_Weakness elements, each of which is used to link to the CWE identifier of the other Weakness. The nature of the relation is captured by the Nature attribute. Please see the RelatedNatureEnumeration simple type definition for details about the valid value and meanings. The optional Chain_ID attribute specifies the unique ID of a named chain that a CanFollow or CanPrecede relationship pertains to. The optional Ordinal attribute is used to determine if this relationship is the primary ChildOf relationship for this weakness for a given View_ID. This attribute can only have the value "Primary" and should only be included for the primary parent/child relationship. For each unique triple of &lt;Nature, CWE_ID, View_ID&gt;, there should be only one relationship that is given a "Primary" ordinal.
  - extracted as: cwe#R-0158 (references, inferred), cwe#R-0159 (only, inferred), cwe#R-0160 (may-only), cwe#R-0161 (should-only), cwe#R-0162 (should-only)

**Structure** — xs:sequence (L542), children in this order

- L543 `Related_Weakness` [1..unbounded] — required (cwe#R-0163); anonymous complexType (L544) — attributes only:
  - L545 `@Nature` : cwe:RelatedNatureEnumeration — required (cwe#R-0164)
  - L546 `@CWE_ID` : xs:integer — required (cwe#R-0165)
  - L547 `@View_ID` : xs:integer — required (cwe#R-0166)
  - L548 `@Chain_ID` : xs:integer — optional
  - L549 `@Ordinal` : cwe:OrdinalEnumeration — optional

## RelationshipsType — complexType (L554–L565)

**Documentation**

- (L556 › RelationshipsType) The RelationshipsType complex type provides elements to show the associated relationships with a given view or category. The Member_Of element is used to denote the individual categories that are included as part of the target view. The Has_Member element is used to define the weaknesses or other categories that are grouped together by a category. In both cases, the required MemberType's CWE_ID attribute specifies the unique CWE ID that is the target entry of the relationship, while the View_ID specifies which view the given relationship is relevant to.
  - extracted as: cwe#R-0167 (references, inferred), cwe#R-0168 (references, inferred)

**Structure** — xs:choice (L558)

- L558 xs:choice [1†..1†] — one branch per occurrence (cwe#R-0169):
  - branch 1: L559 xs:sequence [1†..1†] — children in this order:
    - L560 `Member_Of` : cwe:MemberType [1..unbounded] — required in this branch (cwe#R-0170)
    - L561 `Has_Member` : cwe:MemberType [0..unbounded] — optional
  - branch 2: L563 `Has_Member` : cwe:MemberType [1..unbounded] — required in this branch (cwe#R-0171)

## SuggestionsType — complexType (L566–L578)

**Documentation**

- (L568 › SuggestionsType) The SuggestionsType complex type is used to suggest other CWE entries that might be more appropriate to use for mapping.
  - extracted as: cwe#R-0172 (references, inferred)

**Structure** — xs:sequence (L570), children in this order

- L571 `Suggestion` [1..unbounded] — required (cwe#R-0173); anonymous complexType (L572) — attributes only:
  - L573 `@CWE_ID` : xs:integer — required (cwe#R-0174)
  - L574 `@Comment` : xs:string — required (cwe#R-0175)

## TaxonomyMappingsType — complexType (L579–L595)

**Documentation**

- (L581 › TaxonomyMappingsType) The TaxonomyMappingsType complex type is used to provide a mapping from an entry (Weakness or Category) in CWE to an equivalent entry in a different taxonomy. The required Taxonomy_Name attribute identifies the taxonomy to which the mapping is being made. The Entry_ID and Entry_Name elements identify the ID and name of the entry which is being mapped. The Mapping_Fit element identifies how close the CWE is to the entry in the taxonomy.

**Structure** — xs:sequence (L583), children in this order

- L584 `Taxonomy_Mapping` [1..unbounded] — required (cwe#R-0176); anonymous complexType (L585) — xs:sequence (L586), children in this order; then attributes:
  - L587 `Entry_ID` : xs:string [0..1] — optional
  - L588 `Entry_Name` : xs:string [0..1] — optional
  - L589 `Mapping_Fit` : cwe:TaxonomyMappingFitEnumeration [0..1] — optional
  - L591 `@Taxonomy_Name` : cwe:TaxonomyNameEnumeration — required (cwe#R-0177)

## WeaknessOrdinalitiesType — complexType (L596–L610)

**Documentation**

- (L598 › WeaknessOrdinalitiesType) The WeaknessOrdinalitiesType complex type indicates potential ordering relationships with other weaknesses. The required Ordinality element identifies whether the weakness has a primary, resultant, or indirect relationship. The optional Description contains the context in which the relationship exists. It is important to note that it is possible for the same entry to be primary in some instances and resultant in others.
  - extracted as: cwe#R-0178 (indicative, inferred)

**Structure** — xs:sequence (L600), children in this order

- L601 `Weakness_Ordinality` [1..unbounded] — required (cwe#R-0179); anonymous complexType (L602) — xs:sequence (L603), children in this order:
  - L604 `Ordinality` : cwe:OrdinalityEnumeration [1..1] — required (cwe#R-0180)
  - L605 `Description` : xs:string [0..1] — optional

# ENUMERATIONS

_Source banner comment, L612._

## AbstractionEnumeration — simpleType (L614–L625)

**Documentation**

- (L616 › AbstractionEnumeration) The AbstractionEnumeration simple type defines the different abstraction levels that apply to a weakness. A "Pillar" is the most abstract type of weakness and represents a theme for all class/base/variant weaknesses related to it. A Pillar is different from a Category as a Pillar is still technically a type of weakness that describes a mistake, while a Category represents a common characteristic used to group related things. A "Class" is a weakness also described in a very abstract fashion, typically independent of any specific language or technology. More specific than a Pillar Weakness, but more general than a Base Weakness. Class level weaknesses typically describe issues in terms of 1 or 2 of the following dimensions: behavior, property, and resource. A "Base" is a more specific type of weakness that is still mostly independent of a resource or technology, but with sufficient details to provide specific methods for detection and prevention. Base level weaknesses typically describe issues in terms of 2 or 3 of the following dimensions: behavior, property, technology, language, and resource. A "Variant" is a weakness that is linked to a certain type of product, typically involving a specific language or technology. More specific than a Base weakness. Variant level weaknesses typically describe issues in terms of 3 to 5 of the following dimensions: behavior, property, technology, language, and resource. A "Compound" weakness is a meaningful aggregation of several weaknesses, currently known as either a Chain or Composite.
  - extracted as: cwe#R-0198 (indicative, inferred)

**Values** — restriction of `xs:string` (L618); closed enumeration of 5 values:

- L619 `Pillar`
- L620 `Class`
- L621 `Base`
- L622 `Variant`
- L623 `Compound`

## ArchitectureClassEnumeration — simpleType (L626–L640)

**Documentation**

- (L628 › ArchitectureClassEnumeration) The ArchitectureClassEnumeration simple type contains a list of values corresponding to known classes of architectures. The value "Not Architecture-Specific" is used to indicate that the entry is not limited to a small set of architectures, i.e., it can appear in many different architectures.

**Values** — restriction of `xs:string` (L630); closed enumeration of 4 values:

- L631 `Embedded`
- L632 `Microcomputer`
- L633 `Workstation`
- L634 `Not Architecture-Specific`
  - (L636 › ArchitectureClassEnumeration › "Not Architecture-Specific") Used to indicate that the entry is not limited to a small set of architectures, i.e., it can appear in many different architectures

## ArchitectureNameEnumeration — simpleType (L641–L654)

**Documentation**

- (L643 › ArchitectureNameEnumeration) The ArchitectureNameEnumeration simple type contains a list of values corresponding to known architectures.

**Values** — restriction of `xs:string` (L645); closed enumeration of 7 values:

- L646 `Alpha`
- L647 `ARM`
- L648 `Itanium`
- L649 `Power Architecture`
- L650 `SPARC`
- L651 `x86`
- L652 `Other`

## DetectionMethodEnumeration — simpleType (L655–L680)

**Documentation**

- (L657 › DetectionMethodEnumeration) The DetectionMethodEnumeration simple type defines the different methods used to detect a weakness.

**Values** — restriction of `xs:string` (L659); closed enumeration of 19 values:

- L660 `Automated Analysis`
- L661 `Automated Dynamic Analysis`
- L662 `Automated Static Analysis`
- L663 `Automated Static Analysis - Source Code`
- L664 `Automated Static Analysis - Binary or Bytecode`
- L665 `Fuzzing`
- L666 `Manual Analysis`
- L667 `Manual Dynamic Analysis`
- L668 `Manual Static Analysis`
- L669 `Manual Static Analysis - Source Code`
- L670 `Manual Static Analysis - Binary or Bytecode`
- L671 `White Box`
- L672 `Black Box`
- L673 `Architecture or Design Review`
- L674 `Dynamic Analysis with Manual Results Interpretation`
- L675 `Dynamic Analysis with Automated Results Interpretation`
- L676 `Formal Verification`
- L677 `Simulation / Emulation`
- L678 `Other`

## DetectionEffectivenessEnumeration — simpleType (L681–L697)

**Documentation**

- (L683 › DetectionEffectivenessEnumeration) The DetectionEffectivenessEnumeration simple type defines the different levels of effectiveness that a detection method may have in detecting an associated weakness. The value "High" is used to describe a method that succeeds frequently and does not result in many false reports. The value "Moderate" is used to describe a method that is applicable to multiple circumstances, but it may not have complete coverage of the weakness, or it may result in a number of incorrect reports. The "SOAR Partial" value means that according to SOAR this method can be cost-effective for partial coverage of the objective. The value "Opportunistic" is used to describe a method that does not directly target the weakness but may still succeed by chance, rather than in a reliable manner. The value "Limited" is used to describe a method that may be useful in limited circumstances, only applicable to a subset of potential instances of a given weakness type, requires training/customization, or gives limited visibility. Even in its limited capacity, this may be part of a good defense in depth strategy. The value "None" is used to describe a method that is highly unlikely to work. However, it may be included in an entry to emphasize common, yet incorrect, methods that developers might introduce.
  - extracted as: cwe#R-0181 (may)

**Values** — restriction of `xs:string` (L685); closed enumeration of 6 values:

- L686 `High`
- L687 `Moderate`
- L688 `SOAR Partial`
  - (L690 › DetectionEffectivenessEnumeration › "SOAR Partial") Used to indicate that according to the IATAC State Of the Art Report (SOAR), the detection method is partially effective.
- L693 `Opportunistic`
- L694 `Limited`
- L695 `None`

## EffectivenessEnumeration — simpleType (L698–L711)

**Documentation**

- (L700 › EffectivenessEnumeration) The EffectivenessEnumeration simple type defines the different values related to how effective a mitigation may be in preventing the weakness. A value of "High" means the mitigation is frequently successful in eliminating the weakness entirely. A value of "Moderate" means the mitigation will prevent the weakness in multiple forms, but it does not have complete coverage of the weakness. A value of "Limited" means the mitigation may be useful in limited circumstances, or it is only applicable to a subset of potential errors of this weakness type. A value of "Incidental" means the mitigation is generally not effective and will only provide protection by chance, rather than in a reliable manner. A value of "Defense in Depth" means the mitigation may not necessarily prevent the weakness, but it may help to minimize the potential impact of an attacker exploiting the weakness. A value of "Discouraged Common Practice" is used to indicate mitigations that are commonly attempted but known to be ineffective or highly risky.

**Values** — restriction of `xs:string` (L702); closed enumeration of 7 values:

- L703 `High`
- L704 `Moderate`
- L705 `Limited`
- L706 `Incidental`
- L707 `Discouraged Common Practice`
- L708 `Defense in Depth`
- L709 `None`

## FunctionalAreaEnumeration — simpleType (L712–L742)

**Documentation**

- (L714 › FunctionalAreaEnumeration) The FunctionalAreaEnumeration simple type defines the different functional areas in which the weakness may appear. The value "Functional-Area-Independent" is used to indicate that the entry is not limited to a small set of functional areas, i.e., it can appear in many different functional areas

**Values** — restriction of `xs:string` (L716); closed enumeration of 20 values:

- L717 `Authentication`
- L718 `Authorization`
- L719 `Code Libraries`
- L720 `Counters`
- L721 `Cryptography`
- L722 `Error Handling`
- L723 `Interprocess Communication`
- L724 `File Processing`
- L725 `Logging`
- L726 `Memory Management`
- L727 `Networking`
- L728 `Number Processing`
- L729 `Program Invocation`
- L730 `Protection Mechanism`
- L731 `Session Management`
- L732 `Signals`
- L733 `String Processing`
- L734 `Not Functional-Area-Specific`
  - (L736 › FunctionalAreaEnumeration › "Not Functional-Area-Specific") Used to indicate that the entry is not limited to a small set of functional areas, i.e., it can appear in many different functional areas
- L739 `Power`
- L740 `Clock`

## ImportanceEnumeration — simpleType (L743–L751)

**Documentation**

- (L745 › ImportanceEnumeration) The ImportanceEnumeration simple type lists different values for importance.

**Values** — restriction of `xs:string` (L747); closed enumeration of 2 values:

- L748 `Normal`
- L749 `Critical`

## LanguageClassEnumeration — simpleType (L752–L769)

**Documentation**

- (L754 › LanguageClassEnumeration) The LanguageClassEnumeration simple type contains a list of values corresponding to different classes of source code languages. The same language could belong to multiple language classes, such as 'Object-Oriented' and 'Memory-Unsafe'. The value "Not Language-Specific" is used to indicate that the entry is not limited to a small set of languages.

**Values** — restriction of `xs:string` (L756); closed enumeration of 7 values:

- L757 `Assembly`
- L758 `Compiled`
- L759 `Hardware Description Language`
- L760 `Interpreted`
- L761 `Object-Oriented`
- L762 `Memory-Unsafe`
- L763 `Not Language-Specific`
  - (L765 › LanguageClassEnumeration › "Not Language-Specific") Used to indicate that the entry is not limited to a small set of language classes, i.e., it can appear in many different language classes.

## LanguageNameEnumeration — simpleType (L770–L810)

**Documentation**

- (L772 › LanguageNameEnumeration) The LanguageNameEnumeration simple type contains a list of values corresponding to different source code languages or data formats.

**Values** — restriction of `xs:string` (L774); closed enumeration of 34 values:

- L775 `Ada`
- L776 `ARM Assembly`
- L777 `ASP`
- L778 `ASP.NET`
- L779 `Basic`
- L780 `C`
- L781 `C++`
- L782 `C#`
- L783 `COBOL`
- L784 `Fortran`
- L785 `F#`
- L786 `Go`
- L787 `HTML`
- L788 `Java`
- L789 `JavaScript`
- L790 `JSON`
- L791 `JSP`
- L792 `Objective-C`
- L793 `Pascal`
- L794 `Perl`
- L795 `PHP`
- L796 `Pseudocode`
- L797 `Python`
- L798 `Ruby`
- L799 `Rust`
- L800 `Shell`
- L801 `SQL`
- L802 `Swift`
- L803 `VB.NET`
- L804 `Verilog`
- L805 `VHDL`
- L806 `XML`
- L807 `x86 Assembly`
- L808 `Other`

## LikelihoodEnumeration — simpleType (L811–L821)

**Documentation**

- (L813 › LikelihoodEnumeration) The LikelihoodEnumeration simple type contains a list of values corresponding to different likelihoods. The value "Unknown" should be used when the actual likelihood of something occurring is not known.
  - extracted as: cwe#R-0182 (should)

**Values** — restriction of `xs:string` (L815); closed enumeration of 4 values:

- L816 `High`
- L817 `Medium`
- L818 `Low`
- L819 `Unknown`

## MitigationStrategyEnumeration — simpleType (L822–L842)

**Documentation**

- (L824 › MitigationStrategyEnumeration) The MitigationStrategyEnumeration simple type lists general strategies for protecting a system to which a mitigation contributes.

**Values** — restriction of `xs:string` (L826); closed enumeration of 14 values:

- L827 `Attack Surface Reduction`
- L828 `Compilation or Build Hardening`
- L829 `Enforcement by Conversion`
- L830 `Environment Hardening`
- L831 `Firewall`
- L832 `Input Validation`
- L833 `Language Selection`
- L834 `Libraries or Frameworks`
- L835 `Resource Limitation`
- L836 `Output Encoding`
- L837 `Parameterization`
- L838 `Refactoring`
- L839 `Sandbox or Jail`
- L840 `Separation of Privilege`

## NoteTypeEnumeration — simpleType (L843–L856)

**Documentation**

- (L845 › NoteTypeEnumeration) The NoteTypeEnumeration simple type defines the different types of notes that can be associated with a weakness. An "Applicable Platform" note provides additional information about the list of applicable platforms for a given weakness. A "Maintenance" note contains significant maintenance tasks within this entry that still need to be addressed, such as clarifying the concepts involved or improving relationships. A "Relationship" note provides clarifying details regarding the relationships between entities. A "Research Gap" note identifies potential opportunities for the vulnerability research community to conduct further exploration of issues related to this weakness. It is intended to highlight parts of CWE that have not received sufficient attention from researchers. A "Terminology" note contains a discussion of terminology issues related to this weakness, or clarifications when there is no established terminology, or if there are multiple uses of the same key term. It is different from the Alternate_Terms element, which is focused on specific terms that are commonly used. A "Theoretical" note describes the weakness using vulnerability theory concepts. It should be provided as needed, especially in cases where the application of vulnerability theory is not necessarily obvious for the weakness.
  - extracted as: cwe#R-0183 (should)

**Values** — restriction of `xs:string` (L847); closed enumeration of 7 values:

- L848 `Applicable Platform`
- L849 `Maintenance`
- L850 `Relationship`
- L851 `Research Gap`
- L852 `Terminology`
- L853 `Theoretical`
- L854 `Other`

## OrdinalEnumeration — simpleType (L857–L864)

**Documentation**

- (L859 › OrdinalEnumeration) The OrdinalEnumeration simple type contains a list of values used to determine if a relationship is the primary relationship for a given weakness entry within a given view. Currently, this attribute can only have the value "Primary".
  - extracted as: cwe#R-0184 (may-only)

**Values** — restriction of `xs:string` (L861); closed enumeration of 1 values:

- L862 `Primary`

## OrdinalityEnumeration — simpleType (L865–L874)

**Documentation**

- (L867 › OrdinalityEnumeration) The OrdinalityEnumeration simple type contains a list of values used to indicates potential ordering relationships with other weaknesses. A primary relationship means the weakness exists independent of other weaknesses, while a resultant relationship is when a weakness exists only in the presence of some other weaknesses. An indirect relationship means the weakness does not directly lead to security-relevant weaknesses but is a quality issue that might indirectly make it easier to introduce security-relevant weaknesses or make them more difficult to detect.

**Values** — restriction of `xs:string` (L869); closed enumeration of 3 values:

- L870 `Indirect`
- L871 `Primary`
- L872 `Resultant`

## OperatingSystemClassEnumeration — simpleType (L875–L890)

**Documentation**

- (L877 › OperatingSystemClassEnumeration) The OperatingSystemClassEnumeration simple type contains a list of values corresponding to different classes of operating systems. The value "Not OS-Specific" is used to indicate that the entry is not limited to a small set of operating system classes, i.e., it can appear in many different operating system classes.

**Values** — restriction of `xs:string` (L879); closed enumeration of 5 values:

- L880 `Linux`
- L881 `macOS`
- L882 `Unix`
- L883 `Windows`
- L884 `Not OS-Specific`
  - (L886 › OperatingSystemClassEnumeration › "Not OS-Specific") Used to indicate that the entry is not limited to a small set of operating system classes, i.e., it can appear in many different operating system classes.

## OperatingSystemNameEnumeration — simpleType (L891–L916)

**Documentation**

- (L893 › OperatingSystemNameEnumeration) The OperatingSystemNameEnumeration simple type contains a list of values corresponding to different operating systems.

**Values** — restriction of `xs:string` (L895); closed enumeration of 19 values:

- L896 `AIX`
- L897 `Android`
- L898 `BlackBerry OS`
- L899 `Chrome OS`
- L900 `Darwin`
- L901 `FreeBSD`
- L902 `iOS`
- L903 `macOS`
- L904 `NetBSD`
- L905 `OpenBSD`
- L906 `Red Hat`
- L907 `Solaris`
- L908 `SUSE`
- L909 `tvOS`
- L910 `Ubuntu`
- L911 `watchOS`
- L912 `Windows 9x`
- L913 `Windows Embedded`
- L914 `Windows NT`

## PhaseEnumeration — simpleType (L917–L940)

**Documentation**

- (L919 › PhaseEnumeration) The PhaseEnumeration simple type lists different phases in the product life cycle.

**Values** — restriction of `xs:string` (L921); closed enumeration of 17 values:

- L922 `Policy`
- L923 `Requirements`
- L924 `Architecture and Design`
- L925 `Implementation`
- L926 `Build and Compilation`
- L927 `Testing`
- L928 `Documentation`
- L929 `Bundling`
- L930 `Distribution`
- L931 `Installation`
- L932 `System Configuration`
- L933 `Operation`
- L934 `Patching and Maintenance`
- L935 `Porting`
- L936 `Integration`
- L937 `Manufacturing`
- L938 `Decommissioning and End-of-Life`

## PrevalenceEnumeration — simpleType (L941–L951)

**Documentation**

- (L943 › PrevalenceEnumeration) The PrevalenceEnumeration simple type defines the different regularities that guide the applicability of platforms.

**Values** — restriction of `xs:string` (L945); closed enumeration of 4 values:

- L946 `Often`
- L947 `Sometimes`
- L948 `Rarely`
- L949 `Undetermined`

## ReasonEnumeration — simpleType (L952–L970)

**Documentation**

- (L954 › ReasonEnumeration) The ReasonEnumeration simple type holds all the different types of reasons to why a CWE might not be considered for mapping.

**Values** — restriction of `xs:string` (L956); closed enumeration of 12 values:

- L957 `Abstraction`
- L958 `Category`
- L959 `View`
- L960 `Deprecated`
- L961 `Potential Deprecation`
- L962 `Frequent Misuse`
- L963 `Frequent Misinterpretation`
- L964 `Multiple Use`
- L965 `CWE Overlap`
- L966 `Acceptable-Use`
- L967 `Potential Major Changes`
- L968 `Other`

## RelatedNatureEnumeration — simpleType (L971–L986)

**Documentation**

- (L973 › RelatedNatureEnumeration) The RelatedNatureEnumeration simple type defines the different values that can be used to define the nature of a related weakness. A ChildOf nature denotes a related weakness at a higher level of abstraction. A ParentOf nature denotes a related weakness at a lower level of abstraction. The StartsWith, CanPrecede, and CanFollow relationships are used to denote weaknesses that are part of a chaining structure. The RequiredBy and Requires relationships are used to denote a weakness that is part of a composite weakness structure. The CanAlsoBe relationship denotes a weakness that, in the proper environment and context, can also be perceived as the target weakness. Note that the CanAlsoBe relationship is not necessarily reciprocal. The PeerOf relationship is used to show some similarity with the target weakness that does not fit any of the other type of relationships.
  - extracted as: cwe#R-0185 (indicative, inferred)

**Values** — restriction of `xs:string` (L975); closed enumeration of 9 values:

- L976 `ChildOf`
- L977 `ParentOf`
- L978 `StartsWith`
- L979 `CanFollow`
- L980 `CanPrecede`
- L981 `RequiredBy`
- L982 `Requires`
- L983 `CanAlsoBe`
- L984 `PeerOf`

## ResourceEnumeration — simpleType (L987–L998)

**Documentation**

- (L989 › ResourceEnumeration) The ResourceEnumeration simple type defines different resources of a system.

**Values** — restriction of `xs:string` (L991); closed enumeration of 5 values:

- L992 `CPU`
- L993 `File or Directory`
- L994 `Memory`
- L995 `System Process`
- L996 `Other`

## ScopeEnumeration — simpleType (L999–L1014)

**Documentation**

- (L1001 › ScopeEnumeration) The ScopeEnumeration simple type defines the different areas of security that can be affected by exploiting a weakness.

**Values** — restriction of `xs:string` (L1003); closed enumeration of 9 values:

- L1004 `Confidentiality`
- L1005 `Integrity`
- L1006 `Availability`
- L1007 `Access Control`
- L1008 `Accountability`
- L1009 `Authentication`
- L1010 `Authorization`
- L1011 `Non-Repudiation`
- L1012 `Other`

## StatusEnumeration — simpleType (L1015–L1027)

**Documentation**

- (L1017 › StatusEnumeration) The StatusEnumeration simple type defines the different status values that an entity (view, category, weakness) can have. A value of Deprecated refers to an entity that has been removed from CWE, likely because it was a duplicate or was created in error. A value of Obsolete is used when an entity is still valid but no longer is relevant, likely because it has been superseded by a more recent entity. A value of Incomplete means that the entity does not have all important elements filled, and there is no guarantee of quality. A value of Draft refers to an entity that has all important elements filled, and critical elements such as Name and Description are reasonably well-written; the entity may still have important problems or gaps. A value of Usable refers to an entity that has received close, extensive review, with critical elements verified. A value of Stable indicates that all important elements have been verified, and the entry is unlikely to change significantly in the future. Note that the quality requirements for Draft and Usable status are very resource-intensive to accomplish, while some Incomplete and Draft entries are actively used by the general public; so, this status enumeration might change in the future.
  - extracted as: cwe#R-0186 (defines), cwe#R-0187 (defines)

**Values** — restriction of `xs:string` (L1019); closed enumeration of 6 values:

- L1020 `Deprecated`
- L1021 `Draft`
- L1022 `Incomplete`
- L1023 `Obsolete`
- L1024 `Stable`
- L1025 `Usable`

## StakeholderEnumeration — simpleType (L1028–L1047)

**Documentation**

- (L1030 › StakeholderEnumeration) The StakeholderEnumeration simple type defines the different types of users within the CWE community.

**Values** — restriction of `xs:string` (L1032); closed enumeration of 13 values:

- L1033 `Academic Researchers`
- L1034 `Applied Researchers`
- L1035 `Assessment Teams`
- L1036 `Assessment Tool Vendors`
- L1037 `CWE Team`
- L1038 `Educators`
- L1039 `Hardware Designers`
- L1040 `Information Providers`
- L1041 `Product Customers`
- L1042 `Product Vendors`
- L1043 `Software Developers`
- L1044 `Vulnerability Analysts`
- L1045 `Other`

## StructureEnumeration — simpleType (L1048–L1057)

**Documentation**

- (L1050 › StructureEnumeration) The StructureEnumeration simple type lists the different structural natures of a weakness. A Simple structure represents a single weakness whose exploitation is not dependent on the presence of another weakness. A Composite is a set of weaknesses that must all be present simultaneously in order to produce an exploitable vulnerability, while a Chain is a set of weaknesses that must be reachable consecutively in order to produce an exploitable vulnerability.
  - extracted as: cwe#R-0188 (defines), cwe#R-0189 (defines)

**Values** — restriction of `xs:string` (L1052); closed enumeration of 3 values:

- L1053 `Chain`
- L1054 `Composite`
- L1055 `Simple`

## StructuredCodeNatureEnumeration — simpleType (L1058–L1070)

**Documentation**

- (L1060 › StructuredCodeNatureEnumeration) The StructuredCodeNatureEnumeration sinple type defines the different values that state what type of code is being shown in an eample.

**Values** — restriction of `xs:string` (L1062); closed enumeration of 6 values:

- L1063 `Attack`
- L1064 `Bad`
- L1065 `Good`
- L1066 `Informative`
- L1067 `Mitigation`
- L1068 `Result`

## TaxonomyMappingFitEnumeration — simpleType (L1071–L1082)

**Documentation**

- (L1073 › TaxonomyMappingFitEnumeration) The TaxonomyMappingFitEnumeration simple type defines the different values used to describe how close a certain mapping to CWE is.

**Values** — restriction of `xs:string` (L1075); closed enumeration of 5 values:

- L1076 `Exact`
- L1077 `CWE More Abstract`
- L1078 `CWE More Specific`
- L1079 `Imprecise`
- L1080 `Perspective`

## TaxonomyNameEnumeration — simpleType (L1083–L1116)

**Documentation**

- (L1085 › TaxonomyNameEnumeration) The TaxonomyNameEnumeration simple type lists the different known taxomomies that can be mapped to CWE.

**Values** — restriction of `xs:string` (L1087); closed enumeration of 27 values:

- L1088 `7 Pernicious Kingdoms`
- L1089 `19 Deadly Sins`
- L1090 `Aslam`
- L1091 `Bishop`
- L1092 `CERT C Secure Coding`
- L1093 `CERT C++ Secure Coding`
- L1094 `The CERT Oracle Secure Coding Standard for Java (2011)`
- L1095 `CLASP`
- L1096 `ISA/IEC 62443`
- L1097 `Landwehr`
- L1098 `OMG ASCSM`
- L1099 `OMG ASCRM`
- L1100 `OMG ASCMM`
- L1101 `OMG ASCPEM`
- L1102 `OWASP Top Ten 2004`
- L1103 `OWASP Top Ten 2007`
- L1104 `OWASP Top Ten`
- L1105 `PLOVER`
- L1106 `Protection Analysis`
- L1107 `RISOS`
- L1108 `SEI CERT C Coding Standard`
- L1109 `SEI CERT C++ Coding Standard`
- L1110 `SEI CERT Oracle Coding Standard for Java`
- L1111 `SEI CERT Perl Coding Standard`
- L1112 `Software Fault Patterns`
- L1113 `Weber, Karger, Paradkar`
- L1114 `WASC`

## TechnicalImpactEnumeration — simpleType (L1117–L1157)

**Documentation**

- (L1119 › TechnicalImpactEnumeration) The TechnicalImpactEnumeration simple type describes the technical impacts that can arise if an adversary successfully exploits a weakness.

**Values** — restriction of `xs:string` (L1121); closed enumeration of 25 values:

- L1122 `Modify Memory`
- L1123 `Read Memory`
- L1124 `Modify Files or Directories`
- L1125 `Read Files or Directories`
- L1126 `Modify Application Data`
- L1127 `Read Application Data`
- L1128 `DoS: Crash, Exit, or Restart`
- L1129 `DoS: Amplification`
- L1130 `DoS: Instability`
- L1131 `DoS: Resource Consumption (CPU)`
- L1132 `DoS: Resource Consumption (Memory)`
- L1133 `DoS: Resource Consumption (Other)`
- L1134 `Execute Unauthorized Code or Commands`
- L1135 `Gain Privileges or Assume Identity`
- L1136 `Bypass Protection Mechanism`
- L1137 `Hide Activities`
- L1138 `Alter Execution Logic`
- L1139 `Quality Degradation`
- L1140 `Unexpected State`
- L1141 `Varies by Context`
- L1142 `Increase Analytical Complexity`
  - (L1144 › TechnicalImpactEnumeration › "Increase Analytical Complexity") It is more difficult for humans or tools to analyze the product's code, documentation, and other artifacts understand how the product works or is intended to work, which can make it more difficult to find and fix vulnerabilities.
- L1152 `Reduce Maintainability`
- L1153 `Reduce Performance`
- L1154 `Reduce Reliability`
- L1155 `Other`

## TechnologyClassEnumeration — simpleType (L1158–L1202)

**Documentation**

- (L1160 › TechnologyClassEnumeration) The TechnologyClassEnumeration simple type contains a list of values corresponding to different classes of technologies. The value "Not Technology-Specific" is used to indicate that the entry is not limited to a small set of technologies, i.e., it can appear in many different technologies.

**Values** — restriction of `xs:string` (L1162); closed enumeration of 10 values:

- L1163 `Client Server`
  - (L1165 › TechnologyClassEnumeration › "Client Server") Represents technology involving a distributed application but for the purposes of CWE does not leverage a web browser.
- L1168 `Cloud Computing`
  - (L1170 › TechnologyClassEnumeration › "Cloud Computing") Represents technology that involves data storage and computing power being made available to multiple users via the internet instead of using local systems, without the need for users to perform all system management themselves.
- L1173 `ICS/OT`
  - (L1175 › TechnologyClassEnumeration › "ICS/OT") Represents technology related to Industrial Control Systems (ICS) and Operational Techology (OT), which are often considered to be distinct from Information Technology (IT) systems.
- L1178 `Mainframe`
- L1179 `Mobile`
- L1180 `N-Tier`
- L1181 `SOA`
  - (L1183 › TechnologyClassEnumeration › "SOA") Represents technology related to Service-oriented architecture (SOA).
- L1186 `System on Chip`
  - (L1188 › TechnologyClassEnumeration › "System on Chip") Represents technology that integrates all components of a computer within a single integrated circuit, to include FPGA and ASIC.
- L1191 `Web Based`
  - (L1193 › TechnologyClassEnumeration › "Web Based") Represents technology that involves applications or single-page sites that leverage a web browser to support client interactions.
- L1196 `Not Technology-Specific`
  - (L1198 › TechnologyClassEnumeration › "Not Technology-Specific") Used to indicate that the entry is not limited to a small set of technologies, i.e., it can appear in many different technologies.

## TechnologyNameEnumeration — simpleType (L1203–L1286)

**Documentation**

- (L1205 › TechnologyNameEnumeration) The TechnologyNameEnumeration simple type contains a list of values corresponding to different technologies. A technology represents a generally accepted feature of a system and often refers to a high-level functional component within a system.
- (L1206 › TechnologyNameEnumeration) Within this context, "IP" stands for "Intellectual Property" and is the term used to distinguish unique blocks within a System on Chip, with each block potentially coming from a different source.

**Values** — restriction of `xs:string` (L1208); closed enumeration of 20 values:

- L1209 `AI/ML`
  - (L1211 › TechnologyNameEnumeration › "AI/ML") Represents technology related to Artificial Intelligence (AI) and Machine Learning (ML) systems. Note: terminology in this space is inconsistently used, but the AI WG agreed on this usage for CWE 4.15.
- L1214 `Web Server`
- L1215 `Database Server`
- L1216 `Accelerator Hardware`
  - (L1218 › TechnologyNameEnumeration › "Accelerator Hardware") hardware Intellectual Property (IP) dedicated to offload a specific workload to enhance performance: DSP, packet processing, mathematical, compression, etc.
- L1221 `Analog and Mixed Signal Hardware`
  - (L1223 › TechnologyNameEnumeration › "Analog and Mixed Signal Hardware") hardware Intellectual Property (IP) that controls/senses the electricals for communication which receives/transmits signals conditioned outside of a system’s digital domain.
- L1226 `Audio/Video Hardware`
  - (L1228 › TechnologyNameEnumeration › "Audio/Video Hardware") hardware Intellectual Property (IP) designed to manipulate audio/video data: coders/decoders, speech recognition, format converters, etc.
- L1231 `Bus/Interface Hardware`
  - (L1233 › TechnologyNameEnumeration › "Bus/Interface Hardware") hardware Intellectual Property (IP) implementing an interconnect among elements in a computing system: I2C, PCIe, DDR, MMC, USB, GPIO, NoC, etc.
- L1236 `Clock/Counter Hardware`
  - (L1238 › TechnologyNameEnumeration › "Clock/Counter Hardware") hardware Intellectual Property (IP) reflecting the passage of time in oscillations or human units: Real Time Clock, Watchdog, Monotonic Counter, etc.
- L1241 `Communication Hardware`
  - (L1243 › TechnologyNameEnumeration › "Communication Hardware") hardware Intellectual Property (IP) designed to transmit/receive information: Modulator/Demodulator, GPS, 802.11, Bluetooth, CDMA/DSM, etc.
- L1246 `Controller Hardware`
  - (L1248 › TechnologyNameEnumeration › "Controller Hardware") hardware Intellectual Property (IP) circuit hard-wired (e.g., an FSM) to react in a closed-loop control system or other limited context, to control another entity: Arbiter, APIC, USB, Peripheral, Memory, Storage, etc.
- L1251 `Memory Hardware`
  - (L1253 › TechnologyNameEnumeration › "Memory Hardware") hardware Intellectual Property (IP) implementing volatile (transient) data storage: DRAM, SRAM, etc.
- L1256 `Microcontroller Hardware`
  - (L1258 › TechnologyNameEnumeration › "Microcontroller Hardware") hardware Intellectual Property (IP) implementing a specialized processor acting as a programmable controller.
- L1261 `Network on Chip Hardware`
- L1262 `Power Management Hardware`
  - (L1264 › TechnologyNameEnumeration › "Power Management Hardware") hardware Intellectual Property (IP) that controls and/or monitors the power state of a system: voltage regulators, power controllers, power monitors, etc.
- L1267 `Processor Hardware`
  - (L1269 › TechnologyNameEnumeration › "Processor Hardware") hardware Intellectual Property (IP) implementing a general-purpose computing engine: CPU, GPU, RISC, CISC, etc.
- L1272 `Security Hardware`
  - (L1274 › TechnologyNameEnumeration › "Security Hardware") hardware Intellectual Property (IP), including hardware security modules (HSM), designed to protect assets: cryptography, auth, tamper detection, etc.
- L1277 `Sensor Hardware`
- L1278 `Storage Hardware`
- L1279 `Test/Debug Hardware`
  - (L1281 › TechnologyNameEnumeration › "Test/Debug Hardware") hardware Intellectual Property (IP) designed to verify functionality and identify root cause of defects: JTAG, BIST, boundary scan, pattern generator, etc.
- L1284 `Other`

## UsageEnumeration — simpleType (L1287–L1313)

**Documentation**

- (L1289 › UsageEnumeration) The UsageEnumeration simple type is used for whether this CWE entry is supported for mapping.

**Values** — restriction of `xs:string` (L1291); closed enumeration of 4 values:

- L1292 `Discouraged`
  - (L1294 › UsageEnumeration › "Discouraged") this CWE ID should not be used to map to real-world vulnerabilities
    - extracted as: cwe#R-0190 (should not)
- L1297 `Prohibited`
  - (L1299 › UsageEnumeration › "Prohibited") this CWE ID must not be used to map to real-world vulnerabilities
    - extracted as: cwe#R-0191 (must not)
- L1302 `Allowed`
  - (L1304 › UsageEnumeration › "Allowed") this CWE ID may be used to map to real-world vulnerabilities
    - extracted as: cwe#R-0192 (may)
- L1307 `Allowed-with-Review`
  - (L1309 › UsageEnumeration › "Allowed-with-Review") this CWE ID could be used to map to real-world vulnerabilities in limited situations requiring careful review
    - extracted as: cwe#R-0193 (could)

## ViewTypeEnumeration — simpleType (L1314–L1323)

**Documentation**

- (L1316 › ViewTypeEnumeration) The ViewTypeEnumeration simple type defines the different types of views that can be found within CWE. A graph is a hierarchical representation of weaknesses based on a specific vantage point that a user may take. The hierarchy often starts with a category, followed by a class/base weakness, and ends with a variant weakness. In addition to graphs, a view can be a slice, which is a flat list of entries that does not specify any relationships between those entries. An explicit slice is a subset of weaknesses that are related through some external factor. For example, an explicit slice may be used to represent mappings to external groupings like a Top-N list. An implicit slice is a subset of weaknesses that are related through a specific attribute, as indicated by the Filter element of the View. For example, an implicit slice may refer to all weaknesses in draft status, or all class level weaknesses.

**Values** — restriction of `xs:string` (L1318); closed enumeration of 3 values:

- L1319 `Implicit`
- L1320 `Explicit`
- L1321 `Graph`

# STRUCTURED TEXT

_Source banner comment, L1325._

## StructuredTextType — complexType mixed="true" (L1327–L1334)

**Documentation**

- (L1329 › StructuredTextType) The StructuredTextType complex type is used to allow XHTML content embedded within standard string data. Some common elements are: &lt;BR/&gt; to insert a line break, &lt;UL&gt;&lt;LI/&gt;&lt;/UL&gt; to create a bulleted list, &lt;OL&gt;&lt;LI/&gt;&lt;/OL&gt; to create a numbered list, and &lt;DIV style="margin-left: 40px"&gt;&lt;/DIV&gt; to create a new indented section.

**Structure** — xs:sequence (L1331), children in this order. Mixed content: character data may appear between child elements

- L1332 `<xs:any namespace="http://www.w3.org/1999/xhtml" minOccurs="0" maxOccurs="unbounded" processContents="strict"/>` — element children only from the XHTML namespace, strictly validated (cwe#R-0194)

## StructuredCodeType — complexType mixed="true" (L1335–L1344)

**Documentation**

- (L1337 › StructuredCodeType) The StructuredCodeType complex type is used to present source code examples and other structured text that is not a regular paragraph. It allows embedded XHTML content to enable formatting of the code. The required Nature attribute states what type of code the example shows. The optional Language attribute states which source code language is used in the example. This is mostly appropriate when the Nature is "good" or "bad".
  - extracted as: cwe#R-0195 (indicative)

**Structure** — xs:sequence (L1339), children in this order; then attributes. Mixed content: character data may appear between child elements

- L1340 `<xs:any namespace="http://www.w3.org/1999/xhtml" minOccurs="0" maxOccurs="unbounded" processContents="strict"/>` — element children only from the XHTML namespace, strictly validated (cwe#R-0196)
- L1342 `@Language` : cwe:LanguageNameEnumeration — optional
- L1343 `@Nature` : cwe:StructuredCodeNatureEnumeration — required (cwe#R-0197)

## Extractor notes — source inconsistencies (not source text)

Recorded while extracting, not corrected; the declarations govern validation. Also in `requirements.yaml` › `source_defects`.

1. **D-01** (label-contradiction) CategoryType documentation calls Content_History optional (L123); the declaration has minOccurs="1" (L133). The declaration governs validation.
2. **D-02** (label-contradiction) ViewType documentation calls Content_History optional (L145); the declaration has minOccurs="1" (L156).
3. **D-03** (label-contradiction) AlternateTermsType documentation calls Description required (L199); the declaration has minOccurs="0" (L206).
4. **D-04** (label-contradiction) AudienceType documentation calls Description required (L251); the declaration has minOccurs="0" (L258).
5. **D-05** (label-contradiction) CommonConsequencesType documentation calls Impact optional (L274); the declaration has minOccurs="1" (L282).
6. **D-06** (wrong-value-name) FunctionalAreaEnumeration documentation names the value "Functional-Area-Independent" (L714); no such value exists, the declared value is "Not Functional-Area-Specific" (L734).
7. **D-07** (wrong-type-name) The documentation names "ModeOfIntroductionType" (L436); the type is declared ModesOfIntroductionType (L434).
8. **D-08** (value-case) StructuredCodeType documentation refers to Nature "good" or "bad" (L1337); the enumeration values are Good and Bad (L1064, L1065), and enumeration matching is case-sensitive.
9. **D-09** (example-markup) StructuredTextType documentation shows XHTML examples in upper case (BR, UL, LI, OL, DIV; L1329). XHTML 1.0 Strict element names are lower case, and xs:any with processContents="strict" (L1332) validates against that schema, so the examples taken literally would not validate.
10. **D-10** (ambiguous-rule) In 'For each unique triple of &lt;Nature, CWE_ID, View_ID&gt;' (L540) CWE_ID may be Related_Weakness/@CWE_ID (the target), which makes the rule vacuous, or the owning entry's ID, which means at most one Primary per Nature and View_ID within an entry.
11. **D-11** (ambiguous-semantics) ViewType documentation says Members defines "Member_Of relationships with categories" (L145); RelationshipsType documentation says Member_Of denotes categories included in the target view and Has_Member what a category groups (L556). The xs:choice (L558) allows either, so which element a View's Members carries is not stated consistently.
12. **D-12** (imprecise-description) RelatedWeaknessesType is described as referring to weaknesses "that differ only in their level of abstraction" (L540), but RelatedNatureEnumeration (L973) includes natures that are not abstraction relations (StartsWith, CanFollow, CanPrecede, RequiredBy, Requires, CanAlsoBe, PeerOf).
13. **D-13** (scope-wider-than-name) The identity constraint named uniqueWeaknessName selects ./cwe:*/cwe:* (L60): every child of every top-level container. External_Reference has no @Name, so @Name is unique across all Weaknesses, Categories and Views together, not only among weaknesses.
14. **D-14** (integrity-not-enforced) IDs are unique only within each kind (uniqueWeaknessID L55, uniqueCategoryID L63, uniqueViewID L67); nothing makes Weakness, Category and View IDs disjoint, although MemberType/@CWE_ID and Related_Weakness/@CWE_ID name entries by a single CWE_ID. The schema declares no xs:key or xs:keyref, so no reference (External_Reference_ID, CWE_ID, View_ID, Chain_ID) is checked by validation.
15. **D-15** (inconsistent-definition) "SOAR Partial" is described as "can be cost-effective for partial coverage of the objective" in the type documentation (L683) and as "the detection method is partially effective" in the value documentation (L690).
16. **D-16** (typos) Spelling and grammar slips kept verbatim, not corrected: "taxomomies" (L123, L1085), "to a identify" (L214), "functional_area elements" for Functional_Area (L409), "the valid value and meanings" (L540), "used to indicates" (L867), "sinple type" and "eample" (L1060), "artifacts understand" missing "to" (L1146), "Techology" (L1175).
