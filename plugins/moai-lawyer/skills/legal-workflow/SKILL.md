---
name: legal-workflow
description: |
  한국 법령·계약·규제·특허에 걸친 복합 요청에서 문서와 적용 시점을 확인하고 moai-lawyer의 legal-* 스킬로 연결합니다. 법령·판례 인용은 현재 연결된 법률 자료 도구로 확인합니다.
version: "1.0.1"
---

# 법무 조사 작업 경로

1. 질문의 대상 문서, 당사자 역할, 사업 분야, 관할과 사실 발생 시점을 확인한다. 필수 입력이 없으면 현재 런타임의 질문 채널로 묻고, 질문할 수 없는 하위 실행에서는 누락 자료를 blocker로 반환한다.
2. 계약서는 `legal-contract-review`, NDA는 `legal-nda-triage`, 규제 점검은 `legal-compliance-check`, 법적 위험은 `legal-legal-risk`, 법령·판례는 `legal-law-research`, 특허·상표는 해당 `legal-ip-search-report`·`legal-patent-*` 스킬을 따른다. 식약처·등기 업무는 해당 전담 스킬을 따른다.
3. 법령과 판례를 기억만으로 인용하지 않는다. 현재 연결에서 `korean-law` 도구를 확인하고, 법령 인용은 `legal_analysis(mode=verify_citations)`, 판례는 별도로 `legal_analysis(mode=cite_check)`를 사용한다. 과거 행위의 적용 법령은 `legal_analysis(mode=applicable_law)`로 확인한다. 도구가 없거나 실패하면 접근 가능한 공식 법령·판례 원문과 과거 법령 본문·부칙을 웹으로 대조한다. 웹 대조 기록에는 공식 URL, 확인일, 법령 시행일 또는 판례 선고일, 해당 조문·판시 원문, 과거 법령과 부칙의 적용 판단을 남긴다. 어느 경로로도 확인하지 못한 인용은 사실로 제시하지 않고 검증 공백을 적는다.
4. 각 결론은 확인한 원문, 그 원문에 대한 해석, 미확인 추정을 구분한다. 민감한 계약 내용과 인증 정보는 필요한 범위만 다루고 키를 파일에 기록하지 않는다.
5. 산출물에 `법률 자문이 아닌 참고 자료`임을 밝히고, 구속력 있는 결정은 변호사와 상담하도록 안내한다. 제출 전 `legal-evidence-audit` 기준으로 인용 기록과 위험 등급을 대조한다. 같은 주체의 자기 검수는 독립 감사라고 부르지 않는다.

Claude의 `legal-researcher` 에이전트와 목적이 겹친다. ChatGPT 플러그인에서는 이 스킬이 발견 가능한 진입점이다.
