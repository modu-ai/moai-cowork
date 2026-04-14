# CLAUDE.local.md — cowork-plugins 저장소 로컬 지침

이 파일은 이 저장소에서 Claude Code가 작업할 때 반드시 지켜야 할 로컬 규칙입니다.

---

## 1. 버저닝 정책 (HARD)

**단일 진실 원칙**: cowork-plugins 저장소의 모든 버전 표기는 **완전히 동일**해야 합니다.

### 동기화 대상 (총 88개 지점, v1.1.0 기준)

| 범주 | 경로 | 필드 | 개수 |
|---|---|---|---|
| 마켓플레이스 | `.claude-plugin/marketplace.json` | `metadata.version` | 1 |
| 플러그인 매니페스트 | `<plugin>/.claude-plugin/plugin.json` | `version` | 17 |
| 스킬 frontmatter | `<plugin>/skills/<skill>/SKILL.md` | `metadata.version` | 70 |

플러그인 또는 스킬 추가·삭제 시 이 카운트를 함께 갱신하세요.

### [HARD] 버전 변경 절차

릴리스 버전을 올릴 때는 **반드시 아래 4단계를 함께 실행**합니다. 일부만 올리는 것은 금지.

1. **3곳 동시 업데이트** (위 표의 82개 지점 전부)
   ```bash
   NEW="1.0.4"
   # marketplace
   sed -i '' -E 's/"version": *"[0-9]+\.[0-9]+\.[0-9]+"/"version": "'$NEW'"/' .claude-plugin/marketplace.json
   # 모든 plugin.json
   find . -path "*/.claude-plugin/plugin.json" -not -path "*/.git/*" -exec \
     sed -i '' -E 's/"version": *"[0-9]+\.[0-9]+\.[0-9]+"/"version": "'$NEW'"/' {} +
   # 모든 SKILL.md metadata.version
   find . -name "SKILL.md" -not -path "*/.git/*" -exec \
     sed -i '' -E 's/^(  version: *)"[0-9]+\.[0-9]+\.[0-9]+"/\1"'$NEW'"/' {} +
   ```

2. **CHANGELOG.md 항목 추가**: `## [NEW] - YYYY-MM-DD` 섹션, Added/Changed/Fixed/Removed 분류

3. **커밋**: `chore(release): vX.Y.Z — 요약` 형식의 단일 릴리스 커밋

4. **태그 생성·푸시**: `git tag vX.Y.Z && git push origin vX.Y.Z`
   - 태그는 `vX.Y.Z` 형식 (v 접두어 필수)
   - 태그 값과 파일 내 버전은 **반드시 동일**

### [HARD] 금지 사항

- 일부 파일만 버전 올리기 (예: marketplace.json만 bump, SKILL.md 방치)
- 태그 형식 불일치 (예: `v1.1.0` 태그인데 marketplace.json은 `1.0.3`)
- 버전 번호와 무관한 마이너 수정에 버전 bump
- 이미 배포된 태그를 force-push로 덮어쓰기 (사용자 캐시 손상)

### 검증 명령

커밋 전 반드시 실행:
```bash
# 모든 버전이 동일한지 확인 (한 줄만 출력되어야 통과)
{ grep -h '"version"' .claude-plugin/marketplace.json moai-*/.claude-plugin/plugin.json | grep -oE '[0-9]+\.[0-9]+\.[0-9]+'; \
  grep -h "^  version:" moai-*/skills/*/SKILL.md | grep -oE '[0-9]+\.[0-9]+\.[0-9]+'; } \
  | sort -u
```

---

## 2. 플러그인 컴포넌트 규격 (HARD)

### Skill 슬래시 자동완성 노출

`/<skill-name>` Tab 자동완성에 노출하려면 SKILL.md frontmatter에 다음 필드 **필수**:

```yaml
---
name: <skill-name>
description: >
  ...
user-invocable: true        # ← 슬래시 메뉴 노출 스위치
metadata:
  version: "X.Y.Z"
  status: "active" | "stable" | "experimental"
  updated: "YYYY-MM-DD"
  tags: "tag1,tag2,tag3"
---
```

- `user-invocable` 누락 시 → Tab 자동완성 불가, 모델 자동 호출만 가능
- `keywords` 필드는 **비표준**이므로 사용 금지 (`metadata.tags`로 대체)

### Plugin 매니페스트

`<plugin>/.claude-plugin/plugin.json` 필수 필드:
```json
{
  "name": "plugin-name",
  "version": "1.0.3",
  "description": "...",
  "author": { "name": "..." },
  "keywords": ["..."],
  "license": "MIT"
}
```

---

## 3. 릴리스 후 사용자 안내

신버전 배포 후 사용자 측 캐시 갱신 필요:
```
/plugin marketplace update cowork-plugins
```
이후 플러그인 상세 재진입 시 반영됨. README나 릴리스 노트에 해당 안내 포함.

---

## 4. MCP 서버 통합 정책 (HARD)

플러그인이 MCP 서버를 번들하려면 다음 규칙을 따릅니다:

- 플러그인 루트에 **`.mcp.json`** 파일 배치 (예: `moai-media/.mcp.json`)
- 환경변수는 `${VAR_NAME}` 구문으로만 주입 — 절대 하드코딩 금지
- hosted MCP는 `type: "http"` + `url` + `headers`로 등록
- local stdio MCP는 `command` + `args` (권장: `uvx <package>` 형태)
- API 키 등록 절차는 플러그인 루트의 `CONNECTORS.md`에 필수 문서화

현재 MCP 번들 플러그인:
- `moai-media`: `fal-ai` (hosted), `elevenlabs` (local stdio via uvx)

## 5. 외부 API 모델 ID 업데이트 정책

외부 API(Google, OpenAI, Anthropic 등)가 모델 이름·엔드포인트를 변경하면:

1. 영향 스킬 식별 (`grep -r "<old-model-id>" .`)
2. 공식 문서 확인 후 매핑 테이블 업데이트 (예: `generate_image.py` MODEL_MAP)
3. 레거시 별칭은 **최소 1 메이저 버전** 동안 유지 (v1.0.x → v1.1.x는 호환)
4. 응답 스키마가 바뀌면 스크립트 v번호 메이저 bump (예: `generate_image.py v3 → v4`)
5. CHANGELOG Migration 섹션에 사용자 조치 사항 명시

## 6. 태그 히스토리

- **v1.2.0** (2026-04-14): 공식 MINOR. `moai-media` 신규 플러그인, Nano Banana Pro + 2 체제 확정(Imagen 4 → Gemini 3 Image Preview), Kling 영상 단일화, ElevenLabs·fal.ai MCP 번들, 전 저장소 17 플러그인/70 스킬로 확장.
- v1.1.0~v1.1.3 (2026-04-14, 내부 이터레이션): moai-media 개발 점진 릴리스. v1.2.0에 집약됨.
- **v1.0.3** (2026-04-14): `/moai` 자동완성 수정 + 전체 버전 통일 + 태그 정책 확립
- 이전 로컬 태그(구 v1.1.0/v1.2.0/v1.3.0)는 marketplace 버전과 불일치하여 v1.0.3 시점에 정리·삭제함 (현재 v1.1.0은 재부여됨, 의미가 다름)

---

Version: 1.0.0
Last Updated: 2026-04-14
