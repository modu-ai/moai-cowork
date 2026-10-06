from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
W=ROOT/'www'

groups=[
('시작하기','lightbulb',True,[('홈','/'),('처음 방문했다면','/getting-started/'),('사용 환경 선택','/getting-started/choose-app/'),('앱과 웹 준비','/getting-started/install/'),('첫 결과물 만들기','/getting-started/first-task/'),('핵심 개념','/getting-started/concepts/'),('내 프로젝트 설정','/getting-started/projects/'),('질문에 답하는 방법','/getting-started/questions/')]),
('온라인 강의실','book',True,[('수업 안내','/learn/'),('1강 · 업무 맡기기','/learn/01-delegation/'),('2강 · 프로젝트와 자료','/learn/02-project-context/'),('3강 · 질문과 첫 결과','/learn/03-first-result/'),('4강 · 스킬과 플러그인','/learn/04-skills-plugins/'),('5강 · 전문가 업무 순서','/learn/05-expert-workflow/'),('6강 · 검토와 반복 업무','/learn/06-review-reuse/'),('실제 화면 안내','/learn/screens/'),('강사용 수업 안내','/learn/teaching-guide/')]),
('내 업무에 적용','chef',False,[('프로젝트 업무 흐름','/workflows/'),('첫 프로젝트','/workflows/first-project/'),('전문가 분업','/workflows/experts/'),('파일과 권한','/workflows/permissions/'),('결과 검토','/workflows/review/'),('반복 업무','/workflows/reuse/'),('업무별 실습','/cookbook/'),('실전 프로젝트','/cookbook/projects/'),('분야별 학습','/cookbook/tracks/'),('작성 템플릿','/cookbook/templates/'),('업무 가이드','/cookbook/guides/'),('디자인 실습','/cookbook/design/')]),
('스킬과 플러그인','plug',False,[('기능과 설치 안내','/plugins/'),('설치와 관리','/plugins/install/'),('에이전트 이해','/plugins/agents/'),('팀 구성','/plugins/teams/'),('MCP 연결','/plugins/mcp/'),('MCP 설정','/plugins/mcp/install/'),('API 키와 인증','/plugins/mcp/credentials/'),('연결 문제 해결','/plugins/mcp/troubleshooting/'),('Higgsfield 설정','/plugins/higgsfield-setup/'),('산출물 권리','/plugins/license/'),('오픈소스 고지','/plugins/open-source/')]),
('역할별 코워커','bot',False,[('역할 선택','/moai-agents/'),('PM','/moai-agents/pm/'),('코워커','/moai-agents/coworker/'),('작가','/moai-agents/writer/'),('스토리 크리에이터','/moai-agents/story/'),('마케터','/moai-agents/marketer/'),('미디어 크리에이터','/moai-agents/media/'),('셀러','/moai-agents/seller/'),('사무관','/moai-agents/officer/'),('데이터 애널리스트','/moai-agents/analyst/'),('법무','/moai-agents/lawyer/'),('재무세무','/moai-agents/accountant/'),('인사채용','/moai-agents/recruiter/'),('CS매니저','/moai-agents/cs/'),('컨설턴트','/moai-agents/consultant/'),('커리어코치','/moai-agents/career/'),('튜터','/moai-agents/tutor/'),('디자이너','/moai-agents/designer/'),('SNS 크리에이터','/moai-agents/threads-poster/')]),
('도움말','question',False,[('문제 찾기','/help/'),('두 앱 알아보기','/help/about-claude/'),('계정','/help/account/'),('대화와 결과','/help/conversations/'),('개인화','/help/personalization/'),('요금과 결제','/help/plans-billing/'),('사용량','/help/usage-limits/'),('문제 해결','/help/troubleshooting/'),('Office 파일','/help/office/'),('출처 표기','/help/attribution/'),('공식 자료 색인','/help/source-index/')]),
('고급 설정과 운영','star',False,[('고급 문서','/advanced/'),('개발자 설치','/advanced/plugins/'),('검증과 배포','/advanced/verification/'),('문서 제작과 촬영','/advanced/documentation/'),('문서 개편 기록','/releases/docs-20261005/'),('릴리스 정보','/releases/'),('이전 릴리스','/releases/archive/')])]
lines=['main:']
for name,icon,opened,items in groups:
 lines += [f'  - name: {name}',f'    icon: {icon}',f'    defaultOpen: {str(opened).lower()}','    sub:']
 for label,ref in items:lines += [f'      - name: {label}',f'        ref: {ref}']
(W/'data/menu/main.yaml').write_text('\n'.join(lines)+'\n')

for path in [W/'content/_index.md',W/'content/plugins/_index.md']:
 s=path.read_text().replace('catalog-count "employees"','catalog-count "plugins"')
 if path.name=='_index.md' and path.parent==W/'content':
  s=s.replace('## MoAI-Cowork는 이렇게 씁니다','## 설명을 보며 차근차근 배우세요\n\n[온라인 강의실](/learn/)에는 개념 그림과 실제 화면, 예제 자료, 모범 결과, 확인 문제를 함께 담았습니다. 강의에서 처음부터 따라 하거나 혼자 복습할 수 있습니다.\n\n## MoAI-Cowork는 이렇게 씁니다')
 path.write_text(s)

for path in [W/'content/getting-started/install.md',W/'content/plugins/install.md']:
 s=path.read_text().replace('/screenshots/20261005/claude-customize.png','/screenshots/20261005/claude-plugins.jpg').replace('Claude Desktop을 직접 실행해 확인한 사용자 지정 화면','Claude 웹에서 직접 확인한 사용자 지정의 플러그인 화면').replace('Claude Desktop의 사용자 지정 → 플러그인 화면을 직접 촬영한 예시','Claude 웹의 사용자 지정 → 플러그인 화면을 직접 촬영한 예시')
 if path.parent.name=='getting-started':
  s=s.replace('![Claude 웹에서 직접 확인한 사용자 지정의 플러그인 화면](/screenshots/20261005/claude-plugins.jpg)','![Claude 웹에서 Cowork를 선택한 실제 작업 시작 화면](/screenshots/20261005/claude-cowork-start.jpg)')
 s=s.replace('두 캡처는 2026년','두 캡처는 웹 화면이며 2026년')
 s=s.replace('## Claude Cowork\n','![ChatGPT 웹의 공개 플러그인 목록을 직접 촬영한 화면](/screenshots/20261005/chatgpt-plugins.jpg)\n\n## Claude Cowork\n')
 path.write_text(s)

for rel,image,alt in [
 ('getting-started/projects.md','project-context-ko','프로젝트와 로컬 폴더의 차이와 연결 순서'),
 ('workflows/experts.md','expert-workflow-ko','분석 후 독립적인 작성 작업을 진행하고 합쳐서 검토하는 순서')]:
 p=W/'content'/rel;s=p.read_text();pos=s.index('\n## ');s=s[:pos]+f'\n\n![{alt}](/infographics/{image}.png)\n'+s[pos:];p.write_text(s)

(W/'content/learn/screens.md').write_text('''---
title: "실제 화면으로 시작 위치 찾기"
description: "ChatGPT Work와 Claude Cowork 웹을 직접 실행해 촬영한 입력창과 플러그인 메뉴"
weight: 80
date: 2026-10-05T00:00:00+09:00
lastmod: 2026-10-05T00:00:00+09:00
---

**아래 이미지는 2026년 10월 5일 실제 웹사이트에 접속해 촬영했습니다.** 그림으로 재현한 화면이 아닙니다. 사용하는 계정·조직·앱 버전에 따라 메뉴와 기능이 달라질 수 있으므로 이름과 위치를 함께 확인하세요.

## ChatGPT Work 입력창

![ChatGPT 웹의 Work 선택 상태와 프로젝트·파일·플러그인 메뉴](/screenshots/20261005/chatgpt-web-start.jpg)

화면 위에서 **Work**가 선택된 상태입니다. 가운데에 업무 요청을 입력합니다. 아래의 **프로젝트 선택**은 어느 업무 공간에서 진행할지 정하는 메뉴이고, **파일**은 필요한 자료를 제공하는 경로이며, **플러그인**은 사용할 기능을 찾는 메뉴입니다. 이 캡처만으로 로컬 폴더가 연결되었다고 판단할 수는 없습니다.

실습은 [첫 보고서 요청](/learn/03-first-result/#실습-요청)을 입력하는 것으로 시작합니다. 글을 붙여 넣은 뒤 전송하면 앱이 자료를 읽고 질문하거나 초안을 만듭니다.

## Claude Cowork 입력창

![Claude 웹의 Cowork 선택 상태와 프로젝트 메뉴가 표시된 입력창](/screenshots/20261005/claude-cowork-start.jpg)

입력창 아래에서 **Cowork**가 선택되어 있습니다. 같은 창에서 **채팅**과 작업 모드를 구분하는 화면입니다. 아래의 **프로젝트** 메뉴는 작업할 업무 공간을 고르는 위치입니다. 표시된 모델 이름이나 “베타” 표시는 촬영한 계정의 당시 상태이며 모든 계정의 고정 화면이 아닙니다.

## ChatGPT의 플러그인 탐색

![ChatGPT 웹에서 플러그인 공개 목록과 검색·추가 메뉴를 직접 촬영한 화면](/screenshots/20261005/chatgpt-plugins.jpg)

플러그인 화면에서 검색창과 **공개·개인용** 구분을 확인할 수 있습니다. 필요한 기능의 설명과 설치 경로를 확인합니다. 화면의 목록에 어떤 패키지가 보인다는 사실은 내 작업에서 인증까지 끝났다는 뜻이 아닙니다. [스킬과 플러그인 수업](/learn/04-skills-plugins/)에서 설치 후 확인할 내용을 배웁니다.

## Claude의 플러그인 추가 메뉴

![Claude 웹의 사용자 지정에서 플러그인 탭과 마켓플레이스 추가·업로드 메뉴를 펼친 실제 화면](/screenshots/20261005/claude-plugins.jpg)

**사용자 지정 → 플러그인 → 추가**에서 촬영한 계정에는 **마켓플레이스 추가**, **마켓플레이스 관리**, **플러그인 업로드**가 보입니다. 이는 메뉴의 존재를 확인한 화면이며, MoAI 패키지 설치나 실행을 완료했다는 증거는 아닙니다. 현재 지원되는 경로로 필요한 패키지를 설치한 뒤 작은 예제로 확인합니다. [설치 안내](/plugins/install/).

## 촬영 범위와 해석

| 사진 | 환경·상태 | 촬영에서 제외한 내용 |
|---|---|---|
| Work 시작 | ChatGPT 웹, Work 선택, 입력 전 | 개인 대화 목록·추천 업무·프로필 |
| Cowork 시작 | Claude 웹, Cowork 선택, 입력 전 | 개인 프로젝트·진행 중 업무 목록 |
| ChatGPT 플러그인 | 웹의 공개 탐색 목록 | 개인 설치 목록·프로필 |
| Claude 플러그인 | 웹의 탐색 목록과 추가 메뉴 | 개인 프로젝트·대화·프로필 |

개인 내용이 있는 영역은 사이드바를 접거나 화면 캡처 범위에서 제외했습니다. 입력·설치·외부 서비스 실행은 이 사진에 포함되지 않습니다. ChatGPT 데스크톱 앱은 이번 촬영 도구의 앱 접근 제한으로 촬영하지 못했고, Claude 데스크톱의 게시 가능한 캡처는 확보하지 못했습니다. 따라서 위 사진을 데스크톱 전용 기능의 증거로 사용하지 않습니다.

수업의 인포그래픽은 개념을 설명하기 위해 제작한 그림이며, 이 페이지의 실제 캡처와 구분합니다. 공식 기능 안내는 [자료 색인](/help/source-index/)에서 확인합니다.

[앱과 웹 준비](/getting-started/install/) · [온라인 강의실](/learn/)
''')

release=W/'content/releases/docs-20261005.md'
release.write_text('''---
title: "문서 개편 · 2026.10.05"
description: "ChatGPT Work와 Claude Cowork를 함께 배우는 강의용 문서 개편 내용"
date: 2026-10-05T00:00:00+09:00
lastmod: 2026-10-05T00:00:00+09:00
weight: 1
---

## 개편 내용

- 시작하기, 온라인 강의실, 프로젝트 적용, 업무별 실습, 플러그인, 도움말, 고급 설정으로 학습 순서를 구성했습니다.
- 두 앱을 같은 예제로 설명하며, 프로젝트·파일 접근·플러그인·에이전트의 환경별 차이를 구분했습니다.
- 6개 수업에 한국어 개념 그림, 가상 자료, 실습 요청, 모범 결과, 흔한 실수, 확인 문제를 넣었습니다.
- 실제 웹을 실행해 촬영한 Work·Cowork 입력창과 플러그인 메뉴를 추가했습니다.
- 그림 확대, 수업 이동, 강사용 안내와 다운로드 자료를 추가했습니다.
- 과거 릴리스와 기존 문서 주소를 유지했습니다. 과거 제품 화면·메뉴는 당시 기록으로 읽고 현재 절차는 최신 안내에서 확인하세요.

## 확인 범위

실제 화면의 촬영 범위는 [촬영 기록](/learn/screens/)에서 확인합니다. 파일과 링크의 검증, 실제 앱 업무 수행, 공개 사이트 게시 여부는 각각 확인해야 합니다. 이 개편 기록만으로 모든 계정의 설치·인증·예약 실행이 검증되었다고 판단하지 않습니다.

[온라인 강의실](/learn/) · [현재 설치 안내](/plugins/install/) · [릴리스 정보](/releases/)
''')
p=W/'content/releases/_index.md';s=p.read_text();s=s.replace('## 릴리스 노트','## 문서 개편\n\n[2026년 10월 5일 강의용 문서 개편](/releases/docs-20261005/)에서 두 앱의 학습 경로와 새 수업을 확인합니다. 아래 버전 기록은 당시의 변경 사항이며 현재 사용법은 [시작하기](/getting-started/)와 [설치 안내](/plugins/install/)를 따릅니다.\n\n## 릴리스 노트',1);s=s.replace('**업데이트** — 두 데스크톱 앱 모두 **플러그인(Plugins) 메뉴 → 해당 코워커 → Update**. 터미널 명령은 [플러그인 설치와 관리](/plugins/install/) 4절 참고','**업데이트** — 현재 앱에서 제공하는 플러그인 관리 경로를 확인합니다. [플러그인 설치와 관리](/plugins/install/)를 참고합니다.');p.write_text(s)
print('navigation: 7 groups; screenshots: 4 references; teaching pages and release note linked')
