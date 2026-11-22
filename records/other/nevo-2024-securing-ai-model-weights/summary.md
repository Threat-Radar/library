---
schema: "library-summary/v1"
id: nevo-2024-securing-ai-model-weights
record: nevo-2024-securing-ai-model-weights
type: summary
updated: "2026-11-22"
lane: catalogs-schema
reviewed_by: ""
---

# Securing AI Model Weights: Preventing Theft and Misuse of Frontier Models

|  |  |
|---|---|
| **Type** | paper (a RAND research report) |
| **Maturity** | _unset — do not guess_ |
| **Authors** | Sella Nevo, Dan Lahav, Ajay Karpur, Yogev Bar-On, Henry Alexander Bradley, Jeff Alstott (RAND) |
| **Published** | 2024-05-30. It supersedes the interim report WR-A2849-1 (2023-10-31) |
| **Identifier** | RAND RR-A2849-1 |
| **Source** | https://www.rand.org/content/dam/rand/pubs/research_reports/RRA2800/RRA2849-1/RAND_RRA2849-1.pdf |
| **Digest** | `e728155ee84b2000d7a38f1b26e16bcfaee231412953f679ebcd64d597eaa2b6` (128 pages; matches `pdf-manifest.tsv`) |

## Overview

A threat model and graded security plan for one asset: **the weights of frontier models**. RAND frames them as "the crown jewels of an AI developer's work". Its method draws on literature, real-world examples and interviews with experts. There are four contributions:

1. **38 attack vectors in 9 categories** (Table 5.1):
   - running unauthorized code;
   - compromising credentials;
   - undermining the access-control system;
   - bypassing it altogether;
   - **AI-specific vectors**: vulnerabilities in the ML stack, intentional ML supply-chain compromise, prompt-triggered code execution, model extraction and model distillation;
   - nontrivial access to data or networks (air gaps, side channels and TEMPEST, wiretaps);
   - unauthorized physical access, up to armed break-in and military takeover;
   - supply-chain attacks;
   - human intelligence (bribes, extortion, candidate placement).

   Appendix A gives "hundreds of real-world examples" of these vectors in use.
2. **Five operational-capacity tiers** for attackers (Figure 4.1), each including the ones below it:
   - **OC1**, amateur attempts: up to $1,000 and days;
   - **OC2**, professional opportunistic efforts: up to $10,000 and weeks;
   - **OC3**, cybercrime syndicates *and insider threats*: about ten professionals, up to $1 million and months;
   - **OC4**, standard operations by leading cyber-capable states: about 100 people, up to $10 million and a year;
   - **OC5**, top-priority state operations: about 1,000 people, up to $1 billion and years.
3. **Feasibility of each vector for each tier** (Table 5.2), as averaged expert scores where 1 means likely infeasible. About a dozen vectors are likely infeasible for non-state actors but feasible for states. For the AI-specific vectors, ML-stack vulnerabilities score 1, 2, 4, 4, 5 across OC1 to OC5, and ML supply-chain compromise 1, 2, 4, 5, 5. Prompt-triggered code execution scores 2, 3, 4, 4, 4, while model extraction (1, 1, 1, 2, 3) and distillation (1, 1, 2, 2, 3) score lowest.
4. **Five security levels**, each with a benchmark system (Chapter 6, Appendices B and C). **SL1** to **SL5** are each meant to thwart the matching tier OC1 to OC5. RAND says they are "not meant to be used as a standard".

**Urgent recommendations:** a threat-model-based security plan, centralising all copies of the weights, fewer people with access, hardened model interfaces against exfiltration, insider-threat programs, defense in depth, advanced red-teaming and confidential computing. It judges that protecting internet-facing models against the most capable actors "is currently not feasible" and may take about five years. It suggests bandwidth limits, HSM-like inference hardware, and isolated networks for training.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | A full attack-vector and attacker-capability model for an AI asset |
| Cryptography | adjacent | Encryption, HSM-like hardware and confidential computing appear as controls. The access-control system's cryptography is itself one attack category |
| This project | core | Asset → vector → attacker tier → feasibility → control level is close to tmodel's Asset, AttackStep, Threat-actor capability, RiskScore and Mitigation path (**DEC-001**). A per-tier feasibility score is the shape DEC-003's feasibility rating needs |

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | core | AIT-055, AIT-026 (and AIT-037, AIT-039, AIT-052, AIT-053, AIT-054, AIT-057) | AIT-055 (weight exfiltration by intrusion or insider) and AIT-026 (insider sabotage) cite it. Its AI-specific vectors fit ML-stack and supply-chain compromise (AIT-037), exposed MLOps platforms (AIT-039), model extraction and API parameter extraction (AIT-052, AIT-053) and distillation (AIT-054). Its side-channel category covers AIT-057 (hardware side-channel extraction). Real-world examples are in Appendix A |
| Existing AI threat models | core | TM-099 | TM-099's source. Its capture holds: OC1 to OC5, about 38 vectors in 9 categories, and SL1 to SL5 with benchmarks. TM-099 could add the per-vector feasibility scores (Table 5.2), which `sources.md` mentions but doesn't list. RAND scopes out vectors unlikely to be part of a weight-theft chain, such as data poisoning and prompt injection without code execution |
| Weakness enumerations | adjacent | AML.T0048.004, AML.T0025, AML.T0035; ML05; NISTAML.031 | The mapping is `sources.md`'s. RAND cites ATLAS and ATT&CK as sources but maps no ids. The vectors are attack classes, not weaknesses |
| Attack → asset mapping | core | A02; C03, C04, C05, C11, C12, C15 | The asset is the weights (A02), with training (C03), registry and supply chain (C04), serving (C05), credentials (C11), insiders (C12) and MLOps infrastructure (C15) as the paths to it. The mapping is ours |

## Implementations

None, searched 2026-11-20. RAND gives benchmark security systems in prose (Appendix B), not tools.

| Name | Kind | License | URL |
|---|---|---|---|

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, digest and `cites` |
| `summary.md` | this summary, with the RPT-0014 applicability table |

## Reference expansion

About 280 references, checked against `sources.md` and the library on 2026-11-21. Most document general cyber operations and incidents (Stuxnet, intelligence leaks, supply-chain and physical attacks) and are out of RPT-0014's AI scope. The AI-related ones:
- **In `sources.md` or the library (12):**
  - in `sources.md`: S-0232, S-0163, S-0013, S-1129, S-0977 (the 38 TB exposure), S-0220 (via a Wired report), S-0990 (ShadowRay) and S-0841;
  - in the library: `mitre-atlas`, and `pytorch-2022-torchtriton-dependency-confusion` (two references);
  - ShellTorch, covered by the earlier stub `thn-2023-shelltorch-pytorch-torchserve`.
- **Missing, added as stubs (10):**
  - this report's own interim version (`nevo-2023-…-interim`, linked by `supersedes`);
  - the 2023 versions of Anthropic's RSP and OpenAI's Preparedness Framework, earlier than S-0798 and S-0814;
  - Orca, the model-distillation vector's example;
  - deep-learning acoustic keyboard side channels;
  - NVIDIA on prompt injection and on H100 confidential computing;
  - the Mistral model leak;
  - Wired on AI-written phishing;
  - TensorFlow's security policy ("models are programs").
- **Missing, not stubbed (1):** Naghibijouybari et al., *Side Channel Attacks on GPUs* (IEEE TDSC 2021), which has no open copy.
- **Not stubbed as a work:** Microsoft's Counterfit, an AI security testing tool.
- **Out of scope (about 255):** non-AI security references, policy statements and market reports.

## Limits

- **Expert judgement.** The feasibility scores are rounded averages of expert opinion, and RAND notes that "expert opinions vary significantly on the capabilities of state actors". They are not measurements.
- **One asset.** It covers theft of weights only. Misuse through APIs, poisoning and prompt injection without code execution are scoped out by design.
- **Benchmarks, not a standard.** The security levels describe example systems, and RAND says they shouldn't be used as a standard. Frameworks that adopt them (FSF v3.1, which adds an "SL2+" tier; RSP v3.4) give them that weight anyway.
- **2024 state of practice.** It predates agent deployments at scale and the incidents of 2025 and 2026 in RPT-0014's log.
