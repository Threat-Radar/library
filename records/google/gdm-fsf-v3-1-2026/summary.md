---
schema: "library-summary/v1"
id: gdm-fsf-v3-1-2026
record: gdm-fsf-v3-1-2026
type: summary
updated: "2026-11-22"
lane: catalogs-schema
reviewed_by: ""
---

# Frontier Safety Framework, Version 3.1

|  |  |
|---|---|
| **Type** | article (company framework; the version in force, checked 2026-11-22) |
| **Maturity** | _unset — do not guess_ |
| **Authors** | Google DeepMind |
| **Published** | Version 3.1, 2026-04-17; 20 pages. It supersedes v3.0 (2025-09-22), which RPT-0014 pins as S-0805 |
| **Identifier** | https://deepmind.google/blog/strengthening-our-frontier-safety-framework/ (links this PDF) |
| **Source** | https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/strengthening-our-frontier-safety-framework/frontier-safety-framework_3-1.pdf |
| **Digest** | `ad10d2d240e0d557ecad406dbccedcbb4a70295f8ba8eec46bfe01803cb9c301` |

## Overview

Google DeepMind's framework for severe risks from frontier models, revised from v3.0. Its own changelog (§5.3) lists the changes:
- **Tracked Capability Levels (TCLs).** A new tier below the Critical Capability Levels, for "significant" rather than "severe" harm, with proportionate mitigations and risk-acceptance steps. There are two:
  - the **CBRN uplift TCL**: "material risk of CBRN attacks that could result in significant but not severe harm";
  - the **Stealth and Situational Awareness TCL**: enough situational awareness and stealth ("ability to circumvent basic oversight mechanisms") that "we cannot rule out the model significantly undermining human control".
- **Misalignment merged into ML R&D.** v3.0's exploratory misalignment domain is now a combined "ML R&D and Misalignment" domain. It has a TCL and the ML R&D CCLs, which carry security levels 3 and 4.
- **"Security Level 2+"** for the CBRN, cyber and harmful-manipulation CCLs, which were at level 2 in v3.0. It "uses RAND Security Level 2 (SL2) as a baseline, with additional security measures designed to address risks from insider threats and well-resourced non-state external actors". The named examples:
  - dedicated insider-risk teams;
  - background checks and ID verification;
  - "review of model training data for signs of tampering";
  - sandboxed processing of untrusted inputs;
  - red-teaming that simulates APT groups;
  - 24/7 threat hunting and incident response.
- **Process and governance.** A five-step risk-management process (identification, inherent risk, mitigation, residual risk, acceptance), a governance section and a glossary. Security mitigations now name SAIF and Google's common security infrastructure.
- **Insider misuse** of the misuse capabilities is judged "effectively addressed by our baseline controls (such as background checks and access restrictions)".

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | Capability-to-security-level mapping, now with an explicit insider and non-state-actor tier (SL2+) and training-data tampering review |
| Cryptography | none | No cryptographic content |
| This project | adjacent | Ties attacker capability to asset value, as v3.0 did, which is input to **DEC-003**'s feasibility rating. SL2+ adds a named intermediate actor class |

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | adjacent | AIT-055, AIT-026, AIT-115 | Weight exfiltration and "unauthorized modification" (AIT-055) remain the security concern. SL2+'s training-data tampering review and insider teams bear on insider sabotage (AIT-026). The stealth and situational-awareness TCL bears on rogue-agent behaviour (AIT-115). It reports no attacks |
| Existing AI threat models | core | TM-101 | **TM-101's source (v3.0) is superseded.** TM-101's RAND-aligned security tiering holds, but misuse CCLs now sit at SL2+, adding insiders and well-resourced non-state actors to what level 2 resists. The TCL tier is new |
| Weakness enumerations | adjacent | AML.T0025 | As for v3.0. `sources.md`'s AML.T0024.002 for S-0805 doesn't fit, and ATLAS 2026.10 removed it |
| Attack → asset mapping | core | A02, A01; C12, C15 | Weights (A02), now including unauthorized modification, and training data (A01, tampering review). Insiders (C12) and infrastructure (C15) are named. The mapping is ours |

## Implementations

None, searched 2026-11-22: a policy. It names Google's SAIF (S-0780) as the security approach.

| Name | Kind | License | URL |
|---|---|---|---|

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, digest, `supersedes` and `cites` |
| `summary.md` | this summary, with the RPT-0014 applicability table |

## Reference expansion

Footnote links, checked against `sources.md` and the library on 2026-11-22. Compared with v3.0, it **adds four**:
- Anthropic's RSP updates page;
- Anthropic's SB 53 compliance framework, added as the stub `anthropic-2025-sb53-compliance-framework`;
- SAIF (S-0780);
- Google's infrastructure security design overview, which is general cloud security, out of scope.

It **drops** the 2023 RSP announcement. The rest are already held:
- RAND (S-0793);
- the DeepMind AGI paper (S-0763, `shah-2025-gdm-agi-safety-security`);
- the stealth and situational-awareness paper (`phuong-2025-stealth-situational-awareness`);
- OpenAI's Preparedness Framework (S-0814);
- the past FSF versions.

The METR and Frontier Model Forum index pages, and the UK's *Emerging processes*, are out of scope as for v3.0.

## Limits

- **Goals, not controls, still.** SL2+ lists example measures ("may include"), and security levels align with RAND's goals, not its benchmarks.
- **TCLs are thresholds, not evaluations.** How a TCL is detected isn't specified beyond early-warning evaluations.
- **Found late.** v3.1 came out on 2026-04-17, but the v3.0 record (retrieved 2026-11-13) didn't find it, because v3.0's PDF is still served at its own URL. The digest-match check for S-0805 can't detect a newer version.
- **Read in part.** Read: the overview, the §5.3 changelog, §1.2, §2.1 with the SL2+ definition, the TCL definitions, and a sentence-level comparison with v3.0. The §4 governance section and the glossary were skimmed.
