---
schema: "library-doc/v1"
id: agentic-mcp-wave1
title: "Agentic/MCP WAVE 1 bibliography completion (#78)"
type: assessment
status: draft
version: "0.1.2"
updated: "2026-11-28"
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
  citation edges: 12 held records, 58 works already in the source corpus and
  77 new `status: stub` records. Three frontier citations now resolve to records
  delivered in merged [library#51](https://github.com/Threat-Radar/library/pull/51).
  Corpus works remain `{title, locator}` frontier entries while the library does
  not hold them. No citation is waiting on another PR.
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
That review restored 147 distinct works: nine held identities, 59 corpus
works, 77 new stubs and two pending records. The former 10-held count was wrong.
The later merged-reference resolution below changes their dispositions, not the
147-work or 190-edge totals.

Fifteen ids introduced only by this unmerged PR were corrected before becoming
permanent: 14 overlong or truncated slugs now use short, complete identities,
and `chainguard` becomes `lakera-chainguard` to identify the cited Lakera tool.
The Gemini CLI id retains issue number **2106** in full. Full titles, content
URLs, hashes and prior review evidence are unchanged. The mapping is
[record-id-changes.csv](agentic-mcp-wave1/record-id-changes.csv).

Two papers also proposed in library#51 are not added a second time here:

| arXiv | Canonical library id | Owning PR |
|---|---|---|
| 2305.13860 | `liu-2023-jailbreaking-chatgpt-prompt-engineering` | library#51 |
| 2306.08833 | `wang-2023-safeguarding-crowdsourcing-surveys-prompt-injection` | library#51 |

They were deliberately retained as title/locator frontier entries until #51
merged, avoiding duplicate permanent ids and dangling references in either
merge order. On 2026-11-28, after #51 merged, the two citations were resolved
to its canonical ids. The newly held Brundage report, arXiv 1802.07228
(`brundage-2018-malicious-use-ai`, source-corpus S-0726), also resolves from
Liu's survey to the merged record. Each identity matches the cited arXiv id.

The CSV now classifies all three as `held`, preserves the original cited title,
URL, source-side locator and any corpus id, and clears the two pending fields.
Current totals are 12 held works, 58 corpus works and 77 new stubs, with no
pending PR references. No canonical target record, PDF pin, source metadata or
review is edited. These are citation links, not evidence of reading the targets.

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
copied into a fresh approval or signature. @Clovier approved the bibliography
changes at `4dc474e` on library#53.
The later merged-reference cleanup requires review on its new head.

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

The original pass started from 686 records; the reviewed `4dc474e` head held
763 records. After merging library `main` at `c4cab52` for this follow-up, the
combined tree holds 1,045 records (404 written, 641 scaffold, 42 fully extracted),
25 topics, zero errors and the same 99 warnings. The PR still adds exactly
77 unread stubs relative to current `main`; the other increase comes from merged
work in other lanes. The 20 assigned sources and all 190 citation edges reconcile.

Local CI steps passed: 15 YAML reader tests, 53 requirements files,
181 artifact files (zero errors; 38 existing warnings), export/reindex,
1,045 bibliography entries, the extraction gate and the third-party-document
check. All 20 source assignments, summary sections, applicability ratings,
controlled tags, 190 forward citations, 77 owned stubs and 97 topic members
reconcile. Source metadata, digests and reviews remain unchanged. The companion
tmodel#271 passes its architecture check (29 documents, zero errors). Generated
views remain untracked.

GitHub Actions were restored on 2026-11-27 in
[tmodel#283](https://github.com/Threat-Radar/tmodel/issues/283); library#55 passed
both `validate` and `dco`. At the start of this follow-up, the old library#53
head `4dc474e` had no hosted results. Check the latest exact-head results on
[library#53](https://github.com/Threat-Radar/library/pull/53) and
[tmodel#271](https://github.com/Threat-Radar/tmodel/pull/271); do not inherit CI
success from an earlier commit. Both require fresh passing checks before merge;
tmodel#271 follows the library merge.

## Completion boundaries

| Work | Status / next owner |
|---|---|
| Three calibration sources | Merged in tmodel#117 |
| 20 assigned bibliography records | Original summaries merged in library#22; tag/applicability/reference cleanup in library#53 |
| Controlled tags, applicability, citation stubs and lane note | Implemented; library#53 and companion tmodel#271; merge after current-head checks/review |
| Pending-reference resolution | Implemented: three links, zero pending records |
| Five-source human signatures | @kriishnaa-18, [tmodel#284](https://github.com/Threat-Radar/tmodel/issues/284); the earlier fixes are present, but no `reviewed_by` signature exists yet |
| Review-partner duty for catalogs/schema | @paria03 completed [tmodel#285](https://github.com/Threat-Radar/tmodel/issues/285) |
| Comparable calibration / extraction gate | @nymble, tmodel#84; still open |
| WAVE 2 extraction and news sweep | Deferred until the #84 gate; not claimed complete |

Merge library#53, then tmodel#271 after fresh checks and review. Check the last
WAVE 1 bibliography criterion on #78 only after merge, linking the evidence.
Keep #78 open for its sponsor gate and remaining review requirements. Another
reviewer's signature must come from that reviewer; approval of a PR does not
replace the five-source sign-off.
