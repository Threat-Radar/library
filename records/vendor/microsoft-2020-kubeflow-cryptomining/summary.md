---
schema: "library-summary/v1"
id: microsoft-2020-kubeflow-cryptomining
record: microsoft-2020-kubeflow-cryptomining
type: summary
updated: "2026-11-02"
---

# Misconfigured Kubeflow workloads are a security risk

|  |  |
|---|---|
| **Type** | article (vendor research blog post) |
| **Maturity** | _unset_ (a blog post; no maturity level applies) |
| **Authors** | Yossi Weizman (Microsoft; Azure Security Center, now Microsoft Defender for Cloud) |
| **Published** | 2020-06-10, Microsoft Security Blog |
| **Identifier** | URL only |
| **Source** | https://www.microsoft.com/en-us/security/blog/2020/06/10/misconfigured-kubeflow-workloads-are-a-security-risk/ |
| **Digest** | `sha256:fde5a09af6810abcda2c84206a24f092b4de160a8d72f57ee19bc07ea73692b0` (the live HTML page on 2026-11-02, including current site navigation) |

## Overview

Azure Security Center reports a campaign, seen in April 2020 across tens of Kubernetes
clusters, that targeted Kubeflow, the machine-learning toolkit for Kubernetes, to run
cryptocurrency miners: ML nodes are powerful and often have GPUs. The same image from a public
repository, which runs an XMRIG miner, appeared on many clusters, and most of those clusters
ran Kubeflow, which pointed to the ML framework as the way in. The post explains the
weakness. Kubeflow's dashboard sits behind an Istio ingress gateway that is internal by
default, but some users switch that service to a load balancer for convenience, which puts
the dashboard on the Internet and lets anyone perform operations in Kubeflow. Whoever reaches
it can deploy containers, either by starting a Jupyter notebook server with a custom image or by running
code in a notebook whose mounted service account may deploy containers in its namespace. The
campaign is mapped onto Microsoft's threat matrix for Kubernetes, and the post closes with
detection commands and controls: authentication, monitoring public endpoints, restricting
public load balancers and allowing only trusted images.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | A documented in-the-wild attack on an ML platform through a misconfigured, exposed dashboard |
| Cryptography | `none` | No cryptographic content |
| This project | `adjacent` | The object model has to represent a deployment misconfiguration in ML infrastructure (an exposed service with no authentication) as a weakness, and the path from it to container execution in the cluster |

`bears_on: DEC-001a` (the core type system, accepted in ADR-0010).

## Implementations

Searched on 2026-11-02.

| Name | Kind | License | URL |
|---|---|---|---|
| microsoft/Threat-Matrix-for-Kubernetes | the Kubernetes threat matrix the post maps the campaign onto | not detected (GitHub NOASSERTION) | https://github.com/microsoft/Threat-Matrix-for-Kubernetes |
| Microsoft Defender for Cloud | the commercial monitoring product, formerly Azure Security Center, that detected the campaign | commercial | https://learn.microsoft.com/en-us/azure/defender-for-cloud/ |

Kubeflow itself, the affected platform, is open source (Apache-2.0, https://github.com/kubeflow/kubeflow).

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |
| `summary.md` | this document |

## Limits

- **Thin numbers.** Tens of clusters, observed during April; no counts, victims or dates beyond
  that.
- **The access vector is inferred.** It rests on most affected clusters running Kubeflow and on
  the default namespace name "anonymous" appearing widely, not on a reconstructed intrusion.
- **A product post.** It ends by inviting readers to try Azure Security Center.
- **2020 defaults.** The behaviour described is Kubeflow's as of 2020; current defaults were not
  checked here.
- **A live page.** The digest covers today's HTML, which wraps the 2020 text in current site
  navigation, so it will not match a capture from another day.

## RPT-0014 applicability

| Topic of interest | Rating | Linked ids | Why |
|---|---|---|---|
| Published attacks | core | AIT-039 | AIT-039 cites it, and it is the primary source for INC-017: exposed Kubeflow dashboards on tens of clusters were used to deploy XMRIG cryptominers. The Jupyter notebook servers were reached through the exposed dashboard, not exposed separately, as INC-017's wording could suggest |
| Existing AI threat models | none | none | It maps the campaign onto Microsoft's threat matrix for Kubernetes (initial access, execution, persistence, lateral movement, impact), which is not an AI threat model. threat-models.md does not list it |
| Weakness enumerations | none | AML.T0049, AML.T0034, AML.T0008.000, LLM10:2025, CWE-306 | Not an enumeration, and neither NIST AI 100-2e2025 nor ATLAS 2026.09 cites it (searched 2026-11-02). The ids are RPT-0014's mapping in sources.md: Exploit Public-Facing Application, Cost Harvesting, AI Development Workspaces, Unbounded Consumption and Missing Authentication for Critical Function |
| Attack → asset mapping | core | C15, C03 | Traces the path through named components: the Istio ingress service turned into a public load balancer, the Kubeflow dashboard and notebook servers on the ML control plane (C15), and the training cluster's powerful, often GPU-equipped nodes whose compute was stolen (C03; assets A11 and A10). The component mapping is ours |
