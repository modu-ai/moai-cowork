# moai-legal 커넥터 가이드

## korean-law (국가법령정보센터 MCP)

법제처 법령 원문, 판례, 행정규칙을 실시간 검색합니다.

### API 키 발급

1. [법제처 Open API](https://open.law.go.kr) 접속
2. 회원가입 후 로그인
3. 마이페이지 > API 인증키 신청
4. 발급된 OC(인증코드) 복사

### 환경변수 설정

```
KOREAN_LAW_OC=발급받은_인증코드
```

### 제공 도구 (14개)

| 도구 | 용도 |
|------|------|
| 법령 검색 | 법령명/키워드로 법률 검색 |
| 법령 조문 | 특정 법률의 조항 전문 조회 |
| 판례 검색 | 대법원/헌법재판소 판례 검색 |
| 행정규칙 | 고시, 훈령, 예규 검색 |
| 법령 연혁 | 법률 개정 이력 추적 |

### 요율 제한

- 일 1,000건 (무료)
- 초과 시 별도 신청 필요

### MCP 서버

korean-law-mcp는 [korean-law-mcp.fly.dev](https://korean-law-mcp.fly.dev)에서 호스팅되는 HTTP MCP 서버입니다. URL 파라미터에 OC를 포함하여 인증합니다.

### 활용 스킬

- `contract-review`: 계약 조항의 법적 근거 확인
- `compliance-check`: 규제 준수 여부의 법령 기반 검증
- `legal-risk`: 관련 판례 조회로 리스크 평가
- `nda-triage`: 영업비밀보호법 관련 조항 확인
