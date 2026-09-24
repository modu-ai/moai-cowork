# moai-mcp-smartstore

네이버 [커머스API](https://apicenter.commerce.naver.com/docs/introduction)를 연결하는 자체 제작 MCP 서버다. 현재 서버 import에서 **90개 도구**가 등록된다. 도구 등록은 판매자 계정의 API 권한이나 실제 주문·상품 처리 성공을 뜻하지 않는다.

## 연결

플러그인은 `plugins/moai-seller/.mcp.json`의 `uv run --directory ... moai-mcp-smartstore` 경로로 이 서버를 시작한다. 도구·자격증명 입력은 사용하는 데스크톱 앱에서 확인한다. 인증 정보는 `CONNECTORS.md`를 따른다. 현재 계정에 승인된 API 그룹만 호출할 수 있고, 통계는 별도 서비스 신청이 필요할 수 있다.

| 영역 | 도구 예 |
|---|---|
| 상품 | `product_search`, `product_get_origin` |
| 주문 | `order_changed_product_orders`, `order_dispatch` |
| 정산·문의 | `settlement_daily`, `qna_list` |
| 물류·판매자·솔루션 | `sku_get`, `seller_account`, `solution_subscription_get` |
| 통계 | `stats_marketing`, `stats_sales` |

도구의 현재 목록은 MCP `tools/list`로 확인한다. 작업마다 필수 매개변수와 권한이 다르므로 [공식 API 문서](https://apicenter.commerce.naver.com/docs/introduction)의 해당 작업과 계정 승인 상태를 대조한다. `403` 또는 `400`만 보고 권한 승인 여부를 확정하지 않는다. 주문·환불·상품 삭제 같은 변경 작업은 대상과 현재 상태를 확인한 뒤 호출하고, 응답이 불분명하면 중복 실행 전에 결과를 조회한다.

## 인증

네이버 커머스API의 Client Credentials 인증은 `client_id`, `client_secret`과 밀리초 타임스탬프의 bcrypt 서명을 사용한다. 토큰은 만료 전 갱신하며 `401`과 `GW.AUTHN`이 함께 나타날 때 한 번 다시 발급한다. 첫 인증과 그룹별 권한 신청은 판매자 또는 앱 운영자가 공식 API 센터에서 진행한다.

2026-07-10에 별도 계정으로 읽기 요청을 확인했다는 과거 기록이 있었지만, 현재 계정의 권한이나 이 버전의 실 API 동작을 증명하지 않는다. 이 작업 트리의 로컬 테스트도 실제 판매자 계정을 호출하지 않는다.

## 개발 검증

`uv run --directory plugins/moai-seller/mcp-servers/moai-mcp-smartstore --extra dev pytest -q`로 로컬 단위 테스트를 실행한다. 실인증 점검 스크립트 `scripts/check_auth.py`는 판매자 자격증명과 외부 호출이 필요하므로 계정 운영자의 테스트에서만 사용한다. 데스크톱 앱 사용자에게 터미널 설치를 요구하는 절차는 아니다.

## 라이선스

Apache-2.0. 네이버와의 제휴·보증 관계를 뜻하지 않는다.
