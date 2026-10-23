---
record: osv-schema
kind: design-notes
title: "osv-schema: bearing on our design (tmodel)"
extracted: "2026-10-18"
reviewed_by: ""
source_version: "OSV Schema 1.9.2 (ossf/osv-schema tag v1.9.2, commit c8a57bdc5b0bc54646e140cabbb7834bd0b5aec9)"
source_digest: "96d82f03d763fb408bc344d01fc271f761a81cc225f6f6a42d318e3ed21cebff"
attribution: "Quotes the OSV Schema specification (docs/schema.md), JSON Schema (validation/schema.json) and protobuf definition (proto/vulnerability.proto) of github.com/ossf/osv-schema at tag v1.9.2, licensed under the Apache License 2.0"
---

# OSV Schema 1.9.2: how it bears on the tmodel design

**Scope and provenance conventions.**

- `L<n>` is a line of `docs/schema.md` at tag `v1.9.2` (2010 lines; SHA-256 `96d82f03…cebff`), which is
  the specification; the repository's root `schema.md` only points at the published site. Each source
  locator gives the document's own heading and the line, as `§ affected[].package field / L964-L967`.
  `schema.json` is `validation/schema.json` at the same tag (SHA-256 `15b10dbb…2653`), cited by JSON
  Pointer. `proto` is `proto/vulnerability.proto` (SHA-256 `1c5a7af8…a070`), cited by message and field.
- Curly quotation marks (“ ”) are ours. Everything between them is the source's characters, including
  Markdown backticks and asterisks, straight quotation marks and curly apostrophes. Where a quoted
  passage crosses a line break, the break and the next line's indentation are written as one space. In
  `proto` quotations the comment markers (`//`) are dropped.
- **[1.9.1]** marks a comparison with `docs/schema.md` at tag `v1.9.1` (SHA-256 `e5b87d62…307e`), the text
  that RPT-0004 and RPT-0005 quote, fetched for this extraction on 2026-10-18 (E12).
- tmodel documents are cited by id from `Threat-Radar/tmodel` `main` at `1cb85b74` (2026-10-18). RPT-0004's
  files are cited by name and section, for example `mapping.md` §10 for
  `research/0004-product-composition/mapping.md`; `fanout-vuln-data.md` is RPT-0005's
  (`research/0005-schema-representations/`). The library record `ecma-427` (its FX-1 extraction is on
  branch `topic/rpt-0004-records`, not yet on this branch) is cited for its design notes.
- **[analysis]** marks reasoning of this extraction that neither OSV nor tmodel's documents state.
  **[observation]** marks a tool run or a fetched file, with its date. "Our reading" marks an
  interpretation of a quoted sentence.
- OSV writes its rules in lowercase ("must", "should", "may", "required", "recommended"); no uppercase
  BCP 14 keyword occurs. They are read here as requirement, recommendation and permission. `R-NNNN`
  beside a locator is the entry `osv-schema#R-NNNN` of `requirements.yaml` whose text is the passage
  cited (added in pass 3, cross-check); a quotation with no id has no entry of its own (a rationale, an
  example, a pointer, or text that file does not extract). RPT-0004's candidate rules (R-ID-*, R-MERGE-*,
  R-MATCH-*, R-RANGE-1, R-CWE-1, R-PROV-*) are a different series.

**Decision status, stated plainly.** From `DECISIONS-0001` (v0.1.8, updated 2026-10-12) and the ADRs it
points to: **accepted** are DEC-001a (ADR-0010), DEC-002 (ADR-0007), DEC-003 (ADR-0006), DEC-004
(ADR-0008), DEC-005 (ADR-0002), DEC-006 and DEC-010 (ADR-0003, with ADR-0009), DEC-007 (ADR-0001) and
DEC-011 (ADR-0004); **open** are DEC-001b, DEC-008 and DEC-009. “**A `DEC-*` is accepted only by an
`ADR-NNNN` file**” (`DECISIONS-0001`). APP-0001 is a draft. RPT-0004's rules are candidates: “It accepts
nothing. Every rule is a candidate for #15 and #17, and every "our reading" is ours, not an official
crosswalk.” (`mapping.md`, introduction). **Nothing below accepts, rejects or changes a decision.** Every
adopt, adapt and reject item is evidence and a recommendation, routed to an open decision, to an issue
(#15 core objects and #17 schema; #60 library loader and #61 CWE import, which `mapping.md` names, in
its own reading, as the nearest lanes for an importer) or to the RPT-0004 report. One tmodel
inconsistency matters to a reader of this note: tmodel's `CLAUDE.md` still says “**Every `DEC-*` is
open.**”; this note follows the register and the ADRs.

**What OSV is, for tmodel.** It is the format of the advisory side of RPT-0004's bridge: “Ecosystem
advisories name a package instead: in the OSV format, "The object itself has two required fields,
`ecosystem` and `name`, and an optional `purl` field" (OSV schema).” (`report.md` §5). Its scope is
narrow on purpose: “Overall, the approach of this schema is to define only the fields that absolutely
must be shared between databases, leaving customizations to the "ecosystem_specific" and
"database_specific" blocks (see below)” (§ Format Overview / L109-L111). **[analysis]** Four properties
organise everything below.

1. A record names packages, never products or instances: an ecosystem and a name, with an optional
   versionless purl, and for Linux distributions the source package (Adapt-1, Adapt-2).
2. Applicability is a typed version timeline with printed evaluation pseudocode, but comparing two
   `ECOSYSTEM` versions is left to each ecosystem, and the pseudocode leaves package equality and event
   order open (Adopt-3, Adopt-4, Adapt-5; defects 7, 8 and 17).
3. A record is one database's claim, linked to other databases' claims by `aliases`, `upstream` and
   `related`, with no weakness field, no not-affected status and no review state (Adopt-2, Adapt-4,
   Adapt-8, Reject-2).
4. The JSON Schema checks less than the prose and, in one place, more: it lacks the `id` rules that
   1.9.2 added, and rejects unknown top-level fields that the prose tells clients to ignore (Reject-4;
   defects 3 and 20).

---

## What we adopt

**Adopt-1. An OSV `id` is a catalog identifier, and its prefix names the asserting database.**
“The `id` field is a unique identifier for the vulnerability entry. It is a string of the format
`<DB>-<ENTRYID>`, where `DB` names the database and `ENTRYID` is in the format used by the database.”
(§ id, modified fields / L143-L145, R-0009, R-0010). The database behind the prefix is the record's author: “If `source`
is omitted, the rating is implicitly attributed to the home database (as identified by the record's `id`
field), whether as author or endorser.” (§ severity[].source field / L879-L880, R-0059). Version 1.9.2 adds a
character rule aimed at the same uses tmodel would make of an id (file names and IRIs): “To ensure maximum
compatibility with CLI tools, shell scripts, URL routing, and filesystem storage, the `id` field must
strictly use ASCII characters matching the regular expression:” `^[a-zA-Z0-9:_.-]+$` (§ Character set
constraints / L154-L157, R-0012). **[analysis]** The id fills the accepted `catalog_ref` slot, “External catalog
identifier when the proposal names one (CWE, CAPEC, ATT&CK, CVE, D3FEND). The identifier scheme is not
pinned in §13.” (LinkML `catalog_ref`), the way the vectors write `catalog_ref: "CVE-2026-30111"`
(mvp-01). It is never the node id: “The canonical file ID is authoritative; adapters MUST map to it
**without churning IDs**.” (ADR-0004), and the vectors mint `vulnerability:cve-2026-30111` as the node.
The prefix maps to a Party (an organization) that asserts every Assertion made from the record. Because
the JSON Schema does not check the 1.9.2 character rule (defect 3; E11 P01, P03), the importer checks it
before an id reaches a path or an IRI; a record that fails is kept as evidence and never used as a key.
*Bears on:* DEC-001a (accepted, ADR-0010) and DEC-011 (accepted, ADR-0004), both unchanged. Recording
the asserting party needs provenance on Assertion, which the accepted core lacks (`mapping.md` §3, pilot
finding 5; #15, #17).

**Adopt-2. `aliases`, `upstream` and `related` as three different Assertion predicates, each with the
algebra OSV gives it.**
`aliases` means "the same vulnerability": “This allows one database to claim that its own entry describes
the same vulnerability as one or more entries in other databases.” (§ aliases field / L759-L761), and
“Aliases should be considered symmetric (if A is an alias of B, then B is an alias of A) and transitive
(If A aliases B and B aliases C, then A aliases C).” (L768-L769, R-0034). `upstream` means "derived from", with a
direction: “`upstream` should be considered transitive but not symmetric.” and “if B is an upstream
vulnerability for A, then A cannot be an upstream vulnerability for B.” (§ upstream field / L795-L797, R-0039, R-0040).
`related` is neither: “Related vulnerabilities are symmetric but not transitive.” (§ related field /
L812, R-0042). The line between the first two is a "must not": “the distribution's OSV record must not list the
CVE ID as an alias. Similarly, distributions often bundle multiple upstream vulnerabilities into a single
record. To refer to these upstream vulnerabilities, `upstream` should be used.” (§ aliases field /
L775-L778, R-0036, R-0037). **[analysis]** The accepted `predicate` slot is “Not a closed enum” (LinkML `predicate`), so
each relation is an Assertion between two Vulnerability nodes with no schema change. `upstream` keeps its
direction (subject: the downstream record's node; object: the upstream one), and neither `upstream` nor
`related` is ever read as identity. This corrects one candidate cell of RPT-0004's Phase 1 notes, “key
by CVE id; GHSA, OSV and distribution ids as aliases” (`fanout-bridge.md` §5, Vulnerability row): by
L775-L776 a distribution advisory relates to the CVE through `upstream`, not `aliases` (open question 8).
*Bears on:* DEC-001a (accepted, ADR-0010: Assertion), unchanged; naming these predicates joins the ones
`mapping.md` §3 already lists under "Needs a decision first" (#15); DEC-008 (open).

**Adopt-3. Range evidence kept as written, with everything OSV says is needed to read it.**
R-RANGE-1 already says “Keep a version range as written, with its scheme” (`mapping.md` §10). OSV says
what the scheme is made of. The range type: “It specifies the type of version range being recorded and
defines the interpretation of the `events` object's `introduced`, `fixed`, and any type-specific
fields.” (§ affected[].ranges[].type field / L1092-L1094, R-0162). The ecosystem, because for `ECOSYSTEM` ranges
the versions “are arbitrary, uninterpreted strings specific to the package ecosystem, which does not
conform to SemVer 2.0’s version ordering.” (L1110-L1112, R-0169), and a suffix can change the ordering: an Echo
suffix denotes a build “in which case the `name` is the name of the package within that ecosystem and
its versions are ordered by that ecosystem's rules” (§ Defined ecosystems / L1005, R-0099). The repository, for
`GIT` ranges: “This field is required if `affected[].ranges[].type` is `GIT`.” (§ affected[].ranges[].repo
field / L1198, R-0194). And the enumerated list, recommended “to allow software to easily answer the question "is
this specific version affected?" without having to contain code specific to every different ecosystem”
(§ affected fields / L937-L939, R-0069). OSV also warns that the strings may not be the registry's own: “Note
that these version strings are not guaranteed to exactly match versions of the package found in the
upstream package repository. For example, they may be normalized, or have build metadata stripped.”
(§ affected[].ranges[].events fields / L1144-L1147, R-0176). **[analysis]** For an OSV source, R-RANGE-1's
"scheme" is therefore the tuple (range `type`, full `ecosystem` string, `repo`), and the `versions[]`
list travels with the ranges. Until a slot exists the range has no target in the accepted core (Table
6d, "Version range and its scheme" row).
*Bears on:* RPT-0004 R-RANGE-1 (candidate); DEC-008 and DEC-009 (open); #17.

**Adopt-4. `IsVulnerable` as the meaning of an OSV match, computed in the working store.**
“**A version is considered affected if it lies within any one of the ranges or is listed in the versions
list.**” (§ affected fields / L933-L934, R-0068), and “The algorithm to evaluate if a package `pkg` at version `v`
is vulnerable is given by the `IsVulnerable` function in the pseudocode below:” (§ Evaluation /
L1244-L1245, R-0201). **[analysis]** This is the predicate behind R-MATCH-1's “One Assertion per match”
(`mapping.md` §10) when the source is an OSV record. The Assertion's evidence names the record (`id`,
`modified`), the `affected[]` entry, and whether a range or the `versions` list decided it. The yes or no
itself is derived data, recomputed at load, since the working store is “Still a rebuildable cache.”
(ADR-0008). The pseudocode leaves several things open (defects 7 and 8); Adapt-5 closes them.
*Bears on:* RPT-0004 R-MATCH-1 (candidate); DEC-004 (accepted, ADR-0008), unchanged; DEC-008 (open).

**Adopt-5. Severity entries as attributed evidence, with OSV's default attribution.**
“The `severity` field is a JSON array that allows generating systems to describe the severity of a
vulnerability using one or more quantitative scoring methods.” (§ severity field / L851-L853, R-0050). Each entry
is a `type` and a `score` string, and for the CVSS types the score is “A CVSS vector string”
(§ severity[].type field / L863-L865, R-0053, R-0054, R-0055), not a number. Attribution has a default: “If `source` is omitted,
the rating is implicitly attributed to the home database (as identified by the record's `id` field),
whether as author or endorser.”, and `SELF` is the explicit form: “Unlike omitting `source`, this is an
explicit declaration of provenance.” (§ severity[].source field / L879-L880, R-0059; L886, R-0062). Package-level
severity excludes record-level severity: “If any package level `severity` fields are set, the top level
[`severity`](#severity-field) must not be set.” (§ affected[].severity field / L1071-L1073, R-0154).
**[analysis]** Keep each entry as received (type, vector string, source or "home database by default",
record level or package level), and parse vectors with a CVSS library, because the schema accepts
strings that are not complete vectors (defect 11). Where they go is already a Table 6d rule: “display
attributes once a slot exists; risk itself is ADR-0006's composite vector” (Scores row).
*Bears on:* DEC-003 (accepted, ADR-0006), unchanged (Reject-1); #17 for the slot.

**Adopt-6. `details` as untrusted CommonMark.**
“The `details` field is CommonMark markdown (a subset of GitHub-Flavored Markdown). Display code may at
its discretion sanitize the input further, such as stripping raw HTML and links that do not start with
http:// or https://. Databases are encouraged not to include those in the first place. (The goal is to
balance flexibility of presentation with not exposing vulnerability database display sites to
unnecessary vulnerabilities.)” (§ summary, details fields / L832-L837, R-0047, R-0048, R-0049). **[analysis]** tmodel's GUI is
such a display site. Render `details` with raw HTML removed and only `http` and `https` links, and treat
it as data, never as instructions, wherever an AI proposer reads it (Table 6f names "an AI proposer" as
a source of threats). `summary` (“a one-line, English textual summary”, L823, R-0043) fills the accepted Node
`name`, and `details` fills `description`, both as text the importer does not interpret.
*Bears on:* DEC-006 (accepted, ADR-0003) for display; DEC-001a (accepted, ADR-0010: Node `name`,
`description`), unchanged.

**Adopt-7. Read newer minor versions by ignoring unknown fields, and record `schema_version`.**
“Clients can assume that new minor and patch versions of the schema only add new fields, without
changing the meaning of old fields, so that a client that knows how to read version 1.2.0 can process
data identifying as schema version 1.3.0 by ignoring any unexpected fields.” (§ schema_version field /
L129-L132, R-0008), and “If no value is specified, it should be assumed to be `1.0.0`, matching version 1.0 of
the OSV Schema.” (L128-L129, R-0007). **[analysis]** The importer parses leniently, records the declared
`schema_version` (or "absent, read as 1.0.0") with the import, warns on unknown fields and keeps them in
the raw record. Records in the wild declare 1.4.0, 1.7.0 and 1.9.0 (E9), so mixed versions are the
normal case. This is the opposite of gating on `validation/schema.json` (Reject-4).
*Bears on:* DEC-002 (accepted, ADR-0007), unchanged: “The DEC-002 round-trip contract (CF-008, #9)
governs every import/export vector.” (ADR-0007).

---

## What we adapt, and how

**Adapt-1. Package to Component through a versioned crosswalk, because OSV keys on (ecosystem, name) and
defines no purl mapping.**
OSV's key is the pair: “The two fields must both be present, because the `ecosystem` serves to define the
interpretation of the `name`.” (§ affected[].package field / L956-L957, R-0076), and “Different ecosystems can
define the same names; they identify different packages.” (L969-L970, R-0080). The purl is secondary: it
“identifies the package, without the `@version` component. This field is optional but recommended.”
(L966-L967, R-0078, R-0079), and the schema types it as a plain string
(`schema.json` `/properties/affected/items/properties/package/properties/purl`), so a versioned or
malformed purl validates (E11 P37, P38) and real copies differ (E2). Name conventions differ per
ecosystem: PyPI's `name` “is a [normalized](https://www.python.org/dev/peps/pep-0503/#normalized-names)
PyPI package name” (§ Defined ecosystems / L1028, R-0126), Maven's is “in the format `groupId:artifactId`”
(L1017, R-0114). OSV has no table from ecosystem to purl type; four ecosystem rows mention purls at all
(Homebrew, openSUSE, SUSE, vcpkg; L1012, L1023, L1034, L1038; R-0108, R-0120, R-0133, R-0139) [observation: text search, 2026-10-18].
Recommended, offered to DEC-009 and to R-ID-3 (not a decision):

1. Derive (ecosystem, name) from the Component's purl through a crosswalk table (purl type, namespace
   and name to OSV ecosystem and name), versioned and recorded with every match.
2. Use the record's `purl` only after projecting both sides to (type, namespace, name), as the `ecma-427`
   design notes recommend for advisory purls (their Adapt-4, steps 1 and 2).
3. When (ecosystem, name) and `purl` disagree, (ecosystem, name) governs, since only they are required
   (our reading of L951-L952, R-0073); the record goes to Review.
4. Never compare an OSV `name` with a Component name without the crosswalk.

*Bears on:* DEC-009 (open); RPT-0004 R-ID-3, R-MATCH-1 and R-MATCH-2 (candidates).

**Adapt-2. Distribution ecosystems: match the source package, then reach the binaries.**
Distribution rows name source packages: for Alpine “the `name` is the name of the source package”
(L992, R-0084), and Debian (L1003, R-0097), Ubuntu (L1037, R-0136), AlmaLinux (L990, R-0082) and Rocky Linux (L1031, R-0130) say the same. SBOMs
list binary packages, and Table 6b already proposes the bridge: “a "built from" edge to a source
Component keyed by R-ID-3” (Upstream (source) package row). OSV documents binary lists for some
ecosystems: “There is a `ecosystem_specific` specific array `binaries` of the associated RPM binary
packages in this specific SUSE product.” (L1034, R-0133; openSUSE has a matching sentence, L1023, R-0120), and openEuler's
`ecosystem_specific` “contains all updated packages, including src rpm and binaries of different
architectures” (L1022, R-0119). The release is part of the key: Alpine's ecosystem string “must have a
`:v<RELEASE-NUMBER>` suffix to scope the package to a particular Alpine release branch” (L992, R-0085).
Recommended, offered to DEC-009 and to #15 and #17: match a distribution record against the source
(origin) Component of the instance's distribution release, then reach the binary Components through the
"built from" Assertion; use a documented `binaries` list (SUSE, openSUSE, openEuler; Ubuntu by its own
documentation, E6) as evidence for that edge, never as a second match key.
*Bears on:* DEC-009 (open); RPT-0004 R-ID-3 (candidate) and Table 6b's Upstream row (#15, #17).

**Adapt-3. Ecosystem strings: split once, interpret per ecosystem.**
The schema accepts any suffix after any listed name: its pattern ends in `GIT)(:.+)?$`
(`schema.json` `/$defs/ecosystemWithSuffix/pattern`). The suffix means different things per row: a
release (Alpine `:v<RELEASE-NUMBER>`, L992, R-0085; Debian `:<RELEASE>`, L1003, R-0097), a repository URL
(“`Maven:https://maven.google.com`”, L1017, R-0114), a product-stream CPE (“The ecosystem string has a `:<CPE>`
suffix to scope the RPM to a specific Red Hat product stream.”, L1029, R-0127), another ecosystem (Echo, L1005, R-0099;
Red Hat Lightwell, L1030, R-0128), a hierarchy (“Root:{BaseDistro}:{Version}”, L1032, R-0131), a component (WordPress,
L1041, R-0142), or a release with a prefix and a mandatory tag (“"Ubuntu:Pro:18.04:LTS"”, L1037, R-0138). Several
suffixes contain colons themselves. Recommended, offered to DEC-009: split at the first colon only;
interpret the rest with a per-ecosystem rule from a pinned table; keep an unknown suffix raw and match
it only after Review; and treat the distribution release as an identity attribute of the OS Component,
as the `ecma-427` design notes propose for purl qualifiers (their Adapt-3, "identity-scoping").
*Bears on:* DEC-009 (open); RPT-0004 R-ID-3 (candidate).

**Adapt-4. `aliases` are claims to link, not identities to merge.**
An alias is one database's claim: “This allows one database to claim that its own entry describes the
same vulnerability as one or more entries in other databases.” (§ aliases field / L759-L761). OSV asks
consumers to treat the relation as symmetric and transitive (L768-L769, R-0034, quoted in Adopt-2) but gives no
rule for two databases that disagree, and its own Rust example lists two CVE ids as aliases of one entry,
`"aliases": ["CVE-2020-25574", "CVE-2019-25008"]` (§ Rust vulnerability / L1676), which closure turns
into aliases of each other. Table 6d keys one Vulnerability per CVE id and loses the rest: “other ids
(GHSA, OSV, distribution advisories): `catalog_ref` is single-valued and Vulnerability has no
`identifiers`” (Vulnerability row, Lost column). Recommended, offered to #15 (not a decision):

1. One Vulnerability node per imported record, with the record's id in `catalog_ref` (Adopt-1).
   CVE-keyed nodes stay the hub for ADR-0002's CVE → CWE → CAPEC → ATT&CK backbone.
2. Each `aliases` entry becomes a proposed equivalence Assertion asserted by the home database;
   `upstream` and `related` follow Adopt-2.
3. The symmetric and transitive closure is computed in the working store as a candidate grouping and is
   never written back.
4. Nodes merge only through a reviewed equivalence, the pattern R-MERGE-2 sets for Components (“Merge two
   Components only through an equivalence Assertion”, `mapping.md` §10).

**[analysis]** The cost is more nodes and one more hop in queries. The gain is that GHSA, OSV and
distribution ids, which Table 6d loses, survive, and that a wrong alias claim stays one reviewable edge.
The alternative, keeping Table 6d's rule, needs either a multivalued identifier on Vulnerability, which
changes an accepted class, or accepting the loss (open question 1).
*Bears on:* DEC-001a (accepted, ADR-0010: Vulnerability, Assertion, Review), unchanged under this
recommendation; #15; DEC-008 (open).

**Adapt-5. `IsVulnerable` with its gaps closed: a tmodel evaluation profile.**
The pseudocode is short and leaves five things to the reader (defects 7 and 8): what
`affected.package == pkg` (§ Evaluation / L1250, R-0201) compares; the wildcard (“Use the wildcard package name
`*` to indicate that an advisory affects all packages within the specified `ecosystem`.”,
§ affected[].package field / L959-L960, R-0077); entries with no `package` (L1059, R-0148); withdrawn records; and the
order of `sorted(range.events)` (L1268, R-0201) when two events share a version. Recommended profile, offered
to DEC-009 and to R-MATCH-1 (not a decision):

1. Package equality is Adapt-1's crosswalk, with Adapt-2's source-package rule and Adapt-3's suffix rule.
2. A `*` entry matches the ecosystem release as a whole: one Assertion to the OS or ecosystem Component,
   not one per package [analysis].
3. An entry without `package` is matched only by repository and commit (Reject-6).
4. A withdrawn record yields no new match (Adapt-6).
5. Events sort by the range type's ordering, and at equal versions `introduced` comes first.
   **[analysis]** With `[{"introduced": "1.0.0"}, {"last_affected": "1.0.0"}]` and v = 1.0.1, the printed
   loop returns not affected if `introduced` is visited first and affected if `last_affected` is (a hand
   trace of L1264-L1279, R-0201).
6. A `limit` of `"*"` is unbounded (“`limit` allows versions containing the string `"*"` to represent
   "infinity".”, § Special values / L1153, R-0178); `BeforeLimits` (L1281-L1290, R-0201) needs that case.
7. `IncludedInVersions` compares with `v == version` (L1259, R-0201); compare after the ecosystem's normalization,
   because the strings “may be normalized, or have build metadata stripped” (L1146-L1147) [our reading].
8. Record the profile version with every derived result, as the `ecma-427` design notes do for purl
   comparison (their Adapt-1, step 6).

*Bears on:* DEC-009 and DEC-008 (open); RPT-0004 R-MATCH-1 (candidate); DEC-004 (accepted, ADR-0008)
for where the derived result lives.

**Adapt-6. Withdrawn records: retract the matches, keep the evidence.**
“The `withdrawn` field gives the time the entry should be considered to have been withdrawn, as an
RFC3339-formatted timestamp in UTC (ending in "Z"). If the field is missing, then the entry has not been
withdrawn. Any rationale for why the vulnerability has been withdrawn should go into the summary text.”
(§ withdrawn field / L745-L748, R-0029, R-0030, R-0031). `IsVulnerable` never reads it (L1248-L1255, R-0201). RPT-0005 found that
“Withdrawal has no successor.” (`fanout-vuln-data.md` §1.1; E8). Recommended, offered to #15: when a
record arrives withdrawn, move its match Assertions to a retracted `assertion_status` (the slot's values
are open: “Proposal status of the Assertion (§4).”, LinkML `assertion_status`), keep the node with its
withdrawal time, delete nothing, and flag any accepted Review that rests on those matches for re-review.
*Bears on:* DEC-001a (accepted, ADR-0010: `assertion_status`, Review), unchanged; #15 for the status
value.

**Adapt-7. `modified` decides only among copies from the same source.**
“Given two different entries claiming to describe the same `id` field, the one with the later
modification time is considered authoritative.” (§ modified field / L717-L719, R-0024). The prefix table gives
each database a “Source URL” and an “OSV Formatted URL” (for example L194-L195), and several databases
are “(provided by OSV.dev)” (L212, L300, L311, L344): the same id can arrive from the home database and
from OSV.dev. Those copies differ. OSV.dev adds purls and a newer `schema_version` to GitHub's records
and removes versions from Canonical's purls (E1, E2). Recommended, offered to DEC-008: record the source
(URL or export file, retrieval time, SHA-256 of the bytes), `id` and `modified` with every import; apply
"later `modified` wins" only within one source; keep copies from different sources side by side as
separate evidence; and send a tie (same `id` and `modified`, different content) to Review, since the
specification's own examples contain one (defect 15).
*Bears on:* DEC-008 (open); RPT-0004 R-PROV-2 (candidate); Assertion provenance (`mapping.md` §3, pilot
finding 5; #15, #17).

**Adapt-8. CWE from OSV: one database's convention, read by an opt-in rule.**
OSV has no weakness field, and the place a database could put one is opaque by definition: “The meaning
of the values within the object is entirely defined by the database and beyond the scope of this
document.” (§ affected[].database_specific field / L1229-L1230, R-0199; the same sentence for the record level,
§ database_specific field / L1531-L1532, R-0222). The specification's own GitHub example puts
`"cwe_ids": [ "CWE-327" ]` inside `database_specific` (§ NPM vulnerability in GitHub database /
L1621-L1624). `report.md` §5 already records that “OSV has no CWE field”, and RPT-0004 measured that only
GHSA records carry `cwe_ids` (E5). Recommended, offered to #61 and DEC-008: read
`database_specific.cwe_ids` only from records whose prefix is `GHSA`, each id becoming an R-CWE-1
Assertion whose source names "GitHub Advisory Database, through OSV `database_specific`"; obtain CWEs
for every other record through its CVE alias from CVE or NVD data; and read no other `database_specific`
or `ecosystem_specific` key as tmodel data without a written per-database rule.
*Bears on:* DEC-008 (open); #61; RPT-0004 R-CWE-1 (candidate).

---

## What we reject, and why

**Reject-1. OSV severity as RiskScore, feasibility or impact.**
OSV severity is a database's score for the vulnerability in general (“describe the severity of a
vulnerability using one or more quantitative scoring methods”, L851-L853, R-0050), and one of its types is not a
severity at all: Ubuntu priority “is based on many factors including severity, importance, risk,
estimated number of affected users, software configuration, active exploitation, and other factors.”
(§ severity[].type field / L866, R-0056). tmodel's risk is a composite vector: “No single-number CVSS substituted
for the vector” (ADR-0006, scope guard), and the LinkML `risk` slot says “Not a CVSS base score.”
**[analysis]** Neither a CVSS vector nor a distribution's priority can feed `feasibility`, which ADR-0006
makes ISO/SAE 21434 Table-1 and human-rated at MVP, or `impact`, the human-supplied S/F/O/P vector.
Severity stays attributed evidence (Adopt-5).
*Bears on:* DEC-003 (accepted, ADR-0006), unchanged.

**Reject-2. "No OSV range matches" read as "not affected".**
OSV lists what is affected and nothing else: “The `affected` field is a JSON array containing objects
that describes the affected package versions, meaning those that contain the vulnerability.” (§ affected
fields / L920-L921, R-0063). Its own boundary can fail in the reassuring direction: “Versions above
`last_affected` should be considered unaffected. Unfortunately this opens up the possibility for false
negatives, which is why `fixed` is overwhelmingly preferred.” (§ affected[].ranges[].events fields >
Requirements / L1168-L1170, R-0185). RPT-0005 found that “There is no `not_affected`, no justification, and no
status other than affected-in-range.” (`fanout-vuln-data.md` §1.1), and Ubuntu's records leave out `DNE`
and `not-affected` packages alike (E6). **[analysis]** A Component that no OSV range matches gets no
Assertion at all, not a negative one. A not-affected statement comes only the way the vectors make one:
an Assertion with `predicate: vex_not_affected` and a Review (Table 6d, VEX override row; mvp-18).
*Bears on:* DEC-009 (open); RPT-0004 R-MATCH-1 (candidate); DEC-001a (accepted, ADR-0010), unchanged.

**Reject-3. Importing OSV's JSON Schema or protobuf into the LinkML model, or treating OSV as an
accepted import.**
OSV describes a serving format, not a model: “The format is a JSON-based encoding format, using the
following informal schema.” (§ Format Overview / L39, R-0001) and “Again, this document is only about the JSON
encoding the database serves to consumers, which could be applications or other databases.”
(L102-L103, R-0003). Its protobuf says of itself: “The protobuf representation is *NOT* stable and only used for
implementing the JSON based API.” (`proto` `Vulnerability`, leading comment). ADR-0007 commits two
imports, OTM and STIX 2.1, and says “interchange additions arrive as MAP-NNNN + a vector, never as
silent schema drift”; the LinkML header says “This file is OUR model, not those schemas.” **[analysis]**
An OSV importer is therefore an interchange addition: a `MAP-NNNN` crosswalk plus a vector under
ADR-0007, or part of the radar contract under ADR-0001, a choice `mapping.md` (finding 8) leaves to #15
and #17. Either way OSV's shapes stay outside the LinkML file, and the protobuf is never the contract.
*Bears on:* DEC-002 (accepted, ADR-0007), DEC-001a (accepted, ADR-0010) and DEC-007 (accepted,
ADR-0001), all unchanged.

**Reject-4. `validation/schema.json` as an import gate.**
The prose promises forward compatibility (Adopt-7, L129-L132, R-0008). The schema forbids unknown top-level
properties (`schema.json` `/additionalProperties` is `false`, R-0237) and lists prefixes and ecosystems as closed
patterns (`/$defs/prefix/pattern`, R-0230; `/$defs/ecosystemWithSuffix/pattern`, R-0229), while the table invites new
databases (“Your database here”, L706). It also misses rules the prose states, among them 1.9.2's `id`
characters (defect 3). [observation, E11] A record with an unknown top-level field (P09), from an
unlisted database (P04) or using the table's own spelling `CleanStart` (P05) fails; an id with a space
and a slash after its prefix passes (P01). **[analysis]** A gate on this file would drop exactly the
records a newer OSV version or a newer database produces, and admit ids the specification forbids.
Recommended: tmodel's own checks decide (Adopt-1, Adopt-7, Adapt-3), and the JSON Schema runs as a
warning-only lint, pinned by digest.
*Bears on:* DEC-002 (accepted, ADR-0007; the round-trip contract, #9), unchanged.

**Reject-5. A live service's answer as the match.**
OSV defines a match as an evaluation over the record (Adopt-4, L1244-L1245, R-0201); range expansion is
something “Tooling and infrastructure such as https://osv.dev are able to” do (§ affected fields /
L943-L944), not part of the record. The OSV.dev query API matches differently: its documentation says
“A fuzzy match is done against upstream versions.” (E4), and purl spellings change its answers (0, 52 or
82 advisories for one Debian package version; E3). tmodel's draft requirements ask that the core loop
“works without network for the core loop (ingest → graph → review); external lookups (NVD/CWE) may be
cached (DEC-008)” (APP-0001 A-043, draft). Recommended, offered to DEC-008: evaluate locally against a
pinned export (OSV.dev's per-ecosystem `all.zip`, library record `osv-dev`), recording the export's URL,
date and SHA-256 with each match (R-PROV-2).
*Bears on:* DEC-008 (open); APP-0001 A-043 (draft); RPT-0004 R-PROV-2 (candidate).

**Reject-6. Evaluating `GIT` ranges inside tmodel.**
“The repository’s commit graph is needed to evaluate whether a given version is in the range.” and
“Specifying one or more `GIT` ranges does NOT remove the requirement to specify an explicitly enumerated
`versions` list, because `GIT` range inclusion queries cannot be answered without access to a copy of
the underlying Git repository.” (§ affected[].ranges[].type field / L1123-L1124, L1127-L1129, R-0173).
**[analysis]** Evaluating a `GIT` range means cloning the repository and walking its graph, which is
network access and large local state inside the core loop (A-043), and the printed loop does not settle
the order of commits on different branches (defect 8). Recommended, offered to DEC-008 and DEC-009: use
the record's enumerated `versions` (tags, L1065, R-0150) when present, and otherwise keep the `GIT` range as
unevaluated evidence. A `GIT`-only entry links to a Component only when the Component names the same
repository (a normalized clone URL; `repo` is “directly usable as an argument for the version control
system's clone command”, L1191-L1192, R-0192) at a named commit. Any other link is a "built from" Assertion that
needs a Review, as the `ecma-427` design notes say for purls of different types (their Reject-5).
*Bears on:* DEC-008 and DEC-009 (open); APP-0001 A-043 (draft).

**Reject-7. `credits[]` as Party identities, and contact URLs in tmodel's files.**
A credit is a free-form label: `credits[].name` “should specify the name, label, or other identifier of
the individual or entity being credited, using whatever notation the creditor prefers.” (§ credits[].name
field / L1479-L1480, R-0215), and a contact “should be a valid, fully qualified, plain-text URL at which the
credited can be reached.” (§ credits[].contact[] field / L1487-L1488, R-0217); the specification's example
includes a `mailto:` address (L1520). **[analysis]** A Party is “One reusable identity for an organization
or a person” (LinkML `Party`). A label in whatever notation its owner prefers cannot be matched to one
without guessing, and contact addresses are personal data the threat model does not need in its
canonical git files. The accepted `reported_by` is single-valued (“Reporter (§2b).”, LinkML), and OSV's
own `REPORTER` definition is garbled (defect 22). Recommended: create no Party from a credit and copy no
`contact[]`; keep at most each credit's `type`, with the raw record, as evidence.
*Bears on:* DEC-001a (accepted, ADR-0010: Party, `reported_by`), unchanged.

---

## Mapping to our decisions

### Mapping table: OSV structures and fields to tmodel's accepted core

Targets are the accepted classes and slots of `spec/schema/tmodel-object-model.linkml.yaml` (DEC-001a,
ADR-0010). Where RPT-0004's Table 6 (`mapping.md`) already states a rule, the row cites it by id or row
name instead of restating it. "Lost" is what an importer loses against the accepted core as it stands.

| OSV element (locator) | tmodel class or slot | stance | lost | bears on (status) |
|---|---|---|---|---|
| a record, one JSON object (§ Format Overview / L39, R-0001; L46-L99) | one Vulnerability node per record | adapt (Adapt-4) | nothing under Adapt-4; the record's own id under Table 6d's CVE keying | DEC-001a (accepted, ADR-0010); #15 |
| `id` (§ id, modified fields / L143-L145, R-0009, R-0010; `/properties/id`, R-0230) | Vulnerability `catalog_ref`; the node `id` is minted by tmodel (ADR-0004) | adopt (Adopt-1) | nothing; under Table 6d, every id that is not a CVE (Vulnerability row, Lost) | DEC-001a, DEC-011 (accepted) |
| id prefix (§ Defined database prefixes / L174-L710, R-0019; `/$defs/prefix`, R-0230) | Party (organization) asserting each Assertion | adopt (Adopt-1) | the asserting database, until Assertion has provenance (pilot finding 5) | DEC-001a (accepted); #15, #17 |
| `schema_version` (§ schema_version field / L115-L132, R-0005 to R-0008) | none: import provenance | adopt (Adopt-7) | the declared version, until provenance slots exist | DEC-002 (accepted, ADR-0007) |
| `modified`, `published` (§ modified field, § published field / L714-L735, R-0022 to R-0024, R-0028) | none: import provenance | adapt (Adapt-7) | both times | DEC-008 (open); R-PROV-2 (candidate) |
| `withdrawn` (§ withdrawn field / L737-L748, R-0029 to R-0031) | `assertion_status` of the record's Assertions (value open) | adapt (Adapt-6) | the time, and the reason (free text) | DEC-001a (accepted); #15 |
| `aliases[]` (§ aliases field / L750-L778, R-0032 to R-0037) | Assertion, Vulnerability to Vulnerability: a proposed equivalence | adopt, adapt (Adopt-2, Adapt-4) | the alias ids, under Table 6d's rule ("alias ids (GHSA, OSV)", `mapping.md` §3) | DEC-001a (accepted); #15 |
| `upstream[]` (§ upstream field / L780-L797, R-0038 to R-0040) | Assertion, downstream to upstream Vulnerability | adopt (Adopt-2) | the direction, if folded into `aliases` | DEC-001a (accepted); #15 |
| `related[]` (§ related field / L799-L812, R-0041, R-0042) | Assertion, symmetric, never identity | adopt (Adopt-2) | nothing | DEC-001a (accepted) |
| `summary` (§ summary, details fields / L823-L825, R-0043, R-0044) | Node `name` ≈ | adopt (Adopt-6) | nothing | DEC-001a (accepted) |
| `details` (L827-L837, R-0045, R-0047 to R-0049) | Node `description` ≈, as sanitized CommonMark | adopt (Adopt-6) | Markdown structure, if flattened | DEC-001a, DEC-006 (accepted) |
| record-level `severity[]` (§ severity field / L839-L886, R-0050 to R-0062) | none: Table 6d, Scores row | adopt as evidence (Adopt-5); reject as risk (Reject-1) | every score, until a slot exists | DEC-003 (accepted, ADR-0006); #17 |
| an `affected[]` entry (§ affected fields / L888-L946, R-0063 to R-0071) | one match Assertion per (record, entry, Component): R-MATCH-1 | adopt (Adopt-4) | which entry and which range decided, until provenance slots exist | DEC-009 (open); R-MATCH-1 (candidate) |
| `affected[].package.ecosystem` (L954, R-0074; § Defined ecosystems / L981-L1048, R-0081 to R-0143) | inside the Component's purl (type, release qualifier): Table 6 "Kept only inside a string" | adapt (Adapt-1, Adapt-3) | the suffix's meaning, without a per-ecosystem rule | DEC-009 (open) |
| `affected[].package.name` (L955-L957, R-0075, R-0076) | the Component, through the crosswalk; for distributions, the source Component | adapt (Adapt-1, Adapt-2) | the source and binary distinction, unless a "built from" edge exists | DEC-009 (open); R-ID-3 (candidate) |
| `affected[].package.purl` (§ affected[].package field / L964-L967, R-0078, R-0079) | Component `identifiers`, compared as a versionless projection: R-ID-3, R-MATCH-2 | adapt (Adapt-1) | nothing (kept raw) | DEC-001a (accepted); R-ID-3 (candidate) |
| `affected[].severity[]` (§ affected[].severity field / L1067-L1073, R-0152 to R-0154) | an attribute of the match Assertion (no slot) | adopt as evidence (Adopt-5) | per-package scores | DEC-003 (accepted); #17 |
| `affected[].ranges[]`: `type`, `repo`, `events[]` (L1085-L1198, R-0160 to R-0194) | target: none; R-RANGE-1 | adopt (Adopt-3) | the range as data, until a slot exists (Table 6d, version range row) | DEC-008, DEC-009 (open); #17 |
| `affected[].ranges[].database_specific` (L1200-L1209, R-0195 to R-0197) | none; it has “no effect on the [evaluation algorithm](#evaluation)” (L1209, R-0197) | keep raw | its content | none |
| `affected[].versions[]` (§ affected[].versions field / L1075-L1083, R-0155 to R-0159) | evidence on the match Assertion (no slot) | adopt (Adopt-3) | the list | DEC-009 (open) |
| `affected[].ecosystem_specific` (L1211-L1223, R-0198) | none; per-ecosystem readers only (`binaries`, Adapt-2) | adapt | function-level data such as Go's (L1218-L1220) | DEC-009 (open) |
| `affected[].database_specific` and the record's `database_specific` (L1225-L1240, R-0199, R-0200; L1527-L1539, R-0222, R-0223) | none; GHSA's `cwe_ids` to Weakness through R-CWE-1 | adapt (Adapt-8) | every other key | DEC-008 (open); #61 |
| (no field) a weakness | Weakness `catalog_ref` and an R-CWE-1 Assertion | through Adapt-8, or through the CVE alias | the CWE, for records other than GHSA's | DEC-008 (open); #61 |
| `references[]` (§ references field / L1416-L1455, R-0205 to R-0211) | none; a `FIX` link is remediation evidence on the match (Table 6d, Fix information row) | keep as evidence | every link and its type | #15 |
| `credits[]` (§ credits fields / L1457-L1525, R-0212 to R-0221) | none: not a Party, not `reported_by` | reject (Reject-7) | the credit roles | DEC-001a (accepted) |
| (no field) a product | Product `affects`, only by propagation, as R-MATCH-1 proposes | none from OSV | | DEC-001a (accepted); pilot finding 2 |
| (no field) an instance | ProductInstance, reached through R-MERGE-1's composition Assertions | none from OSV | | DEC-009 (open); #15 |
| (no field) a mitigation | none: a fixed version is a remediation option, not a Mitigation (Table 6d, Fix information row) | none from OSV | | DEC-009 (open) |
| (no field) a review | Review: none imported; imported Assertions start `proposed` (Table 6d, Review row) | none from OSV | | DEC-001a (accepted) |
| the `IsVulnerable` result (§ Evaluation / L1242-L1292, R-0201) | derived in the working store | adopt, adapt (Adopt-4, Adapt-5) | nothing (recomputed) | DEC-004 (accepted, ADR-0008) |

### Per decision

- **DEC-001a (accepted, ADR-0010).** OSV fits the accepted classes as they stand: a record's id is a
  `catalog_ref`; its matches, aliases, upstream links and CWE links are Assertions (`predicate` is open);
  its purls go to Component `identifiers`; and its CWEs go to Weakness through R-CWE-1 (Adopt-1, Adopt-2,
  Adapt-8). Two losses would need an accepted class to change, which only an ADR superseding or refining
  ADR-0010 can do: alias ids under Table 6d's CVE keying (avoided by Adapt-4), and the provenance an
  Assertion cannot hold today (pilot finding 5, already open).
- **DEC-001b (open).** No bearing found. A record's `modified` and `withdrawn` are supersession and
  retraction of a claim; they are not the governed layer's `supersedes` and do not touch blocker C2.
- **DEC-002 (accepted, ADR-0007).** OSV is not on the committed import list. An importer is an
  interchange addition (a `MAP-NNNN` crosswalk plus a vector) or part of the radar contract (open
  question 2); it reads leniently (Adopt-7), does not gate on OSV's JSON Schema (Reject-4), and keeps
  OSV's shapes out of LinkML (Reject-3).
- **DEC-003 (accepted, ADR-0006).** Severity is evidence, never an input to the composite vector
  (Adopt-5, Reject-1).
- **DEC-004 (accepted, ADR-0008) and DEC-011 (accepted, ADR-0004).** Raw records and their provenance
  belong in git; evaluation results, alias groupings and crosswalk outputs are derived in the rebuildable
  store (Adopt-4, Adapt-4, Adapt-5); OSV ids are catalog references, never node ids (Adopt-1).
- **DEC-005 (accepted, ADR-0002).** OSV reaches the CVE → CWE → CAPEC → ATT&CK backbone only through CVE
  aliases and upstream links, and supplies the CVE → CWE step only through GitHub's convention (Adapt-8).
- **DEC-006 (accepted, ADR-0003).** The GUI renders `details` as sanitized Markdown (Adopt-6).
- **DEC-007 (accepted, ADR-0001).** radar's scanners already use OSV-derived data; whether tmodel also
  reads OSV records itself is open question 2.
- **DEC-008 (open).** The channel (pinned exports, not live answers: Reject-5), the copy (Adapt-7), the
  CWE source (Adapt-8) and `GIT` ranges (Reject-6) are evidence for its live-versus-cached question,
  which `DECISIONS-0001` describes as “leaning cached mirror per A-043”. They are evidence, not an
  answer.
- **DEC-009 (open).** Most of the matching lands here: the package crosswalk, the source-to-binary
  bridge, ecosystem suffixes, the evaluation profile, and the rule that no match is not "not affected"
  (Adapt-1 to Adapt-3, Adapt-5, Reject-2). The LinkML description already places `identifiers` in “the
  generic↔instance half of DEC-009”.
- **RPT-0004 (draft report; candidate rules).** R-RANGE-1 holds and gains OSV's parts (Adopt-3).
  R-MATCH-1 holds, with Adapt-5's profile. R-CWE-1 gains GitHub's convention as a source (Adapt-8).
  R-MERGE-2's pattern extends to Vulnerabilities (Adapt-4). Table 6d's "one Vulnerability per CVE id"
  loses OSV ids (Adapt-4), and Phase 1's "distribution ids as aliases" contradicts OSV (Adopt-2).
- **D-3** (the scaffold's rule for COSE, CBOR and envelope documents) does not apply: OSV is none of
  these.

---

## Source defects and ambiguities

Places where OSV 1.9.2 contradicts itself, disagrees with its own JSON Schema or protobuf, or leaves open
something it appears to decide. These are defects of the source, not objections to it. [observation]
items cite the probes in E11 and E12.

1. **Three artifacts, three lists of required fields.** “The `id` and `modified` fields are required. For
   schema versions above 1.0.0, the `schema_version` field is also required. All other fields are
   optional” (§ modified field / L721-L723, R-0025, R-0026, R-0027). `schema.json` `/required` lists only `id` and `modified`. The
   protobuf marks `summary`, `details` and `affected` “Required.” (`proto` `Vulnerability.summary`,
   `.details`, `.affected`) and `Affected.ranges` “Required. Range information.”, although the prose
   lets an entry use `versions` instead of `ranges` (§ affected fields / L931-L946, R-0067, R-0071), and the protobuf
   calls itself “*NOT* stable” (`proto` `Vulnerability`). [observation, E11 P07] A record with only `id`
   and `modified` validates.

2. **"Required above 1.0.0" cannot be checked.** L721-L722 (R-0026) sits beside “If no value is specified, it
   should be assumed to be `1.0.0`” (§ schema_version field / L128, R-0007): a record without the field is by
   definition 1.0.0, so it can never be found in breach, and `schema.json` `/properties/schema_version`
   accepts any string. [observation, E11 P07, P08] Absent and `"banana"` both validate. Two of the
   specification's own complete examples omit the field (Debian, L1764-L1800; R, L1944-L1994).

3. **1.9.2's `id` rules are not in the JSON Schema.** The 1.9.2 text requires `^[a-zA-Z0-9:_.-]+$`
   (§ Character set constraints / L154-L157, R-0012), but `schema.json` `/$defs/prefix/pattern` checks only the
   start of the id and has no end anchor, and [1.9.1] the schema file is byte-identical to v1.9.1's
   (E12). [observation, E11 P01, P03] `GHSA-foo bar/baz` and `x_CUSTOM!0001` validate, and so does `GHSA-`, a listed prefix and its `-`
   with no entry id (examples GAP-41, pass 3). In the other
   direction the pattern requires a `-` after every listed prefix (P02 fails), where the text says
   “followed (ideally) by a `-` separator” (§ Semantically neutral ids / L169, R-0018).

4. **A "must not" inside a "should".** “When establishing new identifier schemes, new IDs **should be
   semantically neutral**:” is followed by “IDs must not describe the vulnerability type or weakness”
   (§ Semantically neutral ids / L166-L168, R-0016, R-0017). Whether the bullet binds every id or only new schemes, and
   whether it is a requirement or part of the recommendation, is not said.

5. **The prefix table and the schema's prefix list differ.** The table's `CleanStart` (L277, R-0019) is
   `CLEANSTART` in `/$defs/prefix/pattern`, and the schema's `FreeBSD` has no row [observation: a script
   over L179-L710, 2026-10-18; E11 P05 fails, P06 passes]. The table asks “Please keep this list
   alphabetically sorted” (L177) but runs `ASB-A`, `ALSA`, `ALPINE` and ends `VCPKG`, `CLSA`. The
   CleanStart row's link has no text (L278), and the DRUPAL URL template has its angle brackets reversed
   (`&gt;module&lt;`, L338).

6. **`GIT` is an ecosystem in the schema, not in the prose.** `/$defs/ecosystemWithSuffix/pattern`
   accepts `GIT` (E11 P11). The prose table (L988-L1042, R-0081) and `/$defs/ecosystemName` list 52 names
   without it, and neither `/$defs/ecosystemName` nor `/$defs/ecosystemSuffix` is referenced anywhere in
   the schema [observation: no `$ref` to either]. The prose says both “This entry should use **no**
   `package` field.” (§ Separating Git and Strict Ecosystems / L1059, R-0148) and “For entries using `GIT`
   "ecosystem"” (§ Version Enumeration for Git Entries / L1065, R-0150), and calls it “the `GIT`
   pseudo-ecosystem” (§ affected[].versions field / L1081, R-0157). A Git-only entry can be written two ways, and
   a consumer must accept both.

7. **`IsVulnerable` does not define what it compares.** `if affected.package == pkg` (§ Evaluation /
   L1250, R-0201) leaves open whether `purl` takes part, whether `Debian` equals `Debian:12`, and how names
   compare (PyPI names are normalized, L1028, R-0126). It has no case for the wildcard `*` (L959-L962, R-0077) or for an
   entry without `package` (L1059, R-0148), and it never reads `withdrawn` (L745-L748, R-0029, R-0030), so a withdrawn record
   still evaluates as affected.

8. **`sorted(range.events)` has no order for ties, and no total order for `GIT`.** L1268 sorts with no
   tie rule, and keeping the stored array sorted is optional: “While not required, it's also recommended
   to keep the `events` array sorted according to the `affected[].ranges[].type` of the range.”
   (§ Requirements / L1182-L1184, R-0190). **[analysis]** For `[{"introduced": "1.0.0"}, {"last_affected":
   "1.0.0"}]` and v = 1.0.1, the loop (L1264-L1279, R-0201) returns not affected if `introduced` is visited first
   and affected otherwise. For `GIT`, “The relation `u < v` is true when commit `u` is a (perhaps
   distant) parent of commit `v`.” (L1124-L1125, R-0172) is a partial order, so `sorted` has no unique result
   across branches; the limit example is explained with `git rev-list` (L1369-L1370), not with the loop.

9. **A `limit` of `"*"` fails in `GIT` ranges, and `"0"` passes where it is not defined.** “`limit`
   allows versions containing the string `"*"`” (§ Special values / L1153, R-0178), and limits “are more useful
   for git ranges” (§ Limit events / L1338), but the schema's “GIT ranges must use full-length commit
   hashes” rule (`/properties/affected/items/properties/ranges/items/allOf/1`) applies
   `^(0|[a-f0-9]{40}|[a-f0-9]{64})$` to all four event kinds. [observation, E11 P15, P16, P17]
   `{"limit": "*"}` fails in a `GIT` range and passes in a `SEMVER` one; `{"fixed": "0"}` passes in a
   `GIT` range although `"0"` is defined only for `introduced` (L1151-L1152, R-0177). "Containing" (L1153, R-0178) is not
   "equal to", and `BeforeLimits` compares `v < evt.limit` with no case for `"*"` (L1287, R-0201). More
   generally the schema checks no version syntax: `SEMVER` events `"v1"` and `"banana"` validate (P22),
   against “with no leading "v" prefix” (L1099, R-0164).

10. **Is `versions` required with `GIT` ranges?** “Specifying one or more `GIT` ranges does NOT remove
    the requirement to specify an explicitly enumerated `versions` list” (§ affected[].ranges[].type field
    / L1127-L1128, R-0173) refers to a requirement that the text states only as a recommendation (“The `versions`
    list is generally recommended to always be present”, § affected fields / L937, R-0069) or as a "must" for
    products whose versions cannot be ranges (L945-L946, R-0071); the schema requires neither, and OSV.dev may
    fill the list itself (L1065). A mixed entry's `versions` holds Git tags and ecosystem versions side by
    side (“versions from both the Git repository and the strict ecosystem will appear in the `versions`
    array”, L1065, R-0151), compared by plain string equality (L1259, R-0201).

11. **Severity: the schema accepts what is not a CVSS vector, and narrows `source`.** The `CVSS_V2` and
    `CVSS_V3` patterns (`/$defs/severity/items/allOf/0` and `/allOf/1`) accept any subset and any
    repetition of metrics; only the `CVSS_V4` pattern (`/allOf/2`) fixes order and completeness.
    [observation, E11 P28, P29, P30] `CVSS:3.1/AV:N`, a 3.1 vector with `AV` twice, and `AV:N` for
    version 2 all validate. The prose calls `source` “an optional string indicating the origin of the
    severity assessment” (§ severity[].source field / L876-L877, R-0058); the schema makes it a closed list (P31).
    A record-level `"severity": null` blocks package-level severity (P26), although L1072-L1073 (R-0154) forbids
    only a top-level value that is set. By L851 a `null` severity is not a JSON array in the first place
    (R-0050), the reading of examples GAP-39 and, since pass 3, EDGE-05.

12. **The `GIT` reference type is undefined.** `schema.json`
    `/properties/references/items/properties/type/enum` and `proto` `Reference.Type` (`GIT = 11`) include
    `GIT`; the prose's “The known reference `type` values are:” (§ references field / L1434, R-0209) does not list
    it (E11 P24). The `FIX` and `INTRODUCED` entries then speak of “the `fix` type” and “the `introduced`
    type” in lower case (L1445, R-0210; L1449, R-0211).

13. **`related` means different things in the prose and the protobuf.** Prose: “A similar but completely
    different vulnerability.” and “Cases that do not satisfy the strict definition of `aliases` or
    `upstream`.” (§ related field / L809-L810, R-0041). Protobuf: “Optional. List of IDs of closely related
    vulnerabilities, such as the same problem in alternate ecosystems.” (`proto` `Vulnerability.related`).
    By the prose, "the same problem in another ecosystem" is an alias if it affects components the same
    way (L763-L766, R-0033), or an upstream link (L771-L778, R-0035 to R-0037).

14. **Alias semantics: a claim, a vague test, and a closure without a conflict rule.** The test is “Two
    vulnerabilities can be described as aliases if they affect any given software component the same way:
    either both vulnerabilities affect the software component or neither do. A subsequent patch addresses
    both of the vulnerabilities (and no others), and vice versa.” (§ aliases field / L763-L766, R-0033), where
    "and vice versa" has no clear referent. Closure is a "should" (L768-L769, R-0034) over claims that single
    databases make (L759-L761), and nothing says what a consumer does when A lists B but B does not list
    A. The Rust example's two CVE aliases (L1676) become aliases of each other under that closure.

15. **Two different example records share an `id` and a `modified`.** The Hackage and GHC examples both
    carry `"id": "HSEC-2023-0006"` and `"modified": "2023-07-26T10:34:39Z"` (L1875-L1876, L1923-L1924)
    with different `affected` content, and the GHC one keeps the Hackage `details` about
    `x509-validation` (L1922). By L717-L719 neither is authoritative. [observation, E11] Both validate.

16. **Examples that are not JSON, or that contradict the guidance.** Range fragments and the credits
    example carry trailing commas at L1302, L1315, L1350, L1364, L1392, L1408 and L1522 [observation:
    `json.loads`, 2026-10-18]. The `last_affected` against `fixed` comparison uses `ECOSYSTEM` for one
    side and `SEMVER` for the other (L1389, L1405). The Python example puts a `GIT` range and an
    `ECOSYSTEM` range in one `PyPI` entry (L1730-L1746), which § Separating Git and Strict Ecosystems
    recommends against (L1056, R-0145). None of the nine complete examples gives a `purl`, which L967
    recommends (R-0079; examples source issue S-15, pass 3).

17. **Ecosystem rules the schema does not check, and suffixes without a grammar.** Alpine, Mageia, Photon
    OS and Red Hat Lightwell require a suffix, Ubuntu a “mandatory `:LTS` suffix” for LTS releases, and
    vcpkg “has no release suffix” (L992, L1016, L1026, L1030, L1037, L1038; R-0085, R-0113, R-0124, R-0128, R-0137, R-0139); the schema's `(:.+)?`
    accepts each either way (E11 P12, P13). Suffixes are URLs, CPEs or colon-separated hierarchies
    (L1017, L1029, L1032, L1037; R-0114, R-0127, R-0131, R-0136), with no grammar. Only four rows state a version ordering (Echo,
    Homebrew, openSUSE, SUSE; L1005, L1012, L1023, L1034; R-0099, R-0108, R-0120, R-0133), and SwiftURL says its versions are SemVer tags
    (L1035, R-0134) [observation: text search]; for the rest, comparing `ECOSYSTEM` versions is outside the
    specification (L1110-L1117, R-0169, R-0170).

18. **Errors in ecosystem rows.** Red Hat: “with the `cpe/:[oa]:(redhat):` prefix removed” (L1029, R-0127),
    while the row's own example translates to a name beginning `cpe:/a:redhat:`; the stated prefix starts
    `cpe/:`, not `cpe:/`. FreeBSD: “The `ranges[].events` versions correspond to specific FreeBSD
    releases, such as 'FreeBSD:base:14.3'.” (L1006, R-0102) offers an ecosystem string as an event version, and
    the same row ends “a particular FreeBSD release like.” (L1006, R-0102). openEuler's suffix is written
    `<RELEASE>` with no colon (L1022, R-0119). Debian has “use the the string” (L1003, R-0097), SwiftURL “comform” (L1035, R-0134).

19. **The `purl` rules are prose only, and the purl specification is not pinned.** The purl “identifies
    the package, without the `@version` component” (L966, R-0078), but the schema types `purl` as any string
    (E11 P37, P38), and Canonical's own records carry versions (E2). The link names the purl-spec
    repository (L965, R-0078), not an edition (ECMA-427, or a purl-spec tag), so which type rules apply is open.

20. **Forward compatibility against `additionalProperties: false`, and an unversioned schema.** L129-L132
    tells clients to ignore unexpected fields; `schema.json` `/additionalProperties` is `false`, at the top
    level only (E11: P09 fails; nested unknown keys pass, P10, P19). The schema's `$id` is
    `https://raw.githubusercontent.com/ossf/osv-schema/main/validation/schema.json` (`/$id`) and the prose
    links to `blob/main` (§ Format Overview / L43-L44): both name a branch. The schema carries no version
    of its own, and [1.9.1] the same bytes serve 1.9.1 and 1.9.2 (E12).

21. **Timestamps and nulls.** `/$defs/timestamp/pattern` has no `^` or `$`, so text around a valid
    timestamp passes unless the validator asserts `format` (E11 P32: valid by default, invalid with
    jsonschema's format checker). `aliases`, `affected`, `references` and both `severity` arrays accept
    `null` (`"type": ["array", "null"]`), while `related`, `upstream` and `credits` do not (P34, P35); the
    prose never mentions `null`.

22. **Misplaced and garbled text.** Under § affected[].ranges[].repo field, “The range object defines the
    fields `type`, `events`, `repo`.  `introduced`, `fixed`, and additional type-specific fields as
    needed.” (L1195-L1196, R-0193) lists event fields as range fields. `REPORTER`: “notified the vendor of the
    vulnerability to a CNA.” (L1497, R-0220). The deprecated `Commit` message: “If this is referring to a commit
    which fixes a vulnerability, then *all* commits in the range is assumed to cause the vulnerability.”
    (`proto` `Commit`). Also: “using a version on the” (L865, R-0055); the `Ubuntu` severity row has no closing
    `|` (L866, R-0056); the pseudocode is fenced as `python` (L1247) but written in a Go-like syntax;
    `ranges[].database_specific` appears in the overview (L83) but not in the § affected fields block
    (L903-L912); and [1.9.1] the heading 1.9.2 adds, “### modified field” (L714), now holds the
    record-wide statement of required fields (L721-L724, R-0025 to R-0027).

---

## Evidence from tmodel's research and this extraction's probes

E1 to E10 come from tmodel's own research (RPT-0004 Phase 1, run 2026-10-08, and RPT-0005), cited by file
and section; E11 to E13 are probes run for this extraction on 2026-10-18 and are marked as such. They
describe tools and data, not the OSV text.

- **E1. OSV.dev rewrites the records it aggregates.** In OSV.dev's exports “every or nearly every
  `affected[].package` carries a purl and none carries a version” (for example Alpine 44,287 of 44,287,
  Debian 188,840 of 188,843, Red Hat 631,373 of 631,373), and GHSA-jfh8-c2jp-5v3q as served by OSV.dev
  has a purl and `schema_version` 1.9.0 while GitHub's own file has no purl and `schema_version` 1.4.0
  (`fanout-bridge.md` §1.4). OSV.dev's copy of GHSA-cpwx-vrp4-4pq7 also lowercases the package name to
  `jinja2` (`fanout-identity.md` §10, notes from agent 3). Bears on Adapt-1 and Adapt-7.
- **E2. Copies of one record disagree on the purl.** Canonical's UBUNTU-CVE-2025-60876 has
  `pkg:deb/ubuntu/busybox@1:1.21.0-1ubuntu1.4+esm1?arch=source&distro=esm-infra-legacy/trusty`, while
  OSV.dev serves `pkg:deb/ubuntu/busybox?arch=source&distro=esm-infra-legacy%2Ftrusty`
  (`fanout-identity.md` §9). Canonical's spelling breaks L966's “without the `@version` component”, which
  the schema does not check (defect 19). Bears on Adapt-1 and Adapt-7.
- **E3. The purl's spelling changes OSV.dev's answer.** One Debian package version gave 52, 0 or 82
  advisories depending on how, or whether, the purl spelled the release; every `pkg:apk/alpine/busybox`
  form gave 0 while the ecosystem query `Alpine:v3.18` gave 5; and OSV.dev's purl parser maps Alpine
  purls to the bare `Alpine` ecosystem, with no release (`fanout-identity.md` §1.22). Bears on Adapt-1,
  Adapt-3 and Reject-5.
- **E4. The query API's version match is fuzzy.** OSV.dev's API documentation: “A fuzzy match is done
  against upstream versions.” (`fanout-bridge.md` §1.4, quoting `post-v1-query.md`). Bears on Reject-5.
- **E5. Only GHSA records carry CWEs.** In the exports, `database_specific.cwe_ids` “appears only on GHSA
  records” (Maven 7,185, PyPI 6,526, Go 4,906, crates.io 1,601), and ALPINE, DEBIAN, DSA, DLA, RHSA,
  PYSEC, GO and RUSTSEC records have none (`fanout-bridge.md` §1.4). Bears on Adapt-8.
- **E6. Ubuntu's conventions.** Ubuntu's records name source packages and list binaries in
  `ecosystem_specific.binaries`; their `ECOSYSTEM` ranges always start at `"0"`; the triage states
  `needs-triage`, `needed`, `ignored`, `pending`, `deferred` and `in-progress` are each “Listed under
  affected and fixed is not set”, while `DNE` and `not-affected` packages are left out alike; and a zlib
  CVE also lists source packages that carry their own copy of zlib (`klibc`, `rsync`, `zsync`)
  (`fanout-bridge.md` §1.8). Bears on Adapt-2, Reject-2 and open question 3.
- **E7. Red Hat keeps the epoch and the product stream.** RHBA-2007:0026 has the ecosystem
  `Red Hat:enterprise_linux:3::as` and a `fixed` version of `2:3.1.6-7.el3` (`fanout-bridge.md` §1.9).
  Bears on Adopt-3 and Adapt-3.
- **E8. Withdrawal without a successor.** GHSA-9xgp-hfw7-73rq “has `withdrawn` equal to `published` and
  `modified`, and keeps its `affected[]`” (`fanout-vuln-data.md` §1.1). Bears on Adapt-6.
- **E9. Mixed schema versions.** “Records in the wild declare `schema_version` 1.4.0 and 1.9.0.”
  (`fanout-vuln-data.md` §1.1); Ubuntu's declare 1.7.0 (`fanout-bridge.md` §1.8). Bears on Adopt-7.
- **E10. Consumers record little, and some recompute.** OSV-Scanner: “The match is implied, not
  recorded.” (`fanout-bridge.md` §1.14). Dependency-Track 5.2.0 converts OSV ranges to `vers` strings with
  `versFromOsvRange` (`fanout-identity.md` §9). Bears on Adopt-3 (R-RANGE-1 keeps the range as written)
  and Adopt-4.
- **E11. Probe for this extraction: the pinned JSON Schema** (jsonschema 4.26.0, Draft 2020-12 validator,
  run 2026-10-18; the script and inputs stayed in the extraction scratchpad and are not committed). Each
  input is a minimal record (`schema_version`, `id`, `modified`) with one change.

  | probe | change | what the 1.9.2 text says | result |
  |---|---|---|---|
  | P01 | `"id": "GHSA-foo bar/baz"` | `^[a-zA-Z0-9:_.-]+$` (L154-L157, R-0012) | valid |
  | P02 | `"id": "GHSAfoo"` | a `-` separator "ideally" (L169, R-0018) | invalid |
  | P03 | `"id": "x_CUSTOM!0001"` | `^[a-zA-Z0-9:_.-]+$` (L154-L157, R-0012) | valid |
  | P04 | `"id": "NEWDB-1"` | new databases by pull request (L706-L707) | invalid |
  | P05 | `"id": "CleanStart-2026-1"` | the table's prefix `CleanStart` (L277, R-0019) | invalid |
  | P06 | `"id": "FreeBSD-2026-1"` | no table row | valid |
  | P07 | `schema_version` removed | required above 1.0.0 (L721-L722, R-0026) | valid |
  | P08 | `"schema_version": "banana"` | SemVer 2.0.0 (L126-L128, R-0006) | valid |
  | P09 | an unknown top-level field | ignore unexpected fields (L129-L132, R-0008) | invalid |
  | P10 | an unknown field in an `affected[]` entry | the same | valid |
  | P11 | `"ecosystem": "GIT"` | not a defined ecosystem (L988-L1042, R-0081) | valid |
  | P12 | `"ecosystem": "Alpine"` | must have a `:v<RELEASE-NUMBER>` suffix (L992, R-0085) | valid |
  | P13 | `"ecosystem": "vcpkg:2026"` | no release suffix (L1038, R-0139) | valid |
  | P14 | an `affected[]` entry with no `package` | a Git entry has no `package` (L1059, R-0148) | valid |
  | P15 | a `GIT` range with `{"limit": "*"}` | `limit` may be `"*"` (L1153, R-0178) | invalid |
  | P16 | a `GIT` range with `{"fixed": "0"}` | `"0"` is defined for `introduced` (L1151, R-0177) | valid |
  | P17 | a `SEMVER` range with `{"limit": "*"}` | `limit` may be `"*"` (L1153, R-0178) | valid |
  | P18 | `{"introduced": "1.0.0", "fixed": "1.0.2"}` | one type per event (L1159-L1161, R-0181) | invalid |
  | P19 | an event with an extra unknown key | not addressed | valid |
  | P20 | `fixed` and `last_affected` in one range | not both (L1163-L1164, R-0182) | invalid |
  | P21 | `fixed` and `last_affected` in two ranges of one entry | not addressed | valid |
  | P22 | `SEMVER` events `"v1"` and `"banana"` | SemVer, no leading "v" (L1098-L1099, R-0164) | valid |
  | P23 | a range with no `introduced` | at least one `introduced` (L1182, R-0189) | invalid |
  | P24 | `references[].type` `GIT` | not a known type (L1434-L1455, R-0209) | valid |
  | P25 | `references[].url` `"not a uri"` | a fully-qualified URL (L1429, R-0207) | valid; invalid with a format checker |
  | P26 | `"severity": null` plus package-level severity | the top level must not be set (L1072-L1073, R-0154) | invalid |
  | P27 | record-level and package-level severity together | the top level must not be set (L1072-L1073, R-0154) | invalid |
  | P28 | `CVSS:3.1/AV:N` | a CVSS vector string (L864, R-0054) | valid |
  | P29 | a CVSS 3.1 vector with `AV` twice | a CVSS vector string (L864, R-0054) | valid |
  | P30 | `CVSS_V2` score `AV:N` | a CVSS vector string (L863, R-0053) | valid |
  | P31 | `severity[].source` `GHSA` | an optional string (L876, R-0058) | invalid |
  | P32 | `modified` with text around a valid timestamp | RFC3339 in UTC (L716-L717, R-0022) | valid; invalid with a format checker |
  | P33 | `modified` ending `+00:00` instead of `Z` | UTC, ending in "Z" (L716-L717, R-0022) | invalid |
  | P34 | `"aliases": null` | not mentioned | valid |
  | P35 | `"related": null` | not mentioned | invalid |
  | P36 | `credits[].contact` `"call me"` | a URL (L1487, R-0217) | valid |
  | P37 | purl `pkg:npm/a@1.0.0` | without `@version` (L966, R-0078) | valid |
  | P38 | purl `hello` | follows the Package URL specification (L964-L965, R-0078) | valid |
  | P39 | `"name": "*"` | the wildcard (L959, R-0077) | valid |
  | P40 | `"ecosystem": "Ubuntu:Pro:18.04:LTS"` | a defined Ubuntu form (L1037, R-0138) | valid |

  All nine complete example records validate, from `GHSA-r9p9-mrjm-926w` (L1554-L1628) to `RSEC-2023-2`
  (L1944-L1994), including the two that share `HSEC-2023-0006` (defect 15). The informal schema blocks
  are not JSON by design (L39).
- **E12. Probe for this extraction: 1.9.1 against 1.9.2.** `docs/schema.md` at tag `v1.9.1`, fetched
  2026-10-18, has SHA-256 `e5b87d6258f133f2fb146661b4d7ee7d6c1ffb15f7b752d49b1b790ea683307e`, the value
  RPT-0004 (`fanout-bridge.md` §1.4) and RPT-0005 recorded. It differs from 1.9.2 only in the version
  line, two added sections (§ Character set constraints, § Semantically neutral ids) and two added
  headings (§ Defined database prefixes, § modified field). `validation/schema.json` has the same
  SHA-256 at both tags (`15b10dbb…2653`, the value both reports recorded for 1.9.1). So every 1.9.1
  quotation in RPT-0004 and RPT-0005 is still verbatim in 1.9.2, and no schema change came with 1.9.2's
  new rules.
- **E13. Probe for this extraction: release facts** (GitHub REST API, unauthenticated, 2026-10-18).
  Release `v1.9.2` was published 2026-10-13T23:37:11Z, and its tag points at commit
  `c8a57bdc5b0bc54646e140cabbb7834bd0b5aec9`, the commit this record pins. The repository licence is
  Apache-2.0, and `bindings/go` at the tag holds the `osvschema` and `osvconstants` packages.

**What the evidence says about OSV 1.9.2.** **[analysis]** Every divergence above sits where OSV leaves a
choice to someone else: to each database (copies, E1 and E2; conventions, E5 to E8), to OSV.dev's
tooling (purl mapping and fuzzy matching, E3 and E4), to each ecosystem (version order, defect 17), or
to a schema that checks less than the text (E11). None is fixed by choosing a better client; each needs
a rule of tmodel's own, which is what the adapt section proposes.

---

## Open questions

Routed to who should answer: the **sponsor** (decision maker for DEC-*), an issue (#15 core objects, #17
schema, #60 library loader, #61 CWE import), the **RPT-0004 author** (owner of the report and of this
record's topic), or the **OSV maintainers** (`ossf/osv-schema`).

1. **Vulnerability identity for OSV records.** One node per record, linked by alias Assertions
   (Adapt-4), or Table 6d's one node per CVE id with GHSA, OSV and distribution ids lost? If neither is
   acceptable, Vulnerability needs a multivalued identifier, a change to an accepted class that only an
   ADR superseding or refining ADR-0010 can make. *#15, then the sponsor.*
2. **Which route does OSV data take into tmodel?** Directly, as an importer under ADR-0007 (a `MAP-NNNN`
   crosswalk plus a vector), or only through radar's scanner output under ADR-0001's contract, as
   `mapping.md` finding 8 asks for SBOM and scanner formats? If directly, which lane builds it; #60
   (library loader, `engine/load/`) is the nearest `mapping.md` names. *#15 and #17; #60; the sponsor for
   DEC-002's import list.*
3. **Predicate names and values.** The match (R-MATCH-1 says “a predicate such as `affects` (name
   open)”), `aliases`, `upstream`, `related`, the retracted `assertion_status` for withdrawn records, and
   the `confidence` of a match from a record that lists untriaged packages as affected (E6). *#15.*
4. **Which copy, which channel, which snapshot?** Home database files, OSV.dev exports or the query API;
   how exports are pinned (URL, date, SHA-256) and refreshed; and whether OSV.dev's enrichments (added
   purls, expanded `versions`) count as OSV.dev's own claims (Adapt-7, Reject-5). *DEC-008, the sponsor.*
5. **Version comparators.** For which ecosystems does tmodel evaluate `ECOSYSTEM` ranges at MVP (apk,
   dpkg, rpm, PEP 440, npm's semver), with which libraries, recorded how; and is the `versions` list
   alone acceptable elsewhere (Adopt-3, Adapt-5)? R-RANGE-1's wording may need Adopt-3's OSV parts. *#17
   and DEC-009; the RPT-0004 author for R-RANGE-1.*
6. **The source-to-binary bridge.** Which signal establishes "built from" between a distribution's
   source package and the binaries an SBOM lists (the purl `upstream=` qualifier, Syft's
   `originPackage`, `ecosystem_specific.binaries`), and does a match on the source Component reach the
   binaries automatically or through Review (Adapt-2)? *#15 and #17 (Table 6b's Upstream row); DEC-009.*
7. **CWEs for vulnerabilities known only through OSV.** Read GHSA's `database_specific.cwe_ids` in the
   CWE importer, or take CWEs only through CVE aliases from CVE and NVD data (Adapt-8)? *#61; DEC-008.*
8. **Should RPT-0004 adopt OSV's split between aliases and upstream?** Phase 1's cell “key by CVE id;
   GHSA, OSV and distribution ids as aliases” (`fanout-bridge.md` §5) contradicts L775-L776 (R-0036), and Table
   6d's Vulnerability rule could name `upstream` for distribution ids. *The RPT-0004 author.*
9. **Should tmodel ever publish OSV records?** The `x_` prefix exists for “a local database that isn't
   aggregated by OSV.dev” (L148-L149, R-0011), so tmodel could export its own findings in OSV form. That adds a
   format to ADR-0007's committed export set, which needs a new ADR. Not recommended here, only recorded.
   *The sponsor (DEC-002).*
10. **This record's metadata.** `record.yaml` names only DEC-001 in `bears_on` (split on 2026-10-12; this
    note finds DEC-001a, DEC-002, DEC-003, DEC-008 and DEC-009), leaves `topic` empty, sets
    `maturity: best-practice` (an RFC 2026 level for an OpenSSF document; the summarize skill says to
    leave maturity unset rather than guess), rates cryptography `adjacent` although OSV carries no
    cryptographic mechanism, and has an empty `content.sha256` with the moving site as `content.url`. This
    pass changes none of them. *The RPT-0004 author (record owner).*
11. **`IsVulnerable`.** Will the evaluation section define package equality, the order of events at equal
    versions and for `GIT`, the wildcard, entries without `package`, and withdrawn records, or name an
    implementation as the reference (defects 7 and 8)? *OSV maintainers.*
12. **Schema and text agreement.** Will `validation/schema.json` gain 1.9.2's `id` rules and anchored
    `prefix` and `timestamp` patterns, a version in its `$id`, one spelling of `CleanStart`, a decision on
    `FreeBSD`, on `GIT` as an ecosystem and as a reference type, and on `limit: "*"` in `GIT` ranges
    (defects 3, 5, 6, 9, 12, 20 and 21)? *OSV maintainers.*
13. **Required fields.** Which fields are required, given that the prose, the schema and the protobuf
    disagree, and is `versions` required with `GIT` ranges (defects 1, 2 and 10)? Does “All other fields are optional”
    (L722-L723, R-0027) cover the members of nested objects, or only the top-level fields named before it?
    Read for every field it would contradict the required members of `package`, `ranges`, `severity`,
    `references` and `credits`; `requirements.yaml` and, since pass 3, `messages.yaml` read it for the top
    level. *OSV maintainers.*
14. **Examples and ecosystem rows.** The duplicated `HSEC-2023-0006` example, the fragments that are not
    JSON, the Red Hat CPE prefix and the FreeBSD row (defects 15, 16 and 18). *OSV maintainers.*
