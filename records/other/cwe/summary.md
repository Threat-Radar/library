---
schema: "library-summary/v1"
id: cwe
record: cwe
type: summary
updated: "2026-10-08"
---

# MITRE CWE — Common Weakness Enumeration

|  |  |
|---|---|
| **Type** | dataset (best-practice) |
| **Publisher** | The MITRE Corporation (CWE Program) |
| **Version** | CWE List 4.20, catalog dated 2026-04-30; XML schema 7.3 (December 11, 2025), namespace `http://cwe.mitre.org/cwe-7` |
| **Source** | https://cwe.mitre.org/data/xml/cwec_v4.20.xml.zip — SHA-256 `3976f599…5e9d7d50`; unzipped `cwec_v4.20.xml` `1f5a78bd…0912e` |
| **Schema** | https://cwe.mitre.org/data/xsd/cwe_schema_v7.3.xsd — SHA-256 `690dedee…e45f98` |
| **Licence** | CWE terms of use (https://cwe.mitre.org/about/termsofuse.html); copies of the schema must keep MITRE's licence header |

## Overview

CWE is a catalog of software and hardware weakness types, published by MITRE
as one XML file per release and validated by a closed XML Schema. Each entry
has a permanent integer id (`CWE-79`) that is never reused, even after
deprecation. Entries are Weaknesses (at Pillar, Class, Base, Variant or
Compound abstraction; Simple, Chain or Composite structure), Categories and
Views. Relations between weaknesses are typed and scoped to a view
(`ChildOf` in view 1000 can differ from `ChildOf` in view 699). Every entry
also says whether it may be used to map real vulnerabilities
(`Mapping_Notes/Usage`).

## Applicability

- **Security: core.** The common vocabulary for weakness classes; CVE records
  and NVD cite it.
- **Cryptography: adjacent.** Covers cryptographic weaknesses as entries; not
  a cryptographic specification.
- **This project: core.** The external key for tmodel's Weakness type
  (ARCH-0001 §3, R-010); its typed, view-scoped relations test DEC-001's edge
  model; its file-per-release distribution bears on DEC-008 (mirror vs live
  lookup) and its closed XSD on DEC-002 (import formats). Details in
  `distilled/design-notes.md`.

## Implementations

Not searched in this pass (2026-10-08); left for the RPT-0005 fan-out.
Consumers already held in this library: CVE Record Format 5.x
(`problemTypes[].descriptions[].cweId`, record `cve-json-5`) and Open Threat
Model (`threats[].cwes`, record `open-threat-model`).

## Artifacts in this record

- `record.yaml` — metadata, digests, relations, FX-1 distillation block.
- `distilled/` — the FX-1 artifact set; `distilled/README.md` indexes each
  file and its coverage: normative text and requirements from the XSD, the
  verbatim XSD, every structure and enumeration, the entry lifecycle, test
  fixtures cut from the 4.20 catalog with expected results, design notes for
  tmodel, and the verification record.

## Limits

- The record pins the XML distribution only. CSV and HTML views, and any
  MITRE web API, were not examined.
- The schema's documentation contradicts its own structure in places, and the
  4.20 data departs from the documentation in a few more (recorded under
  `source_defects` in `distilled/requirements.yaml` and in
  `distilled/verification.md`). The XSD is treated as authoritative for
  structure.
- MITRE's root-cause mapping guidance (which prefers Base and Variant entries)
  is a separate document and not covered here.
- Gathered for RPT-0011 (tmodel #25); fully extracted for RPT-0005 (tmodel #39).
