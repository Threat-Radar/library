---
schema: "library-summary/v1"
id: aquasecurity-trivy
record: aquasecurity-trivy
type: summary
updated: "2026-10-18"
---

# Trivy

|  |  |
|---|---|
| **Type** | repo |
| **Maturity** | `implementation` |
| **Authors** | Aqua Security |
| **Published** | 2026-10-01 |
| **Identifier** | git: https://github.com/aquasecurity/trivy |
| **Source** | https://github.com/aquasecurity/trivy/releases/tag/v0.75.0 |
| **Digest** | `not fetched` |

## Overview

**A stub: not read in full.** Trivy is Aqua Security's security scanner for container images, filesystems, remote git repositories, virtual machine images and Kubernetes. It builds its own package inventory or reads an SBOM, matches OS packages against the OS vendor's advisories and language packages against its listed advisory sources, and writes reports and CycloneDX or SPDX 2.3 SBOMs. Cited by tmodel RPT-0004 (tmodel#38): how a second scanner matches packages (vendor advisories for OS packages, no CPE matching), what each finding records, and how it reads third-party SBOMs (no SPDX 3, and OS packages lost from Syft's SPDX 2.3 output).

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

Not read in full. I checked the v0.75.0 tag, release and checksums, nine source and documentation files at v0.75.0, six trivy-db files at the pinned commit, the v0.76.0 changelog and go.mod, and four GitHub discussions; I did not run Trivy. No digest: Repo record, pinned by commit; the release page itself was not digested. The release asset trivy_0.75.0_checksums.txt has SHA-256 43a87485d39b60dae55cb1a14725dddd612040c0b1ec4caa88948c07d6c06219 and lists trivy_0.75.0_macOS-ARM64.tar.gz at 4a77108cccf8e55c8d6823e1e759939a622277e66cd0daa3c1fc621ed69e4568; both match Phase 1. All nine Trivy files of rows L163 and L226 and all six trivy-db files of row L164 match their Phase 1 digests.
