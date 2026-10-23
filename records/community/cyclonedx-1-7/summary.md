---
schema: "library-summary/v1"
id: cyclonedx-1-7
record: cyclonedx-1-7
type: summary
updated: "2026-10-22"
---

# CycloneDX Bill of Materials Specification

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | `standard` — adopted by the Ecma General Assembly, December 2025 |
| **Authors** | Jan Kowalleck, Steve Springett (Ecma TC54) |
| **Published** | 2025-12 (spec 1.7 released 2025-10-21) |
| **Identifier** | ECMA-424, 2nd edition · CycloneDX 1.7 |
| **Source** | https://ecma-international.org/wp-content/uploads/ECMA-424_2nd_edition_december_2025.pdf |
| **Digest** | `e8c55a3a968f3ef534fbcdd891c361714d3dc303b3747464f1d554f65b04c8e1` |

## Overview

**A stub: nobody has read this specification in full or extracted it (FX-1).**
CycloneDX 1.7 is OWASP's bill-of-materials format, published by Ecma as
ECMA-424, 2nd edition (the same text; `ecma-424` is a duplicate pointer to this
record). A CycloneDX BOM lists components, from libraries and containers to
devices and firmware, with their identifiers, the dependencies between them,
how complete those lists are, and optionally vulnerabilities with a VEX
analysis. Kept because tmodel RPT-0004 (product composition, tmodel#8 and
tmodel#38) and RPT-0005 (schema representations, tmodel#39) cite it.

## Applicability

A stub. `bears_on` (R-M-07, R-M-11) and the `adjacent` ratings in `record.yaml`
are the upstream `sbom` lane's and were not re-assessed here. tmodel's
committed imports are OTM and STIX 2.1 (tmodel ADR-0007, which lets the
tmodel#39 crosswalk extend that list), so tmodel does not import CycloneDX
today. RPT-0004 Table 6 (tmodel#127, a draft) proposes how a CycloneDX SBOM's
fields would fill the inputs of tmodel's core object model, and accepts
nothing.

## Implementations

Not searched for this record. tmodel RPT-0004 §3 covers four tools that write
or read CycloneDX (Syft, Grype, Trivy, Dependency-Track). In Table 6's run on
2026-10-18, Syft 1.52.0 wrote CycloneDX 1.7 JSON and Grype 0.119.0 read it.

`record.yaml` lists two implementations RPT-0004 cites after its adversarial
review (tmodel#152, 2026-10-22), which get no record of their own
(docs/scope.md section 3): cdxgen v13.4.0, whose `--spec-version` accepts 1.6,
1.7 and 2.0, and protobom v0.6.2, which reads and writes CycloneDX 1.4 to 1.7
JSON. Both were read from their READMEs on 2026-10-22, not run.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this summary |

## Limits

Not read in full and not extracted. RPT-0004 §1.1 describes CycloneDX's
identity, hardware, dependency, completeness and vulnerability fields, quoting
their descriptions from the 1.7 JSON reference (cyclonedx.org/docs/1.7/json/).
Table 6 checked every field and enum value it names against
`schema/bom-1.7.schema.json` at CycloneDX/specification tag `1.7.2`, a patch
release of 2026-09-17 (sha256
`73308edec3ab2d38bfffd993e96a042b594314143b6971a6e9ed98bbb6bd76ce`; the file
at tag `1.7` differs). Whether this record gets an FX-1 extraction, here or in
the upstream `sbom` lane, is open (tmodel#38, question 2 of 2026-10-15).
