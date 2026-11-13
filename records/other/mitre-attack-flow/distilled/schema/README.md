---
record: mitre-attack-flow
kind: schema
title: "mitre-attack-flow — published schema and dependency snapshots"
extracted: "2026-11-09"
reviewed_by: ""
---

This extraction preserves the published Attack Flow language schema version 2.0.0
from release v4.1.0, commit `5c8bf4ca9ff64ef9b55c38a2505db318750cbcda`.
Release, language, and schema versions are distinct. The files below are usable
offline without changing their published identifiers or references.

| File | Role and source locator |
|---|---|
| `attack-flow-schema-2.0.0.json` | Verbatim JSON Schema, draft 2020-12; the complete upstream `stix/attack-flow-schema-2.0.0.json` file. Its `$defs` contain the five Attack Flow SDO definitions. |
| `attack-flow-extension-2.0.0.json` | Verbatim STIX **instance**, not a JSON Schema: a bundle containing an `extension-definition` and its creator `identity`; the complete upstream `stix/attack-flow-extension-2.0.0.json` file. |
| `stix-dependencies/stix2.1/schemas/common/*.json` | Twelve verbatim, transitively referenced OASIS STIX schemas, from commit `c4f8d589acf2bdb3783655c89e0ffb6e150006ae`. |
| `stix-dependencies/master/schemas/common/timestamp.json` | One verbatim schema from the separately pinned `master` dependency, commit `9af1db41b7b86c06324f899649ae83480134f66e`. |
| `LICENSE-attack-flow.txt` | Verbatim upstream Apache License 2.0 text for the Attack Flow files. |
| `stix-dependencies/LICENSE` | Verbatim upstream OASIS copyright, redistribution conditions, and disclaimer for the dependency snapshots. |
| `manifest.json` | Source URLs, whole-file or JSON Pointer locators, original reference URIs, immutable commits, byte counts, and SHA-256 digests. |
| `offline_validate.py` | Local integrity, reference-resolution, and object-validation helper; derived extraction tooling, outside the published schema. |

The manifest records provenance for every copied file and the authored README and
helper. It does not contain a recursive digest of itself. Its `files[].sha256`
values describe the exact bytes on disk. No upstream schema, `$id`, `$ref`,
description, spelling, or whitespace has been rewritten in place. The snapshots
retain the dependency cache's branch/path layout so relative references remain
predictable. Only the URI-to-file registry in the helper adapts resolution.

The original [schema source](https://github.com/center-for-threat-informed-defense/attack-flow/blob/5c8bf4ca9ff64ef9b55c38a2505db318750cbcda/stix/attack-flow-schema-2.0.0.json),
[extension instance](https://github.com/center-for-threat-informed-defense/attack-flow/blob/5c8bf4ca9ff64ef9b55c38a2505db318750cbcda/stix/attack-flow-extension-2.0.0.json),
and [language source](https://github.com/center-for-threat-informed-defense/attack-flow/blob/5c8bf4ca9ff64ef9b55c38a2505db318750cbcda/docs/language.rst)
are pinned independently of their public deployment URLs. A schema `$id` is an
identifier, not a guarantee that dereferencing it succeeds: published GitHub Pages
`/schema/` and `/stix/` addresses may return 404. The helper maps both published
Attack Flow schema addresses to the exact local schema and never fetches them.

The Attack Flow schema references OASIS `stix2.1` over HTTP, while the action
execution timestamps reference `master` over HTTPS. These branches can move, so
the manifest records their separate immutable commits instead of presenting them
as part of the Attack Flow release. Both timestamp snapshots currently have the
same bytes and the same `stix2.1` `$id`; their original reference URIs and source
commits remain separate entries. Relative references in the OASIS schemas resolve
against their preserved `$id` values. All 13 dependency documents belong to the
transitive closure of the Attack Flow object schema.

There are source discrepancies that this extraction preserves:

- `docs/language.rst`, **Attack Flow SDOs**, describes seven object types: the
  five `attack-*` types plus `x-detection` and `x-mitigation`. The published
  schema has five `$defs` and no dedicated definitions or type-dispatch branches
  for the two `x-*` types. Passing a custom object through its fallback branch
  does not establish conformance with the missing language definitions.
- The language page's **Attack Flow** table lists five `scope` values. The schema
  also accepts `emulation-plan` and `attack-tree`, for seven values.
- The language page's **Attack Action** table labels `execution_start` and
  `execution_end` as `identifier`; their published schema references are
  timestamp schemas.

The schema validates one SDO at a time. It does not enforce the description's
document-wide exactly-one-`attack-flow` rule, reference-target existence, target
object types after dereferencing, traversal or effect semantics, or timestamp
ordering. It is not a STIX bundle schema and must not be used to validate the
extension bundle as a whole. The dependency closure does not include full STIX
bundle, identity, extension-definition, observable, or other SDO schemas.

From the repository root, with Python and `jsonschema` installed:

```sh
.cache/extraction-venv/bin/python records/other/mitre-attack-flow/distilled/schema/offline_validate.py --check
.cache/extraction-venv/bin/python records/other/mitre-attack-flow/distilled/schema/offline_validate.py path/to/attack-flow-object.json
```

`--check` verifies every manifest digest, meta-validates the 14 schema documents,
resolves every `$ref` in that closure, and checks the extension instance's local
creator and schema references. The last check is reference consistency only, not
STIX instance validation. Missing registry entries raise an error; there is no
network retrieval fallback.

Programmatic use exposes the unchanged root validator, including its fallback
branch, for reproducing source defects:

```python
import importlib.util
from pathlib import Path

schema_dir = Path("records/other/mitre-attack-flow/distilled/schema")
spec = importlib.util.spec_from_file_location("attack_flow_offline", schema_dir / "offline_validate.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
validator = module.load_validator(schema_dir)
errors = list(validator.iter_errors(object_under_test))
```

The CLI accepts the five defined SDO types and reports other types as outside its
schema scope. `load_validator()` deliberately returns the raw published root
schema validator without adding a type filter. As an explicit validation policy,
the helper enables `jsonschema.FormatChecker` for `format` annotations, notably
external-reference URI strings. Neither interface adds graph or prose constraints
absent from the published schema.

Attack Flow attribution: Copyright 2021 MITRE. Approved for public release.
Document number CT0040. Licensed under the Apache License, Version 2.0; see
`LICENSE-attack-flow.txt`. OASIS dependency attribution and redistribution
conditions are retained in `stix-dependencies/LICENSE`.
