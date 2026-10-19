---
record: nistir-7695
kind: normative
title: "nistir-7695: normative statements"
extracted: "2026-10-18"
reviewed_by: ""
source_version: "Version 2.3 (NIST IR 7695, August 2011)"
source_digest: "01553a4638b21eda10018690b71162e91605d78eb15850f881bd0b2b691ac3f6"   # SHA-256 of nistir7695.pdf (49 pages)
attribution: "Quotes NIST IR 7695 (August 2011), published by NIST with no copyright or licence notice; works of NIST employees are not subject to copyright in the United States (17 U.S.C. 105), but two of the three authors were not NIST staff (Acknowledgments, p. iii), so the text is not claimed to be wholly a U.S. Government work. CPE is a trademark of The MITRE Corporation (p. iii)."
---

<!-- FX-1 pass 1 (normative agent). Every normative statement of NIST IR 7695
     (CPE Naming Specification Version 2.3), VERBATIM, with its locator, in
     source order under the source's own section headings. Verbatim source text:
     every blockquote, every fenced block (those inside blockquotes included) and
     the IN and OUT code spans of the Table 6-1 and 6-2 rows. Everything else
     (headings, numbers, locators, tags, notes, tallies, analysis) is extractor
     structure. Quotations were cut from the source rendering by anchors, not
     retyped, and then checked against it by a separate script. -->

Source: NIST Interagency Report 7695, "Common Platform Enumeration: Naming Specification Version 2.3", August 2011, by Brant A. Cheikes, David Waltermire and Karen Scarfone, Computer Security Division, NIST. PDF from https://nvlpubs.nist.gov/nistpubs/Legacy/IR/nistir7695.pdf (SHA-256 above, 49 pages). Text read from `nistir7695.txt` (`pdftotext -layout` of that PDF, 2443 lines) and checked against rendered page images and the glyph positions of `pdftotext -bbox` wherever a table, a figure, a listing or a wrapped line could be ambiguous.

## Conventions

**Verbatim.** Quoted text is the report's own characters: words, punctuation, straight and curly quotes as printed, hyphens and capitalisation. The only normalisations are these:

- A sentence the PDF wraps across lines or pages is joined. The line break and indentation become one space, and the running header ("COMMON PLATFORM ENUMERATION: NAMING SPECIFICATION VERSION 2.3"), page numbers and blank lines inside it are dropped. Where a line ends in a hyphen that belongs to the word, the join adds no space. In quoted text this happens in `valid-values` (§5.3.3.6), `non-normative` (§6.1.2), `round-trip` (§7) and `percent-encoding` (an excluded sentence of §6.1.1); the PDF also breaks `percent-encoded` (§6.1.3.3.2), `800-126` (Appendix A.2) and `otherwise-proscribed` (Appendix B) at their hyphens. Each of these words occurs unbroken elsewhere in the report.
- Runs of spaces inside a line of prose are written as one space.
- The bullet is a private-use character of the Symbol font in the text layer (U+F0B7); it prints as a bullet and is written `•`.
- The em dash (U+2014) is written `{U+2014}`, because house style forbids the character in this library. Replace each `{U+2014}` with U+2014 to recover the source. It occurs in N-0043, N-0271, N-0466 and in the excluded text listed at the end.
- The ordinal suffixes in the unbind_fs comment are superscript in the PDF ("0th", "1st", "2nd", p. 42, N-0438); they are written on the line, as the text layer has them.
- Typography is not reproduced: bold keywords in the pseudocode, the Courier font, italics and hyperlink styling.

Characters that look like errors are kept as printed and recorded as defects: the SMALL TILDE (U+02DC) in Figure 6-1 (DEF-3) and the mixed backslash conventions of the pseudocode (DEF-13).

**Code blocks.** ABNF rules and pseudocode are reproduced line for line, at the columns of the PDF page. The figures and listings are set in Courier New (10 pt in the ABNF figures, 11 pt in the pseudocode), so each word's position on the page fixes its column; the columns were measured from `pdftotext -bbox` (glyph widths 6.0 pt and 6.6 pt) and checked against the page images. `nistir7695.txt` collapses some runs of spaces and, on pages where code is the leftmost text, shifts whole lines left, so compare code blocks with runs of whitespace collapsed. Pseudocode keeps its absolute indentation: a step shows its nesting inside its function. Page headers and numbers inside a listing are dropped. Every line of every listing and every rule line of every figure belongs to exactly one statement; the captions are the figure headings.

**Locators** follow the brief: `§number heading, position / p. N / L<first>-L<last>`. `p.` is the PDF page (1 to 49). The printed page number is the PDF page minus 6 on PDF pages 7 to 49 (printed 1 to 43); PDF pages 3 to 6 are printed ii to v. `L` is the line number in `nistir7695.txt`. "Paragraph" counts the blank-line separated paragraphs of the subsection; "item" is the source's own list label.

**Statements** are numbered N-0001 onward in source order. A statement is one sentence, one list item, one table row, one ABNF rule (with all its `/=` alternatives and continuation lines), or one step of a pseudocode function. A numbered step of a prose procedure summary is one statement even when it has two sentences. A lead-in ending in a colon is its own statement and its items follow it as statements of their own. Six passages stay whole, as their locators say: the abbreviation list (§2.2), the scope exclusions of §5, the notation line of §5.1, the feature list after Figure 6-2 (§6.1.1), the field template of §6.2 and the reference list of Appendix A.1. Table rows of Tables 6-1 and 6-2 are given as list items, one per IN/OUT pair, with the cells in code spans.

**Verbal-form tags** follow the locator, in backticks:

- uppercase BCP 14 keywords as `bin/bcp14-count` counts them (MUST, MUST NOT, SHALL, SHALL NOT, SHOULD, SHOULD NOT, MAY, OPTIONAL), one entry per occurrence, in order; "MUST NOT" is never also counted as "MUST";
- lowercase must, shall, should and may (and their "not" forms) the same way, kept in lowercase. The report cites RFC 2119 only, so whether lowercase forms bind is open (DEF-22); notes say where a lowercase "may" expresses possibility;
- `none: <kind>` when the text has no verbal form. Kinds: declarative (a constraint, constant, structural fact, scope boundary or stated non-requirement without a verbal form), definition, lead-in, list item, table row, imperative, procedure step, keyword definition, ABNF rule, pseudocode;
- a code statement whose comments contain a verbal form is tagged with the forms and its kind, for example `[must, must; pseudocode]`.

Words such as "only", "solely", "cannot", "required" and "needs to" are not tagged, but every sentence that uses them to state a rule is extracted.

**Notes** marked "(inferred)" are extractor readings, not source text. "See D-n" points to a disagreement between the prose, the ABNF, the pseudocode and the examples; "See DEF-n" to another defect in the source. Both lists are at the end of the file, after the excluded material and the tally.

**Requirement ids.** Each statement ends with a "Requirement ids:" line, filled in pass 3 (cross-check). It lists the `nistir-7695#R-NNNN` ids of the `requirements.yaml` entries whose `text`, `enumeration` or `also_at` holds the statement, with a note in parentheses where the match is not one to one: an entry that holds this and other statements, a sentence split into several entries, an enumeration item, a rule printed twice, or an entry that quotes part of a pseudocode step. Otherwise the line reads "none." and gives the reason; a bare R-NNNN in a reason means `nistir-7695#R-NNNN` and points to the entry that carries the rule (for a pseudocode step, the same-result requirement through which the step binds). 321 statements map to entries and 145 give a reason; every one of the 240 entries holds at least one statement.

**Why the pseudocode is extracted.** The report calls its pseudocode and processes "non-normative information" and makes following them OPTIONAL, but requires every URI binding, URI unbinding, formatted string binding and formatted string unbinding to "produce the same result as the suggested pseudocode, processes, etc. would produce" (N-0224, N-0329, N-0405, N-0429). The result of every step is therefore normative, and every step is extracted. Where a step and the prose or the examples disagree, both are given (D-9, D-10, D-13).

## 1 Introduction

Section 1 (PDF p. 7, L187-L217) is background: what CPE is for, the layering of the CPE specifications, and one product named three ways (a WFN, a URI and a formatted string). It is listed under "Informative content excluded"; its three names are the first of the excluded examples.

### 1.1 Purpose and Scope

Section 1.1 states the subject and scope of the report. Each of its four sentences was assessed; none is extracted as a numbered statement.

**S1.** §1.1 Purpose and Scope / p. 7 / L221-L222. Constrains: no.

> This report defines the specification for CPE Naming version 2.3, including the requirements for WFNs and name bindings.

Why: it names the subject of the report.

**S2.** §1.1 Purpose and Scope / p. 7 / L222-L224. Constrains: no.

> This report also defines and explains the requirements that CPE Naming implementations, such as software and services, must meet to claim conformance with the CPE Naming version 2.3 specification.

Why: it announces that the report contains conformance requirements; the lowercase "must" describes them and imposes none itself. The requirements are in Section 4.

**S3.** §1.1 Purpose and Scope / p. 7 / L226. Constrains: no (scope boundary).

> This report only applies to version 2.3 of CPE Naming.

Why: it limits the report to CPE Naming 2.3; it does not constrain an implementation.

**S4.** §1.1 Purpose and Scope / p. 7 / L226-L227. Constrains: no (scope boundary).

> All other versions are out of the scope of this report, as are all CPE specifications other than CPE Naming.

Why: it excludes other versions and other CPE specifications from the report.

### 1.2 Document Structure

Not extracted: a list of what each section contains (PDF pp. 7-8, L231-L248).

### 1.3 Document Conventions

**N-0001.** §1.3 Document Conventions, paragraph 1 / p. 8 / L252-L254 `[none: keyword definition]`

> The key words “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, “SHALL NOT”, “SHOULD”, “SHOULD NOT”, “RECOMMENDED”, “MAY”, and “OPTIONAL” in this document are to be interpreted as described in [RFC2119].

Note: this sentence quotes all ten BCP 14 keywords. `bin/bcp14-count` removes it as boilerplate, so its ten keywords are not among the 108 (see the tally). It defines how the keywords are read and imposes no requirement itself.

Requirement ids: none. The BCP 14 keyword-definition sentence: it says how the keywords are read and binds no actor. `bin/bcp14-count` strips it, and `requirements.yaml` `excluded` lists it.

**N-0002.** §1.3 Document Conventions, paragraph 4, sentence 1 / p. 8 / L269-L270 `[none: declarative]`

> This document uses an abstract pseudocode programming language to specify expected computational behavior.

Requirement ids: none. Says what the pseudocode is for (`requirements.yaml` `excluded`); the pseudocode binds through the four same-result entries R-0148, R-0178, R-0220 and R-0225.

**N-0003.** §1.3 Document Conventions, paragraph 4, sentence 3 / p. 8 / L271-L274 `[none: declarative]`

> Note, however, that pseudocode specifications are not necessarily intended to illustrate efficient or optimized programming code; rather, their purpose is to clearly define the desired behavior, leaving it to implementers to choose the best language-specific design which respects that behavior.

Requirement ids: none. Explains the purpose of the pseudocode and leaves the design to implementers; what binds is the result (R-0148, R-0178, R-0220, R-0225).

**N-0004.** §1.3 Document Conventions, paragraph 4, sentence 4 / p. 8 / L274-L275 `[none: declarative]`

> In some cases, particularly where standardized implementations exist for a given pseudocode function, we describe the function's behavior in prose.

Note: (inferred) the functions defined only by comments (strcat, strlen, substr, reverse, is_alphanum, get_comp_uri, strchr, to_lowercase, get_comp_fs) are of this kind.

Requirement ids: none. Says that some functions are defined in prose. Those definitions are entries (R-0171, R-0172, R-0184, R-0191, R-0232) or are excluded as generic helpers (strcat, strlen, reverse, to_lowercase).

**N-0005.** §1.3 Document Conventions, paragraph 5, lead-in / p. 8 / L277 `[should]`

> When reading pseudocode the following should be kept in mind:

Note: the lowercase "should" is advice to the reader.

Requirement ids: none. Lead-in to the two reading conventions R-0001 and R-0002; its lowercase "should" is advice to the reader (`keyword_accounting`, L277).

**N-0006.** §1.3 Document Conventions, paragraph 5, bullet 1 / p. 8 / L278-L280 `[none: declarative]`

> All pseudocode functions are pass by value, meaning that any changes applied to the supplied arguments within the scope of the function do not affect the values of the variables in the caller’s scope.

Requirement ids: nistir-7695#R-0001.

**N-0007.** §1.3 Document Conventions, paragraph 5, bullet 2, sentence 1 / p. 8 / L281-L282 `[none: declarative]`

> In a few cases, the pseudocode functions reference (more or less) standard library functions, particularly to support string handling.

Requirement ids: nistir-7695#R-0002 (one entry for N-0007 and N-0008).

**N-0008.** §1.3 Document Conventions, paragraph 5, bullet 2, sentence 2 / p. 8 / L282-L284 `[none: declarative]`

> In most cases semantically equivalent functions can be found in the GNU C library, cf. http://www.gnu.org/software/libc/manual/html_node/index.html#toc_String-and-Array-Utilities.

Requirement ids: nistir-7695#R-0002 (one entry for N-0007 and N-0008).

## 2 Definitions and Abbreviations

### 2.1 Definitions

Each definition is one statement. Several are imported from ISO/IEC 19770-2, which Appendix A lists as an informative reference (DEF-20).

**N-0009.** §2.1 Definitions, term "Application" / p. 9 / L303-L305 `[none: definition]`

> Application: A system for collecting, saving, processing, and presenting data by means of a computer [ISO19770-2:4.1.1]. The term application is generally used when referring to a component of software that can be executed. The terms application and software application are often used synonymously.

Requirement ids: none. A §2.1 definition of a term the rules use; it constrains nothing, and `requirements.yaml` extracts only the definitions its rules depend on (Bind, R-0003; Unbind, R-0004).

**N-0010.** §2.1 Definitions, term "Bind" / p. 9 / L307-L309 `[may]`

> Bind: To deterministically transform a logical construct into a machine-readable representation suitable for machine interchange and processing. The result of this transformation is called a binding. A binding may also be referred to as the “bound form” of its associated logical construct.

Note: "may" here gives an alternative name ("bound form"); it grants nothing.

Requirement ids: nistir-7695#R-0003 (the entry quotes the first sentence; the other two name the result of a binding).

**N-0011.** §2.1 Definitions, term "Component" / p. 9 / L311-L313 `[none: definition]`

> Component: An entity with discrete structure, such as an assembly or software module, within a system considered at a particular level of analysis [ISO19770-2:4.1.3]. Component refers to a part of a whole, such as a component of a software product, a component of a software identification tag, etc.

Requirement ids: none. A §2.1 definition of a term the rules use; it constrains nothing, and `requirements.yaml` extracts only the definitions its rules depend on (Bind, R-0003; Unbind, R-0004).

**N-0012.** §2.1 Definitions, term "Computing Device" / p. 9 / L315-L319 `[none: definition]`

> Computing Device: A functional unit that can perform substantial computations, including numerous arithmetic operations and logic operations without human intervention [ISO19770-2:4.1.4]. A computing device can consist of a standalone unit or several interconnected units. It can also be a device that provides a specific set of functions, such as a phone or a personal organizer, or more general functions such as a laptop or desktop computer.

Requirement ids: none. A §2.1 definition of a term the rules use; it constrains nothing, and `requirements.yaml` extracts only the definitions its rules depend on (Bind, R-0003; Unbind, R-0004).

**N-0013.** §2.1 Definitions, term "Configuration Item" / p. 9 / L321-L324 `[may]`

> Configuration Item: An item or aggregation of hardware or software or both that is designed to be managed as a single entity [ISO19770-2:4.1.5]. Configuration items may vary widely in complexity, size and type, ranging from an entire system including all hardware, software and documentation, to a single module, a minor hardware component or a single software package.

Note: "may" here expresses possibility.

Requirement ids: none. A §2.1 definition of a term the rules use; it constrains nothing, and `requirements.yaml` extracts only the definitions its rules depend on (Bind, R-0003; Unbind, R-0004). Its lowercase "may" expresses possibility (`keyword_accounting`, L322).

**N-0014.** §2.1 Definitions, term "Hardware Device" / p. 9 / L326-L328 `[may, may not]`

> Hardware Device: A discrete physical component of an information technology system or infrastructure. A hardware device may or may not be a computing device (e.g., a network hub, a webcam, a keyboard, a mouse).

Note: "may or may not" here expresses possibility.

Requirement ids: none. A §2.1 definition of a term the rules use; it constrains nothing, and `requirements.yaml` extracts only the definitions its rules depend on (Bind, R-0003; Unbind, R-0004). Its "may" and "may not" express possibility (`keyword_accounting`, L327).

**N-0015.** §2.1 Definitions, term "Operating System" / p. 9 / L330-L332 `[none: definition]`

> Operating System: A computer program, implemented in either software or firmware, which acts as an intermediary between users of a computer and the computer hardware. The purpose of an operating system is to provide an environment in which a user can execute applications [Silberschatz].

Requirement ids: none. A §2.1 definition of a term the rules use; it constrains nothing, and `requirements.yaml` extracts only the definitions its rules depend on (Bind, R-0003; Unbind, R-0004).

**N-0016.** §2.1 Definitions, term "Platform" / p. 9 / L334-L336 `[none: definition]`

> Platform: A computer or hardware device and/or associated operating system, or a virtual environment, on which software can be installed or run [ISO19770-2:4.1.17]. Examples of platforms include Linux™, Microsoft Windows Vista®, and Java™.

Requirement ids: none. A §2.1 definition of a term the rules use; it constrains nothing, and `requirements.yaml` extracts only the definitions its rules depend on (Bind, R-0003; Unbind, R-0004).

**N-0017.** §2.1 Definitions, term "Product" / p. 9 / L338-L339 `[none: definition]`

> Product: A complete set of computer programs, procedures and associated documentation and data designed for delivery to a software consumer [ISO19770-2:4.1.19].

Requirement ids: none. A §2.1 definition of a term the rules use; it constrains nothing, and `requirements.yaml` extracts only the definitions its rules depend on (Bind, R-0003; Unbind, R-0004).

**N-0018.** §2.1 Definitions, term "Release" / p. 9 / L341-L342 `[none: definition]`

> Release: A collection of new and/or changed configuration items which are tested and introduced into a production environment together [ISO19770-2:4.1.21].

Requirement ids: none. A §2.1 definition of a term the rules use; it constrains nothing, and `requirements.yaml` extracts only the definitions its rules depend on (Bind, R-0003; Unbind, R-0004).

**N-0019.** §2.1 Definitions, term "Software" / p. 10 / L350-L351 `[none: definition]`

> Software: All or part of the programs, procedures, rules, and associated documentation of an information processing system [ISO19770-2:4.1.25].

Requirement ids: none. A §2.1 definition of a term the rules use; it constrains nothing, and `requirements.yaml` extracts only the definitions its rules depend on (Bind, R-0003; Unbind, R-0004).

**N-0020.** §2.1 Definitions, term "Unbind" / p. 10 / L353 `[none: definition]`

> Unbind: To deterministically transform a binding into its logical-form construct.

Requirement ids: nistir-7695#R-0004.

**N-0021.** §2.1 Definitions, term "Uniform Resource Identifier (URI)" / p. 10 / L355-L356 `[none: definition]`

> Uniform Resource Identifier (URI): A compact sequence of characters that identifies an abstract or physical resource available on the Internet. The syntax used for URIs is defined in [RFC3986].

Requirement ids: none. A §2.1 definition of a term the rules use; it constrains nothing, and `requirements.yaml` extracts only the definitions its rules depend on (Bind, R-0003; Unbind, R-0004).

### 2.2 Abbreviations

**N-0022.** §2.2 Abbreviations, the abbreviation list / p. 10 / L360-L373 `[none: definition]`

> ```text
> ABNF            Augmented Backus-Naur Form
> ASCII           American Standard Code for Information Interchange
> CPE             Common Platform Enumeration
> IEC             International Electrotechnical Commission
> IR              Interagency Report
> ISO             International Organization for Standardization
> IT              Information Technology
> ITL             Information Technology Laboratory
> NIST            National Institute of Standards and Technology
> RFC             Request for Comment
> URI             Uniform Resource Identifier
> UTF-8           Unicode Transformation Format-8
> WFN             Well-Formed CPE Name
> XML             Extensible Markup Language
> ```

Note: the space between abbreviation and expansion is as in `nistir7695.txt`; it is layout, not text.

Requirement ids: none. The abbreviation list; it constrains nothing.

## 3 Relationship to Existing Specifications and Standards

Not extracted. Section 3 (PDF pp. 11-12, L385-L448) describes how CPE 2.3 relates to the other CPE 2.3 specifications, to CPE 2.2 and to ISO/IEC 19770-2. It has no verbal form and states no rule; it is listed under "Informative content excluded".

## 4 Conformance

**N-0023.** §4 Conformance, paragraph 1, sentence 2 / p. 13 / L460-L462 `[must]`

> This section provides the high-level requirements that must be met by any implementation seeking to claim conformance with this specification.

Note: (inferred) the lowercase "must" restates that the numbered items below bind every implementation that claims conformance.

Requirement ids: none. Introduces §4; its lowercase "must" describes items 1 to 5, which are R-0005 to R-0013 (`keyword_accounting`, L461).

**N-0024.** §4 Conformance, paragraph 2 / p. 13 / L467 `[none: lead-in]`

> The following apply to all implementations claiming conformance with this specification:

Requirement ids: none. Lead-in to §4 items 1 to 5; its scope is restated in the `condition` of R-0005 and R-0012.

**N-0025.** §4 Conformance, item 1 / p. 13 / L469-L470 `[MUST]`

> An implementation MUST make an explicit claim of conformance to this specification in any documentation provided to end users.

Requirement ids: nistir-7695#R-0005.

**N-0026.** §4 Conformance, item 2 / p. 13 / L472-L474 `[MUST]`

> If the implementation produces (i.e., generates as an output) CPE names, it MUST produce syntactically correct formatted string bindings as needed to describe or identify applications, operating systems, and hardware devices (cf. 6.2).

Note: See D-2.

Requirement ids: nistir-7695#R-0006.

**N-0027.** §4 Conformance, item 3 / p. 13 / L476-L478 `[MUST, SHOULD]`

> If the implementation produces CPE names in URI form, it MUST produce URIs that adhere to the syntax rules specified in Figure 6-1, and it SHOULD produce URIs that adhere to the more constrained rules specified in Figure 6-2.

Note: See D-3.

Requirement ids: nistir-7695#R-0007, nistir-7695#R-0008 (the sentence is split into one entry per separately testable part).

**N-0028.** §4 Conformance, item 4 / p. 13 / L480-L485 `[MUST, SHOULD, SHOULD]`

> If the implementation consumes (i.e., accepts as valid input) CPE names, (a) it MUST consume syntactically correct formatted string bindings as needed to describe or identify applications, operating systems, and hardware devices (cf. 6.2); (b) it SHOULD be able to consume any CPE name that meets the syntax requirements specified in Figure 6-1 or Figure 6-2; and (c) it SHOULD be able to convert input CPE names in URI form to syntactically correct formatted string bindings (cf. 7.1).

Note: three parts, (a) to (c), each with its own keyword. See D-6.

Requirement ids: nistir-7695#R-0009, nistir-7695#R-0010, nistir-7695#R-0011 (the sentence is split into one entry per separately testable part).

**N-0029.** §4 Conformance, item 5, sentence 1 / p. 13 / L487-L488 `[OPTIONAL]`

> It is OPTIONAL for implementations to be able to convert any syntactically correct formatted string binding to a valid CPE name that meets the requirements specified in [CPE22] (cf. 7.2).

Requirement ids: nistir-7695#R-0012.

**N-0030.** §4 Conformance, item 5, sentence 2 / p. 13 / L488-L490 `[SHOULD]`

> An implementation that offers this functionality SHOULD implement the procedure defined in Section 7.2.

Requirement ids: nistir-7695#R-0013.

## 5 Well-Formed CPE Name Data Model

**N-0031.** §5 Well-Formed CPE Name Data Model, paragraph 1, sentence 2 / p. 14 / L504 `[none: declarative]`

> WFNs can be used to describe a set of products or to identify an individual product.

Requirement ids: none. Says what WFNs can be used for; it constrains nothing.

**N-0032.** §5 Well-Formed CPE Name Data Model, paragraph 2, sentence 3 / p. 14 / L514 `[none: definition]`

> To identify an entity is to describe it uniquely regardless of the domain it is in.

Requirement ids: none. Defines "to identify"; it constrains nothing.

**N-0033.** §5 Well-Formed CPE Name Data Model, paragraph 3, sentence 1 / p. 14 / L516 `[none: declarative]`

> WFNs are used to describe and identify product classes.

Requirement ids: none. Says what WFNs name; it constrains nothing.

**N-0034.** §5 Well-Formed CPE Name Data Model, paragraph 3, sentence 4 / p. 14 / L519-L520 `[none: declarative]`

> The CPE Naming specification leaves all decisions about what distinguishes identifiers and descriptions to the users.

Note: (inferred) a stated non-requirement.

Requirement ids: none. A stated non-requirement: the line between an identifier and a description is left to users. Unlike the stated non-requirements R-0015 and R-0017 it has no entry; `verification.md` (pass 3) records this as a judgement call.

**N-0035.** §5 Well-Formed CPE Name Data Model, paragraph 3, sentence 5 / p. 14 / L520-L522 `[none: declarative]`

> All names constitute descriptions of product classes, and a description becomes an identifier when it contains sufficient information to select a single entity from the universe of possibilities.

Requirement ids: none. Says when a description becomes an identifier; it constrains nothing.

**N-0036.** §5 Well-Formed CPE Name Data Model, paragraph 4, sentence 1 / p. 14 / L524 `[none: declarative]`

> WFNs are used solely for product classes.

Requirement ids: none. A scope statement (`requirements.yaml` `excluded`); its testable part is the SHOULD NOT on instance-specific data, R-0097.

**N-0037.** §5 Well-Formed CPE Name Data Model, paragraph 4, sentence 2 / p. 14 / L524-L527 `[none: declarative]`

> They cannot identify product instances, which are unique, physically discernible entities in the world, such as a specific licensed and configured installation of a product on a particular computing device owned by XYZ Corp. and physically installed in a particular location in the world.

Requirement ids: none. A scope limit (WFNs cannot identify product instances); its testable part is R-0097.

**N-0038.** §5 Well-Formed CPE Name Data Model, paragraph 4, sentence 3 and its five bullets (one statement: a scope boundary) / p. 14 / L527-L535 `[none: declarative]`

> ```text
> Other aspects of product naming and description that are outside the scope of the CPE Naming specification are:
> • Representing relationships (e.g., part of, bundled with, released before/after, same as) between products
> • Representing user-defined configurations of installed products
> • Representing entitlement/licensing information about products
> • Defining procedures and guidelines for assigning “correct” or “valid” values to attributes of product descriptions or identifiers
> • Defining procedures and guidelines for creating or maintaining valid-values lists.
> ```

Requirement ids: none. The §5 list of what lies outside the scope of the specification; a scope boundary that constrains no implementation.

### 5.1 Definitions and Notation

**N-0039.** §5.1 Definitions and Notation, paragraph 1, sentence 1 / p. 14 / L539-L540 `[none: definition]`

> A WFN is an unordered set of attribute-value pairs that collectively (a) describe or identify a software application, operating system, or hardware device, and (b) satisfy the criteria specified in Section 5.2.

Requirement ids: nistir-7695#R-0014 (one entry for N-0039 and N-0040).

**N-0040.** §5.1 Definitions and Notation, paragraph 1, sentence 2 / p. 14 / L541-L542 `[none: definition]`

> Unordered means that there is no prescribed order for the attribute-value pairs, and there is no specified relationship (hierarchical, set-theoretic, or otherwise) among attributes or attribute-value pairs.

Requirement ids: nistir-7695#R-0014 (one entry for N-0039 and N-0040).

**N-0041.** §5.1 Definitions and Notation, paragraph 2, sentence 1 / p. 14 / L544 `[none: declarative]`

> The WFN is a logical construct only.

Requirement ids: none. Says what the WFN is; it constrains nothing. The stated non-requirement of the same paragraph is R-0015.

**N-0042.** §5.1 Definitions and Notation, paragraph 2, sentence 2 / p. 14 / L544-L545 `[none: declarative]`

> The WFN is not intended to be a data format, encoding, or any other kind of machine-readable representation for machine interchange and processing.

Requirement ids: none. Says what the WFN is not (a data format); it constrains nothing. The stated non-requirement of the same paragraph is R-0015.

**N-0043.** §5.1 Definitions and Notation, paragraph 2, sentence 3 / p. 14 / L545-L547 `[none: declarative]`

> Rather, it is a conceptual data structure{U+2014}an abstract canonical form{U+2014}used to clearly and unambiguously specify desired implementations and behaviors.

Requirement ids: none. Says what the WFN is for; it constrains nothing. The stated non-requirement of the same paragraph is R-0015.

**N-0044.** §5.1 Definitions and Notation, paragraph 2, sentence 4 / p. 14 / L547-L548 `[none: declarative]`

> There is no requirement that CPE-conformant tools create or manipulate WFN-like data structures internally to their implementations.

Note: (inferred) a stated non-requirement.

Requirement ids: nistir-7695#R-0015.

**N-0045.** §5.1 Definitions and Notation, paragraph 3, sentence 1 / p. 15 / L558-L559 `[none: definition]`

> An attribute-value pair is a tuple a=v in which a (the attribute) is an alphanumeric label (used to represent a property or state of some entity), and v (the value) is the value assigned to the attribute.

Note: attribute names such as sw_edition contain the underscore; see D-14 on what the report counts as alphanumeric.

Requirement ids: none. Defines an attribute-value pair (`requirements.yaml` `excluded`); the permitted attribute names are R-0019.

**N-0046.** §5.1 Definitions and Notation, paragraph 3, sentence 2 / p. 15 / L560-L561 `[SHALL NOT, SHALL]`

> Lexical case SHALL NOT distinguish attributes from one another, e.g., the attributes Foo, foo, FOO, etc., SHALL be considered equivalent.

Requirement ids: nistir-7695#R-0016.

**N-0047.** §5.1 Definitions and Notation, paragraph 3, sentence 3 / p. 15 / L561-L562 `[none: declarative]`

> ```text
> By convention, attributes will be written in all lowercase letters, with the underscore (“_”) character used to separate distinct words within an attribute.
> ```

Note: (inferred) a writing convention for attribute names.

Requirement ids: none. A notation convention (`requirements.yaml` `excluded`); the case rule for attribute names is R-0016.

**N-0048.** §5.1 Definitions and Notation, paragraph 5 and its notation line / p. 15 / L570-L571 `[none: declarative]`

> ```text
> This document uses the following notation to illustrate WFNs:
> wfn:[a1=v1, a2=v2, …, an=vn]
> ```

Requirement ids: none. Introduces the wfn:[...] notation, which only illustrates (R-0017).

**N-0049.** §5.1 Definitions and Notation, paragraph 6, sentence 1 / p. 15 / L573-L574 `[none: declarative]`

> That is, WFNs will be notated as lists of attribute-value pairs enclosed in square brackets, prefixed with the string “wfn:”.

Requirement ids: none. Describes the notation (`requirements.yaml` `excluded`); R-0017 says no implementation has to use it.

**N-0050.** §5.1 Definitions and Notation, paragraph 6, sentence 2 / p. 15 / L574-L575 `[none: declarative]`

> This notation is used solely for the purposes of explaining and illustrating the concepts and procedures specified herein.

Requirement ids: none. Says the notation only illustrates; the stated non-requirement after it is R-0017.

**N-0051.** §5.1 Definitions and Notation, paragraph 6, sentence 3 / p. 15 / L575-L576 `[none: declarative]`

> There is no requirement that implementations represent WFNs explicitly or use this notation in any way.

Note: (inferred) a stated non-requirement.

Requirement ids: nistir-7695#R-0017.

### 5.2 WFN Attributes

**N-0052.** §5.2 WFN Attributes, lead-in / p. 15 / L580 `[MUST]`

> WFNs MUST satisfy these criteria:

Requirement ids: nistir-7695#R-0018.

**N-0053.** §5.2 WFN Attributes, criterion 1, lead-in / p. 15 / L581 `[SHALL]`

> Only the following attributes SHALL be permitted in a WFN attribute-value pair:

Requirement ids: nistir-7695#R-0019.

**N-0054.** §5.2 WFN Attributes, criterion 1, item a / p. 15 / L582 `[none: list item]`

> part

Requirement ids: nistir-7695#R-0019 (enumeration item 1).

**N-0055.** §5.2 WFN Attributes, criterion 1, item b / p. 15 / L583 `[none: list item]`

> vendor

Requirement ids: nistir-7695#R-0019 (enumeration item 2).

**N-0056.** §5.2 WFN Attributes, criterion 1, item c / p. 15 / L584 `[none: list item]`

> product

Requirement ids: nistir-7695#R-0019 (enumeration item 3).

**N-0057.** §5.2 WFN Attributes, criterion 1, item d / p. 15 / L585 `[none: list item]`

> version

Requirement ids: nistir-7695#R-0019 (enumeration item 4).

**N-0058.** §5.2 WFN Attributes, criterion 1, item e / p. 15 / L586 `[none: list item]`

> update

Requirement ids: nistir-7695#R-0019 (enumeration item 5).

**N-0059.** §5.2 WFN Attributes, criterion 1, item f / p. 15 / L587 `[none: list item]`

> edition

Requirement ids: nistir-7695#R-0019 (enumeration item 6).

**N-0060.** §5.2 WFN Attributes, criterion 1, item g / p. 15 / L588 `[none: list item]`

> language

Requirement ids: nistir-7695#R-0019 (enumeration item 7).

**N-0061.** §5.2 WFN Attributes, criterion 1, item h / p. 15 / L589 `[none: list item]`

> sw_edition

Requirement ids: nistir-7695#R-0019 (enumeration item 8).

**N-0062.** §5.2 WFN Attributes, criterion 1, item i / p. 15 / L590 `[none: list item]`

> target_sw

Requirement ids: nistir-7695#R-0019 (enumeration item 9).

**N-0063.** §5.2 WFN Attributes, criterion 1, item j / p. 15 / L591 `[none: list item]`

> target_hw

Requirement ids: nistir-7695#R-0019 (enumeration item 10).

**N-0064.** §5.2 WFN Attributes, criterion 1, item k / p. 15 / L592 `[none: list item]`

> other

Requirement ids: nistir-7695#R-0019 (enumeration item 11).

**N-0065.** §5.2 WFN Attributes, criterion 2, sentence 1 / p. 15 / L593 `[MAY]`

> Each permitted attribute MAY be used at most once in a WFN.

Note: (inferred) with "at most once" this MAY sets a limit: no attribute appears twice in one WFN.

Requirement ids: nistir-7695#R-0020.

**N-0066.** §5.2 WFN Attributes, criterion 2, sentence 2 / p. 15 / L593-L595 `[SHALL]`

> If an attribute is not used in a WFN, it is said to be unspecified, and its value SHALL default to the logical value ANY (cf. 5.3.1).

Requirement ids: nistir-7695#R-0021.

**N-0067.** §5.2 WFN Attributes, criterion 3 / p. 15 / L596 `[MUST]`

> Attribute values of WFNs MUST satisfy the requirements specified in Section 5.3.

Requirement ids: nistir-7695#R-0022.

**N-0068.** §5.2 WFN Attributes, paragraph 2 / p. 15 / L598-L599 `[none: definition]`

> The attributes sw_edition, target_sw, target_hw, and other are newly introduced in this specification and are referred to collectively as the extended attributes.

Requirement ids: none. Defines the term "extended attributes" (`requirements.yaml` `excluded`), which the packing rules use (R-0157, R-0160, R-0162).

### 5.3 WFN Attribute Values

**N-0069.** §5.3 WFN Attribute Values, lead-in / p. 15 / L603 `[SHALL]`

> Attributes of WFNs SHALL be assigned one of the following values:

Requirement ids: nistir-7695#R-0023.

**N-0070.** §5.3 WFN Attribute Values, item 1 / p. 15 / L604 `[none: list item]`

> A logical value specified in Section 5.3.1

Requirement ids: nistir-7695#R-0023 (enumeration item 1).

**N-0071.** §5.3 WFN Attribute Values, item 2 / p. 15 / L605-L606 `[none: list item]`

> A character string satisfying both (a) the requirements on string values specified in Section 5.3.2, and (b) the per-attribute value restrictions specified in Section 5.5.3.

Note: there is no Section 5.5.3; the per-attribute value restrictions are §5.3.3 (DEF-1).

Requirement ids: nistir-7695#R-0023 (enumeration item 2).

#### 5.3.1 Logical values

**N-0072.** §5.3.1 Logical values, lead-in / p. 16 / L617 `[MAY]`

> An attribute of a WFN MAY be assigned one of these logical values:

Requirement ids: nistir-7695#R-0024.

**N-0073.** §5.3.1 Logical values, item 1, sentence 1 / p. 16 / L618 `[none: list item]`

> ANY (i.e., “any value”).

Requirement ids: nistir-7695#R-0024 (enumeration item 1).

**N-0074.** §5.3.1 Logical values, item 1, sentence 2 / p. 16 / L618-L619 `[SHOULD]`

> The logical value ANY SHOULD be assigned to an attribute when there are no restrictions on acceptable values for that attribute.

Requirement ids: nistir-7695#R-0025.

**N-0075.** §5.3.1 Logical values, item 2, sentence 1 / p. 16 / L620 `[none: list item]`

> NA (i.e., “not applicable/not used”).

Requirement ids: nistir-7695#R-0024 (enumeration item 2).

**N-0076.** §5.3.1 Logical values, item 2, sentence 2 / p. 16 / L620-L622 `[SHOULD]`

> The logical value NA SHOULD be assigned when there is no legal or meaningful value for that attribute, or when that attribute is not used as part of the description.

Requirement ids: nistir-7695#R-0026 (one entry for N-0076 and N-0077).

**N-0077.** §5.3.1 Logical values, item 2, sentence 3 / p. 16 / L622 `[none: declarative]`

> This includes the situation in which an attribute has an obtainable value that is null.

Requirement ids: nistir-7695#R-0026 (one entry for N-0076 and N-0077).

**N-0078.** §5.3.1 Logical values, paragraph 2 / p. 16 / L624-L625 `[none: declarative]`

> In WFNs, these logical values will be written in all uppercase characters, without surrounding quotation marks, on the right side of the equal sign, as in these examples:

Note: notation only; the two examples (L626-L627) are excluded.

Requirement ids: none. A notation convention for the wfn:[...] examples (`requirements.yaml` `excluded`).

#### 5.3.2 Restrictions on attribute-value strings

**N-0079.** §5.3.2 Restrictions on attribute-value strings, paragraph 1 / p. 16 / L631-L633 `[SHALL]`

> Value strings assigned to attributes of WFNs SHALL be non-empty contiguous strings of bytes encoded using printable Unicode Transformation Format-8 (UTF-8) characters with hexadecimal values between x00 and x7F [RFC3629].

Note: See DEF-2 on the range "between x00 and x7F".

Requirement ids: nistir-7695#R-0027.

**N-0080.** §5.3.2 Restrictions on attribute-value strings, paragraph 2, sentence 1 / p. 16 / L635 `[none: declarative]`

> In WFNs, attribute-value strings will be enclosed in double quotes as in the examples below.

Note: notation only; the two examples (L637-L638) are excluded.

Requirement ids: none. A notation convention for the wfn:[...] examples (`requirements.yaml` `excluded`).

**N-0081.** §5.3.2 Restrictions on attribute-value strings, paragraph 2, sentence 2 / p. 16 / L635-L636 `[none: declarative]`

> The quotation marks are, of course, not considered part of the string values themselves.

Requirement ids: none. Part of the notation convention for the examples (`requirements.yaml` `excluded`).

**N-0082.** §5.3.2 Restrictions on attribute-value strings, lead-in / p. 16 / L640 `[SHALL]`

> Value strings in WFNs SHALL satisfy all of the following requirements:

Requirement ids: nistir-7695#R-0028.

**N-0083.** §5.3.2 Restrictions on attribute-value strings, item 1 / p. 16 / L641-L642 `[MAY]`

> Uppercase letters, lowercase letters or digit characters MAY be used (ASCII x41-x5a, x30-x39 and x61-x7a).

Requirement ids: nistir-7695#R-0029.

**N-0084.** §5.3.2 Restrictions on attribute-value strings, item 2 / p. 16 / L643-L644 `[MAY, SHOULD, SHALL NOT]`

> The underscore (x5f) MAY be used, and it SHOULD be used in place of whitespace characters (which SHALL NOT be used).

Requirement ids: nistir-7695#R-0030, nistir-7695#R-0031, nistir-7695#R-0032 (the sentence is split into one entry per separately testable part).

**N-0085.** §5.3.2 Restrictions on attribute-value strings, item 3, sentence 1 / p. 16 / L645 `[MAY]`

> The backslash (x5c) MAY be used, and is designated the escape character.

Requirement ids: nistir-7695#R-0033.

**N-0086.** §5.3.2 Restrictions on attribute-value strings, item 3, sentence 2 / p. 16 / L645-L647 `[SHOULD]`

> It SHOULD be used in a value string when required to modify the interpretation of the character that immediately follows (see below).

Requirement ids: nistir-7695#R-0034.

**N-0087.** §5.3.2 Restrictions on attribute-value strings, item 3, sentence 3 / p. 16 / L647-L648 `[none: definition]`

> In these circumstances, the character following the backslash is said to be quoted.

Requirement ids: none. Defines "quoted"; the quoting rules themselves are R-0034, R-0037, R-0044 and Figure 5-1 (R-0055, R-0056).

**N-0088.** §5.3.2 Restrictions on attribute-value strings, item 4, sentence 1 / p. 16 / L649-L650 `[MAY]`

> The asterisk (x2a) and the question mark (x3f) MAY be used, and are designated special characters.

Requirement ids: nistir-7695#R-0035.

**N-0089.** §5.3.2 Restrictions on attribute-value strings, item 4, sentence 2 / p. 16 / L650-L651 `[MAY]`

> These two characters MAY be assigned special interpretations by other CPE specifications.

Requirement ids: nistir-7695#R-0036.

**N-0090.** §5.3.2 Restrictions on attribute-value strings, item 4, sentence 3 / p. 16 / L651-L652 `[none: imperative]`

> To block special interpretation of these characters, precede them with the escape character, otherwise leave them unquoted in the value string.

Note: (inferred) an instruction without a verbal form.

Requirement ids: nistir-7695#R-0037.

**N-0091.** §5.3.2 Restrictions on attribute-value strings, item 4, sentence 4 / p. 16 / L652-L653 `[MAY]`

> A special character MAY be included at the beginning of an otherwise non-empty value string, and/or at the end of the string.

Requirement ids: nistir-7695#R-0038.

**N-0092.** §5.3.2 Restrictions on attribute-value strings, item 4, sentence 5 / p. 16 / L654 `[MUST NOT]`

> A special character MUST NOT be embedded within a value string.

Note: See D-10.

Requirement ids: nistir-7695#R-0039.

**N-0093.** §5.3.2 Restrictions on attribute-value strings, item 4, sentence 6 / p. 16 / L654-L655 `[MUST NOT]`

> A single asterisk MUST NOT be used by itself as an attribute value.

Note: See D-1.

Requirement ids: nistir-7695#R-0040.

**N-0094.** §5.3.2 Restrictions on attribute-value strings, item 4, sentence 7 / p. 16 / L655-L656 `[MUST NOT]`

> The asterisk MUST NOT be used more than once in sequence.

Note: See D-1.

Requirement ids: nistir-7695#R-0041.

**N-0095.** §5.3.2 Restrictions on attribute-value strings, item 4, sentence 8 / p. 16 / L656 `[MAY]`

> A single question mark MAY be used by itself as an attribute value.

Note: See D-2.

Requirement ids: nistir-7695#R-0042.

**N-0096.** §5.3.2 Restrictions on attribute-value strings, item 4, sentence 9 / p. 16 / L656-L657 `[MAY]`

> The question mark MAY be used more than once in sequence.

Note: See D-2 on a value made only of question marks.

Requirement ids: nistir-7695#R-0043.

**N-0097.** §5.3.2 Restrictions on attribute-value strings, item 5 / p. 16 / L658-L660 `[MUST]`

> All other printable non-alphanumeric characters (i.e., all punctuation marks, brackets, delimiters and other special purpose symbols, except for the special characters defined above) MUST be quoted when embedded in value strings.

Note: See D-14 on which characters "All other" covers.

Requirement ids: nistir-7695#R-0044.

**N-0098.** §5.3.2 Restrictions on attribute-value strings, item 6 / p. 16 / L661 `[MUST NOT]`

> A quoted hyphen MUST NOT be used by itself as a value string.

Requirement ids: nistir-7695#R-0045.

**N-0099.** §5.3.2 Restrictions on attribute-value strings, paragraph 4 / p. 17 / L671-L672 `[none: declarative]`

> These requirements are summarized by the Augmented Backus-Naur Form (ABNF) grammar [RFC2234] for avstring shown in Figure 5-1.

Note: (inferred) "summarized" makes the prose items the governing text where Figure 5-1 differs (D-1).

Requirement ids: nistir-7695#R-0046.

##### Figure 5-1. ABNF Grammar for Attribute-Value Strings (p. 17, L675-L697)

Eighteen rules, quoted at the columns of the PDF figure; the rule names start at the figure's left edge.

**N-0100.** §5.3.2 Restrictions on attribute-value strings, Figure 5-1, rule avstring / p. 17 / L675 `[none: ABNF rule]`

```abnf
avstring      = ( body / ( spec_chrs *body2 )) *1spec_chrs
```

Note: See D-1 and D-2.

Requirement ids: nistir-7695#R-0047.

**N-0101.** §5.3.2 Restrictions on attribute-value strings, Figure 5-1, rule spec_chrs / p. 17 / L676 `[none: ABNF rule]`

```abnf
spec_chrs     = 1*spec1 / spec2
```

Requirement ids: nistir-7695#R-0048.

**N-0102.** §5.3.2 Restrictions on attribute-value strings, Figure 5-1, rule spec1 / p. 17 / L677 `[none: ABNF rule]`

```abnf
spec1         = "?"
```

Requirement ids: nistir-7695#R-0049.

**N-0103.** §5.3.2 Restrictions on attribute-value strings, Figure 5-1, rule spec2 / p. 17 / L678 `[none: ABNF rule]`

```abnf
spec2         = "*"
```

Requirement ids: nistir-7695#R-0050.

**N-0104.** §5.3.2 Restrictions on attribute-value strings, Figure 5-1, rule body / p. 17 / L679 `[none: ABNF rule]`

```abnf
body          = ( body1 *body2 ) / 2*body2
```

Requirement ids: nistir-7695#R-0051.

**N-0105.** §5.3.2 Restrictions on attribute-value strings, Figure 5-1, rule body1 / p. 17 / L680 `[none: ABNF rule]`

```abnf
body1         = unreserved / quoted1
```

Requirement ids: nistir-7695#R-0052.

**N-0106.** §5.3.2 Restrictions on attribute-value strings, Figure 5-1, rule body2 / p. 17 / L681 `[none: ABNF rule]`

```abnf
body2         = unreserved / quoted2
```

Requirement ids: nistir-7695#R-0053.

**N-0107.** §5.3.2 Restrictions on attribute-value strings, Figure 5-1, rule unreserved / p. 17 / L682 `[none: ABNF rule]`

```abnf
unreserved    = ALPHA / DIGIT / "_"
```

Requirement ids: nistir-7695#R-0054.

**N-0108.** §5.3.2 Restrictions on attribute-value strings, Figure 5-1, rule quoted1 / p. 17 / L683 `[none: ABNF rule]`

```abnf
quoted1       = escape (escape / special / punc-no-dash)
```

Requirement ids: nistir-7695#R-0055.

**N-0109.** §5.3.2 Restrictions on attribute-value strings, Figure 5-1, rule quoted2 / p. 17 / L684 `[none: ABNF rule]`

```abnf
quoted2       = escape (escape / special / punc-w-dash)
```

Requirement ids: nistir-7695#R-0056.

**N-0110.** §5.3.2 Restrictions on attribute-value strings, Figure 5-1, rule escape / p. 17 / L685 `[none: ABNF rule]`

```abnf
escape        = "\"
```

Requirement ids: nistir-7695#R-0057.

**N-0111.** §5.3.2 Restrictions on attribute-value strings, Figure 5-1, rule special / p. 17 / L686 `[none: ABNF rule]`

```abnf
special       = spec1 / spec2
```

Requirement ids: nistir-7695#R-0058.

**N-0112.** §5.3.2 Restrictions on attribute-value strings, Figure 5-1, rule dash / p. 17 / L687 `[none: ABNF rule]`

```abnf
dash          = "-"
```

Requirement ids: nistir-7695#R-0059.

**N-0113.** §5.3.2 Restrictions on attribute-value strings, Figure 5-1, rule punc-no-dash / p. 17 / L688-L691 `[none: ABNF rule]`

```abnf
punc-no-dash  = "!" / DQUOTE / "#"/ "$"/ "%" / "&" / "'" /
                "(" / ")" / "+" / "," / "." / "/" /
                ":" / ";" / "<" / "=" / ">" / "@" / "[" /
                "]" / "^" / "`" / "{" / "|" / "}" / "~"
```

Requirement ids: nistir-7695#R-0060.

**N-0114.** §5.3.2 Restrictions on attribute-value strings, Figure 5-1, rule punc-w-dash / p. 17 / L692 `[none: ABNF rule]`

```abnf
punc-w-dash   = punc-no-dash / dash
```

Requirement ids: nistir-7695#R-0061.

**N-0115.** §5.3.2 Restrictions on attribute-value strings, Figure 5-1, rule DQUOTE / p. 17 / L693 `[none: ABNF rule]`

```abnf
DQUOTE        = %x22 ; double quote
```

Requirement ids: nistir-7695#R-0062.

**N-0116.** §5.3.2 Restrictions on attribute-value strings, Figure 5-1, rule ALPHA / p. 17 / L694 `[none: ABNF rule]`

```abnf
ALPHA         = %x41-5a / %x61-7A   ; A-Z or a-z
```

Requirement ids: nistir-7695#R-0063.

**N-0117.** §5.3.2 Restrictions on attribute-value strings, Figure 5-1, rule DIGIT / p. 17 / L695 `[none: ABNF rule]`

```abnf
DIGIT         = %x30-39    ; 0-9
```

Requirement ids: nistir-7695#R-0064.

The thirteen examples of allowable value strings after the figure (L699-L712) are excluded.

#### 5.3.3 Per-attribute value restrictions

##### 5.3.3.1 Part

**N-0118.** §5.3.3.1 Part, lead-in / p. 18 / L729 `[SHALL]`

> The part attribute SHALL have one of these three string values:

Note: See D-4.

Requirement ids: nistir-7695#R-0065.

**N-0119.** §5.3.3.1 Part, bullet 1 / p. 18 / L730 `[none: list item]`

> The value “a”, when the WFN is for a class of applications.

Requirement ids: nistir-7695#R-0065 (enumeration item 1).

**N-0120.** §5.3.3.1 Part, bullet 2 / p. 18 / L731 `[none: list item]`

> The value “o”, when the WFN is for a class of operating systems.

Requirement ids: nistir-7695#R-0065 (enumeration item 2).

**N-0121.** §5.3.3.1 Part, bullet 3 / p. 18 / L732 `[none: list item]`

> The value “h”, when the WFN is for a class of hardware devices.

Requirement ids: nistir-7695#R-0065 (enumeration item 3).

##### 5.3.3.2 Vendor

**N-0122.** §5.3.3.2 Vendor, sentence 1 / p. 18 / L736-L737 `[SHOULD]`

> Values for this attribute SHOULD describe or identify the person or organization that manufactured or created the product.

Requirement ids: nistir-7695#R-0066.

**N-0123.** §5.3.3.2 Vendor, sentence 2 / p. 18 / L737-L738 `[SHOULD, MAY]`

> Values for this attribute SHOULD be selected from an attribute-specific valid-values list, which MAY be defined by other specifications that utilize this specification.

Requirement ids: nistir-7695#R-0067.

**N-0124.** §5.3.3.2 Vendor, sentence 3 / p. 18 / L738-L739 `[MAY]`

> Any character string meeting the requirements for WFNs (cf. 5.3.2) MAY be specified as the value of the attribute.

Requirement ids: nistir-7695#R-0068.

##### 5.3.3.3 Product

**N-0125.** §5.3.3.3 Product, sentence 1 / p. 18 / L743-L744 `[SHOULD]`

> Values for this attribute SHOULD describe or identify the most common and recognizable title or name of the product.

Requirement ids: nistir-7695#R-0069.

**N-0126.** §5.3.3.3 Product, sentence 2 / p. 18 / L744-L745 `[SHOULD, MAY]`

> Values for this attribute SHOULD be selected from an attribute-specific valid-values list, which MAY be defined by other specifications that utilize this specification.

Requirement ids: nistir-7695#R-0070.

**N-0127.** §5.3.3.3 Product, sentence 3 / p. 18 / L745-L746 `[MAY]`

> Any character string meeting the requirements for WFNs (cf. 5.3.2) MAY be specified as the value of the attribute.

Requirement ids: nistir-7695#R-0071.

##### 5.3.3.4 Version

**N-0128.** §5.3.3.4 Version, sentence 1 / p. 18 / L750-L751 `[SHOULD]`

> Values for this attribute SHOULD be vendor-specific alphanumeric strings characterizing the particular release version of the product.

Requirement ids: nistir-7695#R-0072.

**N-0129.** §5.3.3.4 Version, sentence 2 / p. 18 / L751-L753 `[SHOULD, SHOULD NOT]`

> Version information SHOULD be copied directly (with escaping of printable non-alphanumeric characters as required) from discoverable data and SHOULD NOT be truncated or otherwise modified.

Requirement ids: nistir-7695#R-0073.

**N-0130.** §5.3.3.4 Version, sentence 3 / p. 18 / L753-L754 `[MAY]`

> Any character string meeting the requirements for WFNs (cf. 5.3.2) MAY be specified as the value of the attribute.

Requirement ids: nistir-7695#R-0074.

##### 5.3.3.5 Update

**N-0131.** §5.3.3.5 Update, sentence 1 / p. 18 / L758-L759 `[SHOULD]`

> Values for this attribute SHOULD be vendor-specific alphanumeric strings characterizing the particular update, service pack, or point release of the product.

Requirement ids: nistir-7695#R-0075.

**N-0132.** §5.3.3.5 Update, sentence 2 / p. 18 / L759-L761 `[SHOULD, MAY]`

> Values for this attribute SHOULD be selected from an attribute-specific valid-values list, which MAY be defined by other specifications that utilize this specification.

Requirement ids: nistir-7695#R-0076.

**N-0133.** §5.3.3.5 Update, sentence 3 / p. 18 / L761-L762 `[MAY]`

> Any character string meeting the requirements for WFNs (cf. 5.3.2) MAY be specified as the value of the attribute.

Requirement ids: nistir-7695#R-0077.

##### 5.3.3.6 Edition

**N-0134.** §5.3.3.6 Edition, paragraph 1, sentence 1 / p. 18 / L766-L768 `[SHOULD]`

> The edition attribute is considered deprecated in this specification, and it SHOULD be assigned the logical value ANY except where required for backward compatibility with version 2.2 of the CPE specification.

Requirement ids: nistir-7695#R-0078.

**N-0135.** §5.3.3.6 Edition, paragraph 1, sentence 2 / p. 18 / L768 `[none: definition]`

> This attribute is referred to as the “legacy edition” attribute.

Requirement ids: none. Gives the edition attribute a second name ("legacy edition"); the rule of the paragraph is R-0078.

**N-0136.** §5.3.3.6 Edition, paragraph 2, sentence 1 / p. 18 / L770-L771 `[SHOULD]`

> If this attribute is used, values for this attribute SHOULD capture edition-related terms applied by the vendor to the product.

Requirement ids: nistir-7695#R-0079.

**N-0137.** §5.3.3.6 Edition, paragraph 2, sentence 2 / p. 18 / L771-L772 `[SHOULD, MAY]`

> Values for this attribute SHOULD be selected from an attribute-specific valid-values list, which MAY be defined by other specifications that utilize this specification.

Requirement ids: nistir-7695#R-0080.

**N-0138.** §5.3.3.6 Edition, paragraph 2, sentence 3 / p. 18 / L772-L773 `[MAY]`

> Any character string meeting the requirements for WFNs (cf. 5.3.2) MAY be specified as the value of the attribute.

Requirement ids: nistir-7695#R-0081.

##### 5.3.3.7 SW_Edition

**N-0139.** §5.3.3.7 SW_Edition, sentence 1 / p. 19 / L785-L786 `[SHOULD]`

> Values for this attribute SHOULD characterize how the product is tailored to a particular market or class of end users.

Requirement ids: nistir-7695#R-0082.

**N-0140.** §5.3.3.7 SW_Edition, sentence 2 / p. 19 / L786-L787 `[SHOULD, MAY]`

> Values for this attribute SHOULD be selected from an attribute-specific valid-values list, which MAY be defined by other specifications that utilize this specification.

Requirement ids: nistir-7695#R-0083.

**N-0141.** §5.3.3.7 SW_Edition, sentence 3 / p. 19 / L787-L788 `[MAY]`

> Any character string meeting the requirements for WFNs (cf. 5.3.2) MAY be specified as the value of the attribute.

Requirement ids: nistir-7695#R-0084.

##### 5.3.3.8 Target_SW

**N-0142.** §5.3.3.8 Target_SW, sentence 1 / p. 19 / L792-L793 `[SHOULD]`

> Values for this attribute SHOULD characterize the software computing environment within which the product operates.

Requirement ids: nistir-7695#R-0085.

**N-0143.** §5.3.3.8 Target_SW, sentence 2 / p. 19 / L793-L794 `[SHOULD, MAY]`

> Values for this attribute SHOULD be selected from an attribute-specific valid-values list, which MAY be defined by other specifications that utilize this specification.

Requirement ids: nistir-7695#R-0086.

**N-0144.** §5.3.3.8 Target_SW, sentence 3 / p. 19 / L794-L795 `[MAY]`

> Any character string meeting the requirements for WFNs (cf. 5.3.2) MAY be specified as the value of the attribute.

Requirement ids: nistir-7695#R-0087.

##### 5.3.3.9 Target_HW

**N-0145.** §5.3.3.9 Target_HW, sentence 1 / p. 19 / L799-L800 `[SHOULD]`

> Values for this attribute SHOULD characterize the instruction set architecture (e.g., x86) on which the product being described or identified by the WFN operates.

Requirement ids: nistir-7695#R-0088.

**N-0146.** §5.3.3.9 Target_HW, sentence 2 / p. 19 / L800-L802 `[SHALL]`

> Bytecode-intermediate languages, such as Java bytecode for the Java Virtual Machine or Microsoft Common Intermediate Language for the Common Language Runtime virtual machine, SHALL be considered instruction set architectures.

Requirement ids: nistir-7695#R-0089.

**N-0147.** §5.3.3.9 Target_HW, sentence 3 / p. 19 / L802-L804 `[SHOULD, MAY]`

> Values for this attribute SHOULD be selected from an attribute-specific valid-values list, which MAY be defined by other specifications that utilize this specification.

Requirement ids: nistir-7695#R-0090.

**N-0148.** §5.3.3.9 Target_HW, sentence 4 / p. 19 / L804-L805 `[MAY]`

> Any character string meeting the requirements for WFNs (cf. 5.3.2) MAY be specified as the value of the attribute.

Requirement ids: nistir-7695#R-0091.

##### 5.3.3.10 Language

**N-0149.** §5.3.3.10 Language, sentence 1 / p. 19 / L809-L810 `[SHALL, SHOULD]`

> Values for this attribute SHALL be valid language tags as defined by [RFC5646], and SHOULD be used to define the language supported in the user interface of the product being described.

Note: See D-5.

Requirement ids: nistir-7695#R-0092, nistir-7695#R-0093 (the sentence is split into one entry per separately testable part).

**N-0150.** §5.3.3.10 Language, sentence 2 / p. 19 / L810-L811 `[MAY, SHOULD]`

> Although any valid language tag MAY be used, only tags containing language and region codes SHOULD be used.

Note: See D-5.

Requirement ids: nistir-7695#R-0094, nistir-7695#R-0095 (the sentence is split into one entry per separately testable part).

##### 5.3.3.11 Other

**N-0151.** §5.3.3.11 Other, sentence 1 / p. 19 / L815-L816 `[SHOULD]`

> Values for this attribute SHOULD capture any other general descriptive or identifying information which is vendor- or product-specific and which does not logically fit in any other attribute value.

Requirement ids: nistir-7695#R-0096.

**N-0152.** §5.3.3.11 Other, sentence 2 / p. 19 / L816-L818 `[SHOULD NOT]`

> Values SHOULD NOT be used for storing instance-specific data (e.g., globally-unique identifiers or Internet Protocol addresses).

Requirement ids: nistir-7695#R-0097.

**N-0153.** §5.3.3.11 Other, sentence 3 / p. 19 / L818-L819 `[SHOULD, MAY]`

> Values for this attribute SHOULD be selected from a valid-values list that is refined over time; this list MAY be defined by other specifications that utilize this specification.

Requirement ids: nistir-7695#R-0098.

**N-0154.** §5.3.3.11 Other, sentence 4 / p. 19 / L819-L820 `[MAY]`

> Any character string meeting the requirements for WFNs (cf. 5.3.2) MAY be specified as the value of the attribute.

Requirement ids: nistir-7695#R-0099.

### 5.4 Operations on WFNs

**N-0155.** §5.4 Operations on WFNs, paragraph 1, sentence 1 / p. 19 / L824 `[none: declarative]`

> Three functions are defined over WFNs: new, get, and set.

Requirement ids: none. Introduces §5.4; the three functions are R-0100 to R-0102.

#### 5.4.1 Function new()

**N-0156.** §5.4.1 Function new(), sentence 1 / p. 19 / L829 `[none: declarative]`

> The new() function takes no arguments.

Requirement ids: nistir-7695#R-0100 (one entry for N-0156 and N-0157).

**N-0157.** §5.4.1 Function new(), sentence 2 / p. 19 / L829-L830 `[none: declarative]`

> It returns an empty WFN (a WFN containing no attribute-value pairs).

Requirement ids: nistir-7695#R-0100 (one entry for N-0156 and N-0157).

#### 5.4.2 Function get(w,a)

**N-0158.** §5.4.2 Function get(w,a), sentence 1 / p. 20 / L844 `[none: declarative]`

> The get(w,a) function takes two arguments, a WFN w and an attribute a, and returns the value of a.

Requirement ids: nistir-7695#R-0101 (one entry for N-0158 and N-0159).

**N-0159.** §5.4.2 Function get(w,a), sentence 2 / p. 20 / L844-L845 `[none: declarative]`

> If the attribute a is unspecified in w, get(w,a) returns the default value ANY.

Requirement ids: nistir-7695#R-0101 (one entry for N-0158 and N-0159).

#### 5.4.3 Function set(w,a,v)

**N-0160.** §5.4.3 Function set(w,a,v), sentence 1 / p. 20 / L855 `[none: declarative]`

> The set(w,a,v) function takes three arguments, a WFN w, an attribute a, and a value v.

Requirement ids: nistir-7695#R-0102 (one entry for N-0160 to N-0164).

**N-0161.** §5.4.3 Function set(w,a,v), sentence 2 / p. 20 / L855-L856 `[none: declarative]`

> If the attribute a is unspecified in w, set(w,a,v) adds the attribute-value pair a=v to w.

Requirement ids: nistir-7695#R-0102 (one entry for N-0160 to N-0164).

**N-0162.** §5.4.3 Function set(w,a,v), sentence 3 / p. 20 / L856-L857 `[none: declarative]`

> If the attribute a is specified in w, set(w,a,v) replaces its value with v.

Requirement ids: nistir-7695#R-0102 (one entry for N-0160 to N-0164).

**N-0163.** §5.4.3 Function set(w,a,v), sentence 4 / p. 20 / L857-L858 `[none: declarative]`

> If v is nil, set(w,a,v) deletes a from w if a is specified in w, otherwise has no effect.

Requirement ids: nistir-7695#R-0102 (one entry for N-0160 to N-0164).

**N-0164.** §5.4.3 Function set(w,a,v), sentence 5 / p. 20 / L858 `[none: declarative]`

> The function always returns the new value of w.

Requirement ids: nistir-7695#R-0102 (one entry for N-0160 to N-0164).

The examples of new(), get() and set() (L839-L840, L847-L851, L860-L866) are excluded.

### 5.5 WFN Examples

Not extracted: the section says of itself that it only illustrates (L870-L872); its five WFNs (L874-L900) are listed under "Informative content excluded".

## 6 Name Binding and Unbinding

**N-0165.** §6 Name Binding and Unbinding, paragraph 2, sentence 1 / p. 22 / L916 `[none: declarative]`

> This section defines the formats for acceptable bound CPE names.

Requirement ids: none. Describes §6; the sentence after it, on the XML schema, is R-0103.

**N-0166.** §6 Name Binding and Unbinding, paragraph 2, sentence 2 / p. 22 / L916-L918 `[none: declarative]`

> The XML schema implementation of these format requirements, which is the authoritative XML binding definition, can be found at http://scap.nist.gov/schema/cpe/2.3/cpe-naming_2.3.xsd.

Note: See DEF-19.

Requirement ids: nistir-7695#R-0103.

### 6.1 URI Binding

**N-0167.** §6.1 URI Binding, paragraph 1, sentence 2 / p. 22 / L923-L924 `[none: declarative]`

> Section 5.1 of [CPE22] specifies that a CPE name is a percent-encoded URI [RFC3986] with each name having the URI scheme name “cpe:”.

Requirement ids: none. Reports what [CPE22] §5.1 says; it states no rule of this specification.

**N-0168.** §6.1 URI Binding, paragraph 1, sentence 3 / p. 22 / L924-L925 `[none: declarative]`

> The procedure defined here for creating a URI binding ensures that when a WFN is bound to a URI, it will satisfy the requirements of [CPE22] for CPE names.

Note: See D-2 and D-3: the claim fails for some well-formed WFNs.

Requirement ids: nistir-7695#R-0104.

#### 6.1.1 URI Binding Syntax

**N-0169.** §6.1.1 URI Binding Syntax, paragraph 1, sentence 1 / p. 22 / L931 `[none: declarative]`

> The syntax of legal CPE v2.2 URIs is specified in Appendix A of [CPE22].

Requirement ids: none. Points to Appendix A of [CPE22]; Figure 6-1's rules are R-0105 to R-0120 (with R-0064).

**N-0170.** §6.1.1 URI Binding Syntax, paragraph 1, sentence 2 / p. 22 / L931-L932 `[none: declarative]`

> For ease of reference it is shown in Figure 6-1, using ABNF notation [RFC2234].

Requirement ids: none. Says that Figure 6-1 shows the [CPE22] syntax; the figure's rules are R-0105 to R-0120 (with R-0064).

##### Figure 6-1. ABNF for v2.2-Compatible URI Binding (p. 22, L934-L961)

Seventeen rules, at the columns of the PDF figure.

**N-0171.** §6.1.1 URI Binding Syntax, Figure 6-1, rule cpe-name / p. 22 / L934 `[none: ABNF rule]`

```abnf
cpe-name          = "cpe:/" component-list
```

Requirement ids: nistir-7695#R-0105.

**N-0172.** §6.1.1 URI Binding Syntax, Figure 6-1, rule component-list / p. 22 / L936-L945 `[none: ABNF rule]`

```abnf
component-list    = part ":" vendor ":" product ":" version ":" update ":"
                    edition ":" lang
component-list    /= part ":" vendor ":" product ":" version ":" update ":"
                     edition
component-list    /= part ":" vendor ":" product ":" version ":" update
component-list    /= part ":" vendor ":" product ":" version
component-list    /= part ":" vendor ":" product
component-list    /= part ":" vendor
component-list    /= part
component-list    /= empty
```

Requirement ids: nistir-7695#R-0106.

**N-0173.** §6.1.1 URI Binding Syntax, Figure 6-1, rule part / p. 22 / L946 `[none: ABNF rule]`

```abnf
part              = "h" / "o" / "a" / empty
```

Note: See D-3 and D-4.

Requirement ids: nistir-7695#R-0107.

**N-0174.** §6.1.1 URI Binding Syntax, Figure 6-1, rule vendor / p. 22 / L947 `[none: ABNF rule]`

```abnf
vendor            = string
```

Requirement ids: nistir-7695#R-0108.

**N-0175.** §6.1.1 URI Binding Syntax, Figure 6-1, rule product / p. 22 / L948 `[none: ABNF rule]`

```abnf
product           = string
```

Requirement ids: nistir-7695#R-0109.

**N-0176.** §6.1.1 URI Binding Syntax, Figure 6-1, rule version / p. 22 / L949 `[none: ABNF rule]`

```abnf
version           = string
```

Requirement ids: nistir-7695#R-0110.

**N-0177.** §6.1.1 URI Binding Syntax, Figure 6-1, rule update / p. 22 / L950 `[none: ABNF rule]`

```abnf
update            = string
```

Requirement ids: nistir-7695#R-0111.

**N-0178.** §6.1.1 URI Binding Syntax, Figure 6-1, rule edition / p. 22 / L951 `[none: ABNF rule]`

```abnf
edition           = string
```

Requirement ids: nistir-7695#R-0112.

**N-0179.** §6.1.1 URI Binding Syntax, Figure 6-1, rule lang / p. 22 / L952 `[none: ABNF rule]`

```abnf
lang              = LANGTAG / empty
```

Note: See D-3 and D-5.

Requirement ids: nistir-7695#R-0113.

**N-0180.** §6.1.1 URI Binding Syntax, Figure 6-1, rule string / p. 22 / L953 `[none: ABNF rule]`

```abnf
string            = *( unreserved / pct-encoded )
```

Requirement ids: nistir-7695#R-0114.

**N-0181.** §6.1.1 URI Binding Syntax, Figure 6-1, rule empty / p. 22 / L954 `[none: ABNF rule]`

```abnf
empty             = ""
```

Requirement ids: nistir-7695#R-0115.

**N-0182.** §6.1.1 URI Binding Syntax, Figure 6-1, rule unreserved / p. 22 / L955 `[none: ABNF rule]`

```abnf
unreserved        = ALPHA / DIGIT / "-" / "." / "_" / "˜"
```

Note: the last alternative is U+02DC SMALL TILDE, not "~" (DEF-3, D-7).

Requirement ids: nistir-7695#R-0116.

**N-0183.** §6.1.1 URI Binding Syntax, Figure 6-1, rule pct-encoded / p. 22 / L956 `[none: ABNF rule]`

```abnf
pct-encoded       = "%" HEXDIG HEXDIG
```

Note: See D-6.

Requirement ids: nistir-7695#R-0117.

**N-0184.** §6.1.1 URI Binding Syntax, Figure 6-1, rule ALPHA / p. 22 / L957 `[none: ABNF rule]`

```abnf
ALPHA             = %x41-5a / %x61-7a   ; A-Z or a-z
```

Requirement ids: nistir-7695#R-0118.

**N-0185.** §6.1.1 URI Binding Syntax, Figure 6-1, rule DIGIT / p. 22 / L958 `[none: ABNF rule]`

```abnf
DIGIT             = %x30-39  ; 0-9
```

Requirement ids: nistir-7695#R-0064 (printed identically in Figure 5-1, the entry's locator; this copy is in its `also_at`).

**N-0186.** §6.1.1 URI Binding Syntax, Figure 6-1, rule HEXDIG / p. 22 / L959 `[none: ABNF rule]`

```abnf
HEXDIG            = DIGIT / "a" / "b" / "c" / "d" / "e" / "f"
```

Requirement ids: nistir-7695#R-0119.

**N-0187.** §6.1.1 URI Binding Syntax, Figure 6-1, rule LANGTAG / p. 22 / L960 `[none: ABNF rule]`

```abnf
LANGTAG           = cf. [RFC5646]
```

Note: not an ABNF definition (DEF-4).

Requirement ids: nistir-7695#R-0120.

**N-0188.** §6.1.1 URI Binding Syntax, paragraph 2, sentence 2 / p. 23 / L971-L973 `[should]`

> Specifically, it allows any character in the range %01-ff to be percent-encoded, but Section 5.4 of [CPE22] suggests that only certain printable non-alphanumeric characters should be percent-encoded.

Note: the lowercase "should" reports what CPE 2.2 suggests; it is not this report's rule. See D-6 on "%01-ff".

Requirement ids: none. Compares Figure 6-1 with [CPE22] §5.4; its lowercase "should" reports what [CPE22] suggests (`keyword_accounting`, L972). Figure 6-1's percent-encoding is R-0117.

**N-0189.** §6.1.1 URI Binding Syntax, paragraph 3 / p. 23 / L976-L978 `[MUST]`

> To ensure full backward compatibility with [CPE22], any implementation that consumes URIs and claims to be conformant with this Naming specification MUST accept as valid input any URI that obeys the full syntax shown in Figure 6-1.

Note: See D-6 and D-7.

Requirement ids: nistir-7695#R-0121.

##### Figure 6-2. ABNF for Preferred URI Binding (p. 23, L980-L1019)

Twenty-five rules, at the columns of the PDF figure.

**N-0190.** §6.1.1 URI Binding Syntax, Figure 6-2, rule cpe-name / p. 23 / L980 `[none: ABNF rule]`

```abnf
cpe-name          = "cpe:/" component-list
```

Requirement ids: nistir-7695#R-0122.

**N-0191.** §6.1.1 URI Binding Syntax, Figure 6-2, rule component-list / p. 23 / L982-L991 `[none: ABNF rule]`

```abnf
component-list    = part ":" vendor ":" product ":" version ":" update ":"
                    edition ":" lang
component-list    /= part ":" vendor ":" product ":" version ":" update ":"
                     edition
component-list    /= part ":" vendor ":" product ":" version ":" update
component-list    /= part ":" vendor ":" product ":" version
component-list    /= part ":" vendor ":" product
component-list    /= part ":" vendor
component-list    /= part
component-list    /= empty
```

Requirement ids: nistir-7695#R-0123.

**N-0192.** §6.1.1 URI Binding Syntax, Figure 6-2, rule part / p. 23 / L992 `[none: ABNF rule]`

```abnf
part              = "h" / "o" / "a" / empty
```

Note: See D-3 and D-4.

Requirement ids: nistir-7695#R-0107 (printed identically in Figure 6-1, the entry's locator; this copy is in its `also_at`).

**N-0193.** §6.1.1 URI Binding Syntax, Figure 6-2, rule vendor / p. 23 / L993 `[none: ABNF rule]`

```abnf
vendor            = string
```

Requirement ids: nistir-7695#R-0124.

**N-0194.** §6.1.1 URI Binding Syntax, Figure 6-2, rule product / p. 23 / L994 `[none: ABNF rule]`

```abnf
product           = string
```

Requirement ids: nistir-7695#R-0125.

**N-0195.** §6.1.1 URI Binding Syntax, Figure 6-2, rule version / p. 23 / L995 `[none: ABNF rule]`

```abnf
version           = string
```

Requirement ids: nistir-7695#R-0126.

**N-0196.** §6.1.1 URI Binding Syntax, Figure 6-2, rule update / p. 23 / L996 `[none: ABNF rule]`

```abnf
update            = string
```

Requirement ids: nistir-7695#R-0127.

**N-0197.** §6.1.1 URI Binding Syntax, Figure 6-2, rule edition / p. 23 / L997 `[none: ABNF rule]`

```abnf
edition           = string / packed
```

Requirement ids: nistir-7695#R-0128.

**N-0198.** §6.1.1 URI Binding Syntax, Figure 6-2, rule lang / p. 23 / L998 `[none: ABNF rule]`

```abnf
lang              = LANGTAG / empty
```

Note: See D-3 and D-5.

Requirement ids: nistir-7695#R-0129.

**N-0199.** §6.1.1 URI Binding Syntax, Figure 6-2, rule string / p. 23 / L999 `[none: ABNF rule]`

```abnf
string            = str_wo_special / str_w_special
```

Requirement ids: nistir-7695#R-0130.

**N-0200.** §6.1.1 URI Binding Syntax, Figure 6-2, rule str_wo_special / p. 23 / L1000 `[none: ABNF rule]`

```abnf
str_wo_special    = *( unreserved / pct-encoded )
```

Requirement ids: nistir-7695#R-0131.

**N-0201.** §6.1.1 URI Binding Syntax, Figure 6-2, rule str_w_special / p. 23 / L1001 `[none: ABNF rule]`

```abnf
str_w_special     = *1spec_chrs 1*( unreserved / pct-encoded ) *1spec_chrs
```

Note: See D-1 and D-2.

Requirement ids: nistir-7695#R-0132.

**N-0202.** §6.1.1 URI Binding Syntax, Figure 6-2, rule spec_chrs / p. 23 / L1002 `[none: ABNF rule]`

```abnf
spec_chrs         = 1*spec1 / spec2
```

Requirement ids: nistir-7695#R-0133.

**N-0203.** §6.1.1 URI Binding Syntax, Figure 6-2, rule packed / p. 23 / L1003 `[none: ABNF rule]`

```abnf
packed            = "~" string "~" string "~" string "~" string "~" string
```

Requirement ids: nistir-7695#R-0134.

**N-0204.** §6.1.1 URI Binding Syntax, Figure 6-2, rule empty / p. 23 / L1004 `[none: ABNF rule]`

```abnf
empty             = ""
```

Requirement ids: nistir-7695#R-0115 (printed identically in Figure 6-1, the entry's locator; this copy is in its `also_at`).

**N-0205.** §6.1.1 URI Binding Syntax, Figure 6-2, rule unreserved / p. 23 / L1005 `[none: ABNF rule]`

```abnf
unreserved        = ALPHA / DIGIT / "-" / "." / "_"
```

Note: See D-7.

Requirement ids: nistir-7695#R-0135.

**N-0206.** §6.1.1 URI Binding Syntax, Figure 6-2, rule special / p. 23 / L1006 `[none: ABNF rule]`

```abnf
special           = spec1 / spec2
```

Requirement ids: nistir-7695#R-0136.

**N-0207.** §6.1.1 URI Binding Syntax, Figure 6-2, rule spec1 / p. 23 / L1007 `[none: ABNF rule]`

```abnf
spec1             = "%01"
```

Requirement ids: nistir-7695#R-0137.

**N-0208.** §6.1.1 URI Binding Syntax, Figure 6-2, rule spec2 / p. 23 / L1008 `[none: ABNF rule]`

```abnf
spec2             = "%02"
```

Requirement ids: nistir-7695#R-0138.

**N-0209.** §6.1.1 URI Binding Syntax, Figure 6-2, rule pct-encoded / p. 23 / L1009-L1013 `[none: ABNF rule]`

```abnf
pct-encoded       = "%21" / "%22" / "%23" / "%24" / "%25" / "%26" / "%27" /
                  = "%28" / "%29" / "%2a" / "%2b" / "%2c" / "%2f" / "%3a" /
                  = "%3b" / "%3c" / "%3d" / "%3e" / "%3f" / "%40" / "%5b" /
                  = "%5c" / "%5d" / "%5e" / "%60" / "%7b" / "%7c" / "%7d" /
                  = "%7e"
```

Note: the continuation lines begin with "=" (DEF-5).

Requirement ids: nistir-7695#R-0139.

**N-0210.** §6.1.1 URI Binding Syntax, Figure 6-2, rule ALPHA / p. 23 / L1014 `[none: ABNF rule]`

```abnf
ALPHA             = %x41-5a / %x61-7a  ; A-Z or a-z
```

Requirement ids: nistir-7695#R-0118 (printed identically in Figure 6-1, the entry's locator; this copy is in its `also_at`).

**N-0211.** §6.1.1 URI Binding Syntax, Figure 6-2, rule DIGIT / p. 23 / L1015 `[none: ABNF rule]`

```abnf
DIGIT             = %x30-39  ; 0-9
```

Requirement ids: nistir-7695#R-0064 (printed identically in Figure 5-1, the entry's locator; this copy is in its `also_at`).

**N-0212.** §6.1.1 URI Binding Syntax, Figure 6-2, rule LANGTAG / p. 23 / L1016 `[none: ABNF rule]`

```abnf
LANGTAG           = language ["-" region] ; cf. [RFC5646]
```

Note: See D-5.

Requirement ids: nistir-7695#R-0140.

**N-0213.** §6.1.1 URI Binding Syntax, Figure 6-2, rule language / p. 23 / L1017 `[none: ABNF rule]`

```abnf
language          = 2*3ALPHA              ; shortest ISO 639 code
```

Requirement ids: nistir-7695#R-0141.

**N-0214.** §6.1.1 URI Binding Syntax, Figure 6-2, rule region / p. 23 / L1018 `[none: ABNF rule]`

```abnf
region            = 2ALPHA / 3DIGIT       ; ISO 3166-1 code or UN M.49 code
```

Requirement ids: nistir-7695#R-0142.

**N-0215.** §6.1.1 URI Binding Syntax, paragraph 4, sentence 1 / p. 23 / L1021-L1022 `[SHOULD]`

> Although the freer syntax is allowed as valid input, CPE URIs SHOULD obey the more restricted syntax shown in Figure 6-2.

Requirement ids: nistir-7695#R-0143.

**N-0216.** §6.1.1 URI Binding Syntax, paragraph 4, sentence 2 and its three bullets (one statement) / pp. 23-24 / L1022-L1033 `[none: declarative]`

> ```text
> The syntax shown in Figure 6-2 has the following features:
> • It introduces support for “packing” multiple attribute values into the edition component.
> • It introduces support for the use of special characters.
> • It strictly enumerates the allowed percent-encoded forms.
> ```

Requirement ids: none. Describes features of Figure 6-2 (`requirements.yaml` `excluded`), whose rules are R-0122 to R-0142 (with R-0064, R-0107, R-0115 and R-0118).

**N-0217.** §6.1.1 URI Binding Syntax, paragraph 5, sentence 1 / p. 24 / L1035-L1036 `[none: declarative]`

> The bind_to_URI procedure (cf. 6.1.2) is designed to produce URIs that obey the syntax shown in Figure 6-2.

Note: See D-2 and D-3.

Requirement ids: nistir-7695#R-0144.

**N-0218.** §6.1.1 URI Binding Syntax, paragraph 5, sentence 2 / p. 24 / L1036-L1037 `[none: declarative]`

> The unbind_URI procedure (cf. 6.1.3) is designed to accept as valid input URIs that obey the syntax shown in either Figure 6-1 or Figure 6-2.

Note: See D-6 and D-7.

Requirement ids: nistir-7695#R-0145.

#### 6.1.2 Binding a WFN to a URI

**N-0219.** §6.1.2 Binding a WFN to a URI, paragraph 1, sentence 1 / p. 24 / L1041 `[none: declarative]`

> The procedure to bind a given WFN to a URI is specified in pseudocode below.

Requirement ids: none. Introduces the bind_to_URI pseudocode, which binds through R-0148.

**N-0220.** §6.1.2 Binding a WFN to a URI, paragraph 1, sentence 2 / p. 24 / L1041-L1042 `[none: declarative]`

> The top-level binding function, bind_to_URI, is called with the WFN to be bound as its only argument.

Requirement ids: none. Names the top-level function; the pseudocode binds through R-0148.

**N-0221.** §6.1.2 Binding a WFN to a URI, paragraph 1, sentence 8 / p. 24 / L1046-L1047 `[none: declarative]`

> The algorithm defined here assumes that the input WFN complies with the requirements defined in Section 5.2.

Requirement ids: nistir-7695#R-0146 (one entry for N-0221 and N-0222).

**N-0222.** §6.1.2 Binding a WFN to a URI, paragraph 1, sentence 9 / p. 24 / L1047-L1048 `[none: declarative]`

> The behavior of bind_to_URI is undefined if its input is not well formed.

Requirement ids: nistir-7695#R-0146 (one entry for N-0221 and N-0222).

**N-0223.** §6.1.2 Binding a WFN to a URI, paragraph 2, sentence 1 / p. 24 / L1050-L1051 `[OPTIONAL]`

> It is OPTIONAL for implementations of URI binding to follow the pseudocode, processes, and other non-normative information provided in this section.

Note: See D-12.

Requirement ids: nistir-7695#R-0147.

**N-0224.** §6.1.2 Binding a WFN to a URI, paragraph 2, sentence 2 / p. 24 / L1051-L1052 `[MUST]`

> However, the result of an implementation performing a URI binding MUST produce the same result as the suggested pseudocode, processes, etc. would produce.

Note: (inferred) this MUST binds the result, not the steps; it is why the pseudocode steps are extracted. See D-12.

Requirement ids: nistir-7695#R-0148.

##### 6.1.2.1 Notes on URI binding procedure

**N-0225.** §6.1.2.1 Notes on URI binding procedure, lead-in / p. 24 / L1056 `[MUST]`

> The procedure for binding WFNs to URIs MUST address the following issues:

Requirement ids: nistir-7695#R-0149.

**N-0226.** §6.1.2.1 Notes on URI binding procedure, item 1 / p. 24 / L1057 `[none: list item]`

> Handling logical values

Requirement ids: nistir-7695#R-0149 (enumeration item 1).

**N-0227.** §6.1.2.1 Notes on URI binding procedure, item 2 / p. 24 / L1058 `[none: list item]`

> Handling non-alphanumeric and special characters

Requirement ids: nistir-7695#R-0149 (enumeration item 2).

**N-0228.** §6.1.2.1 Notes on URI binding procedure, item 3 / p. 24 / L1059 `[none: list item]`

> “Packing” extended attributes.

Requirement ids: nistir-7695#R-0149 (enumeration item 3).

###### 6.1.2.1.1 Handling logical values

**N-0229.** §6.1.2.1.1 Handling logical values, sentence 1 / p. 24 / L1063 `[none: declarative]`

> The logical values ANY and NA are defined as possible attribute values in WFNs.

Requirement ids: none. Restates §5.3.1 (R-0024); the two binding rules of the paragraph are R-0150 and R-0151.

**N-0230.** §6.1.2.1.1 Handling logical values, sentence 2 / p. 24 / L1063-L1065 `[SHALL]`

> The logical value ANY SHALL bind to what [CPE22] calls a “blank” (i.e., an empty component, indicated by two sequential colons) in the URI.

Requirement ids: nistir-7695#R-0150.

**N-0231.** §6.1.2.1.1 Handling logical values, sentence 3 / p. 24 / L1065 `[SHALL]`

> The logical value NA SHALL bind to a single hyphen.

Note: See D-3.

Requirement ids: nistir-7695#R-0151.

###### 6.1.2.1.2 Handling non-alphanumeric and special characters

**N-0232.** §6.1.2.1.2 Handling non-alphanumeric and special characters, paragraph 1, sentence 1 / p. 24 / L1069-L1070 `[MUST, MAY]`

> ```text
> In WFN attribute-value strings, non-alphanumeric characters generally MUST be quoted, with the exception that the special characters “*” and “?” MAY appear without quoting.
> ```

Note: See D-14.

Requirement ids: nistir-7695#R-0152, nistir-7695#R-0153 (the sentence is split into one entry per separately testable part).

**N-0233.** §6.1.2.1.2 Handling non-alphanumeric and special characters, paragraph 1, sentence 2 / p. 24 / L1070-L1071 `[MUST]`

> When forming the URI binding, certain transformations MUST be applied.

Requirement ids: nistir-7695#R-0154.

**N-0234.** §6.1.2.1.2 Handling non-alphanumeric and special characters, paragraph 1, sentence 3 / p. 24 / L1071-L1073 `[none: declarative]`

> In most cases, quoted non-alphanumeric characters are bound to a percent-encoded form; certain quoted non-alphanumeric characters, however, are passed through without percent-encoding.

Requirement ids: none. A prose summary of Table 6-1 (`requirements.yaml` `excluded`); the table is R-0155.

**N-0235.** §6.1.2.1.2 Handling non-alphanumeric and special characters, paragraph 1, sentence 4 / p. 24 / L1073-L1074 `[none: declarative]`

> When special characters appear without quoting, they are mapped to special percent-encoded forms.

Requirement ids: none. A prose summary of Table 6-2 (`requirements.yaml` `excluded`); the table is R-0156.

**N-0236.** §6.1.2.1.2 Handling non-alphanumeric and special characters, paragraph 2, sentence 1 / p. 24 / L1076-L1078 `[SHALL]`

> Following Table 6-1, the binding procedure SHALL replace quoted non-alphanumeric substrings shown under the columns labeled IN with the substitute character or percent-encoded string shown to its right under the columns labeled OUT.

Requirement ids: nistir-7695#R-0155.

**Table 6-1. Bindings for Quoted Non-Alphanumeric Characters** (p. 25, L1091-L1097)

The table prints seven IN/OUT column pairs per row over five rows (the last row has three pairs). Each pair is one statement, in reading order; IN and OUT are verbatim cell contents.

- **N-0237.** §6.1.2.1.2 Handling non-alphanumeric and special characters, Table 6-1, row 1, pair 1 / p. 25 / L1092 `[none: table row]`: IN `\!` OUT `%21`. Requirement ids: nistir-7695#R-0155 (enumeration item 1).
- **N-0238.** §6.1.2.1.2 Handling non-alphanumeric and special characters, Table 6-1, row 1, pair 2 / p. 25 / L1092 `[none: table row]`: IN `\"` OUT `%22`. Requirement ids: nistir-7695#R-0155 (enumeration item 2).
- **N-0239.** §6.1.2.1.2 Handling non-alphanumeric and special characters, Table 6-1, row 1, pair 3 / p. 25 / L1092 `[none: table row]`: IN `\#` OUT `%23`. Requirement ids: nistir-7695#R-0155 (enumeration item 3).
- **N-0240.** §6.1.2.1.2 Handling non-alphanumeric and special characters, Table 6-1, row 1, pair 4 / p. 25 / L1092 `[none: table row]`: IN `\$` OUT `%24`. Requirement ids: nistir-7695#R-0155 (enumeration item 4).
- **N-0241.** §6.1.2.1.2 Handling non-alphanumeric and special characters, Table 6-1, row 1, pair 5 / p. 25 / L1092 `[none: table row]`: IN `\%` OUT `%25`. Requirement ids: nistir-7695#R-0155 (enumeration item 5).
- **N-0242.** §6.1.2.1.2 Handling non-alphanumeric and special characters, Table 6-1, row 1, pair 6 / p. 25 / L1092 `[none: table row]`: IN `\&` OUT `%26`. Requirement ids: nistir-7695#R-0155 (enumeration item 6).
- **N-0243.** §6.1.2.1.2 Handling non-alphanumeric and special characters, Table 6-1, row 1, pair 7 / p. 25 / L1092 `[none: table row]`: IN `\'` OUT `%27`. Requirement ids: nistir-7695#R-0155 (enumeration item 7).
- **N-0244.** §6.1.2.1.2 Handling non-alphanumeric and special characters, Table 6-1, row 2, pair 1 / p. 25 / L1093 `[none: table row]`: IN `\(` OUT `%28`. Requirement ids: nistir-7695#R-0155 (enumeration item 8).
- **N-0245.** §6.1.2.1.2 Handling non-alphanumeric and special characters, Table 6-1, row 2, pair 2 / p. 25 / L1093 `[none: table row]`: IN `\)` OUT `%29`. Requirement ids: nistir-7695#R-0155 (enumeration item 9).
- **N-0246.** §6.1.2.1.2 Handling non-alphanumeric and special characters, Table 6-1, row 2, pair 3 / p. 25 / L1093 `[none: table row]`: IN `\*` OUT `%2a`. Requirement ids: nistir-7695#R-0155 (enumeration item 10).
- **N-0247.** §6.1.2.1.2 Handling non-alphanumeric and special characters, Table 6-1, row 2, pair 4 / p. 25 / L1093 `[none: table row]`: IN `\+` OUT `%2b`. Requirement ids: nistir-7695#R-0155 (enumeration item 11).
- **N-0248.** §6.1.2.1.2 Handling non-alphanumeric and special characters, Table 6-1, row 2, pair 5 / p. 25 / L1093 `[none: table row]`: IN `\,` OUT `%2c`. Requirement ids: nistir-7695#R-0155 (enumeration item 12).
- **N-0249.** §6.1.2.1.2 Handling non-alphanumeric and special characters, Table 6-1, row 2, pair 6 / p. 25 / L1093 `[none: table row]`: IN `\-` OUT `-`. Requirement ids: nistir-7695#R-0155 (enumeration item 13).
- **N-0250.** §6.1.2.1.2 Handling non-alphanumeric and special characters, Table 6-1, row 2, pair 7 / p. 25 / L1093 `[none: table row]`: IN `\.` OUT `.`. Requirement ids: nistir-7695#R-0155 (enumeration item 14).
- **N-0251.** §6.1.2.1.2 Handling non-alphanumeric and special characters, Table 6-1, row 3, pair 1 / p. 25 / L1094 `[none: table row]`: IN `\/` OUT `%2f`. Requirement ids: nistir-7695#R-0155 (enumeration item 15).
- **N-0252.** §6.1.2.1.2 Handling non-alphanumeric and special characters, Table 6-1, row 3, pair 2 / p. 25 / L1094 `[none: table row]`: IN `\:` OUT `%3a`. Requirement ids: nistir-7695#R-0155 (enumeration item 16).
- **N-0253.** §6.1.2.1.2 Handling non-alphanumeric and special characters, Table 6-1, row 3, pair 3 / p. 25 / L1094 `[none: table row]`: IN `\;` OUT `%3b`. Requirement ids: nistir-7695#R-0155 (enumeration item 17).
- **N-0254.** §6.1.2.1.2 Handling non-alphanumeric and special characters, Table 6-1, row 3, pair 4 / p. 25 / L1094 `[none: table row]`: IN `\<` OUT `%3c`. Requirement ids: nistir-7695#R-0155 (enumeration item 18).
- **N-0255.** §6.1.2.1.2 Handling non-alphanumeric and special characters, Table 6-1, row 3, pair 5 / p. 25 / L1094 `[none: table row]`: IN `\=` OUT `%3d`. Requirement ids: nistir-7695#R-0155 (enumeration item 19).
- **N-0256.** §6.1.2.1.2 Handling non-alphanumeric and special characters, Table 6-1, row 3, pair 6 / p. 25 / L1094 `[none: table row]`: IN `\>` OUT `%3e`. Requirement ids: nistir-7695#R-0155 (enumeration item 20).
- **N-0257.** §6.1.2.1.2 Handling non-alphanumeric and special characters, Table 6-1, row 3, pair 7 / p. 25 / L1094 `[none: table row]`: IN `\?` OUT `%3f`. Requirement ids: nistir-7695#R-0155 (enumeration item 21).
- **N-0258.** §6.1.2.1.2 Handling non-alphanumeric and special characters, Table 6-1, row 4, pair 1 / p. 25 / L1095 `[none: table row]`: IN `\@` OUT `%40`. Requirement ids: nistir-7695#R-0155 (enumeration item 22).
- **N-0259.** §6.1.2.1.2 Handling non-alphanumeric and special characters, Table 6-1, row 4, pair 2 / p. 25 / L1095 `[none: table row]`: IN `\[` OUT `%5b`. Requirement ids: nistir-7695#R-0155 (enumeration item 23).
- **N-0260.** §6.1.2.1.2 Handling non-alphanumeric and special characters, Table 6-1, row 4, pair 3 / p. 25 / L1095 `[none: table row]`: IN `\\` OUT `%5c`. Requirement ids: nistir-7695#R-0155 (enumeration item 24).
- **N-0261.** §6.1.2.1.2 Handling non-alphanumeric and special characters, Table 6-1, row 4, pair 4 / p. 25 / L1095 `[none: table row]`: IN `\]` OUT `%5d`. Requirement ids: nistir-7695#R-0155 (enumeration item 25).
- **N-0262.** §6.1.2.1.2 Handling non-alphanumeric and special characters, Table 6-1, row 4, pair 5 / p. 25 / L1095 `[none: table row]`: IN `\^` OUT `%5e`. Requirement ids: nistir-7695#R-0155 (enumeration item 26).
- **N-0263.** §6.1.2.1.2 Handling non-alphanumeric and special characters, Table 6-1, row 4, pair 6 / p. 25 / L1095 `[none: table row]`: IN `` \` `` OUT `%60`. Requirement ids: nistir-7695#R-0155 (enumeration item 27).
- **N-0264.** §6.1.2.1.2 Handling non-alphanumeric and special characters, Table 6-1, row 4, pair 7 / p. 25 / L1095 `[none: table row]`: IN `\{` OUT `%7b`. Requirement ids: nistir-7695#R-0155 (enumeration item 28).
- **N-0265.** §6.1.2.1.2 Handling non-alphanumeric and special characters, Table 6-1, row 5, pair 1 / p. 25 / L1096 `[none: table row]`: IN `\|` OUT `%7c`. Requirement ids: nistir-7695#R-0155 (enumeration item 29).
- **N-0266.** §6.1.2.1.2 Handling non-alphanumeric and special characters, Table 6-1, row 5, pair 2 / p. 25 / L1096 `[none: table row]`: IN `\}` OUT `%7d`. Requirement ids: nistir-7695#R-0155 (enumeration item 30).
- **N-0267.** §6.1.2.1.2 Handling non-alphanumeric and special characters, Table 6-1, row 5, pair 3 / p. 25 / L1096 `[none: table row]`: IN `\~` OUT `%7e`. Requirement ids: nistir-7695#R-0155 (enumeration item 31).

**N-0268.** §6.1.2.1.2 Handling non-alphanumeric and special characters, paragraph 3 / p. 25 / L1099-L1100 `[SHALL]`

> When an unquoted special character is encountered in an attribute-value string, it SHALL be bound to the special percent-encoded form shown in Table 6-2.

Requirement ids: nistir-7695#R-0156.

**Table 6-2. Bindings for Unquoted Special Characters** (p. 25, L1102-L1105)

- **N-0269.** §6.1.2.1.2 Handling non-alphanumeric and special characters, Table 6-2, row 1 / p. 25 / L1103 `[none: table row]`: IN `?` OUT `%01`. Requirement ids: nistir-7695#R-0156 (enumeration item 1).
- **N-0270.** §6.1.2.1.2 Handling non-alphanumeric and special characters, Table 6-2, row 2 / p. 25 / L1104 `[none: table row]`: IN `*` OUT `%02`. Requirement ids: nistir-7695#R-0156 (enumeration item 2).

###### 6.1.2.1.3 Packing extended attributes

**N-0271.** §6.1.2.1.3 Packing extended attributes, paragraph 1, sentence 1 / p. 25 / L1110-L1111 `[none: declarative]`

> The version 2.3 specification introduces four new attributes{U+2014}the extended attributes{U+2014}that have no assigned position in the URI binding.

Requirement ids: none. Introduces the extended attributes for packing; the rule follows in R-0157.

**N-0272.** §6.1.2.1.3 Packing extended attributes, paragraph 1, sentence 2 / p. 25 / L1111-L1112 `[none: declarative]`

> When these attributes have values other than ANY in the WFN, they are “packed” in a special format, and in a specified order, into the edition component of the URI.

Requirement ids: nistir-7695#R-0157 (one entry for N-0272 and N-0273).

**N-0273.** §6.1.2.1.3 Packing extended attributes, paragraph 1, sentence 3 / p. 25 / L1113 `[none: declarative]`

> This special format uses the tilde character “~” (without percent-encoding) as a sub-delimiter.

Requirement ids: nistir-7695#R-0157 (one entry for N-0272 and N-0273).

**N-0274.** §6.1.2.1.3 Packing extended attributes, paragraph 2, sentence 2 / p. 25 / L1118-L1119 `[should, may]`

> This capability should be used with care, as CPE v2.2-conformant tools may be unable to properly match names that differ in terms of packed attribute values.

Note: the lowercase "should" is advice to the makers of URI names; "may" here expresses possibility.

Requirement ids: none. Lowercase advice to the makers of URI names (`requirements.yaml` `excluded`); "may" here expresses possibility (`keyword_accounting`, L1118).

##### 6.1.2.2 Summary of algorithm

**N-0275.** §6.1.2.2 Summary of algorithm, lead-in / p. 25 / L1123 `[none: lead-in]`

> The URI binding procedure is summarized as follows:

Requirement ids: none. Lead-in to the summary steps R-0158 to R-0167.

**N-0276.** §6.1.2.2 Summary of algorithm, step 1 / p. 25 / L1124 `[none: procedure step]`

> Initialize the output URI binding to the string "cpe:/".

Requirement ids: nistir-7695#R-0158.

**N-0277.** §6.1.2.2 Summary of algorithm, step 2 / p. 25 / L1125-L1126 `[none: procedure step]`

> Begin loop: Iterate over the seven attributes corresponding to the seven components in a v2.2 CPE URI [CPE22:5.2]. Get the value of each attribute and perform steps 3 through 7.

Note: step 7 lies outside the loop that step 6 ends (DEF-7).

Requirement ids: nistir-7695#R-0159.

**N-0278.** §6.1.2.2 Summary of algorithm, step 3 / pp. 25-26 / L1127-L1143 `[none: procedure step]`

> Special handling of edition: When binding to a 2.2 URI, the edition component (the sixth element of the URI) is used as the location to “pack” five attribute values in the WFN: (legacy) edition, sw_edition, target_sw, target_hw, and other. The “packing” process involves concatenating the five values together, prefixed and separated by the tilde. The leading tilde serves as a flag indicating that the contents of the edition field are a packed representation of five separate values, and the internal tildes are used to aid parsing the values out. In the special case in which the four extended attributes are not specified, or all are ANY, only the edition attribute is used and no packing is performed.

Requirement ids: nistir-7695#R-0160, nistir-7695#R-0161, nistir-7695#R-0162 (one entry per part of the step).

**N-0279.** §6.1.2.2 Summary of algorithm, step 4 / p. 26 / L1144 `[none: lead-in]`

> Bind attribute values:

Requirement ids: none. Lead-in to steps 4a to 4c, carried in the `condition` of R-0163, R-0164 and R-0165.

**N-0280.** §6.1.2.2 Summary of algorithm, step 4a / p. 26 / L1145-L1147 `[none: procedure step]`

> For all attributes other than (legacy) “edition”, inspect the value and convert logical values appropriately. If the attribute is unspecified, or its logical value is ANY, bind it to blank (“”) in the URI. If the logical value is NA, bind it to the hyphen (“-”).

Note: See D-13.

Requirement ids: nistir-7695#R-0163.

**N-0281.** §6.1.2.2 Summary of algorithm, step 4b / p. 26 / L1148-L1149 `[none: procedure step]`

> Scan the attribute value for any quoted non-alphanumeric characters and bind them as specified in Table 6-1.

Requirement ids: nistir-7695#R-0164.

**N-0282.** §6.1.2.2 Summary of algorithm, step 4c / p. 26 / L1150-L1151 `[none: procedure step]`

> Scan the attribute value for any unquoted special characters and bind them as specified in Table 6-2.

Requirement ids: nistir-7695#R-0165.

**N-0283.** §6.1.2.2 Summary of algorithm, step 5 / p. 26 / L1152 `[none: procedure step]`

> Append the attribute-value string to the output URI, followed by a trailing colon.

Requirement ids: nistir-7695#R-0166.

**N-0284.** §6.1.2.2 Summary of algorithm, step 6 / p. 26 / L1153 `[none: procedure step]`

> END LOOP.

Requirement ids: none. "END LOOP." only closes the loop of step 2; structure, not a rule (notes of R-0159 and R-0167).

**N-0285.** §6.1.2.2 Summary of algorithm, step 7 / p. 26 / L1154 `[none: procedure step]`

> Return the output URI, trimming away all trailing colons for compactness.

Requirement ids: nistir-7695#R-0167.

##### 6.1.2.3 Pseudocode for algorithm

Eleven functions (PDF pp. 26-29, L1158-L1348). Each function's statements are contiguous and together reproduce every line of its listing.

###### Listing: function bind_to_URI(w)

**N-0286.** §6.1.2.3 Pseudocode for algorithm, bind_to_URI, step 1 (signature, purpose, initialise) / p. 26 / L1158-L1161 `[none: pseudocode]`

```text
function bind_to_URI(w)
  ;; Top-level function used to bind a WFN w to a URI.
  ;; Initialize the output with the CPE v2.2 URI prefix.
  uri := "cpe:/".
```

Requirement ids: none. Sets the prefix that R-0158 states; binds through R-0148.

**N-0287.** §6.1.2.3 Pseudocode for algorithm, bind_to_URI, step 2 (loop over seven attributes) / p. 26 / L1162-L1163 `[none: pseudocode]`

```text
  foreach a in {part,vendor,product,version,update,edition,language}
    do
```

Requirement ids: nistir-7695#R-0168 (the entry quotes L1162 of this step).

**N-0288.** §6.1.2.3 Pseudocode for algorithm, bind_to_URI, step 3 (edition: bind five values and pack) / p. 26 / L1164-L1173 `[none: pseudocode]`

```text
      if a = edition
        then
          ;; Call the pack() helper function to compute the proper
          ;; binding for the edition element.
          ed := bind_value_for_URI(get(w,edition)).
          sw_ed := bind_value_for_URI(get(w,sw_edition)).
          t_sw := bind_value_for_URI(get(w,target_sw)).
          t_hw := bind_value_for_URI(get(w,target_hw)).
          oth := bind_value_for_URI(get(w,other)).
          v := pack(ed,sw_ed,t_sw,t_hw,oth).
```

Note: See D-13.

Requirement ids: nistir-7695#R-0169.

**N-0289.** §6.1.2.3 Pseudocode for algorithm, bind_to_URI, step 4 (other attributes) / p. 26 / L1174-L1178 `[none: pseudocode]`

```text
        else
          ;; Get the value for a in w, then bind to a string
          ;; for inclusion in the URI.
          v := bind_value_for_URI(get(w,a)).
      endif.
```

Note: See D-13.

Requirement ids: none. Binds every attribute other than edition through bind_value_for_URI, as R-0163 to R-0165 state; binds through R-0148.

**N-0290.** §6.1.2.3 Pseudocode for algorithm, bind_to_URI, step 5 (append and close loop) / p. 26 / L1179-L1181 `[none: pseudocode]`

```text
    ;; Append v to the URI then add a colon.
    uri := strcat(uri, v, ":").
  end.
```

Requirement ids: none. Appends the value and a colon, as R-0166 states; binds through R-0148.

**N-0291.** §6.1.2.3 Pseudocode for algorithm, bind_to_URI, step 6 (trim and return) / p. 26 / L1182-L1184 `[none: pseudocode]`

```text
  ;; Return the URI string, with trailing colons trimmed.
  return trim(uri).
end.
```

Requirement ids: none. Trims the trailing colons, as R-0167 states; binds through R-0148.

###### Listing: function bind_value_for_URI(s)

**N-0292.** §6.1.2.3 Pseudocode for algorithm, bind_value_for_URI, step 1 (ANY binds to blank) / p. 26 / L1186-L1190 `[none: pseudocode]`

```text
function bind_value_for_URI(s)
  ;; Takes a string s and converts it to the proper string for
  ;; inclusion in a CPE v2.2-conformant URI.  The logical value ANY
  ;; binds to the blank in the 2.2-conformant URI.
  if s = ANY then return("").
```

Requirement ids: none. ANY binds to the blank: restates R-0150 (`requirements.yaml` `excluded`, bind_value_for_URI).

**N-0293.** §6.1.2.3 Pseudocode for algorithm, bind_value_for_URI, step 2 (NA binds to hyphen) / p. 26 / L1191-L1192 `[none: pseudocode]`

```text
  ;; The value NA binds to a single hyphen.
  if s = NA then return("-").
```

Note: See D-3.

Requirement ids: none. NA binds to a hyphen: restates R-0151 (`requirements.yaml` `excluded`, bind_value_for_URI).

**N-0294.** §6.1.2.3 Pseudocode for algorithm, bind_value_for_URI, step 3 (string values) / p. 27 / L1200-L1202 `[none: pseudocode]`

```text
  ;; If we get here, we’re dealing with a string value.
  return transform_for_uri(s).
end.
```

Requirement ids: none. Hands a string value to transform_for_uri, whose rules are R-0170, R-0155 and R-0156; binds through R-0148.

###### Listing: function transform_for_uri(s)

**N-0295.** §6.1.2.3 Pseudocode for algorithm, transform_for_uri, step 1 (signature and purpose) / p. 27 / L1204-L1209 `[none: pseudocode]`

```text
function transform_for_uri(s)
  ;; Scans an input string s and applies the following
  ;; transformations:
  ;; - Pass alphanumeric characters thru untouched
  ;; - Percent-encode quoted non-alphanumerics as needed
  ;; - Unquoted special characters are mapped to their special forms.
```

Requirement ids: none. Its comment summarises R-0170, R-0155 and R-0156; binds through R-0148.

**N-0296.** §6.1.2.3 Pseudocode for algorithm, transform_for_uri, step 2 (initialise) / p. 27 / L1210-L1211 `[none: pseudocode]`

```text
  result := "".
  idx := 0.
```

Requirement ids: none. Initialises transform_for_uri; no rule of its own; binds through R-0148.

**N-0297.** §6.1.2.3 Pseudocode for algorithm, transform_for_uri, step 3 (scan loop) / p. 27 / L1212-L1213 `[none: pseudocode]`

```text
  while (idx < strlen(s)) do
    thischar := substr(s,idx,idx).  ; get the idx’th character of s.
```

Requirement ids: none. The scan loop of transform_for_uri; no rule of its own; binds through R-0148.

**N-0298.** §6.1.2.3 Pseudocode for algorithm, transform_for_uri, step 4 (alphanumerics pass) / p. 27 / L1214-L1220 `[none: pseudocode]`

```text
    ;; alphanumerics (incl. underscore) pass untouched.
    if (is_alphanum(thischar))
      then
        result := strcat(result,thischar).
        idx := idx + 1.
        continue.
    endif.
```

Requirement ids: nistir-7695#R-0170 (the entry quotes L1214-L1217 of this step).

**N-0299.** §6.1.2.3 Pseudocode for algorithm, transform_for_uri, step 5 (quoted characters) / p. 27 / L1221-L1228 `[none: pseudocode]`

```text
    if (thischar = "\") ; escape character
      then
        idx := idx + 1.
        nxtchar := substr(s,idx,idx).
        result := strcat(result,pct_encode(nxtchar)).
        idx := idx + 1.
        continue.
    endif.
```

Note: See DEF-13.

Requirement ids: none. Binds a quoted character through pct_encode, which restates Table 6-1 (R-0155); binds through R-0148.

**N-0300.** §6.1.2.3 Pseudocode for algorithm, transform_for_uri, step 6 (unquoted `?`) / p. 27 / L1229-L1230 `[none: pseudocode]`

```text
    ;; Bind the unquoted '?' special character to "%01".
    if (thischar = "?") then result := strcat(result,"%01").
```

Note: See D-2.

Requirement ids: none. Restates Table 6-2, row 1 (R-0156); binds through R-0148.

**N-0301.** §6.1.2.3 Pseudocode for algorithm, transform_for_uri, step 7 (unquoted `*`) / p. 27 / L1231-L1232 `[none: pseudocode]`

```text
    ;; Bind the unquoted '*' special character to "%02".
    if (thischar = "*") then result := strcat(result,"%02").
```

Requirement ids: none. Restates Table 6-2, row 2 (R-0156); binds through R-0148.

**N-0302.** §6.1.2.3 Pseudocode for algorithm, transform_for_uri, step 8 (advance and close loop) / p. 27 / L1233-L1234 `[none: pseudocode]`

```text
    idx := idx + 1.
  end.
```

Requirement ids: none. Advances and closes the loop of transform_for_uri; binds through R-0148.

**N-0303.** §6.1.2.3 Pseudocode for algorithm, transform_for_uri, step 9 (return) / p. 27 / L1235-L1236 `[none: pseudocode]`

```text
  return result.
end.
```

Requirement ids: none. Returns the result of transform_for_uri; binds through R-0148.

###### Listing: function pct_encode(c)

**N-0304.** §6.1.2.3 Pseudocode for algorithm, pct_encode, step 1 (signature, purpose, case) / p. 27 / L1238-L1241 `[none: pseudocode]`

```text
function pct_encode(c)
  ;; Return the appropriate percent-encoding of character c.
  ;; Certain characters are returned without encoding.
  case c:
```

Requirement ids: none. pct_encode restates Table 6-1 (R-0155) as a case list (`requirements.yaml` `excluded`).

**N-0305.** §6.1.2.3 Pseudocode for algorithm, pct_encode, step 2 (cases `!` to `,`) / pp. 27-28 / L1242-L1260 `[none: pseudocode]`

```text
    '!': return "%21".
    '"': return "%22".
    '#': return "%23".
    '$': return "%24".
    '%': return "%25".
    '&': return "%26".
    ''': return "%27".
    '(': return "%28".
    ')': return "%29".
    '*': return "%2a".
    '+': return "%2b".
    ',': return "%2c".
```

Note: with steps 3 and 4 this is the mapping of Table 6-1.

Requirement ids: none. pct_encode restates Table 6-1 (R-0155) as a case list (`requirements.yaml` `excluded`).

**N-0306.** §6.1.2.3 Pseudocode for algorithm, pct_encode, step 3 (cases `-` and `.`, no encoding) / p. 28 / L1261-L1262 `[none: pseudocode]`

```text
    '-': return c. ; bound without encoding
    '.': return c. ; bound without encoding
```

Requirement ids: none. pct_encode passes the hyphen and the period without encoding, as Table 6-1 does (R-0155, enumeration items 13 and 14); `requirements.yaml` `excluded` lists the function.

**N-0307.** §6.1.2.3 Pseudocode for algorithm, pct_encode, step 4 (cases `/` to `~`) / p. 28 / L1263-L1279 `[none: pseudocode]`

```text
    '/': return "%2f".
    ':': return "%3a".
    ';': return "%3b".
    '<': return "%3c".
    '=': return "%3d".
    '>': return "%3e".
    '?': return "%3f".
    '@': return "%40".
    '[': return "%5b".
    '\': return "%5c".
    ']': return "%5d".
    '^': return "%5e".
    '`': return "%60".
    '{': return "%7b".
    '|': return "%7c".
    '}': return "%7d".
    '~': return "%7e".
```

Requirement ids: none. pct_encode restates Table 6-1 (R-0155) as a case list (`requirements.yaml` `excluded`).

**N-0308.** §6.1.2.3 Pseudocode for algorithm, pct_encode, step 5 (end) / p. 28 / L1280-L1281 `[none: pseudocode]`

```text
  end case.
end.
```

Requirement ids: none. Closes pct_encode, which restates Table 6-1 (R-0155) (`requirements.yaml` `excluded`).

###### Listing: function pack(ed,sw_ed,t_sw,t_hw,oth)

**N-0309.** §6.1.2.3 Pseudocode for algorithm, pack, step 1 (signature and purpose) / p. 28 / L1283-L1285 `[none: pseudocode]`

```text
function pack(ed,sw_ed,t_sw,t_hw,oth)
  ;; “Pack” the values of the five arguments into the single edition
  ;; component. If all the values are blank, just return a blank.
```

Note: See DEF-14.

Requirement ids: none. pack restates §6.1.2.2 step 3 (R-0160, R-0162) (`requirements.yaml` `excluded`).

**N-0310.** §6.1.2.3 Pseudocode for algorithm, pack, step 2 (no packing when the four extended values are blank) / p. 28 / L1286-L1291 `[none: pseudocode]`

```text
  if (sw_ed = "" and t_sw = "" and t_hw = "" and oth = "")
    then
      ;; All the extended attributes are blank, so don’t do
      ;; any packing, just return ed.
      return ed.
  end.
```

Requirement ids: none. pack returns the edition alone when the four extended values are blank, as R-0162 states (`requirements.yaml` `excluded`).

**N-0311.** §6.1.2.3 Pseudocode for algorithm, pack, step 3 (pack five values) / p. 28 / L1292-L1295 `[none: pseudocode]`

```text
  ;; Otherwise, pack the five values into a single string
  ;; prefixed and internally delimited with the tilde.
  return strcat('~',ed,'~',sw_ed,'~',t_sw,'~',t_hw,'~',oth).
end.
```

Requirement ids: none. pack joins the five values with tildes, as R-0160 states (`requirements.yaml` `excluded`).

###### Listing: function trim(s)

**N-0312.** §6.1.2.3 Pseudocode for algorithm, trim, step 1 (signature and purpose) / p. 28 / L1297-L1298 `[none: pseudocode]`

```text
function trim(s)
  ;; Remove trailing colons from the URI back to the first non-colon.
```

Requirement ids: none. trim restates §6.1.2.2 step 7 (R-0167) (`requirements.yaml` `excluded`).

**N-0313.** §6.1.2.3 Pseudocode for algorithm, trim, step 2 (reverse and initialise) / p. 28 / L1299-L1300 `[none: pseudocode]`

```text
  s1 := reverse(s).
  idx := 0.
```

Requirement ids: none. trim restates §6.1.2.2 step 7 (R-0167) (`requirements.yaml` `excluded`).

**N-0314.** §6.1.2.3 Pseudocode for algorithm, trim, step 3 (count trailing colons) / p. 28 / L1301-L1305 `[none: pseudocode]`

```text
  for i := 0 to strlen(s1) do
    if substr(s1,i,i) = ":"
      then idx := idx + 1.
      else break.
  end.
```

Note: See DEF-15.

Requirement ids: none. trim restates §6.1.2.2 step 7 (R-0167) (`requirements.yaml` `excluded`).

**N-0315.** §6.1.2.3 Pseudocode for algorithm, trim, step 4 (return) / p. 28 / L1306-L1309 `[none: pseudocode]`

```text
  ;; Return the substring after all trailing colons,
  ;; reversed back to its original character order.
  return reverse(substr(s1,idx,strlen(s1)-1)).
end.
```

Requirement ids: none. trim restates §6.1.2.2 step 7 (R-0167) (`requirements.yaml` `excluded`).

###### Helper functions defined by comments (p. 29)

**N-0316.** §6.1.2.3 Pseudocode for algorithm, function strcat / p. 29 / L1319-L1326 `[none: pseudocode]`

```text
function strcat(s1,s2,...sn)
  ;; Returns a copy of the string s1 with the strings s2 to sn
  ;; appended in the order given.
  ;; Cf. the GNU C definition of strcat. This function shown
  ;; here differs only in that it can take a variable number
  ;; of arguments. This is really just shorthand for,
  ;; strcat(s1, strcat(s2, strcat(s3, … ))).
end.
```

Requirement ids: none. A generic string helper (`requirements.yaml` `excluded`; R-0002 points to GNU C for such helpers).

**N-0317.** §6.1.2.3 Pseudocode for algorithm, function strlen / p. 29 / L1328-L1331 `[none: pseudocode]`

```text
function strlen(s)
  ;; Defined as in GNU C, returns the length of string s.
  ;; Returns zero if the string is empty.
end.
```

Requirement ids: none. A generic string helper (`requirements.yaml` `excluded`; R-0002 points to GNU C for such helpers).

**N-0318.** §6.1.2.3 Pseudocode for algorithm, function substr / p. 29 / L1333-L1337 `[must; pseudocode]`

```text
function substr(s,b,e)
  ;; Returns a substring of s, beginning at the b’th character,
  ;; with 0 being the first character, and ending at the e’th
  ;; character. b must be <= e. Returns nil if b >= strlen(s).
end.
```

Requirement ids: nistir-7695#R-0171.

**N-0319.** §6.1.2.3 Pseudocode for algorithm, function reverse / p. 29 / L1339-L1343 `[none: pseudocode]`

```text
function reverse(s)
  ;; Returns a reverse copy of string s, i.e., the last character
  ;; becomes the first character, the second-to-last becomes the
  ;; second character, etc.
end.
```

Requirement ids: none. A generic string helper (`requirements.yaml` `excluded`; R-0002 points to GNU C for such helpers).

**N-0320.** §6.1.2.3 Pseudocode for algorithm, function is_alphanum / p. 29 / L1345-L1348 `[none: pseudocode]`

```text
function is_alphanum(c)
  ;; Returns TRUE iff c is an uppercase letter, a lowercase letter,
  ;; a digit, or the underscore, otherwise FALSE.
end.
```

Note: See D-14.

Requirement ids: nistir-7695#R-0172.

The five examples of §6.1.2.4 (L1352-L1431) are excluded.

#### 6.1.3 Unbinding a URI to a WFN

**N-0321.** §6.1.3 Unbinding a URI to a WFN, paragraph 1, sentence 1 / p. 31 / L1435-L1436 `[none: declarative]`

> Given a CPE v2.2-conformant URI, the procedure to unbind it to a WFN is specified in pseudocode below.

Requirement ids: none. Introduces the unbind_URI pseudocode, which binds through R-0178.

**N-0322.** §6.1.3 Unbinding a URI to a WFN, paragraph 1, sentence 2 / p. 31 / L1436-L1437 `[none: declarative]`

> The top-level unbinding function, unbind_URI, is called with the URI to be unbound as its only argument.

Requirement ids: none. Names the top-level function; the pseudocode binds through R-0178.

**N-0323.** §6.1.3 Unbinding a URI to a WFN, paragraph 1, sentence 7 / p. 31 / L1440-L1441 `[none: declarative]`

> Note that the pseudocode below reuses a number of helper functions defined above in Section 6.1.2.3.

Requirement ids: none. Points to the helpers of §6.1.2.3; it constrains nothing.

**N-0324.** §6.1.3 Unbinding a URI to a WFN, paragraph 1, sentence 8 / p. 31 / L1441-L1442 `[none: declarative]`

> The algorithm expects that the syntax of the input URI conforms to the ABNF in Figure 6-1 or Figure 6-2.

Requirement ids: nistir-7695#R-0173 (one entry for N-0324 and N-0325).

**N-0325.** §6.1.3 Unbinding a URI to a WFN, paragraph 1, sentence 9 / p. 31 / L1442 `[none: declarative]`

> (This is guaranteed if the URI is the result of binding a WFN.)

Note: See D-2 and D-3.

Requirement ids: nistir-7695#R-0173 (one entry for N-0324 and N-0325).

**N-0326.** §6.1.3 Unbinding a URI to a WFN, paragraph 1, sentence 10 / p. 31 / L1442-L1444 `[none: declarative]`

> The algorithm performs some limited error checking and handling: (1) if an illegal percent-encoded form is encountered, an error is raised; (2) if unquoted special characters are used in a way that violates the legal syntax, an error is raised.

Note: See D-6.

Requirement ids: nistir-7695#R-0174, nistir-7695#R-0175 (one entry per error check; the lead-in is in their `condition`).

**N-0327.** §6.1.3 Unbinding a URI to a WFN, paragraph 1, sentence 11 / p. 31 / L1445-L1446 `[SHOULD]`

> A fully robust implementation of the unbinding procedure SHOULD implement additional syntax checks, such as making sure that non-alphanumeric characters do not appear without percent-encoding.

Requirement ids: nistir-7695#R-0176.

**N-0328.** §6.1.3 Unbinding a URI to a WFN, paragraph 2, sentence 1 / p. 31 / L1448-L1449 `[OPTIONAL]`

> It is OPTIONAL for implementations of URI unbinding to follow the pseudocode, processes, and other non-normative information provided in this section.

Note: See D-12.

Requirement ids: nistir-7695#R-0177.

**N-0329.** §6.1.3 Unbinding a URI to a WFN, paragraph 2, sentence 2 / p. 31 / L1449-L1451 `[MUST]`

> However, the result of an implementation performing a URI unbinding MUST produce the same result as the suggested pseudocode, processes, etc. would produce.

Note: See D-12.

Requirement ids: nistir-7695#R-0178.

##### 6.1.3.1 Summary of algorithm

**N-0330.** §6.1.3.1 Summary of algorithm, lead-in / p. 31 / L1455 `[none: lead-in]`

> The procedure for unbinding a URI is straightforward:

Requirement ids: none. Lead-in to the summary steps R-0179 to R-0181.

**N-0331.** §6.1.3.1 Summary of algorithm, step 1 / p. 31 / L1456-L1457 `[none: procedure step]`

> Loop over the seven attributes corresponding to the seven CPE v2.2 components, performing steps 2 through 7.

Note: the summary has three steps (DEF-8).

Requirement ids: nistir-7695#R-0179.

**N-0332.** §6.1.3.1 Summary of algorithm, step 2 / p. 31 / L1458-L1460 `[none: procedure step]`

> For URI components 1-5 and 7, decode the string and set the corresponding WFN attribute value. Decoding entails: converting sole "" to ANY, sole "-" to NA, adding quoting to embedded periods and hyphens, and decoding percent-encoded forms.

Note: See D-13.

Requirement ids: nistir-7695#R-0180.

**N-0333.** §6.1.3.1 Summary of algorithm, step 3 / p. 31 / L1461-L1462 `[none: procedure step]`

> The edition component is "unpacked" if a leading tilde indicates it contains a packed collection of five attribute values.

Requirement ids: nistir-7695#R-0181.

##### 6.1.3.2 Pseudocode for algorithm

Six functions (PDF pp. 31-35, L1466-L1691).

###### Listing: function unbind_URI(uri)

**N-0334.** §6.1.3.2 Pseudocode for algorithm, unbind_URI, step 1 (signature, purpose, empty WFN) / p. 31 / L1466-L1469 `[none: pseudocode]`

```text
function unbind_URI(uri)
  ;; Top-level function used to unbind a URI uri to a WFN.
  ;; Initialize the empty WFN.
  result := new().
```

Requirement ids: none. Starts unbind_URI with new() (R-0100); binds through R-0178.

**N-0335.** §6.1.3.2 Pseudocode for algorithm, unbind_URI, step 2 (loop over seven components) / p. 31 / L1470-L1473 `[none: pseudocode]`

```text
  for i := 1 to 7
    do
      v := get_comp_uri(uri,i). ; get the i’th component of uri
      ;; unbind the parsed string.
```

Requirement ids: nistir-7695#R-0182 (one entry for N-0335 and N-0336).

**N-0336.** §6.1.3.2 Pseudocode for algorithm, unbind_URI, step 3 (components 1 to 5) / p. 31 / L1474-L1479 `[none: pseudocode]`

```text
      case i:
        1: result := set(result,part,decode(v)).
        2: result := set(result,vendor,decode(v)).
        3: result := set(result,product,decode(v)).
        4: result := set(result,version,decode(v)).
        5: result := set(result,update,decode(v)).
```

Requirement ids: nistir-7695#R-0182 (one entry for N-0335 and N-0336).

**N-0337.** §6.1.3.2 Pseudocode for algorithm, unbind_URI, step 4 (component 6: edition, unpack if packed) / p. 32 / L1487-L1498 `[none: pseudocode]`

```text
        6: ;; Special handling for edition component.
           ;; Unpack edition if needed.
           if (v = "" or v = "-" or substr(v,0,0) != "~")
             then
               ;; Just a logical value or a non-packed value.
               ;; So unbind to legacy edition, leaving other
               ;; extended attributes unspecified.
               result := set(result,edition,decode(v)).
             else
               ;; We have five values packed together here
               result := unpack(v,result).
           end.
```

Note: See D-7 and DEF-17.

Requirement ids: nistir-7695#R-0183 (one entry for N-0337, with part of N-0338).

**N-0338.** §6.1.3.2 Pseudocode for algorithm, unbind_URI, step 5 (component 7 and loop end) / p. 32 / L1499-L1501 `[none: pseudocode]`

```text
        7: result := set(result,language,decode(v)).
      end.
  end.
```

Requirement ids: nistir-7695#R-0183 (its first line is the entry's last line; the two "end." lines close the case and the loop).

**N-0339.** §6.1.3.2 Pseudocode for algorithm, unbind_URI, step 6 (return) / p. 32 / L1502-L1503 `[none: pseudocode]`

```text
  return result.
end.
```

Requirement ids: none. Returns the WFN; binds through R-0178.

###### Listing: function get_comp_uri(uri,i)

**N-0340.** §6.1.3.2 Pseudocode for algorithm, function get_comp_uri / p. 32 / L1505-L1517 `[none: pseudocode]`

```text
function get_comp_uri(uri,i)
  ;; Return the i’th CPE component of the URI. If i=0,
  ;; return the URI scheme. For example, given URI:
  ;; cpe:/a:foo::bar:-
  ;; get_comp_uri(uri,0) = "cpe:"
  ;; get_comp_uri(uri,1) = "a"
  ;; get_comp_uri(uri,2) = "foo"
  ;; get_comp_uri(uri,3) = ""
  ;; get_comp_uri(uri,4) = "bar"
  ;; get_comp_uri(uri,5) = "-"
  ;; get_comp_uri(uri,6) = ""
  ;; etc.
end.
```

Requirement ids: nistir-7695#R-0184.

###### Listing: function decode(s)

**N-0341.** §6.1.3.2 Pseudocode for algorithm, decode, step 1 (signature and purpose) / p. 32 / L1519-L1525 `[none: pseudocode]`

```text
function decode(s)
  ;; This function scans the string s and returns a copy
  ;; with all percent-encoded characters decoded. This
  ;; function is the inverse of pct_encode(s) defined in
  ;; Section 6.1.2.3. Only legal percent-encoded forms are
  ;; decoded.  Others raise an error.
  ;; Decode a blank to logical ANY, and hyphen to logical NA.
```

Note: See DEF-16.

Requirement ids: nistir-7695#R-0185 (the entry quotes L1519-L1524 of this step).

**N-0342.** §6.1.3.2 Pseudocode for algorithm, decode, step 2 (blank to ANY, hyphen to NA) / p. 32 / L1526-L1527 `[none: pseudocode]`

```text
  if (s = '') then return ANY.
  if (s = '-') then return NA.
```

Requirement ids: none. Decodes a blank to ANY and a hyphen to NA, as §6.1.3.1 step 2 states (R-0180); binds through R-0178.

**N-0343.** §6.1.3.2 Pseudocode for algorithm, decode, step 3 (lowercase and initialise) / p. 32 / L1528-L1533 `[none: pseudocode]`

```text
  ;; Start the scanning loop.
  ;; Normalize: convert all uppercase letters to lowercase first.
  s := to_lowercase(s).
  result := "".
  idx := 0.
  embedded := false.
```

Note: See D-8 and D-13.

Requirement ids: nistir-7695#R-0186 (the entry quotes L1529-L1530 of this step).

**N-0344.** §6.1.3.2 Pseudocode for algorithm, decode, step 4 (scan loop) / p. 32 / L1534-L1536 `[none: pseudocode]`

```text
  while (idx < strlen(s))
    do
      c := substr(s,idx,idx).  ; get the idx’th character of s.
```

Requirement ids: none. The scan loop of decode; no rule of its own; binds through R-0178.

**N-0345.** §6.1.3.2 Pseudocode for algorithm, decode, step 5 (quote `.`, `-` and `~`) / pp. 32-33 / L1537-L1550 `[none: pseudocode]`

```text
      ;; deal with dot, hyphen and tilde: decode with quoting
      if ((c = '.') or (c = '-') or (c = '~')) then
        result := strcat(result,"\\",c).
        idx := idx + 1.
        embedded := true.  ; a non-%01 encountered.
        continue.
      endif.
```

Note: See D-7.

Requirement ids: nistir-7695#R-0187 (the entry quotes L1537-L1546 of this step).

**N-0346.** §6.1.3.2 Pseudocode for algorithm, decode, step 6 (other unencoded characters pass) / p. 33 / L1551-L1556 `[none: pseudocode]`

```text
      if (c != '%') then
        result := strcat(result,c).
        idx := idx + 1.
        embedded := true.  ; a non-%01 encountered.
        continue.
      endif.
```

Requirement ids: none. Copies any other unencoded character unchanged. No entry of its own; the result binds through R-0178. It is why decode accepts an unencoded asterisk (fixture URI-NEG-09, finding F-35).

**N-0347.** §6.1.3.2 Pseudocode for algorithm, decode, step 7 (three-character form) / p. 33 / L1557-L1559 `[none: pseudocode]`

```text
      ;; we get here if we have a substring starting w/ '%'.
      form := substr(s,idx,idx+2).   ; get the three-char sequence
      case form:
```

Requirement ids: none. Reads the three-character percent form for the case list; binds through R-0178.

**N-0348.** §6.1.3.2 Pseudocode for algorithm, decode, step 8 (case `"%01"`) / p. 33 / L1560-L1578 `[must, must; pseudocode]`

```text
        ;; pseudocode below uses \ within quotes as escape char
        "%01": if ;; %01 legal at beginning or end
                  (((idx = 0) or (idx = (strlen(s)-3))) or
                   ;; embedded is false, so must be preceded by %01
                   (!embedded and (substr(s,idx-3,idx-1) = "%01")) or
                   ;; embedded is true, so must be followed by %01
                   (embedded and (strlen(s) >= idx+6) and
                    (substr(s,idx+3,idx+5) = "%01")))
                 then
                   ;; A percent-encoded question mark is found
                   ;; at the beginning or the end of the string,
                   ;; or embedded in sequence as required.
                   ;; Decode to unquoted form.
                   result := strcat(result,"?").
                   idx := idx + 3.
                   continue.
                 else
                   error.  ;; raise an exception
               endif.
```

Note: See D-2 and D-10.

Requirement ids: nistir-7695#R-0188 (the entry quotes L1561-L1578 of this step).

**N-0349.** §6.1.3.2 Pseudocode for algorithm, decode, step 9 (case `"%02"`) / p. 33 / L1579-L1587 `[none: pseudocode]`

```text
        "%02": if ((idx = 0) or (idx = (strlen(s)-3)))
                 then
                   ;; Percent-encoded asterisk is at the beginning
                   ;; or the end of the string, as required.
                   ;; Decode to unquoted form.
                   result := strcat(result,"*").
                 else
                   error.  ;; raise an exception
               endif.
```

Note: See D-1.

Requirement ids: nistir-7695#R-0189.

**N-0350.** §6.1.3.2 Pseudocode for algorithm, decode, step 10 (cases `"%21"` to `"%7e"`) / pp. 33-34 / L1588-L1623 `[none: pseudocode]`

```text
        "%21": result := strcat(result,"\\!").
        "%22": result := strcat(result,"\\\"").
        "%23": result := strcat(result,"\\#").
        "%24": result := strcat(result,"\\$").
        "%25": result := strcat(result,"\\%").
        "%26": result := strcat(result,"\\&").
        "%27": result := strcat(result,"\\'").
        "%28": result := strcat(result,"\\(").
        "%29": result := strcat(result,"\\)").
        "%2a": result := strcat(result,"\\*").
        "%2b": result := strcat(result,"\\+").
        "%2c": result := strcat(result,"\\,").
        "%2f": result := strcat(result,"\\/").
        "%3a": result := strcat(result,"\\:").
        "%3b": result := strcat(result,"\\;").
        "%3c": result := strcat(result,"\\<").
        "%3d": result := strcat(result,"\\=").
        "%3e": result := strcat(result,"\\>").
        "%3f": result := strcat(result,"\\?").
        "%40": result := strcat(result,"\\@").
        "%5b": result := strcat(result,"\\[").
        "%5c": result := strcat(result,"\\\\").
        "%5d": result := strcat(result,"\\]").
        "%5e": result := strcat(result,"\\^").
        "%60": result := strcat(result,"\\`").
        "%7b": result := strcat(result,"\\{").
        "%7c": result := strcat(result,"\\|").
        "%7d": result := strcat(result,"\\}").
        "%7e": result := strcat(result,"\\~").
```

Note: See DEF-13 on `"\\"`.

Requirement ids: none. Decodes the 29 percent forms of Table 6-1 to their quoted characters, the inverse of R-0155 (the notes of R-0185 cite these lines); binds through R-0178.

**N-0351.** §6.1.3.2 Pseudocode for algorithm, decode, step 11 (any other form is an error) / p. 34 / L1624-L1625 `[none: pseudocode]`

```text
        else: error.  ; any other form is an error
      end case.
```

Note: See D-6.

Requirement ids: none. Any other form is an error: quoted in the notes of R-0185; the rule is error check (1), R-0174.

**N-0352.** §6.1.3.2 Pseudocode for algorithm, decode, step 12 (advance and close loop) / p. 34 / L1626-L1628 `[none: pseudocode]`

```text
    idx := idx + 3.
    embedded := true. ; a non-%01 encountered.
  end.
```

Requirement ids: none. Advances and closes the loop of decode; binds through R-0178.

**N-0353.** §6.1.3.2 Pseudocode for algorithm, decode, step 13 (return) / p. 34 / L1629-L1630 `[none: pseudocode]`

```text
  return result.
end.
```

Requirement ids: none. Returns the result of decode; binds through R-0178.

###### Listing: function unpack(s,wfn)

**N-0354.** §6.1.3.2 Pseudocode for algorithm, unpack, step 1 (signature and purpose) / p. 34 / L1632-L1635 `[none: pseudocode]`

```text
function unpack(s,wfn).
  ;; Argument s is a packed edition string, wfn is a WFN.
  ;; Unpack its elements and set the attributes in wfn accordingly.
  ;; Parse out the five elements.
```

Note: See DEF-12.

Requirement ids: none. unpack's signature and comment; the parsing it introduces is described in the notes of R-0190; binds through R-0178.

**N-0355.** §6.1.3.2 Pseudocode for algorithm, unpack, step 2 (legacy edition) / p. 34 / L1636-L1641 `[none: pseudocode]`

```text
  start := 1.
  end := strchr(s,'~',start).
  if (start = end)
    then ed := "".
    else ed := substr(s,start,end-1).
  end.
```

Note: See DEF-17.

Requirement ids: none. unpack's parsing of the legacy edition field (L1636 to L1671, described in the notes of R-0190); binds through R-0178.

**N-0356.** §6.1.3.2 Pseudocode for algorithm, unpack, step 3 (sw_edition) / p. 34 / L1642-L1647 `[none: pseudocode]`

```text
  start := end+1.
  end := strchr(s,'~',start).
  if (start = end)
    then sw_ed := "".
    else sw_ed := substr(s,start,end-1).
  end.
```

Requirement ids: none. unpack's parsing of the sw_edition field (L1636 to L1671, described in the notes of R-0190); binds through R-0178.

**N-0357.** §6.1.3.2 Pseudocode for algorithm, unpack, step 4 (target_sw) / p. 34 / L1648-L1653 `[none: pseudocode]`

```text
  start := end+1.
  end := strchr(s,'~',start).
  if (start = end)
    then t_sw := "".
    else t_sw := substr(s,start,end-1).
  end.
```

Requirement ids: none. unpack's parsing of the target_sw field (L1636 to L1671, described in the notes of R-0190); binds through R-0178.

**N-0358.** §6.1.3.2 Pseudocode for algorithm, unpack, step 5 (target_hw) / pp. 34-35 / L1654-L1666 `[none: pseudocode]`

```text
  start := end+1.
  end := strchr(s,'~',start).
  if (start = end)
    then t_hw := "".
    else t_hw := substr(s,start,end-1).
  end.
```

Requirement ids: none. unpack's parsing of the target_hw field (L1636 to L1671, described in the notes of R-0190); binds through R-0178.

**N-0359.** §6.1.3.2 Pseudocode for algorithm, unpack, step 6 (other) / p. 35 / L1667-L1671 `[none: pseudocode]`

```text
  start := end+1.
  if (start >= strlen(s))
    then oth := "".
    else oth := substr(s,start,strlen(s)-1).
  end.
```

Requirement ids: none. unpack's parsing of the other field (L1636 to L1671, described in the notes of R-0190); binds through R-0178.

**N-0360.** §6.1.3.2 Pseudocode for algorithm, unpack, step 7 (set the five attributes) / p. 35 / L1672-L1676 `[none: pseudocode]`

```text
  wfn := set(wfn,edition,decode(ed)).
  wfn := set(wfn,sw_edition,decode(sw_ed)).
  wfn := set(wfn,target_sw,decode(t_sw)).
  wfn := set(wfn,target_hw,decode(t_hw)).
  wfn := set(wfn,other,decode(oth)).
```

Requirement ids: nistir-7695#R-0190 (one entry for N-0360, with part of N-0361).

**N-0361.** §6.1.3.2 Pseudocode for algorithm, unpack, step 8 (return) / p. 35 / L1677-L1678 `[none: pseudocode]`

```text
  return wfn.
end.
```

Requirement ids: nistir-7695#R-0190 (its first line, "return wfn.", is the entry's last line).

###### Helper functions defined by comments (p. 35)

**N-0362.** §6.1.3.2 Pseudocode for algorithm, function strchr / p. 35 / L1680-L1687 `[none: pseudocode]`

```text
function strchr(str,chr,off)
  ;; Searches the string str for the character chr starting
  ;; at offset off into the string. Returns the offset of
  ;; the chr if found, otherwise nil.
  ;; Defined similar to the standard C function strchr.
  ;; But this version takes a third argument off, which
  ;; is an offset into the str to begin the search.
end.
```

Requirement ids: nistir-7695#R-0191.

**N-0363.** §6.1.3.2 Pseudocode for algorithm, function to_lowercase / p. 35 / L1689-L1691 `[none: pseudocode]`

```text
function to_lowercase(s)
  ;; convert all alphabetic characters to lowercase.
end.
```

Requirement ids: none. A generic helper (`requirements.yaml` `excluded`); its use is R-0186.

The eight examples of §6.1.3.3 (L1695-L1794) are excluded.

### 6.2 Formatted String Binding

**N-0364.** §6.2 Formatted String Binding, paragraph 1, sentence 2 / p. 37 / L1798-L1801 `[none: declarative]`

> In keeping with the spirit of the v2.2 specification, the formatted string binding looks similar to the URI binding; however, it is defined simply to be a “formatted string” rather than a URI in order to relax the requirements that typically apply to URIs as specified in [RFC3986].

Requirement ids: none. Explains why the formatted string is not a URI; it constrains nothing.

**N-0365.** §6.2 Formatted String Binding, paragraph 2, sentence 1 / p. 37 / L1803 `[none: declarative]`

> The formatted string binding is a colon-delimited list of fields prefixed with the string "cpe:2.3:".

Requirement ids: nistir-7695#R-0192.

**N-0366.** §6.2 Formatted String Binding, paragraph 2, sentence 3 / p. 37 / L1805-L1806 `[none: declarative]`

> The formal syntax of the formatted string binding is presented in ABNF in Section 6.2.1.

Requirement ids: none. Points to the syntax in §6.2.1 (Figure 6-3, R-0199 to R-0217).

**N-0367.** §6.2 Formatted String Binding, paragraph 3 and the field template (one statement) / p. 37 / L1808-L1812 `[none: declarative]`

> ```text
> Similar to the URI binding, the formatted string binds the attributes in a WFN in a fixed order, separated by the colon character:
> cpe:2.3: part : vendor : product : version : update : edition :
>        language : sw_edition : target_sw : target_hw : other
> ```

Note: the template is at the columns of the PDF (Courier New, 11 pt).

Requirement ids: nistir-7695#R-0193 (the field template line is the entry's enumeration item).

**N-0368.** §6.2 Formatted String Binding, paragraph 4, sentence 1 / p. 37 / L1814-L1815 `[none: declarative]`

> ```text
> In a formatted string binding, the alphanumeric characters plus hyphen (“-”), period (“.”) and underscore (“_”) appear unquoted.
> ```

Requirement ids: nistir-7695#R-0194.

**N-0369.** §6.2 Formatted String Binding, paragraph 4, sentence 2 / p. 37 / L1815-L1816 `[none: declarative]`

> ```text
> When used alone, the asterisk (“*”) represents the logical value ANY, and the hyphen (“-”) represents the logical value NA.
> ```

Requirement ids: nistir-7695#R-0195.

**N-0370.** §6.2 Formatted String Binding, paragraph 4, sentence 3 / p. 37 / L1816-L1817 `[MUST]`

> All other non-alphanumeric characters, if used, MUST be quoted (preceded by the backslash).

Requirement ids: nistir-7695#R-0196.

**N-0371.** §6.2 Formatted String Binding, paragraph 4, sentence 4 / p. 37 / L1817-L1818 `[may]`

> The special characters asterisk and question mark may appear without quoting, in which case they are open to special interpretation by other CPE specifications.

Note: (inferred) the lowercase "may" grants a permission here.

Requirement ids: nistir-7695#R-0197.

**N-0372.** §6.2 Formatted String Binding, paragraph 4, sentence 5 / p. 37 / L1818-L1819 `[MUST]`

> Note that all eleven (11) attribute values MUST appear in the formatted string binding.

Note: See D-11.

Requirement ids: nistir-7695#R-0198.

#### 6.2.1 Syntax for Formatted String Binding

**N-0373.** §6.2.1 Syntax for Formatted String Binding, paragraph 1 / p. 37 / L1823 `[none: declarative]`

> The syntax of the formatted string binding is shown in Figure 6-3.

Requirement ids: none. Points to Figure 6-3 (R-0199 to R-0217); the notes of R-0199 quote it.

##### Figure 6-3. ABNF for Formatted String Binding (p. 38, L1834-L1869)

Twenty-nine rules, at the columns of the PDF figure.

**N-0374.** §6.2.1 Syntax for Formatted String Binding, Figure 6-3, rule formstring / p. 38 / L1834 `[none: ABNF rule]`

```abnf
formstring      = "cpe:2.3:" component-list
```

Requirement ids: nistir-7695#R-0199.

**N-0375.** §6.2.1 Syntax for Formatted String Binding, Figure 6-3, rule component-list / p. 38 / L1836-L1838 `[none: ABNF rule]`

```abnf
component-list  = part ":" vendor ":" product ":" version ":" update ":"
                  edition ":" lang ":" sw_edition ":" target_sw ":"
                  target_hw ":" other
```

Requirement ids: nistir-7695#R-0200.

**N-0376.** §6.2.1 Syntax for Formatted String Binding, Figure 6-3, rule part / p. 38 / L1840 `[none: ABNF rule]`

```abnf
part            = "h" / "o" / "a" / logical
```

Note: See D-4.

Requirement ids: nistir-7695#R-0201.

**N-0377.** §6.2.1 Syntax for Formatted String Binding, Figure 6-3, rule vendor / p. 38 / L1841 `[none: ABNF rule]`

```abnf
vendor          = avstring
```

Requirement ids: nistir-7695#R-0202.

**N-0378.** §6.2.1 Syntax for Formatted String Binding, Figure 6-3, rule product / p. 38 / L1842 `[none: ABNF rule]`

```abnf
product         = avstring
```

Requirement ids: nistir-7695#R-0203.

**N-0379.** §6.2.1 Syntax for Formatted String Binding, Figure 6-3, rule version / p. 38 / L1843 `[none: ABNF rule]`

```abnf
version         = avstring
```

Requirement ids: nistir-7695#R-0204.

**N-0380.** §6.2.1 Syntax for Formatted String Binding, Figure 6-3, rule update / p. 38 / L1844 `[none: ABNF rule]`

```abnf
update          = avstring
```

Requirement ids: nistir-7695#R-0205.

**N-0381.** §6.2.1 Syntax for Formatted String Binding, Figure 6-3, rule edition / p. 38 / L1845 `[none: ABNF rule]`

```abnf
edition         = avstring
```

Requirement ids: nistir-7695#R-0206.

**N-0382.** §6.2.1 Syntax for Formatted String Binding, Figure 6-3, rule lang / p. 38 / L1846 `[none: ABNF rule]`

```abnf
lang            = LANGTAG / logical
```

Note: See D-5.

Requirement ids: nistir-7695#R-0207.

**N-0383.** §6.2.1 Syntax for Formatted String Binding, Figure 6-3, rule sw_edition / p. 38 / L1847 `[none: ABNF rule]`

```abnf
sw_edition      = avstring
```

Requirement ids: nistir-7695#R-0208.

**N-0384.** §6.2.1 Syntax for Formatted String Binding, Figure 6-3, rule target_sw / p. 38 / L1848 `[none: ABNF rule]`

```abnf
target_sw       = avstring
```

Requirement ids: nistir-7695#R-0209.

**N-0385.** §6.2.1 Syntax for Formatted String Binding, Figure 6-3, rule target_hw / p. 38 / L1849 `[none: ABNF rule]`

```abnf
target_hw       = avstring
```

Requirement ids: nistir-7695#R-0210.

**N-0386.** §6.2.1 Syntax for Formatted String Binding, Figure 6-3, rule other / p. 38 / L1850 `[none: ABNF rule]`

```abnf
other           = avstring
```

Requirement ids: nistir-7695#R-0211.

**N-0387.** §6.2.1 Syntax for Formatted String Binding, Figure 6-3, rule avstring / p. 38 / L1851 `[none: ABNF rule]`

```abnf
avstring        = *1spec_chrs 1*( unreserved / quoted ) *1spec_chrs / logical
```

Note: See D-1 and D-2.

Requirement ids: nistir-7695#R-0212.

**N-0388.** §6.2.1 Syntax for Formatted String Binding, Figure 6-3, rule spec_chrs / p. 38 / L1852 `[none: ABNF rule]`

```abnf
spec_chrs       = 1*spec1 / spec2
```

Requirement ids: nistir-7695#R-0048 (printed identically in Figure 5-1, the entry's locator; this copy is in its `also_at`).

**N-0389.** §6.2.1 Syntax for Formatted String Binding, Figure 6-3, rule logical / p. 38 / L1853 `[none: ABNF rule]`

```abnf
logical         = "*" / "-"
```

Requirement ids: nistir-7695#R-0213.

**N-0390.** §6.2.1 Syntax for Formatted String Binding, Figure 6-3, rule special / p. 38 / L1854 `[none: ABNF rule]`

```abnf
special         = spec1 / spec2
```

Requirement ids: nistir-7695#R-0058 (printed identically in Figure 5-1, the entry's locator; this copy is in its `also_at`).

**N-0391.** §6.2.1 Syntax for Formatted String Binding, Figure 6-3, rule spec1 / p. 38 / L1855 `[none: ABNF rule]`

```abnf
spec1           = "?"
```

Requirement ids: nistir-7695#R-0049 (printed identically in Figure 5-1, the entry's locator; this copy is in its `also_at`).

**N-0392.** §6.2.1 Syntax for Formatted String Binding, Figure 6-3, rule spec2 / p. 38 / L1856 `[none: ABNF rule]`

```abnf
spec2           = "*"
```

Requirement ids: nistir-7695#R-0050 (printed identically in Figure 5-1, the entry's locator; this copy is in its `also_at`).

**N-0393.** §6.2.1 Syntax for Formatted String Binding, Figure 6-3, rule unreserved / p. 38 / L1857 `[none: ABNF rule]`

```abnf
unreserved      = ALPHA / DIGIT / "-" / "." / "_"
```

Requirement ids: nistir-7695#R-0135 (printed identically in Figure 6-2, the entry's locator; this copy is in its `also_at`).

**N-0394.** §6.2.1 Syntax for Formatted String Binding, Figure 6-3, rule quoted / p. 38 / L1858 `[none: ABNF rule]`

```abnf
quoted          = escape (escape / special / punc)
```

Requirement ids: nistir-7695#R-0214.

**N-0395.** §6.2.1 Syntax for Formatted String Binding, Figure 6-3, rule escape / p. 38 / L1859 `[none: ABNF rule]`

```abnf
escape          = "\"
```

Requirement ids: nistir-7695#R-0057 (printed identically in Figure 5-1, the entry's locator; this copy is in its `also_at`).

**N-0396.** §6.2.1 Syntax for Formatted String Binding, Figure 6-3, rule punc / p. 38 / L1860-L1862 `[none: ABNF rule]`

```abnf
punc            = "!" / DQUOTE / "#" / "$" / "%" / "&" / "'" / "(" / ")" /
                  "+" / "," / "/" / ":" / ";" / "<" / "=" / ">" / "@" /
                  "[" / "]" / "^" / "`" / "{" / "|" / "}" / "~"
```

Requirement ids: nistir-7695#R-0215.

**N-0397.** §6.2.1 Syntax for Formatted String Binding, Figure 6-3, rule ALPHA / p. 38 / L1863 `[none: ABNF rule]`

```abnf
ALPHA           = %x41-5a / %x61-7A   ; a-z
```

Note: the comment says "a-z" for a rule that also covers A-Z (DEF-6).

Requirement ids: nistir-7695#R-0216.

**N-0398.** §6.2.1 Syntax for Formatted String Binding, Figure 6-3, rule DIGIT / p. 38 / L1864 `[none: ABNF rule]`

```abnf
DIGIT           = %x30-39  ; 0-9
```

Requirement ids: nistir-7695#R-0064 (printed identically in Figure 5-1, the entry's locator; this copy is in its `also_at`).

**N-0399.** §6.2.1 Syntax for Formatted String Binding, Figure 6-3, rule DQUOTE / p. 38 / L1865 `[none: ABNF rule]`

```abnf
DQUOTE          = %x22  ; double-quote
```

Requirement ids: nistir-7695#R-0217.

**N-0400.** §6.2.1 Syntax for Formatted String Binding, Figure 6-3, rule LANGTAG / p. 38 / L1866 `[none: ABNF rule]`

```abnf
LANGTAG         = language ["-" region] ; cf. [RFC5646]
```

Note: See D-5.

Requirement ids: nistir-7695#R-0140 (printed identically in Figure 6-2, the entry's locator; this copy is in its `also_at`).

**N-0401.** §6.2.1 Syntax for Formatted String Binding, Figure 6-3, rule language / p. 38 / L1867 `[none: ABNF rule]`

```abnf
language        = 2*3ALPHA              ; shortest ISO 639 code
```

Requirement ids: nistir-7695#R-0141 (printed identically in Figure 6-2, the entry's locator; this copy is in its `also_at`).

**N-0402.** §6.2.1 Syntax for Formatted String Binding, Figure 6-3, rule region / p. 38 / L1868 `[none: ABNF rule]`

```abnf
region          = 2ALPHA / 3DIGIT       ; ISO 3166-1 code or UN M.49 code
```

Requirement ids: nistir-7695#R-0142 (printed identically in Figure 6-2, the entry's locator; this copy is in its `also_at`).

#### 6.2.2 Binding a WFN to a formatted string

**N-0403.** §6.2.2 Binding a WFN to a formatted string, paragraph 1, sentence 1 / p. 38 / L1874 `[SHALL]`

> This section specifies the procedure that SHALL be followed when binding a WFN to a formatted string.

Note: See D-12.

Requirement ids: nistir-7695#R-0218.

**N-0404.** §6.2.2 Binding a WFN to a formatted string, paragraph 2, sentence 1 / p. 38 / L1879-L1880 `[OPTIONAL]`

> It is OPTIONAL for implementations of formatted string binding to follow the pseudocode, processes, and other non-normative information provided in this section.

Note: See D-12.

Requirement ids: nistir-7695#R-0219.

**N-0405.** §6.2.2 Binding a WFN to a formatted string, paragraph 2, sentence 2 / p. 38 / L1880-L1882 `[MUST]`

> However, the result of an implementation performing a formatted string binding MUST produce the same result as the suggested pseudocode, processes, etc. would produce.

Note: See D-9 and D-12.

Requirement ids: nistir-7695#R-0220.

##### 6.2.2.1 Summary of algorithm

**N-0406.** §6.2.2.1 Summary of algorithm, sentence 1 / p. 39 / L1894 `[none: declarative]`

> The procedure iterates over the eleven allowed attributes in a fixed order.

Requirement ids: nistir-7695#R-0221 (one entry for N-0406 to N-0408).

**N-0407.** §6.2.2.1 Summary of algorithm, sentence 2 / p. 39 / L1894-L1895 `[none: declarative]`

> Corresponding attribute values are obtained from the input WFN and conversions of logical values are applied.

Note: See D-13.

Requirement ids: nistir-7695#R-0221 (one entry for N-0406 to N-0408).

**N-0408.** §6.2.2.1 Summary of algorithm, sentence 3 / p. 39 / L1895-L1896 `[none: declarative]`

> A result string is formed by concatenating the attribute values separated by colons.

Requirement ids: nistir-7695#R-0221 (one entry for N-0406 to N-0408).

##### 6.2.2.2 Pseudocode for algorithm

Three functions (PDF pp. 39-40, L1900-L1964).

###### Listing: function bind_to_fs(w)

**N-0409.** §6.2.2.2 Pseudocode for algorithm, bind_to_fs, step 1 (signature, purpose, initialise) / p. 39 / L1900-L1903 `[none: pseudocode]`

```text
function bind_to_fs(w)
  ;; Top-level function used to bind WFN w to formatted string.
  ;; Initialize the output with the CPE v2.3 string prefix.
  fs := "cpe:2.3:".
```

Requirement ids: none. bind_to_fs restates §6.2 (R-0192, R-0193, R-0198) and §6.2.2.1 (R-0221) (`requirements.yaml` `excluded`); this step sets the prefix of R-0192.

**N-0410.** §6.2.2.2 Pseudocode for algorithm, bind_to_fs, step 2 (loop over eleven attributes) / p. 39 / L1904-L1906 `[none: pseudocode]`

```text
  foreach a in {part,vendor,product,version,update,edition,language,
                sw_edition,target_sw,target_hw,other}
    do
```

Requirement ids: none. Loops over the eleven attributes in the order of R-0193, whose notes cite these lines, as R-0221 states (`requirements.yaml` `excluded`, bind_to_fs).

**N-0411.** §6.2.2.2 Pseudocode for algorithm, bind_to_fs, step 3 (bind and append the value) / p. 39 / L1907-L1908 `[none: pseudocode]`

```text
      v := bind_value_for_fs(get(w,a)).
      fs := strcat(fs,v).
```

Requirement ids: none. Binds and appends each value, as R-0221 states (`requirements.yaml` `excluded`, bind_to_fs).

**N-0412.** §6.2.2.2 Pseudocode for algorithm, bind_to_fs, step 4 (colon except after other; loop end) / p. 39 / L1909-L1911 `[none: pseudocode]`

```text
      ;; add a colon except at the very end
      if (a != other) then fs := strcat(fs,":").
  end.
```

Requirement ids: none. Separates the values with colons, as R-0221 states, so that all eleven appear (R-0198) (`requirements.yaml` `excluded`, bind_to_fs).

**N-0413.** §6.2.2.2 Pseudocode for algorithm, bind_to_fs, step 5 (return) / p. 39 / L1912-L1913 `[none: pseudocode]`

```text
  return fs.
end.
```

Requirement ids: none. Returns the formatted string (`requirements.yaml` `excluded`, bind_to_fs).

###### Listing: function bind_value_for_fs(v)

**N-0414.** §6.2.2.2 Pseudocode for algorithm, bind_value_for_fs, step 1 (signature, purpose, case) / p. 39 / L1915-L1918 `[none: pseudocode]`

```text
function bind_value_for_fs(v)
  ;; Convert the value v to its proper string representation for
  ;; insertion into the formatted string.
  case v:
```

Requirement ids: none. bind_value_for_fs restates R-0195 and calls process_quoted_chars (`requirements.yaml` `excluded`).

**N-0415.** §6.2.2.2 Pseudocode for algorithm, bind_value_for_fs, step 2 (ANY to `*`, NA to `-`) / p. 39 / L1919-L1920 `[none: pseudocode]`

```text
    ANY: return("*").
    NA: return("-").
```

Requirement ids: none. ANY binds to * and NA to -: restates R-0195 (`requirements.yaml` `excluded`, bind_value_for_fs).

**N-0416.** §6.2.2.2 Pseudocode for algorithm, bind_value_for_fs, step 3 (other values) / p. 39 / L1921-L1923 `[none: pseudocode]`

```text
    else: return process_quoted_chars(v).
  end.
end.
```

Requirement ids: none. Hands a string value to process_quoted_chars, whose rule is R-0222 (`requirements.yaml` `excluded`, bind_value_for_fs).

###### Listing: function process_quoted_chars(s)

**N-0417.** §6.2.2.2 Pseudocode for algorithm, process_quoted_chars, step 1 (signature and purpose) / p. 39 / L1925-L1928 `[none: pseudocode]`

```text
function process_quoted_chars(s)
  ;; Inspect each character in string s. Certain nonalpha
  ;; characters pass thru without escaping into the result,
  ;; but most retain escaping.
```

Requirement ids: none. process_quoted_chars' signature and comment; the rule of the function is R-0222; binds through R-0220.

**N-0418.** §6.2.2.2 Pseudocode for algorithm, process_quoted_chars, step 2 (initialise) / p. 39 / L1929-L1930 `[none: pseudocode]`

```text
  result := "".
  idx := 0.
```

Requirement ids: none. Initialises process_quoted_chars; binds through R-0220.

**N-0419.** §6.2.2.2 Pseudocode for algorithm, process_quoted_chars, step 3 (scan loop) / p. 39 / L1931-L1933 `[none: pseudocode]`

```text
  while (idx < strlen(s))
    do
      c := substr(s,idx,idx).  ; get the idx’th character of s.
```

Requirement ids: none. The scan loop of process_quoted_chars; binds through R-0220.

**N-0420.** §6.2.2.2 Pseudocode for algorithm, process_quoted_chars, step 4 (unquoted characters pass) / p. 39 / L1934-L1937 `[none: pseudocode]`

```text
      if c != "\"
        then
          ;; unquoted characters pass thru unharmed
          result := strcat(result,c).
```

Note: See D-2.

Requirement ids: none. Copies unquoted characters unchanged. No entry of its own (`messages.yaml`, formatted-string-binding, quoting_on_binding, describes it); binds through R-0220.

**N-0421.** §6.2.2.2 Pseudocode for algorithm, process_quoted_chars, step 5 (escaped character) / p. 39 / L1938-L1941 `[none: pseudocode]`

```text
        else
          ;; Escaped characters are examined
          nextchr := substr(s,idx+1,idx+1).
          case nextchr:
```

Requirement ids: nistir-7695#R-0222 (its last line, "case nextchr:", is the entry's first line).

**N-0422.** §6.2.2.2 Pseudocode for algorithm, process_quoted_chars, step 6 (`.`, `-` and `_` lose their escape) / pp. 39-40 / L1942-L1953 `[none: pseudocode]`

```text
            ;; the period, hyphen and underscore pass unharmed.
            ".":
            "-":
            "_": result := strcat(result,nextchr).
                 idx = idx + 2.
```

Note: `idx = idx + 2.` with no `continue.`: see D-9.

Requirement ids: nistir-7695#R-0222 (one entry for N-0422 and N-0423, with part of N-0421).

**N-0423.** §6.2.2.2 Pseudocode for algorithm, process_quoted_chars, step 7 (other escapes kept) / p. 40 / L1954-L1959 `[none: pseudocode]`

```text
            else:
              ;; all others retain escaping
              result := strcat(result,"\",nextchr).
              idx := idx + 2.
              continue.
          end.
```

Note: See DEF-13.

Requirement ids: nistir-7695#R-0222 (one entry for N-0422 and N-0423, with part of N-0421).

**N-0424.** §6.2.2.2 Pseudocode for algorithm, process_quoted_chars, step 8 (advance and close loop) / p. 40 / L1960-L1962 `[none: pseudocode]`

```text
      endif.
      idx := idx + 1.
  end.
```

Requirement ids: none. Advances and closes the loop of process_quoted_chars; binds through R-0220. With the first branch of R-0222 it makes the defect of D-9.

**N-0425.** §6.2.2.2 Pseudocode for algorithm, process_quoted_chars, step 9 (return) / p. 40 / L1963-L1964 `[none: pseudocode]`

```text
  return result.
end.
```

Requirement ids: none. Returns the result of process_quoted_chars; binds through R-0220.

The five examples of §6.2.2.3 and the sentence that introduces them (L1968-L2051) are excluded.

#### 6.2.3 Unbinding a formatted string to a WFN

**N-0426.** §6.2.3 Unbinding a formatted string to a WFN, paragraph 1, sentence 1 / p. 42 / L2063-L2064 `[SHALL]`

> Given a formatted string binding, the procedure that SHALL be followed to unbind it to a WFN is specified in pseudocode below.

Note: See D-12.

Requirement ids: nistir-7695#R-0223.

**N-0427.** §6.2.3 Unbinding a formatted string to a WFN, paragraph 1, sentence 2 / p. 42 / L2064-L2065 `[none: declarative]`

> The top-level unbinding function, unbind_fs, is called with the formatted string to be unbound as its only argument.

Requirement ids: none. Names the top-level function; the pseudocode binds through R-0225.

**N-0428.** §6.2.3 Unbinding a formatted string to a WFN, paragraph 2, sentence 1 / p. 42 / L2070-L2071 `[OPTIONAL]`

> It is OPTIONAL for implementations of formatted string unbinding to follow the pseudocode, processes, and other non-normative information provided in this section.

Note: See D-12.

Requirement ids: nistir-7695#R-0224.

**N-0429.** §6.2.3 Unbinding a formatted string to a WFN, paragraph 2, sentence 2 / p. 42 / L2071-L2073 `[MUST]`

> However, the result of an implementation performing a formatted string unbinding MUST produce the same result as the suggested pseudocode, processes, etc. would produce.

Note: See D-10, D-11 and D-12.

Requirement ids: nistir-7695#R-0225.

##### 6.2.3.1 Summary of algorithm

**N-0430.** §6.2.3.1 Summary of algorithm, sentence 1 / p. 42 / L2077-L2078 `[none: declarative]`

> Unbinding a formatted string is straightforward, since the attribute values are encoded explicitly and in a fixed left-to-right order in the binding, delimited by colons.

Requirement ids: none. Describes the procedure (`requirements.yaml` `excluded`); its rules follow in R-0226 to R-0231.

**N-0431.** §6.2.3.1 Summary of algorithm, sentence 2 / p. 42 / L2078-L2079 `[may]`

> (Because a colon may appear embedded in a value string if preceded by the escape character, the parsing function needs to ignore escaped colons.)

Note: "may" here expresses possibility; "needs to" states the rule.

Requirement ids: nistir-7695#R-0226.

**N-0432.** §6.2.3.1 Summary of algorithm, sentence 3 / p. 42 / L2079-L2080 `[none: declarative]`

> The algorithm parses the eleven fields of the formatted string, then unbinds each string result.

Note: See D-11.

Requirement ids: nistir-7695#R-0227.

**N-0433.** §6.2.3.1 Summary of algorithm, sentence 4 / p. 42 / L2080-L2081 `[none: declarative]`

> If a field contains only an asterisk, it is unbound to the logical value ANY.

Requirement ids: nistir-7695#R-0228.

**N-0434.** §6.2.3.1 Summary of algorithm, sentence 5 / p. 42 / L2081-L2082 `[none: declarative]`

> If a field contains only a hyphen, it is unbound to the logical value NA.

Requirement ids: nistir-7695#R-0229.

**N-0435.** §6.2.3.1 Summary of algorithm, sentence 6 / p. 42 / L2082-L2084 `[none: declarative]`

> Quoting of non-alphanumeric characters is restored as needed, but the two special characters (asterisk and question mark) are permitted to appear without a preceding escape character.

Requirement ids: nistir-7695#R-0230.

**N-0436.** §6.2.3.1 Summary of algorithm, sentence 7 / p. 42 / L2084-L2085 `[none: declarative]`

> The unbinding procedure performs limited error checking, only ensuring that unquoted special characters adhere to syntax requirements specified in Figure 5-1.

Note: See D-1 and D-10.

Requirement ids: nistir-7695#R-0231.

##### 6.2.3.2 Pseudocode for algorithm

Four functions (PDF pp. 42-44, L2089-L2219).

###### Listing: function unbind_fs(fs)

**N-0437.** §6.2.3.2 Pseudocode for algorithm, unbind_fs, step 1 (signature, purpose, empty WFN) / p. 42 / L2089-L2091 `[none: pseudocode]`

```text
function unbind_fs(fs)
  ;; Top-level function to unbind a formatted string fs to a wfn.
  result := new().
```

Requirement ids: none. unbind_fs restates §6.2.3.1 (R-0227), with the field order of R-0193 (`requirements.yaml` `excluded`).

**N-0438.** §6.2.3.2 Pseudocode for algorithm, unbind_fs, step 2 (loop over fields 2 to 12) / p. 42 / L2092-L2095 `[none: pseudocode]`

```text
  ;; NB: the cpe scheme is the 0th component, the cpe version is the
  ;; 1st. So we start parsing at the 2nd component.
  for a = 2 to 12
    do
```

Note: See DEF-12.

Requirement ids: none. unbind_fs restates §6.2.3.1 (R-0227), with the field order of R-0193 (`requirements.yaml` `excluded`).

**N-0439.** §6.2.3.2 Pseudocode for algorithm, unbind_fs, step 3 (get and unbind the field) / p. 42 / L2096-L2098 `[none: pseudocode]`

```text
      v := get_comp_fs(fs,a).    ; get the a’th field string
      v := unbind_value_fs(v).   ; unbind the string
      ;; set the value of the corresponding attribute.
```

Note: See D-11.

Requirement ids: none. unbind_fs restates §6.2.3.1 (R-0227), with the field order of R-0193 (`requirements.yaml` `excluded`).

**N-0440.** §6.2.3.2 Pseudocode for algorithm, unbind_fs, step 4 (set the attribute for fields 2 to 12) / pp. 42-43 / L2099-L2119 `[none: pseudocode]`

```text
      case a:
        2: result := set(result,part,v).
        3: result := set(result,vendor,v).
        4: result := set(result,product,v).
        5: result := set(result,version,v).
        6: result := set(result,update,v).
        7: result := set(result,edition,v).
        8: result := set(result,language,v).
        9: result := set(result,sw_edition,v).
       10: result := set(result,target_sw,v).
       11: result := set(result,target_hw,v).
       12: result := set(result,other,v).
      end.
```

Requirement ids: none. unbind_fs restates §6.2.3.1 (R-0227), with the field order of R-0193 (`requirements.yaml` `excluded`).

**N-0441.** §6.2.3.2 Pseudocode for algorithm, unbind_fs, step 5 (loop end and return) / p. 43 / L2120-L2122 `[none: pseudocode]`

```text
  end.
  return result.
end.
```

Requirement ids: none. unbind_fs restates §6.2.3.1 (R-0227), with the field order of R-0193 (`requirements.yaml` `excluded`).

###### Listing: function get_comp_fs(fs,i)

**N-0442.** §6.2.3.2 Pseudocode for algorithm, function get_comp_fs / p. 43 / L2124-L2138 `[none: pseudocode]`

```text
function get_comp_fs(fs,i)
  ;; Return the i’th field of the formatted string.  If i=0,
  ;; return the string to the left of the first forward slash.
  ;; The colon is the field delimiter unless prefixed by a
  ;; backslash.
  ;; For example, given the formatted string:
  ;; cpe:2.3:a:foo:bar\:mumble:1.0:*:…
  ;; get_comp_fs(fs,0) = "cpe"
  ;; get_comp_fs(fs,1) = "2.3"
  ;; get_comp_fs(fs,2) = "a"
  ;; get_comp_fs(fs,3) = "foo"
  ;; get_comp_fs(fs,4) = "bar\:mumble"
  ;; get_comp_fs(fs,5) = "1.0"
  ;; etc.
end.
```

Note: "forward slash" contradicts the example on the same listing (DEF-9).

Requirement ids: nistir-7695#R-0232.

###### Listing: function unbind_value_fs(s)

**N-0443.** §6.2.3.2 Pseudocode for algorithm, unbind_value_fs, step 1 (signature, purpose, case) / p. 43 / L2140-L2145 `[none: pseudocode]`

```text
function unbind_value_fs(s)
  ;; Takes a string value s and returns the appropriate logical
  ;; value if s is the bound form of a logical value. If s is some
  ;; general value string, add quoting of non-alphanumerics as
  ;; needed.
  case s:
```

Requirement ids: none. unbind_value_fs restates R-0228 and R-0229 and calls add_quoting (`requirements.yaml` `excluded`).

**N-0444.** §6.2.3.2 Pseudocode for algorithm, unbind_value_fs, step 2 (`*` to ANY, `-` to NA) / p. 43 / L2146-L2147 `[none: pseudocode]`

```text
    "*": return ANY.
    "-": return NA.
```

Requirement ids: none. "*" unbinds to ANY and "-" to NA: restates R-0228 and R-0229 (`requirements.yaml` `excluded`, unbind_value_fs).

**N-0445.** §6.2.3.2 Pseudocode for algorithm, unbind_value_fs, step 3 (other values) / p. 43 / L2148-L2154 `[may; pseudocode]`

```text
    else:
      ;; add quoting to any unquoted non-alphanumeric characters,
      ;; but leave the two special characters alone, as they may
      ;; appear quoted or unquoted.
      return add_quoting(s).
  end.
end.
```

Requirement ids: none. Hands a string value to add_quoting, whose rules are R-0233 to R-0236 (`requirements.yaml` `excluded`, unbind_value_fs). Its lowercase "may" expresses possibility (`keyword_accounting`, L2150).

###### Listing: function add_quoting(s)

**N-0446.** §6.2.3.2 Pseudocode for algorithm, add_quoting, step 1 (signature and purpose) / p. 43 / L2156-L2159 `[none: pseudocode]`

```text
function add_quoting(s)
  ;; Inspect each character in string s. Copy quoted characters,
  ;; with their escaping, into the result. Look for unquoted non
  ;; alphanumerics and if not "*" or "?", add escaping.
```

Requirement ids: none. add_quoting's signature and comment; its rules are R-0233 to R-0236, which R-0230 summarises; binds through R-0225.

**N-0447.** §6.2.3.2 Pseudocode for algorithm, add_quoting, step 2 (initialise) / p. 43 / L2160-L2162 `[none: pseudocode]`

```text
  result := "".
  idx := 0.
  embedded := false.
```

Requirement ids: none. Initialises add_quoting; binds through R-0225.

**N-0448.** §6.2.3.2 Pseudocode for algorithm, add_quoting, step 3 (scan loop) / p. 43 / L2163-L2165 `[none: pseudocode]`

```text
  while (idx < strlen(s))
    do
      c := substr(s,idx,idx).  ; get the idx’th character of s.
```

Requirement ids: none. The scan loop of add_quoting; binds through R-0225.

**N-0449.** §6.2.3.2 Pseudocode for algorithm, add_quoting, step 4 (alphanumerics pass) / pp. 43-44 / L2166-L2179 `[none: pseudocode]`

```text
      if (is_alphanum(c) or c = "_") then
        ;; Alphanumeric characters pass untouched.
        result := strcat(result,c).
        idx := idx + 1.
        embedded := true.
        continue.
      endif.
```

Note: See D-14.

Requirement ids: none. Letters, digits and the underscore pass unchanged (the notes of R-0172 and R-0230 say so); binds through R-0225.

**N-0450.** §6.2.3.2 Pseudocode for algorithm, add_quoting, step 5 (quoted characters stay quoted) / p. 44 / L2180-L2187 `[none: pseudocode]`

```text
      if c = "\" then
        ;; Anything quoted in the bound string stays quoted
        ;; in the unbound string.
        result := strcat(result,substr(s,idx,idx+1)).
        idx := idx + 2.
        embedded := true.
        continue.
      endif.
```

Note: See DEF-13.

Requirement ids: nistir-7695#R-0233 (the entry quotes L2180-L2186 of this step).

**N-0451.** §6.2.3.2 Pseudocode for algorithm, add_quoting, step 6 (unquoted `*`) / p. 44 / L2188-L2197 `[must; pseudocode]`

```text
      if (c = "*") then
        ;; An unquoted asterisk must appear at the beginning or
        ;; end of the string.
        if (idx = 0 or idx = (strlen(s)-1)) then
          result := strcat(result,c).
          idx := idx + 1.
          embedded := true.
          continue.
        else error.
      endif.
```

Note: See D-1 and DEF-12.

Requirement ids: nistir-7695#R-0234.

**N-0452.** §6.2.3.2 Pseudocode for algorithm, add_quoting, step 7 (unquoted `?`) / p. 44 / L2198-L2212 `[must, must, must; pseudocode]`

```text
      if (c = "?") then
        ;; An unquoted question mark must appear at the beginning or
        ;; end of the string, or in a leading or trailing sequence.
        if ;; ? legal at beginning or end
           (((idx = 0) or (idx = (strlen(s)-1))) or
            ;; embedded is false, so must be preceded by ?
            (!embedded and (substr(s,idx-1,idx-1) = "?")) or
            ;; embedded is true, so must be followed by ?
            (embedded and (substr(s,idx+1,idx+1) = "?"))) then
          result := strcat(result,c).
          idx := idx + 1.
          embedded := false.
          continue.
        else error.
      endif.
```

Note: See D-10.

Requirement ids: nistir-7695#R-0235.

**N-0453.** §6.2.3.2 Pseudocode for algorithm, add_quoting, step 8 (quote other characters; loop end) / p. 44 / L2213-L2217 `[must; pseudocode]`

```text
      ;; all other characters must be quoted
      result := strcat(result,"\",c).
      idx := idx + 1.
      embedded := true.
  end.
```

Requirement ids: nistir-7695#R-0236 (the entry quotes L2213-L2216 of this step).

**N-0454.** §6.2.3.2 Pseudocode for algorithm, add_quoting, step 9 (return) / p. 44 / L2218-L2219 `[none: pseudocode]`

```text
  return result.
end.
```

Requirement ids: none. Returns the result of add_quoting; binds through R-0225.

The four examples of §6.2.3.3, the contrasting error case and the sentence that introduces them (L2223-L2293) are excluded.

## 7 Bound Name Conversions

**N-0455.** §7 Bound Name Conversions, paragraph 1, sentence 1 / p. 47 / L2305-L2306 `[SHOULD]`

> This section specifies the procedures that SHOULD be followed when converting between the two required bound forms of WFNs.

Note: See D-12 and DEF-18.

Requirement ids: nistir-7695#R-0237.

**N-0456.** §7 Bound Name Conversions, paragraph 1, sentence 3 / p. 47 / L2307-L2309 `[none: declarative]`

> Both conversions are round-trip safe, meaning that taking one of the two bound forms, converting it to the other form, then converting that back to the original binding form, will result in the original binding.

Note: See D-8.

Requirement ids: nistir-7695#R-0238.

### 7.1 Converting a URI to a Formatted String

**N-0457.** §7.1 Converting a URI to a Formatted String, lead-in / p. 47 / L2313-L2314 `[none: lead-in]`

> Given a URI u which conforms to the CPE v2.2 specification, the procedure for converting it to a formatted string fs has two steps:

Requirement ids: none. Lead-in to §7.1, carried verbatim in the `condition` of R-0239.

#### Listing: function convert_uri_to_fs(u)

**N-0458.** §7.1 Converting a URI to a Formatted String, convert_uri_to_fs, step 1 (unbind the URI) / p. 47 / L2316-L2317 `[none: pseudocode]`

```text
function convert_uri_to_fs(u)
  w := unbind_uri(u).
```

Note: `unbind_uri` is defined as `unbind_URI` (DEF-11).

Requirement ids: nistir-7695#R-0239 (one entry for N-0458 to N-0460).

**N-0459.** §7.1 Converting a URI to a Formatted String, convert_uri_to_fs, step 2 (bind to a formatted string) / p. 47 / L2318 `[none: pseudocode]`

```text
  fs := bind_to_fs(w).
```

Requirement ids: nistir-7695#R-0239 (one entry for N-0458 to N-0460).

**N-0460.** §7.1 Converting a URI to a Formatted String, convert_uri_to_fs, step 3 (return) / p. 47 / L2319-L2320 `[none: pseudocode]`

```text
  return fs.
end.
```

Requirement ids: nistir-7695#R-0239 (one entry for N-0458 to N-0460).

### 7.2 Converting a Formatted String to a URI

**N-0461.** §7.2 Converting a Formatted String to a URI, lead-in / p. 47 / L2324-L2325 `[none: lead-in]`

> Given a formatted string fs which conforms to the description in Section 6.2.2, the procedure for converting it to a URI has two steps:

Note: the syntax is in §6.2.1, not §6.2.2 (DEF-10).

Requirement ids: none. Lead-in to §7.2, carried verbatim in the `condition` of R-0240.

#### Listing: function convert_fs_to_uri(fs)

**N-0462.** §7.2 Converting a Formatted String to a URI, convert_fs_to_uri, step 1 (unbind the formatted string) / p. 47 / L2327-L2328 `[none: pseudocode]`

```text
function convert_fs_to_uri(fs)
  w := unbind_fs(fs).
```

Requirement ids: nistir-7695#R-0240 (one entry for N-0462 to N-0464).

**N-0463.** §7.2 Converting a Formatted String to a URI, convert_fs_to_uri, step 2 (bind to a URI) / p. 47 / L2329 `[none: pseudocode]`

```text
  uri := bind_to_uri(w).
```

Note: `bind_to_uri` is defined as `bind_to_URI` (DEF-11).

Requirement ids: nistir-7695#R-0240 (one entry for N-0462 to N-0464).

**N-0464.** §7.2 Converting a Formatted String to a URI, convert_fs_to_uri, step 3 (return) / p. 47 / L2330-L2331 `[none: pseudocode]`

```text
  return uri.
end.
```

Requirement ids: nistir-7695#R-0240 (one entry for N-0462 to N-0464).

## Appendix A: References

**N-0465.** Appendix A References, paragraph 1 / p. 48 / L2343-L2344 `[none: declarative]`

> The following documents are indispensable references for understanding the application of this specification.

Requirement ids: none. Introduces the reference list (`requirements.yaml` `excluded`).

### A.1 Normative References

**N-0466.** A.1 Normative References, the six normative references (one statement) / p. 48 / L2348-L2364 `[none: declarative]`

> ```text
> [CPE22] Buttner, A. and N. Ziring, Common Platform Enumeration (CPE){U+2014}Specification, Version 2.2, March 11, 2009. See http://cpe.mitre.org/specification/archive/version2.2/cpe-specification_2.2.pdf.
> [RFC2119] Bradner, S. (1997). Key words for use in RFCs to Indicate Requirement Levels. March 1997. See http://www.ietf.org/rfc/rfc2119.txt.
> [RFC2234] Crocker, D. and P. Overell. (1997). Augmented BNF for Syntax Specifications: ABNF. Internet RFC 2234, November 1997. See http://www.ietf.org/rfc/rfc2234.txt.
> [RFC3629] Yergeau, F. (2003). UTF-8, a transformation format of ISO 10646. Internet RFC 3629, November 2003. See http://www.ietf.org/rfc/rfc3629.txt.
> [RFC3986] Berners-Lee, T., Fielding, R. and L. Masinger. (2005). Uniform Resource Identifier (URI): Generic Syntax. Internet RFC 3986, January 2005. See http://www.ietf.org/rfc/rfc3986.txt.
> [RFC5646] Phillips, A. and M. Davis. (2009). Tags for Identifying Languages. RFC 5646, September 2009. See http://www.ietf.org/rfc/rfc5646.txt.
> ```

Note: See DEF-20.

Requirement ids: none. The normative reference list; entries such as R-0027 ([RFC3629]), R-0046 ([RFC2234]) and R-0092 ([RFC5646]) cite it, and it constrains nothing itself.

### A.2 Informative References

Not extracted: five informative references (L2368-L2383). See DEF-20.

## Appendix B: Change Log

Not extracted: the change log (PDF p. 49, L2395-L2438) is history. It holds the only uppercase keywords outside the extracted text, a MUST and a SHOULD on L2405 (see the tally).

## Informative content excluded

Everything below was read and judged not to state a rule. Sentences are quoted verbatim so a verifier can check the judgement; examples and whole sections are identified by locator.

### Whole sections and blocks

| Locator | What | Why excluded |
|---|---|---|
| PDF pp. 1-6, L1-L180 | front matter: cover, title page, "Reports on Computer Systems Technology", the disclaimer, Acknowledgments, Abstract, Trademark Information, Table of Contents, List of Figures and Tables | not part of the specification; the Abstract's "must meet" describes the report and the disclaimer's "may" is possibility |
| §1 Introduction / p. 7 / L187-L217 | §1 Introduction, body | background and examples; no verbal form and no rule |
| §1.2 Document Structure / pp. 7-8 / L231-L248 | §1.2 Document Structure | a description of the report's sections |
| §3 Relationship to Existing Specifications and Standards / pp. 11-12 / L385-L448 | §3 (3.1, 3.2, 3.3) | background and history; no verbal form |
| A.2 Informative References / p. 48 / L2368-L2383 | Appendix A.2 Informative References | informative by its own heading |
| Appendix B Change Log / p. 49 / L2395-L2438 | Appendix B Change Log | history of drafts; it records changes, it states no rule |

### Examples

No example in the report is labelled normative, and §5.5 says its examples "are intended only to illustrate". The examples agent turns these into fixtures; the bound names below are verbatim.

| Locator | Example | What it shows |
|---|---|---|
| §1 Introduction / p. 7 / L199-L200 | §1, paragraph 2 | a WFN for Microsoft Internet Explorer 8.0.6001 Beta |
| §1 Introduction / p. 7 / L208 | §1, paragraph 3 | the URI binding of the same WFN |
| §1 Introduction / p. 7 / L214 | §1, paragraph 4 | the formatted string binding of the same WFN |
| §5 Well-Formed CPE Name Data Model / p. 14 / L506-L508 | §5, paragraph 1 | a car described as attribute=value pairs (not a WFN) |
| §5.1 Definitions and Notation / p. 15 / L565-L568 | §5.1, after paragraph 3 | four attribute-value pairs |
| §5.3.1 Logical values / p. 16 / L626-L627 | §5.3.1 | two WFN fragments showing ANY and NA |
| §5.3.2 Restrictions on attribute-value strings / p. 16 / L637-L638 | §5.3.2, paragraph 2 | two WFN fragments showing quoted value strings |
| §5.3.2 Restrictions on attribute-value strings / p. 17 / L699-L712 | §5.3.2, after Figure 5-1 | thirteen allowable value strings with explanations |
| §5.4.1 Function new() / p. 20 / L839-L840 | §5.4.1 | new() returns `wfn:[]` |
| §5.4.2 Function get(w,a) / p. 20 / L847-L851 | §5.4.2 | two calls of get() |
| §5.4.3 Function set(w,a,v) / p. 20 / L860-L866 | §5.4.3 | four calls of set() |
| §5.5 WFN Examples / pp. 20-21 / L870-L900 | §5.5 WFN Examples | five WFNs; the section says "The examples below are intended only to illustrate names that are well formed" |
| §6.1.2.1.2 Handling non-alphanumeric and special characters / pp. 24-25 / L1078-L1089 | §6.1.2.1.2, paragraph 2 | two worked bindings in prose (`\(` to `%28`, `\-` to `-`), quoted under the excluded sentences |
| §6.1.2.4 Examples of binding a WFN to a URI / p. 29 / L1354-L1364 | §6.1.2.4.1 Example 1 | a WFN and its URI `cpe:/a:microsoft:internet_explorer:8.0.6001:beta` |
| §6.1.2.4 Examples of binding a WFN to a URI / p. 30 / L1374-L1385 | §6.1.2.4.2 Example 2 | a WFN and its URI `cpe:/a:microsoft:internet_explorer:8.%02:sp%01` |
| §6.1.2.4 Examples of binding a WFN to a URI / p. 30 / L1387-L1399 | §6.1.2.4.3 Example 3 | a WFN and its URI `cpe:/a:hp:insight_diagnostics:7.4.0.1570:-:~~online~win2003~x64~` |
| §6.1.2.4 Examples of binding a WFN to a URI / p. 30 / L1401-L1412 | §6.1.2.4.4 Example 4 | a WFN and its URI `cpe:/a:hp:openview_network_manager:7.51::~~~linux~~` |
| §6.1.2.4 Examples of binding a WFN to a URI / pp. 30-31 / L1414-L1431 | §6.1.2.4.5 Example 5 | a WFN and its URI `cpe:/a:foo%5cbar:big%24money_manager_2010:::~~special~ipod_touch~80gb~` |
| §6.1.3.3 Examples of unbinding a URI to a WFN / p. 35 / L1697-L1706 | §6.1.3.3.1 Example 1 | `cpe:/a:microsoft:internet_explorer:8.0.6001:beta` unbinds to a WFN |
| §6.1.3.3 Examples of unbinding a URI to a WFN / pp. 35-36 / L1708-L1726 | §6.1.3.3.2 Example 2 | `cpe:/a:microsoft:internet_explorer:8.%2a:sp%3f` unbinds to a WFN |
| §6.1.3.3 Examples of unbinding a URI to a WFN / p. 36 / L1728-L1736 | §6.1.3.3.3 Example 3 | `cpe:/a:microsoft:internet_explorer:8.%02:sp%01` unbinds to a WFN |
| §6.1.3.3 Examples of unbinding a URI to a WFN / p. 36 / L1738-L1749 | §6.1.3.3.4 Example 4 | `cpe:/a:hp:insight_diagnostics:7.4.0.1570::~~online~win2003~x64~` unbinds to a WFN |
| §6.1.3.3 Examples of unbinding a URI to a WFN / p. 36 / L1751-L1762 | §6.1.3.3.5 Example 5 | `cpe:/a:hp:openview_network_manager:7.51:-:~~~linux~~` unbinds to a WFN (DEF-21) |
| §6.1.3.3 Examples of unbinding a URI to a WFN / p. 36 / L1764-L1768 | §6.1.3.3.6 Example 6 | `cpe:/a:foo%5cbar:big%24money_2010%07:::~~special~ipod_touch~80gb~` unbinds to an error (illegal form "%07", D-6) |
| §6.1.3.3 Examples of unbinding a URI to a WFN / p. 37 / L1777-L1787 | §6.1.3.3.7 Example 7 | `cpe:/a:foo~bar:big%7emoney_2010` unbinds to a WFN (D-7) |
| §6.1.3.3 Examples of unbinding a URI to a WFN / p. 37 / L1789-L1794 | §6.1.3.3.8 Example 8 | `cpe:/a:foo:bar:12.%02.1234` unbinds to an error (embedded "%02") |
| §6.2.2.3 Examples of binding a WFN to a formatted string / p. 40 / L1970-L1980 | §6.2.2.3.1 Example 1 | a WFN and its formatted string `cpe:2.3:a:microsoft:internet_explorer:8.0.6001:beta:*:*:*:*:*:*` |
| §6.2.2.3 Examples of binding a WFN to a formatted string / pp. 40-41 / L1982-L2011 | §6.2.2.3.2 Example 2 | a WFN and its formatted string `cpe:2.3:a:microsoft:internet_explorer:8.*:sp?:*:*:*:*:*:*`; also a variant with a quoted asterisk binding to `cpe:2.3:a:microsoft:internet_explorer:8.\*:sp?:*:*:*:*:*:*` |
| §6.2.2.3 Examples of binding a WFN to a formatted string / p. 41 / L2013-L2025 | §6.2.2.3.3 Example 3 | a WFN and its formatted string `cpe:2.3:a:hp:insight:7.4.0.1570:-:*:*:online:win2003:x64:*` |
| §6.2.2.3 Examples of binding a WFN to a formatted string / p. 41 / L2027-L2038 | §6.2.2.3.4 Example 4 | a WFN and its formatted string `cpe:2.3:a:hp:openview_network_manager:7.51:*:*:*:*:linux:*:*` |
| §6.2.2.3 Examples of binding a WFN to a formatted string / p. 41 / L2040-L2051 | §6.2.2.3.5 Example 5 | a WFN and its formatted string `cpe:2.3:a:foo\\bar:big\$money_2010:*:*:*:*:special:ipod_touch:80gb:*` |
| §6.2.3.3 Examples of unbinding a formatted string to a WFN / pp. 44-45 / L2226-L2242 | §6.2.3.3.1 Example 1 | `cpe:2.3:a:microsoft:internet_explorer:8.0.6001:beta:*:*:*:*:*:*` unbinds to a WFN |
| §6.2.3.3 Examples of unbinding a formatted string to a WFN / p. 45 / L2244-L2253 | §6.2.3.3.2 Example 2 | `cpe:2.3:a:microsoft:internet_explorer:8.*:sp?:*:*:*:*:*:*` unbinds to a WFN |
| §6.2.3.3 Examples of unbinding a formatted string to a WFN / p. 45 / L2255-L2267 | §6.2.3.3.3 Example 3 | a WFN; the formatted string is printed across L2257-L2258 (DEF-21) |
| §6.2.3.3 Examples of unbinding a formatted string to a WFN / p. 45 / L2269-L2273 | §6.2.3.3.3, contrasting case | `cpe:2.3:a:hp:insight_diagnostics:7.4.*.1570:*:*:*:*:*:*` unbinds to an error (embedded asterisk; ten fields, D-11) |
| §6.2.3.3 Examples of unbinding a formatted string to a WFN / p. 46 / L2283-L2293 | §6.2.3.3.4 Example 4 | `cpe:2.3:a:foo\\bar:big\$money:2010:*:*:*:special:ipod_touch:80gb:*` unbinds to a WFN |

### Sentences inside normative sections not extracted

Each states a purpose, a history, a pointer to another section, or an example in prose, without constraining anything. The §1.1 scope sentences (S1 to S4) are assessed under §1.1 above and are not repeated here.

**§1.3 Document Conventions / p. 8 / L256-L257.** Typographic convention.

> Text intended to represent computing system input, output, or algorithmic processing is presented in fixed-width Courier font.

**§1.3 Document Conventions / p. 8 / L259.** Pointer to Appendix A.

> Normative references are listed in Appendix A.

**§1.3 Document Conventions / p. 8 / L259-L260.** Citation style; its two bullets (L261-L267) describe how [CPE22:7] and (cf. 5.3.1) are written.

> The following reference citation conventions are used in the text of this document:

**§1.3 Document Conventions / p. 8 / L270-L271.** Statement of intent.

> Pseudocode is intended to be straightforwardly readable and translatable into actual programming language statements.

**§2 Definitions and Abbreviations / p. 9 / L296-L299.** Section introduction and citation convention (four sentences, L296-L299).

> This section defines a set of common terms used within the document. Many terms have been imported from Section 4 of [ISO19770-2]. These are indicated by appending the particular subsection citation to the overall reference citation separated by a colon, e.g., [ISO19770-2:4.1.1]. This section also defines selected abbreviations, including acronyms, used within the document.

**§4 Conformance / p. 13 / L460.** Motivation; "may" expresses possibility.

> Products may want to claim conformance with this specification for a variety of reasons.

**§4 Conformance / p. 13 / L462-L465.** Rationale.

> These requirements are intended to guarantee that a conformant implementation not only can produce and/or consume the newly-introduced formatted string binding form as needed to interoperate with other implementations, but also can process legacy product identifiers as well.

**§4 Conformance / p. 13 / L490-L491.** States a possible benefit; "may" expresses possibility.

> This functionality may enable an implementation to interoperate to a limited extent with implementations conforming to [CPE22] and possibly prior releases as well.

**§5 Well-Formed CPE Name Data Model / p. 14 / L503.** Section introduction.

> This section defines the foundational logical construct of CPE{U+2014}the well-formed CPE name (WFN).

**§5 Well-Formed CPE Name Data Model / p. 14 / L504-L506.** Background.

> Describing an entity involves enumerating a set of attributes and their values to distinguish that entity from other entities in a domain.

**§5 Well-Formed CPE Name Data Model / p. 14 / L506-L507.** Example.

> For example, Joe might describe his car as a “2004 Subaru Outback with a black leather interior”.

**§5 Well-Formed CPE Name Data Model / p. 14 / L507.** Example (its attribute=value list is on L508).

> Conceptually, this description could be modeled as a set of attribute=value pairs:

**§5 Well-Formed CPE Name Data Model / p. 14 / L510-L511.** Background definition; "ambiguous" is not used by any rule.

> A description is said to be ambiguous for a domain when it cannot be used to distinguish a unique entity possessing all specified attributes and values.

**§5 Well-Formed CPE Name Data Model / p. 14 / L511-L514.** Example.

> The above description is ambiguous for a broad domain, such as all automobiles registered in the state of Massachusetts, but might not be ambiguous for a narrower domain, such as all automobiles registered in a particular nine-digit United States postal code region.

**§5 Well-Formed CPE Name Data Model / p. 14 / L516-L517.** Example.

> An example of a product class is a Lenovo ThinkPad X61; this class could be used to identify a hardware device’s class.

**§5 Well-Formed CPE Name Data Model / p. 14 / L517-L519.** Example.

> More general product classes, such as Lenovo Thinkpads or Lenovo laptops, could be used as class descriptions, not class identifiers.

**§5.1 Definitions and Notation / p. 14 / L548-L549.** Pointer to Section 6.

> Section 6 describes procedures for binding WFNs to machine-readable representations for interchange and processing.

**§5.1 Definitions and Notation / p. 15 / L564.** Lead-in to four examples (L565-L568).

> The following are examples of attribute-value pairs:

**§5.3.3 Per-attribute value restrictions / p. 17 / L716-L717.** Section introduction; the lowercase "should" describes the subsections.

> This section specifies value restrictions on each WFN attribute and provides recommendations for how suitable value strings should be chosen.

**§5.4 Operations on WFNs / p. 19 / L824-L825.** Pointer to Section 6.

> These functions are used in defining binding and unbinding procedures in Section 6.

**§6 Name Binding and Unbinding / p. 22 / L912-L913.** Section introduction.

> This section defines the procedures for binding (cf. 2.1) and unbinding (cf. 2.1) WFNs to and from machine-readable representations.

**§6 Name Binding and Unbinding / p. 22 / L913-L914.** Pointer.

> Section 6.1 addresses URI binding/unbinding, and Section 6.2 covers formatted string binding/unbinding.

**§6.1 URI Binding / p. 22 / L922.** Rationale.

> The URI Binding is included in this specification for backward compatibility with prior CPE versions.

**§6.1 URI Binding / p. 22 / L925-L927.** Pointers to §6.1.1 to §6.1.3 (three sentences).

> Section 6.1.1 defines the syntax of a valid URI binding. Section 6.1.2 specifies the procedure for binding a WFN to a URI. Section 6.1.3 specifies the procedure for unbinding a URI into a WFN.

**§6.1.1 URI Binding Syntax / p. 23 / L970-L971.** Commentary on Figure 6-1 and CPE 2.2 practice.

> This syntax specification is less restrictive than suggested by other text in [CPE22] as well as current CPE operational practice.

**§6.1.1 URI Binding Syntax / p. 23 / L973-L974.** Commentary on CPE 2.2 practice.

> In practice, CPE names appearing in the v2.2 Official CPE Dictionary apply percent-encoding only to a limited set of printable non-alphanumeric characters.

**§6.1.2 Binding a WFN to a URI / p. 24 / L1042-L1044.** Pointer to §5.4.

> The pseudocode references the defined operations on WFNs (cf. 5.4) as well as a number of helper functions also defined in pseudocode.

**§6.1.2 Binding a WFN to a URI / p. 24 / L1044-L1046.** Pointers to §6.1.2.1 to §6.1.2.4 (four sentences).

> Section 6.1.2.1 provides some important notes on the binding procedure. Section 6.1.2.2 summarizes the algorithm in prose. Section 6.1.2.3 provides the pseudocode for the algorithm. Section 6.1.2.4 provides examples of binding WFNs to URIs.

**§6.1.2.1.2 Handling non-alphanumeric and special characters / p. 24 / L1074.** Pointer to Tables 6-1 and 6-2.

> This behavior is summarized as follows.

**§6.1.2.1.2 Handling non-alphanumeric and special characters / pp. 24-25 / L1078-L1087.** Example.

> ```text
> So, for example, if the substring "\(" (exclusive of double quotes) is encountered within an attribute-value string, it would be bound to the substring "%28".
> ```

**§6.1.2.1.2 Handling non-alphanumeric and special characters / p. 25 / L1087-L1089.** Example.

> ```text
> As a second example, if the substring "\-" is encountered within an attribute-value string, it would be bound to the single character "-".
> ```

**§6.1.2.1.3 Packing extended attributes / p. 25 / L1115-L1118.** Statement of purpose.

> The capability to bind WFNs to URIs is provided primarily for use by CPE dictionary creators and maintainers, to allow them to create new CPE names that take full advantage of all features introduced in this specification, while still having a backward-compatible path for creating approximate names that conform to [CPE22].

**§6.1.3 Unbinding a URI to a WFN / p. 31 / L1437-L1438.** Pointer to §5.4.

> The pseudocode references the defined operations on WFNs (cf. 5.4) as well as a number of helper functions also defined in pseudocode.

**§6.1.3 Unbinding a URI to a WFN / p. 31 / L1438-L1440.** Pointers to §6.1.3.1 to §6.1.3.3 (three sentences).

> Section 6.1.3.1 summarizes the algorithm in prose. Section 6.1.3.2 provides the pseudocode for the algorithm. Section 6.1.3.3 provides examples of unbinding URIs to WFNs.

**§6.2 Formatted String Binding / p. 37 / L1798.** History.

> The formatted string binding is new to CPE version 2.3.

**§6.2 Formatted String Binding / p. 37 / L1804-L1805.** Rationale.

> Use of a prefix distinct from the v2.2 URI binding enables tools to inspect a given input string and use a simple syntactic test to determine whether to process the input as a URI or as a formatted string.

**§6.2.2 Binding a WFN to a formatted string / p. 38 / L1875-L1877.** Pointers to §6.2.2.1 to §6.2.2.3 (three sentences).

> Section 6.2.2.1 summarizes the algorithm in prose. Section 6.2.2.2 presents the pseudocode for the algorithm. Section 6.2.2.3 presents examples illustrating the results of binding various WFNs to formatted strings.

**§6.2.3 Unbinding a formatted string to a WFN / p. 42 / L2065-L2066.** Pointer to §5.4.

> The pseudocode references the defined operations on WFNs (cf. 5.4) as well as a number of helper functions also defined in pseudocode.

**§6.2.3 Unbinding a formatted string to a WFN / p. 42 / L2066-L2068.** Pointers to §6.2.3.1 to §6.2.3.3 (three sentences).

> Section 6.2.3.1 summarizes the algorithm in prose. Section 6.2.3.2 provides the pseudocode for the algorithm. Section 6.2.3.3 provides examples of unbinding formatted strings to WFNs.

**§7 Bound Name Conversions / p. 47 / L2306-L2307.** Pointers.

> Section 7.1 specifies the procedure for converting a URI binding to a formatted string binding, and Section 7.2 specifies the inverse conversion.

## Verbal form tally

Counts are taken over the source text after joining wrapped lines (so "MUST" at the end of L654 and "NOT" at the start of L655 count once, as MUST NOT), with the same patterns as `bin/_bcp14.py`: longest match first, uppercase only for BCP 14. "In statements" means the occurrence lies inside the quoted text of a numbered statement; "excluded" means it lies in material listed above.

### BCP 14 keywords (uppercase), by section

`bin/bcp14-count` on `nistir7695.txt` gives 108: SHOULD 33, MAY 29, MUST 18, SHALL 15, OPTIONAL 5, MUST NOT 4, SHALL NOT 2, SHOULD NOT 2. It removes the §1.3 key-words sentence as boilerplate; that sentence, quoted as N-0001, holds ten more uppercase keyword tokens (MUST, MUST NOT, REQUIRED, SHALL, SHALL NOT, SHOULD, SHOULD NOT, RECOMMENDED, MAY, OPTIONAL), which name the keywords and impose nothing. Without that removal the text has 118.

| Section | MUST | MUST NOT | SHALL | SHALL NOT | SHOULD | SHOULD NOT | MAY | OPTIONAL | total | in statements | excluded |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| §4 | 4 |  |  |  | 4 |  |  | 1 | 9 | 9 |  |
| §5.1 |  |  | 1 | 1 |  |  |  |  | 2 | 2 |  |
| §5.2 | 2 |  | 2 |  |  |  | 1 |  | 5 | 5 |  |
| §5.3 |  |  | 1 |  |  |  |  |  | 1 | 1 |  |
| §5.3.1 |  |  |  |  | 2 |  | 1 |  | 3 | 3 |  |
| §5.3.2 | 1 | 4 | 2 | 1 | 2 |  | 8 |  | 18 | 18 |  |
| §5.3.3.1 |  |  | 1 |  |  |  |  |  | 1 | 1 |  |
| §5.3.3.2 |  |  |  |  | 2 |  | 2 |  | 4 | 4 |  |
| §5.3.3.3 |  |  |  |  | 2 |  | 2 |  | 4 | 4 |  |
| §5.3.3.4 |  |  |  |  | 2 | 1 | 1 |  | 4 | 4 |  |
| §5.3.3.5 |  |  |  |  | 2 |  | 2 |  | 4 | 4 |  |
| §5.3.3.6 |  |  |  |  | 3 |  | 2 |  | 5 | 5 |  |
| §5.3.3.7 |  |  |  |  | 2 |  | 2 |  | 4 | 4 |  |
| §5.3.3.8 |  |  |  |  | 2 |  | 2 |  | 4 | 4 |  |
| §5.3.3.9 |  |  | 1 |  | 2 |  | 2 |  | 5 | 5 |  |
| §5.3.3.10 |  |  | 1 |  | 2 |  | 1 |  | 4 | 4 |  |
| §5.3.3.11 |  |  |  |  | 2 | 1 | 2 |  | 5 | 5 |  |
| §6.1.1 | 1 |  |  |  | 1 |  |  |  | 2 | 2 |  |
| §6.1.2 | 1 |  |  |  |  |  |  | 1 | 2 | 2 |  |
| §6.1.2.1 | 1 |  |  |  |  |  |  |  | 1 | 1 |  |
| §6.1.2.1.1 |  |  | 2 |  |  |  |  |  | 2 | 2 |  |
| §6.1.2.1.2 | 2 |  | 2 |  |  |  | 1 |  | 5 | 5 |  |
| §6.1.3 | 1 |  |  |  | 1 |  |  | 1 | 3 | 3 |  |
| §6.2 | 2 |  |  |  |  |  |  |  | 2 | 2 |  |
| §6.2.2 | 1 |  | 1 |  |  |  |  | 1 | 3 | 3 |  |
| §6.2.3 | 1 |  | 1 |  |  |  |  | 1 | 3 | 3 |  |
| §7 |  |  |  |  | 1 |  |  |  | 1 | 1 |  |
| Appendix B | 1 |  |  |  | 1 |  |  |  | 2 | 0 | 2 |
| **all** | **18** | **4** | **15** | **2** | **33** | **2** | **29** | **5** | **108** | **106** | **2** |

The excluded uppercase keywords:

- L2405, MUST: Appendix B Change Log.
- L2405, SHOULD: Appendix B Change Log.

> Relaxed the requirement to consume legacy CPE names from a MUST to a SHOULD, since some applications may have no need to consume legacy content.

Where the included keywords sit, by section (statement, number of keywords):

- §4: N-0025 (1), N-0026 (1), N-0027 (2), N-0028 (3), N-0029 (1), N-0030 (1).
- §5.1: N-0046 (2).
- §5.2: N-0052 (1), N-0053 (1), N-0065 (1), N-0066 (1), N-0067 (1).
- §5.3: N-0069 (1).
- §5.3.1: N-0072 (1), N-0074 (1), N-0076 (1).
- §5.3.2: N-0079 (1), N-0082 (1), N-0083 (1), N-0084 (3), N-0085 (1), N-0086 (1), N-0088 (1), N-0089 (1), N-0091 (1), N-0092 (1), N-0093 (1), N-0094 (1), N-0095 (1), N-0096 (1), N-0097 (1), N-0098 (1).
- §5.3.3.1: N-0118 (1).
- §5.3.3.2: N-0122 (1), N-0123 (2), N-0124 (1).
- §5.3.3.3: N-0125 (1), N-0126 (2), N-0127 (1).
- §5.3.3.4: N-0128 (1), N-0129 (2), N-0130 (1).
- §5.3.3.5: N-0131 (1), N-0132 (2), N-0133 (1).
- §5.3.3.6: N-0134 (1), N-0136 (1), N-0137 (2), N-0138 (1).
- §5.3.3.7: N-0139 (1), N-0140 (2), N-0141 (1).
- §5.3.3.8: N-0142 (1), N-0143 (2), N-0144 (1).
- §5.3.3.9: N-0145 (1), N-0146 (1), N-0147 (2), N-0148 (1).
- §5.3.3.10: N-0149 (2), N-0150 (2).
- §5.3.3.11: N-0151 (1), N-0152 (1), N-0153 (2), N-0154 (1).
- §6.1.1: N-0189 (1), N-0215 (1).
- §6.1.2: N-0223 (1), N-0224 (1).
- §6.1.2.1: N-0225 (1).
- §6.1.2.1.1: N-0230 (1), N-0231 (1).
- §6.1.2.1.2: N-0232 (2), N-0233 (1), N-0236 (1), N-0268 (1).
- §6.1.3: N-0327 (1), N-0328 (1), N-0329 (1).
- §6.2: N-0370 (1), N-0372 (1).
- §6.2.2: N-0403 (1), N-0404 (1), N-0405 (1).
- §6.2.3: N-0426 (1), N-0428 (1), N-0429 (1).
- §7: N-0455 (1).

### Lowercase forms, by section

Lowercase must, shall, should and may are not BCP 14 keywords under RFC 8174, and the report adopts RFC 2119 only (DEF-22). They are counted so that a verifier can recount everything that might carry a requirement. There is no lowercase "shall" and no lowercase "should not" or "must not". `requirements.yaml` also counts the lowercase word "required" (6 occurrences: L646, L752, L767, L1571, L1582, L2306), so its lowercase total is 37, this table's 31 plus those 6.

| Section | must | should | may | may not | in statements | excluded |
|---|---:|---:|---:|---:|---:|---:|
| front matter | 1 |  | 1 |  |  | 2 |
| §1.1 | 1 |  |  |  |  | 1 |
| §1.3 |  | 1 |  |  | 1 |  |
| §2.1 |  |  | 3 | 1 | 4 |  |
| §4 | 1 |  | 2 |  | 1 | 2 |
| §5.3.3 |  | 1 |  |  |  | 1 |
| §6.1.1 |  | 1 |  |  | 1 |  |
| §6.1.2.1.3 |  | 1 | 1 |  | 2 |  |
| §6.1.2.3 | 1 |  |  |  | 1 |  |
| §6.1.3.2 | 2 |  |  |  | 2 |  |
| §6.2 |  |  | 1 |  | 1 |  |
| §6.2.2.3 |  | 1 | 1 |  |  | 2 |
| §6.2.3.1 |  |  | 1 |  | 1 |  |
| §6.2.3.2 | 5 |  | 1 |  | 6 |  |
| Appendix B | 1 | 1 | 1 |  |  | 3 |
| **all** | **12** | **6** | **12** | **1** | **20** | **11** |

Included lowercase forms, by statement:

- §1.3: N-0005 (should).
- §2.1: N-0010 (may), N-0013 (may), N-0014 (may), N-0014 (may not).
- §4: N-0023 (must).
- §6.1.1: N-0188 (should).
- §6.1.2.1.3: N-0274 (should), N-0274 (may).
- §6.1.2.3: N-0318 (must).
- §6.1.3.2: N-0348 (must), N-0348 (must).
- §6.2: N-0371 (may).
- §6.2.3.1: N-0431 (may).
- §6.2.3.2: N-0445 (may), N-0451 (must), N-0452 (must), N-0452 (must), N-0452 (must), N-0453 (must).

Excluded lowercase forms:

- L65, may: front matter.
- L98, must: front matter.
- L223, must: excluded sentence, L222-L224 (assessed as S2 under §1.1 above).
- L460, may: excluded sentence, L460 (motivation; "may" expresses possibility).
- L490, may: excluded sentence, L490-L491 (states a possible benefit; "may" expresses possibility).
- L717, should: excluded sentence, L716-L717 (section introduction; the lowercase "should" describes the subsections).
- L1995, should: example, §6.2.2.3.2 Example 2.
- L2011, may: example, §6.2.2.3.2 Example 2.
- L2405, may: Appendix B Change Log.
- L2411, should: Appendix B Change Log.
- L2436, must: Appendix B Change Log.

### Statements by kind

| Kind | Statements |
|---|---:|
| no verbal form: pseudocode | 100 |
| no verbal form: ABNF rule | 89 |
| uppercase keyword(s) | 88 |
| no verbal form: declarative | 82 |
| no verbal form: table row | 33 |
| no verbal form: list item | 21 |
| no verbal form: definition | 18 |
| no verbal form: procedure step | 12 |
| no verbal form: lead-in | 6 |
| lowercase form(s) only: pseudocode | 6 |
| lowercase form(s) only: declarative | 5 |
| lowercase form(s) only: definition | 3 |
| no verbal form: keyword definition | 1 |
| lowercase form(s) only: lead-in | 1 |
| no verbal form: imperative | 1 |
| **all** | **466** |

466 statements, N-0001 to N-0466.

## Disagreements between prose, ABNF and pseudocode

Recorded, not resolved. Each item quotes the parts that disagree and names the statements involved. Where an item says "traced", the extractor ran a literal transcription of the printed pseudocode on the input shown; the trace is an extractor reading **(inferred)**, not source text, and the examples agent can turn each trace into a fixture.

### D-1. A lone or repeated asterisk

The prose forbids both (N-0093, N-0094):

> A single asterisk MUST NOT be used by itself as an attribute value.

> The asterisk MUST NOT be used more than once in sequence.

Figure 5-1 accepts both (N-0100, N-0101): `*` is a `spec_chrs` with no `body2`, and `**` adds the optional trailing `spec_chrs`. The same derivation accepts `*?` and `?*`, values with no other content.

```text
avstring      = ( body / ( spec_chrs *body2 )) *1spec_chrs
spec_chrs     = 1*spec1 / spec2
```

So do the unbinding procedures, whose results are binding (D-12): decode() takes "%02" at index 0 or as the last three characters (N-0349), so `%02` decodes to `*` and `%02%02` to `**`; add_quoting() takes `*` at the first or last index (N-0451), so a formatted-string field `**` unbinds to `**` (a field `*` alone is ANY). Traced. Figures 6-2 and 6-3 reject both, because each requires at least one character that is not special (N-0201, N-0387):

```text
str_w_special     = *1spec_chrs 1*( unreserved / pct-encoded ) *1spec_chrs
```

```text
avstring        = *1spec_chrs 1*( unreserved / quoted ) *1spec_chrs / logical
```

### D-2. A value made only of question marks

The prose allows a lone question mark and runs of them (N-0095):

> A single question mark MAY be used by itself as an attribute value.

although the sentence before it allows special characters only around other content:

> A special character MAY be included at the beginning of an otherwise non-empty value string, and/or at the end of the string.

Figure 5-1 accepts "?" and "??". The binding procedures pass them on: transform_for_uri binds "?" to "%01" (N-0300) and process_quoted_chars copies an unquoted "?" (N-0420). Traced, a WFN whose version is "?" (part "a", vendor "v", product "p") binds to `cpe:/a:v:p:%01` and to `cpe:2.3:a:v:p:?:*:*:*:*:*:*:*`. Neither result obeys its own grammar: Figure 6-2 needs at least one `unreserved / pct-encoded` character in a string ("%01" is `spec1`, not `pct-encoded`) and Figure 6-3 at least one `unreserved / quoted` character (both rules are quoted under D-1). This contradicts N-0217 ("designed to produce URIs that obey the syntax shown in Figure 6-2") and N-0325, and leaves a producer unable to meet N-0026 ("syntactically correct formatted string bindings") for such a WFN. decode() and add_quoting() accept both strings.

### D-3. NA for part or language in a URI

N-0231 binds NA to a hyphen, and bind_value_for_URI does so for every attribute:

> The logical value NA SHALL bind to a single hyphen.

Figures 6-1 and 6-2 give part and lang no hyphen (N-0173, N-0179, N-0192, N-0198):

```text
part              = "h" / "o" / "a" / empty
```

```text
lang              = LANGTAG / empty
```

Figure 6-2 has the same two rules. Traced, a WFN with part NA binds to `cpe:/-:v`, and one with language NA to `cpe:/a:v:p::::-`; neither obeys Figure 6-1 or Figure 6-2. That contradicts N-0168, N-0217 and N-0325, and it puts a producer between two MUSTs: N-0027 requires URIs that adhere to Figure 6-1, while N-0224 requires the result of the pseudocode. Figure 6-3 has no such gap:

```text
part            = "h" / "o" / "a" / logical
```

```text
lang            = LANGTAG / logical
```

### D-4. The values of part

N-0118 allows three string values:

> The part attribute SHALL have one of these three string values:

Everywhere else part may carry a logical value: an unspecified attribute defaults to ANY (§5.2, criterion 2), any attribute MAY be assigned ANY or NA (§5.3.1), Figures 6-1 and 6-2 allow an empty part (ANY) and Figure 6-3 a logical one, and both unbinding procedures yield ANY or NA for part. Note **(inferred)**: §5.3.3.1 restricts the string values of part only.

### D-5. Language tags

N-0149 requires RFC 5646 tags:

> Values for this attribute SHALL be valid language tags as defined by [RFC5646], and SHOULD be used to define the language supported in the user interface of the product being described.

Figure 6-1 defers to RFC 5646 entirely (N-0187), but Figures 6-2 and 6-3 accept only a two- or three-letter language subtag and an optional region:

```text
LANGTAG           = language ["-" region] ; cf. [RFC5646]
language          = 2*3ALPHA              ; shortest ISO 639 code
region            = 2ALPHA / 3DIGIT       ; ISO 3166-1 code or UN M.49 code
```

So valid RFC 5646 tags with a five- to eight-letter language subtag, an extended language subtag, or script, variant, extension or private-use subtags (for example "zh-Hant-TW") cannot appear in a preferred URI or a formatted string. The quoting rule adds a second tension: N-0097 requires the hyphen to be quoted inside a WFN value string, so the WFN value for "en-us" is `en\-us`, which is not itself an RFC 5646 tag; decode() and add_quoting() produce that quoted form. Note **(inferred)**: the tag is meant in its bound form.

### D-6. Percent-encoded forms accepted when unbinding a URI

§6.1.1 obliges every URI consumer to accept all of Figure 6-1 (N-0189) and says unbind_URI is designed to accept both figures (N-0218):

> To ensure full backward compatibility with [CPE22], any implementation that consumes URIs and claims to be conformant with this Naming specification MUST accept as valid input any URI that obeys the full syntax shown in Figure 6-1.

Figure 6-1 admits any two hex digits after "%" (N-0183):

```text
pct-encoded       = "%" HEXDIG HEXDIG
```

decode() accepts only "%01", "%02" and the 29 forms of its case list, and fails on anything else (N-0351):

```text
        else: error.  ; any other form is an error
```

The report intends the error:

> The algorithm performs some limited error checking and handling: (1) if an illegal percent-encoded form is encountered, an error is raised; (2) if unquoted special characters are used in a way that violates the legal syntax, an error is raised.

> An error is raised when this URI is unbound, because it contains an illegal percent-encoded form, "%07".

and N-0329 makes the pseudocode's result the conformant one. For a URI that uses "%07", "%20", "%2d", "%2e", "%41" or any other form outside the list, both MUSTs cannot hold. A smaller point: §6.1.1 says Figure 6-1 allows "any character in the range %01-ff" (N-0188), but `"%" HEXDIG HEXDIG` also admits "%00"; and §6.1.2.4.2 calls "%01" and "%02" "otherwise prohibited percent-encoded forms", which Figure 6-1 does not prohibit.

### D-7. The unencoded tilde

Figure 6-1's unreserved rule ends in U+02DC SMALL TILDE, not "~" (DEF-3, N-0182), so read literally it admits no unencoded tilde. Figure 6-2 leaves the tilde out of unreserved (N-0205); there "~" is only the packing delimiter. Yet decode() accepts an unencoded "~" and quotes it (N-0345), and §6.1.3.3.7 Example 7 unbinds `cpe:/a:foo~bar:big%7emoney_2010`, saying:

> The original v2.2 URI syntax allows tildes to appear without encoding, but the preferred URI syntax is for tildes to be encoded like any other printable non-alphanumeric character.

The pseudocode and the example follow "~", the printed figure does not. And a v2.2 URI whose edition component begins with an unencoded tilde without being packed (legal if Figure 6-1 is read with "~") is sent to unpack() by unbind_URI (N-0337); there strchr() returns nil and the arithmetic on it is undefined (traced; DEF-17).

### D-8. The round-trip claim

§7 claims (N-0456):

> Both conversions are round-trip safe, meaning that taking one of the two bound forms, converting it to the other form, then converting that back to the original binding form, will result in the original binding.

Traced, four kinds of input do not come back unchanged:

- formatted string to URI to formatted string: decode() lowercases each URI component (N-0343), while process_quoted_chars and add_quoting keep case, so `cpe:2.3:a:Microsoft:IE:8.0:*:*:*:*:*:*:*` comes back as `cpe:2.3:a:microsoft:ie:8.0:*:*:*:*:*:*:*`;
- URI to formatted string to URI: an unencoded tilde comes back encoded (`cpe:/a:foo~bar:baz` becomes `cpe:/a:foo%7ebar:baz`);
- URI to formatted string to URI: a packed edition whose four extended values are blank (`cpe:/a:vendor:product:1.0:sp1:~ed~~~~`) comes back unpacked (`cpe:/a:vendor:product:1.0:sp1:ed`), because pack() packs only when one of them is not blank;
- URI to formatted string to URI: an uppercase percent-encoding (`%2A`) comes back lowercase (`%2a`).

### D-9. process_quoted_chars drops or repeats characters

§6.2 says the period, hyphen and underscore appear unquoted in a formatted string (N-0368), and §6.2.2.3.1 Example 1 binds version `8\.0\.6001` to `cpe:2.3:a:microsoft:internet_explorer:8.0.6001:beta:*:*:*:*:*:*`. The case arm for those characters (N-0422) reads:

```text
            ".":
            "-":
            "_": result := strcat(result,nextchr).
                 idx = idx + 2.
```

It has `=` where every other assignment has `:=`, and no `continue.`, so control falls through to the `idx := idx + 1.` after the endif (N-0423 has the `continue.` this arm lacks). If `idx = idx + 2.` assigns, the index moves three places and the character after each quoted one is lost: traced, `8\.0\.6001` binds to `8..001`. If it compares, the index moves one place and the escaped character is copied a second time: `8..0..6001`. Either way the result differs from Example 1, and N-0405 makes "the same result as the suggested pseudocode" the conformance test. Note **(inferred)**: the intended arm is `idx := idx + 2.` followed by `continue.`; with that change the transcription reproduces all five examples of §6.2.2.3.

### D-10. An embedded run of question marks in a formatted string

§5.3.2 forbids embedding a special character (N-0092) and Figure 5-1 rejects "a??b":

> A special character MUST NOT be embedded within a value string.

decode() rejects the URI form "a%01%01b", because its flag `embedded` stays true after a "%01" (N-0348). add_quoting() resets the flag to false after every unquoted "?" (N-0452), so at the second "?" of "a??b" the test `(!embedded and (substr(s,idx-1,idx-1) = "?"))` succeeds and the field unbinds to "a??b" without error (traced). §6.2.3.1 claims more than the pseudocode does (N-0436):

> The unbinding procedure performs limited error checking, only ensuring that unquoted special characters adhere to syntax requirements specified in Figure 5-1.

and N-0429 makes the pseudocode's acceptance the conformant result.

### D-11. Eleven fields

§6.2 requires all eleven attribute values (N-0372), and Figure 6-3 requires eleven fields. unbind_fs() reads fields 2 to 12 with get_comp_fs() (N-0439) and never checks the count, and get_comp_fs() (N-0442) does not say what it returns for a missing field. The contrasting case of §6.2.3.3.3 has ten fields after the prefix:

```text
FS: cpe:2.3:a:hp:insight_diagnostics:7.4.*.1570:*:*:*:*:*:*
```

yet the only reason the report gives for its error is the asterisk:

> This raises an error during unbinding, due to the embedded unquoted asterisk in the version attribute.

### D-12. The status of the procedures

Two sections say the procedure "SHALL be followed" (N-0403, N-0426) and §7 that the conversions "SHOULD be followed" (N-0455), while §6.1.2, §6.1.3, §6.2.2 and §6.2.3 each make following the pseudocode OPTIONAL and require only the same result, for example:

> This section specifies the procedure that SHALL be followed when binding a WFN to a formatted string.

> It is OPTIONAL for implementations of formatted string binding to follow the pseudocode, processes, and other non-normative information provided in this section.

> However, the result of an implementation performing a formatted string binding MUST produce the same result as the suggested pseudocode, processes, etc. would produce.

The pseudocode is called "non-normative information" in the same breath as its results are made mandatory. The change log (Appendix B, Release 4, excluded) states the intent:

> Explained that binding and unbinding implementations must achieve the same results as the provided pseudocode, processes, etc., but do not have to implement the pseudocode, processes, etc.

Note **(inferred)**: the obligation is on input and output; "the procedure" in the SHALL sentences means its behaviour, not its steps.

### D-13. Prose summaries against the pseudocode

- §6.1.2.2 step 4a converts logical values "For all attributes other than (legacy) “edition”" (N-0280), but bind_to_URI applies bind_value_for_URI, logical values included, to the edition and to the four extended attributes before packing (N-0288).
- §6.1.3.1 step 2 (N-0332) lists what decoding entails ("adding quoting to embedded periods and hyphens") but leaves out two things decode() does: it quotes an unencoded "~" as well (N-0345), and it lowercases the component first (N-0343).
- §6.2.2.1 (N-0407) mentions only the conversion of logical values; process_quoted_chars also removes the escape from `.`, `-` and `_` (N-0422).
- The step numbers inside the two summaries are wrong (DEF-7, DEF-8).

### D-14. What counts as alphanumeric

§5.3.2 item 2 lets the underscore stand unquoted (N-0084), and Figure 5-1 never quotes it: it is in `unreserved` (N-0107) and absent from `punc-no-dash`. Read literally, item 5 requires quoting it, since the underscore is a printable non-alphanumeric character:

> All other printable non-alphanumeric characters (i.e., all punctuation marks, brackets, delimiters and other special purpose symbols, except for the special characters defined above) MUST be quoted when embedded in value strings.

and §6.1.2.1.2 (N-0232) says "non-alphanumeric characters generally MUST be quoted". The pseudocode counts the underscore as alphanumeric (N-0320):

```text
  ;; Returns TRUE iff c is an uppercase letter, a lowercase letter,
  ;; a digit, or the underscore, otherwise FALSE.
```

and add_quoting() then tests for it a second time, redundantly (N-0449):

```text
      if (is_alphanum(c) or c = "_") then
```

§5.1 likewise calls an attribute "an alphanumeric label" (N-0045) although sw_edition, target_sw and target_hw contain the underscore. Note **(inferred)**: read "All other" in item 5 as "other than the characters of items 1 to 4" (letters, digits, underscore, backslash, asterisk, question mark); a literal backslash is then governed by item 3 and Figure 5-1, which writes it quoted (`"\\"`).

## Other source defects

Errors and gaps that are not disagreements between the three forms. Numbered DEF-n.

**DEF-1. Wrong cross-reference in §5.3.** Item 2 points to "Section 5.5.3" (N-0071). There is no Section 5.5.3; §5.5 is "WFN Examples" and the per-attribute value restrictions are §5.3.3.

**DEF-2. "Printable" characters between x00 and x7F.** N-0079 allows "printable" UTF-8 characters "with hexadecimal values between x00 and x7F", a range that includes the control characters x00 to x1F and x7F and the space x20. Item 2 forbids whitespace and Figure 5-1 admits only x21 to x7E, so the paragraph overstates the range.

**DEF-3. SMALL TILDE in Figure 6-1.** The last alternative of the unreserved rule (N-0182) is U+02DC SMALL TILDE in the PDF's text layer (the figure's font is WinAnsi-encoded Courier New, in which that character is code 0x98), and the page image shows a raised small tilde. RFC 3986, which §2.1 names as the URI syntax, has "~" (U+007E) there, and §6.1.3.3.7 says the v2.2 syntax allows unencoded tildes (D-7). Figure 6-2's packed rule (N-0203) uses U+007E. Quoted as printed:

```text
unreserved        = ALPHA / DIGIT / "-" / "." / "_" / "˜"
```

**DEF-4. A prose pointer as an ABNF rule.** `LANGTAG = cf. [RFC5646]` (N-0187) has no ABNF elements; an ABNF tool cannot load Figure 6-1 as printed.

**DEF-5. Invalid continuation lines in Figure 6-2.** The pct-encoded rule (N-0209) continues on four lines that begin with "=":

```text
pct-encoded       = "%21" / "%22" / "%23" / "%24" / "%25" / "%26" / "%27" /
                  = "%28" / "%29" / "%2a" / "%2b" / "%2c" / "%2f" / "%3a" /
                  = "%3b" / "%3c" / "%3d" / "%3e" / "%3f" / "%40" / "%5b" /
                  = "%5c" / "%5d" / "%5e" / "%60" / "%7b" / "%7c" / "%7d" /
                  = "%7e"
```

RFC 2234 continues a rule by indentation alone, so each leading "=" is a syntax error. Read each one as "/".

**DEF-6. ALPHA comment in Figure 6-3.** The comment says "; a-z" for a rule that also covers A-Z (N-0397); Figure 5-1's identical rule says "; A-Z or a-z" (N-0116).

```text
ALPHA           = %x41-5a / %x61-7A   ; a-z
```

**DEF-7. Loop range in the URI binding summary.** Step 2 says "perform steps 3 through 7" (N-0277), but step 6 ends the loop and step 7 returns the result.

**DEF-8. Step range in the URI unbinding summary.** Step 1 says "performing steps 2 through 7" (N-0331); the summary has three steps.

**DEF-9. "forward slash" in get_comp_fs.** The comment (N-0442) contradicts its own example:

```text
  ;; Return the i’th field of the formatted string.  If i=0,
  ;; return the string to the left of the first forward slash.
```

```text
  ;; get_comp_fs(fs,0) = "cpe"
```

A formatted string has no forward slash; "cpe" is the text before the first colon.

**DEF-10. Wrong section in §7.2.** The procedure takes "a formatted string fs which conforms to the description in Section 6.2.2" (N-0461); the syntax is in §6.2.1 (Figure 6-3), and §6.2.2 is the binding procedure.

**DEF-11. Function names change case.** §7.1 calls `unbind_uri(u)` (N-0458) and §7.2 calls `bind_to_uri(w)` (N-0463); the functions are defined as `unbind_URI` and `bind_to_URI`. The report does not say whether pseudocode names are case-insensitive.

**DEF-12. Pseudocode syntax is not uniform.** `function unpack(s,wfn).` ends its signature with a full stop (N-0354); unpack uses `end` as a variable (`end := strchr(s,'~',start).`) while `end.` closes blocks; unbind_fs loops with `for a = 2 to 12` (N-0438) where unbind_URI has `for i := 1 to 7`; process_quoted_chars assigns once with `=` (D-9); and if-blocks close with `endif.` in most functions, with `end.` in pack, unbind_URI and unpack, not at all in trim (N-0314), while in add_quoting one `endif.` closes both the outer and the inner `if` of steps 6 and 7 (N-0451, N-0452).

**DEF-13. Two conventions for a backslash in a string literal.** decode() declares `;; pseudocode below uses \ within quotes as escape char` and writes one backslash as `"\\"` (for example `result := strcat(result,"\\",c).`); transform_for_uri (`if (thischar = "\")`), process_quoted_chars (`if c != "\"`, `result := strcat(result,"\",nextchr).`) and add_quoting (`if c = "\" then`, `result := strcat(result,"\",c).`) write one backslash as `"\"` (N-0299, N-0423, N-0450). A literal transcription of either convention misreads the other.

**DEF-14. pack() comment against its code.** The header comment (N-0309) says "If all the values are blank, just return a blank.", but the code returns `ed` when only the four extended values are blank, whatever `ed` holds; the inner comment ("just return ed.") is right.

**DEF-15. trim() loop bound.** `for i := 0 to strlen(s1) do` (N-0314) runs one index past the end of `s1`; it works only because substr() returns nil there and the comparison with ":" fails.

**DEF-16. decode() is not just the inverse of pct_encode().** Its comment (N-0341) calls it "the inverse of pct_encode(s)", but pct_encode takes one character, and decode also maps a blank to ANY and a hyphen to NA, quotes ".", "-" and "~", and lowercases its input.

**DEF-17. unpack() on a malformed packed string.** If the string has fewer than five tildes, strchr() returns nil and `end-1` and `end+1` are undefined (N-0355). unbind_URI sends every edition component that begins with "~" to unpack() (N-0337) without checking it against Figure 6-2's packed rule, which requires exactly five tildes (D-7).

**DEF-18. "the two required bound forms".** §7 (N-0455) calls both bindings required, but §4 makes only the formatted string mandatory for every producer and consumer (items 2 and 4(a)); producing URIs is conditional (item 3) and consuming them is a SHOULD (item 4(b)).

**DEF-19. An external authority with no precedence rule.** §6 names an XML schema at http://scap.nist.gov/schema/cpe/2.3/cpe-naming_2.3.xsd as "the authoritative XML binding definition" (N-0166). The report does not reproduce it and does not say which text governs where the schema and this report's ABNF or prose differ.

**DEF-20. References.** [RFC2234] (ABNF) was obsoleted by RFC 4234 in 2005 and RFC 5234 in 2008, before this report; [RFC3986] names "L. Masinger" for L. Masinter; [ISO19770-2] is listed as informative although §2.1 imports eight of its definitions (Application, Component, Computing Device, Configuration Item, Platform, Product, Release, Software); [SP800-117], [SP800-126] and [TUCA] are listed but never cited.

> [RFC3986] Berners-Lee, T., Fielding, R. and L. Masinger. (2005). Uniform Resource Identifier (URI): Generic Syntax. Internet RFC 3986, January 2005. See http://www.ietf.org/rfc/rfc3986.txt.

**DEF-21. Defects in excluded examples.** §6.1.3.3.5 writes the attribute as "target_HW=ANY" (attributes are case-insensitive by §5.1, but every other place uses lowercase); the contrasting formatted string of §6.2.3.3.3 has ten fields (D-11); the formatted string of §6.2.3.3.3 Example 3 is printed across two lines after "7.4.0.1570:-" (L2257-L2258) and must be joined without a space; §6.1.2.4.2 calls "%01" and "%02" "otherwise prohibited percent-encoded forms" although Figure 6-1 admits them (D-6).

**DEF-22. Lowercase verbal forms.** §1.3 adopts the keywords of RFC 2119 only (N-0001). RFC 2119 does not say whether lowercase "must", "should" and "may" carry the defined meanings (RFC 8174 later said they do not), and the report uses lowercase forms in rule-like sentences: "must be met" (N-0023), "may appear without quoting" (§6.2), "should be used with care" (§6.1.2.1.3) and "must" in pseudocode comments (see the tally).
