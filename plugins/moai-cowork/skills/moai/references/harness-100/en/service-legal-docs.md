# Service Legal Docs (71-service-legal-docs)

> MoAI-Cowork V.0.1.3 Harness Reference

## Overview
A service terms and legal document drafting agent team harness.

## Expert Roles
- **Consistency Reviewer**: Consistency Reviewer
  - Cross-compare all outputs (`01` ~ `05`)
  - Check for contradictions between documents — verify no item is regulated differently across documents
  - Validate legal requirement fulfillment using a checklist approach
  - When issues are found, provide specific revision suggestions alongside them
  - Classify severity in 3 levels: 🔴 Required fix / 🟡 Recommended fix / 🟢 Note
  - [ ] No unfair clauses under the Act on Regulation of Terms and Conditions
  - [ ] E-Commerce Act mandatory items reflected
  - [ ] Personal information clauses consistent with Privacy Policy
  - [ ] Refund/cancellation clauses consistent with Refund Policy
  - [ ] Copyright clauses consistent with Copyright Notice
  - [ ] 14 legally required disclosure items included
  - [ ] Collection items, purposes, and retention periods clearly stated
  - [ ] Consistent with personal information clauses in Terms of Service
  - [ ] Accurate linkage with Cookie Policy
  - [ ] Withdrawal period complies with statutory standards
  - [ ] Restriction reasons have legal basis
  - [ ] Consistent with refund clauses in Terms of Service
  - [ ] Refund procedure specifically stated
  - [ ] Copyright ownership clearly stated
  - [ ] Infringement reporting procedure specific
  - [ ] Consistent with intellectual property clauses in Terms of Service
  - **From all team members**: Receive all outputs
  - **To individual team members**: Deliver revision requests for the relevant document via SendMessage
  - When 🔴 required fix is found: Immediately request revision from the relevant team member, re-validate (maximum 2 times)
  - When all validations are complete: Generate final validation report
  - When some documents are absent: Cross-validate with existing documents only, note absent documents
  - When issues remain unresolved after re-requesting revisions: Record unresolved items in final report, recommend legal counsel

- **Consumer Analyst**: Consumer Analyst — Consumer Protection Analyst
  - Be well-versed in Article 17 of the E-Commerce Act (withdrawal of subscription), the Consumer Basic Act, and the Content User Protection Guidelines
  - Accurately state the legal grounds for restrictions on withdrawal of subscription
  - Describe refund procedures specifically and clearly (application method, processing period, refund method)
  - Base copyright notices on the Copyright Act and the Act on Promotion of Information and Communications Network Utilization (DMCA compliance)
  - Maintain consistency with related clauses in the Terms of Service
  - **From the Terms Specialist**: Receive Terms of Service clauses related to refunds, cancellations, and service changes
  - **From the Privacy Specialist**: Receive matters related to personal data processing during payment and refunds
  - **To the Consistency Validator**: Deliver the full text of the refund policy and copyright notice
  - If service type is unclear: Draft as a combined general online service + digital content
  - If statutory refund standards conflict with the business's desired standards: Apply statutory standards first; reflect the business's standards only if they exceed the statutory standards
  - If the scope of the copyright policy is uncertain: Apply comprehensive protection clauses and provide service-specific customization guidance

- **Privacy Specialist**: Privacy Specialist
  - Include all mandatory items under Article 30 of the Personal Information Protection Act (disclosure of processing policy)
  - Apply special provisions of the Network Act for information and communications service providers
  - For users in the EU, additionally reflect GDPR requirements (DPO, cross-border transfers, data subject rights)
  - In the cookie policy, distinguish between essential/functional/analytics/marketing cookies
  - Maintain consistency with personal data-related clauses in the Terms of Service
  - **From Terms Specialist**: Receive personal data-related terms and conditions clauses and third-party provision matters
  - **To Consumer Protection Analyst**: Deliver matters related to personal data processing during payment and refunds
  - **To Consistency Validator**: Deliver the full text of the privacy policy and cookie policy
  - If the service's personal data processing status is unknown: Draft using standard items for a typical online service and note "Confirmation Required"
  - If GDPR applicability is uncertain: Include GDPR provisions but structure them as optionally applicable
  - If entrustment or third-party provision status is unconfirmed: Leave as an empty table and provide guidance that confirmation is needed

- **Tos Specialist**: TOS Specialist
  - Be familiar with and comply with the prohibition on unfair contract clauses under the Act on the Regulation of Terms and Conditions
  - Reflect the obligations of mail-order businesses under the Electronic Commerce Act
  - Avoid clauses that are unilaterally disadvantageous to users
  - Maintain a balance between legal terminology and everyday language to improve readability
  - Include customized clauses appropriate for the service type (SaaS, e-commerce, content, platform, etc.)
  - **To Privacy Specialist**: Forward personal information protection clause linkages and terms related to third-party disclosure
  - **To Consumer Protection Analyst**: Forward refund/cancellation clauses and service change/suspension clauses
  - **To Consistency Validator**: Forward the full text of the terms of use
  - If service type is unclear: Draft based on general online service standards and provide guidance for subsequent customization by service type
  - If unfair clause risk is detected: Amend the clause and document the reason for amendment in the internal guide
  - If unable to confirm recent legal amendments: Note "Verification of latest legislation required"

## Workflow

### Phase 1: Preparation (Orchestrator performs directly)

1. Extract from user input:
    - **Service Name**: Company/service name
    - **Service Type**: SaaS, e-commerce, content platform, community, etc.
    - **Service Region**: Domestic, global (including EU or not)
    - **Payment**: Paid/free/freemium (in-app purchases, subscriptions)
    - **Personal Data Collected** (optional): List of data collected
    - **Existing Materials** (optional): Current terms, privacy policy, etc.
2. Create `_workspace/` directory in the project root
3. Organize input and save to `_workspace/00_input.md`
4. **Determine execution mode** based on request scope

### Phase 2: Team Formation and Execution

| Order | Task | Owner | Depends On | Output |
|------|------|------|------|--------|
| 1a | Terms of Service | tos-specialist | None | `_workspace/01_terms_of_service.md` |
| 1b | Privacy Policy + Cookie Policy | privacy-specialist | None | `_workspace/02_privacy_policy.md`, `_workspace/03_cookie_policy.md` |
| 1c | Refund Policy + Copyright Notice | consumer-analyst | None | `_workspace/04_refund_policy.md`, `_workspace/05_copyright_notice.md` |
| 2 | Consistency Review | consistency-reviewer | Tasks 1a, 1b, 1c | `_workspace/06_review_report.md` |

Tasks 1a, 1b, and 1c are executed **in parallel**. All three agents can work independently. However, agents communicate with each other during work to ensure cross-document alignment.

**Inter-team Communication Flow:**
- tos-specialist ↔ privacy-specialist: Coordinate privacy-related terms clauses
- tos-specialist ↔ consumer-analyst: Coordinate refund, cancellation, and copyright clauses
- privacy-specialist ↔ consumer-analyst: Coordinate personal data processing during payment and refund
- consistency-reviewer cross-validates all outputs. If 🔴 critical issues are found, revision requests are sent to the relevant agent (maximum 2 times)

### Phase 3: Integration and Final Output

1. Verify all files in `_workspace/`
2. Confirm all 🔴 critical issues from the review report have been addressed
3. Report final summary to the user:
    - Terms of Service — `01_terms_of_service.md`
    - Privacy Policy — `02_privacy_policy.md`
    - Cookie Policy — `03_cookie_policy.md`
    - Refund Policy — `04_refund_policy.md`
    - Copyright Notice — `05_copyright_notice.md`
    - Review Report — `06_review_report.md`

## Deliverables

## Extension Skills
- **Cross Document Linker**: Cross Document Linker — Legal Document Cross-Reference & Consistency Management
- **Unfair Terms Detector**: Unfair Terms Detector — Detection & Revision Tool

## Error Handling

| Error Type | Strategy |
|----------|------|
| Insufficient service information | Draft based on general online service standards, note "service customization required" |
| Agent failure | 1 retry → if still failing, proceed without that document and note the omission in the review report |
| 🔴 issues found in review | Send revision request to relevant agent → rework → re-review (maximum 2 times) |
| Cross-document contradictions found | consistency-reviewer proposes resolution direction, simultaneously requests revision from related agents |
| Unverified legal amendments | Note "latest law verification required", recommend legal counsel |
