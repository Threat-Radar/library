---
schema: "library-summary/v1"
id: anthropic-rsp-v3-4-2026
record: anthropic-rsp-v3-4-2026
type: summary
updated: "2026-11-22"
lane: catalogs-schema
reviewed_by: ""
---

# Responsible Scaling Policy, Version 3.4

|  |  |
|---|---|
| **Type** | article (company policy; the version in force, checked 2026-11-22) |
| **Maturity** | _unset — do not guess_ |
| **Authors** | Anthropic |
| **Published** | Version 3.4, effective 2026-07-08; 21 pages. v3.0 (2026-02-24) was a full rewrite; v3.1 to v3.3 followed on 2026-04-02, 2026-04-29 and 2026-05-26 |
| **Identifier** | https://www.anthropic.com/responsible-scaling-policy (`/rsp` redirects there) |
| **Source** | https://assets.claude.com/0bacdc8440ea96e62a8766d99ebe1d4eea6d5f3a.pdf |
| **Digest** | `6247b9e4001fd342827526fabc476c9d4dd6b2041ac00055f0ccda26f4d0b07d` |

## Overview

Anthropic's "voluntary framework for managing catastrophic risks". It is current, and it **supersedes v2.2** (S-0798, `anthropic-rsp-v2-2-2025`). The policy has four parts.

1. **Recommendations for industry-wide safety** (§1). A table maps four **thresholds** to two kinds of mitigation: what Anthropic plans as a company, and what it recommends for the whole industry. The recommendations are explicitly not unilateral commitments; Appendix A sets competitor-contingent commitments instead.
   - **Non-novel chemical and biological weapons.**
     - *Company plan:* maintain ASL-3 protections. That means classifier guards "at least as robust as our initial Constitutional Classifiers", access controls for trusted users with classifier exemptions, red-teaming, bug bounties, threat intelligence, and security controls.
     - *Recommendation:* "precautions against opportunistic theft of model weights, such as centralized controls on third-party applications and software updates".
   - **Novel chemical and biological weapons.** Even well-resourced actors should not be able to jailbreak models reliably, or to cause harm "via stolen or modified model weights". That means security "roughly in line with RAND SL4".
   - **Misaligned AI in high-stakes settings.** AI systems that are highly relied on, with access to sensitive assets and some capacity for subterfuge, could carry out sabotage. The defenses are internal compartmentalization and code review, capability assessments, internal monitoring, and evidence about propensity to deceive.
   - **Automated R&D in key domains.**
     - *Company plan:* "moonshot R&D for security"; an "eyes on everything" state, with logs of all critical AI-development work analyzed by AI "for … security threats, concerning behavior by insiders (humans as well as AI systems themselves)"; and internal red-teaming that beats the bug bounty.
     - *Recommendation:* SL4 against top-tier states, and "even malicious employees and other insiders with maximal levels of access", up to the CEO, must not be enabled to cause catastrophic harm.
2. **The Frontier Safety Roadmap** (§2): public goals across Security, Alignment, Safeguards and Policy, graded openly (`anthropic-2026-frontier-safety-roadmap`).
3. **Risk Reports** (§3), every three to six months. Each must cover threat-model identification and specification, evidence, mitigations, a residual risk analysis for each threat model and overall, and a risk-benefit determination. External review is required for highly capable models whose reports are significantly redacted. **The threat models now live in these reports**: see `anthropic-2026-risk-report-august`.
4. **Governance** (§4): a Responsible Scaling Officer, briefings for the Long-Term Benefit Trust, unredacted reports to at least 200 employees, noncompliance reporting, and no non-disparagement terms that block safety concerns.

**Appendix B redefines ASLs.** They are now names for groups of safeguards Anthropic currently maintains, not lists of required controls for future capability levels. Instead, the policy asks "what sort of argument an AI developer should make (and what sorts of actors it should address)".

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | Threat-actor classes for each threshold (individuals and small teams, well-resourced teams, top-tier states, maximal-access insiders, the AI itself), with weight-security targets tied to RAND SL levels |
| Cryptography | none | No cryptographic content |
| This project | adjacent | Actor classes per threshold are the input **DEC-003**'s feasibility rating needs. The threat model and mitigations to import (**DEC-001**) are in the Risk Reports, not here |

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | adjacent | AIT-055, AIT-073 to AIT-077, AIT-026, AIT-117, AIT-115 | It names weight theft and modification (AIT-055), jailbreaking (AIT-073 to 077), insiders (AIT-026, AIT-117) and AI sabotage (AIT-115) as what the mitigations must address. It reports no attacks; the Risk Reports carry the incidents |
| Existing AI threat models | core | TM-100 | **TM-100's source (v2.2) is superseded.** v3.4 replaces v2.2's ASL-3 attacker-group list with threshold rows naming actor classes, and moves threat models into the Risk Reports. TM-100 should follow v3.4 together with the August 2026 Risk Report, whose ASL-3 security scope is still non-state actors in, sophisticated insiders and nation states out |
| Weakness enumerations | adjacent | AML.T0025, AML.T0048.004, AML.T0054 | The policy cites no catalog. Weight theft maps to AML.T0025 and AML.T0048.004 (as for AIT-055), and jailbreaks to AML.T0054. `sources.md`'s AML.T0024.002 for S-0798 doesn't fit, and ATLAS 2026.10 removed it |
| Attack → asset mapping | core | A02, A03; C05, C12, C15, C08 | It protects the weights (A02) and safeguard behaviour (A03) on product surfaces (C05) and internal infrastructure (C15), against insiders (C12) and internal AI agents (C08). The mapping is ours |

## Implementations

None, searched 2026-11-22: a policy. Its required outputs are the Risk Reports and the Roadmap, recorded separately.

| Name | Kind | License | URL |
|---|---|---|---|

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, digest, `supersedes` and `cites` |
| `summary.md` | this summary, with the RPT-0014 applicability table |

## Reference expansion

The policy has no reference list. The documents it names were checked against `sources.md` and the library on 2026-11-22:
- **In `sources.md`:** RAND's SL levels (S-0793, `nevo-2024-securing-ai-model-weights`) and Constitutional Classifiers (S-0460).
- **Added (none were held):**
  - the August 2026 Risk Report, published after v3.4 and summarized under `see_also`;
  - three stubs: the February 2026 Risk Report (its "initial Risk Report"), the Frontier Safety Roadmap, and the ASL-3 activation report (the ASL-3 protections it says it will maintain);
  - the SB 53 compliance framework announcement, a stub, because the policy defers statutory definitions to separate compliance frameworks.
- **Out of scope:** the Usage Policy, and the v3.0 change summary.

## Limits

- **Recommendations aren't commitments.** The right-hand column is "ambitious" and explicitly not unilateral. What binds Anthropic is the company-plan column and Appendix A, which depends on what competitors do.
- **No control lists.** Apart from the ASL-3 safeguards it says it will maintain, the policy names no controls. Thresholds are argued case by case, so a threat model gets more from the Risk Reports.
- **A living document.** Four revisions came in five months of 2026, so check the RSP page before citing it.
- **Read in part.** Read in full: the introduction, §1's table, §2, §3.1 to §3.3, §3.6, §4, Appendices A and B, and the changelog for v3.0 to v3.4. §3.4 and §3.5 (procedures, redactions) were skimmed.
