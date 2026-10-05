---
schema: "library-summary/v1"
id: slsa-v1-0
record: slsa-v1-0
type: summary
updated: "2026-10-05"
---

# SLSA v1.0 (Build track) — summary

Supply-chain provenance levels **L0-L3** (provenance exists -> signed by a hosted platform ->
hardened/isolated build + protected signing keys), with provenance as an **in-toto attestation**
that consumers verify against expectations. No central certification. Feeds radar->tmodel build
provenance (ADR-0001) and the conformance **evidence** mechanism (R-042).

**Summarized** (WebFetch summary-grade): requirement names are paraphrased; the Hosted level and
the in-toto predicate detail are unverified; v1.0 is **retired/superseded by v1.2**. FX-1 verbatim
verify pending (T-029): raw-fetch /levels, /requirements, /provenance, /threats.
