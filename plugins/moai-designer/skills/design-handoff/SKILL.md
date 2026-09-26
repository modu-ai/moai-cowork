---
name: design-handoff
description: |
  디자인 브리프와 실제 브랜드·화면 자료로 Claude Design 또는 코드 구현에 넘길 핸드오프 문서를 만듭니다.
  "디자인 핸드오프 준비해줘", "Claude Design에 넘길 프롬프트 써줘" 같은 요청에 사용하세요.
  MoAI 프로젝트의 기존 다섯 파일 경로는 해당 파이프라인에서 필요할 때 사용합니다.
user-invocable: false
version: "1.1.3"
---

# 디자인 핸드오프 작성

사용자가 제공한 목표, 대상 사용자, 디자인 시스템, 화면 범위, 실제 참고 자료를 하나의 전달 가능한 지시로 정리한다. `design-brief`와 `design-handoff-reader`의 산출물이 실제로 있다면 읽고 연결한다. 읽지 않은 번들이나 연구 결과를 입력으로 채우지 않는다.

## 작성 절차

1. **자료 확인**: 제공된 브리프·화면·브랜드 보이스·토큰·참고 URL의 출처와 최신성을 확인한다. MoAI 프로젝트에서 `.moai/project/brand/`가 있으면 해당 브랜드 결정을 존중한다. 데스크톱 앱에 폴더가 없으면 사용자 자료를 사용한다.
2. **범위 정리**: 만들 화면·상태·콘텐츠와 제외 범위 중 사용자가 실제로 정한 내용을 기록한다. 빠진 브랜드나 레퍼런스는 미정으로 표시하고 가상의 제품·URL·후기를 넣지 않는다.
3. **붙여넣기 지시**: 외부 디자인 세션용 문구에서 내부 SPEC ID·로컬 경로·에이전트 이름을 제거하고 목적, 대상, 참고 자료, 브랜드 규칙, 결과 형식과 검토 기준을 자연어로 적는다. 파일이 없는 경우에도 채팅에서 바로 사용할 수 있는 본문을 제공한다.
4. **보조 파일**: 사용자가 요청하거나 기존 MoAI Path A 파이프라인이 필요로 하면 `prompt.md`, `context.md`, `references.md`, `acceptance.md`, `checklist.md`로 분리한다. 파일을 만들었다면 실제 경로를 읽어 확인한다. 파일 분할은 Claude Design의 공식 내보내기 형식이라고 주장하지 않는다.
5. **검수**: 브리프의 수치·디자인 값과 핸드오프가 일치하는지 대조한다. 구현 화면이 없는데 WCAG 준수·반응형 동작·디자인 완료를 PASS로 기록하지 않는다.

[Claude Design 공식 안내](https://support.claude.com/en/articles/14604416-get-started-with-claude-design)에 따라 사용자는 Claude 대화, Artifacts 또는 `claude.ai/design`에서 디자인을 시작할 수 있다. ChatGPT Work 사용자에게는 동일한 브리프를 현재 사용할 수 있는 디자인 도구나 코드 작업에 전달할 수 있게 제공한다. 도구 간 자동 동기화나 붙여넣기가 실제로 일어나지 않았다면 완료라고 말하지 않는다.

참고 형식은 `references/prompt-template.md`와 `references/supporting-files.md`에 있다. 결과에는 생성한 문서의 위치, 실제 확인한 근거, 미결정 사항과 다음 작업을 짧게 적는다.
