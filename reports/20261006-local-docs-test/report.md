# 로컬 온라인 문서 실행 테스트 보고서

작성일: 2026년 10월 6일  
작업 세션: `01a10aae-6716-7681-b5d7-d558155d9f86`

## Claim · 실행 결과

로컬 Hugo 서버를 직접 실행하고 브라우저에서 문서 기능을 사용했다. 테스트에서 발견한 강의 절 순서와 태블릿 헤더 넘침을 수정한 뒤 재검사했다. 현재 서버는 **http://127.0.0.1:1313/** 에서 실행 중이다. 로컬 컴퓨터에서 접근하는 주소다.

최종 HTTP 검사는 문서 288개와 리소스 196개, 합계 484개 응답을 확인했다. 모두 HTTP 200과 비어 있지 않은 본문을 반환했다. 정적 리소스는 비교 빌드와 바이트 해시가 일치했다. 없는 주소 한 개는 별도로 HTTP 404를 반환했고, 브라우저에서 한국어 안내와 홈 복귀가 동작했다.

실제 브라우저에서는 한국어 검색, 결과 문서 이동, 검색 결과 없음, Escape 닫기, 펼침 메뉴, 강의 답안, 다음 강의, 코드 복사, CSV 다운로드, 인포그래픽 확대와 본문 앵커를 확인했다. 6개 강의는 모두 학습 목표가 첫 절이며 확인 문제가 있었다. 모바일·태블릿의 대표 화면과 전환 경계 16개에서는 가로 넘침과 화면 밖 검색 버튼이 없었고, 화면에 보이는 이미지가 로드됐다.

## 발견하여 수정한 내용

### 1. 3·4·6강에서 학습 목표보다 그림이 먼저 나오는 문제

초기 실행 화면에서 `그림으로 먼저 이해하기`가 `이번 수업에서 배울 내용`보다 먼저 나왔다. 본문을 확인해 그림과 설명 블록이 문서 상단에 있고, 관리용 마커만 뒤에 떨어져 있는 상태를 확인했다. 앞선 인포그래픽 보고서의 배치 완료 설명을 정정했다.

3·4·6강의 그림·설명·관리 마커를 한 블록으로 묶어 목표 다음으로 옮겼다. 최초 생성 스크립트도 학습 목표 다음에 삽입하도록 고쳤다. 문서 검사기는 강의의 첫 절이 학습 목표인지 확인한다. 임시 복제본에 잘못된 선행 절을 넣었을 때 검사기가 실제로 오류를 냈다. 수정 전·후 파일 해시는 [수정 기록](lesson-order-fix.json)에 있다.

### 2. 태블릿에서 상단 메뉴가 문서 폭을 밀어내는 문제

768px 화면에서 실제 문서 폭은 757px인데 스크롤 폭은 833px이었다. 헤더 요소의 경계를 측정해 GitHub 링크와 검색 버튼이 오른쪽으로 밀린 것을 확인했다. 검색 버튼의 오른쪽 끝은 833.54px이었다.

작은 화면에서 상단 메뉴와 GitHub 버튼을 숨기는 기준을 600px에서 850px로 조정했다. 문서 내부의 메뉴와 검색 기능을 이용할 수 있다. 첫 재검사에서는 브라우저 CSS에 기존 600px 규칙이 남아 있었다. 파일 내용 해시를 CSS 주소의 버전값으로 붙여 새 스타일을 불러오도록 수정했다. 이후 브라우저가 적용한 CSS에서 850px 규칙과 내용 해시를 확인했다.

최종 768px 화면: 문서 폭 757px, 스크롤 폭 757px. 모바일 390px·태블릿 768px에서 홈·3강·플러그인·역할 안내·질문 안내·데이터 분석 문서를 검사했다. 홈에서는 600·601·850·851px 경계도 검사했다. [수정 전 측정](responsive-before.json), [캐시가 남아 있던 재검사](responsive-cache-before.json), [최종 측정](responsive-browser.json), [적용 CSS](css-browser.json)를 보존했다.

## Evidence · 이번 실행의 근거

### 서버

실행 명령:

```sh
hugo server --source www --bind 127.0.0.1 --baseURL http://127.0.0.1:1313/ --port 1313 --disableFastRender --enableGitInfo=false --noBuildLock --quiet
```

포트 확인 명령과 실제 출력:

```sh
lsof -nP -iTCP:1313 -sTCP:LISTEN
```

```text
COMMAND   PID USER   FD   TYPE             DEVICE SIZE/OFF NODE NAME
hugo    39010 goos    4u  IPv4 0xe4fe88ea019cc302      0t0  TCP 127.0.0.1:1313 (LISTEN)
```

서버 PID는 보고 시점의 값이다. 종료할 때는 이 프로세스가 같은 Hugo 서버인지 먼저 확인한다.

### 전체 로컬 응답

```sh
hugo --source www --destination /tmp/moai-docs-local-test-20261006 --baseURL http://127.0.0.1:1313/ --enableGitInfo=false --quiet
python3 reports/20261006-local-docs-test/check-live.py /tmp/moai-docs-local-test-20261006
```

최종 실행은 종료 코드 0. [전체 HTTP 기록](live-http.json)과 [명령 출력](live-http.stdout)을 저장했다.

```json
{
  "html_responses": 288,
  "asset_responses": 196,
  "checked_responses": 484,
  "errors": [],
  "missing_route_status": 404
}
```

초기 비교에서는 기본 서버 주소 `localhost`와 비교 빌드의 `127.0.0.1`이 달랐고, 소스 변경 중 서버 색인과 비교 빌드의 내용도 달랐다. 동일한 baseURL을 지정하고 서버를 다시 시작한 뒤 수정된 소스로 새 빌드를 만들어 최종 비교했다. 최종 색인·사이트맵을 포함한 리소스 196개는 바이트 해시가 일치했다.

### 문서 링크와 학습 자료

```sh
hugo --source www --destination /tmp/moai-docs-local-test-20261006-production --enableGitInfo=false --quiet
python3 scripts/check-docs.py /tmp/moai-docs-local-test-20261006-production --report reports/20261006-local-docs-test/site-check.json
python3 reports/20261006-local-docs-test/check-fixtures.py /tmp/moai-docs-local-test-20261006-production
```

모두 종료 코드 0. [문서 검사](site-check.json): HTML 288개, 내부 참조 25,598개, 절 앵커 3,551개, 이미지 521개, 검색 항목 170개, 사이트맵 항목 192개, 오류 0개. 가상 예제 계산 11개와 강의 6개도 검사했다.

[다운로드·회귀 검사](fixture-check.json): 브라우저에서 내려받은 CSV는 소스와 바이트 해시가 일치했다. 문의 6건은 배송 3건·반품 2건·결제 1건이었다. 임시 복제본의 잘못된 강의 순서는 아래 오류로 탐지했고 복제본은 자동 제거했다.

```text
03-first-result.md: learning goal must precede other sections
```

### 브라우저 사용 흐름

[실행 기록](browser-journeys.json)과 [6개 강의 측정](lessons-browser.json)을 저장했다. UI는 Codex 브라우저 도구로 조작했다. 전체 페이지의 HTTP 확인과 브라우저에서 클릭한 흐름은 별도의 근거다.

| 직접 테스트한 흐름 | 최종 결과 |
|---|---|
| 한국어 검색 결과에서 문서 이동 | 통과 |
| 존재하지 않는 검색어 | 통과 |
| 검색창 Escape 닫기 | 통과 |
| 강의 답안 펼치기 | 통과 |
| 강의 다음 이동 | 통과 |
| 4강 수정 후 학습 목표 순서 | 통과 |
| 실습 CSV 다운로드 | 통과 |
| 강의 예제 코드 복사 | 통과 |
| 접힌 메뉴 펼치고 첫 프로젝트 이동 | 통과 |
| 그림 확대 보기 | 통과 |
| 모바일 메뉴에서 질문 안내 이동 | 통과 |
| 모바일 홈에서 첫 결과물 이동 | 통과 |
| 없는 주소의 안내 | 통과 |
| 없는 주소 안내에서 홈 복귀 | 통과 |
| 본문 절 앵커 이동 | 통과 |

코드 복사는 화면에 표시된 예제 130자와 실제 클립보드 내용을 대조해 일치를 확인했다. 테스트 전 클립보드 내용을 복원했으며 그 내용은 보고서나 파일에 기록하지 않았다. CSV는 실제 다운로드 이벤트를 기다려 저장 파일을 읽었다. 답안 펼침은 설명 영역의 `open` 상태와 답안 내용으로 확인했다. 확대 보기는 새 탭의 SVG 제목과 설명으로 확인했다.

### 실제 화면

- [최종 데스크톱 홈](screenshots/home-desktop.jpg)
- [검색 결과](screenshots/search-desktop.jpg)
- [강의 답안](screenshots/lesson-answer.jpg)
- [수정 후 학습 목표와 그림](screenshots/lesson-order-after.jpg)
- [모바일 메뉴](screenshots/menu-mobile.jpg)
- [모바일 질문 안내](screenshots/questions-mobile.jpg)
- [수정 전 태블릿 넘침](screenshots/tablet-overflow-before.jpg)
- [수정 후 태블릿 홈](screenshots/tablet-after.jpg)
- [없는 주소 안내](screenshots/not-found.jpg)

## Baseline-attribution · 확인한 기준

작업 경로는 `/Users/goos/.codex/worktrees/b0aa/moai-cowork`, 기준 커밋은 `2c3cef1d24e88b3bfe8db61c713ffae317b346d0`이다. 앞선 요청에서 수정한 플러그인·문서와 이번 수정이 포함된 미커밋 작업 트리를 대상으로 했다. HTML·리소스 응답은 이번 실행의 로컬 서버, 브라우저 동작은 현재 macOS의 Codex 인앱 브라우저에서 관측했다.

HTTP 비교 빌드는 로컬 baseURL을 사용했다. 일반 문서 링크 검사는 운영 사이트 baseURL을 사용하는 별도 빌드에서 실행했다. 두 빌드 모두 이번 실행에서 생성했다. 서버는 루프백 주소에 바인딩되어 있다. 브라우저 화면 크기 설정은 테스트가 끝난 뒤 원래대로 복원한다.

## Gaps · 확인하지 않은 범위

484개 HTTP 응답 확인은 모든 페이지의 모든 버튼을 클릭했다는 뜻이 아니다. 실제 클릭 흐름은 위 목록, 반응형 측정은 대표 화면 16개다. 외부 공식 문서·CDN·GitHub API의 가용성을 전수 검사하지 않았다. 공개 사이트에 배포하지 않았고, ChatGPT Work·Claude Cowork에서 플러그인 설치·인증·업무 실행을 검증한 것으로 해석하지 않는다. 다른 브라우저·운영체제와 실제 수강생 계정에서의 실습은 확인하지 않았다.

## Residual-risk · 남는 확인 사항

이 서버는 개발용이며 실행 프로세스가 종료되면 주소에 접근할 수 없다. 이후 본문이나 스타일이 바뀌면 해당 사용 흐름을 다시 테스트해야 한다. 공개 강의에 반영하려면 변경 통합·배포와 배포 후 확인이 별도로 필요하다.
