# 스마트스토어 연결

판매자 또는 앱 운영자가 [네이버 커머스API 센터](https://apicenter.commerce.naver.com/docs/introduction)에서 앱과 필요한 API 그룹 권한을 준비한다. 인증의 서명·토큰 규격은 [공식 인증 문서](https://apicenter.commerce.naver.com/docs/auth)를 따른다. 통계 API데이터솔루션은 별도 사용 조건을 확인한다.

## 필요한 값

- `NAVER_COMMERCE_CLIENT_ID`: 발급된 앱 ID
- `NAVER_COMMERCE_CLIENT_SECRET`: 발급된 앱 시크릿
- `NAVER_COMMERCE_TYPE`: 본인 계정의 `SELF` 또는 판매자 대행 앱의 `SELLER`
- `NAVER_COMMERCE_ACCOUNT_ID`: `SELLER` 유형에 필요한 판매자 계정 ID

플러그인의 Claude 설정에는 입력 항목이 선언돼 있다. 사용하는 앱에서 자격증명 입력 기능을 제공하는지 확인한다. 제공하지 않는 경우 서버는 사용자 홈의 `.moai/mcp/smartstore.json`도 읽는다. 정확한 경로는 macOS·Linux·Windows 모두 사용자 홈 디렉터리를 기준으로 해석한다. 비밀값을 코드·저장소·채팅·공유 문서에 넣지 않는다.

자격증명 파일의 키는 위 환경변수 이름과 동일하다. `plugins/moai-seller/.mcp.json`에 실제 비밀값을 직접 적지 않는다. `user_config` 입력값이 호스트에서 전달되지 않는 경우 서버는 자리표시자를 무시하고 사용자 홈의 파일을 확인한다.

## 연결 확인

MCP 도구 `smartstore_config_status`는 설정 항목의 존재 여부를 보여준다. `smartstore_test_connection`은 실제 토큰 발급과 읽기 API를 호출하므로 판매자 계정으로 연결 확인할 때 사용한다. 응답이 성공해도 다른 API 그룹의 권한까지 확인된 것은 아니다. 실패 시 비밀값을 공유하지 말고 HTTP 상태와 공식 API 센터의 앱 권한을 대조한다.

현재 `.mcp.json` 서버 키는 `moai-mcp-smartstore`, 실행 명령은 `uv`, 배포 엔트리포인트는 `moai-mcp-smartstore`다. 게시되지 않은 PyPI 패키지를 `uvx`로 설치하라는 예전 안내는 사용하지 않는다.
