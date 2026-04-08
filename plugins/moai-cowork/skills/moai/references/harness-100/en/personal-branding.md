# Personal Branding (65-personal-branding)

> MoAI-Cowork v0.1.3 Harness Reference

## Overview
A personal branding agent team harness.

## Expert Roles
- **cover-letter-writer**: Cover Letter Writing Specialist. Writes authentic yet strategic cover letters customized for target positions.
  - Customized Writing: Craft messages tailored to the target company and position
  - Storytelling: Weave experience and motivation into a single persuasive narrative
  - Korean-style Personal Statement: Structure around growth background, motivation, strengths, and aspirations following Korean hiring conventions
  - English Cover Letter: Apply the concise, direct Western cover letter format
  - Tone Adjustment: Select the appropriate tone for the company culture (startup/enterprise/multinational)
- **portfolio-designer**: Portfolio Designer. Curates key projects, designs the storytelling structure for each project, and plans the overall composition of the portfolio site/document.
  - Project Curation: Select 3-5 projects that best demonstrate core competencies
  - Case Study Design: Design a storytelling structure (Problem -> Process -> Solution -> Results) for each project
  - Visual Planning: Plan screenshots, diagrams, and before/after comparisons
  - Portfolio Structure: Design the overall flow — introduction, projects, skills, contact
  - Platform Recommendation: Recommend appropriate portfolio platforms by field (GitHub Pages, Notion, Behance, etc.)
- **positioning-strategist**: Positioning Strategist. Analyzes an individual's strengths, experience, and goals, and designs differentiation points and brand narratives for the target market.
  - Strength Analysis: Systematically organize the individual's skills, experience, achievements, and personality traits
  - Target Market Research: Analyze the target industry/role's requirements, trends, and competitive landscape
  - UVP Definition: Define a Unique Value Proposition — "the reason to choose me over others"
  - Brand Narrative Design: Weave career experiences and vision into a consistent story
  - Differentiation Strategy: Identify points of differentiation from competitors (other candidates)
- **profile-optimizer**: LinkedIn Profile Optimization Specialist. Maximizes search visibility and creates profile content that attracts recruiters.
  - Headline Optimization: Write a headline containing key search terms (120 characters)
  - About Section Writing: Write a compelling summary that conveys UVP and career story
  - Experience Optimization: Apply keyword-rich, achievement-focused descriptions for each position
  - Skills & Endorsements Strategy: Select and prioritize skills aligned with target roles
  - SSI Improvement: Provide guidance on activities that increase Social Selling Index
- **resume-writer**: Resume/CV Writing Specialist. Creates ATS-optimized, achievement-focused resumes that reflect the positioning strategy.
  - ATS Optimization: Maximize keyword match rates with target job descriptions
  - Achievement Quantification: Transform all experiences into "Action + Result + Impact" format
  - Format Design: Design clean, scannable layouts appropriate for the industry
  - Multi-version Management: Create tailored versions for different target positions
  - Format Adaptation: Produce both Korean and English resumes, adapting to cultural conventions

## Workflow
### Phase 1: Preparation (Performed Directly by Orchestrator)

1. Extract from user input:
    - **Career Information**: Current role, years of experience, key experiences
    - **Goals**: Desired position, target companies/industries
    - **Existing Materials** (optional): Current resume, portfolio, LinkedIn URL
    - **Request Scope** (optional): Full package or specific documents only
2. Create the `_workspace/` directory in the project root
3. Organize inputs and save to `_workspace/00_input.md`
4. If existing materials are provided, copy them to `_workspace/` and use as analysis basis
5. Determine the **execution mode** based on the scope of the request

### Phase 2: Team Assembly and Execution

| Order | Task | Owner | Dependencies | Deliverable |
|-------|------|-------|-------------|-------------|
| 1 | Positioning Strategy | positioning-strategist | None | `_workspace/01_positioning_brief.md` |
| 2a | Resume Writing | resume-writer | Task 1 | `_workspace/02_resume.md` |
| 2b | Portfolio Design | portfolio-designer | Task 1 | `_workspace/03_portfolio.md` |
| 3a | LinkedIn Profile | profile-optimizer | Tasks 1, 2a | `_workspace/04_linkedin_profile.md` |
| 3b | Cover Letter | cover-letter-writer | Tasks 1, 2a | `_workspace/05_cover_letter.md` |

Tasks 2a (resume) and 2b (portfolio) are executed **in parallel**.
Tasks 3a (LinkedIn) and 3b (cover letter) are executed **in parallel**.

**Inter-agent Communication Flow:**
- positioning-strategist completes -> Delivers UVP, keywords, and narrative to all agents
- resume-writer completes -> Delivers career descriptions to profile-optimizer; delivers key achievements to cover-letter-writer
- portfolio-designer completes -> Delivers featured items to profile-optimizer; delivers project achievements to cover-letter-writer
- Cross-verify **brand consistency** across all deliverables

### Phase 3: Integration and Final Deliverables

1. Review all files in `_workspace/`
2. Verify brand message consistency across deliverables:
    - Resume <-> LinkedIn career descriptions consistency
    - Portfolio <-> Resume project alignment
    - Cover letter <-> Positioning UVP reflection
3. Present the final summary to the user

## Deliverables


## Extension Skills
- **ats-optimizer**: A specialized skill that provides resume keyword strategies and formatting guidelines for passing ATS (Applicant Tracking Systems). Used by the resume-writer agent to create ATS-friendly resumes and maximize JD matching rates. Automatically applied in contexts such as 'ATS optimization', 'resume keywords', 'JD matching', 'resume format', 'applicant tracking system', 'application pass rate', etc. Note: Directly accessing ATS software (Workday, Greenhouse) or handling actual recruitment processes is outside the scope of this skill.
- **linkedin-seo**: A specialized skill that provides LinkedIn profile search optimization (SEO) strategies and section-by-section optimization guides. Used by the profile-optimizer agent to maximize LinkedIn profile search visibility and increase recruiter traffic. Automatically applied in contexts such as 'LinkedIn SEO', 'LinkedIn optimization', 'profile search', 'recruiter visibility', 'LinkedIn keywords', 'LinkedIn headline', etc. Note: Directly accessing the LinkedIn API or operating automated networking tools is outside the scope of this skill.
- **personal-branding**: A pipeline where an agent team systematically performs personal branding. Use this skill for requests such as 'write my resume,' 'personal branding,' 'CV writing,' 'create a portfolio,' 'optimize LinkedIn profile,' 'write a cover letter,' 'organize my career,' 'help with job preparation,' or 'prepare for a job change.' Note: job posting search, interview simulation, and salary negotiation coaching are outside the scope of this skill.

## Error Handling
| Error Type | Strategy |
|-----------|----------|
| Insufficient career information | Present a list of key questions; draft based on available info |
| Goal unspecified | Propose 3 positioning scenarios |
| Web search failure | Work based on general JD trend knowledge; note "limited market data" |
| Agent failure | Retry once; if still failing, proceed without that deliverable; note omission in report |
| Confidential career details | Apply number/company name abstraction guidelines |
