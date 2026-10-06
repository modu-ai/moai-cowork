#!/usr/bin/env bash
set -eu
# 합성 치수 검증용 1×1 단색 PNG이며 실제 상품 사진이나 판매 증거가 아니다.
python3 - <<'PY'
import struct
import zlib
from pathlib import Path
root = Path("fixtures/sections")
root.mkdir(parents=True, exist_ok=True)
def chunk(kind, data):
    return struct.pack(">I", len(data)) + kind + data + struct.pack(">I", zlib.crc32(kind + data))
def pixel(color):
    return b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", 1, 1, 8, 2, 0, 0, 0)) + chunk(b"IDAT", zlib.compress(bytes([0, color, 0, 0]))) + chunk(b"IEND", b"")
names = ["01_hero", "02_pain", "03_problem", "04_story", "05_solution", "06_how", "07_proof", "08_authority", "09_benefits", "10_risk", "11_compare", "12_filter", "13_cta"]
for number, name in enumerate(names, 1):
    (root / (name + ".png")).write_bytes(pixel(number * 15))
PY
