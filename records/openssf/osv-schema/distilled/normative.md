---
record: osv-schema
kind: normative
title: "osv-schema: normative statements"
extracted: "2026-10-18"
extracted_by: "claude (FX-1 pass 1, normative agent)"
reviewed_by: ""
source_version: "OSV Schema 1.9.2 (October 13, 2026); github.com/ossf/osv-schema tag v1.9.2, commit c8a57bdc5b0bc54646e140cabbb7834bd0b5aec9"
source_digest: "96d82f03d763fb408bc344d01fc271f761a81cc225f6f6a42d318e3ed21cebff"   # SHA-256 of docs/schema.md (2010 lines)
source_digest_schema: "15b10dbb4c4e31c7aae11d22cdd991a9a374758db7c8389e62b3cc37cac92653"   # SHA-256 of validation/schema.json (584 lines)
source_digest_proto: "1c5a7af863c576398e333358c006d30577dd111c810416cd2f3fc0cecd20a070"   # SHA-256 of proto/vulnerability.proto (234 lines)
licence: "Apache-2.0"
attribution: "Contains text from the OSV Schema (github.com/ossf/osv-schema, tag v1.9.2), licensed under the Apache License, Version 2.0; see Licence at the end of this file"
statements: 384   # N-0001 to N-0384: 317 from docs/schema.md, 31 from validation/schema.json, 36 from proto/vulnerability.proto
---

<!-- FX-1 pass 1 (normative agent). Every normative statement of the OSV
     Schema v1.9.2, verbatim, with its locator, in source order under the
     source's own headings. Verbatim source text: every blockquote and every
     cell of the transcribed tables (the N, line, forms and req columns are
     extractor structure). JSON Schema values are re-serialised; see
     Conventions. Everything else is extractor text. -->

Source: OSV Schema, "Open Source Vulnerability format", version 1.9.2 (October 13,
2026), OpenSSF, github.com/ossf/osv-schema at tag v1.9.2 (commit
c8a57bdc5b0bc54646e140cabbb7834bd0b5aec9), Apache-2.0. Three files were read:

| file | role | lines | SHA-256 |
|---|---|---|---|
| docs/schema.md | the specification, published at https://ossf.github.io/osv-schema/ | 2010 | `96d82f03d763fb408bc344d01fc271f761a81cc225f6f6a42d318e3ed21cebff` |
| validation/schema.json | the JSON Schema the specification links "for validation" | 584 | `15b10dbb4c4e31c7aae11d22cdd991a9a374758db7c8389e62b3cc37cac92653` |
| proto/vulnerability.proto | the protobuf definition of the same structure | 234 | `1c5a7af863c576398e333358c006d30577dd111c810416cd2f3fc0cecd20a070` |

The repository's root schema.md says only "Moved to" the published page and holds
no statements. Unless a locator says "schema" or "proto", a line number is a
line of docs/schema.md.

## Conventions

**What is extracted.** 384 numbered statements, N-0001 to N-0384, in
three parts: 317 from the prose (docs/schema.md), in source order under its own
headings; 31 JSON Schema constraint statements in document order; 36 proto
statements, for the parts of the proto that add to or differ from the other two
(see the proto section). From the prose, every sentence that carries a verbal
form (below) and every sentence that constrains or defines a field, a value or
how data is read is extracted, together with every normative table row and
list item, every field block (the JSON snippet at the top of a field section),
the informal schema and the evaluation pseudocode. 75 passages are excluded,
each listed with its reason under Informative content excluded: front matter,
the Purpose section, examples, rationale, navigation pointers, descriptions of
osv.dev tooling, HTML comments, invitation rows, worked-example narrative and
the ten example records.

**Verbatim.** Quoted text is the source's characters: punctuation, quotation
marks (straight and curly), backticks, emphasis markers (`**`, `_`, `*`) and
Markdown link syntax are copied as they are, so a quote renders as the
published page does. The only normalisation is joining a sentence the source
wrapped across lines: a line break, with the spaces or tab around it, becomes
one space. Spaces inside a line are kept (the source has double spaces after
some full stops). Code, field blocks, lists that belong to a sentence, and the
proto are quoted line by line inside fences, tabs and indentation included.
Tables are transcribed one statement per row, each cell verbatim; the N, line,
forms and req columns are extractor structure. Quotes were cut from the source
by line and marker, never retyped, and after generation every blockquote and
every fenced quote line in this file was checked against the source files.
Short quotations inside notes and in the D and U lists are verbatim too; one
that runs over two proto comment lines is joined without the `//` marker.

**JSON Schema values** are re-serialised compactly from the parsed schema
(`json.dumps` with separators `, ` and `: `). Every string is
character-identical to the source with its JSON escaping kept (so `\\.` in a
pattern is one backslash and a dot); only whitespace between tokens differs.
They are fenced as `json` without a blockquote for that reason.

**Locators.** Prose: `§ <heading path> / L<line>` or `L<first>-<last>`. The
heading path is the source's own headings from level 2 down, joined with
` > `; the level-1 heading is named only where no level-2 heading is in force
(Purpose, Format Overview). JSON Schema: the JSON Pointer (RFC 6901) of the
keyword or `allOf` item and its line range in validation/schema.json. Proto:
`Message.field`, `Message.Enum` or `Message`, and its line range in
proto/vulnerability.proto.

**Kinds.** `sentence`; `list item` (a bullet's sentence, quoted without its
`- ` marker; `list item, sentence 2` for a later sentence of the same bullet,
`list item, paragraph 2` for a later paragraph of it);
`lead-in` (a sentence ending in a colon that introduces a list or table whose
items are numbered separately; it may carry a verbal form of its own);
`sentence and list`, `sentence and pattern`, `sentence and pseudocode` (a
sentence quoted with the block it introduces); `field block`; `informal
schema`; `table row`; for the JSON Schema the keyword or `allOf` item; for the
proto `field comment`, `enum`, `message`, `message comment`. A list is
numbered item by item where each item defines a value with its own description
(the reference types and the credit types); a list of bare names or of
examples stays in one statement with the sentence that introduces it (the
`related` list, the four event kinds, the SoC vendors).

**Verbal forms.** Each statement carries the forms found in its own quoted
text, in order, in backticks: must, must not, should, should not, may, may not,
can, cannot, might, shall, required, not required, require, recommended,
recommend, optional, optionally, only, allowed, not allowed, permitted,
invalid, encouraged, preferred, preferable, mandatory. Matching is
case-insensitive on whole words. "must not", "should not", "may not", "not
required" and "not allowed" are counted once, as that form, also when Markdown
emphasis sits between the words (`should **not**`), and never also as the
shorter form. `imperative` is added by hand where a sentence instructs without
a verbal form ("Do not encode", "Use", "use the"). `[none]` means no form. A
table row or list item counts the forms in all its cells; its sentences are not
numbered separately, so every occurrence belongs to exactly one statement or
one exclusion. The source writes its rules in lowercase and has no uppercase
BCP 14 keyword; this file does not decide which forms bind. Notes marked
**(inferred)** are extractor readings, not source text; they flag "may", "can"
and "might" that state a possibility rather than a permission, and "should"
that defines how data is read.

**req.** Every statement has a `req:` field (a column in tables), filled in
pass 3 (cross-check). It holds the `requirements.yaml` entries (cite as
`osv-schema#R-NNNN`) whose `text` is this statement or contains it, or, for a
JSON Schema statement, whose locator or `also_at` names this keyword (and the
prose entry that states the same rule). `(item)` marks a table row or list
item that is one item of that entry's `enumeration` (the prefix, ecosystem,
severity type, reference type and credit type lists). `none:` gives the
reason a statement has no entry. Proto statements have none, because
`requirements.yaml` does not extract the proto (its `source_files` entry), and
name the prose entry they agree with, add to or differ from.

**Structure, not statements.** Headings (reproduced as this file's headings,
one level lower), code-fence lines, list markers, blank lines, the HTML table
markup and header row (L179-187, L709-710) and the Markdown table header rows
(L861-862, L882-883, L988-989).

**Cross-references.** D-n: disagreements between the prose, the JSON Schema and
the proto. U-n: inconsistencies or unclear points in the prose. X-nnn:
exclusions.

## Purpose

No statements in this section (L17 to L36); its content is listed under Informative content excluded.

## Format Overview

**N-0001.** § Format Overview / L39 · sentence · `[none]` · req: R-0001

> The format is a JSON-based encoding format, using the following informal schema.

**N-0002.** § Format Overview / L40 · sentence · `[none]` · req: none: pointer (quoted in the notes of R-0001)

> The exact details of each field are elaborated in the next section.

Note (inferred): makes the informal schema that follows (N-0005) subordinate to the Field Details section; where they differ, Field Details governs. See D-21.

**N-0003.** § Format Overview / L40-41 · sentence · `[none]` · req: R-0002

> All strings contain UTF-8 text.

**N-0004.** § Format Overview / L43-44 · sentence · `[none]` · req: none: pointer to the JSON Schema (named in the notes of R-0001)

> A JSON Schema for validation is also available [here](https://github.com/ossf/osv-schema/blob/main/validation/schema.json).

Note: the only prose statement tying the JSON Schema to the format. The link names the `main` branch, not the v1.9.2 tag (U-27).

**N-0005.** § Format Overview / L47-99 · informal schema · `[none]` · req: none: informal schema that R-0001 introduces; field types are carried in messages.yaml

> ```json
> {
> 	"schema_version": string,
> 	"id": string,
> 	"modified": string,
> 	"published": string,
> 	"withdrawn": string,
> 	"aliases": [ string ],
> 	"upstream": [ string ],
> 	"related": [ string ],
> 	"summary": string,
> 	"details": string,
> 	"severity": [ {
> 		"type": string,
> 		"score": string,
> 		"source": string
> 	} ],
> 	"affected": [ {
> 		"package": {
> 			"ecosystem": string,
> 			"name": string,
> 			"purl": string
> 		},
> 		"severity": [ {
> 			"type": string,
> 			"score": string,
> 			"source": string
> 		} ],
> 		"ranges": [ {
> 			"type": string,
> 			"repo": string,
> 			"events": [ {
> 				"introduced": string,
> 				"fixed": string,
> 				"last_affected": string,
> 				"limit": string
> 			} ],
> 			"database_specific": { see description }
> 		} ],
> 		"versions": [ string ],
> 		"ecosystem_specific": { see description },
> 		"database_specific": { see description }
> 	} ],
> 	"references": [ {
> 		"type": string,
> 		"url": string
> 	} ],
> 	"credits": [ {
> 		"name": string,
> 		"contact": [ string ],
> 		"type": string
> 	} ],
> 	"database_specific": { see description }
> }
> ```

Note: tab-indented in the source; copied byte for byte. Field types are written as bare `string`, and three objects as `{ see description }`, so this block is not itself valid JSON.

**N-0006.** § Format Overview / L102-103 · sentence · `[only]` · req: R-0003

> Again, this document is only about the JSON encoding the database serves to consumers, which could be applications or other databases.

Note (inferred): "only" limits what the document governs (the served JSON encoding), not what a party may do.

**N-0007.** § Format Overview / L103-105 · sentence · `[might, might]` · req: R-0003

> A database might store its entries in an entirely different format, or it might store them using this schema but in a more human-editable encoding, such as TOML or YAML.

Note (inferred): "might" grants freedom for storage formats, which the format does not govern.

**N-0008.** § Format Overview / L105-107 · sentence · `[only, allowed]` · req: R-0004

> For serving, only the JSON encoding format is allowed, not a transliteration into any other encoding.

**N-0009.** § Format Overview / L109-111 · sentence · `[only, must]` · req: none: design rationale; its must is excluded (keyword_accounting, L110)

> Overall, the approach of this schema is to define only the fields that absolutely must be shared between databases, leaving customizations to the "ecosystem_specific" and "database_specific" blocks (see below)

Note (inferred): "must" here describes which fields the schema chose to define; it binds no party. The rule it implies, that custom data goes in the two `*_specific` objects, is enforced at the top level only by the JSON Schema's `additionalProperties: false` (N-0348). The source sentence has no final full stop.

## Field Details

### schema_version field

**N-0010.** § schema_version field / L118-120 · field block · `[none]` · req: none: field block; the types are carried in messages.yaml

> ```json
> {
> 	"schema_version": string
> }
> ```

**N-0011.** § schema_version field / L123-124 · sentence · `[none]` · req: R-0005

> The `schema_version` field is used to indicate which version of the OSV schema a particular vulnerability was exported with.

**N-0012.** § schema_version field / L126-128 · sentence · `[should]` · req: R-0006

> The value should be a string matching the OSV Schema version, which follows the [SemVer 2.0.0](https://semver.org) format, with no leading "v" prefix.

Note: not checked by the JSON Schema (`/properties/schema_version` has only `type: string`).

**N-0013.** § schema_version field / L128-129 · sentence · `[should]` · req: R-0007

> If no value is specified, it should be assumed to be `1.0.0`, matching version 1.0 of the OSV Schema.

Note (inferred): "should" here states how a consumer interprets an absent value.

**N-0014.** § schema_version field / L129-132 · sentence · `[can, only, can]` · req: R-0008

> Clients can assume that new minor and patch versions of the schema only add new fields, without changing the meaning of old fields, so that a client that knows how to read version 1.2.0 can process data identifying as schema version 1.3.0 by ignoring any unexpected fields.

Note: a consumer rule (ignore unexpected fields). The JSON Schema rejects unexpected top-level fields (`additionalProperties: false`, N-0348); see D-14.

### id, modified fields

**N-0015.** § id, modified fields / L137-140 · field block · `[none]` · req: none: field block; the types are carried in messages.yaml

> ```json
> {
> 	"id": string,
> 	"modified": string
> }
> ```

**N-0016.** § id, modified fields / L143 · sentence · `[none]` · req: R-0009

> The `id` field is a unique identifier for the vulnerability entry.

**N-0017.** § id, modified fields / L143-145 · sentence · `[none]` · req: R-0010

> It is a string of the format `<DB>-<ENTRYID>`, where `DB` names the database and `ENTRYID` is in the format used by the database.

Note: compare N-0025 ("followed (ideally) by a `-` separator") and the JSON Schema prefix pattern (N-0338), which makes the `-` mandatory; see D-2 and U-25.

**N-0018.** § id, modified fields / L148-149 · sentence · `[can]` · req: R-0011

> The `x_` prefix can be used to denote a local database that isn't aggregated by OSV.dev, allowing external records to be schema-compliant.

#### Character set constraints

**N-0019.** § id, modified fields > Character set constraints / L154-157 · sentence and pattern · `[must]` · req: R-0012

> To ensure maximum compatibility with CLI tools, shell scripts, URL routing, and filesystem storage, the `id` field must strictly use ASCII characters matching the regular expression:
>
> ```text
> ^[a-zA-Z0-9:_.-]+$
> ```

Note: the JSON Schema does not apply this expression; `/properties/id` refers only to the prefix pattern (N-0338), which has no end anchor. See D-2.

**N-0020.** § id, modified fields > Character set constraints / L160 · sentence · `[only, permitted]` · req: R-0013

> Only alphanumeric characters (`a-z`, `A-Z`, `0-9`) and `:`, `-`, `_`, and `.` are permitted.

**N-0021.** § id, modified fields > Character set constraints / L160 · sentence · `[not allowed]` · req: R-0014

> Characters outside this set (such as spaces, slashes `/`, backslashes `\`, parentheses, or exclamation marks) are not allowed.

#### Semantically neutral ids

**N-0022.** § id, modified fields > Semantically neutral ids / L164 · sentence · `[should]` · req: R-0015

> Identifiers should function solely as unique, permanent pointers to a vulnerability record rather than human-readable summaries.

**N-0023.** § id, modified fields > Semantically neutral ids / L166 · lead-in · `[should]` · req: R-0016

> When establishing new identifier schemes, new IDs **should be semantically neutral**:

Note: introduces the two bullets N-0024 and N-0025; scoped to new identifier schemes.

**N-0024.** § id, modified fields > Semantically neutral ids / L168 · list item · `[imperative, must not]` · req: R-0017

> **Do not encode mutable vulnerability metadata:** IDs must not describe the vulnerability type or weakness (e.g. `SQLI`, `RCE`), package or component name (e.g. `LOG4J`), or severity rating (e.g. `CRITICAL`, `HIGH`).

**N-0025.** § id, modified fields > Semantically neutral ids / L169 · list item · `[imperative, should]` · req: R-0018

> **Use scoped prefixes:** IDs should always begin with the correctly scoped database prefix from the defined database prefixes below (or `x_` for local databases), followed (ideally) by a `-` separator (e.g., `OSV-2026-X7Y2`, `GHSA-vp9c-fpxx-744v`).

Note: "(ideally)" makes the `-` separator a preference; the JSON Schema prefix pattern requires it (D-2).

#### Defined database prefixes

**N-0026.** § id, modified fields > Defined database prefixes / L174 · lead-in · `[none]` · req: R-0019

> The defined database prefixes and their "home" databases are:

Defined database prefixes: the 47 prefix rows of the HTML table (L188 to L704), one statement per row. Each cell is the verbatim inner HTML of the source cell (the Prefix and Database `<td>` elements and the three `<li>` items of the Description cell), so links and code render as they do on the published page; the item labels "How to contribute:", "Source URL:" and "OSV Formatted URL:" are moved to the column headings. The Description items are informative contact and location data; they are kept because each row is transcribed whole.

| N | lines | Prefix | Database | How to contribute | Source URL | OSV Formatted URL | forms | req |
|---|---|---|---|---|---|---|---|---|
| N-0027 | L188-198 | <code>ASB-A</code>/<code>PUB-A</code> | <a href="https://source.android.com/docs/security/bulletin">Android Security Bulletin</a> | <a href="https://bughunters.google.com/about/rules/android-friends/6171833274204160/android-and-google-devices-security-reward-program-rules">Android Vulnerability Rewards Program</a> | <a href="https://storage.googleapis.com/android-osv/index.html"><code>https://storage.googleapis.com/android-osv/&lt;ID&gt;.json</code></a> | <code>https://storage.googleapis.com/android-osv/&lt;ID&gt;.json</code> | `[none]` | R-0019 (item) |
| N-0028 | L199-209 | <code>ALSA</code>/<code>ALBA</code>/<code>ALEA</code> | <a href="https://errata.almalinux.org/">AlmaLinux Security Advisory</a> | TBD | <code>https://errata.almalinux.org/&lt;alma version&gt;/&lt;ID&gt;.html</code> | <code>N/A</code> | `[none]` | R-0019 (item) |
| N-0029 | L210-220 | <code>ALPINE</code> | <a href="https://secdb.alpinelinux.org/">Alpine (provided by OSV.dev)</a> | TBD | <code>https://security.alpinelinux.org/vuln/&lt;ID&gt;</code> | <code>https://api.osv.dev/v1/vulns/ALPINE-&lt;ID&gt;</code> | `[none]` | R-0019 (item) |
| N-0030 | L221-231 | <code>AZL</code> | <a href="https://github.com/microsoft/AzureLinuxVulnerabilityData">Azure Linux Security Advisory</a> | TBD | <code>https://github.com/microsoft/AzureLinuxVulnerabilityData</code> | <code>TBD</code> | `[none]` | R-0019 (item) |
| N-0031 | L232-242 | <code>BELL</code> | <a href="https://docs.bell-sw.com/security/search/">BellSoft Security Advisory</a> | TBD | <code>https://bell-sw.com/vulnerability-report/</code> | <code>N/A</code> | `[none]` | R-0019 (item) |
| N-0032 | L243-253 | <code>BIT</code> | <a href="https://github.com/bitnami/vulndb">Bitnami Vulnerability Database</a> | <a href="https://github.com/bitnami/vulndb/blob/main/CONTRIBUTING.md">https://github.com/bitnami/vulndb/blob/main/CONTRIBUTING.md</a> | <code>https://github.com/bitnami/vulndb/blob/main/data/&lt;component&gt;/&lt;ID&gt;.json</code> | <code>N/A</code> | `[none]` | R-0019 (item) |
| N-0033 | L254-264 | <code>BREW</code> | <a href="https://github.com/Homebrew/advisory-database">Homebrew Advisory Database</a> | <a href="https://github.com/Homebrew/advisory-database/blob/HEAD/CONTRIBUTING.md">https://github.com/Homebrew/advisory-database/blob/HEAD/CONTRIBUTING.md</a> | <code>https://github.com/Homebrew/advisory-database/blob/HEAD/advisories/&lt;ID&gt;.json</code> | <code>https://raw.githubusercontent.com/Homebrew/advisory-database/HEAD/advisories/&lt;ID&gt;.json</code> | `[none]` | R-0019 (item) |
| N-0034 | L265-275 | <code>CGA</code> | <a href="https://packages.cgr.dev/chainguard/osv/all.json">Chainguard Security Notices</a> | TBD | TBD | <code>https://packages.cgr.dev/chainguard/osv/&lt;ID&gt;.json</code> | `[none]` | R-0019 (item) |
| N-0035 | L276-286 | <code>CleanStart</code> | <a href="https://github.com/cleanstart-dev/cleanstart-security-advisories"></a> | <code>https://github.com/cleanstart-dev/cleanstart-security-advisories/issues</code> | <code>https://github.com/cleanstart-dev/cleanstart-security-advisories</code> | <code>https://github.com/cleanstart-dev/cleanstart-security-advisories/tree/main/advisories/&lt;YYYY&gt;/CLEANSTART-YYYY-&lt;ID&gt;.json</code> | `[none]` | R-0019 (item) |
| N-0036 | L287-297 | <code>CURL</code> | <a href="https://curl.se/docs/security.html">Curl CVEs</a> | TBD | <code>https://curl.se/docs/&lt;ID&gt;.html</code> | <code>https://curl.se/docs/&lt;ID&gt;.json</code> | `[none]` | R-0019 (item) |
| N-0037 | L298-308 | <code>CVE</code> | <a href="https://nvd.nist.gov/">National Vulnerability Database (provided by OSV.dev)</a> | TBD | <code>https://nvd.nist.gov/vuln/detail/&lt;ID&gt;</code> | <code>https://api.osv.dev/v1/vulns/&lt;ID&gt;</code> | `[none]` | R-0019 (item) |
| N-0038 | L309-319 | <code>DEBIAN</code> | <a href="https://security-tracker.debian.org/tracker/">Debian Security Tracker (provided by OSV.dev)</a> | TBD | <code>https://security-tracker.debian.org/tracker/&lt;ID&gt;</code> | <code>https://api.osv.dev/v1/vulns/&lt;ID&gt;</code> | `[none]` | R-0019 (item) |
| N-0039 | L320-330 | <code>DHI</code> | <a href="https://github.com/docker-hardened-images/advisories">Docker Hardened Images Advisories</a> | TBD | <code>https://github.com/docker-hardened-images/advisories</code> | <code>https://github.com/docker-hardened-images/advisories/blob/main/osv/&lt;MODULE&gt;/&lt;ID&gt;</code> | `[none]` | R-0019 (item) |
| N-0040 | L331-341 | <code>DRUPAL</code> | <a href="https://github.com/DrupalSecurityTeam/drupal-advisory-database">Drupal Advisory Database</a> | <a href="https://www.drupal.org/docs/develop/issues/issue-procedures-and-etiquette/reporting-a-security-issue">https://www.drupal.org/docs/develop/issues/issue-procedures-and-etiquette/reporting-a-security-issue</a> | <code>https://www.drupal.org/security/</code> | <code>https://github.com/DrupalSecurityTeam/drupal-advisory-database/blob/main/advisories/&gt;module&lt;/&gt;ID&lt;.json</code> | `[none]` | R-0019 (item) |
| N-0041 | L342-352 | <code>DSA</code>/<code>DLA</code>/<code>DTSA</code> | <a href="https://www.debian.org/security/">Debian Security Advisory Database (provided by OSV.dev)</a> | TBD | <code>https://debian.org/security/&lt;YEAR&gt;/&lt;ID&gt;</code> (lowercase dsa) | <code>https://api.osv.dev/v1/vulns/&lt;ID&gt;</code> | `[none]` | R-0019 (item) |
| N-0042 | L353-363 | <code>ECHO</code> | <a href="https://advisory.echohq.com/osv/all.json">Echo Security Advisory Database</a> | <a href="https://echo.ai/">https://echo.ai</a> or contact us via <a href="mailto:support@echo.ai">support@echo.ai</a> | TBD | <code>https://advisory.echohq.com/osv/&lt;ID&gt;.json</code> | `[none]` | R-0019 (item) |
| N-0043 | L364-374 | <code>EEF</code> | <a href="https://cna.erlef.org/osv/all.json">Erlang Ecosystem Foundation CNA Vulnerabilities</a> | <a href="https://cna.erlef.org/contact">https://cna.erlef.org/contact</a> | <code>https://github.com/erlef-cna/website/tree/main/_data/osv</code> | <code>https://cna.erlef.org/osv/&lt;ID&gt;.json</code> | `[none]` | R-0019 (item) |
| N-0044 | L375-385 | <code>ELA</code> | <a href="https://www.freexian.com/lts/extended/">Debian Extended LTS Security Advisories (provided by Freexian)</a> | <a href="https://github.com/captn3m0/debian-elts-advisories/#contributing">https://github.com/captn3m0/debian-elts-advisories/#contributing</a> | <code>https://deb.freexian.com/extended-lts/tracker/&lt;ID&gt;</code> | <code>https://captnemo.in/debian-elts-advisories/advisories/&lt;ID&gt;.json</code> | `[none]` | R-0019 (item) |
| N-0045 | L386-396 | <code>GHSA</code> | <a href="https://github.com/github/advisory-database">GitHub Security Advisory Database</a> | <a href="https://github.com/github/advisory-database#contributions">https://github.com/github/advisory-database#contributions</a> | <code>https://github.com/advisories/&lt;ID&gt;</code> | <code>https://api.osv.dev/v1/vulns/&lt;ID&gt;</code> | `[none]` | R-0019 (item) |
| N-0046 | L397-407 | <code>GO</code> | <a href="https://pkg.go.dev/vuln/">Go Vulnerability Database</a> | <a href="https://github.com/golang/vulndb/issues/new/choose">https://github.com/golang/vulndb/issues/new/choose</a> | <code>https://pkg.go.dev/vuln/&lt;ID&gt;</code> | <code>https://vuln.go.dev/ID/&lt;ID&gt;.json</code> | `[none]` | R-0019 (item) |
| N-0047 | L408-418 | <code>GSD</code> | <a href="https://github.com/cloudsecurityalliance/gsd-database">Global Security Database</a> | TBD | <code>https://gsd.id/&lt;ID&gt;</code> | <code>https://api.gsd.id/&lt;ID&gt;</code> | `[none]` | R-0019 (item) |
| N-0048 | L419-429 | <code>HSEC</code> | <a href="https://github.com/haskell/security-advisories">Haskell Security Advisory Database</a> | <a href="https://github.com/haskell/security-advisories/blob/main/CONTRIBUTING.md">https://github.com/haskell/security-advisories/blob/main/CONTRIBUTING.md</a> | <code>TBD</code> | <code>https://raw.githubusercontent.com/haskell/security-advisories/main/advisories/&lt;ID&gt;.json</code> | `[none]` | R-0019 (item) |
| N-0049 | L430-440 | <code>JLSEC</code> | <a href="https://github.com/JuliaLang/SecurityAdvisories.jl">Julia Security Advisory Database</a> | <a href="https://github.com/JuliaLang/SecurityAdvisories.jl/blob/main/CONTRIBUTING.md">https://github.com/JuliaLang/SecurityAdvisories.jl/blob/main/CONTRIBUTING.md</a> | <code>https://github.com/JuliaLang/SecurityAdvisories.jl/blob/main/advisories/published/&lt;YEAR&gt;/&lt;ID&gt;.toml</code> | <code>https://github.com/JuliaLang/SecurityAdvisories.jl/blob/generated/osv/&lt;YEAR&gt;/&lt;ID&gt;.json</code> | `[none]` | R-0019 (item) |
| N-0050 | L441-451 | <code>KUBE</code> | <a href="https://github.com/kubernetes-sigs/cve-feed-osv">Kubernetes Official CVE Feed</a> | <a href="https://github.com/kubernetes-sigs/cve-feed-osv/blob/main/CONTRIBUTING.md">https://github.com/kubernetes-sigs/cve-feed-osv/blob/main/CONTRIBUTING.md</a> | <code>https://kubernetes.io/docs/reference/issues-security/official-cve-feed/index.json</code> | <code>https://raw.githubusercontent.com/kubernetes-sigs/cve-feed-osv/blob/main/vulns/&lt;ID&gt;.json</code> | `[none]` | R-0019 (item) |
| N-0051 | L452-462 | <code>LBSEC</code> | <a href="https://github.com/loopbackio/security/tree/main/advisories">LoopBack Advisory Database</a> | TBD | <code>N/A</code> | <code>N/A</code> | `[none]` | R-0019 (item) |
| N-0052 | L463-473 | <code>LSN</code> | <a href="https://ubuntu.com/security/livepatch">Livepatch Security Notices</a> | TBD | <code>https://ubuntu.com/security/notices/&lt;ID&gt;</code> | <code>https://github.com/canonical/ubuntu-security-notices/blob/main/osv/lsn/&lt;ID&gt;.json</code> | `[none]` | R-0019 (item) |
| N-0053 | L474-484 | <code>MGASA</code> | <a href="https://advisories.mageia.org/">Mageia Security Advisories</a> | <code>TBD</code> | <code>https://advisories.mageia.org/&lt;ID&gt;.html</code> | <code>https://advisories.mageia.org/&lt;ID&gt;.json</code> | `[none]` | R-0019 (item) |
| N-0054 | L485-495 | <code>MAL</code> | <a href="https://github.com/ossf/malicious-packages/tree/main/osv/">Malicious Packages Repository</a> | <a href="https://github.com/ossf/malicious-packages/blob/main/CONTRIBUTING.md">https://github.com/ossf/malicious-packages/blob/main/CONTRIBUTING.md</a> | <code>N/A</code> | <code>https://api.osv.dev/v1/vulns/&lt;ID&gt;</code> | `[none]` | R-0019 (item) |
| N-0055 | L496-506 | <code>MINI</code> | <a href="https://packages.mini.dev/advisories/osv/all.json">Minimus Security Notices</a> | <code>TBD</code> | <code>TBD</code> | <code>https://packages.mini.dev/advisories/osv/&lt;ID&gt;.json</code> | `[none]` | R-0019 (item) |
| N-0056 | L507-517 | <code>OESA</code> | <a href="https://www.openeuler.org/en/security/security-bulletins">openEuler Security Advisories</a> | <a href="https://www.openeuler.org/en/security/vulnerability-reporting">https://www.openeuler.org/en/security/vulnerability-reporting</a> | <code>https://www.openeuler.org/en/security/security-bulletins/detail/?id=openEuler-SA-&lt;ENTRYID&gt;</code> | <code>https://repo.openeuler.org/security/data/osv/&lt;ID&gt;.json</code> | `[none]` | R-0019 (item) |
| N-0057 | L518-528 | <code>OSEC</code> | <a href="https://github.com/ocaml/security-advisories">OCaml Security Advisory Database</a> | <a href="https://github.com/ocaml/security-advisories?tab=readme-ov-file#reporting-vulnerabilities">https://github.com/ocaml/security-advisories?tab=readme-ov-file#reporting-vulnerabilities</a> | <code>https://github.com/ocaml/security-advisories/advisories/&lt;YEAR&gt;/&lt;ID&gt;.md</code> | <code>https://raw.githubusercontent.com/ocaml/security-advisories/generated-osv/&lt;YEAR&gt;/&lt;ID&gt;.json</code> | `[none]` | R-0019 (item) |
| N-0058 | L529-539 | <code>OSV</code> | <a href="https://osv.dev/list">Advisories allocated by OSV.dev (currently only from OSS-Fuzz)</a> | <a href="https://github.com/google/oss-fuzz-vulns/issues">https://github.com/google/oss-fuzz-vulns/issues</a> | <code>https://osv.dev/vulnerability/&lt;ID&gt;</code> | <code>https://api.osv.dev/v1/vulns/&lt;ID&gt;</code> | `[only]` | R-0019 (item) |
| N-0059 | L540-550 | <code>PHSA</code> | <a href="https://github.com/vmware/photon/wiki/Security-Advisories">VMWare Photon Security Advisory Database</a> | <a href="https://github.com/captn3m0/photon-os-advisories#contributing">https://github.com/captn3m0/photon-os-advisories#contributing</a> | <code>https://github.com/vmware/photon/wiki/&lt;ID&gt;</code> | <code>https://github.com/captn3m0/photon-os-advisories/blob/main/advisories/&lt;ID&gt;.json</code> (unofficial) | `[none]` | R-0019 (item) |
| N-0060 | L551-561 | <code>PSF</code> | <a href="https://github.com/psf/advisory-database">Python Software Foundation Vulnerability Database</a> | <a href="https://github.com/psf/advisory-database/issues">https://github.com/psf/advisory-database/issues</a> | <code>TBD</code> | <code>TBD</code> | `[none]` | R-0019 (item) |
| N-0061 | L562-572 | <code>PYSEC</code> | <a href="https://github.com/pypa/advisory-db">PyPI Vulnerability Database</a> | <a href="https://github.com/pypa/advisory-database/issues">https://github.com/pypa/advisory-database/issues</a> | <code>https://osv.dev/vulnerability/&lt;ID&gt;</code> | <code>https://api.osv.dev/v1/vulns/&lt;ID&gt;</code> | `[none]` | R-0019 (item) |
| N-0062 | L573-583 | <code>RHSA</code>/<code>RHBA</code>/<code>RHEA</code> | <a href="https://security.access.redhat.com/data">Red Hat Security Data</a> | <a href="https://access.redhat.com/security/team/contact/">https://access.redhat.com/security/team/contact/</a> | <code>https://access.redhat.com/security/security-updates/security-advisories</code> | <code>https://security.access.redhat.com/data/osv/</code> | `[none]` | R-0019 (item) |
| N-0063 | L584-594 | <code>RHLW</code> | <a href="https://www.redhat.com/en/lightwell">Red Hat Lightwell</a> | TBD | <code>TBD</code> | <code>TBD</code> | `[none]` | R-0019 (item) |
| N-0064 | L595-605 | <code>RLSA</code>/<code>RXSA</code> | <a href="https://errata.rockylinux.org">Rocky Linux Security Advisory Database</a> | TBD | <code>https://errata.rockylinux.org/&lt;ID&gt;</code> | <code>https://apollo.build.resf.org/api/v3/osv/&lt;ID&gt;</code> | `[none]` | R-0019 (item) |
| N-0065 | L606-616 | <code>RSEC</code> | <a href="https://github.com/RConsortium/r-advisory-database">RConsortium Advisory Database</a> | <a href="https://github.com/RConsortium/r-advisory-database#readme">https://github.com/RConsortium/r-advisory-database#readme</a> | <code>https://osv.dev/vulnerability/&lt;ID&gt;</code> | <code>https://github.com/RConsortium/r-advisory-database/blob/main/vulns/&lt;package&gt;/&lt;ID&gt;.yaml</code> | `[none]` | R-0019 (item) |
| N-0066 | L617-627 | <code>ROOT</code> | <a href="https://api.root.io/external/osv/all.json">Root Security Advisories</a> | TBD | <code>TBD</code> | <code>https://api.root.io/external/osv/all.json</code> | `[none]` | R-0019 (item) |
| N-0067 | L628-638 | <code>RUSTSEC</code> | <a href="https://github.com/rustsec/advisory-db">RustSec Advisory Database</a> | <a href="https://github.com/RustSec/advisory-db/blob/main/CONTRIBUTING.md">https://github.com/RustSec/advisory-db/blob/main/CONTRIBUTING.md</a> | <code>https://rustsec.org/advisories/&lt;ID&gt;</code> | <code>https://raw.githubusercontent.com/rustsec/advisory-db/osv/crates/&lt;ID&gt;.json</code> | `[none]` | R-0019 (item) |
| N-0068 | L639-649 | <code>SUSE-SU</code>/<code>SUSE-RU</code>/<code>SUSE-FU</code>/<code>SUSE-OU</code>/<code>openSUSE-SU</code> | <a href="https://www.suse.com/support/security/">SUSE Security Landing page</a> | <a href="https://www.suse.com/support/security/contact/">https://www.suse.com/support/security/contact/</a> | <code>https://www.suse.com/support/update/</code> | <code>https://ftp.suse.com/pub/projects/security/osv/</code> | `[none]` | R-0019 (item) |
| N-0069 | L650-660 | <code>UBUNTU</code> | <a href="https://ubuntu.com/security/cves">Ubuntu CVE Reports</a> | TBD | <code>https://ubuntu.com/security/&lt;ID&gt;</code> | <code>https://github.com/canonical/ubuntu-security-notices/blob/main/osv/cve/&lt;YEAR&gt;/UBUNTU-&lt;ID&gt;.json</code> | `[none]` | R-0019 (item) |
| N-0070 | L661-671 | <code>USN</code> | <a href="https://ubuntu.com/security/notices">Ubuntu Security Notices</a> | TBD | <code>https://ubuntu.com/security/notices/&lt;ID&gt;</code> | <code>https://github.com/canonical/ubuntu-security-notices/blob/main/osv/usn/&lt;ID&gt;.json</code> | `[none]` | R-0019 (item) |
| N-0071 | L672-682 | <code>V8</code> | <a href="https://chromium.googlesource.com/chromium/src/+/refs/heads/main/docs/security/updates.md">V8/Chromium Time-Based Policy</a> | <a href="https://github.com/google/chromium-policy-vulnfeed/tree/main?tab=readme-ov-file#chromium-policy-vulnfeed">https://github.com/google/chromium-policy-vulnfeed/tree/main?tab=readme-ov-file#chromium-policy-vulnfeed</a> | <code>https://github.com/google/chromium-policy-vulnfeed/blob/main/advisories/V8-advisory.json</code> | <code>https://github.com/google/chromium-policy-vulnfeed/blob/main/advisories/V8-advisory.json</code> | `[none]` | R-0019 (item) |
| N-0072 | L683-693 | <code>VCPKG</code> | <a href="https://github.com/microsoft/vcpkg">vcpkg Security Advisory</a> | TBD | <code>TBD</code> | <code>TBD</code> | `[none]` | R-0019 (item) |
| N-0073 | L694-704 | <code>CLSA</code> | <a href="https://security.tuxcare.com/errata/">TuxCare Security Advisory</a> | Contact us via <a href="mailto:security-advisories@tuxcare.com">security-advisories@tuxcare.com</a> | <code>https://security.tuxcare.com/errata/&lt;component&gt;/&lt;os&gt;/&lt;ID&gt;.html</code> | <code>N/A</code> | `[none]` | R-0019 (item) |

Locator for every row: § id, modified fields > Defined database prefixes.

Row notes:

- N-0035 (L276-286): the Database cell is a link with no text, and the prefix `CleanStart` differs from the URL template `CLEANSTART-YYYY-<ID>.json` and from the JSON Schema's `CLEANSTART` (U-8, D-3).
- N-0040 (L331-341): the OSV Formatted URL has its angle-bracket entities reversed (U-9).
- N-0058 (L529-539): "only" is descriptive ("currently only from OSS-Fuzz"); it constrains nothing.
- N-0073 (L694-704): the last row, out of alphabetical order (U-7).

**N-0074.** § id, modified fields > Defined database prefixes / L712 · sentence · `[should]` · req: R-0020

> Publishers should publish information within their reasonable scope or ecosystem.

**N-0075.** § id, modified fields > Defined database prefixes / L712 · sentence · `[none]` · req: R-0021

> If one wants to derive their ID from a CVE record, adding the home database prefix is sufficient to communicate this.

#### modified field

**N-0076.** § id, modified fields > modified field / L716-717 · sentence · `[none]` · req: R-0022, R-0023

> The `modified` field gives the time the entry was last modified, as an RFC3339-formatted timestamp in UTC (ending in "Z").

**N-0077.** § id, modified fields > modified field / L717-719 · sentence · `[none]` · req: R-0024

> Given two different entries claiming to describe the same `id` field, the one with the later modification time is considered authoritative.

Note: a consumer rule for resolving two copies of one entry.

**N-0078.** § id, modified fields > modified field / L721 · sentence · `[required]` · req: R-0025

> The `id` and `modified` fields are required.

Note: the JSON Schema agrees (`/required`, N-0333); the proto marks neither field Required (D-12).

**N-0079.** § id, modified fields > modified field / L721-722 · sentence · `[required]` · req: R-0026

> For schema versions above 1.0.0, the `schema_version` field is also required.

Note: not enforced by the JSON Schema (D-1).

**N-0080.** § id, modified fields > modified field / L722-723 · sentence · `[optional]` · req: R-0027

> All other fields are optional, although of course an entry with no other metadata is not particularly useful.

Note: the proto comments mark `summary`, `details` and `affected` Required (D-12).

### published field

**N-0081.** § published field / L729-731 · field block · `[none]` · req: none: field block; the types are carried in messages.yaml

> ```json
> {
> 	"published": string
> }
> ```

**N-0082.** § published field / L734-735 · sentence · `[should]` · req: R-0028

> The `published` field gives the time the entry should be considered to have been published, as an RFC3339-formatted time stamp in UTC (ending in "Z").

Note (inferred): "should be considered" states how the value is read; the format part (RFC 3339, UTC, "Z") is a constraint on the value. Spelled "time stamp" here and "timestamp" elsewhere.

### withdrawn field

**N-0083.** § withdrawn field / L740-742 · field block · `[none]` · req: none: field block; the types are carried in messages.yaml

> ```json
> {
> 	"withdrawn": string
> }
> ```

**N-0084.** § withdrawn field / L745-746 · sentence · `[should]` · req: R-0029

> The `withdrawn` field gives the time the entry should be considered to have been withdrawn, as an RFC3339-formatted timestamp in UTC (ending in "Z").

**N-0085.** § withdrawn field / L746-747 · sentence · `[none]` · req: R-0030

> If the field is missing, then the entry has not been withdrawn.

**N-0086.** § withdrawn field / L747-748 · sentence · `[should]` · req: R-0031

> Any rationale for why the vulnerability has been withdrawn should go into the summary text.

Note: "the summary text" is not linked to a field; `summary` is defined as one line (U-6).

### aliases field

**N-0087.** § aliases field / L753-755 · field block · `[none]` · req: none: field block; the types are carried in messages.yaml

> ```json
> {
> 	"aliases": [ string ]
> }
> ```

**N-0088.** § aliases field / L758-759 · sentence · `[none]` · req: R-0032

> The `aliases` field gives a list of IDs of the same vulnerability in other databases, in the form of the `id` field.

**N-0089.** § aliases field / L759-761 · sentence · `[none]` · req: none: explains R-0032 (quoted in its notes)

> This allows one database to claim that its own entry describes the same vulnerability as one or more entries in other databases.

**N-0090.** § aliases field / L763-765 · sentence · `[can]` · req: R-0033

> Two vulnerabilities can be described as aliases if they affect any given software component the same way: either both vulnerabilities affect the software component or neither do.

**N-0091.** § aliases field / L765-766 · sentence · `[none]` · req: R-0033

> A subsequent patch addresses both of the vulnerabilities (and no others), and vice versa.

**N-0092.** § aliases field / L768-769 · sentence · `[should]` · req: R-0034

> Aliases should be considered symmetric (if A is an alias of B, then B is an alias of A) and transitive (If A aliases B and B aliases C, then A aliases C).

Note (inferred): "should be considered" defines how consumers interpret the relation.

**N-0093.** § aliases field / L771-773 · sentence · `[should not]` · req: R-0035

> Aliases should **not** be used to refer to vulnerabilities in packages upstream or downstream in a software supply chain from the given OSV record's affected package(s).

**N-0094.** § aliases field / L773-776 · sentence · `[must not]` · req: R-0036

> For example, if a CVE describes a vulnerability in a language library, and a Linux distribution package contains that library and therefore publishes an advisory, the distribution's OSV record must not list the CVE ID as an alias.

Note: an example sentence that carries its own "must not"; the general rule before it (N-0093) says "should **not**" (U-1).

**N-0095.** § aliases field / L777-778 · sentence · `[should]` · req: R-0037

> To refer to these upstream vulnerabilities, `upstream` should be used.

### upstream field

**N-0096.** § upstream field / L783-785 · field block · `[none]` · req: none: field block; the types are carried in messages.yaml

> ```text
> {
>   "upstream": [ string ]
> }
> ```

Note: the source fence has no `json` info string and uses two-space indentation, unlike the other field blocks.

**N-0097.** § upstream field / L788-789 · sentence · `[none]` · req: R-0038

> The `upstream` field gives a list of IDs of upstream vulnerabilities that are referred to by the vulnerability entry.

**N-0098.** § upstream field / L795 · sentence · `[should]` · req: R-0039

> `upstream` should be considered transitive but not symmetric.

**N-0099.** § upstream field / L797 · sentence · `[cannot]` · req: R-0040

> At the same time, if B is an upstream vulnerability for A, then A cannot be an upstream vulnerability for B.

Note: "cannot" makes the relation asymmetric, which is stronger than "not symmetric" in N-0098 (U-16).

### related field

**N-0100.** § related field / L802-804 · field block · `[none]` · req: none: field block; the types are carried in messages.yaml

> ```json
> {
> 	"related": [ string ]
> }
> ```

**N-0101.** § related field / L807-810 · sentence and list · `[none]` · req: R-0041

> The `related` field gives a list of IDs of closely related vulnerabilities, such as:
>
> ```text
> - A similar but completely different vulnerability.
> - Cases that do not satisfy the strict definition of `aliases` or `upstream`.
> ```

**N-0102.** § related field / L812 · sentence · `[none]` · req: R-0042

> Related vulnerabilities are symmetric but not transitive.

Note: stated as fact, where aliases and upstream use "should be considered" (U-17).

### summary, details fields

**N-0103.** § summary, details fields / L817-820 · field block · `[none]` · req: none: field block; the types are carried in messages.yaml

> ```json
> {
> 	"summary": string,
> 	"details": string
> }
> ```

**N-0104.** § summary, details fields / L823-824 · sentence · `[none]` · req: R-0043

> The `summary` field gives a one-line, English textual summary of the vulnerability.

**N-0105.** § summary, details fields / L824-825 · sentence · `[recommended]` · req: R-0044

> It is recommended that this field be kept short, on the order of no more than 120 characters.

Note: the proto comment says "under 120 characters" (D-19).

**N-0106.** § summary, details fields / L827-828 · sentence · `[none]` · req: R-0045

> The `details` field gives additional English textual details about the vulnerability.

**N-0107.** § summary, details fields / L830 · sentence · `[none]` · req: R-0046

> The `summary` field is plain text.

**N-0108.** § summary, details fields / L832-833 · sentence · `[none]` · req: R-0047

> The `details` field is CommonMark markdown (a subset of GitHub-Flavored Markdown).

**N-0109.** § summary, details fields / L833-834 · sentence · `[may]` · req: R-0048

> Display code may at its discretion sanitize the input further, such as stripping raw HTML and links that do not start with http:// or https://.

Note: the actor is display code (a consumer), not the producer.

**N-0110.** § summary, details fields / L835 · sentence · `[encouraged]` · req: R-0049

> Databases are encouraged not to include those in the first place.

Note: a recommendation without a modal verb ("are encouraged not to").

### severity field

**N-0111.** § severity field / L842-848 · field block · `[none]` · req: none: field block; the types are carried in messages.yaml

> ```json
> {
> 	"severity": [ {
> 		"type": string,
> 		"score": string,
> 		"source": string
> 	} ]
> }
> ```

**N-0112.** § severity field / L851-852 · sentence · `[none]` · req: R-0050

> The `severity` field is a JSON array that allows generating systems to describe the severity of a vulnerability using one or more quantitative scoring methods.

**N-0113.** § severity field / L853-854 · sentence · `[optional]` · req: R-0051

> Each `severity` item is a JSON object specifying a `type` and `score` property, as well as an optional `source` property, described below.

Note: the JSON Schema requires `type` and `score` (`/$defs/severity/items/required`, N-0345).

#### severity[].type field

**N-0114.** § severity field > severity[].type field / L858-859 · sentence · `[must]` · req: R-0052

> The `severity[].type` property must be one of the types defined below, which describes the quantitative method used to calculate the associated `score`.

Note: the four rows N-0115 to N-0118; the JSON Schema enum agrees (N-0339).

Severity types: the four type rows of the source table (L863 to L866), one statement per row; cells verbatim.

| N | line | Severity Type | Score Description | forms | req |
|---|---|---|---|---|---|
| N-0115 | L863 | `CVSS_V2` | A CVSS vector string representing the unique characteristics and severity of the vulnerability using a version of the [Common Vulnerability Scoring System notation](https://www.first.org/cvss/v2/guide#Metric-Groups) that is == 2.0 (e.g.`"AV:L/AC:M/Au:N/C:N/I:P/A:C"`). | `[none]` | R-0052 (item), R-0053 |
| N-0116 | L864 | `CVSS_V3` | A CVSS vector string representing the unique characteristics and severity of the vulnerability using a version of the [Common Vulnerability Scoring System notation](https://www.first.org/cvss/v3.0/specification-document#Vector-String) that is >= 3.0 and < 4.0 (e.g.`"CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:C/C:H/I:N/A:N"`). | `[none]` | R-0052 (item), R-0054 |
| N-0117 | L865 | `CVSS_V4` | A CVSS vector string representing the unique characteristics and severity of the vulnerability using a version on the [Common Vulnerability Scoring System notation](https://www.first.org/cvss/v4.0/specification-document#Vector-String) that is >= 4.0 and < 5.0 (e.g. `"CVSS:4.0/AV:N/AC:L/AT:N/PR:H/UI:N/VC:L/VI:L/VA:N/SC:N/SI:N/SA:N"`). | `[none]` | R-0052 (item), R-0055 |
| N-0118 | L866 | `Ubuntu`  | A lowercased string representing the [Ubuntu priority](https://ubuntu.com/security/cves/about#priority). This is based on many factors including severity, importance, risk, estimated number of affected users, software configuration, active exploitation, and other factors. | `[none]` | R-0052 (item), R-0056 |

Locator for every row: § severity field > severity[].type field.

Row notes:

- N-0115 (L863): the JSON Schema adds a score pattern (N-0341); D-9.
- N-0116 (L864): the JSON Schema admits only `CVSS:3.0/` and `CVSS:3.1/` (N-0342); D-9.
- N-0117 (L865): "a version on the" (U-12); the JSON Schema admits only `CVSS:4.0/` (N-0343); D-9.
- N-0118 (L866): the source row has no closing `|` (U-12); the JSON Schema closes the set of scores (N-0344); D-8.

#### severity[].score field

**N-0119.** § severity field > severity[].score field / L871-872 · sentence · `[none]` · req: R-0057

> The `severity[].score` property is a string representing the severity score based on the selected `severity[].type`, as described above.

#### severity[].source field

**N-0120.** § severity field > severity[].source field / L876-877 · sentence · `[optional]` · req: R-0058

> The `severity[].source` property is an optional string indicating the origin of the severity assessment.

**N-0121.** § severity field > severity[].source field / L879-880 · sentence · `[none]` · req: R-0059

> If `source` is omitted, the rating is implicitly attributed to the home database (as identified by the record's `id` field), whether as author or endorser.

Severity sources: the three rows of the source table (L884 to L886), one statement per row; cells verbatim.

| N | line | Source | Description | forms | req |
|---|---|---|---|---|---|
| N-0122 | L884 | `NVD` | The severity was provided by the [National Vulnerability Database (NVD)](https://nvd.nist.gov/). | `[none]` | R-0060 |
| N-0123 | L885 | `CNA` | The severity was provided by the [CVE Numbering Authority (CNA)](https://www.cve.org/ProgramOrganization/CNAs) that assigned the CVE. | `[none]` | R-0061 |
| N-0124 | L886 | `SELF` | The severity was provided by the home database. Unlike omitting `source`, this is an explicit declaration of provenance. | `[none]` | R-0062 |

Locator for every row: § severity field > severity[].source field.

Row notes:

- N-0122 (L884): the prose does not say this list is closed; the JSON Schema enum closes it (N-0340); D-7.

### affected fields

**N-0125.** § affected fields / L891-917 · field block · `[none]` · req: none: field block; the types are carried in messages.yaml

> ```json
> {
> 	"affected": [ {
> 		"package": {
> 			"ecosystem": string,
> 			"name": string,
> 			"purl": string
> 		},
> 		"severity": [ {
> 			"type": string,
> 			"score": string,
> 			"source": string
> 		} ],
> 		"ranges": [ {
> 			"type": string,
> 			"repo": string,
> 			"events": [ {
> 				"introduced": string,
> 				"fixed": string,
> 				"last_affected": string,
> 				"limit": string
> 			} ]
> 		} ],
> 		"versions": [ string ],
> 		"ecosystem_specific": { see description },
> 		"database_specific": { see description }
> 	} ]
> }
> ```

Note: unlike the Format Overview block (N-0005), this block has no `database_specific` inside `ranges` (D-21).

**N-0126.** § affected fields / L920-921 · sentence · `[none]` · req: R-0063

> The `affected` field is a JSON array containing objects that describes the affected package versions, meaning those that contain the vulnerability.

**N-0127.** § affected fields / L923-924 · sentence · `[none]` · req: R-0064

> Within each object in the `affected` array, the `package` field identifies the package containing the vulnerability.

**N-0128.** § affected fields / L924-926 · sentence · `[should]` · req: R-0065

> In most cases, there should be exactly one entry in the `affected` array per affected `package` to describe all affected versions.

**N-0129.** § affected fields / L926-929 · sentence · `[may]` · req: R-0066

> In rare cases, for example if the `ecosystem_specific` encodes platform information that doesn't apply equally to all listed versions and ranges, a separate entry with the same `package` in the `affected` array may be needed.

Note (inferred): "may be needed" permits a second entry for the same package in the stated case.

**N-0130.** § affected fields / L931-933 · sentence · `[can, can]` · req: R-0067

> The `versions` field can enumerate a specific set of affected versions, and the `ranges` field can list ranges of affected versions, under a given defined ordering.

**N-0131.** § affected fields / L933-934 · sentence · `[none]` · req: R-0068

> **A version is considered affected if it lies within any one of the ranges or is listed in the versions list.**

Note: the core matching rule; the algorithm in N-0271 implements it.

**N-0132.** § affected fields / L937-939 · sentence · `[recommended]` · req: R-0069

> The `versions` list is generally recommended to always be present, to allow software to easily answer the question "is this specific version affected?" without having to contain code specific to every different ecosystem.

Note: compare N-0135 ("must include"), N-0224 and N-0232 (U-2).

**N-0133.** § affected fields / L939-942 · sentence · `[can, may]` · req: R-0070

> If the affected versions can be accurately summarized by one or more non-overlapping ranges, they may be encoded using the `ranges` field with an appropriate type (see below).

**N-0134.** § affected fields / L942-943 · sentence · `[none]` · req: none: explains R-0070 (quoted in its notes)

> In this case, the ranges act as a kind of compact form of a larger `versions` list.

**N-0135.** § affected fields / L945-946 · sentence · `[can, must]` · req: R-0071

> Products or ecosystems that do not use version identifiers that can be represented as ranges must include the enumerated `versions` list instead.

Note: not checkable by the JSON Schema, which cannot know whether an ecosystem's versions can be represented as ranges (D-16).

#### affected[].package field

**N-0136.** § affected fields > affected[].package field / L950-951 · sentence · `[none]` · req: R-0072

> The `affected` object's `package` field is a JSON object identifying the affected code library or command provided by the package.

**N-0137.** § affected fields > affected[].package field / L951-952 · sentence · `[required, optional]` · req: R-0073

> The object itself has two required fields, `ecosystem` and `name`, and an optional `purl` field.

Note: the JSON Schema requires `ecosystem` and `name` (N-0318).

**N-0138.** § affected fields > affected[].package field / L954 · sentence · `[none]` · req: R-0074

> The `ecosystem` identifies the overall library ecosystem.

**N-0139.** § affected fields > affected[].package field / L954-955 · sentence · `[must]` · req: R-0074

> It must be one of the strings in the table below.

Note: the table is rows N-0147 to N-0198. The JSON Schema pattern (N-0337) also accepts `GIT` and any `:` suffix on every ecosystem (D-4, D-5).

**N-0140.** § affected fields > affected[].package field / L955-956 · sentence · `[none]` · req: R-0075

> The `name` field is a string identifying the library within its ecosystem.

**N-0141.** § affected fields > affected[].package field / L956-957 · sentence · `[must]` · req: R-0076

> The two fields must both be present, because the `ecosystem` serves to define the interpretation of the `name`.

**N-0142.** § affected fields > affected[].package field / L959-960 · sentence · `[imperative]` · req: R-0077

> Use the wildcard package name `*` to indicate that an advisory affects all packages within the specified `ecosystem`.

Note: an imperative without a verbal form. Not reconciled with ecosystems that restrict `name`, such as `Linux` (U-24).

**N-0143.** § affected fields > affected[].package field / L964-966 · sentence · `[none]` · req: R-0078

> The `purl` field is a string following the [Package URL specification](https://github.com/package-url/purl-spec) that identifies the package, without the `@version` component.

Note: the JSON Schema checks only that `purl` is a string.

**N-0144.** § affected fields > affected[].package field / L967 · sentence · `[optional, recommended]` · req: R-0079

> This field is optional but recommended.

**N-0145.** § affected fields > affected[].package field / L969-970 · sentence · `[can]` · req: R-0080

> Different ecosystems can define the same names; they identify different packages.

##### Defined ecosystems

**N-0146.** § affected fields > affected[].package field > Defined ecosystems / L983 · lead-in · `[none]` · req: R-0081

> The defined ecosystems are:

Defined ecosystems: the 52 ecosystem rows of the source table (L990 to L1041), one statement per row; cells verbatim. A row's forms are counted on the row itself; sentences inside a row are not numbered separately.

| N | line | Ecosystem | Description | forms | req |
|---|---|---|---|---|---|
| N-0147 | L990 | `AlmaLinux` | AlmaLinux package ecosystem; the `name` is the name of the source package. The ecosystem string might optionally have a `:<RELEASE>` suffix to scope the package to a particular AlmaLinux release. `<RELEASE>` is a numeric version. | `[might, optionally]` | R-0081 (item), R-0082 |
| N-0148 | L991 | `Alpaquita` | BellSoft Alpaquita Linux package ecosystem; the `name` is the name of the source package. The ecosystem string has a `:<RELEASE>` suffix to scope the package to a particular Alpaquita Linux release. `<RELEASE>` is the id of the particular Alpaquita Linux release. Examples: `Alpaquita:23`, `Alpaquita:stream`. | `[none]` | R-0081 (item), R-0083 |
| N-0149 | L992 | `Alpine` | The Alpine package ecosystem; the `name` is the name of the source package. The ecosystem string must have a `:v<RELEASE-NUMBER>` suffix to scope the package to a particular Alpine release branch (the `v` prefix is required). E.g. `v3.16`. | `[must, required]` | R-0081 (item), R-0084, R-0085 |
| N-0150 | L993 | `Android` | The Android ecosystem. Android organizes code using [`repo` tool](https://gerrit.googlesource.com/git-repo/+/HEAD/README.md), which manages multiple git projects under one or more remote git servers, where each project is identified by its name in [repo configuration](https://gerrit.googlesource.com/git-repo/+/HEAD/docs/manifest-format.md#Element-project) (e.g. `platform/frameworks/base`). The `name` field should contain the name of that affected git project/submodule. One exception is when the project contains the Linux kernel source code, in which case `name` field will be `:linux_kernel:`, followed by an optional SoC vendor name e.g. `:linux_kernel:Qualcomm`. The list of recognized SoC vendors is listed in the [Appendix](#android-soc-vendors) | `[should, optional]` | R-0081 (item), R-0086, R-0087 |
| N-0151 | L994 | `Azure Linux` | The Azure Linux package ecosystem; the `name` is the name of the source package. The ecosystem string has a `:<RELEASE>` suffix to scope the package to a particular Azure Linux release. `<RELEASE>` is a numeric version. | `[none]` | R-0081 (item), R-0088 |
| N-0152 | L995 | `BellSoft Hardened Containers` | BellSoft Hardened Containers package ecosystem; the `name` is the name of the source package. The ecosystem string has a `:<RELEASE>` suffix to scope the package to a particular Hardened Containers release. `<RELEASE>` is the id of the particular Hardened Containers release. Examples: `BellSoft Hardened Containers:23`, `BellSoft Hardened Containers:stream`. | `[none]` | R-0081 (item), R-0089 |
| N-0153 | L996 | `Bioconductor` | The biological R package ecosystem. The `name` is an R package name. | `[none]` | R-0081 (item), R-0090 |
| N-0154 | L997 | `Bitnami` | Bitnami package ecosystem; the `name` is the name of the affected component. | `[none]` | R-0081 (item), R-0091 |
| N-0155 | L998 | `Chainguard` | The Chainguard package ecosystem; the `name` is the name of the package. | `[none]` | R-0081 (item), R-0092 |
| N-0156 | L999 | `CleanStart` | The CleanStart package ecosystem; the `name` is the name of the package. | `[none]` | R-0081 (item), R-0093 |
| N-0157 | L1000 | `ConanCenter` | The ConanCenter ecosystem for C and C++; the `name` field is a Conan package name. | `[none]` | R-0081 (item), R-0094 |
| N-0158 | L1001 | `CRAN` | The R package ecosystem. The `name` is an R package name. | `[none]` | R-0081 (item), R-0095 |
| N-0159 | L1002 | `crates.io` | The crates.io ecosystem for Rust; the `name` field is a crate name. | `[none]` | R-0081 (item), R-0096 |
| N-0160 | L1003 | `Debian` | The Debian package ecosystem; the `name` is the name of the source package. The ecosystem string might optionally have a `:<RELEASE>` suffix to scope the package to a particular Debian release. `<RELEASE>` is a numeric version specified in the [Debian distro-info-data](https://debian.pages.debian.net/distro-info-data/debian.csv). For example, the ecosystem string "Debian:7" refers to the Debian 7 (wheezy) release. For versions without a numeric version, use the the string in the `series` column of the  `distro-info-data` CSV, e.g. "Debian:sid". | `[might, optionally, imperative]` | R-0081 (item), R-0097 |
| N-0161 | L1004 | `Docker Hardened Images` | The Docker Hardened Images package ecosystem; the `name` is the name of the package. | `[none]` | R-0081 (item), R-0098 |
| N-0162 | L1005 | `Echo` | The Echo package ecosystem; the `name` is the name of the source package. The ecosystem string might optionally have a `:<ECOSYSTEM>` suffix to denote an Echo secured build of a package from another ecosystem, in which case the `name` is the name of the package within that ecosystem and its versions are ordered by that ecosystem's rules. The supported values are `Echo:PyPI`, `Echo:Maven`, `Echo:npm` and `Echo:NuGet`. Without a suffix the package is an Echo OS package, whose versions are ordered by the Debian version ordering. Echo's secured builds carry a `+echo.<N>` build suffix, e.g. `1.2.3+echo.1`. | `[might, optionally]` | R-0081 (item), R-0099 |
| N-0163 | L1006 | `FreeBSD` | The FreeBSD ecosystem consists of three main components: the base system, kernel, and ports. For ports, the `name` refers to the name of a package managed by `pkg(8)`, which is the FreeBSD package manager. Ecosystem strings can include `:ports`, indicating that an issue pertains to ports (e.g., 'FreeBSD:ports'). Base system issues should be categorized under `:base`. The `ranges[].events` versions correspond to specific FreeBSD releases, such as 'FreeBSD:base:14.3'. Kernel-related issues are denoted by `:kernel`, with examples like 'FreeBSD:kernel'. Every namespace can have optional `:<RELEASE>` segment at last, which can be used to specify that an issue applies only to a particular FreeBSD release like. | `[can, should, can, optional, can, only]` | R-0081 (item), R-0100, R-0101, R-0102 |
| N-0164 | L1007 | `GHC` | The Haskell compiler ecosystem. The `name` field is the name of a component of the GHC compiler ecosystem (e.g., compiler, GHCI, RTS). | `[none]` | R-0081 (item), R-0103 |
| N-0165 | L1008 | `GitHub Actions` | The GitHub Actions ecosystem; the `name` field is the action's repository name with owner e.g. `{owner}/{repo}`. | `[none]` | R-0081 (item), R-0104 |
| N-0166 | L1009 | `Go` | The Go ecosystem; the `name` field is a Go module path. | `[none]` | R-0105 |
| N-0167 | L1010 | `Hackage` | The Haskell package ecosystem. The `name` field is a Haskell package name as published on Hackage. | `[none]` | R-0081 (item), R-0106 |
| N-0168 | L1011 | `Hex` | The package manager for the Erlang ecosystem; the `name` is a Hex package name. | `[none]` | R-0081 (item), R-0107 |
| N-0169 | L1012 | `Homebrew` | The Homebrew package manager for macOS and Linux; the `name` is the formula name (e.g. `openssl@3`). Casks are not currently in scope. Without a `:<tap>` suffix the formula is assumed to come from the default `homebrew/core` tap. A version is the formula version as reported by `brew info` with an `_N` suffix when the formula revision is nonzero (e.g. `1.81.6_6`), matching the version component of a `pkg:brew` purl. The ECOSYSTEM version ordering is Homebrew's [`PkgVersion`](https://github.com/Homebrew/brew/blob/HEAD/Library/Homebrew/pkg_version.rb) comparison: the version segment compared by Homebrew's [`Version`](https://github.com/Homebrew/brew/blob/HEAD/Library/Homebrew/version.rb) class, then the numeric revision suffix. The database uses `introduced` and `fixed` boundaries. | `[none]` | R-0081 (item), R-0108 |
| N-0170 | L1013 | `Julia` | The Julia Programming Language ecosystem; the `name` is a registered package in the General registry. | `[none]` | R-0081 (item), R-0109 |
| N-0171 | L1014 | `Kubernetes` | The Kubernetes ecosystem; `name` is the Go module name associated with the relevant Kubernetes component (e.g. `k8s.io/apiserver`) | `[none]` | R-0081 (item), R-0110 |
| N-0172 | L1015 | `Linux` | The Linux kernel. The only supported `name` is `Kernel`. | `[only]` | R-0081 (item), R-0111 |
| N-0173 | L1016 | `Mageia` | The Mageia Linux package ecosystem; the `name` is the name of the source package. The ecosystem string must have a `:<RELEASE-NUMBER>` suffix to scope the package to a particular Mageia release. Eg `Mageia:9`. | `[must]` | R-0081 (item), R-0112, R-0113 |
| N-0174 | L1017 | `Maven` | The Maven Java package ecosystem. The `name` field is a Maven package name in the format `groupId:artifactId`. The ecosystem string might optionally have a `:<REMOTE-REPO-URL>` suffix to denote the remote repository URL that best represents the source of truth for this package, without a trailing slash (e.g. `Maven:https://maven.google.com`). If this is omitted, this is assumed to be the Maven Central repository (`https://repo.maven.apache.org/maven2`). | `[might, optionally]` | R-0081 (item), R-0114 |
| N-0175 | L1018 | `MinimOS` | The MinimOS package ecosystem; the `name` is the name of the package. | `[none]` | R-0081 (item), R-0115 |
| N-0176 | L1019 | `npm` | The NPM ecosystem; the `name` field is an NPM package name. | `[none]` | R-0081 (item), R-0116 |
| N-0177 | L1020 | `NuGet` | The NuGet package ecosystem. The `name` field is a NuGet package name. | `[none]` | R-0081 (item), R-0117 |
| N-0178 | L1021 | `opam` | The OCaml package manager ecosystem. The `name` field is an opam package name. | `[none]` | R-0081 (item), R-0118 |
| N-0179 | L1022 | `openEuler` | The openEuler ecosystem; The `name` field is the name of the source RPM. The ecosystem string has a `<RELEASE>` suffix, specifying a particular openEuler LTS Release.`<RELEASE>` is numeric (YY.MM) version maintained in our [archive list](https://www.openeuler.org/en/download/?archive=true). Here, `LTS` stands for long term support and `SP` stands for service pack which offers extensions and enhancements of the major LTS version. Note innovation versions (those without `LTS`) are out of our security advisories' scope. The `ecosystem_specific` field contains all updated packages, including src rpm and binaries of different architectures. For more information, please refer to our [vulnerability disclosure policy](https://gitee.com/openeuler/security-committee/blob/master/docs/en/vulnerability-management-process/security-disclosure-en.md) and this [example](https://www.openeuler.org/en/security/security-bulletins/detail/?id=openEuler-SA-2025-1612) of a source security advisory. | `[none]` | R-0081 (item), R-0119 |
| N-0180 | L1023 | `openSUSE` | The openSUSE ecosystem; The ecosystem string has a `:<RELEASE>` suffix presenting the marketing name of the openSUSE distribution. `<RELEASE>` matches the value in the `/etc/os-release` `PRETTY_NAME` field. The `name` field is the name of the source RPM and accompanied by a purl. There is an `ecosystem_specific` specific array `binaries` of the associated RPM binary packages in this specific openSUSE distribution. The ECOSYSTEM version ordering is the RPM versioncompare ordering, and the database uses the `introduced` and `fixed` boundaries. | `[none]` | R-0081 (item), R-0120 |
| N-0181 | L1024 | `OSS-Fuzz` | For reports from the OSS-Fuzz project that have no more appropriate ecosystem; the `name` field is the name assigned by the OSS-Fuzz project, as recorded in the submitted fuzzing configuration. | `[none]` | R-0081 (item), R-0121 |
| N-0182 | L1025 | `Packagist` | The PHP package manager ecosystem; the `name` is a package name. The ecosystem string might optionally have a `:<REMOTE-REPO-URL>` suffix to denote the remote repository URL that best represents the source of truth for this package, without a trailing slash (e.g. `Packagist:https://packages.drupal.org/8`). If this is omitted, this is assumed to be the Packagist repository (`https://packagist.org`). | `[might, optionally]` | R-0081 (item), R-0122 |
| N-0183 | L1026 | `Photon OS` | The Photon OS package ecosystem; the `name` is the name of the RPM package. The ecosystem string must have a `:<RELEASE-NUMBER>` suffix to scope the package to a particular Photon OS release. Eg `Photon OS:3.0`. | `[must]` | R-0081 (item), R-0123, R-0124 |
| N-0184 | L1027 | `Pub` | The package manager for the Dart ecosystem; the `name` field is a Dart package name. | `[none]` | R-0081 (item), R-0125 |
| N-0185 | L1028 | `PyPI` | the Python PyPI ecosystem; the `name` field is a [normalized](https://www.python.org/dev/peps/pep-0503/#normalized-names) PyPI package name. | `[none]` | R-0081 (item), R-0126 |
| N-0186 | L1029 | `Red Hat` | The Red Hat package ecosystem; the `name` field is the name of a binary or source RPM. The ecosystem string has a `:<CPE>` suffix to scope the RPM to a specific Red Hat product stream. `<CPE>` is a translation of a Red Hat [Common Platform Enumerations](https://cpe.mitre.org/) (CPE) with the `cpe/:[oa]:(redhat):` prefix removed (for example, `Red Hat:rhel_aus:8.4::appstream` translates to `cpe:/a:redhat:rhel_aus:8.4::appstream`). Red Hat ecosystem identifiers can be used to identify vulnerable RPMs installed on a Red Hat system as explained [here](https://www.redhat.com/en/blog/how-accurately-match-oval-security-data-installed-rpms). | `[can]` | R-0081 (item), R-0127 |
| N-0187 | L1030 | `Red Hat Lightwell` | The Red Hat Lightwell ecosystem; Lightwell is an automated vulnerability-remediation service that publishes patched builds of open source libraries across multiple language ecosystems. The ecosystem **must** have a suffix matching an existing OSV ecosystem (e.g. `Red Hat Lightwell:Maven`) to denote what ecosystem the advisory is describing. The `name` field uses the naming convention of the package's native ecosystem. | `[must]` | R-0081 (item), R-0128, R-0129 |
| N-0188 | L1031 | `Rocky Linux` | The Rocky Linux package ecosystem; the `name` is the name of the source package. The ecosystem string might optionally have a `:<RELEASE>` suffix to scope the package to a particular Rocky Linux release. `<RELEASE>` is a numeric version. | `[might, optionally]` | R-0081 (item), R-0130 |
| N-0189 | L1032 | `Root` | The Root container security ecosystem. Root provides patched container images across multiple base distributions. The ecosystem uses hierarchical variants: Root:{BaseDistro}:{Version} for OS packages (e.g., Root:Alpine:3.18, Root:Debian:12) and Root:{PackageManager} for application packages (e.g., Root:PyPI, Root:npm). Package names use Root-specific prefixes (root-{package} for most, @root/{package} for npm). | `[none]` | R-0081 (item), R-0131 |
| N-0190 | L1033 | `RubyGems` | The RubyGems ecosystem; the `name` field is a gem name. | `[none]` | R-0081 (item), R-0132 |
| N-0191 | L1034 | `SUSE` | The SUSE ecosystem; The ecosystem string has a `:<RELEASE>` suffix representing the marketing name of the SUSE product. `<RELEASE>` matches the value in the /etc/os-release `PRETTY_NAME` field. The `name` field is the name of the source RPM and accompanied by a purl. There is a `ecosystem_specific` specific array `binaries` of the associated RPM binary packages in this specific SUSE product. The ECOSYSTEM version ordering is the RPM versioncompare ordering, and the database uses the `introduced` and `fixed` boundaries. | `[none]` | R-0081 (item), R-0133 |
| N-0192 | L1035 | `SwiftURL` | The Swift Package Manager ecosystem. The `name` is a Git URL to the source of the package. Versions are Git tags that comform to [SemVer 2.0](https://docs.swift.org/package-manager/PackageDescription/PackageDescription.html#version). | `[none]` | R-0081 (item), R-0134 |
| N-0193 | L1036 | `TuxCare` | TuxCare package ecosystem; the `name` is the name of the source package. The ecosystem string might optionally have a `:<RELEASE>` suffix to scope the package to a particular TuxCare release. `<RELEASE>` is a numeric version. | `[might, optionally]` | R-0081 (item), R-0135 |
| N-0194 | L1037 | `Ubuntu` | The Ubuntu package ecosystem; the `name` field is the name of the source package. The ecosystem string has a `:<RELEASE>` suffix to scope the package to a particular Ubuntu release. `<RELEASE>` is a numeric ("YY.MM") version as specified in [Ubuntu Releases](https://wiki.ubuntu.com/Releases), with a mandatory `:LTS` suffix if the release is marked as LTS. The release version may also be prefixed with `:Pro:` to denote Ubuntu Pro (aka Expanded Security Maintenance (ESM)) updates. For example, the ecosystem string "Ubuntu:22.04:LTS" refers to Ubuntu 22.04 LTS (jammy), while "Ubuntu:Pro:18.04:LTS" refers to fixes that landed in Ubuntu 18.04 LTS (bionic) under Ubuntu Pro/ESM. | `[mandatory, may]` | R-0081 (item), R-0136, R-0137, R-0138 |
| N-0195 | L1038 | `vcpkg` | The vcpkg ecosystem for Microsoft's C/C++ package manager; the `name` is the vcpkg port name (e.g. `bzip2`, `ffmpeg`). The ecosystem string has no release suffix. A version is the upstream port version; the integer `port-version` (incremented when the port packaging changes) is carried in the purl `port_version` qualifier. The default registry is [`microsoft/vcpkg`](https://github.com/microsoft/vcpkg); non-default registries are denoted by the purl `repository_url` / `repository_revision` qualifiers. | `[none]` | R-0081 (item), R-0139 |
| N-0196 | L1039 | `VSCode` | The Visual Studio Code extensions ecosystem; the `name` is the `<publisher>.<name>` string which uniquely identifies a package. This identifier is composed from the `Publisher` and `Id` attributes of the `Identity` element in the package's `.vsixmanifest` file. It also corresponds to the `itemName` parameter of the package as found on the [Visual Studio Marketplace for VS Code](https://marketplace.visualstudio.com/vscode) extensions page, or the `namespace` and `name` fields of the [OpenVSX](https://open-vsx.org/) API response for the target package. The ecosystem string might optionally have a `:<REMOTE-REPO-URL>` suffix to denote the remote repository URL that best represents the source of truth for this package, without a trailing slash (e.g. `VSCode:https://open-vsx.org`). If this is omitted, this is assumed to be the Visual Studio Marketplace for VSCode (`https://marketplace.visualstudio.com/vscode`). | `[might, optionally]` | R-0081 (item), R-0140 |
| N-0197 | L1040 | `Wolfi` | The Wolfi package ecosystem; the `name` is the name of the package. | `[none]` | R-0081 (item), R-0141 |
| N-0198 | L1041 | `WordPress` | The WordPress ecosystem. The ecosystem string may have a suffix to specify the component: `:Core` for WordPress Core (the `name` is `wordpress`), `:Plugin` for plugins (the `name` is the plugin slug), or `:Theme` for themes (the `name` is the theme slug). The slug is the unique identifier used in the WordPress.org repository. | `[may]` | R-0081 (item), R-0142 |

Locator for every row: § affected fields > affected[].package field > Defined ecosystems.

Row notes:

- N-0149 (L992): "must" and "required" are not checked by the JSON Schema (D-5).
- N-0150 (L993): the `name` rules are not checked by the JSON Schema; the vendor list is N-0317.
- N-0160 (L1003): "use the the string" is an imperative (U-12); the JSON Schema does not check the suffix.
- N-0162 (L1005): "The supported values are" closes the set of suffixes; not checked by the JSON Schema (D-5).
- N-0163 (L1006): the last sentence breaks off; see U-10.
- N-0172 (L1015): "only" restricts `name`; not checked by the JSON Schema (D-5, U-24).
- N-0173 (L1016): not checked by the JSON Schema (D-5).
- N-0179 (L1022): the suffix is written without `:` (U-11).
- N-0183 (L1026): not checked by the JSON Schema (D-5).
- N-0186 (L1029): "can" is possibility (U-15).
- N-0187 (L1030): not checked by the JSON Schema (D-5).
- N-0192 (L1035): "comform" (U-12).
- N-0194 (L1037): see U-13; not checked by the JSON Schema (D-5).
- N-0195 (L1038): "has no release suffix"; the JSON Schema accepts any suffix (D-5).
- N-0198 (L1041): the three suffixes form a closed set; not checked by the JSON Schema (D-5).

**N-0199.** § affected fields > affected[].package field > Defined ecosystems / L1046-1048 · sentence · `[permitted, can]` · req: R-0143

> It is permitted for a database name (the DB prefix in the `id` field) and an ecosystem name to be the same, provided they have the same owner who can make decisions about the meaning of the `ecosystem_specific` field (see below).

#### Depicting multiple ecosystems in the same record

**N-0200.** § affected fields > Depicting multiple ecosystems in the same record / L1052 · sentence · `[can]` · req: R-0144

> An OSV record can describe a vulnerability affecting multiple ecosystems.

**N-0201.** § affected fields > Depicting multiple ecosystems in the same record / L1052 · sentence · `[none]` · req: R-0144

> This is done by including multiple objects in the `affected` array, each specifying a different `package.ecosystem`.

##### Separating Git and Strict Ecosystems

**N-0202.** § affected fields > Depicting multiple ecosystems in the same record > Separating Git and Strict Ecosystems / L1056 · sentence · `[recommended]` · req: R-0145

> When providing vulnerability information for both a strict packaging ecosystem (such as `npm`, `PyPI`, or `Go`) and Git-level details (such as commit hashes), it is recommended to use separate entries in the `affected` array.

**N-0203.** § affected fields > Depicting multiple ecosystems in the same record > Separating Git and Strict Ecosystems / L1058 · list item · `[should]` · req: R-0146

> **Strict Ecosystem Entry**: This entry should use the specific ecosystem name (e.g., `"ecosystem": "npm"`).

**N-0204.** § affected fields > Depicting multiple ecosystems in the same record > Separating Git and Strict Ecosystems / L1058 · list item, sentence 2 · `[should]` · req: R-0147

> It should list affected versions in the `versions` field or use `ECOSYSTEM` or `SEMVER` range types in the `ranges` field.

**N-0205.** § affected fields > Depicting multiple ecosystems in the same record > Separating Git and Strict Ecosystems / L1059 · list item · `[should]` · req: R-0148

> **Git Entry**: This entry should use **no** `package` field.

Note: the JSON Schema accepts `GIT` as a `package.ecosystem` value, and the proto marks `package` Optional (D-4).

**N-0206.** § affected fields > Depicting multiple ecosystems in the same record > Separating Git and Strict Ecosystems / L1059 · list item, sentence 2 · `[should]` · req: R-0149

> It should use the `GIT` range type in the `ranges` field to specify affected commit ranges.

##### Version Enumeration for Git Entries

**N-0207.** § affected fields > Depicting multiple ecosystems in the same record > Version Enumeration for Git Entries / L1065 · sentence · `[none]` · req: R-0150

> For entries using `GIT` "ecosystem", the `versions` field is typically populated with enumerated versions (tags) derived from the Git repository specified in `ranges[].repo`.

Note (inferred): describes what `versions` holds for GIT entries ("typically"); it does not oblige anyone to populate it.

**N-0208.** § affected fields > Depicting multiple ecosystems in the same record > Version Enumeration for Git Entries / L1065 · sentence · `[none]` · req: R-0151

> If in the same affected field as a strict ecosystem, versions from both the Git repository and the strict ecosystem will appear in the `versions` array.

#### affected[].severity field

**N-0209.** § affected fields > affected[].severity field / L1069 · sentence · `[optional]` · req: R-0152

> The `severity` field is an optional element [defined here](#severity-field).

**N-0210.** § affected fields > affected[].severity field / L1070-1071 · sentence · `[none]` · req: R-0153

> This `severity` field applies to a specific package, in cases where affected packages have differing severities for the same vulnerability.

**N-0211.** § affected fields > affected[].severity field / L1071-1073 · sentence · `[must not]` · req: R-0154

> If any package level `severity` fields are set, the top level [`severity`](#severity-field) must not be set.

Note: the JSON Schema enforces the contrapositive (`/allOf/0`, N-0334); "set" is not defined for `null` or an empty array (D-11, U-26).

#### affected[].versions field

**N-0212.** § affected fields > affected[].versions field / L1077 · sentence · `[none]` · req: R-0155

> The `affected` object's `versions` field is a JSON array of strings.

**N-0213.** § affected fields > affected[].versions field / L1077-1079 · sentence · `[none]` · req: R-0156

> Each string is a single affected version in whatever version syntax is used by the given package ecosystem.

**N-0214.** § affected fields > affected[].versions field / L1081 · sentence · `[cannot]` · req: R-0157

> When using the `GIT` pseudo-ecosystem (either because there is no well-defined packaging ecosystem, or to provide supplementary Git-level details), versions specified in this array typically represent Git tags and cannot be relied upon to conform to any particular package manager's syntax.

**N-0215.** § affected fields > affected[].versions field / L1081 · sentence · `[should]` · req: R-0158

> In this situation, the GIT commit ranges in [`affected[].ranges`](#affectedranges-field) should be used to match vulnerabilities by Git commit hashes.

**N-0216.** § affected fields > affected[].versions field / L1083 · sentence · `[recommended]` · req: R-0159

> If you are providing both strict ecosystem versions and Git-level details, it is recommended to separate them into different entries.

#### affected[].ranges[] field

**N-0217.** § affected fields > affected[].ranges[] field / L1087-1088 · sentence · `[none]` · req: R-0160

> The `affected` object's `ranges` field is a JSON array of objects describing the affected ranges of versions.

#### affected[].ranges[].type field

**N-0218.** § affected fields > affected[].ranges[].type field / L1092 · sentence · `[required]` · req: R-0161

> In the `ranges` field, the `type` field is required.

Note: JSON Schema (`/properties/affected/items/properties/ranges/items/required`, N-0327) and proto agree.

**N-0219.** § affected fields > affected[].ranges[].type field / L1092-1094 · sentence · `[none]` · req: R-0162

> It specifies the type of version range being recorded and defines the interpretation of the `events` object's `introduced`, `fixed`, and any type-specific fields.

**N-0220.** § affected fields > affected[].ranges[].type field / L1096 · lead-in · `[none]` · req: R-0163

> The defined types and their additional fields are:

Note: the JSON Schema enum is `GIT`, `SEMVER`, `ECOSYSTEM` (N-0319).

**N-0221.** § affected fields > affected[].ranges[].type field / L1098-1099 · list item · `[none]` · req: R-0164

> `SEMVER`: The versions `introduced` and `fixed` are semantic versions as defined by [SemVer 2.0.0](https://semver.org), with no leading "v" prefix.

**N-0222.** § affected fields > affected[].ranges[].type field / L1099-1100 · list item, sentence 2 · `[none]` · req: R-0165

> The relation `u < v` denotes the precedence order defined in [section 11 of SemVer 2.0](https://semver.org/#spec-item-11).

**N-0223.** § affected fields > affected[].ranges[].type field / L1101-1102 · list item, sentence 3 · `[should not]` · req: R-0166

> Ranges listed with type `SEMVER` should not overlap: since SEMVER is a strict linear ordering, it is always possible to simplify to non-overlapping ranges.

**N-0224.** § affected fields > affected[].ranges[].type field / L1104-1105 · list item, paragraph 2 · `[none]` · req: R-0167

> Specifying one or more `SEMVER` ranges removes the requirement to specify an explicit enumerated `versions` list (see the discussion above).

Note: "the requirement" refers back to N-0132, which is only a recommendation (U-2).

**N-0225.** § affected fields > affected[].ranges[].type field / L1107-1108 · list item, paragraph 3 · `[may, recommend]` · req: R-0168

> Some ecosystems may recommend using SemVer 2.0 for versioning without explicitly enforcing it.

Note (inferred): "may" is possibility and "recommend" is the ecosystem's, not this document's; the sentence sets the condition for N-0226.

**N-0226.** § affected fields > affected[].ranges[].type field / L1108 · list item, paragraph 3, sentence 2 · `[should]` · req: R-0168

> In those cases you should use the `ECOSYSTEM` type instead.

**N-0227.** § affected fields > affected[].ranges[].type field / L1110-1112 · list item · `[none]` · req: R-0169

> `ECOSYSTEM`: The versions `introduced` and `fixed` are arbitrary, uninterpreted strings specific to the package ecosystem, which does not conform to SemVer 2.0’s version ordering.

**N-0228.** § affected fields > affected[].ranges[].type field / L1114-1118 · list item, paragraph 2 · `[recommended, may not, may not]` · req: R-0170

> It is recommended that you provide an explicitly enumerated `versions` list when specifying one or more `ECOSYSTEM` ranges, because `ECOSYSTEM` range inclusion queries may not be able to be answered without reference to the package ecosystem’s own logic and therefore may not be able to be used by ecosystem-independent processors.

Note (inferred): both "may not" express possibility (U-15).

**N-0229.** § affected fields > affected[].ranges[].type field / L1122-1123 · list item · `[none]` · req: R-0171

> `GIT`: The versions `introduced` and `fixed` are full-length Git commit hashes.

Note: the JSON Schema pattern also admits `0` and 64-hex-digit hashes and rejects `*` (D-10).

**N-0230.** § affected fields > affected[].ranges[].type field / L1123-1124 · list item, sentence 2 · `[none]` · req: none: explains R-0171 (quoted in its notes)

> The repository’s commit graph is needed to evaluate whether a given version is in the range.

**N-0231.** § affected fields > affected[].ranges[].type field / L1124-1125 · list item, sentence 3 · `[none]` · req: R-0172

> The relation `u < v` is true when commit `u` is a (perhaps distant) parent of commit `v`.

**N-0232.** § affected fields > affected[].ranges[].type field / L1127-1129 · list item, paragraph 2 · `[cannot]` · req: R-0173

> Specifying one or more `GIT` ranges does NOT remove the requirement to specify an explicitly enumerated `versions` list, because `GIT` range inclusion queries cannot be answered without access to a copy of the underlying Git repository.

Note: "does NOT remove the requirement" (uppercase in the source) refers to N-0132 and N-0135 (U-2).

#### affected[].ranges[].events fields

**N-0233.** § affected fields > affected[].ranges[].events fields / L1133 · sentence · `[none]` · req: R-0174

> The `ranges` object's `events` field is a JSON array of objects.

**N-0234.** § affected fields > affected[].ranges[].events fields / L1133-1138 · sentence and list · `[none]` · req: R-0174

> Each object describes a single version that either:
>
> ```text
> 1. Introduces a vulnerability: `{"introduced": string}`
> 2. Fixes a vulnerability: `{"fixed": string}`
> 3. Describes the last known affected version: `{"last_affected": string}`
> 4. Sets an upper limit on the range being described: `{"limit": string}`
> ```

**N-0235.** § affected fields > affected[].ranges[].events fields / L1140-1141 · sentence · `[none]` · req: none: explains R-0174 (quoted in its notes)

> These `events` objects represent a "timeline" of status changes for the affected package.

**N-0236.** § affected fields > affected[].ranges[].events fields / L1143-1144 · sentence · `[none]` · req: R-0175

> The values of `introduced`, `fixed`, `last_affected` and `limit` are version strings as defined by the `affected[].ranges[].type` field.

**N-0237.** § affected fields > affected[].ranges[].events fields / L1144-1146 · sentence · `[none]` · req: R-0176

> Note that these version strings are not guaranteed to exactly match versions of the package found in the upstream package repository.

##### Special values

**N-0238.** § affected fields > affected[].ranges[].events fields > Special values / L1151-1152 · list item · `[none]` · req: R-0177

> `introduced` allows a version of the value `"0"` to represent a version that sorts before any other version.

Note: the JSON Schema GIT pattern admits `0` for every event type, not only `introduced` (D-10).

**N-0239.** § affected fields > affected[].ranges[].events fields > Special values / L1153 · list item · `[none]` · req: R-0178

> `limit` allows versions containing the string `"*"` to represent "infinity".

Note: the text says containing, not equal to (U-5). The JSON Schema GIT pattern rejects `*` in GIT ranges (D-10).

**N-0240.** § affected fields > affected[].ranges[].events fields > Special values / L1154-1155 · list item, sentence 2 · `[none]` · req: R-0179

> If no limit events are provided, an implicit `{ "limit": "*" }` is assumed to exist.

**N-0241.** § affected fields > affected[].ranges[].events fields > Special values / L1155 · list item, sentence 3 · `[allowed]` · req: R-0180

> Multiple `limit` events are allowed in the same range.

##### Requirements

**N-0242.** § affected fields > affected[].ranges[].events fields > Requirements / L1159-1160 · sentence · `[only, allowed]` · req: R-0181

> Only **a single type** (either `introduced`, `fixed`, `last_affected`, `limit`) is allowed in each event object.

Note: the JSON Schema enforces this with `oneOf` (N-0322); the proto `Event` message cannot express it (D-13).

**N-0243.** § affected fields > affected[].ranges[].events fields > Requirements / L1160-1161 · sentence · `[invalid]` · req: none: the example of R-0181 (quoted in its notes; examples SRC-L1161-1, EMB-L1161)

> For instance, `{"introduced": "1.0.0", "fixed": "1.0.2"}` is **invalid**.

Note: an example inside the rule that states a verdict; a ready negative test vector.

**N-0244.** § affected fields > affected[].ranges[].events fields > Requirements / L1163-1164 · sentence · `[may]` · req: R-0182

> Entries in the `events` array may be "last_affected" or "fixed" events, but not both.

Note: "but not both" is the prohibition; JSON Schema `allOf/2` (N-0326) enforces it.

**N-0245.** § affected fields > affected[].ranges[].events fields > Requirements / L1164-1166 · sentence · `[recommended]` · req: R-0183

> It's **strongly recommended** to use `fixed` instead of `last_affected` where possible, as it precisely identifies the version which contains the fix.

**N-0246.** § affected fields > affected[].ranges[].events fields > Requirements / L1166-1167 · sentence · `[should]` · req: R-0184

> `last_affected` should be thought of as the hard ceiling of the vulnerability _at the time of publication_ in the absence of a fixed version.

**N-0247.** § affected fields > affected[].ranges[].events fields > Requirements / L1168 · sentence · `[should]` · req: R-0185

> Versions above `last_affected` should be considered unaffected.

**N-0248.** § affected fields > affected[].ranges[].events fields > Requirements / L1168-1170 · sentence · `[preferred]` · req: none: rationale for R-0183 (quoted in its notes)

> Unfortunately this opens up the possibility for false negatives, which is why `fixed` is overwhelmingly preferred.

Note: restates the preference of N-0245 with its reason.

**N-0249.** § affected fields > affected[].ranges[].events fields > Requirements / L1173-1174 · sentence · `[none]` · req: none: scopes R-0186 and R-0187 to GIT ranges (quoted in the notes of R-0186)

> The `fixed` and `limit` events are closely related and involve a similar trade-off for `GIT` ranges.

Note (inferred): kept because it scopes the next sentence to GIT ranges (U-4).

**N-0250.** § affected fields > affected[].ranges[].events fields > Requirements / L1175-1177 · sentence · `[must]` · req: R-0186

> `events` arrays with `fixed` events must include all other cherrypicked fix commits in all branches as separate `fixed` events to avoid *false positive* matches in other branches.

**N-0251.** § affected fields > affected[].ranges[].events fields > Requirements / L1177-1179 · sentence · `[may]` · req: R-0187

> Conversely, `limit` events restrict the set of vulnerable commits to those reachable from the `limit`, which may result in *false negatives*.

Note (inferred): "may" is possibility.

**N-0252.** § affected fields > affected[].ranges[].events fields > Requirements / L1179-1180 · sentence · `[recommended]` · req: R-0188

> Where possible, it's strongly recommended to use `fixed` over `limit`.

**N-0253.** § affected fields > affected[].ranges[].events fields > Requirements / L1182 · sentence · `[must]` · req: R-0189

> There must be at least one `introduced` object in the `events` array.

Note: JSON Schema `contains` (N-0321) and `minItems: 1` enforce it; the proto does not.

**N-0254.** § affected fields > affected[].ranges[].events fields > Requirements / L1182-1184 · sentence · `[not required, recommended]` · req: R-0190

> While not required, it's also recommended to keep the `events` array sorted according to the `affected[].ranges[].type` of the range.

#### affected[].ranges[].repo field

**N-0255.** § affected fields > affected[].ranges[].repo field / L1190-1191 · sentence · `[none]` · req: R-0191

> The `ranges` object's `repo` field is the URL of the package's code repository.

**N-0256.** § affected fields > affected[].ranges[].repo field / L1191-1192 · sentence · `[should]` · req: R-0192

> The value should be in a format that's directly usable as an argument for the version control system's clone command (e.g. `git clone`).

**N-0257.** § affected fields > affected[].ranges[].repo field / L1194-1195 · sentence · `[none]` · req: R-0193

> The `affected` object's `ranges` field is a JSON array of objects, each describing a single range.

Note: repeats N-0217 under the `repo` heading (U-3).

**N-0258.** § affected fields > affected[].ranges[].repo field / L1195-1196 · sentence · `[none]` · req: R-0193

> The range object defines the fields `type`, `events`, `repo`.  `introduced`, `fixed`, and additional type-specific fields as needed.

Note: the part after the first full stop has no verb, and the list omits `database_specific` (U-3).

**N-0259.** § affected fields > affected[].ranges[].repo field / L1198 · sentence · `[required]` · req: R-0194

> This field is required if `affected[].ranges[].type` is `GIT`.

Note: "This field" follows a paragraph about `ranges`; under this heading it means `repo` (U-3). JSON Schema `allOf/0` (N-0324) and the proto agree.

#### affected[].ranges[].database_specific field

**N-0260.** § affected fields > affected[].ranges[].database_specific field / L1202-1203 · sentence · `[none]` · req: R-0195

> The `ranges` object's `database_specific` field is a JSON object holding additional information about the range as defined by the database from which the record was obtained.

**N-0261.** § affected fields > affected[].ranges[].database_specific field / L1203-1205 · sentence · `[none]` · req: R-0195

> The meaning of the values within the object is entirely defined by the database and beyond the scope of this document.

**N-0262.** § affected fields > affected[].ranges[].database_specific field / L1207-1208 · sentence · `[should, only, may]` · req: R-0196

> Databases should only use this field to store additional context that may be useful in converting from the OSV format back into the original database representation.

Note (inferred): "may" is possibility.

**N-0263.** § affected fields > affected[].ranges[].database_specific field / L1208-1209 · sentence · `[none]` · req: R-0197

> Values in this field have no effect on the [evaluation algorithm](#evaluation).

#### affected[].ecosystem_specific field

**N-0264.** § affected fields > affected[].ecosystem_specific field / L1213-1215 · sentence · `[none]` · req: R-0198

> The `affected` object's `ecosystem_specific` field is a JSON object holding additional information about the vulnerability as defined by the ecosystem for which the record applies.

**N-0265.** § affected fields > affected[].ecosystem_specific field / L1215-1216 · sentence · `[none]` · req: R-0198

> The meaning of the values within the object is entirely defined by the ecosystem and beyond the scope of this document.

**N-0266.** § affected fields > affected[].ecosystem_specific field / L1222-1223 · sentence · `[none]` · req: none: says the R-0198 object is one field (named in the notes of R-0198)

> Note that this is a single field with key "ecosystem_specific", which itself contains a JSON object with unspecified fields.

#### affected[].database_specific field

**N-0267.** § affected fields > affected[].database_specific field / L1227-1229 · sentence · `[none]` · req: R-0199

> The `affected` object's `database_specific` field is a JSON object holding additional information about the vulnerability as defined by the database from which the record was obtained.

**N-0268.** § affected fields > affected[].database_specific field / L1229-1230 · sentence · `[none]` · req: R-0199

> The meaning of the values within the object is entirely defined by the database and beyond the scope of this document.

**N-0269.** § affected fields > affected[].database_specific field / L1232-1234 · sentence · `[should]` · req: R-0200

> In general, the canonical database for a particular ecosystem should record its information in `ecosystem_specific`, allowing other aggregator databases to put their own summaries in `database_specific`.

**N-0270.** § affected fields > affected[].database_specific field / L1239-1240 · sentence · `[none]` · req: none: says the R-0199 object is one field (named in the notes of R-0199)

> Note that this is a single field with key "database_specific", which itself contains a JSON object with unspecified fields.

#### Evaluation

**N-0271.** § affected fields > Evaluation / L1244-1291 · sentence and pseudocode · `[none]` · req: R-0201

> The algorithm to evaluate if a package `pkg` at version `v` is vulnerable is given by the `IsVulnerable` function in the pseudocode below:
>
> ```text
> func IsVulnerable(pkg, v, osv)
>   for affected in osv.affected
>     if affected.package == pkg
>       if IncludedInVersions(v, affected.versions) ||
>            IncludedInRanges(v, affected.ranges)
>         return true
>
>   return false
>
> func IncludedInVersions(v, versions)
>   for version in versions
>     if v == version
>       return true
>
>   return false
>
> func IncludedInRanges(v, ranges)
>   for range in ranges
>     if BeforeLimits(v, range)
>       vulnerable = false
>       for evt in sorted(range.events)
>         if evt.introduced is present && v >= evt.introduced
>            vulnerable = true
>         else if evt.fixed is present && v >= evt.fixed
>            vulnerable = false
>         else if evt.last_affected is present && v > evt.last_affected
>            vulnerable = false
>
>       if vulnerable
>         return true
>
>   return false
>
> func BeforeLimits(v, range)
>   if no limit events in range.events
>     # implicit "*" entry is assumed
>     return true
>
>   for evt in range.events
>     if evt.limit is present and v < evt.limit
>       return true
>
>   return false
>
> ```

Note: the fence is labelled `python` but the code is pseudocode. It does not say how `sorted` and the comparisons work for GIT ranges, where versions are commits ordered by ancestry, or how `affected.package == pkg` treats an entry without `package` (U-23).

#### Examples

##### Unfixed vulnerability example

No statements in this section (L1295 to L1306); its content is listed under Informative content excluded.

##### Fixed vulnerability example

No statements in this section (L1307 to L1319); its content is listed under Informative content excluded.

##### Multiple range example

No statements in this section (L1320 to L1335); its content is listed under Informative content excluded.

##### Limit events

**N-0272.** § affected fields > Examples > Limit events / L1337-1338 · sentence · `[should not]` · req: R-0202

> `limit` events are typically not necessary for describing numbered (linear) version ranges and should not be used.

Note: a general rule printed inside a worked-example subsection.

**N-0273.** § affected fields > Examples > Limit events / L1371-1372 · sentence · `[may]` · req: none: a statement of possibility; its may is excluded (keyword_accounting, L1371; notes of R-0203)

> This may be useful if the scope of a vulnerability entry is limited to a small set of linear branches.

Note (inferred): "may" is possibility; guidance on when to use `limit`.

**N-0274.** § affected fields > Examples > Limit events / L1372-1373 · sentence · `[may]` · req: R-0203

> Multiple `limit` events may be specified for each branch -- each expands the scope of the git commit graph to cover.

##### `last_affected` vs `fixed` example

**N-0275.** § affected fields > Examples > `last_affected` vs `fixed` example / L1413 · sentence · `[preferable]` · req: R-0204

> Using `fixed` is preferable to `last_affected` whenever possible.

### references field

**N-0276.** § references field / L1419-1424 · field block · `[none]` · req: none: field block; the types are carried in messages.yaml

> ```json
> {
> 	"references": [ {
> 		"type": string,
> 		"url": string
> 	} ]
> }
> ```

**N-0277.** § references field / L1427 · sentence · `[none]` · req: R-0205

> The `references` field contains a list of JSON objects describing references.

**N-0278.** § references field / L1428-1429 · sentence · `[none]` · req: R-0206

> Each object has a string field `type` specifying the type of reference, and a string field `url`.

Note: the JSON Schema requires both (N-0330); so do the proto comments.

**N-0279.** § references field / L1429-1431 · sentence · `[none]` · req: R-0207

> The `url` is the fully-qualified URL (including the scheme, typically "https://") linking to additional information, advisories, issue tracker entries, and so on about the vulnerability itself.

Note: JSON Schema `format: uri` (N-0329) is an annotation unless format assertion is enabled (D-15).

**N-0280.** § references field / L1431-1432 · sentence · `[none]` · req: R-0208

> The `type` specifies what kind of reference the URL is.

**N-0281.** § references field / L1434 · lead-in · `[none]` · req: R-0209

> The known reference `type` values are:

Note: "known" does not say the list is closed; the JSON Schema enum closes it and adds `GIT` (D-6, D-7).

Known reference types: the ten list items (L1436 to L1455), one statement per item; text verbatim from after the `- ` list marker, wrapped lines joined.

| N | lines | item | forms | req |
|---|---|---|---|---|
| N-0282 | L1436 | `ADVISORY`: A published security advisory for the vulnerability. | `[none]` | R-0209 (item) |
| N-0283 | L1437 | `ARTICLE`: An article or blog post describing the vulnerability. | `[none]` | R-0209 (item) |
| N-0284 | L1438-1440 | `DETECTION`: A tool, script, scanner, or other mechanism that allows for detection of the vulnerability in production environments. e.g. YARA rules, hashes, virus signature, or other scanners. | `[none]` | R-0209 (item) |
| N-0285 | L1441-1442 | `DISCUSSION`: A social media discussion regarding the vulnerability, e.g. a Twitter, Mastodon, Hacker News, or Reddit thread. | `[none]` | R-0209 (item) |
| N-0286 | L1443 | `REPORT`: A report, typically on a bug or issue tracker, of the vulnerability. | `[none]` | R-0209 (item) |
| N-0287 | L1444-1447 | `FIX`: A source code browser link to the fix (e.g., a GitHub commit) Note that the `fix` type is meant for viewing by people using web browsers.  Programs interested in analyzing the exact commit range would do better to use the `GIT`-typed `affected[].ranges` entries (described above). | `[none]` | R-0209 (item), R-0210 |
| N-0288 | L1448-1451 | `INTRODUCED`: A source code browser link to the introduction of the vulnerability (e.g., a GitHub commit) Note that the `introduced` type is meant for viewing by people using web browsers.  Programs interested in analyzing the exact commit range would do better to use the `GIT`-typed `affected[].ranges` entries (described above). | `[none]` | R-0209 (item), R-0211 |
| N-0289 | L1452 | `PACKAGE`: A home web page for the package. | `[none]` | R-0209 (item) |
| N-0290 | L1453-1454 | `EVIDENCE`: A demonstration of the validity of a vulnerability claim, e.g. `app.any.run` replaying the exploitation of the vulnerability. | `[none]` | R-0209 (item) |
| N-0291 | L1455 | `WEB`: A web page of some unspecified kind. | `[none]` | R-0209 (item) |

Locator for every row: § references field.

Row notes:

- N-0287 (L1444-1447): says "the `fix` type" in lowercase (U-21); "would do better to use" recommends GIT ranges without a verbal form.
- N-0288 (L1448-1451): says "the `introduced` type" in lowercase (U-21); "would do better to use" recommends GIT ranges without a verbal form.

### credits fields

**N-0292.** § credits fields / L1460-1466 · field block · `[none]` · req: none: field block; the types are carried in messages.yaml

> ```json
> {
> 	"credits": [ {
> 		"name": string,
> 		"contact": [ string ],
> 		"type": string,
> 	} ]
> }
> ```

Note: a trailing comma follows `"type": string` in the source (U-18).

**N-0293.** § credits fields / L1469-1471 · sentence · `[none]` · req: R-0212

> The `credits` field is a JSON array providing a way to give credit for the discovery, confirmation, patch, or other events in the life cycle of a vulnerability.

**N-0294.** § credits fields / L1473-1475 · sentence · `[must]` · req: R-0213

> Each of the objects in the `credits` array must contain at minimum a `name` field specifying the name of the individual or entity being credited, using whatever notation they prefer.

**N-0295.** § credits fields / L1475 · sentence · `[can, optionally]` · req: R-0214

> It can also optionally include a `contact` JSON array.

#### credits[].name field

**N-0296.** § credits fields > credits[].name field / L1479-1480 · sentence · `[should]` · req: R-0215

> `credits[].name` should specify the name, label, or other identifier of the individual or entity being credited, using whatever notation the creditor prefers.

Note: "the creditor prefers" here, "they prefer" in N-0294 (U-20).

**N-0297.** § credits fields > credits[].name field / L1482-1483 · sentence · `[required]` · req: R-0216

> This field is required for each `credits` entry.

#### credits[].contact[] field

**N-0298.** § credits fields > credits[].contact[] field / L1487-1488 · sentence · `[should, can]` · req: R-0217

> Each `credits[].contact[]` entry should be a valid, fully qualified, plain-text URL at which the credited can be reached.

Note: the JSON Schema checks only that each entry is a string.

**N-0299.** § credits fields > credits[].contact[] field / L1488 · sentence · `[optional]` · req: R-0218

> Providing contacts is optional.

#### credits[].type field

**N-0300.** § credits fields > credits[].type field / L1492-1493 · sentence · `[optional, should]` · req: R-0219

> The optional `credits[].type` field should specify the type or role of the individual or entity being credited.

**N-0301.** § credits fields > credits[].type field / L1493-1494 · lead-in · `[must]` · req: R-0220

> It must be one of the following defined credit types:

Note: the ten items N-0302 to N-0311; the JSON Schema enum agrees (N-0331).

Defined credit types: the ten list items (L1496 to L1505), one statement per item; text verbatim from after the `- ` list marker.

| N | line | item | forms | req |
|---|---|---|---|---|
| N-0302 | L1496 | `FINDER`: identified the vulnerability. | `[none]` | R-0220 (item) |
| N-0303 | L1497 | `REPORTER`: notified the vendor of the vulnerability to a CNA. | `[none]` | R-0220 (item) |
| N-0304 | L1498 | `ANALYST`: validated the vulnerability to ensure accuracy or severity. | `[none]` | R-0220 (item) |
| N-0305 | L1499 | `COORDINATOR`: facilitated the coordinated response process. | `[none]` | R-0220 (item) |
| N-0306 | L1500 | `REMEDIATION_DEVELOPER`: prepared a code change or other remediation plans. | `[none]` | R-0220 (item) |
| N-0307 | L1501 | `REMEDIATION_REVIEWER`: reviewed vulnerability remediation plans or code changes for effectiveness and completeness. | `[none]` | R-0220 (item) |
| N-0308 | L1502 | `REMEDIATION_VERIFIER`: tested and verified the vulnerability or its remediation. | `[none]` | R-0220 (item) |
| N-0309 | L1503 | `TOOL`: names of tools used in vulnerability discovery or identification. | `[none]` | R-0220 (item) |
| N-0310 | L1504 | `SPONSOR`: supported the vulnerability identification or remediation activities. | `[none]` | R-0220 (item) |
| N-0311 | L1505 | `OTHER`: any other type or role that does not fall under the categories described above. | `[none]` | R-0220 (item) |

Locator for every row: § credits fields > credits[].type field.

**N-0312.** § credits fields > credits[].type field / L1507-1508 · sentence · `[none]` · req: R-0221

> These values and their definitions correspond directly to the credit types defined in the [MITRE CVE specification](https://cveproject.github.io/cve-schema/schema/v5.0/docs/#collapseDescription_oneOf_i0_containers_cna_credits_items_type).

##### Examples

No statements in this section (L1510 to L1526); its content is listed under Informative content excluded.

### database_specific field

**N-0313.** § database_specific field / L1529-1531 · sentence · `[none]` · req: R-0222

> The top-level `database_specific` field is a JSON object holding additional information about the vulnerability as defined by the database from which the record was obtained.

**N-0314.** § database_specific field / L1531-1532 · sentence · `[none]` · req: R-0222

> The meaning of the values within the object is entirely defined by the database and beyond the scope of this document.

**N-0315.** § database_specific field / L1534-1536 · sentence · `[none]` · req: R-0223

> Unlike the `affected[].database_specific` field which is specific to each affected product, this top-level field allows aggregator databases to add custom data that they considered applicable to the whole vulnerability.

**N-0316.** § database_specific field / L1538-1539 · sentence · `[none]` · req: none: says the R-0222 object is one field (named in the notes of R-0223)

> Note that this is a single field with key "database_specific", which itself contains a JSON object with unspecified fields.

## Examples

No statements. The section (L1541 to L1995) holds ten informative example records under these headings: Go vulnerability (L1543); NPM vulnerability in GitHub database (L1549); OSV vulnerability (L1631); Rust vulnerability (L1665); Python vulnerability (L1707); Debian vulnerability (L1757); Ruby vulnerability (L1803); Haskell Hackage vulnerability (L1843); Haskell GHC vulnerability (L1889); R CRAN & Bioconductor vulnerability (L1937). They are listed under Informative content excluded and belong to the examples artifact.

## Appendix

### Android SoC Vendors

**N-0317.** § Android SoC Vendors / L2001-2010 · sentence and list · `[optionally]` · req: R-0224

> When a package in the `Android` ecosystem is the Linux kernel source code, its `name` will be `:linux_kernel:`, optionally appended with one of the following SoC vendor names indicating applicability of the vulnerability to kernels of that particular vendor:
>
> ```text
> - AMLogic
> - ARM
> - Broadcom
> - MediaTek
> - Marvell
> - NVIDIA
> - Qualcomm
> - Unisoc
> ```

Note: the list the `Android` row (N-0150) calls "recognized SoC vendors"; the JSON Schema does not check `name`.

## JSON Schema: validation/schema.json

Dialect: JSON Schema draft 2020-12 (`/$schema`). The prose offers this schema
"for validation" (N-0004); it is a check, not the specification.
The schema itself is not copied here (the schema artifact under
`distilled/schema/` carries it verbatim). This section records its normative
content: every constraint as a numbered statement with its JSON Pointer and
value, an index of every validation keyword occurrence, the `type` keywords by
value and the `$ref` bindings. Under draft 2020-12 `format` only annotates
unless a validator turns on format assertion, and `title` and `description`
never validate.

### Schema identification and annotations

Annotations only: they do not validate. Values verbatim (as JSON strings).

| JSON Pointer | schema line | value |
|---|---|---|
| `/$schema` | L2 | `"https://json-schema.org/draft/2020-12/schema"` |
| `/$id` | L3 | `"https://raw.githubusercontent.com/ossf/osv-schema/main/validation/schema.json"` |
| `/title` | L4 | `"Open Source Vulnerability"` |
| `/description` | L5 | `"A schema for describing a vulnerability in an open source package. See also https://ossf.github.io/osv-schema/"` |
| `/$defs/ecosystemName/title` | L397 | `"Currently supported ecosystems"` |
| `/$defs/ecosystemName/description` | L398 | `"These ecosystems are also documented at https://ossf.github.io/osv-schema/#affectedpackage-field"` |
| `/$defs/ecosystemWithSuffix/title` | L460 | `"Currently supported ecosystems"` |
| `/$defs/ecosystemWithSuffix/description` | L461 | `"These ecosystems are also documented at https://ossf.github.io/osv-schema/#affectedpackage-field"` |
| `/$defs/prefix/title` | L466 | `"Currently supported home database identifier prefixes"` |
| `/$defs/prefix/description` | L467 | `"These home databases are also documented at https://ossf.github.io/osv-schema/#id-modified-fields"` |

The four `title` strings inside `affected[].ranges[]` are part of the numbered statements below, because three of them carry a verbal form.

### Constraint statements

**N-0318.** `/properties/affected/items/properties/package/required` / schema L74-77 · `required` · `[none]` · req: R-0073, R-0076

```json
["ecosystem", "name"]
```

Prose: N-0137, N-0141. Proto: both fields marked Required (N-0350, N-0351).

**N-0319.** `/properties/affected/items/properties/ranges/items/properties/type/enum` / schema L89-93 · `enum` · `[none]` · req: R-0226

```json
["GIT", "SEMVER", "ECOSYSTEM"]
```

Prose: N-0220. The proto enum adds `UNSPECIFIED = 0` (N-0354).

**N-0320.** `/properties/affected/items/properties/ranges/items/properties/events/title` / schema L99 · annotation (`title`) · `[must, may]` · req: R-0189

```json
"events must contain an introduced object and may contain fixed, last_affected or limit objects"
```

An annotation: it has no validation effect. Its "must" and "may" restate N-0253 and N-0234.

**N-0321.** `/properties/affected/items/properties/ranges/items/properties/events/contains` / schema L101-105 · `contains` · `[none]` · req: R-0189

```json
{"required": ["introduced"]}
```

At least one item must have an `introduced` key. Prose: N-0253.

**N-0322.** `/properties/affected/items/properties/ranges/items/properties/events/items/oneOf` / schema L108-153 · `oneOf` · `[none]` · req: R-0181

```json
[{"type": "object", "properties": {"introduced": {"type": "string"}}, "required": ["introduced"]}, {"type": "object", "properties": {"fixed": {"type": "string"}}, "required": ["fixed"]}, {"type": "object", "properties": {"last_affected": {"type": "string"}}, "required": ["last_affected"]}, {"type": "object", "properties": {"limit": {"type": "string"}}, "required": ["limit"]}]
```

Exactly one subschema must match. Each requires one key and forbids none, so an event with two of the four keys matches two subschemas and fails (this enforces N-0242); an event with one key plus an unknown key passes (D-13).

**N-0323.** `/properties/affected/items/properties/ranges/items/properties/events/minItems` / schema L155 · `minItems` · `[none]` · req: R-0189

```json
1
```

Already implied by `contains`. Prose: N-0253.

**N-0324.** `/properties/affected/items/properties/ranges/items/allOf/0` / schema L162-176 · `allOf` item (`if`/`then`) · `[require]` · req: R-0194

```json
{"title": "GIT ranges require a repo", "if": {"properties": {"type": {"const": "GIT"}}}, "then": {"required": ["repo"]}}
```

Prose: N-0259. Proto: N-0356.

**N-0325.** `/properties/affected/items/properties/ranges/items/allOf/1` / schema L177-244 · `allOf` item (`if`/`then`) · `[must]` · req: R-0227

```json
{"title": "GIT ranges must use full-length commit hashes", "if": {"properties": {"type": {"const": "GIT"}}}, "then": {"properties": {"events": {"items": {"oneOf": [{"type": "object", "properties": {"introduced": {"type": "string", "pattern": "^(0|[a-f0-9]{40}|[a-f0-9]{64})$"}}, "required": ["introduced"]}, {"type": "object", "properties": {"fixed": {"type": "string", "pattern": "^(0|[a-f0-9]{40}|[a-f0-9]{64})$"}}, "required": ["fixed"]}, {"type": "object", "properties": {"last_affected": {"type": "string", "pattern": "^(0|[a-f0-9]{40}|[a-f0-9]{64})$"}}, "required": ["last_affected"]}, {"type": "object", "properties": {"limit": {"type": "string", "pattern": "^(0|[a-f0-9]{40}|[a-f0-9]{64})$"}}, "required": ["limit"]}]}}}}}
```

Prose: N-0229. The pattern admits `0` for every event type and 40 or 64 lowercase hexadecimal digits, and rejects `*` (D-10).

**N-0326.** `/properties/affected/items/properties/ranges/items/allOf/2` / schema L245-271 · `allOf` item (`if`/`then`) · `[none]` · req: R-0182

```json
{"title": "last_affected and fixed events are mutually exclusive", "if": {"properties": {"events": {"contains": {"required": ["last_affected"]}}}}, "then": {"not": {"properties": {"events": {"contains": {"required": ["fixed"]}}}}}}
```

Prose: N-0244.

**N-0327.** `/properties/affected/items/properties/ranges/items/required` / schema L273-276 · `required` · `[none]` · req: R-0161, R-0189

```json
["type", "events"]
```

Prose requires `type` (N-0218); it never says `events` itself is required, though N-0253 implies it. Proto marks both Required (N-0355, N-0357).

**N-0328.** `/properties/references/items/properties/type/enum` / schema L304-316 · `enum` · `[none]` · req: R-0228

```json
["ADVISORY", "ARTICLE", "DETECTION", "DISCUSSION", "REPORT", "FIX", "INTRODUCED", "GIT", "PACKAGE", "EVIDENCE", "WEB"]
```

The prose list (N-0282 to N-0291) has no `GIT`; the proto enum has it (N-0370). See D-6 and D-7.

**N-0329.** `/properties/references/items/properties/url/format` / schema L320 · `format` · `[none]` · req: R-0207

```json
"uri"
```

Prose: N-0279. Under draft 2020-12 `format` only annotates unless the validator turns on format assertion (D-15).

**N-0330.** `/properties/references/items/required` / schema L323-326 · `required` · `[none]` · req: R-0206

```json
["type", "url"]
```

Prose: N-0278. Proto: N-0371, N-0372.

**N-0331.** `/properties/credits/items/properties/type/enum` / schema L345-356 · `enum` · `[none]` · req: R-0220

```json
["FINDER", "REPORTER", "ANALYST", "COORDINATOR", "REMEDIATION_DEVELOPER", "REMEDIATION_REVIEWER", "REMEDIATION_VERIFIER", "TOOL", "SPONSOR", "OTHER"]
```

Prose: N-0301 and items N-0302 to N-0311; the same ten values. The proto enum adds `UNSPECIFIED = 0` (N-0368).

**N-0332.** `/properties/credits/items/required` / schema L359-361 · `required` · `[none]` · req: R-0213, R-0216

```json
["name"]
```

Prose: N-0294, N-0297. The proto does not mark `name` Required (D-12).

**N-0333.** `/required` / schema L368-371 · `required` · `[none]` · req: R-0025

```json
["id", "modified"]
```

Prose: N-0078. `schema_version`, required by N-0079 for versions above 1.0.0, is not listed (D-1).

**N-0334.** `/allOf/0` / schema L373-392 · `allOf` item (`if`/`then`) · `[none]` · req: R-0154

```json
{"if": {"required": ["severity"]}, "then": {"properties": {"affected": {"items": {"properties": {"severity": {"type": "null"}}}}}}}
```

If the top-level `severity` key is present (whatever its value, `null` and `[]` included), every `affected[].severity` that is present must be `null`. The prose rule N-0211 is the contrapositive (D-11).

**N-0335.** `/$defs/ecosystemName/enum` / schema L399-452 · `enum` · `[none]` · req: none: an unreferenced $defs that validates nothing; its 52 values equal the R-0081 enumeration

```json
["AlmaLinux", "Alpaquita", "Alpine", "Android", "Azure Linux", "BellSoft Hardened Containers", "Bioconductor", "Bitnami", "Chainguard", "CleanStart", "ConanCenter", "CRAN", "crates.io", "Debian", "Docker Hardened Images", "Echo", "FreeBSD", "GHC", "GitHub Actions", "Go", "Hackage", "Hex", "Homebrew", "Julia", "Kubernetes", "Linux", "Mageia", "Maven", "MinimOS", "npm", "NuGet", "opam", "openEuler", "openSUSE", "OSS-Fuzz", "Packagist", "Photon OS", "Pub", "PyPI", "Red Hat", "Red Hat Lightwell", "Rocky Linux", "Root", "RubyGems", "SUSE", "SwiftURL", "TuxCare", "Ubuntu", "vcpkg", "VSCode", "Wolfi", "WordPress"]
```

No `$ref` points to `/$defs/ecosystemName`, so this enum validates nothing. Its 52 values equal the prose table (N-0147 to N-0198), in the same order (D-25).

**N-0336.** `/$defs/ecosystemSuffix/pattern` / schema L456 · `pattern` · `[none]` · req: none: an unreferenced $defs that validates nothing

```json
":.+"
```

No `$ref` points to `/$defs/ecosystemSuffix`; unanchored (D-25).

**N-0337.** `/$defs/ecosystemWithSuffix/pattern` / schema L462 · `pattern` · `[none]` · req: R-0229

```json
"^(AlmaLinux|Alpaquita|Alpine|Android|Azure Linux|BellSoft Hardened Containers|Bioconductor|Bitnami|Chainguard|CleanStart|ConanCenter|CRAN|crates\\.io|Debian|Docker Hardened Images|Echo|FreeBSD|GHC|GitHub Actions|Go|Hackage|Hex|Homebrew|Julia|Kubernetes|Linux|Mageia|Maven|MinimOS|npm|NuGet|opam|openEuler|openSUSE|OSS-Fuzz|Packagist|Photon OS|Pub|PyPI|Red Hat|Red Hat Lightwell|Rocky Linux|Root|RubyGems|SUSE|SwiftURL|TuxCare|Ubuntu|vcpkg|VSCode|Wolfi|WordPress|GIT)(:.+)?$"
```

Used by `package.ecosystem` (`/properties/affected/items/properties/package/properties/ecosystem/$ref`). Anchored at both ends. The 52 prose ecosystems plus `GIT`, each optionally followed by `:` and at least one character (D-4, D-5). Prose: N-0139.

**N-0338.** `/$defs/prefix/pattern` / schema L468 · `pattern` · `[none]` · req: R-0230

```json
"^(x_|(ASB-A|PUB-A|ALPINE|ALSA|ALBA|ALEA|AZL|BELL|BIT|BREW|CGA|CLEANSTART|CLSA|CURL|CVE|DEBIAN|DHI|DRUPAL|DSA|DLA|ELA|DTSA|ECHO|EEF|FreeBSD|GHSA|GO|GSD|HSEC|JLSEC|KUBE|LBSEC|LSN|MAL|MINI|MGASA|OESA|OSEC|OSV|openSUSE-SU|PHSA|PSF|PYSEC|RHBA|RHEA|RHLW|RHSA|RLSA|RXSA|RSEC|ROOT|RUSTSEC|SUSE-[SRFO]U|UBUNTU|USN|V8|VCPKG)-)"
```

Used by `id` (`/properties/id/$ref`); its only constraint. Anchored at the start only, so it checks the prefix and nothing after it. `x_` may be followed by anything; every other prefix must be followed by `-`. Lists `CLEANSTART` where the prose table has `CleanStart`, and `FreeBSD`, which has no prose row (D-2, D-3). Prose: N-0017, N-0019, N-0025, rows from N-0026.

**N-0339.** `/$defs/severity/items/properties/type/enum` / schema L480-485 · `enum` · `[none]` · req: R-0052

```json
["CVSS_V2", "CVSS_V3", "CVSS_V4", "Ubuntu"]
```

Prose: N-0114, rows N-0115 to N-0118. The proto enum adds `UNSPECIFIED = 0` (N-0365).

**N-0340.** `/$defs/severity/items/properties/source/enum` / schema L492-496 · `enum` · `[none]` · req: R-0231

```json
["NVD", "CNA", "SELF"]
```

Prose rows N-0122 to N-0124; the prose does not say the list is closed (D-7). The proto enum adds `SOURCE_UNSPECIFIED = 0` (N-0366).

**N-0341.** `/$defs/severity/items/allOf/0` / schema L500-515 · `allOf` item (`if`/`then`) · `[none]` · req: R-0232

```json
{"if": {"properties": {"type": {"const": "CVSS_V2"}}}, "then": {"properties": {"score": {"pattern": "^((AV:[NAL]|AC:[LMH]|Au:[MSN]|[CIA]:[NPC]|E:(U|POC|F|H|ND)|RL:(OF|TF|W|U|ND)|RC:(UC|UR|C|ND)|CDP:(N|L|LM|MH|H|ND)|TD:(N|L|M|H|ND)|[CIA]R:(L|M|H|ND))/)*(AV:[NAL]|AC:[LMH]|Au:[MSN]|[CIA]:[NPC]|E:(U|POC|F|H|ND)|RL:(OF|TF|W|U|ND)|RC:(UC|UR|C|ND)|CDP:(N|L|LM|MH|H|ND)|TD:(N|L|M|H|ND)|[CIA]R:(L|M|H|ND))$"}}}}
```

Prose row N-0115. Accepts any non-empty `/`-separated sequence of known CVSS v2 metrics, in any order and with repeats; a complete base vector is not required (D-9).

**N-0342.** `/$defs/severity/items/allOf/1` / schema L516-531 · `allOf` item (`if`/`then`) · `[none]` · req: R-0233

```json
{"if": {"properties": {"type": {"const": "CVSS_V3"}}}, "then": {"properties": {"score": {"pattern": "^CVSS:3[.][01]/((AV:[NALP]|AC:[LH]|PR:[NLH]|UI:[NR]|S:[UC]|[CIA]:[NLH]|E:[XUPFH]|RL:[XOTWU]|RC:[XURC]|[CIA]R:[XLMH]|MAV:[XNALP]|MAC:[XLH]|MPR:[XNLH]|MUI:[XNR]|MS:[XUC]|M[CIA]:[XNLH])/)*(AV:[NALP]|AC:[LH]|PR:[NLH]|UI:[NR]|S:[UC]|[CIA]:[NLH]|E:[XUPFH]|RL:[XOTWU]|RC:[XURC]|[CIA]R:[XLMH]|MAV:[XNALP]|MAC:[XLH]|MPR:[XNLH]|MUI:[XNR]|MS:[XUC]|M[CIA]:[XNLH])$"}}}}
```

Accepts only the prefixes `CVSS:3.0/` and `CVSS:3.1/`, where the prose row allows any version from 3.0 up to but excluding 4.0. Metrics in any order, repeats allowed, base vector not required (D-9).

**N-0343.** `/$defs/severity/items/allOf/2` / schema L532-547 · `allOf` item (`if`/`then`) · `[none]` · req: R-0234

```json
{"if": {"properties": {"type": {"const": "CVSS_V4"}}}, "then": {"properties": {"score": {"pattern": "^CVSS:4[.]0/AV:[NALP]/AC:[LH]/AT:[NP]/PR:[NLH]/UI:[NPA]/VC:[HLN]/VI:[HLN]/VA:[HLN]/SC:[HLN]/SI:[HLN]/SA:[HLN](/E:[XAPU])?(/CR:[XHML])?(/IR:[XHML])?(/AR:[XHML])?(/MAV:[XNALP])?(/MAC:[XLH])?(/MAT:[XNP])?(/MPR:[XNLH])?(/MUI:[XNPA])?(/MVC:[XNLH])?(/MVI:[XNLH])?(/MVA:[XNLH])?(/MSC:[XNLH])?(/MSI:[XNLHS])?(/MSA:[XNLHS])?(/S:[XNP])?(/AU:[XNY])?(/R:[XAUI])?(/V:[XDC])?(/RE:[XLMH])?(/U:(X|Clear|Green|Amber|Red))?$"}}}}
```

Accepts only `CVSS:4.0/`, where the prose row allows any version from 4.0 up to but excluding 5.0. Requires the eleven base metrics in order (D-9).

**N-0344.** `/$defs/severity/items/allOf/3` / schema L548-569 · `allOf` item (`if`/`then`) · `[none]` · req: R-0235

```json
{"if": {"properties": {"type": {"const": "Ubuntu"}}}, "then": {"properties": {"score": {"enum": ["negligible", "low", "medium", "high", "critical"]}}}}
```

Closes a set the prose row leaves open: it describes only a lowercased string for the Ubuntu priority (D-8).

**N-0345.** `/$defs/severity/items/required` / schema L571-574 · `required` · `[none]` · req: R-0051

```json
["type", "score"]
```

Prose: N-0113. The proto marks neither field Required.

**N-0346.** `/$defs/timestamp/format` / schema L579 · `format` · `[none]` · req: R-0022, R-0028, R-0029

```json
"date-time"
```

Used by `modified`, `published`, `withdrawn`. Annotation only unless format assertion is enabled (D-15).

**N-0347.** `/$defs/timestamp/pattern` / schema L580 · `pattern` · `[none]` · req: R-0236

```json
"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}(\\.[0-9]+)?Z"
```

No `^` or `$` anchor, so it matches anywhere inside the string; requires uppercase `T` and `Z` (D-15).

**N-0348.** `/additionalProperties` / schema L583 · `additionalProperties` · `[none]` · req: R-0237

```json
false
```

Top level only; nested objects accept unknown keys. Compare N-0014 and N-0009 (D-14).

### Keyword index

Every occurrence of the validation keywords `required`, `enum`, `const`, `pattern`, `format`, `minItems`, `contains`, `oneOf`, `allOf`, `if`, `then`, `not`, `additionalProperties` in document order, with the statement that carries it. Counts: `required` 19, `enum` 7, `const` 6, `pattern` 11, `format` 2, `minItems` 1, `contains` 3, `oneOf` 2, `allOf` 3, `if` 8, `then` 8, `not` 1, `additionalProperties` 1; 72 in all. Values are in the statements above.

| JSON Pointer | schema line | keyword | statement |
|---|---|---|---|
| `/properties/affected/items/properties/package/required` | L74 | `required` | N-0318 |
| `/properties/affected/items/properties/ranges/items/properties/type/enum` | L89 | `enum` | N-0319 |
| `/properties/affected/items/properties/ranges/items/properties/events/contains` | L101 | `contains` | N-0321 |
| `/properties/affected/items/properties/ranges/items/properties/events/contains/required` | L102 | `required` | N-0321 |
| `/properties/affected/items/properties/ranges/items/properties/events/items/oneOf` | L108 | `oneOf` | N-0322 |
| `/properties/affected/items/properties/ranges/items/properties/events/items/oneOf/0/required` | L116 | `required` | N-0322 |
| `/properties/affected/items/properties/ranges/items/properties/events/items/oneOf/1/required` | L127 | `required` | N-0322 |
| `/properties/affected/items/properties/ranges/items/properties/events/items/oneOf/2/required` | L138 | `required` | N-0322 |
| `/properties/affected/items/properties/ranges/items/properties/events/items/oneOf/3/required` | L149 | `required` | N-0322 |
| `/properties/affected/items/properties/ranges/items/properties/events/minItems` | L155 | `minItems` | N-0323 |
| `/properties/affected/items/properties/ranges/items/allOf` | L161 | `allOf` | N-0324, N-0325, N-0326 |
| `/properties/affected/items/properties/ranges/items/allOf/0/if` | L164 | `if` | N-0324 |
| `/properties/affected/items/properties/ranges/items/allOf/0/if/properties/type/const` | L167 | `const` | N-0324 |
| `/properties/affected/items/properties/ranges/items/allOf/0/then` | L171 | `then` | N-0324 |
| `/properties/affected/items/properties/ranges/items/allOf/0/then/required` | L172 | `required` | N-0324 |
| `/properties/affected/items/properties/ranges/items/allOf/1/if` | L179 | `if` | N-0325 |
| `/properties/affected/items/properties/ranges/items/allOf/1/if/properties/type/const` | L182 | `const` | N-0325 |
| `/properties/affected/items/properties/ranges/items/allOf/1/then` | L186 | `then` | N-0325 |
| `/properties/affected/items/properties/ranges/items/allOf/1/then/properties/events/items/oneOf` | L190 | `oneOf` | N-0325 |
| `/properties/affected/items/properties/ranges/items/allOf/1/then/properties/events/items/oneOf/0/properties/introduced/pattern` | L196 | `pattern` | N-0325 |
| `/properties/affected/items/properties/ranges/items/allOf/1/then/properties/events/items/oneOf/0/required` | L199 | `required` | N-0325 |
| `/properties/affected/items/properties/ranges/items/allOf/1/then/properties/events/items/oneOf/1/properties/fixed/pattern` | L208 | `pattern` | N-0325 |
| `/properties/affected/items/properties/ranges/items/allOf/1/then/properties/events/items/oneOf/1/required` | L211 | `required` | N-0325 |
| `/properties/affected/items/properties/ranges/items/allOf/1/then/properties/events/items/oneOf/2/properties/last_affected/pattern` | L220 | `pattern` | N-0325 |
| `/properties/affected/items/properties/ranges/items/allOf/1/then/properties/events/items/oneOf/2/required` | L223 | `required` | N-0325 |
| `/properties/affected/items/properties/ranges/items/allOf/1/then/properties/events/items/oneOf/3/properties/limit/pattern` | L232 | `pattern` | N-0325 |
| `/properties/affected/items/properties/ranges/items/allOf/1/then/properties/events/items/oneOf/3/required` | L235 | `required` | N-0325 |
| `/properties/affected/items/properties/ranges/items/allOf/2/if` | L247 | `if` | N-0326 |
| `/properties/affected/items/properties/ranges/items/allOf/2/if/properties/events/contains` | L250 | `contains` | N-0326 |
| `/properties/affected/items/properties/ranges/items/allOf/2/if/properties/events/contains/required` | L251 | `required` | N-0326 |
| `/properties/affected/items/properties/ranges/items/allOf/2/then` | L258 | `then` | N-0326 |
| `/properties/affected/items/properties/ranges/items/allOf/2/then/not` | L259 | `not` | N-0326 |
| `/properties/affected/items/properties/ranges/items/allOf/2/then/not/properties/events/contains` | L262 | `contains` | N-0326 |
| `/properties/affected/items/properties/ranges/items/allOf/2/then/not/properties/events/contains/required` | L263 | `required` | N-0326 |
| `/properties/affected/items/properties/ranges/items/required` | L273 | `required` | N-0327 |
| `/properties/references/items/properties/type/enum` | L304 | `enum` | N-0328 |
| `/properties/references/items/properties/url/format` | L320 | `format` | N-0329 |
| `/properties/references/items/required` | L323 | `required` | N-0330 |
| `/properties/credits/items/properties/type/enum` | L345 | `enum` | N-0331 |
| `/properties/credits/items/required` | L359 | `required` | N-0332 |
| `/required` | L368 | `required` | N-0333 |
| `/allOf` | L372 | `allOf` | N-0334 |
| `/allOf/0/if` | L374 | `if` | N-0334 |
| `/allOf/0/if/required` | L375 | `required` | N-0334 |
| `/allOf/0/then` | L379 | `then` | N-0334 |
| `/$defs/ecosystemName/enum` | L399 | `enum` | N-0335 |
| `/$defs/ecosystemSuffix/pattern` | L456 | `pattern` | N-0336 |
| `/$defs/ecosystemWithSuffix/pattern` | L462 | `pattern` | N-0337 |
| `/$defs/prefix/pattern` | L468 | `pattern` | N-0338 |
| `/$defs/severity/items/properties/type/enum` | L480 | `enum` | N-0339 |
| `/$defs/severity/items/properties/source/enum` | L492 | `enum` | N-0340 |
| `/$defs/severity/items/allOf` | L499 | `allOf` | N-0341, N-0342, N-0343, N-0344 |
| `/$defs/severity/items/allOf/0/if` | L501 | `if` | N-0341 |
| `/$defs/severity/items/allOf/0/if/properties/type/const` | L504 | `const` | N-0341 |
| `/$defs/severity/items/allOf/0/then` | L508 | `then` | N-0341 |
| `/$defs/severity/items/allOf/0/then/properties/score/pattern` | L511 | `pattern` | N-0341 |
| `/$defs/severity/items/allOf/1/if` | L517 | `if` | N-0342 |
| `/$defs/severity/items/allOf/1/if/properties/type/const` | L520 | `const` | N-0342 |
| `/$defs/severity/items/allOf/1/then` | L524 | `then` | N-0342 |
| `/$defs/severity/items/allOf/1/then/properties/score/pattern` | L527 | `pattern` | N-0342 |
| `/$defs/severity/items/allOf/2/if` | L533 | `if` | N-0343 |
| `/$defs/severity/items/allOf/2/if/properties/type/const` | L536 | `const` | N-0343 |
| `/$defs/severity/items/allOf/2/then` | L540 | `then` | N-0343 |
| `/$defs/severity/items/allOf/2/then/properties/score/pattern` | L543 | `pattern` | N-0343 |
| `/$defs/severity/items/allOf/3/if` | L549 | `if` | N-0344 |
| `/$defs/severity/items/allOf/3/if/properties/type/const` | L552 | `const` | N-0344 |
| `/$defs/severity/items/allOf/3/then` | L556 | `then` | N-0344 |
| `/$defs/severity/items/allOf/3/then/properties/score/enum` | L559 | `enum` | N-0344 |
| `/$defs/severity/items/required` | L571 | `required` | N-0345 |
| `/$defs/timestamp/format` | L579 | `format` | N-0346 |
| `/$defs/timestamp/pattern` | L580 | `pattern` | N-0347 |
| `/additionalProperties` | L583 | `additionalProperties` | N-0348 |

### `type` keywords by value

`type` is also a validation constraint; its 64 occurrences, grouped by value. Property types are carried field by field in the messages artifact, so they are not numbered here; the nullable ones are discussed in D-11.

| value | count | JSON Pointers (schema line) |
|---|---|---|
| `"string"` | 32 | `/properties/schema_version/type` (9), `/properties/aliases/items/type` (29), `/properties/related/items/type` (35), `/properties/upstream/items/type` (41), `/properties/summary/type` (45), `/properties/details/type` (48), `/properties/affected/items/properties/package/properties/name/type` (68), `/properties/affected/items/properties/package/properties/purl/type` (71), `/properties/affected/items/properties/ranges/items/properties/type/type` (88), `/properties/affected/items/properties/ranges/items/properties/repo/type` (96), `/properties/affected/items/properties/ranges/items/properties/events/items/oneOf/0/properties/introduced/type` (113), `/properties/affected/items/properties/ranges/items/properties/events/items/oneOf/1/properties/fixed/type` (124), `/properties/affected/items/properties/ranges/items/properties/events/items/oneOf/2/properties/last_affected/type` (135), `/properties/affected/items/properties/ranges/items/properties/events/items/oneOf/3/properties/limit/type` (146), `/properties/affected/items/properties/ranges/items/allOf/1/then/properties/events/items/oneOf/0/properties/introduced/type` (195), `/properties/affected/items/properties/ranges/items/allOf/1/then/properties/events/items/oneOf/1/properties/fixed/type` (207), `/properties/affected/items/properties/ranges/items/allOf/1/then/properties/events/items/oneOf/2/properties/last_affected/type` (219), `/properties/affected/items/properties/ranges/items/allOf/1/then/properties/events/items/oneOf/3/properties/limit/type` (231), `/properties/affected/items/properties/versions/items/type` (282), `/properties/references/items/properties/type/type` (303), `/properties/references/items/properties/url/type` (319), `/properties/credits/items/properties/name/type` (335), `/properties/credits/items/properties/contact/items/type` (340), `/properties/credits/items/properties/type/type` (344), `/$defs/ecosystemName/type` (396), `/$defs/ecosystemSuffix/type` (455), `/$defs/ecosystemWithSuffix/type` (459), `/$defs/prefix/type` (465), `/$defs/severity/items/properties/type/type` (479), `/$defs/severity/items/properties/score/type` (488), `/$defs/severity/items/properties/source/type` (491), `/$defs/timestamp/type` (578) |
| `"object"` | 20 | `/type` (6), `/properties/affected/items/type` (59), `/properties/affected/items/properties/package/type` (62), `/properties/affected/items/properties/ranges/items/type` (85), `/properties/affected/items/properties/ranges/items/properties/events/items/type` (107), `/properties/affected/items/properties/ranges/items/properties/events/items/oneOf/0/type` (110), `/properties/affected/items/properties/ranges/items/properties/events/items/oneOf/1/type` (121), `/properties/affected/items/properties/ranges/items/properties/events/items/oneOf/2/type` (132), `/properties/affected/items/properties/ranges/items/properties/events/items/oneOf/3/type` (143), `/properties/affected/items/properties/ranges/items/properties/database_specific/type` (158), `/properties/affected/items/properties/ranges/items/allOf/1/then/properties/events/items/oneOf/0/type` (192), `/properties/affected/items/properties/ranges/items/allOf/1/then/properties/events/items/oneOf/1/type` (204), `/properties/affected/items/properties/ranges/items/allOf/1/then/properties/events/items/oneOf/2/type` (216), `/properties/affected/items/properties/ranges/items/allOf/1/then/properties/events/items/oneOf/3/type` (228), `/properties/affected/items/properties/ecosystem_specific/type` (286), `/properties/affected/items/properties/database_specific/type` (289), `/properties/references/items/type` (300), `/properties/credits/items/type` (332), `/properties/database_specific/type` (365), `/$defs/severity/items/type` (476) |
| `"array"` | 7 | `/properties/related/type` (33), `/properties/upstream/type` (39), `/properties/affected/items/properties/ranges/type` (83), `/properties/affected/items/properties/ranges/items/properties/events/type` (100), `/properties/affected/items/properties/versions/type` (280), `/properties/credits/type` (330), `/properties/credits/items/properties/contact/type` (338) |
| `["array", "null"]` | 4 | `/properties/aliases/type` (24), `/properties/affected/type` (54), `/properties/references/type` (295), `/$defs/severity/type` (471) |
| `"null"` | 1 | `/allOf/0/then/properties/affected/items/properties/severity/type` (385) |

### `$ref` bindings

| JSON Pointer | schema line | refers to |
|---|---|---|
| `/properties/id/$ref` | L12 | `#/$defs/prefix` |
| `/properties/modified/$ref` | L15 | `#/$defs/timestamp` |
| `/properties/published/$ref` | L18 | `#/$defs/timestamp` |
| `/properties/withdrawn/$ref` | L21 | `#/$defs/timestamp` |
| `/properties/severity/$ref` | L51 | `#/$defs/severity` |
| `/properties/affected/items/properties/package/properties/ecosystem/$ref` | L65 | `#/$defs/ecosystemWithSuffix` |
| `/properties/affected/items/properties/severity/$ref` | L80 | `#/$defs/severity` |

## Protocol Buffers definition: proto/vulnerability.proto

proto3, package `osv`. The file says of itself that the protobuf
representation is not stable and serves the JSON API (N-0373).
proto3 has no required fields, so "Required." and "Optional." are comments,
not enforced rules. Numbered here are the parts that add to or differ from the
prose and the JSON Schema: every comment that marks a field Required or
Optional or states another rule, every enumeration, the `Event` message (which
differs in structure) and the deprecated `Commit` message. Each statement says
whether it agrees with, adds to or differs from the prose and the JSON Schema.
Field numbers and the Go package option are wire and build details and are not
extracted. Lines are quoted verbatim, comment markers and indentation included.

**N-0349.** `Commit` / proto L24-53 · message (deprecated) · `[may, required, required, can, required, may]` · adds · req: none: proto, not extracted (requirements.yaml source_files); no counterpart in the prose (D-23)

> ```proto
> // Commit reference (DEPRECATED).
> //
> // In some rare cases, this may refer to a small range of commits rather than an
> // exact commit (to accommodate for automated systems). In such cases, the
> // semantics are as follows:
> //
> // - If this is referring to a commit which introduces a vulnerability, then
> // *any* commits in the range is assumed to cause the vulnerability.
> //
> // - If this is referring to a commit which fixes a vulnerability, then *all*
> // commits in the range is assumed to cause the vulnerability.
> message Commit {
>   option deprecated = true;
>   // The repository type.
>   enum RepoType {
>     UNSPECIFIED = 0;
>     GIT = 1;
>   }
>
>   // Required. The type of the repo.
>   RepoType repo_type = 1;
>   // Required. The publicly accessible URL of the repo that can be directly
>   // passed to clone commands.
>   string repo_url = 2;
>   // Required. The commit identifier (e.g. git SHA). In some cases where the
>   // exact commit fails to be determined by automation, this may be a small
>   // range in the form "A:B" which means the commit range from A (exclusive) to
>   // B (inclusive).
>   string commit = 3;
> }
> ```

Deprecated, and no other message has a `Commit` field, so it never appears in a record. No counterpart in the prose or the JSON Schema (D-23). `repo_type` and `repo_url` have no `json_name`, so proto3 JSON would spell them `repoType` and `repoUrl`.

**N-0350.** `Package.name` / proto L57-60 · field comment · `[required, should]` · adds · req: none: proto, not extracted (requirements.yaml source_files); prose counterpart R-0073, R-0075

> ```proto
>   // Required. Name of the package. Should match the name used in the package
>   // ecosystem (e.g. the npm package name). For C/C++ projects integrated in
>   // OSS-Fuzz, this is the name used for the integration.
>   string name = 1;
> ```

Required agrees with N-0137. "Should match the name used in the package ecosystem" has no prose counterpart outside the ecosystem table.

**N-0351.** `Package.ecosystem` / proto L61-64 · field comment · `[required]` · agrees · req: none: proto, not extracted (requirements.yaml source_files); prose counterpart R-0073, R-0074

> ```proto
>   // Required. The ecosystem for this package.
>   // For the complete list of valid ecosystem names, see
>   // <https://ossf.github.io/osv-schema/#affectedpackage-field>.
>   string ecosystem = 2;
> ```

Prose: N-0137, N-0139.

**N-0352.** `Package.purl` / proto L65-66 · field comment · `[optional]` · agrees · req: none: proto, not extracted (requirements.yaml source_files); prose counterpart R-0073, R-0079

> ```proto
>   // Optional. The package URL for this package.
>   string purl = 3;
> ```

Prose: N-0137, N-0144.

**N-0353.** `Event` / proto L69-80 · message · `[none]` · differs · req: none: proto, not extracted (requirements.yaml source_files); prose counterpart R-0181

> ```proto
> // Version events.
> message Event {
>   // The earliest version/commit where this vulnerability
>   // was introduced in.
>   string introduced = 1;
>   // The version/commit that this vulnerability was fixed in.
>   string fixed = 2;
>   // The limit to apply to the range.
>   string limit = 3;
>   // The last affected version.
>   string last_affected = 4 [json_name="last_affected"];
> }
> ```

Four plain `string` fields and no `oneof`, so one `Event` can carry several of them, which N-0242 forbids; proto3 also cannot tell an absent string from an empty one (D-13).

**N-0354.** `Range.Type` / proto L84-90 · enum · `[none]` · agrees · req: none: proto, not extracted (requirements.yaml source_files); prose counterpart R-0163, R-0226

> ```proto
>   // Type of the version information.
>   enum Type {
>     UNSPECIFIED = 0;
>     GIT = 1;
>     SEMVER = 2;
>     ECOSYSTEM = 3;
>   }
> ```

Same three values as the prose (N-0220) and the JSON Schema (N-0319), plus `UNSPECIFIED = 0` (D-22).

**N-0355.** `Range.type` / proto L91-92 · field comment · `[required]` · agrees · req: none: proto, not extracted (requirements.yaml source_files); prose counterpart R-0161

> ```proto
>   // Required. The type of version information.
>   Type type = 1;
> ```

Prose: N-0218.

**N-0356.** `Range.repo` / proto L93-95 · field comment · `[required, can]` · agrees · req: none: proto, not extracted (requirements.yaml source_files); prose counterpart R-0192, R-0194

> ```proto
>   // Required if type is GIT. The publicly accessible URL of the repo that can
>   // be directly passed to clone commands.
>   string repo = 2;
> ```

Prose: N-0259, N-0256; adds "publicly accessible".

**N-0357.** `Range.events` / proto L96-97 · field comment · `[required]` · agrees · req: none: proto, not extracted (requirements.yaml source_files); prose counterpart R-0189

> ```proto
>   // Required. Version event information.
>   repeated Event events = 3;
> ```

JSON Schema: N-0327.

**N-0358.** `Range.database_specific` / proto L98-100 · field comment · `[optional]` · differs · req: none: proto, not extracted (requirements.yaml source_files); prose counterpart R-0195

> ```proto
>   // Optional. JSON object holding additional information about the
>   // vulnerability as defined by the database for which the record applies.
>   google.protobuf.Struct database_specific = 4 [json_name="database_specific"];
> ```

The prose (N-0260) says the object holds information "about the range" from the database "from which the record was obtained"; this comment says "about the vulnerability" and "for which the record applies" (D-20).

**N-0359.** `Affected.package` / proto L105-106 · field comment · `[optional]` · adds · req: none: proto, not extracted (requirements.yaml source_files); prose counterpart R-0148

> ```proto
>   // Optional. Package information.
>   Package package = 1;
> ```

The prose never says outright that `package` is optional; N-0205 implies it, and the JSON Schema does not require it (D-17).

**N-0360.** `Affected.ranges` / proto L107-108 · field comment · `[required]` · differs · req: none: proto, not extracted (requirements.yaml source_files); prose counterpart R-0160

> ```proto
>   // Required. Range information.
>   repeated Range ranges = 2;
> ```

Neither the prose nor the JSON Schema requires `ranges` (D-12).

**N-0361.** `Affected.versions` / proto L109-110 · field comment · `[optional]` · differs · req: none: proto, not extracted (requirements.yaml source_files); prose counterpart R-0069, R-0071, R-0173

> ```proto
>   // Optional. List of affected versions.
>   repeated string versions = 3;
> ```

Agrees with the JSON Schema; the prose requires `versions` in some cases (N-0135, N-0232) (D-16).

**N-0362.** `Affected.ecosystem_specific` / proto L111-113 · field comment · `[optional]` · agrees · req: none: proto, not extracted (requirements.yaml source_files); prose counterpart R-0198

> ```proto
>   // Optional. JSON object holding additional information about the
>   // vulnerability as defined by the ecosystem for which the record applies.
>   google.protobuf.Struct ecosystem_specific = 4 [json_name="ecosystem_specific"];
> ```

Prose: N-0264.

**N-0363.** `Affected.database_specific` / proto L114-116 · field comment · `[optional]` · agrees · req: none: proto, not extracted (requirements.yaml source_files); prose counterpart R-0199

> ```proto
>   // Optional. JSON object holding additional information about the
>   // vulnerability as defined by the database for which the record applies.
>   google.protobuf.Struct database_specific = 5 [json_name="database_specific"];
> ```

Prose (N-0267) says "from which the record was obtained"; this comment says "for which the record applies".

**N-0364.** `Affected.severity` / proto L117-118 · field comment · `[optional]` · agrees · req: none: proto, not extracted (requirements.yaml source_files); prose counterpart R-0152

> ```proto
>   // Optional. Severity of the vulnerability for this package.
>   repeated Severity severity = 6;
> ```

Prose: N-0209.

**N-0365.** `Severity.Type` / proto L122-129 · enum · `[none]` · agrees · req: none: proto, not extracted (requirements.yaml source_files); prose counterpart R-0052

> ```proto
>   // Type of the severity.
>   enum Type {
>     UNSPECIFIED = 0;
>     CVSS_V3 = 1;
>     CVSS_V2 = 2;
>     CVSS_V4 = 3;
>     Ubuntu = 4;
>   }
> ```

Same four values as the prose and the JSON Schema (N-0339), plus `UNSPECIFIED = 0` (D-22).

**N-0366.** `Severity.Source` / proto L130-136 · enum · `[none]` · agrees · req: none: proto, not extracted (requirements.yaml source_files); prose counterpart R-0231

> ```proto
>   // Source of the severity.
>   enum Source {
>     SOURCE_UNSPECIFIED = 0;
>     NVD = 1;
>     CNA = 2;
>     SELF = 3;
>   }
> ```

Same three values as the prose table and the JSON Schema (N-0340), plus `SOURCE_UNSPECIFIED = 0` (D-22).

**N-0367.** `Severity.source` / proto L141-142 · field comment · `[optional]` · agrees · req: none: proto, not extracted (requirements.yaml source_files); prose counterpart R-0058

> ```proto
>   // Optional. The source of this severity assessment.
>   Source source = 3;
> ```

Prose: N-0120.

**N-0368.** `Credit.Type` / proto L151-163 · enum · `[none]` · agrees · req: none: proto, not extracted (requirements.yaml source_files); prose counterpart R-0220

> ```proto
>   enum Type {
>     UNSPECIFIED = 0;
>     OTHER = 1;
>     FINDER = 2;
>     REPORTER = 3;
>     ANALYST = 4;
>     COORDINATOR = 5;
>     REMEDIATION_DEVELOPER = 6;
>     REMEDIATION_REVIEWER = 7;
>     REMEDIATION_VERIFIER = 8;
>     TOOL = 9;
>     SPONSOR = 10;
>   }
> ```

Same ten values as the prose and the JSON Schema (N-0331), plus `UNSPECIFIED = 0` (D-22).

**N-0369.** `Credit.type` / proto L164-165 · field comment · `[optional]` · agrees · req: none: proto, not extracted (requirements.yaml source_files); prose counterpart R-0219

> ```proto
>   // Optional. The type or role of the individual or entity being credited.
>   Type type = 3;
> ```

Prose: N-0300.

**N-0370.** `Reference.Type` / proto L170-184 · enum · `[none]` · differs · req: none: proto, not extracted (requirements.yaml source_files); prose counterpart R-0209, R-0228

> ```proto
>   enum Type {
>     // Next ID = 12.
>     NONE = 0;
>     ADVISORY = 2;
>     ARTICLE = 6;
>     DETECTION = 9;
>     DISCUSSION = 8;
>     EVIDENCE = 7;
>     FIX = 4;
>     GIT = 11;
>     INTRODUCED = 10;
>     PACKAGE = 5;
>     REPORT = 3;
>     WEB = 1;
>   }
> ```

Has `GIT = 11`, which the JSON Schema has (N-0328) and the prose list does not (D-6); plus `NONE = 0` (D-22).

**N-0371.** `Reference.type` / proto L186-187 · field comment · `[required]` · agrees · req: none: proto, not extracted (requirements.yaml source_files); prose counterpart R-0206

> ```proto
>   // Required. The type of the reference.
>   Type type = 1;
> ```

JSON Schema: N-0330.

**N-0372.** `Reference.url` / proto L188-189 · field comment · `[required]` · agrees · req: none: proto, not extracted (requirements.yaml source_files); prose counterpart R-0206

> ```proto
>   // Required. The URL.
>   string url = 2;
> ```

JSON Schema: N-0330.

**N-0373.** `Vulnerability` / proto L192-195 · message comment · `[only]` · adds · req: none: proto, not extracted; this is the sentence requirements.yaml gives as the reason

> ```proto
> // A vulnerability entry.
> // The protobuf representation is *NOT* stable and only used for implementing
> // the JSON based API.
> message Vulnerability {
> ```

Sets the weight of this file: the protobuf form is an implementation aid for the API, not a definition of the format (D-24).

**N-0374.** `Vulnerability.withdrawn` / proto L207-209 · field comment · `[optional]` · agrees · req: none: proto, not extracted (requirements.yaml source_files); prose counterpart R-0029

> ```proto
>   // Optional. The RFC3339 timestamp indicating when this entry is considered to
>   // be withdrawn.
>   google.protobuf.Timestamp withdrawn = 12;
> ```

Prose: N-0084.

**N-0375.** `Vulnerability.aliases` / proto L210-211 · field comment · `[optional]` · agrees · req: none: proto, not extracted (requirements.yaml source_files); prose counterpart R-0032

> ```proto
>   // Optional. IDs for the same vulnerability in other databases.
>   repeated string aliases = 8;
> ```

Prose: N-0088.

**N-0376.** `Vulnerability.related` / proto L212-214 · field comment · `[optional]` · differs · req: none: proto, not extracted (requirements.yaml source_files); prose counterpart R-0041

> ```proto
>   // Optional. List of IDs of closely related vulnerabilities, such as the same
>   // problem in alternate ecosystems.
>   repeated string related = 13;
> ```

"the same problem in alternate ecosystems" reads like the prose definition of an alias (N-0088), not of `related` (N-0101) (D-18).

**N-0377.** `Vulnerability.upstream` / proto L215-216 · field comment · `[optional]` · agrees · req: none: proto, not extracted (requirements.yaml source_files); prose counterpart R-0038

> ```proto
>   // Optional. List of IDs of upstream vulnerabilities of a vulnerability.
>   repeated string upstream = 14;
> ```

Prose: N-0097.

**N-0378.** `Vulnerability.summary` / proto L217-219 · field comment · `[required, recommended]` · differs · req: none: proto, not extracted (requirements.yaml source_files); prose counterpart R-0027, R-0044

> ```proto
>   // Required. One line human readable summary for the vulnerability. It is
>   // recommended to keep this under 120 characters.
>   string summary = 3;
> ```

Required, where the prose makes every field but `id`, `modified` and `schema_version` optional (N-0080) (D-12); "under 120 characters" against "on the order of no more than 120 characters" (N-0105) (D-19).

**N-0379.** `Vulnerability.details` / proto L220-221 · field comment · `[required]` · differs · req: none: proto, not extracted (requirements.yaml source_files); prose counterpart R-0027

> ```proto
>   // Required. Any additional human readable details for the vulnerability.
>   string details = 4;
> ```

Required (D-12).

**N-0380.** `Vulnerability.affected` / proto L222-223 · field comment · `[required]` · differs · req: none: proto, not extracted (requirements.yaml source_files); prose counterpart R-0027

> ```proto
>   // Required. Affected commit ranges and versions.
>   repeated Affected affected = 17;
> ```

Required (D-12).

**N-0381.** `Vulnerability.references` / proto L224-226 · field comment · `[optional]` · agrees · req: none: proto, not extracted (requirements.yaml source_files); prose counterpart R-0205, R-0207

> ```proto
>   // Optional. URLs to more information/advisories (including the
>   // scheme e.g. "https://").
>   repeated Reference references = 16;
> ```

Prose: N-0279.

**N-0382.** `Vulnerability.database_specific` / proto L227-229 · field comment · `[optional]` · agrees · req: none: proto, not extracted (requirements.yaml source_files); prose counterpart R-0222

> ```proto
>   // Optional. JSON object holding additional information about the
>   // vulnerability as defined by the database for which the record applies.
>   google.protobuf.Struct database_specific = 15 [json_name="database_specific"];
> ```

Prose (N-0313) says "from which the record was obtained"; this comment says "for which the record applies".

**N-0383.** `Vulnerability.severity` / proto L230-231 · field comment · `[optional]` · agrees · req: none: proto, not extracted (requirements.yaml source_files); prose counterpart R-0050

> ```proto
>   // Optional. Severity of the vulnerability.
>   repeated Severity severity = 19;
> ```

Prose: N-0112.

**N-0384.** `Vulnerability.credits` / proto L232-233 · field comment · `[optional]` · agrees · req: none: proto, not extracted (requirements.yaml source_files); prose counterpart R-0212

> ```proto
>   // Optional. Credits for the vulnerability.
>   repeated Credit credits = 20;
> ```

Prose: N-0293.

Proto lines outside the numbered statements:

- proto L1-13: licence header (Apache License 2.0); reproduced under Licence below. Its "required", "may not" and "may" are licence text.
- proto L15-22: syntax, package, imports and `go_package` option.
- proto L55-56: message `Package` comment and opening line.
- proto L67: closing brace.
- proto L82-83: message `Range` comment and opening line.
- proto L101: closing brace.
- proto L103-104: message `Affected` comment and opening line.
- proto L119-121: closing brace; message `Severity` opening line.
- proto L137-140: `Severity.type` and `Severity.score`: comments without a rule marker (see the field comparison table).
- proto L143: closing brace.
- proto L145-150: message `Credit`: `name` and `contact` comments without a rule marker (see the field comparison table).
- proto L166-169: closing brace; message `Reference` comment and opening line.
- proto L190: closing brace.
- proto L196-206: `schema_version`, `id`, `published`, `modified`: comments without a rule marker (see the field comparison table).
- proto L234: closing brace.

## Informative content excluded

75 passages (X-001 to X-075), each assessed and listed with its reason, and quoted where it is prose. Together with the statements and the structural lines named in Conventions they cover every non-blank character of docs/schema.md; this was checked mechanically when the file was generated.

### Front matter

Not specification text.

**X-001.** § front matter / L1-9: YAML front matter; Jekyll page metadata (layout, title, description, permalink, table-of-contents switch); publishing configuration, not specification text.

**X-002.** § front matter / L11: version line; document identification; recorded in this file's front matter as source_version.

**X-003.** § front matter / L13-15: original authors; authorship; not specification text.

### Purpose

Statements of scope, motivation, status and process; each was assessed, and none constrains a record, a producer or a consumer.

**X-004.** § Purpose / L19-20: scope statement: names what the document defines; no actor, no verbal form.

> This document defines a standard interchange format for describing vulnerabilities in open source packages.

**X-005.** § Purpose / L22-27: motivation. Forms: `[can]`.

> We hope to define a simple format that all vulnerability databases can export, to make it easier for users, security researchers, and any other efforts to consume all available databases. Use of this format would also make it easier for the databases themselves to share or cross-check information. Ultimately, this format aims to enable automated, accurate, and distributed management of vulnerabilities in open source dependencies.

**X-006.** § Purpose / L29: status of the specification itself; "may" is the possibility of future revisions and binds no producer or consumer (the forward-compatibility rule that does bind consumers is N-0014). Forms: `[may]`.

> This format is stable, but further backwards compatible changes may still be made.

**X-007.** § Purpose / L30-32: invitation to give feedback (process); "Please feel free" is an imperative addressed to readers.

> Feedback from maintainers of other vulnerability databases and security response teams is most welcome. Please feel free to create an [issue in this repo](https://github.com/ossf/osv-schema/issues/new).

### Examples inside normative sections

Sentences that begin "For example", "For instance" or "e.g." and add nothing the rule around them does not state, and the example blocks. Example sentences that carry their own verbal form or verdict are extracted instead (for example N-0094, N-0243).

**X-010.** § id, modified fields / L145-146: examples of ids.

> For example: "OSV-2020-111", "CVE-2021-3114", or "GHSA-vp9c-fpxx-744v".

**X-011.** § id, modified fields / L149-150: example of a local id.

> For example: "x_CUSTOM-0001".

**X-015.** § id, modified fields > Defined database prefixes / L712: example id.

> e.g. `DEBIAN-CVE-2000-0001`.

**X-018.** § upstream field / L791-793: example of a downstream advisory ("may" is possibility). Forms: `[may]`.

> For example, a downstream package ecosystem (such as a Linux distribution) may issue its own advisories that include (possibly multiple) upstream vulnerabilities.

**X-019.** § upstream field / L795-797: illustrates transitivity; adds nothing to the rule before it.

> For example, if B is an upstream vulnerability for A, and C is an upstream vulnerability for B, then C is also an upstream vulnerability for A.

**X-024.** § affected fields > affected[].package field / L960-962: example use case.

> For example, this is useful when an ecosystem version reaches end-of-life (EOL) and receives no further security support.

**X-025.** § affected fields > affected[].package field / L970-971: lead-in to the two example objects.

> For example, these denote different libraries with different sets of versions and different potential vulnerabilities:

**X-026.** § affected fields > affected[].package field / L973-979: example blocks; two example `package` objects (`npm`/`zlib` and `PyPI`/`zlib`).

**X-035.** § affected fields > affected[].ranges[].events fields / L1146-1147: examples of normalisation ("may" is possibility). Forms: `[may]`.

> For example, they may be normalized, or have build metadata stripped.

**X-039.** § affected fields > affected[].ecosystem_specific field / L1218-1220: example of one ecosystem's use.

> For example, the Go ecosystem includes here information about the affected functions and which modules the packages were found in, along with severity in the Go project-specific severity scale.

**X-040.** § affected fields > affected[].database_specific field / L1236-1237: example use ("could").

> For example, databases that add additional information such as computed CVSS scores for ecosystems that do not provide them could add that information here.

**X-063.** § credits fields > credits[].name field / L1481-1482: examples of names ("could").

> For instance, this could contain a real name like `Kovács János`, an Internet handle like `erikamustermann`, an entity name like `GitHub`, or something else.

**X-064.** § credits fields > credits[].type field > Examples / L1512: lead-in to the example.

> Including a URL and an email address in `credits[].contact[]` and a credit type:

**X-065.** § credits fields > credits[].type field > Examples / L1514-1525: example block; example `credits` array (JSON with a trailing comma, U-18).

### Rationale and context

Each states a reason or describes something without constraining it.

**X-009.** § schema_version field / L124-126: rationale ("can" is possibility). Forms: `[can]`.

> This can help consumer applications decide how to import the data for their own systems and offer some protection against future breaking changes.

**X-017.** § aliases field / L776-777: descriptive context for the next sentence; constrains nothing.

> Similarly, distributions often bundle multiple upstream vulnerabilities into a single record.

**X-020.** § summary, details fields / L835-837: rationale.

> (The goal is to balance flexibility of presentation with not exposing vulnerability database display sites to unnecessary vulnerabilities.)

**X-031.** § affected fields > Depicting multiple ecosystems in the same record > Separating Git and Strict Ecosystems / L1061: rationale.

> This separation ensures that tools relying on strict version parsing for a specific ecosystem do not get confused by Git commit hashes, and vice versa.

**X-062.** § affected fields > Examples > `last_affected` vs `fixed` example / L1413-1414: rationale. Forms: `[require]`.

> The use of `fixed` requires fewer assumptions and eliminates the possibilities for false negatives.

### Asides

**X-016.** § id, modified fields > modified field / L724: aside on what a minimal entry could mean ("could" is possibility).

> (It could potentially stand for a reserved ID with no other public information.)

### What one service does

Descriptions of osv.dev tooling; they constrain no record.

**X-023.** § affected fields / L943-945: describes what one service (osv.dev) does; constrains no record.

> Tooling and infrastructure such as https://osv.dev are able to expand these ranges for supported ecosystems into the `versions` list for easier consumption.

**X-032.** § affected fields > Depicting multiple ecosystems in the same record > Version Enumeration for Git Entries / L1065: describes what one service (osv.dev) can do; "can" is capability. Forms: `[can]`.

> OSV infrastructure (such as https://osv.dev) can automatically perform this enumeration during ingestion, populating the `versions` array with relevant tags that fall within the specified commit ranges.

**X-034.** § affected fields > affected[].ranges[].type field / L1118-1120: describes what one service (osv.dev) provides.

> The infrastructure and tooling provided by https://osv.dev also provides automation for auto-populating the `versions` list based on supported `ECOSYSTEM` ranges as part of the ingestion process.

### Navigation pointers

Sentences whose only content is a pointer to another part of this document; the target is extracted in its own place.

**X-008.** § Purpose / L34-35: pointer to the prefix table, extracted in its own place. Forms: `[can]`.

> The current list of databases exporting this format can be found [here](#id-modified-fields).

**X-022.** § affected fields / L934-935: pointer to the Evaluation section, extracted as N-0271.

> Pseudocode for evaluating if a given version is affected is available [here](#evaluation).

**X-033.** § affected fields > affected[].versions field / L1083: pointer to N-0202.

> See [Separating Git and Strict Ecosystems](#separating-git-and-strict-ecosystems) for more details.

**X-036.** § affected fields > affected[].ranges[].events fields > Requirements / L1170-1171: pointer to the worked example.

> An [example](#last_affected-vs-fixed-example) is available to illustrate the difference.

**X-037.** § affected fields > affected[].ranges[].events fields > Requirements / L1174-1175: pointer to the worked example.

> (See the [limit example](#limit-events) for details about how they differ.)

**X-038.** § affected fields > affected[].ranges[].events fields > Requirements / L1186: pointer to the worked examples.

> See [examples](#examples) for examples of how to describe affected ranges.

### HTML comments

Notes to the document's editors; not rendered on the published page.

**X-012.** § id, modified fields > Defined database prefixes / L176: HTML comment to editors; not rendered.

> <!-- Unfortunately, markdown tables are even worse than this to read/write -->

**X-013.** § id, modified fields > Defined database prefixes / L177: HTML comment to editors ("Please keep this list alphabetically sorted"); not rendered, and not followed (U-7).

> <!-- Please keep this list alphabetically sorted -->

**X-027.** § affected fields > affected[].package field > Defined ecosystems / L985: HTML comment to editors (generation instructions); not rendered.

> <!-- (re)generate this list using scripts/update-ecosystems.list.py after changing ecosystems.json -->

**X-028.** § affected fields > affected[].package field > Defined ecosystems / L986: HTML comment marking the start of the generated list; not rendered.

> <!-- begin auto-generated ecosystems list -->

**X-030.** § affected fields > affected[].package field > Defined ecosystems / L1044: HTML comment marking the end of the generated list; not rendered.

> <!-- end auto-generated ecosystems list -->

### Invitation rows

The last row of three tables invites new entries by pull request; it defines nothing.

**X-014.** § id, modified fields > Defined database prefixes / L705-708: table row "Your database here"; invitation row ("Your database here" / "Send us a PR"); process, not a prefix.

**X-021.** § severity field > severity[].type field / L867: table row "Your quantitative severity type here."; invitation row ("Your quantitative severity type here." / "Send us a PR"); process, not a type.

**X-029.** § affected fields > affected[].package field > Defined ecosystems / L1042: table row "Your ecosystem here."; invitation row ("Your ecosystem here." / "Send us a PR"); process, not an ecosystem.

### Worked examples under affected fields > Examples

Narrative about the example data and the example blocks. The general rules printed in this subsection are extracted (N-0272, N-0273, N-0274, N-0275).

**X-041.** § affected fields > Examples > Unfixed vulnerability example / L1296: worked example narrative.

> The following expresses that "every possible version is affected".

**X-042.** § affected fields > Examples > Unfixed vulnerability example / L1298-1305: example block; example range (JSON fragment with a trailing comma, U-18).

**X-043.** § affected fields > Examples > Fixed vulnerability example / L1308: worked example narrative.

> The following expresses that "everything before `1.0.2`" is affected.

**X-044.** § affected fields > Examples > Fixed vulnerability example / L1310-1318: example block; example range (JSON fragment with a trailing comma).

**X-045.** § affected fields > Examples > Multiple range example / L1321-1322: worked example narrative.

> The following expresses that versions in the SemVer ranges `[1.0.0, 1.0.2)` or `[3.0.0, 3.2.5)` are affected. Everything else is unaffected.

**X-046.** § affected fields > Examples > Multiple range example / L1324-1334: example block; example range (JSON fragment).

**X-047.** § affected fields > Examples > Limit events / L1338-1339: explanation.

> They are more useful for git ranges, where it has more implications for the evaluation algorithm.

**X-048.** § affected fields > Examples > Limit events / L1339-1340: lead-in to the example.

> Take the following git commit graph and git range:

**X-049.** § affected fields > Examples > Limit events / L1342: image; image `images/git_graph.png` (not part of the extracted source files).

**X-050.** § affected fields > Examples > Limit events / L1344-1353: example block; example GIT range with `fixed` (JSON fragment with a trailing comma).

**X-051.** § affected fields > Examples > Limit events / L1355-1356: worked example result (depends on the image).

> Without an explicit `limit`, the list of computed affected commits will be `X, A, B, C, D, E, F`.

**X-052.** § affected fields > Examples > Limit events / L1356: comment on the example.

> This is the desired behaviour in most cases.

**X-053.** § affected fields > Examples > Limit events / L1358-1367: example block; example GIT range with `limit` (JSON fragment with a trailing comma).

**X-054.** § affected fields > Examples > Limit events / L1369: worked example result (depends on the image).

> If `limit` is set to `Y`, the list of affected commits will be `X, A, B, C`.

**X-055.** § affected fields > Examples > Limit events / L1369-1370: worked example explanation in git terms.

> This is equivalent to `git rev-list X..Y` (but including `X` and excluding `Y`).

**X-056.** § affected fields > Examples > Limit events / L1375: comment on the example.

> Note that we did not specify a `fixed` event here as `limit` makes it redundant.

**X-057.** § affected fields > Examples > `last_affected` vs `fixed` example / L1378-1379: motivation ("may" is possibility). Forms: `[may]`.

> Understanding the difference between `last_affected` and `fixed` is essential to identifying where false negatives may occur.

**X-058.** § affected fields > Examples > `last_affected` vs `fixed` example / L1381-1385: worked example narrative.

> The following example expresses that the vulnerability is present in all versions of the package, up to and including version `2.1.214`. Versions above `2.1.214` are assumed to be free from the vulnerability, but there is a potential for a false negative. The `last_affected` field is typically assigned at the time of discovery and assumes the vulnerability will be addressed in the following version.

**X-059.** § affected fields > Examples > `last_affected` vs `fixed` example / L1387-1395: example block; example `last_affected` range (JSON fragment with a trailing comma).

**X-060.** § affected fields > Examples > `last_affected` vs `fixed` example / L1397-1401: worked example narrative.

> The following example looks similar, but there are differences in how it is interpreted. The vulnerability is present in all versions of the package up to version `2.1.214`. In this case `2.1.214` is not vulnerable. Versions `2.1.214` and above do not include the vulnerability and there isn't the possibility for false negatives that we see in the `last_affected` case.

**X-061.** § affected fields > Examples > `last_affected` vs `fixed` example / L1403-1411: example block; example `fixed` range (JSON fragment with a trailing comma).

### Example records under the Examples heading

Ten informative example records; the examples artifact carries them as fixtures.

**X-066.** § Go vulnerability / L1545-1547: Go vulnerability; statement that the Go database uses the format, with a pointer.

**X-067.** § NPM vulnerability in GitHub database / L1551-1629: NPM vulnerability in GitHub database; example record GHSA-r9p9-mrjm-926w and its lead-in.

**X-068.** § OSV vulnerability / L1633-1663: OSV vulnerability; example record OSV-2020-584 and its lead-in.

**X-069.** § Rust vulnerability / L1667-1705: Rust vulnerability; example record RUSTSEC-2019-0033 and its lead-in ("can" is in the record's `summary` text). Forms: `[can]`.

**X-070.** § Python vulnerability / L1709-1755: Python vulnerability; example record PYSEC-2021-XXXX and its lead-in.

**X-071.** § Debian vulnerability / L1759-1801: Debian vulnerability; example record DSA-3029-1 and its lead-in ("can" in the lead-in is possibility; "recommend" is in the record's `details` text). Forms: `[can, recommend]`.

**X-072.** § Ruby vulnerability / L1804-1841: Ruby vulnerability; example record CVE-2019-3881 and its lead-in.

**X-073.** § Haskell Hackage vulnerability / L1845-1887: Haskell Hackage vulnerability; example record HSEC-2023-0006.

**X-074.** § Haskell GHC vulnerability / L1890-1935: Haskell GHC vulnerability; hypothetical GHC record (a copy of the Hackage record with `ecosystem` and `name` changed) and its lead-in.

**X-075.** § R CRAN & Bioconductor vulnerability / L1939-1995: R CRAN & Bioconductor vulnerability; example record RSEC-2023-2 and its lead-in ("can" is in the record's `details` text). Forms: `[can]`.

## Verbal form tally

Counted mechanically over docs/schema.md with the rules under Conventions.
Regions are the source's own heading sections: each runs from its heading line
to the line before the next heading, and the front matter runs from L1 to L16,
so the rows partition the file. Each cell gives the total, or total
(included/excluded) when some occurrences sit in excluded passages; a blank
cell is 0. Column "required" includes "not required"; "recommended" includes
"recommend"; "optional" includes "optionally"; "other" holds allowed, not
allowed, permitted, invalid, encouraged, preferred, preferable and mandatory,
listed occurrence by occurrence below the table.

| region | lines | must | must not | should | should not | may | may not | can | cannot | might | required | recommended | optional | only | other |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| front matter | L1-16 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Purpose | L17-36 |  |  |  |  | 1 (0/1) |  | 2 (0/2) |  |  |  |  |  |  |  |
| Format Overview | L37-112 | 1 |  |  |  |  |  |  |  | 2 |  |  |  | 3 | 1 |
| Field Details | L113-114 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| schema_version field | L115-133 |  |  | 2 |  |  |  | 3 (2/1) |  |  |  |  |  | 1 |  |
| id, modified fields | L134-151 |  |  |  |  |  |  | 1 |  |  |  |  |  |  |  |
| id, modified fields > Character set constraints | L152-161 | 1 |  |  |  |  |  |  |  |  |  |  |  | 1 | 2 |
| id, modified fields > Semantically neutral ids | L162-171 |  | 1 | 3 |  |  |  |  |  |  |  |  |  |  |  |
| id, modified fields > Defined database prefixes | L172-713 |  |  | 1 |  |  |  |  |  |  |  |  |  | 1 |  |
| id, modified fields > modified field | L714-725 |  |  |  |  |  |  |  |  |  | 2 |  | 1 |  |  |
| published field | L726-736 |  |  | 1 |  |  |  |  |  |  |  |  |  |  |  |
| withdrawn field | L737-749 |  |  | 2 |  |  |  |  |  |  |  |  |  |  |  |
| aliases field | L750-779 |  | 1 | 2 | 1 |  |  | 1 |  |  |  |  |  |  |  |
| upstream field | L780-798 |  |  | 1 |  | 1 (0/1) |  |  | 1 |  |  |  |  |  |  |
| related field | L799-813 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| summary, details fields | L814-838 |  |  |  |  | 1 |  |  |  |  |  | 1 |  |  | 1 |
| severity field | L839-855 |  |  |  |  |  |  |  |  |  |  |  | 1 |  |  |
| severity field > severity[].type field | L856-868 | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| severity field > severity[].score field | L869-873 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| severity field > severity[].source field | L874-887 |  |  |  |  |  |  |  |  |  |  |  | 1 |  |  |
| affected fields | L888-947 | 1 |  | 1 |  | 2 |  | 4 |  |  |  | 1 |  |  |  |
| affected fields > affected[].package field | L948-980 | 2 |  |  |  |  |  | 1 |  |  | 1 | 1 | 2 |  |  |
| affected fields > affected[].package field > Defined ecosystems | L981-1049 | 4 |  | 2 |  | 2 |  | 5 |  | 8 | 1 |  | 10 | 2 | 2 |
| affected fields > Depicting multiple ecosystems in the same record | L1050-1053 |  |  |  |  |  |  | 1 |  |  |  |  |  |  |  |
| affected fields > Depicting multiple ecosystems in the same record > Separating Git and Strict Ecosystems | L1054-1062 |  |  | 4 |  |  |  |  |  |  |  | 1 |  |  |  |
| affected fields > Depicting multiple ecosystems in the same record > Version Enumeration for Git Entries | L1063-1066 |  |  |  |  |  |  | 1 (0/1) |  |  |  |  |  |  |  |
| affected fields > affected[].severity field | L1067-1074 |  | 1 |  |  |  |  |  |  |  |  |  | 1 |  |  |
| affected fields > affected[].versions field | L1075-1084 |  |  | 1 |  |  |  |  | 1 |  |  | 1 |  |  |  |
| affected fields > affected[].ranges[] field | L1085-1089 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| affected fields > affected[].ranges[].type field | L1090-1130 |  |  | 1 | 1 | 1 | 2 |  | 1 |  | 1 | 2 |  |  |  |
| affected fields > affected[].ranges[].events fields | L1131-1148 |  |  |  |  | 1 (0/1) |  |  |  |  |  |  |  |  |  |
| affected fields > affected[].ranges[].events fields > Special values | L1149-1156 |  |  |  |  |  |  |  |  |  |  |  |  |  | 1 |
| affected fields > affected[].ranges[].events fields > Requirements | L1157-1187 | 2 |  | 2 |  | 2 |  |  |  |  | 1 | 3 |  | 1 | 3 |
| affected fields > affected[].ranges[].repo field | L1188-1199 |  |  | 1 |  |  |  |  |  |  | 1 |  |  |  |  |
| affected fields > affected[].ranges[].database_specific field | L1200-1210 |  |  | 1 |  | 1 |  |  |  |  |  |  |  | 1 |  |
| affected fields > affected[].ecosystem_specific field | L1211-1224 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| affected fields > affected[].database_specific field | L1225-1241 |  |  | 1 |  |  |  |  |  |  |  |  |  |  |  |
| affected fields > Evaluation | L1242-1293 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| affected fields > Examples | L1294-1294 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| affected fields > Examples > Unfixed vulnerability example | L1295-1306 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| affected fields > Examples > Fixed vulnerability example | L1307-1319 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| affected fields > Examples > Multiple range example | L1320-1335 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| affected fields > Examples > Limit events | L1336-1376 |  |  |  | 1 | 2 |  |  |  |  |  |  |  |  |  |
| affected fields > Examples > `last_affected` vs `fixed` example | L1377-1415 |  |  |  |  | 1 (0/1) |  |  |  |  |  |  |  |  | 2 (1/1) |
| references field | L1416-1456 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| credits fields | L1457-1476 | 1 |  |  |  |  |  | 1 |  |  |  |  | 1 |  |  |
| credits fields > credits[].name field | L1477-1484 |  |  | 1 |  |  |  |  |  |  | 1 |  |  |  |  |
| credits fields > credits[].contact[] field | L1485-1489 |  |  | 1 |  |  |  | 1 |  |  |  |  | 1 |  |  |
| credits fields > credits[].type field | L1490-1509 | 1 |  | 1 |  |  |  |  |  |  |  |  | 1 |  |  |
| credits fields > credits[].type field > Examples | L1510-1526 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| database_specific field | L1527-1540 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Examples | L1541-1542 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Go vulnerability | L1543-1548 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| NPM vulnerability in GitHub database | L1549-1630 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| OSV vulnerability | L1631-1664 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Rust vulnerability | L1665-1706 |  |  |  |  |  |  | 1 (0/1) |  |  |  |  |  |  |  |
| Python vulnerability | L1707-1756 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Debian vulnerability | L1757-1802 |  |  |  |  |  |  | 1 (0/1) |  |  |  | 1 (0/1) |  |  |  |
| Ruby vulnerability | L1803-1842 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Haskell Hackage vulnerability | L1843-1888 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Haskell GHC vulnerability | L1889-1936 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| R CRAN & Bioconductor vulnerability | L1937-1996 |  |  |  |  |  |  | 1 (0/1) |  |  |  |  |  |  |  |
| Appendix | L1997-1998 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Android SoC Vendors | L1999-2010 |  |  |  |  |  |  |  |  |  |  |  | 1 |  |  |
| **whole document** | L1-2010 | **14** | **3** | **29** | **3** | **15 (11/4)** | **2** | **24 (17/7)** | **3** | **10** | **8** | **11 (10/1)** | **20** | **10** | **12 (11/1)** |

Plain word counts (case-insensitive whole words, as in the brief): must 17 (= must 14 + must not 3), should 32 (= 29 + should not 3), may 17 (= 15 + may not 2), required 8 (= 7 + not required 1). shall 0; uppercase BCP 14 keywords 0 (`bin/bcp14-count`).

The "other" column, occurrence by occurrence:

- L106 "allowed": statement N-0008
- L160 "permitted": statement N-0020
- L160 "not allowed": statement N-0021
- L835 "encouraged": statement N-0110
- L1037 "mandatory": statement N-0194
- L1046 "permitted": statement N-0199
- L1155 "allowed": statement N-0241
- L1160 "allowed": statement N-0242
- L1161 "invalid": statement N-0243
- L1170 "preferred": statement N-0248
- L1413 "preferable": statement N-0275
- L1414 "require": excluded X-062

Where the included occurrences sit (statement ids), and the excluded ones (exclusion ids):

- must (14): included 14: N-0009, N-0019, N-0114, N-0135, N-0139, N-0141, N-0149, N-0173, N-0183, N-0187, N-0250, N-0253, N-0294, N-0301.
- must not (3): included 3: N-0024, N-0094, N-0211.
- should (29): included 29: N-0012, N-0013, N-0022, N-0023, N-0025, N-0074, N-0082, N-0084, N-0086, N-0092, N-0095, N-0098, N-0128, N-0150, N-0163, N-0203, N-0204, N-0205, N-0206, N-0215, N-0226, N-0246, N-0247, N-0256, N-0262, N-0269, N-0296, N-0298, N-0300.
- should not (3): included 3: N-0093, N-0223, N-0272.
- may (15): included 11: N-0109, N-0129, N-0133, N-0194, N-0198, N-0225, N-0244, N-0251, N-0262, N-0273, N-0274; excluded 4: X-006, X-018, X-035, X-057.
- may not (2): included 2: N-0228 (×2).
- can (24): included 17: N-0014 (×2), N-0018, N-0090, N-0130 (×2), N-0133, N-0135, N-0145, N-0163 (×3), N-0186, N-0199, N-0200, N-0295, N-0298; excluded 7: X-005, X-008, X-009, X-032, X-069, X-071, X-075.
- cannot (3): included 3: N-0099, N-0214, N-0232.
- might (10): included 10: N-0007 (×2), N-0147, N-0160, N-0162, N-0174, N-0182, N-0188, N-0193, N-0196.
- required (8): included 8: N-0078, N-0079, N-0137, N-0149, N-0218, N-0254, N-0259, N-0297.
- recommended (11): included 10: N-0105, N-0132, N-0144, N-0202, N-0216, N-0225, N-0228, N-0245, N-0252, N-0254; excluded 1: X-071.
- optional (20): included 20: N-0080, N-0113, N-0120, N-0137, N-0144, N-0147, N-0150, N-0160, N-0162, N-0163, N-0174, N-0182, N-0188, N-0193, N-0196, N-0209, N-0295, N-0299, N-0300, N-0317.
- only (10): included 10: N-0006, N-0008, N-0009, N-0014, N-0020, N-0058, N-0163, N-0172, N-0242, N-0262.
- other (12): included 11: N-0008, N-0020, N-0021, N-0110, N-0194, N-0199, N-0241, N-0242, N-0243, N-0248, N-0275; excluded 1: X-062.

Imperatives without a verbal form (tagged by hand, not counted in the table): N-0024 (L168), N-0025 (L169), N-0142 (L959), N-0160 (L1003). Two more imperatives are informative: "Please feel free" (L31, excluded as X-007) and "please refer" (L1022), which sits inside the `openEuler` row N-0179 and is carried by that row.

Numbered prose statements by kind:

| kind | statements |
|---|---|
| sentence | 145 |
| table row | 106 |
| list item | 29 |
| field block | 12 |
| lead-in | 6 |
| list item, sentence 2 | 5 |
| sentence and list | 3 |
| list item, sentence 3 | 3 |
| list item, paragraph 2 | 3 |
| informal schema | 1 |
| sentence and pattern | 1 |
| list item, paragraph 3 | 1 |
| list item, paragraph 3, sentence 2 | 1 |
| sentence and pseudocode | 1 |
| **all prose statements** | **317** |

113 prose statements carry at least one counted form; 204 carry none (`[none]`, or `[imperative]` only).

JSON Schema strings: verbal forms occur only in `title` annotations inside `affected[].ranges[]`, three of the four there: N-0320 `[must, may]`; N-0324 `[require]`; N-0325 `[must]`. No `description` string carries one.

Proto comments, by form, with the statement that carries each occurrence ("licence" is the header, proto L1-13, reproduced under Licence):

| form | count | where |
|---|---|---|
| optional | 17 | N-0352, N-0358, N-0359, N-0361, N-0362, N-0363, N-0364, N-0367, N-0369, N-0374, N-0375, N-0376, N-0377, N-0381, N-0382, N-0383, N-0384 |
| required | 15 | licence, N-0349 (×3), N-0350, N-0351, N-0355, N-0356, N-0357, N-0360, N-0371, N-0372, N-0378, N-0379, N-0380 |
| may | 3 | licence, N-0349 (×2) |
| can | 2 | N-0349, N-0356 |
| may not | 1 | licence |
| should | 1 | N-0350 |
| only | 1 | N-0373 |
| recommended | 1 | N-0378 |

## Disagreements between the prose, the JSON Schema and the proto

Recorded, not fixed. Each item names the prose statements, the JSON Schema
statements and the proto statements involved; the field comparison table at
the end of this section shows every field side by side. Nothing in the three
files says which one governs when they disagree (D-24).

**D-1. `schema_version` is required only in the prose.** N-0079
requires it for schema versions above 1.0.0. `/required` (N-0333)
lists only `id` and `modified`, and the proto field (proto L196-197) carries no
marker. A record without `schema_version` validates, and by N-0013 a
consumer reads it as 1.0.0.

**D-2. `id`: format, character set and separator.** The prose constrains an
`id` three ways: the format `<DB>-<ENTRYID>` (N-0017); the character set
(N-0019, N-0020, N-0021); and a scoped prefix
"followed (ideally) by a `-` separator" (N-0025). The JSON Schema
applies only `/$defs/prefix/pattern` (N-0338). (a) The pattern has no `$`
anchor and says nothing about the characters after the prefix, so an id such as
`GHSA-a b/c` validates although N-0021 forbids spaces and slashes.
(b) It requires `-` after every database prefix, which N-0025 makes
a preference and N-0017 implies (U-25). (c) After `x_` it accepts
anything, including nothing: the string `x_` alone validates. The proto
constrains nothing beyond `string`.

**D-3. The prefix list.** The prose table (rows after N-0026) and the
prefix pattern (N-0338) list the same prefixes with two exceptions: the
prose row spells `CleanStart` where the pattern has `CLEANSTART` (the row's own
OSV Formatted URL template is `CLEANSTART-YYYY-<ID>.json`, U-8), and the
pattern has `FreeBSD`, which has no row in the prose table (it is a prose
ecosystem). So an id `CleanStart-...` fails the schema and `FreeBSD-...`
passes. The pattern's `SUSE-[SRFO]U` equals the four `SUSE-` prefixes of the
prose row.

**D-4. `GIT` as an ecosystem.** `/$defs/ecosystemWithSuffix/pattern`
(N-0337) accepts `GIT`, and `GIT:` followed by anything, as
`affected[].package.ecosystem`. The prose has no `GIT` row in its ecosystem
table, says the ecosystem "must be one of the strings in the table below"
(N-0139), says a Git entry should use no `package` field
(N-0205), and calls GIT a "pseudo-ecosystem"
(N-0214). The proto comment (N-0351)
points to the prose list. The unused `/$defs/ecosystemName/enum`
(N-0335) matches the prose exactly.

**D-5. Ecosystem suffix and name rules are not checked.** Rows of the prose
ecosystem table state: a required suffix (`Alpine`, `Mageia`, `Photon OS` and
`Red Hat Lightwell`: "must have"; `Ubuntu`: a "mandatory `:LTS`" suffix for LTS
releases); a suffix the string has (`Alpaquita`, `Azure Linux`,
`BellSoft Hardened Containers`, `openEuler`, `openSUSE`, `Red Hat`, `SUSE`,
`Ubuntu`); no suffix (`vcpkg`: "has no release suffix"); and closed sets of
suffixes (`Echo`: "The supported values are" four; `WordPress`: `:Core`,
`:Plugin`, `:Theme`). The pattern (N-0337) accepts every
ecosystem with or without any non-empty `:` suffix. Name rules are not checked
either, for example `Linux` ("The only supported `name` is `Kernel`.") and
`Android` (`:linux_kernel:` plus a vendor from N-0317).

**D-6. Reference type `GIT`.** The JSON Schema enum (N-0328) and
the proto enum (N-0370, `GIT = 11`) include `GIT`; the prose list
(N-0282 to N-0291) does not, and the prose never says what
a `GIT` reference is.

**D-7. Open lists closed by the schema.** The prose introduces the reference
types as "The known reference `type` values" (N-0281) and gives the
severity source table without a "must be one of" (N-0120,
rows N-0122 to N-0124). The JSON Schema closes both with
`enum` (N-0328, N-0340). The prose does close
the severity types (N-0114) and the credit types
(N-0301), and those enums match.

**D-8. Ubuntu severity score.** The prose row (N-0118) says only "A
lowercased string representing the" Ubuntu priority; the JSON Schema
(N-0344) allows exactly `negligible`, `low`, `medium`, `high` and
`critical`.

**D-9. CVSS scores.** The prose rows allow a CVSS version "== 2.0", ">= 3.0 and
< 4.0" and ">= 4.0 and < 5.0" (N-0115 and the next two rows). The
JSON Schema accepts only `CVSS:3.0/` and `CVSS:3.1/` for `CVSS_V3`
(N-0342) and only `CVSS:4.0/` for `CVSS_V4` (N-0343). Its
`CVSS_V2` and `CVSS_V3` patterns accept any non-empty sequence of known
metrics in any order with repeats, so `CVSS:3.1/AV:N` and `AV:N/AV:L` validate;
the `CVSS_V4` pattern requires all eleven base metrics in order. The proto
checks nothing.

**D-10. GIT event values.** The prose says GIT `introduced` and `fixed` are
"full-length Git commit hashes" (N-0229), gives `"0"` a meaning for
`introduced` (N-0238) and `"*"` for `limit` (N-0239,
N-0240). JSON Schema `allOf/1` (N-0325) requires every
event value of a GIT range to match `^(0|[a-f0-9]{40}|[a-f0-9]{64})$`. So (a)
`"0"` also passes for `fixed`, `last_affected` and `limit`, where the prose
gives it no meaning; (b) an explicit `{"limit": "*"}` fails in a GIT range; (c)
uppercase hexadecimal fails; (d) `last_affected` and `limit` values must also
be hashes, where the GIT bullet names only `introduced` and `fixed` (though
N-0236 says all four are version strings as the range type
defines them); (e) 64-digit (SHA-256) hashes pass, which the prose neither
names nor excludes. The proto checks nothing.

**D-11. `null` arrays and the severity rule.** The JSON Schema types `aliases`,
`affected`, `references` and both `severity` arrays as `["array", "null"]`
(schema L24, L54, L295 and L471); the prose describes each as a list or a JSON
array and never mentions `null`. The prose rule N-0211
(package-level `severity` set, so the top level must not be) is enforced as its
contrapositive by `/allOf/0` (N-0334): when the top-level key is
present, every `affected[].severity` must be absent or `null`. The prose does
not define "set" (U-26), so a top-level `"severity": null` or `[]` next to a
filled `affected[].severity` fails the schema although a reader of the prose
may not count `null` as set.

**D-12. Required markers in the proto.** The proto marks `summary`
(N-0378), `details` (N-0379), `affected` (N-0380) and
`Affected.ranges` (N-0360) Required. The prose makes every
top-level field except `id`, `modified` and (above 1.0.0) `schema_version`
optional (N-0080) and never requires `ranges`; the JSON Schema
requires none of the four. The other way round, the proto puts no marker on
`id`, `modified`, `schema_version`, `Severity.type`, `Severity.score` or
`Credit.name`, which the prose or the JSON Schema requires. proto3 has no
required fields, so every marker is a comment.

**D-13. One event type per event.** The prose rule is N-0242. The
JSON Schema `oneOf` (N-0322) enforces it, but the event object
has no `additionalProperties: false`, so `{"introduced": "0", "note": "x"}`
validates. The proto `Event` (N-0353) has four independent string fields
and no `oneof`, so it can hold several event types at once.

**D-14. Unknown fields.** N-0014 lets a client that reads 1.2.0
process 1.3.0 data "by ignoring any unexpected fields".
`/additionalProperties` (N-0348) rejects any top-level key the schema
does not list, so a record from a later minor version with a new top-level
field fails this schema. Nested objects (`affected[]`, `package`, `ranges[]`,
`events[]`, `severity[]`, `references[]`, `credits[]`) accept unknown keys.

**D-15. Timestamps and URLs.** The prose wants RFC 3339 in UTC ending in "Z"
(N-0076, N-0082, N-0084) and a fully qualified
`url` (N-0279). In the JSON Schema (N-0346, N-0347,
N-0329) the `format` keywords only annotate under draft
2020-12 unless the validator turns format assertion on; a default validator
applies only the timestamp pattern, which has no anchors (so
`x2021-01-01T00:00:00Zx` passes) and requires uppercase `T` and `Z`
(**(inferred)** RFC 3339 §5.6 also allows lowercase). The proto uses
`google.protobuf.Timestamp`, whose JSON form is always UTC with `Z`.

**D-16. `versions` is never required by a schema.** The prose requires
`versions` for products whose versions cannot be represented as ranges
(N-0135) and says GIT ranges do not remove that requirement
(N-0232). The JSON Schema does not require `versions`, and the
proto says "Optional. List of affected versions." (N-0361).
A GIT-only entry without `versions` validates (U-2).

**D-17. `package` optional only in the proto.** The proto says "Optional.
Package information." (N-0359); the JSON Schema does not
require `package`; the prose never says it outright, though
N-0205 implies it and the evaluation pseudocode (N-0271)
assumes every entry has one (U-23).

**D-18. Meaning of `related`.** The proto comment (N-0376) gives "the
same problem in alternate ecosystems" as an example of a related
vulnerability. In the prose, an alias is the same vulnerability in other
databases (N-0088), and `related` covers a similar but different
vulnerability or cases that are neither aliases nor upstream (N-0101).

**D-19. `summary` length.** The prose recommends "on the order of no more than
120 characters" (N-0105); the proto comment (N-0378) says
"under 120 characters".

**D-20. `ranges[].database_specific`.** The prose (N-0260) says
the object holds information "about the range" from the database "from which
the record was obtained"; the proto comment (N-0358) says "about
the vulnerability" and "for which the record applies".

**D-21. The informal schemas.** The Format Overview block (N-0005)
shows `database_specific` inside `ranges`; the `affected` block
(N-0125) does not, and the sentence that lists the range fields
(N-0258) names only `type`, `events` and `repo`. The JSON Schema
(schema L157-159) and the proto (L98-100) both define
`ranges[].database_specific`, as does the prose section for it
(N-0260).

**D-22. Proto zero values.** `UNSPECIFIED` (`Range.Type`, `Severity.Type`,
`Credit.Type`), `SOURCE_UNSPECIFIED` (`Severity.Source`) and `NONE`
(`Reference.Type`) are proto defaults with no prose or JSON Schema counterpart;
a record that carried one as a string would fail the matching JSON Schema enum.

**D-23. `Commit` exists only in the proto.** The deprecated `Commit` message
(N-0349) defines commit references with an `A:B` range form; no message
uses it, and neither the prose nor the JSON Schema has it.

**D-24. Which file governs.** The proto calls itself "*NOT* stable" and "only
used for implementing the JSON based API" (N-0373); the prose calls
the JSON Schema a schema "for validation" (N-0004). None of the
three files says which prevails when they differ. **(inferred)** This file
treats the prose as the definition, the JSON Schema as its machine check and
the proto as an implementation aid; the requirements pass should confirm that
reading.

**D-25. Inside the JSON Schema.** `/$defs/ecosystemName` (N-0335)
and `/$defs/ecosystemSuffix` (N-0336) are defined but never
referenced, so they validate nothing.

### Prose rules the JSON Schema does not check

| prose | rule | JSON Schema |
|---|---|---|
| N-0079 | `schema_version` required above 1.0.0 | not required (D-1) |
| N-0012 | `schema_version` is SemVer without a leading "v" | `type: string` only |
| N-0017, N-0019, N-0020, N-0021 | `<DB>-<ENTRYID>`, ASCII character set | prefix only (D-2) |
| N-0022, N-0024 | semantically neutral ids | none |
| N-0104, N-0107, N-0105 | one line, English, plain text, short | `type: string` only |
| N-0106, N-0108 | English, CommonMark | `type: string` only |
| N-0076, N-0082, N-0084 | RFC 3339, UTC, ends in "Z" | unanchored pattern; `format` annotates (D-15) |
| N-0088, N-0093, N-0094 | aliases are ids of the same vulnerability, not upstream or downstream | array of strings |
| N-0135, N-0232 | `versions` required in stated cases | not required (D-16) |
| N-0143 | `purl` follows the purl specification, without `@version` | `type: string` only |
| N-0139 and the ecosystem rows | suffix and name rules | any suffix (D-5) |
| N-0223 | SEMVER ranges should not overlap | none |
| N-0254 | `events` sorted | none |
| N-0250 | every cherry-picked fix listed | none |
| N-0256 | `repo` usable by the clone command | `type: string` only |
| N-0298 | contacts are valid, fully qualified URLs | `type: string` only |
| N-0272 | no `limit` for linear version ranges | none |

### JSON Schema constraints with no prose statement

- `null` accepted for `aliases`, `affected`, `references` and `severity` (D-11).
- `additionalProperties: false` at the top level (N-0348); the prose
  comes closest in N-0009 (D-14).
- `-` required after every database prefix, `CLEANSTART` and `FreeBSD` in the
  prefix list (N-0338; D-2, D-3).
- `GIT` as an ecosystem and as a reference type (D-4, D-6).
- Closed lists for reference types, severity sources and Ubuntu scores (D-7,
  D-8); the CVSS version and vector patterns (D-9).
- The exact GIT event value pattern (D-10).
- `events` itself required (N-0327) and `minItems: 1`
  (N-0323); the prose implies both through N-0253.

### Field comparison

The prose column gives the presence rule and the main constraint, the JSON
Schema column what a validator checks, and the proto column the field's type,
line in the proto file and marker.

| field | prose | JSON Schema | proto | see |
|---|---|---|---|---|
| `schema_version` | required above 1.0.0; SemVer | string; not required | `string`, L197; no marker | D-1 |
| `id` | required; `<DB>-<ENTRYID>`; character set | required; prefix pattern | `string`, L202; no marker | D-2, D-3 |
| `modified` | required; RFC 3339 UTC | required; timestamp | `Timestamp`, L206; no marker | D-12, D-15 |
| `published` | optional; RFC 3339 UTC | timestamp | `Timestamp`, L204; no marker | D-15 |
| `withdrawn` | optional; RFC 3339 UTC | timestamp | `Timestamp`, L209; Optional | D-15 |
| `aliases` | optional; ids in the form of `id` | array of string, or null | repeated `string`, L211; Optional | D-11 |
| `upstream` | optional; ids | array of string | repeated `string`, L216; Optional | |
| `related` | optional; ids | array of string | repeated `string`, L214; Optional | D-18 |
| `summary` | optional; one line, plain text | string | `string`, L219; Required | D-12, D-19 |
| `details` | optional; CommonMark | string | `string`, L221; Required | D-12 |
| `severity` | optional; not with package-level severity | array of objects, or null | repeated `Severity`, L231; Optional | D-11 |
| `severity[].type` | must be one of four | required; enum of four | `Severity.Type`, L138; no marker; `UNSPECIFIED` | D-22 |
| `severity[].score` | string for the type | required; pattern or enum per type | `string`, L140; no marker | D-8, D-9 |
| `severity[].source` | optional; three values listed | enum of three | `Severity.Source`, L142; Optional | D-7 |
| `affected` | optional | array of objects, or null | repeated `Affected`, L223; Required | D-11, D-12 |
| `affected[].package` | implied optional | object; not required | `Package`, L106; Optional | D-17 |
| `package.ecosystem` | required; one of the table | required; pattern (+ `GIT`, any suffix) | `string`, L64; Required | D-4, D-5 |
| `package.name` | required | required; string | `string`, L60; Required | |
| `package.purl` | optional, recommended | string | `string`, L66; Optional | |
| `affected[].severity` | optional; excludes top-level severity | array, or null; null if top-level present | repeated `Severity`, L118; Optional | D-11 |
| `affected[].ranges` | optional | array of objects | repeated `Range`, L108; Required | D-12 |
| `ranges[].type` | required; three values | required; enum of three | `Range.Type`, L92; Required; `UNSPECIFIED` | D-22 |
| `ranges[].repo` | required if `GIT` | required if `GIT` | `string`, L95; Required if GIT | |
| `ranges[].events` | at least one `introduced`; one type per event; not both `last_affected` and `fixed` | required; `contains`; `minItems`; `oneOf`; `allOf/2` | repeated `Event`, L97; Required; no `oneof` | D-10, D-13 |
| `ranges[].database_specific` | object about the range | object | `Struct`, L100; Optional | D-20, D-21 |
| `affected[].versions` | recommended; required in stated cases | array of string | repeated `string`, L110; Optional | D-16 |
| `affected[].ecosystem_specific` | object | object | `Struct`, L113; Optional | |
| `affected[].database_specific` | object | object | `Struct`, L116; Optional | |
| `references` | optional | array of objects, or null | repeated `Reference`, L226; Optional | D-11 |
| `references[].type` | ten known values | required; enum of eleven (+ `GIT`) | `Reference.Type`, L187; Required; `NONE` | D-6, D-7 |
| `references[].url` | fully qualified URL | required; `format: uri` | `string`, L189; Required | D-15 |
| `credits` | optional | array of objects | repeated `Credit`, L233; Optional | |
| `credits[].name` | required | required; string | `string`, L147; no marker | D-12 |
| `credits[].contact` | optional; URLs | array of string | repeated `string`, L149; no marker | |
| `credits[].type` | optional; one of ten | enum of ten | `Credit.Type`, L165; Optional; `UNSPECIFIED` | D-22 |
| `database_specific` | object | object | `Struct`, L229; Optional | |
| any other top-level key | ignored by clients | rejected | not representable | D-14 |

## Inconsistencies and unclear points in the prose

Recorded, not fixed.

**U-1. Strength of the alias rule.** N-0093 says aliases
"should **not**" refer to upstream or downstream vulnerabilities; the example
that follows (N-0094) says the distribution's record "must not"
list the CVE as an alias.

**U-2. Is `versions` required?** It is "generally recommended"
(N-0132); products whose versions cannot be ranges "must
include" it (N-0135); SEMVER ranges remove "the requirement"
(N-0224); GIT ranges do "NOT remove the requirement"
(N-0232); for ECOSYSTEM ranges "It is recommended"
(N-0228). Whether a GIT-only entry without `versions` is
non-conforming or only discouraged is not settled (D-16).

**U-3. The `repo` section.** After the two `repo` sentences, a paragraph
repeats the definition of `ranges` (N-0257 repeats N-0217),
breaks into a fragment without a verb and leaves out `database_specific`
(N-0258). The next sentence, "This field is required if" the type is
`GIT` (N-0259), follows that paragraph, so only the heading
says that "This field" is `repo`.

**U-4. Scope of the cherry-pick rule.** By its words N-0250
applies to every `events` array with `fixed` events; the sentence before it
(N-0249) frames the passage as a trade-off for GIT ranges, and
cherry-picked commits exist only there.

**U-5. The `limit` value `"*"`.** N-0239 speaks of "versions
containing the string" `"*"`, not versions equal to it, so whether `1.*`
means infinity is not said; the pseudocode (N-0271) compares `v < evt.limit`
without treating `*` specially.

**U-6. Where a withdrawal rationale goes.** N-0086 says "the
summary text", while `summary` is one line (N-0104); `details` may be
meant.

**U-7. Prefix table order.** An HTML comment above the table asks to keep the
list alphabetically sorted (L177). It is not: `ASB-A` comes before `ALSA`,
`ALSA` before `ALPINE`, `MGASA` before `MAL`, `RHSA` before `RHLW`, `RSEC`
before `ROOT`, and `CLSA` is last.

**U-8. The CleanStart row.** Its Database cell is a link with no text, so the
home database has no name; its prefix `CleanStart` does not match its own URL
template `CLEANSTART-YYYY-<ID>.json` (D-3); "How to contribute:" has no space
before its value.

**U-9. The DRUPAL row.** Its OSV Formatted URL is written with the angle
bracket entities reversed (`&gt;module&lt;/&gt;ID&lt;.json`), which renders as
`>module</>ID<.json`.

**U-10. The FreeBSD ecosystem row.** The last sentence breaks off ("applies
only to a particular FreeBSD release like."); `FreeBSD:base:14.3` is given as
an example of `ranges[].events` versions although it has the shape of an
ecosystem string; "namespace" is used for a part of the ecosystem string
without definition.

**U-11. The openEuler ecosystem row.** It "has a `<RELEASE>` suffix", without
the `:` that every other row writes; "Release.`<RELEASE>`" lacks a space; the
row mixes in the publisher's own policy (its archive list, and which versions
are in the scope of its advisories).

**U-12. Small slips.** Debian row: "use the the string" and a double space
before `distro-info-data`. CVSS_V4 row: "a version on the". SwiftURL row:
"comform". The Ubuntu severity row has no closing `|`. N-0082 says
"time stamp" where the other fields say "timestamp". N-0126:
"objects that describes".

**U-13. Order of the Ubuntu ecosystem parts.** The row says "The release
version may also be prefixed with `:Pro:`" and requires `:LTS` for LTS
releases; the order of the parts (`Ubuntu:Pro:18.04:LTS`) is shown only by
example.

**U-14. What follows `x_`.** N-0018 and N-0025 allow `x_` "for
local databases" and the example is `x_CUSTOM-0001`; whether a database name
and `-` must follow `x_` is not said. The JSON Schema accepts any string that
starts with `x_`.

**U-15. Possibility, not permission.** Some "may", "can", "might" and "cannot"
sentences state what is possible and grant or forbid nothing:
N-0225, N-0228 (twice "may not"),
N-0251, N-0262, N-0273,
N-0214, N-0298 ("can be reached") and the
`Red Hat` ecosystem row ("can be used"). The requirements pass should not read
them as permissions or prohibitions.

**U-16. "should" that defines a reading.** N-0013, N-0082,
N-0084, N-0092, N-0098,
N-0246 and N-0247 use "should be assumed", "should be
considered" or "should be thought of" to say how data is to be read, not to
recommend something a producer could decline. N-0099 ("cannot")
makes `upstream` asymmetric, which is stronger than "not symmetric" in
N-0098.

**U-17. `related` stated as fact.** N-0102 says related vulnerabilities
"are symmetric", without the "should be considered" used for aliases and
upstream.

**U-18. Snippets that are not valid JSON.** The `credits` field block
(N-0292), the worked-example ranges (L1302, L1315, L1350, L1364, L1392
and L1408) and the credits example (L1522) have trailing commas. The examples
are excluded here; fixtures built from them need the commas removed.

**U-19. Scope of "should not overlap".** N-0223 does not say
whether it means ranges across the `ranges` array of one entry, events within
one range, or both.

**U-20. Whose notation.** N-0294 says "using whatever notation
they prefer"; N-0296 says "the creditor prefers".

**U-21. Lowercase type names.** The `FIX` and `INTRODUCED` reference items say
"the `fix` type" and "the `introduced` type" (N-0287 and the item
after it); the values are `FIX` and `INTRODUCED`, and `introduced` is also an
event name.

**U-22. Heading structure.** "modified field" is a level-3 heading under "id,
modified fields", placed after the prefix table, and the record-level rules on
required and optional fields (N-0078, N-0079,
N-0080) sit under it.

**U-23. Gaps in the evaluation pseudocode.** N-0271 (a) uses `sorted` and
`>=`, `>` and `<` without saying how they work for GIT ranges, where order is
commit ancestry (N-0231) and two commits may be unordered; (b) compares
`affected.package == pkg`, which is undefined for an entry without `package`
(N-0205); (c) does not treat the special values `"0"` and
`"*"` explicitly.

**U-24. Wildcard names.** N-0142 allows the name `*` for every
ecosystem; the `Linux` row says "The only supported `name` is `Kernel`.", and
the `Android` row fixes the form of kernel names. The rules are not
reconciled.

**U-25. The `-` in an id.** N-0017 gives the format `<DB>-<ENTRYID>`,
with a `-`; N-0025 says the prefix is followed "(ideally)" by `-`.

**U-26. What "set" means for `severity`.** N-0211 does not
say whether an empty array or `null` counts as set (D-11).

**U-27. Which JSON Schema.** N-0004 links to the JSON Schema on the
`main` branch, and the schema's `$id` is a `main` URL too; neither is pinned to
1.9.2. This file reads the schema at tag v1.9.2.

**U-28. What "All other fields" covers.** N-0080 says "All other fields are
optional" right after the required `id`, `modified` and (above 1.0.0)
`schema_version` (N-0078, N-0079), all top-level fields. It does not say whether
the members of nested objects are covered; read for every field, it would
contradict the members other sentences make mandatory: the two `package` fields
(N-0137, N-0141), a range's `type` (N-0218) and `introduced` event (N-0253), a
credit's `name` (N-0294, N-0297), a reference's `type` and `url` (N-0278) and a
severity item's `type` and `score` (N-0113). `requirements.yaml` (R-0027) and,
since pass 3, `messages.yaml` read it for the top level. (Added in pass 3,
cross-check.)

## Licence

The OSV Schema is distributed under the Apache License, Version 2.0
(https://www.apache.org/licenses/LICENSE-2.0). This file quotes docs/schema.md,
validation/schema.json and proto/vulnerability.proto at tag v1.9.2 for
commentary and analysis. It changes nothing in the quoted text except joining
wrapped lines and re-serialising JSON values as described under Conventions;
everything outside the quotations is the library's own. The proto file's
header, reproduced verbatim:

> ```proto
> // Copyright 2025 Google LLC
> //
> // Licensed under the Apache License, Version 2.0 (the "License");
> // you may not use this file except in compliance with the License.
> // You may obtain a copy of the License at
> //
> //      http://www.apache.org/licenses/LICENSE-2.0
> //
> // Unless required by applicable law or agreed to in writing, software
> // distributed under the License is distributed on an "AS IS" BASIS,
> // WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
> // See the License for the specific language governing permissions and
> // limitations under the License.
> ```
