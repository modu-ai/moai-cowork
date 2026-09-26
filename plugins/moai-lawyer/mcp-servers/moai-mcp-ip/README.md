# moai-mcp-ip

특허·상표 공식 데이터 MCP 서버입니다. `moai-lawyer` 플러그인에 들어 있으며, 공식 기관이 MCP를 제공하지 않아 직접 만들었습니다.

| 소스 | 도구 |
|---|---|
| 자격증명 게이트 | `ip_check_access` |
| KIPRIS Plus (한국) | `kipris_patent_search` · `kipris_patent_detail` · `kipris_trademark_search` · `kipris_trademark_detail` |
| USPTO ODP·TSDR (미국) | `uspto_patent_search` · `uspto_patent_application` · `uspto_trademark_status` |
| JPO (일본) | `jpo_patent_progress` · `jpo_patent_registration` · `jpo_trademark_progress` · `jpo_trademark_registration` · `jpo_case_number_reference` · `jpo_applicant_lookup` |
| EPO OPS (유럽·국제) | `epo_search` · `epo_biblio` · `epo_family` · `epo_legal` |

API 등록과 자격증명 설정: [CONNECTORS.md](CONNECTORS.md)

## 원칙

- 조사 전에 `ip_check_access` 로 필요한 소스를 확인합니다. 없으면 검색하지 않고 등록 안내를 돌려줍니다.
- 자격증명 값은 어떤 응답·오류 메시지에도 싣지 않습니다(KIPRIS 키가 섞일 수 있는 오류 문자열은 가립니다).
- 자격증명은 `moai_mcp_core.CredentialStore` 로 해석합니다 — 환경변수 → `~/.moai/mcp/ip.json`.
- JPO·EPO 토큰은 메모리에서만 발급·갱신합니다.
- TLS 검증을 끄지 않습니다.

## 실행

```bash
uv run --directory plugins/moai-lawyer/mcp-servers/moai-mcp-ip moai-mcp-ip
```

## 테스트

네트워크 없이 `httpx.MockTransport` 로 돌립니다.

```bash
uv run --directory plugins/moai-lawyer/mcp-servers/moai-mcp-ip pytest -q
```

`src/moai_mcp_core/` 는 복제본입니다. 수정은 `plugins/_shared/moai-mcp-core/` 에서 하고 `python3 scripts/sync-mcp-core.py` 로 동기화합니다.
