# moai-mcp-cafe24

카페24 쇼핑몰의 Admin API와 Analytics API를 연결하는 자체 제작 MCP 서버다. 현재 소스에는 **20개 카테고리 도구**와 **526개 작업 정의**가 있다. 한 카테고리 도구에서 `action`을 골라 작업을 호출한다. 작업 정의가 등록된 사실은 각 작업의 최신 API 호환성과 판매자 계정 접근을 보증하지 않는다.

카페24는 별도의 [공식 MCP 시작 문서](https://developers.cafe24.com/en/app/front/mcpserver/mcpstart)에서 몰 상품 검색과 결제 링크, Global Catalog MCP를 소개한다. 공식 MCP의 `tools/list`를 대상 몰에서 확인해 필요한 기능이 제공되면 그것을 우선한다. 이 서버가 다루는 Admin API 쓰기·Analytics 기능을 공식 MCP가 모두 제공한다는 근거는 확인하지 못했다.

## 연결 범위

| 범위 | 현재 작업 정의 | 계정에서 확인할 것 |
|---|---:|---|
| Admin API | 502 | 앱의 `mall.read_*`·`mall.write_*` 권한과 각 작업의 사용 조건 |
| Analytics API | 24 | 통계 API 접근 권한, 조회 기간·응답 형식 |
| MCP 도구 | 20 | 각 카테고리의 `action` 목록과 매개변수 |

Claude 연결 정보는 플러그인의 `.mcp.json`과 `.claude-plugin/plugin.json`의 `userConfig`에서 선언한다. ChatGPT Work는 `.codex-plugin/plugin.json`의 상대 경로와 `cwd`로 서버를 시작한다. 앱에서 입력 폼이나 도구가 실제로 표시되는지는 호스트별로 확인해야 한다. 직접 설정할 때는 자격증명 파일 `Path.home() / ".moai" / "mcp" / "cafe24.json"`도 읽는다. Windows와 macOS·Linux 모두 사용자 홈 디렉터리를 기준으로 해석한다. 토큰과 비밀값을 문서·채팅·로그에 붙여 넣지 않는다.

## 앱과 토큰

1. [카페24 개발자 문서](https://developers.cafe24.com/en/app/front/app)에서 앱을 만들고 필요한 권한만 선택한다.
2. 판매자 몰에서 OAuth 인가를 마친 뒤 발급된 토큰을 플러그인 자격증명에 입력한다. 이 서버는 최초 브라우저 인가 화면을 제공하지 않는다.
3. 액세스 토큰 만료로 HTTP 401을 받으면 서버는 리프레시 토큰으로 한 번 갱신을 시도한다. 카페24의 회전된 리프레시 토큰은 사용자 홈의 `.moai/mcp/cafe24-tokens.json`에 저장한다.
4. 저장에 실패하면 다음 앱 실행에서 인증이 끊길 수 있다. 서버 경고를 확인하고 새 인가가 필요한지 판단한다.

필요한 값은 `CAFE24_MALL_ID`, `CAFE24_CLIENT_ID`, `CAFE24_CLIENT_SECRET`, `CAFE24_ACCESS_TOKEN`, `CAFE24_REFRESH_TOKEN`이다. `CAFE24_API_VERSION`은 앱에 적용된 API 버전을 명시할 때 사용한다. 기본값은 현재 코드의 `2026-03-01`이며, 실제 앱의 지원 버전은 개발자센터에서 확인한다.

## 호출

예를 들어 상품 목록은 `cafe24_product(action="list", params={"limit": 20})`, 상품 상세는 `cafe24_product(action="get", params={"product_no": 128})` 형태다. 작업 이름·필수 본문·권한은 대상 서버의 `tools/list`와 [카페24 Admin API 문서](https://developers.cafe24.com/docs/en/api/admin/)에서 확인한다. 생성·수정·삭제 전에 대상 몰·상품·주문과 변경 범위를 사용자에게 보여준다.

`paginate=true`는 목록을 여러 번 읽을 수 있다. 작업마다 조회 상한과 커서 방식이 달라 자동 페이지네이션이 완전한 전체 수집을 보장하지 않는다. 429 응답은 제한된 횟수만 재시도한다. 이미 처리됐을 수 있는 쓰기 요청은 응답이 불분명할 때 결과 상태를 확인하고 중복 실행을 피한다.

## 개발 검증

이 저장소에서는 `uv run --directory plugins/moai-seller/mcp-servers/moai-mcp-cafe24 --group dev pytest -q`로 로컬 테스트를 실행한다. `uv`와 Python은 개발 환경의 준비물이다. 데스크톱 앱 사용자에게 터미널 설치를 요구하는 안내가 아니다. macOS·Windows·Linux와 Claude Cowork·ChatGPT Work에서 자격증명 입력, 서버 시작, 실제 API 호출까지 별도로 확인해야 한다.
