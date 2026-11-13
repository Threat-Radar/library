---
record: iso-sae-21434-2021
kind: examples
title: "iso-sae-21434-2021: annex data, the worked TARA, and test vectors"
extracted: "2026-11-13"
reviewed_by: ""
---

# ISO/SAE 21434:2021 examples and test vectors

ISO/SAE 21434 is a licensed standard. Nothing here copies its text: every description is our own
wording, and only labels, ratings, point values, ranges and the order of steps are carried as
data, with the annex content held as structured fields (actor, action, target; level, access,
typical case) rather than as sentences, each with its clause, table or figure locator (sponsor
decision: tmodel#69 sponsor note, hold 1 (2026-10-02); tmodel#154). Read from the purchased PDF,
SHA-256 `73f990078d3a5b47dec91dd0d2b4e6c24cecd9e4160ae5b143c3b3fa80b7cdf4` (87 pages), through
`pdftotext -layout`, with the figures and merged-cell tables read from the rendered pages.

| file | what it holds | source |
|---|---|---|
| `annex-e-cal.yaml` | the CAL idea, Figure E.1's story, the CAL table, rigour per CAL, the concept and development rules, independence and testing per CAL | Annex E, Tables E.1 to E.4, Figure E.1 |
| `annex-f-impact.yaml` | impact criteria per category and level | Annex F, Tables F.1 to F.4 |
| `annex-g-feasibility.yaml` | the five attack-potential factors with their levels and values, the sum-to-rating bands, the CVSS exploitability formula and bands, the attack-vector ratings | Annex G, Tables G.1 to G.9 |
| `annex-h-headlamp-tara.yaml` | the worked concept-phase TARA: item, environment, assets, damage and threat scenarios, attack paths, both feasibility ratings, risk matrix and formula, risk values, treatment, and seven inconsistencies and three caveats inside the annex | Annex H, Tables H.1 to H.11, Figures H.1 to H.3 |
| `expected.yaml` | 59 test vectors with their expected results, worked out by hand | Annexes E, G and H |
| `run-fixtures.derived.py` | recomputes every vector from the annex files and fails on any difference | ours |

`python3 -I records/iso/iso-sae-21434-2021/distilled/examples/run-fixtures.derived.py` from the
repository root prints `all 108 checks pass`. It needs PyYAML (`requirements-dev.txt`).

**What the vectors show.** The Table H.8 matrix and the Table H.10 formula agree in 12 of the 16
cells when the formula is left unrounded; the annex only claims agreement for its two threat
scenarios, which holds. The attack-potential rating of Table H.7 comes out the same when
recomputed from Table G.6 and Table G.7, and Table H.9's aggregated feasibility is the worst
path of each threat scenario. The CVSS vectors use CVSS v3.1's per-metric values (library record
`first-cvss-v3-1`), since Annex G gives only their ranges.

## Not carried as fixtures

- **The EXAMPLE notes in the body.** Clauses 3 to 15 hold 55 EXAMPLE notes (clause 3: 7,
  clause 5: 15, clause 6: 6, clause 7: 4, clause 8: 5, clause 9: 1, clause 10: 6, clause 12: 2,
  clause 13: 1, clause 15: 8). They illustrate a provision in a sentence or a list and carry
  nothing a test could run; restating them would mostly copy the standard. The provisions they
  illustrate are in `requirements.yaml`.
- **The EXAMPLE notes inside the annexes** (26: Annex D 5, folded into `normative.md` §5.4; Annex F
  3 and Annex G 18, folded into the annex files above as typical cases).
- **Annexes A to D** hold no computable example: A is a table of subclauses and work products,
  B contrasts weak and strong cybersecurity culture, C is an empty interface-agreement
  template, and D is a decision diagram. `normative.md` §5 covers all four.
