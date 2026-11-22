---
schema: "library-summary/v1"
id: shah-2025-gdm-agi-safety-security
record: shah-2025-gdm-agi-safety-security
type: summary
updated: "2026-11-22"
lane: catalogs-schema
reviewed_by: ""
---

# An Approach to Technical AGI Safety and Security

|  |  |
|---|---|
| **Type** | paper (a frontier developer's technical safety and security agenda) |
| **Maturity** | _unset — do not guess_ (arXiv preprint) |
| **Authors** | Rohin Shah, Alex Irpan, Alexander Matt Turner, Anna Wang, Arthur Conmy and 25 others (Google DeepMind) |
| **Published** | arXiv v1, 2025-04-02 (the only version on 2026-11-22) |
| **Identifier** | arXiv:2504.01849 |
| **Source** | https://arxiv.org/pdf/2504.01849 |
| **Digest** | `8f6b9fb28658ae812e379ae4435193af727d7ecf0882a02b820f55ad90f16bf3` (145 pages; matches `pdf-manifest.tsv`) |

## Overview

Google DeepMind's plan for preventing *severe harm* from AGI-level systems. It rests on stated assumptions: the current paradigm continues, there is no human ceiling on capability, timelines are uncertain, progress may accelerate, and change is roughly continuous. So defenses can be tested iteratively against "the next several scales" rather than arbitrary capability.

**Four risk areas**, grouped by who is the adversary (Figure 1). The paper says this is "not a categorization": the areas overlap.
- **Misuse:** "the user is an adversary", who instructs the system to cause harm against the developer's intent.
- **Misalignment:** "the AI is an adversary", knowingly acting against the developer's intent. This covers deception, scheming and active loss of control.
- **Mistakes:** harm the AI doesn't know it causes. Ordinary safety engineering handles it, so it is out of scope.
- **Structural risks:** multi-agent dynamics where no single agent is at fault. These need norms and institutions, so they are out of scope too.

**Against misuse** (§5, Figure 2), the aim is to block bad actors from dangerous capabilities. This is put into practice through the Frontier Safety Framework:
- **Risk assessment:** misuse threat modelling, then dangerous-capability evaluations against capability thresholds.
- **Model-level mitigations:** safety post-training with jailbreak resistance, and capability suppression (unlearning, which "has so far remained elusive").
- **System-level mitigations:** monitoring (classifiers, activation probes, manual audit) and access restrictions (vetted users, and action on users who repeatedly trigger monitors).
- **Weight security (§5.6):** least-privilege identity and access control with multi-factor keys, hardened environments with exfiltration detection, narrow APIs, and encrypted processing. It notes weights can be "exfiltrated in time through API use", citing Carlini et al. on stealing part of a production model. It defers to RAND (Nevo et al. 2024) for detail.
- **Red-teaming the mitigations (§5.8):** manual tests, AI-assisted tests, algorithmic search and targeted attacks.

**Against misalignment** (§6, Figure 3), there are two lines of defense:
1. **Train an aligned model:** amplified oversight such as debate, guiding model behaviour, and robust training through adversarial and online training.
2. **Limit harm if the model is misaligned** ("AI control"). It treats the AI "as an untrusted insider" (§6.4):
   - sandboxes with a small trusted base, air gaps with a narrow API, and formal methods;
   - the AI as "a principal" with its own identity and access control;
   - intrusion and anomaly detection, logging and auditing, and least privilege;
   - hierarchical monitoring, with cheap monitors escalating to expensive ones.

**Enablers and assurance:** interpretability, uncertainty estimation, safer design patterns, alignment stress tests, and **safety cases** (inability, control, incentives, understanding).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | A threat model naming two adversaries (user and model) with controls for each, including weight security and insider controls for the model itself |
| Cryptography | adjacent | Encrypted processing and confidential computing for weights; it specifies nothing |
| This project | adjacent | Two Threat sources (malicious user, misaligned model as insider), Mitigations at the model, system and security levels, and evaluation-gated controls. These map to Threat, Mitigation and Evidence (**DEC-001**). It is a developer's agenda, not a system model |

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | adjacent | AIT-115; AIT-055, AIT-026, AIT-052, AIT-053, AIT-073 to AIT-077, AIT-081, AIT-082, AIT-122 | AIT-115 (rogue or misaligned agent behaviour) cites it, and the misalignment area is that class. Its misuse section cites the evidence for weight exfiltration (AIT-055), insider sabotage (AIT-026), API parameter extraction (AIT-052, 053), jailbreaks (AIT-073 to 077), safety removal by fine-tuning and white-box edits (AIT-081, 082), and AI vulnerability discovery (Big Sleep, AIT-122). It reports no incidents of its own |
| Existing AI threat models | core | TM-104 | TM-104's source, and its capture holds: four risk areas, two lines of defense, and the model as insider. TM-104 could add the adversary axis (user vs model), which is the paper's reason for the split, and the gating chain from threat model to capability evaluation, threshold, mitigation and red-team test |
| Weakness enumerations | adjacent | ASI10; ASI03?; NISTAML.04; OWASP agentic T7, T13 | The mapping is `sources.md`'s, apart from T7 and T13 (ours, from `owasp-agentic-threats-mitigations-v1-1`: misaligned and deceptive behaviours, rogue agents). The paper cites no catalog. ASI10 (rogue agents) fits the misalignment area. ASI03 stays `sources.md`'s open question; it isn't checked here |
| Attack → asset mapping | core | A02, A03; C05, C08, C12, C13, C15 | Assets are the weights (A02) and safeguard behaviour (A03). Paths are serving and APIs (C05), agents acting on hosts (C08), insiders (C12), hosted frontier models (C13) and the training and serving infrastructure (C15). The insider framing turns the model itself into an actor against C08 and C15. The mapping is ours |

## Implementations

None, searched 2026-11-22: a research agenda. Its misuse strategy is carried out through the Frontier Safety Framework (`gdm-fsf-v3-2025`, and the version it cites, `gdm-2025-updating-frontier-safety-framework`).

| Name | Kind | License | URL |
|---|---|---|---|

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, digest and `cites` |
| `summary.md` | this summary, with the RPT-0014 applicability table |

## Reference expansion

About 650 references, 648 of them with links, checked against `sources.md` and the library on 2026-11-22. In scope: attacks on AI systems and defenses tested against them, AI-enabled offense (cyber and bio uplift), misalignment threats acting against developers (scheming, alignment faking, sabotage, reward tampering), and AI threat models.
- **In `sources.md` (45):** among them Sleeper Agents (S-0270), emergent misalignment (S-0370), WMDP (S-0923), Constitutional Classifiers (S-0460), stealing part of a production model (S-0232), Big Sleep (S-0980), RAND (S-0793) and the International AI Safety Report (S-0751). They're all in `cites`.
- **In the library only (11):** among them the dangerous-capability evaluations (`phuong-2024-dangerous-capabilities`), Project Naptime, AI sandbagging, deliberative alignment, the 2023 Preparedness Framework, and the jailbreak study cited under its workshop title (`liu-2023-jailbreaking-chatgpt-prompt-engineering`).
- **Earlier versions of `sources.md` entries, added as stubs (2):** Anthropic's RSP v2.0 (2024-10-15; S-0798 is v2.2) and DeepMind's "Updating the Frontier Safety Framework" (2025-02-04; S-0805 is v3.0).
- **Missing, added as stubs (44):**
  - **37 arXiv papers:**
    - misalignment threats: alignment faking, in-context scheming, sabotage evaluations, reward tampering, Carlsmith on scheming, the AI deception survey, and situational awareness (Berglund; SAD);
    - AI control: AI control, Ctrl-Z, adaptive deployment of untrusted models, and CoT monitoring with obfuscation;
    - jailbreaks and defenses: h4rm3l, multi-turn human jailbreaks, red-team LMs from multi-agent games, build-it-break-it, latent adversarial training, refusal-feature adversarial training, SafeDecoding, Safe LoRA, and high-stakes adversarial training;
    - attacks on unlearning: Deeb and Roger, Lynch, quantization recovery, Cooper, concealment in diffusion models, and Barez's open problems;
    - misuse and offense: combinations of safe models, the misuse taxonomy, open weights and pandemic agents, the reality of AI biorisk, AI persuasion, DeepDGA, hard-label model stealing, autonomous replication tasks, model evaluation for extreme risks, and the catastrophic-risks overview;
  - **7 web documents, pinned by Wayback copies:** RMU unlearning is shallow, training on reward-hacking documents, specification gaming, the RAND bio red-team study, OpenAI on covert influence operations and on a bio early-warning evaluation, and Zwetsloot and Dafoe on accidents, misuse and structure.
- **Not stubbed (2):** the International AI Safety Report's interim version (an earlier version of S-0751), and Carlini's alignment-workshop talk, which has no document.
- **Out of scope (the rest, about 540):**
  - capability, scaling and forecasting work;
  - amplified oversight and debate;
  - interpretability and lie-detection methods;
  - unlearning and refusal methods without a security evaluation;
  - safety-case frameworks, an assurance method;
  - red-teaming methodology reviews;
  - conceptual alignment posts (gradient hacking, collusion, corrigibility);
  - existential-risk arguments;
  - vendor safety pages;
  - economics, policy, history and psychology references.

## Limits

- **An agenda, not results.** Most of it is planned or open research directions; the paper says its security thinking for misaligned AI "is particularly tentative".
- **Severe harm only.** Mistakes and structural risks are scoped out, and so are lesser harms, which most company threat models would cover.
- **One developer's view.** It is aligned with DeepMind's own Frontier Safety Framework, and it cites the February 2025 version, which v3.0 has since replaced.
- **Thin on concrete controls.** Weight security (§5.6) and security against a misaligned model (§6.4) get a page or two each, and it defers detail to RAND.
