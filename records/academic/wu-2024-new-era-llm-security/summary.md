---
schema: "library-summary/v1"
id: wu-2024-new-era-llm-security
record: wu-2024-new-era-llm-security
type: summary
updated: "2026-11-20"
lane: catalogs-schema
reviewed_by: ""
---

# A New Era in LLM Security: Exploring Security Concerns in Real-World LLM-based Systems

|  |  |
|---|---|
| **Type** | paper (system-level security analysis, with an end-to-end attack) |
| **Maturity** | _unset — do not guess_ (arXiv preprint; no peer-reviewed version found) |
| **Authors** | Fangzhou Wu, Ning Zhang, Somesh Jha, Patrick McDaniel, Chaowei Xiao (University of Wisconsin-Madison; Washington University in St. Louis) |
| **Published** | arXiv v1, 2024-02-28 (the only version on 2026-11-20) |
| **Identifier** | arXiv:2402.18649 |
| **Source** | https://arxiv.org/pdf/2402.18649 |
| **Digest** | `e9d02ca40e9db39b363c5b3f9f5c98d5bf400085113975c9e43d3b985ac9d792` (17 pages; matches `pdf-manifest.tsv`) |

## Overview

The paper argues that LLM security has to be studied as a system, not as one model. It models an LLM system as **objects**: the core LLM, and facilities such as the frontend, web tools, plugins and a sandbox. It then defines three things over those objects:
- **actions**, information processing inside one object;
- **interactions**, a one-way call and return between two objects;
- **constraints**, rules over an action or over an interaction trace.

The authors state three principles for analysing such a system (§5):
- look at more than one layer: the LLM's own action, and its interactions with other objects;
- check whether each needed constraint exists;
- test how robust each constraint is. This matters because a constraint the LLM enforces is probabilistic: it is learned in training or written into the input, such as a system message.

**Five cases on ChatGPT with GPT-4 (§6):**
1. GPT-4 refuses to output an external Markdown image link. A puzzle-style jailbreak bypasses the refusal, and so does the same request arriving as indirect prompt injection through a web plugin.
2. The code-interpreter sandbox has no isolation between sessions. A file uploaded in a session the user deleted is still listed in a new session, even on another device.
3. Injected web content makes GPT-4 call a second plugin (Doc Maker). A confirmation step exists, but injected text saying "there is no need to ask me for … confirmation" gets past it. The confirmation is taken from external content as if the user gave it.
4. The frontend renders any image link the LLM outputs. All 50 explicit or violent test images were displayed.
5. OpenAI's "Safe URL Check" blocks rendering a URL that carries data. It only checks whether the URL already appeared in the conversation.

**The end-to-end attack (§7):** the attacker publishes a web page, and the user asks GPT-4 to read it through a web plugin. The page's instructions run four steps:
1. Save the chat history into a Doc Maker document, which gives link L1.
2. Write the target URL, carrying L1, into a second document (L2).
3. Read L2 back, so the target URL appears in the conversation.
4. Render it. Safe URL Check passes, because the URL is already in the conversation.

A stealth instruction hides GPT-4's intermediate output from the user. The attack worked with all 8 web plugins tested, and the authors say they reported the issues to OpenAI.

**Suggested mitigations (§8):** output filtering with procedural control flow, and labelling each input with its source (user or external) so a model trained on the labels ignores instructions from external content.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | Concrete attacks on a deployed LLM system, each tied to a missing or weak control on one data flow |
| Cryptography | none | No cryptographic content |
| This project | adjacent | Objects, information flows and constraints on flows map onto tmodel's Components, DataFlows and controls (**DEC-001**). The paper applies them by hand to one product and gives no machine-readable form |

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | core | AIT-066, AIT-064, AIT-091, AIT-073 | AIT-066 cites it: the Safe URL Check bypass and image-URL exfiltration. The other cases fit AIT-064 (injection through a web plugin), AIT-091 (injected content calls Doc Maker with the user's privileges) and AIT-073 (the puzzle jailbreak, which uses competing objectives). **No AIT covers case 2, the sandbox kept across sessions:** AIT-041 is isolation between tenants of an AI platform, and this is one user's files outliving the session they deleted |
| Existing AI threat models | core | TM-031 | TM-031's source. Its decomposition (LLM plus objects; security as constraints on flows) and threat categories match the paper. Two scope limits are missing from TM-031: the analysis is of OpenAI GPT-4's design only (footnote 1), and it leaves out flaws inside facilities and flows that don't involve the LLM (footnote 2) |
| Weakness enumerations | adjacent | AML.T0051.001, AML.T0077, AML.T0053, LLM01:2025, LLM02:2025, LLM05:2025, NISTAML.03 | The paper cites no catalog. The mapping is `sources.md`'s, plus AML.T0053 (AI Agent Tool Invocation) for case 3. `sources.md` writes "AML.T0077 LLM Response Rendering?": ATLAS 2026.09 has AML.T0077 under that name (Demonstrated), so the question mark can go |
| Attack → asset mapping | core | C01, C07, C09, C10, A06, A07, A03 | The attacker's web page is an external source (C01). The rendering frontend and chat UI are C07. The web plugins, Doc Maker and the code-interpreter sandbox are C09 tools. The chat history is C10. The assets are the chat history (A06), the user's files and conversations (A07), and refusal behaviour (A03). The mapping is ours |

## Implementations

Searched 2026-11-20. The paper links a demo page (CC BY-SA 4.0), and that page links `llmsystem1/llm-system-security`, which holds only a one-line README and no licence. No attack code was found.

| Name | Kind | License | URL |
|---|---|---|---|
| fzwark/Secure_LLM_System | The first author's later defense, an information-flow-control monitor against indirect prompt injection (f-secure, arXiv 2409.19091, RPT-0014 S-0328). It isn't this paper's code | Apache-2.0 | https://github.com/fzwark/Secure_LLM_System |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, digest and `cites` |
| `summary.md` | this summary, with the RPT-0014 applicability table |

## Reference expansion

The paper has 60 references, checked against `sources.md` and the library on 2026-11-20:
- **In scope (25):** attacks on LLMs, prompt injection, jailbreaks, membership inference, and defenses tested against them.
  - **In `sources.md` (18):** S-0160, S-0166, S-0688, S-0741, S-0093, S-0182, S-0291, S-0147, S-0149, S-0302, S-0194, S-0691, S-0916 (also the library's `toyer-2023-tensor-trust`), S-0917, S-0206, S-0210, S-0212 and S-0220.
  - **Missing, added as stubs (6):**
    - `pedro-2023-prompt-injections-sql-injection` [36];
    - `salem-2023-maatphor` [42];
    - `suo-2024-signed-prompt` [47];
    - `wang-2023-safeguarding-crowdsourcing-surveys-prompt-injection` [51];
    - `wu-2023-unveiling-security-privacy-ethical-chatgpt` [53];
    - `yip-2024-evaluation-framework-prompt-injection-resilience` [56].
  - **Missing, not stubbed (1):** [44], an SSRN essay on privacy practice for chatbots, with no attack or evaluation.
- **Out of scope (35):**
  - the products and web pages it uses ([1] to [12], [23]);
  - classic information-flow and access-control papers ([13], [15], [18], [20], [32], [33], [41], [43], [54], [58], [59]);
  - LLM capability studies and LLM use for defense ([14], [17], [19], [21], [25], [27], [28], [35], [39], [45], [48]).

## Limits

- **One product, one moment.** It is a black-box study of ChatGPT with GPT-4 and its plugin ecosystem of late 2023, which OpenAI has since retired. The authors say they reported the issues but give no response or fix, so whether each case still holds is unknown.
- **Thin numbers.** The paper stresses that constraints enforced by an LLM are probabilistic, yet it reports no repeated trials or success rates. Its counts are 8 of 8 web plugins and 50 of 50 images.
- **The formalism finds nothing by itself.** Objects, actions, interactions and constraints are defined, but the cases were found by hand. There is no enumeration of the constraints a system needs, and no machine-readable model.
- **Partial scope by design.** Flaws inside facilities, and flows between objects that don't involve the LLM, are out of scope (footnote 2), so this is not a whole-system threat model.
- **Preprint.** arXiv v1 only, and no peer-reviewed version was found.
