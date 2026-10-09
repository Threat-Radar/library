#!/usr/bin/env python3
"""
Normalization loader for library requirement sets (raw v2 -> v3-conformant).

The 44 on-disk `records/<body>/<id>/distilled/requirements.yaml` files are RAW
v2: document-specific long-tail keys sit as top-level siblings, the version key
is `schema:`, header `note:` is the set note, `maps_to` entries use publisher
spellings (`source`/`relationship`/`target_edition`/`kind`), YAML parses
`testable: yes` as a bool, and a few multivalued fields appear as scalars.

`normalize_set(doc)` returns a dict that conforms to
`schema/requirements.linkml.yaml` (library_requirements v3.1): it renames keys
to the canonical slot names, folds the parallel header taxonomies into
`taxonomy`, relocates every non-slot key into an `attributes` bag (per-req and a
header extension bag, symmetric), coerces `yes/no` booleans back to strings,
wraps scalars into the 1-element lists the multivalued slots expect, and derives
`verb_bcp14`. It mutates nothing on disk — the raw files stay v2 until the
separate migration PR.

Pure stdlib + PyYAML. Used by `bin/check-requirements`.
"""
from __future__ import annotations
import copy

# --- canonical slot sets (mirror schema/requirements.linkml.yaml) ----------

SET_SLOTS = {
    "conforms_to", "record", "source_version", "source_digest",
    "source_keyword_count", "extracted_keyword_count", "reconciliation",
    "counts", "native_counts", "source_normative_forms",
    "extracted_normative_forms", "audience", "generated_from", "generated_by",
    "extracted", "extracted_by", "reviewed_by", "set_note",
    "reference_editions", "required_deliverables", "taxonomy", "excluded",
    "requirements", "attributes",
}

# parallel header lists folded into `taxonomy`, tagged with taxonomy_kind
HEADER_TAXONOMY_KEYS = {
    "practices": "practice",
    "security_levels": "security-level",
    "requirement_areas": "requirement-area",
    "principles": "principle",
    "tasks": "ssdf-task",
    "sources": "source",
    "reference_schemes": "reference-scheme",
}

REQ_SLOTS = {
    "id", "designator", "native_id", "entry_type", "status", "formerly",
    "former_ids", "moved_to", "withdrawn_to", "inherits_from", "added_by",
    "cite_as", "verb", "verbs", "verb_bcp14", "actor", "condition", "locator",
    "text", "short_title", "title", "kind", "inferred_note", "object", "field",
    "context", "applies_from", "normativity", "nature", "phase", "level",
    "tailorable", "parent", "children", "group", "practice", "task", "tasks",
    "testable", "testable_reason", "verification", "audit_status",
    "expects_deliverables", "contributes_to_assurance",
    "notional_implementation_examples", "footnote", "footnotes", "section",
    "section_title", "section_name", "chapter", "role", "verifier", "variant",
    "requirement_type", "maturity_level", "question", "answer_set", "track",
    "family", "basis", "maps_to", "satisfied_by", "applies_to", "scopes_to",
    "external_refs", "notes", "attributes",
}

# raw per-req key -> canonical slot
REQ_RENAMES = {
    "note": "notes",
    "additional_notes": "notes",
    "testable_note": "testable_reason",
    "refs": "external_refs",
}

# Requirement multivalued slots: a scalar in the raw file is wrapped to [scalar]
REQ_MULTIVALUED = {
    "former_ids", "moved_to", "withdrawn_to", "inherits_from", "verbs", "actor",
    "context", "tasks", "children", "expects_deliverables", "external_refs",
}

CROSSREF_SLOTS = {
    "scheme", "framework", "standard", "target", "ids", "entries", "ref",
    "target_id", "source_text", "relation", "provenance", "target_record",
    "library_record", "xref_record", "xref_id", "xref_basis", "title",
    "published_by", "mapping_source", "edition", "edition_note", "rationale",
    "xref_kind", "adopted", "refs", "xref_note", "also", "attributes",
}
CROSSREF_RENAMES = {
    "source": "mapping_source",
    "source_ref": "mapping_source",
    "relationship": "relation",
    "target_edition": "edition",
    "kind": "xref_kind",
    "published_by_source": "published_by",
    "note": "xref_note",
    "target_note": "xref_note",
    "record": "xref_record",
    "id": "xref_id",
    "basis": "xref_basis",
}
CROSSREF_MULTIVALUED = {"ids", "entries", "refs", "also"}

DELIVERABLE_SLOTS = {
    "deliverable_id", "designator", "title", "from_requirements",
    "from_subclauses", "deliverable_note", "attributes",
}
DELIVERABLE_RENAMES = {"id": "deliverable_id"}

TAXONOMY_NODE_SLOTS = {"taxonomy_kind", "number", "name", "title", "attributes"}

# canonical BCP 14 keywords (RFC 2119 as updated by RFC 8174)
BCP14 = {
    "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD",
    "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", "OPTIONAL",
}


def _coerce_bool_yesno(v):
    if isinstance(v, bool):
        return "yes" if v else "no"
    return v


def _as_list(v):
    if v is None:
        return []
    return v if isinstance(v, list) else [v]


def _bag_put(bag, key, value):
    """Stash a relocated key into an attributes bag without clobbering."""
    if key in bag:
        i = 2
        while f"{key}__{i}" in bag:
            i += 1
        bag[f"{key}__{i}"] = value
    else:
        bag[key] = value


def _apply_renames(src, renames, canon_slots, bag):
    """Return a dict: rename raw keys, relocate unknown keys into `bag`.

    Keys that collide on rename (canonical already taken) are relocated too, so
    nothing is ever silently dropped.
    """
    out = {}
    for k, v in src.items():
        canon = renames.get(k, k)
        if canon in canon_slots:
            if canon in out:
                _bag_put(bag, k, v)
            else:
                out[canon] = v
        else:
            _bag_put(bag, k, v)
    return out


def _normalize_footnote(v):
    if isinstance(v, dict):
        return v
    return {"text": v}


def normalize_crossref(raw):
    if not isinstance(raw, dict):
        # a bare-string crosswalk entry is the raw reference text as printed
        # (e.g. "sp-800-218#PS.1", "FD&C Act §524B(a)") — round-trip via `ref`.
        return {"ref": raw}
    bag = {}
    out = _apply_renames(raw, CROSSREF_RENAMES, CROSSREF_SLOTS, bag)
    for k in CROSSREF_MULTIVALUED:
        if k in out and not isinstance(out[k], list):
            out[k] = [out[k]]
    if "also" in out:
        out["also"] = [normalize_crossref(a) for a in out["also"]]
    if bag:
        out["attributes"] = bag
    return out


def normalize_deliverable(raw):
    if not isinstance(raw, dict):
        return raw
    bag = {}
    out = _apply_renames(raw, DELIVERABLE_RENAMES, DELIVERABLE_SLOTS, bag)
    for k in ("from_requirements", "from_subclauses"):
        if k in out and not isinstance(out[k], list):
            out[k] = [out[k]]
    if bag:
        out["attributes"] = bag
    return out


def normalize_example(raw):
    if not isinstance(raw, dict):
        return {"text": raw}
    out = {}
    for k, v in raw.items():
        if k == "id":
            out["example_id"] = v
        elif k in ("example_id", "text"):
            out[k] = v
        # examples in the corpus carry only id+text; anything else is dropped
        # into text-adjacent prose is not expected, so keep strictly.
    return out


def _fold_taxonomy_item(kind, item):
    if isinstance(item, dict):
        bag = {}
        node = {"taxonomy_kind": kind}
        for k, v in item.items():
            if k in ("number", "name", "title"):
                node[k] = v
            else:
                _bag_put(bag, k, v)
        if bag:
            node["attributes"] = bag
        return node
    return {"taxonomy_kind": kind, "name": item}


def normalize_requirement(raw):
    if not isinstance(raw, dict):
        return raw
    bag = {}
    out = _apply_renames(raw, REQ_RENAMES, REQ_SLOTS, bag)

    # bool -> string coercions
    if "testable" in out:
        out["testable"] = _coerce_bool_yesno(out["testable"])
    if "contributes_to_assurance" in out:
        out["contributes_to_assurance"] = _coerce_bool_yesno(
            out["contributes_to_assurance"])

    # a numeric `level` is a maturity/assurance TIER (BSIMM 1/2/3); it rides the
    # string arm of StructuralLevel verbatim and migrates to attributes.tier later.
    if "level" in out and isinstance(out["level"], (int, float)) and not isinstance(out["level"], bool):
        out["level"] = str(out["level"])

    # scalar -> 1-list for multivalued slots
    for k in REQ_MULTIVALUED:
        if k in out and not isinstance(out[k], list):
            out[k] = [out[k]]

    # nested objects
    if "maps_to" in out:
        out["maps_to"] = [normalize_crossref(m) for m in _as_list(out["maps_to"])]
    if "notional_implementation_examples" in out:
        out["notional_implementation_examples"] = [
            normalize_example(e)
            for e in _as_list(out["notional_implementation_examples"])
        ]
    if "footnote" in out:
        fn = out["footnote"]
        # a single footnote; if a list sneaks in, move to footnotes
        if isinstance(fn, list):
            out.setdefault("footnotes", [])
            out["footnotes"] = _as_list(out.pop("footnote")) + out["footnotes"]
        else:
            out["footnote"] = _normalize_footnote(fn)
    if "footnotes" in out:
        out["footnotes"] = [_normalize_footnote(f) for f in _as_list(out["footnotes"])]

    # derive verb_bcp14 (never overwrites the verbatim `verb`)
    if "verb_bcp14" not in out:
        bc = _derive_bcp14(out.get("verb"))
        if bc:
            out["verb_bcp14"] = bc

    if bag:
        out["attributes"] = bag
    return out


def _derive_bcp14(verb):
    if not isinstance(verb, str):
        return None
    cand = " ".join(verb.strip().upper().split())
    return cand if cand in BCP14 else None


def normalize_set(doc):
    """Raw v2 requirement-set dict -> v3.1-conformant dict (deep copy; no disk writes)."""
    if not isinstance(doc, dict):
        raise TypeError("requirement set must be a mapping")
    doc = copy.deepcopy(doc)
    bag = {}
    taxonomy = []

    out = {}
    for k, v in doc.items():
        if k == "schema":
            out["conforms_to"] = v
        elif k == "note":
            out["set_note"] = v
        elif k in HEADER_TAXONOMY_KEYS:
            kind = HEADER_TAXONOMY_KEYS[k]
            for item in _as_list(v):
                taxonomy.append(_fold_taxonomy_item(kind, item))
        elif k == "requirements":
            out["requirements"] = [normalize_requirement(r) for r in _as_list(v)]
        elif k == "required_deliverables":
            out["required_deliverables"] = [normalize_deliverable(d) for d in _as_list(v)]
        elif k == "taxonomy":
            for item in _as_list(v):
                taxonomy.append(_fold_taxonomy_item(
                    item.get("taxonomy_kind", "other") if isinstance(item, dict) else "other",
                    item))
        elif k in SET_SLOTS:
            out[k] = v
        else:
            _bag_put(bag, k, v)

    if taxonomy:
        out["taxonomy"] = taxonomy
    if bag:
        out["attributes"] = bag
    return out
