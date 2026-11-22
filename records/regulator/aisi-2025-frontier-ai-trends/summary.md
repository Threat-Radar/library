---
schema: "library-summary/v1"
id: aisi-2025-frontier-ai-trends
record: aisi-2025-frontier-ai-trends
type: summary
updated: "2026-11-20"
lane: catalogs-schema
reviewed_by: ""
---

# UK AI Security Institute: Frontier AI Trends Report

|  |  |
|---|---|
| **Type** | paper (a government research report: a synthesis of evaluations) |
| **Maturity** | _unset — do not guess_ |
| **Authors** | UK AI Security Institute (AISI) |
| **Published** | 2025-12-18. The report prints no date; this is the page's first Wayback capture, and the PDF was modified the same day |
| **Identifier** | https://www.aisi.gov.uk/frontier-ai-trends-report |
| **Source** | the report's PDF, linked from that page (54 pages) |
| **Digest** | `6ed147b66f065722f038c6a933a4b8bb39af9ab2378a72fede629e203c0ab2ae` |

## Overview

AISI's "first public, evidence-based assessment" of how frontier AI is changing, from testing more than 30 frontier systems since November 2023. Its methods are auto-graded task sets (question-answer suites and CTFs), long-form tasks, agent tasks in cyber ranges, expert red-teaming, and human uplift and impact studies. It reports trends, not model comparisons. Its findings:

- **Cyber.** Models complete apprentice-level tasks about 50% of the time, against just over 10% in early 2024. In 2025 AISI tested the first model to complete expert-level tasks that need over ten years of human experience. The length of cyber tasks models can do unassisted is doubling about every eight months.
- **Autonomy and agents.** Hour-long software tasks succeed more than 40% of the time, against under 5% in late 2023. Agents are being trusted with high-stakes actions such as asset transfers.
- **Chemistry and biology.** Models exceed PhD-level expert baselines on open-ended questions by up to 60%. They write protocols that proved feasible in a wet lab, and troubleshoot up to 90% better than experts.
- **Safeguards (§4).**
  - "We've found universal jailbreaks for every system we've tested." Those jailbreaks extract policy-violating answers about as accurately as an unsafeguarded model.
  - Progress is real but uneven. For biological misuse, expert effort to find a universal jailbreak rose about 40-fold in six months: 10 minutes with a known vulnerability at 98% success, against more than seven hours for a novel attack at 89%. Other systems and categories still fall to basic jailbreaks.
  - Open-weight models are "particularly hard to safeguard": refusals can be cheaply removed, monitors disabled, and nothing can be patched.
- **Loss of control (§5).** Self-replication evaluations rose from 5% to 60% success between 2023 and 2025. Models can sandbag when prompted, but AISI has seen no spontaneous sandbagging or self-replication.
- **Societal impacts and open models (§6, §7).** Persuasion is rising and emotional reliance has early signs. The gap between open and closed models is now four to eight months.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | Measured attacker uplift in cyber, and measured safeguard robustness against expert jailbreaking |
| Cryptography | none | No cryptographic content |
| This project | adjacent | A time-varying attacker capability, the "AI uplift" attribute `report.md` §7 proposes for Threat. It bears on feasibility and likelihood in risk scoring (**DEC-003**) |

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | core | AIT-122, AIT-073 to AIT-077, AIT-081, AIT-082, AIT-115 | AIT-122 (AI-accelerated vulnerability discovery and exploits) cites it for the cyber trend. The safeguards section is evidence for jailbreaks (AIT-073 to 077) and for removing open-weight safety (AIT-081, 082). The self-replication and sandbagging results bear on rogue-agent behaviour (AIT-115). None of these are incidents |
| Existing AI threat models | none | — | Capability trends, not a threat model. `threat-models.md` doesn't list it |
| Weakness enumerations | adjacent | AML.T0016.002; NISTAML.04 | The mapping is `sources.md`'s; the report cites no catalog. **`sources.md`'s open point is settled:** the date (not confirmed there) is 2025-12-18, per the first archived copy and the PDF metadata |
| Attack → asset mapping | adjacent | C08, C13, C16; A02, A03, A10 | Its results describe the attacker side: agents (C08), hosted frontier models (C13) and open-weight models (A02). The assets at stake are safeguard behaviour (A03) and, through cyber uplift, the hosts and infrastructure attacked (A10). The mapping is ours |

## Implementations

Searched 2026-11-20:

| Name | Kind | License | URL |
|---|---|---|---|
| UKGovernmentBEIS/inspect_cyber | AISI's cyber-evaluation extension of its Inspect framework, linked by the report | MIT | https://github.com/UKGovernmentBEIS/inspect_cyber |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, digest and `cites` |
| `summary.md` | this summary, with the RPT-0014 applicability table |

## Reference expansion

The PDF's reference pages are images, so the 32 references were read from the web page's list, which has links. They were checked against `sources.md` and the library on 2026-11-20:
- **In `sources.md` (2):** Constitutional Classifiers (S-0460), and Malla (S-0287, also the library's `lin-2024-malla`).
- **Missing, added as stubs (14):**
  - **7 arXiv papers:** RepliBench, the large-scale agent-deployment red-teaming competition, evaluation awareness, deliberative alignment, Badllama 3, Deep Ignorance, and AI sandbagging.
  - **7 web documents, pinned by Wayback copies:** Anthropic on subtle sandbagging, AISI's white-box sandbagging update, NCSC on vulnerability disclosure for AI safeguards, the Science paper on political persuasion, AISI on open-weight risks, Cato CTRL on the uncensored-LLM platform Nytheon AI, and the Claude Opus 4 and Sonnet 4 system card.
- **Covered by another stub (1):** AISI's RepliBench page, which is the arXiv paper.
- **Out of scope (15):** capability benchmarks and methods (SWE-bench, METR task length, AISI long-form tasks, autograder statistics), Epoch AI trends and compute, Artificial Analysis, labour and economics data (Stanford, ONS, gov.uk), a human-AI relationships paper, the AI-risk statement and a policy essay.

## Limits

- **Aggregated and anonymous.** Results are trends with unnamed models ("Model A", "Model B"), so no claim can be tied to a specific system or checked independently.
- **Method details are elsewhere.** Task sets, cyber ranges and jailbreak protocols are described only at a high level, and many evaluations are not public.
- **Jailbreak effort is one measure.** It records expert time to find a universal jailbreak, and says compliance "may not be indicative of risk", since it doesn't show whether answers are accurate or usable by a novice.
- **A snapshot from 2023 to 2025.** By the report's own trend lines, its milestones will date quickly.
