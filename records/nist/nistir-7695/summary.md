---
schema: "library-summary/v1"
id: nistir-7695
record: nistir-7695
type: summary
updated: "2026-10-19"
---

# Common Platform Enumeration: Naming Specification Version 2.3

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | _unset_: a NIST Interagency Report, not a NIST SP or a ratified standard |
| **Authors** | Brant A. Cheikes (The MITRE Corporation), David Waltermire (NIST), Karen Scarfone (Scarfone Cybersecurity), as named in the Acknowledgments |
| **Publisher** | National Institute of Standards and Technology (NIST), Computer Security Division |
| **Published** | 2011-08 (August 2011, 49 pages) |
| **Identifier** | nist: NIST IR 7695; doi: 10.6028/NIST.IR.7695 |
| **Source** | https://nvlpubs.nist.gov/nistpubs/Legacy/IR/nistir7695.pdf |
| **Digest** | `01553a4638b21eda10018690b71162e91605d78eb15850f881bd0b2b691ac3f6` |
| **Licence** | No copyright or licence notice in the document. NIST's employees' works are not subject to U.S. copyright, but two of the three authors were not NIST staff. "CPE is a trademark of The MITRE Corporation." (p. iii) |

## Overview

NIST IR 7695 defines CPE 2.3 naming. Its logical model is the well-formed CPE name (WFN): an unordered set of attribute-value pairs over eleven attributes (`part`, `vendor`, `product`, `version`, `update`, `edition`, `language`, `sw_edition`, `target_sw`, `target_hw`, `other`), whose values are restricted strings or the logical values ANY and NA. The WFN has two string bindings, a URI binding kept compatible with CPE 2.2 (`cpe:/a:...`) and the formatted string binding (`cpe:2.3:a:...`), and the document gives pseudocode to bind, unbind and convert between them, plus conformance rules for products that produce or consume CPE names (§4). A CPE names a class of products, never an instance (§5), and the specification governs only syntax: rules for which values are "correct" or "valid" for an attribute are out of scope (§5), so a well-formed CPE can still be a guess. Matching (NIST IR 7696), the dictionary (NIST IR 7697) and the applicability language (NIST IR 7698) are separate specifications with their own records.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | NVD keys its vulnerability applicability data on CPE names, so a CPE is how a component reaches a CVE wherever no ecosystem or distribution advisory covers it. SBOM generators such as Syft emit CPE candidates, and scanners such as Dependency-Check identify dependencies by CPE. |
| Cryptography | none | No signatures, digests or keys. |
| This project | core | tmodel's accepted `identifiers` slot (DEC-001a, ADR-0010) carries CPE strings: the LinkML example and 16 strings in the example vectors. Because a CPE names a class, it is never instance identity (DEC-005, ADR-0002). It bears most on the open DEC-009 (where a CPE's provenance lives, the comparison profile, the forms for Product and Component) and DEC-008 (which NVD data to mirror), and on RPT-0004's candidate rules R-ID-2, R-ID-3, R-MATCH-1 and R-MERGE-2. |

Bears on DEC-001a, DEC-002 and DEC-005 (accepted) and DEC-008 and DEC-009 (open). Kept as a stub for RPT-0004 (product composition, tmodel #38), then extracted to FX-1 for it. `distilled/design-notes.md` gives 6 adopt, 6 adapt and 6 reject items, 21 source defects and 20 open questions.

## Implementations

Searched 2026-10-19: GitHub's REST API for the repositories below (licences and latest releases). Commercial products were not surveyed.

| Name | Kind | License | URL |
|---|---|---|---|
| CPE-Parser 3.0.1 (`us.springett:cpe-parser`) | Java library: validates and parses CPE 2.2 and 2.3 names | Apache-2.0 | https://github.com/stevespringett/CPE-Parser |
| `cpe` 1.3.1 | Python library | LGPL-3.0 | https://github.com/nilp0inter/cpe |
| go-cpe (no tagged release) | Go library for CPE 2.3 | MIT | https://github.com/knqyf263/go-cpe |
| nvdtools v0.1.5, `wfn` package | Go tools for NVD feeds and the CPE dictionary (repository archived) | Apache-2.0 | https://github.com/facebookincubator/nvdtools |
| Syft v1.54.1 | SBOM generator that emits CPE candidates for each package (library record `anchore-syft`) | Apache-2.0 | https://github.com/anchore/syft |
| Dependency-Check v13.0.0 | scanner that identifies a dependency by CPE and links it to CVEs | Apache-2.0 | https://github.com/dependency-check/DependencyCheck |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, labels and relations, and the FX-1 `distillation` block |
| `distilled/README.md` | index of the extracted artifacts and what each one covers |
| `distilled/normative.md` | the specification's normative statements, ABNF rules, pseudocode steps and table rows, verbatim, with locators |
| `distilled/requirements.yaml` | one entry per requirement (`nistir-7695#R-NNNN`), reconciled against `bin/bcp14-count` and the lowercase forms by line |
| `distilled/schema/` | the four ABNF figures verbatim, a repaired `.derived.` grammar beside each, a derived JSON Schema for a WFN, and NIST's CPE naming XML schema |
| `distilled/messages.yaml` | the WFN, its values and both bindings field by field: type, whether required, allowed characters, encoding and locators |
| `distilled/examples/` | the specification's examples as fixtures plus derived positives and negatives, with expected results and a reference implementation of the §5 to §7 pseudocode |
| `distilled/design-notes.md` | what tmodel adopts, adapts or rejects, mapped to its decisions; a WFN-to-tmodel mapping; source defects; open questions |
| `distilled/verification.md` | the verify and cross-check record (passes 2 and 3) |

Protocol and state machine are not applicable; the reasons are in `record.yaml`.

## Limits

- **Syntax, not truth.** The document defines how a name is spelled, not which vendor, product or version string is right; that is left to dictionaries (NIST IR 7697) and to whoever writes the name.
- **A class, not an instance.** "WFNs are used solely for product classes. They cannot identify product instances" (§5).
- **The printed grammars and pseudocode are defective.** None of the four ABNF figures is valid RFC 2234 ABNF as printed (`/=` where ABNF writes `=/`, continuation lines that begin with `=`, a small tilde U+02DC in Figure 6-1, `LANGTAG = cf. [RFC5646]`). `process_quoted_chars` as printed turns `8\.0\.6001` into `8..001`, against the document's own examples. §6.1.1 says consumers MUST accept every Figure 6-1 URI, but `decode()` rejects some of them, and §7's round-trip claim fails for uppercase names and unencoded tildes. The extraction keeps the literal text and records a repaired reading beside it.
- **The model and its bindings disagree in places.** Unbinding a URI lowercases values while unbinding a formatted string keeps case; a lone `?` is a valid WFN value that neither binding's grammar (Figures 6-2 and 6-3) can express; NA for `part` or `language` binds to `-`, which the URI grammar rejects; and §5.2 says an attribute not used in a WFN "SHALL default to the logical value ANY", while §5.3.1 says NA "SHOULD be assigned" when an attribute "is not used as part of the description".
- **Old.** Published in August 2011. Whether NIST or NVD published errata for these defects is an open question in `distilled/design-notes.md`.
