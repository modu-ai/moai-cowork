# 일정 템플릿 (schedule-templates)

> moai-schedules v1.0.0 | 비즈니스 자동화 스케줄 템플릿 가이드

자동화 일정(Scheduled Task)으로 반복 실행할 수 있는 5가지 표준 비즈니스 스케줄 템플릿입니다.
Cowork `/schedule` 명령으로 각 템플릿을 등록할 수 있습니다.

---

## 템플릿 1: 매일 아침 브리핑

| 항목 | 내용 |
|------|------|
| **이름** | 매일 아침 브리핑 |
| **대상 스킬** | `moai-business:daily-briefing` |
| **실행 빈도** | 매일 오전 8:30 |
| **Cron 표현식** | `30 8 * * 1-5` (평일 기준) |

**프롬프트 전문:**
```
오늘의 주요 비즈니스 뉴스, 산업 동향, 일정을 요약해줘
```

**Cowork /schedule 설정:**
```
/schedule create \
  --name "매일 아침 브리핑" \
  --skill moai-business:daily-briefing \
  --cron "30 8 * * 1-5" \
  --prompt "오늘의 주요 비즈니스 뉴스, 산업 동향, 일정을 요약해줘"
```

**활용 팁:**
- 전날 저장된 즐겨찾기 뉴스 소스를 자동 포함
- 캘린더 연동 시 당일 미팅 일정 자동 추가
- 출력 결과를 Slack #daily-briefing 채널로 자동 전달 가능

---

## 템플릿 2: 주간 마케팅 리포트

| 항목 | 내용 |
|------|------|
| **이름** | 주간 마케팅 리포트 |
| **대상 스킬** | `moai-marketing:performance-report` |
| **실행 빈도** | 매주 월요일 오전 9:00 |
| **Cron 표현식** | `0 9 * * 1` |

**프롬프트 전문:**
```
지난 주 마케팅 성과를 채널별로 분석하고 KPI 달성률을 보고해줘
```

**Cowork /schedule 설정:**
```
/schedule create \
  --name "주간 마케팅 리포트" \
  --skill moai-marketing:performance-report \
  --cron "0 9 * * 1" \
  --prompt "지난 주 마케팅 성과를 채널별로 분석하고 KPI 달성률을 보고해줘"
```

**활용 팁:**
- 분석 채널: SNS, 이메일, 검색광고, 콘텐츠 마케팅
- 전주 대비 증감률 자동 계산
- KPI 미달 항목은 원인 분석 및 개선 제안 포함

---

## 템플릿 3: 월간 세무 체크

| 항목 | 내용 |
|------|------|
| **이름** | 월간 세무 체크 |
| **대상 스킬** | `moai-finance:tax-helper` |
| **실행 빈도** | 매월 20일 오전 10:00 |
| **Cron 표현식** | `0 10 20 * *` |

**프롬프트 전문:**
```
이번 달 세무 신고 마감일과 준비사항을 확인해줘
```

**Cowork /schedule 설정:**
```
/schedule create \
  --name "월간 세무 체크" \
  --skill moai-finance:tax-helper \
  --cron "0 10 20 * *" \
  --prompt "이번 달 세무 신고 마감일과 준비사항을 확인해줘"
```

**활용 팁:**
- 체크 항목: 부가세, 원천세, 법인세 중간예납, 4대보험
- 마감 D-10/D-3/D-1 알림 자동 추가 권장
- 사업자 유형(개인/법인)에 따라 맞춤 안내

---

## 템플릿 4: 분기 사업 리뷰

| 항목 | 내용 |
|------|------|
| **이름** | 분기 사업 리뷰 |
| **대상 스킬** | `moai-business:strategy-planner` |
| **실행 빈도** | 분기 마지막 금요일 (3/6/9/12월 마지막 금요일) |
| **Cron 표현식** | `0 9 * 3,6,9,12 5L` (지원 스케줄러 필요, 미지원 시 수동 등록) |

**프롬프트 전문:**
```
이번 분기 사업 성과를 분석하고 다음 분기 전략 방향을 제안해줘
```

**Cowork /schedule 설정:**
```
/schedule create \
  --name "분기 사업 리뷰" \
  --skill moai-business:strategy-planner \
  --cron "0 9 28-31 3,6,9,12 5" \
  --prompt "이번 분기 사업 성과를 분석하고 다음 분기 전략 방향을 제안해줘"
```

**활용 팁:**
- 분석 항목: 매출, 영업이익, 고객 수, 제품별 성과
- OKR/KPI 달성률 자동 계산
- 다음 분기 목표 초안 자동 작성
- 임원 보고용 요약본 별도 생성 가능

---

## 템플릿 5: 주간 CS 요약

| 항목 | 내용 |
|------|------|
| **이름** | 주간 CS 요약 |
| **대상 스킬** | `moai-support:escalation-manager` |
| **실행 빈도** | 매주 금요일 오후 5:00 |
| **Cron 표현식** | `0 17 * * 5` |

**프롬프트 전문:**
```
이번 주 고객 문의 트렌드, 에스컬레이션 현황, 주요 이슈를 요약해줘
```

**Cowork /schedule 설정:**
```
/schedule create \
  --name "주간 CS 요약" \
  --skill moai-support:escalation-manager \
  --cron "0 17 * * 5" \
  --prompt "이번 주 고객 문의 트렌드, 에스컬레이션 현황, 주요 이슈를 요약해줘"
```

**활용 팁:**
- 카테고리별 문의량 추이 (배송/환불/기술/일반)
- 미해결 에스컬레이션 건 목록 자동 포함
- CSAT 점수 주간 추이 시각화
- 반복 문의 패턴 → FAQ 업데이트 제안 자동 생성

---

## 전체 템플릿 요약

| 이름 | 대상 스킬 | 빈도 | Cron |
|------|---------|------|------|
| 매일 아침 브리핑 | `moai-business:daily-briefing` | 평일 매일 8:30 | `30 8 * * 1-5` |
| 주간 마케팅 리포트 | `moai-marketing:performance-report` | 매주 월 9:00 | `0 9 * * 1` |
| 월간 세무 체크 | `moai-finance:tax-helper` | 매월 20일 10:00 | `0 10 20 * *` |
| 분기 사업 리뷰 | `moai-business:strategy-planner` | 분기말 금요일 9:00 | `0 9 28-31 3,6,9,12 5` |
| 주간 CS 요약 | `moai-support:escalation-manager` | 매주 금 17:00 | `0 17 * * 5` |

---

## Cowork /schedule 공통 옵션

```
/schedule create --name <이름> --skill <스킬> --cron <표현식> --prompt <프롬프트>
/schedule list               # 등록된 스케줄 목록
/schedule pause <이름>       # 일시 정지
/schedule resume <이름>      # 재개
/schedule delete <이름>      # 삭제
/schedule run <이름>         # 즉시 실행 (테스트)
```
