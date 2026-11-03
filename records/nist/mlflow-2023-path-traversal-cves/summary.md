---
schema: "library-summary/v1"
id: mlflow-2023-path-traversal-cves
record: mlflow-2023-path-traversal-cves
type: summary
updated: "2026-11-02"
---

# MLflow path traversal: CVE-2023-1177 and CVE-2023-6831

|  |  |
|---|---|
| **Type** | dataset (two CVE records) |
| **Maturity** | _unset_ (vulnerability records; no maturity level applies) |
| **Authors** | huntr, the CVE Numbering Authority for both; the CVE-2023-1177 report on huntr is by Dan McInerney |
| **Published** | CVE-2023-1177: 2023-03-24 (fixed in MLflow 2.2.1, released 2023-03-02). CVE-2023-6831: 2023-12-15 (fixed in MLflow 2.9.2) |
| **Identifier** | CVE-2023-1177 (GHSA-xg73-94fp-g449); CVE-2023-6831 (GHSA-554w-xh4j-8w64); NVD: https://nvd.nist.gov/vuln/detail/CVE-2023-1177 |
| **Source** | CVE List V5 records in CVEProject/cvelistV5: `cves/2023/1xxx/CVE-2023-1177.json` at commit 525d93ce211b, and `cves/2023/6xxx/CVE-2023-6831.json` at commit 63f87251f479 |
| **Digest** | `sha256:eb908f62e5f8236320f852ebd4853f742efb0a14c2a79bed349d447f1299deb7` (CVE-2023-1177, 6,068 bytes); CVE-2023-6831: `sha256:878d7ceef1e442b5a9a058063b2373c8a8be8fb0ac2c71b7df73432d218eb8c0` (3,996 bytes) |

## Overview

Both records say only "Path Traversal: '\..\filename' in GitHub repository mlflow/mlflow",
before 2.2.1 and before 2.9.2. The substance is elsewhere. CVE-2023-1177 is the serious one.
Its huntr report, filed on 3 March 2023 for the CVE after private disclosure to the
maintainers, shows that a default `mlflow server` or `mlflow ui`, with no authentication,
lets anyone register a model, create a model version whose source is a local directory (the
example is the server user's `.ssh` folder), and then download any file in it through the
model-version artifact endpoint. A source such as an S3 bucket extends this to the remote
artifact store. The report argues that most deployments use S3, so cloud credentials can be
stolen, and that stolen SSH keys allow takeover. The maintainers' advisory
(GHSA-xg73-94fp-g449) confirms that an actor can download arbitrary files from the host and
from remote locations the server can reach. It limits the impact to `mlflow server` and
`mlflow ui` (not Databricks Managed MLflow or MLflow on Azure Machine Learning), and
recommends restricting who can reach the server and scoping its cloud credentials to MLflow
files. huntr scores it CVSS 3.1 9.3 with CWE-29; NVD scores it 9.8 with CWE-22; CISA's
enrichment records proof-of-concept exploitation, automatable, partial technical impact.
CVE-2023-6831, fixed in December 2023, is a later bypass: MLflow's path check validated a
URL before decoding it, so an encoded path got through (PR #10650). It needs low privileges
and is scored 8.1, for integrity and availability rather than confidentiality.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | An unauthenticated arbitrary file read on a widely deployed MLOps server, whose own credentials are the prize |
| Cryptography | `none` | Only incidental: SSH private keys and cloud credentials are among the files an attacker would read |
| This project | `adjacent` | The object model has to represent an MLOps server reachable without authentication and the credentials it holds for a remote artifact store, so that a file read on one host becomes access to another |

`bears_on: DEC-001a` (the core type system, accepted in ADR-0010).

## Implementations

Searched on 2026-11-02. None applies: these are vulnerability records. The fixes are in
MLflow (Apache-2.0, https://github.com/mlflow/mlflow): its 2.2.1 release notes name PR #7908,
"Disallow local source for model version", as the patch for GHSA-xg73-94fp-g449, and PR
#10650 moved URL decoding ahead of path validation for CVE-2023-6831.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this document |

## Limits

- **The CVE text says almost nothing.** The detail comes from the huntr report, read from
  the Internet Archive's copy of 2023-03-27 because huntr.com was down for maintenance on
  2026-11-02, and from the maintainers' advisory in GitHub's advisory database.
- **The linked patch is not the one the release notes name.** CVE-2023-1177's record and
  the huntr report link commit 7162a50c, from PR #7891, which applies path validation to
  the `/mlflow-artifacts/` endpoints. MLflow 2.2.1's release notes name PR #7908, which
  blocks local model-version sources, the route the report uses.
- **Impact beyond the file read is the reporter's claim.** That most deployments use S3
  rests on a Shodan survey the report does not present, and takeover through SSH keys is
  argued, not shown.
- **No report text for CVE-2023-6831.** The archived huntr page holds no report content; the
  description here comes from the fix and the CVSS vector.
- **The scores differ.** huntr 9.3 against NVD 9.8, and CWE-29 against CWE-22; RPT-0014
  quotes huntr's 9.3.

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | core | AIT-039 | AIT-039 cites S-1086: an MLflow server that is exposed and unpatched lets a network attacker read arbitrary files (CVE-2023-1177, with no authentication) and, through a later encoding bypass, attack integrity and availability (CVE-2023-6831). The huntr report includes a working proof of concept, and CISA records exploitation as proof of concept; no incident in incidents.md cites S-1086. sources.md's detail that the flaw exposes SSH keys and cloud credentials and can lead to takeover is the huntr report's impact statement, not CVE or NVD text |
| Existing AI threat models | none | none | Vulnerability records; they model nothing. threat-models.md does not list them |
| Weakness enumerations | adjacent | CWE-29, CWE-22, AML.T0049, AML.T0055, AML.T0035, LLM03:2025, ML05, ML06 | They are entries in a vulnerability enumeration, classed by CWE: CWE-29 by huntr and CWE-22 by NVD, for both. Neither NIST AI 100-2e2025 nor ATLAS 2026.09 mentions MLflow (searched 2026-11-02). The other ids are RPT-0014's mapping in sources.md |
| Attack → asset mapping | core | C15, C04, C11, A09, A10, A02 | The report traces the route: the MLflow tracking and model-registry server (C15; its registry is C04), a model version pointing at a local directory or a remote artifact store, and what that exposes: SSH private keys and cloud credentials (A09, held under C11), the host and cloud account behind them (A10), and model files in the artifact store (A02). The mapping is ours |
