#!/usr/bin/env python
"""
smartstore_test_connection 실인증 검증 스크립트.

동작:
  1. 패키지 루트의 .env 자동 로드 (있을 때).
  2. 네이버 커머스 API 토큰 발급(client_id + client_secret_sign).
  3. GET /v1/seller/account 호출로 Bearer 인증 + 도메인 API 응답 확인.

출력은 비밀키·토큰·계정 상세 정보를 포함하지 않는다.

실행:
  uv run --directory plugins/moai-seller/mcp-servers/moai-mcp-smartstore python scripts/check_auth.py
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

_BASE = Path


def _load_dotenv(env_path) -> None:
    """단순 .env 파서 — KEY=VALUE 만 처리, 따옴표 제거, 주석 무시."""
    path = env_path
    if not path.exists():
        return
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, val = line.split("=", 1)
        key = key.strip()
        val = val.strip().strip('"').strip("'")
        os.environ.setdefault(key, val)


def _mask(value: str, show: int = 4) -> str:
    if not value:
        return "(empty)"
    return value[:show] + "***" if len(value) > show else "***"


def main() -> int:
    here = _BASE(__file__).resolve().parent
    pkg_root = here.parent
    _load_dotenv(pkg_root / ".env")

    # 패키지 임포트는 .env 로드 이후(설정이 env 에 의존).
    from moai_mcp_smartstore.client import NaverCommerceClient
    from moai_mcp_smartstore.config import Config

    cfg = Config.from_env()
    print("=" * 56)
    print("네이버 커머스 API 실인증 검증")
    print("=" * 56)
    print(f"client_id   : {_mask(cfg.client_id)}")
    print(f"account_id  : {'설정됨' if cfg.account_id else '미설정'}")
    print(f"type        : {cfg.type}")
    print(f"base_url    : {cfg.base_url}")
    print("-" * 56)

    if not cfg.is_configured:
        print("FAIL: 자격증명 미설정 — .env (또는 환경변수) 에 CLIENT_ID/SECRET 을 입력하세요.")
        return 1

    client = NaverCommerceClient(cfg)

    # 1) 토큰 발급
    try:
        client.get_token()
    except Exception as exc:
        print(f"FAIL: 토큰 발급 실패 — {type(exc).__name__}")
        return 2
    print("토큰 발급    : 성공")

    # 2) 도메인 API 호출 (GET /v1/seller/account)
    try:
        data = client.request("GET", "/v1/seller/account")
    except Exception as exc:
        status = getattr(exc, "status_code", "?")
        print(f"FAIL: 도메인 API 호출 실패 — HTTP {status} {type(exc).__name__}")
        return 3

    print(f"GET /v1/seller/account : 성공 ({type(data).__name__} 응답)")
    print("=" * 56)
    print("PASS: 인증·연결 정상 (토큰 발급 + 도메인 API 응답 확인)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
