---
schema: "library-summary/v1"
id: cwe-1426-genai-output-validation
record: cwe-1426-genai-output-validation
type: summary
updated: "2026-10-13"
---

# CWE-1426: Improper Validation of Generative AI Output

|  |  |
|---|---|
| **Type** | web (CWE weakness entry) |
| **Maturity** | _unset — do not guess_ |
| **Authors** | CWE AI Working Group (submitted 2024-07-02); MITRE CWE Content Team |
| **Published** | Added in CWE 4.15 (2024-07-16); read as CWE 4.20 (last modified 2026-04-30) |
| **Identifier** | CWE-1426 |
| **Source** | https://cwe.mitre.org/data/definitions/1426.html |
| **Digest** | `ae231ad85146fd428d14780d897fc8c7c1a4df16a6633ca0350f97efde81d09e` (HTML as fetched; living page) |

## Overview

A CWE **Base** weakness: *the product invokes a generative AI/ML component whose outputs cannot be directly controlled, but does not validate (or insufficiently validates) those outputs* against its security, content or privacy policy. Its main mitigation is architectural — treat model output as **untrusted** and run it in a non-privileged space — plus operational controls such as semantic comparators and independent checking components. The observed example is **CVE-2024-3402**, a ChatGPT GUI that validated input but not model output, leading to cross-site scripting (CWE-79). CWE marks the entry's **vulnerability mapping as DISCOURAGED**: it should not be used to map real CVEs directly.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | A catalogued AI weakness in the standard weakness list. |
| Cryptography | none | Not about cryptography. |
| This project | core | Gives tmodel's Weakness nodes a CWE id for unvalidated model output (the sink side of injection chains). |

Bears on **DEC-001** (object model — Weakness nodes for AI) and **R-010** (CWE mapping).

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | adjacent | AIT-072 | The weakness behind prompt injection reaching classic sinks (XSS, command execution) |
| Existing AI threat models | none | — | A catalog entry, not a threat model |
| Weakness enumerations | core | CWE-1426, CWE-79, LLM05:2025 | Is the enumeration entry; chains to CWE-79; matches OWASP 'improper output handling' |
| Attack → asset mapping | core | C07, C17 | LLM application output handling; downstream consumers that render or execute it |

## Implementations

Part of the CWE catalog (`cwe` record). Searched 2026-10-13.

| Name | Kind | License | URL |
|---|---|---|---|


## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this summary |

## Limits

- **Mapping discouraged by CWE itself,** so it cannot serve as the main id for real vulnerabilities.
- **Living entry:** relationships changed in CWE 4.19 and 4.20; cite the version.
- **One weakness only;** most AI attack classes still have no CWE (RPT-0014 enumerations).
