---
schema: "library-summary/v1"
id: odonoghue-2024-sbom-generation
record: odonoghue-2024-sbom-generation
type: summary
updated: "2026-10-18"
---

# Impacts of Software Bill of Materials (SBOM) Generation on Vulnerability Detection

|  |  |
|---|---|
| **Type** | paper |
| **Maturity** | _unset_ |
| **Authors** | Eric O'Donoghue, Brittany Boles, Clemente Izurieta, Ann Marie Reinhold |
| **Published** | 2024-10-18 |
| **Identifier** | doi: 10.1145/3689944.3696164 |
| **Source** | https://fdn.montana.edu/cyber/products/Impacts%20of%20Software%20Bill%20of%20Materials%20-%20SBOM%20-%20Generation%20on%20Vulnerability%20Detection%20Final%20Version.pdf |
| **Digest** | `cb01909f3126bb46dde10488ec8fc2c1a6c4f423f4f6de43cc968a9eefa599de` |

## Overview

**A stub: not read in full.** A workshop paper that builds four SBOM corpora from 2,313 Docker images by varying the generator (Syft or Trivy) and the format (CycloneDX or SPDX), then scans them with Trivy, Grype and CVE-bin-tool to measure how much the reported vulnerabilities for the same artifact change with generation alone. It finds high variability attributable to SBOM generation. Cited by tmodel RPT-0004 (tmodel#38): published evidence that the SBOM generator and format change scanner results for the same artifact (dimension 5, Q4).

## Applicability

A stub. `bears_on` (DEC-002, DEC-008) comes from RPT-0004's source log and was not re-assessed here.

## Implementations

Not searched.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this summary |

## Limits

Not read in full. I read the title page and abstract of the authors' final version and the Crossref record; I did not re-check the paper's numbers or fetch its data pipeline repository.
