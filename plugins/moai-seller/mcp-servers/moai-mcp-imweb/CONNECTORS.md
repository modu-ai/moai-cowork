# 아임웹 OPEN API 연동

이 서버는 아임웹 [공식 개발자 문서](https://developers-docs.imweb.me/)의 앱 등록·OAuth 인가 절차로 발급한 자격증명을 사용합니다. 사이트별 이용 권한과 필요한 scope는 호출할 작업의 공식 명세에서 확인하세요. 실제 계정 인가가 끝나기 전에는 주문·상품 작업을 실행할 수 없습니다.

## 준비

1. 아임웹 개발자센터에서 앱을 등록하고 필요한 권한을 신청합니다. 인가 URL·토큰 요청의 필드와 사용 가능한 scope는 최신 [공식 명세](https://developers-docs.imweb.me/reference/openapi.json)를 따릅니다.
2. 앱의 인가 절차를 거쳐 access token과 refresh token을 발급받습니다. 이 MCP 서버는 최초 브라우저 인가를 대신하지 않습니다.
3. 데스크톱 앱의 플러그인 설정에서 자격증명을 입력합니다. 호스트가 해당 설정을 서버 환경변수로 전달하지 않는 경우, 사용자 홈의 `.moai/mcp/imweb.json` 파일을 사용할 수 있습니다. Windows에서도 사용자 홈 아래 같은 경로를 사용합니다.

```json
{
  "IMWEB_CLIENT_ID": "<앱 ID>",
  "IMWEB_CLIENT_SECRET": "<앱 시크릿>",
  "IMWEB_ACCESS_TOKEN": "<액세스 토큰>",
  "IMWEB_REFRESH_TOKEN": "<갱신 토큰>"
}
```

`IMWEB_UNIT_CODE`는 작업에 필요한 경우에만 지정합니다. 값은 해당 사이트의 유닛 코드여야 하며, 통화 코드로 가정하지 않습니다. 토큰은 비밀로 보관하고 저장소에 커밋하지 마세요.

## 동작과 확인

서버는 인증 헤더에 access token을 넣습니다. 401 응답 시 refresh token으로 한 번 갱신한 뒤 재시도합니다. 갱신 토큰이 유효하지 않으면 앱 인가 절차를 다시 진행해야 합니다. 도구 등록 여부는 MCP 클라이언트의 도구 목록에서 확인하고, API 권한은 허용된 읽기 작업으로 계정에서 별도 검증하세요.

기본 API 주소는 `https://openapi.imweb.me`입니다. `IMWEB_API_BASE`, `IMWEB_TOKEN_FILE`, `IMWEB_REQUEST_DELAY` 설정은 필요한 경우에만 사용합니다. 기본 토큰 파일 위치와 자격증명 우선순위는 서버의 `_base.py`와 공유 코어 구현을 기준으로 합니다.
