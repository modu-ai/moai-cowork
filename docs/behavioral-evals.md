# 실제 업무 평가

정적 계약 검사와 모델·호스트의 업무 평가는 따로 기록한다. 생성된 eval 파일이 있다는 사실은 평가 통과가 아니다.

## 기존 사례 연결

`scripts/sync-skill-evals.py`가 각 스킬의 `tests/test-cases.yaml`을 Claude Code의 공식 `evals/generated/<사례>/case.yaml`로 변환한다. 원본 사례와 별도 rubric·반례를 유지하며 `scripts/skill-evals-index.json`에 출처와 미실행 상태를 기록한다. 이 인덱스는 실행 결과를 덮어쓰는 저장소가 아니다.

```bash
uv run --no-project --with pyyaml==6.0.3 python scripts/sync-skill-evals.py --check
claude plugin eval ./plugins/moai-pm --case missing-context --runs 1 --concurrency 1 --no-publish --mocks record
```

Claude Code 2.1.269 이상과 정상 인증이 필요하다. 첫 명령은 파일 정합성만 검사한다. 두 번째는 실제 계정으로 모델을 실행한다. 기본 비교군과 judge도 사용량이 있으므로 먼저 한 사례를 확인한다. 보고서는 로컬에 보존하며 게시하지 않는다. 실행 출력과 aggregate 결과의 도구 trace·산출물을 확인한다. 모델 판정만으로 실제 계정 변경이나 독립 검수를 확인하지 않는다.

기본 사례에는 읽기 도구만 허용한다. 파일 생성·스크립트·fixture가 필요한 사례는 그 경로와 도구를 먼저 검토한 후 정확한 `--allow-tools` 범위와 `--scaffold`를 지정한다. 실제 MCP 서버는 기본값으로 시작하지 않는다. 판매 자료·법무·재무의 실제 데이터가 필요한 사례는 입력을 별도로 준비하고 미준비 상태를 실패 또는 미실행으로 기록한다.

`commerce-detail-page-image--all_sections`의 scaffold는 13장의 단색 PNG를 빈 작업 폴더 안에 만든다. 합성 치수·순서용 fixture이며 상품 품질이나 광고 근거를 평가하지 않는다. 사용 시 Python·Pillow 실행 환경과 해당 합성 동작의 쓰기 범위를 확인한다.

## 호스트별 확인

ChatGPT Work, 로컬/Synced Work, Claude Cowork의 지원 프로젝트 유형별로 PM 네 회귀 사례를 같은 입력으로 실행한다. Project 적용 전후·새 작업 읽기·실제 스킬 노출·전문가 호출·대기 질문 복원·산출물 증거를 함께 보존한다. Cloud와 로컬 파일의 접근 차이를 기록한다. Claude CLI 평가 결과를 다른 앱의 설치 성공으로 확대하지 않는다.

품질 평가는 분야별로 추가한다: 법무의 관할·기준일·원출처, 재무의 산술 재계산, 커머스의 실제 계정·행위·중복 실행, 한국어 윤문의 원문 의미·수치·인용 보존. 문자열 검사와 LLM judge는 보조 수단이다.

실행 기록은 baseline(tree·HEAD·변경 digest), 입력 출처, 실행 명령·호스트 버전, 실제 출력·trace·산출물, PASS/FAIL/NOT-RUN, 미확인 범위로 남긴다. 독립 검수 기능이 없으면 동일 실행의 재검토로 명시한다.

근거: [Claude 플러그인 eval 공식 문서](https://code.claude.com/docs/en/plugin-evals), [OpenAI 스킬 테스트 안내](https://developers.openai.com/plugins/build/skills).
