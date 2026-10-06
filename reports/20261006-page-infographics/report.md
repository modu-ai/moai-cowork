# 페이지별 인포그래픽 추가 결과

작성일: 2026년 10월 6일  
작업 세션: `01a10aae-6716-7681-b5d7-d558155d9f86`

> 후속 로컬 브라우저 테스트에서 3·4·6강의 그림이 학습 목표보다 앞에 있는 것을 발견했다. 앞선 배치 완료 보고를 정정한다. 세 강의의 그림 블록 전체를 목표 다음으로 옮기고 6개 강의의 실제 화면과 검사기로 다시 확인했다. 현재 상태와 후속 수정 근거는 [로컬 문서 테스트 보고서](../20261006-local-docs-test/report.md)에 기록한다.

## Claim · 반영한 내용

문서 171개에 대해 그림 추가 여부와 근거를 계획하고, 108개 문서에 한국어 인포그래픽을 추가했다. 서로 다른 개념 86개를 데스크톱·모바일용으로 각각 제작하여 SVG 파일은 172개다. 같은 개념은 필요한 페이지에서 재사용한다. 그림 아래 설명과 기존 상세 본문을 함께 읽을 수 있게 배치했다.

| 페이지별 결정 | 문서 수 | 적용 기준 |
|---|---:|---|
| 새 그림 추가 | 108 | 핵심 관계·업무 순서·검토 기준·예제를 먼저 보여 준다. |
| 기존 그림 유지 | 13 | 기존 개념도·실제 화면·관계도를 사용한다. |
| 새 그림을 추가하지 않음 | 50 | 릴리스 세부 기록 48개와 권리·이용 고지 2개를 보존한다. |

[171개 페이지별 계획](plan.md)에서 모든 페이지의 우선순위, 결정 이유와 그림 경로를 확인할 수 있다. 현재 사용 안내 122개 중 108개에 새 그림을 넣고, 12개는 기존 그림을 유지했다. 권리·이용 고지 2개에는 그림을 추가하지 않았다.

### 무엇을 그림으로 설명했는가

- 공통 개념 27개: 질문에 답하는 방법, 설치와 실제 실행의 차이, 프로젝트 지침, 검토, 결과 전달, 계정·비용·권한, MCP 연결과 확인 범위 등을 49개 문서에서 설명한다.
- 업무 실습 42개: 해당 업무에 필요한 자료, 핵심 작업, 검토 기준, 만들 결과, 가상 예제와 자주 생기는 혼동을 담았다.
- 역할 안내 17개: 각 역할이 사용할 자료와 업무 범위, 검토할 내용, 결과물을 해당 본문에서 뽑았다.

기존 문서 전체의 본문·제목·절·이미지 경로를 파일로 읽어 목록과 해시를 기록했다. 반복되는 안내는 공통 문단과 페이지 고유 내용을 나누어 살폈다. 과거 릴리스는 현재 기능 안내와 구분하여 보존했다. 59개 업무·역할 안내에서 추출한 자료·진행 순서·질문·예제·결과·혼동 설명은 현재 본문과 다시 대조했다. 이 작업은 과거 릴리스의 모든 제품 동작을 다시 검증한 것으로 해석하지 않는다.

### 읽기와 접근성

데스크톱에서는 네 항목을 두 열로, 모바일에서는 큰 글자의 한 열로 보여 준다. 화면 너비 600px 이하에서는 동일 내용을 담은 모바일 SVG를 선택한다. 그림을 누르면 원본 SVG가 새 탭에 열린다. 각 그림에는 HTML 대체 텍스트와 SVG 제목·설명이 있다. 본문에도 설명이 남아 있어 그림만 읽어야 내용을 알 수 있는 구성은 피했다.

모든 그림에 개념 설명임을 표시했다. 앞서 수집한 ChatGPT·Claude 실제 화면 캡처와 구분한다. 숫자와 한글을 수정할 수 있는 SVG로 직접 제작했으며, 이번 추가 작업에서는 이미지 생성 API를 호출하지 않았다. SVG 합계 용량은 842,514바이트다.

학습 목표가 있는 강의는 목표 다음에 그림을 배치했다. 태그 목록에서는 짧은 소개만 보이도록 108개 문서의 요약 경계를 지정했다. 문서 안에 넣은 그림이 목록에도 반복되어 목록이 길어지는 현상을 정리했다.

### 계산을 보여 주는 그림

데이터 예제 5개에는 A지역 24/30 = 80%, B지역 10/20 = 50%, 전체 34/50 = 68%의 막대를 넣었다. 전체 비율을 두 지역 비율의 단순 평균 65%로 계산하는 혼동도 설명했다. 지출 예제 3개에는 12,000 + 8,000 + 5,000 = 25,000원 계산을 넣었다. 모두 본문의 가상 자료이며 실서비스의 실행 결과가 아니다.

### 수정·재제작 자료

| 자료 | 역할 |
|---|---|
| [page-plan.json](page-plan.json) | 171개 원본의 해시·절·기존 그림·추가 결정 |
| [example-facts.json](example-facts.json) | 59개 업무·역할 안내에서 추출한 본문 근거 |
| [diagram-specs.json](diagram-specs.json) | 86개 그림의 제목·항목·예제·주의할 혼동 |
| [render-diagrams.py](render-diagrams.py) | SVG 제작과 최초 삽입; 기존 제작물 해시 확인 |
| [assets.json](assets.json) | 172개 SVG 경로·해시·글자 배치 |
| [verify-diagrams.py](verify-diagrams.py) | 원본 근거·숫자·모바일 변형·페이지 보존 검사 |

`prepare-plan.py`는 최초 조사 목록을 만든 기록이다. 현재 파일로 다시 실행하면 조사 기준이 바뀌므로 기존 계획을 재사용할 때 다시 실행하지 않는다. 본문을 수정한 뒤 그림을 업데이트할 때는 먼저 해당 명세의 근거를 함께 수정한다.

## Evidence · 이번 실행에서 확인한 결과

### 문서 빌드와 링크

실행 명령:

```sh
hugo --source www --destination /tmp/moai-docs-infographics-20261006-final --enableGitInfo=false --quiet
python3 scripts/check-docs.py /tmp/moai-docs-infographics-20261006-final --report reports/20261006-page-infographics/site-check.json
```

Hugo는 출력 없이 종료 코드 0으로 완료했다. 문서 검사도 종료 코드 0이었다. 검사 출력의 주요 항목은 다음과 같다. [전체 출력](site-check.stdout)과 [JSON](site-check.json)에 실습 계산 11개의 결과도 기록했다.

```json
{
  "html_files": 288,
  "internal_references": 25598,
  "fragment_references": 3551,
  "images": 521,
  "search_entries": 170,
  "sitemap_entries": 192,
  "lessons": 6,
  "errors": []
}
```

### 그림·본문·주소 보존

실행 명령:

```sh
python3 reports/20261006-page-infographics/verify-diagrams.py /tmp/moai-docs-infographics-20261006-final
```

종료 코드 0. [전체 출력](artifact-check.stdout)과 [JSON](artifact-check.json)에 결과를 기록했다.

- 171개 페이지 계획, 추가 108개, 변경하지 않은 문서 63개의 원본 해시 일치.
- 86개 개념, SVG 172개: XML 파싱, 제목·설명, 파일 해시, 빌드 사본 일치.
- 86개 개념의 데스크톱·모바일 내용 일치; 현재 본문에 근거한 업무·역할 예제 59개 일치.
- 반응형 그림이 있는 문서 108개, 그림 108개, 재사용을 제외한 개념 86개. 태그 목록에는 새 그림 없음.
- 이전 문서 개편 빌드의 HTML 주소 288개와 이번 빌드의 주소 288개 비교: 누락 0개.
- 비율 예제 5개 × 두 변형의 숫자와 막대 길이 일치; 지출 예제 3개 × 두 변형의 합계 일치.
- 이번 작업의 임시 빌드에서 모바일 그림 하나를 잠시 제거해 검사기가 누락을 탐지하는지 확인한 뒤 원래 바이트로 복구.

누락 실험에서 실제 관측한 오류:

```text
getting-started/questions/index.html: missing /infographics/pages/questions-mobile.svg
```

### 실제 브라우저 표시

로컬 Hugo 서버를 직접 실행하고 Codex의 브라우저 도구로 확인했다. 전체 SVG를 넣은 임시 측정 페이지에서 `getBoundingClientRect()`로 각 SVG와 글자의 실제 영역을 측정했다. 수치가 0인 영역도 따로 세어 빈 측정을 정상 결과로 취급하지 않았다.

[측정 기록](svg-browser-check.json):

```json
{
  "svgCount": 172,
  "textCount": 5418,
  "zeroSvgBoxes": 0,
  "zeroTextBoxes": 0,
  "outside": [],
  "overlaps": []
}
```

[데스크톱 기록](desktop-browser-check.json): 실제 문서 폭 1,269px, 가로 스크롤 폭 1,269px, 데스크톱 SVG 로드 완료. [모바일 기록](mobile-browser-check.json): 실제 문서 폭 379px, 가로 스크롤 폭 379px, 모바일 SVG 로드 완료. [확대 보기 기록](enlarge-browser-check.json): 질문 문서의 확대 링크를 클릭하여 새 탭에서 해당 SVG의 제목과 주소를 확인했다.

실제 문서 화면은 다음 파일에 저장했다.

- [문서 상단과 그림 도입](screenshots/data-overview-desktop.jpg)
- [데이터 예제의 수치 도표](screenshots/data-desktop.jpg)
- [모바일 질문 안내](screenshots/questions-mobile.jpg)

전체 SVG의 글자 경계는 측정했다. 모든 문서의 모든 스크롤 위치를 하나씩 촬영한 것은 아니다. 임시 측정 페이지는 소스와 최종 빌드에서 제거했다. 브라우저 화면 크기 설정을 원래대로 복원했다.

## Baseline-attribution · 확인한 기준

- 작업 경로: `/Users/goos/.codex/worktrees/b0aa/moai-cowork`
- 기준 커밋: `2c3cef1d24e88b3bfe8db61c713ffae317b346d0`, detached HEAD.
- 최초 페이지 기준: 이 작업 시작 시점의 171개 본문 해시를 `page-plan.json`에 기록. 이전 요청에서 수행한 미커밋 플러그인·문서 수정이 포함된 작업 트리를 기준으로 했다.
- URL 비교 기준: 이전 문서 개편의 로컬 빌드 `/tmp/moai-docs-20261005-final`과 이번 실행의 `/tmp/moai-docs-infographics-20261006-final`. 서버에 배포된 문서와 비교한 값이 아니다.
- 브라우저 기준: 이번 실행의 macOS 글꼴 환경과 로컬 Hugo 문서. SVG 파일 해시는 `assets.json`에 있다.
- `moai session current` 관측: `01a10aae-6716-7681-b5d7-d558155d9f86`.

## Gaps · 확인하지 않은 범위

공개 사이트에 이번 변경을 배포하지 않았다. ChatGPT Work·Claude Cowork에서 플러그인 설치·인증·업무 실행을 이번 그림 작업으로 다시 검증하지 않았다. 제품 기능의 공식 문서 검토와 앞선 개선 내용은 이전 조사·개편 보고서의 범위이며, 이번 작업은 그 본문을 설명하는 그림 추가다. 다른 운영체제·브라우저의 글꼴 배치와 입문자 수업에서의 실제 이해도는 측정하지 않았다.

## Residual-risk · 남는 확인 사항

본문의 기능·예제·결과가 바뀌면 그림 명세도 함께 갱신해야 한다. 글꼴 대체가 일어나는 환경은 실제 화면으로 추가 확인해야 한다. 공개 온라인 강의에 반영하려면 이 변경의 통합·배포와 배포 후 화면 확인이 필요하다.

## 공통 개념별 배치

업무 실습 42개와 역할 안내 17개의 개별 그림은 페이지별 계획에서 확인할 수 있다. 아래는 여러 문서에서 재사용하는 공통 개념 27개다. 각 경로에는 같은 이름의 `-mobile.svg` 변형도 있다.

| 설명할 개념 | 사용 문서 수 | 데스크톱 그림 |
|---|---:|---|
| 처음부터 내 업무 적용까지 | 3 | `/infographics/pages/learning-path.svg` |
| 앱 이름보다 실제 접근 범위 확인 | 2 | `/infographics/pages/environment.svg` |
| 질문을 받았을 때 이렇게 답하세요 | 1 | `/infographics/pages/questions.svg` |
| 같은 숫자라도 상태가 다릅니다 | 2 | `/infographics/pages/report-status.svg` |
| 설치부터 실행까지, 증거가 다릅니다 | 2 | `/infographics/pages/install-states.svg` |
| 내 프로젝트에 맞는 지침 만들기 | 4 | `/infographics/pages/pm-setup.svg` |
| 완료 보고보다 결과물을 확인하세요 | 1 | `/infographics/pages/review.svg` |
| 잘된 업무를 반복하는 순서 | 3 | `/infographics/pages/reuse.svg` |
| 원본에서 결과까지 접근을 확인 | 1 | `/infographics/pages/permissions.svg` |
| 세 가지 계정 범위를 나눠 보세요 | 1 | `/infographics/pages/account.svg` |
| 무료 패키지와 서비스 비용은 별개 | 1 | `/infographics/pages/cost.svg` |
| 새 작업에 넘길 맥락은 직접 남기기 | 1 | `/infographics/pages/handoff.svg` |
| 기준마다 저장할 곳이 다릅니다 | 1 | `/infographics/pages/personalization.svg` |
| 출처와 권리를 함께 남기세요 | 1 | `/infographics/pages/attribution.svg` |
| Office 작업의 세 가지 방식 | 3 | `/infographics/pages/office.svg` |
| 큰 작업을 확인 가능한 단위로 나누기 | 1 | `/infographics/pages/limits.svg` |
| 멈춘 단계를 찾고 그 부분부터 확인 | 4 | `/infographics/pages/troubleshooting.svg` |
| 계정별 인증 정보와 조회를 분리 | 1 | `/infographics/pages/credentials.svg` |
| MCP: 실행 위치와 연결 방식을 따로 확인 | 1 | `/infographics/pages/server-modes.svg` |
| 외부 연결을 확인하는 네 단계 | 1 | `/infographics/pages/connector.svg` |
| 업무 방법과 실행 역할을 구분 | 1 | `/infographics/pages/skills-agents.svg` |
| 다음 담당자에게 전달할 네 묶음 | 2 | `/infographics/pages/team-handoff.svg` |
| 어떤 확인을 했는지 범위를 밝히기 | 2 | `/infographics/pages/verification.svg` |
| 온라인 강의 한 페이지를 만드는 순서 | 1 | `/infographics/pages/authoring.svg` |
| 설명에서 직접 수행까지 이어지는 수업 | 1 | `/infographics/pages/teaching.svg` |
| 결과물로 실습과 역할을 고르세요 | 6 | `/infographics/pages/choose-recipe.svg` |
| 생성 도구 연결과 제작을 분리 | 1 | `/infographics/pages/higgsfield.svg` |
