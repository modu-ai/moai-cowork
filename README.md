<div align="center">

# 🗿 K-Harness Marketplace

**한국발 AI 하네스 플러그인 마켓플레이스**

</div>

---

## 포함 플러그인

| 플러그인 | 버전 | 설명 |
|---------|------|------|
| [moai-cowork](plugins/moai-cowork/) | 0.2.0 | 84개 도메인 하네스 + 11개 스킬 + 10개 한국 특화 실행 모듈 |

---

## 설치 방법

### 방법 1: 마켓플레이스에서 설치
```
/plugin marketplace add modu-ai/cowork-plugins
/plugin install moai-cowork@cowork-plugins
```

### 방법 2: .plugin 파일로 설치

1. [Releases](https://github.com/modu-ai/cowork-plugins/releases)에서 `moai-cowork.plugin` 다운로드
2. Claude Desktop → Cowork → 플러그인 관리 → **파일에서 설치**
3. 다운로드한 `.plugin` 파일 선택

### 설치 후 초기 설정

Cowork 채팅에서 아래 커맨드를 입력합니다:
```
/moai init
```
대화형 설문을 거쳐 프로젝트에 맞춤형 `.claude/CLAUDE.md`가 자동 생성됩니다.

---

## 업데이트

```
/plugin marketplace update cowork-plugins
```

---

## 라이선스

MIT — [모두의AI (MoAI)](https://github.com/modu-ai) | 제작: GOOS
