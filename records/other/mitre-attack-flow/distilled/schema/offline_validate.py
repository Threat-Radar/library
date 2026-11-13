"""Offline resolution for the verbatim Attack Flow 2.0.0 schema snapshots.

Record: mitre-attack-flow. Extracted: 2026-11-09. reviewed_by: "".
Derived helper; it never changes or augments the published schemas.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker
from referencing import Registry, Resource
from referencing.exceptions import NoSuchResource


SCHEMA_NAME = "attack-flow-schema-2.0.0.json"
EXTENSION_NAME = "attack-flow-extension-2.0.0.json"
EXTENSION_ID = "extension-definition--fb9c968a-745b-4ade-9b25-c324172197f4"


def _deny_retrieval(uri):
    raise NoSuchResource(ref=uri)


def _load_files(schema_dir=None):
    base = Path(schema_dir or Path(__file__).resolve().parent).resolve()
    manifest = json.loads((base / "manifest.json").read_bytes())
    documents = {}
    for item in manifest["files"]:
        path = (base / item["path"]).resolve()
        if not path.is_relative_to(base):
            raise ValueError(f"Manifest path escapes schema directory: {item['path']}")
        data = path.read_bytes()
        if hashlib.sha256(data).hexdigest() != item["sha256"]:
            raise ValueError(f"Snapshot SHA-256 mismatch: {item['path']}")
        if len(data) != item["bytes"]:
            raise ValueError(f"Snapshot byte-count mismatch: {item['path']}")
        if item["kind"] in ("json-schema", "stix-instance"):
            documents[item["path"]] = json.loads(data)
    return base, manifest, documents


def _load_registry(schema_dir=None):
    base, manifest, documents = _load_files(schema_dir)
    registry = Registry(retrieve=_deny_retrieval)
    for item in manifest["files"]:
        if item["kind"] != "json-schema":
            continue
        schema = documents[item["path"]]
        Draft202012Validator.check_schema(schema)
        resource = Resource.from_contents(schema)
        uris = {item["reference"], item["url"], schema["$id"]}
        uris.update(item.get("aliases", []))
        for uri in sorted(uris):
            registry = registry.with_resource(uri, resource)
    return base, manifest, documents, registry.crawl()


def load_validator(schema_dir: Path | None = None) -> Draft202012Validator:
    """Verify hashes and return the raw root validator with offline resolution.

    The caller decides which object types are in scope. This API deliberately
    retains the published schema's fallback branch for unknown object types.
    """
    _, _, documents, registry = _load_registry(schema_dir)
    return Draft202012Validator(
        documents[SCHEMA_NAME], registry=registry, format_checker=FormatChecker()
    )


def _references(value):
    if isinstance(value, dict):
        if "$ref" in value:
            yield value["$ref"]
        for child in value.values():
            yield from _references(child)
    elif isinstance(value, list):
        for child in value:
            yield from _references(child)


def validate_extension(schema_dir: Path | None = None):
    """Check extension-instance reference consistency, not STIX conformance."""
    _, manifest, documents = _load_files(schema_dir)
    bundle = documents[EXTENSION_NAME]
    errors = []
    if bundle.get("type") != "bundle":
        return ["Published extension instance must be a bundle."]
    objects = bundle.get("objects", [])
    by_id = {obj.get("id"): obj for obj in objects if isinstance(obj, dict)}
    extension = by_id.get(EXTENSION_ID)
    if extension is None:
        return ["Published extension-definition ID is absent from its bundle."]
    if extension.get("type") != "extension-definition":
        errors.append("Extension ID does not identify an extension-definition.")
    schema_entry = next(item for item in manifest["files"] if item["path"] == SCHEMA_NAME)
    schema_uris = {schema_entry["reference"], schema_entry["url"]}
    schema_uris.update(schema_entry.get("aliases", []))
    if extension.get("schema") not in schema_uris:
        errors.append("Extension schema URI does not map to the local published schema.")
    if extension.get("version") != "2.0.0":
        errors.append("Extension version is inconsistent with schema version 2.0.0.")
    if extension.get("extension_types") != ["new-sdo"]:
        errors.append("Extension type is inconsistent with the published new-sdo schema.")
    for obj in objects:
        creator = by_id.get(obj.get("created_by_ref"))
        if creator is None or creator.get("type") != "identity":
            errors.append(f"Creator identity reference is unresolved for {obj.get('id')}.")
    return errors


def check_snapshot(schema_dir: Path | None = None):
    """Check integrity, schema syntax, complete $ref resolution, and references."""
    _, manifest, documents, registry = _load_registry(schema_dir)
    schemas = [item for item in manifest["files"] if item["kind"] == "json-schema"]
    ref_count = 0
    for item in schemas:
        schema = documents[item["path"]]
        resolver = registry.resolver(schema["$id"])
        for ref in _references(schema):
            resolver.lookup(ref)
            ref_count += 1
    extension_errors = validate_extension(schema_dir)
    if extension_errors:
        raise ValueError("; ".join(extension_errors))
    return {
        "status": "pass",
        "integrity_files": len(manifest["files"]),
        "schema_documents": len(schemas),
        "resolved_ref_occurrences": ref_count,
        "extension_check": "reference-consistency-only",
        "stix_bundle_validation": "not-performed",
        "network_retrieval": "disabled",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", type=Path, nargs="*", help="Individual Attack Flow SDO JSON files.")
    parser.add_argument("--check", action="store_true", help="Check snapshot integrity and every schema reference.")
    args = parser.parse_args()
    try:
        if args.check or not args.paths:
            print(json.dumps(check_snapshot(), indent=2))
        if not args.paths:
            return 0
        validator = load_validator()
        supported = set(validator.schema["$defs"])
        result_code = 0
        for path in args.paths:
            obj = json.loads(path.read_bytes())
            if not isinstance(obj, dict) or obj.get("type") not in supported:
                print(json.dumps({"path": str(path), "status": "outside-schema-scope"}))
                result_code = max(result_code, 2)
                continue
            errors = [
                {
                    "instance_path": list(error.absolute_path),
                    "schema_path": list(error.absolute_schema_path),
                    "message": error.message,
                }
                for error in validator.iter_errors(obj)
            ]
            print(json.dumps({"path": str(path), "status": "fail" if errors else "pass", "errors": errors}, indent=2))
            if errors:
                result_code = max(result_code, 1)
        return result_code
    except (OSError, ValueError, LookupError) as error:
        print(json.dumps({"status": "error", "message": str(error)}))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
