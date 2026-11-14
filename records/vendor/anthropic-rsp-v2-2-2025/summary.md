---
schema: "library-summary/v1"
id: anthropic-rsp-v2-2-2025
record: anthropic-rsp-v2-2-2025
type: summary
updated: "2026-11-13"
lane: catalogs-schema
reviewed_by: ""
---

# Responsible Scaling Policy, Version 2.2

|  |  |
|---|---|
| **Type** | article (company policy; **superseded**, see Limits) |
| **Maturity** | _unset — do not guess_ |
| **Authors** | Anthropic |
| **Published** | Version 2.2, effective 2025-05-14; 23 pages |
| **Identifier** | https://www.anthropic.com/rsp (version history) |
| **Source** | https://assets.claude.com/872c653b2d0501d6ab44cf87f43e1dc4853e4d37.pdf |
| **Digest** | `4807f3970c76968a75a6dffa55d8ffe547014522b63c67e261cd02f7b6fc1e39` (matches `sources.md` S-0798) |

## Overview

Anthropic's policy for deciding when a model is capable enough to need stronger protection. **Capability Thresholds** (here, CBRN weapons and autonomous AI R&D) trigger **Required Safeguards**, defined as AI Safety Level (ASL) standards with two halves: a Deployment Standard against misuse and a Security Standard against weight theft. The rest of the policy is the procedure: capability and safeguards assessments, what happens when a safeguard cannot be met, and internal governance.

For a threat model, the useful part is §4.2, the **ASL-3 Security Standard**. It says which attackers the weight security must stop.
- **In scope:** hacktivists, criminal hacker groups, organized cybercrime, terrorist organizations, corporate espionage teams, internal employees, and state programs that use broad, non-targeted techniques.
- **Out of scope:** state programs that target Anthropic specifically (novel attack chains, insider compromise), and about ten non-state actors with state-level resources who can build 0-day attack chains.
- **Footnote 11 narrows "internal employees" to basic insiders,** those with no persistent or requestable access to systems that process weights. Sophisticated and state-compromised insiders are out of scope.

It asks for threat modeling with MITRE ATT&CK, and alignment with existing guidance including RAND's *Securing AI Model Weights*.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | An explicit attacker scope for protecting model weights, from a frontier developer. |
| Cryptography | none | Encryption is named only as one perimeter control. |
| This project | adjacent | An attacker-capability tiering such as "non-targeted state programs in, targeted ones out" is the kind of input **DEC-003**'s feasibility rating needs (ADR-0006, attack potential). It is policy, not a model tmodel can import. |

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | adjacent | AIT-055 | One of AIT-055's five sources (weight exfiltration by intrusion or insider). It reports no attack; it sets which attackers the defence must stop. |
| Existing AI threat models | core | TM-100 | It is TM-100's source. TM-100's "attacker groups in scope" decomposition comes from §4.2, and that structure is gone from the current policy (see Limits). |
| Weakness enumerations | adjacent | AML.T0025, AML.T0048.004 | The policy cites no catalog ids. `sources.md` gives S-0798 **AML.T0024.002**, which ATLAS 2026.09 names "Extract AI Model", that is, extraction by querying. The policy is about stealing the weights themselves, which AIT-055 maps to Exfiltration via Cyber Means (AML.T0025) and AI Intellectual Property Theft (AML.T0048.004). `sources.md`'s other id, AML.T0054 (LLM Jailbreak), fits the Deployment Standard. |
| Attack → asset mapping | core | A02; C03, C04, C05 | The protected asset is the weights (A02) wherever they are processed, which spans training, registry and serving. The policy names no components; it asks for perimeters, lifecycle security and monitoring around them. |

## Implementations

None, searched 2026-11-13: a policy, not software. Anthropic's capability and safeguards reports under the policy are separate documents.

| Name | Kind | License | URL |
|---|---|---|---|

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, digest, `superseded_by` and `cites` |
| `summary.md` | this summary, with the RPT-0014 applicability table |

## Reference expansion

The policy has no reference list. Its named sources were checked against `sources.md` and the library on 2026-11-13:
- RAND, *Securing AI Model Weights* (S-0793);
- *Deploying AI Systems Securely* (S-1180);
- MITRE ATT&CK (library `mitre-attack`);
- SSDF (S-0843; library `sp-800-218`).

SOC 2 and NIST SP 800-53 are general security control frameworks, out of scope for RPT-0014. No in-scope source is missing, so there are no stubs.

## Limits

- **Superseded.** Anthropic replaced it with v3.0 on 2026-02-24, a full rewrite, and then v3.1 to v3.4. v3.4 is in effect from 2026-07-08 and recorded as `anthropic-rsp-v3-4-2026`.
  - v3.4 drops the ASL-3 attacker-group list.
  - Its weight security for highly capable models is stated as "roughly in line with RAND SL4", and it names maximal-access insiders as a threat.
  - **TM-100 therefore describes a policy no longer in force.** The integration lane should decide whether TM-100 follows v3.4 (which then lines up with TM-101's RAND-level approach) or stays a historical entry.
- **A promise to test, not a result.** Whether Anthropic met the standard is outside this document.
- **The out-of-scope list sets a ceiling.** A tmodel threat model that adopted it would deliberately not defend against targeted state actors.
- **Two "v2.2" PDFs.** The RSP page also links a redline of v2.1 to v2.2 (sha256 `3fd9544b…`) with the same label; it differs in footnote 11's tracked changes. This record is the clean copy that `sources.md` pins.
- **Read in part.** Read in full: the overview (§§1–2), §4.2 with its footnotes, and the change log. The assessment procedures and governance sections (§§3, 5–7) were skimmed.
