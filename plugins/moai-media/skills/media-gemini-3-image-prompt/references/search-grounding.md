# Gemini 3 Pro Image — Search Grounding (Google Search 연동)

Gemini 3 Pro Image의 차별 기능 중 하나. 이미지 생성 도중 Google Search를 호출해 실시간 사실 데이터를 가져와 인포그래픽·지도·통계 그래프 같은 데이터 기반 이미지의 정확도를 끌어올립니다.

## 언제 사용하나

| 사용 케이스 | Search Grounding 효과 |
|---|---|
| 통계 인포그래픽 | 최신 자료를 검색할 수 있으나 수치와 기준 시점은 별도 대조 |
| 지도·지리 다이어그램 | 노선·역 순서를 공식 자료와 별도 대조 |
| 시사 일러스트 | 기준 날짜와 출처를 확인한 뒤 시각화 |
| 차트·그래프 | 검색 결과의 원자료와 그림 속 수치를 별도 대조 |
| 다이어그램 (역사·과학) | 공식·학술 자료와 개념을 별도 대조 |

## 언제 사용하지 않나

| 케이스 | 이유 |
|---|---|
| 일반 제품샷·인물·풍경 | 사실 데이터 불필요, latency만 증가 |
| 일러스트·아트 | 창의성을 제약 |
| 텍스트 없는 이미지 | grounding이 영향 없음 |
| 가상 시나리오 | "2030년 화성 정착지" 같은 미래 가상 case는 grounding이 부적합 |

## 활성화 방법

### Google AI Studio (UI)
- 현재 계정의 이미지 생성 화면에 Google Search 도구가 제공되는지 확인하고, 제공될 때만 켭니다. 고정된 체크박스 이름이나 추론 모드를 필수 단계로 가정하지 않습니다.

### API

[Google의 현재 이미지 생성 가이드](https://ai.google.dev/gemini-api/docs/image-generation#grounding-with-google-search)는 이미지 요청에 `google_search` 도구를 따로 지정합니다. 이 프롬프트 전용 스킬은 API 호출을 실행하지 않으며, 검색 사용 여부만 제안합니다.

### Gemini App (consumer)
- 현재 앱의 검색 연결 제공 여부를 확인합니다. 프롬프트에 검색을 지시한 것만으로 도구가 켜졌다고 보고하지 않습니다.

## 프롬프트 작성 팁

### 시간 명시
Search가 최신 자료를 가져올 수 있도록:

- 기준 날짜와 자료명을 구체적으로 적습니다. 예: "2026년 9월 25일 기준으로 확인한 공식 자료".
- 실제로 확인하지 않은 기관·통계 연도나 수치는 프롬프트에 넣지 않습니다.

### 출처 우선순위 제시
Gemini가 신뢰할 출처를 명시적으로 지시:

```
A donut chart showing <verified subject and figures>.
Use the official source supplied for this request, dated <date>.
<composition>. <lighting>. <style>. Display the verified
percentages and labels verbatim from that source.
```

### 데이터 검증 요청
Gemini가 자신의 출력을 검증하도록 자기-참조 권유:

```
Cross-reference the percentages with at least two sources before
finalizing the visualization.
```

## 한계와 주의

- Search 결과는 **항상 별도 검증** 필요. 모델이 wiki·블로그 등 신뢰도 낮은 출처를 가져올 수 있음.
- 한국어 검색 결과는 영어보다 품질 편차 큼. 중요 데이터는 영어 키워드로 추가 검증.
- 검색 사용은 응답 시간과 비용에 영향을 줄 수 있으므로 현재 서비스의 가격·사용량을 확인합니다.

## 완성 프롬프트 예

### 예 1 — 인포그래픽

```
A horizontal infographic showing <verified SNS platform data>
in South Korea for <source period>.
Wide composition with clean white background, captured in
flat editorial design style. Soft consistent lighting.
Modern infographic design, sans-serif typography. Each
platform displays its name in Korean and the supplied percentage
verbatim. Verify each figure and its denominator against the
cited source before publishing.
```

### 예 2 — 지도

```
A minimalist map of the Seoul Subway Line 2 (Loop Line). Top-
down view, simplified vector style. Soft pastel palette. Modern
transit map aesthetic. Each station name displayed in Korean
verbatim from the current official Seoul Metro source supplied for this request.
Maintain the correct loop sequence and the inner-outer track
distinction.
```

## 출처

- [Google AI for Developers — Gemini image generation](https://ai.google.dev/gemini-api/docs/image-generation)
- [Vertex AI — Grounding with Google Search](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/3-pro-image)
- [Google Cloud Blog — Nano Banana prompting guide](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-nano-banana)
