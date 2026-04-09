# moai-business

비즈니스 전략 플러그인 — 사업계획서, 시장조사, 재무모델, 투자제안서.

창업 초기 린 캔버스부터 Series B IR 자료, TAM/SAM/SOM 시장 분석, 재무 시뮬레이션까지 비즈니스 의사결정 전반을 지원합니다.

## 스킬

| 스킬 | 설명 | 상태 |
|------|------|:----:|
| [strategy-planner](./skills/strategy-planner/) | 비즈니스 전략 기획 — 사업계획서, 린 캔버스, MVP, SWOT, OKR, Blue Ocean 전략 | ✅ 완성 |
| [market-analyst](./skills/market-analyst/) | 시장 분석 — TAM/SAM/SOM, 경쟁사 분석, 고객 세그멘테이션, 가격 전략 | ✅ 완성 |
| [investor-relations](./skills/investor-relations/) | 투자자 관계 관리 — IR 자료, 피칭 덱, 매출 예측, 손익분석, 현금흐름 | ✅ 완성 |
| [daily-briefing](./skills/daily-briefing/) | 일일 비즈니스 브리핑 — 시장 동향, 경쟁사 모니터링, 주요 지표 대시보드 | 📝 초안 |

## 에이전트

| 에이전트 | 모델 | 설명 |
|---------|:----:|------|
| market-researcher | Sonnet | DART/KOSIS/네이버 데이터랩 기반 시장 데이터 자율 수집. moai-product 등에서 공유 호출 가능 |

## MCP 커넥터

| 커넥터 | 설명 |
|--------|------|
| dart | 금융감독원 DART 공시 데이터 API (DART_API_KEY 필요) |

## 사용 예시

```
스타트업 사업계획서 초안 작성해줘. 타깃은 B2B SaaS, 시리즈 A 준비 중이야.
```

```
우리 경쟁사 세 곳 분석해서 포지셔닝 맵 만들어줘
```
