#!/usr/bin/env python3
"""Reproduce source extraction and expected outcomes without network retrieval."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import sys


sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
CORE_REFERENCE = (
    "http://raw.githubusercontent.com/oasis-open/"
    "cti-stix2-json-schemas/stix2.1/schemas/common/core.json"
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def read_json(path: Path) -> dict:
    return json.loads(path.read_bytes())


def verify_digest(path: Path, digest: str, length: int | None = None) -> bytes:
    raw = path.read_bytes()
    require(hashlib.sha256(raw).hexdigest() == digest, f"SHA256 mismatch: {path}")
    if length is not None:
        require(len(raw) == length, f"Byte length mismatch: {path}")
    return raw


def source_slice(lines: list[bytes], fixture: dict) -> bytes:
    locator = fixture["locator"]
    start, end = locator["line_start"], locator["line_end"]
    require(1 <= start <= end <= len(lines), f"Invalid locator: {fixture['path']}")
    selected = lines[start - 1 : end]
    transform = fixture["transform"]["kind"]
    if transform == "strip-rst-code-indent":
        prefix = b" " * fixture["transform"]["spaces"]
        require(
            all(not line.strip() or line.startswith(prefix) for line in selected),
            f"Unindented code line: {fixture['path']}",
        )
        return b"".join(
            line[len(prefix) :] if line.startswith(prefix) else line for line in selected
        )
    require(transform == "identity-line-slice", f"Unknown transform: {transform}")
    return b"".join(selected)


def extract_code_blocks(lines: list[bytes]) -> list[tuple[int, int, bytes]]:
    """Find all JSON directives independently of the recorded line locators."""
    result = []
    for index, line in enumerate(lines):
        if line.rstrip(b"\r\n") != b".. code:: json":
            continue
        start = index + 1
        while start < len(lines) and not lines[start].strip():
            start += 1
        end = start
        while end < len(lines) and (
            not lines[end].strip() or lines[end].startswith(b"    ")
        ):
            end += 1
        while end > start and not lines[end - 1].strip():
            end -= 1
        require(end > start, f"Empty JSON block at line {index + 1}")
        raw = b"".join(
            row[4:] if row.startswith(b"    ") else row for row in lines[start:end]
        )
        result.append((start + 1, end, raw))
    return result


def check_source(manifest: dict, source_root: Path) -> dict:
    source = manifest["source"]
    raw = verify_digest(source_root / source["path"], source["sha256"])
    lines = raw.splitlines(keepends=True)
    json_fixtures = []
    for fixture in manifest["fixtures"]:
        require(
            fixture["source_path"] == source["path"],
            f"Unexpected source path: {fixture['path']}",
        )
        actual = source_slice(lines, fixture)
        require(actual == (HERE / fixture["path"]).read_bytes(), f"Source bytes differ: {fixture['path']}")
        anchor = f".. _{fixture['locator']['anchor']}:".encode()
        require(
            any(row.rstrip(b"\r\n") == anchor for row in lines[: fixture["locator"]["line_start"]]),
            f"Missing source anchor: {fixture['path']}",
        )
        if fixture["kind"] == "source-json-example":
            json_fixtures.append(fixture)
    blocks = extract_code_blocks(lines)
    require(len(blocks) == len(json_fixtures) == 7, "JSON example coverage is not 7/7")
    for block, fixture in zip(blocks, json_fixtures):
        start, end, raw = block
        require(
            (start, end) == (fixture["locator"]["line_start"], fixture["locator"]["line_end"]),
            f"Code block locator differs: {fixture['path']}",
        )
        require(raw == (HERE / fixture["path"]).read_bytes(), f"Code block differs: {fixture['path']}")
    instance = manifest["related_source_instance"]
    require(
        verify_digest(source_root / instance["source_path"], instance["sha256"], instance["bytes"])
        == (HERE / instance["path"]).read_bytes(),
        "Extension instance differs from source",
    )
    return {"status": "matched", "fixture_count": len(manifest["fixtures"]), "json_blocks": len(blocks), "related_instances": 1}


def error_record(error) -> dict:
    return {
        "instance_path": list(error.absolute_path),
        "schema_path": list(error.absolute_schema_path),
        "keyword": error.validator,
        "message": error.message,
    }


def ordered_errors(errors: list[dict]) -> list[dict]:
    return sorted(errors, key=lambda error: json.dumps(error, sort_keys=True))


def load_validator(schema_dir: Path):
    module_path = schema_dir / "offline_validate.py"
    spec = importlib.util.spec_from_file_location("attack_flow_offline_schema", module_path)
    require(spec is not None and spec.loader is not None, "Cannot load offline schema helper")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.load_validator(schema_dir)


def check_json_examples(manifest: dict, expected: dict, validator) -> list[dict]:
    schema = validator.schema
    common_validator = validator.evolve(schema={"$ref": CORE_REFERENCE})
    results = []
    fixtures = [entry for entry in manifest["fixtures"] if entry["kind"] == "source-json-example"]
    require(len(fixtures) == len(expected["json_examples"]) == 7, "JSON expected-result coverage differs")
    for fixture in fixtures:
        data = read_json(HERE / fixture["path"])
        object_type = data["type"]
        require(object_type == fixture["id"], f"Unexpected object type in {fixture['path']}")
        target = expected["json_examples"][object_type]
        errors = [error_record(error) for error in validator.iter_errors(data)]
        core_errors = [error_record(error) for error in common_validator.iter_errors(data)]
        require((not errors) == target["schema_valid"], f"Root-schema result differs: {object_type}")
        require(
            ordered_errors(errors) == ordered_errors(target["schema_errors"]),
            f"Root-schema errors differ: {object_type}\n{json.dumps(errors, indent=2)}",
        )
        require((not core_errors) == target["stix_common_core_valid"], f"STIX common-core result differs: {object_type}")
        require(
            ordered_errors(core_errors) == ordered_errors(target["stix_common_core_errors"]),
            f"STIX common-core errors differ: {object_type}",
        )
        supported = object_type in schema["$defs"]
        require(supported == target["supported_attack_flow_sdo"], f"Schema type coverage differs: {object_type}")
        if supported:
            require(schema["$defs"][object_type]["x-exampleObject"] == data["id"], f"Schema example selector differs: {object_type}")
        results.append(
            {"fixture": fixture["path"], "json_parse": "valid", "attack_flow_root_valid": not errors,
             "attack_flow_root_errors": len(errors), "stix_common_core_valid": not core_errors,
             "stix_common_core_errors": len(core_errors), "expected_result_matched": True}
        )
    return results


def check_confidence(expected: dict) -> dict:
    source_table = (HERE / "confidence-scale.rst").read_text()
    rows = []
    for match in re.finditer(r"^  \* - ([^\n]+)\n(.*?)(?=^  \* - |\Z)", source_table, re.M | re.S):
        numbers = re.search(r"^    - (\d+)\n    - (\d+)-(\d+)\n?\Z", match[2], re.M)
        if numbers is None:
            require(match[1] == "Term", "Unrecognized confidence table row")
            continue
        rows.append(
            {"term": match[1], "value": int(numbers[1]),
             "inclusive_range": [int(numbers[2]), int(numbers[3])], "source_row": len(rows) + 1}
        )
    require(rows == expected["confidence_scale"], "Confidence scale differs from source fixture")
    by_term = {row["term"]: row for row in rows}

    def term_for(number: int) -> str:
        matching = [row["term"] for row in rows if row["inclusive_range"][0] <= number <= row["inclusive_range"][1]]
        require(len(matching) == 1, f"Confidence range gap or overlap at {number}")
        return matching[0]

    for number in range(101):
        term_for(number)
    for row in rows:
        require(term_for(row["value"]) == row["term"], f"Representative confidence outside range: {row['term']}")
    worked_text = (HERE / "confidence-examples.rst").read_text()
    term_example = re.search(
        r'^\* Convert "([^"]+)" to a confidence number:\n.*?^    \* Read off the Confidence Value for row (\d+): it is (\d+)\.',
        worked_text, re.M | re.S,
    )
    number_example = re.search(
        r'^\* Convert (\d+) to a confidence term\.\n.*?^    \* Read off the term from row (\d+): "([^"]+)"\.',
        worked_text, re.M | re.S,
    )
    require(term_example is not None and number_example is not None, "Cannot parse two worked confidence examples")
    worked = expected["source_worked_conversions"]
    require(len(worked) == 2 and all(case["derived"] is False for case in worked), "Worked confidence coverage differs")
    require(worked[0]["input"] == {"term": term_example[1]} and worked[0]["expected"] == {"confidence": int(term_example[3])}, "Term-to-number worked expectation differs")
    require(worked[1]["input"] == {"confidence": int(number_example[1])} and worked[1]["expected"] == {"term": number_example[3]}, "Number-to-term worked expectation differs")
    require(by_term[term_example[1]]["value"] == int(term_example[3]) and by_term[term_example[1]]["source_row"] == int(term_example[2]), "Term-to-number worked conversion failed")
    require(term_for(int(number_example[1])) == number_example[3] and by_term[number_example[3]]["source_row"] == int(number_example[2]), "Number-to-term worked conversion failed")
    boundaries = expected["derived_confidence_boundary_cases"]
    boundary_numbers = {number for row in rows for number in row["inclusive_range"]}
    require(len(boundaries) == len(boundary_numbers) == 12, "Confidence boundary coverage differs")
    require({case["input"]["confidence"] for case in boundaries} == boundary_numbers, "Missing confidence boundary")
    for case in boundaries:
        require(case["derived"] is True, "Boundary case must be marked derived")
        require(case["expected"]["term"] == term_for(case["input"]["confidence"]), "Confidence boundary conversion failed")
    return {"table_rows": len(rows), "source_worked_examples": len(worked), "derived_boundary_cases": len(boundaries), "integer_range_partition": "0..100, no gaps or overlaps"}


def check_effects(manifest: dict, expected: dict) -> dict:
    fixture = next(entry for entry in manifest["fixtures"] if entry["path"] == "effects.rst")
    lines = (HERE / fixture["path"]).read_text().splitlines(keepends=True)
    first_line = fixture["locator"]["line_start"]
    cases = expected["effects_cases"]
    require(len(cases) == 10 and len({case["id"] for case in cases}) == 10, "Effects expectation coverage differs")
    for case in cases:
        require(case["derived"] is True, f"Effects case must be marked derived: {case['id']}")
        locator = re.fullmatch(r"docs/language\.rst:(\d+)(?:-(\d+))?", case["source_locator"])
        require(locator is not None, f"Invalid Effects locator: {case['id']}")
        start, end = int(locator[1]), int(locator[2] or locator[1])
        require(first_line <= start <= end <= fixture["locator"]["line_end"], f"Effects locator outside source fixture: {case['id']}")
        require("".join(lines[start - first_line : end - first_line + 1]) == case["source_text"], f"Effects source evidence differs: {case['id']}")
    return {"derived_cases_registered": len(cases), "verbatim_evidence": "matched", "engine_execution": "not performed"}


def check_extension(manifest: dict, expected: dict, schema: dict) -> dict:
    target = expected["extension_instance"]
    instance = read_json(HERE / target["path"])
    require(instance["type"] == target["type"] and instance["id"] == target["id"], "Extension bundle identity differs")
    require(len(instance["objects"]) == target["object_count"] == 2, "Extension bundle object count differs")
    objects = {obj["id"]: obj for obj in instance["objects"]}
    definition = objects[target["extension_definition_id"]]
    creator = objects[target["creator_identity_id"]]
    require(definition["type"] == "extension-definition" and creator["type"] == "identity", "Extension object types differ")
    require(definition["version"] == target["version"], "Extension version differs")
    require(definition["extension_types"] == [target["extension_type"]], "Extension types differ")
    require(definition["schema"] == target["schema_reference"] and schema["$id"] == target["schema_document_id"], "Published schema URLs differ from recorded pair")
    for obj in objects.values():
        require(obj["created_by_ref"] == creator["id"], "Extension creator reference is unresolved")
    required_extensions = schema["allOf"][1]["properties"]["extensions"]["required"]
    require(required_extensions == [definition["id"]], "Root-schema extension id differs")
    count = 0
    for fixture in manifest["fixtures"]:
        if fixture["kind"] != "source-json-example":
            continue
        obj = read_json(HERE / fixture["path"])
        if obj["type"] in schema["$defs"]:
            require(obj["extensions"][definition["id"]]["extension_type"] in definition["extension_types"], f"Example extension declaration differs: {fixture['path']}")
            count += 1
    return {"json_parse": "valid", "local_creator_references": "resolved", "attack_flow_example_declarations": count, "schema_reference_and_id": "recorded differing URL paths", "full_stix_bundle_validation": "not run (schema closure not included)"}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path, help="Optional cache root containing docs/language.rst and stix/attack-flow-extension-2.0.0.json")
    parser.add_argument("--report", type=Path, help="Write the JSON outcome report to this path")
    args = parser.parse_args()
    try:
        manifest = read_json(HERE / "manifest.json")
        for fixture in manifest["fixtures"]:
            verify_digest(HERE / fixture["path"], fixture["sha256"], fixture["bytes"])
        instance = manifest["related_source_instance"]
        verify_digest(HERE / instance["path"], instance["sha256"], instance["bytes"])
        results = manifest["expected_results"]
        verify_digest(HERE / results["path"], results["sha256"])
        expected = read_json(HERE / results["path"])
        validator = load_validator(HERE.parent / "schema")
        report = {
            "record": "mitre-attack-flow", "checked": "2026-11-09", "reviewed_by": "",
            "result": "expected outcomes reproduced", "network_retrieval": False,
            "source_equality": check_source(manifest, args.source_root) if args.source_root else {"status": "not requested; fixture hashes checked"},
            "json_examples": check_json_examples(manifest, expected, validator),
            "confidence": check_confidence(expected),
            "effects": check_effects(manifest, expected),
            "extension_instance": check_extension(manifest, expected, validator.schema),
        }
        report["schema_summary"] = {
            "attack_flow_root_valid": sum(item["attack_flow_root_valid"] for item in report["json_examples"]),
            "attack_flow_root_invalid": sum(not item["attack_flow_root_valid"] for item in report["json_examples"]),
            "expected_source_defects_reproduced": [item["fixture"] for item in report["json_examples"] if not item["attack_flow_root_valid"]],
            "complete_flow_reference_validation": "not performed; source examples are fragments",
        }
        text = json.dumps(report, indent=2) + "\n"
        if args.report:
            args.report.write_text(text)
        print(text, end="")
        return 0
    except (AssertionError, KeyError, ValueError, OSError) as error:
        print(f"Fixture check failed: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
