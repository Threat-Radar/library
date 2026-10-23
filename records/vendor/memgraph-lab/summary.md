---
schema: "library-summary/v1"
id: memgraph-lab
record: memgraph-lab
type: summary
updated: "2026-10-14"
---

# Memgraph Lab documentation

## Overview

Memgraph Lab 3.x is a browser workbench for querying, visualizing, styling, and inspecting
Memgraph property graphs. Official sources document graph/query split views, Graph Style
Script, expand/collapse, configurable render limits, query collections, and GraphChat with
generated-query context and response feedback.

## Evidence used by RPT-0006

- Product page: https://memgraph.com/lab
- Graph Style Script: https://memgraph.com/docs/memgraph-lab/features/graph-style-script
- Release notes: https://memgraph.com/docs/release-notes
- Legal and license families: https://memgraph.com/legal
- Repository context: https://github.com/memgraph/memgraph

## Applicability

Product precedent for Issue #10 query/graph views, visual weighting, expansion, and
LLM-assisted querying. It informs DEC-006, R-014, and R-018 without accepting a decision.

## Limits

GraphChat feedback is not evidence of an AI graph-change accept/reject workflow. Practical
display limits, embedding terms, and threat-specific path interaction remain unresolved;
Memgraph Lab is coupled to the Memgraph database product.
