# moai-support 커넥터 가이드

## Slack

고객 지원 채널의 메시지를 조회하고, 에스컬레이션 알림을 전송합니다.

### 설정 방법

1. [Slack API](https://api.slack.com/apps) 에서 새 앱 생성
2. OAuth & Permissions > Bot Token Scopes 추가:
   - `channels:read`, `channels:history` (채널 읽기)
   - `chat:write` (메시지 전송)
   - `users:read` (사용자 정보)
3. 워크스페이스에 앱 설치
4. Bot User OAuth Token 복사
5. 워크스페이스 설정 > Team ID 확인

### 환경변수 설정

```
SLACK_BOT_TOKEN=xoxb-로_시작하는_토큰
SLACK_TEAM_ID=T로_시작하는_팀_ID
```

### 활용 스킬

- `ticket-triage`: Slack 채널에서 CS 문의 자동 수집 및 분류
- `escalation-manager`: 에스컬레이션 시 담당자에게 Slack DM 알림
- `draft-response`: Slack 스레드에 응답 초안 작성

---

## Notion

KB(Knowledge Base) 문서를 Notion 데이터베이스로 관리합니다.

### 설정 방법

1. [Notion Integrations](https://www.notion.so/my-integrations) 에서 새 통합 생성
2. 기능 선택: Read content, Update content, Insert content
3. Internal Integration Secret 복사
4. Notion에서 연동할 페이지/데이터베이스를 열고 **연결 추가** > 생성한 통합 선택

### 환경변수 설정

```
NOTION_API_KEY=ntn_로_시작하는_시크릿
```

### 활용 스킬

- `kb-article`: Notion 데이터베이스에 KB 문서 생성/업데이트
- `escalation-manager`: Notion에 에스컬레이션 로그 기록
