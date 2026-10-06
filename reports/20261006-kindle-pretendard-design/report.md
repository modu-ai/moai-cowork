# 킨들 시안 Pretendard 적용

## Claim · 변경 내용

한글·영문과 제목·본문·표·버튼·입력·코드·Mermaid를 Pretendard Variable 1.3.9로 통일했다. 제목은 실제 700 굵기를 사용한다. 킨들 배경 색상과 픽셀 PNG 두 장은 바꾸지 않았다. 이미지 안에 그려진 픽셀 글자는 그대로다. 전체 문서 반영은 이전 요청대로 보류하고 검토용 시안만 수정했다.

## Evidence · 확인 결과

공식 고정 버전의 웹폰트를 내려받아 로컬에서 제공한다. 파일 출처·해시는 `font-source.json`, 라이선스는 `assets/fonts/Pretendard-LICENSE.txt`에 있다. 실제 브라우저에서 400·700 굵기 로드 완료를 확인했다. 4개 화면을 390·768·1440px에서 검사했다. 모든 측정 텍스트의 첫 글꼴이 Pretendard였다. Mermaid 원본 5개를 새 글꼴로 다시 렌더링했고 시안에는 그중 3개를 사용한다.

실행 명령:

```bash
python3 www/design-system/eink-proposal/build.py
python3 reports/20261006-kindle-pretendard-design/verify.py
```

검증 출력 그대로:

```json
{"layouts": 12, "measured_texts": 516, "minimum_font_px": 16.0, "minimum_contrast": 6.12, "page_overflow": 0, "svg_text_clips": 0, "minimum_mobile_content_width": 335, "duplicate_ids": 0, "broken_aria_references": 0, "inline_svg": 4, "pixel_images": 2, "pretendard_loaded": true, "remote_render_assets": 0, "original_files_unchanged": 191, "http": [{"path": "index.html", "status": 200, "bytes_match": true}, {"path": "assets/parallel-pixel-ko.png", "status": 200, "bytes_match": true}, {"path": "assets/context-pixel-ko.png", "status": 200, "bytes_match": true}, {"path": "assets/fonts/PretendardVariable.woff2", "status": 200, "bytes_match": true}, {"path": "assets/fonts/Pretendard-LICENSE.txt", "status": 200, "bytes_match": true}]}
```

`before/tokens.json`과 현재 색상 토큰이 같고, 두 픽셀 PNG의 SHA-256도 같음을 검사했다. 새 폰트·이미지·HTML·라이선스의 로컬 HTTP 응답은 모두 200이며 파일 바이트가 일치한다. 현재 브라우저 탭도 새로고침했다.

## Baseline-attribution · 측정 대상

작업 트리: `/Users/goos/.codex/worktrees/b0aa/moai-cowork`. 세션: `01a10aae-6716-7681-b5d7-d558155d9f86`. HTML SHA-256: `d4c7396e9e5eefcba84cff3a15440c6f2044b69fb458bbe423f7bfa76b95703b`. 로컬 시안: `http://127.0.0.1:1314/`. 기존 문서·사이트 CSS·partials 191개의 이전 해시와 일치한다. 이전 픽셀 폰트 시안은 `before/`에 보존했다.

## Gaps · 확인하지 않은 범위

실제 Kindle 기기와 중문·일문 조판, 다른 브라우저는 검사하지 않았다. 이번 변경에서 복사·폼 기능을 새로 시험하지는 않았다. 전체 사이트 적용·공개 배포는 진행하지 않았다.

## Residual-risk · 남은 조건

픽셀 그림은 이미지이므로 웹폰트 변경의 영향을 받지 않는다. 모바일에서는 큰 그림과 도식을 해당 영역 안에서 가로로 이동해 읽는다. 일반 텍스트와 Mermaid의 현재 측정에서는 가로 넘침·글자 잘림이 없었다.

캡처: `home-desktop.png`, `home-mobile.png`, `diagrams-desktop.png`. 기준 문서: `www/design-system/eink-proposal/README.md`.
