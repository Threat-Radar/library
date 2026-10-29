---
record: nistir-7695
kind: index
title: "nistir-7695: distilled artifacts"
extracted: "2026-10-18"
reviewed_by: ""
source_version: "CPE Naming Specification Version 2.3, NIST IR 7695, August 2011"
source_digest: "01553a4638b21eda10018690b71162e91605d78eb15850f881bd0b2b691ac3f6"
attribution: "Contains text from NIST IR 7695 (August 2011), published by NIST with no copyright or licence notice; works of NIST employees are not subject to copyright in the United States (17 U.S.C. 105), but two of the three authors were not NIST staff (Acknowledgments, p. iii), so the text is not claimed to be wholly a U.S. Government work. CPE is a trademark of The MITRE Corporation (p. iii). Provenance of every other source below."
---

# nistir-7695: distilled artifacts

FX-1 (`docs/extraction.md`) for NIST Interagency Report 7695, *Common Platform Enumeration: Naming Specification Version 2.3* (August 2011). The source is the 49-page PDF named in `record.yaml` (SHA-256 above); it is not committed. Every quotation was taken from a `pdftotext -layout` rendering of that PDF (2443 lines, the line numbers in the locators) and checked against the rendered pages and the PDF's content streams where the text layer was ambiguous (figures, tables, listings, wrapped lines).

How to read the verbal forms: §1.3 adopts the uppercase keywords of RFC 2119. `bin/bcp14-count` finds 108 of them (it strips the §1.3 key-words sentence); 106 sit in requirement texts and the other 2 in the Appendix B change log. The report also says that following its pseudocode is OPTIONAL while every binding and unbinding MUST "produce the same result as the suggested pseudocode, processes, etc. would produce" (§6.1.2, §6.1.3, §6.2.2, §6.2.3), so the pseudocode's steps are extracted and bind through those four requirements.

| kind | file | coverage |
|---|---|---|
| normative | normative.md | 466 numbered statements N-0001 to N-0466, verbatim, in source order under the source's headings from §1.3 to Appendix A, including the 89 rules of the four ABNF figures, the 33 pairs of Tables 6-1 and 6-2 and every pseudocode step; each ends with its requirement ids (321) or the reason it has none (145). Excluded material is listed, and the file ends with a verbal-form tally per section, 14 disagreements between prose, ABNF and pseudocode (D-1 to D-14) and 22 other source defects (DEF-1 to DEF-22). |
| requirements | requirements.yaml | 240 entries `nistir-7695#R-0001` to `R-0240` (requirement 31, prohibition 6, recommendation 33, permission 27, constraint 124, definition 11, exemption 4, informative 4; none inferred). BCP 14: source 108, extracted 106, the other 2 in the Appendix B change log; all 37 lowercase forms accounted for by line; 74 ABNF rules (15 more in `also_at`), 23 pseudocode excerpts and 38 excluded passages with reasons. |
| schema | schema/ | The four ABNF figures verbatim at the page's columns (none valid RFC 2234 as printed), each with a repaired `.derived.abnf` twin that loads into an ABNF tool (the Figure 5-1 twin adds the prose of §5.3.2 as a grammar); `wfn.derived.schema.json`, a JSON Schema for a WFN held as JSON (the library's shape); and `cpe-naming_2.3.xsd`, the XML schema §6 calls authoritative, bytes unchanged. Provenance, repairs, digests and disagreements in `schema/README.md`. |
| messages | messages.yaml | 8 structures and 46 fields: the WFN and its eleven attributes, the attribute-value pair, the logical values, the value string of Figure 5-1, the URI binding and its packed edition, the formatted string binding and the language tag of both bindings, with type, position, separators, encoding, case, the source's rules verbatim and flags where the source disagrees with itself. `constrained_by` (pass 3): 961 links to 229 requirements, 865 on fields and 96 on structures; the 11 entries that constrain no structure are listed in `verification.md`. |
| protocol | (not applicable) | See `record.yaml` `distillation.not_applicable`. |
| state-machine | (not applicable) | See `record.yaml` `distillation.not_applicable`. |
| examples | examples/ | 177 fixtures: the 65 examples the report prints, verbatim, and 112 derived inputs (positives, negatives, disputed and edge cases, bindings, conversions and round trips), each with the expected result worked out from the text and the actual result of `run-fixtures.derived.py`, which reproduces every result; 28 findings. The 78 rules the fixtures cite carry their requirement ids (`requirements`), and each of the 77 `violates` entries, on 65 fixtures, names the ids it breaks (`breaks`; pass 3). |
| design-notes | design-notes.md | 6 adopt, 6 adapt and 6 reject items for tmodel, each grounded in a quotation and mapped to a DEC or ADR with its status, with the requirement ids of the rules it rests on wherever those rules have an entry (pass 3); a 21-row mapping table; 21 numbered source defects; evidence E1 to E11; 20 open questions routed to their owners. |
| verification | verification.md | The verify and cross-check record (passes 2 and 3): recounts, every defect found and fixed, the wiring counts and what was not checked. |

Files the library wrote rather than copied from the source carry `.derived.` in their name or say so in their first lines. The em dash (U+2014), which house style forbids in this library, is written `{U+2014}` wherever a quotation of the report contains one; each file states its other character conventions.

## Provenance

**NIST IR 7695.** The PDF carries no copyright or licence notice. It was published by NIST, and works of NIST employees are not subject to copyright in the United States (17 U.S.C. 105), but two of its three authors were not NIST staff: the Acknowledgments (p. iii) place them at The MITRE Corporation and at Scarfone Cybersecurity. The text is therefore not claimed to be wholly a U.S. Government work. Page iii also says: "CPE is a trademark of The MITRE Corporation." Every artifact that quotes the report says so at its top, in its front matter, a header comment or an `attribution` key; the fixture inputs under `examples/verbatim/` (copies of printed examples) and `examples/derived/` are bare files, described in `examples/README.md`.

**The XML schema.** `schema/cpe-naming_2.3.xsd` is the file that §6 calls "the authoritative XML binding definition". It is not printed in the report. It was fetched on 2026-10-19 from the address §6 prints, `http://scap.nist.gov/schema/cpe/2.3/cpe-naming_2.3.xsd`, which redirected to `https://csrc.nist.gov/schema/cpe/2.3/cpe-naming_2.3.xsd`: 2254 bytes, SHA-256 `d37f813fe223922fb7456751d453482009fc7075a3f5ad5e1999d075d190dd69`, kept byte for byte. Because it is not part of the PDF, the record's content digest does not cover it, and it carries no copyright or licence statement.

**The CPE 2.2 specification.** `schema/README.md` (finding F-07) quotes two grammar lines of Appendix A of the CPE 2.2 specification of The MITRE Corporation (Version 2.2, March 2009, p. 28; each page reads "©2009 The MITRE Corporation. All rights reserved."), the `string` and `PUNC` productions, to compare them with Figure 6-1. They were read from the archived copy `https://web.archive.org/web/20110727091530id_/http://cpe.mitre.org/files/cpe-specification_2.2.pdf` (38 pages, SHA-256 `e3a3a806b9ac0b7d6dc941ea741519c8669ff8b944e341bb4179ae1b4745a61d`), which the library does not hold.

**RFC text.** Short quotations of RFC 2234 (ABNF) in `schema/README.md`, `examples/expected.yaml`, the error messages of `examples/run-fixtures.derived.py` and `design-notes.md` ("ABNF strings are case-insensitive", the `defined-as`, `rulename` and `=/` lines) are from RFC 2234 as the RFC Editor publishes it at rfc-editor.org (fetched 2026-10-19, SHA-256 `dcaf77997b83a9a0bda70bc00aa4670c084087e86b4aed57f5b705dfef6eb9ca`), which reads "Copyright (C) The Internet Society (1997). All Rights Reserved." Other RFCs (RFC 2119, 3629, 3986, 5234, 5646, 7405, 8174) are cited, not quoted.

**Other sources.** `design-notes.md` also quotes one sentence of NIST IR 7697 §6.2 (library record `nistir-7697`) and the tmodel documents it cites, each with its source and commit.
