---
record: cwe
kind: schema
title: "cwe — schemas"
extracted: "2026-10-08"
reviewed_by: ""
---

# Schema — CWE XML Schema 7.3

| file | what | status |
|---|---|---|
| `cwe_schema_v7.3.xsd` | The CWE XML Schema, version 7.3. It is the schema that the CWE List 4.20 XML release names in its `xsi:schemaLocation`. | **source, verbatim**: a byte-identical copy (SHA-256 below), with its licence header intact |

No derived schema is held, because the source is itself machine-checkable and validates the CWE 4.20 catalogue unchanged (see Results below). Field-by-field structure with line numbers is in `../messages.yaml`. Fixtures and whole-catalogue expected results are in `../examples/`.

## Source

| | |
|---|---|
| URL | https://cwe.mitre.org/data/xsd/cwe_schema_v7.3.xsd (the `xsi:schemaLocation` of `cwec_v4.20.xml`). The cached `cwe_schema_latest.xsd` (cache dated 2026-10-08) is byte-identical. |
| Version | 7.3 (`version="7.3"` on `xs:schema`, L2; appinfo `<version>`, L8) |
| Date | December 11, 2025 (appinfo `<date>`, L9) |
| Namespace | target `http://cwe.mitre.org/cwe-7` (prefix `cwe`); `elementFormDefault="qualified"`, `attributeFormDefault="unqualified"` |
| Size | 96,240 bytes, 1,345 lines, LF line ends, UTF-8 (the only non-ASCII character is one U+2019 at L1223) |
| SHA-256 | `690dedeed4e12eb8ba7244bbab90176afac549cfd6403de37000de7481e45f98` |
| Copy | made 2026-10-08 from `.cache/cwe-src/cwe_schema_v7.3.xsd`; `cmp` reports the two files identical and the digests match |

Licence header (appinfo `<terms_of_use>`, L10, verbatim). It is retained in the copy, as the header itself requires:

> Copyright (c) 2006-2025, The MITRE Corporation. All rights reserved. The contents of this file are subject to the terms of the CWE License located at https://cwe.mitre.org/about/termsofuse.html. See the CWE License for the specific language governing permissions and limitations for use of this schema. When distributing copies of the CWE Schema, this license header must be included.

## What it declares

- **One global element**, `Weakness_Catalog` (L16), so it is the root of every valid document. Its four containers (`Weaknesses`, `Categories`, `Views`, `External_References`) are each optional, but each one present must hold at least one entry, in that order.
- **31 named complexTypes and 29 anonymous ones**: the root, its 4 containers, and 24 element-local types.
- **34 named simpleTypes** with 342 enumeration values, plus one anonymous enumeration (`Contribution/@Type`: `Content` | `Feedback`, L337), giving 344 `xs:enumeration` facets in all.
- **145 element declarations, 55 attribute declarations, and 2 wildcards**. There are 3 `xs:choice` groups (L299, L369, L558) and 2 extensions (simpleContent L349, complexContent L457). No `default` or `fixed` value is declared anywhere.

Every structure, field, cardinality and enumeration is in `../messages.yaml`, with line numbers into this copy.

## The XHTML import is load-bearing

L3:

```xml
<xs:import namespace="http://www.w3.org/1999/xhtml" schemaLocation="http://www.w3.org/2002/08/xhtml/xhtml1-strict.xsd"/>
```

`xhtml1-strict.xsd` in turn imports `http://www.w3.org/2001/xml.xsd` (for `xml:lang` and `xml:space`). Both are third-party W3C files. They are held only in `.cache/w3c-xhtml/` (gitignored) and are never committed:

| file | URL | bytes | SHA-256 (retrieved 2026-10-08, twice, same bytes) |
|---|---|---|---|
| `xhtml1-strict.xsd` | http://www.w3.org/2002/08/xhtml/xhtml1-strict.xsd (`$Id: xhtml1-strict.xsd,v 1.2 2002/08/28 08:05:44 mimasa Exp $`) | 65,477 | `9f89777c95be6866317de83852f9fbddd6c48c381a36d8fd9b00e11b864a209f` |
| `xml.xsd` | http://www.w3.org/2001/xml.xsd | 8,836 | `61960fb3131e38022caad5360e2f33a3382578ab3c80cd58bd74320ede61b20c` |

Both wildcards are `processContents="strict"`, so every XHTML element in a CWE document must match a declaration in that schema. If the import cannot be loaded, libxml2 does **not** reject the schema. It warns `Element '{http://www.w3.org/2001/XMLSchema}import': Failed to locate a schema at location 'http://www.w3.org/2002/08/xhtml/xhtml1-strict.xsd'. Skipping the import.`, compiles anyway, and then rejects every XHTML element. Run offline without the catalog below, `cwec_v4.20.xml` fails with exit 3 and 5,457 errors of the form `No matching global element declaration available, but demanded by the strict wildcard.` That is exactly one error per top-level XHTML element: 2,902 in StructuredTextType slots and 2,555 in `Example_Code`.

## Identity constraints

There are five `xs:unique` constraints on `Weakness_Catalog`. There is no `xs:key` and no `xs:keyref`.

| name | lines | selector | field | effective scope |
|---|---|---|---|---|
| `uniqueWeaknessID` | L55–58 | `./cwe:Weaknesses/cwe:Weakness` | `@ID` | Weakness IDs |
| `uniqueWeaknessName` | L59–62 | `./cwe:*/cwe:*` | `@Name` | Names across **Weakness, Category and View together**. The selector reaches every grandchild of the root, and External_Reference has no `Name`, so `xs:unique` skips it. Proven by `../examples/neg-duplicate-name-across-kinds.xml`. |
| `uniqueCategoryID` | L63–66 | `./cwe:Categories/cwe:Category` | `@ID` | Category IDs |
| `uniqueViewID` | L67–70 | `./cwe:Views/cwe:View` | `@ID` | View IDs |
| `uniqueReferenceID` | L71–74 | `./cwe:External_References/cwe:External_Reference` | `@Reference_ID` | Reference IDs |

ID uniqueness is enforced only **within** each kind. The schema would accept a Category and a Weakness with the same ID; 4.20 has none (`../examples/catalog-stats.yaml` I24). Cross-references are typed (`xs:integer` / `xs:string`) but never resolved by validation. That covers Related_Weakness `CWE_ID` / `View_ID` / `Chain_ID`, Has_Member / Member_Of `CWE_ID` / `View_ID`, Suggestion `CWE_ID` and Reference `External_Reference_ID`. A consumer resolves them itself; see `unchecked_references` in `../messages.yaml`.

## The two `xs:any` slots

| line | in | namespace | processContents | cardinality | elements that carry it |
|---|---|---|---|---|---|
| L1332 | `StructuredTextType` (`mixed="true"`) | `http://www.w3.org/1999/xhtml` | strict | 0..unbounded | 17 element declarations (L87 Extended_Description, L127 Summary, L149 Objective, L206, L269, L284, L368, L370, L390, L392, L404, L421 Rationale, L422 Comments, L443, L474, L492, L494) and `NotesType/Note` by extension (L457) |
| L1340 | `StructuredCodeType` (`mixed="true"`) | `http://www.w3.org/1999/xhtml` | strict | 0..unbounded | `Demonstrative_Example/Example_Code` (L371) only |

Both slots allow character data interleaved with XHTML elements, and nothing else: no CWE-namespace and no un-namespaced elements. `Weakness/Description` (L86) is plain `xs:string`, **not** StructuredTextType, so it may carry no markup (`../examples/neg-xhtml-in-plain-description.xml`). The documentation's own XHTML examples (L1329) are written in upper case and fail the strict wildcard as written (`../examples/documented-formats.yaml` D10).

## Validate offline: exact commands

Run these from the library root, the directory that holds `records/` and `.cache/`. They were tested 2026-10-08 in a fresh directory, downloads included.

```sh
# one-time: the two W3C schemas the CWE XSD imports (cache only, never committed)
mkdir -p .cache/w3c-xhtml
curl -sSL -A "Mozilla/5.0" -o .cache/w3c-xhtml/xhtml1-strict.xsd http://www.w3.org/2002/08/xhtml/xhtml1-strict.xsd
curl -sSL -A "Mozilla/5.0" -o .cache/w3c-xhtml/xml.xsd http://www.w3.org/2001/xml.xsd
shasum -a 256 .cache/w3c-xhtml/xhtml1-strict.xsd .cache/w3c-xhtml/xml.xsd   # expect the digests above

# an OASIS XML catalog that maps the two remote schemaLocations to the local copies
cat > .cache/w3c-xhtml/catalog.xml <<'EOF'
<?xml version="1.0"?>
<catalog xmlns="urn:oasis:names:tc:entity:xmlns:xml:catalog">
  <uri name="http://www.w3.org/2002/08/xhtml/xhtml1-strict.xsd" uri="xhtml1-strict.xsd"/>
  <uri name="http://www.w3.org/2001/xml.xsd" uri="xml.xsd"/>
</catalog>
EOF

# validate any CWE XML file; --nonet guarantees nothing is fetched
XML_CATALOG_FILES="$PWD/.cache/w3c-xhtml/catalog.xml" xmllint --nonet --noout \
  --schema records/other/cwe/distilled/schema/cwe_schema_v7.3.xsd  path/to/file.xml
```

Exit code 0 means the file validates (`<file> validates`). Exit code 3 means it is invalid; one line per error is printed, then `<file> fails to validate`. The catalog's relative `uri` values resolve against the catalog file's own location. `<system systemId=… uri="file:///…"/>` entries with absolute paths work as well.

## Results (2026-10-08, xmllint using libxml2 2.9.13)

| input | result |
|---|---|
| `cwec_v4.20.xml`: CWE List 4.20, `Date="2026-04-30"`, 18,192,305 bytes, SHA-256 `1f5a78bd62e00f86436b4fe32d5034a57e8f0da88e4063b2072b664ae510912e` (from `cwec_v4.20.xml.zip`, SHA-256 `3976f599e5e5200219a3108bb896d06e2a88fbb293369e1883cb423a5e9d7d50`) | **validates** (`cwec_v4.20.xml validates`, exit 0, about 0.13 s), against both the cached source and this copy |
| the same file, offline without the catalog | fails, exit 3: 5,457 strict-wildcard errors (see above) |
| `../examples/*.xml` (20 fixtures) | 14 valid and 6 invalid, each exactly as `../examples/expected.yaml` records |

Separately from xmllint, a type-directed walk of the whole 4.20 file (stdlib parser) resolved every element and attribute to exactly one declaration of this schema, with 0 anomalies. Its per-declaration counts are the `observed_4_20` figures in `../messages.yaml`.
