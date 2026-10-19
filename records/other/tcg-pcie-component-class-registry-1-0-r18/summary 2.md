---
schema: "library-summary/v1"
id: tcg-pcie-component-class-registry-1-0-r18
record: tcg-pcie-component-class-registry-1-0-r18
type: summary
updated: "2026-10-18"
---

# PCIe-based Component Class Registry

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | `standard` |
| **Authors** | TCG Infrastructure Work Group (IWG) |
| **Published** | 2021-10-27 |
| **Identifier** | https://trustedcomputinggroup.org/wp-content/uploads/TCG_PCIe_Component_Class_Registry_v1_r18_pub10272021.pdf |
| **Source** | https://trustedcomputinggroup.org/wp-content/uploads/TCG_PCIe_Component_Class_Registry_v1_r18_pub10272021.pdf |
| **Digest** | `453bad2ac9729058c3403592952d1c2a0a8aec6702fc8a5aed351e26c80eea10` |

## Overview

**A stub: not read in full.** TCG registry that specifies how identifiers held in PCI and PCIe configuration space and capabilities are translated into the componentIdentifier fields of a Platform Certificate, so that a verifier can compare a certificate's component data with values read from the device. It gives the required values, a notation, and worked examples with sample configuration-space data. Cited by tmodel RPT-0004 (tmodel#38): the rule that maps PCIe configuration-space identifiers (class code, vendor, device and serial data) to Platform Certificate component fields.

## Applicability

A stub. `bears_on` (DEC-001) comes from RPT-0004's source log and was not re-assessed here.

## Implementations

Not searched.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this summary |

## Limits

Not read in full. Checked the cover, scope, contents list and acknowledgements; the translation table was not re-read field by field here.
