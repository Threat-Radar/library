---
record: cwe
kind: examples
title: "cwe — examples and test vectors"
extracted: "2026-10-08"
reviewed_by: ""
---

# Examples and test vectors: CWE XML Schema 7.3 with CWE List 4.20

The XSD has **no test vectors of its own**. Its documentation does give examples of identifier and content formats, and those are held as vectors in `documented-formats.yaml`. Everything else here is cut from the real CWE List 4.20 release, `cwec_v4.20.xml` (SHA-256 `1f5a78bd62e00f86436b4fe32d5034a57e8f0da88e4063b2072b664ae510912e`), so an importer is tested against the data it will actually meet.

| file | what |
|---|---|
| `*.xml` (20) | standalone `Weakness_Catalog` documents: 13 hold entries copied **verbatim** from 4.20; 7 are **derived** (1 positive control and 6 negatives) |
| `expected.yaml` | for every fixture: source entry with catalog line and byte range, SHA-256 of the fixture and of the verbatim entry bytes, the **actual** xmllint result (exit code; for negatives, every error message), and the semantic values an importer must produce (abstraction, structure, status, usage, reasons, suggestions, related weaknesses with Nature / View_ID / Ordinal / Chain_ID, taxonomy mappings with Mapping_Fit, members, content-history summary, successor-in-prose text). It ends with 5 cross-fixture assertions (X1–X5). |
| `catalog-stats.yaml` | whole-catalogue expected results for 4.20: counts, distributions (Status, Usage per kind, Abstraction, Structure, Nature, Taxonomy_Name, Mapping_Fit …), deprecated-successor classification, and 32 observed invariants with exceptions (I01–I32). It includes the derivation logic, and its figures were cross-checked against an independent first pass. |
| `documented-formats.yaml` | 12 vectors (D01–D12), one per example in the XSD documentation (`REF-1`, `[REF-1]`, `CC-1`, `DX-1`, `DM-1`, `MIT-1`, CVE ids, `YYYY` / `--MM` / `---DD`, the XHTML snippets, `"good"` / `"bad"`, CWE-23), each with 4.20 conformance |

## Fixtures

Total 166,585 bytes. The 13 verbatim fixtures are 144,386 bytes, of which CWE-79 alone is 75,908.

| file | kind | bytes | source in `cwec_v4.20.xml` | what it exercises |
|---|---|---|---|---|
| `weakness-79-base-allowed.xml` | verbatim | 75,908 | Weakness 79 L221591–222480 | Weakness CWE-79: Base / Simple / Stable / Allowed. 20 of the 23 WeaknessType children, including consequences, detection methods, mitigations, demonstrative and observed examples, taxonomy mappings with and without Mapping_Fit, 4 Previous_Entry_Names and a Contribution. It is also the CanPrecede target of chain CWE-692. |
| `weakness-1174-variant.xml` | verbatim | 4,896 | Weakness 1174 L16124–16209 | Weakness CWE-1174: Variant / Draft / Allowed. The smallest non-deprecated Allowed Variant. |
| `weakness-710-pillar.xml` | verbatim | 10,846 | Weakness 710 L206511–206705 | Weakness CWE-710: Pillar / Incomplete / Discouraged. The smallest Pillar; it has no Related_Weaknesses (a root of view 1000). |
| `weakness-1093-class-allowed-with-review.xml` | verbatim | 5,144 | Weakness 1093 L9418–9508 | Weakness CWE-1093: Class / Allowed-with-Review (Reason Abstraction). Primary ChildOf CWE-710, so the class/pillar edge lies between two fixtures. |
| `weakness-692-chain.xml` | verbatim | 12,179 | Weakness 692 L202592–202795 | Weakness CWE-692: Compound / **Chain** / Discouraged. StartsWith CWE-184 in view 709 with Chain_ID 692. The smallest of the three named chains. |
| `weakness-689-composite.xml` | verbatim | 11,744 | Weakness 689 L201574–201750 | Weakness CWE-689: Compound / **Composite** / Allowed. Requires CWE-362 and CWE-732, and is also a Primary ChildOf CWE-362. The smallest of the four composites. |
| `weakness-1187-deprecated.xml` | verbatim | 2,451 | Weakness 1187 L16700–16736 | Weakness CWE-1187: **Deprecated** / Prohibited. The successor is named only in prose (`… duplicate of CWE-908. All content has been transferred to CWE-908.`); the pre-deprecation name is kept as a Previous_Entry_Name. Base of the negative fixtures. |
| `weakness-769-deprecated-suggestion.xml` | verbatim | 5,822 | Weakness 769 L214110–214198 | Weakness CWE-769: Deprecated, with a **machine-readable** successor, `Mapping_Notes/Suggestions/Suggestion CWE_ID="774"`. One of only 2 of the 25 Deprecated weaknesses to have one. |
| `weakness-373-deprecated-critical.xml` | verbatim | 4,219 | Weakness 373 L124258–124318 | Weakness CWE-373: Deprecated. The deprecation is recorded as a Modification with `Modification_Importance` **Critical** (`Deprecated entry`), and the prose names two CWEs. |
| `category-411.xml` | verbatim | 3,981 | Category 411 L261828–261893 | Category CWE-411: Draft / Prohibited. 8 Has_Member (view 699), a Category-level Taxonomy_Mapping (PLOVER, Entry_Name only), and Submission_Version `Draft 3` (a non-numeric version). |
| `category-811-obsolete.xml` | verbatim | 3,072 | Category 811 L267269–267318 | Category CWE-811: **Obsolete**. It keeps its content and its name, and has Has_Member CWE-79 in view 809. |
| `view-709-implicit-filter.xml` | verbatim | 2,436 | View 709 L277991–278027 | View CWE-709 "Named Chains": Implicit, with Filter `/Weakness_Catalog/Weaknesses/Weakness[@Structure='Chain']`. 709 is also the View_ID of every StartsWith edge in 4.20. |
| `external-references-REF-7-44-726.xml` | verbatim | 1,688 | External_Reference REF-7 L279311–279321, External_Reference REF-44 L279561–279568, External_Reference REF-726 L281840–281849 | External_Reference REF-7, REF-44 and REF-726: all cited by CWE-79, and together they use every ExternalReferenceType child (multiple Author, Edition, Publication, gYear / gMonth / gDay, Publisher, URL, URL_Date). **CRLF line ends**, as in the source. |
| `doc-example-xhtml-lowercase.xml` | derived ✓ | 2,575 | Weakness 1187 L16700–16736 | Derived, valid: CWE-1187 with the four XHTML examples of the StructuredTextType documentation (L1329) written in lower case in Mapping_Notes/Comments. The control for the next file. |
| `neg-missing-id.xml` | derived ✗ | 2,441 | Weakness 1187 L16700–16736 | Derived, invalid: CWE-1187 with `ID` removed (a required attribute, L110). |
| `neg-duplicate-weakness-id.xml` | derived ✗ | 4,536 | Weakness 1187 L16700–16736, Weakness 1187 L16700–16736 | Derived, invalid: CWE-1187 twice, with the second Name changed, so only `uniqueWeaknessID` fires. |
| `neg-status-out-of-enumeration.xml` | derived ✗ | 2,448 | Weakness 1187 L16700–16736 | Derived, invalid: CWE-1187 with `Status="Retired"`. |
| `neg-duplicate-name-across-kinds.xml` | derived ✗ | 5,154 | Weakness 1187 L16700–16736, Category 811 L267269–267318 | Derived, invalid: CWE-1187 plus Category CWE-811 renamed to the weakness's Name. `uniqueWeaknessName` spans Weakness, Category and View. |
| `neg-doc-example-xhtml-uppercase.xml` | derived ✗ | 2,575 | Weakness 1187 L16700–16736 | Derived, invalid: the same four examples written as the documentation spells them (`<BR/>`, `<UL><LI/></UL>`, `<OL><LI/></OL>`, `<DIV …>`). Four strict-wildcard errors. |
| `neg-xhtml-in-plain-description.xml` | derived ✗ | 2,470 | Weakness 1187 L16700–16736 | Derived, invalid: an `xhtml:b` inside `Weakness/Description`, which is `xs:string`, not StructuredTextType. |

**How a fixture is built.** It starts with the 4.20 file's own first bytes, up to and including the `Weakness_Catalog` start tag. That keeps the XML declaration, `Name="CWE" Version="4.20" Date="2026-04-30"`, the default and `xhtml` namespace declarations and `xsi:schemaLocation`, all verbatim. Next comes, for each container used, `LF TAB <Container> LF`, each entry with its original indentation followed by LF, and `TAB </Container>`. It ends with `LF </Weakness_Catalog> LF`. Only the entry bytes are claimed verbatim. `entry_sha256` in `expected.yaml` is the SHA-256 of exactly `catalog_bytes` [start, end) of the 4.20 file. The derived fixtures say in `expected.yaml` exactly which bytes were changed.

**Why these.** Each kind and shape an importer must handle has one small 4.20 entry that carries the features named. The Variant (1174), Pillar (710), Class (1093), chain (692), composite (689) and the three Deprecated weaknesses are each the **smallest** 4.20 entry of their shape: 1187 is the smallest weakness overall, 769 the smaller of the two with a Suggestion, and 373 the smallest with a Critical modification. The others were chosen for a feature or a cross-fixture link: View 709 for the chain, Category 411 for its category-level Taxonomy_Mapping, Obsolete 811 for its member CWE-79, and the three references because CWE-79 cites them. CWE-79 itself was requested as the canonical Base example. It is half of the total, which is why the set stays near 150 KB rather than under it. Left out deliberately:

- CWE-184 (28.8 KB). It holds the `CanPrecede 79 Chain_ID=692` link of chain 692. `expected.yaml` X4 gives that edge with its catalog lines, so the chain can still be reconstructed: 692 = 184 → 79.
- A Graph or Explicit View with `Members`. Has_Member is exercised by both Category fixtures. 4.20 has no Obsolete or Usable **weakness** and no `Member_Of` anywhere, so those cannot be fixtures.
- CWE-546. Its own text contains the placeholder marker word that `bin/validate` forbids in distilled artifacts (CWE-546, "Suspicious Comment").

**Line ends.** The External_Reference fixture contains CRLF, because every External_Reference in 4.20 is CRLF-only. The digests assume no line-end conversion. This repository has no `.gitattributes` and `core.autocrlf` is unset, so git stores the bytes as they are.

## Re-run

From the library root, after the one-time setup in `../schema/README.md` (W3C schemas plus `.cache/w3c-xhtml/catalog.xml`):

```sh
# validation: expect exit 0 for the 14 non-neg files and exit 3 for the 6 neg-* files
for f in records/other/cwe/distilled/examples/*.xml; do
  XML_CATALOG_FILES="$PWD/.cache/w3c-xhtml/catalog.xml" xmllint --nonet --noout \
    --schema records/other/cwe/distilled/schema/cwe_schema_v7.3.xsd "$f"; echo "exit=$? $f"
done

# fixture digests: compare with sha256 in expected.yaml
shasum -a 256 records/other/cwe/distilled/examples/*.xml

# a verbatim entry against the release (CWE-79: catalog_bytes [14213467, 14288988))
tail -c +14213468 .cache/cwe-src/unz/cwec_v4.20.xml | head -c 75521 | shasum -a 256   # = entry_sha256 8a40837f…d3a0

# view 709's Filter, as written and namespace-agnostically (expected.yaml X5)
xmllint --xpath "count(/Weakness_Catalog/Weaknesses/Weakness[@Structure='Chain'])" records/other/cwe/distilled/examples/weakness-692-chain.xml   # 0
xmllint --xpath "/*[local-name()='Weakness_Catalog']/*[local-name()='Weaknesses']/*[local-name()='Weakness'][@Structure='Chain']/@ID" records/other/cwe/distilled/examples/weakness-692-chain.xml   # ID="692"
```

All of the above was run on 2026-10-08 with xmllint (libxml2 2.9.13), and the outputs are the ones recorded in `expected.yaml`.

## Licence and attribution

The XML entries in these fixtures are CWE content from CWE List 4.20, © The MITRE Corporation. They are reproduced, and in the derived fixtures modified, under the CWE Terms of Use. That licence authorises copies on the condition that MITRE's copyright designation and the licence are reproduced in each copy. Both follow verbatim, from https://cwe.mitre.org/about/termsofuse.html (retrieved 2026-10-08; the page says "Page Last Updated: July 20, 2023").

> Copyright © 2006–2026, The MITRE Corporation. CWE, CWSS, CWRAF, and the CWE logo are trademarks of The MITRE Corporation.

> CWE™ is free to use by any organization or individual for any research, development, and/or commercial purposes, per these CWE Terms of Use. Accordingly, The MITRE Corporation hereby grants you a non-exclusive, royalty-free license to use CWE for research, development, and commercial purposes. Any copy you make for such purposes is authorized on the condition that you reproduce MITRE’s copyright designation and this license in any such copy. CWE is a trademark of The MITRE Corporation. Please contact cwe@mitre.org if you require further clarification on this issue.

The schema copy in `../schema/` carries its own licence header. The disclaimers on the same page also apply.
