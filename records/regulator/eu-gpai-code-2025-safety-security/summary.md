---
schema: "library-summary/v1"
id: eu-gpai-code-2025-safety-security
record: eu-gpai-code-2025-safety-security
type: summary
updated: "2026-11-20"
lane: catalogs-schema
reviewed_by: ""
---

# Code of Practice for General-Purpose AI Models: Safety and Security Chapter

|  |  |
|---|---|
| **Type** | spec (a code under AI Act Article 56; **stub**: summarized for WAVE 1, not FX-1 extracted) |
| **Maturity** | _unset — do not guess_ |
| **Authors** | Chairs and vice-chairs of Working Groups 2 to 4, with the European Commission AI Office |
| **Published** | 2025-07-10 |
| **Identifier** | https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai |
| **Source** | https://ec.europa.eu/newsroom/dae/redirection/document/118119 |
| **Digest** | `d879f9b54c6068aae57ebaead9d90ddaa46f2503312b9185367a724fa8da2f4a` (43 pages) |

## Overview

The chapter applies to providers of general-purpose AI models with systemic risk (AI Act Article 55). Adhering to it is a way to show compliance, but "does not constitute conclusive evidence". It has ten Commitments:
1. a Safety and Security Framework;
2. systemic risk identification, with scenarios;
3. risk analysis (model-independent information, evaluations, modelling, estimation, post-market monitoring);
4. a risk acceptance determination, and whether to proceed;
5. safety mitigations;
6. **security mitigations**;
7. Model Reports;
8. allocation of responsibility;
9. **serious-incident reporting**;
10. further documentation.

Appendix 1.4 names four specified systemic risks: CBRN, loss of control, cyber offence and harmful manipulation.

**Commitment 6** protects models and infrastructure against "unauthorised releases, unauthorised access, and/or model theft". It doesn't apply to a model that is less capable than one whose weights are already public.
- **Measure 6.1:** a **Security Goal** naming the threat actors to resist, "including non-state external threats, insider threats".
- **Measure 6.2:** implement **Appendix 4**, or equivalent alternatives. Appendix 4 has five parts:
  - **4.1 general controls:** identity and access management, zero trust, email filtering, removable media, patching;
  - **4.2 unreleased weights:** a registry of every copy, copy alerts, 256-bit encryption with TPM-held keys, decryption only into non-persistent memory, confidential computing, physical access control;
  - **4.3 interface hardening:** least access with MFA reviewed every six months, security review of interface code, output rate limiting;
  - **4.4 insider threats,** "including in the form of (self-)exfiltration or sabotage carried out by models": background checks, training, sandboxes around models, and checking training data for tampering;
  - **4.5 assurance:** external reviews, red-teaming, bug bounties, personnel integrity tests, EDR/IDS and incident response.

**Measure 9.3** sets reporting deadlines from awareness:
- 2 days for serious disruption of critical infrastructure;
- **5 days for a serious cybersecurity breach, "including the (self-)exfiltration of model weights"**;
- 10 days for a death;
- 15 days for serious harm to health, rights, property or the environment.

Unresolved incidents get updates every four weeks, and a final report is due within 60 days of resolution.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | Concrete weight-security and insider controls, and incident deadlines, for frontier models |
| Cryptography | adjacent | Encryption at rest and in transit (256-bit, TPM-held keys) and confidential computing, named but not specified |
| This project | adjacent | A source of Requirements and controls for model-hosting Components (**DEC-001**). Appendix 4's objectives read as mitigations with stated aims |

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | adjacent | AIT-055, AIT-026 | AIT-055 (weight exfiltration by intrusion or insider) and AIT-026 (insider sabotage of training) cite it. It names attack goals, not techniques or incidents |
| Existing AI threat models | adjacent | — | The Security Goal is a threat-actor statement like the RSP's and FSF's (S-0798, S-0805), but each signatory chooses its own actors. The Code sets no actor tiers, unlike RAND's SL1 to SL5 |
| Weakness enumerations | adjacent | AML.T0048.004, ASI10, NISTAML.031 | The mapping is `sources.md`'s; the Code cites no catalog. `sources.md`'s "cites the RAND Securing AI Model Weights report" holds: Measure 7.3 names it as relevant guidance |
| Attack → asset mapping | core | C05, C15, C03, C12; A02, A01 | It protects model weights (A02) in storage, transport and use on serving and infrastructure (C05, C15), and training data against tampering (A01, C03). Insiders (C12) are a named threat. The mapping is ours |

## Implementations

None, searched 2026-11-20: commitments, not software.

| Name | Kind | License | URL |
|---|---|---|---|

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, digest and relations |
| `summary.md` | this summary, with the RPT-0014 applicability table |

## Reference expansion

The chapter cites one external work, the RAND *Securing AI Model Weights* report (Measure 7.3), which is RPT-0014 S-0793. No stubs were needed.

## Limits

- **A stub for FX-1.** A `spec`: its Commitments and Measures need full extraction before the record moves past stub.
- **Voluntary and scoped.** It binds only signatories, and only for systemic-risk models. The "less capable than an open-weight model" exemption can remove Commitment 6 entirely.
- **Signatories set their own threat actors.** The Security Goal has no required minimum attacker tier, so two compliant providers can defend against very different actors.
- **Only one chapter read.** The Code's Transparency and Copyright chapters aren't part of this record.
