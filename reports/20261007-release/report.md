# 커밋·배포 전 검증 기록

작성일: 2026-10-07

## Claim

승인된 ChatGPT Work·Claude Cowork 플러그인 개선, 온라인 강의 문서 개편, 킨들 스타일과 macOS 코드 창을 배포 대상으로 준비했다. 이 기록은 배포 전 검증이며 운영 배포 완료를 주장하지 않는다.

## Evidence

- `reports/20261005-work-cowork-update/run_checks.py`의 검사 목록을 그대로 실행하고 출력 위치만 현재 보고서 폴더로 변경했다. 출력: `RESULT 15 checks; 15 passed`. 실제 명령·출력은 `checks.json`과 각 로그에 저장했다.
- `hugo --source www --destination /tmp/moai-release-20261007 --baseURL https://cowork.mo.ai.kr/ --enableGitInfo=false --quiet --minify`: 종료 코드 0, 출력 없음.
- `python3 scripts/check-docs.py /tmp/moai-release-20261007 --report reports/20261007-release/site-check.json`: HTML 290개, 내부 참조 26,792개, 앵커 3,549개, 이미지 419개, 오류 0개.

## Baseline-attribution

작업 사본: `/Users/goos/.codex/worktrees/b0aa/moai-cowork`. 검사 당시 HEAD: `2c3cef1d24e88b3bfe8db61c713ffae317b346d0`와 미커밋 변경. source_session_id: `01a10aae-6716-7681-b5d7-d558155d9f86`.

## Gaps

이 검사에서 실제 계정 인증·앱의 플러그인 설치·업무 수행·모델 행동 평가를 실행하지 않았다. macOS 실행에서 Windows 런처 검사 1개는 제외됐다. 이전 문서·화면 검증의 한계는 각 보고서에 유지했다. 운영 배포와 공개 사이트 검증은 커밋·푸시 이후 수행한다.

## Residual-risk

공급자 메뉴와 구독별 지원 조건은 달라질 수 있다. 공개 사이트 반영 여부는 배포 상태와 실제 페이지의 내용·스타일·이미지를 함께 관찰해야 한다.
