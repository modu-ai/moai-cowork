# Privacy Engineer (69-privacy-engineer)

> MoAI-Cowork v0.1.3 Harness Reference

## Overview
A privacy engineering agent team harness.

## Expert Roles
- **consent-designer**: Consent document author. Designs and drafts personal information collection/use consent forms, privacy policies, and notices based on legal analysis and PIA results.
  - Consent Form Design: Design personal information collection/use consent forms in compliance with legal requirements
  - Required/Optional Consent Distinction: Clearly distinguish between required and optional consent, and specify methods for withdrawing consent
  - Privacy Policy Drafting: Draft privacy policies that include all legally required disclosures without omission
  - Plain Language: Convert legal terminology into plain expressions that the general public can understand
  - GDPR Consent Requirements: Where applicable, reflect GDPR's valid consent requirements (freely given, specific, informed, unambiguous)
- **pia-assessor**: PIA Assessor. Systematically conducts Privacy Impact Assessments, calculates risk levels, and recommends protective measures.
  - Processing Activity Mapping: Map the entire lifecycle of personal data — collection → use → disclosure → retention → destruction
  - Risk Identification & Assessment: Identify risks that may arise from each processing activity and calculate risk levels
  - Protective Measure Design: Design technical and administrative safeguards to reduce risks to an acceptable level
  - Residual Risk Assessment: Evaluate residual risk after protective measures have been applied
  - DPIA Report Writing: Produce impact assessment reports conforming to GDPR Article 35 or the Personal Information Protection Act Enforcement Decree standards
- **privacy-law-analyst**: Privacy law analyst. Analyzes applicable laws including GDPR, Personal Information Protection Act (PIPA), and the Act on Promotion of Information and Communications Network Utilization, and maps obligations by service type.
  - Applicable Law Determination: Identify applicable laws based on service type, user geography, and data type
  - GDPR Applicability Analysis: Determine whether the service targets EU residents and assess extraterritorial application conditions
  - PIPA (Personal Information Protection Act) Analysis: Map obligations of personal data controllers under domestic law, article by article
  - Special Act Applicability: Confirm whether special acts such as the Network Act, Credit Information Act, or Medical Act apply
  - Lawful Basis Analysis: Determine the lawful basis for each processing activity
- **process-architect**: Process designer. Designs the full lifecycle of personal data processing, specifies technical and administrative safeguards, and defines operational processes.
  - Processing Workflow Design: Design operational processes covering the full cycle — collection → use → provision → retention → destruction
  - Technical Safeguard Design: Specify technical measures such as encryption, access control, log management, and pseudonymization
  - Administrative Safeguard Design: Design management frameworks including internal management plans, training, outsourcing management, and incident response
  - Data Subject Rights Processes: Design processes for handling requests to access, rectify, delete, or restrict processing
  - Incident Response Framework: Design response procedures and notification processes for personal data breach incidents

## Workflow
### Phase 1: Preparation (Orchestrator performs directly)

1. Extract from user input:
    - **Service name/type**: web, app, SaaS, e-commerce, etc.
    - **Data processed**: personal data items collected
    - **User regions**: domestic, EU, US, etc.
    - **Service scale**: number of users, data volume
    - **Existing materials** (optional): current privacy policy, consent forms, system architecture diagrams
2. Create a `_workspace/` directory at the project root
3. Organize inputs and save to `_workspace/00_input.md`
4. **Determine execution mode** based on request scope

### Phase 2: Team Assembly and Execution

| Step | Task | Owner | Depends On | Output |
|------|------|------|------|--------|
| 1 | Legal analysis | privacy-law-analyst | None | `_workspace/01_privacy_law_analysis.md` |
| 2 | PIA execution | pia-assessor | Step 1 | `_workspace/02_pia_report.md` |
| 3a | Consent form drafting | consent-designer | Steps 1, 2 | `_workspace/03_consent_documents.md` |
| 3b | Process design | process-architect | Steps 1, 2 | `_workspace/04_process_design.md` |

Steps 3a (consent) and 3b (process) run **in parallel**. Both depend on legal analysis and PIA, so they can start simultaneously after Step 2 completes.

**Inter-agent communication flow:**
- privacy-law-analyst completes → sends processing activity list and risk factors to pia-assessor
- pia-assessor completes → sends disclosure requirements to consent-designer, sends safeguard recommendations to process-architect
- consent-designer → sends consent collection timing and management requirements to process-architect
- process-architect cross-validates logical consistency across all outputs during final design

### Phase 3: Integration and Final Deliverables

1. Review all files in `_workspace/`
2. Verify consistency across legal analysis → PIA → consent forms → process design
3. Report final summary to user:
    - Legal analysis report — `01_privacy_law_analysis.md`
    - PIA report — `02_pia_report.md`
    - Consent forms and notices set — `03_consent_documents.md`
    - Process design document — `04_process_design.md`

## Deliverables


## Extension Skills
- **data-flow-mapper**: A data flow mapping tool that systematically maps personal information processing flows and identifies risk points. The 'pia-assessor' and 'process-architect' agents must utilize this skill's mapping methodology and risk point identification patterns when analyzing data flows and designing protective measures. Use for 'data flow analysis', 'processing activity mapping', 'risk point identification', and similar tasks. Note that legal analysis or consent form drafting is outside the scope of this skill.
- **gdpr-pipa-cross-reference**: Cross-reference database for GDPR and Korea's Personal Information Protection Act (PIPA). The 'privacy-law-analyst' and 'consent-designer' agents must use this skill's article mappings and gap analysis when analyzing multi-jurisdiction privacy requirements and designing consent forms. Use for 'GDPR vs PIPA comparison', 'legal requirements cross-analysis', 'global compliance strategies', etc. Note: data flow mapping and technical safeguard design are outside the scope of this skill.
- **privacy-engineer**: Full privacy engineering pipeline. An agent team collaborates to perform GDPR/PIPA analysis → PIA → consent forms → process design in a single run. Use this skill for all privacy-related needs including: 'privacy by design', 'GDPR compliance', 'privacy impact assessment', 'PIA execution', 'consent form drafting', 'privacy policy', 'privacy design', 'personal data protection law compliance', 'PIPA response', 'data protection framework', etc. Note: actual submissions to the Personal Information Protection Commission, legal litigation representation, ISMS-P certification audits, and physical security system implementation are outside the scope of this skill.

## Error Handling
| Error Type | Strategy |
|----------|------|
| Web search failure | Legal analyst works from general knowledge, notes "latest guidelines not verified" |
| Insufficient service information | Assumes standard web service baseline, notes "assumption-based" |
| Uncertain GDPR applicability | Proceeds assuming GDPR applies, recommends separate confirmation |
| Agent failure | Retry once → if still failing, proceed without that deliverable, note omission in final report |
| Inconsistency between PIA and legal analysis | process-architect identifies inconsistency, applies conservative judgment |
