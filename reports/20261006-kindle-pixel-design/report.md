# 킨들·픽셀 디자인 시안 검토 보고

## Claim · 만든 내용

사용자의 최신 요청에 맞춰 킨들 리더를 연상시키는 회백색 바탕, 각진 선과 면, 한글 픽셀 폰트로 시안을 제작했다. 이후 “먼저 시안을 제공” 요청을 받아 전체 사이트 반영은 진행하지 않았다.

홈·강의 본문·인포그래픽·구성 요소의 네 화면을 제공한다. 기본 Neo둥근모와 코드용 Neo둥근모 Code는 공식 웹폰트 1.601을 로컬 파일로 제공한다. 두 개의 픽셀 PNG는 내장 이미지 생성 도구로 새로 제작했고, 한글 라벨과 연결 방향을 생성 결과 및 실제 문서 화면에서 육안 확인했다. 질문 분기·인계·재사용 Mermaid 3개와 수치 차트 1개도 포함한다.

시안: [홈](http://127.0.0.1:1314/#home) · [강의](http://127.0.0.1:1314/#lesson) · [인포그래픽](http://127.0.0.1:1314/#diagrams) · [구성 요소](http://127.0.0.1:1314/#components).

## Evidence · 실제 확인

실제 CUA 브라우저에서 390·768·1440px 뷰포트로 네 화면을 각각 확인했다. 스크롤바를 제외한 본문 화면 폭은 375·753·1425px였다. 모바일 본문 폭은 335px이며, 그림 영역 폭은 333px이다. 키보드 오른쪽 화살표로 그림의 가로 위치가 0에서 40px로 이동했다.

요청 복사는 원문과 일치했고 기존 클립보드를 복원했다. 키보드 탭 전환, 목표 입력·환경 선택·확인, 답안 펼치기가 동작했다. 두 픽셀 글꼴의 실제 로드 완료를 확인했다. 이미지 3회 배치 모두 원본 1536×1024 픽셀로 로드됐다. 기록된 브라우저 오류는 없었다.

실행 명령:

```bash
python3 www/design-system/eink-proposal/build.py
python3 reports/20261006-kindle-pixel-design/verify.py
```

검증 명령 출력 그대로:

```json
{"layouts": 12, "measured_texts": 516, "minimum_font_px": 16.0, "minimum_contrast": 6.12, "page_overflow": 0, "svg_text_clips": 0, "minimum_mobile_content_width": 335, "duplicate_ids": 0, "broken_aria_references": 0, "inline_svg": 4, "pixel_images": 2, "pixel_fonts_loaded": true, "remote_render_assets": 0, "copy_exact": true, "keyboard_tabs": true, "form_confirmation": true, "quiz_open": true, "original_files_unchanged": 191, "http": [{"path": "index.html", "status": 200, "bytes_match": true}, {"path": "assets/parallel-pixel-ko.png", "status": 200, "bytes_match": true}, {"path": "assets/context-pixel-ko.png", "status": 200, "bytes_match": true}, {"path": "assets/fonts/NeoDunggeunmo.woff2", "status": 200, "bytes_match": true}, {"path": "assets/fonts/NeoDunggeunmoCode.woff2", "status": 200, "bytes_match": true}, {"path": "assets/fonts/LICENSE.txt", "status": 200, "bytes_match": true}]}
```

캡처: `home-desktop.png`, `lesson-pixel-desktop.png`, `context-desktop.png`, `components-desktop.png`, `home-mobile.png`, `lesson-mobile.png`. 모두 실제 브라우저에서 촬영했다.

공식 [Neo둥근모 웹폰트](https://github.com/neodgm/neodgm-webfont)와 [글꼴 사용 지침](https://neodgm.dalgona.dev/guides.html)에 따라 16px 배수 크기와 일반 굵기를 사용했다. [Mermaid 설정](https://mermaid.js.org/config/schema-docs/config.html)을 참고하고 저장소 번들로 실제 렌더링했다. 원본 번들은 바꾸지 않았으며 로컬 준비용 도우미만 폰트 로드를 기다리도록 구성했다.

## Baseline-attribution · 측정 대상

- 작업 트리: `/Users/goos/.codex/worktrees/b0aa/moai-cowork`
- HEAD: `2c3cef1d24e88b3bfe8db61c713ffae317b346d0`, detached HEAD
- 세션: `01a10aae-6716-7681-b5d7-d558155d9f86`
- 최종 HTML SHA-256: `7dfb37aa5521787cf017e10adae33d532fb7c1004e51db4e4be1281da18968f3`
- 로컬 서버: `http://127.0.0.1:1314/`
- 기존 문서·사이트 CSS·partials 191개는 이번 시안 작업 전후 SHA-256이 일치한다. 이 수치는 전체 저장소의 미변경 여부를 주장하지 않는다.
- 변경 전 A/B 시안은 이 보고서 폴더의 `before/`에 보존했다.

## Gaps · 이번에 확인하지 않은 범위

실제 Kindle 기기, 다른 브라우저, Google Noto CJK 로딩 및 중문·일문 조판은 검사하지 않았다. 픽셀 PNG의 글자와 화살표는 육안으로 확인했고 자동 OCR 검사는 하지 않았다. Work/Cowork의 실제 업무 실행, 전체 문서 개편 반영, 공개 배포는 이번 시안 확인의 범위가 아니다.

## Residual-risk · 적용 때 확인할 점

큰 픽셀 그림은 모바일에서 영역 안 가로 이동이 필요하다. 축소로 글자가 작아지는 대신 원본을 확대해서 열 수 있다. 사용자 선택 후 전체 문서에 반영할 때는 각 본문의 개념·자료·관계를 검토해 그림을 제작하고, 실제 앱 캡처는 원본 색과 화면을 유지해야 한다.

구성·규칙: `www/design-system/eink-proposal/README.md`. 생성 프롬프트·이미지 원본 경로: `image-prompts.md`. 글꼴 출처·해시: `font-sources.json`. 재현 가능한 검사: `verify.py`와 각 JSON 측정 기록.
