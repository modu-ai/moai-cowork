"""정확한 GPT Image 2.5 모델을 지정하는 로컬 MCP 서버."""

from __future__ import annotations

import base64
import binascii
import json
import os
import re
import stat
from typing import Literal

import httpx
from mcp.server.fastmcp import FastMCP
from mcp.types import CallToolResult, ImageContent, TextContent

from moai_mcp_core.credentials import CredentialStore, is_unset

API_URL = "https://api.openai.com/v1/images/generations"
MODELS = ("gpt-image-2.5-flare", "gpt-image-2.5-sunburst")
MAX_IMAGE_BYTES = 100 * 1024 * 1024

mcp = FastMCP(
    "moai-mcp-openai",
    instructions=(
        "OpenAI API 키가 별도로 설정된 경우에만 GPT Image 2.5 이미지를 생성합니다. "
        "사용자가 정확한 모델을 지정하면 이를 유지하고, ChatGPT 기본 이미지 도구를 "
        "2.5 결과로 표시하지 마세요. 생성 전 API 과금 사실을 알리세요."
    ),
)


def _error(message: str) -> CallToolResult:
    return CallToolResult(
        content=[TextContent(type="text", text=message)], isError=True
    )


def _valid_size(size: str) -> bool:
    if size == "auto":
        return True
    match = re.fullmatch(r"(\d{3,4})x(\d{3,4})", size)
    if match is None:
        return False
    width, height = map(int, match.groups())
    area = width * height
    return (
        width % 16 == 0
        and height % 16 == 0
        and max(width, height) <= 3840
        and max(width, height) <= 3 * min(width, height)
        and 655_360 <= area <= 8_294_400
    )


@mcp.tool()
def openai_image_generate(
    prompt: str,
    model: Literal["gpt-image-2.5-flare", "gpt-image-2.5-sunburst"] = "gpt-image-2.5-flare",
    size: str = "1024x1024",
    quality: Literal["low", "medium", "high", "xhigh", "max", "auto"] = "medium",
    output_format: Literal["png", "jpeg", "webp"] = "png",
) -> CallToolResult:
    """유료 OpenAI Image API로 GPT Image 2.5 이미지 한 장을 직접 생성합니다."""
    if not isinstance(prompt, str) or not prompt.strip() or len(prompt) > 32_000:
        return _error("프롬프트는 1~32,000자 문자열이어야 합니다. API를 호출하지 않았습니다.")
    if model not in MODELS or not _valid_size(size):
        return _error("모델 또는 이미지 크기가 지원 범위를 벗어납니다. API를 호출하지 않았습니다.")
    store = CredentialStore("openai")
    key = store.get("OPENAI_API_KEY")
    if not key:
        return _error(
            "OpenAI API 키가 없어 생성하지 않았습니다. 앱의 MCP 연결 설정 또는 "
            "사용자 컴퓨터의 ~/.moai/mcp/openai.json에 OPENAI_API_KEY를 설정하세요. "
            "키를 채팅에 입력하지 마세요."
        )
    if os.name != "nt" and store.path.is_file() and is_unset(os.environ.get("OPENAI_API_KEY")):
        try:
            file_mode = stat.S_IMODE(store.path.stat().st_mode)
            dir_mode = stat.S_IMODE(store.path.parent.stat().st_mode)
        except OSError:
            return _error("OpenAI API 키 파일 권한을 확인하지 못해 생성하지 않았습니다.")
        if file_mode & 0o077 or dir_mode & 0o077:
            return _error(
                "OpenAI API 키 파일은 소유자만 읽을 수 있는 0600, "
                "상위 mcp 폴더는 0700 권한이어야 합니다. 생성하지 않았습니다."
            )
    try:
        with httpx.Client(timeout=120.0) as client:
            response = client.post(
                API_URL,
                headers={"Authorization": f"Bearer {key}"},
                json={
                    "model": model,
                    "prompt": prompt,
                    "size": size,
                    "quality": quality,
                    "output_format": output_format,
                    "n": 1,
                },
            )
        response.raise_for_status()
        payload = response.json()
        encoded = payload["data"][0]["b64_json"]
        if not isinstance(encoded, str) or len(encoded) > MAX_IMAGE_BYTES * 2:
            raise ValueError("이미지 데이터가 없거나 너무 큽니다")
        image = base64.b64decode(encoded, validate=True)
        if not image or len(image) > MAX_IMAGE_BYTES:
            raise ValueError("이미지 데이터가 없거나 너무 큽니다")
    except httpx.HTTPStatusError as exc:
        return _error(f"OpenAI Image API 요청 실패: HTTP {exc.response.status_code}. 이미지를 받지 못했습니다.")
    except (httpx.HTTPError, ValueError, KeyError, IndexError, TypeError, binascii.Error) as exc:
        return _error(f"OpenAI Image API 결과를 받거나 해석하지 못했습니다: {type(exc).__name__}.")
    usage = payload.get("usage")
    metadata = {"model_requested": model, "size": size, "quality": quality}
    if isinstance(usage, dict):
        metadata["usage"] = usage
    return CallToolResult(
        content=[
            TextContent(type="text", text=json.dumps(metadata, ensure_ascii=False)),
            ImageContent(type="image", data=encoded, mimeType=f"image/{output_format}"),
        ]
    )


def main() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
