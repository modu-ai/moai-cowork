# 인포그래픽 재표현 계획

원본을 일괄 변경하기 전 검토할 계획이다. 같은 개념의 PC·모바일 파일은 한 묶음으로 센다.

| 개념 | 제안 | 이유 | 사용 페이지 |
|---|---|---|---|
| 처음부터 내 업무 적용까지 | HTML 본문 통합 | 짧은 정의·비교·단순 순서는 기존 본문의 표·목록으로 통합하고 중복 그림을 제거한다. | www/content/cookbook/best-practices.md<br>www/content/getting-started/_index.md<br>www/content/help/source-index.md |
| 앱 이름보다 실제 접근 범위 확인 | HTML 본문 통합 | 짧은 정의·비교·단순 순서는 기존 본문의 표·목록으로 통합하고 중복 그림을 제거한다. | www/content/getting-started/choose-app.md<br>www/content/help/about-claude.md |
| 질문을 받았을 때 이렇게 답하세요 | Mermaid 분기 | 필수 맥락이 없을 때 보류하고 질문하는 분기와 독립 작업 경로를 표시한다. | www/content/getting-started/questions.md |
| 같은 숫자라도 상태가 다릅니다 | HTML 본문 통합 | 짧은 정의·비교·단순 순서는 기존 본문의 표·목록으로 통합하고 중복 그림을 제거한다. | www/content/getting-started/first-task.md<br>www/content/learn/03-first-result.md |
| 설치부터 실행까지, 증거가 다릅니다 | HTML 본문 통합 | 짧은 정의·비교·단순 순서는 기존 본문의 표·목록으로 통합하고 중복 그림을 제거한다. | www/content/advanced/plugins.md<br>www/content/learn/04-skills-plugins.md |
| 내 프로젝트에 맞는 지침 만들기 | Mermaid 흐름 | 질문 → 역할·스킬 매핑 → 지침 저장 → 실제 참조 확인의 의존 관계를 표시한다. | www/content/cookbook/projects/_index.md<br>www/content/moai-agents/pm.md<br>www/content/workflows/_index.md<br>www/content/workflows/first-project.md |
| 완료 보고보다 결과물을 확인하세요 | HTML 본문 통합 | 짧은 정의·비교·단순 순서는 기존 본문의 표·목록으로 통합하고 중복 그림을 제거한다. | www/content/workflows/review.md |
| 잘된 업무를 반복하는 순서 | Mermaid 순환 | 검토 결과를 지침에 반영하고 다시 실행하는 반복 경로를 표시한다. | www/content/cookbook/automation-recipes.md<br>www/content/learn/06-review-reuse.md<br>www/content/workflows/reuse.md |
| 원본에서 결과까지 접근을 확인 | Mermaid 관계 | 프로젝트와 허용한 폴더의 경계, 읽기와 별도 결과 저장을 표시한다. | www/content/workflows/permissions.md |
| 세 가지 계정 범위를 나눠 보세요 | HTML 본문 통합 | 짧은 정의·비교·단순 순서는 기존 본문의 표·목록으로 통합하고 중복 그림을 제거한다. | www/content/help/account.md |
| 무료 패키지와 서비스 비용은 별개 | HTML 본문 통합 | 짧은 정의·비교·단순 순서는 기존 본문의 표·목록으로 통합하고 중복 그림을 제거한다. | www/content/help/plans-billing.md |
| 새 작업에 넘길 맥락은 직접 남기기 | Mermaid 인계 | 이전 작업의 결과·미정 항목이 다음 작업의 입력이 되는 인계를 표시한다. | www/content/help/conversations.md |
| 기준마다 저장할 곳이 다릅니다 | HTML 본문 통합 | 짧은 정의·비교·단순 순서는 기존 본문의 표·목록으로 통합하고 중복 그림을 제거한다. | www/content/help/personalization.md |
| 출처와 권리를 함께 남기세요 | HTML 본문 통합 | 짧은 정의·비교·단순 순서는 기존 본문의 표·목록으로 통합하고 중복 그림을 제거한다. | www/content/help/attribution.md |
| Office 작업의 세 가지 방식 | HTML 본문 통합 | 짧은 정의·비교·단순 순서는 기존 본문의 표·목록으로 통합하고 중복 그림을 제거한다. | www/content/cookbook/templates/_index.md<br>www/content/help/office/_index.md<br>www/content/help/office/microsoft-365.md |
| 큰 작업을 확인 가능한 단위로 나누기 | Mermaid 분기·합류 | 작업을 분리하되 선행 결과가 필요한 작업은 합류 뒤에 시작하도록 표시한다. | www/content/help/usage-limits.md |
| 멈춘 단계를 찾고 그 부분부터 확인 | Mermaid 분기 | 설치·노출·인증·실행 중 어느 단계가 막혔는지 조건별로 표시한다. | www/content/cookbook/troubleshooting.md<br>www/content/help/_index.md<br>www/content/help/troubleshooting.md<br>www/content/plugins/mcp/troubleshooting.md |
| 계정별 인증 정보와 조회를 분리 | Mermaid 관계 | 사용자·서비스·인증 저장 범위의 대응 관계를 표시한다. 비밀 값은 넣지 않는다. | www/content/plugins/mcp/credentials.md |
| MCP: 실행 위치와 연결 방식을 따로 확인 | Mermaid 관계 | 실행 위치와 연결 방식을 서로 다른 축으로 표시한다. | www/content/plugins/mcp/_index.md |
| 외부 연결을 확인하는 네 단계 | HTML 본문 통합 | 짧은 정의·비교·단순 순서는 기존 본문의 표·목록으로 통합하고 중복 그림을 제거한다. | www/content/plugins/mcp/install.md |
| 업무 방법과 실행 역할을 구분 | HTML 본문 통합 | 짧은 정의·비교·단순 순서는 기존 본문의 표·목록으로 통합하고 중복 그림을 제거한다. | www/content/plugins/agents.md |
| 다음 담당자에게 전달할 네 묶음 | HTML 본문 통합 | 짧은 정의·비교·단순 순서는 기존 본문의 표·목록으로 통합하고 중복 그림을 제거한다. | www/content/cookbook/skill-chaining.md<br>www/content/plugins/teams.md |
| 어떤 확인을 했는지 범위를 밝히기 | HTML 본문 통합 | 짧은 정의·비교·단순 순서는 기존 본문의 표·목록으로 통합하고 중복 그림을 제거한다. | www/content/advanced/_index.md<br>www/content/advanced/verification.md |
| 온라인 강의 한 페이지를 만드는 순서 | HTML 본문 통합 | 짧은 정의·비교·단순 순서는 기존 본문의 표·목록으로 통합하고 중복 그림을 제거한다. | www/content/advanced/documentation.md |
| 설명에서 직접 수행까지 이어지는 수업 | HTML 본문 통합 | 짧은 정의·비교·단순 순서는 기존 본문의 표·목록으로 통합하고 중복 그림을 제거한다. | www/content/learn/teaching-guide.md |
| 결과물로 실습과 역할을 고르세요 | HTML 본문 통합 | 짧은 정의·비교·단순 순서는 기존 본문의 표·목록으로 통합하고 중복 그림을 제거한다. | www/content/cookbook/_index.md<br>www/content/cookbook/design/_index.md<br>www/content/cookbook/guides/_index.md<br>www/content/cookbook/tracks/_index.md<br>www/content/moai-agents/_index.md<br>www/content/plugins/_index.md |
| 생성 도구 연결과 제작을 분리 | HTML 본문 통합 | 짧은 정의·비교·단순 순서는 기존 본문의 표·목록으로 통합하고 중복 그림을 제거한다. | www/content/plugins/higgsfield-setup.md |
| 블로그 파이프라인 한눈에 보기 | HTML 본문 통합 | 준비 자료·작업·검토·결과 설명과 예제는 선택·복사 가능한 본문으로 통합하고 중복 그림을 제거한다. | www/content/cookbook/blog-pipeline.md |
| 사업계획서 자동화 한눈에 보기 | HTML 본문 통합 | 준비 자료·작업·검토·결과 설명과 예제는 선택·복사 가능한 본문으로 통합하고 중복 그림을 제거한다. | www/content/cookbook/business-plan.md |
| 계약서 검토 리포트 한눈에 보기 | HTML 본문 통합 | 준비 자료·작업·검토·결과 설명과 예제는 선택·복사 가능한 본문으로 통합하고 중복 그림을 제거한다. | www/content/cookbook/contract-review.md |
| 프레젠테이션 디자인 원칙 한눈에 보기 | HTML 본문 통합 | 준비 자료·작업·검토·결과 설명과 예제는 선택·복사 가능한 본문으로 통합하고 중복 그림을 제거한다. | www/content/cookbook/design/presentation.md |
| 콘텐츠 마케팅 전략 한눈에 보기 | HTML 본문 통합 | 준비 자료·작업·검토·결과 설명과 예제는 선택·복사 가능한 본문으로 통합하고 중복 그림을 제거한다. | www/content/cookbook/guides/content-marketing.md |
| 계약서 작성 가이드 한눈에 보기 | HTML 본문 통합 | 준비 자료·작업·검토·결과 설명과 예제는 선택·복사 가능한 본문으로 통합하고 중복 그림을 제거한다. | www/content/cookbook/guides/contract-drafting.md |
| 데이터 분석 가이드 한눈에 보기 | SVG 차트 + HTML 표 | 네 칸 설명은 본문으로 통합하고 분모가 다른 완료율만 눈금·값이 있는 차트로 남긴다. | www/content/cookbook/guides/data-analysis.md |
| 시각화 최적화 원칙 한눈에 보기 | SVG 차트 + HTML 표 | 네 칸 설명은 본문으로 통합하고 분모가 다른 완료율만 눈금·값이 있는 차트로 남긴다. | www/content/cookbook/guides/data-visualization.md |
| 투자 유치 가이드 한눈에 보기 | HTML 본문 통합 | 준비 자료·작업·검토·결과 설명과 예제는 선택·복사 가능한 본문으로 통합하고 중복 그림을 제거한다. | www/content/cookbook/guides/funding.md |
| 법률 리스크 관리 한눈에 보기 | HTML 본문 통합 | 준비 자료·작업·검토·결과 설명과 예제는 선택·복사 가능한 본문으로 통합하고 중복 그림을 제거한다. | www/content/cookbook/guides/legal-risk.md |
| SNS 최적화 가이드 한눈에 보기 | HTML 본문 통합 | 준비 자료·작업·검토·결과 설명과 예제는 선택·복사 가능한 본문으로 통합하고 중복 그림을 제거한다. | www/content/cookbook/guides/social-media.md |
| IR 덱 제작 한눈에 보기 | HTML 본문 통합 | 준비 자료·작업·검토·결과 설명과 예제는 선택·복사 가능한 본문으로 통합하고 중복 그림을 제거한다. | www/content/cookbook/ir-deck.md |
| NDA 일괄 검토 파이프라인 한눈에 보기 | HTML 본문 통합 | 준비 자료·작업·검토·결과 설명과 예제는 선택·복사 가능한 본문으로 통합하고 중복 그림을 제거한다. | www/content/cookbook/legal-nda-batch.md |
| 브랜드에서 랜딩 페이지까지 한눈에 보기 | HTML 본문 통합 | 준비 자료·작업·검토·결과 설명과 예제는 선택·복사 가능한 본문으로 통합하고 중복 그림을 제거한다. | www/content/cookbook/projects/brand-to-landing.md |
| 이직 준비 프로젝트 한눈에 보기 | HTML 본문 통합 | 준비 자료·작업·검토·결과 설명과 예제는 선택·복사 가능한 본문으로 통합하고 중복 그림을 제거한다. | www/content/cookbook/projects/career-transition-4weeks.md |
| 계약서 검토와 리스크 보고 한눈에 보기 | HTML 본문 통합 | 준비 자료·작업·검토·결과 설명과 예제는 선택·복사 가능한 본문으로 통합하고 중복 그림을 제거한다. | www/content/cookbook/projects/contract-risk-report.md |
| 정부 지원사업 신청서 완성하기 한눈에 보기 | HTML 본문 통합 | 준비 자료·작업·검토·결과 설명과 예제는 선택·복사 가능한 본문으로 통합하고 중복 그림을 제거한다. | www/content/cookbook/projects/gov-grant-application.md |
| 채용 공고부터 오퍼레터까지 한눈에 보기 | HTML 본문 통합 | 준비 자료·작업·검토·결과 설명과 예제는 선택·복사 가능한 본문으로 통합하고 중복 그림을 제거한다. | www/content/cookbook/projects/hiring-pipeline.md |
| 공공데이터로 시장 보고서 만들기 한눈에 보기 | SVG 차트 + HTML 표 | 네 칸 설명은 본문으로 통합하고 분모가 다른 완료율만 눈금·값이 있는 차트로 남긴다. | www/content/cookbook/projects/public-data-report.md |
| 스마트스토어 신제품 런칭하기 한눈에 보기 | HTML 본문 통합 | 준비 자료·작업·검토·결과 설명과 예제는 선택·복사 가능한 본문으로 통합하고 중복 그림을 제거한다. | www/content/cookbook/projects/smartstore-launch.md |
| 한 달치 SNS 콘텐츠 캘린더 만들기 한눈에 보기 | HTML 본문 통합 | 준비 자료·작업·검토·결과 설명과 예제는 선택·복사 가능한 본문으로 통합하고 중복 그림을 제거한다. | www/content/cookbook/projects/sns-content-month.md |
| 상권분석으로 창업 타당성 검증하기 한눈에 보기 | HTML 본문 통합 | 준비 자료·작업·검토·결과 설명과 예제는 선택·복사 가능한 본문으로 통합하고 중복 그림을 제거한다. | www/content/cookbook/projects/startup-feasibility.md |
| VOC 분석으로 FAQ 지식베이스 구축하기 한눈에 보기 | HTML 본문 통합 | 준비 자료·작업·검토·결과 설명과 예제는 선택·복사 가능한 본문으로 통합하고 중복 그림을 제거한다. | www/content/cookbook/projects/voc-to-faq.md |
| 웹소설 기획부터 연재·표지까지 한눈에 보기 | HTML 본문 통합 | 준비 자료·작업·검토·결과 설명과 예제는 선택·복사 가능한 본문으로 통합하고 중복 그림을 제거한다. | www/content/cookbook/projects/webnovel-project.md |
| 주간보고 자동화 루틴 만들기 한눈에 보기 | HTML 본문 통합 | 준비 자료·작업·검토·결과 설명과 예제는 선택·복사 가능한 본문으로 통합하고 중복 그림을 제거한다. | www/content/cookbook/projects/weekly-report-routine.md |
| 주간 보고서 자동화 한눈에 보기 | HTML 본문 통합 | 준비 자료·작업·검토·결과 설명과 예제는 선택·복사 가능한 본문으로 통합하고 중복 그림을 제거한다. | www/content/cookbook/report-automation.md |
| 컴플라이언스 체크리스트 한눈에 보기 | HTML 본문 통합 | 준비 자료·작업·검토·결과 설명과 예제는 선택·복사 가능한 본문으로 통합하고 중복 그림을 제거한다. | www/content/cookbook/templates/compliance.md |
| 이메일 마케팅 템플릿 한눈에 보기 | HTML 본문 통합 | 준비 자료·작업·검토·결과 설명과 예제는 선택·복사 가능한 본문으로 통합하고 중복 그림을 제거한다. | www/content/cookbook/templates/email.md |
| 엑셀 고급 기법 한눈에 보기 | HTML 본문 통합 | 준비 자료·작업·검토·결과 설명과 예제는 선택·복사 가능한 본문으로 통합하고 중복 그림을 제거한다. | www/content/cookbook/templates/excel.md |
| 재무 모델링 템플릿 한눈에 보기 | HTML 본문 통합 | 준비 자료·작업·검토·결과 설명과 예제는 선택·복사 가능한 본문으로 통합하고 중복 그림을 제거한다. | www/content/cookbook/templates/financial.md |
| 광고 트랙 한눈에 보기 | HTML 본문 통합 | 준비 자료·작업·검토·결과 설명과 예제는 선택·복사 가능한 본문으로 통합하고 중복 그림을 제거한다. | www/content/cookbook/tracks/track-advertising.md |
| 부록 트랙 한눈에 보기 | HTML 본문 통합 | 준비 자료·작업·검토·결과 설명과 예제는 선택·복사 가능한 본문으로 통합하고 중복 그림을 제거한다. | www/content/cookbook/tracks/track-appendix.md |
| 이커머스 트랙 한눈에 보기 | HTML 본문 통합 | 준비 자료·작업·검토·결과 설명과 예제는 선택·복사 가능한 본문으로 통합하고 중복 그림을 제거한다. | www/content/cookbook/tracks/track-commerce.md |
| 콘텐츠 트랙 한눈에 보기 | HTML 본문 통합 | 준비 자료·작업·검토·결과 설명과 예제는 선택·복사 가능한 본문으로 통합하고 중복 그림을 제거한다. | www/content/cookbook/tracks/track-content.md |
| 데이터 트랙 한눈에 보기 | SVG 차트 + HTML 표 | 네 칸 설명은 본문으로 통합하고 분모가 다른 완료율만 눈금·값이 있는 차트로 남긴다. | www/content/cookbook/tracks/track-data.md |
| 문서 트랙 한눈에 보기 | HTML 본문 통합 | 준비 자료·작업·검토·결과 설명과 예제는 선택·복사 가능한 본문으로 통합하고 중복 그림을 제거한다. | www/content/cookbook/tracks/track-documents.md |
| 재무 트랙 한눈에 보기 | HTML 본문 통합 | 준비 자료·작업·검토·결과 설명과 예제는 선택·복사 가능한 본문으로 통합하고 중복 그림을 제거한다. | www/content/cookbook/tracks/track-finance.md |
| HR·커리어 트랙 한눈에 보기 | HTML 본문 통합 | 준비 자료·작업·검토·결과 설명과 예제는 선택·복사 가능한 본문으로 통합하고 중복 그림을 제거한다. | www/content/cookbook/tracks/track-hr.md |
| 법률 트랙 한눈에 보기 | HTML 본문 통합 | 준비 자료·작업·검토·결과 설명과 예제는 선택·복사 가능한 본문으로 통합하고 중복 그림을 제거한다. | www/content/cookbook/tracks/track-legal.md |
| 마케팅 트랙 한눈에 보기 | HTML 본문 통합 | 준비 자료·작업·검토·결과 설명과 예제는 선택·복사 가능한 본문으로 통합하고 중복 그림을 제거한다. | www/content/cookbook/tracks/track-marketing.md |
| 운영 트랙 한눈에 보기 | HTML 본문 통합 | 준비 자료·작업·검토·결과 설명과 예제는 선택·복사 가능한 본문으로 통합하고 중복 그림을 제거한다. | www/content/cookbook/tracks/track-operations.md |
| 제품 개발 트랙 한눈에 보기 | HTML 본문 통합 | 준비 자료·작업·검토·결과 설명과 예제는 선택·복사 가능한 본문으로 통합하고 중복 그림을 제거한다. | www/content/cookbook/tracks/track-product.md |
| 재무·세무 담당 한눈에 보기 | HTML 본문 통합 | 준비 자료·작업·검토·결과 설명과 예제는 선택·복사 가능한 본문으로 통합하고 중복 그림을 제거한다. | www/content/moai-agents/accountant.md |
| 데이터 애널리스트 한눈에 보기 | SVG 차트 + HTML 표 | 네 칸 설명은 본문으로 통합하고 분모가 다른 완료율만 눈금·값이 있는 차트로 남긴다. | www/content/moai-agents/analyst.md |
| 커리어코치 한눈에 보기 | HTML 본문 통합 | 준비 자료·작업·검토·결과 설명과 예제는 선택·복사 가능한 본문으로 통합하고 중복 그림을 제거한다. | www/content/moai-agents/career.md |
| 컨설턴트 한눈에 보기 | HTML 본문 통합 | 준비 자료·작업·검토·결과 설명과 예제는 선택·복사 가능한 본문으로 통합하고 중복 그림을 제거한다. | www/content/moai-agents/consultant.md |
| 코워커 한눈에 보기 | HTML 본문 통합 | 준비 자료·작업·검토·결과 설명과 예제는 선택·복사 가능한 본문으로 통합하고 중복 그림을 제거한다. | www/content/moai-agents/coworker.md |
| CS매니저 한눈에 보기 | HTML 본문 통합 | 준비 자료·작업·검토·결과 설명과 예제는 선택·복사 가능한 본문으로 통합하고 중복 그림을 제거한다. | www/content/moai-agents/cs.md |
| 디자이너 한눈에 보기 | HTML 본문 통합 | 준비 자료·작업·검토·결과 설명과 예제는 선택·복사 가능한 본문으로 통합하고 중복 그림을 제거한다. | www/content/moai-agents/designer.md |
| 법무 담당 한눈에 보기 | HTML 본문 통합 | 준비 자료·작업·검토·결과 설명과 예제는 선택·복사 가능한 본문으로 통합하고 중복 그림을 제거한다. | www/content/moai-agents/lawyer.md |
| 마케터 한눈에 보기 | HTML 본문 통합 | 준비 자료·작업·검토·결과 설명과 예제는 선택·복사 가능한 본문으로 통합하고 중복 그림을 제거한다. | www/content/moai-agents/marketer.md |
| 미디어 크리에이터 한눈에 보기 | HTML 본문 통합 | 준비 자료·작업·검토·결과 설명과 예제는 선택·복사 가능한 본문으로 통합하고 중복 그림을 제거한다. | www/content/moai-agents/media.md |
| 사무관 한눈에 보기 | HTML 본문 통합 | 준비 자료·작업·검토·결과 설명과 예제는 선택·복사 가능한 본문으로 통합하고 중복 그림을 제거한다. | www/content/moai-agents/officer.md |
| 인사·채용 담당 한눈에 보기 | HTML 본문 통합 | 준비 자료·작업·검토·결과 설명과 예제는 선택·복사 가능한 본문으로 통합하고 중복 그림을 제거한다. | www/content/moai-agents/recruiter.md |
| 셀러 한눈에 보기 | HTML 본문 통합 | 준비 자료·작업·검토·결과 설명과 예제는 선택·복사 가능한 본문으로 통합하고 중복 그림을 제거한다. | www/content/moai-agents/seller.md |
| 스토리 크리에이터 한눈에 보기 | HTML 본문 통합 | 준비 자료·작업·검토·결과 설명과 예제는 선택·복사 가능한 본문으로 통합하고 중복 그림을 제거한다. | www/content/moai-agents/story.md |
| SNS 크리에이터 한눈에 보기 | HTML 본문 통합 | 준비 자료·작업·검토·결과 설명과 예제는 선택·복사 가능한 본문으로 통합하고 중복 그림을 제거한다. | www/content/moai-agents/threads-poster.md |
| 튜터 한눈에 보기 | HTML 본문 통합 | 준비 자료·작업·검토·결과 설명과 예제는 선택·복사 가능한 본문으로 통합하고 중복 그림을 제거한다. | www/content/moai-agents/tutor.md |
| 작가 한눈에 보기 | HTML 본문 통합 | 준비 자료·작업·검토·결과 설명과 예제는 선택·복사 가능한 본문으로 통합하고 중복 그림을 제거한다. | www/content/moai-agents/writer.md |

## 기존 PNG

| 파일 | 현재 사용 | 제안 | 이유 |
|---|---|---|---|
| attribution-flow.png | 0개 페이지 | 미참조 보관·재사용 보류 | 권리·출처 확인 기준을 근거 링크가 있는 표로 표현한다. |
| core-concepts.png | 0개 페이지 | 미참조 보관·재사용 보류 | 네 용어의 짧은 정의를 본문 표로 통합한다. |
| coworker-concept.png | 0개 페이지 | 미참조 보관·재사용 보류 | 역할 이름 목록은 검색·링크가 가능한 HTML 목록으로 표현한다. |
| coworker-family-map.png | 0개 페이지 | 미참조 보관·재사용 보류 | 분야 분류와 역할 이름을 링크 가능한 목록으로 표현한다. |
| docsite-map.png | 0개 페이지 | 미참조 보관·재사용 보류 | 문서 탐색은 클릭 가능한 목차가 적합하다. |
| expert-workflow-ko.png | 2개 페이지 | Mermaid 분기·합류 | 분석 뒤 작성 작업의 분기와 검토 전 합류를 남기고 설명은 본문으로 옮긴다. |
| first-workflow-ko.png | 4개 페이지 | Mermaid 순환 | 결과 검토 → 수정 요청의 되돌아가는 경로를 남긴다. |
| install-3steps.png | 0개 페이지 | 미참조 보관·재사용 보류 | 설치 단계는 실제 UI 캡처와 체크리스트로 안내한다. |
| install-manage-flow.png | 0개 페이지 | 미참조 보관·재사용 보류 | 단순 직선 단계는 체크리스트와 실제 화면으로 안내한다. |
| mcp-bridge.png | 0개 페이지 | 미참조 보관·재사용 보류 | 앱·연결·외부 서비스의 경계와 실제 지원 확인을 표시한다. |
| project-concepts-ko.png | 2개 페이지 | Mermaid 관계 | 지침·스킬·역할·패키지·외부 연결의 관계를 간결하게 다시 그린다. |
| project-context-ko.png | 2개 페이지 | Mermaid 관계 | 앱 프로젝트와 허용한 로컬 폴더의 경계를 분리한다. 긴 설명은 HTML로 옮긴다. |
| project-flow.png | 0개 페이지 | 미참조 보관·재사용 보류 | 맥락 질문과 기능 확인에서 지침 생성·참조 확인으로 이어지는 관계를 그린다. |
| quickstart-5min.png | 0개 페이지 | 미참조 보관·재사용 보류 | 지침 설정과 첫 요청은 실행 가능한 본문으로 안내한다. |
| skill-chain-flow.png | 0개 페이지 | 미참조 보관·재사용 보류 | 생성·변환·검수의 선후 관계를 명확한 화살표로 다시 그린다. |
| skill-chaining-pattern.png | 0개 페이지 | 미참조 보관·재사용 보류 | 도메인 방법 → 결과 형식 → 검토 기준이 어디에 적용되는지 다시 그린다. |
| team-pattern.png | 0개 페이지 | 미참조 보관·재사용 보류 | 담당자별 입력·출력과 합류 조건을 추가해 다시 그린다. |
