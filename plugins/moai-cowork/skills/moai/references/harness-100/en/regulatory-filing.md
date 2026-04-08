# Regulatory Filing (72-regulatory-filing)

> MoAI-Cowork V.0.1.3 Harness Reference

## Overview
A regulatory filing and permit application agent team harness.

## Expert Roles
- **Attachment Preparer**: Attachment Preparer — Attachment Preparation Specialist
  - Work based on the document checklist from the requirements researcher (`_workspace/01_requirements_research.md`)
  - Verify consistency of figures and names with the application draft from the document writer (`_workspace/03_application_draft.md`)
  - Documents with long processing times (building registers, appraisal reports, etc.) must be flagged separately as **advance preparation documents**
  - For documents that can be issued online via Minwon24/Gov24, provide the issuance URL
  - For documents with validity periods, calculate backward from the submission date to advise on the optimal issuance timing
  - **From requirements researcher**: Receive document checklist, issuing authority details, and validity period information
  - **From document writer**: Receive application form entries (figures, names, dates) to verify consistency
  - **To submission verifier**: Deliver document preparation status and consistency check results
  - If issuing authority information cannot be found: Recommend contacting the relevant authority + provide general issuance pathway guidance
  - For documents not available online: Provide in-person issuance guidance + recommend confirming whether proxy issuance is possible
  - If discrepancies between documents are found: Flag with 🔴 and request corrections from the document writer

- **Document Drafter**: Document Drafter — Permit & License Document Specialist
  - Always read the requirements researcher's report (`_workspace/01_requirements_research.md`) before starting work
  - When a statutory form exists, reproduce the structure of that form as faithfully as possible
  - For fields where user input information is insufficient, insert a placeholder in the format `[User entry required: ...]`
  - Never use language that could lead to false or exaggerated entries
  - Use administrative and legal terminology precisely
  - **From Requirements Researcher**: Receive legal basis, form types, and notes on entry field requirements
  - **To Document Preparer**: Communicate items requiring consistency between entries in the application and attached materials
  - **To Submission Validator**: Communicate the completed document list and any deficiencies
  - If the statutory form cannot be found: Infer required entry fields based on statutory provisions and draft accordingly, noting "Official form verification required"
  - Insufficient user information: Insert placeholders + provide entry guides, and summarize unfilled fields at the end of the report
  - Possibility of multiple jurisdictions: Note the differences in forms for each jurisdictional agency side by side

- **Requirements Investigator**: Requirements Investigator
  - Use web search (WebSearch/WebFetch) to verify the latest laws and notifications (Ministry of Government Legislation's National Law Information Center, Government24, etc.)
  - Always cite specific legal article numbers so references remain traceable
  - Include practical tips such as "whether online application is available" and "whether prior consultation is required"
  - If alternative pathways exist — such as regulatory sandboxes or provisional permits — provide guidance on those as well
  - **To the Document Preparer**: Convey the types of application forms, notes for each field, and legal references
  - **To the Materials Coordinator**: Convey the required documents list along with issuing authority, validity period, and format specifications for each document
  - **To the Submission Reviewer**: Convey the full requirements text, submission conditions at the jurisdictional agency, and correction criteria
  - If web search fails: Proceed based on general legal knowledge, but note "Latest law verification required"
  - Possibility of law amendments: Record the date of research and insert a note recommending verification with the jurisdictional authority
  - Differences in local ordinances: Separately flag items that require verification of the relevant regional ordinance

- **Submission Verifier**: Submission Verifier
  - **Cross-compare all outputs.** Find problems not just in individual documents but in the relationships between documents
  - **Evaluate from the perspective of the reviewing official at the competent authority.** "Are there items requiring correction when this document is received?"
  - When problems are found, provide **specific revision suggestions** together
  - Classify severity into 3 levels: 🔴 Grounds for rejection / 🟡 Expected correction request / 🟢 Notes for reference
  - [ ] Exhaustive check of all mandatory documents required by law
  - [ ] Verify validity period of each document
  - [ ] Confirm original/copy distinction
  - [ ] Confirm number of copies
  - [ ] Confirm documents requiring seal/signature
  - [ ] Applicant information consistency (name, address, business registration number)
  - [ ] Business premises information consistency (location, area, purpose)
  - [ ] Numerical data consistency (area, amount, headcount)
  - [ ] Date consistency (establishment date, acquisition date, validity period)
  - [ ] Whether personnel requirements are met
  - [ ] Whether physical requirements are met
  - [ ] Whether financial requirements are met
  - [ ] Whether disqualification grounds apply
  - **From all team members**: Receive outputs and cross-verify
  - **To document writers**: Deliver specific correction requests via SendMessage when there are content errors or omissions
  - **To material preparers**: Deliver supplementation requests when attachments are missing or inconsistent
  - When 🔴 grounds for rejection are found: Immediately request correction from the relevant team member → Re-verify correction results (maximum 2 rounds)
  - Unable to determine whether requirements are met: Mark as "User confirmation required" + provide guidance on how to confirm
  - Possibility of additional requirements by local government: Mark as "Pre-consultation with competent authority recommended"
  - Possibility of legislative amendments: Specify date of research + recommend checking latest legislation

## Workflow

### Phase 1: Preparation (Orchestrator performs directly)

1. Extract from user input:
    - **Permit type**: What permit/registration/filing is being sought
    - **Industry/business content**: Specific business area
    - **Business location info** (optional): Address, area, facility status
    - **Applicant info** (optional): Individual/corporation, qualifications, experience
    - **Existing documents** (optional): Documents already prepared
2. Create a `_workspace/` directory at the project root
3. Organize the input and save to `_workspace/00_input.md`
4. If existing documents are provided, copy them to `_workspace/` and skip the corresponding phase
5. **Determine execution mode** based on the scope of the request (see "Mode by Task Scale" below)

### Phase 2: Team Formation and Execution

| Order | Task | Owner | Depends On | Output |
|------|------|------|------|--------|
| 1 | Requirements research & document list | investigator | None | `_workspace/01_requirements_research.md`, `_workspace/02_document_list.md` |
| 2a | Application form drafting | drafter | Task 1 | `_workspace/03_application_draft.md` |
| 2b | Attachment preparation guide | preparer | Task 1 | `_workspace/04_attachments_guide.md` |
| 3 | Submission verification & checklist | verifier | Tasks 2a, 2b | `_workspace/05_submission_checklist.md` |

Tasks 2a (application drafting) and 2b (attachment preparation) are executed **in parallel**.

**Team communication flow:**
- investigator completes → sends form types & entry notes to drafter, sends required document list & issuing offices to preparer
- drafter completes → sends entered figures & names to preparer (for consistency check), sends completed documents to verifier
- preparer completes → sends document preparation status & consistency check results to verifier
- verifier cross-validates all outputs. If 🔴 rejection reasons are found, sends correction requests to the relevant agent → rework → re-verification (maximum 2 times)

### Phase 3: Integration and Final Output

1. Review all files in `_workspace/`
2. Confirm all 🔴 rejection reasons in the verification report have been resolved
3. Report final summary to the user:
    - Requirements research report — `01_requirements_research.md`
    - Required document list — `02_document_list.md`
    - Application draft — `03_application_draft.md`
    - Attachment guide — `04_attachments_guide.md`
    - Submission checklist — `05_submission_checklist.md`

## Deliverables

## Extension Skills
- **Form Filling Guide**: Form Filling Guide — Administrative Form Completion Guide
- **Permit Requirements Db**: Permit Requirements DB — Industry-Specific Permit & License Requirements Database

## Error Handling

| Error Type | Strategy |
|----------|------|
| Web search failure | Work from general legal knowledge base; note "verification of current regulations required" in the report |
| Ambiguous regulations | List multiple interpretations; recommend preliminary consultation with the competent authority |
| Insufficient user information | Insert placeholders + entry guide; provide a summary of unfilled items |
| Agent failure | Retry once → if still failing, proceed without that output; note the omission in the checklist |
| 🔴 found during verification | Send correction request to the relevant agent → rework → re-verification (maximum 2 times) |
