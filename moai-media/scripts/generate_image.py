#!/usr/bin/env python3
"""
Google Nano Banana Image Generator (v4.1.0 - 공식 문서 정합)

Google Gemini API (Gemini 3 Image Preview 계열)로 이미지를 생성합니다.
공식 문서(ai.google.dev/gemini-api/docs/image-generation) 스펙 100% 정합.

[v4.3.0 변경사항 — 2026-04-14]
- nano-banana-ultra 제거: Pro + 2 단 두 가지만 유지
- ULTRA_ALIASES 상수 및 is_ultra 분기 제거 → 코드 단순화
- 제거된 별칭(nano-banana, nano-banana-ultra, cheap, ultra)은 Pro/2로 자동 승격

[v4.2.0 — 2026-04-14]
- 공식 모델 2종만 사용: Nano Banana Pro + Nano Banana 2
- gemini-2.5-flash-image 제거: v1.1.1의 nano-banana 별칭은 Pro로 자동 승격
- image_size 필수화 (always set): 모델별 자동 기본값

[v4.1.0 — 2026-04-14]
- 화면비 리스트 수정: 공식 14종 (1:4, 4:1, 1:8, 8:1 추가)
- REST API 페이로드 camelCase 정리 (공식 REST 스펙 준수)
- 응답 파싱 inlineData(camelCase) 우선 (REST 기본값)
- image_size 지원 목록 공식화: "512", "1K", "2K", "4K"

[v4.0.0 — 2026-04-14]
- 모델 전환: imagen-4.0-* → gemini-3-pro-image-preview / gemini-3.1-flash-image-preview
- 엔드포인트: :predict → :generateContent
- 파라미터: numberOfImages + top-level aspectRatio → imageConfig + imageSize
- 응답 파싱: predictions[].bytesBase64Encoded → candidates[].content.parts[].inlineData.data
- 환경변수: GEMINI_API_KEY 우선, NANO_BANANA_API_KEY 레거시 호환

[v3.0.0 패치 유지 — 2026-03]
- sanitize_text(): 단독 서로게이트 문자(U+D800~U+DFFF) 자동 제거
- safe_json_encode(): ensure_ascii=False + 서로게이트 이스케이프 제거
- 타임아웃 90초

사용법:
  python generate_image.py "<프롬프트>" <저장경로.png> [aspect_ratio] [model]

예시:
  python generate_image.py "평온한 아침 커피" slide_01.png 3:4
  python generate_image.py "'오늘의 인사이트' 제목" cover.png 1:1 nano-banana-pro
  python generate_image.py "저가 시안" draft.png 3:4 nano-banana-2

aspect_ratio (공식 14종):
  3:4   → 인스타 카드뉴스 (기본값)
  1:1   → 정사각
  9:16  → 스토리/릴스
  16:9  → 와이드 / 유튜브
  21:9  → 시네마틱
  2:3, 3:2, 4:3, 4:5, 5:4 → 기타 표준 비율
  1:4, 4:1, 1:8, 8:1 → 배너·띠 형식

model (공식 2종):
  nano-banana-pro → gemini-3-pro-image-preview     (기본, 2K, SOTA 텍스트)
  nano-banana-2   → gemini-3.1-flash-image-preview (빠름, 저비용, 1K)
"""
from __future__ import annotations

import base64
import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import TypedDict

# ── 설정 ────────────────────────────────────────────────────────────────────

BASE_URL = (
    "https://generativelanguage.googleapis.com/v1beta/"
    "models/{model}:generateContent?key={key}"
)

DEFAULT_TIMEOUT = 90  # 초

# 모델 별칭 매핑 (v4.3: Pro + 2 단 두 가지)
# 참고: https://ai.google.dev/gemini-api/docs/image-generation
MODEL_MAP: dict[str, str] = {
    # 공식 Nano Banana 2종
    "nano-banana-pro": "gemini-3-pro-image-preview",      # SOTA, 2K 기본
    "nano-banana-2":   "gemini-3.1-flash-image-preview",  # 비용 효율, 1K 기본
    # 단축 별칭
    "pro":  "gemini-3-pro-image-preview",
    "fast": "gemini-3.1-flash-image-preview",
    # 레거시 Imagen 4 (v1.0.x) → Pro 자동 전환
    "imagen-4.0-generate-001":       "gemini-3-pro-image-preview",
    "imagen-4.0-fast-generate-001":  "gemini-3.1-flash-image-preview",
    "imagen-4.0-ultra-generate-001": "gemini-3-pro-image-preview",
    # 레거시 Imagen 3 하위호환
    "imagen-3.0-generate-002":       "gemini-3-pro-image-preview",
    "imagen-3.0-fast-generate-001":  "gemini-3.1-flash-image-preview",
    # 제거된 별칭 자동 승격 (사용자 코드 무수정 보장)
    "nano-banana":       "gemini-3-pro-image-preview",  # v1.1.1 별칭
    "nano-banana-ultra": "gemini-3-pro-image-preview",  # v1.1.2 프리셋 (v1.1.3 제거)
    "cheap":             "gemini-3.1-flash-image-preview",
    "ultra":             "gemini-3-pro-image-preview",
}

# Gemini Image Preview 공식 지원 화면비 (14종, 공식 문서 기준)
# 참고: https://ai.google.dev/gemini-api/docs/image-generation
SUPPORTED_ASPECT_RATIOS = {
    "1:1", "2:3", "3:2", "3:4", "4:3", "4:5", "5:4",
    "9:16", "16:9", "21:9",
    "1:4", "4:1", "1:8", "8:1",
}

# Gemini Image Preview 지원 해상도 (공식 문서 기준)
SUPPORTED_IMAGE_SIZES = {"512", "1K", "2K", "4K"}


class Job(TypedDict, total=False):
    """배치 생성 작업 단위."""
    prompt: str
    filename: str
    ratio: str
    model: str


# ── API 키 로딩 ────────────────────────────────────────────────────────────


def _find_key_file() -> Path | None:
    """MoAI-Cowork 환경의 키 파일 자동 탐색."""
    candidates: list[Path] = []
    plugin_data = os.environ.get("CLAUDE_PLUGIN_DATA")
    if plugin_data:
        candidates.append(Path(plugin_data) / "moai-credentials.env")
    candidates.append(Path.home() / ".gemini-api-key")
    candidates.append(Path.home() / ".nano-banana-api-key")
    for p in candidates:
        if p.exists():
            return p
    return None


def load_api_key() -> str | None:
    """
    API 키 로드 우선순위:
    1. GEMINI_API_KEY 환경변수 (권장)
    2. NANO_BANANA_API_KEY 환경변수 (레거시 호환)
    3. 키 파일 (~/.gemini-api-key, ~/.nano-banana-api-key, moai-credentials.env)
    """
    for env_name in ("GEMINI_API_KEY", "NANO_BANANA_API_KEY"):
        key = os.environ.get(env_name)
        if key:
            return key.strip()

    kf = _find_key_file()
    if not kf:
        return None

    content = kf.read_text()
    if kf.name == "moai-credentials.env":
        for line in content.splitlines():
            for prefix in ("GEMINI_API_KEY=", "NANO_BANANA_API_KEY="):
                if line.startswith(prefix):
                    return line[len(prefix):].strip()
        return None
    return content.strip()


# ── 서로게이트 안전 처리 ───────────────────────────────────────────────────


def sanitize_text(text: str) -> str:
    """단독 서로게이트 문자(U+D800~U+DFFF) 제거."""
    if not text:
        return text
    return re.sub(r"[\ud800-\udfff]", "", str(text))


def safe_json_dumps(obj: object, **kwargs: object) -> str:
    """ensure_ascii=False + 서로게이트 이스케이프 제거."""
    kwargs.setdefault("ensure_ascii", False)
    result = json.dumps(obj, **kwargs)  # type: ignore[arg-type]
    result = re.sub(
        r"\\u[dD][89aAbB][0-9a-fA-F]{2}(?!\\u[dD][cCdDeEfF][0-9a-fA-F]{2})",
        "", result,
    )
    result = re.sub(
        r"(?<!\\u[dD][89aAbB][0-9a-fA-F]{2})\\u[dD][cCdDeEfF][0-9a-fA-F]{2}",
        "", result,
    )
    return result


def safe_json_encode(obj: object) -> bytes:
    """UTF-8 JSON bytes로 안전 변환."""
    return safe_json_dumps(obj).encode("utf-8")


# ── 화면비 검증 ───────────────────────────────────────────────────────────


def validate_ratio(aspect_ratio: str) -> str:
    """Gemini 3 Image Preview 지원 화면비 검증. 미지원 시 3:4 대체."""
    if aspect_ratio in SUPPORTED_ASPECT_RATIOS:
        return aspect_ratio
    print(
        f"[WARN] 미지원 화면비 '{aspect_ratio}'. 기본값 '3:4'로 대체합니다.",
        file=sys.stderr,
    )
    return "3:4"


# ── 이미지 생성 ───────────────────────────────────────────────────────────


def generate_image(
    prompt: str,
    output_path: str,
    aspect_ratio: str = "3:4",
    model_alias: str = "nano-banana-pro",
) -> bool:
    """Gemini 3 Image Preview API로 이미지 생성."""
    api_key = load_api_key()
    if not api_key:
        print(
            "[ERROR] API 키가 없습니다. GEMINI_API_KEY 환경변수를 설정하세요.",
            file=sys.stderr,
        )
        return False

    prompt = sanitize_text(prompt)

    model_id = MODEL_MAP.get(model_alias, model_alias)

    if model_alias.startswith("imagen-") or model_alias in (
        "nano-banana", "nano-banana-ultra", "cheap", "ultra",
    ):
        print(
            f"[WARN] 레거시/제거된 별칭 '{model_alias}' → '{model_id}'로 자동 전환.",
            file=sys.stderr,
        )

    aspect_ratio = validate_ratio(aspect_ratio)

    # 해상도 기본값 자동 선택 (공식 문서 권장치)
    # Pro = 2K, 2 = 1K. 4K 등 다른 해상도는 호출자가 직접 스크립트 수정해서 사용.
    if model_id == "gemini-3.1-flash-image-preview":
        image_size = "1K"
    else:
        image_size = "2K"

    # REST API는 camelCase 사용 (Python SDK는 snake_case)
    # 참고: https://ai.google.dev/gemini-api/docs/image-generation
    image_config: dict[str, str] = {
        "aspectRatio": aspect_ratio,
        "imageSize": image_size,
    }

    payload: dict[str, object] = {
        "contents": [
            {
                "role": "user",
                "parts": [{"text": prompt}],
            }
        ],
        "generationConfig": {
            "responseModalities": ["TEXT", "IMAGE"],
            "imageConfig": image_config,
        },
    }

    url = BASE_URL.format(model=model_id, key=api_key)
    body = safe_json_encode(payload)
    req = urllib.request.Request(
        url,
        data=body,
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=DEFAULT_TIMEOUT) as resp:
            data = json.loads(resp.read())

        candidates = data.get("candidates", [])
        if not candidates:
            print(
                f"[ERROR] 빈 응답: {safe_json_dumps(data)[:300]}",
                file=sys.stderr,
            )
            return False

        # REST API는 camelCase (inlineData)를 반환하지만, 일부 SDK/gateway는
        # snake_case(inline_data)로 정규화할 수 있으므로 둘 다 확인
        parts = candidates[0].get("content", {}).get("parts", [])
        img_b64: str = ""
        for part in parts:
            inline = part.get("inlineData") or part.get("inline_data")
            if inline and inline.get("data"):
                img_b64 = inline["data"]
                break

        if not img_b64:
            finish = candidates[0].get("finishReason", "UNKNOWN")
            print(
                f"[ERROR] 이미지 데이터 없음 (finishReason={finish}). "
                "RAI 차단 또는 안전 정책 위반 가능성.",
                file=sys.stderr,
            )
            return False

        os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
        with open(output_path, "wb") as f:
            f.write(base64.b64decode(img_b64))

        size_kb = os.path.getsize(output_path) // 1024
        print(
            f"[OK] {output_path} ({size_kb}KB, {aspect_ratio}, "
            f"model={model_id}, size={image_size})"
        )
        return True

    except urllib.error.HTTPError as e:
        body_err = e.read().decode("utf-8", errors="replace")[:500]
        print(f"[ERROR] HTTP {e.code}: {body_err}", file=sys.stderr)
        return False
    except urllib.error.URLError as e:
        print(f"[ERROR] 네트워크 오류: {e.reason}", file=sys.stderr)
        return False
    except (OSError, ValueError, KeyError) as e:
        print(f"[ERROR] 예외 발생: {type(e).__name__}: {e}", file=sys.stderr)
        return False


def generate_batch(jobs: list[Job], output_dir: str = ".") -> dict[str, bool]:
    """
    여러 이미지를 순차 생성.
    jobs: [{"prompt": "...", "filename": "s01.png", "ratio": "3:4", "model": "nano-banana-pro"}]
    반환: {"s01.png": True/False, ...}
    """
    results: dict[str, bool] = {}
    total = len(jobs)
    for i, job in enumerate(jobs, 1):
        filename = job.get("filename", f"image_{i:02d}.png")
        path = os.path.join(output_dir, filename)
        ratio = job.get("ratio", "3:4")
        model = job.get("model", "nano-banana-pro")
        prompt = sanitize_text(job.get("prompt", ""))
        print(f"[{i}/{total}] 생성 중: {filename} ({ratio}, {model})")
        results[filename] = generate_image(prompt, path, ratio, model)
    return results


# ── CLI ────────────────────────────────────────────────────────────────────


def _cli() -> int:
    if len(sys.argv) < 3:
        print(__doc__)
        return 1

    _prompt = sys.argv[1]
    _output = sys.argv[2]
    _ratio = sys.argv[3] if len(sys.argv) > 3 else "3:4"
    _model = sys.argv[4] if len(sys.argv) > 4 else "nano-banana-pro"

    success = generate_image(_prompt, _output, _ratio, _model)
    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(_cli())
