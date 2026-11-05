---
schema: "library-doc/v1"
id: requirements
title: "What is a requirement"
type: policy
status: draft
version: "0.3.0"
updated: "2026-11-05"
needs_review: true
reviewed: false
source: "sponsor question 2026-09-22: what is a requirement?"
---

# What is a requirement

**Status: draft. Open for review.** Governs `records/<body>/<id>/requirements/`.

> **Formal schema (new).** This prose is the human spec; the **machine schema** is
> now `schema/requirements.linkml.yaml` (`library_requirements` v3, LinkML — an
> open IDL owned by the library). It formalizes the de-facto `library-requirements/v2`
> shape that 41 records already use: the four mandatory parts (verb/actor/condition/
> locator), verbatim `text`, the `<record>#<designator>` id, the polymorphic
> `maps_to` crosswalk with MAP-0001 provenance, and OPTIONAL provenance-bearing
> `applies_to`/`satisfied_by` edges to products/organizations/projects/procedures in
> a consuming KG (targets are opaque — the dependency points consumer→library, never
> the reverse). A documented v2→v3 migration and ten open questions ship with the
> schema PR; cross-field invariants (count reconciliation, "inferred needs a reason",
> "ours mapping needs a rationale") stay in `bin/validate`, not generated SHACL.
> The schema describes the NORMALIZED v3 shape; the 44 files stay raw v2 and are
> bridged by a normalization loader. See `docs/requirements-schema.md` for the
> loader, the v2→v3 transforms, and the `bin/check-requirements` acceptance gate.

## 1. Definition

> A **requirement** is a statement in a source document that constrains what a
> conforming implementation may do, expressed with a normative verb, attributed
> to an actor, and traceable to an exact locator.

Four parts, all mandatory. Missing any one and it is not a requirement:

| Part | Test |
|---|---|
| **Normative verb** | MUST, MUST NOT, SHALL, SHALL NOT, SHOULD, SHOULD NOT, MAY, REQUIRED, RECOMMENDED, OPTIONAL — [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119.html) as updated by [RFC 8174](https://www.rfc-editor.org/rfc/rfc8174.html) |
| **Actor** | *who* must do it — verifier, issuer, transparency service, implementation |
| **Condition** | when it applies; unconditional is a valid condition, stated as such |
| **Locator** | section or clause. Not a page number — pages do not survive conversion |

## 2. What is not a requirement

- **Description.** "The Transparency Service maintains an append-only log" states
  a fact about a design, not an obligation. Common and easy to misfile.
- **Motivation and rationale.** "This avoids a round trip" explains; it does not
  constrain.
- **Examples**, unless the example text itself carries a normative verb.
- **Lowercase modals.** RFC 8174 is explicit: only *capitalised* keywords carry
  normative force. "should be careful" is advice.
- **Our own conclusions.** A thing we decided is an `R-*` in ARCH-0001, not an
  extracted requirement. Keep the direction of travel straight: requirements are
  extracted *from sources*; our requirements are *authored*.

## 3. Shape

`requirements/<set>.yaml`:

```yaml
schema: "library-requirements/v1"
record: rfc-9943
source_version: "2026-06"
extracted: 2026-09-22
extracted_by: agent            # or a person
reviewed_by: ""                # REQUIRED before this set is used
requirements:
  - id: rfc-9943-R-012
    verb: MUST
    actor: transparency-service
    condition: "on registering a Signed Statement"
    text: "The Transparency Service MUST perform signature verification."
    locator: "§4.2"
    kind: stated                # stated | inferred
    testable: yes               # yes | no | partial
    notes: ""
```

Rules:

- **`text` is verbatim** — except for licensed standards (§3a). Never paraphrase
  a normative sentence from a source we may quote — paraphrase is how a MUST
  silently becomes a SHOULD.
- **`kind: inferred` for anything the document implies but does not state**, and
  it must say so in `notes`. **An invented MUST is a defect that propagates into
  our own specification**, which is the whole reason this file exists.
- **`testable: no` is a finding**, not a failure. A requirement nobody can test
  is worth recording precisely because it cannot be checked.
- **Extraction comes from `distilled.md`, never from `summary.md`** — and
  `distilled.md` comes from the source. Two hops from the source is where drift
  starts.
- **`reviewed_by` empty means unusable.** An unreviewed extraction may be read,
  but nothing may be built on it.

## 3a. Exception: licensed standards are paraphrased, never quoted

Some sources may not be republished. ISO, IEC, ISO/SAE and other paywalled or
all-rights-reserved standards forbid posting their text without permission, and
this library is public. For those sources the verbatim rule is reversed
(sponsor decision, tmodel#38 Q3, 2026-10-19; first applied in tmodel#154):

- **`text` MUST be our own paraphrase.** Never copy the standard's wording into
  any file, issue, PR or commit message. Short defined terms and names (*item*,
  *cybersecurity goal*, *attack feasibility*, the levels of a rating scale) may be
  used as names; sentences may not.
- **Mark it.** The set header carries `text_origin: paraphrase` and a
  `licensed_text` note naming the decision; an entry may repeat
  `text_origin: paraphrase`.
- **Keep the anchors beside the paraphrase**, so drift is visible: designator or
  tag, `normativity`, `verb`, `locator`, and the set's `source_digest` of the
  bytes that were read. **`verb` is authoritative for force**: the paraphrase
  states the same modal (shall stays shall, should stays should, may stays may)
  and must not soften or harden it.
- **Preserve meaning, not words**: the actor, the condition, the action, the
  objects and every list item. A paraphrase that drops a list item is a defect,
  as a truncated quote is.
- **Never invent to fill a gap.** If the text we extracted is cut off or wrong,
  paraphrase only the intact part, or leave a placeholder, and flag the entry
  (`audit_status: text-defect-needs-licensed-copy` plus `notes`) until someone
  with a licensed copy checks it.
- **Free and public sources stay verbatim**: IETF, W3C, NIST, CISA, EU law,
  UNECE and other sources whose terms allow quotation.

Verification for a paraphrased entry checks meaning against the licensed copy
(actor, condition, action, objects, modal, list items), not string equality.

## 3b. External reference — a requirement must be citable

**Every extracted requirement gets an identifier that resolves to a specific
statement in a specific version of a specific document.**

```
draft-ietf-vcon-vcon-core-04#R-0004
└── record id ──────────────┘ └seq┘
```

Resolving it yields:

| | |
|---|---|
| `locator` | `§4.1.4` — where in the source |
| `source_version` | `-04` — which revision |
| `source_digest` | the bytes we read |
| `verb` | MUST / MUST NOT / … |
| `text` | verbatim, or our paraphrase for a licensed standard (§3a) |

That is what makes a requirement **qualified**: another document can cite
`draft-ietf-vcon-vcon-core-04#R-0004` and a reader can get back to the exact
sentence, in the exact revision, that we read. A requirement without all five
is an assertion about a document, not a reference into one.

**Sequence numbers are stable and never reused.** A withdrawn requirement keeps
its id and is marked withdrawn — renumbering silently retargets every citation.

## 4. Why ids are namespaced by record

`rfc-9943-R-012` carries its provenance in its name. A bare `R-012` collides
across sources, and the first thing anyone asks of an extracted requirement is
"says who?"

Do not renumber. If a requirement is withdrawn, mark it, keep the id.

## 5. Open questions

1. Should requirements be extracted for every summarised record, or only where
   we intend to conform or map? Extraction is expensive; most records will
   never need it.
2. Do we track requirement **satisfaction** — which of ours discharges which of
   theirs? That is a conformance matrix and a much larger commitment.
3. Should `verb` normalise SHALL → MUST? They are synonymous in RFC 2119, but
   normalising loses the source's own wording.
