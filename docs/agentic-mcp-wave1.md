---
schema: "library-doc/v1"
id: agentic-mcp-wave1
title: "Agentic/MCP WAVE 1 bibliography completion (#78)"
type: assessment
status: draft
version: "0.1.1"
updated: "2026-11-26"
needs_review: true
reviewed: false
---

# Agentic/MCP WAVE 1 bibliography

Part of [tmodel#78](https://github.com/Threat-Radar/tmodel/issues/78).
This completes the bounded bibliography pass in
[LANES.md](https://github.com/Threat-Radar/tmodel/blob/main/research/0014-ai-threat-model/LANES.md),
not the extraction lane. New metadata and applicability additions are research
proposals awaiting review. No human review or `reviewed_by` signature is added here.

## Delivered and retained

- All 20 assigned subset-1 sources resolve to distinct library records: 19 from
  merged [library#22](https://github.com/Threat-Radar/library/pull/22), plus the
  previously existing `cisa-ai-in-ot-principles` record. Every source now has the
  six summary sections, three applicability axes and four RPT-0014 topic rows.
- The 14 AI subject tags actually used by this lane are promoted into
  `schema/tags.yaml`. Shelf labels are removed from the 19 lane-authored tag
  lists; the two OWASP records gain the semantic role `prior-art`. The reused
  CISA record keeps its existing topic, tags and extracted material.
- The first-hop reference pass records 147 distinct cited works in 190 source
  citation edges: nine held records, 59 works already in the source corpus,
  77 new `status: stub` records and two works whose canonical records are
  proposed in [library#51](https://github.com/Threat-Radar/library/pull/51).
  Corpus and pending works remain `{title, locator}` frontier entries while
  the library does not hold them.
- `topics/ai-threat-model-agentic-mcp.yaml` names @paria03 and groups the 20
  assigned sources and 77 new stubs (97 members). It stays open because the lane has later work.

The machine-readable evidence is [sources.csv](agentic-mcp-wave1/sources.csv)
(20 assignment rows) and [references.csv](agentic-mcp-wave1/references.csv)
(190 edges with a source-side locator, disposition and target identity).
The cited titles are bibliographic metadata, not a new summary of the cited works.

## Scope and decisions

The pass follows one hop from the assigned sources. It keeps agent/MCP threats,
prompt-injection and multimodal instruction attacks, concrete defenses and
benchmarks, and agent governance or authorization controls. It does not recurse
through the new stubs. Generic model architectures, prompting tutorials,
optimization methods, broad social/economic or military AI policy, OT safety
standards, and ordinary application/UI documentation are outside this lane's
reference expansion. The vision-language survey's general evasion, training and
data-poisoning bibliography belongs to the other research lanes; its instruction
injection and agent-related papers are included here.

The Google AI Overviews post and Lenovo incident report have no additional
technical security reference in this scope; their product, satire, marketing and
general-news links are not new security-library records. The OWASP MCP Top 10
landing page links its own ten category sections; those are parts of the same
catalog, not ten new works. CISA's security-resource citations already have
library records or source-corpus entries; its existing citation list is retained.
Its unrelated ICS-access, functional-safety and basic LLM-settings references
do not create agentic/MCP stubs.

`cites` records the actual document references. Reverse library `cited_by`
links were removed following review: `docs/references.md` reserves that field
for project documents, and inverse citation views are derived. No `see_also`
relation is promoted into a citation. The companion tmodel change corrects
WAVE 1 Step 2.5's conflicting instruction.

## Review corrections and cross-lane identities

The [review on library#53](https://github.com/Threat-Radar/library/pull/53)
identified an incorrect identity for Habler et al. [4]. It cites the
[OWASP Multi-Agentic System Threat Modeling Guide v1.0](https://genai.owasp.org/resource/multi-agentic-system-threat-modeling-guide-v1-0/),
not *Agentic AI: Threats and Mitigations*. The guide is source-corpus S-0761,
not a held library record. The source's generic OWASP locator is preserved;
the citation now uses an unresolved title/locator instead of the wrong record.
This restores 147 distinct works: nine held identities, 59 corpus works,
77 new stubs and two pending records. The former 10-held count was wrong.

Fifteen ids introduced only by this unmerged PR were corrected before becoming
permanent: 14 overlong or truncated slugs now use short, complete identities,
and `chainguard` becomes `lakera-chainguard` to identify the cited Lakera tool.
The Gemini CLI id retains issue number **2106** in full. Full titles, content
URLs, hashes and prior review evidence are unchanged. The mapping is
[record-id-changes.csv](agentic-mcp-wave1/record-id-changes.csv).

Two papers also proposed in library#51 are not added a second time here:

| arXiv | Pending canonical library id | Owning PR |
|---|---|---|
| 2305.13860 | `liu-2023-jailbreaking-chatgpt-prompt-engineering` | library#51 |
| 2306.08833 | `wang-2023-safeguarding-crowdsourcing-surveys-prompt-injection` | library#51 |

Their original citations remain title/locator frontier entries. The CSV records
`pending-library-pr`, `pending_library_record` and `pending_pr`; it does not
pretend those records exist. This avoids duplicate permanent ids, dangling
links and overlapping record edits in either merge order. The owning lane
retains its PDF pins, metadata and review responsibility. After #51 merges,
resolve these frontier entries to those ids in the normal bibliography pass;
until then they are explicitly pending. No other lane's records are changed.

## Source access and identity checks

Twelve original PDFs match the recorded SHA-256, including Khodayari v1 fetched
explicitly after its unversioned URL advanced to v2. Six current HTML captures
differ from their older hashes. Lenovo and Tracebit were inspected through the
publisher text in an indexed view because direct retrieval was blocked or a
browser challenge. These later views support only this reference-list pass:
they do not replace or reauthenticate the original captures. No original source
hash, publication version or review is overwritten.

New stub hashes identify the exact captured target landing page (HTML) or, for
NIST SP 800-207, the PDF returned by its DOI. They do not imply full paper reading.
Four targets were not retrieved and deliberately have no digest:
- `ai-agents-formal-security-guarantees`: access blocked / browser verification; identity retained from the citing document.
- `skillspector-prepublication-control`: access blocked / browser verification; identity retained from the citing document.
- `aim-curxecute-mcp-rce`: access blocked / browser verification; identity retained from the citing document.
- `lakera-chainguard`: 404 at the cited URL.

Other identity decisions:

- SkillSecurer's POISE citation resolves by arXiv 2606.07943 to the current title
  *One Skill, Two Masters*. The stub uses the verified current title and the audit
  retains the source's cited title. The same rule applies to the updated title of
  *Tricking LLMs into Disobedience*.
- SecGPT / IsolateGPT resolve to arXiv 2403.04960. Alternate titles do not create
  duplicate records. *Prompts Should Not Be Seen as Secrets* resolves to the
  corpus's *Effective Prompt Extraction*, S-0216.
- MCP Authorization revision 2025-11-25 is distinct from the corpus's 2025-06-18
  edition S-0854. The newly cited revision is kept explicitly, without replacing it.
- The Cursor FAQ and the two original research write-ups are different works;
  the latter are recorded separately rather than treating the FAQ as their identity.
- Jones et al. [5] gives a wrong arXiv number for WebArena; [18] supplies no
  verifiable locator for its claimed multimodal/tool-injection paper. Habler et al.
  [20] similarly gives no verifiable locator for its BeyondCorp/agent claim. These
  are source-quality caveats, not evidence to invent paper records. Generic
  benchmarks and unverifiable bibliographic claims are excluded from this pass.
- CWE-1426's actual bibliography entry REF-1445 is *Building Guardrails for
  Large Language Models*, arXiv 2402.01822. CVE example identifiers are catalog
  data, not additional bibliographic works.

## Review provenance and handoff

Calibration was delivered in merged [tmodel#117](https://github.com/Threat-Radar/tmodel/pull/117).
The existing independent five-record check by @kriishnaa-18 is recorded on
[library#22](https://github.com/Threat-Radar/library/pull/22#issuecomment-6355715327).
It covers that earlier change, not this new bibliography pass. No prior review is
copied into a fresh approval or signature. Request review of these new changes.

**Every new scaffold is owned by @paria03 in tmodel#78.** Its next source-reading
and applicability pass is explicit future work; full extraction belongs to #73
after the #84 gate. The stubs remain unread, low-confidence metadata and are not
attack paths, accepted claims, new risk ratings or a knowledge-graph load.

The sponsor's [#84 instruction](https://github.com/Threat-Radar/tmodel/issues/84)
keeps the lanes open until comparable calibration units are agreed. The six
WAVE 2 extraction units, reconciled verification files, review-partner signatures
and news sweep are not claimed complete here. A new PR should say **Part of #78**,
not **Closes #78**.

## Validation

Baseline: 686 records (381 written, 305 scaffold, 42 fully extracted), 24 topics,
0 errors and 99 warnings. After review corrections: 763 records (381 written, 382 scaffold,
42 fully extracted), 25 topics, 0 errors and the same 99 warnings. The 77-record
increase is exactly the requested bibliography stubs; it does not increase the
written or extracted counts. Generated views remain untracked.

An isolated trial merge with library#51 at `8fc3878` is conflict-free. Its
combined 1,045 records validate with zero errors and the same 99 warnings;
the two cross-lane arXiv duplicates no longer add warnings. No peer branch
is modified by this check.

Commands and cross-checks are recorded in the companion
[tmodel lane log, PR #271](https://github.com/Threat-Radar/tmodel/pull/271).
The prior library head `7390bfa` had no hosted runs: GitHub paused this fork's
Actions because of usage volume. Local validation is distinct from hosted CI;
a maintainer must restore Actions before a fresh hosted pass can be claimed.
