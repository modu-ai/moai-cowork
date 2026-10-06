# 모두의 코워크 · 한국어 온라인 강의 문서

ChatGPT Work와 Claude Cowork로 첫 결과물부터 프로젝트 업무와 전문가 협업까지 배우는 Hugo 문서 사이트입니다. 공개 주소는 https://cowork.mo.ai.kr/ 입니다. 로컬 수정과 공개 배포의 상태는 따로 확인합니다.

## 학습 구조

- `content/getting-started/`: 사용 환경, 개념, 첫 결과물, 질문과 프로젝트 지침.
- `content/learn/`: 6개 수업, 실제 화면 안내, 강사용 진행·평가 안내.
- `content/workflows/`: 프로젝트 맥락, 역할과 스킬, 업무 순서, 권한, 검토와 반복.
- `content/cookbook/`: 업무별 실습, 프로젝트, 트랙, 가이드, 템플릿.
- `content/moai-agents/`: 역할별 준비물, 가상 사례, 소스 기반 스킬과 에이전트 카탈로그.
- `content/plugins/`: 설치, MCP, 인증, 라이선스와 고지.
- `content/help/`: 계정, 사용량, 문제 해결, 공식 자료 색인.
- `content/advanced/`: 개발자 설정, 검증, 문서 제작과 화면 촬영.
- `content/releases/`: 변경 기록. 과거 내용과 URL을 유지하며 현재 안내와 구분.

목차는 `data/menu/main.yaml`에서 관리합니다. 플러그인 수와 스킬 수는 `data/agent_teams.json`에서 읽으며 내 계정의 설치 수와 구분합니다. 데이터 갱신 절차는 저장소의 생성·정합성 검사기를 따릅니다.

## 구현과 파일

Hugo extended 0.160.1과 저장소 안의 `themes/hugo-geekdoc` 테마를 사용합니다. `hugo.toml`의 테마 설정은 로컬 테마 경로를 사용하므로 실행 전에 테마를 자동 업데이트하지 않습니다.

- `layouts/`: 헤더, 검색, 메뉴, 수업 이동과 이미지 렌더링.
- `static/moai-learning.css`: 수업 카드, 이미지, 답안, 모바일 표·코드 표시.
- `static/infographics/`: 한국어 개념 그림. 앱 UI의 실제 증거로 사용하지 않습니다.
- `static/screenshots/20261005/`: 실제 웹 화면. `content/learn/screens.md`에 상태와 촬영 범위를 기록합니다.
- `static/downloads/classroom/`: 가상 CSV·정책·업무 메모. 실제 고객 자료가 아닙니다.

글꼴과 기존 디자인 시스템 로딩 순서는 `layouts/partials/head/custom.html`을 따릅니다. 강의 스타일은 기존 스타일 뒤에 추가합니다.

## 빌드와 검사

저장소 루트에서 실행합니다. 빌드 출력은 소스와 분리된 위치에 만듭니다.

```bash
hugo --source www --destination /tmp/moai-docs-preview --enableGitInfo=false --quiet --minify
python3 scripts/check-docs.py /tmp/moai-docs-preview
hugo server --source www --bind 127.0.0.1 --port 1313 --disableFastRender --enableGitInfo=false
```

검사기는 로컬 링크·앵커·그림 alt·검색 대상·사이트맵·가상 자료와 수업 구조를 확인합니다. 그 다음 실제 브라우저에서 수업 이동, 그림 확대, 답안 펼치기, 검색과 모바일 메뉴를 확인합니다. 파일 빌드와 링크 검사를 실제 앱 업무 수행이나 학습 효과 검증으로 보고하지 않습니다.

## 작성 기준

수업은 배울 내용, 쉬운 설명, 그림, 가상 사례, 실습 요청, 모범 결과, 흔한 실수, 확인 문제, 다음 단계로 구성합니다. 중요한 설명은 그림뿐 아니라 본문에도 남깁니다. 기능·메뉴는 현재 공식 문서와 실제 화면으로 확인하며 출처를 가까이 표시합니다.

실제 캡처는 직접 실행한 화면만 사용합니다. 개인정보는 접거나 촬영 범위에서 제외하고 촬영일·제품·환경·상태를 남깁니다. 접근하지 못한 화면은 미촬영으로 기록합니다. 생성한 개념 그림과 실제 캡처를 혼용하지 않습니다.

## 공개 배포

`vercel.json`은 Hugo 빌드 설정이며 Vercel 프로젝트의 루트는 `www`, 출력은 `public`입니다. 배포한 뒤 공개 주소의 학습 경로·검색·이미지·기존 URL을 다시 확인합니다. 로컬 검사 성공만으로 배포 완료라고 기록하지 않습니다.

## 라이선스

저장소의 `LICENSE`, `LICENSE-OUTPUT.md`, `NOTICE`와 제3자 자료의 조건을 함께 확인합니다. 자세한 내용은 온라인 문서의 산출물 권리 안내를 참고합니다.
