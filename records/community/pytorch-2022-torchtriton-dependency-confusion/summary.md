---
schema: "library-summary/v1"
id: pytorch-2022-torchtriton-dependency-confusion
record: pytorch-2022-torchtriton-dependency-confusion
type: summary
updated: "2026-11-02"
---

# Compromised PyTorch-nightly dependency chain between December 25th and December 30th, 2022.

|  |  |
|---|---|
| **Type** | article (security notice on the project blog) |
| **Maturity** | _unset_ (an incident notice; no maturity level applies) |
| **Authors** | PyTorch Foundation |
| **Published** | 2022-12-31 (the page also shows a modified date, 2024-11-14) |
| **Identifier** | URL only |
| **Source** | https://pytorch.org/blog/compromised-nightly-dependency/ |
| **Digest** | `sha256:4932f467ece6724163d0a6990f45446db7fbc4d70c561053d931d9ef181f18ee` (the live HTML page on 2026-11-02, 179,800 bytes, including current site navigation) |

## Overview

PyTorch tells users who installed PyTorch-nightly on Linux with pip between 25 and 30
December 2022 to uninstall it and `torchtriton` at once. Someone had uploaded a package named
`torchtriton` to PyPI, the same name as a dependency PyTorch ships on its own nightly index.
Because pip gives PyPI precedence over the extra index, it installed the attacker's package
instead: the post calls this a supply chain attack on dependencies hosted on public indices.
The package carried a malicious `triton` binary, whose SHA-256 the post gives. When run, it
collected system information (nameservers, hostname, user name, working directory,
environment variables) and read `/etc/hosts`, `/etc/passwd`, `$HOME/.gitconfig`, the files
in `$HOME/.ssh` and the first 1,000 files in `$HOME`. It uploaded all of it, files only if
under 99,999 bytes, through encrypted DNS queries to a domain under `h4ck[.]cfd`. The binary ran only when
code imported `triton`, which PyTorch does not do by default, and stable releases were not
affected. The post gives a one-line check for the binary. It lists the response: the
dependency renamed to `pytorch-triton` (pytorch/pytorch#91539), a placeholder `torchtriton`
registered on PyPI, the affected nightlies removed from download.pytorch.org, and a request
to PyPI's security team for ownership of the name and deletion of the malicious version.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | An in-the-wild dependency-confusion attack on an ML framework's dependency, with the payload's behaviour described |
| Cryptography | `none` | Only incidental: the binary used encrypted DNS queries to exfiltrate, and the response was a rename and a placeholder package |
| This project | `adjacent` | The object model has to represent a dependency resolved across two package indexes, a name collision between them, and a payload that runs only on import |

`bears_on: DEC-001a` (the core type system, accepted in ADR-0010).

## Implementations

Searched on 2026-11-02. None applies: this is an incident notice. The fix it describes is in
PyTorch itself (pytorch/pytorch#91539, which renamed the dependency to `pytorch-triton`).

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this document |

## Limits

- **Written the day after discovery.** It gives no count of affected installs, no
  attribution and no timeline of the package's upload.
- **Narrower than "installed".** By the post's own account the binary ran only if code
  imported `triton`; how often that happened is not stated.
- **Only the pip route on Linux** is described; other installation routes are not discussed.
- **A live page.** The digest covers today's HTML, which wraps the 2022 text in current site
  navigation, so it will not match a capture from another day.

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | core | AIT-037 | AIT-037 cites it, and it is the primary source for INC-023: a malicious `torchtriton` on PyPI took precedence over PyTorch's own nightly index. INC-023 says installs "ran a malicious binary", as the post's opening does; the post's detail is that the binary ran only when `triton` was imported |
| Existing AI threat models | none | none | An incident notice; it models nothing. threat-models.md does not list it |
| Weakness enumerations | adjacent | AML.CS0015, AML.T0010.001, AML.T0011.001, LLM03:2025, ML06, CWE-427, CWE-829, NISTAML.05 | ATLAS 2026.09's case study AML.CS0015 (Compromised PyTorch Dependency Chain) cites it as the first of two references; ATLAS dates the announcement 2022-12-30, while the post is dated 2022-12-31. NIST AI 100-2e2025 does not cite it (searched 2026-11-02). The ids are RPT-0014's mapping in sources.md |
| Attack → asset mapping | core | C04, C14, A09, A08, A10 | Traces the path: a public package index (PyPI) shadowing the project's own index, pip's resolution, the installed package (C04: ML libraries and packages), and the Linux host that imports it (C14 in AIT-037's mapping), from which it takes SSH keys and environment variables (A09), `.gitconfig` (A08) and host and home-directory files (A10). The component and asset mapping is ours |
