---
record: ecma-427
kind: index
title: "ecma-427: distilled artifacts"
extracted: "2026-10-15"
reviewed_by: ""
source_version: "ECMA-427 1st edition, December 2025"
source_digest: "037180df99e7d7c26d910dc3adb3fa07c4fb787cc4bd29e43634de3802313825"
attribution: "Contains text from ECMA-427 1st edition, © Ecma International 2025, reproduced under the Ecma copyright notice below."
---

# Distilled artifacts

FX-1 (`docs/extraction.md`) for ECMA-427, *Package-URL (PURL) specification*, 1st edition (December 2025). The source is the 40-page PDF named in `record.yaml` (SHA-256 above); it is not committed. Every quotation was taken from a `pdftotext -layout` rendering of that PDF and checked against the rendered pages where the text layer was ambiguous.

How to read the verbal forms: ECMA-427 writes its provisions in lowercase ("shall", "shall not", "should", "may"), following the ISO/IEC Directives Part 2 conventions, and never uses BCP 14 capitals except twice in licence boilerplate on p. 31. `requirements.yaml` therefore reconciles against the document's own lowercase baseline, not `bin/bcp14-count`.

| kind | file | coverage |
|---|---|---|
| normative | normative.md | 291 numbered statements, verbatim, in source order under the source's clause headings: Clauses 2, 3, 5 and 6, the Clause 6 property blocks and Tables 1 to 8, and Annex A (its constraint keywords with JSON Pointers and the "shall" sentences inside description strings). Clause 1 and Clause 4 (declared non-normative) and the informative examples are listed as excluded. Ends with a verbal-form tally per region and the source's inconsistencies. |
| requirements | requirements.yaml | 168 entries `ecma-427#R-0001` to `R-0168`: every shall, shall not, should and may statement in Clauses 2, 3, 5, 6 and Annex A, the Requirement columns of Tables 1 to 8, the "Shall be one of" enumerations and the checkable declarative constraints, except property types (the Type column and Type lines of Clause 6, the Annex A type keywords), which `messages.yaml` carries field by field. Every occurrence of shall, shall not, should and may in the document (108) is accounted for by line in `keyword_accounting`; can, cannot and must are accounted for by line in `reconciliation`. |
| schema | schema/ | `purl-type-definition.schema-1.0.json`: the Annex A JSON Schema (draft-07), verbatim, byte-identical to purl-spec tag v1.0.0, proven equal to the printed Annex A token for token. `purl.derived.abnf`: an RFC 5234 grammar for the purl string, derived from Clause 5 (the 1st edition has no grammar). Provenance, licences, smoke tests and schema defects in `schema/README.md`. |
| messages | messages.yaml | 13 structures and 65 fields: the purl string's seven components, a qualifier pair, and every object of the type-definition document, with type, required, constraints, locators and the requirement ids that constrain each field (`constrained_by`: 344 links to 147 requirements, and 7 more requirements on 4 structures as a whole; pass 3); where Tables 2 to 8, the subclauses and Annex A disagree, all three values are given. |
| protocol | (not applicable) | See `record.yaml` `distillation.not_applicable`. |
| state-machine | (not applicable) | See `record.yaml` `distillation.not_applicable`. |
| examples | examples/ | 54 fixtures: the 10 source examples verbatim, derived positives, and negatives that each break a stated rule (PURL-NEG-02 necessarily breaks three; PURL-NEG-06 is accepted, its empty value read as an absent pair), with expected and actual results from jsonschema and packageurl-python 0.17.6. `examples/run-fixtures.derived.py` reproduces every result. Each of the 63 rules the fixtures cite carries its requirement ids, and each negative and gap fixture names the ids it breaks (`breaks`, pass 3). |
| design-notes | design-notes.md | Adopt, adapt and reject items for tmodel, each mapped to an ADR or DEC with its status and grounded in a quotation, with the requirement id beside each rule it argues from (pass 3); a mapping table; numbered source defects with whether the 2nd edition fixes them; evidence from tmodel's tool runs; open questions routed to their owners. |
| verification | verification.md | The verify and cross-check record (passes 2 and 3). |

Files the library wrote rather than copied from the source carry `.derived.` in their name, or say so in their first lines.

## Copyright notice

ECMA-427's copyright notice (p. v) permits copies and derivative works that provide commentary or explanation, provided the notice and this Copyright License and Disclaimer are included. It is reproduced here verbatim for every file in this directory that quotes the standard.

> COPYRIGHT NOTICE
>
> © 2025 Ecma International
>
> By obtaining and/or copying this work, you (the licensee) agree that you have read, understood, and will comply with the following terms and conditions.
>
> This document may be copied, published and distributed to others, and certain derivative works of it may be prepared, copied, published, and distributed, in whole or in part, provided that the above copyright notice and this Copyright License and Disclaimer are included on all such copies and derivative works. The only derivative works that are permissible under this Copyright License and Disclaimer are:
>
> (i) works which incorporate all or portion of this document for the purpose of providing commentary or explanation (such as an annotated version of the document),
>
> (ii) works which incorporate all or portion of this document for the purpose of incorporating features that provide accessibility,
>
> (iii) translations of this document into languages other than English and into different formats and
>
> (iv) works by making use of this specification in standard conformant products by implementing (e.g. by copy and paste wholly or partly) the functionality therein.
>
> However, the content of this document itself may not be modified in any way, including by removing the copyright notice or references to Ecma International, except as required to translate it into languages other than English or into a different format.
>
> The official version of an Ecma International document is the English language version on the Ecma International website. In the event of discrepancies between a translated version and the official version, the official version shall govern.
>
> The limited permissions granted above are perpetual and will not be revoked by Ecma International or its successors or assigns.
>
> This document and the information contained herein is provided on an “AS IS” basis and ECMA INTERNATIONAL DISCLAIMS ALL WARRANTIES, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO ANY WARRANTY THAT THE USE OF THE INFORMATION HEREIN WILL NOT INFRINGE ANY OWNERSHIP RIGHTS OR ANY IMPLIED WARRANTIES OF MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE.

The Annex A schema is "Software" under the BSD licence printed on p. 31 of the standard; that licence text is reproduced in `schema/README.md`.
