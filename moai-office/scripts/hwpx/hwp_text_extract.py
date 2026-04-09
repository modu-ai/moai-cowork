# Based on seocholaw HWPX utilities (MIT License)
"""
HWP(구형 바이너리) 텍스트 추출 스크립트

한컴 HWP 5.x 구형 바이너리 포맷(.hwp)에서 텍스트를 추출합니다.
HWPX(ZIP+XML)와 달리 HWP는 독점 OLE2 복합 문서 포맷입니다.

사용법:
    python hwp_text_extract.py document.hwp
    python hwp_text_extract.py document.hwp --output extracted.txt
    python hwp_text_extract.py document.hwp --encoding cp949

의존성 (선택):
    pip install olefile          # OLE2 파싱용 (권장)

olefile 미설치 시 heuristic 바이트 스캔 폴백을 사용합니다.
"""

from __future__ import annotations

import argparse
import os
import struct
import sys
from pathlib import Path
from typing import Optional


# HWP5 파일 시그니처
HWP5_SIGNATURE = b"\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1"  # OLE2 헤더


def _check_hwp_signature(path: str) -> bool:
    """HWP5 OLE2 시그니처를 확인합니다."""
    try:
        with open(path, "rb") as f:
            header = f.read(8)
        return header == HWP5_SIGNATURE
    except OSError:
        return False


# ---------------------------------------------------------------------------
# olefile 기반 추출 (정확도 높음)
# ---------------------------------------------------------------------------

def _extract_with_olefile(path: str) -> str:
    """olefile 라이브러리를 사용하여 HWP 텍스트를 추출합니다."""
    import olefile  # type: ignore[import]

    texts: list[str] = []
    ole = olefile.OleFileIO(path)

    # HWP BodyText 스트림 탐색
    for entry in ole.listdir():
        entry_path = "/".join(entry)
        # BodyText/Section* 스트림에 본문 데이터가 있음
        if entry[0] == "BodyText" and len(entry) == 2:
            try:
                stream = ole.openstream(entry)
                raw = stream.read()
                text = _parse_hwp_body_stream(raw)
                if text:
                    texts.append(text)
            except Exception:
                pass

    ole.close()
    return "\n".join(texts)


def _parse_hwp_body_stream(data: bytes) -> str:
    """HWP BodyText 스트림 바이너리에서 텍스트를 파싱합니다."""
    import zlib

    # HWP Body 스트림은 zlib 압축됨 (일반적으로)
    try:
        # 처음 4바이트는 압축 전 크기
        uncompressed = zlib.decompress(data, -zlib.MAX_WBITS)
    except zlib.error:
        # 비압축 스트림
        uncompressed = data

    texts: list[str] = []
    i = 0
    while i + 4 <= len(uncompressed):
        # HWP 레코드 헤더: 32비트
        header = struct.unpack_from("<I", uncompressed, i)[0]
        tag_id = header & 0x3FF          # 하위 10비트
        level = (header >> 10) & 0x3FF  # 다음 10비트
        size = (header >> 20) & 0xFFF   # 상위 12비트

        if size == 0xFFF:
            # 크기가 4096 이상이면 다음 4바이트에 실제 크기
            if i + 8 > len(uncompressed):
                break
            size = struct.unpack_from("<I", uncompressed, i + 4)[0]
            i += 8
        else:
            i += 4

        if i + size > len(uncompressed):
            break

        # tag_id 67 = HWPTAG_PARA_TEXT (단락 텍스트)
        if tag_id == 67:
            chunk = uncompressed[i:i + size]
            # UTF-16LE 디코딩
            try:
                text = chunk.decode("utf-16-le", errors="replace")
                # 제어 문자(0x0000-0x001F) 제거 (일부 레이아웃 코드)
                clean = "".join(c for c in text if c >= " " or c in "\n\t")
                if clean.strip():
                    texts.append(clean)
            except Exception:
                pass

        i += size

    return "\n".join(texts)


# ---------------------------------------------------------------------------
# 폴백: 휴리스틱 바이트 스캔
# ---------------------------------------------------------------------------

def _extract_heuristic(path: str, encoding: str = "cp949") -> str:
    """olefile 없이 바이너리에서 한글 텍스트를 휴리스틱으로 추출합니다.

    주의: 이 방법은 불완전합니다. 일부 본문만 추출될 수 있습니다.
    """
    texts: list[str] = []
    with open(path, "rb") as f:
        raw = f.read()

    # UTF-16LE 한글 범위(가-힣) 연속 시퀀스 탐색
    i = 0
    buffer: list[int] = []
    while i + 1 < len(raw):
        lo, hi = raw[i], raw[i + 1]
        # 한글 완성형: U+AC00-D7A3 (UTF-16LE에서 hi byte 0xAC-0xD7)
        # 기본 라틴: U+0020-007E
        code = lo | (hi << 8)
        if (0xAC00 <= code <= 0xD7A3) or (0x0020 <= code <= 0x007E) or code in (0x000A, 0x0009):
            buffer.append(lo)
            buffer.append(hi)
        else:
            if len(buffer) >= 4:
                try:
                    text = bytes(buffer).decode("utf-16-le", errors="replace").strip()
                    if text:
                        texts.append(text)
                except Exception:
                    pass
            buffer = []
        i += 2

    return "\n".join(t for t in texts if len(t) > 1)


# ---------------------------------------------------------------------------
# 공개 인터페이스
# ---------------------------------------------------------------------------

def extract_text(hwp_path: str, encoding: str = "cp949") -> str:
    """HWP 파일에서 텍스트를 추출합니다.

    Args:
        hwp_path: .hwp 파일 경로
        encoding: 폴백 인코딩 (기본: cp949)

    Returns:
        추출된 텍스트 문자열
    """
    path = Path(hwp_path)
    if not path.exists():
        print(f"오류: 파일을 찾을 수 없습니다: {hwp_path}", file=sys.stderr)
        sys.exit(1)

    if not _check_hwp_signature(str(path)):
        print(f"경고: HWP5 시그니처가 없습니다. 계속 진행합니다.", file=sys.stderr)

    try:
        import olefile  # type: ignore[import]  # noqa: F401
        return _extract_with_olefile(str(path))
    except ImportError:
        print(
            "경고: olefile 미설치. 휴리스틱 모드로 텍스트 추출합니다.\n"
            "  pip install olefile  # 정확한 추출을 위해 권장",
            file=sys.stderr,
        )
        return _extract_heuristic(str(path), encoding)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="HWP(구형 바이너리) 텍스트 추출기",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("hwp", help="입력 .hwp 파일 경로")
    parser.add_argument("--output", "-o", default=None, help="출력 파일 경로 (기본: stdout)")
    parser.add_argument("--encoding", default="cp949", help="폴백 인코딩 (기본: cp949)")

    args = parser.parse_args()
    text = extract_text(args.hwp, args.encoding)

    if args.output:
        Path(args.output).write_text(text, encoding="utf-8")
        print(f"저장 완료: {args.output} ({len(text):,} 글자)")
    else:
        sys.stdout.write(text)
        if not text.endswith("\n"):
            sys.stdout.write("\n")


if __name__ == "__main__":
    main()
