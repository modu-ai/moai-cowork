# 공통 플러그인 스키마

2026-10-05에 Agent Plugins 1.0.0 공식 스키마를 그대로 저장했다.

- [plugin.schema.json 원본](https://agent-plugins.org/schemas/1.0.0/plugin.schema.json)
- [mcp.schema.json 원본](https://agent-plugins.org/schemas/1.0.0/mcp.schema.json)
- [OpenAI의 공통 패키지 안내](https://developers.openai.com/plugins/build/plugins)

CI는 저장된 파일로 검사한다. 스키마 갱신은 공식 버전과 변경 내용을 검토한 후 별도 변경으로 처리한다.

호환 매니페스트가 이 저장소의 생성 입력이다. `uv run --no-project --with pyyaml python scripts/sync-plugin-contracts.py`로 루트 매니페스트와 PM 추천 카탈로그를 갱신한다. `--check`는 파일을 수정하지 않는다. OpenAI 확장 설정은 전체 overlay 우선순위에 맞춰 한 객체로 생성하며, 공통 MCP는 실제 transport 타입을 선언한다.
