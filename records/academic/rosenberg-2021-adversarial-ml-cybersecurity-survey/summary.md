---
schema: "library-summary/v1"
id: rosenberg-2021-adversarial-ml-cybersecurity-survey
record: rosenberg-2021-adversarial-ml-cybersecurity-survey
type: summary
updated: "2026-11-01"
---

# Adversarial Machine Learning Attacks and Defense Methods in the Cyber Security Domain

|  |  |
|---|---|
| **Type** | paper (survey) |
| **Maturity** | _unset_ (peer-reviewed survey; no maturity level applies) |
| **Authors** | Ishai Rosenberg, Asaf Shabtai, Yuval Elovici, Lior Rokach (Ben-Gurion University of the Negev) |
| **Published** | arXiv v1 2020-07-05; v3 2021-03-13 (summarized here); ACM Computing Surveys 54(5), pp. 1-36 (Crossref date 2021-05-25) |
| **Identifier** | arXiv:2007.02407; DOI 10.1145/3453158 (ACM version of record, not read) |
| **Source** | https://arxiv.org/pdf/2007.02407v3 |
| **Digest** | `sha256:c796dadb9e8db71d81aa204f1e5bf859758babd20f0c194e9051e1f12c34a63d` (arXiv v3, 57 pages; matches pdf-manifest.tsv) |

## Overview

The survey argues that security is the domain where adversarial machine learning matters
most, because malware authors and phishers are real adversaries, yet it is where end-to-end
attacks are hardest: a perturbed sample must keep working, features such as API calls are
discrete, and executables are variable-length and described by several feature types at once
(§1, §2). It proposes a taxonomy of seven attack characteristics in four phases: the threat
model (attacker knowledge, training-set access), the attack type (goal, targeted phase,
targeting), the perturbed features, and the output, either a feature vector or a working
sample (§4, Figure 2). It then reviews published attacks on malware, phishing-URL, DGA,
intrusion, spam, industrial-control and biometric classifiers, marking each for realistic
attacker knowledge, end-to-end output, effectiveness and representative data and features
(§5, Tables 1-7). It concludes that feature-vector attacks are easy but real-life attacks on
commercial products remain hard, and it names gaps that other domains had already filled:
backdoor attacks, resource-exhaustion attacks, model extraction and side channels, and
exploits of the ML frameworks themselves (§7, §8).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | A survey of adversarial attacks and defenses for ML-based security products, with a taxonomy and a per-attack feasibility check (§4, §5) |
| Cryptography | `none` | No cryptographic content |
| This project | `adjacent` | Its attacker-knowledge and training-set-access levels, and its split between attacks that produce a working sample and those that only change a feature vector, are candidate fields for an attack step's preconditions and feasibility (§4.2, §4.3, §4.7) |

`bears_on: DEC-001a` (the core type system, accepted in ADR-0010).

## Implementations

Searched on 2026-11-01. The survey releases no code.

| Name | Kind | License | URL |
|---|---|---|---|
| endgameinc/gym-malware | reinforcement-learning environment for evading static PE classifiers (Anderson et al. 2018, §5.1.1) | MIT | https://github.com/endgameinc/gym-malware |
| pralab/secml_malware | library of attacks on Windows malware detectors, including the byte-padding and FGSM attacks reviewed in §5.1.2 | MIT | https://github.com/pralab/secml_malware |
| elastic/ember | EMBER PE malware dataset and baseline model (Table 8); repository archived | not detected (GitHub NOASSERTION) | https://github.com/elastic/ember |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this document |

## Limits

- **Coverage ends in 2020.** It predates LLM-based security tools, so attacks such as prompt
  injection against AI-driven security tooling (AIT-130) are outside it.
- **The feasibility marks are the authors' judgement.** Each attack gets five yes or no marks
  (Tables 1-7). Effective means a success rate over 90% as each paper reports it, and whether a
  dataset or feature set is representative is the authors' call, not a measurement.
- **Most intrusion-detection and industrial-control attacks reviewed are not realizable.**
  Fewer than 10% of them produce a working network stream or sensor trace (§7.5).
- **The gaps are stated as of 2020.** That no backdoor or model-extraction attack had been
  applied to security classifiers (§7.1, §7.3) describes the literature reviewed, not the
  present.
- **Defenses get a short section** (§6) with no comparative evaluation.
- **The in-the-wild evidence is one report.** The claim that such attacks had already been
  used against a commercial static-analysis classifier rests on Skylight Cyber's 2019 Cylance
  bypass (§1, §7.6).
- **Preprint, not the version of record.** arXiv v3 (57 pages) was read in full apart from the
  model background in Appendix A, which was skimmed. The 36-page ACM version was not compared.

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | core | AIT-007, AIT-003, AIT-011, AIT-012, AIT-015, AIT-010, AIT-006, AIT-008 | A review of attacks on security classifiers, each marked for attacker knowledge, end-to-end output, effectiveness and representativeness (Tables 1-7). AIT-007 cites it: evasion of malware, phishing-URL, DGA and intrusion detectors is most of §5. The other links are ours: transfer through substitute models, which most of the black-box attacks reviewed rely on (AIT-003, §3); dictionary poisoning of a spam filter (AIT-011, §5.4); targeted poisoning of an Android malware classifier (AIT-012, §5.1.1); trojaned face recognition (AIT-015, §5.6.1); printed eyeglasses against face recognition (AIT-010, §5.6.1); adversarial audio against speaker recognition (AIT-006, §5.6.2); and word substitutions against spam filters (AIT-008, §5.4). Sponge examples, model extraction and framework exploits appear only as gaps (§7.2 to §7.4) and are not linked |
| Existing AI threat models | adjacent | none | Its taxonomy (Figure 2) is an attacker model for ML in security: knowledge (black, gray, white or transparent box, with query-limited variants), training-set access (none, read, add, modify), goal, phase, targeting, perturbed features and output. threat-models.md does not list it |
| Weakness enumerations | none | AML.T0015, AML.T0020, ML01:2023, ML02:2023, NISTAML.022 | Not an enumeration, and neither NIST AI 100-2e2025 nor ATLAS 2026.09 cites it (searched 2026-11-01). The ids are RPT-0014's mapping in sources.md |
| Attack → asset mapping | adjacent | C05, C17, C03, C16 | Organized by the security product attacked, not by asset. Our mapping: classifiers queried in deployment (C05) inside tools that act on their verdict, such as antivirus, intrusion detection and spam filters (C17); the training sets that poisoning reaches (C03); and the cameras, microphones and plant sensors that the biometric and industrial-control attacks pass through (C16) |
