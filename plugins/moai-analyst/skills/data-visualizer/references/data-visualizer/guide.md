# 시각화 가이드

## Chart.js 차트 HTML 템플릿

HTML 파일 생성 시 아래 구조를 따릅니다:
- DOCTYPE html, UTF-8 인코딩
- 전달 환경에서 실제 접속이 확인된 경우에만 Chart.js CDN 사용: https://cdn.jsdelivr.net/npm/chart.js
- 오프라인 전달이면 사용 허가된 로컬 스크립트를 포함하거나 외부 의존성이 없는 SVG 차트 사용
- 한국어 폰트: Pretendard 또는 시스템 폰트
- 반응형: 선택한 canvas 또는 SVG의 너비 조정

## Mermaid 차트 종류

| 유형 | 용도 | 문법 |
|------|------|------|
| pie | 비율/구성 | pie title "제목" |
| xychart-beta | 막대/선 | xychart-beta |
| flowchart | 프로세스 | flowchart TD |
| gantt | 일정 | gantt |

## 색상 팔레트 (한국 비즈니스)

기본 5색: #2563EB, #DC2626, #059669, #D97706, #7C3AED
