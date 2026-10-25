---
schema: "library-summary/v1"
id: mulval
record: mulval
type: summary
updated: "2026-10-25"
---

# MulVAL: A Logic-based Network Security Analyzer (Ou, Govindavajhala, Appel — USENIX Security 2005)

|  |  |
|---|---|
| **Type** | paper (white-paper) |
| **Authors** | Xinming Ou, Sudhakar Govindavajhala, Andrew W. Appel (Princeton) |
| **Published** | 14th USENIX Security Symposium, 2005 |
| **Source** | https://www.usenix.org/legacy/event/sec05/tech/full_papers/ou/ou.pdf |
| **Digest** | `a3007a72146d7d3413fb48dc5cf8908c4e5b4bbf6e858b007b0254a103fa5958` (16 pp) |

## Overview

MulVAL does multi-host, multi-stage vulnerability analysis by writing everything as **Datalog** (abstract; §2):
- vulnerability advisories, taken from OVAL scanner output and the ICAT database (§3);
- host and network configuration, including host access-control lists;
- principals;
- **interaction rules**, which say what an attacker gains from exploiting a vulnerability class, e.g. remote exploit → code execution as the service's privilege (§4);
- a **policy** of who may access what.

The XSB engine evaluates the rules. Any derivable access that the policy does not allow is a violation. The paper prints the derivation trace and shows it as an attack tree (Appendix A, Fig. 4). §6 covers **hypothetical analysis**: assume an unknown bug in a given program and ask what an attacker could then reach. The authors report that the framework reasons about 84% of the Red Hat bugs in OVAL (abstract). The analysis engine took 15.8 s for a 2000-host synthetic network (§7 table). The scanner itself took 236 s per host, run in parallel.

## Applicability to tmodel

| Axis | Rating | Why |
|---|---|---|
| Security | core | The canonical rule-based attack-graph generator. |
| Cryptography | adjacent | — |
| This project | core | The reference model for deriving `AttackPath`s from facts + rules, with a derivation trace as the reviewable artifact. |

Bears on **DEC-001** (AND/OR `gate` on AttackSteps mirrors MulVAL's rule bodies (AND) and alternative rules (OR)) and **DEC-005**.

**Implications for tmodel (inference).** (1) MulVAL's "consequence of a vulnerability class" rules are the missing piece in a pure CVE→CWE→CAPEC→ATT&CK walk (`bron`, `capec`), which says *what kind* of attack but not *what the attacker gains on this host*. tmodel needs a small, reviewed rule set of this kind to turn generic threats into product paths (DEC-009). (2) The derivation trace is a natural `Assertion` provenance chain: every derived step cites the facts and rule it came from. (3) Hypothetical analysis (§6) matches tmodel's need to model unknown or unpublished weaknesses in a component.

## Implementations

`risksense/mulval` on GitHub (licence shown as "Other"; last push 2023-01). Other forks were not surveyed.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata; PDF digest and page count |
| `summary.md` | this summary |

## Limits

- 2005 paper: OVAL/ICAT inputs are historical (ICAT became NVD). The performance numbers are for 2005 hardware.
- The paper's network model is host and service reachability. It has no notion of software supply chain or component-level structure.
- Read the abstract and §§2–4, 6–7. The §8 discussion and related work were skimmed.
