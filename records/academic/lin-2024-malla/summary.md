---
schema: "library-summary/v1"
id: lin-2024-malla
record: lin-2024-malla
type: summary
updated: "2026-11-03"
---

# Malla: Demystifying Real-world Large Language Model Integrated Malicious Services

|  |  |
|---|---|
| **Type** | paper (a measurement study) |
| **Maturity** | _unset_. A peer-reviewed conference paper; no standing is asserted |
| **Authors** | Zilong Lin, Jian Cui, Xiaojing Liao, XiaoFeng Wang (Indiana University Bloomington) |
| **Published** | 33rd USENIX Security Symposium, Philadelphia, 14–16 August 2024, pp. 4693–4710, ISBN 978-1-939133-44-1. arXiv v1 2024-01-06 |
| **Identifier** | arXiv:2401.03315; https://www.usenix.org/conference/usenixsecurity24/presentation/lin-zilong |
| **Source** | https://www.usenix.org/system/files/usenixsecurity24-lin-zilong.pdf, the open-access proceedings PDF |
| **Digest** | `sha256:2bea7562bb330cf56ebb0aaa18db2e150849cf1dee38a189cc6d7179bb848c66` (1,029,204 bytes, 19 pages, retrieved 2026-11-03). The RPT-0014 manifest has no entry for S-0287 |

## Overview

**What it studies.** "Mallas" are LLM applications sold or shared as malicious services, mainly for writing malware, phishing emails and phishing sites.

**Data (§3, Table 2).**
- 13,353 listings from nine underground markets and forums (November 2022 to October 2023), yielding 14 commercial Malla services. The authors obtained 9 of them: 2 free copies and 7 purchases, under IRB approval.
- 198 Malla projects hosted on the public LLM-app platforms Poe and FlowGPT.

**Findings.**
- *Two ways to build one (§6):* wrap an uncensored model (Davinci-002/003, Pygmalion-13B, Luna AI Llama2 Uncensored), or jailbreak a public API, mostly gpt-3.5-turbo. The authors collected 182 jailbreak prompts.
- *Economics (§4.3):* subscriptions cost about $5–199 a month. WormGPT's crypto addresses took in about $28K over two months.
- *Output quality (§5):* mixed.
  - Some Mallas write compilable code that VirusTotal does not detect, and readable phishing emails.
  - None of 22 compilable exploits for two specific CVEs worked (§5.3).
  - Crowd workers recognised Malla-written phishing more often than ordinary phishing (§5.4).
- *Persistence (§4.1):* many services and Poe/FlowGPT projects stayed up after the authors disclosed them to the platforms.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Primary evidence of real criminal use of LLMs through jailbreaks and uncensored models |
| Cryptography | `none` | No cryptographic content |
| This project | `adjacent` | Evidence for jailbreak and misuse classes, and for platform-level abuse. Not a threat-modeling source |

`bears_on: none yet.` The paper informs no ARCH-0001 decision or requirement. It is `summarized` because LANES.md requires full summaries for subset-1 sources; no relevance is claimed.

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | core | AIT-073; AIT-081, AIT-082; AIT-083; AIT-126 | **AIT-073 (manual jailbreaks):** 182 role-play and rule-breaking jailbreak prompts drive Mallas built on public APIs (§6.3, Tables 4–5). **AIT-081 / AIT-082 (safety removal):** Mallas wrap models released without safety training or fine-tuned on NSFW data (§6.2). RPT-0014's catalog lists S-0287 under both. **AIT-083 (system-prompt extraction):** the authors used a "previous instructions" leak to recover the hidden jailbreak prompts of 54 of 55 Poe and FlowGPT projects, succeeding on 93% of a ground-truth set (§6.1). **AIT-126 (AI-written phishing):** Malla-written phishing emails and sites were measured (§5.2, §5.4). Only the Malla ecosystem itself is in the wild; the quality tests are the authors' own |
| Existing AI threat models | none | — | §2.2 and Fig. 1 describe the criminal supply chain: develop, deploy, promote, sell, use. That is an ecosystem model, not a threat model of a system |
| Weakness enumerations | adjacent | AML.T0054, AML.T0016.002, AML.T0052.000; NISTAML.018 — **concept-level, our mapping** | Neither ATLAS release 2026.09 nor NIST AI 100-2e2025 cites the paper (checked 2026-11-03). The ATLAS ids are concept matches: LLM Jailbreak; Obtain Capabilities: Generative AI; Spearphishing via Social Engineering LLM |
| Attack → asset mapping | adjacent | A13; C07, C13 — **assigned by us** | The paper names the parties harmed or abused: LLM vendors whose APIs are jailbroken, hosting platforms (Poe, FlowGPT) whose policies are broken, and payment hosts (§4.2, §7). It gives no asset model. Our ids: A13 (brand, reputation and legal standing of providers and platforms); C13 (third-party model providers); C07 (the LLM-app layer that hosts Malla projects) |

RPT-0014's incident INC-179 is this paper.

## Implementations

Searched 2026-11-03. The authors released their prompts, jailbreak prompts and Malla responses at https://github.com/idllresearch/malicious-gpt, with no licence file declared. This is a dataset for building detectors, not a tool to build on.

| Name | Kind | License | URL |
|---|---|---|---|
| malicious-gpt | open data and code from the study | none declared | https://github.com/idllresearch/malicious-gpt |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | Metadata. `cites` lists the jailbreak, prompt-injection and LLM-misuse work the paper builds on |
| `summary.md` | This document |

**Reference expansion.** The references were screened with the Batch 1 rule. The in-scope primary sources it relies on are all in `sources.md` already: Do Anything Now (S-0201), PromptInject (S-0149), ThreatGPT (S-0688), LLM spear phishing (S-0168) and indirect prompt injection (S-0166). **No stubs are proposed.** The rest are marketplace pages, model cards, tools and earlier cybercrime measurement studies, which are outside RPT-0014's attack scope.

## Limits

- **A snapshot of a moving market.** Data runs from February to October 2023, with follow-up to March 2024. Several services died with OpenAI's Davinci deprecation (§4.1), and new ones kept appearing (§7).
- **Small, purchase-biased sample.** 9 of 14 services were obtained. Some purchases yielded nothing, and some services are themselves scams (§3.1).
- **Quality metrics are proxies.** Compilability, readability and VirusTotal or OOPSpam evasion do not show that the output works (§5.1). The one functional test, of exploits for two specific CVEs, found no working exploit (§5.3).
- **The user study omits key phishing cues.** Sender addresses and URLs were left out, which the authors say may misstate real susceptibility (§5.4).
- **No in-the-wild attribution.** No real phishing sample or malware hash could be tied to Malla output (§7).
- **Backend attribution is partly inferred.** For three services the backend comes from a classifier with 0.87 precision, not from direct evidence (§6.1).
