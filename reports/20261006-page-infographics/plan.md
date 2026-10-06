# 페이지별 인포그래픽 추가 계획

작성일: 2026년 10월 6일

171개 Markdown의 본문·제목·구조·기존 그림을 읽어 계획의 근거와 해시를 기록했다. 현재 사용 문서는 준비물, 작업 순서, 결과와 검토 기준을 비교했다. 반복 설명은 공통 문단과 페이지 고유 내용을 나누어 살폈다. 과거 릴리스는 당시 변경 기록을 보존한다.

## 제작 순서와 기준

1. 질문·설치·프로젝트·검토의 핵심 관계와 혼동을 설명한다.
2. 업무별 실습 42개와 역할 안내 17개에는 해당 본문에서 뽑은 자료·업무·검토·결과와 가상 예제를 넣는다.
3. 도움말과 고급 설정에는 계정·비용·연결·검증 범위의 비교도를 넣는다.
4. 같은 개념을 설명하는 페이지는 같은 그림을 재사용한다. 기존 개념도·실제 캡처가 충분한 페이지와 과거 변경 기록에는 새 그림을 중복해서 넣지 않는다.
5. SVG 원본으로 한글과 숫자를 정확히 조판하고 확대 시 읽을 수 있게 한다. 데스크톱은 두 열, 모바일은 큰 글자의 한 열로 같은 내용을 보여 준다. 실제 앱 화면과 구분하고 이미지 아래에 내용을 설명한다. 별도 생성 API는 사용하지 않는다.
6. XML·경로·본문 근거·배치·실제 브라우저 표시를 확인한다. 이 확인은 제품의 실제 연결·설치·업무 실행을 대신하지 않는다.
7. 각 문서에는 그림을 하나씩 넣고, 태그 목록의 요약에는 반복해서 나오지 않도록 요약 경계를 지정한다.

## 페이지별 결정

| 페이지 | 우선순위 | 결정 | 설명할 내용 | 그림 |
|---|---|---|---|---|
| _index.md | Low | 유지 | 기존 개념도·실제 캡처·관계도가 핵심 내용을 설명함 | /infographics/first-workflow-ko.png |
| advanced/_index.md | Medium | 추가 | 어떤 확인을 했는지 범위를 밝히기 | /infographics/pages/verification.svg |
| advanced/documentation.md | Medium | 추가 | 온라인 강의 한 페이지를 만드는 순서 | /infographics/pages/authoring.svg |
| advanced/plugins.md | Medium | 추가 | 설치부터 실행까지, 증거가 다릅니다 | /infographics/pages/install-states.svg |
| advanced/verification.md | Medium | 추가 | 어떤 확인을 했는지 범위를 밝히기 | /infographics/pages/verification.svg |
| cookbook/_index.md | Medium | 추가 | 결과물로 실습과 역할을 고르세요 | /infographics/pages/choose-recipe.svg |
| cookbook/automation-recipes.md | Medium | 추가 | 잘된 업무를 반복하는 순서 | /infographics/pages/reuse.svg |
| cookbook/best-practices.md | Medium | 추가 | 처음부터 내 업무 적용까지 | /infographics/pages/learning-path.svg |
| cookbook/blog-pipeline.md | Medium | 추가 | 블로그 파이프라인 한눈에 보기 | /infographics/pages/example-cookbook-blog-pipeline.svg |
| cookbook/business-plan.md | Medium | 추가 | 사업계획서 자동화 한눈에 보기 | /infographics/pages/example-cookbook-business-plan.svg |
| cookbook/contract-review.md | Medium | 추가 | 계약서 검토 리포트 한눈에 보기 | /infographics/pages/example-cookbook-contract-review.svg |
| cookbook/design/_index.md | Medium | 추가 | 결과물로 실습과 역할을 고르세요 | /infographics/pages/choose-recipe.svg |
| cookbook/design/presentation.md | Medium | 추가 | 프레젠테이션 디자인 원칙 한눈에 보기 | /infographics/pages/example-cookbook-design-presentation.svg |
| cookbook/guides/_index.md | Medium | 추가 | 결과물로 실습과 역할을 고르세요 | /infographics/pages/choose-recipe.svg |
| cookbook/guides/content-marketing.md | Medium | 추가 | 콘텐츠 마케팅 전략 한눈에 보기 | /infographics/pages/example-cookbook-guides-content-marketing.svg |
| cookbook/guides/contract-drafting.md | Medium | 추가 | 계약서 작성 가이드 한눈에 보기 | /infographics/pages/example-cookbook-guides-contract-drafting.svg |
| cookbook/guides/data-analysis.md | Medium | 추가 | 데이터 분석 가이드 한눈에 보기 | /infographics/pages/example-cookbook-guides-data-analysis.svg |
| cookbook/guides/data-visualization.md | Medium | 추가 | 시각화 최적화 원칙 한눈에 보기 | /infographics/pages/example-cookbook-guides-data-visualization.svg |
| cookbook/guides/funding.md | Medium | 추가 | 투자 유치 가이드 한눈에 보기 | /infographics/pages/example-cookbook-guides-funding.svg |
| cookbook/guides/legal-risk.md | Medium | 추가 | 법률 리스크 관리 한눈에 보기 | /infographics/pages/example-cookbook-guides-legal-risk.svg |
| cookbook/guides/social-media.md | Medium | 추가 | SNS 최적화 가이드 한눈에 보기 | /infographics/pages/example-cookbook-guides-social-media.svg |
| cookbook/ir-deck.md | Medium | 추가 | IR 덱 제작 한눈에 보기 | /infographics/pages/example-cookbook-ir-deck.svg |
| cookbook/legal-nda-batch.md | Medium | 추가 | NDA 일괄 검토 파이프라인 한눈에 보기 | /infographics/pages/example-cookbook-legal-nda-batch.svg |
| cookbook/projects/_index.md | Medium | 추가 | 내 프로젝트에 맞는 지침 만들기 | /infographics/pages/pm-setup.svg |
| cookbook/projects/brand-to-landing.md | Medium | 추가 | 브랜드에서 랜딩 페이지까지 한눈에 보기 | /infographics/pages/example-cookbook-projects-brand-to-landing.svg |
| cookbook/projects/career-transition-4weeks.md | Medium | 추가 | 이직 준비 프로젝트 한눈에 보기 | /infographics/pages/example-cookbook-projects-career-transition-4weeks.svg |
| cookbook/projects/contract-risk-report.md | Medium | 추가 | 계약서 검토와 리스크 보고 한눈에 보기 | /infographics/pages/example-cookbook-projects-contract-risk-report.svg |
| cookbook/projects/gov-grant-application.md | Medium | 추가 | 정부 지원사업 신청서 완성하기 한눈에 보기 | /infographics/pages/example-cookbook-projects-gov-grant-application.svg |
| cookbook/projects/hiring-pipeline.md | Medium | 추가 | 채용 공고부터 오퍼레터까지 한눈에 보기 | /infographics/pages/example-cookbook-projects-hiring-pipeline.svg |
| cookbook/projects/public-data-report.md | Medium | 추가 | 공공데이터로 시장 보고서 만들기 한눈에 보기 | /infographics/pages/example-cookbook-projects-public-data-report.svg |
| cookbook/projects/smartstore-launch.md | Medium | 추가 | 스마트스토어 신제품 런칭하기 한눈에 보기 | /infographics/pages/example-cookbook-projects-smartstore-launch.svg |
| cookbook/projects/sns-content-month.md | Medium | 추가 | 한 달치 SNS 콘텐츠 캘린더 만들기 한눈에 보기 | /infographics/pages/example-cookbook-projects-sns-content-month.svg |
| cookbook/projects/startup-feasibility.md | Medium | 추가 | 상권분석으로 창업 타당성 검증하기 한눈에 보기 | /infographics/pages/example-cookbook-projects-startup-feasibility.svg |
| cookbook/projects/voc-to-faq.md | Medium | 추가 | VOC 분석으로 FAQ 지식베이스 구축하기 한눈에 보기 | /infographics/pages/example-cookbook-projects-voc-to-faq.svg |
| cookbook/projects/webnovel-project.md | Medium | 추가 | 웹소설 기획부터 연재·표지까지 한눈에 보기 | /infographics/pages/example-cookbook-projects-webnovel-project.svg |
| cookbook/projects/weekly-report-routine.md | Medium | 추가 | 주간보고 자동화 루틴 만들기 한눈에 보기 | /infographics/pages/example-cookbook-projects-weekly-report-routine.svg |
| cookbook/report-automation.md | Medium | 추가 | 주간 보고서 자동화 한눈에 보기 | /infographics/pages/example-cookbook-report-automation.svg |
| cookbook/skill-chaining.md | Medium | 추가 | 다음 담당자에게 전달할 네 묶음 | /infographics/pages/team-handoff.svg |
| cookbook/templates/_index.md | Medium | 추가 | Office 작업의 세 가지 방식 | /infographics/pages/office.svg |
| cookbook/templates/compliance.md | Medium | 추가 | 컴플라이언스 체크리스트 한눈에 보기 | /infographics/pages/example-cookbook-templates-compliance.svg |
| cookbook/templates/email.md | Medium | 추가 | 이메일 마케팅 템플릿 한눈에 보기 | /infographics/pages/example-cookbook-templates-email.svg |
| cookbook/templates/excel.md | Medium | 추가 | 엑셀 고급 기법 한눈에 보기 | /infographics/pages/example-cookbook-templates-excel.svg |
| cookbook/templates/financial.md | Medium | 추가 | 재무 모델링 템플릿 한눈에 보기 | /infographics/pages/example-cookbook-templates-financial.svg |
| cookbook/tracks/_index.md | Medium | 추가 | 결과물로 실습과 역할을 고르세요 | /infographics/pages/choose-recipe.svg |
| cookbook/tracks/track-advertising.md | Medium | 추가 | 광고 트랙 한눈에 보기 | /infographics/pages/example-cookbook-tracks-track-advertising.svg |
| cookbook/tracks/track-appendix.md | Medium | 추가 | 부록 트랙 한눈에 보기 | /infographics/pages/example-cookbook-tracks-track-appendix.svg |
| cookbook/tracks/track-commerce.md | Medium | 추가 | 이커머스 트랙 한눈에 보기 | /infographics/pages/example-cookbook-tracks-track-commerce.svg |
| cookbook/tracks/track-content.md | Medium | 추가 | 콘텐츠 트랙 한눈에 보기 | /infographics/pages/example-cookbook-tracks-track-content.svg |
| cookbook/tracks/track-data.md | Medium | 추가 | 데이터 트랙 한눈에 보기 | /infographics/pages/example-cookbook-tracks-track-data.svg |
| cookbook/tracks/track-documents.md | Medium | 추가 | 문서 트랙 한눈에 보기 | /infographics/pages/example-cookbook-tracks-track-documents.svg |
| cookbook/tracks/track-finance.md | Medium | 추가 | 재무 트랙 한눈에 보기 | /infographics/pages/example-cookbook-tracks-track-finance.svg |
| cookbook/tracks/track-hr.md | Medium | 추가 | HR·커리어 트랙 한눈에 보기 | /infographics/pages/example-cookbook-tracks-track-hr.svg |
| cookbook/tracks/track-legal.md | Medium | 추가 | 법률 트랙 한눈에 보기 | /infographics/pages/example-cookbook-tracks-track-legal.svg |
| cookbook/tracks/track-marketing.md | Medium | 추가 | 마케팅 트랙 한눈에 보기 | /infographics/pages/example-cookbook-tracks-track-marketing.svg |
| cookbook/tracks/track-operations.md | Medium | 추가 | 운영 트랙 한눈에 보기 | /infographics/pages/example-cookbook-tracks-track-operations.svg |
| cookbook/tracks/track-product.md | Medium | 추가 | 제품 개발 트랙 한눈에 보기 | /infographics/pages/example-cookbook-tracks-track-product.svg |
| cookbook/troubleshooting.md | Medium | 추가 | 멈춘 단계를 찾고 그 부분부터 확인 | /infographics/pages/troubleshooting.svg |
| getting-started/_index.md | High | 추가 | 처음부터 내 업무 적용까지 | /infographics/pages/learning-path.svg |
| getting-started/choose-app.md | High | 추가 | 앱 이름보다 실제 접근 범위 확인 | /infographics/pages/environment.svg |
| getting-started/concepts.md | Low | 유지 | 기존 개념도·실제 캡처·관계도가 핵심 내용을 설명함 | /infographics/project-concepts-ko.png |
| getting-started/first-task.md | High | 추가 | 같은 숫자라도 상태가 다릅니다 | /infographics/pages/report-status.svg |
| getting-started/install.md | Low | 유지 | 기존 개념도·실제 캡처·관계도가 핵심 내용을 설명함 | /screenshots/20261005/chatgpt-web-start.jpg · /screenshots/20261005/claude-cowork-start.jpg |
| getting-started/projects.md | Low | 유지 | 기존 개념도·실제 캡처·관계도가 핵심 내용을 설명함 | /infographics/project-context-ko.png |
| getting-started/questions.md | High | 추가 | 질문을 받았을 때 이렇게 답하세요 | /infographics/pages/questions.svg |
| getting-started/quick-start.md | Low | 유지 | 기존 개념도·실제 캡처·관계도가 핵심 내용을 설명함 | /infographics/first-workflow-ko.png |
| help/_index.md | Medium | 추가 | 멈춘 단계를 찾고 그 부분부터 확인 | /infographics/pages/troubleshooting.svg |
| help/about-claude.md | Medium | 추가 | 앱 이름보다 실제 접근 범위 확인 | /infographics/pages/environment.svg |
| help/account.md | Medium | 추가 | 세 가지 계정 범위를 나눠 보세요 | /infographics/pages/account.svg |
| help/attribution.md | Medium | 추가 | 출처와 권리를 함께 남기세요 | /infographics/pages/attribution.svg |
| help/conversations.md | Medium | 추가 | 새 작업에 넘길 맥락은 직접 남기기 | /infographics/pages/handoff.svg |
| help/office/_index.md | Medium | 추가 | Office 작업의 세 가지 방식 | /infographics/pages/office.svg |
| help/office/microsoft-365.md | Medium | 추가 | Office 작업의 세 가지 방식 | /infographics/pages/office.svg |
| help/personalization.md | Medium | 추가 | 기준마다 저장할 곳이 다릅니다 | /infographics/pages/personalization.svg |
| help/plans-billing.md | Medium | 추가 | 무료 패키지와 서비스 비용은 별개 | /infographics/pages/cost.svg |
| help/source-index.md | Medium | 추가 | 처음부터 내 업무 적용까지 | /infographics/pages/learning-path.svg |
| help/troubleshooting.md | Medium | 추가 | 멈춘 단계를 찾고 그 부분부터 확인 | /infographics/pages/troubleshooting.svg |
| help/usage-limits.md | Medium | 추가 | 큰 작업을 확인 가능한 단위로 나누기 | /infographics/pages/limits.svg |
| learn/01-delegation.md | Low | 유지 | 기존 개념도·실제 캡처·관계도가 핵심 내용을 설명함 | /infographics/project-concepts-ko.png |
| learn/02-project-context.md | Low | 유지 | 기존 개념도·실제 캡처·관계도가 핵심 내용을 설명함 | /infographics/project-context-ko.png |
| learn/03-first-result.md | High | 추가 | 같은 숫자라도 상태가 다릅니다 | /infographics/pages/report-status.svg |
| learn/04-skills-plugins.md | High | 추가 | 설치부터 실행까지, 증거가 다릅니다 | /infographics/pages/install-states.svg |
| learn/05-expert-workflow.md | Low | 유지 | 기존 개념도·실제 캡처·관계도가 핵심 내용을 설명함 | /infographics/expert-workflow-ko.png |
| learn/06-review-reuse.md | High | 추가 | 잘된 업무를 반복하는 순서 | /infographics/pages/reuse.svg |
| learn/_index.md | Low | 유지 | 기존 개념도·실제 캡처·관계도가 핵심 내용을 설명함 | /infographics/first-workflow-ko.png |
| learn/screens.md | Low | 유지 | 기존 개념도·실제 캡처·관계도가 핵심 내용을 설명함 | /screenshots/20261005/chatgpt-web-start.jpg · /screenshots/20261005/claude-cowork-start.jpg · /screenshots/20261005/chatgpt-plugins.jpg · /screenshots/20261005/claude-plugins.jpg |
| learn/teaching-guide.md | High | 추가 | 설명에서 직접 수행까지 이어지는 수업 | /infographics/pages/teaching.svg |
| moai-agents/_index.md | Medium | 추가 | 결과물로 실습과 역할을 고르세요 | /infographics/pages/choose-recipe.svg |
| moai-agents/accountant.md | Medium | 추가 | 재무·세무 담당 한눈에 보기 | /infographics/pages/example-moai-agents-accountant.svg |
| moai-agents/analyst.md | Medium | 추가 | 데이터 애널리스트 한눈에 보기 | /infographics/pages/example-moai-agents-analyst.svg |
| moai-agents/career.md | Medium | 추가 | 커리어코치 한눈에 보기 | /infographics/pages/example-moai-agents-career.svg |
| moai-agents/consultant.md | Medium | 추가 | 컨설턴트 한눈에 보기 | /infographics/pages/example-moai-agents-consultant.svg |
| moai-agents/coworker.md | Medium | 추가 | 코워커 한눈에 보기 | /infographics/pages/example-moai-agents-coworker.svg |
| moai-agents/cs.md | Medium | 추가 | CS매니저 한눈에 보기 | /infographics/pages/example-moai-agents-cs.svg |
| moai-agents/designer.md | Medium | 추가 | 디자이너 한눈에 보기 | /infographics/pages/example-moai-agents-designer.svg |
| moai-agents/lawyer.md | Medium | 추가 | 법무 담당 한눈에 보기 | /infographics/pages/example-moai-agents-lawyer.svg |
| moai-agents/marketer.md | Medium | 추가 | 마케터 한눈에 보기 | /infographics/pages/example-moai-agents-marketer.svg |
| moai-agents/media.md | Medium | 추가 | 미디어 크리에이터 한눈에 보기 | /infographics/pages/example-moai-agents-media.svg |
| moai-agents/officer.md | Medium | 추가 | 사무관 한눈에 보기 | /infographics/pages/example-moai-agents-officer.svg |
| moai-agents/pm.md | Medium | 추가 | 내 프로젝트에 맞는 지침 만들기 | /infographics/pages/pm-setup.svg |
| moai-agents/recruiter.md | Medium | 추가 | 인사·채용 담당 한눈에 보기 | /infographics/pages/example-moai-agents-recruiter.svg |
| moai-agents/seller.md | Medium | 추가 | 셀러 한눈에 보기 | /infographics/pages/example-moai-agents-seller.svg |
| moai-agents/story.md | Medium | 추가 | 스토리 크리에이터 한눈에 보기 | /infographics/pages/example-moai-agents-story.svg |
| moai-agents/threads-poster.md | Medium | 추가 | SNS 크리에이터 한눈에 보기 | /infographics/pages/example-moai-agents-threads-poster.svg |
| moai-agents/tutor.md | Medium | 추가 | 튜터 한눈에 보기 | /infographics/pages/example-moai-agents-tutor.svg |
| moai-agents/writer.md | Medium | 추가 | 작가 한눈에 보기 | /infographics/pages/example-moai-agents-writer.svg |
| plugins/_index.md | High | 추가 | 결과물로 실습과 역할을 고르세요 | /infographics/pages/choose-recipe.svg |
| plugins/agents.md | High | 추가 | 업무 방법과 실행 역할을 구분 | /infographics/pages/skills-agents.svg |
| plugins/higgsfield-setup.md | High | 추가 | 생성 도구 연결과 제작을 분리 | /infographics/pages/higgsfield.svg |
| plugins/install.md | Low | 유지 | 기존 개념도·실제 캡처·관계도가 핵심 내용을 설명함 | /screenshots/20261005/chatgpt-plugins.jpg · /screenshots/20261005/claude-plugins.jpg |
| plugins/license.md | Low | 추가하지 않음 | 과거 변경 기록 또는 권리·고지 원문과 표를 보존하고 현재 기능 그림을 섞지 않음 |  |
| plugins/mcp/_index.md | High | 추가 | MCP: 실행 위치와 연결 방식을 따로 확인 | /infographics/pages/server-modes.svg |
| plugins/mcp/credentials.md | High | 추가 | 계정별 인증 정보와 조회를 분리 | /infographics/pages/credentials.svg |
| plugins/mcp/install.md | High | 추가 | 외부 연결을 확인하는 네 단계 | /infographics/pages/connector.svg |
| plugins/mcp/troubleshooting.md | High | 추가 | 멈춘 단계를 찾고 그 부분부터 확인 | /infographics/pages/troubleshooting.svg |
| plugins/open-source.md | Low | 추가하지 않음 | 과거 변경 기록 또는 권리·고지 원문과 표를 보존하고 현재 기능 그림을 섞지 않음 |  |
| plugins/teams.md | High | 추가 | 다음 담당자에게 전달할 네 묶음 | /infographics/pages/team-handoff.svg |
| releases/_index.md | Low | 유지 | 기존 개념도·실제 캡처·관계도가 핵심 내용을 설명함 | 기존 Mermaid 버전 관계도 |
| releases/archive/_index.md | Low | 추가하지 않음 | 과거 변경 기록 또는 권리·고지 원문과 표를 보존하고 현재 기능 그림을 섞지 않음 |  |
| releases/archive/v1.0.md | Low | 추가하지 않음 | 과거 변경 기록 또는 권리·고지 원문과 표를 보존하고 현재 기능 그림을 섞지 않음 |  |
| releases/archive/v1.2.md | Low | 추가하지 않음 | 과거 변경 기록 또는 권리·고지 원문과 표를 보존하고 현재 기능 그림을 섞지 않음 |  |
| releases/archive/v1.3.md | Low | 추가하지 않음 | 과거 변경 기록 또는 권리·고지 원문과 표를 보존하고 현재 기능 그림을 섞지 않음 |  |
| releases/archive/v1.5.md | Low | 추가하지 않음 | 과거 변경 기록 또는 권리·고지 원문과 표를 보존하고 현재 기능 그림을 섞지 않음 |  |
| releases/archive/v1.6.md | Low | 추가하지 않음 | 과거 변경 기록 또는 권리·고지 원문과 표를 보존하고 현재 기능 그림을 섞지 않음 |  |
| releases/archive/v2.0.md | Low | 추가하지 않음 | 과거 변경 기록 또는 권리·고지 원문과 표를 보존하고 현재 기능 그림을 섞지 않음 |  |
| releases/archive/v2.1.md | Low | 추가하지 않음 | 과거 변경 기록 또는 권리·고지 원문과 표를 보존하고 현재 기능 그림을 섞지 않음 |  |
| releases/archive/v2.10.md | Low | 추가하지 않음 | 과거 변경 기록 또는 권리·고지 원문과 표를 보존하고 현재 기능 그림을 섞지 않음 |  |
| releases/archive/v2.11.1.md | Low | 추가하지 않음 | 과거 변경 기록 또는 권리·고지 원문과 표를 보존하고 현재 기능 그림을 섞지 않음 |  |
| releases/archive/v2.11.md | Low | 추가하지 않음 | 과거 변경 기록 또는 권리·고지 원문과 표를 보존하고 현재 기능 그림을 섞지 않음 |  |
| releases/archive/v2.12.1.md | Low | 추가하지 않음 | 과거 변경 기록 또는 권리·고지 원문과 표를 보존하고 현재 기능 그림을 섞지 않음 |  |
| releases/archive/v2.12.2.md | Low | 추가하지 않음 | 과거 변경 기록 또는 권리·고지 원문과 표를 보존하고 현재 기능 그림을 섞지 않음 |  |
| releases/archive/v2.12.3.md | Low | 추가하지 않음 | 과거 변경 기록 또는 권리·고지 원문과 표를 보존하고 현재 기능 그림을 섞지 않음 |  |
| releases/archive/v2.12.md | Low | 추가하지 않음 | 과거 변경 기록 또는 권리·고지 원문과 표를 보존하고 현재 기능 그림을 섞지 않음 |  |
| releases/archive/v2.13.md | Low | 추가하지 않음 | 과거 변경 기록 또는 권리·고지 원문과 표를 보존하고 현재 기능 그림을 섞지 않음 |  |
| releases/archive/v2.14.md | Low | 추가하지 않음 | 과거 변경 기록 또는 권리·고지 원문과 표를 보존하고 현재 기능 그림을 섞지 않음 |  |
| releases/archive/v2.15.md | Low | 추가하지 않음 | 과거 변경 기록 또는 권리·고지 원문과 표를 보존하고 현재 기능 그림을 섞지 않음 |  |
| releases/archive/v2.16.md | Low | 추가하지 않음 | 과거 변경 기록 또는 권리·고지 원문과 표를 보존하고 현재 기능 그림을 섞지 않음 |  |
| releases/archive/v2.17.md | Low | 추가하지 않음 | 과거 변경 기록 또는 권리·고지 원문과 표를 보존하고 현재 기능 그림을 섞지 않음 |  |
| releases/archive/v2.18.md | Low | 추가하지 않음 | 과거 변경 기록 또는 권리·고지 원문과 표를 보존하고 현재 기능 그림을 섞지 않음 |  |
| releases/archive/v2.19.md | Low | 추가하지 않음 | 과거 변경 기록 또는 권리·고지 원문과 표를 보존하고 현재 기능 그림을 섞지 않음 |  |
| releases/archive/v2.2.md | Low | 추가하지 않음 | 과거 변경 기록 또는 권리·고지 원문과 표를 보존하고 현재 기능 그림을 섞지 않음 |  |
| releases/archive/v2.20.md | Low | 추가하지 않음 | 과거 변경 기록 또는 권리·고지 원문과 표를 보존하고 현재 기능 그림을 섞지 않음 |  |
| releases/archive/v2.21.md | Low | 추가하지 않음 | 과거 변경 기록 또는 권리·고지 원문과 표를 보존하고 현재 기능 그림을 섞지 않음 |  |
| releases/archive/v2.22.md | Low | 추가하지 않음 | 과거 변경 기록 또는 권리·고지 원문과 표를 보존하고 현재 기능 그림을 섞지 않음 |  |
| releases/archive/v2.23.md | Low | 추가하지 않음 | 과거 변경 기록 또는 권리·고지 원문과 표를 보존하고 현재 기능 그림을 섞지 않음 |  |
| releases/archive/v2.24.md | Low | 추가하지 않음 | 과거 변경 기록 또는 권리·고지 원문과 표를 보존하고 현재 기능 그림을 섞지 않음 |  |
| releases/archive/v2.25.md | Low | 추가하지 않음 | 과거 변경 기록 또는 권리·고지 원문과 표를 보존하고 현재 기능 그림을 섞지 않음 |  |
| releases/archive/v2.26.md | Low | 추가하지 않음 | 과거 변경 기록 또는 권리·고지 원문과 표를 보존하고 현재 기능 그림을 섞지 않음 |  |
| releases/archive/v2.27.md | Low | 추가하지 않음 | 과거 변경 기록 또는 권리·고지 원문과 표를 보존하고 현재 기능 그림을 섞지 않음 |  |
| releases/archive/v2.3.md | Low | 추가하지 않음 | 과거 변경 기록 또는 권리·고지 원문과 표를 보존하고 현재 기능 그림을 섞지 않음 |  |
| releases/archive/v2.4.md | Low | 추가하지 않음 | 과거 변경 기록 또는 권리·고지 원문과 표를 보존하고 현재 기능 그림을 섞지 않음 |  |
| releases/archive/v2.5.md | Low | 추가하지 않음 | 과거 변경 기록 또는 권리·고지 원문과 표를 보존하고 현재 기능 그림을 섞지 않음 |  |
| releases/archive/v2.6.md | Low | 추가하지 않음 | 과거 변경 기록 또는 권리·고지 원문과 표를 보존하고 현재 기능 그림을 섞지 않음 |  |
| releases/archive/v2.7.md | Low | 추가하지 않음 | 과거 변경 기록 또는 권리·고지 원문과 표를 보존하고 현재 기능 그림을 섞지 않음 |  |
| releases/archive/v2.8.md | Low | 추가하지 않음 | 과거 변경 기록 또는 권리·고지 원문과 표를 보존하고 현재 기능 그림을 섞지 않음 |  |
| releases/archive/v2.9.md | Low | 추가하지 않음 | 과거 변경 기록 또는 권리·고지 원문과 표를 보존하고 현재 기능 그림을 섞지 않음 |  |
| releases/docs-20261005.md | Low | 추가하지 않음 | 과거 변경 기록 또는 권리·고지 원문과 표를 보존하고 현재 기능 그림을 섞지 않음 |  |
| releases/v1.0.0.md | Low | 추가하지 않음 | 과거 변경 기록 또는 권리·고지 원문과 표를 보존하고 현재 기능 그림을 섞지 않음 |  |
| releases/v1.1.0.md | Low | 추가하지 않음 | 과거 변경 기록 또는 권리·고지 원문과 표를 보존하고 현재 기능 그림을 섞지 않음 |  |
| releases/v1.2.0.md | Low | 추가하지 않음 | 과거 변경 기록 또는 권리·고지 원문과 표를 보존하고 현재 기능 그림을 섞지 않음 |  |
| releases/v1.2.1.md | Low | 추가하지 않음 | 과거 변경 기록 또는 권리·고지 원문과 표를 보존하고 현재 기능 그림을 섞지 않음 |  |
| releases/v1.2.2.md | Low | 추가하지 않음 | 과거 변경 기록 또는 권리·고지 원문과 표를 보존하고 현재 기능 그림을 섞지 않음 |  |
| releases/v1.2.3.md | Low | 추가하지 않음 | 과거 변경 기록 또는 권리·고지 원문과 표를 보존하고 현재 기능 그림을 섞지 않음 |  |
| releases/v1.2.4.md | Low | 추가하지 않음 | 과거 변경 기록 또는 권리·고지 원문과 표를 보존하고 현재 기능 그림을 섞지 않음 |  |
| releases/v1.2.5.md | Low | 추가하지 않음 | 과거 변경 기록 또는 권리·고지 원문과 표를 보존하고 현재 기능 그림을 섞지 않음 |  |
| releases/v1.2.6.md | Low | 추가하지 않음 | 과거 변경 기록 또는 권리·고지 원문과 표를 보존하고 현재 기능 그림을 섞지 않음 |  |
| workflows/_index.md | High | 추가 | 내 프로젝트에 맞는 지침 만들기 | /infographics/pages/pm-setup.svg |
| workflows/experts.md | Low | 유지 | 기존 개념도·실제 캡처·관계도가 핵심 내용을 설명함 | /infographics/expert-workflow-ko.png |
| workflows/first-project.md | High | 추가 | 내 프로젝트에 맞는 지침 만들기 | /infographics/pages/pm-setup.svg |
| workflows/permissions.md | High | 추가 | 원본에서 결과까지 접근을 확인 | /infographics/pages/permissions.svg |
| workflows/reuse.md | High | 추가 | 잘된 업무를 반복하는 순서 | /infographics/pages/reuse.svg |
| workflows/review.md | High | 추가 | 완료 보고보다 결과물을 확인하세요 | /infographics/pages/review.svg |
