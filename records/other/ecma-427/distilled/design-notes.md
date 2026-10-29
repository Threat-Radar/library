---
record: ecma-427
kind: design-notes
title: "ecma-427: bearing on our design (tmodel)"
extracted: "2026-10-15"
reviewed_by: ""
attribution: "Contains text from ECMA-427 1st edition, © Ecma International 2025, reproduced under the Ecma copyright notice; full notice in distilled/README.md"
---

# ECMA-427 (purl), 1st edition: how it bears on the tmodel design

**Scope and provenance conventions.**

- A bare `Clause 5.6.6`, `Table 2` or `Annex A` is **ECMA-427 1st edition** (December 2025; PDF
  SHA-256 `037180df…3825`), quoted from `.cache/ecma-427.txt` (`pdftotext -layout`). Curly
  quotation marks (“ ”) are ours; straight quotation marks inside them belong to the quoted text.
  Inside a quotation, PDF line breaks and page footers are removed and nothing else is changed.
- **[2nd ed.]** marks text from purl-spec **v1.1.0** (`docs/specification/` at tag `v1.1.0`, commit
  `7cd2d344`), the 2nd edition text that TC54 approved for the December 2026 Ecma General Assembly.
  It is not this record's edition. Markdown emphasis (asterisks, underscores, backticks) is dropped
  from its quotations.
- tmodel documents are cited by id from `Threat-Radar/tmodel` `origin/main` at `9f566281`
  (2026-10-14). tmodel's research is cited by file and section, for example `fanout-identity.md` §5
  for `research/0004-product-composition/fanout-identity.md`.
- **[analysis]** marks reasoning of this extraction that neither ECMA-427 nor tmodel's documents
  state. **[observation]** marks a tool run, an API response or a fetched file, with its date. “Our
  reading” marks an interpretation of a quoted sentence.
- Ecma's verbal forms are lowercase and are read per the ISO/IEC Directives, Part 2: “shall” is a
  requirement, “should” a recommendation, “may” a permission.
- `R-NNNN` beside a clause locator is the entry `ecma-427#R-NNNN` in `requirements.yaml` that states
  the rule quoted or cited there (added in pass 3, cross-check). RPT-0004's candidate rules (R-ID-1
  to R-ID-5, R-MERGE-1, R-MERGE-2) are a different series.

**Decision status, stated plainly.** From `DECISIONS-0001` (v0.1.8, updated 2026-10-12) and the
ADRs it points to: **accepted** are DEC-001a (ADR-0010), DEC-002 (ADR-0007), DEC-003 (ADR-0006),
DEC-004 (ADR-0008), DEC-005 (ADR-0002), DEC-006 and DEC-010 (ADR-0003, with ADR-0009), DEC-007
(ADR-0001) and DEC-011 (ADR-0004); **open** are DEC-001b, DEC-008 and DEC-009. “A `DEC-*` is
accepted only by an `ADR-NNNN` file” (`DECISIONS-0001`). APP-0001 (A-001, A-043) and the ARCH-0001
§4 requirements are drafts. RPT-0004's identity rules (R-ID-1 to R-ID-5, R-MERGE-1, R-MERGE-2) are
candidates: “Every rule is a candidate for #15 and #17, not a decision.” (`fanout-identity.md` §5).
**Nothing below accepts, rejects or changes a decision.** Every adopt, adapt and reject item is
evidence and a recommendation, routed to an open decision or to the RPT-0004 report. One tmodel
inconsistency matters here: the LinkML description of `identifiers` still ends “Additive DRAFT slot
(DEC-001 open); not a new §13 class.”, while ADR-0010 accepted “the opaque multivalued
`identifiers` slot (purl/CPE/SBOM/firmware digest; ADR-0002 per-type instance identity)”. This
note treats the slot as accepted (open question 12).

**What ECMA-427 is, for tmodel.** It defines the string that the accepted `identifiers` slot
already carries (`"pkg:pypi/libxml-parse@1.8.2"` in `spec/vectors/mvp-01-software-doc-service.yaml`).
Its scope is narrow: “This Standard specifies the syntax for PURLs and the schema for defining PURL
types, but it does not include any specific PURL type definitions, such as maven, pypi or npm.”
(Clause 1). **[analysis]** Three consequences organise everything below. Parsing is defined
component by component (Clause 5), though without an algorithm and with a few edges left open
(defects 11 and 12, and the empty qualifier value of Adopt-4). Equality of two purls is not
(defects 1, 2, 4 and 16): Clause 2 (R-0006) promises a canonical
representation that the edition only partly writes down and partly delegates to type definitions it
does not contain. And versions carry no meaning: “A version is a plain and opaque string.”
(Clause 5.6.5, R-0073). tmodel's open design questions sit on the second and third points.

---

## What we adopt

**Adopt-1. Keep every purl exactly as received, as a string, in the `identifiers` slot.**
ECMA-427 defines the object as a string: “A PURL string is an ASCII URL string composed of seven
components.” (Clause 5.6, R-0041). Its canonical form depends on rules the edition does not contain
(Clause 1; defect 16), is worded differently in the 2nd edition (defects 1 and 2), and is computed
differently by libraries (E11). **[analysis]** The received string is therefore the only form that
is stable across editions, registry versions and libraries; every normalised form is derived from
it. This needs no change to tmodel's model: the accepted slot holds “Opaque external /
instance-identity strings for a structural node” with `range: string`, and “The scheme is NOT pinned
and no CPE/SBOM schema is imported (ADR-0004 substrate-neutrality).” (LinkML `identifiers`). The
scheme prefix is safe to dispatch on, because “The scheme is a constant with the value "pkg".”
(Clause 5.6.1, R-0044); a `pkg:` prefix makes a string a purl candidate, not a purl (E8). Upstream, the
radar contract should carry the string as emitted: RPT-0004 already asks for “The purl string
exactly as emitted plus its parsed parts and qualifiers” (`fanout-identity.md` §2, dimension 6 Q3,
item 3), and ADR-0001 says tmodel “consumes radar's results through a composition→model-input
contract”.
*Bears on:* DEC-001a (accepted, ADR-0010), DEC-011 (accepted, ADR-0004) and DEC-007 (accepted,
ADR-0001), all unchanged; recommended to RPT-0004 for R-ID-3 (candidate).

**Adopt-2. Clause 5 as the parser's definition.**
“Components are separated by a specific character for unambiguous parsing.” (Clause 5). Clause 5.3
(R-0033) gives each separator one role (for example “'@' (at sign) is the separator between name and
version” and “'?' (question mark) is the separator before qualifiers”), Clauses 5.6.1 to 5.6.7 (R-0044 to R-0098) give
each component's rules, and Clause 5.4 (R-0034 to R-0038) gives the decoding. One parser rule is easy to miss: “PURL
parsers shall accept URLs where the scheme and colon ':' are followed by one or more slash '/'
characters, such as 'pkg://', and shall ignore and remove all such '/' characters.”
(Clause 5.6.1, R-0046, R-0047). The result tmodel needs is the decoded tuple (type, namespace segments, name,
version, qualifier map, subpath segments). **[analysis]** It is derived data: the working store
“stays a rebuildable cache (git files remain the SoT, ADR-0004)” (ADR-0008), so the parse is
recomputed from the raw string at every load and needs no slot.
*Bears on:* APP-0001 A-001, “ingest a product/instance + components (CPE/purl) and build the KG”
(draft); DEC-009 (open); DEC-004 (accepted, ADR-0008) for where the derived parse lives.

**Adopt-3. Clause 2's identify-and-reject rule, applied to join keys.**
“Invalid PURLs that fail to conform to the specification shall be identified and rejected by any
conforming implementation.” (Clause 2, R-0008). Clause 5 supplies cheap, structural tests: “The type shall
start with an ASCII letter.” (Clause 5.6.2, R-0049); “The key shall be composed only of lowercase ASCII
letters and numbers, period '.', dash '-' and underscore '_'.”, “A key shall start with an ASCII
letter.” and “Each key shall be unique among all the keys of the qualifiers component.”
(Clause 5.6.6, R-0083, R-0084, R-0086); a subpath segment “shall not be any of '..' or '.'” (Clause 5.6.7, R-0096); and “All
required components of a PURL, such as the scheme, type, and name, shall be present and validated
according to the rules defined in this Standard.” (Clause 2, R-0004). Adopted for one purpose: a string that
fails these tests is never used to merge two Components or to match a Vulnerability. It is not
deleted (Adapt-7). tmodel has to run the tests itself, because the package-url project's Python
library accepts and silently repairs duplicate keys, `..` segments and uppercase keys (E11).
Encoding deviations are handled differently (Adapt-1, step 3), because real producers and the
registry's own examples make them (E3, defect 13).
*Bears on:* DEC-009 (open); RPT-0004 R-MERGE-2 (candidate).

**Adopt-4. The equivalences the edition does state, as the first layer of comparison.**
Four are explicit. “The type is case insensitive. The canonical form is lowercase.” (Clause 5.6.2, R-0051, R-0052).
“All leading and trailing slashes '/' are not significant and should be stripped in the canonical
form.” (Clause 5.6.3, R-0055, and in the same words for the name in Clause 5.6.4, R-0065; Clause 5.6.7 says it for
the subpath, R-0092). “A value shall not be an empty string: a key=value pair with an empty value is the
same as if no key=value pair exists for this key.” (Clause 5.6.6, R-0081, R-0082). And the `pkg://` rule of
Adopt-2 (R-0046, R-0047). A fifth follows, in our reading, from the way Clause 5.6 states each component's content on
its decoded value (“When percent-decoded, a name may contain any Unicode character unless the
package's type definition provides otherwise.”, Clause 5.6.4, R-0068): two spellings that differ only in
which octets are percent-encoded, or in the case of the hex digits, decode to the same value and
compare equal. Under Clause 5.4 only the hex-digit case can differ between two valid spellings; a
spelling that encodes a character Clause 5.4 (R-0036) says “shall not be percent-encoded” is invalid under
Clause 2 (R-0008), and Adapt-1 step 3 decodes it on purpose.
*Bears on:* DEC-009 (open).

**Adopt-5. The left-to-right hierarchy as the basis for package-level and version-level keys.**
“Components are designed such that they form a hierarchy from the most significant on the left to
the least significant components on the right.” (Clause 5), and Table 1 marks `version` “Optional” (R-0020).
**[analysis]** Dropping the version gives a valid, less specific purl that names the package across
its versions. That is how vulnerability records use purls (Adapt-4) and what RPT-0005 recommends:
“keep both when present; purl without version for the package, with version for the instance”
(`research/0005-schema-representations/fanout-vuln-data.md` §7). Adopted for type, namespace, name
and version only. Qualifiers sit to the right of the version but can carry identity (`arch`), so for
them the hierarchy is not a truncation order (Adapt-3).
*Bears on:* DEC-009 (open); RPT-0004 R-ID-2 (candidate).

**Adopt-6. The subpath as a part of a package.**
“The subpath shall be interpreted as relative to the root of the package.” (Clause 5.6.7, R-0098); Table 1:
“Subpath within a package, relative to the package root.” tmodel's vectors already use it this way
(`"pkg:github/papermill/doc-service@3.1.0#render"` for the render worker in mvp-01; `#token` in
tv-software-auth-service). **[analysis]** A purl with a subpath names a part of the package that its
prefix names, which fits `composed_of` between two Components; for package-level matching the
subpath is dropped.
*Bears on:* DEC-009 (open); uses `composed_of` as accepted in DEC-001a (ADR-0010).

---

## What we adapt, and how

**Adapt-1. A tmodel comparison profile, because the 1st edition leaves the canonical form open.**
Clause 2 (R-0006) requires that “equivalent PURLs are consistently resolved to the same canonical
representation”, but the edition has no rule for the order of qualifiers or the case of
percent-encoding hex digits (defect 4), no definition of equivalence (defect 1), and leaves
per-type rules to prose: “These are plain text, unstructured rules as some require programming and
cannot be enforced only with a schema. Tools are expected to apply these rules programmatically.”
(Clause 6.5.7, R-0132). tmodel has to write the missing part down itself. Recommended profile, offered to
DEC-009 and to RPT-0004 (not a decision):

1. Parse per Clause 5 (Adopt-2); mark invalid strings per Adopt-3.
2. Apply the edition's stated equivalences (Adopt-4).
3. Compare decoded component values, never encoded spellings. A spelling that breaks Clause 5.4
   without changing the parse (a percent-encoded colon, an unencoded `+`, or an unencoded `/`
   inside a qualifier value) is decoded and flagged, not rejected. This departs on purpose from
   Clause 2's “shall be identified and rejected” (R-0008), because the registry's own examples and real
   producers use such spellings (defect 13, E3, E7); tmodel should say so where it states the
   profile.
4. Treat qualifiers as an unordered map; keys are unique by Clause 5.6.6 (R-0086).
5. Apply the type definition's rules (“If false, the canonical form shall be lowercased.”, Table 4, R-0131;
   `normalization_rules` implemented by hand per type) from one pinned purl-spec tag (Adapt-6).
6. Record the profile version and the pinned tag with every derived key.

Where it lives: derived in the working store, never written over the raw string (Adopt-1).
**[analysis]** Re-normalising after a type-definition fix is then a rebuild of the cache, not a
migration of the canonical files, which is the property ADR-0004 and ADR-0008 already give derived
data. If the team instead wants a normalised or structured identifier stored in git, the stored
shape of the accepted `identifiers` slot changes, and ADR-0010's own policy applies: “semver; an
accepted ADR is 1.0.0 and only changes to record superseding” (ADR-0010 front matter). That would
need a new ADR.
*Bears on:* DEC-009 (open); RPT-0004 R-ID-3 (candidate); ADR-0010 (accepted) only if stored.

**Adapt-2. Comparing two Components' purls: graded results, recorded as Assertions.**
**[analysis]** Because equality is only partly defined, a comparison should say which level
matched rather than answer yes or no:

| level | equal when | what tmodel does with it |
|---|---|---|
| L0 | the raw strings are identical | the same purl |
| L1 | equal after Adapt-1 steps 1 to 4 (the 1st edition's own rules) | the same purl under the 1st edition |
| L2 | equal after Adapt-1 step 5 (a pinned type definition) | an equivalence Assertion whose justification names the purl-spec tag |
| L3 | equal on the identity projection of Adapt-3, other qualifiers ignored | an equivalence Assertion that needs a Review |

Whether one purl means one shared Component node is DEC-009's to settle; the object-model proposal
already lists “Component (CPE/purl, shared)” (`ARCH-0001-PROPOSAL-v0.2.0` §1, status proposed).
Assertion and Review are accepted core classes (ADR-0010), and RPT-0004's candidate R-MERGE-2
already says: “merge two Components or Artifacts only through an equivalence Assertion with a
justification (for example "same type-normalized purl", "same SHA-256"); heuristic mappings
(qualifier spellings, CPE to purl) need a Review” (`fanout-identity.md` §5). L2 needs the tag in
its justification because Clause 6.5.7's rules are prose and the registry changed between tags
(E12).
*Bears on:* DEC-009 (open); DEC-001a classes (accepted), unchanged.

**Adapt-3. Which qualifiers matter for identity: tmodel must classify them, because the edition
does not.**
Table 1 says only “Qualifier data for a package such as OS, architecture, repository, etc.
Qualifiers are type-specific.”, and Clause 6.8 (R-0141) lets a type require keys: “The PURL qualifiers
component is optional for a specific PURL type, but a qualifiers key or keys may be required for a
specific PURL type.” **[observation, 2026-10-15]** Across the registry only two keys are required,
`uuid` (julia) and `tag_id` (swid), in 35 type definitions at purl-spec v1.0.0 and 42 at v1.1.0.
RPT-0004's candidate R-ID-3 keys a Component on “(type, namespace, name, version, type-required
qualifiers only)”. With today's registry that drops `arch` and the distribution release for `apk`,
`deb` and `rpm`: two architectures' builds of one package version become one Component, and the
release that OSV needs is lost (E2). Recommended classes, offered to DEC-009 and to the R-ID-3
revision:

- **identity-scoping:** type-required keys; `arch`; the distribution release (`distro`, or
  `os_name` with `os_version`), kept as a separate normalised attribute because producers spell it
  differently (E1);
- **artifact-selecting:** keys that pick one file of a version (`file_name` in `pypi`; `classifier`
  and `type` in `maven`), which lead to R-ID-4's content identity rather than to the Component key;
- **locating:** `repository_url`, `download_url`, `vcs_url`; never part of the key. [2nd ed.]
  Annex B.1 names the two roles, “necessary for accurate package identification or location”,
  without saying which key plays which;
- **tool-local or unknown:** any key the pinned type definition does not define (Grype's
  `package-id`, Syft's `upstream`, E4); kept in the raw string, never in the key. `upstream` is
  better used as evidence for a “built from” Assertion (`pilot.md` §4).

*Bears on:* DEC-009 (open); DEC-008 (open) for the release attribute; RPT-0004 R-ID-3 (candidate).

**Adapt-4. Versionless purls in CVE and OSV records.**
ECMA-427 allows them: `version` is “Optional” (Table 1, R-0020), and “The version is prefixed by a '@'
separator when not empty.” (Clause 5.6.5, R-0069). Vulnerability formats require them. CVE Record Format
5.2.0: “The Package URL MUST NOT include a version.” (`definitions.product.properties.packageURL`,
CVEProject/cve-schema tag v5.2.0, `schema/CVE_Record_Format.json`, SHA-256 `33f75174…de67`, read
2026-10-15; library record `cve-json-5`). OSV 1.9.1: the `purl` “identifies the package, without
the `@version` component.”
(`docs/schema.md` at tag v1.9.1, `affected[].package`; library record `osv-schema`). Recommended
matching, offered to DEC-008 and DEC-009:

1. Project the Component's purl to (type, namespace, name) under the pinned profile, project the
   advisory's purl the same way, and compare.
2. Treat qualifiers in the advisory's purl as constraints: a Component with the same key and a
   different value does not match; a Component without the key is a match that needs a Review.
   CVE's own schema examples carry such qualifiers (`pkg:deb/debian/curl?arch=i386&distro=jessie`).
3. Take applicability from the record's own version data (CVE `versions[]`, OSV `ranges[]`), in
   the record's version scheme, never from the purl (Reject-3).
4. Record the result as an Assertion from the Vulnerability to the Component. **[analysis]** The
   accepted `affects` slot ranges only over Product (“Vulnerability/Finding affects a vendor
   Product (§2b).”, LinkML `affects`), so a per-Component match is an Assertion, as RPT-0004's pilot
   already proposes: “an Assertion (subject: Vulnerability, predicate: `affects`, object:
   Component)” (`pilot.md` §4).
5. A versionless purl of a different type (an upstream `pkg:github/...` against a distribution
   `pkg:apk/...`) is never a match; it is a “built from” link that needs a Review (Reject-5, E6).

*Bears on:* DEC-008 (open); DEC-009 (open); DEC-001a classes (accepted), unchanged.

**Adapt-5. Which purl form goes on Product, ProductInstance and Component.**
From Adopt-5, a versionless purl names a package line and a versioned purl names one version.
**[analysis]** So: Product carries versionless purls (RPT-0004 candidate R-ID-2: “key on the
versionless repository purl”); Component carries versioned purls; ProductInstance is keyed by build
digests, not by purls. ADR-0002's per-type instance identity is “software = a build/commit/hash/SBOM;
hardware = firmware + buses + cores (HBOM)” (as quoted in the LinkML `identifiers` description), and
ECMA-427 names packages, not builds: “This Standard defines the Package-URL (PURL) syntax for
identifying software packages independently from their ecosystem or distribution channel.”
(Clause 1). The 1st edition has no checksum qualifier; [2nd ed.] Annex B.3.1 adds an informative
one. An `oci` purl whose version is a digest can serve as a ProductInstance alias, but it does not
say which digest it carries (manifest, index or config; `fanout-identity.md` §1.2), so the digest
kind has to be recorded beside it. tmodel's vectors disagree on this today (E10): mvp-01 puts a
versionless purl on its Product, mvp-03 a versioned one
(`"pkg:generic/connected-vehicle-system@2026.3"`). R-ID-2's own example also needs a spelling fix
(E10).
*Bears on:* DEC-009 (open); DEC-005 (accepted, ADR-0002), unchanged; the mvp vectors (DEC-001a
evidence).

**Adapt-6. Pin, and record, the type-definition registry version.**
Clause 1 leaves the types out; Clause 5.6.3 (R-0053) makes the namespace “optional, unless required by the
package's type definition”; Table 4 (R-0120, R-0131) makes case a per-type property. The edition gives no way to cite
which version of a type definition applies (defect 16). **[observation]** The registry moves:
between purl-spec v1.0.0 (2025-12-19) and v1.1.0 (2026-10-07) the `npm` namespace and name changed
from `"case_sensitive": false` to `true`, and so did `golang`'s (E12). Recommended: the profile names
one purl-spec tag. tmodel's research calls v1.0.0 “the 1st edition baseline” (`fanout-identity.md`
§1.2). R-ID-3 already asks to “keep the raw string, producer, purl edition and type-definition
version” (`fanout-identity.md` §5).
*Bears on:* DEC-009 (open); RPT-0004 R-ID-3 (candidate).

**Adapt-7. Keep invalid purls as evidence, not as keys.**
Clause 2 (R-0008) says invalid purls “shall be identified and rejected”. For a PURL implementation that is
right; for tmodel, which records what producers claimed, deleting the string loses evidence.
**[analysis]** Keep the raw string in `identifiers` (Adopt-1), compute its validity at load
(Adopt-3), never use it as a join key, and show it for Review. tmodel's research has real cases:
purl-shaped strings that are not purls (`pkg:<GUID>` in a firmware SBOM specification) and
unregistered types (`pkg:supplier/...` in CERT-In guidance) (E8).
*Bears on:* DEC-009 (open); APP-0001 A-001 (draft).

---

## What we reject, and why

**Reject-1. A purl as a node's identity, or as an RDF IRI.**
One purl has several valid spellings under the 1st edition alone: `pkg://` is accepted
(Clause 5.6.1, R-0046), the type is case insensitive (Clause 5.6.2, R-0051), leading and trailing slashes are “not
significant” (Clause 5.6.3, R-0055), and qualifiers have no order (defect 4). tmodel's working store is RDF
(ADR-0008), and RDF compares IRIs as strings: “Two IRIs are equal if and only if they are
equivalent under Simple String Comparison according to section 5.1 of [RFC3987]. Further
normalization MUST NOT be performed when comparing IRIs for equality.” (RDF 1.1 Concepts and
Abstract Syntax, W3C Recommendation 25 February 2014, §3.2; library record `rdf-1-1-concepts`).
**[analysis]** A purl used as a node
IRI would split one package into several nodes, and could not be re-normalised later without
renaming nodes, which ADR-0004 rules out: “The canonical file ID is authoritative”. Node ids stay as
ADR-0004 mints them; purls stay string literals.
*Bears on:* DEC-011 (accepted, ADR-0004), DEC-004 (accepted, ADR-0008), DEC-001a (accepted,
ADR-0010); consistent with all three, no change.

**Reject-2. A library's re-serialised “canonical” string as the stored value.**
The canonical representation that Clause 2 requires (R-0006) is not fully defined (defect 1), so a library's
output is that library's reading of it. **[observation, E11]** packageurl-python 0.17.6 turns
`#a/../b` into `#a/b`, keeps the last of two `arch` values, lowercases npm names although npm's
v1.1.0 definition makes them case sensitive, and re-serialises the name `a%2Fb` as `a/b`, which
parses back as a different purl. Storing that output would write one library version's choices into
the canonical files. RPT-0004's candidate R-ID-3 already keeps the raw string.
*Bears on:* RPT-0004 R-ID-3 (candidate). Also DEC-001b (open), through blocker C2, which ADR-0010
states as “`approval_digest` has no defined binding/canonicalization”: **[analysis]** a governed
snapshot's digest over the canonical files stays stable across normaliser upgrades only if the
files hold raw strings.

**Reject-3. The purl version as an ordered or comparable value.**
“A version is a plain and opaque string.” (Clause 5.6.5, R-0073), and the edition “does not cover
ecosystem-specific types or extensions such as PURL Version Ranges (VERS)” (Clause 4, which is
non-normative). Applicability comes from the advisory's own version scheme (Adapt-4, step 3).
*Bears on:* DEC-008 (open).

**Reject-4. Dereferencing a purl during ingest.**
Clause 5.1 says “A PURL is a valid URL because it is a locator even though it has no Authority URL
component: each type has a default repository location when defined.”, but Table 3 (R-0114) makes
`default_repository_url` “Optional” and the edition gives no way to resolve one (defect 14). tmodel's
core loop “works without network for the core loop (ingest → graph → review); external lookups
(NVD/CWE) may be cached (DEC-008)” (APP-0001 A-043, draft). **[analysis]** `repository_url`,
`download_url` and `vcs_url` values are recorded, not fetched.
*Bears on:* DEC-008 (open); APP-0001 A-043 (draft).

**Reject-5. Equality across types.**
“The PURL type component defines the ecosystem-specific structure and meaning for the other PURL
components.” (Clause 1). Our reading: two purls of different types are different identifiers even
when every other component matches. The NVD-carried `pkg:github/<owner>/zlib` and Syft's
`pkg:apk/alpine/zlib@1.3.2-r0` (E6) are linked, if at all, by a reviewed “built from” Assertion
(`pilot.md` §4), never by purl equality.
*Bears on:* DEC-009 (open); DEC-008 (open).

**Reject-6. Claiming ECMA-427 conformance for tmodel, and importing the type-definition schema into
the object model.**
Conformance is broad: “A conforming implementation of Package-URL (PURL) shall fully implement and
support all elements defined within this Standard, including the syntax, components, and semantic
requirements for constructing and interpreting valid PURLs.” (Clause 2, R-0001), and one of its duties
cannot be checked (defect 3). tmodel reads purls; it does not construct or publish them. Recommended
wording for tmodel documents: *parses purls per ECMA-427 1st edition, Clause 5*. The Annex A schema
describes type definitions, not purls. It belongs to the normaliser's input, not to LinkML, which
keeps the accepted slot's “no CPE/SBOM schema is imported” and ADR-0007's rule that “interchange
additions arrive as MAP-NNNN + a vector, never as silent schema drift”.
*Bears on:* DEC-001a (accepted, ADR-0010) and DEC-002 (accepted, ADR-0007), both unchanged.

**Reject-7. “uniquely identifies” as an identity guarantee.**
The Introduction, which is informative, says “PURL introduces a standardized URL-based syntax that
uniquely identifies software packages, independent of their ecosystem or distribution channel.” The
normative clauses do not make that true (defect 20): qualifiers are optional and type-specific, and
two correct tools wrote different purls for the same bytes (E1). **[analysis]** Equal purls are
strong evidence of sameness, not proof; unequal purls are not evidence of difference. Merges go
through Assertions (Adapt-2).
*Bears on:* DEC-009 (open); RPT-0004 R-MERGE-1 and R-MERGE-2 (candidates).

---

## Mapping to our decisions

### Mapping table

| ECMA-427 element | tmodel class or slot | stance | decision it bears on (status) |
|---|---|---|---|
| Clause 5.6 (R-0041): the purl is an ASCII string | `identifiers` on Product, ProductInstance, Component | adopt (Adopt-1): keep as received | DEC-001a (accepted, ADR-0010); DEC-011 (accepted, ADR-0004) |
| Clause 5.6.1 (R-0044): the scheme `pkg` | `identifiers` scheme prefix | adopt (Adopt-1) | DEC-001a (accepted, ADR-0010) |
| the purl as a producer emitted it | radar to tmodel contract | adopt (Adopt-1) | DEC-007 (accepted, ADR-0001); RPT-0004 (draft) |
| Clauses 5.3, 5.4, 5.6.1 to 5.6.7 (R-0033 to R-0098): parsing | ingest; derived parse in the working store | adopt (Adopt-2) | DEC-009 (open); DEC-004 (accepted, ADR-0008); APP-0001 A-001 (draft) |
| Clause 2 (R-0008): invalid purls rejected | join-key eligibility | adopt (Adopt-3); adapt (Adapt-7) | DEC-009 (open); RPT-0004 R-MERGE-2 (candidate) |
| Clauses 5.6.1 to 5.6.4, 5.6.6 and 5.6.7 (R-0047, R-0051, R-0055, R-0065, R-0082, R-0092): stated equivalences | comparison key, first layer | adopt (Adopt-4) | DEC-009 (open) |
| Clause 5: hierarchy; Table 1 (R-0020): `version` optional | Product (versionless) and Component (versioned) | adopt (Adopt-5); adapt (Adapt-5) | DEC-009 (open); RPT-0004 R-ID-2 (candidate) |
| Clause 5.6.7 (R-0098): subpath | `composed_of` between Components | adopt (Adopt-6) | DEC-009 (open); DEC-001a (accepted, ADR-0010) |
| Clause 2 (R-0006): canonical representation; no order or hex-case rule; Clause 6.5.7 (R-0132): prose rules | tmodel comparison profile (derived) | adapt (Adapt-1) | DEC-009 (open); RPT-0004 R-ID-3 (candidate); a new ADR only if stored (ADR-0010, accepted) |
| (no ECMA-427 rule) | graded comparison results as Assertions | adapt (Adapt-2) | DEC-009 (open); DEC-001a classes (accepted) |
| Table 1 (R-0021): qualifiers; Clause 6.8 (R-0141): required keys | identity projection of a Component | adapt (Adapt-3) | DEC-009 (open); DEC-008 (open); RPT-0004 R-ID-3 (candidate) |
| Table 1 and Clause 5.6.5 (R-0020, R-0069): versionless purls | Vulnerability-to-Component match (Assertion) | adapt (Adapt-4) | DEC-008 (open); DEC-009 (open); DEC-001a (accepted: `affects` ranges over Product) |
| Clause 1: packages, not builds | ProductInstance identity | adapt (Adapt-5) | DEC-005 (accepted, ADR-0002); DEC-009 (open) |
| Clause 1 and Table 4 (R-0120, R-0131): types outside the edition | the normaliser's pinned purl-spec tag | adapt (Adapt-6) | DEC-009 (open); RPT-0004 R-ID-3 (candidate) |
| Clause 2 (R-0008): rejection | raw string kept as evidence | adapt (Adapt-7) | DEC-009 (open); APP-0001 A-001 (draft) |
| Clauses 5.6.1 to 5.6.3 (R-0046, R-0051, R-0055): several spellings of one purl | Node `id`; RDF IRI | reject (Reject-1) | DEC-011 (accepted, ADR-0004); DEC-004 (accepted, ADR-0008) |
| Clause 2 (R-0006): canonical representation | the stored value | reject a library's output (Reject-2) | RPT-0004 R-ID-3 (candidate); DEC-001b (open, blocker C2) |
| Clause 5.6.5 (R-0073); Clause 4: VERS out of scope | version ordering | reject (Reject-3) | DEC-008 (open) |
| Clause 5.1: a purl as a locator | ingest | reject dereferencing (Reject-4) | DEC-008 (open); APP-0001 A-043 (draft) |
| Clause 1: the type defines the meaning | cross-ecosystem links | reject cross-type equality (Reject-5) | DEC-009 (open); DEC-008 (open) |
| Clause 2 (R-0001): conformance; Annex A | tmodel's claims; the LinkML model | reject (Reject-6) | DEC-001a (accepted, ADR-0010); DEC-002 (accepted, ADR-0007) |
| Introduction: “uniquely identifies” | merge rules | reject as a guarantee (Reject-7) | DEC-009 (open); RPT-0004 R-MERGE-1, R-MERGE-2 (candidates) |

### Per decision

- **DEC-001a (accepted, ADR-0010).** ECMA-427 fits the accepted `identifiers` slot as it stands:
  opaque strings, scheme not pinned, no schema imported. Nothing here needs it changed. One choice
  would: storing a normalised or structured purl in git (Adapt-1), which needs a superseding ADR.
- **DEC-001b (open).** One bearing, through blocker C2 (the binding of `approval_digest`): raw
  strings keep a governed snapshot's digest independent of the normaliser version (Reject-2).
- **DEC-002 (accepted, ADR-0007).** A purl is not an interchange format. **[analysis]** With
  `range: string`, the derived JSON-LD and Turtle carry `identifiers` as string literals, which is
  what Reject-1 needs. Annex A stays out of LinkML (Reject-6).
- **DEC-004 (accepted, ADR-0008) and DEC-011 (accepted, ADR-0004).** Raw strings in git; the parse,
  the validity flag and the comparison keys are derived in the rebuildable store; purls never become
  IRIs (Adopt-2, Adapt-1, Reject-1).
- **DEC-005 (accepted, ADR-0002).** A purl names a package version, not a build, so it is not
  software instance identity (Adapt-5).
- **DEC-007 (accepted, ADR-0001).** The radar contract should pass purls as emitted, with the
  producer and its version (Adopt-1).
- **DEC-008 (open).** Advisory purls are versionless; matching is a projection plus the advisory's
  own ranges, recorded as Assertions, with no dereferencing (Adapt-4, Reject-3, Reject-4). NVD
  carries the CNA's purls but does not accept them as a query key, while OSV.dev does (E6, E2):
  a purl-keyed match against NVD data needs a local copy. That is evidence for DEC-008's
  live-versus-cached question, not an answer to it.
- **DEC-009 (open).** Most of this note lands here: the comparison profile, graded results,
  qualifier classes, the purl form per class, the pinned registry and invalid purls kept as evidence
  (Adapt-1 to Adapt-7). The LinkML description already places `identifiers` in “the
  generic↔instance half of DEC-009”.
- **RPT-0004 (draft report; candidate rules).** R-ID-3 should replace “type-required qualifiers
  only” with Adapt-3's classes and keep its raw-string and type-definition-version parts. R-ID-2 and
  R-MERGE-2 agree with this note; R-ID-2's example needs one encoding fix (E10).
- **D-3** (the upstream library's rule for COSE, CBOR and envelope documents, named in the scaffold)
  does not apply: ECMA-427 is none of these.

---

## Source defects

Places where ECMA-427 1st edition contradicts itself, points at something that does not exist, or
leaves open something it appears to decide. Each ends with the 2nd edition's status (purl-spec
v1.1.0). These are defects of the source, not objections to it.

1. **Clause 2 requires “equivalence rules” that the edition never states.** “Implementations shall
   ensure that equivalent PURLs are consistently resolved to the same canonical representation.
   This includes strict adherence to normalisation and equivalence rules.” (Clause 2, R-0006). The only
   other uses of “equivalent” are the qualifier `native_name` description, “The equivalent native
   name for this qualifier key.” (Clause 6.8.1.7, Table 7, Annex A) [observation: text search,
   2026-10-15]. The parts of a canonical form that do exist are scattered: “A canonical PURL is
   composed of these permitted ASCII characters” (Clause 5.2, R-0032), “The canonical form is lowercase.”
   (Clause 5.6.2, R-0052), “should be stripped in the canonical form” (Clauses 5.6.3, 5.6.4, 5.6.7; R-0055, R-0065, R-0092), “If
   false, the canonical form shall be lowercased.” (Tables 4, 5, 6 and 8; R-0131) and “Example of valid,
   canonical PURLs for this package type.” (Clause 6.10, R-0155). **2nd ed.:** not fixed. Clause 2 is word for word
   the same, while “canonical” is removed from Clause 5 (“The type is case insensitive. The form is
   lowercase.”, [2nd ed.] Clause 5.6.2) and from Clause 6, so the duty stays and the partial
   definition goes.

2. **Invalid input and valid-but-non-canonical input are told apart only by each rule's verbal
   form.** Clause 2 (R-0008): “Invalid PURLs that fail to conform to the specification shall be identified
   and rejected by any conforming implementation.” The edition defines neither what makes a purl
   invalid nor what makes it non-canonical; the reader infers the line from each rule. An uppercase
   type is valid (“The type is case insensitive.”, Clause 5.6.2, R-0051), an uppercase qualifier key breaks
   a “shall” (“The key shall
   be composed only of lowercase ASCII letters and numbers, period '.', dash '-' and underscore
   '_'.”, Clause 5.6.6, R-0083) and so is to be rejected, and a leading slash only “should be stripped”
   (Clause 5.6.3, R-0055). Clause 5.2 (R-0032) states the characters of “A canonical PURL” only, which reads as if a
   non-canonical purl could hold others; the encoding duties still apply to every purl (each
   component “shall be encoded as defined in the Character encoding clause”, Clause 5.6, R-0043, and “Where
   the space ' ' is permitted, it shall be percent-encoded as '%20'.”, Clause 5.4, R-0037), so a raw space is
   invalid and the Clause 5.2 wording misleads rather than leaves the question open (corrected in
   pass 2, which found the earlier wording of this item overstated). The package-url project's Python
   library normalises an uppercase key where Clause 2 says reject (E11). **2nd ed.:** partly fixed.
   [2nd ed.] Clause 5.2 now reads “A valid PURL is composed of these permitted ASCII characters”,
   which removes the misleading wording; the rest is unchanged, and tmodel's research records the
   question as open upstream (purl-spec issue #741, `fanout-identity.md` §1.2).

3. **A prohibition on extensions that are never identified.** “Any prohibited extensions explicitly
   identified in the specification shall not be implemented.” (Clause 2, R-0012). No clause identifies one.
   The word “extensions” appears only in Clause 2 (permitted extensions, “as long as these
   extensions do not violate the core specification”, R-0009) and in Clause 4 (“extensions such as PURL
   Version Ranges (VERS)”) [observation: text search]. The duty cannot be checked. **2nd ed.:** not fixed (Clause 2
   unchanged).

4. **No order for qualifiers and no case for percent-encoding hex digits.** A search of the text for
   “sort”, “order” and “lexico” finds nothing [observation]; Clause 5.6.6 fixes the separators, the
   key syntax and key uniqueness (R-0077, R-0079, R-0083 to R-0086), but no order. Clause 5.4 (R-0035, R-0038) borrows “the percent-encoding mechanism
   defined in RFC 3986 section 2.1” and then says “With the exception of the percent-encoding mechanism, the rules regarding
   percent-encoding are defined by this Standard alone.” RFC 3986 §2.1 itself says “For consistency,
   URI producers and normalizers should use uppercase hexadecimal digits for all
   percent-encodings.”; whether that sentence is part of “the mechanism” is not said. Two conforming
   producers can emit different strings for one purl. **2nd ed.:** not fixed normatively. [2nd ed.]
   Annex B.1 (informative): “Tools that build PURLs should sort multiple qualifiers lexicographically
   by key, but this is not expected behaviour for a tool to parse or validate a PURL.” Hex case is
   still unstated, and the informative Annex C writes hex digits as quoted letters, which RFC 5234
   §2.3 makes case-insensitive (“ABNF strings are case insensitive and the character set for these
   strings is US-ASCII.”).

5. **A dead reference to a `repository_url` qualifier.** “A URL host or Authority shall not be used
   as a namespace. Use instead a repository_url qualifier.” (Clause 5.6.3, R-0061, R-0062). The 1st edition defines
   no qualifier keys: “Qualifiers are type-specific.” (Table 1), and the type definitions are outside
   the edition (Clause 1). `repository_url` appears nowhere else except inside the type-definition
   property `default_repository_url` (Table 3, Clause 6.4.2, Annex A). **2nd ed.:** fixed
   informatively. [2nd ed.] Annex B.3.4 defines the qualifier and says “A 'repository_url' value
   shall be percent-encoded.”

6. **The electronic form of Annex A is at a dead, moving address.** “The schema shown below is
   available in electronic form at:
   https://github.com/package-url/purl-spec/blob/main/schemas/purl-type-definition.schema.json”
   (Annex A; one PDF line break inside the URL removed). [observation, 2026-10-15] The address returns
   HTTP 404 at github.com and at raw.githubusercontent.com. Two months before the December 2025
   adoption, purl-spec commit `178ec1aadd` (2025-10-08, “Update schema files filenames and ids
   #699”) renamed that path to `schemas/purl-type-definition.schema-1.1.json`, the development line.
   The file that matches Annex A is `schemas/purl-type-definition.schema-1.0.json`, added on
   2025-09-19 by commit `4899f1528f` (“Freeze purl-type schemas for Ecma standard”); its `$id`,
   `https://packageurl.org/schemas/purl-type-definition.schema-1.0.json`, resolves. The link also
   names a branch (`main`), not a tag, so even a live link would move. **2nd ed.:** partly fixed.
   [2nd ed.] Annex A points at `.../blob/main/schemas/purl-type-definition.schema-1.1.json`, which
   exists on `main` (2026-10-15) but is still a branch link.

7. **Table types contradict the clauses and Annex A.** Table 2 gives `namespace_definition`,
   `name_definition`, `version_definition` and `subpath_definition` the type “Array”; Clauses 6.5,
   6.6, 6.7 and 6.9 say “Type: Object”, and Annex A says `"type": "object"`. Tables 4 to 8 give
   `requirement` the type “Array”; Clauses 6.5.1, 6.6.1, 6.7.1, 6.8.1.2 and 6.9.1 say “Type:
   String”, and Annex A says `"type": "string"`. **2nd ed.:** not fixed; [2nd ed.] Tables 2, 4, 5,
   6, 7 and 8 still say “Array”.

8. **Table 2 omits `$id` and `$schema`, which Annex A requires or constrains.** Annex A's root
   lists `"$id"` first in its `"required"` array, sets `"additionalProperties": false`, and gives
   `"$schema"` a `"const"` (R-0163, R-0162, R-0164). Neither property is in Table 2 or described anywhere in Clause 6, so a
   type definition written from Clause 6 alone fails Annex A. **2nd ed.:** not fixed, and two new
   mismatches. [2nd ed.] Annex A's own `$id` is
   `https://packageurl.org/schemas/purl-type-definition.schema-1.1.json` while its `$schema` property
   still requires the const `https://packageurl.org/schemas/purl-type-definition.schema-1.0.json`,
   and [2nd ed.] Clause 6.1 places the versioned schemas at
   `https://packageurl.org/purl-schemas/purl-type-definition.schema-<major>.<minor>.json` (a
   `purl-schemas` path, not `schemas`).

9. **The schema's type patterns are narrower than Clause 5.6.2.** Clause 5.6.2 (R-0048, R-0049): “The package type
   shall be composed only of ASCII letters and numbers, period '.', and dash '-'.” and “The type
   shall start with an ASCII letter.”, with no minimum length. Clause 6.1 (R-0112): “Pattern Constraint:
   ^[a-z][a-z0-9-\.]+$”, which needs at least two characters; Clause 6.10's examples pattern (R-0154),
   `^pkg:[a-z][a-z0-9-\.]+/.*$`, likewise. Annex A's `$id` pattern (R-0165) allows only `[a-z0-9-]` before
   `-definition.json`, so a type containing a period, which Clause 5.6.2 and Clause 6.1 allow, cannot
   have a valid `$id` that embeds its type string; nothing in the edition requires the `$id` to embed
   it, so this half is a potential mismatch, not a broken rule. Latent: no registered type at v1.0.0
   (35 types) or v1.1.0 (42 types)
   has one letter or a period [observation]. **2nd ed.:** not fixed. The patterns are unchanged,
   and the informative [2nd ed.] Annex C grammar, `type = alpha-lc *( alpha-lc / DIGIT / "." / "-" )`,
   allows one letter, so the 2nd edition's grammar and schema disagree.

10. **A uniqueness rule attached to the wrong property.** Clause 6.8.1.7 reads “The equivalent
    native name for this qualifier key.” followed by “All items shall be unique.” (R-0150). The property is a
    string; the array that Annex A makes unique is `qualifiers_definition` (`"uniqueItems": true`).
    **2nd ed.:** not fixed ([2nd ed.] Clause 6.9.1.8, same text).

11. **The slash before a name with no namespace.** “The name is prefixed by a single slash '/'
    separator when the namespace is not empty.” (Clause 5.6.4, R-0064). Read literally, a name with an empty
    namespace has no slash in front of it, yet Clause 5.3 (R-0033) says “'/' (slash) is the separator between
    type, namespace and name”, Example 3 of Clause 5 is `pkg:npm/foobar@12.3.1`, and the Clause 6.10
    pattern (R-0154) requires a `/` after the type. Our reading: the bullet means the slash between namespace
    and name. **2nd ed.:** same wording; settled only informatively by the [2nd ed.] Annex C rule
    `PURL = scheme ":" type [ "/" namespace ] "/" name [ "@" version ] [ "?" qualifiers ] [ "#" subpath ]`.

12. **The case of the scheme is not stated.** “The scheme is a constant with the value "pkg".”
    (Clause 5.6.1, R-0044). Clause 2 (R-0007) requires that “implementations shall process URI encoding and decoding
    for PURL components according to the standards outlined in RFC 3986”, and RFC 3986 §3.1 says
    “Although schemes are case-insensitive, the canonical form is lowercase” and “An implementation
    should accept uppercase letters as equivalent to lowercase in scheme names”. Whether `PKG:` is a
    valid purl is open; the package-url project's Python library rejects it (E11). **2nd ed.:**
    settled only informatively: [2nd ed.] Annex C, `scheme = %x70.6B.67 ; constant with the value "pkg" (lowercase only)`.

13. **The colon rule against the registry's own “canonical” examples.** Clause 5.4 (R-0036): “The following
    characters shall not be percent-encoded:” and, in that list, “the colon ':', whether used as a
    Separator Character or otherwise”. Table 2 (R-0155) defines a type definition's `examples` as “Example of
    valid, canonical PURLs for this package type.” At purl-spec tag v1.0.0 (2025-12-19), which
    tmodel's research calls “the 1st edition baseline”, the `oci` examples include
    `pkg:oci/debian@sha256%3A244fd47e07d10?repository_url=docker.io/library/debian&arch=amd64&tag=latest`
    and the `docker` examples include
    `pkg:docker/customer/dockerimage@sha256%3A244fd47e07d10?repository_url=gcr.io`: percent-encoded
    colons, against Clause 5.4, and in the `oci` case unencoded slashes inside a qualifier value,
    also against Clause 5.4, because “"allowed set" is composed of the Alphanumeric Characters and the
    Punctuation Characters” (R-0035) and the slash is in neither [observation]. The registry is outside the
    edition (Clause 1), so this is a defect of the ecosystem the edition relies on. **2nd ed.:** not
    fixed in the registry. Clause 5.4 is unchanged; at v1.1.0 the `oci` slashes are encoded
    (`repository_url=docker.io%2Flibrary%2Fdebian`), but three of the four `oci` examples and the
    `docker` example still encode the colon, which the informative [2nd ed.] Annex C grammar
    excludes.

14. **A purl “is a locator” without the means, and is defined by four references.** “A PURL is a
    valid URL because it is a locator even though it has no Authority URL component: each type has
    a default repository location when defined.” (Clause 5.1). Table 3 (R-0114) makes
    `default_repository_url` “Optional”, and the edition gives no procedure to resolve a purl. The same clause defines validity by four sources (R-0025),
    “A PURL is a valid URL and URI that conforms to the URL definitions or specifications at:” RFC
    3986, two Wikipedia articles and the WHATWG URL Standard, of which only RFC 3986 is a normative
    reference (Clause 3). The next bullet (R-0028; R-0030 repeats it) mixes terms: “are not valid PURL types. They are valid URL
    or URI schemes but they are not a valid PURL scheme.” **2nd ed.:** partly fixed. The Clause 5
    file at tag v1.1.0 no longer contains the “because it is a locator” bullet (the release notes
    describe a rewording instead), and adds “A PURL should be a locator based on three paths to
    specify or derive a URL:”; the Wikipedia and WHATWG references and the type-or-scheme wording
    remain.

15. **An “opaque” version that types may rewrite.** “A version is a plain and opaque string.”
    (Clause 5.6.5, R-0073). Yet Table 6 (R-0120, R-0121) gives the version a `case_sensitive` flag and a “List of rules to
    normalize this component for this PURL type.”, and the `pypi` type sets the version's
    `case_sensitive` to false at both v1.0.0 and v1.1.0 [observation]. Our reading: “opaque” means
    the core gives the string no order or meaning, not that it is never rewritten. **2nd ed.:** not
    fixed (same text).

16. **Equivalence depends on type definitions the edition neither contains nor versions.** Clause 1
    excludes them; Table 4 makes case a per-type flag (“true if this PURL component is case
    sensitive. If false, the canonical form shall be lowercased.”, R-0131); Clause 6.5.7 (R-0132) makes other rules
    prose. Nothing in the edition says which version of a type definition applies. [observation]
    Between purl-spec v1.0.0 and v1.1.0 the `npm` namespace and name went from
    `"case_sensitive": false` to `true`, and `golang`'s too, while the v1.1.0 `golang` note still
    says “The name shall be lowercased.”; `pkg:npm/Core` and `pkg:npm/core` were one package under
    v1.0.0's rules and are two under v1.1.0's. **2nd ed.:** made explicit, not fixed. [2nd ed.]
    Clause 5.7 says the Standard “does not include the set of current "registered" PURL type (JSON
    format) definition files because there are ongoing additions and changes to these files” and
    makes them binding: “If the PURL type is registered, then the PURL is invalid if it does not
    conform to all of the rules from the corresponding PURL type definition.” Still no version pin.

17. **The published edition defers to a moving web page.** “The document at https://tc54.org/purl/
    is the most accurate and up-to-date Package-URL specification.” (About this specification,
    p. iv). The same page carries rendering leftovers, “This document is available as a single page
    and as multiple pages.”, and link texts whose targets did not survive into the PDF (“Issues: All
    Issues, File a New Issue”, “Chat: Slack Channel”). **[analysis]** A citable edition that calls a
    living page more accurate than itself leaves no rule for which text governs when the two differ;
    this record pins the PDF. **2nd ed.:** not fixed. [2nd ed.] About still defers, with a link text
    (`https://tc54.org/ecm427/`) that differs from its target (`https://tc54.org/ecma427/`).

18. **Normative references that float.** “For undated references, the latest edition of the
    referenced document (including any amendments) applies.” (Clause 3, R-0014). The Unicode Standard is
    listed undated (`https://www.unicode.org/versions/latest/`), but Clause 5.5 (R-0039) cites a section
    number and a term: “References to "lowercase" in this Standard refer to the culture-invariant
    full case mapping defined in Section 3.13.2 of the Unicode Standard.” [observation, 2026-10-15]
    §3.13.2 is “Default Case Conversion” in Unicode 16.0.0 and in 18.0.0 (what “latest” serves
    today), and “culture-invariant” occurs in neither version's chapter 3; our reading is that the
    untailored default conversion is meant. ECMA-262 is undated in Clause 3, while the Bibliography
    pins “ECMA-262, ECMAScript® language specification, 16th Edition. Annex A.8: Grammar Summary for
    Regular Expressions”, an annex that ECMA-262 itself marks informative [observation]. ASCII
    (INCITS 4-1986) and JSON Schema draft-07, on which Clause 5.2 and Annex A depend, are listed only
    in the Bibliography. **2nd ed.:** partly addressed. [2nd ed.] Clause 5.5 links to Unicode 16.0.0
    (a dated link) while Clause 3 still says “latest”; RFC 3629 and RFC 5234 join Clause 3; the
    `Bibliography.md` file at tag v1.1.0 lists the same four entries, although the release notes say
    “Added 6 references.”

19. **Annex A as printed is not usable JSON, and two keywords do nothing.** The PDF breaks string
    literals across lines (for example the `$schema` constant ends one line with
    `https://packageurl.org/schemas/purl-type-` and starts the next with `definition.schema-1.0.json`),
    so a copy of the printed text does not parse. [observation] Rejoined, the printed schema equals
    `schemas/purl-type-definition.schema-1.0.json` at tag v1.0.0 (SHA-256 `b8988773…e983`), so the
    content is right. Separately, `qualifiers_definition` has `"additionalItems": false` beside a
    single-schema `items`, which draft-07 ignores (“Otherwise, "additionalItems" MUST be ignored, as
    the "items" schema (possibly the default value of an empty schema) is applied to all elements.”,
    draft-handrews-json-schema-validation-01 §6.4.2), and `use_repository` has `"default": false`
    although Table 3 and Annex A make it required (R-0113). **2nd ed.:** partly fixed. The Markdown source
    has no broken literals; both keywords are unchanged.

20. **The Introduction's “uniquely identifies”.** “PURL introduces a standardized URL-based syntax
    that uniquely identifies software packages, independent of their ecosystem or distribution
    channel.” (Introduction). Nothing normative makes one purl unique to one package: qualifiers are
    “Optional” and “type-specific” (Table 1, R-0021), and one package can be written with or without them
    (E1). The Introduction is informative, so this is an overclaim rather than a contradiction.
    **2nd ed.:** not fixed (same sentence).

21. **Editorial.** “Version control system (VCS) URLs such git://” (Clause 5.1, a missing “as”) and
    “programing languages” (Clause 6). **2nd ed.:** both fixed.

---

## Evidence from tmodel's tool runs

Observations from tmodel's own research (RPT-0004 Phase 1, run 2026-10-08, and RPT-0005), cited by
file and section, then two items from probes run for this extraction (2026-10-15), marked as such.
They describe tools and data, not ECMA-427.

- **E1. Same bytes, two producers, two purls.** For the same arm64 manifest of `alpine:latest`,
  Docker's SBOM attestation (Docker Scout 1.18.1) writes
  `pkg:apk/alpine/zlib@1.3.2-r0?os_name=alpine&os_version=3.24` and Syft 1.52.0 writes
  `pkg:apk/alpine/zlib@1.3.2-r0?arch=aarch64&distro=alpine-3.24.2` (`fanout-identity.md` headline 2,
  §1.20, §1.21). Both parse under Clause 5; the `apk` type defines only `arch`. Bears on Adapt-3 and
  Reject-7.
- **E2. Qualifier spelling changes vulnerability lookups.** OSV.dev returned 52 advisories for
  `pkg:deb/debian/openssl@3.0.11-1~deb12u2?distro=bookworm`, 0 for the same purl with
  `?arch=amd64&distro=debian-12`, and 82 with no qualifiers; every `pkg:apk/alpine/busybox` form
  tried returned 0 while the ecosystem query `Alpine:v3.18` returned 5 (`fanout-identity.md` §1.22).
  Bears on Adapt-3 and Adapt-4.
- **E3. Percent-encoded colons in real output.** Syft's SPDX 2.3 root package carries
  `pkg:oci/alpine@sha256%3A260479a1…?arch=arm64&tag=latest` (`fanout-identity.md` §1.21), the
  spelling of the registry examples in defect 13 and against Clause 5.4. Bears on Adopt-4 (decode
  before comparing).
- **E4. Tool-local qualifiers.** Grype's CycloneDX output re-wraps Syft's `bom-ref` “inside a new
  `package-id` qualifier (URL-encoded)” (`pilot.md` §3), and “10 of the 16 purls carry an
  `upstream=` qualifier” (`pilot.md` §2). Neither key is defined by the `apk` type. Bears on
  Adapt-3.
- **E5. Graph tools split nodes on qualifiers.** GUAC v1.1.0: “Two nodes that have different
  qualifiers and/or subpath but the same version mean two different packages in the trie (they are
  different).” (`fanout-identity.md` §1.25; library record `guac`). Bears on Adapt-2.
- **E6. Versionless advisory purls, and who keys on them.** OSV's `purl` is versionless and
  optional (`fanout-identity.md` §1.22). NVD carries the CNA's `packageURL` but its API refuses it as
  a query parameter (“Invalid parameter: purl.”), and the one sampled value named a source
  repository, `pkg:github/<owner>/zlib` (owner omitted), not a distribution package
  (`fanout-identity.md` §9). Bears on Adapt-4 and Reject-5.
- **E7. Copies of one record disagree.** Canonical's file has
  `pkg:deb/ubuntu/busybox@1:1.21.0-1ubuntu1.4+esm1?arch=source&distro=esm-infra-legacy/trusty`;
  OSV.dev serves `pkg:deb/ubuntu/busybox?arch=source&distro=esm-infra-legacy%2Ftrusty`, with the
  “version removed, slash percent-encoded” (`fanout-identity.md` §9). **[analysis]** Under Clause 5.4 (R-0035)
  the OSV.dev spelling of the qualifier is the conforming one; the source file's `+` and `/` are not
  encoded as Clause 5.4 requires. Bears on Adopt-1 and Adopt-4.
- **E8. Strings that look like purls and are not.** A firmware SBOM specification's VEX product id
  `pkg:<GUID>` has no name part, and CERT-In guidance prescribes an unregistered `supplier` type,
  `pkg:supplier/OrganizationName/ComponentName@Version?qualifiers&subpath` (`fanout-identity.md`
  §10; `dimensions.md` Table 3). Bears on Adopt-3 and Adapt-7.
- **E9. An independent study agrees.** SBOMproof (arXiv 2510.05798), as quoted in
  `fanout-identity.md` §1.27: “Tools do not employ the same pURLs and none of them respects the
  standard.” Bears on Reject-7.
- **E10. tmodel's own documents.** Four vector purls put a namespace on the `oci` type:
  `pkg:oci/papermill/doc-service@sha256:3b9e1d2a` (mvp-01), `pkg:oci/fleet/ingest-api@sha256:c0ffee11`
  and `pkg:oci/fleet/datastore@sha256:d0cada11` (mvp-03), and `pkg:oci/acme/auth-service@sha256:8f2c1a7e`
  (tv-software-auth-service). The `oci` type definition, at v1.0.0 and at v1.1.0, has
  `"requirement": "prohibited"` for the namespace and the note “OCI purls do not contain a
  namespace, although, repository_url may contain a namespace as part of the physical location of
  the package.” The 1st edition delegates the point (“The namespace is optional, unless required by
  the package's type definition.”, Clause 5.6.3, R-0053); under [2nd ed.] Clause 5.7 these purls would be
  invalid. The vectors are examples (“These are EXAMPLES, not accepted truth”,
  `spec/vectors/README.md`), so this is a correction to the vectors, not to the model. Separately,
  the Product purl is versionless in mvp-01 and versioned in mvp-03 (Adapt-5), and R-ID-2's example,
  `pkg:oci/alpine?repository_url=index.docker.io/library/alpine` (`fanout-identity.md` §5), leaves
  slashes unencoded inside a qualifier value, which is not the encoding Clause 5.4 (R-0035) requires; the
  conforming spelling is `repository_url=index.docker.io%2Flibrary%2Falpine`.
- **E11. Probe for this extraction: what the package-url project's Python library does**
  (packageurl-python 0.17.6, run 2026-10-15; the script stayed in the extraction scratchpad and is
  not committed):

  | input | 1st-edition rule | `PackageURL.from_string(...).to_string()` |
  |---|---|---|
  | `pkg:npm/foo@1.0.0?Arch=x86` | key lowercase only (Clause 5.6.6, R-0083) | accepted: `pkg:npm/foo@1.0.0?arch=x86` |
  | `pkg:deb/debian/curl@7.50.3-1?arch=i386&arch=amd64` | keys unique (Clause 5.6.6, R-0086) | accepted: `?arch=amd64` (last wins) |
  | `pkg:github/acme/repo@1.0#a/../b` | no `..` segment (Clause 5.6.7, R-0096) | accepted: `#a/b` |
  | `pkg:generic/my package@1.0` | space as `%20` (Clause 5.4, R-0037) | accepted: `my%20package` |
  | `pkg:npm/Core@1.0.0` | npm name case-sensitive at v1.1.0, not at v1.0.0 | `pkg:npm/core@1.0.0` |
  | `pkg:npm/%40Angular/Core@1.0.0` | the same, for namespace and name | `pkg:npm/%40Angular/core@1.0.0` (matches neither tag) |
  | `pkg:generic/a%2Fb@1` | a `/` inside a name stays encoded (Clause 5.4, R-0035) | `pkg:generic/a/b@1`, which re-parses as namespace `a`, name `b` |
  | `pkg:oci/debian@sha256%3A244fd47e07d10` | colon not encoded (Clause 5.4, R-0036) | `pkg:oci/debian@sha256:244fd47e07d10` (conforms) |
  | `pkg:oci/papermill/doc-service@sha256:3b9e1d2a` | `oci` namespace prohibited (type definition) | accepted unchanged |
  | `PKG:npm/foo@1.0.0` | not stated (defect 12) | rejected |
  | `pkg:deb/debian/curl@7.50.3-1?distro=jessie&arch=i386` | no order (defect 4) | `?arch=i386&distro=jessie` (sorted) |
  | `pkg:x/foo@1` | valid by Clause 5.6.2 (R-0048, R-0049; defect 9) | accepted |

  **[analysis]** The library repairs where Clause 2 says reject, sorts where the edition is silent,
  and applies a per-type list written into its code (its `normalize_name` lowercases names for
  `npm`, `github`, `pypi`, `apk`, `oci` and others) rather than reading the registry. That is
  reasonable for a library, and it is exactly why tmodel should keep the raw string (Adopt-1,
  Reject-2).
- **E12. Probe for this extraction: registry and schema facts** (2026-10-15). Required qualifier keys
  across all type definitions: only `uuid` (julia) and `tag_id` (swid), at v1.0.0 (35 types) and
  v1.1.0 (42 types); no key is marked `recommended` at v1.1.0, although the repository's
  `schemas/purl-type-definition.schema-1.1.json` at that tag allows it. The 2nd edition's own Annex A
  text at the same tag does not: its qualifier key `requirement` admits only `optional` and
  `required`, so the printed annex and the electronic copy it points to differ (pass 2 observation,
  2026-10-15). `npm`: namespace and name `case_sensitive` false at v1.0.0 and true at v1.1.0, with the
  note changing from “therefore the name must be lowercased” to “old packages with mixed case names
  were "grandfathered in"”; `golang` has the same flip. The registry kept changing after v1.1.0
  (`main` commit `accf27abf1`, 2026-10-09). The Annex A link is dead (defect 6). CVE 5.2.0's own
  `packageURL` examples include
  `pkg:maven/org.apache.xmlgraphics/batik-anim?repository_url=repo.spring.io/release`, with a slash
  unencoded inside a qualifier value. IANA's URI Schemes registry lists `pkg` as “Provisional”,
  consistent with `fanout-identity.md` §1.31, so the “future official registration” that Table 1
  anticipates has begun.

**What the evidence says about the 1st edition.** **[analysis]** Every divergence above parses under
Clause 5, and every one sits in a place the edition leaves open or delegates: qualifier meaning (E1,
E2, E4, E5), encoding spelling (E3, E7, E10), type rules (E10, E11, E12) and version scope (E6). None
is fixed by choosing a better library; each needs a rule of tmodel's own, which is what the adapt
section proposes.

---

## Open questions

Routed to who should answer: the **sponsor** (decision maker for DEC-*), the **RPT-0004 author**
(the student who owns the report and this record's topic), or **purl-spec upstream** (Ecma TC54 and
the Package-URL community).

1. **Where should the purl comparison rule be decided?** This note recommends DEC-009 (open), since
   the LinkML description puts `identifiers` in “the generic↔instance half of DEC-009”, with the
   profile kept derived (Adapt-1). If the team wants a normalised or structured identifier stored in
   git, that changes the accepted slot and needs an ADR superseding ADR-0010. *Sponsor.*
2. **Should the radar contract require purls exactly as emitted, with producer and version?**
   RPT-0004 already proposes it (dimension 6 Q3, item 3); ADR-0001 owns the contract. *Sponsor.*
3. **Is R-ID-3's “type-required qualifiers only” intended?** With only julia `uuid` and swid
   `tag_id` required across 42 types, it keys `apk`, `deb` and `rpm` Components without architecture
   or distribution release (Adapt-3, E12). Proposed: Adapt-3's four classes. *RPT-0004 author.*
4. **Which purl-spec tag does the normaliser pin, and is the edition recorded per identifier or per
   load?** v1.0.0 is the 1st edition baseline, v1.1.0 the 2nd edition text, and `main` keeps moving
   (Adapt-6, E12). *RPT-0004 author.*
5. **How confident is an advisory-purl match?** Proposed: the levels of Adapt-2 and the five steps of
   Adapt-4, with qualifier constraints and cross-type links going to Review. The answer shapes how
   DEC-008's automation runs. *RPT-0004 author, then the sponsor for DEC-008.*
6. **Should the vectors be corrected?** Four `oci` purls carry a namespace the type prohibits, the
   Product purl is versionless in mvp-01 and versioned in mvp-03, and R-ID-2's example leaves slashes
   unencoded (E10). Correct them as editorial fixes to DEC-001a's evidence, or record them as
   findings, as `spec/vectors/README.md` does for other gaps? *Sponsor.*
7. **What should tmodel's documents claim?** Proposed: *parses purls per ECMA-427 1st edition,
   Clause 5*, and no conformance claim (Reject-6). After the December 2026 General Assembly, which
   edition do they cite? *Sponsor.*
8. **Where are Clause 2's “equivalence rules” (R-0006) and its “prohibited extensions explicitly
   identified” (R-0012)?** Both persist unchanged in the 2nd edition (defects 1 and 3). *purl-spec upstream.*
9. **Will qualifier order, hex-digit case and the line between invalid and non-canonical input
   become normative?** The 2nd edition makes ordering an informative “should” for builders only
   (defects 2 and 4; purl-spec issue #741). *purl-spec upstream.*
10. **What does the `oci` type mean?** Its namespace is prohibited, so a registry's repository path
    can live only in `repository_url`; its version note says the digest “is required to uniquely
    identify the artifact” while the version's
    `requirement` is `optional`; its examples encode the colon against Clause 5.4 (R-0036); and it does not
    say which digest (manifest, index or config) the version holds (defect 13, E3, E10). *purl-spec
    upstream.*
11. **Will the schema and table defects be corrected?** Defects 7 to 10 and 19 carry over to the 2nd
    edition, which adds the `$schema` and `$id` version mismatch and the `purl-schemas` path of
    defect 8. *purl-spec upstream.*
12. **Should this record's labels and tmodel's slot description be brought up to date?**
    `record.yaml` now has `bears_on: DEC-001, DEC-002, DEC-009` (DEC-009 was added after this note
    was drafted), but DEC-001 is now split, and of the live bearings found here DEC-008 (open) and
    DEC-001a (accepted) are still not named; the LinkML description of `identifiers` still says
    “DEC-001 open” after ADR-0010 accepted the slot. Neither is changed by this pass. *RPT-0004
    author (record and topic owner), with the sponsor for the LinkML text.*
13. **Can the authority prohibition be enforced at all?** “A PURL shall not contain a URL
    Authority, i.e. there is no support for username, password, host and port components.”
    (Clause 5, R-0023; restated in Clause 5.1 as R-0027), yet parsers “shall ignore and remove all
    such '/' characters” after `pkg:` (Clause 5.6.1, R-0046, R-0047). Once the slashes are gone no
    authority is left to detect: `pkg://example.com/npm/foobar@12.3.1` parses with the type
    `example.com` (`examples/expected.yaml`, PURL-EDGE-01), and the derived grammar's
    `purl-parser-input` accepts it. Recorded in `examples/README.md` (item 2) since pass 1; carried
    here by pass 3 (cross-check), which met it again while mapping R-0023 to the grammar. The 2nd
    edition was not checked for it in pass 3. *purl-spec upstream.*
14. **What do a qualifier definition's `default_value` and an absent `requirement` mean?** “The
    optional default value of this qualifier if not provided.” (Clause 6.8.1.6; “Optional” in
    Table 7, R-0146). The edition does not say whether the value is written percent-encoded or
    decoded, whether it must itself meet the Clause 5.6.6 value rules (“A value shall not be an empty
    string”, R-0081; R-0087, R-0088), or whether a purl that carries the default equals one that
    omits the qualifier (R-0006 lists this among the gaps in the canonical form). Table 7 also makes
    `requirement` “Optional” (R-0144) without saying what an absent one means, so a qualifier
    definition with no `requirement` is neither required nor stated optional. Found in pass 3
    (cross-check) while wiring `messages.yaml`; the 2nd edition was not checked for it. *purl-spec
    upstream.*
