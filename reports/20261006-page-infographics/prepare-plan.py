"""페이지별 그림 계획과 본문 근거를 저장한다. 문서와 이미지에는 아직 쓰지 않는다."""
from pathlib import Path
import hashlib,json,re

ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent

def spec(title,mode,cards,note):
    return {'title':title,'mode':mode,'cards':cards,'note':note}

SPECS={
'learning-path':spec('처음부터 내 업무 적용까지','flow',[
 ['작게 시작','목표 하나와 예제 자료로 첫 초안을 만듭니다.'],
 ['프로젝트 준비','계속 쓸 지침과 이번 자료를 구분합니다.'],
 ['필요한 기능 선택','실제 사용할 스킬과 역할을 확인합니다.'],
 ['검토하고 재사용','원문과 비교한 기준을 다음 작업에 남깁니다.']],
 '순서를 외우기보다 각 단계에서 확인한 결과를 설명해 보세요.'),
'environment':spec('앱 이름보다 실제 접근 범위 확인','compare',[
 ['ChatGPT Work','현재 화면에서 Work 작업을 시작할 위치를 찾습니다.'],
 ['Claude Cowork','Cowork 또는 통합 입력창에서 작업을 시작합니다.'],
 ['웹에 제공한 자료','업로드·연결한 자료를 실제 읽었는지 확인합니다.'],
 ['컴퓨터의 파일','실행 위치와 컴퓨터 연결, 폴더 접근을 확인합니다.']],
 '웹 프로젝트 생성과 컴퓨터 폴더 연결은 각각 확인해야 합니다.'),
'questions':spec('질문을 받았을 때 이렇게 답하세요','compare',[
 ['알고 있는 정보','선택지를 고르거나 직접 답합니다. 답이 반영됐는지 확인합니다.'],
 ['아직 모르는 정보','미정·자료 없음으로 남깁니다. 건너뛰기는 답변 완료가 아닙니다.'],
 ['꼭 필요한 정보','해당 작업은 기다리고 필요한 자료나 결정을 요청합니다.'],
 ['독립적으로 가능한 일','미정 조건과 무관한 목차·초안은 진행할 수 있습니다.']],
 '이미 답한 목적·독자·형식을 다시 묻지 않도록 작업 맥락에 남깁니다.'),
'report-status':spec('같은 숫자라도 상태가 다릅니다','compare',[
 ['문의 12건','답변을 완료한 사실입니다. 원문 수치와 비교합니다.'],
 ['FAQ 4개','검토 전 초안입니다. 최종 완료로 바꾸지 않습니다.'],
 ['배송 지연 원인','아직 확인하지 못했습니다. 원인을 추측하지 않습니다.'],
 ['다음 행동','안내문 수정과 FAQ 검토. 담당자·기한이 없으면 미정입니다.']],
 '강의용 가상 메모입니다. 자연스러운 문장보다 숫자와 상태의 일치를 확인하세요.'),
'install-states':spec('설치부터 실행까지, 증거가 다릅니다','compare',[
 ['카탈로그에 있음','패키지의 공개된 구성만 확인한 상태입니다.'],
 ['설치되어 있음','내 앱의 설치 상태를 확인한 것입니다.'],
 ['현재 작업에 노출','스킬·도구가 이 작업에서 보이는지 확인합니다.'],
 ['작은 예제 실행','실제 결과를 받고 원문과 비교해야 실행을 확인할 수 있습니다.']],
 '설치됨 표시만으로 인증 성공이나 전체 업무 완료를 보고하지 않습니다.'),
'pm-setup':spec('내 프로젝트에 맞는 지침 만들기','flow',[
 ['맥락과 실제 기능','목표·독자·자료를 질문하고 사용할 스킬과 도구를 확인합니다.'],
 ['역할과 업무 순서','각 역할의 입력·출력·완료 기준과 인계 조건을 정합니다.'],
 ['지침 생성과 적용','지원되는 프로젝트 지침 경로에 저장하고 새 작업에서 읽기를 확인합니다.'],
 ['첫 업무와 결과 검토','작은 업무를 실행해 결과 파일과 미정 항목을 확인합니다.']],
 '지침 파일 생성, 앱 Projects 저장, 실제 참조는 서로 다른 상태입니다.'),
'review':spec('완료 보고보다 결과물을 확인하세요','compare',[
 ['사실과 출처','원문을 나란히 보고 출처가 주장을 뒷받침하는지 확인합니다.'],
 ['숫자와 상태','기간·단위·합계와 초안·완료·미정 상태를 비교합니다.'],
 ['파일과 서식','다운로드한 파일을 열어 글꼴·표·페이지·수식을 확인합니다.'],
 ['실제 실행','조회·저장·게시·발송은 각각의 실제 결과를 확인합니다.']],
 '수정할 위치와 근거를 지정합니다. 자기 점검과 별도 검토자 실행도 구분하세요.'),
'reuse':spec('잘된 업무를 반복하는 순서','flow',[
 ['한 번 실행하고 검토','원본과 결과가 맞는 작은 업무부터 확인합니다.'],
 ['유지할 기준 저장','독자·형식·검토 기준은 지침에, 이번 숫자는 새 자료에 둡니다.'],
 ['반복 조건 확인','주기·시간대·자료 접근·결과 위치와 실행 범위를 정합니다.'],
 ['등록과 첫 실행 확인','실제 예약 목록을 확인하고 첫 결과와 오류를 직접 봅니다.']],
 '예약 등록과 예약 실행 성공은 다릅니다. 새 자료로 다시 확인하세요.'),
'permissions':spec('원본에서 결과까지 접근을 확인','flow',[
 ['원본 자료 지정','업로드한 파일이나 허용한 폴더, 읽을 파일 이름을 정합니다.'],
 ['읽은 내용 확인','행 수·제목·기간을 원본과 비교하고 못 읽은 자료는 남깁니다.'],
 ['결과 별도 저장','원본을 보존하고 결과의 이름과 저장 위치를 지정합니다.'],
 ['파일 열고 상태 확인','실제 파일 열기와 외부 게시·발송 상태를 각각 확인합니다.']],
 '폴더가 보임, 파일을 읽음, 결과를 저장함은 같은 뜻이 아닙니다.'),
'account':spec('세 가지 계정 범위를 나눠 보세요','compare',[
 ['앱 로그인 계정','지금 누구로 로그인했는지 확인합니다.'],
 ['조직·워크스페이스','프로젝트 공개 범위와 설치·실행 정책을 확인합니다.'],
 ['연결 서비스 계정','실제 조회에 사용한 외부 계정과 권한을 확인합니다.'],
 ['결과와 출처','어느 계정·기간의 자료인지 결과에 남깁니다.']],
 '다른 프로젝트의 인증 정보를 덮어쓰지 않고 키·토큰을 공유 대화에 넣지 않습니다.'),
'cost':spec('무료 패키지와 서비스 비용은 별개','compare',[
 ['MoAI 패키지','플러그인 소스의 이용 조건을 확인합니다.'],
 ['AI 앱 이용','본인 계정의 현재 요금제와 지원 범위를 확인합니다.'],
 ['외부 생성 서비스','이미지·영상 등 서비스의 크레딧과 사용량을 확인합니다.'],
 ['API·조직 설정','API 청구·한도와 조직의 관리 조건을 확인합니다.']],
 '첫 실습은 가상 텍스트로 시작합니다. 가격을 그림에 고정하지 않습니다.'),
'handoff':spec('새 작업에 넘길 맥락은 직접 남기기','flow',[
 ['결과 중심으로 작업','보고서·시안·분석처럼 목표별로 기록을 나눕니다.'],
 ['결정과 남은 질문','최종 결과·결정 사항·미정 항목을 정리합니다.'],
 ['지침과 자료에 보관','다음 작업에 필요한 기준과 결과를 저장합니다.'],
 ['새 작업에서 확인','어떤 자료와 기준을 실제 참조했는지 확인합니다.']],
 '다른 대화의 모든 맥락이 자동으로 전달된다고 가정하지 않습니다.'),
'personalization':spec('기준마다 저장할 곳이 다릅니다','compare',[
 ['개인 취향','쉬운 한국어 같은 공통 취향 → 지원되는 개인 설정'],
 ['프로젝트 규칙','보고서 한 장·수치 추측 금지 → 프로젝트 지침'],
 ['반복 업무 방법','자료 확인·초안·검토 순서 → 스킬과 업무 절차'],
 ['이번 결과 수정','이 문단만 짧게 → 현재 작업의 수정 요청']],
 '저장한 뒤 새 작업에서 적용을 확인합니다. 중요한 기준을 메모리에만 맡기지 않습니다.'),
'attribution':spec('출처와 권리를 함께 남기세요','compare',[
 ['웹 자료','제목·원문 링크·확인일을 기록합니다.'],
 ['통계와 표','기관·자료명·기준 기간·단위를 기록합니다.'],
 ['내부 자료','허용된 문서 이름·버전·기준일을 남깁니다.'],
 ['사진·글·코드','이용 조건·권리·필요한 고지를 각각 확인합니다.']],
 'AI 사용 표시는 원문 출처와 자료의 이용 조건 확인을 대신하지 않습니다.'),
'office':spec('Office 작업의 세 가지 방식','compare',[
 ['문서 파일 제작','제공 자료로 DOCX·XLSX·PPTX 파일을 만듭니다.'],
 ['계정 문서 연결','인증된 서비스의 문서를 조회·수정합니다.'],
 ['앱 추가 기능','Office 앱 안에서 지원되는 사이드바 기능을 사용합니다.'],
 ['방식에 맞는 확인','파일 열기, 실제 계정 변경, 추가 기능 지원을 각각 확인합니다.']],
 '파일 생성, 클라우드 저장, 공유, 메일 발송은 각각의 실행 결과를 확인하세요.'),
'limits':spec('큰 작업을 확인 가능한 단위로 나누기','flow',[
 ['결과물 하나 정하기','이번에 만들 결과와 완료 기준을 정합니다.'],
 ['필요한 자료 선택','목차·범위를 확인하고 필요한 원본을 제공합니다.'],
 ['수정할 위치 지정','전체 재작성보다 틀린 위치와 근거를 알려 줍니다.'],
 ['기준과 남은 일 기록','반복 기준은 지침에, 미완료 업무는 다음 작업에 남깁니다.']],
 '계정 사용량 한도와 자료 길이는 별도로 확인합니다.'),
'troubleshooting':spec('멈춘 단계를 찾고 그 부분부터 확인','compare',[
 ['준비·노출','앱 환경과 설치·활성화·현재 스킬 목록을 확인합니다.'],
 ['자료·연결','파일 읽기와 실제 계정·인증·조회 결과를 확인합니다.'],
 ['작성·인계','앞 결과와 필요한 입력, 미정 조건을 확인합니다.'],
 ['검토·반복','원문 차이와 예약 등록·첫 실행 결과를 확인합니다.']],
 '관측한 오류를 기록합니다. 실행하지 못한 단계는 완료로 표시하지 않습니다.'),
'credentials':spec('계정별 인증 정보와 조회를 분리','flow',[
 ['서비스와 계정 선택','어느 프로젝트에서 어떤 계정 자료가 필요한지 정합니다.'],
 ['지원되는 경로로 설정','비밀정보 입력란 또는 해당 서버의 자격증명 파일을 사용합니다.'],
 ['읽기 전용 조회','키 이름·권한·만료와 실제 연결 계정을 확인합니다.'],
 ['계정과 결과 비교','올바른 계정·기간의 결과인지 확인하고 빈 결과와 오류를 구분합니다.']],
 '자격증명 파일 생성은 인증 성공이 아닙니다. 키·토큰은 그림이나 채팅에 넣지 않습니다.'),
'server-modes':spec('MCP: 실행 위치와 연결 방식을 따로 확인','compare',[
 ['로컬 서버','실행 환경에 필요한 프로그램과 서버 시작 상태를 확인합니다.'],
 ['원격 서버','접속 가능한 서버와 지원되는 인증 경로를 확인합니다.'],
 ['웹·클라우드 작업','컴퓨터의 로컬 서버를 자동 사용할 수 있다고 가정하지 않습니다.'],
 ['실제 조회','현재 작업의 도구와 인증 계정으로 자료를 읽어 확인합니다.']],
 '패키지 설정, 도구 노출, 실제 조회 성공은 각각의 근거가 필요합니다.'),
'connector':spec('외부 연결을 확인하는 네 단계','flow',[
 ['호스트·서버 방식','웹·데스크톱·클라우드와 로컬·원격 방식을 확인합니다.'],
 ['필요한 실행 도구','로컬 실행에 필요한 경우에만 uv·Node.js 등을 준비합니다.'],
 ['계정 인증','해당 서비스가 지원하는 로그인 또는 비밀정보 설정을 사용합니다.'],
 ['작은 조회와 검토','필요한 범위만 읽고 계정·기간·자료를 직접 확인합니다.']],
 '버전 출력만으로 플러그인 로드·서버 시작·계정 인증까지 확인된 것은 아닙니다.'),
'skills-agents':spec('업무 방법과 실행 역할을 구분','compare',[
 ['스킬 사용','업무 지침을 읽고 해당 방법을 적용합니다.'],
 ['별도 에이전트','지원되는 도구가 실제로 별도 역할을 실행합니다.'],
 ['독립 검토','별도 실행과 읽기 권한 제한을 확인한 경우에 기록합니다.'],
 ['자기 점검','같은 실행이 자기 결과를 다시 읽어 확인합니다.']],
 '스킬 이름을 말한 것과 별도 에이전트 실행은 다릅니다. 현재 호스트 기능을 확인하세요.'),
'team-handoff':spec('다음 담당자에게 전달할 네 묶음','compare',[
 ['목표와 역할','무엇을 만들고 누가 맡을지 지정합니다.'],
 ['자료와 앞 결과','원본·버전·앞 단계 결과와 출처를 전달합니다.'],
 ['미정 정보와 질문','모르는 값과 필요한 질문을 함께 넘깁니다.'],
 ['출력과 완료 기준','형식·저장 위치·검토 조건을 정합니다.']],
 '독립된 작업만 병렬 후보입니다. 기간·단위·중복을 맞춘 뒤 합치세요.'),
'verification':spec('어떤 확인을 했는지 범위를 밝히기','compare',[
 ['정적 계약 검사','형식·필드·참조를 확인합니다. 설치·인증의 증거는 아닙니다.'],
 ['도구 목록·단위 검사','정의와 지정된 동작을 확인합니다. 외부 조회 전체를 대신하지 않습니다.'],
 ['대표 업무 실행','실제로 실행한 예제와 결과만 평가합니다.'],
 ['사용자 여정 확인','앱에서 자료·기능·결과 흐름을 확인하고 환경을 기록합니다.']],
 '검증 명령·출력·트리·범위를 남깁니다. 미실행 예제는 통과로 표시하지 않습니다.'),
'authoring':spec('온라인 강의 한 페이지를 만드는 순서','flow',[
 ['목표와 쉬운 설명','수업 후 할 수 있는 일을 정하고 처음 보는 개념을 풉니다.'],
 ['그림과 실제 예제','개념도와 직접 촬영한 화면을 구분하고 자료·요청을 준비합니다.'],
 ['실습과 검토','예상 결과·흔한 실수·확인 문제와 해설을 제공합니다.'],
 ['게시 전 문서 확인','출처·링크·그림·검색·모바일·기존 주소를 확인합니다.']],
 '생성한 개념 그림을 실제 앱 화면으로 표시하지 않습니다.'),
'teaching':spec('설명에서 직접 수행까지 이어지는 수업','flow',[
 ['개념 설명과 시연','그림의 관계를 짚고 같은 가상 자료로 예제를 보여 줍니다.'],
 ['수강생 개별 실습','직접 요청하고 필요한 질문에 답하게 합니다.'],
 ['원문과 결과 비교','숫자·미정 상태·정책 근거를 비교하게 합니다.'],
 ['해설과 내 업무 과제','답의 이유를 설명하고 자기 업무의 검토 기준을 작성합니다.']],
 '모범 결과와 수강생의 실제 수행은 구분합니다. 앱이 막히면 미실행 상태를 기록합니다.'),
'choose-recipe':spec('결과물로 실습과 역할을 고르세요','compare',[
 ['보고·기획·문서','보고서와 문서 파일 → 코워커·사무관 실습'],
 ['콘텐츠·시안','글·캠페인·발표 → 작가·마케터·디자이너 실습'],
 ['분석·고객지원','표·자료·FAQ → 애널리스트·CS 실습'],
 ['여러 분야의 프로젝트','역할과 인계 조건을 PM으로 정리합니다.']],
 '선택 후보를 현재 설치·노출된 기능과 비교하고 작은 결과부터 확인하세요.'),
'higgsfield':spec('생성 도구 연결과 제작을 분리','flow',[
 ['목적과 기능 확인','만들 이미지·영상과 현재 제공되는 도구를 확인합니다.'],
 ['제품별 연결 경로','Claude의 공식 MCP, ChatGPT의 공식 플러그인 경로를 확인합니다.'],
 ['계정과 사용 범위','로그인·이용 조건·크레딧과 실행 범위를 확인합니다.'],
 ['작은 결과 검토','실제 생성 결과의 글자·형태·권리와 저장 파일을 확인합니다.']],
 '설정과 제작 성공은 다릅니다. 지원 기능·비용은 현재 공식 안내에서 확인하세요.'),
}

MAPPING={
'advanced/_index.md':'verification','advanced/documentation.md':'authoring','advanced/plugins.md':'install-states','advanced/verification.md':'verification',
'cookbook/_index.md':'choose-recipe','cookbook/automation-recipes.md':'reuse','cookbook/best-practices.md':'learning-path','cookbook/design/_index.md':'choose-recipe','cookbook/guides/_index.md':'choose-recipe','cookbook/projects/_index.md':'pm-setup','cookbook/skill-chaining.md':'team-handoff','cookbook/templates/_index.md':'office','cookbook/tracks/_index.md':'choose-recipe','cookbook/troubleshooting.md':'troubleshooting',
'getting-started/_index.md':'learning-path','getting-started/choose-app.md':'environment','getting-started/first-task.md':'report-status','getting-started/questions.md':'questions',
'help/_index.md':'troubleshooting','help/about-claude.md':'environment','help/account.md':'account','help/attribution.md':'attribution','help/conversations.md':'handoff','help/office/_index.md':'office','help/office/microsoft-365.md':'office','help/personalization.md':'personalization','help/plans-billing.md':'cost','help/source-index.md':'learning-path','help/troubleshooting.md':'troubleshooting','help/usage-limits.md':'limits',
'learn/03-first-result.md':'report-status','learn/04-skills-plugins.md':'install-states','learn/06-review-reuse.md':'reuse','learn/teaching-guide.md':'teaching',
'moai-agents/_index.md':'choose-recipe','moai-agents/pm.md':'pm-setup',
'plugins/_index.md':'choose-recipe','plugins/agents.md':'skills-agents','plugins/higgsfield-setup.md':'higgsfield','plugins/mcp/_index.md':'server-modes','plugins/mcp/credentials.md':'credentials','plugins/mcp/install.md':'connector','plugins/mcp/troubleshooting.md':'troubleshooting','plugins/teams.md':'team-handoff',
'workflows/_index.md':'pm-setup','workflows/first-project.md':'pm-setup','workflows/permissions.md':'permissions','workflows/reuse.md':'reuse','workflows/review.md':'review'
}

facts=json.loads((OUT/'example-facts.json').read_text())
for f in facts:
    path=Path(f['path']);rel=str(path.relative_to('www/content'));s=(ROOT/path).read_text()
    title=f['title'].strip('"');title=title.split(' — ')[0].strip('「」')
    if f['sequence']:
        inputs=f['inputs'].split('를 준비합니다')[0].split('을 준비합니다')[0]
        work=re.search(r'3\. \*\*초안 작성:\*\* (.*)',f['sequence']).group(1)
        review=re.search(r'4\. \*\*검토:\*\* (.*)',f['sequence']).group(1)
        result=re.search(r'이 실습의 결과는 (.+?)입니다',s).group(1)
    else:
        row=re.search(r'^\| ([^|]+) \| ([^|]+) \| 제공 자료',s,re.M)
        assert row,rel
        inputs,result=row.group(1),row.group(2)
        first=re.search(r'## 첫 요청\s+```text\n(.*?)\n',s,re.S).group(1)
        work=first;review='제공 자료와 결과를 비교하고 미정 항목을 구분합니다.'
    key='example-'+rel.replace('/','-').removesuffix('.md')
    SPECS[key]=spec(title+' 한눈에 보기','flow',[
        ['준비할 자료',inputs],['작업의 핵심',work],['검토 기준',review],['만들 결과',result]],
        f['mistake'].strip())
    SPECS[key]['example']={'input':f['example'].strip(),'expected':f['expected'].strip()}
    MAPPING[rel]=key

rows=[]
for p in sorted((ROOT/'www/content').rglob('*.md')):
    rel=str(p.relative_to(ROOT/'www/content'));s=p.read_text();images=re.findall(r'!\[[^\]]*\]\(([^)]+)\)',s)
    title=re.search(r'^title: (.+)',s,re.M).group(1).strip('"')
    if rel in MAPPING:
        key=MAPPING[rel];action='추가';asset='/infographics/pages/'+key+'.svg';reason=SPECS[key]['title'];priority='High' if rel.split('/')[0] in ('learn','getting-started','workflows','plugins') else 'Medium'
    elif images or rel=='releases/_index.md':
        action='유지';asset=' · '.join(images) or '기존 Mermaid 버전 관계도';reason='기존 개념도·실제 캡처·관계도가 핵심 내용을 설명함';priority='Low'
    else:
        action='추가하지 않음';asset='';reason='과거 변경 기록 또는 권리·고지 원문과 표를 보존하고 현재 기능 그림을 섞지 않음';priority='Low'
    rows.append({'path':rel,'title':title,'source_sha256':hashlib.sha256(s.encode()).hexdigest(),'source_bytes':len(s.encode()),'headings':re.findall(r'^#{1,3} (.+)',s,re.M),'existing_images':images,'action':action,'asset':asset,'reason':reason,'priority':priority})
assert len(rows)==171
(OUT/'page-plan.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
(OUT/'diagram-specs.json').write_text(json.dumps(SPECS,ensure_ascii=False,indent=2)+'\n')
plan='''# 페이지별 인포그래픽 추가 계획

작성일: 2026년 10월 6일

171개 Markdown의 본문·제목·구조·기존 그림을 읽어 계획의 근거와 해시를 기록했다. 현재 사용 문서는 준비물, 작업 순서, 결과와 검토 기준을 비교했다. 반복 설명은 공통 문단과 페이지 고유 내용을 나누어 살폈다. 과거 릴리스는 당시 변경 기록을 보존한다.

## 제작 순서와 기준

1. 질문·설치·프로젝트·검토의 핵심 관계와 혼동을 설명한다.
2. 업무별 실습 42개와 역할 안내 17개에는 해당 본문에서 뽑은 자료·업무·검토·결과와 가상 예제를 넣는다.
3. 도움말과 고급 설정에는 계정·비용·연결·검증 범위의 비교도를 넣는다.
4. 같은 개념을 설명하는 페이지는 같은 그림을 재사용한다. 기존 개념도·실제 캡처가 충분한 페이지와 과거 변경 기록에는 새 그림을 중복해서 넣지 않는다.
5. SVG 원본으로 한글과 숫자를 정확히 조판하고 확대 시 읽을 수 있게 한다. 실제 앱 화면과 구분하고 이미지 아래에 내용을 설명한다. 별도 생성 API는 사용하지 않는다.
6. XML·경로·본문 근거·배치·실제 브라우저 표시를 확인한다. 이 확인은 제품의 실제 연결·설치·업무 실행을 대신하지 않는다.

## 페이지별 결정

| 페이지 | 우선순위 | 결정 | 설명할 내용 | 그림 |
|---|---|---|---|---|
'''
for row in rows:
    plan+='| '+row['path']+' | '+row['priority']+' | '+row['action']+' | '+row['reason']+' | '+row['asset']+' |\n'
(OUT/'plan.md').write_text(plan)
from collections import Counter
print(json.dumps({'pages':len(rows),'actions':dict(Counter(r['action'] for r in rows)),'new_diagrams':len(SPECS)},ensure_ascii=False))
