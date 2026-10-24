---
schema: "library-summary/v1"
id: mecca-2026-skillsecurer
record: mecca-2026-skillsecurer
type: summary
updated: "2026-10-13"
---

# SkillSecurer: Detecting and Patching Prompt-Injection Vulnerabilities in AI Agent Skills

|  |  |
|---|---|
| **Type** | paper (tool + measurement; 18 pp.) |
| **Maturity** | _unset — do not guess_ |
| **Authors** | D. Mecca, A. Verna, Y. Bouchari, N. Jha, M. Mellia (Politecnico di Torino) |
| **Published** | arXiv v1, 2026-09-12 (no venue stated) |
| **Identifier** | arXiv:2609.14079 |
| **Source** | https://arxiv.org/pdf/2609.14079 |
| **Digest** | `3dc4816c0d01ae70a136377c5c89c4b47e32e99851031c14e96b515939400107` (not in `pdf-manifest.tsv`; computed on the arXiv copy) |

## Overview

**Agent skills** — reusable packages of instructions, scripts and configuration that extend agents such as Codex and Claude — are a new injection channel. **SkillSecurer** is an agentic framework to find and fix this: a **red agent** inserts context-compatible injections of **nine threat types** into skills (recording exactly what it changed), a **blue agent** analyses whole skill packages, gives grounded evidence and proposes patches, and a **verifier** scores findings against the recorded injections. With its best backend it detects 100% of injected cases. Applied to popular skills on **skills.sh**, it finds **latent vulnerabilities in more than 17%**, and triggers real incidents when testing some. Attack success varies widely by model (about 7–17% on Claude Opus 4.5, 57–83% on Gemini models).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | Measures a new agent supply-chain channel. |
| Cryptography | none | Not about cryptography. |
| This project | core | Skills are installable agent components; tmodel needs them as supply-chain components with their own attack steps. |

Bears on **DEC-001** (object model — agent skills as components).

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | core | AIT-095 | Rules-file, context-file and agent-skill poisoning, measured in the wild |
| Existing AI threat models | none | — | A tool and measurement |
| Weakness enumerations | adjacent | AML.T0115.002, LLM03:2025, ASI04 | Catalog entries for skill poisoning |
| Attack → asset mapping | core | C04, C08, C09 | Skill registries and marketplaces, agent runtime, tools |

## Implementations

Framework described; availability of code not checked here. Searched 2026-10-13.

| Name | Kind | License | URL |
|---|---|---|---|


## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this summary |

## Limits

- **Very recent preprint** (Sept 2026), not peer-reviewed.
- **LLM-judged detection:** results depend on the backend model chosen.
- **Not in the team PDF manifest;** digest computed here.
- Reference expansion not done in this pass (see PR notes).
