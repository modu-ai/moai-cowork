# localization-protocol.md — 로케일 현지화 프로토콜

## 개요
MoAI가 사용자의 로케일(언어, 국가, 시간대, 통화)을 자동 감지하고 
현지 규제, 문화, 비즈니스 관행을 반영하여 산출물을 생성하는 프로토콜입니다.

---

## 1. 로케일 자동감지

### 1-1. 감지 순서

```
Priority 1: 글로벌 프로필
  → /mnt/.auto-memory/moai-profile.md
  ├─ user_profile.country (개인 국가)
  └─ company_profile.company_country (회사 국가)

Priority 2: 시스템 환경
  → OS 시스템 로케일
  → 브라우저 언어 설정
  
Priority 3: /moai init 과정
  → Phase 1-A Q2 (국가 선택)
  
Priority 4: 웹 요청 헤더
  → Accept-Language 헤더
  → Cloudflare 지역 정보
```

### 1-2. 로케일 구성

```yaml
locale_config:
  country: "KR"              # ISO 3166-1 alpha-2
  language: "ko"             # ISO 639-1
  script: "Hang"             # ISO 15924 (선택)
  locale_string: "ko_KR"     # BCP 47 형식
  timezone: "Asia/Seoul"     # IANA 타임존
  currency: "KRW"            # ISO 4217
  week_start: "monday"       # [sunday, monday, saturday]
  number_format: "1,000.00"  # [1,000.00, 1.000,00, 1 000,00]
  date_format: "YYYY-MM-DD"  # [YYYY-MM-DD, DD/MM/YYYY, MM/DD/YYYY]
  time_format: "24h"         # [12h, 24h]
```

### 1-3. 저장 위치

```
.moai/locale-context.md

내용:
country: KR
language: korean
timezone: Asia/Seoul
currency: KRW
business_hours: 09:00-18:00
holidays: [설, 추석, ...] # 정부 공휴일 + 기업별
web_search_locale: ko.search.naver.com (또는 google.co.kr)
laws: [개인정보보호법, 전자상거래법, ...]
```

---

## 2. 비-카테고리10 하네스의 로케일 참조

모든 하네스가 로케일을 고려합니다:

### 2-1. 화폐 표기

**content_generator**
```
현금흐름 언급 시:
한국: "연 10억 원 규모의 투자"
미국: "Investment of $10 million annually"
일본: "年10億円規模の投資"

저장: 모든 숫자에 통화 기호 + 국가별 형식
```

### 2-2. 날짜 표기

**email_harness**
```
한국: "2026년 4월 4일" 또는 "2026-04-04"
미국: "April 4, 2026" 또는 "04/04/2026"
일본: "2026年4月4日"
```

### 2-3. 비즈니스 관행

**automation_harness**
```
한국:
- 근무 시간: 09:00 ~ 18:00
- 주말: 토요일, 일요일
- 공휴일: 설(3일), 추석(3일)
- 오토메이션 스케줄: 오전 9시 또는 자정

미국:
- 근무 시간: 08:00 ~ 17:00
- 주말: 토요일, 일요일
- 공휴일: Thanksgiving, Christmas 등
- 오토메이션 스케줄: 자정 또는 새벽
```

---

## 3. 카테고리10 하네스 — 웹검색 현지화

### 3-1. 웹검색 키워드 패턴

**하네스별 맞춤 검색 전략**

**content_generator**
```
주제: "디지털 마케팅 트렌드"
로케일: ko_KR

검색 패턴:
1. 한국 특화 키워드:
   "한국 디지털 마케팅 동향 2026"
   "국내 SNS 마케팅 트렌드"
   "한국 소비자 구매 패턴"

2. 로컬 언론/통계:
   - 조중동 (경제섹션)
   - 매일경제, 한국경제
   - 통계청, 소비자 분석 리포트

3. 로컬 사이트 우선:
   .kr, .co.kr 도메인
   NAVER, Daum 검색 결과

4. 제외 키워드:
   "China", "US market" (맥락 불일치)
```

**marketing_strategist**
```
주제: "B2B SaaS 마케팅 전략"
로케일: ko_KR

검색 패턴:
1. 한국 SaaS 사례:
   "한국 SaaS 기업 성공 사례"
   "국내 B2B 마케팅 벤치마크"
   "한국 B2B 구매 의사결정 프로세스"

2. 로컬 시장 특성:
   "한국 IT 시장 규모"
   "한국 엔터프라이즈 구매 결정 요인"

3. 한국식 비즈니스 문화:
   - 관계 중심 (Relationship-driven)
   - ROI 강조
   - 신뢰도 중시
```

### 3-2. 검색 결과 필터링

```python
def filter_search_results(results, locale):
  filtered = []
  
  FOR result in results:
    # 1. 언어 매칭
    IF result.language != locale.language:
      continue
    
    # 2. 시간 신선도
    IF result.date < now() - 90days:
      continue  # 오래된 정보 제외
    
    # 3. 신뢰도 평가
    IF result.domain NOT IN trusted_sources:
      score -= 20%
    
    # 4. 로컬 특화
    IF result.mentions_local_context:
      score += 30%
    
    # 5. 정부/공식 출처
    IF result.is_official_source:
      score += 50%
    
    filtered.append((score, result))
  
  RETURN sorted(filtered, by=score, descending=True)
```

### 3-3. 결과 저장

```
.moai/locale-context.md에 추가:

web_search_results:
  - query: "한국 디지털 마케팅 동향 2026"
    results:
      - source: "조중동 경제면"
        title: "2026년 한국 마케팅 전망"
        url: https://...
        relevance: 95%
      - source: "매일경제"
        title: "국내 SNS 마케팅 현황"
        ...
```

---

## 4. 규제 및 법률 적용

### 4-1. 로케일별 규제 매핑

**한국 (KR)**
```
적용 법률:
1. 개인정보보호법
   - 수집 목적 명시 필수
   - 3년 보유 제한
   - GDPR 대신 PIPA 준수

2. 전자상거래법
   - 통신판매신고 필수
   - 반품 권리: 7일
   - 환불 기한: 3일

3. 통신판매법
   - 광고 메일: 수신동의 필수
   - "광고" 표시 의무
   - 스팸 금지

4. 개인정보보호지침
   - 개인정보 유출 신고 의무
   - 암호화 권장
```

**미국 (US)**
```
적용 법률:
1. GDPR (EU 거주자)
   - 명시적 동의 필수
   - DPIA 수행

2. CCPA (캘리포니아)
   - 옵트아웃 권리
   - 삭제 권리

3. CAN-SPAM
   - 메일 주제에 "광고" 표시
   - 수신 거부 옵션 제공

4. FTC 규칙
   - 허위 광고 금지
   - 공시 요구사항
```

### 4-2. 규제 강제 적용

```python
def apply_regulations(output, harness, locale):
  
  regulations = load_regulations(locale.country)
  
  FOR regulation in regulations:
    # 1. 규제 검증
    IF regulation.applies_to(harness, output):
      
      # 2. 컴플라이언스 확인
      IF NOT output.complies_with(regulation):
        
        # 3. 자동 수정
        output = apply_fix(output, regulation)
        
        # 4. 경고 기록
        log_warning(f"{regulation.name} 적용됨")
  
  RETURN output
```

---

## 5. 문화 및 비즈니스 관행

### 5-1. 문화 적응

**인사말 및 호칭**
```
한국:
- 존칭 사용 (님, 님께서)
- 나이/서열 존중
- 공식적 어조

미국:
- 캐주얼한 호칭 (First name)
- 평등한 톤
- 친근한 어조

일본:
- 경어 (です体, ます체)
- 높임 표현
- 간접적 표현
```

**이모지 및 특수문자**
```
한국: 
- 이모지 사용 최소화 (공식 문서)
- 전통 기호 존중 (불, 복, 길 등)

미국:
- 이모지 자유로움
- 타이포그래피 활용

일본:
- 전통 기호 (吉, 福)
- 이모지 선별적 사용
```

### 5-2. 비즈니스 관행

**의사결정 프로세스**
```
한국:
- 의사결정 자가 중심적 (결정자 명확)
- 보고 체계 엄격
- 관계 기반 협상

미국:
- 팀 기반 의사결정
- 투명성 중시
- 계약 기반 협상

일본:
- 합의 기반 (Consensus)
- 위계 중시
- 시간 여유 필요
```

---

## 6. 타임존 및 스케줄링

### 6-1. 자동 스케줄 조정

```python
def schedule_automation(task, locale):
  # 근무 시간 기반 스케줄
  business_hours = get_business_hours(locale.country)
  
  # 퍼센타일 기반 최적 시간
  optimal_time = calculate_optimal_time(
    business_hours,
    locale.timezone,
    task.type
  )
  
  # 예: 한국 메일링
  # 근무 시간: 09:00 ~ 18:00
  # 최적 시간: 10:00 (오픈율 최고)
  
  schedule_task(task, optimal_time)
```

### 6-2. 시간대 표시

```
한국 사용자 기준:
- 모든 시간은 Asia/Seoul (UTC+09:00)
- 다른 국가 시간 참조 시 변환:
  "미국 동부 시간 10:00 AM = 한국 시간 밤 11:00 PM"
```

---

## 7. 수치 및 통화 표기

### 7-1. 숫자 형식

```
한국:
  1,000,000 (쉼표)
  소수점: . (마침표)
  예: ₩1,000,000.00

미국:
  1,000,000 (쉼표)
  소수점: . (마침표)
  예: $1,000,000.00

독일:
  1.000.000 (마침표)
  소수점: , (쉼표)
  예: €1.000.000,00
```

### 7-2. 통화 표기

```
자동 변환:
"월 10억 원" (한국) → "$800,000" (미국) → "€750,000" (EU)

환율 출처: 세계은행 또는 OANDA (일일 업데이트)
주의: 환율 변동 안내 필수
```

---

## 8. 성능 및 최적화

### 8-1. 현지화 캐싱

```
로케일 설정 캐시:
- TTL: 30일 (또는 명시적 변경까지)
- 저장: .moai/locale-cache.yaml
- 히트율 목표: > 95%
```

### 8-2. 웹검색 최적화

```
검색 결과 캐싱:
- 쿼리별 캐시 (동일 쿼리 반복 최소화)
- 언어별 분리 캐싱
- 신선도: 30일
- 크기 제한: 100MB
```

---

## 9. 다중 로케일 처리

### 9-1. 다국가 조직

```
회사가 다국가 운영 시:
primary_locale: "ko_KR" (개인 국가)
secondary_locales: ["en_US", "ja_JP"] (회사 국가)

규칙: 개인 선호 우선, 회사 요구시 조정
```

### 9-2. 국제 프로젝트

```
/moai {harness} --locale=en_US
→ 일시적으로 미국 로케일로 작업
→ 프로젝트 종료 후 원래 로케일 복귀
```

---

## 10. 피드백 및 개선

### 10-1. 현지화 피드백

```
평가 후:
"이 콘텐츠가 한국 시장에 적합했나요?"
[1] 매우 적합
[2] 적합
[3] 보통
[4] 부적합
[5] 전혀 부적합

부적합 시 → 규칙 조정
```

### 10-2. 새 로케일 추가

```
/moai locale --add --country=VN --language=vi

단계:
1. 규제 정보 수집
2. 비즈니스 관행 정의
3. 웹검색 소스 매핑
4. 테스트 프로젝트 실행
5. 피드백 기반 조정
```

---

## 11. 감사 및 컴플라이언스

### 11-1. 규제 감사

```
매월 자동 감사:
- 적용 법규 현행 여부 확인
- 규정 변경 모니터링
- 컴플라이언스 체크리스트 업데이트

변경 시 알림:
/moai notifications --type=regulatory
```

### 11-2. 컴플라이언스 로그

```
.moai/compliance-log.md:

2026-04-04 컴플라이언스 체크
├─ 개인정보보호법: ✓ 준수
├─ 전자상거래법: ✓ 준수
└─ 통신판매법: ✓ 준수

위반 이력: 없음
