---
record: nistir-7695
kind: design-notes
title: "nistir-7695: bearing on our design (tmodel)"
extracted: "2026-10-18"
reviewed_by: ""
attribution: "Contains text from NIST IR 7695 (August 2011), published by NIST with no copyright or licence notice; works of NIST employees are not subject to copyright in the United States (17 U.S.C. 105), but two of the three authors were not NIST staff (Acknowledgments, p. iii), so the text is not claimed to be wholly a U.S. Government work. CPE is a trademark of The MITRE Corporation (p. iii)."
---

# NIST IR 7695 (CPE Naming 2.3): how it bears on the tmodel design

**Scope and provenance conventions.**

- A bare `§5.3.2`, `Figure 6-3` or `Table 6-1` is **NIST IR 7695**, *Common Platform Enumeration:
  Naming Specification Version 2.3* (August 2011; PDF SHA-256 `01553a46…f3f6`), quoted from its
  `pdftotext -layout` rendering `nistir7695.txt`. Locators read section / PDF page / line in that
  rendering (`§5 / p. 14 / L524`); in the body, the PDF page is the printed page plus 6. Curly
  quotation marks (“ ”) around a quotation are ours; inside one, every character is the source's,
  including its own curly marks and hyphens, except that an em dash (U+2014) is written
  `{U+2014}`, because house style forbids the character in this library (as in `normative.md`).
  PDF line breaks inside a quotation are joined and nothing else is changed. BCP 14 keywords are
  the source's own, read per RFC 2119 (§1.3).
- tmodel documents are cited by id from `Threat-Radar/tmodel` `main` at `1cb85b74` (2026-10-18);
  its research by file and section, for example `mapping.md` §10 for
  `research/0004-product-composition/mapping.md`. Markdown bold and italics are dropped from
  quotations of tmodel files; code marks are kept.
- **[analysis]** marks reasoning of this extraction that neither NIST IR 7695 nor tmodel's documents
  state. **[observation]** marks a tool run, a fetched file or an API response, with its date. “Our
  reading” marks an interpretation of a quoted sentence.
- `messages.yaml` decomposes every structure named here (`wfn`, `wfn-attribute-value-pair`,
  `logical-value`, `wfn-value-string`, `uri-binding`, `uri-packed-edition`,
  `formatted-string-binding`, `binding-language-tag`); its `constrained_by` keys hold the
  requirement ids that constrain each one. `R-NNNN` beside a locator, a quoted rule or a claim about
  the source is the `requirements.yaml` entry `nistir-7695#R-NNNN` that states the rule it rests on
  (added in pass 3, cross-check); a quotation without one has no entry of its own. RPT-0004's candidate rules (R-ID-1 to R-ID-5,
  R-MERGE-1, R-MERGE-2, R-MATCH-1, R-MATCH-2, R-RANGE-1 and the others in `mapping.md` §10) are a
  different series.
- Probes P1 to P9 run our own literal transcription of the §6 pseudocode (Python 3.13.9); E9 and
  E10 add checks against the XML schema §6 cites and PyYAML 6.0.3. The scripts and their outputs
  stayed in the extraction scratchpad and are not committed; E8 to E10 give the results.

**Decision status, stated plainly.** From `DECISIONS-0001` (v0.1.8, updated 2026-10-12) and the
ADRs it points to: **accepted** are DEC-001a (ADR-0010), DEC-002 (ADR-0007), DEC-003 (ADR-0006),
DEC-004 (ADR-0008), DEC-005 (ADR-0002), DEC-006 and DEC-010 (ADR-0003, with ADR-0009), DEC-007
(ADR-0001) and DEC-011 (ADR-0004); **open** are DEC-001b, DEC-008 and DEC-009. “A `DEC-*` is
accepted only by an `ADR-NNNN` file” (`DECISIONS-0001`). APP-0001 (A-001, A-043) is a draft, and
the ARCH-0001 proposal is at `0.2.0-proposed.15`. RPT-0004's rules are candidates: “It accepts
nothing. Every rule is a candidate for #15 and #17” (`mapping.md`). **Nothing below accepts,
rejects or changes a decision.** Every adopt, adapt and reject item is evidence and a
recommendation, routed to an open decision, an issue or the RPT-0004 report. One tmodel
inconsistency matters here: the LinkML description of `identifiers` still ends “Additive DRAFT
slot (DEC-001 open); not a new §13 class.”, while ADR-0010 accepted “the opaque multivalued
`identifiers` slot (purl/CPE/SBOM/firmware digest; ADR-0002 per-type instance identity)”. This note
treats the slot as accepted (open question 14).

**What CPE Naming 2.3 is, for tmodel.** It defines the string that the accepted `identifiers` slot
already carries: the LinkML example `"cpe:2.3:a:openssl:openssl:3.0.2:*:*:*:*:*:*:*"` and 16
strings in the example vectors (E7). It is also the name NVD keys its applicability data on, so it
is the bridge from a Component to a CVE wherever no ecosystem or distribution advisory covers the
package (`report.md` §5). Its scope is the name only; other versions are out of scope, “as are all
CPE specifications other than CPE Naming” (§1.1 / p. 7 / L227), so matching (NIST IR 7696),
dictionaries (NIST IR 7697) and applicability statements (NIST IR 7698) are separate records.
**[analysis]** Three properties organise everything below. First, a CPE names a class, never an instance: “WFNs are used
solely for product classes. They cannot identify product instances” (§5 / p. 14 / L524). Second,
the syntax is defined to the character and the values not at all: “Defining procedures and
guidelines for assigning “correct” or “valid” values to attributes of product descriptions or
identifiers” is out of scope (§5 / p. 14 / L533), so a perfectly formed CPE can be a guess (E1).
Third, the canonical form is an abstract structure, not a string: “an abstract canonical form{U+2014}a
kind of interlingua{U+2014}was chosen to serve as the standardized form for processing CPE information”
(§3.2 / p. 11 / L416). One WFN has two bindings with different spellings, the two unbinding
procedures disagree about case, and the printed pseudocode does not reproduce its own examples
(defects 13 to 16). tmodel's open design questions sit on the second and third points.

---

## What we adopt

**Adopt-1. Keep every CPE exactly as received, as a string, in the `identifiers` slot.**
NIST IR 7695 makes the bound string the thing that is exchanged: the formatted string is “a
colon-delimited list of fields prefixed with the string "cpe:2.3:"” (§6.2 / p. 37 / L1803, R-0192), and the
WFN “is not intended to be a data format, encoding, or any other kind of machine-readable
representation for machine interchange and processing” (§5.1 / p. 14 / L544). One WFN has several
spellings: a URI and a formatted string (`cpe:/a:microsoft:internet_explorer:8.0.6001:beta` and
`cpe:2.3:a:microsoft:internet_explorer:8.0.6001:beta:*:*:*:*:*:*`, §1 / p. 7), and inside the URI,
letters in either case and a tilde written raw or as `%7e`. The two unbinding procedures disagree
about case (P3), and the printed binding procedure corrupts quoted periods (P1). **[analysis]** The
received string is therefore the only form that is stable across producers, libraries and fixes to
the pseudocode; every normalised form is derived from it. This needs no change to tmodel's model:
the accepted slot's values are “Scheme-prefixed and OPAQUE”, and “The scheme is NOT pinned and no
CPE/SBOM schema is imported (ADR-0004 substrate-neutrality).” (LinkML `identifiers`). The prefix is
safe to dispatch on, which is what §6.2 designed it for: “Use of a prefix distinct from the v2.2 URI
binding enables tools to inspect a given input string and use a simple syntactic test to determine
whether to process the input as a URI or as a formatted string.” (§6.2 / p. 37 / L1804). RPT-0004
already proposes the same: “Keep the raw string as emitted; put every other identifier in its own
`identifiers` entry with its scheme prefix; mark which CPEs are generated.” (`mapping.md` §10,
R-ID-3).
*Bears on:* DEC-001a (accepted, ADR-0010) and DEC-011 (accepted, ADR-0004), both unchanged; RPT-0004
R-ID-3 (candidate).

**Adopt-2. A CPE never keys a ProductInstance; it describes Products and Components.**
“WFNs are used solely for product classes. They cannot identify product instances, which are unique,
physically discernible entities in the world, such as a specific licensed and configured
installation of a product on a particular computing device owned by XYZ Corp. and physically
installed in a particular location in the world.” (§5 / p. 14 / L524). The `other` attribute repeats
the boundary: “Values SHOULD NOT be used for storing instance-specific data (e.g., globally-unique
identifiers or Internet Protocol addresses).” (§5.3.3.11 / p. 19 / L816, R-0097). tmodel's instance identity
is per type and is not a name: “software = a build/commit/hash/SBOM; hardware = firmware + buses +
cores (HBOM)” (ADR-0002, as quoted in the LinkML `identifiers` description), and the ProductInstance
description says “The firmware image digest / build hash is an opaque `identifiers` string (ADR-0002
per-type instance identity), not a pinned slot.” **[observation, E7]** The vectors already follow
this: their 16 CPE strings sit on 6 Products and 10 Components and on no ProductInstance. Adopted as
a rule for the importer: a CPE on an SBOM's root component goes to the Product, or is kept as a
description of the instance's product class, never as the instance key, which RPT-0004's R-ID-1 sets
to a digest.
*Bears on:* DEC-005 (accepted, ADR-0002) and DEC-001a (accepted, ADR-0010), unchanged; DEC-009
(open), whose “generic↔instance half” the LinkML description gives to `identifiers`; RPT-0004 R-ID-1
(candidate).

**Adopt-3. Unbind to a WFN for every comparison, in the working store.**
The WFN exists so that processing does not depend on spelling: “Using this interlingua it is
possible to define conversions simply in terms of transforms into and out of the canonical form, and
to define matching and other higher-level processes in generic rather than representation-specific
terms.” (§3.2 / p. 11 / L418). Unbinding is specified for both forms: the formatted string field by
field, “(Because a colon may appear embedded in a value string if preceded by the escape character,
the parsing function needs to ignore escaped colons.)” (§6.2.3.1 / p. 42 / L2078, R-0226), with all eleven
fields present (“Note that all eleven (11) attribute values MUST appear in the formatted string
binding.”, §6.2 / p. 37 / L1818, R-0198); the URI component by component, with the packed edition unpacked
(§6.1.3.1, R-0179 to R-0181). **[analysis]** The WFN is derived data. “The store stays a rebuildable cache (git files
remain the SoT, ADR-0004)” (ADR-0008), so the parse is recomputed from the raw string at every load
and needs no slot. An importer that splits on every colon breaks on `\:` (the §6.2.3.2 example
`bar\:mumble`) and misses the URI's trimmed components.
*Bears on:* DEC-004 (accepted, ADR-0008) and DEC-011 (accepted, ADR-0004), for where the parse
lives; APP-0001 A-001, “ingest a product/instance + components (CPE/purl) and build the KG” (draft);
the importer for which `PLAN-0002` §1 reserves `engine/load/` (“library loader + importers (OTM/STIX
2.1, CWE, …)”), with #60 the nearest lane (`mapping.md`, its reading).

**Adopt-4. Keep ANY, NA and a value as three different answers.**
§5.3.1 defines two logical values with different meanings: “ANY (i.e., “any value”). The logical
value ANY SHOULD be assigned to an attribute when there are no restrictions on acceptable values for
that attribute.” (§5.3.1 / p. 16 / L618, R-0024, R-0025) and “NA (i.e., “not applicable/not used”). The logical
value NA SHOULD be assigned when there is no legal or meaningful value for that attribute, or when
that attribute is not used as part of the description.” (§5.3.1 / p. 16 / L620, R-0024, R-0026); an unused attribute
is ANY (§5.2 / p. 15 / L593, R-0021). Both bindings keep the difference (`*` and `-` in the formatted
string, R-0195; an empty component and `-` in the URI, R-0150 and R-0151). **[observation, E1, E5, E7]** The three answers
carry different claims in the data tmodel will see: NVD's criterion
`cpe:2.3:a:zlib:zlib:*:*:*:*:*:*:*:*` uses ANY for the version and keeps the range in NVD's own
fields; Syft's candidates write `*` for every attribute after the version; seven of the fifteen
distinct vector CPEs use NA for the version (`cpe:2.3:o:acme_auto:tcu:-:*:*:*:*:*:*:*`). Adopted:
the derived parse keeps value, ANY and NA apart, never folds NA into ANY or into an empty value, and
reads an unspecified attribute as ANY. How ANY and NA compare with each other and with values is
NIST IR 7696's subject (open question 4).
*Bears on:* DEC-008 (open); DEC-009 (open).

**Adopt-5. Check syntax with Figure 6-3, and never read a valid CPE as a correct one.**
Figure 6-3 (R-0199 to R-0217), and the XML schema that §6 calls “the authoritative XML binding definition” (§6 / p. 22
/ L917, R-0103), give a cheap structural test: eleven fields, the part letter, quoting, and special
characters only at the ends of a value. **[observation, E9]** The schema's `cpe23Type` pattern,
which has the shape of Figure 6-3 except for case, accepts the LinkML example, all 15 distinct vector
CPEs and the three tool and NVD strings RPT-0004 quotes, and rejects the source's own malformed example. The test certifies
form only: “Any character string meeting the requirements for WFNs (cf. 5.3.2) MAY be specified as
the value of the attribute.” (§5.3.3.2 / p. 18 / L738, R-0068, and the same sentence for every free-text
attribute: R-0071, R-0074, R-0077, R-0081, R-0084, R-0087, R-0091 and R-0099), and choosing “correct” values is out of scope (§5). **[observation, E1]** All 81 of
Syft's CPEs for the pilot image are well formed and every one is `syft-generated`; 13 of the 16
vendor:product pairs in the standard `cpe` field are not in NVD's dictionary. Adopted for one
purpose: a string that fails the test is never parsed into a comparison key or sent to a matcher; it
is kept as evidence, with its provenance (Adapt-1).
*Bears on:* DEC-009 (open); DEC-008 (open); RPT-0004 R-ID-3 (candidate).

**Adopt-6. Take no structure from a CPE.**
“Representing relationships (e.g., part of, bundled with, released before/after, same as) between
products” is outside the scope of CPE Naming (§5 / p. 14 / L529), and so is “Representing
user-defined configurations of installed products” (§5 / p. 14 / L531). `target_sw` and `target_hw`
describe the kind of environment a product class runs in (§5.3.3.8, R-0085; §5.3.3.9, R-0088); they are attributes
of a name, not links to other products. **[analysis]** So `composed_of`, `depends_on` and
`uses_component` come from an SBOM's structure (`mapping.md` R-EDGE-1 to R-EDGE-3) and never from
CPE attributes, and two CPEs never say that two products are the same (Reject-4).
*Bears on:* DEC-001a (accepted, ADR-0010), unchanged; RPT-0004 R-EDGE-2 and R-MERGE-2 (candidates).

---

## What we adapt, and how

**Adapt-1. Record where each CPE came from, beside it, because NIST IR 7695 cannot tell a dictionary
name from a guess.**
The document recommends values but does not govern them: “Values for this attribute SHOULD be
selected from an attribute-specific valid-values list, which MAY be defined by other specifications
that utilize this specification.” (§5.3.3.2 / p. 18 / L737, R-0067). In practice the names tools check
against are NVD's Official CPE Dictionary, defined by NIST IR 7697 (`fanout-identity.md` §1.6),
which this record does not cover. **[observation, E1, E4]** A real scan mixes both kinds, and the
output format decides how many survive: Syft says which candidates are generated and which come from
the dictionary only in its own JSON; its CycloneDX output keeps one CPE per package in `cpe` and
moves the rest into `syft:cpe23` properties; its SPDX output lists all of them; Dependency-Track
keeps one. tmodel's slot cannot hold the difference. Table 6b's “Lost” cell for `identifiers` reads
“which tool asserted which identifier, and that every CPE here is a guess: the slot has no source”
(`mapping.md` §5), and RPT-0004's Phase 1 notes name what to keep: “Stored with it: `source`
(dictionary or generated), NVD `cpeNameId`, `deprecated`, and the lookup date.”
(`fanout-identity.md` §2, dimension 7 Q5). Options, offered to #17 and #15, not decided: (a) a
provenance record per (node id, identifier string), written by the importer as evidence of the
import (`mapping.md` R-PROV-1, R-PROV-2); (b) one Assertion per (Component, CPE), which needs the
identifier to be a Node, because `object` ranges over `Node`; (c) a structured identifier (scheme,
value, source, producer), which changes the accepted slot and so needs a new ADR (“a change to a
core class needs a new ADR that supersedes or refines ADR-0010”, `mapping.md` §2). Keeping the raw
string (Adopt-1) leaves all three open.
*Bears on:* DEC-001a (accepted, ADR-0010; option c only); #17 and #15; RPT-0004 R-ID-3, R-PROV-1,
R-PROV-2 (candidates).

**Adapt-2. A tmodel comparison profile for CPEs, because the source leaves case and equality open
and its procedures disagree.**
§5.3.2 allows both cases (“Uppercase letters, lowercase letters or digit characters MAY be used”,
§5.3.2 / p. 16 / L641, R-0029) and never says whether two values that differ only in case are one value. The
URI unbinder folds them (“;; Normalize: convert all uppercase letters to lowercase first.”, §6.1.3.2
/ p. 32 / L1529, R-0186; “Ensured that uppercase letters are transformed to lowercase in unbind_URI.”,
Appendix B / p. 49 / L2423); the formatted-string unbinder does not (P3). The document defines no
equality of two WFNs, and its pseudocode has defects 10 to 14. Recommended profile, offered to
DEC-009 and to RPT-0004 (not a decision):

1. Dispatch on the prefix: `cpe:2.3:` is a formatted string, `cpe:/` a URI (Adopt-1); a prefix in
   another case is parsed and flagged (defect 15).
2. Unbind per §6.2.3 and §6.1.3 (R-0225, R-0178), with three repairs written down: the `continue` that
   `process_quoted_chars` lacks when binding (defect 13, R-0222); rejection of the embedded `?` runs that
   `add_quoting` lets through (defect 14, R-0235); and, for URIs, decoding every `%HH` of a printable ASCII
   character to its quoted form, flagged, instead of the error `decode()` raises, because §6.1.1
   requires Figure 6-1 input to be accepted (defect 10; R-0121 against R-0185).
3. Fold value case to lower case in the comparison key, as `unbind_URI` already does (R-0186), and keep the
   raw string (open question 4 asks whether NIST IR 7696 agrees).
4. Compare attribute by attribute on the WFN, with value, ANY and NA distinct (Adopt-4), and
   versions as opaque strings (Reject-3).
5. Record the profile version with every derived key.

Where it lives: derived in the working store, never written over the raw string. **[analysis]** A
later fix to the profile is then a rebuild of the cache, not a migration of the canonical files.
*Bears on:* DEC-009 (open); DEC-008 (open); DEC-004 (accepted, ADR-0008), for where it lives.

**Adapt-3. Record an NVD match as an Assertion from the Vulnerability to the Component, at the
lowest confidence, with NVD's range fields as written.**
NIST IR 7695 names classes; it does not match them. Its unquoted special characters are left to
other documents: “These two characters MAY be assigned special interpretations by other CPE
specifications.” (§5.3.2 / p. 16 / L650, R-0036), and its version attribute has no order (Reject-3).
**[observation, E3, E5]** What NVD publishes is a criterion with ANY in the version and the range in
NVD's own fields (`versionEndIncluding` 1.2.12 for zlib in CVE-2022-37434), which RPT-0004's notes
read as “an NVD convention layered on top of CPE 2.3, not part of IR 7696” (`fanout-identity.md`
§1.5); and 29 of Grype's 30 matches on the pilot image were `cpe-match`, a kind Anchore says
“requires verification” (`report.md` §5). RPT-0004 already proposes the record: “One Assertion per
match: subject the Vulnerability, a predicate such as `affects` (name open), object the Component,
`assertion_status: proposed`.” and “Set `confidence` from the match type at first (exact direct,
then exact indirect, then `cpe-match`, which Anchore says needs verification); the scale stays
open.” (`mapping.md` §10, R-MATCH-1). Added from this record: the Assertion keeps the criterion
string as NVD wrote it, the Component's CPE that matched (raw), NVD's range fields as written
(R-RANGE-1), and the matcher and database date (R-PROV-2); and a match through a generated CPE
(Adapt-1) never rises above `cpe-match` confidence, whatever the matcher reports. **[analysis]** The
accepted `affects` slot ranges over Product only (“Vulnerability/Finding affects a vendor Product
(§2b).”, LinkML `affects`), so a per-Component match has to be an Assertion, as `mapping.md` finding
2 records.
*Bears on:* DEC-008 (open); DEC-009 (open); DEC-001a classes (accepted), unchanged; RPT-0004
R-MATCH-1, R-RANGE-1, R-PROV-2 (candidates).

**Adapt-4. Decide which CPE form goes on a Product and on a Component, and keep pattern CPEs out of
`identifiers`.**
The source leaves the line between a description and an identifier to the user: “The CPE Naming
specification leaves all decisions about what distinguishes identifiers and descriptions to the
users. All names constitute descriptions of product classes, and a description becomes an identifier
when it contains sufficient information to select a single entity from the universe of
possibilities.” (§5 / p. 14 / L519). **[analysis]** tmodel has to draw it. Recommended, offered to
DEC-009: a Product (a design) carries a CPE whose version is ANY, naming the product line, in the
spirit of RPT-0004's note that a Product may take “Official CPE vendor:product as aliases”
(`fanout-identity.md` §5, R-ID-2); a Component carries the versioned CPE of what it is; and a CPE
with an unquoted `*` or `?` (R-0036, R-0197), or with ANY in part, vendor or product, is a pattern, which belongs in
a match criterion (Adapt-3) and never in `identifiers`. **[observation, E7]** The vectors mix the
forms today: two Products pair a versionless purl with a versioned CPE
(`pkg:github/papermill/doc-service` with `cpe:2.3:a:papermill:doc_service:3.1.0:*:*:*:*:*:*:*` in
mvp-01; `pkg:github/acme/auth-service` with `cpe:2.3:a:acme:auth_service:2.4.1:*:*:*:*:*:*:*` in
tv-software-auth-service), the two mvp-18 Products carry versioned CPEs, and the two ECU Products
carry version NA with part `o`.
*Bears on:* DEC-009 (open); the vectors, as DEC-001a evidence (accepted, ADR-0010); RPT-0004 R-ID-2
(candidate).

**Adapt-5. Read CPE 2.2 URIs, convert them through the WFN, and never emit one.**
SBOMs carry both bindings: SPDX 3.0.1's `externalIdentifier` types include `cpe22` and `cpe23`
(`report.md` §1.2). §4 asks a consumer, with SHOULD, to read and convert URIs: “(b) it SHOULD be
able to consume any CPE name that meets the syntax requirements specified in Figure 6-1 or Figure
6-2; and (c) it SHOULD be able to convert input CPE names in URI form to syntactically correct
formatted string bindings (cf. 7.1).” (§4 / p. 13 / L482, R-0010, R-0011). The URI binding exists “for backward
compatibility with prior CPE versions” (§6.1 / p. 22 / L922), and its edition component may hold
five packed values: “The leading tilde serves as a flag indicating that the contents of the edition
field are a packed representation of five separate values” (§6.1.2.2 / p. 25 / L1130, R-0161), which “CPE
v2.2-conformant tools may be unable to properly match” (§6.1.2.1.3 / p. 25 / L1118). Recommended:
the importer unbinds a URI (unpacking the edition, and decoding leniently per Adapt-2 step 2), keeps
the raw URI in `identifiers`, and derives the formatted string for comparison; tmodel never writes a
URI, because §4 item 2 makes the formatted string the form a producer MUST emit (R-0006).
*Bears on:* DEC-002 (accepted, ADR-0007), under which an SBOM import arrives as “MAP-NNNN + a
vector”; DEC-008 (open).

**Adapt-6. Write CPE strings in canonical YAML so that their backslashes survive.**
The formatted string quotes with a backslash: “All other non-alphanumeric characters, if used, MUST
be quoted (preceded by the backslash).” (§6.2 / p. 37 / L1816, R-0196); the source's own example is
`cpe:2.3:a:foo\\bar:big\$money_2010:*:*:*:*:special:ipod_touch:80gb:*` (§6.2.2.3.5 / p. 41 / L2048).
ADR-0007 fixes “Canonical instance data = LinkML-shaped YAML/JSON + explicit link records in git”,
and YAML's double-quoted style treats the backslash as an escape. **[observation, E10]** PyYAML
6.0.3 refuses that string double-quoted (`\$` is not a YAML escape) and silently turns
`"cpe:2.3:a:foo\\bar:baz:*:*:*:*:*:*:*:*"` into a string with one backslash, which is no longer a
valid formatted string; single-quoted and plain styles keep it. The vectors write every CPE
double-quoted, which is harmless today because none has a backslash. Recommended: single-quoted (or
plain) style for every `identifiers` value in authored YAML, and a loader check that each `cpe:2.3:`
value still matches Figure 6-3 (R-0199) after parsing; JSON, JSON-LD and Turtle writers escape the backslash
themselves.
*Bears on:* DEC-002 (accepted, ADR-0007) and DEC-011 (accepted, ADR-0004), unchanged; #17
(identifier patterns); the vectors.

---

## What we reject, and why

**Reject-1. A CPE as a node's identity, or as an RDF IRI.**
The formatted string is deliberately not a URI: “it is defined simply to be a “formatted string”
rather than a URI in order to relax the requirements that typically apply to URIs as specified in
[RFC3986].” (§6.2 / p. 37 / L1799). One WFN has two bindings (R-0105, R-0192) and, in the URI, several spellings
(Adopt-1), and the dictionary renames names on purpose: “Any updates to the product data captured in
the identifier name MUST occur through deprecation.” (NIST IR 7697 §6.2, as quoted in
`fanout-identity.md` §1.6; checked in pass 2 against the PDF of library record `nistir-7697`,
SHA-256 `3e5b36aa…a592`). tmodel's ids must not move: “The
canonical file ID is authoritative” (ADR-0004). **[analysis]** A CPE used as a node id would split
one product class into several nodes and would have to be renamed whenever NVD deprecates the name.
Node ids stay as ADR-0004 mints them; CPEs stay string literals in `identifiers`.
*Bears on:* DEC-011 (accepted, ADR-0004), DEC-004 (accepted, ADR-0008) and DEC-001a (accepted,
ADR-0010); consistent with all three, no change.

**Reject-2. Storing a tool's or a library's re-serialised CPE instead of the received one.**
The bound form a tool writes depends on choices the source leaves open or gets wrong. Executed as
printed, the binding pseudocode turns `8\.0\.6001` into `8..001` or `8..0..6001`, depending on how
its `=` is read (P1; R-0222), although its result is the normative one: “the result of an implementation
performing a formatted string binding MUST produce the same result as the suggested pseudocode, processes, etc. would produce.” (§6.2.2 / p. 38 /
L1880, R-0220). The URI unbinder lowercases and the formatted-string one does not (P3; R-0186), and two authors pick
different names for one package: tmodel's own vector writes
`cpe:2.3:a:apache:log4j:2.14.1:*:*:*:*:*:*:*` for log4j-core, where Syft's first candidate is
`cpe:2.3:a:apache:log4j-core:…` (E7). Storing any of these outputs would write one tool's choices
into the canonical files. RPT-0004's R-ID-3 already keeps the raw string (Adopt-1).
*Bears on:* RPT-0004 R-ID-3 (candidate). Also DEC-001b (open), through blocker C2, which ADR-0010
states as “`approval_digest` has no defined binding/canonicalization”: **[analysis]** a governed
snapshot's digest over the canonical files stays stable across normaliser upgrades only if the files
hold raw strings.

**Reject-3. Ordering or comparing CPE versions, or reading version ranges into NIST IR 7695.**
The version attribute is a copied string: “Version information SHOULD be copied directly (with
escaping of printable non-alphanumeric characters as required) from discoverable data and SHOULD NOT
be truncated or otherwise modified.” (§5.3.3.4 / p. 18 / L751, R-0073), and nothing in the document orders
two versions. **[observation, E1]** Copying is also what makes generated CPEs miss NVD: Syft writes
the Alpine release suffix (`cpe:2.3:a:zlib:zlib:1.3.2-r0:*:*:*:*:*:*:*`), and none of the 16 full
names is in the dictionary. Applicability comes from the advisory's own range fields, recorded as
written (“Keep a version range as written, with its scheme”, `mapping.md` §10, R-RANGE-1), never
from comparing CPE version strings.
*Bears on:* DEC-008 (open); RPT-0004 R-RANGE-1 (candidate).

**Reject-4. CPE equality, or a CPE-to-purl mapping, as grounds for merging two Components.**
“same as” relationships are out of scope (§5 / p. 14 / L529), the values are not governed (§5), and
generated names both collide and miss: in the pilot, 15 of 16 vendor:product pairs repeat one word,
and none of the four candidates for `libcrypto3` names OpenSSL, while Grype matched it through the
upstream's CPE `cpe:2.3:a:openssl:openssl:3.5.8:*:*:*:*:*:*:*` (E1, E2). **[analysis]** Equal CPE
strings from generated sources are weak evidence of sameness, and unequal ones are no evidence of
difference. Merges go through an equivalence Assertion, as RPT-0004 proposes: “heuristic matches
(CPE to purl, qualifier spellings) need a Review” (`mapping.md` §10, R-MERGE-2).
*Bears on:* DEC-009 (open); RPT-0004 R-MERGE-1 and R-MERGE-2 (candidates).

**Reject-5. Deriving a Party from the CPE vendor attribute.**
The vendor value “SHOULD describe or identify the person or organization that manufactured or
created the product” (§5.3.3.2 / p. 18 / L736, R-0066), but it is a string chosen from a list the document
does not define, and any well-formed string is allowed (R-0067, R-0068). **[observation, E1, E11]** Generated vendors
repeat the product name in 15 of 16 pilot CPEs, and NVD's own vendor strings were inconsistent for
about 10% of ≈19K vendors in a 2018 snapshot (`fanout-identity.md` §10, citing arXiv:2006.15074;
library record `anwar-2020-cleaning-nvd`). RPT-0004's notes say it directly: “CPE vendor strings are
names, not Party ids” (`fanout-identity.md` §5). Rejected as an identity. A dictionary vendor can
still be evidence for a `manufactured_by` Assertion that a human reviews, the way mvp-18 records a
chip maker (`mapping.md` Table 6c).
*Bears on:* DEC-001a (accepted, ADR-0010; `manufactured_by` and `supplied_by` exist on Product
only), unchanged; #15.

**Reject-6. Claiming NIST IR 7695 conformance for tmodel, and importing its XML schema into the
object model.**
A claim is itself a duty: “An implementation MUST make an explicit claim of conformance to this
specification in any documentation provided to end users.” (§4 / p. 13 / L469, R-0005), and one consumer
duty cannot be met as written: §6.1.1 requires every Figure 6-1 URI to be accepted, while the
unbinding procedure, whose result is normative, raises an error on many of them (defect 10; R-0121, R-0178, R-0185).
**[analysis]** tmodel reads CPEs; it does not mint or publish them. Recommended wording for tmodel
documents: *reads CPE 2.3 formatted strings (NIST IR 7695 §6.2.3) and CPE 2.2 URIs (§6.1.3), with
the deviations listed in its comparison profile*. The XML schema that §6 cites (R-0103) describes bound
names, not tmodel's objects; it belongs to the importer's validation, not to LinkML, which keeps the
accepted slot's “no CPE/SBOM schema is imported” and ADR-0007's rule that “interchange additions
arrive as MAP-NNNN + a vector, never as silent schema drift”.
*Bears on:* DEC-001a (accepted, ADR-0010) and DEC-002 (accepted, ADR-0007), both unchanged.

---

## Mapping to our decisions

### Mapping table

What an importer of radar output (`mapping.md`) would do with each part of a CPE name, and what it
would lose. "Kept in the string" means the value survives only inside the raw `identifiers` entry
and its derived parse, with no slot to query it by.

| NIST IR 7695 element | tmodel class or slot | stance | what an importer loses | decision it bears on (status) |
|---|---|---|---|---|
| formatted string, `cpe:2.3:` (§6.2; R-0192) | `identifiers` on Product and Component | adopt (Adopt-1): keep as received | nothing in the string; its source (dictionary or generated) and producer, which the slot cannot hold (Adapt-1) | DEC-001a (accepted, ADR-0010); DEC-011 (accepted, ADR-0004); #17 |
| URI binding, `cpe:/` (§6.1; R-0105, R-0122) | `identifiers`; derived formatted string | adapt (Adapt-5): keep raw, convert through the WFN | the case of letters, if normalised; for CPE 2.2 tools, the meaning of a packed edition | DEC-001a (accepted); DEC-002 (accepted, ADR-0007) |
| WFN (§5.1; R-0014); unbinding (§6.1.3, §6.2.3; R-0178, R-0225) | derived parse in the working store | adopt (Adopt-3) | nothing: rebuilt from the raw string at load | DEC-004 (accepted, ADR-0008); DEC-011 (accepted); APP-0001 A-001 (draft); #60 |
| product class, never an instance (§5; R-0097) | Product and Component; never a ProductInstance key | adopt (Adopt-2) | none | DEC-005 (accepted, ADR-0002); DEC-009 (open); RPT-0004 R-ID-1 (candidate) |
| `part` (§5.3.3.1; R-0065) | no slot; a Component kind is a gap (`mapping.md` Table 6b) | kept in the string | the part letter as a queryable kind | #17 |
| `vendor` (§5.3.3.2; R-0066 to R-0068) | no slot; not a Party | reject as an identity (Reject-5); evidence for a reviewed `manufactured_by` Assertion | the vendor as a queryable field and as a Party link | DEC-001a (accepted); #15 |
| `product` (§5.3.3.3; R-0069 to R-0071) | no slot (`name` is “Human-readable name.”, not a token) | kept in the string | the product token as a queryable field | #17 |
| `version` (§5.3.3.4; R-0072 to R-0074) | no version slot (`mapping.md` finding 3) | kept in the string; opaque (Reject-3) | the version as a queryable field; any order | #17; DEC-008 (open) |
| `update`, `edition` (§5.3.3.5, §5.3.3.6; R-0075 to R-0081) | no slot | kept in the string | both as queryable fields | #17 |
| `language` (§5.3.3.10; R-0092 to R-0095) | no slot | kept in the string | the user-interface language, not a threat-model input (our reading) | none |
| `sw_edition`, `target_sw`, `target_hw`, `other` (§5.3.3.7 to §5.3.3.11; R-0082 to R-0091, R-0096 to R-0099) | no slot; not an Environment and not an edge (Adopt-6) | kept in the string | target platform and instruction set as queryable facts | #17; DEC-009 (open) |
| ANY and NA (§5.3.1; R-0024 to R-0026) | derived parse | adopt (Adopt-4) | the difference, when a tool writes `*` for every attribute it does not fill (E1) | DEC-008 (open); DEC-009 (open) |
| unquoted `*` and `?` (§5.3.2; R-0035 to R-0043) | match criterion only, never `identifiers` | adapt (Adapt-4) | none | DEC-008 (open); DEC-009 (open) |
| description versus identifier (§5) | Product: version ANY; Component: versioned | adapt (Adapt-4) | which form a source meant, when it gives one | DEC-009 (open); RPT-0004 R-ID-2 (candidate) |
| relationships out of scope (§5) | `composed_of`, `depends_on`, `uses_component` from SBOM structure only | adopt (Adopt-6) | none | DEC-001a (accepted); RPT-0004 R-EDGE-2 (candidate) |
| NVD criteria and ranges (outside NIST IR 7695) | Assertion from Vulnerability to Component | adapt (Adapt-3) | the criterion, the ranges and the matcher, unless the Assertion keeps them | DEC-008 (open); RPT-0004 R-MATCH-1, R-RANGE-1 (candidates); `affects` ranges over Product (DEC-001a, accepted) |
| Figure 6-3 (R-0199 to R-0217); the XSD of §6 (R-0103) | importer validation | adopt (Adopt-5): validity is not correctness | none | DEC-009 (open) |
| conformance (§4; R-0005 to R-0013); the XSD (§6; R-0103) | tmodel's claims; LinkML | reject (Reject-6) | none | DEC-001a (accepted); DEC-002 (accepted) |
| backslash quoting (§6.2; R-0196) | authored YAML | adapt (Adapt-6) | the value itself, if written double-quoted | DEC-002 (accepted); DEC-011 (accepted); #17 |
| a bound string | Node `id`; RDF IRI | reject (Reject-1) | none | DEC-011 (accepted); DEC-004 (accepted) |
| a tool's re-serialisation | the stored value | reject (Reject-2) | the received string, if replaced | RPT-0004 R-ID-3 (candidate); DEC-001b (open, blocker C2) |

### Per decision

- **DEC-001a (accepted, ADR-0010).** NIST IR 7695 fits the accepted `identifiers` slot as it stands:
  opaque strings, scheme not pinned, no schema imported. One option would change it: a structured
  identifier carrying the CPE's source (Adapt-1, option c), which needs a new ADR. The vectors,
  which are DEC-001a's evidence, need two editorial decisions (Adapt-4, Adapt-6; open question 3).
- **DEC-001b (open).** One bearing, through blocker C2: raw strings keep a governed snapshot's digest
  independent of the CPE normaliser (Reject-2).
- **DEC-002 (accepted, ADR-0007).** A CPE is an identifier inside imported data, not an interchange
  format of tmodel's own; an SBOM import that carries CPEs arrives under ADR-0007's MAP-NNNN rule.
  The XML schema stays out of LinkML (Reject-6), and authored YAML needs the quoting rule of Adapt-6.
- **DEC-004 (accepted, ADR-0008) and DEC-011 (accepted, ADR-0004).** Raw strings in git; the WFN
  parse, the validity flag and the comparison keys are derived in the rebuildable store; CPEs never
  become node ids or IRIs (Adopt-3, Adapt-2, Reject-1).
- **DEC-005 (accepted, ADR-0002).** A CPE names a class, so it is never software or hardware instance
  identity (Adopt-2).
- **DEC-007 (accepted, ADR-0001).** The radar contract should carry every CPE candidate as emitted,
  with its source and producer (Adapt-1). Today radar drops them: tradar “does not read how Grype
  made each match (`matchDetails`), related CVE IDs, the fix state, the package's purl or CPEs, or
  any CWE” (`report.md` §4).
- **DEC-008 (open).** NVD's applicability data is CPE-keyed: criteria with ANY versions plus NVD's
  range fields (E5). Matches become Assertions with the lowest confidence (Adapt-3), versions stay
  opaque (Reject-3), and NVD's supply changed in 2025 and 2026 (E6): fewer new CVEs receive NVD
  criteria at all, live or mirrored. That is evidence for DEC-008's live-versus-cached
  question, which APP-0001 A-043 (draft) frames as “external lookups (NVD/CWE) may be cached
  (DEC-008)”, not an answer to it.
- **DEC-009 (open).** Most of this note lands here: provenance (Adapt-1), the comparison profile
  (Adapt-2), the forms for Product and Component (Adapt-4) and validity versus correctness
  (Adopt-5). The LinkML description already places `identifiers` in “the generic↔instance half of
  DEC-009”.
- **RPT-0004 (draft report; candidate rules).** R-ID-3 agrees with this note and could add the CPE
  fields its own Phase 1 notes list (`source`, `cpeNameId`, `deprecated`, lookup date). R-MATCH-1
  agrees and could add the criterion and range fields (Adapt-3). R-MERGE-2 agrees (Reject-4). R-ID-2
  could name the versionless CPE as a Product alias (Adapt-4).
- **D-3** (the library's rule for COSE, CBOR and envelope documents, named in the scaffold) does not
  apply: NIST IR 7695 is none of these.

---

## Source defects

Places where NIST IR 7695 contradicts itself, points at something that does not exist, or leaves
open something it appears to decide. They are defects of the source, not objections to it. Most
also appear as flags in `messages.yaml`.

1. **A dangling reference.** §5.3 item 2 requires “the per-attribute value restrictions specified in
   Section 5.5.3.” (§5.3 / p. 15 / L606, R-0023). §5.5 (WFN Examples) has no subsections; the restrictions
   are §5.3.3.

2. **Figure 5-1 is not the summary the text says it is.** “These requirements are summarized by the
   Augmented Backus-Naur Form (ABNF) grammar [RFC2234] for avstring shown in Figure 5-1.” (§5.3.2 /
   p. 17 / L671, R-0046). But `avstring = ( body / ( spec_chrs *body2 )) *1spec_chrs` (L675, R-0047) derives a lone
   `*` and `**`, which §5.3.2 item 4 forbids: “A single asterisk MUST NOT be used by itself as an
   attribute value. The asterisk MUST NOT be used more than once in sequence.” (§5.3.2 / p. 16 /
   L654, R-0040, R-0041).

3. **The character range and the verbs of §5.3.2.** Values are “printable Unicode Transformation
   Format-8 (UTF-8) characters with hexadecimal values between x00 and x7F” (§5.3.2 / p. 16 / L632, R-0027),
   a range that includes the control characters x00 to x1F and x7F and the space, which item 2
   forbids (R-0032); our reading is x21 to x7E. Item 3 says the escape character “SHOULD be used” (R-0034) where item
   5 says punctuation “MUST be quoted when embedded in value strings” (L659, R-0044), and Figure 5-1 makes
   quoting compulsory (R-0055, R-0056) at every position, not only when “embedded”.

4. **An attribute that is not used: ANY or NA?** “If an attribute is not used in a WFN, it is said
   to be unspecified, and its value SHALL default to the logical value ANY” (§5.2 / p. 15 / L593, R-0021),
   yet “The logical value NA SHOULD be assigned when there is no legal or meaningful value for that
   attribute, or when that attribute is not used as part of the description.” (§5.3.1 / p. 16 /
   L620, R-0026). Our reading separates a missing pair (ANY) from a pair marked not applicable (NA); the
   text does not.

5. **A valid value that no preferred binding can carry.** “A single question mark MAY be used by
   itself as an attribute value.” (§5.3.2 / p. 16 / L656, R-0042), and Figure 5-1 agrees, but Figure 6-3 (R-0212) and
   the XSD's `cpe23Type` (formatted string) and Figure 6-2 (URI, R-0132) all need at least one character
   besides the special ones, so the value `?` binds to a formatted string (`cpe:2.3:a:foo:*:*:?:…`)
   and a URI component (`%01`) that their own grammars reject (P5).

6. **Logical NA without a URI form for `part` and `language`.** Figures 6-1 and 6-2 give
   `part = "h" / "o" / "a" / empty` (§6.1.1 / p. 22 / L946, R-0107) and `lang = LANGTAG / empty` (§6.1.1 /
   p. 23 / L998, R-0129), while `bind_value_for_URI` returns `-` for NA (R-0151), so `bind_to_URI` writes
   `cpe:/-:foo` and `cpe:/a:foo:::::-` (P4). §4 item 3 says a producer “MUST produce URIs that adhere
   to the syntax rules specified in Figure 6-1” (§4 / p. 13 / L476, R-0007). The formatted string has a form
   for both (`logical`, Figure 6-3, R-0201 and R-0207).

7. **Language tags narrower in the bindings than in the WFN.** “Values for this attribute SHALL be
   valid language tags as defined by [RFC5646], and SHOULD be used to define the language supported
   in the user interface of the product being described. Although any valid language tag MAY be
   used, only tags containing language and region codes SHOULD be used.” (§5.3.3.10 / p. 19 / L809, R-0092 to R-0095).
   Figures 6-2 and 6-3 carry only `language ["-" region]` (R-0140), so a valid tag such as `zh-Hant-TW`
   cannot be bound (E9). And in a WFN the tag's hyphen must be quoted (`en\-us`, R-0044), so the WFN value
   is not literally an RFC 5646 tag.

8. **Figure 6-1's tilde is not a tilde.** The rule reads `unreserved = ALPHA / DIGIT / "-" / "." /
   "_" / "˜"` (§6.1.1 / p. 22 / L955, R-0116); the text layer has U+02DC SMALL TILDE and the page shows a
   small raised tilde. Everywhere else the document uses the ASCII `~` (x7E), and §6.1.3.3.7 says
   “The original v2.2 URI syntax allows tildes to appear without encoding” (§6.1.3.3.7 / p. 37 /
   L1786). Read literally, Figure 6-1 rejects the §6.1.3.3.7 input `cpe:/a:foo~bar:big%7emoney_2010`,
   which the procedure unbinds without error. The XSD uses the ASCII tilde (E9).

9. **Figures 6-1 and 6-2 are not RFC 2234 ABNF as printed.** They write the incremental alternative
   as `/=` (`component-list /= part ":" vendor`, §6.1.1 / p. 22 / L938, R-0106 and R-0123), where RFC 2234 §3.3 defines
   `=/` (“oldrule =/ additional-alternatives”); Figure 6-2 continues `pct-encoded` on four lines that
   each begin with `=` (§6.1.1 / p. 23 / L1010 to L1013, R-0139); and Figure 6-1's `LANGTAG = cf. [RFC5646]`
   (L960, R-0120) is a pointer, not a rule. An ABNF tool rejects both figures; the schema artifact has to
   repair them.

10. **MUST accept, MUST error.** “To ensure full backward compatibility with [CPE22], any
    implementation that consumes URIs and claims to be conformant with this Naming specification
    MUST accept as valid input any URI that obeys the full syntax shown in Figure 6-1.” (§6.1.1 /
    p. 23 / L976, R-0121). Figure 6-1 admits any `"%" HEXDIG HEXDIG` (R-0117), and the text says it “allows any
    character in the range %01-ff to be percent-encoded” (L971), but `decode()` raises an error for
    every form outside Tables 6-1 and 6-2 (R-0185), and “the result of an implementation performing a URI
    unbinding MUST produce the same result as the suggested pseudocode” (§6.1.3 / p. 31 / L1449, R-0178).
    The source's own Example 6 shows the clash: “An error is raised when this URI is unbound,
    because it contains an illegal percent-encoded form, "%07".” (§6.1.3.3.6 / p. 36 / L1768), for a
    URI that Figure 6-1 admits. `%2e`, `%20` and the like fail the same way (P6).

11. **Packed editions with no defined failure.** `unbind_URI` sends any edition whose first
    character is a tilde to `unpack()` (§6.1.3.2 / p. 32 / L1489, R-0183). When there are fewer than five
    parts, `strchr` returns nil (R-0191) and the next step (`start := end+1`) is undefined; an edition such as
    `~x`, legal under Figure 6-1 with the tilde of defect 8, reaches it (P6). A sixth part is folded
    into `other`.

12. **A lone `%02` unbinds to a forbidden value.** Figure 6-1 admits `cpe:/a:%02`; `decode()` turns
    it into the vendor value `*` (R-0189), which §5.3.2 forbids (P6; R-0040).

13. **The binding pseudocode does not give the result of its own examples.** In
    `process_quoted_chars` (§6.2.2.2 / p. 40 / L1950 to L1961, R-0222), the branch for a quoted period,
    hyphen or underscore sets `idx = idx + 2.` (with `=`, not `:=`) and has no `continue.`, so
    control falls through to `idx := idx + 1.`. Read as an assignment, the next character is
    skipped and the §6.2.2.3.1 version `8\.0\.6001` binds to `8..001`; read as a comparison, as `=`
    is used elsewhere in the pseudocode, the quoted character is copied twice (`8..0..6001`).
    Neither is the `8.0.6001` the example shows (P1). Every value with a quoted period, hyphen or
    underscore is affected, and §6.2.2 makes the pseudocode's result normative (L1880, R-0220). Appendix B's
    Release 3 lists “Bugfixes to pseudocode for binding and unbinding.” (Appendix B / p. 49 /
    L2429), which did not reach this one.

14. **The two unbinders disagree about special characters.** After an unquoted `?`, `add_quoting`
    sets `embedded := false` (§6.2.3.2 / p. 44 / L2209, R-0235), so the next `?` passes as if it led the
    string: `a??b` unbinds without error to a WFN value that “A special character MUST NOT be
    embedded within a value string.” (§5.3.2 / p. 16 / L654, R-0039) forbids. `decode()` rejects the URI
    equivalent `a%01%01b` (P2; R-0188), and §6.2.3.1 claims the procedure ensures “that unquoted special
    characters adhere to syntax requirements specified in Figure 5-1” (§6.2.3.1 / p. 42 / L2084, R-0231).

15. **No rule for case, and three answers.** §5.3.2 allows both cases (R-0029) and never says whether case
    distinguishes values. `unbind_URI` lowercases every value (§6.1.3.2 / p. 32 / L1529, R-0186);
    `unbind_fs` keeps case. RFC 2234, the ABNF reference the document cites ([RFC2234], §5.3.2 and
    §6.1.1), says in §2.3 “ABNF strings are case-insensitive and the character set for these strings
    is us-ascii.”, so the literals `"cpe:2.3:"` and `"a"` also match `CPE:2.3:A:…`, which
    `unbind_fs` would turn into the part value `A`. The XSD admits lower case only (E9).

16. **The round trip of §7 does not hold.** “Both conversions are round-trip safe, meaning that
    taking one of the two bound forms, converting it to the other form, then converting that back to
    the original binding form, will result in the original binding.” (§7 / p. 47 / L2307, R-0238). With the
    pseudocode as printed, any name with a period or hyphen followed by another character in a value
    fails (defect 13). With that fixed,
    `cpe:2.3:a:Microsoft:Internet_Explorer:8.0.6001:beta:*:*:*:*:*:*` comes back as
    `cpe:2.3:a:microsoft:internet_explorer:…`, and the §6.1.3.3.7 URI
    `cpe:/a:foo~bar:big%7emoney_2010` comes back as `cpe:/a:foo%7ebar:big%7emoney_2010` (P3). Even
    with defect 13 fixed, the claim holds only for URIs already in `bind_to_URI`'s output form and
    for formatted strings in lower case.

17. **A formatted-string helper documented in URI terms.** `get_comp_fs` says “If i=0, ;; return the
    string to the left of the first forward slash.” (§6.2.3.2 / p. 43 / L2125, R-0232), but a formatted
    string has no slash; its own example gives `get_comp_fs(fs,0) = "cpe"` (L2131). Its rule that the
    colon “is the field delimiter unless prefixed by a” backslash also leaves a colon after an escaped
    backslash (`foo\\:bar`) unsettled: read literally the colon is escaped, while Figure 6-3 and
    `add_quoting` read the two backslashes as one pair and the colon as a delimiter (R-0226; examples
    finding F-25).

18. **The negative example is malformed twice.**
    `cpe:2.3:a:hp:insight_diagnostics:7.4.*.1570:*:*:*:*:*:*` “raises an error during unbinding, due
    to the embedded unquoted asterisk in the version attribute.” (§6.2.3.3.3 / p. 45 / L2273). It
    also has ten attribute fields, not the eleven §6.2 requires (P7, E9; R-0198).

19. **SHALL follow, OPTIONAL to follow.** “This section specifies the procedure that SHALL be followed
    when binding a WFN to a formatted string.” (§6.2.2 / p. 38 / L1874, R-0218), then “It is OPTIONAL for
    implementations of formatted string binding to follow the pseudocode, processes, and other
    non-normative information provided in this section.” (L1879, R-0219); §6.2.3 repeats the pair (L2063,
    L2070; R-0223, R-0224), and §6.1.2 and §6.1.3 call the pseudocode non-normative while making its result
    binding (R-0147 and R-0148, R-0177 and R-0178). Our reading: the result is normative, the steps are not; combined with defect 13, the
    normative result of binding is defined by code that is wrong.

20. **The authoritative XML schema is outside the document and differs from it.** “The XML schema
    implementation of these format requirements, which is the authoritative XML binding definition,
    can be found at http://scap.nist.gov/schema/cpe/2.3/cpe-naming_2.3.xsd.” (§6 / p. 22 / L916, R-0103).
    **[observation, 2026-10-19]** The address redirects to `csrc.nist.gov`. The schema's `cpe23Type`
    matches Figure 6-3 except that it admits lower case only; its `cpe22Type` checks neither the
    percent-encoded forms nor the packing of Figure 6-2 and requires a lower-case `c` (E9). Nothing
    says which governs when the schema and the figures differ.

21. **Editorial.** The §6.1.3.3.5 example writes `target_HW=ANY` (§6.1.3.3.5 / p. 36 / L1758),
    harmless under §5.1's case rule (R-0016); §5.1 prints its example pairs with curly quotation marks
    (`color=“red”`, L565) where every other WFN uses straight ones; Figure 6-3 comments
    `ALPHA = %x41-5a / %x61-7A` with “; a-z” (L1863, R-0216); §7.2 points to “the description in Section
    6.2.2” (L2324), the binding procedure, for the syntax that is §6.2.1; §7 calls `unbind_uri` and
    `bind_to_uri` (L2317, L2329; R-0239, R-0240) the functions defined as `unbind_URI` and `bind_to_URI`; and §5.1
    calls an attribute “an alphanumeric label” (L558), although three names contain an underscore.

---

## Evidence

Observations from tmodel's own research (RPT-0004 Phase 1 and the pilot, run 2026-10-08, and the
2026-10-18 re-run), cited by file and section, then three items from probes run for this extraction
(2026-10-19), marked as such. They describe tools, data and the source's pseudocode.

- **E1. Generated CPEs.** For the 16 packages of the pilot's Alpine image, “Syft's JSON marks all 81
  candidate CPEs `syft-generated`”, and “in 15 of the 16 `cpe` values the vendor and the product are
  the same word” (`pilot.md` §2). For the 16 standard `cpe` values, “13 vendor:product pairs are not
  in NVD's CPE dictionary and none of the 16 full names is” (`fanout-identity.md` headline 3, from
  the NVD CPE API on 2026-10-08), because each version carries the Alpine release suffix
  (`cpe:2.3:a:zlib:zlib:1.3.2-r0:*:*:*:*:*:*:*`, §1.21). Bears on Adopt-5, Adapt-1, Reject-3 to
  Reject-5.
- **E2. Binary packages named after themselves, matched through their upstream.** “None of the four
  candidates for `libcrypto3` names `openssl`” (`fanout-identity.md` §1.21), yet Grype matched 13
  OpenSSL CVEs on `libcrypto3` and `libssl3` after it “searched
  `cpe:2.3:a:openssl:openssl:3.5.8:*:*:*:*:*:*:*`, the upstream's CPE” (`pilot.md` §3). Bears on
  Reject-4 and Adapt-3.
- **E3. CPE matching dominates one scan.** Grype's JSON for the image has “31 entries on 30 matches,
  29 `cpe-match`” (`mapping.md` Table 6d), and Anchore's guidance is that “exact-direct-match and
  exact-indirect-match are high confidence, cpe-match requires verification” (`report.md` §5). Bears
  on Adapt-3.
- **E4. The output format decides how many CPEs survive.** “The CycloneDX output puts one CPE per
  package in that field and the rest (65 for Alpine, 920 for tradar) in Syft's own `syft:cpe23`
  properties, while the SPDX output of tradar lists all 996 as `cpe23Type` references” (`report.md`
  §3); Dependency-Track keeps one `cpe` per component (`fanout-tools.md` §1.4), and “Matching
  against data from the NVD requires components to have a valid CPE” (`report.md` §3). Bears on
  Adapt-1.
- **E5. NVD publishes descriptions, not identifiers.** For CVE-2022-37434, “one criterion is
  `cpe:2.3:a:zlib:zlib:*:*:*:*:*:*:*:*` with `versionEndIncluding` 1.2.12” (`report.md` §5), a match
  string with “80 `matches` (dictionary names with `cpeNameId`)” (`fanout-identity.md` §1.7). The
  range fields are NVD's, not NIST IR 7696's (`fanout-identity.md` §1.5). Bears on Adopt-4, Adapt-3,
  Reject-3.
- **E6. NVD's CPE supply changed.** The legacy XML dictionary files were removed on 2025-08-20, and
  since 2026-04-15 NVD enriches only prioritized CVEs (`fanout-identity.md` §1.7, quoting NVD's news
  page); the zlib CVE of the pilot was “Awaiting Analysis” with “no configurations at all” (NVD API,
  2026-09-30; `report.md` §5). Bears on DEC-008 and Adapt-3.
- **E7. tmodel's own CPEs.** **[observation, 2026-10-19, read from the vectors at `1cb85b74`]** The
  six vectors carry 16 CPE strings (15 distinct), on 6 Products and 10 Components and on no
  ProductInstance. All 16, and the LinkML example, have eleven fields and pass Figure 6-3 and the
  XSD pattern (E9). Seven of the 15 use version NA (`-`), all on hardware or ECU names. Of the six
  Products, four carry versioned CPEs: `papermill:doc_service:3.1.0` and `acme:auth_service:2.4.1`
  (part `a`, each beside a versionless purl) and `applianceco:crypto_server:4.0` and
  `sensorco:edge_sensor:1.2` (part `o`). The two ECU Products (`cpe:2.3:o:acme_auto:tcu:-:…` and
  `cpe:2.3:o:acme_auto:brake_ecu:-:…`) carry version NA and part `o`, which §5.3.3.1 gives to “a class
  of operating systems”, for products whose composition lists the SoC and the firmware as separate
  Components. Two Component names repeat vendor as product
  (`libxml_parse:libxml_parse`, `jwt_verify:jwt_verify`), the pattern of E1. For log4j-core the
  vector writes `cpe:2.3:a:apache:log4j:2.14.1:*:*:*:*:*:*:*`, while Syft's first candidate for the
  same jar is `cpe:2.3:a:apache:log4j-core:…` (`fanout-tools.md` §1.4). The vectors are examples
  (“These are EXAMPLES, not accepted truth”, `spec/vectors/README.md`). Bears on Adopt-2, Adopt-4,
  Adapt-4, Reject-2.
- **E8. Probe for this extraction: the §6 pseudocode executed as printed** (our transcription,
  Python 3.13.9, 2026-10-19; one variant adds the missing `continue` of defect 13):

  | probe | input | result | what the source says |
  |---|---|---|---|
  | P1 | the §6.2.2.3.1 WFN, version `8\.0\.6001`, to `bind_to_fs` | `…:8..001:beta:…` as printed with `=` read as an assignment, `…:8..0..6001:beta:…` with it read as a comparison; `…:8.0.6001:beta:…` with `idx := idx + 2.` and `continue` | `cpe:2.3:a:microsoft:internet_explorer:8.0.6001:beta:*:*:*:*:*:*` (§6.2.2.3.1) |
  | P2 | formatted string with version `a??b`; URI with version `a%01%01b` | `unbind_fs` accepts, version `"a??b"`; `unbind_URI` raises an error | no embedded special character (§5.3.2 item 4, R-0039) |
  | P3 | `cpe:2.3:a:Microsoft:Internet_Explorer:8.0.6001:beta:*:*:*:*:*:*` to URI and back | `cpe:/a:Microsoft:Internet_Explorer:8.0.6001:beta`, then `cpe:2.3:a:microsoft:internet_explorer:…` | round-trip safe (§7, R-0238) |
  | P3 | `cpe:/a:foo~bar:big%7emoney_2010` (§6.1.3.3.7) to formatted string and back | `cpe:2.3:a:foo\~bar:big\~money_2010:*:*:*:*:*:*:*:*`, then `cpe:/a:foo%7ebar:big%7emoney_2010` | round-trip safe (§7, R-0238) |
  | P3 | `cpe:/a:foo:big%24MONEY` to formatted string and back | `cpe:2.3:a:foo:big\$money:…`, then `cpe:/a:foo:big%24money` | round-trip safe (§7, R-0238) |
  | P4 | WFN with part NA; with language NA, to `bind_to_URI` | `cpe:/-:foo`; `cpe:/a:foo:::::-` | `part` and `lang` have no NA form (Figures 6-1, 6-2; R-0107, R-0113, R-0129) |
  | P5 | WFN with update `?` | `cpe:2.3:a:foo:*:*:?:*:*:*:*:*:*`; `cpe:/a:foo:::%01` | a lone `?` is a valid value (§5.3.2, R-0042) |
  | P6 | Figure 6-1 URIs: §6.1.3.3.6 (`%07`); `cpe:/a:foo%2ebar`; `cpe:/a:foo%20bar`; edition `~x`; vendor `%02` | error; error; error; undefined (`strchr` returns nil); vendor `"*"` | consumers MUST accept Figure 6-1 input (§6.1.1, R-0121) |
  | P7 | the §6.2.3.3.3 negative example | ten attribute fields; `unbind_fs` stops at the asterisk first | blamed on the asterisk only |
  | P8 | `{part=a}` and `{part=a, vendor=ANY}` to `bind_to_fs` | the same string | an unspecified attribute is ANY (§5.2, R-0021) |
  | P9 | a WFN that is not well formed, version `8.0` (unquoted period), to `bind_to_URI` | `cpe:/a:foo:bar:80` | “The behavior of bind_to_URI is undefined if its input is not well formed.” (§6.1.2 / p. 24 / L1047, R-0146) |

  **[analysis]** P1, P2 and P6 are why Adapt-2 writes its repairs down, and P9 is why the importer
  validates before it binds anything.
- **E9. Probe for this extraction: the schema §6 cites.** **[observation, 2026-10-19]** Fetched from
  the address in §6, redirected to `https://csrc.nist.gov/schema/cpe/2.3/cpe-naming_2.3.xsd`
  (SHA-256 `d37f813f…dd69`, 2254 bytes, `version="2.3"`, dated 2011-07-29). It defines two simple
  types, `cpe22Type` and `cpe23Type`, whose patterns `messages.yaml` gives in full. Checked with
  Python's `re` (full match) beside our regular-expression transcription of Figure 6-3:

  | input | `cpe23Type` | Figure 6-3 (ours) |
  |---|---|---|
  | the LinkML example and the 15 distinct vector CPEs | all pass | all pass |
  | Syft's `cpe:2.3:a:zlib:zlib:1.3.2-r0:*:*:*:*:*:*:*`, Grype's search string for OpenSSL, NVD's zlib criterion | all pass | all pass |
  | the 8 well-formed formatted strings of §1 and §6.2 | all pass | all pass |
  | the §6.2.3.3.3 negative example (ten fields) | fails | fails |
  | `CPE:2.3:A:foo:bar:*:*:*:*:*:*:*:*` | fails (lower case only) | our transcription fails it too; RFC 2234 literals would admit it (defect 15) |
  | `cpe:2.3:a:foo:bar:?:*:*:*:*:*:*:*` (a lone `?`) | fails | fails |
  | `cpe:2.3:a:foo:bar:1.0:*:*:zh-Hant-TW:*:*:*:*` | fails | fails |

  `cpe22Type` accepts all 11 URI examples of §1 and §6.1, including the two the unbinding procedure
  rejects (`%07`, an embedded `%02`), and rejects `CPE:/a:foo` and `cpe:/-:foo`. **[analysis]** The
  schema checks less than the pseudocode on URIs and agrees with Figure 6-3 on formatted strings
  except for case, which makes `cpe23Type` a usable executable check for Adopt-5.
- **E10. Probe for this extraction: CPE strings in YAML** (PyYAML 6.0.3, 2026-10-19). The §6.2.2.3.5
  output `cpe:2.3:a:foo\\bar:big\$money_2010:*:*:*:*:special:ipod_touch:80gb:*` loads unchanged
  from single-quoted and plain scalars; double-quoted, it fails with a scanner error at `\$`. The
  double-quoted scalar `"cpe:2.3:a:foo\\bar:baz:*:*:*:*:*:*:*:*"` loads as
  `cpe:2.3:a:foo\bar:baz:…` with one backslash, a different string that Figure 6-3 rejects, without
  any error. Bears on Adapt-6.
- **E11. NVD's own vendor strings.** “The NVD includes ≈19K distinct vendors, and about 10% of them
  were impacted by vendor naming inconsistencies.” (Anwar et al., arXiv:2006.15074, “a snapshot of
  NVD captured on May 21, 2018”, as checked in `fanout-identity.md` §10; library record
  `anwar-2020-cleaning-nvd`). Bears on Reject-5.

**What the evidence says about NIST IR 7695.** **[analysis]** Every failure above is a well-formed
name: the syntax works, and what goes wrong sits where the document stops (value choice, E1, E2,
E7, E11), where it hands over to other documents (matching and ranges, E3, E5, E6), or where its
own procedures and examples disagree (E8, E9). None is fixed by picking a better library; each
needs a rule of tmodel's own, which is what the adapt section proposes.

---

## Open questions

Routed to who should answer: the **sponsor** (decision maker for DEC-* and the ADRs), the
**RPT-0004 author** (owner of the report, of `mapping.md` and of this record's topic), an issue, or
**NIST and NVD** (the maintainers of CPE 2.3 and of the Official CPE Dictionary).

1. **Where does a CPE's provenance live?** Adapt-1 gives three options; (a) and (b) fit the accepted
   model, (c) needs an ADR that supersedes or refines ADR-0010. *#17 with #15; the sponsor if (c).*
2. **Which comparison profile, and is it DEC-009's to decide?** Adapt-2 proposes five steps, three
   of them repairs to the source's pseudocode. *DEC-009 (sponsor), drafted by the RPT-0004 author.*
3. **Which CPE form goes on a Product, and should the vectors change?** Two Products pair a
   versionless purl with a versioned CPE, two ECU Products use version NA with part `o`, and two
   Component CPEs repeat vendor as product (Adapt-4, E7); the vectors also double-quote every
   identifier (Adapt-6). Correct them as editorial fixes to DEC-001a's evidence, or record them as
   findings, as `spec/vectors/README.md` does for other gaps? *Sponsor, through #17.*
4. **Does NIST IR 7696 compare values case-insensitively, and how do ANY, NA and the special
   characters compare?** The answer fixes Adapt-2 step 3 and the comparison side of Adopt-4.
   *The `nistir-7696` extraction (RPT-0004 author).*
5. **Which NVD data does tmodel mirror for CPE matching?** The dictionary (with `cpeNameId`,
   deprecation and dates) and the match criteria (with ranges), given that NVD now serves them only
   through API 2.0 and its feeds and enriches fewer CVEs (E6). *DEC-008 (sponsor); `nvd-cpe-apis`
   for the API facts.*
6. **Should the radar contract carry every CPE candidate as emitted, with its source and producer?**
   Radar drops CPEs today (`report.md` §4). *ADR-0001 contract (sponsor), proposed by the RPT-0004
   author.*
7. **Who builds the CPE parser of the importer, and does it read CPE 2.2 URIs leniently?** Adopt-3,
   Adapt-2 step 2 and Adapt-5 need one; no issue owns the importer yet. *#60, the nearest lane by
   `mapping.md`'s reading, or a new issue; RPT-0004 author to propose.*
8. **What `confidence` does a `cpe-match` Assertion get?** R-MATCH-1 says “the scale stays open”.
   *#15 and #17.*
9. **Which YAML style do authored identifiers use?** Adapt-6 recommends single quotes and a loader
   check. *#17 (identifier patterns), with the sponsor for the vectors.*
10. **Is there an erratum or a later revision for defects 5, 10, 13, 14 and 16?** RPT-0004's notes
    found the CSRC page marked Final, with no superseded or withdrawn text, on 2026-10-08
    (`fanout-identity.md` §1.4). If NIST has published a correction elsewhere, this record needs an
    `updates` or `superseded_by` link; if not, tmodel's profile carries the repairs. *NIST and NVD.*
11. **When the XSD and the ABNF disagree (case, percent-encoded forms, the tilde), which governs,
    and is the scap.nist.gov address still the reference?** (Defects 8, 15 and 20; R-0103.) *NIST.*
12. **Does NA mean "not applicable" only, or also "not used"?** (Defect 4; R-0021, R-0026.) *NIST.*
13. **Should this record's labels be brought up to date?** `record.yaml` has `bears_on: DEC-002,
    DEC-008` and `status: stub`; the live bearings found here also include DEC-009 (open), DEC-001a
    (accepted) and DEC-005 (accepted). Not changed by this pass. *RPT-0004 author (record and topic
    owner).*
14. **Should the LinkML description of `identifiers` drop “DEC-001 open”?** ADR-0010 accepted the
    slot. *Sponsor.*

Questions 15 to 20 were added in pass 3 (cross-check): each records a disagreement or a gap inside
NIST IR 7695 that the other artifacts of this record already carried and this list did not.

15. **May `part` be ANY or NA?** §5.3.3.1 lists three string values (R-0065), while §5.2 defaults an
    unspecified attribute to ANY (R-0021), §5.3.1 lets any attribute take ANY or NA (R-0024), and
    Figures 6-1 and 6-3 give part an empty or a logical form (R-0107, R-0201). This record reads
    §5.3.3.1 as restricting the string values only (normative.md D-4; examples finding F-13;
    `messages.yaml`, wfn.part). *NIST.*
16. **Which governs for a quoted hyphen followed by special characters, and for a quoted
    underscore?** Figure 5-1 rejects `\-?` and `\-*` (R-0051, R-0055), the prose forbids a quoted
    hyphen only by itself (R-0045), and Figures 6-2 and 6-3 accept the bound forms `-%01` and `-?`,
    which both unbinding procedures turn into `\-?` (examples finding F-11). For `\_`,
    process_quoted_chars has a branch (R-0222) that Figure 5-1 and pct_encode do not have (examples
    finding F-17). *NIST.*
17. **Does the same-result MUST leave room for the checks the SHOULD asks for?** §6.1.3 says a
    fully robust unbinder SHOULD add syntax checks (R-0176) and that its result MUST equal the
    pseudocode's (R-0178), which returns a WFN for `cpe:/a:foo*bar` (fixture URI-NEG-09). §6.2's
    quoting MUST (R-0196) meets §6.2.3's same-result MUST (R-0225) the same way: the pseudocode
    quotes `foo!bar` without an error and turns an empty field into an empty value (FS-NEG-03,
    FS-NEG-14; examples findings F-24, F-35, F-36). *NIST.*
18. **Is Figure 6-1 the CPE 2.2 grammar?** §6.1.1 says the figure shows the syntax of Appendix A of
    [CPE22] (normative.md N-0169, N-0170), but that grammar admits a bare `%` and has no component
    list with the part alone (examples finding F-07; `schema/README.md`). R-0121 rests on “full
    backward compatibility with [CPE22]”: which syntax must a consumer accept? *NIST.*
19. **Do the prose summaries or the pseudocode decide where they differ?** §6.1.2.2 step 4a leaves
    the edition out of the conversion of logical values (R-0163) while bind_to_URI converts it
    (R-0169); §6.1.3.1 step 2 (R-0180) leaves out the lowercasing and the quoting of `~` that
    decode() performs (R-0186, R-0187); §6.2.2.1 (R-0221) leaves out the escapes that
    process_quoted_chars removes (R-0222) (normative.md D-13). This record follows the pseudocode,
    as the same-result requirements imply (R-0148, R-0178, R-0220). *NIST.*
20. **Do the lowercase forms bind?** §1.3 adopts the uppercase keywords of RFC 2119 only
    (normative.md N-0001), yet rule-like sentences use lowercase forms: “may appear without quoting”
    (§6.2 / p. 37 / L1817, R-0197), “needs to ignore escaped colons” (R-0226) and the “must” of the
    add_quoting comments (R-0234 to R-0236). This record reads them as ordinary English, and R-0197
    as a permission (normative.md DEF-22; the `reconciliation` of `requirements.yaml`). *NIST.*
