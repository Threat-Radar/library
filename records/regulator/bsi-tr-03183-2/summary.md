---
schema: "library-summary/v1"
id: bsi-tr-03183-2
record: bsi-tr-03183-2
type: summary
updated: "2026-11-03"
---

# Technical Guideline BSI TR-03183: Cyber Resilience Requirements for Manufacturers and Products, Part 2: Software Bill of Materials (SBOM)

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | `best-practice` |
| **Authors** | Bundesamt für Sicherheit in der Informationstechnik (BSI) |
| **Published** | 2025-08-20 (version 2.1.0) |
| **Identifier** | bsi: TR-03183-2 |
| **Source** | https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/Publications/TechGuidelines/TR03183/BSI-TR-03183-2_v2_1_0.pdf?__blob=publicationFile |
| **Digest** | `dda0ccd9b6148571d1d12241a1618b30027f22bc15e24248fdd21a011e62845c` |

## Overview

BSI TR-03183-2 sets the formal and technical requirements for a software bill of materials (SBOM). It is written to help manufacturers meet the EU Cyber Resilience Act (§1). It is a technical guideline, not part of the Act: it notes that the CRA makes an SBOM mandatory (§1), uses its own terminology rather than the CRA's (§3.2.9), and nowhere claims that following it establishes conformity with the CRA.

- **Format.** An SBOM must be a JSON or XML document, valid under an officially released CycloneDX 1.6 or later, or SPDX 3.0.1 or later (§4).
- **One per version, no vulnerability data.** Each software version gets its own SBOM. It carries no vulnerability information, which belongs in security advisories such as CSAF or VEX (§1, §3.1).
- **Depth.** Dependencies are resolved recursively, from every delivered component down to the first component outside the scope of delivery (§5.1).
- **Fields** (§5.2):
  - each SBOM carries its creator and a timestamp;
  - each fully described component carries its creator, name, version, filename, dependencies with a completeness flag, distribution licences, a SHA-512 hash, and three properties (executable, archive, structured);
  - other components carry fewer, decided in the order referenced, identified, fully described (§5.1):
    - a logical component: creator, name, version, dependencies, distribution licences, its other licence fields, other unique identifiers and the security.txt URL, but no filename, hash or file properties (§3.2.2);
    - a component that only has to be identified: creator, name, version and other unique identifiers (§3.2.4);
    - a component recorded in another BOM: its creator, name and version beside the reference, and nothing more (§3.2.5);
  - a required field that the way a component was assembled makes unavailable, such as its hash or filename, is left out (§3.2.1);
  - further fields are required when they exist.
- **Licences.** They are named by SPDX identifier, then from the ScanCode LicenseDB, then by the inventorying party's own LicenseRef (§6.1).

Version 2.1.0 raised the minimum formats from CycloneDX 1.5 and SPDX 2.2.1. It also introduced logical and identified components, and added an informative mapping of every field to CycloneDX and SPDX (Table 1, §8.2).

## Applicability

- **Security: adjacent.** SBOM data supports vulnerability handling, because a product's component list can be compared with vulnerability data (§1). But the guideline sets no security controls, and it keeps vulnerability statements out of the SBOM.
- **Cryptography: adjacent.** Its one cryptographic requirement is a SHA-512 hash of each deployable component (§5.2.2). The optional source-code hash has no defined method yet (§5.2.5).
- **This project: core.** It is the national SBOM baseline in RPT-0004 (product composition). Its fields bear on component identity in the core object model (DEC-001a), and its format floor bears on which SBOM formats and versions tmodel imports (DEC-002). tmodel#172 extracts its requirements, including those stated in notes, into `research/0017-requirements-extraction/bsi-tr-03183-2.yaml` (59 Requirements).

## Implementations

**Open source**, checked 2026-11-02. None was run here.

| Tool | What it does | Licence |
|---|---|---|
| sbomqs (Interlynk) | Compliance mode for TR-03183-2 v2.1.0, v2.0 and v1.1, per its README | Apache-2.0 |
| CycloneDX.CRA.Validator | Validates CycloneDX SBOMs against v2.1.0, per its repository description | Apache-2.0 |
| TR-03183 CycloneDX property taxonomy (the tr-03183 organisation) | CycloneDX property names for the guideline's fields | Apache-2.0 |

The library's `cyclonedx-property-taxonomy` record is CycloneDX's own taxonomy, not this one.

**Commercial:** not surveyed.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this summary |

## Limits

- **One version.** Only version 2.1.0 was read. Versions 1.0, 1.1 and 2.0.0 were compared only through the document history (Table 1), and Part 1 (`bsi-tr-03183-1`) was not compared.
- **Appendix not checked.** Sections 1 to 7 were read in full. The informative appendix (§8: explanations, the field mapping, levels of detail and SBOM classifications) was read only by its contents, so its mapping was not checked field by field against CycloneDX or SPDX.
- **Not every requirement can be checked mechanically:**
  - fields required only "if it exists" (§5.2.3, §5.2.4);
  - the source-code hash, whose method is not yet defined (§5.2.5);
  - the rule that an SBOM holds the same information as was available at build time (§5.1).
- **Notes and lowercase wording.** §2 says only that the capitalised BCP 14 keywords carry their BCP 14 meaning. It does not say that notes are informative. Most notes explain, but six state a duty, a recommendation or a permission in lowercase words: identifying the first dependencies outside the scope of delivery and letting the SBOM's filename name its primary component (§5.1), setting the effective licence anew when SBOMs are merged (§3.2.8), using UTC timestamps (§5.2.1), and, for a component, giving its name as it was at integration or its creator's current name (§5.2.2). Their force is plain English, not BCP 14; tmodel#172's extraction lists each one and says how it was read.
