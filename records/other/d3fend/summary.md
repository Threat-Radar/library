---
schema: "library-summary/v1"
id: d3fend
record: d3fend
type: summary
updated: "2026-10-25"
---

# MITRE D3FEND 1.6.0 — defensive countermeasures knowledge graph

|  |  |
|---|---|
| **Type** | spec (ontology) |
| **Publisher** | The MITRE Corporation |
| **Version** | 1.6.0 (released 2026-08-31 per `d3fend.mitre.org/api/version.json`) |
| **Source** | https://d3fend.mitre.org/ontologies/d3fend.ttl |
| **Digest** | `4909a5bb66b75d2c359624398848936fb56a6b246bcd5cfcd277977a1277753a` (the TTL as downloaded; the site's published `ontology_hash_sha256` is for a different serialisation and does not match it) |

## Overview

D3FEND is an OWL ontology of defensive techniques. It is linked to offensive techniques (ATT&CK) through shared **digital artifacts**: a defence acts on an artifact that an offensive technique also uses. The ontology repository `d3fend/d3fend-ontology` is MIT-licensed.

**Counts computed from the 1.6.0 TTL with rdflib (2026-10-25):**

| Measure | Count |
|---|---|
| triples | 47,397 |
| defensive tactics | 7: Model, Harden, Detect, Isolate, Deceive, Evict, Restore |
| subclasses of `DefensiveTechnique` (transitive) | 272 |
| subclasses of `OffensiveTechnique` (transitive) | 874 |
| subclasses of `DigitalArtifact` (transitive) | 903 |

## Applicability to tmodel

| Axis | Rating | Why |
|---|---|---|
| Security | core | The only open, structured mitigation taxonomy tied to ATT&CK. |
| Cryptography | adjacent | Includes crypto-related hardening techniques. |
| This project | core | Mitigation vocabulary for ADR-0006 mitigation status; the artifact classes overlap tmodel's object model. |

Bears on **DEC-001** and **DEC-004**.

**Implications for tmodel (inference).** (1) D3FEND's artifact-mediated link (defence → artifact ← attack) is a typed path, not a direct "mitigates" edge. tmodel can store the derived mitigates edge as an `Assertion` with D3FEND provenance, which keeps the review layer honest. (2) The 903 artifact classes are a candidate controlled vocabulary for tmodel component types, but adopting them would tie the core schema to an external OWL release. Pin a version, per DEC-008. (3) ATT&CK v20.0 ships 44 mitigations of its own (`mitre-attack`). D3FEND is far finer-grained, so tmodel should pick one as primary and map the other.

## Implementations

Official site, API and ontology repo (MIT). No third-party tools searched.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata; pinned TTL digest |
| `summary.md` | this summary |

## Limits

- Counts are transitive `rdfs:subClassOf` closures. They include intermediate grouping classes, so they are not the number of leaf techniques shown on the website.
- The ATT&CK version that D3FEND's offensive classes track was not checked against v20.0.
