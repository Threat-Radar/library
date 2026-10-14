---
schema: "library-summary/v1"
id: owasp-agentic-threats-mitigations-v1-1
record: owasp-agentic-threats-mitigations-v1-1
type: summary
updated: "2026-10-13"
---

# Agentic AI - Threats and Mitigations

|  |  |
|---|---|
| **Type** | web (resource page for a guide published as PDF) |
| **Maturity** | _unset — do not guess_ |
| **Authors** | OWASP GenAI Security Project — Agentic Security Initiative (ASI) |
| **Published** | Resource page dated 2025-02-17 (v1.0); `sources.md` records a v1.1 of December 2025 |
| **Identifier** | https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/ |
| **Source** | https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/ |
| **Digest** | `not fetched` (PDF is behind OWASP's download form; not fetched or read here) |

## Overview

**Not yet read** — the guide's PDF sits behind OWASP's download form, which this pass did not fill in. What the official resource page states: it is **the first in a series of guides** from the OWASP **Agentic Security Initiative (ASI)**, giving a **threat-model-based reference of emerging agentic threats** and discussing **mitigations**, motivated by LLMs expanding the scale, capabilities and risks of agentic systems. The team's round-1 catalog (`sources.md`, `threat-models.md` TM-059) indexes it for threats such as memory poisoning, tool misuse, privilege compromise and resource overload, and maps it to the OWASP agentic ids (ASI01–ASI10). Those claims are recorded as the catalog's, not verified here.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | A primary industry catalog of agentic threats. |
| Cryptography | none | Not about cryptography. |
| This project | core | Directly feeds tmodel's agentic attack classes and the agentic lane's crosswalk. |

Bears on **DEC-001** (object model — agentic threat classes). Status left `queued` until the PDF is read.

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | not assessed | AIT-139, AIT-140 (catalog) | Not read; catalog links only |
| Existing AI threat models | core | TM-059 | Is an agentic threat model (per the resource page) |
| Weakness enumerations | not assessed | ASI01–ASI10 (catalog) | Not read |
| Attack → asset mapping | not assessed | — | Not read |

## Implementations

Guide only. Searched 2026-10-13.

| Name | Kind | License | URL |
|---|---|---|---|


## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this summary |

## Limits

- **Not read.** The PDF requires OWASP's download form; to be completed after a team member downloads it (the team PDF manifest already lists a copy, sha256 `65e3bd59…`).
- **Version uncertain here:** the page shows v1.0 (Feb 2025); `sources.md` cites v1.1 (Dec 2025).
