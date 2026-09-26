"""Path arguments must stay inside one URL segment, including during pagination."""

from __future__ import annotations

import httpx
import pytest

from moai_mcp_cafe24.client import Cafe24Client


def test_path_value_cannot_change_endpoint_or_query(cfg):
    seen: list[httpx.Request] = []

    def respond(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        return httpx.Response(200, json={"items": []})

    client = Cafe24Client(cfg)
    client._http.close()
    client._http = httpx.Client(transport=httpx.MockTransport(respond))
    try:
        client.request(
            "GET", "/api/v2/admin/products/{product_no}/variants",
            path_params={"product_no": "123/other?limit=999"},
        )
        assert seen[0].url.raw_path == b"/api/v2/admin/products/123%2Fother%3Flimit%3D999/variants"
        assert seen[0].url.query == b""
    finally:
        client.close()


def test_pagination_passes_path_parameters_on_every_page(cfg):
    paths: list[bytes] = []

    def respond(request: httpx.Request) -> httpx.Response:
        paths.append(request.url.raw_path)
        rows = [{"id": 1}, {"id": 2}] if request.url.params["offset"] == "0" else []
        return httpx.Response(200, json={"variants": rows})

    client = Cafe24Client(cfg)
    client._http.close()
    client._http = httpx.Client(transport=httpx.MockTransport(respond))
    try:
        result = client.list_paginated(
            "/api/v2/admin/products/{product_no}/variants",
            path_params={"product_no": 123}, page_size=2,
        )
        assert result["pagination"]["pages_fetched"] == 2
        assert len(result["variants"]) == 2
        assert paths == [b"/api/v2/admin/products/123/variants?limit=2&offset=0",
                         b"/api/v2/admin/products/123/variants?limit=2&offset=2"]
    finally:
        client.close()


def test_missing_path_parameter_fails_before_network(cfg):
    client = Cafe24Client(cfg)
    try:
        with pytest.raises(ValueError, match="Missing path parameter"):
            client.request("GET", "/api/v2/admin/products/{product_no}/variants")
    finally:
        client.close()
