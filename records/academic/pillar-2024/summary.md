---
schema: "library-summary/v1"
id: pillar-2024
record: pillar-2024
type: summary
updated: "2026-11-03"
---

# PILLAR: an AI-Powered Privacy Threat Modeling Tool

|  |  |
|---|---|
| **Type** | paper (a preprint describing a tool) |
| **Maturity** | _unset_. A preprint; no peer-reviewed version found and no standing asserted |
| **Authors** | Majid Mollaeefar, Andrea Bissoli, Silvio Ranise (FBK Center for Cybersecurity; University of Trento) |
| **Published** | arXiv preprint, v1 2024-10-11, the only version |
| **Identifier** | arXiv:2410.08755 |
| **Source** | https://arxiv.org/pdf/2410.08755v1 |
| **Digest** | `sha256:ac066c325ca2354ed5d33a9414f0aef56a86187bc55afdaa34421610e858da06` (198,009 bytes, 10 pages, retrieved 2026-11-03). This matches the RPT-0014 `pdf-manifest.tsv` entry for S-0959 |

## Overview

**What PILLAR is.** PILLAR applies LLMs to LINDDUN privacy threat modeling. It is not a model of threats to AI.

**What it does (§3, Fig. 1).** From a plain-language system description, it can:
- generate or import a data-flow diagram (DFD);
- run three threat-elicitation modes:
  - a quick, single-prompt LINDDUN threat list;
  - a simulation of LINDDUN GO, the card-game method, in which several LLM "experts" discuss over several rounds and a judge LLM gives the verdict;
  - LINDDUN PRO, per DFD edge, using LINDDUN's mapping table and threat trees;
- generate impact assessments and suggest controls drawn from privacy patterns;
- produce a PDF report.

**Implementation.** A Streamlit web app over the OpenAI, Gemini and Mistral APIs, with code on GitHub.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | Privacy threat modeling: a security-adjacent method, not an attack or defence |
| Cryptography | `none` | No cryptographic content |
| This project | `core` | A direct comparator for tmodel. It turns a system description into DFD-based threats with LLMs, which is what tmodel's generation pipeline does. RPT-0014 lists it as TM-036 |

**What it bears on.** **R-018** (attach a human review to any element; nothing machine-proposed is final without it). ARCH-0001 §2 treats an AI-generated threat model as a set of hypotheses.
- PILLAR lets users edit LLM-generated assessments and choose which threats go into the report (§3.2.3–3.2.4), but records no review trail.
- It publishes no evaluation of its outputs' accuracy.

That illustrates why the traceability requirement matters.

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | none | — | It describes no attack |
| Existing AI threat models | adjacent | TM-036 | RPT-0014's TM-036 is this tool. It is an LLM-assisted threat-modeling method, LINDDUN on DFDs, rather than a threat model of AI systems, hence adjacent |
| Weakness enumerations | none | — | LINDDUN's privacy threat categories are a threat taxonomy, not one of RPT-0014's weakness enumerations (CWE, NISTAML, ATLAS, OWASP) |
| Attack → asset mapping | adjacent | — | The LINDDUN PRO mode maps each threat category to the source, data flow and destination of a chosen DFD edge (§3.2.2). That is a threat-to-component mapping method, but for privacy threats, with no AI attacks and no RPT-0014 ids |

## Implementations

Searched 2026-11-03. PILLAR is released at https://github.com/stfbk/PILLAR under Apache-2.0, still maintained (last push 2026-08). It needs an OpenAI, Gemini or Mistral API key.

| Name | Kind | License | URL |
|---|---|---|---|
| PILLAR | open source, authors' tool | Apache-2.0 | https://github.com/stfbk/PILLAR |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | Metadata. `cites` points to LINDDUN (`deng-linddun-2011`, `linddun-org`) and STRIDE-GPT (`stride-gpt`), records this library already holds |
| `summary.md` | This document |

**Reference expansion.** The references were screened with the Batch 1 rule. LINDDUN and STRIDE-GPT are already library records, cited by id. The other references are general LLM-for-security surveys and tools outside RPT-0014's attack scope. AttackGen is a GitHub tool, which would be an `implementations` entry, not a record. **No stubs are proposed.**

## Limits

- **No evaluation, despite the claim.** §1 says "Section 4 presents our case studies and evaluation results". Section 4 is Related Work, and the paper has no case study or evaluation. Its claims of improved accuracy and efficiency (Abstract, §5) are therefore unsupported in this paper. This is a confirmed defect.
- **The outline is garbled.** §1 says related work and the conclusion are both in "Section 4"; the conclusion is Section 5.
- **A preprint.** No peer review was found, and there is only one arXiv version.
- **Privacy only.** The tool covers LINDDUN privacy threats, not security threats such as STRIDE, and not AI-specific threats.
- **Depends on external LLM APIs**, with the cost, data-sharing and reproducibility issues that brings. The output varies with the provider chosen (§3.1.2).
