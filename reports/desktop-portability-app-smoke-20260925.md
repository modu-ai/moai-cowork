# 데스크톱 앱 현장 확인표

기준 브랜치: `WT-cowork-desktop-portability`. 정적 조사와 OS별 MCP 자동 테스트는 `reports/desktop-portability-audit-20260924.md`에 있다. 아래 항목은 **실제 앱에서 아직 실행하지 않았다**. 결과를 적을 때 앱 버전·운영체제·플러그인 버전·화면에 보인 도구 이름과 실행 시각을 함께 남긴다.

[현재 코드 SHA `8bb6f998`의 MCP 교차 플랫폼 CI](https://github.com/modu-ai/moai-cowork/actions/runs/36080731545)는 macOS·Windows·Ubuntu 작업 27개가 성공했다. 이 결과는 아래 앱 현장 확인을 대체하지 않는다.

| 호스트 | macOS | Windows | Linux |
|---|---|---|---|
| Claude Cowork | 미실행 — UI 도구에서 창 확인 불가 | 미실행 — 기기 없음 | 미실행 — 기기 없음, 베타 |
| ChatGPT Work | 미실행 — UI 도구 접근 제한 | 미실행 — 기기 없음 | 미실행 — 기기 없음, 공개 미리보기 |

Linux 지원 배포판과 기능 제한은 [Claude Desktop 설치 안내](https://support.claude.com/en/articles/10065433-install-claude-desktop) 및 [ChatGPT 릴리스 노트](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)의 현재 내용을 확인한다. 앱 지원은 이 저장소 플러그인의 설치·도구 호출 성공을 보장하지 않는다.

## 각 앱·OS에서 기록할 항목

1. 앱 UI에서 `moai-story`와 `moai-seller`를 설치한다. 플러그인 카드에 표시된 버전과 스킬·MCP 또는 연결 앱 목록을 기록한다. Claude와 ChatGPT의 설치 절차는 [설치와 관리](../www/content/plugins/install.md)에 있다.
2. 새 대화에서 `story-webtoon-art`에 **가상 캐릭터의 단일 컷 프롬프트**를 요청한다. 이미지 도구를 사용했다면 실제 파일·도구 이름·화면에 표시된 모델을 기록한다. 모델이 숨겨져 있으면 “이미지 생성 확인, Images 2.5 정확한 모델 미확인”으로 기록한다. 이미지 도구가 없으면 프롬프트만 나왔는지 확인한다.
3. 같은 대화에서 `commerce-product-image-pipeline`에 **가상 무지 제품 상자 한 장**을 요청한다. `moai-media`를 추가 설치하지 않은 상태에서 현재 앱의 기본 이미지 도구로 진행하는지, 실제 파일이 생성됐는지 기록한다. 실물 상품·후기·인증 표시를 테스트 자료로 사용하지 않는다.
4. Higgsfield를 쓰는 검사는 계정·크레딧 잔액과 비용을 확인하고 사용자가 해당 유료 호출을 승인한 뒤에만 진행한다. Claude는 공식 MCP, ChatGPT는 Higgsfield 공식 플러그인을 각각 설치·인증한다. 비용 조회와 이미지 도구가 실제 노출되는지 기록한다. 참조 이미지 검사는 공식 업로드 창에서 **업로드 완료된** 가상 자산만 사용하고, 채팅 첨부만으로 전달됐다고 간주하지 않는다. 생성 ID·결과 파일·실제 차감 크레딧을 기록한다.
5. `moai-seller`의 `commerce-detail-page-image`에서 합성 실행 환경을 확인한다. Python·Pillow가 없으면 섹션 파일과 합성 명세를 받되 단일 PNG는 미완료로 표시하는지 확인한다. 도구가 있으면 더미 섹션 13장의 합성 파일을 다시 열어 1080×12720과 누락 섹션 0개를 확인한다.

각 단계의 상태는 `PASS`·`FAIL`·`NOT-RUN`·`BLOCKED` 중 하나로 기록한다. 설치 화면만 봤거나 CI만 통과한 경우에는 앱 이미지 생성 `PASS`를 주지 않는다. 로그인·권한·유료 생성으로 중단되면 어느 단계에서 무엇이 표시됐는지 남긴다.
