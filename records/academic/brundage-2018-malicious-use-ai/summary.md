---
schema: "library-summary/v1"
id: brundage-2018-malicious-use-ai
record: brundage-2018-malicious-use-ai
type: summary
updated: "2026-11-21"
lane: catalogs-schema
reviewed_by: ""
---

# The Malicious Use of Artificial Intelligence: Forecasting, Prevention, and Mitigation

|  |  |
|---|---|
| **Type** | paper (a multi-institution report, from a February 2017 workshop) |
| **Maturity** | _unset — do not guess_ (arXiv preprint) |
| **Authors** | Miles Brundage, Shahar Avin, Jack Clark, Helen Toner, Peter Eckersley and 21 others (FHI, CSER, OpenAI, CNAS, EFF and others) |
| **Published** | arXiv v1 2018-02-20; v2 2024-12-01 (read here) |
| **Identifier** | arXiv:1802.07228 |
| **Source** | https://arxiv.org/pdf/1802.07228 |
| **Digest** | `f8876c43ae1ac11ea32b91fb1c4cf1b297f6b3fc20422b32cb228a8abfaf1b08` (101 pages; matches `pdf-manifest.tsv`) |

## Overview

A survey of "potential security threats from malicious uses of artificial intelligence", focused on attacks likely soon if defenses lag. It doesn't try to settle the long-run balance between attackers and defenders.

**Its general framework** sees AI changing threats in three ways:
- **expansion of existing threats:** lower cost, so more actors, a faster pace and more targets;
- **new threats:** tasks impractical for humans, and attacks on defenders' own AI systems;
- **a changed character:** "especially effective, finely targeted, difficult to attribute".

**Three security domains**, each with illustrative scenarios:
- **Digital:**
  - automated social engineering and spear-phishing;
  - automated vulnerability discovery and sophisticated automated hacking;
  - human-like denial of service, and automation of criminal service tasks;
  - prioritising targets with ML;
  - exploiting AI used in applications (adversarial examples, data poisoning);
  - black-box model extraction.
- **Physical:** terrorist repurposing of commercial AI, low-skill actors gaining high-skill attack capability, larger-scale attacks, swarms, and attacks further removed in time and space, including subverting autonomous vehicles.
- **Political:** state surveillance to suppress dissent, fabricated video and audio, automated influence campaigns, denial-of-information attacks, and manipulation of what information is available.

**Four recommendations:** policymakers and researchers work together; researchers take dual use seriously; borrow best practice from fields like computer security; and widen the set of stakeholders. Four research areas: learning from cybersecurity (red teaming, formal verification, responsible disclosure of AI vulnerabilities, secure hardware), openness models such as pre-publication risk assessment and access licensing, a culture of responsibility, and technical and policy solutions.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | The baseline taxonomy of AI-enabled offense, together with attacks on AI systems, by domain |
| Cryptography | adjacent | It mentions secure multiparty computation, homomorphic encryption and differential privacy as protective technologies |
| This project | adjacent | Threat classes and the "expansion, new, changed character" lens for AI-enabled actors (**DEC-001**: Threat). It has no system or asset model |

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | adjacent | AIT-126, AIT-122, AIT-121, AIT-127, AIT-129, AIT-052, AIT-001 to AIT-004, AIT-011 | Its forecasts are now catalog entries: AI-automated spear-phishing (AIT-126), vulnerability discovery and exploits (AIT-122), autonomous intrusion (AIT-121), voice and video impersonation (AIT-127), influence operations (AIT-129), model extraction (AIT-052), and adversarial examples and poisoning (AIT-001 to 004, AIT-011). In 2018 these were scenarios, not incidents |
| Existing AI threat models | core | TM-107 | TM-107's source. TM-107's "security domain" decomposition matches. TM-107 could note the three-way change lens (expansion, new threats, changed character), which is the analytic core |
| Weakness enumerations | none | NISTAML.04 | The mapping is `sources.md`'s; the report cites no catalog, and none existed for AI in 2018 |
| Attack → asset mapping | adjacent | C12, C16, C05, C17; A15, A12, A13, A02 | Targets are people (C12: phishing and persuasion), physical and edge systems (C16: drones and vehicles), deployed models (C05: evasion and extraction) and downstream decisions (C17). The assets are human trust (A15), physical safety (A12), reputation and information integrity (A13) and models (A02). The mapping is ours |

## Implementations

None, searched 2026-11-21: a policy and research-agenda report. It cites tools such as CleverHans, now stubbed as `papernot-2016-cleverhans`.

| Name | Kind | License | URL |
|---|---|---|---|

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, digest and `cites` |
| `summary.md` | this summary, with the RPT-0014 applicability table |

## Reference expansion

About 193 references, checked against `sources.md` and the library on 2026-11-21. 81 mention AI, and 24 of those are in scope: attacks on ML, AI-enabled offense, and AI security and safety foundations.
- **In `sources.md` (10):** S-0001, S-0003 (also the library's `szegedy-2013-intriguing-properties`), S-0007, S-0008, S-0019, S-0026, S-0027, S-0038, S-0673 and S-0853.
- **Missing, added as stubs (13):**
  - **Barreno et al., *The security of machine learning*** (2010), from the authors' PDF;
  - **7 arXiv papers:** *Concrete Problems in AI Safety*, RL-based evasion of PE-malware models, NLG-targeted phishing, the Google Cloud Vision noise attack, adversarial malware perturbations, CleverHans, and exploitable bugs in ML software;
  - **5 web documents:** Microsoft's neural fuzzing, Gizmodo on hackers weaponizing AI, MIT Technology Review on the adversarial-example competition, ANTIDOTE (poisoning anomaly detectors; PDF), and SNAP_R automated spear-phishing (Black Hat 2016 white paper).
- **Not stubbed (1):** Everett et al. on what makes automated text convincing (ACM SAC 2016), which has no open copy.
- **Out of scope (the rest):**
  - AI capability and RL papers (AlphaGo, Dota, DQN, GANs, Face2Face);
  - privacy-preserving computation and verification methods;
  - surveys and opinion pieces;
  - drones and autonomous-weapons law and policy;
  - non-AI security and political references.

## Limits

- **2017 forecasts.** It predates transformers at scale, LLM agents and deepfake fraud. Its digital scenarios came true in forms it didn't foresee in detail, such as agentic intrusion and LLM-written phishing.
- **Scenarios, not evidence.** Its hypothetical scenarios illustrate classes and have no likelihood estimates.
- **The political domain is broad.** Surveillance and censorship by states are harms of AI use, not attacks a company threat model would usually contain.
- **Defensive agenda only sketched.** Its interventions are research areas, not controls with stated effectiveness.
