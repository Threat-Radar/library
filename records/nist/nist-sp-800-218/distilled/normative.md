---
schema: "library-normative/v1"
id: nist-sp-800-218-normative
record: nist-sp-800-218
type: normative
updated: "2026-10-05"
coverage: "Group structure (PO/PS/PW/RV), practice elements, recommendation-style stance, conformance/attestation model, v1.2 draft status, tmodel anchors."
reviewed_by: ""
---

# NIST SP 800-218 (SSDF v1.1) — normative structure

**Status note.** SSDF v1.1 (Feb 2022) is the current final version. SP 800-218 Rev.1
(SSDF **v1.2**) was an Initial Public Draft (17 Dec 2025, comments closed 30 Jan 2026) and
is **not final as of 2026-10-05**. Written in response to EO 14028 §4 (Appendix Table 2 maps
practices to the EO). Supersedes CSWP 13 (2020).

## Shape
- **4 practice groups** → **19 practices** → tasks:
  - **PO — Prepare the Organization** (PO.1–5)
  - **PS — Protect the Software** (PS.1–3)
  - **PW — Produce Well-Secured Software** (PW.1, PW.2, PW.4–9; PW.3 withdrawn)
  - **RV — Respond to Vulnerabilities** (RV.1–3)
- Each practice has four elements: **Practice, Tasks, Notional Implementation Examples,
  References**. Examples are explicitly **not required**. References map to BSIMM, BSAFSS,
  SP 800-160, OWASP ASVS and others.

## Normative stance
- Recommendation-style: the document uses **no "shall"**; tasks are "recommended practices"
  with an implicit actor "the organization". When writing requirements, treat the verb as
  **should/recommended**. Terms like "well-secured", "sensitive data", "qualified person" are
  left for the adopting organization to define.

## Conformance
- **No certification, no tiers, no assessment regime** in the SP itself. It states the
  practices are "only a subset of what an organization may need to do."
- Attestation appears only in the **acquirer/supplier** context (PO.1.3; provider-attests
  passages). **Self-attestation is a federal-procurement mechanism** (EO 14028 / OMB forms),
  **outside** SP 800-218.

## Anchors for tmodel
- **PW.1.1** = perform threat/attack/attack-surface modeling (the SDL threat-modeling requirement).
- **PW.4.x / PS.3.2** = third-party components + provenance/SBOM.
- **PW.7 / PW.8** = code review/SAST + executable testing.
- **RV.1–3** = vulnerability identification, response, root-cause.
These map onto the SDL `Gate` exit-criteria and the `Requirement` crosswalk (MAP-0001, R-044).
