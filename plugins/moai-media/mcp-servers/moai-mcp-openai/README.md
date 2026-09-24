# OpenAI GPT Image 2.5 MCP

`moai-mcp-openai`는 OpenAI Image API의 `gpt-image-2.5-flare`와
`gpt-image-2.5-sunburst`를 직접 지정해 이미지를 생성합니다. 생성 요청은 별도
OpenAI API 계정에 청구됩니다. ChatGPT 앱 구독이나 로그인 정보로 API 인증을
대체하지 않습니다.

앱의 MCP 연결 설정에서 `OPENAI_API_KEY`를 입력할 수 없다면, 사용자의 컴퓨터에서
`~/.moai/mcp/openai.json`(Windows에서는 사용자 프로필의 `.moai/mcp/openai.json`)을
만들고 `{"OPENAI_API_KEY":"발급받은 키"}`를 저장하세요. 키를 채팅에 입력하지
마세요. 파일은 저장소에 넣지 않습니다.

macOS·Linux에서 파일을 쓸 때는 `.moai/mcp` 폴더를 소유자 전용(`0700`),
`openai.json`을 소유자 읽기·쓰기 전용(`0600`)으로 설정해야 서버가 키를
사용합니다. Windows에서는 파일 속성 → 보안에서 본인 계정의 접근 권한을 확인하세요.
Windows ACL의 자동 검사는 아직 구현되지 않았습니다.

서버는 `openai_image_generate` 도구 한 개를 제공합니다. 모델은 위 두 값 중 하나만
받고 한 번의 호출에 한 장만 생성합니다. 결과 이미지는 MCP 이미지 블록으로 돌려줍니다.
실제 API 계정 인증과 과금, 데스크톱 앱의 이미지 표시 여부는 별도로 확인해야 합니다.

개발 검사: `uv run --directory plugins/moai-media/mcp-servers/moai-mcp-openai
--group dev pytest -q`
