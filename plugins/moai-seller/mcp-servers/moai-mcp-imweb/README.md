# 아임웹 OPEN API MCP

아임웹 [공식 OPEN API 명세](https://developers-docs.imweb.me/reference/openapi.json)를 바탕으로 만든 판매자용 MCP 서버입니다. 현재 명세의 OAuth 엔드포인트 2개를 제외한 작업 138개를 카테고리 도구 8개에 묶었습니다. 실제 호출에는 해당 사이트의 앱 권한과 유효한 토큰이 필요합니다.

## 구성

- MCP 서버 키와 실행 파일: `moai-mcp-imweb`
- 실행: 플러그인의 `.mcp.json`에 지정된 `uv run --directory ${CLAUDE_PLUGIN_ROOT}/mcp-servers/moai-mcp-imweb moai-mcp-imweb`
- 도구: `imweb_site_info`, `imweb_member_info`, `imweb_community`, `imweb_promotion`, `imweb_product`, `imweb_order`, `imweb_script`, `imweb_payment`
- 각 도구는 `action`으로 작업을 고릅니다. 경로·조회 조건은 `params`, 요청 본문은 `body`에 넣습니다. `paginate=True`는 명세에 `page`와 `limit`가 있는 GET 작업에만 사용합니다.
- 액세스 토큰 만료 시 refresh token을 이용한 갱신을 지원합니다. 초기 앱 등록·인가·토큰 발급은 [연동 안내](./CONNECTORS.md)를 따릅니다.

## 명세 갱신

공식 명세를 `tools/openapi.json`에 저장한 뒤 다음 명령을 실행합니다. 생성된 `src/moai_mcp_imweb/tools/*.py`는 직접 수정하지 않습니다.

```text
uv run --directory mcp-servers/moai-mcp-imweb python tools/_generator.py
uv run --directory mcp-servers/moai-mcp-imweb --group dev pytest -q
```

위 상대 경로는 `plugins/moai-seller`에서 실행할 때 기준입니다. 도구 생성·단위 테스트 통과는 실제 아임웹 계정 권한이나 API 호출 성공을 뜻하지 않습니다.
