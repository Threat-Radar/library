---
schema: "library-summary/v1"
id: ecma-427
record: ecma-427
type: summary
updated: "2026-10-15"
---

# ECMA-427 Package-URL (PURL) specification, 1st edition

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | standard (adopted by the Ecma General Assembly, December 2025; p. iii) |
| **Editors** | John Horan, Michael Herzog, Philippe Ombredanne, Steve Springett (p. iv) |
| **Publisher** | Ecma International, Technical Committee 54 (TC54) |
| **Published** | December 2025, 1st edition, 40 pages |
| **Identifier** | ECMA-427; listed by Ecma as ISO/IEC DIS 27056 |
| **Source** | https://ecma-international.org/wp-content/uploads/ECMA-427_1st_edition_december_2025.pdf |
| **Digest** | `037180df99e7d7c26d910dc3adb3fa07c4fb787cc4bd29e43634de3802313825` (SHA-256 of the PDF, retrieved 2026-10-15) |
| **Licence** | Ecma copyright notice allowing copies and commentary with the notice kept (p. v); the Annex A schema is under the BSD licence printed on p. 31 |

## Overview

A package URL (purl) names a software package with one string, `pkg:type/namespace/name@version?qualifiers#subpath`, whatever ecosystem it comes from. ECMA-427 fixes the syntax of that string (Clause 5: which components exist, which characters they may hold, how each is percent-encoded, and which parts are case-insensitive) and the JSON Schema that a purl *type* definition must follow (Clause 6 and Annex A). It deliberately defines no types: the rules for `npm`, `maven`, `deb` and the rest live in the purl-spec repository's type files, not in the standard. Conformance (Clause 2) requires implementations to resolve equivalent purls to "the same canonical representation", but the standard gives the canonical form only in pieces (lowercase type, stripped slashes, unique lowercase qualifier keys) and states no ordering rule for qualifiers.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | adjacent | purl is how SBOMs, CVE records (`packageURL`), OSV advisories and scanners such as Grype name a package, so vulnerability matching depends on it; the standard itself defines no security mechanism. |
| Cryptography | none | No digests, signatures or keys. A version may be a digest for some types, but that is a type rule, not this standard. |
| This project | core | tmodel's accepted object model (ADR-0010, DEC-001a) carries purl strings in the opaque `identifiers` slot on Product, ProductInstance and Component. Whether two Components are "the same" depends on how purls are compared, which bears on DEC-001 (identity) and DEC-002 (interchange). RPT-0004 (tmodel #38) rule R-ID-3 proposes Component identity = a type-normalized purl. |

## Implementations

Searched 2026-10-15 (GitHub organisation `package-url`). Libraries that parse and build purls: packageurl-python (0.17.6, MIT), packageurl-java, packageurl-go, packageurl-js, packageurl-dotnet, packageurl.rs, packageurl-ruby and packageurl-php (all MIT). These track the purl-spec repository, which already holds the 2nd edition text (v1.1.0), so their behaviour can differ from the 1st edition. The purl-spec repository also publishes a conformance test suite (`purl-test.schema-0.1.json` and the test files) that this record does not copy.

| Name | Kind | License | URL |
|---|---|---|---|
| packageurl-python | library | MIT | https://github.com/package-url/packageurl-python |
| packageurl-java | library | MIT | https://github.com/package-url/packageurl-java |
| packageurl-go | library | MIT | https://github.com/package-url/packageurl-go |
| packageurl-js | library | MIT | https://github.com/package-url/packageurl-js |
| purl-spec (type definitions, tests) | specification repository | MIT (per its `LICENSE` file) | https://github.com/package-url/purl-spec |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations and the FX-1 distillation block |
| `distilled/README.md` | index of the extracted artifacts and their coverage |
| `distilled/normative.md` | every normative statement, verbatim, with its clause |
| `distilled/requirements.yaml` | one entry per requirement, with verb, actor, condition and locator |
| `distilled/schema/` | the Annex A JSON Schema verbatim, and a derived grammar for the purl string |
| `distilled/messages.yaml` | the purl string's seven components and the type-definition document, field by field |
| `distilled/examples/` | the standard's examples as fixtures, with expected results |
| `distilled/design-notes.md` | what tmodel adopts, adapts or rejects, mapped to its decisions |
| `distilled/verification.md` | the verify and cross-check record |

## Limits

- **The canonical form is under-specified.** Clause 2 requires a canonical representation, but nothing in the 1st edition says how qualifiers are ordered, and normalization per type is free text that "cannot be enforced only with a schema" (§6.5.7). Two conforming tools can therefore print different strings for the same package. RPT-0004's tool runs found exactly this (Syft and Docker Scout chose different qualifiers for the same Alpine package).
- **No types, so no equality rules.** Whether `pkg:pypi/Django` and `pkg:pypi/django` are the same package is decided by the `pypi` type file, outside this standard.
- **A version is opaque** (§5.6.5). Version ranges are a separate specification (VERS), which this standard says it does not cover (Clause 4).
- **It is already being replaced.** TC54 approved the 2nd edition text (purl-spec v1.1.0, 2026-10-07) for the December 2026 General Assembly; it adds an ABNF grammar and rules for unregistered types. Anything built on this record should expect a superseding record.
- **Internal inconsistencies** (recorded in the design notes): the property tables in Clause 6 call several objects and strings "Array", while the clause text and Annex A schema say object or string; the Annex A schema requires `$id`, which Table 2 does not list; and the electronic copy Annex A points to (`schemas/purl-type-definition.schema.json` on `main`) no longer exists under that name.
