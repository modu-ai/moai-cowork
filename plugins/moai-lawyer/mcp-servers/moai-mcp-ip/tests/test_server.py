"""moai-mcp-ip 단위 테스트 — 네트워크 없이 httpx.MockTransport 로 검증한다.

검증 축
- 자격증명 게이트: 미설정이면 외부 호출 없이 setup_required, 응답에 값이 절대 없음
- KIPRIS: HTTP 200 + successYN=N 판정, 기간 만료(31) → auth_error, count 가 body 옆에 있는 구조, 키 가림
- 상표 검색 필수 그룹 플래그
- USPTO ODP: X-API-KEY 헤더, 429 → 5초 이상 대기 후 재시도
- TSDR: 번호 정규화, 인증서 오류 안내
- JPO: 토큰 발급 → Bearer, statusCode 107(없음)/203(한도)
- EPO: Basic 토큰, X-OPS-Range 가 401 재인증 뒤에도 유지
"""

from __future__ import annotations

import json

import httpx
import pytest

from moai_mcp_ip import server
from moai_mcp_ip.epo import EpoAuth, EpoClient
from moai_mcp_ip.jpo import JpoAuth, JpoClient
from moai_mcp_ip.kipris import KiprisClient
from moai_mcp_ip.uspto import OdpClient, TsdrClient

ALL_KEYS = (
    "KIPRIS_API_KEY", "USPTO_ODP_API_KEY", "USPTO_TSDR_API_KEY", "USPTO_API_KEY",
    "JPO_API_USER", "JPO_API_PASSWORD", "JPO_ACCESS_TOKEN", "EPO_OPS_KEY", "EPO_OPS_SECRET",
)

KIPRIS_TRADEMARK_OK = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?><response><header>
<successYN>Y</successYN><resultCode>00</resultCode><resultMsg>NORMAL SERVICE.</resultMsg></header>
<body><items><item><applicationNumber>4020210124213</applicationNumber><applicationStatus>등록</applicationStatus>
<classificationCode>38</classificationCode><title>모두의 상회</title><viennaCode></viennaCode></item>
<item><applicationNumber>4020220202448</applicationNumber><title>모두의 봄</title></item></items></body>
<count><numOfRows>2</numOfRows><pageNo>1</pageNo><totalCount>535</totalCount></count></response>"""

KIPRIS_EXPIRED = """<response><header><successYN>N</successYN><resultCode>31</resultCode>
<resultMsg>DEADLINE_HAS_EXPIRED_ERROR</resultMsg></header></response>"""


@pytest.fixture(autouse=True)
def _isolate(monkeypatch, tmp_path):
    for key in ALL_KEYS:
        monkeypatch.delenv(key, raising=False)
    monkeypatch.setenv("IP_CREDENTIALS_FILE", str(tmp_path / "ip.json"))
    server._reset_for_tests()
    monkeypatch.setattr(server, "_TRANSPORT", None)
    yield
    server._reset_for_tests()


def _no_network(request: httpx.Request) -> httpx.Response:  # pragma: no cover - 호출되면 실패
    raise AssertionError(f"외부 호출이 나가면 안 됩니다: {request.url}")


# ------------------------------------------------------------------ 게이트
def test_check_access_reports_missing_without_values(monkeypatch):
    result = server.ip_check_access()
    assert result["ready"] is False
    assert set(result["missing"]) == {"kipris-plus", "uspto-odp", "uspto-tsdr", "jpo", "epo-ops"}
    assert all(s["registration_url"].startswith("https://") for s in result["sources"])


def test_check_access_never_echoes_secret(monkeypatch):
    monkeypatch.setenv("KIPRIS_API_KEY", "SECRET-VALUE-123")
    result = server.ip_check_access(["kipris-plus"])
    assert result["ready"] is True
    assert "SECRET-VALUE-123" not in json.dumps(result, ensure_ascii=False)


def test_placeholder_is_treated_as_missing(monkeypatch):
    monkeypatch.setenv("KIPRIS_API_KEY", "${user_config.KIPRIS_API_KEY}")
    assert server.ip_check_access(["kipris-plus"])["missing"] == ["kipris-plus"]


def test_credentials_file_is_read(monkeypatch, tmp_path):
    (tmp_path / "ip.json").write_text(json.dumps({"EPO_OPS_KEY": "k", "EPO_OPS_SECRET": "s"}), encoding="utf-8")
    assert server.ip_check_access(["epo-ops"])["ready"] is True


def test_unknown_source_is_flagged():
    result = server.ip_check_access(["wipo"])
    assert result["ready"] is False
    assert result["unknown_sources"] == ["wipo"]


def test_tool_without_credentials_returns_setup_required_and_no_call(monkeypatch):
    monkeypatch.setattr(server, "_TRANSPORT", httpx.MockTransport(_no_network))
    result = server.kipris_trademark_search(trademark_name="모두의")
    assert result["ok"] is False
    assert result["error"] == "setup_required"
    assert "plus.kipris.or.kr" in result["details"]["guide"]


def test_verify_distinguishes_expired_product(monkeypatch):
    monkeypatch.setenv("KIPRIS_API_KEY", "k")

    def handler(request: httpx.Request) -> httpx.Response:
        if "patUtiModInfoSearchSevice" in request.url.path:
            return httpx.Response(200, text=KIPRIS_EXPIRED)
        return httpx.Response(200, text=KIPRIS_TRADEMARK_OK)

    monkeypatch.setattr(server, "_TRANSPORT", httpx.MockTransport(handler))
    entry = server.ip_check_access(["kipris-plus"], verify=True)["sources"][0]
    assert entry["verification"]["patent_product"]["result"] == "auth_error"
    assert entry["verification"]["trademark_product"]["result"] == "ok"


# ------------------------------------------------------------------ KIPRIS
def test_kipris_trademark_search_parses_items_and_count():
    seen: dict = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["params"] = dict(request.url.params)
        seen["path"] = request.url.path
        return httpx.Response(200, text=KIPRIS_TRADEMARK_OK)

    client = KiprisClient("k", transport=httpx.MockTransport(handler))
    result = client.trademark_search(trademark_name="모두의", statuses=["registration"])
    assert seen["path"].endswith("/trademarkInfoSearchService/getAdvancedSearch")
    assert seen["params"]["ServiceKey"] == "k"
    assert seen["params"]["registration"] == "true" and seen["params"]["application"] == "false"
    assert seen["params"]["trademark"] == "true" and seen["params"]["character"] == "true"
    assert result["total_count"] == 535
    assert result["returned_count"] == 2
    assert result["items"][0]["title"] == "모두의 상회"
    assert "viennaCode" not in result["items"][0]  # 빈 값은 버린다
    assert "ServiceKey" not in result["query"]


def test_kipris_rejects_unknown_status_flag():
    client = KiprisClient("k", transport=httpx.MockTransport(_no_network))
    with pytest.raises(Exception) as info:
        client.trademark_search(trademark_name="x", statuses=["granted"])
    assert "statuses" in str(info.value)


def test_kipris_error_in_http_200_is_raised():
    client = KiprisClient("k", transport=httpx.MockTransport(lambda r: httpx.Response(200, text=KIPRIS_EXPIRED)))
    result = server._run(lambda: client.patent_search(word="battery"))
    assert result["error"] == "auth_error"
    assert result["details"]["result_code"] == "31"


def test_kipris_network_error_scrubs_key():
    def handler(request: httpx.Request) -> httpx.Response:
        raise httpx.ConnectError(f"boom {request.url}")

    client = KiprisClient("TOPSECRET", transport=httpx.MockTransport(handler))
    client._http._sleep = lambda _s: None
    result = server._run(lambda: client.trademark_detail("40-2021-0124213"))
    assert "TOPSECRET" not in json.dumps(result, ensure_ascii=False)


def test_kipris_patent_search_requires_a_condition():
    client = KiprisClient("k", transport=httpx.MockTransport(_no_network))
    result = server._run(lambda: client.patent_search())
    assert result["ok"] is False


# ------------------------------------------------------------------ USPTO
def test_odp_search_sends_key_header_and_waits_on_429():
    calls: list[httpx.Request] = []
    sleeps: list[float] = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(request)
        if len(calls) == 1:
            return httpx.Response(429)
        return httpx.Response(200, json={"count": 1, "patentFileWrapperDataBag": []})

    client = OdpClient("odp-key", transport=httpx.MockTransport(handler), sleep=sleeps.append)
    result = client.patent_search(q="battery", limit=5)
    assert calls[0].headers["X-API-KEY"] == "odp-key"
    assert json.loads(calls[0].content)["pagination"] == {"offset": 0, "limit": 5}
    assert sleeps and sleeps[0] >= 5.0
    assert result["data"]["count"] == 1


def test_tsdr_normalizes_prefixed_number():
    seen: dict = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["path"] = request.url.path
        seen["key"] = request.headers.get("USPTO-API-KEY")
        return httpx.Response(200, text="<ns:Tx xmlns:ns='urn:x'><ns:Mark>THREAD</ns:Mark></ns:Tx>")

    client = TsdrClient("tsdr-key", transport=httpx.MockTransport(handler))
    result = client.trademark_status("sn 78787878")
    assert seen["path"] == "/ts/cd/casestatus/sn78787878/info"
    assert seen["key"] == "tsdr-key"
    assert result["status"] == {"Mark": "THREAD"}


def test_tsdr_rejects_bad_serial():
    client = TsdrClient("k", transport=httpx.MockTransport(_no_network))
    result = server._run(lambda: client.trademark_status("123", "sn"))
    assert result["ok"] is False


def test_tsdr_certificate_error_is_explained():
    def handler(request: httpx.Request) -> httpx.Response:
        raise httpx.ConnectError("[SSL: CERTIFICATE_VERIFY_FAILED] certificate has expired")

    client = TsdrClient("k", transport=httpx.MockTransport(handler))
    client._http._sleep = lambda _s: None
    result = server._run(lambda: client.trademark_status("78787878"))
    assert result["error"] == "upstream_error"
    assert "인증서" in result["message"]


# ------------------------------------------------------------------ JPO
def _jpo_handler(status_code: str = "100", data: dict | None = None):
    seen: dict = {"token_calls": 0}

    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.path == "/auth/token":
            seen["token_calls"] += 1
            seen["form"] = request.content.decode()
            return httpx.Response(200, json={"access_token": "jpo-token", "expires_in": 3600, "refresh_token": "r"})
        seen["auth"] = request.headers.get("Authorization")
        seen["path"] = request.url.path
        return httpx.Response(200, json={"result": {"statusCode": status_code, "remainAccessCount": "799", "data": data or {}}})

    return handler, seen


def test_jpo_progress_uses_bearer_token():
    handler, seen = _jpo_handler(data={"inventionTitle": "電池"})
    transport = httpx.MockTransport(handler)
    client = JpoClient(JpoAuth(username="u", password="p", transport=transport), transport=transport)
    result = client.progress("patent", "2020-008423")
    assert "grant_type=password" in seen["form"]
    assert seen["auth"] == "Bearer jpo-token"
    assert seen["path"] == "/api/patent/v1/app_progress/2020008423"
    assert result["found"] is True and result["data"]["inventionTitle"] == "電池"


def test_jpo_not_found_is_not_an_error():
    handler, _ = _jpo_handler(status_code="107")
    transport = httpx.MockTransport(handler)
    client = JpoClient(JpoAuth(username="u", password="p", transport=transport), transport=transport)
    result = client.registration("trademark", "2018009480")
    assert result["ok"] is True and result["found"] is False


def test_jpo_daily_limit_maps_to_quota():
    handler, _ = _jpo_handler(status_code="203")
    transport = httpx.MockTransport(handler)
    client = JpoClient(JpoAuth(username="u", password="p", transport=transport), transport=transport)
    assert server._run(lambda: client.progress("trademark", "2018009480"))["error"] == "quota_exhausted"


def test_jpo_validates_number_and_kind():
    client = JpoClient(JpoAuth(username="u", password="p", transport=httpx.MockTransport(_no_network)))
    assert server._run(lambda: client.progress("patent", "12345"))["ok"] is False
    assert server._run(lambda: client.case_number_reference("trademark", "publication", "1"))["ok"] is False


# ------------------------------------------------------------------ EPO
def test_epo_search_keeps_range_header_after_reauth():
    seen: dict = {"tokens": 0, "api": []}

    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.path == "/3.2/auth/accesstoken":
            seen["tokens"] += 1
            assert request.headers["Authorization"].startswith("Basic ")
            return httpx.Response(200, json={"access_token": f"t{seen['tokens']}", "expires_in": "1199"})
        seen["api"].append(request)
        if len(seen["api"]) == 1:
            return httpx.Response(401, text="<fault/>")
        return httpx.Response(200, json={"ops:world-patent-data": {}}, headers={"X-Throttling-Control": "idle"})

    transport = httpx.MockTransport(handler)
    client = EpoClient(EpoAuth("key", "secret", transport=transport), transport=transport)
    result = client.search('ta="battery"', start=1, end=50)
    assert seen["tokens"] == 2
    assert [r.headers.get("X-OPS-Range") for r in seen["api"]] == ["1-50", "1-50"]
    assert result["quota"] == {"X-Throttling-Control": "idle"}


def test_epo_range_limits():
    client = EpoClient(EpoAuth("k", "s", transport=httpx.MockTransport(_no_network)))
    assert server._run(lambda: client.search("ta=x", start=1, end=101))["ok"] is False
    assert server._run(lambda: client.search("ta=x", start=1990, end=2010))["ok"] is False


def test_bounded_truncates_large_payload(monkeypatch):
    monkeypatch.setattr(server, "MAX_RESPONSE_CHARS", 50)
    result = server._run(lambda: {"ok": True, "data": "x" * 500})
    assert result["truncated"] is True


def test_request_urls_are_not_logged(caplog):
    """KIPRIS 키는 쿼리 파라미터에 실린다 — httpx INFO 로그로 새면 안 된다."""
    import logging

    caplog.set_level(logging.DEBUG)
    client = KiprisClient("LOGSECRET", transport=httpx.MockTransport(lambda r: httpx.Response(200, text=KIPRIS_TRADEMARK_OK)))
    client.trademark_search(trademark_name="x")
    assert logging.getLogger("httpx").getEffectiveLevel() >= logging.WARNING
    assert "LOGSECRET" not in caplog.text


# ------------------------------------------------------------------ 응답 경계 가림 (codex 감사 반영)
def test_encoded_kipris_key_is_redacted_in_network_error(monkeypatch):
    monkeypatch.setenv("KIPRIS_API_KEY", "KIPRIS+SECRET/=")

    def handler(request: httpx.Request) -> httpx.Response:
        raise httpx.ConnectError(f"boom {request.url}")

    monkeypatch.setattr(server, "_TRANSPORT", httpx.MockTransport(handler))
    text = json.dumps(server.kipris_trademark_detail("4020210124213"), ensure_ascii=False)
    assert "KIPRIS+SECRET/=" not in text and "KIPRIS%2BSECRET%2F%3D" not in text


def test_reflected_key_in_kipris_http200_error_is_redacted(monkeypatch):
    monkeypatch.setenv("KIPRIS_API_KEY", "KIPRIS_SECRET_9f3")
    body = "<response><header><successYN>N</successYN><resultCode>99</resultCode><resultMsg>KIPRIS_SECRET_9f3</resultMsg></header></response>"
    monkeypatch.setattr(server, "_TRANSPORT", httpx.MockTransport(lambda r: httpx.Response(200, text=body)))
    text = json.dumps(server.kipris_patent_search(word="x"), ensure_ascii=False)
    assert "KIPRIS_SECRET_9f3" not in text


def test_reflected_key_in_broken_xml_is_redacted(monkeypatch):
    monkeypatch.setenv("KIPRIS_API_KEY", "KIPRIS_PARSE_SECRET_a7b")
    monkeypatch.setattr(server, "_TRANSPORT", httpx.MockTransport(lambda r: httpx.Response(200, text="<broken>KIPRIS_PARSE_SECRET_a7b")))
    text = json.dumps(server.kipris_patent_search(word="x"), ensure_ascii=False)
    assert "KIPRIS_PARSE_SECRET_a7b" not in text


def test_uspto_header_key_reflected_in_error_body_is_redacted(monkeypatch):
    monkeypatch.setenv("USPTO_ODP_API_KEY", "USPTO_HEADER_SECRET_b8c")
    monkeypatch.setattr(server, "_TRANSPORT", httpx.MockTransport(lambda r: httpx.Response(400, text="bad key USPTO_HEADER_SECRET_b8c")))
    text = json.dumps(server.uspto_patent_search(q="x"), ensure_ascii=False)
    assert "USPTO_HEADER_SECRET_b8c" not in text


def test_uspto_key_reflected_in_success_payload_is_redacted(monkeypatch):
    monkeypatch.setenv("USPTO_TSDR_API_KEY", "USPTO_XML_SECRET_c9d")
    monkeypatch.setattr(server, "_TRANSPORT", httpx.MockTransport(lambda r: httpx.Response(200, text="<a><echo>USPTO_XML_SECRET_c9d</echo></a>")))
    text = json.dumps(server.uspto_trademark_status("78787878"), ensure_ascii=False)
    assert "USPTO_XML_SECRET_c9d" not in text and "***" in text


def test_named_params_are_redacted_even_without_configured_secret():
    from moai_mcp_ip.redact import redact_text

    out = redact_text("GET https://x/?word=a&ServiceKey=abc%2F%3D&pageNo=1 X-API-KEY: zzz", [])
    assert "abc%2F%3D" not in out and "zzz" not in out and "word=a" in out
