---
version: alpha
name: Linear-design-analysis
description: 울트라 미니멀·퍼플 (getdesign.md 컬렉션 — 테마_컴포넌트_쇼케이스에서 추출한 경량 토큰. 풍부한 브랜드 분석·typography 스케일은 추후 보강.)

colors:
  primary: "#7c84ec"
  primary-active: "#7c84ec"
  ink: "#f4f4f6"
  body: "#f4f4f6"
  body-strong: "#f4f4f6"
  muted: "#8a8f98"
  muted-soft: "#8a8f98"
  hairline: "#2b2b33"
  hairline-soft: "#2b2b33"
  canvas: "#16161a"
  surface-soft: "#1f1f25"
  surface-card: "#1f1f25"
  surface-strong: "#1f1f25"
  on-primary: "#ffffff"
  success: "#22c55e"
  warning: "#f59e0b"
  error: "#ef4444"

typography:
  display-xl:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 72px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -2.5px
  display-lg:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 56px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -2px
  display-md:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -1.5px
  title-lg:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: -0.3px
  title-md:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0px
  body-lg:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0px
  body-md:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0px
  body-sm:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px

rounded:
  radius: 12px
  radius-button: 10px
  # 분류: dark (canvas luminance 기반)
---

# Linear 디자인 시스템

울트라 미니멀·퍼플. 본 파일은 `테마_컴포넌트_쇼케이스_전체.html`에서 추출한 경량 토큰이며, 풍부한 브랜드 분석과 typography 스케일은 추후 보강 예정입니다.

## 사용

별도 `moai-officer` 플러그인이 설치되고 현재 앱에서 `doc-html-report` 또는 `doc-html-slide` 스킬을 사용할 수 있다면 `design_system: linear.app` 값을 지정해 본 토큰을 참고할 수 있습니다. 해당 스킬이 없으면 이 파일의 토큰과 적용 지침만 제공합니다.
