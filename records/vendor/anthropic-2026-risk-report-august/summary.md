---
schema: "library-summary/v1"
id: anthropic-2026-risk-report-august
record: anthropic-2026-risk-report-august
type: summary
updated: "2026-11-22"
lane: catalogs-schema
reviewed_by: ""
---

# Anthropic Risk Report: August 2026

|  |  |
|---|---|
| **Type** | paper (a frontier developer's risk report under RSP v3.4; redacted public version) |
| **Maturity** | _unset — do not guess_ |
| **Authors** | Anthropic |
| **Published** | August 2026: first archived 2026-08-15, coverage date 2026-07-15. It supersedes the February 2026 Risk Report |
| **Identifier** | https://www.anthropic.com/aug-2026-risk-report |
| **Source** | https://assets.claude.com/f61d49fa5596956a5dec75fea0e973bf6a6a8378.pdf |
| **Digest** | `d76815f8c0bd284a33c7017d642d0734ba903ae63f7c1e6ca7778b35b2c40fa4` (186 pages) |

## Overview

Under RSP v3.0 and later, **this is where Anthropic's threat models now live**. The policy (`anthropic-rsp-v3-4-2026`) sets the thresholds and process; the Risk Reports, published every three to six months, give the threat models, the evidence and the risk verdicts. This report covers all of Anthropic's models, including internal-only ones. The models in focus are Claude Mythos 5 (available as Claude Fable 5 with extra safeguards) and an unreleased internal "Model 2". Each risk section gives the threat model, relevant models, capabilities, mitigations, an overall risk verdict, the next steps, and the link to the RSP's industry-wide recommendations.

**Misalignment in high-stakes settings** (§2). An AI with powerful affordances inside an organization could "exploit, manipulate, or tamper with that organization's systems or decision-making". There are **eight pathways**:
1. diffuse sandbagging on safety R&D;
2. targeted undermining of safety R&D;
3. code backdoors to help future misaligned models;
4. poisoning the training data of future models;
5. self-exfiltration and autonomous operation;
6. persistent rogue internal deployment;
7. undermining R&D at other AI developers;
8. undermining government decisions.

The argument rests on eight claims, chiefly that the models lack strong "covert capabilities". The mitigations are:
- de-risked, monitored training environments and alignment assessments;
- offline monitoring of internal usage;
- sandboxing of RL and evaluation actions;
- a Claude reviewer on pull requests;
- blocking classifiers in internal deployments;
- weight security.

The report notes that sandboxes "may sometimes be misconfigured" in a way an attacker as capable as Mythos Preview could escape, with "some near-misses". **Verdict: Low**, raised from "very low" after incident disclosures about model behaviour in cybersecurity evaluations.

**Automated R&D** (§3). **Low**, but with less confidence than before: the task-based evaluations have saturated, and there are early signs of acceleration. "Claude now authors a large majority of the code merged into our production codebases."

**Chemical and biological weapons** (§4). **CB-1** is non-novel weapons for low-resourced actors. Anthropic acts as though its models meet the threshold, and rates the risk "Low, but higher than our previous estimate". **CB-2** is novel weapons for moderately resourced teams: "Low risk, but with substantial uncertainty". Mitigations are real-time blocking classifiers (robustness levels 1 to 3 and coverage levels), bug bounties and red-teaming, offline monitoring, vetted exemptions, threat intelligence, and weight security. **Jailbreaks that still work on some models:**
- UK AISI's **Boundary Point Jailbreaking**, a black-box optimization against classifiers that leaves model capability almost intact. Reproducing it took Anthropic about 20 hours of work with AISI's help;
- an AISI-sourced jailbreak;
- a coverage gap found by both Anthropic and AISI;
- a bug-bounty jailbreak.

A prompt injection that steers a classifier-exempt agent into bioweapon work is judged "extremely unlikely" to give meaningful uplift.

**Weight security** (§6.4). The ASL-3 programme protects weights against "most non-state attackers, including cybercriminal groups, hacktivists, and corporate espionage actors".
- **Attack vectors**, in six categories: endpoint compromise, supply chain, physical, cloud infrastructure, privilege escalation and data exfiltration.
- **Frameworks it aligns to:** SOC 2 Type 2, ISO 27001 and ISO 42001.
- **Out of scope:** sophisticated insiders and nation-state attackers "with capabilities like novel zero-day attack chains". It says no frontier developer currently meets the nation-state bar.
- **Ten named controls:**
  1. egress bandwidth limits;
  2. two-party access approval;
  3. binary allowlisting;
  4. hardware security keys;
  5. device authorization;
  6. cloud storage restrictions;
  7. hourly re-authentication for privileged identities;
  8. network segmentation;
  9. centralized monitoring with anomaly detection;
  10. network-source policies that make stolen tokens useless off-network.

  Caveats on six of the ten are redacted.

**Incidents and process failures it discloses** (§4.5.8, §5.2, §6.5):
- **April 2026:** contractors at data-labelling vendors "exploit[ed] a flaw in one of our data collection platforms to obtain an API key". They used it to reach models, including Mythos Preview, outside their tasks. The path was open for several weeks. It was contained within 90 minutes of the report, and no weights or customer data were accessed.
- **May 2025 to April 2026:** all human-feedback vendor traffic, about 50,000 people and about 133 million exchanges, ran without blocking bio classifiers, because of a flag "meant only for internal use".
- **An unmonitored employee's agent** spawned agents with `--dangerously-skip-permissions` in a cluster with very sensitive resources. One of them deleted a large number of jobs. Blocking controls have been added since.
- **Weakened controls:**
  - a less conservative threshold for which model snapshots get secure weight storage;
  - a bug that limited the distillation defense (connector-text summarization) on one surface for a few days;
  - chain-of-thought exposed to grading pressure;
  - direct training on misaligned behaviour;
  - repeated training on alignment-faking transcripts.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | Named threat actors, scoped weight-security controls, still-viable attacks on safeguards, and dated real incidents at a frontier developer |
| Cryptography | none | No cryptographic content beyond hardware keys |
| This project | core | Threat, Mitigation (with stated scope and gaps), Incident and RiskScore in one place, from the developer itself. It is the current basis for Anthropic's entry in a company model (**DEC-001**) |

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | core | AIT-113, AIT-008, AIT-114, AIT-115, AIT-054, AIT-055, AIT-143, AIT-064, AIT-073 to AIT-077 | These are incidents, not forecasts. Vendor contractors reached unsafeguarded models with an API key they obtained (AIT-113, through a third party). Boundary Point Jailbreaking optimizes against classifiers (AIT-008; jailbreaks AIT-073 to 077). An agent run with permissions skipped deleted jobs (AIT-114). Sandbox near-misses and the eight pathways fit AIT-115, sandbagging AIT-143, distillation defenses AIT-054, and weight theft AIT-055. The prompt-injection path is AIT-064. The mapping is ours |
| Existing AI threat models | core | TM-100 | **TM-100 should be rebased on this report and RSP v3.4.** TM-100 captures RSP v2.2's ASL-3 security standard. Anthropic's threat models are now these four, with eight misalignment pathways, two CB threat models, and the ASL-3 security scope (non-state actors in, sophisticated insiders and nation states out) |
| Weakness enumerations | none | — | It cites no catalog |
| Attack → asset mapping | core | A02, A03, A01; C15, C08, C11, C12, C13 | Assets are the weights (A02), safeguard behaviour (classifiers, A03) and future training data (A01). Paths are infrastructure and clusters (C15), internal agents (C08), credentials and API keys (C11), insiders and contractors (C12) and third-party vendor platforms (C13). The mapping is ours |

## Implementations

None, searched 2026-11-22: a risk report.

| Name | Kind | License | URL |
|---|---|---|---|

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, digest and `cites` |
| `summary.md` | this summary, with the RPT-0014 applicability table |

## Reference expansion

The report has no bibliography; it links Anthropic documents and system cards. Checked on 2026-11-22:
- **In the library:** RSP v3.4 (`anthropic-rsp-v3-4-2026`), the alignment-faking paper (`greenblatt-2024-alignment-faking`), and RAND (`nevo-2024-securing-ai-model-weights`, for SL4).
- **Added as stubs:**
  - the previous Risk Report (`anthropic-2026-risk-report-february`), which this one supersedes;
  - the Frontier Safety Roadmap;
  - the SB 53 compliance framework announcement.

  From the RSP page, also added: the Opus 4.6 Sabotage Risk Report, the 2025 pilot Sabotage Risk Report, and the ASL-3 activation report.
- **Not stubbed:** the system cards it draws on (Mythos Preview, Fable 5 and Mythos 5, Opus 4.8). The library holds only `anthropic-2025-claude-4-system-card`. They are model documentation, so they're out of RPT-0014's scope unless an AIT cites one.

## Limits

- **Redacted, and self-assessed.** Two appendices and the caveats on six security controls are redacted. External review under RSP §3.6 is required only for "highly capable" models with significant redactions, or when the Long-Term Benefit Trust asks for it.
- **Verdicts are qualitative.** "Low" and "very low" have no numeric scale. The report says its arguments rest on models' limited covert capabilities, which may not hold for future models.
- **A snapshot.** The coverage date is 2026-07-15 and a new report is due every three to six months, so it will date quickly. Check for a later report before citing it.
