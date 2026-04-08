# router.md — 자연어 → 하네스 매핑 프로토콜

## 개요
사용자의 자연어 요청을 분석하여 적절한 MoAI 하네스(skill)를 자동 감지하고 라우팅하는 프로토콜입니다.
의도 분류, 키워드 매핑, 모호성 해소를 통해 최적의 실행 경로를 결정합니다.

---

## 1. 요청 분석 단계

### 1.1 자연어 파싱
사용자 입력에서 다음을 추출합니다:
- **핵심 동사**: "작성", "분석", "계획", "검토", "자동화" 등
- **도메인 키워드**: 마케팅, 재무, 기술, 전략, 콘텐츠 등
- **문맥 신호**: 긴급성, 복잡도, 팀 규모, 기한 등
- **명시적 대상**: 산출물(문서, 이메일, 계획서 등)

### 1.2 의도 분류 알고리즘
- IF 사용자_요청 IN [콘텐츠_생성, 글쓰기, 블로그, SNS, 이메일] → copywriting, email-crafter, social-media
- IF 사용자_요청 IN [자동화, 워크플로우_최적화, 프로세스] → sop-writer, project-tracker, remote-work-ops
- IF 사용자_요청 IN [법규_검토, 규제, 컴플라이언스] → compliance, contract-review, regulatory
- IF 사용자_요청 IN [일정관리, 협업, 커뮤니케이션] → meeting-strategist, stakeholder-report

---

## 2. 키워드 매핑 테이블 (100 하네스 전체)

### 2.1 콘텐츠 & 크리에이티브 (10개)

| 하네스 ID | 한글 키워드 | English Keywords | 우선순위 |
|----------|-----------|------------------|---------|
| youtube-production | 유튜브, 영상 제작, 채널 관리, 스크립트 | YouTube, video production, channel growth | 1순위 |
| podcast-studio | 팟캐스트, 팟방, 오디오, 음성 콘텐츠 | podcast, audio production, sound editing | 1순위 |
| newsletter-engine | 뉴스레터, 구독 콘텐츠, 메일링, 정기 발송 | newsletter, email subscription, content dispatch | 1순위 |
| content-repurposer | 콘텐츠 재활용, 변환, 다채널 배포, 리믹스 | content repurposing, multi-channel, remix | 1순위 |
| game-narrative | 게임 스토리, 내러티브 디자인, 게임 기획 | game narrative, storytelling, quest design | 1순위 |
| brand-identity | 브랜드 정체성, 로고, 브랜드 가이드, 톤앤매너 | brand identity, brand guidelines, tone of voice | 1순위 |
| comic-creator | 만화, 웹툰, 일러스트 콘텐츠, 그래픽 노블 | comic, webtoon, illustration, visual story | 1순위 |
| visual-storytelling | 비주얼 스토리, 인포그래픽, 데이터 시각화 | visual storytelling, infographic, data visualization | 1순위 |
| book-publishing | 책 출판, 원고 편집, 출판 기획, 저술 | book publishing, manuscript editing, author | 1순위 |
| advertising-campaign | 광고 캠페인, 광고 기획, 마케팅 캠페인 | advertising campaign, ad strategy, creative brief | 1순위 |

### 2.2 엔지니어링 & 개발 (15개)

| 하네스 ID | 한글 키워드 | English Keywords | 우선순위 |
|----------|-----------|------------------|---------|
| fullstack-webapp | 웹앱, 풀스택, 웹 개발, 웹 애플리케이션 | fullstack web app, web development, SPA | 1순위 |
| mobile-app-builder | 모바일 앱, iOS, 안드로이드, 모바일 개발 | mobile app, iOS, Android, cross-platform | 1순위 |
| api-designer | API 설계, REST, GraphQL, API 아키텍처 | API design, REST API, GraphQL, endpoint | 1순위 |
| database-architect | 데이터베이스, 스키마 설계, DB 아키텍처 | database design, schema, SQL, NoSQL | 1순위 |
| cicd-pipeline | CI/CD, 배포 파이프라인, 자동화 배포, DevOps | CI/CD pipeline, continuous deployment, GitLab CI | 1순위 |
| code-reviewer | 코드 리뷰, 코드 품질, PR 검토, 코드 컨설팅 | code review, pull request, code quality | 2순위 |
| legacy-modernizer | 레거시 코드 개선, 코드 마이그레이션, 리팩토링 | legacy code, modernization, refactoring | 2순위 |
| microservice-designer | 마이크로서비스, 서비스 아키텍처, 분산 시스템 | microservice architecture, service design | 2순위 |
| test-automation | 자동화 테스트, 테스트 케이스, QA, 테스트 전략 | test automation, unit test, QA, testing strategy | 2순위 |
| incident-postmortem | 장애 분석, 포스트모템, 사건 보고서, RCA | incident response, postmortem, root cause analysis | 2순위 |
| infra-as-code | 인프라 자동화, IaC, Terraform, 클라우드 설정 | infrastructure as code, Terraform, cloud setup | 2순위 |
| data-pipeline | 데이터 파이프라인, ETL, 데이터 처리, 스트리밍 | data pipeline, ETL, data processing, stream | 2순위 |
| security-audit | 보안 감시, 취약점 분석, 보안 검토, 침투테스트 | security audit, vulnerability assessment, pentesting | 2순위 |
| performance-optimizer | 성능 최적화, 속도 개선, 프로파일링, 튜닝 | performance optimization, speed improvement, profiling | 2순위 |
| open-source-launcher | 오픈소스, 공개 프로젝트, OSS 전략, 커뮤니티 | open source, OSS launch, community building | 2순위 |

### 2.3 데이터 & AI (12개)

| 하네스 ID | 한글 키워드 | English Keywords | 우선순위 |
|----------|-----------|------------------|---------|
| ml-experiment | 머신러닝, ML 모델, 실험, 학습 알고리즘 | machine learning, ML model, experiment, training | 1순위 |
| data-analysis | 데이터 분석, 통계 분석, 인사이트, 리포팅 | data analysis, analytics, insights, reporting | 1순위 |
| text-processor | 텍스트 처리, NLP, 언어 처리, 감정 분석 | text processing, NLP, sentiment analysis, OCR | 1순위 |
| data-migration | 데이터 이전, 마이그레이션, 데이터 이관 | data migration, ETL mapping, data transfer | 2순위 |
| api-client-generator | API 클라이언트, SDK 생성, 코드 생성 | API client generator, SDK generation, code gen | 2순위 |
| design-system | 디자인 시스템, 컴포넌트 라이브러리, UI 가이드 | design system, component library, UI kit | 2순위 |
| web-scraper | 웹 스크래핑, 크롤링, 데이터 수집, 자동 수집 | web scraping, web crawler, data extraction | 2순위 |
| chatbot-builder | 챗봇, 대화형 AI, 자동응답, 챗 플랫폼 | chatbot, conversational AI, chat interface | 2순위 |
| changelog-generator | 변경 로그, 릴리스 노트, 버전 히스토리 | changelog, release notes, version history | 3순위 |
| cli-tool-builder | CLI 도구, 커맨드라인, 자동화 스크립트 | CLI tool, command-line utility, automation script | 2순위 |
| llm-app-builder | LLM 애플리케이션, 생성형 AI, 프롬프트 엔지니어링 | LLM application, generative AI, prompt engineering | 2순위 |
| bi-dashboard | BI 대시보드, 데이터 시각화, 대시보드 설계 | BI dashboard, data visualization, analytics board | 2순위 |

### 2.4 비즈니스 & 전략 (11개)

| 하네스 ID | 한글 키워드 | English Keywords | 우선순위 |
|----------|-----------|------------------|---------|
| startup-launcher | 스타트업, 사업 계획서, 창업, 신사업 기획 | startup, business plan, launch, new venture | 1순위 |
| market-research | 시장 조사, 경쟁사 분석, 시장 분석, 산업 분석 | market research, competitive analysis, industry analysis | 1순위 |
| gov-funding-plan | 정부 지원금, 보조금, 지원 사업, 정부 자금 | government funding, grants, subsidy application | 1순위 |
| product-manager | 제품 관리, 제품 전략, PM, 프로덕트 오너 | product management, product strategy, roadmap | 1순위 |
| strategy-framework | 전략 수립, 프레임워크, 비즈니스 모델, 전략안 | strategy framework, business model, strategic plan | 1순위 |
| sales-enablement | 영업 활성화, 세일즈 자료, 영업 전략, 영업 지원 | sales enablement, sales strategy, pitch deck | 1순위 |
| customer-support | 고객 지원, 고객 서비스, CS 전략, 지원 체계 | customer support, customer service, support strategy | 1순위 |
| pricing-strategy | 가격 전략, 가격 책정, 요금제, 수익 모델 | pricing strategy, pricing model, revenue model | 1순위 |
| investor-report | 투자자 보고서, 실적 보고, 분기 보고, IR | investor report, earnings report, quarterly update | 2순위 |
| scenario-planner | 시나리오 분석, 의사결정 분석, 시뮬레이션 | scenario planning, what-if analysis, simulation | 2순위 |
| financial-modeler | 재무 모델, 예산 계획, 재무 분석, 수익 예측 | financial modeling, budgeting, financial forecast | 1순위 |
| grant-writer | 그래프트 작성, 기금 신청, 프로젝트 기금 | grant writing, grant proposal, funding application | 2순위 |
| rfp-responder | RFP 응답, 입찰 제안서, 제안서 작성 | RFP response, proposal writing, tender response | 2순위 |

### 2.5 교육 & 연구 (10개)

| 하네스 ID | 한글 키워드 | English Keywords | 우선순위 |
|----------|-----------|------------------|---------|
| language-tutor | 언어 튜터, 외국어 학습, 언어 교육, 영어 강사 | language tutor, language learning, ESL teaching | 1순위 |
| exam-prep | 시험 대비, 수능, 자격증, 시험 준비, 수험 전략 | exam preparation, test prep, certification study | 1순위 |
| thesis-advisor | 논문 지도, 학위논문, 논문 상담, 학술 지원 | thesis advisor, dissertation help, academic writing | 1순위 |
| coding-bootcamp | 코딩 부트캠프, 프로그래밍 교육, 개발 과정 | coding bootcamp, programming course, dev training | 1순위 |
| debate-simulator | 토론 시뮬레이션, 논쟁 연습, 디베이팅 | debate simulator, argumentation, debate practice | 2순위 |
| competency-modeler | 역량 모델, 역량 평가, 직무 역량, 스킬 맵 | competency modeling, skills assessment, capability | 2순위 |
| adr-writer | ADR 문서, 아키텍처 결정, 설계 문서, 기술 결정 | ADR, architecture decision record, design doc | 2순위 |
| research-assistant | 연구 보조, 논문 검색, 참고문헌, 문헌조사 | research assistant, literature review, citation | 2순위 |
| knowledge-base-builder | 지식 베이스, 문서화, wiki, 정보 정리 | knowledge base, documentation, wiki, knowledge hub | 2순위 |
| course-builder | 교육 과정, 커리큘럼, 온라인 코스, 수업 설계 | course builder, curriculum design, online course | 1순위 |
| documentary-research | 다큐멘터리, 영상 연구, 역사 조사, 아카이브 | documentary research, archival research, history | 2순위 |
| academic-paper | 학술 논문, 저널 논문, 학위논문, 연구 논문 | academic paper, journal article, research article | 1순위 |

### 2.6 법률 & 컴플라이언스 (6개)

| 하네스 ID | 한글 키워드 | English Keywords | 우선순위 |
|----------|-----------|------------------|---------|
| contract-analyzer | 계약서 검토, 계약 분석, 법적 검토, 계약 자문 | contract analysis, legal review, agreement | 1순위 |
| compliance-checker | 컴플라이언스, 규정 준수, 규제 검토, 법규 준수 | compliance, regulatory compliance, audit readiness | 1순위 |
| patent-drafter | 특허 출원, 특허 작성, 특허 명세서, 지식재산 | patent drafting, IP protection, patent application | 1순위 |
| privacy-engineer | 개인정보보호, GDPR, 데이터 보안, 개인정보 정책 | privacy engineering, GDPR, data protection, DPA | 1순위 |
| legal-research | 법률 조사, 판례 조사, 법적 근거, 법률 자료 | legal research, case law, legal precedent | 2순위 |
| service-legal-docs | 이용약관, 개인정보정책, 약관 작성, 법률 문서 | terms of service, privacy policy, legal document | 1순위 |
| regulatory-filing | 규제 신청, 인허가, 신고, 규제 제출 | regulatory filing, license application, submission | 2순위 |
| ip-portfolio | 지식재산 포트폴리오, IP 관리, 저작권, 상표 | IP portfolio, intellectual property, trademark | 2순위 |
| audit-report | 감사 보고서, 감시, 내부 감시, 외부 감시 | audit report, internal audit, external audit | 2순위 |

### 2.7 라이프스타일 (10개)

| 하네스 ID | 한글 키워드 | English Keywords | 우선순위 |
|----------|-----------|------------------|---------|
| meal-planner | 식단 계획, 메뉴 계획, 요리 레시피, 영양 관리 | meal planning, recipe, nutrition, diet plan | 1순위 |
| fitness-program | 피트니스, 운동 계획, 헬스, 트레이닝 프로그램 | fitness program, workout plan, exercise routine | 1순위 |
| tax-calculator | 세금 계산, 세무, 소득세, 세금 전략 | tax calculation, tax planning, income tax | 1순위 |
| travel-planner | 여행 계획, 여행 일정, 관광 가이드, 여행 예산 | travel planning, itinerary, trip planning, vacation | 1순위 |
| space-concept-board | 공간 설계, 인테리어, 집 꾸미기, 공간 레이아웃 | space design, interior design, room layout | 1순위 |
| personal-finance | 개인 재무, 자산 관리, 자산 계획, 재정 계획 | personal finance, financial planning, asset mgmt | 1순위 |
| side-project-launcher | 사이드 프로젝트, 부업 기획, 창업 준비, 개인 사업 | side project, side hustle, personal venture | 2순위 |
| wedding-planner | 결혼식 계획, 웨딩, 예식 관리, 결혼 준비 | wedding planning, event planning, ceremony | 1순위 |
| personal-branding | 개인 브랜드, 개인 마케팅, 커리어 브랜딩, 프로필 | personal branding, personal brand, self-marketing | 2순위 |
| ecommerce-launcher | 이커머스, 온라인 스토어, 쇼핑몰, 온라인 판매 | ecommerce, online store, Shopify, Woocommerce | 1순위 |
| real-estate-analyst | 부동산 분석, 물건 분석, 투자 분석, 시세 조사 | real estate analysis, property analysis, market | 2순위 |

### 2.8 커뮤니케이션 & 문서 (10개)

| 하네스 ID | 한글 키워드 | English Keywords | 우선순위 |
|----------|-----------|------------------|---------|
| technical-writer | 기술 문서, 매뉴얼 작성, 문서화, 가이드 작성 | technical writing, documentation, user manual | 1순위 |
| report-generator | 보고서 작성, 리포트, 분석 보고서, 정기 보고 | report generation, reporting, analysis report | 1순위 |
| sop-writer | SOP, 업무 절차, 프로세스 문서, 표준 운영 절차 | SOP, standard operating procedure, process doc | 1순위 |
| meeting-strategist | 회의 전략, 회의 기획, 회의 진행, 미팅 준비 | meeting strategy, meeting facilitation, agenda | 1순위 |
| public-speaking | 공개 연설, 발표, 스피치, 프레젠테이션 스킬 | public speaking, presentation, speech coaching | 1순위 |
| proposal-writer | 제안서 작성, 제안 문서, 비즈니스 제안, 프로포절 | proposal writing, business proposal, pitch | 1순위 |
| crisis-communication | 위기 소통, 위기 관리, 대응 전략, 보도 자료 | crisis communication, PR response, statement | 2순위 |
| presentation-designer | 프레젠테이션 설계, 슬라이드, 비주얼 디자인 | presentation design, slide design, visual deck | 1순위 |
| translation-localization | 번역, 다국어, 현지화, 언어 지원, 지역화 | translation, localization, multilingual, i18n | 2순위 |

### 2.9 운영 & HR (9개)

| 하네스 ID | 한글 키워드 | English Keywords | 우선순위 |
|----------|-----------|------------------|---------|
| risk-register | 위험 관리, 리스크 등록, 위험 식별, 리스크 분석 | risk management, risk register, risk assessment | 2순위 |
| event-organizer | 행사 기획, 이벤트, 컨퍼런스, 세미나 | event planning, event management, conference | 1순위 |
| hiring-pipeline | 채용 파이프라인, 채용 공고, 인력 채용, 교용 프로세스 | hiring, recruiting, job posting, candidate pipeline | 1순위 |
| onboarding-system | 온보딩, 신입 교육, 직원 입사, 교육 프로그램 | onboarding, employee onboarding, training | 1순위 |
| operations-manual | 운영 매뉴얼, 운영 문서, 프로세스 가이드 | operations manual, operational procedures | 1순위 |
| feedback-analyzer | 피드백 분석, 설문 분석, 의견 분석, 평가 | feedback analysis, survey analysis, sentiment | 2순위 |
| procurement-docs | 구매 관리, 구매 요청, 조달 문서, 공급업체 관리 | procurement, purchasing, vendor management | 1순위 |
| social-media-manager | 소셜 미디어, SNS 관리, 커뮤니티 관리, 포스팅 | social media management, community, engagement | 1순위 |

---

## 3. 모호성 해소 로직

### 3.1 감지 신호
- 여러 하네스가 동등한 점수 (예: content + email 동시 매칭)
- 도메인 신호 부재 (추상적/일반적 요청)
- 상충하는 키워드 (예: "마케팅 자동화 법규 검토")
- 첫 사용자 또는 프로필 불완전

### 3.2 AskUserQuestion 재질문
모호성 감지 시, 최대 **4개 질문**으로 확인합니다:
- Q1: 주요 작업 타입 (4옵션)
- Q2: 도메인 (4옵션)
- Q3: 산출물 형태 (3-4옵션)
- Q4: 긴급도/복잡도 (3옵션)

---

## 4. 복합 요청 분기 처리

### 4.1 순차 실행 (Sequential)
예: "캠페인 계획 → 이메일 초안 → 성과 분석"
- Phase 1: advertising-campaign
- Phase 2: proposal-writer
- Phase 3: data-analysis

### 4.2 병렬 실행 (Parallel)
예: "마케팅 전략 + 재무 예산 동시 필요"
- Track A: market-research
- Track B: financial-modeler
- 병합 및 통합 분석

### 4.3 의존적 실행 (Dependent)
예: "법규 검토 후 계약서 작성"
- Phase 1: compliance-checker (제약사항 산출)
- Phase 2: contract-analyzer (Phase 1 결과 참조)

---

## 5. 라우팅 결정 트리

```
사용자_요청_분석
├─ [콘텐츠&마케팅] 신호?
│  ├─ YES → 콘텐츠 타입 확인
│  │       ├─ 비디오 → youtube-production
│  │       ├─ 팟캐스트 → podcast-studio
│  │       ├─ 이메일 → newsletter-engine
│  │       ├─ 광고 → advertising-campaign
│  │       └─ 기타 → content-repurposer
│  └─ NO → 다음 분기
├─ [기술&개발] 신호?
│  ├─ YES → 개발 타입 확인
│  │       ├─ 웹 → fullstack-webapp
│  │       ├─ 모바일 → mobile-app-builder
│  │       ├─ API → api-designer
│  │       ├─ DB → database-architect
│  │       └─ 배포 → cicd-pipeline
│  └─ NO → 다음 분기
├─ [데이터&AI] 신호?
│  ├─ YES → AI 타입 확인
│  │       ├─ ML → ml-experiment
│  │       ├─ 분석 → data-analysis
│  │       ├─ 텍스트 → text-processor
│  │       └─ 챗봇 → chatbot-builder
│  └─ NO → 다음 분기
├─ [비즈니스&전략] 신호?
│  ├─ YES → 비즈니스 타입 확인
│  │       ├─ 창업 → startup-launcher
│  │       ├─ 조사 → market-research
│  │       ├─ 전략 → strategy-framework
│  │       ├─ 영업 → sales-enablement
│  │       └─ 재무 → financial-modeler
│  └─ NO → 다음 분기
├─ [교육&연구] 신호?
│  ├─ YES → 교육 타입 확인
│  │       ├─ 언어 → language-tutor
│  │       ├─ 시험 → exam-prep
│  │       ├─ 논문 → thesis-advisor
│  │       └─ 코딩 → coding-bootcamp
│  └─ NO → 다음 분기
├─ [법률&규제] 신호?
│  ├─ YES → 법률 타입 확인
│  │       ├─ 계약 → contract-analyzer
│  │       ├─ 컴플라이언스 → compliance-checker
│  │       ├─ 특허 → patent-drafter
│  │       └─ 개인정보 → privacy-engineer
│  └─ NO → 다음 분기
├─ [라이프&커뮤니케이션] 신호?
│  ├─ YES → 라이프 타입 확인
│  │       ├─ 식단 → meal-planner
│  │       ├─ 운동 → fitness-program
│  │       ├─ 여행 → travel-planner
│  │       └─ 결혼식 → wedding-planner
│  └─ NO → 다음 분기
├─ [운영&HR] 신호?
│  ├─ YES → 운영 타입 확인
│  │       ├─ 채용 → hiring-pipeline
│  │       ├─ 행사 → event-organizer
│  │       ├─ 온보딩 → onboarding-system
│  │       └─ SNS → social-media-manager
│  └─ NO → 일반 AskUserQuestion
```

---

## 6. 실행 순서 (Priority Ranking)

라우팅 후 최적 하네스 선택:

1. **프로필 기반 가중치**: 사용자 role/industry와 하네스 매칭
2. **요청 신선도**: 최근 선택한 하네스 선호 (학습 효과)
3. **완성도**: 필수 컨텍스트 충분 여부
4. **복잡도**: 요청 복잡도와 하네스 난이도 매칭

---

## 7. 확장성 및 커스터마이징

### 7.1 조직별 라우팅 규칙
`.moai/routing-rules.yaml`:
```yaml
tech_startup:
  high_priority: [fullstack-webapp, ml-experiment, product-manager]
finance_corp:
  high_priority: [financial-modeler, compliance-checker, legal-research]
media_agency:
  high_priority: [advertising-campaign, content-repurposer, presentation-designer]
education:
  high_priority: [course-builder, exam-prep, language-tutor]
```

### 7.2 사용자 선호도 학습
- 선택 이력 추적 (.moai/user-preferences.md)
- 실행 성공률 기반 가중치 조정
- 피드백 루프: 평점 → 가중치 재계산

---

## 8. 오류 처리 및 폴백

| 상황 | 조치 |
|-----|------|
| 하네스 미설치 | `/moai init --harness {name}` 제안 |
| 프로필 불완전 | `/moai init` 재실행 유도 |
| 모두 불확실 | 일반 AI 어시스턴트로 폴백 |
| 모호 (해소 불가) | 2회 재시도 후 다시 분류 |

---

## 9. 성능 메트릭

- **정확성**: 선택 하네스 = 사용자 예상 (%)
- **응답 속도**: 라우팅 결정 시간 (< 2초)
- **재질문 빈도**: 모호성 해소 시도 횟수
- **성공률**: 라우팅 후 작업 완료율

---

## 버전 정보

**V0.1.3** (2026-04-08)
- 100개 하네스 전체 매핑 완료
- 한글 + 영문 트리거 키워드 추가
- 도메인별 우선순위 정의
- 복합 라우팅 패턴 명세화
