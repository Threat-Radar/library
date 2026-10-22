---
record: ecma-427
kind: normative
title: "ecma-427: normative statements"
extracted: "2026-10-15"
reviewed_by: ""
source_version: "1st edition (December 2025)"
source_digest: "037180df99e7d7c26d910dc3adb3fa07c4fb787cc4bd29e43634de3802313825"   # SHA-256 of ECMA-427_1st_edition_december_2025.pdf (40 pages)
attribution: "Contains text from ECMA-427 1st edition, © Ecma International 2025, reproduced under the Ecma copyright notice; full notice at the end of this file and in distilled/README.md"
---

<!-- FX-1 pass 1 (normative agent). Every normative statement of ECMA-427,
     1st edition, VERBATIM, with its locator, in source order. Verbatim source
     text: every blockquote, every cell of the eight transcribed tables, the
     values in the Annex A keyword tables and the captions and contents in the
     examples table. Everything else (headings, numbers, locators, tags, notes)
     is extractor structure. -->

Source: ECMA-427, "Package-URL (PURL) specification", 1st edition, December
2025, Ecma International Technical Committee 54 (TC54). Editors: John Horan,
Michael Herzog, Philippe Ombredanne, Steve Springett. PDF from
https://ecma-international.org/wp-content/uploads/ECMA-427_1st_edition_december_2025.pdf
(SHA-256 above). Text read from `pdftotext -layout` of that PDF and checked
against rendered page images wherever a table or wrapped line could be
ambiguous.

## Conventions

**Verbatim.** Quoted text is the Standard's own words, punctuation, quote marks
(straight and curly), hyphens and capitalisation. The only normalisation is
joining a sentence the PDF wrapped across lines or pages: the line break and
indentation become one space and page footers inside it are dropped. Where the
PDF broke a line straight after a hyphen or slash that is part of the word or
URL, the join adds no space. These are the only such joins:
`percent-encoding` (§5.4, bullet 1), `Package-URL` (§6.5.5, §6.6.3, §6.7.3,
§6.9.3 and Tables 4, 5, 6 and 8), the Annex A URL
`https://github.com/package-url/purl-spec/blob/main/schemas/purl-type-definition.schema.json`,
and the two Annex A schema strings `purl-type-definition.schema-1.0.json` and
`[a-z0-9-]+-definition\\.json$`. The first schema string is confirmed by the
identical, unwrapped `$id` value on p. 19. PDF typography (bold, monospace,
italics, hyperlinks) is not reproduced; the words are. Lists are quoted inside
`text` fences with the source's own bullet glyphs (• and ◦) so that characters
such as `_`, `~`, `#` and `\` are not reinterpreted as Markdown.

**Table captions.** In the source each caption joins "Table N" and the title
with an em dash (U+2014). House style forbids that character in this library,
so captions are given as "Table N: title". This is the only deliberate
departure from the source's characters; every cell is verbatim.

**Locators** are clause, bullet, paragraph, table, property-block and JSON
Pointer references, with the printed page in parentheses. Printed pages 1 to 18
are PDF pages 9 to 26; Annex A pages 19 to 25 are PDF pages 27 to 33; the
Copyright Notice (p. v) is PDF page 7.

**Verbal forms.** ECMA-427 uses lowercase verbal forms and never states its
own convention (it has no terms-and-definitions clause and no keyword
boilerplate). This file relies on the convention of the ISO/IEC Directives,
Part 2, which Ecma drafting follows: "shall" and "shall not" express a
requirement, "should" a recommendation, "may" a permission, "can" and "cannot"
a possibility or capability. Sentence-initial "Shall" (five times, "Shall be one
of:") is the same verbal form. Uppercase BCP 14 keywords occur only in the
Software License on p. 31 and are outside the extracted text.

**Tags.** Each numbered statement carries one tag set, in backticks, after its
locator:

- `[shall]`, `[shall not]`, `[should]`, `[may]`, `[can]`, `[cannot]`: one entry
  per occurrence of that verbal form in the quoted text, in order (statement 55
  is `[shall, shall]`; statement 96 is `[may, shall]`). "shall not" is counted
  only as "shall not", never also as "shall". `[can]` is never used: the only
  "can" in Clauses 1 to 6 is in an excluded sentence.
- `[none: declarative]`: no verbal form; a definition, constant, structural
  fact or cross-reference that defines or constrains.
- `[none: lead-in]`: a fragment ending in a colon whose list items carry their
  own verbal forms and are numbered as separate statements directly after it.
  Lists whose items are plain definitions stay inside one statement.
- `[none: imperative]`: an instruction in the imperative mood, without a
  verbal form.
- `[none: table cell]`: a whole normative table. Every sentence in a table cell
  that contains a verbal form is also quoted as its own numbered statement
  directly after the table, so each occurrence belongs to exactly one tagged
  statement.
- `[none: property block]`: the Location, Property, Type, Pattern Constraint,
  Format, Default Value and Constant lines of a Clause 6 subclause.

Every occurrence of "shall", "shall not", "should", "may" and "cannot" in
Clauses 2, 5 and 6 and in the Annex A description strings belongs to exactly
one numbered statement. Notes marked **(inferred)** are extractor readings,
not source text.

## 1 Scope

Clause 1 states the subject and field of application of the Standard. Each of
its five sentences was assessed; none is extracted as a numbered statement.

**S1.** §1, paragraph 1, sentence 1 (p. 1). Constrains: no.

> This Standard defines the Package-URL (PURL) syntax for identifying software packages independently from their ecosystem or distribution channel.

Why: it names the subject of the Standard; it has no actor and no verbal form.

**S2.** §1, paragraph 1, sentence 2 (p. 1). Constrains: no.

> PURL is used to identify software packages across software supply chains supporting many use cases, identifying software packages in Software Bills of Materials, vulnerability databases, vulnerability advisories, vulnerability disclosures and exploitability reports, and managing software package dependencies.

Why: it lists use cases; it is descriptive.

**S3.** §1, paragraph 2, sentence 1 (p. 1). Constrains: yes in substance, but not
extracted here.

> A PURL is a valid URL and URI composed of seven components to identify a software package.

Why: the same constraint is stated normatively in Clause 5 (statement 20, "A
PURL is a URL composed of seven components:") and §5.1 (statement 26, "A PURL
is a valid URL and URI that conforms to the URL definitions or specifications
at:"). Extracting the Scope restatement as well would double-count it.

**S4.** §1, paragraph 2, sentence 2 (p. 1). Constrains: not by itself.

> The PURL type component defines the ecosystem-specific structure and meaning for the other PURL components.

Why: a design principle with no actor and no verbal form. Clause 5 applies it
piecemeal ("unless the package's type definition provides otherwise",
"Namespace is type-specific", "Qualifiers are type-specific") and Clause 6 gives
it a schema. This is the only place the principle is stated in general terms,
so it is flagged here for the requirements pass.

**S5.** §1, paragraph 2, sentence 3 (p. 1). Constrains: no (scope boundary).

> This Standard specifies the syntax for PURLs and the schema for defining PURL types, but it does not include any specific PURL type definitions, such as maven, pypi or npm.

Why: it limits what the Standard contains (no type definitions such as maven,
pypi or npm are part of this edition); it does not constrain an implementation.

## 2 Conformance

**1.** §2, paragraph 1 (p. 1) `[shall]`

> A conforming implementation of Package-URL (PURL) shall fully implement and support all elements defined within this Standard, including the syntax, components, and semantic requirements for constructing and interpreting valid PURLs.

**2.** §2, paragraph 2, sentence 1 (p. 1) `[shall]`

> A conforming implementation of PURL shall adhere to the syntax defined in this Standard, ensuring that all PURLs are parsed, constructed, and validated according to the prescribed rules.

**3.** §2, paragraph 2, sentence 2 (p. 1) `[shall]`

> The implementation shall provide full support for ecosystem-agnostic behaviour, enabling PURLs to function consistently and reliably across diverse environments.

**4.** §2, paragraph 3, sentence 1 (p. 1) `[shall]`

> All required components of a PURL, such as the scheme, type, and name, shall be present and validated according to the rules defined in this Standard.

**5.** §2, paragraph 3, sentence 2 (p. 1) `[shall]`

> Additionally, optional components, including qualifiers and subpaths, shall be handled appropriately if provided, in full compliance with their specified behaviours.

**6.** §2, paragraph 4, sentence 1 (p. 1) `[shall]`

> Implementations shall ensure that equivalent PURLs are consistently resolved to the same canonical representation.

**7.** §2, paragraph 4, sentence 2 (p. 1) `[none: declarative]`

> This includes strict adherence to normalisation and equivalence rules.

Note: extends statement 6.

**8.** §2, paragraph 4, sentence 3 (p. 1) `[shall]`

> Furthermore, implementations shall process URI encoding and decoding for PURL components according to the standards outlined in RFC 3986.

**9.** §2, paragraph 5, sentence 1 (p. 1) `[shall]`

> Invalid PURLs that fail to conform to the specification shall be identified and rejected by any conforming implementation.

Paragraph 5, sentence 2 is motivation and is listed under "Informative content
excluded".

**10.** §2, paragraph 6, sentence 1 (p. 1) `[may]`

> A conforming implementation of PURL may extend its functionality by providing ecosystem-specific validation, processing, or metadata handling, as long as these extensions do not violate the core specification.

**11.** §2, paragraph 6, sentence 2 (p. 1) `[may]`

> Additionally, implementations may offer auxiliary tools or features, such as utilities for constructing or validating PURLs, provided they align with the standard's requirements.

**12.** §2, paragraph 7, sentence 1 (p. 1) `[shall not]`

> A conforming implementation shall not redefine or alter the core syntax, components, or semantics defined by this Standard.

**13.** §2, paragraph 7, sentence 2 (p. 1) `[shall not]`

> Any prohibited extensions explicitly identified in the specification shall not be implemented.

**14.** §2, paragraph 7, sentence 3 (p. 1) `[none: declarative]`

> Furthermore, behaviours that compromise the interoperability of PURLs across tools, platforms, or ecosystems are strictly disallowed.

Note **(inferred)**: a prohibition expressed without a verbal form ("are
strictly disallowed").

## 3 Normative references

**15.** §3, paragraph 1, sentence 1 (p. 2) `[none: declarative]`

> The following documents are referred to in the text in such a way that some or all of their content constitutes requirements of this document.

**16.** §3, paragraph 1, sentence 2 (p. 2) `[none: declarative]`

> For dated references, only the edition cited applies.

**17.** §3, paragraph 1, sentence 3 (p. 2) `[none: declarative]`

> For undated references, the latest edition of the referenced document (including any amendments) applies.

**18.** §3, reference list (p. 2) `[none: declarative]`

> ```text
> ECMA-262, ECMAScript® language specification
> https://ecma-international.org/publications-and-standards/standards/ecma-262/
>
> RFC 3986, Uniform Resource Identifier (URI): Generic Syntax
> https://datatracker.ietf.org/doc/html/rfc3986
>
> The Unicode Standard
> https://www.unicode.org/versions/latest/
> ```

Note: all three entries are undated, so statement 17 applies to each.

## 4 Overview

Not extracted. Clause 4 declares itself non-normative at its start and its end
(§4, paragraph 1 and paragraph 6, p. 2):

> This Clause contains a non-normative overview of the Package-URL specification.

> This overview is non-normative and serves to provide context for the specification’s intent, purpose, and audience. For detailed requirements and conformance criteria, refer to the normative clauses of this Standard.

The four paragraphs between them contain no "shall", "shall not", "should",
"may", "can" or "cannot".

## 5 Package-URL specification

**19.** §5, paragraph 1 (p. 2) `[none: declarative]`

> PURL stands for Package-URL.

**20.** §5, paragraph 2 and the syntax line (p. 2) `[none: declarative]`

> A PURL is a URL composed of seven components:
>
> ```text
> scheme:type/namespace/name@version?qualifiers#subpath
> ```

**21.** §5, paragraph 3 (p. 2) `[none: declarative]`

> Components are separated by a specific character for unambiguous parsing.

**22.** §5, Table 1 (p. 3) `[none: table cell]`

**Table 1: Components of a PURL**

| Component | Requirement | Description |
|---|---|---|
| scheme | Required | The URL scheme with the constant value of "pkg". One of the primary reasons for this single scheme is to facilitate the future official registration of the "pkg" scheme for Package-URLs. |
| type | Required | The package "type" or package "protocol" such as maven, npm, nuget, gem, pypi, etc. |
| namespace | Optional | A name prefix such as a Maven groupid, a Docker image owner, a GitHub user or organization. Namespace is type-specific. |
| name | Required | The name of the package. |
| version | Optional | The version of the package. |
| qualifiers | Optional | Qualifier data for a package such as OS, architecture, repository, etc. Qualifiers are type-specific. |
| subpath | Optional | Subpath within a package, relative to the package root. |

Note: Table 1 contains no verbal form. The second sentence of the scheme row is
rationale; it stays because the table is transcribed whole.

**23.** §5, paragraph 4, after Table 1 (p. 3) `[none: declarative]`

> Components are designed such that they form a hierarchy from the most significant on the left to the least significant components on the right.

**24.** §5, paragraph 5, sentence 1 (p. 3) `[shall not]`

> A PURL shall not contain a URL Authority, i.e. there is no support for username, password, host and port components.

**25.** §5, paragraph 5, sentence 2 (p. 3) `[may]`

> A namespace segment may sometimes look like a host, but its interpretation is specific to a type.

Note **(inferred)**: "may" here expresses possibility, not permission; it grants
nothing.

### 5.1 A PURL is a URL

**26.** §5.1, bullet 1 (p. 3) `[none: declarative]`

> ```text
> • A PURL is a valid URL and URI that conforms to the URL definitions or specifications at:
>     ◦ https://tools.ietf.org/html/rfc3986
>     ◦ https://en.wikipedia.org/wiki/URL#Syntax
>     ◦ https://en.wikipedia.org/wiki/Uniform_Resource_Identifier#Syntax
>     ◦ https://url.spec.whatwg.org/
> ```

**27.** §5.1, bullet 2 (p. 3) `[none: declarative]`

> A PURL is a valid URL because it is a locator even though it has no Authority URL component: each type has a default repository location when defined.

**28.** §5.1, bullet 3, lead and sub-bullets (p. 3) `[none: declarative]`

> ```text
> • The PURL components are mapped to these URL components:
>     ◦ PURL scheme: this is a URL scheme with a constant value: pkg
>     ◦ PURL type, namespace, name and version components: these are collectively mapped to a URL path
>     ◦ PURL qualifiers: this maps to a URL query
>     ◦ PURL subpath: this is a URL fragment
> ```

**29.** §5.1, bullet 3, closing sentence (p. 3) `[none: declarative]`

> In a PURL, there is no support for a URL Authority (e.g. no username, password, host and port components).

**30.** §5.1, bullet 4, sentence 1 (p. 3) `[none: declarative]`

> Special URL schemes as defined in https://url.spec.whatwg.org/ such as file://, https://, http:// and ftp:// are not valid PURL types.

**31.** §5.1, bullet 4, sentence 2 (p. 3) `[none: declarative]`

> They are valid URL or URI schemes but they are not a valid PURL scheme.

**32.** §5.1, bullet 4, sentence 3 (pp. 3-4) `[may]`

> They may be used to reference URLs in separate attributes outside of a PURL or in a PURL qualifier.

**33.** §5.1, bullet 5, sentence 1 (p. 4) `[none: declarative]`

> Version control system (VCS) URLs such git://, svn://, hg:// or as defined in Python pip or SPDX download locations are not valid PURL types.

**34.** §5.1, bullet 5, sentence 2 (p. 4) `[none: declarative]`

> They are valid URL or URI schemes but they are not a valid PURL scheme.

Bullet 5, sentence 3 is descriptive and is listed under "Informative content
excluded".

**35.** §5.1, bullet 5, sentence 4 (p. 4) `[may]`

> They may be used as references in separate attributes outside of a PURL or in a PURL qualifier.

### 5.2 Permitted characters

**36.** §5.2 (p. 4) `[none: declarative]`

> ```text
> A canonical PURL is composed of these permitted ASCII characters:
> • the Alphanumeric Characters: A to Z, a to z, 0 to 9
> • the Punctuation Characters: .-_~ (period '.', dash '-', underscore '_' and tilde '~')
> • the Percent Character: % (percent sign '%')
> • the Separator Characters :/@?=&# (colon ':', slash '/', at sign '@', question mark '?', equal sign '=', ampersand '&' and hash sign '#')
> ```

### 5.3 Separator characters

**37.** §5.3 (p. 4) `[none: declarative]`

> ```text
> This is how each of the Separator Characters is used:
> • ':' (colon) is the separator between scheme and type
> • '/' (slash) is the separator between type, namespace and name
> • '/' (slash) is the separator between subpath segments
> • '@' (at sign) is the separator between name and version
> • '?' (question mark) is the separator before qualifiers
> • '=' (equals) is the separator between a key and a value of a qualifier
> • '&' (ampersand) is the separator between qualifiers (each being a key=value pair)
> • '#' (hash sign) is the separator before subpath
> ```

### 5.4 Character encoding

**38.** §5.4, bullet 1 (p. 4) `[none: declarative]`

> In the Rules for each PURL component clause, each component defines when and how to apply percent-encoding and decoding to its content.

**39.** §5.4, bullet 2 (p. 4) `[shall]`

> When percent-encoding is required by a component definition, the component string shall first be encoded as UTF-8.

**40.** §5.4, bullet 3 and its sub-bullets (p. 4) `[shall]`

> ```text
> • In the component string, each "data octet" shall be replaced by the percent-encoded "character triplet" applying the percent-encoding mechanism defined in RFC 3986 section 2.1, including the RFC definition of "data octet" and "character triplet", and using these definitions for RFC's "allowed set" and "delimiters":
>     ◦ "allowed set" is composed of the Alphanumeric Characters and the Punctuation Characters
>     ◦ "delimiters" is composed of the Separator Characters
> ```

**41.** §5.4, bullet 4 and its sub-bullets (p. 4) `[shall not]`

> ```text
> • The following characters shall not be percent-encoded:
>     ◦ the Alphanumeric Characters
>     ◦ the Punctuation Characters
>     ◦ the Separator Characters when being used as PURL separators
>     ◦ the colon ':', whether used as a Separator Character or otherwise
>     ◦ the percent sign '%' when used to represent a percent-encoded character
> ```

**42.** §5.4, bullet 5 (p. 4) `[shall]`

> Where the space ' ' is permitted, it shall be percent-encoded as '%20'.

**43.** §5.4, bullet 6 (p. 4) `[none: declarative]`

> With the exception of the percent-encoding mechanism, the rules regarding percent-encoding are defined by this Standard alone.

### 5.5 Case folding

**44.** §5.5, paragraph 1 (p. 4) `[none: declarative]`

> References to "lowercase" in this Standard refer to the culture-invariant full case mapping defined in Section 3.13.2 of the Unicode Standard.

**45.** §5.5, paragraph 2, sentence 1 (p. 4) `[none: declarative]`

> When applied to the ASCII character set, this operation converts uppercase Latin letters (A to Z) to their corresponding lowercase forms (a to z).

**46.** §5.5, paragraph 2, sentence 2 (p. 4) `[none: declarative]`

> All other ASCII characters remain unchanged.

### 5.6 Rules for each PURL component

**47.** §5.6, paragraph 1, sentence 1 (p. 5) `[none: declarative]`

> A PURL string is an ASCII URL string composed of seven components.

**48.** §5.6, paragraph 1, sentence 2 (p. 5) `[none: lead-in]`

> Except as expressly stated otherwise in this Clause, each component:

**49.** §5.6, bullet 1 (p. 5) `[may]`

> may be composed of any of the characters defined in the Permitted characters clause

**50.** §5.6, bullet 2 (p. 5) `[shall]`

> shall be encoded as defined in the Character encoding clause

**51.** §5.6, paragraph 2 (p. 5) `[none: declarative]`

> The "lowercase" rules are defined in the Case folding clause.

**52.** §5.6, paragraph 3 (p. 5) `[none: lead-in]`

> The rules for each component are:

Note: introduces §5.6.1 to §5.6.7.

### 5.6.1 Scheme

**53.** §5.6.1, bullet 1 (p. 5) `[none: declarative]`

> The scheme is a constant with the value "pkg".

**54.** §5.6.1, bullet 2 (p. 5) `[shall]`

> The scheme shall be followed by an unencoded colon ':'.

**55.** §5.6.1, bullet 3 (p. 5) `[shall, shall]`

> PURL parsers shall accept URLs where the scheme and colon ':' are followed by one or more slash '/' characters, such as 'pkg://', and shall ignore and remove all such '/' characters.

### 5.6.2 Type

**56.** §5.6.2, bullet 1 (p. 5) `[shall]`

> The package type shall be composed only of ASCII letters and numbers, period '.', and dash '-'.

**57.** §5.6.2, bullet 2 (p. 5) `[shall]`

> The type shall start with an ASCII letter.

**58.** §5.6.2, bullet 3 (p. 5) `[shall not]`

> The type shall not be percent-encoded.

**59.** §5.6.2, bullet 4, sentence 1 (p. 5) `[none: declarative]`

> The type is case insensitive.

**60.** §5.6.2, bullet 4, sentence 2 (p. 5) `[none: declarative]`

> The canonical form is lowercase.

### 5.6.3 Namespace

**61.** §5.6.3, bullet 1 (p. 5) `[none: declarative]`

> The namespace is optional, unless required by the package's type definition.

**62.** §5.6.3, bullet 2 (p. 5) `[may]`

> If present, the namespace may contain one or more segments, separated by a single unencoded slash '/' character.

**63.** §5.6.3, bullet 3, sentence 1 (p. 5) `[should]`

> All leading and trailing slashes '/' are not significant and should be stripped in the canonical form.

**64.** §5.6.3, bullet 3, sentence 2 (p. 5) `[none: declarative]`

> They are not part of the namespace.

**65.** §5.6.3, bullet 4 (p. 5) `[shall]`

> Each namespace segment shall be a percent-encoded string.

**66.** §5.6.3, bullet 5, lead (p. 5) `[none: lead-in]`

> When percent-decoded, a segment:

**67.** §5.6.3, bullet 5, sub-bullet 1 (p. 5) `[shall not]`

> shall not contain any slash '/' characters

**68.** §5.6.3, bullet 5, sub-bullet 2 (p. 5) `[shall not]`

> shall not be empty

**69.** §5.6.3, bullet 5, sub-bullet 3 (p. 5) `[may]`

> may contain any Unicode character other than '/' unless the package's type definition provides otherwise

**70.** §5.6.3, bullet 6, sentence 1 (p. 5) `[shall not]`

> A URL host or Authority shall not be used as a namespace.

**71.** §5.6.3, bullet 6, sentence 2 (p. 5) `[none: imperative]`

> Use instead a repository_url qualifier.

Note **(inferred)**: an instruction without a verbal form. No qualifier key
"repository_url" is defined in this Standard.

**72.** §5.6.3, bullet 6, sentence 3 (p. 5) `[may]`

> Note however, that for some types, the namespace may look like a host.

Note **(inferred)**: "may" here expresses possibility, not permission.

### 5.6.4 Name

**73.** §5.6.4, bullet 1 (p. 5) `[none: declarative]`

> The name is prefixed by a single slash '/' separator when the namespace is not empty.

**74.** §5.6.4, bullet 2, sentence 1 (p. 5) `[should]`

> All leading and trailing slashes '/' are not significant and should be stripped in the canonical form.

**75.** §5.6.4, bullet 2, sentence 2 (p. 5) `[none: declarative]`

> They are not part of the name.

**76.** §5.6.4, bullet 3 (p. 5) `[shall]`

> A name shall be a percent-encoded string.

**77.** §5.6.4, bullet 4 (p. 5) `[may]`

> When percent-decoded, a name may contain any Unicode character unless the package's type definition provides otherwise.

### 5.6.5 Version

**78.** §5.6.5, bullet 1 (p. 5) `[none: declarative]`

> The version is prefixed by a '@' separator when not empty.

**79.** §5.6.5, bullet 2 (p. 5) `[none: declarative]`

> This '@' is not part of the version.

**80.** §5.6.5, bullet 3 (p. 5) `[shall]`

> A version shall be a percent-encoded string.

**81.** §5.6.5, bullet 4 (pp. 5-6) `[may]`

> When percent-decoded, a version may contain any Unicode character unless the package's type definition provides otherwise.

**82.** §5.6.5, bullet 5 (p. 6) `[none: declarative]`

> A version is a plain and opaque string.

### 5.6.6 Qualifiers

**83.** §5.6.6, bullet 1, sentence 1 (p. 6) `[shall]`

> The qualifiers component shall be prefixed by an unencoded question mark '?' separator when not empty.

**84.** §5.6.6, bullet 1, sentence 2 (p. 6) `[none: declarative]`

> This '?' separator is not part of the qualifiers component.

**85.** §5.6.6, bullet 2, sentence 1 (p. 6) `[none: declarative]`

> The qualifiers component is composed of one or more key=value pairs.

**86.** §5.6.6, bullet 2, sentence 2 (p. 6) `[shall]`

> Multiple key=value pairs shall be separated by an unencoded ampersand '&'.

**87.** §5.6.6, bullet 2, sentence 3 (p. 6) `[none: declarative]`

> This '&' separator is not part of an individual qualifier.

**88.** §5.6.6, bullet 3, sentence 1 (p. 6) `[shall]`

> A key and value shall be separated by the unencoded equal sign '=' character.

**89.** §5.6.6, bullet 3, sentence 2 (p. 6) `[none: declarative]`

> This '=' separator is not part of the key or value.

**90.** §5.6.6, bullet 4 (p. 6) `[shall not]`

> A value shall not be an empty string: a key=value pair with an empty value is the same as if no key=value pair exists for this key.

**91.** §5.6.6, bullet 5, lead (p. 6) `[none: lead-in]`

> For each key=value pair:

**92.** §5.6.6, bullet 5, sub-bullet 1 (p. 6) `[shall]`

> The key shall be composed only of lowercase ASCII letters and numbers, period '.', dash '-' and underscore '_'.

**93.** §5.6.6, bullet 5, sub-bullet 2 (p. 6) `[shall]`

> A key shall start with an ASCII letter.

**94.** §5.6.6, bullet 5, sub-bullet 3 (p. 6) `[shall not]`

> A key shall not be percent-encoded.

**95.** §5.6.6, bullet 5, sub-bullet 4 (p. 6) `[shall]`

> Each key shall be unique among all the keys of the qualifiers component.

**96.** §5.6.6, bullet 5, sub-bullet 5 (p. 6) `[may, shall]`

> A value may contain any Unicode character and all characters shall be encoded as described in the Character encoding clause.

### 5.6.7 Subpath

**97.** §5.6.7, bullet 1 (p. 6) `[none: declarative]`

> The subpath string is prefixed by a '#' separator when not empty.

**98.** §5.6.7, bullet 2 (p. 6) `[none: declarative]`

> The '#' is not part of the subpath.

**99.** §5.6.7, bullet 3 (p. 6) `[none: declarative]`

> The subpath contains zero or more segments, separated by slash '/'.

**100.** §5.6.7, bullet 4 (p. 6) `[should]`

> Leading and trailing slashes '/' are not significant and should be stripped in the canonical form.

**101.** §5.6.7, bullet 5 (p. 6) `[shall]`

> Each subpath segment shall be a percent-encoded string.

**102.** §5.6.7, bullet 6, lead (p. 6) `[none: lead-in]`

> When percent-decoded, a segment:

**103.** §5.6.7, bullet 6, sub-bullet 1 (p. 6) `[shall not]`

> shall not contain any slash '/' characters

**104.** §5.6.7, bullet 6, sub-bullet 2 (p. 6) `[shall not]`

> shall not be empty

**105.** §5.6.7, bullet 6, sub-bullet 3 (p. 6) `[shall not]`

> shall not be any of '..' or '.'

**106.** §5.6.7, bullet 6, sub-bullet 4 (p. 6) `[may]`

> may contain any Unicode character other than '/' unless the package's type definition provides otherwise

**107.** §5.6.7, bullet 7 (p. 6) `[shall]`

> The subpath shall be interpreted as relative to the root of the package.

## 6 Package-URL Type Definition Schema

**108.** §6, paragraph 1, sentence 1 (p. 6) `[none: declarative]`

> The PURL Type Definition JSON Schema is the reference data model that is used to define PURL types in a structured way.

**109.** §6, paragraph 1, sentence 2 (p. 6) `[none: declarative]`

> Each PURL type is specified in a JSON document that matches this schema.

Paragraph 1, sentence 3 states a purpose and is listed under "Informative
content excluded".

**110.** §6, property block (p. 6) `[none: property block]`

> ```text
> Location: /
> Type: Object
> ```

**111.** §6, description (p. 6) `[none: declarative]`

> Schema to specify a Package-URL (PURL) type as a structured definition.

**112.** §6, Table 2 (p. 7) `[none: table cell]`

**Table 2: Properties for the root object**

| Property | Type | Requirement | Description |
|---|---|---|---|
| type | String | Required | The type string for this Package-URL type. |
| type_name | String | Required | The name for this PURL type. |
| description | String | Required | The description of this PURL type. |
| repository | Object | Required | The package repository usage for this PURL type. |
| namespace_definition | Array | Required | Definition of the namespace component for this PURL type. The PURL namespace component shall be required, optional or prohibited for a specific PURL type definition. |
| name_definition | Array | Required | Definition of the name component for this PURL type. The PURL name component is required for all PURL type definitions. |
| version_definition | Array | Optional | Definition of the version component for this PURL type. The PURL version component is optional for a specific PURL type definition. |
| qualifiers_definition | Array | Optional | Definition of the qualifiers specific to this PURL type. The PURL qualifiers component is optional for a specific PURL type, but a qualifiers key or keys may be required for a specific PURL type. |
| subpath_definition | Array | Optional | The definition for the subpath for this PURL type. The PURL subpath component is optional for a specific PURL type definition. |
| examples | Array | Required | Example of valid, canonical PURLs for this package type. |
| note | String | Optional | Note about this PURL type. |
| reference_urls | Array | Optional | Optional list of informational reference URLs about this PURL type. |

**113.** Table 2, row namespace_definition, Description, sentence 2 (p. 7) `[shall]`

> The PURL namespace component shall be required, optional or prohibited for a specific PURL type definition.

Note: the same sentence is statement 132 (§6.5) and statement 290 (Annex A).

**114.** Table 2, row qualifiers_definition, Description, sentence 2 (p. 7) `[may]`

> The PURL qualifiers component is optional for a specific PURL type, but a qualifiers key or keys may be required for a specific PURL type.

Note: the same sentence is statement 223 (§6.8) and statement 291 (Annex A).

### 6.1 PURL type

**115.** §6.1, property block (p. 7) `[none: property block]`

> ```text
> Location: /type
> Property: type (Required)
> Type: String
> Pattern Constraint: ^[a-z][a-z0-9-\.]+$
> ```

**116.** §6.1, description (p. 7) `[none: declarative]`

> The type string for this Package-URL type.

### 6.2 Type name

**117.** §6.2, property block (p. 8) `[none: property block]`

> ```text
> Location: /type_name
> Property: type_name (Required)
> Type: String
> ```

**118.** §6.2, description (p. 8) `[none: declarative]`

> The name for this PURL type.

### 6.3 Description

**119.** §6.3, property block (p. 8) `[none: property block]`

> ```text
> Location: /description
> Property: description (Required)
> Type: String
> ```

**120.** §6.3, description (p. 8) `[none: declarative]`

> The description of this PURL type.

### 6.4 Repository

**121.** §6.4, property block (p. 8) `[none: property block]`

> ```text
> Location: /repository
> Property: repository (Required)
> Type: Object
> ```

**122.** §6.4, description (p. 8) `[none: declarative]`

> The package repository usage for this PURL type.

**123.** §6.4, Table 3 (p. 8) `[none: table cell]`

**Table 3: Properties for the repository object**

| Property | Type | Requirement | Description |
|---|---|---|---|
| use_repository | Boolean | Required | true if this PURL type uses a public package repository. |
| default_repository_url | String | Optional | The default public repository URL for this PURL type. |
| note | String | Optional | Extra note text. |

Note: Table 3 contains no verbal form.

### 6.4.1 Use repository

**124.** §6.4.1, property block (p. 8) `[none: property block]`

> ```text
> Location: /repository/use_repository
> Property: use_repository (Required)
> Type: Boolean
> ```

**125.** §6.4.1, description (p. 8) `[none: declarative]`

> true if this PURL type uses a public package repository.

### 6.4.2 Default repository URL

**126.** §6.4.2, property block (p. 8) `[none: property block]`

> ```text
> Location: /repository/default_repository_url
> Property: default_repository_url (Optional)
> Type: String
> Format: URI as specified in RFC 3986
> ```

**127.** §6.4.2, description (p. 8) `[none: declarative]`

> The default public repository URL for this PURL type.

### 6.4.3 Note

**128.** §6.4.3, property block (p. 9) `[none: property block]`

> ```text
> Location: /repository/note
> Property: note (Optional)
> Type: String
> ```

**129.** §6.4.3, description (p. 9) `[none: declarative]`

> Extra note text.

### 6.5 Namespace definition

**130.** §6.5, property block (p. 9) `[none: property block]`

> ```text
> Location: /namespace_definition
> Property: namespace_definition (Required)
> Type: Object
> ```

**131.** §6.5, description, sentence 1 (p. 9) `[none: declarative]`

> Definition of the namespace component for this PURL type.

**132.** §6.5, description, sentence 2 (p. 9) `[shall]`

> The PURL namespace component shall be required, optional or prohibited for a specific PURL type definition.

**133.** §6.5, Table 4 (p. 9) `[none: table cell]`

**Table 4: Properties for the namespace_definition object**

| Property | Type | Requirement | Description |
|---|---|---|---|
| requirement | Array | Required | States that the PURL namespace component is optional, required or prohibited for a PURL type. |
| permitted_characters | String | Optional | A regular expression (ECMA-262 dialect) defining the 'Permitted characters' for this component of this Package-URL type. If provided, this shall be a subset of the 'Permitted characters' defined in the PURL specification. |
| case_sensitive | Boolean | Optional | true if this PURL component is case sensitive. If false, the canonical form shall be lowercased. |
| normalization_rules | Array | Optional | List of rules to normalize this component for this PURL type. These are plain text, unstructured rules as some require programming and cannot be enforced only with a schema. Tools are expected to apply these rules programmatically. |
| native_name | String | Optional | The native name of this PURL component in the package ecosystem. For instance, the 'namespace' for the 'maven' type is 'groupId', and 'scope' for the 'npm' PURL type. |
| note | String | Optional | Extra note text. |

**134.** Table 4, row permitted_characters, Description, sentence 2 (p. 9) `[shall]`

> If provided, this shall be a subset of the 'Permitted characters' defined in the PURL specification.

**135.** Table 4, row case_sensitive, Description, sentence 2 (p. 9) `[shall]`

> If false, the canonical form shall be lowercased.

**136.** Table 4, row normalization_rules, Description, sentence 2 (p. 9) `[cannot]`

> These are plain text, unstructured rules as some require programming and cannot be enforced only with a schema.

### 6.5.1 Namespace requirement

**137.** §6.5.1, property block (p. 9) `[none: property block]`

> ```text
> Location: /namespace_definition/requirement
> Property: requirement (Required)
> Type: String
> ```

**138.** §6.5.1, description (p. 9) `[none: declarative]`

> States that the PURL namespace component is optional, required or prohibited for a PURL type.

**139.** §6.5.1, "Shall be one of" list (p. 9) `[shall]`

> ```text
> Shall be one of:
>
>  1. Component optional requirement
>  2. Component required requirement
>  3. Component prohibited requirement
> ```

Note: the three items name §6.5.2, §6.5.3 and §6.5.4.

### 6.5.2 Component optional requirement

**140.** §6.5.2, property block (p. 10) `[none: property block]`

> ```text
> Type: String
> Constant: optional
> ```

**141.** §6.5.2, description (p. 10) `[none: declarative]`

> States that this PURL component is optional for a PURL type.

### 6.5.3 Component required requirement

**142.** §6.5.3, property block (p. 10) `[none: property block]`

> ```text
> Type: String
> Constant: required
> ```

**143.** §6.5.3, description (p. 10) `[none: declarative]`

> States that this PURL component is required for a PURL type.

### 6.5.4 Component prohibited requirement

**144.** §6.5.4, property block (p. 10) `[none: property block]`

> ```text
> Type: String
> Constant: prohibited
> ```

**145.** §6.5.4, description (p. 10) `[none: declarative]`

> States that this PURL component is prohibited for a PURL type.

### 6.5.5 Permitted characters in this PURL component

**146.** §6.5.5, property block (p. 10) `[none: property block]`

> ```text
> Location: /namespace_definition/permitted_characters
> Property: permitted_characters (Optional)
> Type: String
> Format: A regular expression dialect defined by ECMA-262
> ```

**147.** §6.5.5, description, sentence 1 (p. 10) `[none: declarative]`

> A regular expression (ECMA-262 dialect) defining the 'Permitted characters' for this component of this Package-URL type.

**148.** §6.5.5, description, sentence 2 (p. 10) `[shall]`

> If provided, this shall be a subset of the 'Permitted characters' defined in the PURL specification.

### 6.5.6 Case sensitive

**149.** §6.5.6, property block (p. 10) `[none: property block]`

> ```text
> Location: /namespace_definition/case_sensitive
> Property: case_sensitive (Optional)
> Type: Boolean
> Default Value: true
> ```

**150.** §6.5.6, description, sentence 1 (p. 10) `[none: declarative]`

> true if this PURL component is case sensitive.

**151.** §6.5.6, description, sentence 2 (p. 10) `[shall]`

> If false, the canonical form shall be lowercased.

### 6.5.7 Normalization rules

**152.** §6.5.7, property block (p. 10) `[none: property block]`

> ```text
> Location: /namespace_definition/normalization_rules
> Property: normalization_rules (Optional)
> Type: array (of String)
> ```

**153.** §6.5.7, description, sentence 1 (p. 10) `[none: declarative]`

> List of rules to normalize this component for this PURL type.

**154.** §6.5.7, description, sentence 2 (p. 10) `[cannot]`

> These are plain text, unstructured rules as some require programming and cannot be enforced only with a schema.

**155.** §6.5.7, description, sentence 3 (p. 10) `[none: declarative]`

> Tools are expected to apply these rules programmatically.

Note **(inferred)**: an expectation without a verbal form; it is not stated as a
requirement.

**156.** §6.5.7, description, sentence 4 (p. 10) `[shall]`

> Each item of this array shall be a string.

**157.** §6.5.7, closing line (p. 10) `[shall]`

> All items shall be unique.

### 6.5.8 Native name

**158.** §6.5.8, property block (p. 11) `[none: property block]`

> ```text
> Location: /namespace_definition/native_name
> Property: native_name (Optional)
> Type: String
> ```

**159.** §6.5.8, description, sentence 1 (p. 11) `[none: declarative]`

> The native name of this PURL component in the package ecosystem.

**160.** §6.5.8, description, sentence 2 (p. 11) `[none: declarative]`

> For instance, the 'namespace' for the 'maven' type is 'groupId', and 'scope' for the 'npm' PURL type.

Note: an illustration inside the description; it is not marked "(Informative)".

### 6.5.9 Note

**161.** §6.5.9, property block (p. 11) `[none: property block]`

> ```text
> Location: /namespace_definition/note
> Property: note (Optional)
> Type: String
> ```

**162.** §6.5.9, description (p. 11) `[none: declarative]`

> Extra note text.

### 6.6 Name definition

**163.** §6.6, property block (p. 11) `[none: property block]`

> ```text
> Location: /name_definition
> Property: name_definition (Required)
> Type: Object
> ```

**164.** §6.6, description, sentence 1 (p. 11) `[none: declarative]`

> Definition of the name component for this PURL type.

**165.** §6.6, description, sentence 2 (p. 11) `[none: declarative]`

> The PURL name component is required for all PURL type definitions.

**166.** §6.6, Table 5 (p. 11) `[none: table cell]`

**Table 5: Properties for the name_definition object**

| Property | Type | Requirement | Description |
|---|---|---|---|
| requirement | Array | Required | States that the PURL name component is always required. |
| permitted_characters | String | Optional | A regular expression (ECMA-262 dialect) defining the 'Permitted characters' for this component of this Package-URL type. If provided, this shall be a subset of the 'Permitted characters' defined in the PURL specification. |
| case_sensitive | Boolean | Optional | true if this PURL component is case sensitive. If false, the canonical form shall be lowercased. |
| normalization_rules | Array | Optional | List of rules to normalize this component for this PURL type. These are plain text, unstructured rules as some require programming and cannot be enforced only with a schema. Tools are expected to apply these rules programmatically. |
| native_name | String | Optional | The native name of this PURL component in the package ecosystem. For instance, the 'namespace' for the 'maven' type is 'groupId', and 'scope' for the 'npm' PURL type. |
| note | String | Optional | Extra note text. |

**167.** Table 5, row permitted_characters, Description, sentence 2 (p. 11) `[shall]`

> If provided, this shall be a subset of the 'Permitted characters' defined in the PURL specification.

**168.** Table 5, row case_sensitive, Description, sentence 2 (p. 11) `[shall]`

> If false, the canonical form shall be lowercased.

**169.** Table 5, row normalization_rules, Description, sentence 2 (p. 11) `[cannot]`

> These are plain text, unstructured rules as some require programming and cannot be enforced only with a schema.

### 6.6.1 Name component requirement

**170.** §6.6.1, property block (p. 12) `[none: property block]`

> ```text
> Location: /name_definition/requirement
> Property: requirement (Required)
> Type: String
> ```

**171.** §6.6.1, description (p. 12) `[none: declarative]`

> States that the PURL name component is always required.

**172.** §6.6.1, "Shall be one of" list (p. 12) `[shall]`

> ```text
> Shall be one of:
>
> 1. Component required requirement
> ```

### 6.6.2 Component required requirement

**173.** §6.6.2, property block (p. 12) `[none: property block]`

> ```text
> Type: String
> Constant: required
> ```

**174.** §6.6.2, description (p. 12) `[none: declarative]`

> States that this PURL component is required for a PURL type.

### 6.6.3 Permitted characters in this PURL component

**175.** §6.6.3, property block (p. 12) `[none: property block]`

> ```text
> Location: /name_definition/permitted_characters
> Property: permitted_characters (Optional)
> Type: String
> Format: A regular expression dialect defined by ECMA-262
> ```

**176.** §6.6.3, description, sentence 1 (p. 12) `[none: declarative]`

> A regular expression (ECMA-262 dialect) defining the 'Permitted characters' for this component of this Package-URL type.

**177.** §6.6.3, description, sentence 2 (p. 12) `[shall]`

> If provided, this shall be a subset of the 'Permitted characters' defined in the PURL specification.

### 6.6.4 Case sensitive

**178.** §6.6.4, property block (p. 12) `[none: property block]`

> ```text
> Location: /name_definition/case_sensitive
> Property: case_sensitive (Optional)
> Type: Boolean
> Default Value: true
> ```

**179.** §6.6.4, description, sentence 1 (p. 12) `[none: declarative]`

> true if this PURL component is case sensitive.

**180.** §6.6.4, description, sentence 2 (p. 12) `[shall]`

> If false, the canonical form shall be lowercased.

### 6.6.5 Normalization rules

**181.** §6.6.5, property block (p. 12) `[none: property block]`

> ```text
> Location: /name_definition/normalization_rules
> Property: normalization_rules (Optional)
> Type: array (of String)
> ```

**182.** §6.6.5, description, sentence 1 (p. 12) `[none: declarative]`

> List of rules to normalize this component for this PURL type.

**183.** §6.6.5, description, sentence 2 (p. 12) `[cannot]`

> These are plain text, unstructured rules as some require programming and cannot be enforced only with a schema.

**184.** §6.6.5, description, sentence 3 (p. 12) `[none: declarative]`

> Tools are expected to apply these rules programmatically.

**185.** §6.6.5, description, sentence 4 (p. 12) `[shall]`

> Each item of this array shall be a string.

**186.** §6.6.5, closing line (p. 12) `[shall]`

> All items shall be unique.

### 6.6.6 Native name

**187.** §6.6.6, property block (p. 12) `[none: property block]`

> ```text
> Location: /name_definition/native_name
> Property: native_name (Optional)
> Type: String
> ```

**188.** §6.6.6, description, sentence 1 (p. 12) `[none: declarative]`

> The native name of this PURL component in the package ecosystem.

**189.** §6.6.6, description, sentence 2 (p. 12) `[none: declarative]`

> For instance, the 'namespace' for the 'maven' type is 'groupId', and 'scope' for the 'npm' PURL type.

### 6.6.7 Note

**190.** §6.6.7, property block (p. 13) `[none: property block]`

> ```text
> Location: /name_definition/note
> Property: note (Optional)
> Type: String
> ```

**191.** §6.6.7, description (p. 13) `[none: declarative]`

> Extra note text.

### 6.7 Version definition

**192.** §6.7, property block (p. 13) `[none: property block]`

> ```text
> Location: /version_definition
> Property: version_definition (Optional)
> Type: Object
> ```

**193.** §6.7, description, sentence 1 (p. 13) `[none: declarative]`

> Definition of the version component for this PURL type.

**194.** §6.7, description, sentence 2 (p. 13) `[none: declarative]`

> The PURL version component is optional for a specific PURL type definition.

**195.** §6.7, Table 6 (p. 13) `[none: table cell]`

**Table 6: Properties for the version_definition object**

| Property | Type | Requirement | Description |
|---|---|---|---|
| requirement | Array | Required | States that the PURL version is optional. |
| permitted_characters | String | Optional | A regular expression (ECMA-262 dialect) defining the 'Permitted characters' for this component of this Package-URL type. If provided, this shall be a subset of the 'Permitted characters' defined in the PURL specification. |
| case_sensitive | Boolean | Optional | true if this PURL component is case sensitive. If false, the canonical form shall be lowercased. |
| normalization_rules | Array | Optional | List of rules to normalize this component for this PURL type. These are plain text, unstructured rules as some require programming and cannot be enforced only with a schema. Tools are expected to apply these rules programmatically. |
| native_name | String | Optional | The native name of this PURL component in the package ecosystem. For instance, the 'namespace' for the 'maven' type is 'groupId', and 'scope' for the 'npm' PURL type. |
| note | String | Optional | Extra note text. |

**196.** Table 6, row permitted_characters, Description, sentence 2 (p. 13) `[shall]`

> If provided, this shall be a subset of the 'Permitted characters' defined in the PURL specification.

**197.** Table 6, row case_sensitive, Description, sentence 2 (p. 13) `[shall]`

> If false, the canonical form shall be lowercased.

**198.** Table 6, row normalization_rules, Description, sentence 2 (p. 13) `[cannot]`

> These are plain text, unstructured rules as some require programming and cannot be enforced only with a schema.

### 6.7.1 Version requirement

**199.** §6.7.1, property block (p. 13) `[none: property block]`

> ```text
> Location: /version_definition/requirement
> Property: requirement (Required)
> Type: String
> ```

**200.** §6.7.1, description (p. 13) `[none: declarative]`

> States that the PURL version is optional.

**201.** §6.7.1, "Shall be one of" list (p. 13) `[shall]`

> ```text
> Shall be one of:
>
>  1. Component optional requirement
> ```

### 6.7.2 Component optional requirement

**202.** §6.7.2, property block (p. 13) `[none: property block]`

> ```text
> Type: String
> Constant: optional
> ```

**203.** §6.7.2, description (p. 13) `[none: declarative]`

> States that this PURL component is optional for a PURL type.

### 6.7.3 Permitted characters in this PURL component

**204.** §6.7.3, property block (p. 14) `[none: property block]`

> ```text
> Location: /version_definition/permitted_characters
> Property: permitted_characters (Optional)
> Type: String
> Format: A regular expression dialect defined by ECMA-262
> ```

**205.** §6.7.3, description, sentence 1 (p. 14) `[none: declarative]`

> A regular expression (ECMA-262 dialect) defining the 'Permitted characters' for this component of this Package-URL type.

**206.** §6.7.3, description, sentence 2 (p. 14) `[shall]`

> If provided, this shall be a subset of the 'Permitted characters' defined in the PURL specification.

### 6.7.4 Case sensitive

**207.** §6.7.4, property block (p. 14) `[none: property block]`

> ```text
> Location: /version_definition/case_sensitive
> Property: case_sensitive (Optional)
> Type: Boolean
> Default Value: true
> ```

**208.** §6.7.4, description, sentence 1 (p. 14) `[none: declarative]`

> true if this PURL component is case sensitive.

**209.** §6.7.4, description, sentence 2 (p. 14) `[shall]`

> If false, the canonical form shall be lowercased.

### 6.7.5 Normalization rules

**210.** §6.7.5, property block (p. 14) `[none: property block]`

> ```text
> Location: /version_definition/normalization_rules
> Property: normalization_rules (Optional)
> Type: array (of String)
> ```

**211.** §6.7.5, description, sentence 1 (p. 14) `[none: declarative]`

> List of rules to normalize this component for this PURL type.

**212.** §6.7.5, description, sentence 2 (p. 14) `[cannot]`

> These are plain text, unstructured rules as some require programming and cannot be enforced only with a schema.

**213.** §6.7.5, description, sentence 3 (p. 14) `[none: declarative]`

> Tools are expected to apply these rules programmatically.

**214.** §6.7.5, description, sentence 4 (p. 14) `[shall]`

> Each item of this array shall be a string.

**215.** §6.7.5, closing line (p. 14) `[shall]`

> All items shall be unique.

### 6.7.6 Native name

**216.** §6.7.6, property block (p. 14) `[none: property block]`

> ```text
> Location: /version_definition/native_name
> Property: native_name (Optional)
> Type: String
> ```

**217.** §6.7.6, description, sentence 1 (p. 14) `[none: declarative]`

> The native name of this PURL component in the package ecosystem.

**218.** §6.7.6, description, sentence 2 (p. 14) `[none: declarative]`

> For instance, the 'namespace' for the 'maven' type is 'groupId', and 'scope' for the 'npm' PURL type.

### 6.7.7 Note

**219.** §6.7.7, property block (p. 14) `[none: property block]`

> ```text
> Location: /version_definition/note
> Property: note (Optional)
> Type: String
> ```

**220.** §6.7.7, description (p. 14) `[none: declarative]`

> Extra note text.

### 6.8 Qualifiers definition

**221.** §6.8, property block (p. 14) `[none: property block]`

> ```text
> Location: /qualifiers_definition
> Property: qualifiers_definition (Optional)
> Type: Array
> ```

**222.** §6.8, description, sentence 1 (p. 14) `[none: declarative]`

> Definition of the qualifiers specific to this PURL type.

**223.** §6.8, description, sentence 2 (p. 14) `[may]`

> The PURL qualifiers component is optional for a specific PURL type, but a qualifiers key or keys may be required for a specific PURL type.

**224.** §6.8, description, sentence 3 (p. 14) `[shall]`

> Each item of this array shall be a Qualifiers definition object.

### 6.8.1 Qualifiers definition

**225.** §6.8.1, property block (p. 15) `[none: property block]`

> ```text
> Location: /qualifiers_definition/[]
> Type: Object
> ```

**226.** §6.8.1, description (p. 15) `[none: declarative]`

> The definition of a qualifier specific to this PURL type.

**227.** §6.8.1, Table 7 (p. 15) `[none: table cell]`

**Table 7: Properties for the qualifiers_definition object**

| Property | Type | Requirement | Description |
|---|---|---|---|
| key | String | Required | The key for the qualifier. |
| requirement | Array | Optional | States that a PURL qualifier key is optional or required for a PURL type. |
| description | String | Required | The description of this qualifier. |
| default_value | String | Optional | The optional default value of this qualifier if not provided. |
| native_name | String | Optional | The equivalent native name for this qualifier key. |

Note: Table 7 contains no verbal form. The §6.8.1.1 to §6.8.1.7 property blocks
have no "Property:" line, so Table 7 (and Annex A) is the only Clause 6 source
of whether each qualifier property is required.

### 6.8.1.1 Qualifier key

**228.** §6.8.1.1, property block (p. 15) `[none: property block]`

> ```text
> Location: /qualifiers_definition/[]/key
> Type: String
> ```

**229.** §6.8.1.1, description (p. 15) `[none: declarative]`

> The key for the qualifier.

### 6.8.1.2 Qualifier key requirement

**230.** §6.8.1.2, property block (p. 15) `[none: property block]`

> ```text
> Location: /qualifiers_definition/[]/requirement
> Type: String
> ```

**231.** §6.8.1.2, description (p. 15) `[none: declarative]`

> States that a PURL qualifier key is optional or required for a PURL type.

**232.** §6.8.1.2, "Shall be one of" list (p. 15) `[shall]`

> ```text
> Shall be one of:
>
>  1. Component optional requirement
>  2. Component required requirement
> ```

### 6.8.1.3 Component optional requirement

**233.** §6.8.1.3, property block (p. 15) `[none: property block]`

> ```text
> Type: String
> Constant: optional
> ```

**234.** §6.8.1.3, description (p. 15) `[none: declarative]`

> States that this PURL component is optional for a PURL type.

### 6.8.1.4 Component required requirement

**235.** §6.8.1.4, property block (p. 15) `[none: property block]`

> ```text
> Type: String
> Constant: required
> ```

**236.** §6.8.1.4, description (p. 15) `[none: declarative]`

> States that this PURL component is required for a PURL type.

### 6.8.1.5 Description

**237.** §6.8.1.5, property block (p. 16) `[none: property block]`

> ```text
> Location: /qualifiers_definition/[]/description
> Type: String
> ```

**238.** §6.8.1.5, description (p. 16) `[none: declarative]`

> The description of this qualifier.

### 6.8.1.6 Default value

**239.** §6.8.1.6, property block (p. 16) `[none: property block]`

> ```text
> Location: /qualifiers_definition/[]/default_value
> Type: String
> ```

**240.** §6.8.1.6, description (p. 16) `[none: declarative]`

> The optional default value of this qualifier if not provided.

### 6.8.1.7 Native name

**241.** §6.8.1.7, property block (p. 16) `[none: property block]`

> ```text
> Location: /qualifiers_definition/[]/native_name
> Type: String
> ```

**242.** §6.8.1.7, description (p. 16) `[none: declarative]`

> The equivalent native name for this qualifier key.

**243.** §6.8.1.7, closing line (p. 16) `[shall]`

> All items shall be unique.

Note: printed under "Native name" (a String), but the only array in §6.8 is
qualifiers_definition; see Inconsistencies observed, U-1.

### 6.9 Subpath definition

**244.** §6.9, property block (p. 16) `[none: property block]`

> ```text
> Location: /subpath_definition
> Property: subpath_definition (Optional)
> Type: Object
> ```

**245.** §6.9, description, sentence 1 (p. 16) `[none: declarative]`

> The definition for the subpath for this PURL type.

**246.** §6.9, description, sentence 2 (p. 16) `[none: declarative]`

> The PURL subpath component is optional for a specific PURL type definition.

**247.** §6.9, Table 8 (p. 16) `[none: table cell]`

**Table 8: Properties for the subpath_definition object**

| Property | Type | Requirement | Description |
|---|---|---|---|
| requirement | Array | Required | States that the PURL subpath is optional. |
| permitted_characters | String | Optional | A regular expression (ECMA-262 dialect) defining the 'Permitted characters' for this component of this Package-URL type. If provided, this shall be a subset of the 'Permitted characters' defined in the PURL specification. |
| case_sensitive | Boolean | Optional | true if this PURL component is case sensitive. If false, the canonical form shall be lowercased. |
| normalization_rules | Array | Optional | List of rules to normalize this component for this PURL type. These are plain text, unstructured rules as some require programming and cannot be enforced only with a schema. Tools are expected to apply these rules programmatically. |
| native_name | String | Optional | The native name of this PURL component in the package ecosystem. For instance, the 'namespace' for the 'maven' type is 'groupId', and 'scope' for the 'npm' PURL type. |
| note | String | Optional | Extra note text. |

**248.** Table 8, row permitted_characters, Description, sentence 2 (p. 16) `[shall]`

> If provided, this shall be a subset of the 'Permitted characters' defined in the PURL specification.

**249.** Table 8, row case_sensitive, Description, sentence 2 (p. 16) `[shall]`

> If false, the canonical form shall be lowercased.

**250.** Table 8, row normalization_rules, Description, sentence 2 (p. 16) `[cannot]`

> These are plain text, unstructured rules as some require programming and cannot be enforced only with a schema.

### 6.9.1 Subpath requirement

**251.** §6.9.1, property block (p. 17) `[none: property block]`

> ```text
> Location: /subpath_definition/requirement
> Property: requirement (Required)
> Type: String
> ```

**252.** §6.9.1, description (p. 17) `[none: declarative]`

> States that the PURL subpath is optional.

**253.** §6.9.1, "Shall be one of" list (p. 17) `[shall]`

> ```text
> Shall be one of:
>
>  1. Component optional requirement
> ```

### 6.9.2 Component optional requirement

**254.** §6.9.2, property block (p. 17) `[none: property block]`

> ```text
> Type: String
> Constant: optional
> ```

**255.** §6.9.2, description (p. 17) `[none: declarative]`

> States that this PURL component is optional for a PURL type.

### 6.9.3 Permitted characters in this PURL component

**256.** §6.9.3, property block (p. 17) `[none: property block]`

> ```text
> Location: /subpath_definition/permitted_characters
> Property: permitted_characters (Optional)
> Type: String
> Format: A regular expression dialect defined by ECMA-262
> ```

**257.** §6.9.3, description, sentence 1 (p. 17) `[none: declarative]`

> A regular expression (ECMA-262 dialect) defining the 'Permitted characters' for this component of this Package-URL type.

**258.** §6.9.3, description, sentence 2 (p. 17) `[shall]`

> If provided, this shall be a subset of the 'Permitted characters' defined in the PURL specification.

### 6.9.4 Case sensitive

**259.** §6.9.4, property block (p. 17) `[none: property block]`

> ```text
> Location: /subpath_definition/case_sensitive
> Property: case_sensitive (Optional)
> Type: Boolean
> Default Value: true
> ```

**260.** §6.9.4, description, sentence 1 (p. 17) `[none: declarative]`

> true if this PURL component is case sensitive.

**261.** §6.9.4, description, sentence 2 (p. 17) `[shall]`

> If false, the canonical form shall be lowercased.

### 6.9.5 Normalization rules

**262.** §6.9.5, property block (p. 17) `[none: property block]`

> ```text
> Location: /subpath_definition/normalization_rules
> Property: normalization_rules (Optional)
> Type: array (of String)
> ```

**263.** §6.9.5, description, sentence 1 (p. 17) `[none: declarative]`

> List of rules to normalize this component for this PURL type.

**264.** §6.9.5, description, sentence 2 (p. 17) `[cannot]`

> These are plain text, unstructured rules as some require programming and cannot be enforced only with a schema.

**265.** §6.9.5, description, sentence 3 (p. 17) `[none: declarative]`

> Tools are expected to apply these rules programmatically.

**266.** §6.9.5, description, sentence 4 (p. 17) `[shall]`

> Each item of this array shall be a string.

**267.** §6.9.5, closing line (p. 17) `[shall]`

> All items shall be unique.

### 6.9.6 Native name

**268.** §6.9.6, property block (p. 17) `[none: property block]`

> ```text
> Location: /subpath_definition/native_name
> Property: native_name (Optional)
> Type: String
> ```

**269.** §6.9.6, description, sentence 1 (p. 17) `[none: declarative]`

> The native name of this PURL component in the package ecosystem.

**270.** §6.9.6, description, sentence 2 (p. 17) `[none: declarative]`

> For instance, the 'namespace' for the 'maven' type is 'groupId', and 'scope' for the 'npm' PURL type.

### 6.9.7 Note

**271.** §6.9.7, property block (p. 18) `[none: property block]`

> ```text
> Location: /subpath_definition/note
> Property: note (Optional)
> Type: String
> ```

**272.** §6.9.7, description (p. 18) `[none: declarative]`

> Extra note text.

### 6.10 PURL examples

**273.** §6.10, property block (p. 18) `[none: property block]`

> ```text
> Location: /examples
> Property: examples (Required)
> Type: array (of String)
> Pattern Constraint: ^pkg:[a-z][a-z0-9-\.]+/.*$
> ```

**274.** §6.10, description, sentence 1 (p. 18) `[none: declarative]`

> Example of valid, canonical PURLs for this package type.

**275.** §6.10, description, sentence 2 (p. 18) `[shall]`

> Each item of this array shall be a string.

**276.** §6.10, closing line (p. 18) `[shall]`

> All items shall be unique.

### 6.11 Note

**277.** §6.11, property block (p. 18) `[none: property block]`

> ```text
> Location: /note
> Property: note (Optional)
> Type: String
> ```

**278.** §6.11, description (p. 18) `[none: declarative]`

> Note about this PURL type.

### 6.12 Reference URLs

**279.** §6.12, property block (p. 18) `[none: property block]`

> ```text
> Location: /reference_urls
> Property: reference_urls (Optional)
> Type: array (of String)
> Format: URI as specified in RFC 3986
> ```

**280.** §6.12, description, sentence 1 (p. 18) `[none: declarative]`

> Optional list of informational reference URLs about this PURL type.

**281.** §6.12, description, sentence 2 (p. 18) `[shall]`

> Each item of this array shall be a string.

**282.** §6.12, closing line (p. 18) `[shall]`

> All items shall be unique.

## Annex A (normative) PURL Type Definition

Annex A (pp. 19 to 25) is normative. The schema itself is not copied here: the
schema artifact (`distilled/schema/`) carries it verbatim. This section records
the Annex's introductory sentences, every constraint keyword with its JSON
Pointer and value, and every description-string sentence that contains a verbal
form. JSON Pointers (RFC 6901) are relative to the schema document root.

### Annex A introductory text

**283.** Annex A, heading (p. 19) `[none: declarative]`

> Annex A
> (normative)
>
> PURL Type Definition

**284.** Annex A, paragraph 1, sentence 1 (p. 19) `[none: declarative]`

> This Annex provides a copy of the current Package-URL Type Definition Schema.

**285.** Annex A, paragraph 1, sentence 2 (p. 19) `[none: declarative]`

> The format is JSON Schema version draft-07.

**286.** Annex A, paragraph 2 (p. 19) `[none: declarative]`

> The schema shown below is available in electronic form at: https://github.com/package-url/purl-spec/blob/main/schemas/purl-type-definition.schema.json

Schema identification (root keywords, p. 19, verbatim values):

| JSON pointer | keyword | value |
|---|---|---|
| `/$schema` | $schema | `"http://json-schema.org/draft-07/schema#"` |
| `/$id` | $id | `"https://packageurl.org/schemas/purl-type-definition.schema-1.0.json"` |
| `/title` | title | `"Package-URL Type Definition"` |

### Annex A constraint keywords

All 38 occurrences of the keywords required, const, pattern, uniqueItems,
minItems, additionalProperties, additionalItems, oneOf, allOf, format and
default, in document order. Counts: required 7, oneOf 5, const 4, format 4,
uniqueItems 4, allOf 4, additionalProperties 3, pattern 3, default 2,
additionalItems 1, minItems 1. Values are re-serialised compactly from the
parsed schema; every string is character-identical to the source (JSON
escaping kept, so `\\` is one backslash in the value).

| # | JSON pointer | keyword | value | page |
|---|---|---|---|---|
| K1 | `/additionalProperties` | additionalProperties | `false` | 19 |
| K2 | `/definitions/optional_requirement/const` | const | `"optional"` | 19 |
| K3 | `/definitions/required_requirement/const` | const | `"required"` | 19 |
| K4 | `/definitions/prohibited_requirement/const` | const | `"prohibited"` | 19 |
| K5 | `/definitions/purl_component_definition/properties/permitted_characters/format` | format | `"regex"` | 19 |
| K6 | `/definitions/purl_component_definition/properties/case_sensitive/default` | default | `true` | 20 |
| K7 | `/definitions/purl_component_definition/properties/normalization_rules/uniqueItems` | uniqueItems | `true` | 20 |
| K8 | `/required` | required | `["$id", "type", "type_name", "description", "repository", "namespace_definition", "name_definition", "examples"]` | 20 |
| K9 | `/properties/$schema/const` | const | `"https://packageurl.org/schemas/purl-type-definition.schema-1.0.json"` | 20 |
| K10 | `/properties/$schema/format` | format | `"uri"` | 20 |
| K11 | `/properties/$id/pattern` | pattern | `"^https:\\/\\/packageurl\\.org/types/[a-z0-9-]+-definition\\.json$"` | 20 |
| K12 | `/properties/type/pattern` | pattern | `"^[a-z][a-z0-9-\\.]+$"` | 21 |
| K13 | `/properties/repository/additionalProperties` | additionalProperties | `false` | 21 |
| K14 | `/properties/repository/required` | required | `["use_repository"]` | 21 |
| K15 | `/properties/repository/properties/use_repository/default` | default | `false` | 21 |
| K16 | `/properties/repository/properties/default_repository_url/format` | format | `"uri"` | 21 |
| K17 | `/properties/namespace_definition/required` | required | `["requirement"]` | 21 |
| K18 | `/properties/namespace_definition/properties/requirement/oneOf` | oneOf | `[{"$ref": "#/definitions/optional_requirement"}, {"$ref": "#/definitions/required_requirement"}, {"$ref": "#/definitions/prohibited_requirement"}]` | 22 |
| K19 | `/properties/namespace_definition/allOf` | allOf | `[{"$ref": "#/definitions/purl_component_definition"}]` | 22 |
| K20 | `/properties/name_definition/required` | required | `["requirement"]` | 22 |
| K21 | `/properties/name_definition/properties/requirement/oneOf` | oneOf | `[{"$ref": "#/definitions/required_requirement"}]` | 22 |
| K22 | `/properties/name_definition/allOf` | allOf | `[{"$ref": "#/definitions/purl_component_definition"}]` | 22 |
| K23 | `/properties/version_definition/required` | required | `["requirement"]` | 22 |
| K24 | `/properties/version_definition/properties/requirement/oneOf` | oneOf | `[{"$ref": "#/definitions/optional_requirement"}]` | 23 |
| K25 | `/properties/version_definition/allOf` | allOf | `[{"$ref": "#/definitions/purl_component_definition"}]` | 23 |
| K26 | `/properties/qualifiers_definition/additionalItems` | additionalItems | `false` | 23 |
| K27 | `/properties/qualifiers_definition/uniqueItems` | uniqueItems | `true` | 23 |
| K28 | `/properties/qualifiers_definition/items/additionalProperties` | additionalProperties | `false` | 23 |
| K29 | `/properties/qualifiers_definition/items/required` | required | `["key", "description"]` | 23 |
| K30 | `/properties/qualifiers_definition/items/properties/requirement/oneOf` | oneOf | `[{"$ref": "#/definitions/optional_requirement"}, {"$ref": "#/definitions/required_requirement"}]` | 23 |
| K31 | `/properties/subpath_definition/required` | required | `["requirement"]` | 24 |
| K32 | `/properties/subpath_definition/properties/requirement/oneOf` | oneOf | `[{"$ref": "#/definitions/optional_requirement"}]` | 24 |
| K33 | `/properties/subpath_definition/allOf` | allOf | `[{"$ref": "#/definitions/purl_component_definition"}]` | 24 |
| K34 | `/properties/examples/uniqueItems` | uniqueItems | `true` | 24 |
| K35 | `/properties/examples/minItems` | minItems | `1` | 24 |
| K36 | `/properties/examples/items/pattern` | pattern | `"^pkg:[a-z][a-z0-9-\\.]+/.*$"` | 24 |
| K37 | `/properties/reference_urls/uniqueItems` | uniqueItems | `true` | 24 |
| K38 | `/properties/reference_urls/items/format` | format | `"uri"` | 25 |

### Annex A type keywords

The `type` keyword is also a validation constraint; its 39 occurrences are
grouped by value. `/properties/$schema` has no `type` keyword.

| value | count | JSON pointers (page) |
|---|---|---|
| `"object"` | 8 | `/type` (19), `/definitions/purl_component_definition/type` (19), `/properties/repository/type` (21), `/properties/namespace_definition/type` (21), `/properties/name_definition/type` (22), `/properties/version_definition/type` (22), `/properties/qualifiers_definition/items/type` (23), `/properties/subpath_definition/type` (24) |
| `"array"` | 4 | `/definitions/purl_component_definition/properties/normalization_rules/type` (20), `/properties/qualifiers_definition/type` (23), `/properties/examples/type` (24), `/properties/reference_urls/type` (24) |
| `"boolean"` | 2 | `/definitions/purl_component_definition/properties/case_sensitive/type` (20), `/properties/repository/properties/use_repository/type` (21) |
| `"string"` | 25 | `/definitions/optional_requirement/type` (19), `/definitions/required_requirement/type` (19), `/definitions/prohibited_requirement/type` (19), `/definitions/purl_component_definition/properties/permitted_characters/type` (19), `/definitions/purl_component_definition/properties/normalization_rules/items/type` (20), `/definitions/purl_component_definition/properties/native_name/type` (20), `/definitions/purl_component_definition/properties/note/type` (20), `/properties/$id/type` (20), `/properties/type/type` (21), `/properties/type_name/type` (21), `/properties/description/type` (21), `/properties/repository/properties/default_repository_url/type` (21), `/properties/repository/properties/note/type` (21), `/properties/namespace_definition/properties/requirement/type` (22), `/properties/name_definition/properties/requirement/type` (22), `/properties/version_definition/properties/requirement/type` (23), `/properties/qualifiers_definition/items/properties/key/type` (23), `/properties/qualifiers_definition/items/properties/requirement/type` (23), `/properties/qualifiers_definition/items/properties/description/type` (23), `/properties/qualifiers_definition/items/properties/default_value/type` (24), `/properties/qualifiers_definition/items/properties/native_name/type` (24), `/properties/subpath_definition/properties/requirement/type` (24), `/properties/examples/items/type` (24), `/properties/note/type` (24), `/properties/reference_urls/items/type` (25) |

### Annex A description strings with a verbal form

In JSON Schema, `description` is an annotation with no validation effect, but
these strings are part of a normative annex. Five of the 37 description strings
contain a verbal form; each such sentence is quoted below in document order. The
other 32 contain none. Every description string also occurs word for word in
Clause 6, except the descriptions at `/properties/$schema/description`,
`/properties/$id/description` and
`/definitions/purl_component_definition/description`, which have no Clause 6
counterpart; the default_repository_url string matches except for its missing
final full stop (Inconsistencies observed, C-10).

**287.** Annex A, `/definitions/purl_component_definition/properties/permitted_characters/description`, sentence 2 (p. 19) `[shall]`

> If provided, this shall be a subset of the 'Permitted characters' defined in the PURL specification.

**288.** Annex A, `/definitions/purl_component_definition/properties/case_sensitive/description`, sentence 2 (p. 20) `[shall]`

> If false, the canonical form shall be lowercased.

**289.** Annex A, `/definitions/purl_component_definition/properties/normalization_rules/description`, sentence 2 (p. 20) `[cannot]`

> These are plain text, unstructured rules as some require programming and cannot be enforced only with a schema.

**290.** Annex A, `/properties/namespace_definition/description`, sentence 2 (p. 21) `[shall]`

> The PURL namespace component shall be required, optional or prohibited for a specific PURL type definition.

**291.** Annex A, `/properties/qualifiers_definition/description`, sentence 2 (p. 23) `[may]`

> The PURL qualifiers component is optional for a specific PURL type, but a qualifiers key or keys may be required for a specific PURL type.

## Informative content excluded

### Examples marked "(Informative)"

| Locator | Caption (verbatim) | Content (verbatim) |
|---|---|---|
| §5, after paragraph 5 (p. 3) | Example 1 (Informative): Debian | `pkg:deb/debian/curl@7.50.3-1?arch=i386&distro=jessie` |
| §5, after paragraph 5 (p. 3) | Example 2 (Informative): Maven | `pkg:maven/org.apache.xmlgraphics/batik-anim@1.9.1?packaging=sources` |
| §5, after paragraph 5 (p. 3) | Example 3 (Informative): Node Package Manager (NPM) | `pkg:npm/foobar@12.3.1` |
| §6.1 (p. 7) | Example 1 (Informative) | `maven` |
| §6.1 (p. 7) | Example 2 (Informative) | `npm` |
| §6.1 (p. 7) | Example 3 (Informative) | `pypi` |
| §6.2 (p. 8) | Example 1 (Informative) | `Apache Maven` |
| §6.2 (p. 8) | Example 2 (Informative) | `Python Package` |

The Annex A annotation keywords `/properties/type/examples` (`["maven", "npm",
"pypi"]`, p. 21) and `/properties/type_name/examples` (`["Apache Maven",
"Python Package"]`, p. 21) carry the same values as the §6.1 and §6.2 examples.
They are not labelled "(Informative)", but `examples` is a JSON Schema
annotation with no validation effect, so they are excluded with the examples.

### Clause 1 and Clause 4

- Clause 1 (Scope, p. 1): all five sentences assessed under "1 Scope" above;
  none extracted.
- Clause 4 (Overview, p. 2): excluded in full because it declares itself
  non-normative (quoted under "4 Overview" above).

### Sentences inside normative clauses not extracted

Each states a purpose or describes something without constraining it.

**§2, paragraph 5, sentence 2 (p. 1).** Motivation for statement 9.

> This guarantees the integrity and reliability of PURLs in all supported contexts.

**§5.1, bullet 5, sentence 3 (p. 4).** Describes VCS URLs; constrains nothing.

> They are a closely related, compact and uniform way to reference VCS URLs.

**§6, paragraph 1, sentence 3 (p. 6).** Purpose of type-definition documents;
it holds the only "can" in Clauses 1 to 6.

> These JSON documents are then used to generate PURL type documentation and to support PURL libraries and tools so that they can more easily parse, build, and validate PURLs by type in a consistent and standardized manner across programing languages and technology stacks.

Clause and subclause headings and the eight table captions are structure and
appear here as headings or table labels.

### Annex A material not itemised

The schema body is the schema artifact's job. Its `title` strings repeat the
Clause 6 subclause headings, and its 32 description strings without a verbal
form are not itemised (see "Annex A description strings with a verbal form").

### Front matter and back matter

- Front matter (pp. i to v): cover, Contents (pp. i to ii), Introduction
  (p. iii), "About this specification" (p. iv) and the Copyright Notice (p. v).
  The Introduction and "About this specification" are informative; the Copyright
  Notice is licence text, reproduced in full at the end of this file but not
  extracted as statements.
- Back matter: Bibliography (p. 27, informative references), Colophon (p. 29)
  and Software License (p. 31, BSD licence text). Not extracted.
- PDF pages 8, 34, 36 and 38 are blank; PDF page 2 carries only a trademark
  line and the copyright line; PDF page 40 is the back cover.

## Verbal form tally

Counts are of lowercase forms in the source text (sentence-initial "Shall"
included), after joining wrapped lines. "shall not" and "may not" are counted
separately and never also as "shall" or "may". Each cell gives found
(included/excluded). "can" is counted as well because it is the ISO/IEC
Directives possibility form. No "should not", "need not" or "must" occurs
outside the Software License. Counted case-insensitively, as
`requirements.yaml` counts them, the whole document has shall 71 (this table's
70 plus the licence's uppercase SHALL) and may 21 (may 20 plus may not 1); the
pass 2 recount (`verification.md`) agrees with both.

| Region | shall | shall not | should | may | may not | cannot | can | why excluded |
|---|---|---|---|---|---|---|---|---|
| Front matter (pp. i to v) | 1 (0/1) | 0 | 0 | 2 (0/2) | 1 (0/1) | 0 | 1 (0/1) | Copyright Notice (shall, may, may, may not) is licence text, reproduced verbatim at the end but not extracted; "can" is in the informative Introduction |
| Clause 1 Scope | 0 | 0 | 0 | 0 | 0 | 0 | 0 | none present |
| Clause 2 Conformance | 8 (8/0) | 2 (2/0) | 0 | 2 (2/0) | 0 | 0 | 0 | none excluded |
| Clause 3 Normative references | 0 | 0 | 0 | 0 | 0 | 0 | 0 | none present |
| Clause 4 Overview | 0 | 0 | 0 | 0 | 0 | 0 | 0 | none present (clause excluded as non-normative) |
| Clause 5 | 21 (21/0) | 11 (11/0) | 3 (3/0) | 11 (11/0) | 0 | 0 | 0 | none excluded |
| Clause 6 | 37 (37/0) | 0 | 0 | 2 (2/0) | 0 | 8 (8/0) | 1 (0/1) | "can" is in §6 paragraph 1 sentence 3, a statement of purpose |
| **Clauses 1 to 6** | **66 (66/0)** | **13 (13/0)** | **3 (3/0)** | **15 (15/0)** | **0** | **8 (8/0)** | **1 (0/1)** | |
| Annex A introductory text | 0 | 0 | 0 | 0 | 0 | 0 | 0 | none present |
| Annex A description strings | 3 (3/0) | 0 | 0 | 1 (1/0) | 0 | 1 (1/0) | 0 | none excluded |
| Back matter: Bibliography, Colophon | 0 | 0 | 0 | 0 | 0 | 0 | 0 | none present |
| Back matter: Software License (p. 31) | 0 | 0 | 0 | 2 (0/2) | 0 | 0 | 0 | BSD licence boilerplate; it also holds the only uppercase BCP 14 keywords, SHALL (1) and REQUIRED (1), and 2 lowercase "must", all excluded |
| **Whole document** | **70 (69/1)** | **13 (13/0)** | **3 (3/0)** | **20 (16/4)** | **1 (0/1)** | **9 (9/0)** | **2 (0/2)** | |

Where the included occurrences sit (statement numbers):

- Clause 2: "shall" (8) 1, 2, 3, 4, 5, 6, 8, 9; "shall not" (2) 12, 13; "may"
  (2) 10, 11.
- Clause 5: "shall" (21) 39, 40, 42, 50, 54, 55 (twice), 56, 57, 65, 76, 80,
  83, 86, 88, 92, 93, 95, 96, 101, 107; "shall not" (11) 24, 41, 58, 67, 68,
  70, 90, 94, 103, 104, 105; "should" (3) 63, 74, 100; "may" (11) 25, 32, 35,
  49, 62, 69, 72, 77, 81, 96, 106.
- Clause 6: "shall" (37) 113, 132, 134, 135, 139, 148, 151, 156, 157, 167,
  168, 172, 177, 180, 185, 186, 196, 197, 201, 206, 209, 214, 215, 224, 232,
  243, 248, 249, 253, 258, 261, 266, 267, 275, 276, 281, 282; "may" (2) 114,
  223; "cannot" (8) 136, 154, 169, 183, 198, 212, 250, 264. Of the 37 "shall",
  9 are table-cell sentences (113 in Table 2; 134, 135 in Table 4; 167, 168 in
  Table 5; 196, 197 in Table 6; 248, 249 in Table 8) and 5 are the "Shall be
  one of:" lines (139, 172, 201, 232, 253). Statement 114 ("may") and
  statements 136, 169, 198 and 250 ("cannot") are also table-cell sentences.
- Annex A description strings: "shall" (3) 287, 288, 290; "may" (1) 291;
  "cannot" (1) 289.

Numbered statements by tag (291 statements; statement 96 carries two forms and
counts under each, so the rows sum to 292):

| tag | statements | occurrences |
|---|---|---|
| `[shall]` | 68 | 69 |
| `[shall not]` | 13 | 13 |
| `[should]` | 3 | 3 |
| `[may]` | 16 | 16 |
| `[cannot]` | 9 | 9 |
| `[none: declarative]` | 115 | |
| `[none: property block]` | 54 | |
| `[none: lead-in]` | 5 | |
| `[none: table cell]` | 8 | |
| `[none: imperative]` | 1 | |

## Inconsistencies observed

Recorded, not fixed. "C" items are contradictions between parts of the source;
"U" items are places where the source is unclear or incomplete.

### Contradictions

**C-1. Type of the four component-definition properties.** In Table 2 (p. 7)
the Type cell is "Array" in the rows namespace_definition, name_definition,
version_definition and subpath_definition (statement 112). Their own property
blocks say Object, for example §6.5 (statement 130):

> Location: /namespace_definition
> Property: namespace_definition (Required)
> Type: Object

The same holds for §6.6, §6.7 and §6.9 ("Type: Object"), and Annex A gives
`"type": "object"` at `/properties/namespace_definition/type`,
`/properties/name_definition/type`, `/properties/version_definition/type` and
`/properties/subpath_definition/type`.

**C-2. Type of every `requirement` property.** In Tables 4, 5, 6, 7 and 8 the
Type cell of the requirement row is "Array" (statements 133, 166, 195, 227,
247). The property blocks of §6.5.1, §6.6.1, §6.7.1, §6.8.1.2 and §6.9.1 say
String, for example §6.5.1 (statement 137):

> Location: /namespace_definition/requirement
> Property: requirement (Required)
> Type: String

Annex A gives `"type": "string"` with a `oneOf` of string constants (K18, K21,
K24, K30, K32).

**C-3. `$id` and `$schema` exist only in Annex A.** Annex A requires `$id` (K8)
and constrains it with a pattern (K11), and fixes `$schema` with a const (K9).
Neither property appears in Table 2 or anywhere in Clause 6, so a type
definition that follows Clause 6 exactly fails Annex A for lack of `$id`.

**C-4. Default of `use_repository`.** Annex A gives a default (K15:
`/properties/repository/properties/use_repository/default` = `false`); §6.4.1
has no "Default Value" line, although the case_sensitive blocks (§6.5.6,
§6.6.4, §6.7.4, §6.9.4) print "Default Value: true" to match K6. The property is
also required (K14), so the default has no effect on a valid document.

**C-5. Annex A constraints with no Clause 6 counterpart.** `additionalProperties`
false at the root (K1), on repository (K13) and on qualifier items (K28);
`minItems` 1 on examples (K35); `additionalItems` false on
qualifiers_definition (K26). The qualifiers_definition `uniqueItems` (K27)
appears in Clause 6 only as the misplaced line in §6.8.1.7 (U-1).

**C-6. Minimum type length.** §6.1 and Annex A K12 require at least two
characters (`+` after the second class), and the examples pattern (§6.10, K36)
does the same for the type in each example; §5.6.2 admits a one-letter type.

> Pattern Constraint: ^[a-z][a-z0-9-\.]+$

> The package type shall be composed only of ASCII letters and numbers, period '.', and dash '-'.

> The type shall start with an ASCII letter.

**C-7. Which document defines the encoding rules.** §2 points to RFC 3986 for
encoding and decoding; §5.4 says only the mechanism comes from RFC 3986.

> Furthermore, implementations shall process URI encoding and decoding for PURL components according to the standards outlined in RFC 3986.

> With the exception of the percent-encoding mechanism, the rules regarding percent-encoding are defined by this Standard alone.

**C-8. Withdrawn in pass 2 (verify).** First recorded here as a contradiction
between §5.6.6 and §2. It is not one: the §5.6.6 sentence gives an empty value
its own meaning, so it does not collide with the §2 rejection duty. Restated
as U-16 below.

**C-9. Canonical form: recommended steps, required outcome.** Stripping leading
and trailing slashes is only recommended (§5.6.3, §5.6.4, §5.6.7), while §2
requires a single canonical representation.

> All leading and trailing slashes '/' are not significant and should be stripped in the canonical form.

> Implementations shall ensure that equivalent PURLs are consistently resolved to the same canonical representation.

**C-10. default_repository_url description punctuation.** Table 3 and §6.4.2
end "The default public repository URL for this PURL type." with a full stop;
the Annex A string at
`/properties/repository/properties/default_repository_url/description` is "The
default public repository URL for this PURL type" without one (p. 21).
Editorial only.

### Unclear or incomplete

**U-1. Misplaced uniqueness line.** §6.8.1.7 ends with a uniqueness rule under
"Native name", whose Type is String. The only array in §6.8 is
qualifiers_definition, which Annex A marks unique (K27).

> Location: /qualifiers_definition/[]/native_name
> Type: String

> All items shall be unique.

**U-2. `additionalItems` with a single-schema `items`.** At
`/properties/qualifiers_definition` (K26) `"additionalItems": false` sits beside
an object-valued `items`. Under JSON Schema draft-07 (the Bibliography's
draft-handrews-json-schema-validation-01, §6.4.2), `additionalItems` is ignored
unless `items` is an array of schemas, so K26 has no effect and its intent is
unstated.

**U-3. No prohibited extension is identified.** §2 forbids "prohibited
extensions explicitly identified in the specification", but the Standard
identifies none; "extensions" occurs only in §2 and in the non-normative
Clause 4.

> Any prohibited extensions explicitly identified in the specification shall not be implemented.

**U-4. `repository_url` is not defined.** §5.6.3 directs users to a qualifier
that this edition does not define; the key occurs nowhere else, and §1 says the
Standard "does not include any specific PURL type definitions".

> Use instead a repository_url qualifier.

**U-5. "types" or "scheme".** Both §5.1 exclusion bullets call the listed
schemes invalid "PURL types" and then invalid "PURL scheme", so it is unclear
whether the rule restricts the type component, the scheme, or both.

> Special URL schemes as defined in https://url.spec.whatwg.org/ such as file://, https://, http:// and ftp:// are not valid PURL types.

> They are valid URL or URI schemes but they are not a valid PURL scheme.

**U-6. Normative references are incomplete.** §5.1 defines a PURL against four
URL documents, three of which (the WHATWG URL Standard and two Wikipedia pages)
are not in Clause 3, and bullet 4 relies on the WHATWG definition of special
schemes. Annex A states "The format is JSON Schema version draft-07.", but JSON
Schema appears only in the informative Bibliography. Clause 3 lists only
ECMA-262, RFC 3986 and The Unicode Standard.

**U-7. What "Permitted characters" a `permitted_characters` regex must be a
subset of.** §5.2 defines the ASCII characters of a canonical, percent-encoded
PURL, but §5.6.3 to §5.6.7 allow "any Unicode character" after percent-decoding.
The Standard does not say whether the regex applies to the encoded or the
decoded form, or whether "the PURL specification" means this Standard or the
web document named on p. iv.

> If provided, this shall be a subset of the 'Permitted characters' defined in the PURL specification.

**U-8. Name prefix with an empty namespace.** §5.6.4 states the slash prefix
only for a non-empty namespace, while §5.3 and Example 3 (`pkg:npm/foobar@12.3.1`)
show a slash between type and name when there is no namespace.

> The name is prefixed by a single slash '/' separator when the namespace is not empty.

> '/' (slash) is the separator between type, namespace and name

**U-9. Prohibited namespace not reflected in Clause 5.** §5.6.3 mentions only
"required"; a type definition may also prohibit the namespace (§6.5,
statement 132; §6.5.4 Constant "prohibited").

> The namespace is optional, unless required by the package's type definition.

**U-10. "opaque" versions and type-level normalisation.** §5.6.5 calls a version
opaque, but a type definition may declare the version component case
insensitive (lowercased canonical form) and give normalization rules (§6.7,
Table 6, §6.7.4, §6.7.5). "opaque" is not defined.

> A version is a plain and opaque string.

**U-11. `$id` pattern and type characters.** K11 admits only `[a-z0-9-]` before
`-definition.json`, while §5.6.2, §6.1 and K12 admit "." in a type. The
Standard does not say that `$id` embeds the type string, so this is only a
potential mismatch.

**U-12. Which text governs.** The front matter, Clause 4 and Annex A point at
different authorities, and the schema file named in Annex A differs from the
schema's own `$id` (`https://packageurl.org/schemas/purl-type-definition.schema-1.0.json`).
Nothing says which prevails when they diverge.

> The document at https://tc54.org/purl/ is the most accurate and up-to-date Package-URL specification.

> The official version of an Ecma International document is the English language version on the Ecma International website.

> While this document serves as the authoritative reference for implementing PURL, it is complemented by various ecosystem-specific guidance documents, examples, and related standards.

> This Annex provides a copy of the current Package-URL Type Definition Schema.

> The schema shown below is available in electronic form at: https://github.com/package-url/purl-spec/blob/main/schemas/purl-type-definition.schema.json

**U-13. Untestable prohibition.** §2 (statement 14) forbids "behaviours that
compromise the interoperability of PURLs" without a verbal form and without a
criterion for what compromises interoperability.

> Furthermore, behaviours that compromise the interoperability of PURLs across tools, platforms, or ecosystems are strictly disallowed.

**U-14. "may" used for possibility.** Two "may" sentences grant no permission
(statements 25 and 72); the ISO/IEC Directives form for possibility is "can".

> A namespace segment may sometimes look like a host, but its interpretation is specific to a type.

> Note however, that for some types, the namespace may look like a host.

**U-15. Expectation without a verbal form.** "Tools are expected to apply these
rules programmatically." occurs eight times in Clause 6 (Tables 4, 5, 6, 8;
§6.5.7, §6.6.5, §6.7.5, §6.9.5) and once in Annex A; it is not stated whether
applying normalization_rules is required.

**U-16. Empty qualifier values: forbidden and given a meaning in one
sentence.** (Replaces C-8.) §5.6.6 forbids an empty value and, after the colon,
says what a pair with an empty value means. Note **(inferred)**: read as one
sentence, the first half binds what a producer writes and the second tells a
reader to treat the pair as absent, so a PURL whose only fault is an empty value
has a stated meaning and §2's rejection duty does not collide with it. What the
text leaves open is whether a strict validator may also flag such a string.
`examples/expected.yaml` follows the stated equivalence (PURL-NEG-06: accept,
pair dropped); `schema/purl.derived.abnf` refuses `key=` in all three roots
(its gap G7).

> A value shall not be an empty string: a key=value pair with an empty value is the same as if no key=value pair exists for this key.

> Invalid PURLs that fail to conform to the specification shall be identified and rejected by any conforming implementation.

## Copyright notice

The following is the Ecma Copyright Notice from p. v of ECMA-427 1st edition,
reproduced verbatim as its terms require for copies and commentary.

> COPYRIGHT NOTICE
>
> © 2025 Ecma International
>
> By obtaining and/or copying this work, you (the licensee) agree that you have read, understood, and will comply with the following terms and conditions.
>
> This document may be copied, published and distributed to others, and certain derivative works of it may be prepared, copied, published, and distributed, in whole or in part, provided that the above copyright notice and this Copyright License and Disclaimer are included on all such copies and derivative works. The only derivative works that are permissible under this Copyright License and Disclaimer are:
>
> (i) works which incorporate all or portion of this document for the purpose of providing commentary or explanation (such as an annotated version of the document),
>
> (ii) works which incorporate all or portion of this document for the purpose of incorporating features that provide accessibility,
>
> (iii) translations of this document into languages other than English and into different formats and
>
> (iv) works by making use of this specification in standard conformant products by implementing (e.g. by copy and paste wholly or partly) the functionality therein.
>
> However, the content of this document itself may not be modified in any way, including by removing the copyright notice or references to Ecma International, except as required to translate it into languages other than English or into a different format.
>
> The official version of an Ecma International document is the English language version on the Ecma International website. In the event of discrepancies between a translated version and the official version, the official version shall govern.
>
> The limited permissions granted above are perpetual and will not be revoked by Ecma International or its successors or assigns.
>
> This document and the information contained herein is provided on an “AS IS” basis and ECMA INTERNATIONAL DISCLAIMS ALL WARRANTIES, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO ANY WARRANTY THAT THE USE OF THE INFORMATION HEREIN WILL NOT INFRINGE ANY OWNERSHIP RIGHTS OR ANY IMPLIED WARRANTIES OF MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE.
