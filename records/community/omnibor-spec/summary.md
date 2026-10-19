---
schema: "library-summary/v1"
id: omnibor-spec
record: omnibor-spec
type: summary
updated: "2026-10-18"
---

# OmniBOR Specification

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | `draft` |
| **Authors** | OmniBOR Community |
| **Published** | 2024-10-13 |
| **Identifier** | git: https://github.com/omnibor/spec |
| **Source** | https://raw.githubusercontent.com/omnibor/spec/03cd41e6faffcdb7b54dc99e2ba1ec54456b2866/spec/SPEC.md |
| **Digest** | `d81992650a9feed63a128e5e2c066df86d91e3d97e4e75991e0fe6323567d698` |

## Overview

**A stub: not read in full.** The OmniBOR specification defines content-based Artifact Identifiers (gitoids, computed the way git computes a blob object id), Input Manifests that list the identifiers of every input used to build an artifact, and the Artifact Dependency Graph these manifests form, with annexes on file system storage and on embedding identifiers in ELF and source files. Version 0.1 is a draft that allows SHA-1 and SHA-256 gitoids. Cited by tmodel RPT-0004 (tmodel#38): how artifact identifiers are computed (git object header plus bytes), SHA-1 versus SHA-256, the v0.2 draft's SHA-256-only and newline-normalization rules, and the provisional IANA gitoid scheme.

## Applicability

A stub. `bears_on` (DEC-001, DEC-002) comes from RPT-0004's source log and was not re-assessed here.

## Implementations

Not searched.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this summary |

## Limits

Not read in full. The v0.1 SPEC.md header and structure, the v0.2 draft header and the IANA registration checked 2026-10-18; the annexes were not read.
