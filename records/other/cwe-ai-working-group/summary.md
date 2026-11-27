---
schema: "library-summary/v1"
id: cwe-ai-working-group
record: cwe-ai-working-group
type: summary
updated: "2026-11-20"
lane: catalogs-schema
reviewed_by: ""
---

# CWE AI Working Group

|  |  |
|---|---|
| **Type** | repo (meeting minutes and slides; no code) |
| **Maturity** | _unset — do not guess_ (working-group records, not CWE content) |
| **Authors** | CWE Program (MITRE) and the CWE AI Working Group, led by MITRE's CWE team with community co-leads |
| **Published** | repository created 2024-07-12; latest minutes 2026-06-12, latest slides 2026-06-26; read at commit `c34115ac` (2026-07-07) |
| **Identifier** | https://github.com/CWE-CAPEC/AI-Working-Group |
| **Source** | `meeting_minutes/20260612-CWE-AI-Working-Group-Meeting-Minutes.pdf` at that commit |
| **Digest** | `1f61c8ec00a38762329c7c7e0bdf441b952dc517eae23c58a2beee92c99815cf` (minutes, 6 pages); slides of 2026-06-26 `92cfd2ac…` |

## Overview

The working group is a forum of CWE and CVE stakeholders. Its stated mission is "to identify and address gaps in the CWE corpus where AI-related weaknesses are not adequately covered". The repository holds its minutes and slides from May 2024 to June 2026: 37 minutes files and 41 slide decks. It has two subgroups: one improves existing CWE content for AI systems, and one drafts new entries.

**The pipeline in June 2026.** The 2026-06-12 minutes count nine AI-specific submissions, seven of them proposing new entries. CWE's lead expected most to end as changes to existing entries instead. The 2026-06-26 slides list ten.
- **Proposed new entries:**
  - improper isolation of task-relevant context (RAND, CDR #204);
  - improper isolation of executable logic in AI/ML workflow definitions (#183);
  - improper neutralization of reserved special tokens in AI instruction streams (Sentry, #173);
  - improper control of learned representation stability (Cloud Security Alliance, #179);
  - bypass of human authorization controls (Kodem Security, #174). CWE plans a more general "lack of human in the loop" entry instead.
- **Likely changes to existing entries:**
  - cross-model scripting, as an example under CWE-79 (#180);
  - neutralization of MCP client configurations (#158);
  - neutralization of retrieved content in RAG prompts (#161).
- **Deprioritized:** "Insufficient Input Validation in Generative AI Applications" (proposed for decline) and "Bias in AI Models", whose security relevance the group questioned.

**How CWE frames AI submissions** (slide 6): "Most/all AI-related submissions are too low-level to have their own entry", and "CWE doesn't make separate entries for 'where the bad input came from'". So prompt injection will not be split by channel. The minutes also record the CWE lead's view on outputs: a model's incorrect output is a weakness when it guides security decisions or downstream behaviour, whatever the intent, as with package hallucination. They also note that CVSS discussions declined to score output manipulation alone. The group was reviewing RAND's draft criteria for which AI issues belong in CVE and CWE, which is not yet published.

**What CWE 5.0 delivered.** The slides said "CWE 5.0 to be released in October", with "support for AI-specific lifecycles" and a "goal: significant increase in AI coverage". CWE 5.0 shipped dated 2026-10-28, checked against MITRE's `cwec_v5.0.xml.zip`:
- **No new AI entry.** It adds 18 entries, all about sessions, credentials, parsing or hardware. The AI-specific weaknesses are still CWE-1039, 1426, 1427 and 1434.
- **AI life-cycle phases.** A new `Custom_Phase` with `Domain="AI"` gives those four entries "Data Collection", "Training", "Fine-tuning" and "Prompting" as modes of introduction.
- **A new format.** It is written to CWE schema 8 (namespace `cwe-8`), which replaces the Categories with Groupings.

On 2026-11-20, every AI-labelled submission in the content development repository is still open except #109 (closed), and #207 and #208 were filed after June.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | core | Decides which AI weaknesses get stable CWE ids, and on what principle others are refused |
| Cryptography | none | No cryptographic content |
| This project | adjacent | It decides whether tmodel's Weakness nodes for AI attacks can point to CWE ids or need local entries (**DEC-001**, **DEC-008**). With CWE 5.0 adding none, the candidate local weaknesses in `enumerations.md` §5 still have no CWE to supersede them |

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | adjacent | AIT-069, AIT-093, AIT-039, AIT-064 | AIT-069 (special-token role forgery) and AIT-093 (human-approval bypass) cite it. The workflow-definition and RAG submissions (#183, #161) are the weakness side of AIT-039 and AIT-064. It describes no attacks of its own |
| Existing AI threat models | none | — | No system model |
| Weakness enumerations | core | CWE-1039, CWE-1426, CWE-1427, CWE-1434, CWE-1448 (view); CDR #73, #109, #158, #161, #173, #174, #179, #180, #183, #204 | `enumerations.md`'s "9 AI submissions, 7 proposing new entries" matches the 2026-06-12 minutes. The 2026-06-26 slides add #204, making ten. **Report §6 and §7 call CWE 5.0 "pending" with more AI entries: 5.0 shipped on 2026-10-28 with none**, only AI life-cycle phases on the existing four. LW-005 tracks #174, which is still open |
| Attack → asset mapping | adjacent | C05, C06, C09, C12, C15 | The submissions sit on tokenizer and inference input (C05: #173, #179), RAG prompt assembly (C06: #161), MCP clients (C09: #158), human approvers (C12: #174) and workflow platforms (C15: #183). The mapping is ours |

## Implementations

None, searched 2026-11-20: the repository holds documents, not code. CWE content itself is the `cwe` record.

| Name | Kind | License | URL |
|---|---|---|---|

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, digest, commit and `cites` |
| `summary.md` | this summary, with the RPT-0014 applicability table |

## Reference expansion

The June slides and minutes cite three things, checked against `sources.md` and the library on 2026-11-20:
- **Missing, added as a stub (1):** the CWE Content Development Repository, `cwe-content-development-repository`. Each AI submission is an issue there, labelled `related-to-ai`.
- **In `sources.md` (1):** the CVE AI Working Group (S-0838), whose CVSS and CVE positions the minutes cite.
- **Not stubbed (1):** RAND's draft inclusion-criteria paper, which is unpublished. No copy was found.

## Limits

- **Minutes, not decisions.** The 2026-06-12 minutes say "No final decisions made", and they were drafted with Microsoft Teams Copilot, then edited by the CWE team. A proposal listed here is not CWE content until a release carries it.
- **Stops in June 2026.** Nothing after the 2026-06-26 slides is in the repository, so how the group judged CWE 5.0 isn't recorded. The 5.0 facts above come from MITRE's release file, not from the group.
- **Who submits shapes the list.** The proposals come from vendors and researchers who chose to file them, so they don't systematically cover AI attack classes. Poisoning, extraction and membership inference have no submission.
- **Names change as they're reviewed.** #179 is titled "Unstable Internal Model Representations …" on the slides and "Improper Control of Learned Representation Stability" in its description.
