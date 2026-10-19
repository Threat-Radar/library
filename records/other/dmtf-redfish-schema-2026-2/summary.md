---
schema: "library-summary/v1"
id: dmtf-redfish-schema-2026-2
record: dmtf-redfish-schema-2026-2
type: summary
updated: "2026-10-18"
---

# Redfish Schema Bundle

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | `standard` |
| **Authors** |  |
| **Published** | 2026-08-07 |
| **Identifier** | dmtf: DSP8010 |
| **Source** | https://www.dmtf.org/sites/default/files/standards/documents/DSP8010_2026.2.zip |
| **Digest** | `86df1429b90ac2e2f96ec54687cb0bafadf0620588319de3b285a05ae4bfe680` |

## Overview

**A stub: not read in full.** DMTF's Redfish Schema Bundle, release 2026.2: the normative definitions of the Redfish data model in three functionally equivalent schema languages (CSDL, JSON Schema and OpenAPI), plus Redfish Device Enablement dictionaries. The model describes the resources a management service reports, such as processors and their cores, memory, PCIe devices and functions, chassis and their containment, assemblies, software and firmware inventory, and component integrity reported through SPDM, a TPM or similar modules. Cited by tmodel RPT-0004 (tmodel#38): Redfish properties for processors and cores, PCIe devices and functions, chassis containment, assemblies with country of origin, software inventory bound to devices and component integrity (Table 4b; mapping rows on processors, buses, composition and origin).

## Applicability

A stub. `bears_on` (DEC-001, DEC-004) comes from RPT-0004's source log and was not re-assessed here.

## Implementations

Not searched.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this summary |

## Limits

Not read in full. Checked the bundle's identity, readme cover, folder layout, six schema digests and the ComponentIntegrity types; the record covers the whole bundle while RPT-0004 relies on about nine schemas, which were not re-read property by property.
