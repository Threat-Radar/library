---
schema: "library-summary/v1"
id: google-2025-gtig-ai-threat-tracker
record: google-2025-gtig-ai-threat-tracker
type: summary
updated: "2026-11-02"
---

# GTIG AI Threat Tracker: Advances in Threat Actor Usage of AI Tools

|  |  |
|---|---|
| **Type** | article (vendor threat-intelligence report, published as a blog post and a PDF) |
| **Maturity** | _unset_ (a vendor report; no maturity level applies) |
| **Authors** | Google Threat Intelligence Group (no individual authors named) |
| **Published** | 2025-11-05 (blog post date; the PDF cover says November 2025) |
| **Identifier** | URL only: https://cloud.google.com/blog/topics/threat-intelligence/threat-actor-usage-of-ai-tools |
| **Source** | https://services.google.com/fh/files/misc/advances-in-threat-actor-usage-of-ai-tools-en.pdf (the report's download link in the blog post) |
| **Digest** | `sha256:bc517904af9d5c40ad4f3a7dc1f8bba30c6b874f42ca93a1146a02ea1f86bf45` (PDF, 20 pages; the same digest as RPT-0014's `pdf-manifest.tsv`) |

## Overview

Google Threat Intelligence Group (GTIG) updates its January 2025 analysis of generative-AI
misuse and reports a shift: attackers now deploy malware that uses AI during execution, not
only AI for productivity. Table 1 lists five families seen in 2025. PROMPTFLUX, an
experimental VBScript dropper found in early June 2025, sends a hard-coded API key and a
prompt to Gemini asking for antivirus-evading VBScript; one variant asks Gemini to rewrite
the whole script every hour. PROMPTSTEAL, used by APT28 against Ukraine and reported by
CERT-UA as LAMEHUG, queries Qwen2.5-Coder-32B-Instruct through the Hugging Face API for
one-line Windows commands, which it runs blindly before sending the results out; GTIG calls
it the first malware it has seen querying an LLM in live operations. PROMPTLOCK is a
proof-of-concept ransomware that has an LLM write Lua scripts. QUIETVAULT steals GitHub and
npm tokens and has AI command-line tools installed on the host search for other secrets.
FRUITSHELL, a PowerShell reverse shell, carries prompts meant to defeat LLM-based security
analysis. The rest of the report covers actors who tried to talk Gemini past its safeguards
by posing as capture-the-flag players, students or researchers (a China-nexus actor got
useful exploitation help this way), and state actors from China, Iran and North Korea who
used Gemini at every stage of an intrusion: reconnaissance, phishing lures, exploit research,
C2 development, data exfiltration and, in one case, an attempt to build an agent that turns
questions into SQL over personal data. The report also covers an underground market for AI
tools that almost always advertise phishing support, and North Korean deepfake lures. Most
cases end with Google's response: disabled accounts and assets, and stronger classifiers and
model.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Threat-intelligence evidence of malware that calls LLMs while running, and of state actors using an LLM across intrusion stages |
| Cryptography | `none` | Only incidental: PROMPTLOCK encrypts files, and one actor's script exposed its encryption key to Gemini |
| This project | `adjacent` | The object model has to represent AI on the attacker's side: a hosted model API that malware calls at runtime, and AI command-line tools on a developer workstation that malware turns against their owner |

`bears_on: DEC-001a` (the core type system, accepted in ADR-0010) and `DEC-003` (the risk
metric, accepted in ADR-0006, in which attack feasibility is one input). The DEC-003 link is
ours: Table 1's status for each family (experimental, or observed in operations) is evidence
for feasibility, but the report does not discuss risk metrics.

## Implementations

Searched on 2026-11-02. None applies: this is a threat-intelligence report. Table 1 links one
VirusTotal sample per malware family; the samples are malware and were not downloaded.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this document |

## Limits

- **Two of the five families are experimental.** PROMPTFLUX's self-modification function is
  commented out and GTIG says it cannot compromise a victim network or device; PROMPTLOCK is a
  proof of concept.
- **Few numbers.** No counts of victims, samples or prompts; the findings rest on Google's
  visibility, chiefly of Gemini use.
- **Assessments, not proof.** Attribution is GTIG's, and some claims are hedged: PROMPTSTEAL
  "likely" uses stolen API tokens, and PROMPTFLUX is unattributed, linked to financially
  motivated actors only through its lure file names.
- **Unmeasured mitigations.** Google says it strengthened its classifiers and the model, but
  gives no measurement.
- **Two forms of one text.** The blog post states that it includes the report in full. The
  PDF digested here also carries the text of the attack-lifecycle figures; the blog post
  shows PROMPTSTEAL's two prompts as text (Figures 2 and 3), where the PDF shows them as
  images.

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | core | AIT-123, AIT-125, AIT-130, AIT-073, AIT-113, AIT-126, AIT-127, AIT-122 | AIT-123 and AIT-125 cite it, and it is the primary source for INC-131: PROMPTFLUX, PROMPTSTEAL, PROMPTLOCK and QUIETVAULT call an LLM while running (AIT-123), and QUIETVAULT has installed AI command-line tools hunt for secrets (AIT-125). The other links are ours: FRUITSHELL's prompts aimed at LLM-powered security analysis (AIT-130); capture-the-flag, student and researcher pretexts used to get past Gemini's guardrails, successfully in one capture-the-flag exchange (AIT-073); PROMPTSTEAL's use of what GTIG calls likely stolen Hugging Face API tokens (AIT-113); phishing lures written with Gemini by APT42 and UNC1069 (AIT-126); UNC1069's deepfake image and video lures (AIT-127); and exploit research by UNC4899 and a China-nexus actor (AIT-122). QUIETVAULT's described behaviour resembles INC-118 (Nx "s1ngularity"), but the report does not name Nx, so INC-118 is not linked |
| Existing AI threat models | none | none | A threat-intelligence report on AI as the attacker's tool, not a threat model of an AI system; its figures map each actor's Gemini use onto attack-lifecycle stages. threat-models.md does not list it |
| Weakness enumerations | none | AML.T0102, AML.T0096, AML.T0112.000, AML.CS0044, NISTAML.04 | Not an enumeration. ATLAS 2026.09 does not cite it, but its case study AML.CS0044 covers PROMPTSTEAL under CERT-UA's name, LAMEHUG, citing CERT-UA, BleepingComputer and Logpoint; NIST AI 100-2e2025 predates it. The ids are RPT-0014's mapping in sources.md: Generate Malicious Commands, AI Service API, Local AI Agent, the LAMEHUG case study and NIST's misuse category |
| Attack → asset mapping | adjacent | C14, C13, C11, C12 | Names what each family takes but models no system. Our mapping, following the catalog's use of C14 for endpoints in AIT-123: victim endpoints and developer workstations with AI command-line tools (C14; documents A07, secrets A09, hosts A10); hosted model APIs that serve as attacker infrastructure (C13: Gemini, Hugging Face), reached with hard-coded or likely stolen keys (C11); and the people targeted by lures and deepfakes (C12; A15) |
