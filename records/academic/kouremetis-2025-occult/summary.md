---
schema: "library-summary/v1"
id: kouremetis-2025-occult
record: kouremetis-2025-occult
type: summary
updated: "2026-11-13"
lane: catalogs-schema
reviewed_by: ""
---

# OCCULT: Evaluating Large Language Models for Offensive Cyber Operation Capabilities

|  |  |
|---|---|
| **Type** | paper (evaluation framework with three prototype benchmarks; not peer reviewed) |
| **Maturity** | _unset — do not guess_ |
| **Authors** | M. Kouremetis, M. Dotter, A. Byrne, D. Martin, E. Michalak, G. Russo, M. Threet, G. Zarrella (The MITRE Corporation) |
| **Published** | arXiv v1, 2025-02-18 (title page dated 2025-02-25); 44 pages including references and appendix |
| **Identifier** | arXiv:2502.15797 |
| **Source** | https://arxiv.org/pdf/2502.15797 |
| **Digest** | `6b6a747c91b4672c4091a3c918c11377395ae35a4a1c5c1f4c45d4f73376c215` |

## Overview

MITRE argues that most tests of whether an LLM can help attackers measure the wrong thing: capture-the-flag puzzles, general security quizzes and pass/fail scores that say little about real offensive cyber operations (OCO). OCCULT is a method for designing such tests, not a single benchmark. Every test is placed on three axes: the **OCO capability** it measures (labelled by ATT&CK technique where possible), the **use case** (knowledge assistant, co-orchestration with a tool such as Caldera, or autonomous agent), and the **reasoning** it can show evidence of (planning, perception of the environment, creating and adapting actions, and generalizing). Tests are meant to show graded progress, not pass or fail, and to resist memorization.

Three prototypes show the method:
- **TACTL**, about 180 scenario-driven multiple-choice questions with randomized variables. Its 30-question Ground2Crown scenario spans 14 ATT&CK tactics and 44 techniques.
- **BloodHound Equivalency**: can an LLM find Active Directory attack paths as the BloodHound tool does?
- **CyberLayer**, a high-fidelity network simulation in which the LLM acts as the attacker and is scored on reaching its goal, steps taken and artifacts left behind.

The preliminary results are small and the authors say so. DeepSeek-R1 scored 91.8% on all 183 TACTL questions and 100% on Ground2Crown. Two Mixtral models averaged 52.5% on 12 BloodHound queries. In CyberLayer's lateral-movement scenario, Llama 3.1 70B reached the goal in the fewest steps with the fewest artifacts.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | Measures how much an LLM lifts an attacker against conventional networks, mapped to ATT&CK. |
| Cryptography | none | No cryptographic content. |
| This project | adjacent | Evidence for how feasible AI-enabled intrusion is, which bears on the feasibility inputs of **DEC-003** (ADR-0006 rates feasibility by attack potential, and AI uplift lowers the expertise and time an attack needs). It is about AI as the attacker's tool, not threats to an AI system, so it adds no object or edge to tmodel's model. |

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | adjacent | AIT-121 | One of AIT-121's seven sources. It measures capability in question sets and a simulator, and reports no attack on a real system, so it supports feasibility, not occurrence. |
| Existing AI threat models | adjacent | — | Its three use cases form a small threat model of AI as an attacker's tool, but not of an AI system, and `threat-models.md` has no entry for it. |
| Weakness enumerations | adjacent | AML.T0116, AML.T0117 | ATLAS 2026.09's Autonomous Reconnaissance and Autonomous Attack-Path Adaptation, which AIT-121 carries, describe what CyberLayer and BloodHound Equivalency test. OCCULT predates both ids and labels its tests by ATT&CK technique instead. |
| Attack → asset mapping | adjacent | A09, A10 | The targets are conventional: hosts, Active Directory and credentials. No AI component of the reference architecture (C01–C21) is attacked. |

## Implementations

Searched 2026-11-13 (GitHub, including MITRE's organizations): **none found** for OCCULT, TACTL, BloodHound Equivalency or CyberLayer. §7.2 says MITRE plans to release TACTL, BloodHound Equivalency and the evaluation platform. The tools the benchmarks are built on are public:

| Name | Kind | License | URL |
|---|---|---|---|
| Inspect AI (UK AISI) | LLM evaluation framework TACTL runs on | MIT | https://github.com/UKGovernmentBEIS/inspect_ai |
| BloodHound CE (SpecterOps) | Active Directory attack-path tool, the baseline for BloodHound Equivalency | Apache-2.0 | https://github.com/SpecterOps/BloodHound |
| Caldera | adversary emulation platform, the co-orchestration example | Apache-2.0 | https://github.com/apache/caldera (formerly `mitre/caldera`) |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, digest, applicability, and `cites` for every in-scope reference |
| `summary.md` | this summary, with the RPT-0014 applicability table |

## Reference expansion

All 56 references were checked against RPT-0014's `sources.md` on 2026-11-13, by arXiv id and title, then by author and keyword. Refs. 8 and 30 are the same Cybench paper. 27 cited works are in scope (LLM offensive-security evaluation, autonomous exploitation, and their defences):

- **In `sources.md` (9):** refs. 1 (S-0923), 3 (S-0954), 4 (S-0929), 8/30 (S-0944), 17 (S-0914), 21 (S-0919), 24 (S-0254), 25 (S-0253), 29 (S-0604). Of these, only CyberSecEval 3 and Cybench are library records yet.
- **Covered by other documents (1):** ref. 27, DARPA's AIxCC "about" page. The challenge itself is S-0725 and S-1139.
- **Missing, added as `status: stub` with `cited_by` this record (16):** refs. 5, 6, 7, 9, 11, 12, 13, 14, 15, 18, 19, 20, 22, 23, 26 and 50. Twelve are arXiv papers pinned by digest. Project Naptime (22) and Vulnhuntr (26) are web pages; the Vulnhuntr URL the paper gives returns 404, so its stub pins the Wayback copy of 2024-11-05. SecEval (19) is a repository pinned by commit. Mirage (50) is a paywalled journal article, recorded by DOI.
- **Missing, not stubbed (1):** ref. 10, Yang et al., NeurIPS 2023 MASec workshop. No locator could be confirmed (it is not on arXiv under that title, and OpenReview search did not find it). It is in `cites` by title.

**Out of scope (28):**
- general LLM and AI work: refs. 2, 16, 28, 34–39 and 47–49;
- non-AI security references: 31 (ATT&CK design; the library already holds `mitre-attack`), 32, 40 and 41;
- tools and services: 33, 42–46 and 51–54;
- MITRE's press release: 55;
- a test-data library: 56.

## Limits

- **Preliminary, small and not reproducible yet.** The results cover a handful of models, with BloodHound Equivalency run only on two Mixtral models, and no test data or code has been released. The authors call the samples too small for firm conclusions.
- **TACTL is multiple choice.** The authors call that a compromise: it measures knowledge, not the ability to carry out an operation.
- **Reasoning is scored qualitatively**, as weak or strong evidence per component.
- **Simulated, not real.** CyberLayer abstracts networks, so success there is a lower bar than a live intrusion.
- **No defensive mapping** beyond ATT&CK labels.
- **Checked against `sources.md`.** S-0807's note says its benchmark names and the DeepSeek-R1 finding were "from memory". The paper confirms both: TACTL, BloodHound Equivalency and CyberLayer, and DeepSeek-R1 above 90% on TACTL.
- **Read in part.** Read in full: §§1–3, the designs of the three tests (§4.1, §4.2 and the start of §4.3), §§6–7 and the references. §4.3.3–4.3.4 (CyberLayer internals), §5 (the platform) and the appendix were skimmed.
