---
schema: "library-summary/v1"
id: sentinelone-2026-silent-brothers-ollama
record: sentinelone-2026-silent-brothers-ollama
type: summary
updated: "2026-11-02"
---

# Silent Brothers | Ollama Hosts Form Anonymous AI Network Beyond Platform Guardrails

|  |  |
|---|---|
| **Type** | article (vendor research post) |
| **Maturity** | _unset_ (a research blog post; no maturity level applies) |
| **Authors** | Gabriel Bernadett-Shapiro (SentinelOne) and Silas Cutler (Censys) |
| **Published** | 2026-01-29 (the page's date and its `datePublished` metadata; the Internet Archive first captured it the same day) |
| **Identifier** | URL only: https://www.sentinelone.com/labs/silent-brothers-ollama-hosts-form-anonymous-ai-network-beyond-platform-guardrails/ |
| **Source** | https://web.archive.org/web/20260302174036id_/https://www.sentinelone.com/labs/silent-brothers-ollama-hosts-form-anonymous-ai-network-beyond-platform-guardrails/ (the Internet Archive's copy of 2026-03-02, original bytes) |
| **Digest** | `sha256:b9cb7d4b04bece6d3800f6c3566cd034d910eed1da3047b36c37571e9d81ea72` (the archived response as served, gzip-compressed, 101,410 bytes; the decompressed HTML is `sha256:440337bd5c9e8f5bc1b647abd530aa2c6044600a044809108ea732406ce95d06`, 335,814 bytes) |

## Overview

SentinelLABS and Censys measured how many Ollama servers, which bind to localhost by default
but are one setting away from the open internet, are publicly reachable. Over 293 days they
recorded 7.23 million observations of 175,108 unique hosts in 130 countries and 4,032
autonomous systems. The population is bimodal: hosts seen more than 100 times are 13% of
hosts but 76% of observations, around a persistent core the summary puts at 23,000. By
network tier, hyperscalers and telecom or residential networks each hold 32% of hosts, and
about a fifth cannot be attributed at all. Model choice is concentrated: Llama, Qwen2 and
Gemma2 rank first to third under every weighting, the Q4_K_M quantization runs on 48% of
hosts, and 4-bit formats make up 72% of quantizations. Capabilities matter more than counts:
48% of hosts advertise tool calling, 22% vision and 26% reasoning models, at least 201 run
standard "uncensored" system prompts, and about 5,000 combine high capability with 87%
average uptime. The security section names five risks: free compute for spam, phishing or
disinformation; tool-enabled and retrieval-backed hosts that answer anyone's prompts;
residential addresses that launder malicious traffic; a monoculture that one flaw could hit
at once; and owners who cannot be identified or reached. The authors call the result a
governance inversion, with deployment scattered across home networks while dependency
concentrates on a few labs' models, and they conclude that exposed LLM endpoints need the
same authentication, monitoring and network controls as any other internet-facing service.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Measures an unauthenticated, internet-reachable AI attack surface at scale and analyses the threats it creates |
| Cryptography | `none` | No cryptographic content |
| This project | `adjacent` | The object model has to represent self-hosted inference servers whose exposure, capabilities (tool calling, retrieval, vision) and network tier change what an attacker can do with them |

`bears_on: DEC-001a` (the core type system, accepted in ADR-0010).

## Implementations

Searched on 2026-11-02. None applies: this is a measurement study. The software measured is
Ollama (https://ollama.com/); the scan data is Censys's.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this document |

## Limits

- **Exposure, not exploitation.** It counts reachable hosts and their advertised
  capabilities; it reports no observed abuse of them, and its threat vectors are argued.
- **Method in outline only.** Scan cadence, how a host was identified as Ollama, and how
  capabilities and system prompts were queried are not described in detail, and the
  "uncensored" count is a stated lower bound.
- **A joint study with the scan provider.** One author is from Censys, whose data it uses.
- **Read from an archive.** sentinelone.com answered scripted requests with HTTP 429 on
  2026-11-02; the digest is of the Internet Archive's copy of 2026-03-02, and the live page
  may have changed since.

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | adjacent | AIT-040, AIT-113, AIT-051, AIT-064 | AIT-040 and AIT-113 cite it. It measures the reachable surface AIT-040 attacks, but demonstrates and reports no exploitation. Its compute-abuse scenario needs no credentials, since the hosts are unauthenticated, so it fits AIT-113 (stolen keys and credentials) only loosely. Links that are ours: prompting a reachable retrieval deployment for data such as API keys (AIT-051) and indirect prompt injection through images on vision-capable hosts (AIT-064), both argued, not shown |
| Existing AI threat models | adjacent | none | Its security section sets out five threat vectors for exposed self-hosted LLMs: resource hijacking, excessive agency, identity laundering and proxy abuse, concentration risk, and governance gaps. It is a short threat analysis, not a structured model, and threat-models.md does not list it |
| Weakness enumerations | none | AML.T0049, AML.T0008.005, CWE-306, AML.T0000.003 | Not an enumeration. ATLAS 2026.09 does not cite it, though its AML.T0000.003 (Scan Databases) describes adversaries querying services such as Censys to find exposed AI infrastructure, the kind of data this study rests on; NIST AI 100-2e2025 predates it. The first three ids are RPT-0014's mapping in sources.md; AML.T0000.003 is ours |
| Attack → asset mapping | adjacent | C05, C06, C09, A11, A09, A10 | Maps the exposed surface by capability and network tier rather than by attack path. Our mapping: the inference server and its API (C05), retrieval pairings (C06) and tool calling (C09), exposing compute (A11), secrets reachable through retrieval (A09) and the hosts themselves, including residential addresses (A10) |
