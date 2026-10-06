"""측정 결과와 전수 계획을 시안 검토 보고서로 묶는다."""
from pathlib import Path
import json

O = Path(__file__).resolve().parent
R = O.parents[1]
D = R / 'www/design-system/eink-proposal'
summary = json.loads((O / 'summary.json').read_text())
v = json.loads((O / 'verification.json').read_text())
baseline = json.loads((O / 'baseline.json').read_text())

report = f'''# MoAI-Cowork 문서·인포그래픽 개편 시안 보고서

2026-10-06 · 시안 검토 단계

## Claim · 완료한 범위

**본문 요약 카드 이미지를 계속 늘리는 방식을 중단하고, HTML 본문과 관계·과정 도식을 구분하는 전수 계획을 만들었다.** 무채색 e-ink 디자인은 독립 시안으로 제작했으며, 전체 사이트 적용은 사용자 선택 후 진행한다.

| 조사 대상 | 이 작업에서 확인한 범위 |
|---|---:|
| 문서 본문 | {summary['pages_read']}개 — 현재 문서 122개, 출시 기록 49개 |
| 인포그래픽 자산 | {summary['asset_files']}개 — SVG 172개, PNG 17개 |
| 새 SVG의 개념 수 | 86개 — 각 개념의 PC·모바일 버전 |
| 기존 Mermaid 코드 | 27개 — 출시 기록에 있는 도식 |
| 새 시안 | 2가지 스타일 × 홈·수업·도식·구성 요소 4화면 |
| 시안 도식 | Mermaid 원본 5개, 수치 차트 1개 |

### 전수 개선 계획

| 대상 | 재표현 제안 | 이유 |
|---|---|---|
| 72개 개념 / SVG 144개 | HTML 본문·표·목록으로 통합 | 정의·항목 비교·상태·예제 텍스트를 복사·검색·수정할 수 있게 한다. 이미 있는 본문과 중복되면 그림을 제거한다. |
| 9개 개념 / SVG 18개 | Mermaid 도식으로 교체 | 질문과 보류, 지침 생성, 반복, 접근 범위, 인계, 작업 분리, 문제 진단, 인증 범위, 연결 방식을 관계·분기로 나타낸다. |
| 5개 개념 / SVG 10개 | 수치 차트 + HTML 원자료 표 | 네 칸 설명은 본문으로 옮기고, 분모가 다른 완료율 비교만 차트로 남긴다. |
| 현재 사용하는 PNG 4개 | 관계·과정 도식으로 다시 제작 | 프로젝트와 폴더, 개념의 관계, 첫 업무의 검토·수정, 전문가 업무의 분기·합류를 간결하게 그린다. |
| 현재 참조하지 않는 PNG 13개 | 보관·재사용 보류 | 현재 본문에서 참조하지 않는 사실을 확인했다. 전역 삭제는 하지 않는다. |
| 기존 Mermaid 27개 | 구조·당시 내용 유지, 표시 스타일 통일 | 출시 기록의 의미를 보존하고 공통 무채색 테마와 한글 글꼴 기준을 적용한다. |

이 분류는 읽기 방식에 대한 **설계 제안**이다. 렌더링 결함으로 단정한 목록이 아니다. 개념별 이유와 사용 페이지는 [전수 목록]({O / 'inventory.md'}), 모든 페이지의 계획·본문 해시는 [171개 페이지 계획]({O / 'page-plan.json'})에 있다.

새 SVG 172개 모두에 요청받은 불필요한 머리말·푸터가 들어 있음을 문자열 검사로 확인했다. SVG의 연결선·화살표 마커도 검사했다. 단순 카드 네 개를 배치한 그림은 제목에 순서를 적어도 담당자별 의존 관계나 분기·합류를 충분히 드러내지 못한다. 이번 시안에서는 해당 머리말·푸터를 넣지 않았다.

### 두 디자인 시안

| 항목 | A · 종이책 | B · 전자책 |
|---|---|---|
| 열기 | [A 시안](http://127.0.0.1:1314/?style=paper#home) | [B 시안](http://127.0.0.1:1314/?style=reader#home) |
| 바탕 | 연회색 | 흰색 |
| 제목 | 시스템 명조 | 시스템 고딕 |
| 본문 최대 폭 | 740px | 800px |
| 절 사이 간격 | 64px | 48px |
| 느낌 | 책을 펼쳐 읽는 구성 | 화면에서 찾아 읽는 구성 |

공통으로 본문 18px, 가는 선, 반경 3px, 그림자·그라디언트·애니메이션 없는 형태를 사용한다. 상태에는 항상 이름을 쓰고 면·파선·점선으로 구분한다. 제목과 본문을 장식 카드에 가두지 않고, 본문의 읽는 흐름에 맞춰 표·요청·문제·도식을 배치한다.

색·글꼴·간격 토큰과 버튼, 상태, 표, 탭, 접기, 질문 입력, 요청 복사, 안내, 확인 문제, 도식, 차트, 탐색 컴포넌트는 [디자인 시스템]({D / 'README.md'})에 정리했다. 코드의 기준은 `tokens.json`, `mermaid.config.json`, `prototype.css`, `prototype.js`이며 완성 시안은 `index.html`이다.

### 한글 잘림 수정

처음 렌더링한 화면에서 한글 라벨의 실제 표시 폭과 `foreignObject` 폭이 달랐다. 예를 들어 ‘기준 · 지침 보완’의 글자는 약 137px, 표시 영역은 약 113px로 측정했다. 렌더링과 표시 단계의 글꼴을 일치시키고 전역 `htmlLabels: false`를 적용해 SVG 텍스트로 다시 렌더링했다. 노드 안쪽 여백은 16px이며 도식의 원래 크기를 유지한다.

현재 시안은 한글 라벨이 노드와 SVG 경계 밖으로 잘리지 않는다. 작은 화면에서는 페이지 전체 대신 도식·표 영역 안에서만 가로로 이동한다. 모바일의 주요 도식 영역에서 키보드 오른쪽 화살표로 이동했을 때 `scrollLeft`가 0에서 40으로 바뀐 것도 확인했다. 글꼴·크기·원본을 변경하면 재렌더링하도록 원본 해시 검사도 추가했다.

Mermaid의 `base` 테마와 색·글꼴 설정은 [공식 테마 문서](https://mermaid.js.org/config/theming.html), 전역 `fontFamily`·`htmlLabels`는 [공식 설정 문서](https://mermaid.js.org/config/schema-docs/config.html)를 참고했다. 모든 도식 원본에 `accTitle`·`accDescr`을 넣었으며 해당 기능은 [공식 접근성 문서](https://mermaid.js.org/config/accessibility.html)에 설명돼 있다. 공식 문서를 읽는 것과 실제 저장소 번들의 실행은 분리하여 확인했다.

### 실제 촬영한 시안

A · 종이책 홈

![종이책 스타일의 실제 로컬 홈 화면]({O / 'screenshots/a-home-desktop.png'})

B · 전자책 홈

![전자책 스타일의 실제 로컬 홈 화면]({O / 'screenshots/b-home-desktop.png'})

한글 폭과 분기·합류를 수정한 도식

![분석 후 FAQ와 안내문이 나뉘고 검토 전에 합쳐지는 실제 화면]({O / 'screenshots/a-parallel-desktop.png'})

[도식 전체 화면]({O / 'screenshots/a-diagrams-full.png'}) · [구성 요소 전체 화면]({O / 'screenshots/a-components-full.png'}) · [모바일 홈]({O / 'screenshots/a-home-mobile.png'}) · [모바일 수업]({O / 'screenshots/a-lesson-mobile.png'})

## Evidence · 실행과 관측

전수 조사:

```text
python3 reports/20261006-eink-design/audit.py
{(O / 'audit.stdout').read_text().strip()}
```

시안 생성:

```text
python3 www/design-system/eink-proposal/build.py
{(O / 'build.stdout').read_text().strip()}
```

실제 DOM 검증 결과 계산:

```text
python3 reports/20261006-eink-design/verify.py
{(O / 'verify.stdout').read_text().strip()}
```

| 실제 브라우저 검사 | 관측 결과 |
|---|---:|
| 화면 조합 | {v['layouts']}개 — 두 스타일, 네 화면, 390·768·1280px |
| 검사한 문자 기록 | {v['measured_texts']}개 |
| 검사한 문자 최소 크기 | {v['minimum_font_px']}px |
| SVG 문자 최소 표시 크기 | {v['minimum_svg_font_px']}px |
| 검사한 문자 최소 대비 | {v['minimum_contrast']}:1 |
| 노드·SVG 경계의 글자 잘림 | 0 |
| 페이지 전체 가로 넘침 | 0 |
| 중복 ID / 끊어진 ARIA 연결 | 0 / 0 |
| 최종 화면 검사 중 콘솔 오류 | 0 |
| 요청 복사 | 원문과 일치, 기존 클립보드 복원 |
| 키보드 탭 / 입력 확인 / 해설 접기 | 실제 동작 확인 |
| 바뀐 Mermaid 원본·설정의 오래된 SVG 빌드 | 두 경우 모두 거부 |
| 기존 문서 본문 해시 변화 | 0 |

24개 화면은 CUA로 실제 브라우저의 화면과 스타일을 전환하면서 검사했다. [좌표·색·글꼴 원자료]({O / 'browser-layouts.json'}), [측정 함수]({O / 'measure-layout.js'}), [검증 결과]({O / 'verification.json'}), [상호작용]({O / 'interactions.json'}), [오래된 렌더링 거부 확인]({O / 'stale-render-check.json'})을 저장했다.

초기 렌더 준비 과정에서는 Mermaid 청크 경로가 없어 오류가 발생했다. 저장소의 청크 경로를 연결한 뒤 5개 도식을 렌더링했고, 완성 시안은 SVG를 내장하므로 렌더용 스크립트를 불러오지 않는다. 초기 오류와 최종 화면 검사 중 오류를 구분해 기록했다. 측정 중에는 부모 SVG 텍스트의 색과 실제 글자를 그리는 `tspan` 색을 구분해 대비를 계산했다.

로컬 A·B 주소는 HTTP 200이며, 응답 바이트가 완성 HTML 파일과 일치한다. 기존 문서 서버 1313도 HTTP 200이다. [HTTP 결과]({O / 'http.json'})에 저장했다.

## Baseline-attribution · 측정 대상

- 작업 폴더: `{baseline['root']}`
- HEAD: `{baseline['head']}` — {baseline['branch']}
- 세션: `{baseline['source_session_id']}`
- 시안 서버: `127.0.0.1:1314`, PID 86652, 도구 세션 99073
- 기존 문서 서버: `127.0.0.1:1313`
- 완성 HTML: {baseline['prototype_bytes']:,}바이트, SHA-256 `{baseline['prototype_sha256']}`
- Mermaid SVG는 실제 브라우저에서 렌더링한 DOM을 저장했다. 원본·설정·번들 해시는 [렌더링 기록]({D / 'render-provenance.json'})에 있다.

기존 문서 171개의 SHA-256을 조사 시점과 검증 시점에 비교했다. 이번 시안 작업으로 본문을 일괄 교체하지 않았다. 이 보고서는 이 작업 폴더와 로컬 시안에서 측정한 결과이며, 공개 사이트의 새 디자인 배포를 의미하지 않는다.

## Gaps · 아직 실행하지 않은 범위

- A·B 선택과 전체 사이트 적용은 남아 있다. 전수 계획의 86개 개념을 모두 다시 제작한 상태는 아니다.
- 기존 사이트의 DS v2, 본문 인포그래픽, 출시 기록 Mermaid는 아직 새 디자인으로 일괄 교체하지 않았다.
- 공개 사이트 배포는 수행하지 않았다.
- 실제 e-ink 기기, Safari·다른 운영체제, 인쇄, 스크린 리더의 전체 사용 흐름은 검증하지 않았다.
- ChatGPT Work·Claude Cowork의 설치·인증·외부 업무 실행을 새 시안의 화면 검사로 검증했다고 주장하지 않는다.

## Residual-risk · 선택 후 확인할 것

**권장 방향은 B의 고딕 제목·넓은 본문을 강의 기본 화면으로 쓰는 것이다.** A의 여백과 명조 제목은 책처럼 읽는 경험을 원하는 경우 선택할 수 있다. 이는 시안의 스타일에 대한 제안이며 학습 효과를 측정한 결론은 아니다.

시스템 글꼴은 운영체제마다 폭이 달라질 수 있다. 최종 글꼴을 정하면 Mermaid를 그 글꼴로 다시 렌더링하고, 노드 경계를 재검사해야 한다. 작은 화면의 가로 이동도 도식별로 사용성을 확인한다. 실제 앱 캡처는 원본을 보존하며, 무채색으로 맞추려고 앱 UI를 임의로 다시 칠하지 않는다.

전체 적용은 다음 순서로 진행한다.

1. 선택된 토큰·글꼴을 정식 디자인 기준에 반영한다.
2. 사이트 셸·공통 구성 요소·Mermaid 설정을 반영한다. 렌더링 뒤 색을 바꾸는 기존 경로를 교체한다.
3. 72개 HTML 대상의 중복 그림을 본문과 통합하고 9개 도식·5개 차트를 제작한다.
4. 현재 사용하는 PNG 4개를 교체하고, 미참조 PNG 13개는 보관한다.
5. 출시 기록의 도식 27개는 의미를 유지하며 스타일을 통일한다.
6. 전체 문서의 링크·자료·모바일 폭·한글 노드·복사·탐색을 다시 검사하고 적용 결과를 보고한다.
'''
(O / 'report.md').write_text(report)
print('report.md written: audit, proposal, evidence, baseline, gaps, rollout plan')
