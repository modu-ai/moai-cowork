exec((__import__('pathlib').Path(__file__).parent/'rebuild_content.py').read_text().split("page('getting-started/_index.md'")[0])
employees=json.loads((ROOT/'www/data/agent_teams.json').read_text())['employees']
# Topic-specific inputs, outputs, completion checks. No performance promises or imaginary execution.
D={
'blog-pipeline':('제품·독자·주제·참고 자료','블로그 초안과 검토 메모','인용 출처·독자에 맞는 표현·공개 범위','marketer','주제와 독자를 정한 뒤 개요, 초안, 사실 확인, 제목 순서로 진행'),
'business-plan':('사업 개요·고객·수익 구조·근거 자료','사업계획서 초안','시장 수치 출처·가정·수익 계산','consultant','고객 문제, 해결책, 운영 방식, 재무 가정을 구분해 작성'),
'contract-review':('계약서·당사자 역할·관할·검토 목적','조항별 쟁점 표','조항 번호·원문·법령 출처·미확인 쟁점','lawyer','문서 종류를 확인하고 쟁점 추출, 근거 확인, 검토 메모 순서로 진행'),
'ir-deck':('사업 자료·지표·투자 목적·독자','IR 발표 초안','수치와 기간·가정·출처·슬라이드 메시지','consultant','핵심 주장과 근거를 먼저 정리한 뒤 슬라이드로 구성'),
'legal-nda-batch':('NDA 문서 묶음·검토 기준·관할','문서별 검토표와 종합 쟁점','문서별 누락·조항 인용·공통 기준·원본 보존','lawyer','문서별 결과를 별도 파일로 작성하고 같은 기준으로 모아 비교'),
'report-automation':('업무 메모·보고 양식·기간','주간보고와 반복 실행 계획','원문 숫자·기간·단위·미정 담당자·예약 등록 상태','coworker','수동으로 보고서를 먼저 검토한 뒤 현재 예약 기능과 자료 접근을 확인'),
'guides/content-marketing':('대상 고객·제품·콘텐츠 목표','콘텐츠 운영안','브랜드 기준·주장 근거·평가 지표','marketer','대상 고객, 메시지, 채널, 검토 기준을 정한 뒤 콘텐츠를 작성'),
'guides/contract-drafting':('합의 내용·당사자·관할·조건','계약 초안과 확인 목록','정의·의무·금액·기한·관할과 미정 항목','lawyer','합의된 내용과 미정 조건을 나눈 뒤 조항 초안을 구성'),
'guides/data-analysis':('데이터 표·질문·기간·단위','분석표와 해석','누락·중복·계산·인과 추정과 관측의 구분','analyst','구조와 누락을 확인하고 필요한 집계와 해석을 수행'),
'guides/data-visualization':('표·독자·전달할 메시지','차트와 설명','축·단위·기간·색 대비·원문 값','analyst','비교, 변화, 분포 중 전달 목적을 정하고 차트를 선택'),
'guides/funding':('사업 지표·투자 단계·검토 질문','투자 설명 자료','실적과 전망의 구분·자금 사용 근거','consultant','투자자에게 설명할 질문과 근거를 정리한 뒤 자료를 구성'),
'guides/legal-risk':('사업 범위·관할·관련 문서','법률 확인 목록','공식 출처·기준일·관할·미확인 사항','lawyer','업무 영역별로 확인할 쟁점을 정리하고 공식 자료로 대조'),
'guides/social-media':('콘텐츠 초안·채널·대상·말투','채널별 콘텐츠 초안','링크·문구·이미지 권리·게시 여부','marketer','핵심 메시지를 정한 뒤 채널별 형식으로 다듬고 게시 전 검토'),
'design/presentation':('발표 내용·청중·양식','발표 구성과 시안','한 장의 메시지·글자 가독성·차트 단위','designer','슬라이드마다 주장 하나와 근거를 배치하고 흐름을 확인'),
'projects/brand-to-landing':('브랜드·고객·제품·기존 자료','브랜드 기준과 랜딩 페이지 초안','주장 근거·행동 버튼·모바일 가독성','designer','브랜드 기준, 콘텐츠, 시안, 접근성 검토를 순서대로 진행'),
'projects/career-transition-4weeks':('경력·희망 직무·이력서·활동 가능 범위','이직 준비 목록과 지원 자료','실제 경력·수치·지원 요건·미정 일정','career','직무 요구를 확인하고 경력 정리, 이력서 수정, 면접 준비로 진행'),
'projects/contract-risk-report':('계약서·검토 목적·관할','조항별 쟁점 보고서','원문 인용·근거·미확인 조건','lawyer','조항 추출, 쟁점 분석, 근거 확인, 보고서 순서로 진행'),
'projects/gov-grant-application':('공고문·사업 자료·자격 요건','지원사업 신청서 초안','공고 버전·신청 자격·필수 서류·제출 기한','consultant','공고의 필수 조건을 먼저 확인하고 그 목차에 맞춰 작성'),
'projects/hiring-pipeline':('직무 요구·채용 절차·공고 양식','채용 문서와 진행 기준','직무 관련성·평가 기준·민감정보 범위','recruiter','공고, 평가 기준, 인터뷰 질문, 후속 문서 순서를 구성'),
'projects/public-data-report':('조사 질문·공공데이터·지역·기간','근거가 있는 시장 분석 보고서','데이터 출처·갱신일·지역·단위','analyst','질문에 맞는 자료를 수집하고 단위·기간을 맞춰 분석'),
'projects/smartstore-launch':('상품 정보·사진·고객·판매 조건','상품 소개와 출시 준비 목록','인증·효능 근거·가격·배송 조건·게시 상태','seller','상품 사실, 상세페이지 문구, 이미지, 등록 전 점검을 순서대로 진행'),
'projects/sns-content-month':('브랜드·대상·채널·게시 주제','SNS 콘텐츠 달력과 초안','중복 주제·브랜드 기준·소재 권리·게시 상태','marketer','주제 묶음과 채널을 정하고 달력과 초안을 작성'),
'projects/startup-feasibility':('창업 아이디어·입지·고객·비용 자료','타당성 검토표','시장 근거·비용 가정·검증이 필요한 조건','consultant','고객 문제, 시장 자료, 운영 비용, 미검증 가정을 나눠 분석'),
'projects/voc-to-faq':('고객 문의·기존 정책·FAQ','문의 분류와 FAQ 초안','정책 근거·개인정보 제거·반복 질문의 대표성','cs','문의 유형을 분류하고 정책과 대조한 뒤 FAQ 초안을 검토'),
'projects/webnovel-project':('장르·독자·세계관·등장인물','웹소설 기획안과 첫 회 초안','설정 일관성·인물 동기·저작권과 유사성','story','기획, 설정, 회차 구조, 초안, 설정 검토 순서로 진행'),
'projects/weekly-report-routine':('업무 기록·양식·보고 주기','주간보고와 반복 업무 설정','누락·숫자·담당자·예약 첫 실행','coworker','수동 보고서를 검토한 뒤 자료 수집과 예약 실행 가능 여부를 확인'),
 'templates/compliance':('사업·관할·처리 정보·관련 정책','준수 여부 확인 목록','공식 근거·적용 범위·검토 책임·미확인 항목','lawyer','적용 가능성을 확인할 질문과 관련 정책을 함께 정리'),
 'templates/email':('독자·메일 목적·제품 정보','이메일 초안 묶음','사실·링크·수신 대상·동의 범위·발송 상태','marketer','목적과 독자에 맞춰 초안, 제목, 다음 행동을 구성'),
 'templates/excel':('표·열 정의·원하는 계산','집계표 또는 스프레드시트','원문 값·수식·단위·누락·파일 열기','officer','입력 구조를 확인하고 집계, 수식, 서식, 파일 검토 순서로 진행'),
 'templates/financial':('실적·비용·성장 가정·기간','재무 모델 초안','가정과 실적 구분·수식·기간·현금흐름','accountant','가정을 별도로 기록하고 계산과 시나리오를 확인')}
tracks={'advertising':('광고 자료·기간·목표','광고 성과 분석과 개선안','marketer','지표 정의·계정·기간·예산 변경 여부'), 'commerce':('상품·주문·고객 자료','쇼핑몰 운영안','seller','상품 사실·계정·재고·게시 상태'), 'content':('원고·독자·채널','콘텐츠 초안','writer','원문·어투·권리·게시 상태'), 'data':('표·조사 질문·출처','데이터 분석 보고서','analyst','누락·단위·계산·해석'), 'documents':('초안·양식·파일 형식','문서 파일','officer','원문·서식·파일 열기'), 'finance':('재무 자료·가정·기간','재무 검토표','accountant','가정·기간·단위·계산'), 'hr':('직무·채용 기준·양식','채용·인사 문서','recruiter','직무 기준·개인정보·미정 조건'), 'legal':('문서·관할·검토 목적','법률 확인 목록','lawyer','원문 조항·공식 근거·관할'), 'marketing':('제품·고객·브랜드·목표','마케팅 실행안','marketer','주장 근거·대상·평가 기준'), 'operations':('업무 절차·팀 기준','운영 절차와 보고서','coworker','담당·인계·미정 사항'), 'product':('제품 문제·사용자 자료','제품 검토안','coworker','사용자 근거·요구와 가정·우선순위'), 'appendix':('학습 목표·연구 자료·공고','학습·연구 확인 목록','tutor','출처·목표·평가 기준')}
for slug,(inputs,out,role,checks) in tracks.items():D['tracks/track-'+slug]=(inputs,out,checks,role,'자료 확인, 요구 정리, 초안, 검토 순서로 진행')
for key,(inputs,out,checks,role,steps) in D.items():
 path=f'cookbook/{key}.md';old=BEFORE[path];title=re.search(r'^title:\s*"(.*)"',old,re.M).group(1)
 title=re.sub(r'^[①②③④⑤⑥⑦⑧⑨⑩⑪⑫]\s*','',title).replace('이직 준비 4주 플랜 실행하기','이직 준비 프로젝트')
 matching=[]
 for e in employees:
  for sk in e['skills']:
   name=sk['name']
   if re.search(r'(?<![\w-])'+re.escape(name)+r'(?![\w-])',old) and not name.endswith('-workflow'):
    matching.append((e['id'],name))
 matching=list(dict.fromkeys(matching))[:5]
 skills='\n'.join(f'- `{plugin}:{name}`' for plugin,name in matching)
 if not skills:skills=f'- [관련 역할의 스킬 목록](/moai-agents/{role}/)'
 page(path,title,f'{inputs}를 준비해 {out}을 만드는 실습',f'''
**이 실습의 결과는 {out}입니다.** ChatGPT Work와 Claude Cowork 모두 목표와 자료를 제공하는 방식으로 시작합니다. 실제 서비스 연결과 지원 도구는 현재 앱에서 확인하세요.

## 준비물

{inputs}를 준비합니다. 실습에서는 가상 자료나 공개 가능한 자료를 사용할 수 있습니다. [관련 역할](/moai-agents/{role}/)의 스킬을 추가하려면 [설치 안내](/plugins/install/)를 확인합니다.

## 첫 요청

```text
제공한 자료로 {out}을 만들어 줘.
목표·독자·결과 형식을 먼저 확인하고 부족한 정보는 질문해 줘.
{steps}해 줘.
자료 없는 사실과 수치는 만들지 말고 미정 항목을 표시해 줘.
외부 게시·발송·계정 변경 없이 검토용 결과부터 보여 줘.
```

## 진행 순서

1. **자료 확인:** {inputs} 중 읽을 수 있는 것과 없는 것을 구분합니다.
2. **맥락 확인:** 독자·형식·범위를 질문에 답해 정합니다.
3. **초안 작성:** {steps}합니다.
4. **검토:** {checks}을 확인합니다.
5. **수정·저장:** 변경할 부분을 지정하고 결과를 별도 위치에 저장합니다.

독립적인 조사만 병렬로 진행하고, 앞 결과가 필요한 작성·변환은 순차로 진행합니다. [전문가 분업](/workflows/experts/)의 역할·입출력 계약을 사용할 수 있습니다.

## 사용할 수 있는 스킬 후보

아래는 이 업무에 참고할 수 있는 패키지 기능입니다. 실제 설치·노출 상태를 먼저 확인하며 이 순서로 반드시 자동 실행된다는 뜻은 아닙니다.

{skills}

## 완료 기준

결과물에 사용 자료와 미확인 항목이 표시되어 있습니다. {checks}을 직접 확인했습니다. 파일을 요청한 경우 저장된 파일을 열어 확인합니다. 실제 게시·발송·예약 작업은 별도의 실행 결과로 확인합니다.

## 막혔을 때

자료나 연결이 없으면 제공 자료로 가능한 초안과 다음 준비 목록을 요청합니다. 원문·수치가 다르면 해당 위치와 근거를 지정해 고칩니다. 전문 판단이 필요한 부분은 근거와 쟁점을 정리하고 해당 업무 책임자가 확인합니다.

[결과 검토](/workflows/review/) · [반복 업무](/workflows/reuse/) · [다른 실습 선택](/cookbook/)
''',sources=[('관련 플러그인 원본',f'https://github.com/modu-ai/moai-cowork/tree/main/plugins/moai-{role}')])
page('cookbook/_index.md','업무별 실습','원하는 결과물로 실습을 선택하고 준비물·요청·검토를 따라갑니다', '''
**만들 결과물 하나를 고르세요.** 모든 실습은 준비물 → 첫 요청 → 진행 순서 → 완료 기준으로 읽습니다. ChatGPT Work와 Claude Cowork를 함께 다루며, 실제 연결 기능은 현재 환경에서 확인합니다.

| 원하는 결과 | 실습 |
|---|---|
| 보고서 | [주간보고](/cookbook/report-automation/) |
| 글과 콘텐츠 | [블로그](/cookbook/blog-pipeline/) · [SNS 달력](/cookbook/projects/sns-content-month/) |
| 사업 자료 | [사업계획서](/cookbook/business-plan/) · [IR 덱](/cookbook/ir-deck/) |
| 데이터 분석 | [공공데이터 보고서](/cookbook/projects/public-data-report/) |
| 고객지원 | [VOC → FAQ](/cookbook/projects/voc-to-faq/) |
| 문서 검토 | [계약서 검토](/cookbook/contract-review/) |

## 내 상황에 맞게 찾기

- [프로젝트 실습](/cookbook/projects/): 여러 역할을 이어서 결과물 만들기.
- [직무별 트랙](/cookbook/tracks/): 분야별 실습 선택.
- [주제별 가이드](/cookbook/guides/): 분석·콘텐츠·법률 등 업무 방법.
- [템플릿](/cookbook/templates/): 이메일·표·재무 초안.
- [디자인 원칙](/cookbook/design/): 발표 자료 구성.

처음이라면 [가상 메모로 첫 보고서](/getting-started/first-task/)를 만든 뒤 시작하세요. 반복 실행은 [반복 업무와 개선](/workflows/reuse/)에서 설정합니다.
''')
for sub,title in [('projects','프로젝트 실습'),('tracks','직무별 트랙'),('guides','주제별 가이드'),('templates','업무 템플릿'),('design','디자인 원칙')]:
 rows=[]
 for key in D:
  if key.startswith(sub+'/'):
   p=CONTENT/f'cookbook/{key}.md';t=re.search(r'^title:\s*"(.*)"',p.read_text(),re.M).group(1);rows.append(f'- [{t}](/cookbook/{key}/)')
 page(f'cookbook/{sub}/_index.md',title,'원하는 결과물을 고르고 준비물과 첫 요청부터 시작합니다','**원하는 결과물로 실습을 선택하세요.** 각 페이지에서 준비물, 첫 요청, 완료 기준을 확인할 수 있습니다.\n\n'+'\n'.join(rows)+'\n\n[전체 실습](/cookbook/) · [첫 프로젝트 구성](/workflows/first-project/)')
page('cookbook/skill-chaining.md','업무 단계를 이어 쓰기','앞 단계의 결과를 다음 단계에 전달하고 검토 기준을 유지합니다', '''
**스킬을 잇는다는 것은 업무 결과를 다음 단계에 전달하는 것입니다.** 이름을 나열하는 것만으로 실제 호출·인계가 완료되지는 않습니다.

## 주간보고 예

| 단계 | 입력 | 결과 | 확인 기준 |
|---|---|---|---|
| 자료 확인 | 업무 메모 | 사실·미정 목록 | 원문과 일치 |
| 작성 | 확인한 사실 | 보고서 초안 | 독자·분량·구조 |
| 문서 제작 | 검토한 초안 | 요청한 파일 | 열기·표·페이지 |
| 검토 | 결과물·원문 | 수정 목록 | 숫자·출처·누락 |

단계마다 담당 역할과 사용할 스킬을 현재 목록에서 확인합니다. 앞 결과가 필요한 단계는 순서대로, 독립적인 자료 조사는 병렬로 진행할 수 있습니다. 합칠 때는 기간·단위·중복을 확인합니다.

```text
이 보고서 업무를 자료 확인, 작성, 문서 제작, 검토로 나눠 줘.
각 단계에 실제 사용할 수 있는 스킬, 입력, 결과, 완료 기준을 지정해 줘.
실행하지 못한 단계는 완료로 표시하지 마.
```

[전문가 분업](/workflows/experts/) · [주간보고 실습](/cookbook/report-automation/)
''')
page('cookbook/best-practices.md','업무를 잘 맡기는 방법','목표·자료·질문·완료 기준으로 요청하고 검토 가능한 결과를 받습니다', '''
**원하는 결과와 판단 기준을 알려 주세요.** 요청이 짧아도 자료와 기준을 질문으로 보완할 수 있습니다.

1. 목표를 하나로 정합니다. “이 자료로 팀장용 주간보고를 만들어 줘.”
2. 사용할 자료와 기준 시점을 제공합니다.
3. 독자·형식·제약을 알려 주고 미정 항목은 남깁니다.
4. 현재 사용할 스킬과 연결 도구를 확인합니다.
5. 초안을 검토한 뒤 수정할 부분을 지정합니다.
6. 실제 파일·조회·발송·예약 결과를 각각 확인합니다.

## 좋은 요청 예

```text
첨부 메모로 팀장용 주간보고를 한 장으로 만들어 줘.
없는 수치는 만들지 말고 부족한 정보는 질문해 줘.
초안과 미확인 항목을 먼저 보여 줘.
```

같은 방식이 잘되면 [프로젝트 지침](/getting-started/projects/)에 남기세요. 숫자·차트·코드도 각각 계산·단위·실행을 확인하며, 문장 다듬기와 사실 검증은 따로 봅니다.

[첫 실습](/getting-started/first-task/) · [결과 검토](/workflows/review/)
''')
page('cookbook/automation-recipes.md','반복 업무와 예약 실습','한 번 검토한 업무를 현재 앱의 예약 기능으로 반복하고 실행 결과를 확인합니다', '''
**예약은 수동 작업이 잘된 뒤 설정하세요.** 예를 들어 주간보고 초안을 한 번 확인하고, 반복할 자료·주기·저장 위치를 정합니다.

## 준비물

검토한 업무 흐름, 자료 접근 방식, 사용할 계정, 시간대와 주기, 결과 전달 범위를 준비합니다. 현재 앱의 예약 기능과 로컬·클라우드 실행을 확인합니다.

```text
이 보고서 작업을 반복하고 싶어. 예약 기능과 자료 접근이 가능한지 확인해 줘.
한국 시간 기준 주기와 결과 저장 위치를 질문해 줘.
외부 발송은 제외하고 검토용 초안을 만들도록 구성해 줘.
실제 등록된 예약 항목과 첫 실행 결과도 확인해 줘.
```

## 확인 순서

1. 동일 자료로 수동 실행하고 결과 검토.
2. 예약 기능·필요한 컴퓨터 접근 확인.
3. 주기·시간대·연결 계정·결과 범위 지정.
4. 실제 예약 목록에서 등록 상태 확인.
5. 첫 실행의 결과·오류·미확인 사항 확인.

컴퓨터가 필요 없는 클라우드 작업과 로컬 파일을 읽는 작업은 조건이 다릅니다. 실패하면 입력·연결·예약 실행 중 어디서 멈췄는지 기록합니다. 자동 게시나 발송은 초안 작성과 별도 실행 범위로 설정합니다.

[반복 업무와 개선](/workflows/reuse/) · [주간보고 실습](/cookbook/report-automation/)
''',sources=[('ChatGPT 예약 작업','https://learn.chatgpt.com/docs/scheduled-tasks'),('Claude Cowork',CLAUDE)])
page('cookbook/troubleshooting.md','실습이 막혔을 때','자료·기능·인계·결과를 확인해 실패한 단계를 찾습니다', '''
**어느 단계가 끝났고 어느 단계가 멈췄는지 확인하세요.** 전체를 다시 실행하기 전에 실패한 입력과 결과를 찾습니다.

| 막힌 곳 | 확인 항목 | 요청 예 |
|---|---|---|
| 자료 읽기 | 파일·폴더·실행 환경 | 읽은 파일과 못 읽은 파일을 알려 줘 |
| 스킬 선택 | 설치·현재 노출 | 추천과 실제 사용 가능한 기능을 나눠 줘 |
| 단계 인계 | 앞 결과·형식·미정 정보 | 다음 단계에 필요한 입력을 확인해 줘 |
| 결과 검토 | 숫자·출처·파일 | 원문과 다른 위치만 고쳐 줘 |
| 반복 실행 | 예약 목록·계정·컴퓨터 접근 | 등록과 실제 실행 결과를 구분해 줘 |

연결 문제는 [MCP 문제 해결](/plugins/mcp/troubleshooting/)에서 확인합니다. 같은 수정이 반복되면 [프로젝트 기준](/getting-started/projects/)에 반영합니다.
''')
existing=json.loads((ROOT/'reports/20261005-docs-rebuild/authored-pages.json').read_text()); existing+=changed
(ROOT/'reports/20261005-docs-rebuild/authored-pages.json').write_text(json.dumps(existing,ensure_ascii=False,indent=2)+'\n')
print('Cookbook pages rebuilt:',len(changed))
