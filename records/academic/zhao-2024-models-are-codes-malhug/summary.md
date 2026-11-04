---
schema: "library-summary/v1"
id: zhao-2024-models-are-codes-malhug
record: zhao-2024-models-are-codes-malhug
type: summary
updated: "2026-11-01"
---

# Models Are Codes: Towards Measuring Malicious Code Poisoning Attacks on Pre-trained Model Hubs

|  |  |
|---|---|
| **Type** | paper |
| **Maturity** | _unset_ (peer-reviewed conference paper; no maturity level applies) |
| **Authors** | Jian Zhao, Shenao Wang, Yanjie Zhao, Xinyi Hou, Kailong Wang, Peiming Gao, Yuanchao Zhang, Chen Wei, Haoyu Wang (Huazhong University of Science and Technology; MYbank, Ant Group) |
| **Published** | arXiv v1 2024-09-14 (summarized here); ASE '24, Sacramento, October 27 to November 1, 2024 |
| **Identifier** | arXiv:2409.09368; DOI 10.1145/3691620.3695271 (ACM version of record, not read) |
| **Source** | https://arxiv.org/pdf/2409.09368v1 |
| **Digest** | `sha256:a96784cd34bdff60e946ef8ddd2726ed77865125cefbf1db339ad2fd237f4d78` (arXiv v1, 12 pages; matches pdf-manifest.tsv) |

## Overview

Model hubs such as Hugging Face let anyone publish models and datasets, and loading them can
run the publisher's code: pickle-based model files execute code when they are deserialized,
and the datasets library ran a dataset's loading script by default (§2.2). The paper calls
this malicious code poisoning and, by its own account, gives the first systematic study of
it: a threat model, a taxonomy of 15 model formats by whether they can carry code (Table 2),
and the root cause, serialization formats that instantiate arbitrary objects (§3). Its
pipeline, MalHug, extracts dataset scripts, disassembles pickles and Keras Lambda layers
without running them, and applies taint analysis and YARA rules to the extracted code (§4).
Run for more than three months on Ant Group's mirror of Hugging Face, it found 91 malicious
models (76 pickle variants, 15 Keras Lambda layers) and 9 malicious dataset loading scripts
among 705,991 models and 176,386 datasets, with reverse shells, browser credential theft
and system reconnaissance among the payloads (§5). Over 55% of the models use pickle-based
serialization (§5.2).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | Measures malicious code in real model files and dataset scripts on the largest hub, and explains which formats can carry it (§3, §5) |
| Cryptography | `none` | Encryption and base64 calls appear only as detection signals (Table 3) |
| This project | `adjacent` | A model file is a component whose serialization format decides whether loading it runs code. The object model needs the format on the component and CWE-502 as the weakness it brings |

`bears_on: DEC-001a` (the core type system, accepted in ADR-0010). The paper is the measured
case of RPT-0014's trust boundary TB3 (public hub into the enterprise), where downloaded
artifacts can execute.

## Implementations

Searched on 2026-11-01. MalHug's pipeline code is not released: its repository holds the
results only.

| Name | Kind | License | URL |
|---|---|---|---|
| security-pride/MalHug | the paper's results: a CSV of the 100 malicious repositories with code slices; their source files are on Zenodo (record 13850049) | none stated | https://github.com/security-pride/MalHug |
| trailofbits/fickling | pickle decompiler and static analyzer; MalHug's model decompilation builds on it (§5.1) | LGPL-3.0 | https://github.com/trailofbits/fickling |
| protectai/modelscan | scanner for pickle variants, TensorFlow and Keras; MalHug builds on it (§5.1) | Apache-2.0 | https://github.com/protectai/modelscan |
| mmaitre314/picklescan | pickle import scanner (Table 6) | MIT | https://github.com/mmaitre314/picklescan |
| dropbox/bhakti | Keras and TensorFlow model checks (Table 6) | Apache-2.0 | https://github.com/dropbox/bhakti |
| Hugging Face pickle scanning | hosted scanning on the Hub: ClamAV plus a listing of a pickle's imports (Table 6) | service | https://huggingface.co/docs/hub/security-pickle |

The Zenodo archive holds live malicious code; it was not downloaded for this record.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this document |

## Limits

- **A floor, not a rate.** One hub, one enterprise mirror, three months, and repositories
  with restricted access excluded (§5.1, §6).
- **Proofs of concept are in the count.** The manual review judged some flagged code to be
  harmless researcher demonstrations, and Figure 4 keeps them as a category beside remote
  control and information theft. The text does not give the split.
- **Static analysis with a hand-made list.** The unsafe-API list comes from Pyre, Semgrep and
  Pysa rules and may miss exploits. No obfuscated model was seen, but the authors cannot rule
  one out (§6). TensorFlow models with risky operators are only flagged, so some may be false
  positives (§4.2, §6).
- **No precision or recall.** There is no ground-truth set. The comparison with Fickling,
  ModelScan and the rest is a feature table (Table 6), not a measured detection rate.
- **The format verdicts date from 2024 and cover code execution on load.** Table 2 rates GGUF
  and ONNX as not vulnerable, as far as was known then. A GGUF file still carries a chat
  template, a Jinja2 program that runs on every inference call, and RPT-0014 records a 2025
  demonstration of backdoors planted that way (INC-094, AIT-031).
- **The dataset-script vector has narrowed.** Hugging Face's datasets 4.0.0 (2025-07-09)
  removed loading scripts altogether. Environments pinned to older versions are not covered by
  that change.
- **Preprint, not the version of record.** arXiv v1 was read; the ACM version was not
  compared.

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | core | AIT-028, AIT-043 | Measures both in the wild: 91 malicious models (76 pickle variants, 15 Keras Lambda layers) and 9 malicious dataset loading scripts among 705,991 models and 176,386 datasets, published between March 2022 and June 2024 (§5.2). Payloads include reverse shells, a Chrome credential stealer and system reconnaissance (§5.4). The reverse shell in star23/baller10 resembles the baller423/goober2 model that JFrog reported (INC-046). Account takeover with leaked tokens and re-registering abandoned names appear only as one-sentence assumptions in the threat model (§2.2), so AIT-036 is not linked |
| Existing AI threat models | adjacent | none | §2.2 is a threat model for code poisoning on model hubs: two attack vectors, users' trust in popular hubs and contributors, and attacker routes to borrowed trust. threat-models.md does not list it |
| Weakness enumerations | adjacent | CWE-502, CWE-94, AML.T0011.000, AML.T0010.003, AML.T0010.002, AML.T0115.001, AML.T0115.000, AML.T0018.002, LLM03:2025, ASI04:2026 | Its tables form a small enumeration with no external ids: 15 model formats rated for code injection (Table 2), unsafe Python APIs (Table 3) and unsafe pickle opcodes (Table 4). Neither NIST AI 100-2e2025 nor ATLAS 2026.09 cites it (searched 2026-11-01). The CWE ids are RPT-0014's crosswalk for unsafe model deserialization (enumerations.md); the ATLAS and OWASP ids are its mapping in sources.md |
| Attack → asset mapping | core | C04, C02, C14, C03, C05 | Places the malicious code by artifact: model files in a hub or an enterprise mirror of it (C04) and dataset loading scripts (C02). The code runs wherever the artifact is loaded: a developer's machine (C14) or a training or inference job (C03, C05) (§1, §2.2). The payloads target hosts and secrets (A10, A09) |
