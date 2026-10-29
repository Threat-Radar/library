---
schema: "library-summary/v1"
id: spdx-3-0-1
record: spdx-3-0-1
type: summary
updated: "2026-10-22"
---

# System Package Data Exchange (SPDX) Specification Version 3.0.1

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | _unset_ — approved SPDX release; ISO/OMG ratification of the 3.x line still in progress |
| **Authors** | The Linux Foundation and its Contributors |
| **Published** | 2024-12-17 |
| **Identifier** | SPDX 3.0.1 · git tag `3.0.1` |
| **Source** | https://spdx.github.io/spdx-spec/v3.0.1/ |
| **Digest** | none — multi-page site and multi-part PDF; release tag pinned instead |

## Overview

**A stub: nobody has read this specification in full or extracted it (FX-1).**
SPDX 3.0.1 is the bill-of-materials specification of the Linux Foundation's
SPDX project. SPDX 3 is a graph model: packages, files, relationships,
vulnerabilities and their assessments are all elements with a global `spdxId`,
and machine-readable files define the model (an RDF/OWL ontology with SHACL
shapes, a JSON-LD context and a JSON Schema). Kept because tmodel RPT-0004
(product composition, tmodel#8 and tmodel#38) and RPT-0005 (schema
representations, tmodel#39) cite it.

## Applicability

A stub. `bears_on` R-M-07 and R-M-11 and the `adjacent` ratings in
`record.yaml` are the upstream `sbom` lane's; DEC-002 was added in this fork
for the RDF model (see the note below). None was re-assessed here. tmodel's
committed imports are OTM and STIX 2.1 (tmodel ADR-0007, which lets the
tmodel#39 crosswalk extend that list), so tmodel does not import SPDX today.
RPT-0004 Table 6 (tmodel#127, a draft) proposes how an SPDX 3 SBOM's elements
would fill the inputs of tmodel's core object model, and accepts nothing.

## Implementations

Not searched for this record. tmodel RPT-0004 §3 covers four tools that write
or read SBOMs (Syft, Grype, Trivy, Dependency-Track). In Table 6's run on
2026-10-18, Syft 1.52.0 wrote SPDX 3.0.1 JSON-LD (`-o spdx-json@3.0`) and
Grype 0.119.0 read it.

`record.yaml` lists three more implementations RPT-0004 cites, which get no
record of their own (docs/scope.md section 3): spdx3-validate 0.0.7,
spdx/tools-golang (SPDX 3 code only in the v0.6.0-rc4 pre-release; SPDX 3.0.1
support on its main branch, unreleased) and the OpenEmbedded-Core SPDX 3.0
classes of Yocto Project 6.0.3. Zephyr's `west spdx` is cited too, but its
v4.4.2 release writes only SPDX 2.2 and 2.3, so it is not listed here.

Two more were added after RPT-0004's adversarial review (tmodel#152,
2026-10-22), from release notes, READMEs and test files, not runs:
Microsoft's sbom-tool, which writes and validates SPDX 3.0 on request since
v4.0.2, and cdxgen, which converts its CycloneDX output to SPDX 3.0.1 JSON-LD
since v12.3.0. protobom v0.6.2 lists SPDX 3.0 and 3.1 as planned, so it is
listed under `cyclonedx-1-7` instead.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this summary |

## Limits

Not read in full and not extracted. RPT-0004 §1.2 describes SPDX's identity,
hardware, relationship, completeness and vulnerability terms. Table 6 checked
every class, property and enum value it names against three 3.0.1 model files
as served by spdx.org: `rdf/3.0.1/spdx-model.ttl` (sha256
`30ebb4af2d70a9809044ef46f44cc3dc5125226d70f818a50ed2e1d5f404c593`),
`rdf/3.0.1/spdx-context.jsonld`
(`c72b0928f094c83e5c127784edb1ebca2af74a104fcacc007c332b23cbc788bd`) and
`schema/3.0.1/spdx-json-schema.json`
(`582c64e809d5b3ef9bd0c4de13a32391b47b0284a3e8d199569fb96f649234b1`).

The served model is not byte-identical to `rdf/spdx-model.ttl` at this record's
pinned tag `3.0.1`
(`77b058ebbea268db1ad191f54da908945d4c279110a5e28b20eae4ac201a5cf8`).
Compared with rdflib on 2026-10-18, the two define the same classes,
properties, descriptions and enum values, and differ only in the ontology's
label and in their SHACL shapes: the served file has 124 `sh:class`
constraints against 71 at the tag, and one more property shape. SHACL
validation of real SPDX output was not run. Whether this record gets an FX-1
extraction, here or in the upstream `sbom` lane, is open (tmodel#38, question
2 of 2026-10-15).

## Note — RDF/graph-native serialization (tmodel)

SPDX 3.0.1 defines an **RDF/OWL model with a SHACL profile** ([RDF-model annex](https://spdx.github.io/spdx-spec/v3.0.1/annexes/rdf-model/)) — the most graph-native SBOM standard, a first-class fit if tmodel uses a triple store. (Consolidated here from the former `other/spdx-3-rdf`; bears on tmodel DEC-002.)
