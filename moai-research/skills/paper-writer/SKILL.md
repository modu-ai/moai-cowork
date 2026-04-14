---
name: paper-writer
description: >
  학술 논문을 구조화하여 작성합니다.
  '논문 써줘', '초록 작성', '참고문헌 정리', 'APA 포맷'이라고 요청할 때 사용하세요.
  서론-선행연구-방법론-결과-논의-결론 구조로 논문을 작성하고 APA/KCI/IEEE 참고문헌을 자동 생성합니다.
user-invocable: true
metadata:
  version: "1.1.1"
  category: "domain"
  status: "active"
  updated: "2026-04-10"
  tags: "논문, 작성, 초록, APA, KCI, IEEE, 참고문헌, 학술"
---

# 학술 논문 작성 (Paper Writer)

> MoAI-Cowork v1.0.0 하네스 참고자료

## 역할
학술 논문을 체계적으로 구조화하고 작성하는 전문가. APA, KCI, IEEE 등 주요 인용 포맷을 지원합니다.

## 논문 구조 (표준)

1. 제목 / Title
2. 초록 / Abstract (한국어 + 영어)
3. 키워드 / Keywords (5-7개)
4. 서론 / Introduction
5. 이론적 배경 / Literature Review
6. 연구 방법 / Methodology
7. 결과 / Results
8. 논의 / Discussion
9. 결론 / Conclusion
10. 참고문헌 / References

## 참고문헌 포맷

| 포맷 | 사용처 | 예시 |
|------|--------|------|
| APA 7th | 사회과학, 교육학 | Author, A. A. (Year). Title. *Journal*, *Vol*(Issue), pp. |
| KCI | 한국연구재단 | 저자 (연도). 제목. 학술지명, 권(호), 쪽. |
| IEEE | 공학, IT | [1] A. Author, "Title," *Journal*, vol. X, no. Y, pp. Z, Year. |

## 이 스킬을 사용하지 말아야 할 때
- **논문 검색** → moai-research:paper-search 사용
- **특허 명세서** → moai-research:patent-analyzer 사용
