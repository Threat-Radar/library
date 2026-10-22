---
schema: "library-normative/v1"
id: cisa-ai-in-ot-principles-normative
record: cisa-ai-in-ot-principles
type: normative
updated: "2026-10-21"
coverage: "Verbatim: regulatory status (Disclaimer), the three Important Terminology definitions, the Appendix definitions of AI-Enabled OT System and Risks, Table 1 and Table 2 cell by cell, and all 123 normative statements of requirements.yaml in source order under their section headings. Excludes descriptive prose (benefit lists, challenge lists, technique descriptions), Resources, Acknowledgements and References; the challenge lists and Table 2 risks are carried as threats in threats.yaml."
reviewed_by: ""
---

# Principles for the Secure Integration of AI in OT — normative text

Verbatim from the source (`content.sha256` `1fde3cba…1560`, 25 pp.), taken from the gitignored
capture `.cache/cisa-ai-in-ot-principles.capture.txt` (PyMuPDF text blocks; page furniture,
bullet glyphs and footnote markers dropped; line breaks joined — the rules are listed in
`verification.md`). Statement ids resolve in `requirements.yaml` as
`cisa-ai-in-ot-principles#R-NNNN`; each carries its page. Table cells are verbatim; the row
split is ours, read from the PDF's cell layout.

## 0. Status of the guidance

> This document does not create policies, impose requirements, mandate actions, or override existing legal or regulatory obligations. All actions taken under this document are voluntary, so anyone taking actions described in this document does so of their own volition.
>
> — Disclaimer, p. 22

It is joint guidance with no conformance claim: every statement below is a recommendation in
force, whatever verb it uses. The PDF's Version History lists one version ("December 3, 2025:
Initial version.", p. 22) although the file is the January 2026 revision `508cV2`.

## 1. Definitions the statements rely on

> The scope of this guidance specifically covers how critical infrastructure owners and operators can help ensure the safety and security of AI systems in OT environments. As such, the authoring agencies use the following specific definitions for terms in this guidance in order to avoid conflation with their definitions in other contexts:
>
> — Important Terminology, p. 3

- Artificial intelligence (AI) is a system that uses machine- and human-based inputs to make predictions, recommendations, or decisions influencing real or virtual environments. (p. 4)
- Safety refers to physical safety (formally, functional safety) in an OT environment. OT systems control physical systems that can harm people or property, such as systems that deliver biological or chemical agents, control operations for a dam or wastewater treatment, or automate the flow of vehicle traffic. In this guidance, “safety” as a word on its own always refers to functional safety. (p. 4)
- Security (used interchangeably in this guidance with “information security” and “cybersecurity”) refers to ensuring the security properties—such as confidentiality, integrity, and availability—of information and information systems. (p. 4)

Footnote 1 (p. 4): This document uses this AI definition from 15 U.S.C. 9401(3); however, definitions of AI may vary among groups and jurisdictions.

> AI-Enabled OT System. This is defined as any OT system and/or OT network that has at least one AI component within the overall system.
>
> — Appendix: Terminology, p. 23

> Risks. As defined in NIST’s AI Risk Management Framework: “[R]isk refers to the composite measure of an event’s probability of occurring and the magnitude or degree of the consequences of the corresponding event.” In this guidance, the definition of AI risk is the measure of probability that integrating AI into a system will cause an event that harmfully impacts the safety, security, or function of critical infrastructure systems in an organization (or the ecosystem that includes the organization), and the magnitude of the consequences of this event.
>
> — Appendix: Terminology, p. 23

> While AI risk includes broader considerations across industry, academia, and other stakeholders—covering a wide range of issues, such as fairness, bias, and ethics, and the misuse of AI (including harmful content generation)—these issues are not discussed in this guidance. For a discussion of these additional types of harm, visit NIST’s AI Risk Management Framework.
>
> — Appendix: Terminology, p. 23 (the guidance's own exclusion: fairness, bias, ethics and misuse of AI)

## 2. Table 1 — AI Applications According to the Purdue Model (pp. 5–6)

Informative: it shows where AI sits, not what to do. Kept because the threat mapping uses its levels.

| Level | Description | Example AI Uses |
|---|---|---|
| Level 0: Field Devices | Sensors, actuators, and other devices that interact with physical processes. | OT data source: Field devices may generate OT data that can be used for training AI models (primarily predictive ML models) or identifying significant deviations. |
| Level 1: Local Controllers | Apparatus and systems designed to offer automated regulation of a process, cell, or line; examples include programmable logic controllers (PLCs) and remote terminal units (RTUs). | AI for local control: Some modern PLCs or edge controllers execute lightweight, pre-trained predictive models for classification for tasks like local anomaly detection, load balancing, and maintaining a known safe state. |
| Level 2: Local Supervisory | Observation and managerial oversight for an individual process, line, or cell; examples include supervisory control and data acquisition (SCADA) systems, distributed control systems (DCSs), and human-machine interfaces (HMIs). | Quality control: AI models (primarily predictive ML models) may be used for analyzing data from the SCADA system or DCS to detect early signs of equipment anomalies and alert operators that corrective action may be required. |
| Level 3: Site-Wide Supervisory | Monitoring, supervisory, and operational support for all or part of the regions covered by the company; examples include manufacturing execution systems and historians. | Predictive maintenance: AI models (primarily predictive ML models) may be used for analyzing aggregated historian OT data and predicting equipment maintenance requirements. Support operator decision-making: AI models may also be integrated into local supervisory systems to provide system recommendations that support operator decision-making, such as operations measurement. |
| Levels 4 & 5: Enterprise & Business Networks | IT systems that manage business and corporate processes and decisions; in the context of critical infrastructure and OT, examples include OT data analysis and autonomous defense for both OT and IT systems. | Workflow optimization: AI systems (including AI agents and LLMs) may be used for improving business processes, such as the intersection between business use cases and engineering. Behavioral analytics and profiling of OT and IT data: AI can be used for analyzing OT data in conjunction with IT data to measure operations, perform anomaly and threat detection, determine hardening mitigations, and provide information that supports prioritized resiliency decisions. |

## 3. Table 2 — AI Risks and Impacts in an OT Environment (pp. 7–9)

| AI Risks in an OT Environment | OT Impacts | Mitigations |
|---|---|---|
| Cybersecurity Risks: AI data, models, and deployment software can be manipulated to cause incorrect outcomes or bypass security and functional safety measures or guardrails. Traditional cybersecurity risks remain within AI systems; as such, security measures like access control, auditing, and encryption still apply for securing AI and AI-enabled systems. In addition, AI-enabled systems are subject to AI-specific cybersecurity risks, such as prompt injection. | Impacted system availability, functional safety risks, financial losses, reputational damage, network/OT compromise, cascading compromise. | 1.2 Understand the Secure AI System Development Lifecycle; 2.4 Evaluate Challenges in AI-OT System Integration; 3.3 Conduct Thorough AI Testing and Evaluation |
| Data Quality: AI models can only be as effective as the quality of their training data. Collecting high-quality, normalized sensor data can be difficult, especially in distributed OT environments. Centralizing this operational data creates its own risk as threat actors can use it to create a more targeted engineering impact. | Reduced OT safety and system availability from poor data quality. | 2.2 Manage OT Data Security Risks for AI Systems |
| AI Model Drift: AI models may become less accurate over time due to data being introduced to the model that is not represented by the model’s initial training data. Alterations to production processes can affect model performance. | Increased dependencies on changes, loss of productivity, reduced OT safety and system availability. | 4.1 Establish Monitoring and Oversight Mechanisms for AI in OT |
| Lack of Explainability: Understanding an AI model’s decision-making process may be difficult; this makes it challenging to diagnose and correct errors or properly audit a system. | Increased recovery time, functional safety risks, reduced system availability, complexity in troubleshooting. | 1.3 Educate Personnel on AI; 4.1 Establish Monitoring and Oversight Mechanisms for AI in OT |
| Operator Cognitive Load and Unnecessary Downtime: AI may generate alarm errors that could cause unnecessary downtime or safety incidents. These alarm errors increase cognitive load, distract operators, and potentially lead to further human error. | Reduced system availability, functional safety risks, financial losses, reputational damage. | 1.3 Educate Personnel on AI; 4.1 Establish Monitoring and Oversight Mechanisms for AI in OT |
| Regulatory Compliance: Compliance with regulatory requirements, such as those related to OT safety or privacy, can be challenging due to the evolving nature of AI, technical standards, and regulatory frameworks. For example, while producing a robust audit trail of AI-driven decision-making may be difficult, it may be required for regulatory compliance. | Functional safety risks, financial losses, reputational damage. | 3.4 Navigating Regulatory and Compliance Considerations for AI in OT; 4.1 Establish Monitoring and Oversight Mechanisms for AI in OT; 4.2 Embed Safety and Failsafe Mechanisms |
| AI Dependency: Overreliance on AI can lead to operators missing critical safety-related information if the AI misses it, and losing valuable skills for safely operating equipment manually or without the AI functionality. | Dependence on technology, complexity in troubleshooting. | 1.3 Educate Personnel on AI |
| Interoperability Issues: Integrating AI systems with existing OT infrastructure can be complicated by interoperability challenges, which may arise from differences in OT communication protocols or data formats. | Increased maintenance costs, recovery challenges. | 2.1 Consider the OT Business Case for AI Use; 2.4 Evaluate Challenges in AI-OT System Integration; 3.1 Establish Governance Mechanisms for AI in OT; 3.3 Conduct Thorough AI Testing and Evaluation |
| Complexity: Incorporating AI usually requires increasing the complexity of the overall system to support process automation. | Functional safety risks, complexity in troubleshooting. | 2.1 Consider the OT Business Case for AI Use; 2.4 Evaluate Challenges in AI-OT System Integration |
| Reliability: AI may not be reliable enough to independently make critical decisions in industrial environments. AI can also hallucinate (i.e., fabricate a plausible, but false, response or data), which would provide operators with incorrect information for decision-making. As such, AI such as LLMs almost certainly should not be used to make safety decisions for OT environments. | Decisions made by AI developers may pose OT safety and reliability risks, increased documentation costs, uncertainty due to changes in automated decision-making over time, increased risk of cascading failure due to tighter coupling of actions. False information provided to decision makers poses risks of unsafe operating conditions, equipment damage, production halts. | 2.1 Consider the OT Business Case for AI Use; 3.1 Establish Governance Mechanisms for AI in OT; 3.2 Integrating AI Into Existing Security and Cybersecurity Frameworks; 3.3 Conduct Thorough AI Testing and Evaluation; 4.1 Establish Monitoring and Oversight Mechanisms for AI in OT; 4.2 Embed Safety and Failsafe Mechanisms |

The Mitigations column cross-references the sections that discuss each risk; the Reliability
row's last sentence is requirement R-0010. The rows are carried as threats in `threats.yaml`.

## 4. Normative statements, in source order

One bullet per `requirements.yaml` entry: id, verb, page, then the verbatim text. Items of a
list are indented under their lead-in.

### Introduction

- **R-0001** (must, p. 3) — Despite the many benefits, integrating AI into operational technology (OT) environments that manage essential public services also introduces significant risks—such as OT process models drifting over time or safety-process bypasses—that owners and operators must carefully manage to ensure the availability and reliability of critical infrastructure.
- **R-0002** (Understand, p. 3) — Understand AI. Understand the unique risks and potential impacts of AI integration into OT environments, the importance of educating personnel on these risks, and the secure AI development lifecycle.
- **R-0003** (Assess, p. 3) — Consider AI Use in the OT Domain. Assess the specific business case for AI use in OT environments and manage OT data security risks, the role of vendors, and the immediate and long-term challenges of AI integration.
- **R-0004** (Implement, p. 3) — Establish AI Governance and Assurance Frameworks. Implement robust governance mechanisms, integrate AI into existing security frameworks, continuously test and evaluate AI models, and consider regulatory compliance.
- **R-0005** (Implement, p. 3) — Embed Safety and Security Practices Into AI and AI-Enabled OT Systems. Implement oversight mechanisms to ensure the safe operation and cybersecurity of AI-enabled OT systems, maintain transparency, and integrate AI into incident response plans.
- **R-0006** (encourage, p. 3) — The authoring agencies encourage critical infrastructure owners and operators to review this guidance and action the principles so they can safely and securely integrate AI into OT systems.

### Scope

- **R-0007** (may, p. 4) — However, this guidance may also be applied to systems augmented with traditional statistical modeling and other logic-based automation.

### 1.1 Understand the Unique Risks of AI and Potential Impact to OT

*Principle 1 – Understand AI*

- **R-0008** (should, p. 7) — Table 2 provides a broad overview of known AI risks that critical infrastructure owners and operators should consider.
- **R-0009** (should, p. 7) — critical infrastructure owners and operators should investigate risks specific to their organization.
- **R-0010** (should not, p. 9) — As such, AI such as LLMs almost certainly should not be used to make safety decisions for OT environments.

### 1.2 Understand the Secure AI System Development Lifecycle

*Principle 1 – Understand AI*

- **R-0011** (should, p. 9) — To address the unique challenges of integrating AI into OT environments, critical infrastructure owners and operators should verify that the AI system was designed securely and understand their roles and responsibilities through the AI system’s lifecycle.
- **R-0012** (must, p. 9) — Similar to hybrid ownership models used with cloud systems, owners and operators must clearly define and communicate these roles and responsibilities with the AI system manufacturer, OT supplier, and any system integrator or managed service provider roles.
- **R-0013** (emphasizes, p. 10) — NCSC-UK and CISA’s joint Guidelines for Secure AI System Development emphasizes the following key stages of the AI system development lifecycle:
  - **R-0014** (Design, p. 10) — Secure Design. Design the AI system with security considerations in mind from its inception, including using robust coding, protocols, and data protection measures.
  - **R-0015** (Select, p. 10) — Secure Procurement or Development. Select vendors who adhere to secure practices and develop AI systems using secure methodologies and tools.
  - **R-0016** (Deploy, p. 10) — Secure Deployment. Deploy the AI system using methods that maintain its security posture, including using proper network segmentation and access control, as well as verifying and validating that the AI system works as intended.
  - **R-0017** (Ensure, p. 10) — Secure Operation and Maintenance. Ensure the AI system continues operating securely throughout its lifecycle, including by implementing regular updates and patches, and monitoring potential vulnerabilities.
- **R-0018** (should, p. 10) — Critical infrastructure owners and operators should also carefully evaluate the trade-offs between different methods for sourcing an AI system: Procure an AI System. Select a pre-developed AI system from a vendor that meets specific security requirements and that the OT supplier agrees with. Develop an AI System. Build an AI system in house; this enables complete control over its design and implementation. Customize an Existing AI System. Work with a vendor to tailor their existing AI system to meet specific OT system needs.
- **R-0019** (should, p. 10) — Where possible, critical infrastructure owners and operators should demand AI systems that are secure by design and will not negatively impact OT operation and safety.
- **R-0020** (should, p. 10) — Critical infrastructure owners and operators should consult CISA’s Secure by Design webpage and resources, and the joint guidance Secure by Demand: Priority Considerations for Operational Technology Owners and Operators when Selecting Digital Products for opportunities to incorporate these principles into the design of their AI and OT systems.

### 1.3 Educate Personnel on AI

*Principle 1 – Understand AI*

- **R-0021** (may, p. 11) — Critical infrastructure owners and operators may mitigate these risks by focusing on skill development and cross-disciplinary collaboration, such as:
  - **R-0022** (may (training), p. 11) — Training OT teams on AI fundamentals and threat modeling so teams can effectively interpret and validate AI outputs and maintain operational competencies alongside AI systems—for example, training teams to use alternative sensors (e.g., human senses, vibration or temperature sensors, voltage readings) for validating AI output—and know what actions to take if AI outputs are invalid.
  - **R-0023** (may (developing), p. 11) — Developing clear standard operating procedures (SOPs) for all operations (including AI-related operations), interventions, and incidents to support stakeholder awareness of their roles and responsibilities in managing AI-enabled OT systems.
  - **R-0024** (may (leveraging), p. 11) — Leveraging explainable AI by having operators request that AI outputs include clear and transparent documentation of decision-making processes; this enables humans to better understand and validate outputs.

### 2.1 Consider the OT Business Case for AI Use

*Principle 2 – Consider AI Use in the OT Domain*

- **R-0025** (should, p. 11) — Before incorporating an AI system into their OT environment, critical infrastructure owners and operators should assess if AI technologies are the most appropriate solution for their specific needs and requirements compared to other technologies.
- **R-0026** (should, p. 11) — Critical infrastructure owners and operators should further consider whether an established capability meets their needs before pursuing more complex and novel AI-enabled solutions.
- **R-0027** (should, p. 11) — This assessment should incorporate various factors—including security, performance, complexity, cost, and effect on OT-environment safety depending on the specific application—and assess the benefits and risks of using the AI technologies against the functional requirements the application should meet.
- **R-0028** (should, p. 11) — Critical infrastructure owners and operators should understand the organization’s current capacity for maintaining an AI system in their OT environment and the potential impact of expanding the environment’s risk surface, such as requiring additional hardware and software for processing data through models or additional security infrastructure to protect the expanded attack surface.
- **R-0029** (should, p. 11) — If the assessment indicates an AI system is the best solution, then critical infrastructure owners and operators should follow the secure AI system development lifecycle outlined above and consult AI risk management frameworks, such as the National Institute of Standards and Technology’s (NIST’s) AI Risk Management Framework to help ensure the system is used safely and securely.

### 2.2 Manage OT Data Security Risks for AI Systems

*Principle 2 – Consider AI Use in the OT Domain*

- **R-0030** (should, p. 12) — When integrating AI into OT environments, critical infrastructure owners and operators should work with AI model developers when addressing several data-related challenges, including:
  - **R-0031** (Understand, p. 12) — Data Assurance. Understand where OT data used for training AI models is stored and ensure it is within the organization’s control. Securely manage access to OT data, including who can view, access, or modify it. Understand how AI vendors access and use the organization’s OT data, especially if it involves remote, cloud, or offshore access.
  - **R-0032** (Be aware, p. 12) — Data Sovereignty. Be aware that businesses based in foreign countries are subject to foreign government control and laws and may have to comply with directions that may be contrary to your business’ interests.
  - **R-0033** (Minimize, p. 13) — Exposure of Sensitive Information. Minimize risk by not sharing sensitive data with AI models, especially if the AI models are hosted in an environment hosted or controlled by external parties, such as public cloud infrastructure.
  - **R-0034** (Protect, p. 13) — Data Privacy and Security. Protect proprietary and personal information within OT datasets, including by instituting protection from access abuse, intentional or inadvertent data poisoning, or dependency on synthetic, generated data.
  - **R-0035** (Address, p. 13) — Data Silos. Address the complexity of integrating AI systems in OT environments due to OT/IT network segregation, proprietary protocols, formats, diversity of OT products, and a multitude of suppliers.
  - **R-0036** (Apply, p. 13) — Data Quality and Availability. Apply specialized domain knowledge that curates high-quality, comprehensive datasets for effective AI performance. This can be challenging in industrial settings; potential difficulties include the environment containing proprietary or outdated systems and bespoke solutions, and the difficulty of capturing safety-related edge cases. OT operator expertise is necessary for capturing this specialized knowledge.
  - **R-0037** (should, p. 13) — Additionally, operators should work with AI model developers to ensure a data integrity program covers AI systems.
- **R-0038** (Prioritize, p. 13) — Prioritize the protection of critical types of OT data, including the following: Engineering Configuration Data. These include network diagrams, asset inventories, documentation on operations sequences, safety-related information, logic diagrams, and schematics. These data points have enduring value and are highly valuable to cyber adversaries. Ephemeral OT Data. Data from industrial measurement technology, especially process measurement technology (e.g., voltage or temperature, pressure levels, mass/volume flow rates) can provide insight into organizational activities or system behavior. If that data is used to train or update an AI model, the data may become accessible or stored (statistically) for a longer period of time in the model. As such, securing these data points can be important for protecting intellectual property (IP) and patterns of activity.

### 2.3 Understanding the Role of OT Vendors in AI Integration

*Principle 2 – Consider AI Use in the OT Domain*

- **R-0039** (should, p. 14) — Critical infrastructure owners and operators should demand transparency and security considerations from OT vendors regarding how AI technologies are embedded into their products. This includes:
  - **R-0040** (Negotiate, p. 14) — Contractual Agreements. Negotiate contractual agreements that ensure OT vendors provide explicit details on AI features and functionalities.
  - **R-0041** (Require, p. 14) — Software Supply Chain and Software Bill of Materials (SBOM). Require OT vendors to provide information on how AI is embedded into their OT products (including by requesting vendors provide an SBOM) and clarify the supply chain of AI models used in their products (e.g., where models are hosted).
  - **R-0042** (should, p. 14) — Vendor Notifications. In addition to typical vulnerability disclosure policies for the lifecycle of the product, the AI vendor should disclose if they have discovered an indication that the AI can provide improper advice or take inappropriate action.
  - **R-0043** (can, p. 14) — Explicit Data Usage Policy Review and Enforcement. Operators may not want vendors to train AI on operational data as it could include IP or be sensitive. Operators can control their information via a data usage policy with clear reference to data residency, communications paths, encryption, and storage.
  - **R-0044** (Ask, p. 14) — Increased Connectivity. Ask if vendors can operate on premises or without continuous access to the internet/vendor cloud.
  - **R-0045** (Specify, p. 14) — Disabling AI Features. Specify conditions under which certain AI features can be disabled or enabled, with control given to the operator.

### 2.4 Evaluate Challenges in AI-OT System Integration

*Principle 2 – Consider AI Use in the OT Domain*

- **R-0046** (should, p. 14) — When integrating AI into OT environments, critical infrastructure owners and operators should carefully evaluate the existing infrastructure to ensure compatibility and security.
- **R-0047** (should, p. 15) — To mitigate these challenges, critical infrastructure owners and operators should:
  - **R-0048** (Integrate, p. 15) — Integrate AI systems into their overall security and cybersecurity framework (see 3.2 Integrating AI Into Existing Security and Cybersecurity Frameworks).
  - **R-0049** (Add, p. 15) — Add AI security considerations to a comprehensive security strategy that also includes traditional cybersecurity considerations, such as data encryption, access controls, and intrusion detection systems.
  - **R-0050** (should, p. 15) — Critical infrastructure owners and operators should define and validate security clauses in cloud contracts, explicitly outlining any AI security responsibilities, compliance standards, and support provisions, including data protection, access controls, incident response, and audit capabilities.
  - **R-0051** (should, p. 15) — Cloud providers should provide detailed documentation that outlines security obligations specific to AI capabilities, in addition to traditional cloud security shared responsibility models.
  - **R-0052** (Consider, p. 15) — Consider existing OT infrastructure and assess and develop an integration plan for AI systems.
  - **R-0053** (Consider, p. 15) — Consider using test infrastructure before deployment to production systems, if possible (see Principle 3 – Establish AI Governance and Assurance Frameworks).
  - **R-0054** (Encourage, p. 15) — Encourage push-based architectures where data is pushed out of the OT network for AI systems to use without persistent access into the OT network.
  - **R-0055** (Prioritize, p. 15) — Prioritize the organization’s control over critical functions that AI systems may integrate with or enable when hosting AI systems locally or in the cloud.
  - **R-0056** (Ensure, p. 15) — Ensure there are failsafe mechanisms that revert to traditional automation or manual for any AI-enabled system processes.
  - **R-0057** (Integrate, p. 15) — Integrate AI systems the same as any new OT systems: test AI systems for safety impacts (e.g., latency, interoperability) and verify they work within existing device management policy (i.e., new connection paths such as remote access are approved and work through the existing demilitarized zone [DMZ] or jump host infrastructure).
  - **R-0058** (Limit, p. 16) — Limit active control of OT infrastructure by AI without a human in the loop to account for safety concerns and latency limitations.
  - **R-0059** (Regularly update, p. 16) — Regularly update and validate AI models for accuracy and effectiveness.

### 3.1 Establish Governance Mechanisms for AI in OT

*Principle 3 – Establish AI Governance and Assurance Frameworks*

- **R-0060** (are essential, p. 16) — Effective governance structures are essential for the safe and secure integration of AI into OT environments. This involves establishing clear policies, procedures, and accountability structures for AI decision-making processes within OT.
- **R-0061** (should, p. 16) — An AI governance structure should include the key stakeholders listed below, as well as any AI vendors needed for maintaining oversight during procurement, development, design, deployment, and operations.
  - **R-0062** (is essential, p. 16) — Leadership. Securing commitment from senior leadership, including the CEO and CISO, is essential for establishing a robust AI governance framework. This helps ensure that the organization’s leadership is fully invested in the secure lifecycle management of AI systems and considers AI security risks and mitigations alongside AI functionality.
  - **R-0063** (is critical, p. 16) — OT/IT Subject Matter Experts. Engaging OT, IT, and AI subject matter experts is critical for effective and secure integration of AI systems into OT environments. These experts provide valuable insights into the OT environment and can help identify potential risks and challenges associated with AI integration.
  - **R-0064** (is vital, p. 16) — Cybersecurity Teams. Collaborating with cybersecurity teams is vital for developing policies and procedures that protect sensitive OT data used by AI models. Cybersecurity teams can help identify potential vulnerabilities and provide mitigation recommendations to help maintain the security of the organization’s data.
- **R-0065** (may, p. 16) — Other key components of governance structures may include:
  - **R-0066** (may (enforcing), p. 16) — Enforcing strict data governance policies that protect sensitive OT data used by AI models, including encryption, access controls, and user behavior analytics.
  - **R-0067** (may (establishing), p. 16) — Establishing clear roles and responsibilities that ensure everyone involved in the development, deployment, and operations and maintenance of AI systems (e.g., data owners, model developers, and end users) understands their tasks and expectations—and to avoid liability and confusion over stakeholder responsibilities in the event of safety or operational incidents.
  - **R-0068** (may (implementing), p. 16) — Implementing regular audits and compliance testing to help identify potential issues and ensure ongoing adherence to AI governance requirements.
  - **R-0069** (Continuously validate, p. 16) — Continuously validate and verify the performance of AI systems to make sure they meet the organization’s objectives and regulatory requirements.

### 3.2 Integrating AI Into Existing Security and Cybersecurity Frameworks

*Principle 3 – Establish AI Governance and Assurance Frameworks*

- **R-0070** (should, p. 17) — When integrating AI into OT environments, critical infrastructure owners and operators should consider the existing security and cybersecurity frameworks that govern these systems and embed AI system assessments within existing risk evaluation, mitigation, and monitoring processes.
- **R-0071** (must, p. 17) — This means that traditional cybersecurity requirements, vulnerability management, and critical infrastructure regulations must be factored in when integrating AI systems.
  - **R-0072** (Conduct, p. 17) — Regular Security Audits and Risk Assessments. Conduct, or obtain proof of the AI vendor conducting, regular security audits and risk assessments to identify potential vulnerabilities in AI systems.
  - **R-0073** (Implement, p. 17) — Robust Security Controls. Implement robust security controls, such as encryption, access controls, and intrusion detection systems, that protect and detect anomalies in AI systems and data.
  - **R-0074** (Collect, p. 17) — Collect flow logs and access logs for AI endpoints and track data egress by asset and identity.
  - **R-0075** (Integrate, p. 17) — Integrate with data loss prevention for prompts and output inspection.
  - **R-0076** (should, p. 17) — AI-Tailored Security Information. Security teams should incorporate AI-related tactics, techniques, and procedures (TTPs) when evaluating risk or modeling threats.
  - **R-0077** (should, p. 17) — For instance, when using the MITRE ATT&CK® Matrix for Enterprise for threat actor behavior mapping, teams should also incorporate AI-related TTPs using tools such as the MITRE Adversarial Threat Landscape for Artificial-Intelligence Systems (ATLAS™) Matrix, which is tailored for TTPs against AI-enabled systems,

### 3.3 Conduct Thorough AI Testing and Evaluation

*Principle 3 – Establish AI Governance and Assurance Frameworks*

- **R-0078** (are crucial, p. 17) — Thorough testing and evaluation (T&E) are crucial when introducing AI into OT environments to support the safe and reliable operation of these systems.
- **R-0079** (should, p. 17) — Operators should initially conduct tests of the AI system on infrastructure specifically designed for testing.
- **R-0080** (work with, p. 17) — Alternatively, work with vendors to understand their testing and if it includes dependencies (e.g., operating system versions, protocols).
- **R-0081** (can, p. 17) — As the system matures, operators can test with more realistic, non-production systems, including hardware in the loop.
- **R-0082** (should, p. 17) — Operators should only move the AI system into production for additional testing after sufficient testing in a non-production environment.
- **R-0083** (should, p. 17) — Critical infrastructure owners and operators should also comply with traditional data protection mechanisms when conducting AI testing and evaluation, such as avoiding production data exposure in non-production environments.

### 3.4 Navigating Regulatory and Compliance Considerations for AI in OT

*Principle 3 – Establish AI Governance and Assurance Frameworks*

- **R-0084** (should, p. 18) — Critical infrastructure owners and operators should evaluate the applicability of current AI technical standards in their OT domain as AI technical standards are rapidly evolving.
- **R-0085** (should, p. 18) — Critical infrastructure owners and operators should continuously validate and verify that the performance of AI systems meets stringent OT performance and safety regulations.
- **R-0086** (should, p. 18) — Critical infrastructure owners and operators should also identify and deploy thresholds for defaulting back to non-AI systems in OT, such as if AI system outputs fall below performance and safety thresholds.

### Principle 4 – Embed Oversight and Failsafe Practices Into AI and AI-Enabled OT Systems

- **R-0087** (are responsible, p. 18) — Ultimately, humans are responsible for functional safety. Humans make tools that ensure or operationalize oversight, safety, and failsafe practices—this is no different for AI tools.

### 4.1 Establish Monitoring and Oversight Mechanisms for AI in OT

*Principle 4 – Embed Oversight and Failsafe Practices Into AI and AI-Enabled OT Systems*

- **R-0088** (should, p. 18) — Critical infrastructure owners and operators should implement oversight of AI-enabled OT systems by taking inventory of any AI components, as well as other components reliant on the AI.
- **R-0089** (Log and monitor, p. 18) — Log and monitor inputs and outputs for these components.
- **R-0090** (establish and maintain, p. 18) — Also, establish and maintain a known good state or thresholds for safe behavior in an OT environment, allowing for knowledge of when maintenance or restoration should be performed from a backup.
- **R-0091** (Consider, p. 18) — Consider the following points when embedding safety processes into AI-enabled OT systems to ensure effective implementation and management:
  - **R-0092** (Provide, p. 18) — Human-in-the-Loop Decision-Making. Provide adequate transparency that involves operators and engineers in decision-making, especially for critical OT operations and actions. For more passive AI systems, operators and engineers can implement this by incorporating the recommendations into an existing change management process.
  - **R-0093** (Use caution, p. 19) — Use caution with active AI systems directly influencing control, as problems can escalate before operators become aware of them.
  - **R-0094** (use, p. 19) — Where AI is actively updating control logic, use safety thresholds, alternative sensor output, or state changes that add human-in-the-loop intervention points.
  - **R-0095** (Understand, p. 19) — Understand the correctness of AI system results to support continued safe operation of systems in an OT environment. It is vital for critical infrastructure owners and operators to understand the states where an AI system can fail to produce accurate and reliable results. This understanding includes expectations for false positives and false negatives in the system’s performance, and how the false positives compare to the base rate of true positives.
  - **R-0096** (Implement, p. 19) — Implement anomaly detection and behavioral analytics. Establish safe operating bounds for OT devices that detect AI drift, model changes that impact safety and performance, or security risks.
  - **R-0097** (Configure, p. 19) — Configure logging so AI decisions can be tracked for compliance and forensic analysis, and so the logged AI identity is distinct from any typical machine or user identifiers.
- **R-0098** (should, p. 19) — The example below demonstrates how operators and engineers should monitor a predictive maintenance system (with read-only access to OT data output) in the data zone that uses ML to produce recommendations:
  - **R-0099** (should (monitor), p. 19) — AI System Output. Predictive maintenance recommendations for equipment downtime.
  - **R-0100** (should (monitor), p. 19) — Anomaly Detection Algorithm. Statistical process control that detects outliers in predicted downtime values.
  - **R-0101** (should (monitor), p. 19) — Monitoring Tools. Real-time dashboards, charts, or metrics that track AI system performance and detect anomalies—ideally, these are integrated into existing human-machine interface (HMI) views for consolidated monitoring.
  - **R-0102** (should (monitor), p. 19) — Audit Trail. Logging of all AI system operating data (including timestamps, inputs, and outputs) for auditing and analysis of AI system behavior.
  - **R-0103** (Regularly evaluate, p. 19) — Offensive Security Assessments/AI Red Teaming. Regularly evaluate AI system functions, identifying vulnerabilities and testing resilience.
  - **R-0104** (Define and enforce, p. 19) — Network and Egress Security. Define and enforce network controls; see CISA’s Cybersecurity Performance Goals (CPGs) 2.F.
- **R-0105** (Establish, p. 19) — Establish key performance indicators (KPIs) that measure AI effectiveness and track progress over time.
- **R-0106** (should, p. 19) — Critical infrastructure owners and operators should schedule regular review sessions with AI stakeholders, such as vendors, governance boards, and operators, to discuss results, address concerns, and identify areas for improvement.
- **R-0107** (Continuously validate and refine, p. 20) — Continuously validate and refine AI models in simulated environments before deployment.
- **R-0108** (Regularly update, p. 20) — Regularly update threat models with AI-specific attack vectors (such as adversarial inputs or data poisoning) and monitor AI system performance for anomalies or manipulation attempts.
- **R-0109** (Continuously update and refine, p. 20) — Continuously update and refine AI models with new OT data to improve precision and reduce false positives/negatives.
- **R-0110** (Explore, p. 20) — Explore new AI explainability and transparency tools.
- **R-0111** (should, p. 20) — Critical infrastructure owners and operators should, where possible, explore interpretable models or tools that make AI decisions more understandable to humans.
- **R-0112** (is critical, p. 20) — Such transparency is critical for safety and regulatory compliance in OT.
- **R-0113** (Prefer, p. 20) — Prefer push-based or brokered architectures that move required features or summaries out of OT without granting persistent inbound access.
- **R-0114** (use, p. 20) — Where data must traverse to business networks, use one-way transfer patterns and audited staging buffers.

### 4.2 Embed Safety and Failsafe Mechanisms

*Principle 4 – Embed Oversight and Failsafe Practices Into AI and AI-Enabled OT Systems*

- **R-0115** (Establish, p. 20) — Establish failsafe mechanisms that enable AI systems to fail gracefully without disrupting critical operations.
- **R-0116** (Incorporate, p. 20) — Incorporate new AI system failure states, including how to bypass or replace an AI system, into existing functional safety and incident response processes.
- **R-0117** (should, p. 20) — Therefore, operators responsible for revising the existing functional safety and incident response processes should incorporate these new failure states as they are critical to ensuring safe operation of these systems.
- **R-0118** (Design, p. 20) — Design functional safety procedures that account for the AI system.
- **R-0119** (should, p. 20) — Per Principle 2 – Consider AI Use in the OT Domain, critical infrastructure owners and operators should review how they are integrating the AI system into their existing procedures and create new safe use and implementation procedures that focus on the AI system integration into the OT environment.
- **R-0120** (Incorporate, p. 20) — Incorporate AI considerations into the cybersecurity incident response plan.
- **R-0121** (should, p. 20) — To account for this, critical infrastructure owners and operators should update their incident response plans and functional safety procedures with steps for responding to malicious activity directed against an AI system and AI system failure.

### Conclusion

- **R-0122** (is essential, p. 21) — For successful mitigation of the risks of integrating AI into OT systems, it is essential critical infrastructure owners and operators follow the principles in this guidance: understand AI, consider AI use in the OT domain, establish AI governance and assurance frameworks, and embed safety and security practices into AI and AI-enabled OT systems.

### Appendix: Terminology

- **R-0123** (should, p. 23) — However, as definitions of AI and OT may vary among groups, readers should also understand their local jurisdiction’s specific definition of these concepts and consider how they are applicable to this guidance.

## 5. What is not here, and why

- Descriptive prose: background on AI techniques (Scope, Types of AI Techniques), the
  human-in-the-loop benefit list (p. 19), the §1.3 consequence list and the §2.4 and §3.4
  challenge lists. The consequence and challenge lists describe risks, so they are in
  `threats.yaml` with locators.
- Navigation sentences ("See …", "Visit …", "For more definitions …").
- The §2.1 business-case example (pp. 11–12) states no recommendation, so it is not here; it is
  kept whole as a fixture in `examples/`. The §4.1 monitoring example (p. 19) is here, because its
  lead-in says how operators "should monitor", and is also kept as a fixture.
- Resources, Acknowledgements, References and footnotes other than footnote 1: bibliography,
  held in `record.yaml` `cites`.
