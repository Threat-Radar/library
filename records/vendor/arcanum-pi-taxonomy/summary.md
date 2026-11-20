---
schema: "library-summary/v1"
id: arcanum-pi-taxonomy
record: arcanum-pi-taxonomy
type: summary
updated: "2026-11-20"
lane: catalogs-schema
reviewed_by: ""
---

# Arcanum Prompt Injection Taxonomy

|  |  |
|---|---|
| **Type** | dataset (a taxonomy as one JSON file, with an interactive web viewer) |
| **Maturity** | _unset — do not guess_ (practitioner work, not peer-reviewed) |
| **Authors** | Jason Haddix, Arcanum Information Security |
| **Published** | repository created 2025-02-26; v1.6 and v1.6.1 released 2026-06-29; read at commit `e02cf5b6` (2026-06-29) |
| **Identifier** | https://www.arcanum-sec.com/pitax; https://github.com/Arcanum-Sec/arc_pi_taxonomy |
| **Source** | `docs/data/taxonomy.json` at commit `e02cf5b6e202f195c6b6c01484e99519f797acc6` (CC BY 4.0) |
| **Digest** | `fc26b73a909faf73087dac4829cbd2118eb3f4505db6729dc048bc6fb3e1daa7` (that file) |

## Overview

A classification of prompt injection and jailbreak attacks, written for penetration testers moving into AI red teaming. It has **172 nodes in four pillars**, each node with a stable reference code:

| Pillar | Code | What it answers | Count |
|---|---|---|---|
| Intents | `PIT-I-NN` | What the attacker wants (system prompt leak, data exfiltration, unauthorized action, denial of wallet, cross-tenant leakage …) | 27 |
| Techniques | `PIT-T-NN` | How the model is manipulated (role play, Crescendo, many-shot, tool-definition injection, confused deputy, prompt worm …) | 70 |
| Evasions | `PIT-E-NN` | How the payload gets past filters (encodings, ciphers, Unicode tags, bidirectional text, adversarial poetry …) | 63 |
| Inputs | `PIT-N-NN` | Where the payload enters (API, chat, file upload, indirect input, image, audio, supply chain, sensor …) | 12 |

Each node has a title, a description, "ideas", example prompts (except the inputs), "also known as" names from other frameworks and papers, and a delivery tag: direct (134 nodes), indirect (12) or both (26). Two white-box techniques that need the model's weights are flagged `local`: gradient-based attacks and abliteration.

The pillars are independent lists, so the data has no links between an intent, a technique and an input. v1.6 grew the taxonomy from 107 to 171 nodes, added the codes and alias lists, and replaced the per-node Markdown with the JSON. v1.6.1 added PIT-T-70 (function-call parameter smuggling).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | An enumeration of attacks on LLM applications and agents, with example payloads |
| Cryptography | none | Ciphers appear only as evasion encodings |
| This project | adjacent | Stable codes and a JSON file make it importable as a weakness or attack-pattern catalog beside CWE and CAPEC (**DEC-008**), with each pillar a separate facet. Joining the four into one attack pattern would be tmodel's own modelling |

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | adjacent | AIT-063, AIT-064, AIT-073 to AIT-077, AIT-091, AIT-096, AIT-098 | AIT-063 (direct prompt injection) cites it. Its techniques name many attacks the catalog has: manual, optimization, multi-turn, many-shot and best-of-N jailbreaks (AIT-073 to 077), indirect injection (AIT-064), confused deputy (AIT-091), tool-definition poisoning (AIT-096) and tool-preference manipulation (AIT-098). It lists techniques, not incidents, and gives no evidence of use in the wild |
| Existing AI threat models | none | — | A taxonomy with no system model. `threat-models.md` doesn't list it |
| Weakness enumerations | core | PIT-I/T/E/N-NN; AML.T0051.000/.001/.002, AML.T0054, AML.T0056, AML.T0057, AML.T0077 (23 ATLAS ids in all); LLM01:2025 to LLM10:2025; NISTAML.02, .027, .031, .035, .038, .04 | The counts match `enumerations.md` (27 + 70 + 63 + 12). Catalog aliases are sparser than `sources.md` suggests: 118 of 172 nodes have some alias, but only 24 carry an ATLAS id, 23 an OWASP LLM id and 9 a NIST id, and none cites a CWE. All 23 ATLAS ids exist in ATLAS 2026.09. **ATLAS 2026.10 removes AML.T0056 and AML.T0057**, which PIT-I-13, PIT-I-16 and PIT-I-19 cite. **`sources.md`'s "aliases to … AML.T0068" doesn't hold:** no node cites AML.T0068 (LLM Prompt Obfuscation), not even among the 63 evasions, which are exactly that |
| Attack → asset mapping | adjacent | C01, C04, C05, C06, C07, C09, C10, C16; A04, A07, A01, A02, A11, A13 | The inputs are entry points: API (C05), chat (C07), files, collaboration and productivity content (C01), indirect input and retrieval (C01, C06), tools and memory (C09, C10), supply chain (C04), and sensor and cross-modal input (C16). Intents name the assets: the system prompt (A04), sensitive and cross-tenant data (A07), training data and model (A01, A02), spend (A11) and business integrity (A13). The mapping is ours |

## Implementations

Searched 2026-11-20 (GitHub repository and code search):

| Name | Kind | License | URL |
|---|---|---|---|
| Arcanum-Sec/arc_pi_taxonomy | The taxonomy's own interactive viewer (`docs/index.html`, `app.js`) | CC BY 4.0 | https://github.com/Arcanum-Sec/arc_pi_taxonomy |
| 0x0pointer/agent-smith | Red-team MCP server that vendors `taxonomy.json` as its attack vocabulary | AGPL-3.0 | https://github.com/0x0pointer/agent-smith |
| xenprotocol/llm-pentesting-book | Companion code for a 2026 book, which builds attack combinations from the taxonomy | MIT | https://github.com/xenprotocol/llm-pentesting-book |

Microsoft's `agent-governance-toolkit` cites it in a policy mapping but doesn't use the data.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, digest, commit and `cites` |
| `summary.md` | this summary, with the RPT-0014 applicability table |

## Reference expansion

The taxonomy cites works only in its "also known as" lists. They hold 66 arXiv papers and many named attacks without a link, such as vendor names and Pangea, garak and HiddenLayer codes. The 66 papers were checked against `sources.md` and the library on 2026-11-20, by arXiv id and then by title:
- **In `sources.md` (28):** S-0074, S-0166, S-0173 (also the library's `llm-programmatic-dual-use`), S-0199, S-0207, S-0211, S-0213, S-0214, S-0242, S-0249, S-0261, S-0271, S-0274, S-0283, S-0291, S-0308, S-0310, S-0343, S-0369, S-0392, S-0397, S-0419, S-0431, S-0446, S-0493, S-0577, S-0615 and S-0699. S-0577 and S-0615 are cited there by DOI, not arXiv id.
- **Missing, added as stubs (37):** jailbreak and injection papers from 2023 to 2025, such as CodeAttack, FlipAttack, SATA, MetaCipher, ChatInject, ToolTweak, PARASITE, Chain-of-Thought Hijacking, adversarial poetry and BitBypass. Each is cited by this record.
- **Out of scope (1):** Trojan Source (arXiv 2111.00169), on invisible bidirectional characters in program source code. Arcanum borrows it for an evasion, but it is not about AI.

## Limits

- **Practitioner judgement.** The taxonomy gives no method for choosing or bounding nodes and no evidence of how often each attack works. Its labels are retitled plain-English names, and its alias lists are mappings it asserts without checking.
- **Thin catalog crosswalk.** About one node in seven names an ATLAS or OWASP id, and none a CWE. A crosswalk from it would mostly be new work.
- **Some aliases don't match their source.** PIT-T-44 calls arXiv 2505.16888 "SPECTRE", but its current title is PARASITE. PIT-T-08 gives AML.T0043.003 as "Manual Adversarial Data", where ATLAS says "Manual Modification".
- **A living file.** The "always-current" web app is canonical. The commit pin fixes what was read, and node codes are stable, but the contents and counts change between releases (107 to 172 nodes in v1.6).
- **No combinations.** The four pillars are independent lists. Which technique, evasion and input combine for which intent is left to the tester.
