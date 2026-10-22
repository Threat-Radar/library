---
record: cisa-ai-in-ot-principles
kind: examples
title: "cisa-ai-in-ot-principles — examples and test vectors"
extracted: "2026-10-21"
reviewed_by: ""
---

# Examples

The guidance has two worked examples. Both are kept whole and verbatim (cut from the capture by
text block), with the requirement ids they exercise. Neither has an expected result in the
source: they are reference cases, not tests with an outcome, and each file says so under
`expected_result`. There are no test vectors.

| file | source | what it is | expected result |
|---|---|---|---|
| `business-case-predictive-maintenance.yaml` | §2.1, pp. 11–12 | a fictional assessment of AI for predictive maintenance of an industrial generator: use case, problem, goal, risk, stakeholders, requirements, safety and security requirements, success metrics | none stated. `derived_checks` (ours) turns its five numeric thresholds into machine-checkable targets |
| `monitoring-predictive-maintenance.yaml` | §4.1, p. 19 | how operators and engineers should monitor an ML predictive maintenance system with read-only access to OT data: six monitoring elements | none stated; each element is also a requirement (R-0098 … R-0104) |

Use in tmodel: the first is a fixture for a concept-phase business-case record (DEC-001b) and for
ADR-0006 inputs; the second for a model with one `machine_learning_model` component in a data zone
and its monitoring mitigations (tmodel#130).
