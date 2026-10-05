---
schema: "library-summary/v1"
id: nist-sp-800-218
record: nist-sp-800-218
type: summary
updated: "2026-10-05"
---

# NIST SSDF (SP 800-218 v1.1) — summary

The **Secure Software Development Framework**: NIST's outcome-based, SDLC-agnostic catalogue
of secure-development practices, grouped **PO / PS / PW / RV** (19 practices, ~40 live tasks).
It is the reference against which other SDLs are mapped (MAP-0001). For tmodel it supplies the
canonical **"perform threat modeling" requirement (PW.1.1)**, plus SBOM/provenance (PW.4, PS.3.2),
code review/testing (PW.7/PW.8) and vulnerability response (RV.1–3).

No certification scheme — conformance is self-attestation via federal procurement (EO 14028/OMB),
not part of the SP. Companion profile **SP 800-218A** augments it for generative-AI/dual-use models.
SSDF **v1.2** (SP 800-218r1) is in draft (not final as of 2026-10-05).

Distilled: `distilled/requirements.yaml` (practices/tasks with Practice.Task locators),
`distilled/normative.md` (structure + conformance). FX-1 verbatim verify pending (T-029).
