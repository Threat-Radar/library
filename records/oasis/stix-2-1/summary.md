---
schema: "library-summary/v1"
id: stix-2-1
record: stix-2-1
type: summary
updated: "2026-10-25"
---

# STIX Version 2.1 (OASIS Standard, 10 June 2021)

|  |  |
|---|---|
| **Type** | spec (standard) |
| **Publisher** | OASIS Cyber Threat Intelligence (CTI) TC |
| **Version** | STIX 2.1 OASIS Standard, 10 June 2021 |
| **Source** | https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html |
| **Digest** | `612b61506fd85d1e49f3bf12ca61a6bd5dcb676e351d714b99134bb494ff6c69` (the HTML) |

## Overview

STIX 2.1 is a JSON graph language for cyber threat intelligence. Its node types are **19 STIX Domain Objects** (§4.1–4.19): Attack Pattern, Campaign, Course of Action, Grouping, Identity, Incident, Indicator, Infrastructure, Intrusion Set, Location, Malware, Malware Analysis, Note, Observed Data, Opinion, Report, Threat Actor, Tool, Vulnerability. It also defines Cyber-observable Objects and two **STIX Relationship Objects** (§5.1 Relationship, §5.2 Sighting). Appendix B summarises the allowed relationship types per object pair. A common `confidence` property takes 0–100 (Appendix A maps other scales onto it). The spec marks **Course of Action** as a stub in 2.1 (§4.3): it supports prose courses of action, not automated ones.

The earlier version of this record said "17 SDO node types"; the OS text has 19.

## Applicability to tmodel

| Axis | Rating | Why |
|---|---|---|
| Security | core | The interchange format for CTI; ATT&CK ships in it. |
| Cryptography | adjacent | — |
| This project | core | The schema tmodel's import layer reads (`mitre-attack` is a STIX bundle) and a reference for typed edges. |

Bears on **DEC-001** and **DEC-002**.

**Implications for tmodel (inference).** (1) STIX Opinion and Note are a ready-made pattern for DEC-001a's `Review` and the reified `Assertion` edges: a separate object that points at other objects and carries an author and confidence. tmodel can map to them on export without adopting STIX internally. (2) Because Course of Action is a stub, STIX gives no structure for mitigation status. ADR-0006's mitigation status (a peer of risk) has to stay tmodel-native. (3) The 0–100 `confidence` is a single number. If exported, it should be a projection of tmodel's review state, never an input to Risk = M(I,F).

## Implementations

`oasis-open/cti-python-stix2` (BSD-3-Clause) is the reference Python library. Others were not searched.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata; digest of the OS HTML |
| `summary.md` | this summary |

## Limits

- Read the table of contents, §4 headings, the Course of Action note and the confidence rules. Not a property-by-property reading.
- TAXII and the STIX patterning grammar were not reviewed.
