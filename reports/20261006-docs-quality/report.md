# 설치·플러그인 안내와 문서 품질 개선 보고서

조사일: 2026년 10월 6일. 설치 안내는 보강했고 전체 목차와 실습 구성은 개선했습니다. **설치부터 실제 스킬 실행까지의 모든 화면을 확보한 상태는 아닙니다.** 직접 확보한 사진과 공식 절차, 아직 확인하지 못한 단계를 구분합니다.

## Claim · 적용한 개선

기존 Markdown 171개 전체의 본문·제목·목차·그림·스킬 참조를 구조 조사했습니다. 현재 문서는 173개이며 이번 턴에 77개 문서를 수정하거나 추가했습니다. 신규 문서는 준비 수업과 전체 목차 2개입니다. 문장·사례 대조는 설치·강의·실습·역할별 설명을 중심으로 진행했고, 과거 릴리스는 당시 기록으로 보존했습니다.

| 확인한 문제 | 적용한 개선 | 읽을 위치 |
|---|---|---|
| 설치 안내가 앱 실행 수준에 머물러 다운로드·운영체제 선택·설치 확인을 따라가기 어려움 | 공식 다운로드, 컴퓨터 종류 확인, 설치·로그인·업무 입력창 확인을 분리. 막힌 단계별 안내 추가 | [데스크톱 설치](http://127.0.0.1:1313/getting-started/install/) |
| 탐색 목록과 설치·인증·업무 실행의 차이를 사진만으로 판단하기 어려움 | 앱 준비와 기능 추가 도식, 외부 인증이 필요한 경우의 분기 도식 추가. 새 작업과 작은 예제로 검토 | [플러그인 설치](http://127.0.0.1:1313/plugins/install/) |
| 사진 4장이 웹 화면에 한정되어 있고 상세 추가 경로가 부족함 | 실제 사진 7장 추가. Claude Desktop, 공식 다운로드 2종, ChatGPT 추가·상세 화면, Claude 추가·URL 선택 촬영 | [촬영 기록](http://127.0.0.1:1313/learn/screens/) |
| 입문 과정에 앱 준비가 빠지고 문서를 한곳에서 찾기 어려움 | 준비 수업을 앞에 배치. 큰 분야와 하위 문서를 묶은 전체 목차·학습 경로 생성 | [준비 수업](http://127.0.0.1:1313/learn/preparation/) · [전체 목차](http://127.0.0.1:1313/learn/contents/) |
| 분야별 시작 페이지의 설명이 비어 있거나 선택 기준이 부족함 | 가이드·템플릿·직무·고급·디자인·Office·역할·프로젝트·도움말·워크플로 시작 페이지에 안내와 하위 목록 추가 | [페이지별 처리 목록](/Users/goos/.codex/worktrees/b0aa/moai-cowork/reports/20261006-docs-quality/page-audit.md) |
| 브랜드·제품 개발·상권·지원사업·NDA·컴플라이언스 예제가 제목의 업무와 맞지 않거나 필요한 입력이 없음 | 6개 사례의 입력 자료·질문·결과 기준·오류·확인 문제를 업무별로 교체. 모두 가상 자료로 명시 | [실습](http://127.0.0.1:1313/cookbook/) |
| 결과를 읽는 방법은 설명하지만 직접 비교할 결과가 부족함 | 업무 실습 38개와 역할 안내 16개에 모범 결과 표 추가. 기존 계산 도표 5개까지 총 59개 예제에서 결과 비교 | [실습별 기록](/Users/goos/.codex/worktrees/b0aa/moai-cowork/reports/20261006-docs-quality/worked-results.json) · [역할별 기록](/Users/goos/.codex/worktrees/b0aa/moai-cowork/reports/20261006-docs-quality/role-results.json) |
| 사업계획·웹소설·제품·학습자료의 전문 스킬 후보가 빠짐 | 실제 저장소 설명과 대조해 사업 계획·타당성 검토, 웹소설 기획·집필·표지, 사용자 조사·PRD, 학습자료 후보 보강 | [페이지별 구조 기록](/Users/goos/.codex/worktrees/b0aa/moai-cowork/reports/20261006-docs-quality/page-audit.json) |
| ‘양식를’, ‘범위을’, ‘표을 만드는’ 등 조사 오류 | 해당 동사 앞 조사 오류 53곳 수정. 설치 문서의 강조 기호가 글자로 남던 3곳도 실제 출력과 대조해 수정 | [수정 기록](/Users/goos/.codex/worktrees/b0aa/moai-cowork/reports/20261006-docs-quality/particle-fixes.json) |
| 10월 5일의 Cowork 변경 예고가 남아 있음 | 10월 6일 공식 시작 안내를 다시 확인해 새 클라우드 작업과 기존 로컬 작업, Desktop 연결 필요 범위로 갱신 | [환경 선택](http://127.0.0.1:1313/getting-started/choose-app/) |

### 목차와 학습 흐름

준비 수업 → 업무 목표 → 프로젝트·자료 → 첫 결과 → 스킬·플러그인 → 전문가 협업 → 결과 검토·반복 업무 순서로 읽습니다. 이미 앱을 쓰는 사람은 첫 실습부터 시작하고, 설치에서 막힌 사람은 해당 단계로 돌아갑니다. 고급 설정과 과거 릴리스는 별도 경로로 찾습니다.

전체 목차에는 다른 문서 171개가 연결되어 있습니다. 홈과 목차 자신을 합쳐 173개 원문에 대응하며 검사에서 빠진 경로는 없었습니다. 검색 항목 수와 HTML 수는 원문 수와 다릅니다. 홈·별칭·분류 페이지 등 생성 방식의 차이가 있습니다.

### 인포그래픽·사진·설명의 기준

- 설치의 두 단계와 인증 갈림길은 **도식**으로 설명합니다. 사각형은 할 일, 마름모는 확인할 질문, 화살표는 다음 단계입니다. 막힌 곳에서 무엇을 다시 확인하는지도 그림에 남깁니다.
- 본문과 대조할 수 있는 **모범 결과 표 54개**를 추가했습니다. 숫자·정책·미정 항목을 그림에 반복해서 넣지 않고 HTML 표와 문장으로 설명합니다.
- 기존 픽셀 그림 3종을 직접 열어 한국어 글자, 자료 연결·병렬 작성·검토와 재사용의 화살표를 확인했습니다. 본문·폰트·킨들 배경은 유지합니다. 이미지 자체의 글자와 본문의 Pretendard는 별도 요소입니다.
- 실제 앱·웹 사용법은 **직접 촬영한 사진**으로 설명합니다. 사진 옆에서 촬영 환경·눌러야 할 메뉴·다음 확인을 설명하고, 사진을 크게 열 수 있게 합니다.
- 페이지별 그림 처리 방식은 [173개 문서 조사표](/Users/goos/.codex/worktrees/b0aa/moai-cowork/reports/20261006-docs-quality/page-audit.md)에 기록했습니다. 모든 페이지에 이미지를 추가하는 방식으로 처리하지 않았습니다.

### 이번에 다시 확인한 공식 문서

설치·플러그인 기능과 변경 안내는 아래 공식 문서를 검색한 뒤 본문을 열어 확인했습니다. 사진은 이 문서들의 기능 지원 범위 전체를 증명하는 자료가 아닙니다.

- [ChatGPT Desktop 설치와 시작](https://learn.chatgpt.com/docs/app)
- [ChatGPT 플러그인](https://learn.chatgpt.com/docs/plugins)
- [ChatGPT Work 시작](https://learn.chatgpt.com/docs/get-started-with-work)
- [Claude Desktop 설치](https://support.claude.com/en/articles/10065433-install-claude-desktop)
- [Claude 플러그인](https://support.claude.com/en/articles/13837440-use-plugins-in-claude)
- [Claude Cowork 시작](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork)

## Evidence · 이번 실행에서 확인한 결과

최종 빌드와 검사에 사용한 명령:

```text
hugo --source www --destination /tmp/moai-docs-quality-20261006 --baseURL https://cowork.mo.ai.kr/ --enableGitInfo=false --quiet
python3 scripts/check-docs.py /tmp/moai-docs-quality-20261006 --report reports/20261006-docs-quality/site-check.json
```

빌드는 종료 코드 0, quiet 출력은 비어 있었습니다. 검사 결과의 요약 출력은 다음과 같습니다. 전체 원문 출력은 [site-check-output.txt](/Users/goos/.codex/worktrees/b0aa/moai-cowork/reports/20261006-docs-quality/site-check-output.txt)에 있습니다.

```json
{"html_files": 290, "internal_references": 26792, "fragment_references": 3549, "images": 419, "search_entries": 172, "sitemap_entries": 194, "classroom_rows": 6, "classroom_types": {"배송": 3, "반품": 2, "결제": 1}, "lessons": 6, "errors": [], "scope": "built_site_local_references_and_fixtures_only"}
```

| 이번 실행의 검사 | 실제 관측 |
|---|---|
| 원문 구조 | 173개 원문, 현재 문서의 미해결 스킬 경로 0개 |
| 빌드된 문서 | HTML 290개, 내부 참조 26,792개, 앵커 3,549개, 이미지 태그 419개, 오류 0개 |
| 예제 계산 | 원문과 모범 설명의 계산 11건 일치. 전체 완료율 68%, 지출 합계 25,000원, 가정 차액 700,000원 등 |
| 실제 모바일 브라우저 | 390×844에서 문서 173개. 가로 넘침 0개, SVG 노드 글자 경계 초과 0개 |
| 도식 표시 | 모바일 검사에서 도식 50개 표시, 노드 글자 378개 경계 검사 |
| 실제 데스크톱 브라우저 | 기본 폭 1280에서 주요 12개 문서. 가로 넘침·SVG 노드 경계 초과 0개 |
| 마지막 수정 후 재검사 | 전체 목차·앱 설치·플러그인 설치를 모바일에서 다시 확인. 목차의 빠진 경로 0개 |
| 로컬 응답 | 문서 173개와 신규 사진 7개, 180건 모두 HTTP 200. 사진의 응답 크기와 저장 파일 크기 일치 |
| 수정 파일 형식 | `git diff --check -- www reports/20261006-docs-quality` 종료 코드 0, 출력 없음 |

브라우저 검사는 모든 글의 학습 효과를 측정한 것이 아닙니다. DOM의 문서 폭, 렌더링된 도식과 노드 글자의 경계를 검사했습니다. 도식의 의미와 사진의 설명은 핵심 안내를 직접 읽어 대조했습니다. 사진을 실제 문서에서 열었을 때 신규 파일 7종의 읽기 경로를 로컬 응답으로 확인했고, 플러그인 안내의 사진 5종은 실제 페이지에서 이미지 로딩까지 확인했습니다.

측정 자료: [모바일](/Users/goos/.codex/worktrees/b0aa/moai-cowork/reports/20261006-docs-quality/browser-mobile.json) · [데스크톱](/Users/goos/.codex/worktrees/b0aa/moai-cowork/reports/20261006-docs-quality/browser-desktop.json) · [최종 재검사](/Users/goos/.codex/worktrees/b0aa/moai-cowork/reports/20261006-docs-quality/browser-final-rechecks.json) · [목차](/Users/goos/.codex/worktrees/b0aa/moai-cowork/reports/20261006-docs-quality/toc-coverage.json) · [로컬 응답](/Users/goos/.codex/worktrees/b0aa/moai-cowork/reports/20261006-docs-quality/local-http.json) · [캡처 원본과 SHA](/Users/goos/.codex/worktrees/b0aa/moai-cowork/reports/20261006-docs-quality/screenshot-ledger.json).

## Baseline-attribution · 측정한 작업 사본

- 작업 사본: `/Users/goos/.codex/worktrees/b0aa/moai-cowork`
- HEAD: `2c3cef1d24e88b3bfe8db61c713ffae317b346d0`, detached HEAD.
- source_session_id: `01a10aae-6716-7681-b5d7-d558155d9f86`.
- 이번 편집 전 원문: [baseline.json](/Users/goos/.codex/worktrees/b0aa/moai-cowork/reports/20261006-docs-quality/baseline.json)에 171개 문서의 SHA·목차·그림·스킬 참조를 기록했습니다.
- 이번 편집 후 원문: [page-audit.json](/Users/goos/.codex/worktrees/b0aa/moai-cowork/reports/20261006-docs-quality/page-audit.json)에 173개 문서의 SHA와 처리 유형을 기록했습니다.
- 앞선 턴의 킨들 검사 수치를 이번 검사의 결과로 사용하지 않았습니다. 이미 승인된 디자인 작업 위에 이번 변경을 더했고, 위 검사는 현재 작업 사본에서 다시 실행했습니다.
- 로컬 서버: `http://127.0.0.1:1313/`. 이 보고서 작성 시 실행 중입니다. 커밋·원격 반영·운영 배포는 수행하지 않았습니다.

## Gaps · 아직 관측하지 못한 범위

| 범위 | 상태와 이유 |
|---|---|
| ChatGPT Desktop의 실제 화면 | CUA가 `/Applications/ChatGPT.app`의 앱 접근을 제한했습니다. 우회하지 않았고 공식 다운로드 웹·ChatGPT 웹 사진으로 보강했습니다. Desktop 사진으로 표시하지 않았습니다. |
| Claude Desktop의 추가 세부 과정 | 실제 탐색 화면은 확보했지만 앱 내부 입력 조작에서 창 처리 오류가 발생했습니다. 추가 메뉴와 URL 선택은 웹에서 촬영했습니다. |
| 운영체제 설치 프로그램·로그인 | 앱을 새로 설치하는 전 과정을 촬영하지 않았습니다. 공식 절차를 설명하고 미촬영 상태를 본문에 표시했습니다. |
| Windows·Linux | 실제 기기에서의 설치·작업 수행 화면은 촬영·검증하지 않았습니다. 앱 지원과 로컬 컴퓨터 접근 기능을 분리해 확인하도록 안내했습니다. |
| MoAI 패키지 설치 완료·실제 스킬 실행 | 이번 촬영은 메뉴와 주소 선택까지입니다. Claude 주소 선택은 동기화 전 취소했습니다. ChatGPT 파일 업로드·Outlook 설치·외부 계정 인증도 실행하지 않았습니다. |
| 모든 계정·조직·구독의 메뉴 | 촬영 계정에서 관측한 메뉴입니다. 지원이 다른 계정에 같은 메뉴가 있다고 단정하지 않습니다. |
| 실제 학습 효과 | 입문자가 혼자 설치·실습을 끝내는 수행률을 측정하지 않았습니다. 강사용 확인표와 모범 결과로 검토할 수 있게 했습니다. |
| 과거 스킬 이름 | 과거 릴리스 15개 문서에서 현재 경로와 맞지 않는 참조를 발견했습니다. 당시 기록을 현재 기능으로 바꾸지 않고 목차에서 과거 기록으로 구분했습니다. |

## Residual-risk · 다음 확인에서 필요한 것

**High:** 상세 설치 강의의 모든 단계를 실제 화면으로 보여 주려면, 허용된 촬영 환경에서 각 앱의 설치 프로그램·로그인·플러그인 설치 완료·새 작업의 실제 스킬 사용을 추가로 촬영해야 합니다. 현재 사진 7장을 그 전 과정의 완료 증거로 제시하면 안 됩니다.

**Medium:** 공급자의 화면과 실행 위치가 바뀔 수 있으므로 수업 당일 계정에서 메뉴·지원 조건을 확인합니다. 실제 로컬 자료 접근, 인증, 예약 실행·알림은 해당 환경에서 결과를 확인해야 합니다.

**Medium:** 입문자의 실제 수행을 관찰해 어디에서 막혔는지 기록해야 설명의 학습 효과를 판단할 수 있습니다. 설치 과정이 미완료인 수강생에게는 준비 수업 확인표를 사용하고, 설치·실행 성공과 문서의 모범 결과를 구분합니다.

![로컬 플러그인 안내에서 실제 저장소 주소 선택 사진과 설명을 확인한 화면](/Users/goos/.codex/worktrees/b0aa/moai-cowork/reports/20261006-docs-quality/plugin-guide-local.jpg)
