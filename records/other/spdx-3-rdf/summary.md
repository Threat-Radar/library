---
schema: "library-summary/v1"
id: spdx-3-rdf
record: spdx-3-rdf
type: summary
updated: "2026-09-26"
---

# SPDX 3.0 RDF Model (ISO/IEC 5962)

|  |  |
|---|---|
| **Type** | spec (standard) |
| **Source** | https://spdx.github.io/spdx-spec/v3.0.1/annexes/rdf-model/ |

## Overview

SBOM data model as RDF/OWL/SHACL (Element, Artifact, Package, Vulnerability, License; Core/Software/Security/Build/AI profiles).

## Applicability to tmodel

Most graph-native SBOM standard — first-class fit if tmodel uses a triple store.

- Ratings — security: core · cryptography: adjacent · this project: adjacent
- Bears on: DEC-002
- Gathered for RPT-0011 (Knowledge Graphs and NSF OKN), tmodel #25.
