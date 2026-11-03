---
schema: "library-summary/v1"
id: bsi-tr-03183-2
record: bsi-tr-03183-2
type: summary
updated: "2026-11-02"
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

BSI TR-03183-2 sets the formal and technical requirements for a software bill of materials (SBOM). It is written to help manufacturers meet the EU Cyber Resilience Act (§1).

- **Format.** An SBOM must be a JSON or XML document, valid under an officially released CycloneDX 1.6 or later, or SPDX 3.0.1 or later (§4).
- **One per version, no vulnerability data.** Each software version gets its own SBOM. It carries no vulnerability information, which belongs in security advisories such as CSAF or VEX (§1, §3.1).
- **Depth.** Dependencies are resolved recursively, from every delivered component down to the first component outside the scope of delivery (§5.1).
- **Fields** (§5.2):
  - each SBOM carries its creator and a timestamp;
  - each component carries its creator, name, version, filename, dependencies with a completeness flag, distribution licences, a SHA-512 hash, and three properties (executable, archive, structured);
  - further fields are required when they exist.
- **Licences.** They are named by SPDX identifier, then from the ScanCode LicenseDB, then by the inventorying party's own LicenseRef (§6.1).

Version 2.1.0 raised the minimum formats from CycloneDX 1.5 and SPDX 2.2.1. It also introduced logical and identified components, and added an informative mapping of every field to CycloneDX and SPDX (Table 1, §8.2).

## Applicability

- **Security: adjacent.** SBOM data supports vulnerability handling, because a product's component list can be compared with vulnerability data (§1). But the guideline sets no security controls, and it keeps vulnerability statements out of the SBOM.
- **Cryptography: adjacent.** Its one cryptographic requirement is a SHA-512 hash of each deployable component (§5.2.2). The optional source-code hash has no defined method yet (§5.2.5).
- **This project: core.** It is the national SBOM baseline in RPT-0004 (product composition). Its fields bear on component identity in the core object model (DEC-001a), and its format floor bears on which SBOM formats and versions tmodel imports (DEC-002). tmodel#172 extracts its normative statements into `research/0017-requirements-extraction/bsi-tr-03183-2.yaml` (52 Requirements).

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
- **Notes are not normative.** Notes in the text use lowercase "must" and "recommended"; under §2 they are not normative. One example is the advice to use UTC timestamps.
