# 한국어 폰트 정책 — doc-html-report

`moai-officer:doc-html-report`의 선택형 웹폰트 CDN과 폴백 참고 자료. 최종 산출물에서 URL 접근성과 라이선스 조건을 다시 확인합니다.

---

## 폰트 정책 근거

폰트 CDN도 네트워크 연결, URL 변경, 라이선스 조건에 영향을 받습니다. 오프라인 파일에서는 시스템 폴백으로 문서를 읽을 수 있게 만들고 실제 렌더를 확인합니다. macOS, Windows, Linux의 기본 서체와 줄바꿈은 같지 않습니다.

---

## 모드별 폰트 매핑 표

| 모드 | sans (본문) | serif (제목·강조) | mono (코드·태그) | CDN 출처 |
|------|-------------|-------------------|------------------|---------|
| `status` | Pretendard | Pretendard 700 | JetBrains Mono | jsdelivr + Google |
| `financial` | Pretendard | Pretendard 700 | JetBrains Mono | jsdelivr + Google |
| `pr` | Pretendard | Pretendard 700 | JetBrains Mono | jsdelivr + Google |
| `incident` | Pretendard | Pretendard 700 | JetBrains Mono | jsdelivr + Google |
| `plan` | Pretendard | Noto Serif KR | JetBrains Mono | jsdelivr + Google |
| `explainer` | Noto Sans KR | Noto Serif KR | JetBrains Mono | Google |

---

## CDN URL 및 라이선스

### Pretendard
- **라이선스**: OFL-1.1 (SIL Open Font License)
- **CDN**: jsDelivr (GitHub 미러, pinned v1.3.9)
- **URL**: `https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css`
- **포함 웨이트**: 100-900 (Variable Font)
- **preconnect 호스트**: `https://cdn.jsdelivr.net`

### Noto Serif KR + Noto Sans KR (Google Fonts)
- **라이선스**: OFL-1.1
- **CDN**: Google Fonts API
- **URL (결합)**: `https://fonts.googleapis.com/css2?family=Noto+Serif+KR:wght@400;700&family=Noto+Sans+KR:wght@400;700&display=swap`
- **preconnect 호스트**: `https://fonts.googleapis.com`, `https://fonts.gstatic.com`

### JetBrains Mono (Google Fonts)
- **라이선스**: SIL Open Font License 1.1 ([JetBrains 공식 안내](https://www.jetbrains.com/lp/mono/))
- **CDN**: Google Fonts API
- **URL**: `https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500&display=swap`
- **preconnect 호스트**: `https://fonts.googleapis.com`, `https://fonts.gstatic.com`

---

## preconnect 패턴

### status / financial / pr / incident 모드 (Pretendard + JetBrains Mono)

```html
<link rel="preconnect" href="https://cdn.jsdelivr.net" crossorigin>
<link rel="preconnect" href="https://fonts.googleapis.com" crossorigin>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500&display=swap">
```

### plan 모드 (Pretendard + Noto Serif KR + JetBrains Mono)

```html
<link rel="preconnect" href="https://cdn.jsdelivr.net" crossorigin>
<link rel="preconnect" href="https://fonts.googleapis.com" crossorigin>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Serif+KR:wght@400;700&family=JetBrains+Mono:wght@400;500&display=swap">
```

### explainer 모드 (Noto Sans KR + Noto Serif KR + JetBrains Mono)

```html
<link rel="preconnect" href="https://fonts.googleapis.com" crossorigin>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700&family=Noto+Serif+KR:wght@400;700&family=JetBrains+Mono:wght@400;500&display=swap">
```

---

## CSS 변수 오버라이드 패턴

모드별 폰트 적용은 `:root`의 `--sans`, `--serif`, `--mono` 오버라이드로 처리합니다.

```css
/* status / financial / pr / incident 기본 */
:root {
  --sans:  "Pretendard", system-ui, -apple-system, sans-serif;
  --serif: "Pretendard", ui-serif, Georgia, serif;
  --mono:  "JetBrains Mono", ui-monospace, "SF Mono", monospace;
}

/* plan 모드 override */
:root {
  --serif: "Noto Serif KR", ui-serif, Georgia, serif;
}

/* explainer 모드 override */
:root {
  --sans:  "Noto Sans KR", system-ui, sans-serif;
  --serif: "Noto Serif KR", ui-serif, Georgia, serif;
}

```

---

## font-display: swap 일관 적용

Google Fonts URL에 `&display=swap`을 항상 포함합니다.
Pretendard CDN의 CSS와 최종 브라우저에서 `font-display` 및 폴백 동작을 확인합니다.

---

## 변경 이력

| 날짜 | 버전 | 변경 내용 |
|------|------|-----------|
| 2026-05-09 | 1.0.0 | 초기 작성 — 6개 폰트 매핑, CDN URL, preconnect 패턴 |
