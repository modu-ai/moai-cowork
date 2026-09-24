"""도구 응답 경계의 자격증명 가림.

클라이언트마다 따로 가리면 빠지는 곳이 생긴다(codex 적대적 감사 2026-09-14: KIPRIS 키의
URL 인코딩 형태, HTTP 200 오류 본문에 반사된 키, USPTO 헤더 키가 반사된 4xx 본문이 모두
응답에 남았다). 그래서 `server._run()`이 성공·오류 응답을 가리지 않고 전부 여기로 보낸다.

가리는 대상
- 설정된 모든 자격증명 값 — 원문, `quote`, `quote_plus`, HTML 이스케이프 형태
- 이름으로 아는 민감 파라미터·헤더 — `ServiceKey=…`, `X-API-KEY: …` 등 값이 무엇이든
"""

from __future__ import annotations

import html
import re
import urllib.parse
from typing import Any

MASK = "***"
#: 값이 무엇이든 이름만으로 가리는 쿼리 파라미터·헤더.
_NAMED_PATTERNS = (
    re.compile(r"(ServiceKey=)[^&\s\"'<>]+", re.I),
    re.compile(r"((?:X-API-KEY|USPTO-API-KEY|Authorization)\s*[:=]\s*)[^\s\"'<>,;]+", re.I),
    re.compile(r"(\bBasic\s+)[A-Za-z0-9+/=]+", re.I),
)


def _forms(secret: str) -> list[str]:
    forms = {
        secret,
        urllib.parse.quote(secret, safe=""),
        urllib.parse.quote_plus(secret),
        html.escape(secret),
    }
    return sorted((f for f in forms if f), key=len, reverse=True)


def redact_text(text: str, secrets: list[str]) -> str:
    for secret in secrets:
        for form in _forms(secret):
            if len(form) >= 6:
                text = text.replace(form, MASK)
            else:
                # 짧은 키도 독립된 값으로 반사되면 가린다. 단어 내부의 같은 글자는 보존한다.
                text = re.sub(rf"(?<![\w]){re.escape(form)}(?![\w])", MASK, text)
    for pattern in _NAMED_PATTERNS:
        text = pattern.sub(lambda m: m.group(1) + MASK, text)
    return text


def redact(value: Any, secrets: list[str]) -> Any:
    """딕셔너리·리스트를 재귀적으로 훑어 문자열마다 가린다."""
    if isinstance(value, str):
        return redact_text(value, secrets)
    if isinstance(value, dict):
        return {k: redact(v, secrets) for k, v in value.items()}
    if isinstance(value, list):
        return [redact(v, secrets) for v in value]
    if isinstance(value, tuple):
        return tuple(redact(v, secrets) for v in value)
    return value
