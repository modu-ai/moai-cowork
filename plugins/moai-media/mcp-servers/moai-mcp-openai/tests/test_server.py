"""외부 과금 없이 Image API 요청과 MCP 결과를 확인한다."""

import base64
import os

import httpx
import pytest
import respx
from mcp.types import ImageContent
from moai_mcp_core import credentials

from moai_mcp_openai.server import API_URL, openai_image_generate


def test_missing_key_does_not_call_api(monkeypatch, tmp_path):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    monkeypatch.setenv("HOME", str(tmp_path))
    with respx.mock(assert_all_called=False) as router:
        route = router.post(API_URL).mock(return_value=httpx.Response(200, json={}))
        result = openai_image_generate("테스트 이미지")
    assert result.isError is True
    assert route.called is False


def test_exact_model_and_image_content(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "test-only-key")
    raw = b"\x89PNG\r\n\x1a\nexample"
    encoded = base64.b64encode(raw).decode("ascii")
    with respx.mock() as router:
        route = router.post(API_URL).mock(
            return_value=httpx.Response(200, json={"data": [{"b64_json": encoded}], "usage": {"output_tokens": 1}})
        )
        result = openai_image_generate("파란 의자", model="gpt-image-2.5-sunburst")
    assert route.called is True
    sent = route.calls[0].request
    assert sent.headers["Authorization"] == "Bearer test-only-key"
    assert b'"model":"gpt-image-2.5-sunburst"' in sent.content
    assert b'"n":1' in sent.content
    assert result.isError is not True
    image = next(block for block in result.content if isinstance(block, ImageContent))
    assert image.mimeType == "image/png"
    assert base64.b64decode(image.data) == raw


def test_invalid_request_does_not_call_api(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "test-only-key")
    with respx.mock(assert_all_called=False) as router:
        route = router.post(API_URL).mock(return_value=httpx.Response(200, json={}))
        assert openai_image_generate(" ").isError is True
        assert openai_image_generate("a", size="15x15").isError is True
        assert openai_image_generate("a", model="gpt-image-2").isError is True
    assert route.called is False


def test_http_error_hides_key(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "test-only-key")
    with respx.mock() as router:
        router.post(API_URL).mock(return_value=httpx.Response(401, json={"error": {"message": "bad key"}}))
        result = openai_image_generate("의자")
    assert result.isError is True
    assert "test-only-key" not in result.content[0].text
    assert "401" in result.content[0].text


@pytest.mark.skipif(os.name == "nt", reason="POSIX file mode only")
def test_loose_key_file_permissions_block_api(monkeypatch, tmp_path):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    monkeypatch.setattr(credentials, "DEFAULT_DIR", tmp_path)
    path = tmp_path / "openai.json"
    path.write_text('{"OPENAI_API_KEY":"test-only-key"}', encoding="utf-8")
    tmp_path.chmod(0o755)
    path.chmod(0o644)
    with respx.mock(assert_all_called=False) as router:
        route = router.post(API_URL).mock(return_value=httpx.Response(200, json={}))
        result = openai_image_generate("의자")
    assert result.isError is True
    assert route.called is False


def test_large_allowed_image_is_returned(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "test-only-key")
    encoded = base64.b64encode(b"x" * (26 * 1024 * 1024)).decode("ascii")
    with respx.mock() as router:
        router.post(API_URL).mock(return_value=httpx.Response(200, json={"data": [{"b64_json": encoded}]}))
        result = openai_image_generate("큰 이미지", size="3840x2160")
    assert result.isError is not True
    image = next(block for block in result.content if isinstance(block, ImageContent))
    assert len(base64.b64decode(image.data)) == 26 * 1024 * 1024
