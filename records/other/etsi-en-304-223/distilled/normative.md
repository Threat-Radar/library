---
schema: "library-normative/v1"
id: etsi-en-304-223-normative
record: etsi-en-304-223
type: normative
updated: "2026-10-21"
coverage: "Verbatim: modal verbs clause, transposition dates, the Introduction's phase statement and ISO/IEC 22989 NOTE, scope (§1), §2.1, every clause 3.1 term, all of clause 4 incl. Table 4-1, and all 72 clause 5 provisions with every principle heading, 'Primarily applies to' and References line, and the 5.3.1 NOTE. Excludes front-matter notices, IPR and trademark text, the §2.2 reference list (held in record.yaml cites) and the 3.3 abbreviations. Reading aids at the end are ours, not verbatim."
reviewed_by: ""
---

# ETSI EN 304 223 V2.1.1 — normative text

Quoted text under §0–§5 is **verbatim** from the source (`content.sha256` `1ef542ac…d21a`), cut
out of the text by script so it cannot drift: page headers and footers dropped, line breaks
joined with one space, bullet glyphs removed. Each quote ends with its clause and PDF page.
Provision ids resolve in `requirements.yaml` as `etsi-en-304-223#<designator>`. §7 is a
reading aid we wrote and §6 lists what is left out; neither is part of the standard.

The EN has **no normative references** (§2.1), so this text is the whole normative content.

## 0. Status and verbal forms
> In the present document "shall", "shall not", "should", "should not", "may", "need not", "will", "will not", "can" and "cannot" are to be interpreted as described in clause 3.2 of the ETSI Drafting Rules (Verbal forms for the expression of provisions). "must" and "must not" are NOT allowed in ETSI deliverables except when used in direct citation.
>
> — Modal verbs terminology, p. 4

Transposition dates (Foreword, p. 4), as printed:

> Date of adoption of this EN: 8 December 2025 Date of latest announcement of this EN (doa): 31 March 2026 Date of latest publication of new National Standard or endorsement of this EN (dop/e): 30 September 2026 Date of withdrawal of any conflicting National Standard (dow): 30 September 2026

History (p. 16), as printed:

> Version Date Status V1.1.1 April 2025 Publication as ETSI TS 104 223 V2.0.0 September 2025 ENAP process AP 20251207: 2025-09-08 to 2025-12-08 V2.1.1 December 2025 Publication

## 1. Introduction (lifecycle phases)

> The present document separates principles and requirements into five phases. These are secure design, secure development, secure deployment, secure maintenance and secure end of life. Relevant standards and publications are signposted at the start of each principle to highlight links between the various documents and the present document. This is not an exhaustive list.
>
> — Introduction, p. 5

> NOTE: The principles, described in the present document, can also be mapped to the life cycle stages described in ISO/IEC 22989 [i.3] as follows: the secure design and development principles can be applied during the Design and development life cycle stage; the secure deployment principles can be applied during the Deployment stage; secure maintenance to the Operations and monitoring stage; and secure end of life during the Retirement stage.
>
> — Introduction, NOTE, p. 5

> ETSI TS 104 216 [i.4] provides guidance on how to evaluate and validate AI systems in accordance with the provisions of the present document.
>
> — Introduction, p. 5

## 2. Scope and references

> The present document defines baseline security requirements for AI models and systems. The present document includes in its scope systems that incorporate deep neural networks, such as generative AI. For consistency, the term "AI systems" is used throughout the present document when framing the scope of provisions and the term "AI security", which is considered a subset of cybersecurity, is used when addressing any cybersecurity issues in the scope of the provisions. The present document is not designed for academics who are creating and testing AI systems only for research purposes (AI systems which are not going to be deployed).
>
> — §1 Scope, p. 6

> The following referenced documents are necessary for the application of the present document. Not applicable.
>
> — §2.1 Normative references, p. 6

## 3. Terms (§3.1)

> For the purposes of the present document, the following terms apply:

- **adversarial attack** — attempt to manipulate an AI model by introducing specially crafted inputs to cause the model to produce errors or unintended outcomes (p. 7)
- **AI system** — engineered system that generates outputs such as content, forecasts, recommendations or decisions for a given set of human-defined objectives (p. 7)
- **Application Programming Interface (API)** — set of tools and protocols that allow different software systems to communicate and interact (p. 7)
- **data poisoning** — type of adversarial attack where malicious data is introduced into training datasets to compromise the AI system's performance or behaviour (p. 7)
- **guardrails** — predefined constraints or rules implemented to control and limit an AI system's outputs and behaviours, ensuring safety, reliability, and alignment with ethical or operational guidelines (p. 7)
- **inference** — reasoning by which conclusions are derived from known premises NOTE 1: In AI, a premise is either a fact, a rule, a model, a feature or raw data. NOTE 2: The term "inference" refers both to the process and its result. (p. 8)
- **input data** — data for which an AI system calculates a predicted output or inference (p. 8)
- **machine learning algorithm** — algorithm to determine parameters of a machine learning model from data according to given criteria (p. 8)
- **machine learning model** — mathematical construct that generates an inference or prediction based on input data or information (p. 8)
- **model inversion** — privacy attack where an adversary infers sensitive information about the training data by analysing the AI model's outputs (p. 8)
- **model training** — process to determine or to improve the parameters of a machine learning model, based on a machine learning algorithm, by using training data (p. 8)
- **prediction** — primary output of an AI system when provided with input data or information NOTE 1: Predictions can be followed by additional outputs, such as recommendations, decisions and actions. NOTE 2: Prediction does not necessarily refer to predicting something in the future. NOTE 3: Predictions can refer to various kinds of data analysis or production applied to new data or historical data (including translating text, creating synthetic images or diagnosing a previous power failure). (p. 8)
- **prompt** — input provided to an AI model, often in the form of text, that directs or guides its response NOTE: Prompts can include questions, instructions, or context for the desired output. (p. 8)
- **risk assessment** — process of identifying, analysing and mitigating potential threats to the security or functionality of an AI system (p. 8)
- **sanitisation** — process of cleaning and validating data or inputs to remove errors, inconsistencies and malicious content, ensuring data integrity and security (p. 8)
- **system prompt** — predefined input or set of instructions provided to guide the behaviour of an AI model, often used to define its tone, rules, or operational context (p. 8)
- **threat modelling** — process to identify and address potential security threats to a system during its design and development phases (p. 8)
- **training** — process of teaching an AI model to recognize patterns, make decisions, or generate outputs by exposing it to labelled data and adjusting its parameters to minimize errors (p. 8)
- **training data** — data used to train a machine learning model (p. 8)

## 4. Stakeholders (clause 4)

> The present clause defines the stakeholder groups that form the AI supply chain. An indication is given for each principle on which stakeholders are primarily responsible for its implementation. A single entity can hold multiple stakeholder roles, as defined in the present document, in addition to any responsibilities arising from different regulatory regimes.
>
> — §4, p. 9

> EXAMPLE: Under data protection law, when processing personal data, organizations can have a role of controller and/or joint controller and/or processor, depending on their role in creating and setting up AI systems.
>
> — §4, EXAMPLE, p. 9

> All stakeholders included in Table 4-1 should note that they can have data protection obligations. Additionally, senior leaders in an organization also have responsibilities to help protect their staff and infrastructure. Some provisions for Developers in the present document are less applicable to AI systems involving open-source models. Further information and guidance about different types of AI systems can be found in ETSI TR 104 128 [i.1].
>
> — §4 (first sentence = entry C4-1, a recommendation), p. 9

**Table 4-1: Stakeholder definition** (pp. 9–10). Cells verbatim; the row split is ours.

| Stakeholder | Definitions |
|---|---|
| Developers | This encompasses any type of business or organization across any sector as well as individuals that are responsible for creating or adapting an AI model and/or system. This applies to all AI technologies, including proprietary and open-source models. For context, a business or organization that creates an AI model and who is also responsible for embedding/deploying that model/system in their organization are defined in the present document to be both a Developer and a System Operator. Developers can be AI providers under the EU AI Act [i.2], when putting a system into service or placing it on the market. |
| System Operators | This includes any type of business or organization across any sector that has responsibility for embedding/deploying an AI model and system within their infrastructure and/or its ongoing maintenance. This applies to all AI technologies, including proprietary and open-source models. This term also includes those businesses that provide a contractual service to organizations to embed/deploy an AI model and system for business purposes. System operators can be deployers under the EU AI Act [i.2] and can also be AI providers if they make changes to the system. |
| Data Custodians | This includes any type of business, organization or individual that controls data permissions and the integrity of data that is used for any AI model or system to function. This stakeholder group also includes those entities that set the policies for how data is used and managed for an AI model and/or system. In the context of an AI system, there could be multiple data custodians involved because some data used to create a model could come from the organization that is deploying/embedding the system in their infrastructure and other data could be from public databases and other sources. |
| End-users | This encompasses any employee within an organization or business and consumers who use an AI model and system for any purpose, including to support their work and day-to-day activities. This applies to all AI technologies and both proprietary and open-source models. This stakeholder group has been created because the voluntary Code has placed expectations on Developers, System Operators and Data custodians to help inform and protect end-users. |
| Affected entities | Encompasses all individuals and technologies, such as apps and autonomous systems, that are not directly affected by AI systems or decisions based on the output of AI systems. These individuals do not necessarily interact with the deployed system or application. |

## 5. Principles and provisions (clause 5)

Each principle: heading, the 'Primarily applies to' and References lines, then every
provision in order. Principle 10 (§5.3.1) has no 'Primarily applies to' or References line
and Principle 13 (§5.5.1) has no References line; neither is omitted here.

### 5.1 Secure Design

#### 5.1.1 Principle 1: Raise awareness of AI security threats and risks (p. 10)

Primarily applies to: System Operators, Developers, and Data Custodians (p. 10)

References: [i.7], [i.8], [i.9], [i.10], [i.11], [i.12], [i.13], [i.14], [i.15]. (p. 10)

- **5.1.1-1** (p. 10) — Organizations' cyber security training programme shall include AI security content which shall be regularly reviewed and updated, such as if new substantial AI-related security threats emerge.
- **5.1.1-1.1** (p. 10) — AI security training shall be tailored to the specific roles and responsibilities of staff members.
- **5.1.1-2** (p. 10) — As part of an Organization's wider staff training programme, they shall require all staff to maintain awareness of the latest security threats and vulnerabilities that are AI-related. Where available, this awareness shall include proposed mitigations.
- **5.1.1-2.1** (p. 10) — These updates should be communicated through multiple channels, such as security bulletins, newsletters, or internal knowledge-sharing platforms. This will ensure broad dissemination and understanding among the staff.
- **5.1.1-2.2** (p. 10) — Organizations shall provide developers with training in secure coding and system design techniques specific to AI development, with a focus on preventing and mitigating security vulnerabilities in AI algorithms, models, and associated software.

#### 5.1.2 Principle 2: Design the AI system for security as well as functionality and performance (p. 10)

Primarily applies to: System Operators and Developers (p. 10)

References: [i.11], [i.12], [i.10], [i.18], [i.19], [i.20], [i.15], [i.21], [i.22], [i.23], [i.9], [i.24]. (p. 10)

- **5.1.2-1** (p. 10) — As part of deciding whether to create an AI system, a System Operator and/or Developer shall conduct a thorough assessment that includes determining and documenting the business requirements and/or problem they are seeking to address, along with associated AI security risks and mitigation strategies.
- **5.1.2-1.1** (p. 10) — Where the Data Custodian is part of a Developer's organization, they shall be included in internal discussions when determining the requirements and data needs of an AI system.
- **5.1.2-2** (p. 10) — Developers and System Operators shall ensure that AI systems are designed and implemented to withstand adversarial AI attacks, unexpected inputs and AI system failure.
- **5.1.2-3** (p. 10) — To support the process of preparing data, security auditing and incident response for an AI system, Developers shall document and create an audit trail in relation to the AI system. This shall include the operation, and lifecycle management of models, datasets and prompts incorporated into the system.
- **5.1.2-4** (p. 10) — If a Developer or System Operator uses an external component, they shall conduct an AI security risk assessment and due diligence process in line with their existing software development processes, that assesses AI specific risks.
- **5.1.2-5** (p. 11) — Data Custodians shall ensure that the intended usage of the system is appropriate to the sensitivity of the data it was trained on as well as the controls intended to ensure the security of the data.
- **5.1.2-5.1** (p. 11) — Organizations should ensure that employees are encouraged to proactively report and identify any potential security risks in AI systems and ensure appropriate safeguards are in place.
- **5.1.2-6** (p. 11) — Where the AI system will be interacting with other systems or data sources, (be they internal or external), Developers and System Operators shall ensure that the permissions granted to the AI system on other systems are only provided as required for functionality and are risk assessed.
- **5.1.2-7** (p. 11) — If a Developer or System Operator chooses to work with an external provider, they shall undertake a due diligence assessment and should ensure that the provider is adhering to the present document.

#### 5.1.3 Principle 3: Evaluate the threats and manage the risks to the AI system (p. 11)

Primarily applies to: Developers and System Operators (p. 11)

References: [i.5], [i.11], [i.10], [i.25], [i.18], [i.13], [i.21], [i.19], [i.12], [i.17] (p. 11)

- **5.1.3-1** (p. 11) — Developers and System Operators shall analyse threats and manage security risks to their systems. Threat modelling should include regular reviews and updates and address AI-specific attacks, such as data poisoning, model inversion, and membership inference.
- **5.1.3-1.1** (p. 11) — The threat modelling and risk management process shall be conducted to address any security risks that arise when a new setting or configuration option is implemented or updated at any stage of the AI lifecycle.
- **5.1.3-1.2** (p. 11) — Developers shall manage the security risks associated with AI models that provide superfluous functionalities, where increased functionality leads to increased risk. For example, where a multi-modal model is being used but only single modality is used for system function.
- **5.1.3-1.3** (p. 11) — System Operators shall apply controls to risks identified through the analysis based on a range of considerations, including the cost of implementation in line with their corporate risk tolerance.
- **5.1.3-2** (p. 11) — Where AI security threats are identified that cannot be resolved by Developers, this shall be communicated to System Operators so they can threat model their systems. System Operators shall communicate this information to End-users, so they are made aware of these threats. This communication should include detailed descriptions of the risks, potential impacts, and recommended actions to address or monitor these threats.
- **5.1.3-3** (p. 11) — Where an external entity has responsibility for AI security risks identified within an organizations infrastructure, System Operators should attain assurance that these parties are able to address such risks.
- **5.1.3-4** (p. 11) — Developers and System Operators should continuously monitor and review their system infrastructure according to risk appetite. It is important to recognize that a higher level of risk will remain in AI systems despite the application of controls to mitigate against them.

#### 5.1.4 Principle 4: Enable human responsibility for AI systems (p. 11)

Primarily applies to: Developers and System Operators (p. 11)

References: [i.11], [i.12], [i.20] (p. 11)

- **5.1.4-1** (p. 11) — When designing an AI system, Developers and/or System Operators should incorporate and maintain capabilities to enable human oversight.
- **5.1.4-2** (p. 11) — Developers should design systems to make it easy for humans to assess outputs that they are responsible for in said system (such as by ensuring that models outputs are explainable or interpretable).
- **5.1.4-3** (p. 11) — Where human oversight is a risk control, Developers and/or System Operators shall design, develop, verify and maintain technical measures to reduce the risk through such oversight.
- **5.1.4-4** (p. 11) — Developers should verify that the security controls specified by the Data Custodian have been built into the system.
- **5.1.4-5** (p. 12) — Developers and System Operators should make End-users aware of prohibited use cases of the AI system.

### 5.2 Secure Development

#### 5.2.1 Principle 5: Identify, track and protect the assets (p. 12)

Primarily applies to: Developers, System Operators and Data Custodians (p. 12)

References: [i.11], [i.25], [i.19], [i.20], [i.15], [i.16], [i.21], [i.24] (p. 12)

- **5.2.1-1** (p. 12) — Developers, Data Custodians and System Operators shall maintain a comprehensive inventory of their assets (including their interdependencies/connectivity).
- **5.2.1-2** (p. 12) — As part of broader software security practices, Developers, Data Custodians and System Operators shall have processes and tools to track, authenticate, manage version control and secure their assets due to the increased complexities of AI specific assets.
- **5.2.1-3** (p. 12) — System Operators shall develop and tailor their disaster recovery plans to account for specific attacks aimed at AI systems.
- **5.2.1-3.1** (p. 12) — System Operators should ensure that a known good state can be restored.
- **5.2.1-4** (p. 12) — Developers, System Operators, Data Custodians and End-users shall protect sensitive data, such as training or test data, against unauthorized access (see clause 5.2.3 for details on securing data).
- **5.2.1-4.1** (p. 12) — Developers, Data Custodians and System Operators shall apply checks and sanitisation to data and inputs when designing the model based on their access to said data and inputs and where those data and inputs are stored. This shall be repeated when model revisions are made in response to user feedback or continuous learning. See clause 5.2.2 for relevant provisions for open source.
- **5.2.1-4.2** (p. 12) — Where training data or model weights could be confidential, Developers shall put proportionate protections in place.

#### 5.2.2 Principle 6: Secure the infrastructure (p. 12)

Primarily applies to: Developers and System Operators (p. 12)

References: [i.11], [i.12], [i.10], [i.19], [i.24] (p. 12)

- **5.2.2-1** (p. 12) — Developers and System Operators shall evaluate their organization's access control frameworks and identify appropriate measures to secure APIs, models, data, and training and processing pipelines.
- **5.2.2-2** (p. 12) — If a Developer offers an API to external customers or collaborators, they shall apply controls that mitigate attacks on the AI system via the API. For example, placing limits on model access rate to limit an attacker's ability to reverse engineer or overwhelm defences to rapidly poison a model.
- **5.2.2-3** (p. 12) — Developers shall also create dedicated environments for development and model tuning activities. The dedicated environments shall be backed by technical controls to ensure separation and principle of least privilege. In the context of AI, this is particularly necessary because training data shall only be present in the training and development environments where this training data is not based on publicly available data.
- **5.2.2-4** (p. 12) — Developers and System Operators shall implement and publish a clear and accessible vulnerability disclosure policy.
- **5.2.2-5** (p. 12) — Developers and System Operators shall create, test and maintain an AI system incident management plan and an AI system recovery plan.
- **5.2.2-6** (p. 12) — Developers and System Operators should ensure that, where they are using cloud service operators to help to deliver the capability, their contractual agreements support compliance with the above requirements.

#### 5.2.3 Principle 7: Secure the supply chain (p. 13)

Primarily applies to: Developers, System Operators and Data Custodians (p. 13)

References: [i.6], [i.11], [i.19], [i.9] (p. 13)

- **5.2.3-1** (p. 13) — Developers and System Operators shall follow secure software supply chain processes for their AI model and system development.
- **5.2.3-2** (p. 13) — System Operators that choose to use or adapt any models, or components, which are not well-documented or secured shall be able to justify their decision to use such models or components through documentation (for example if there was no other supplier for said component).
- **5.2.3-2.1** (p. 13) — In this case, Developers and System Operators shall have mitigating controls and undertake a risk assessment linked to such models or components.
- **5.2.3-2.2** (p. 13) — System Operators shall share this documentation with End-users in an accessible way.
- **5.2.3-3** (p. 13) — Developers and System Operators shall re-run evaluations on released models that they intend on using.
- **5.2.3-4** (p. 13) — System Operators shall communicate their intention to update models to End-users in an accessible way prior to models being updated.

#### 5.2.4 Principle 8: Document data, models and prompts (p. 13)

Primarily applies to: Developers (p. 13)

References: [i.11], [i.10], [i.19], [i.15], [i.24] (p. 13)

- **5.2.4-1** (p. 13) — Developers shall document and maintain a clear audit trail of their system design and post-deployment maintenance plans. Developers should make the documentation available to the downstream System Operators and Data Custodians.
- **5.2.4-1.1** (p. 13) — Developers should ensure that the document includes security-relevant information, such as the sources of training data (including fine-tuning data and human or other operational feedback), intended scope and limitations, guardrails, retention time, suggested review frequency and potential failure modes.
- **5.2.4-1.2** (p. 13) — Developers shall release cryptographic hashes for model components that are made available to other stakeholders to allow them to verify the authenticity of the components.
- **5.2.4-2** (p. 13) — Where training data has been sourced from publicly available sources, there is a risk that this data might have been poisoned. As discovery of poisoned data is likely to occur after training (if at all), Developers shall document how they obtained the public training data, where it came from and how that data is used in the model.
- **5.2.4-2.1** (p. 13) — The documentation of training data should include at a minimum the source of the data, such as the URL of the scraped page, and the date/time the data was obtained. This will allow Developers to identify whether a reported data poisoning attack was in their data sets.
- **5.2.4-3** (p. 13) — Developers should ensure that they have an audit log of changes to system prompts or other model configuration (including prompts) that affect the underlying working of the systems. Developers can make this available to any System Operators and End-Users that have access to the model.

#### 5.2.5 Principle 9: Conduct appropriate testing and evaluation (p. 13)

Primarily applies to: Developers and System Operators (p. 13)

References: [i.11], [i.10], [i.25], [i.19], [i.18], [i.13], [i.21] (p. 13)

- **5.2.5-1** (p. 13) — Developers shall ensure that all models, applications and systems that are released to System Operators and/or End-users have been tested as part of a security assessment process.
- **5.2.5-2** (p. 13) — System Operators shall conduct testing prior to the system being deployed with support from Developers.
- **5.2.5-2.1** (p. 14) — For security testing, System Operators and Developers should use independent security testers with technical skills relevant to their AI systems.
- **5.2.5-3** (p. 14) — Developers should ensure that the findings from the testing and evaluation are shared with System Operators, to inform their own testing and evaluation.
- **5.2.5-4** (p. 14) — Developers should evaluate model outputs to ensure they do not allow System Operators or End-users to reverse engineer non-public aspects of the model or the training data.
- **5.2.5-4.1** (p. 14) — Additionally, Developers should evaluate model outputs to ensure they do not provide System Operators or End-users with unintended influence over the system.

### 5.3 Secure Deployment

#### 5.3.1 Principle 10: Communication and processes associated with End-users and Affected Entities (p. 14)

NOTE: As part of an organization's wider deployment practices, pre-deployment testing of AI systems is to be considered alongside the requirements below. (p. 14)

- **5.3.1-1** (p. 14) — System Operators shall convey to End-users in an accessible way where and how their data will be used, accessed and stored (for example, if it is used for model retraining, or reviewed by employees or partners). If the Developer is an external entity, they shall provide this information to System Operators.
- **5.3.1-2** (p. 14) — System Operators shall provide End-users with accessible guidance to support their use, management, integration, and configuration of AI systems. If the Developer is an external entity, they shall provide all necessary information to help System Operators.
- **5.3.1-2.1** (p. 14) — System Operators shall include guidance on the appropriate use of the model or system, which includes highlighting limitations and potential failure modes.
- **5.3.1-2.2** (p. 14) — System Operators shall proactively inform End-users of any security relevant updates and provide clear explanations in an accessible way.
- **5.3.1-3** (p. 14) — Developers and System Operators should support End-users and Affected Entities during and following a cyber security incident to contain and mitigate the impacts of an incident. The process for undertaking this should be documented and agreed in contracts with End-users.

### 5.4 Secure Maintenance

#### 5.4.1 Principle 11: Maintain regular security updates, patches and mitigations (p. 14)

Primarily applies to: Developers and System Operators (p. 14)

References: [i.24] (p. 14)

- **5.4.1-1** (p. 14) — Developers shall provide security updates and patches, where possible, and notify System Operators of the security updates. System Operators shall deliver these updates and patches to End-users.
- **5.4.1-1.1** (p. 14) — Developers shall have mechanisms and contingency plans to mitigate security risks, particularly in instances where updates cannot be provided for AI systems.
- **5.4.1-2** (p. 14) — Developers should treat major AI system updates as though a new version of a model has been developed and therefore undertake a new security testing and evaluation process to help protect users.
- **5.4.1-3** (p. 14) — Developers should support System Operators to evaluate and respond to model changes, (for example by providing preview access via beta-testing and versioned APIs).

#### 5.4.2 Principle 12: Monitor the system's behaviour (p. 15)

Primarily applies to: Developers and System Operators (p. 15)

References: [i.11], [i.10], [i.25], [i.18], [i.20], [i.15], [i.16], [i.21], [i.24] (p. 15)

- **5.4.2-1** (p. 15) — System Operators shall log system and user actions to support security compliance, incident investigations, and vulnerability remediation.
- **5.4.2-2** (p. 15) — System Operators should analyse their logs to ensure that AI models continue to produce desired outputs and to detect anomalies, security breaches, or unexpected behaviour over time (such as due to data drift or data poisoning).
- **5.4.2-3** (p. 15) — System Operators and Developers should monitor internal states of their AI systems where this could better enable them to address security threats, or to enable future security analytics.
- **5.4.2-4** (p. 15) — System Operators and Developers should monitor the performance of their models and system over time so that they can detect sudden or gradual changes in behaviour that could affect security.

### 5.5 Secure End of Life

#### 5.5.1 Principle 13: Ensure proper data and model disposal (p. 15)

Primarily applies to: Developers and System Operators (p. 15)

- **5.5.1-1** (p. 15) — If a Developer or System Operator decides to transfer or share ownership of training data and/or a model to another entity they shall involve Data Custodians and securely dispose of these assets. This will protect AI against security issues that can transfer from one AI system instantiation to another.
- **5.5.1-2** (p. 15) — If a Developer or System Operators decides to decommission a model and/or system, they shall involve Data Custodians and securely delete applicable data and configuration details. 

## 6. What is not here, and why

- Front-matter notices, disclaimer, copyright, IPR and trademark text (pp. 2, 4): ETSI boilerplate;
  every modal verb in them is itemised as excluded in `requirements.yaml` `reconciliation`.
- §2.2 informative references [i.1]–[i.25]: held as `cites` in `record.yaml`.
- §3.2 Symbols ("Void.") and §3.3 Abbreviations (AI, API).

## 7. Reading aids (ours, not verbatim)

Written in the first pass (2026-10-01) and checked again in this one; the counts come from
`requirements.yaml`.

| # | clause | principle | phase | primarily applies to | provisions | shall / should |
|---|---|---|---|---|---|---|
| 1 | §5.1.1 | Raise awareness of AI security threats and risks | design | System Operators, Developers, and Data Custodians | 5 | 4 / 1 |
| 2 | §5.1.2 | Design the AI system for security as well as functionality and performance | design | System Operators and Developers | 9 | 8 / 1 |
| 3 | §5.1.3 | Evaluate the threats and manage the risks to the AI system | design | Developers and System Operators | 7 | 5 / 2 |
| 4 | §5.1.4 | Enable human responsibility for AI systems | design | Developers and System Operators | 5 | 1 / 4 |
| 5 | §5.2.1 | Identify, track and protect the assets | development | Developers, System Operators and Data Custodians | 7 | 6 / 1 |
| 6 | §5.2.2 | Secure the infrastructure | development | Developers and System Operators | 6 | 5 / 1 |
| 7 | §5.2.3 | Secure the supply chain | development | Developers, System Operators and Data Custodians | 6 | 6 / 0 |
| 8 | §5.2.4 | Document data, models and prompts | development | Developers | 6 | 3 / 3 |
| 9 | §5.2.5 | Conduct appropriate testing and evaluation | development | Developers and System Operators | 6 | 2 / 4 |
| 10 | §5.3.1 | Communication and processes associated with End-users and Affected Entities | deployment | not stated | 5 | 4 / 1 |
| 11 | §5.4.1 | Maintain regular security updates, patches and mitigations | maintenance | Developers and System Operators | 4 | 2 / 2 |
| 12 | §5.4.2 | Monitor the system's behaviour | maintenance | Developers and System Operators | 4 | 1 / 3 |
| 13 | §5.5.1 | Ensure proper data and model disposal | end-of-life | Developers and System Operators | 2 | 2 / 0 |

"shall / should" counts provisions by their strongest verb (a provision with both counts as
shall). The AI attacks the standard names, with the attack class and ids we map them to, are in
`threats.yaml`; how each provision bears on tmodel is in `design-notes.md`.
