# Based on seocholaw HWPX utilities (MIT License)
"""
HWPX 텍스트 추출 스크립트

HWPX(ZIP+XML OWPML 포맷) 파일에서 모든 섹션의 텍스트를 추출합니다.

사용법:
    python text_extract.py document.hwpx
    python text_extract.py document.hwpx --output extracted.txt
    python text_extract.py document.hwpx --sections 0 1 2
    python text_extract.py document.hwpx --separator "\\n---\\n"
"""

from __future__ import annotations

import argparse
import re
import sys
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Optional


# OWPML 네임스페이스
_HP_NS = "http://www.hancom.co.kr/hwpml/2016/HwpDoc"
_HP_TAG_P = f"{{{_HP_NS}}}p"
_HP_TAG_T = f"{{{_HP_NS}}}t"
_HP_TAG_LINEBREAK = f"{{{_HP_NS}}}br"


def _get_section_files(zf: zipfile.ZipFile) -> list[str]:
    """ZIP 내 section*.xml 파일 목록을 정렬하여 반환합니다."""
    pattern = re.compile(r"Contents/section(\d+)\.xml")
    sections = [(int(m.group(1)), name) for name in zf.namelist() if (m := pattern.match(name))]
    return [name for _, name in sorted(sections)]


def _extract_section_text(xml_data: bytes) -> str:
    """section XML 데이터에서 텍스트를 추출합니다."""
    try:
        root = ET.fromstring(xml_data)
    except ET.ParseError as e:
        return f"[XML 파싱 오류: {e}]"

    lines: list[str] = []
    for para in root.iter(_HP_TAG_P):
        parts: list[str] = []
        for child in para.iter():
            if child.tag == _HP_TAG_T and child.text:
                parts.append(child.text)
            elif child.tag == _HP_LINEBREAK:
                parts.append("\n")
        line = "".join(parts).rstrip()
        lines.append(line)

    return "\n".join(lines)


# 줄바꿈 태그 별칭 (네임스페이스 없을 수도 있음)
_HP_LINEBREAK = _HP_TAG_LINEBREAK


def extract_text(
    hwpx_path: str,
    section_indices: Optional[list[int]] = None,
    separator: str = "\n\n",
) -> str:
    """HWPX 파일에서 텍스트를 추출합니다.

    Args:
        hwpx_path: .hwpx 파일 경로
        section_indices: 추출할 섹션 인덱스 목록 (None이면 전체)
        separator: 섹션 간 구분자

    Returns:
        추출된 텍스트 문자열
    """
    path = Path(hwpx_path)
    if not path.exists():
        print(f"오류: 파일을 찾을 수 없습니다: {hwpx_path}", file=sys.stderr)
        sys.exit(1)

    if not zipfile.is_zipfile(str(path)):
        print(f"오류: 유효한 HWPX(ZIP) 파일이 아닙니다: {hwpx_path}", file=sys.stderr)
        sys.exit(1)

    section_texts: list[str] = []

    with zipfile.ZipFile(str(path), "r") as zf:
        section_files = _get_section_files(zf)
        if not section_files:
            print("경고: 섹션 파일을 찾을 수 없습니다.", file=sys.stderr)
            return ""

        # 인덱스 필터 적용
        if section_indices is not None:
            selected = []
            for idx in section_indices:
                if 0 <= idx < len(section_files):
                    selected.append(section_files[idx])
                else:
                    print(f"경고: 섹션 인덱스 {idx}가 범위를 벗어났습니다 (전체: {len(section_files)}개).",
                          file=sys.stderr)
        else:
            selected = section_files

        for sf in selected:
            try:
                data = zf.read(sf)
            except KeyError:
                print(f"경고: {sf} 읽기 실패.", file=sys.stderr)
                continue
            text = _extract_section_text(data)
            section_texts.append(text)

    return separator.join(section_texts)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="HWPX 파일 텍스트 추출기",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("hwpx", help="입력 .hwpx 파일 경로")
    parser.add_argument("--output", "-o", default=None, help="출력 파일 경로 (기본: stdout)")
    parser.add_argument(
        "--sections", "-s",
        nargs="+",
        type=int,
        default=None,
        metavar="N",
        help="추출할 섹션 인덱스 (기본: 전체, 예: --sections 0 1)",
    )
    parser.add_argument(
        "--separator",
        default="\n\n",
        help="섹션 간 구분자 (기본: 빈 줄)",
    )

    args = parser.parse_args()

    text = extract_text(args.hwpx, args.sections, args.separator)

    if args.output:
        Path(args.output).write_text(text, encoding="utf-8")
        print(f"저장 완료: {args.output} ({len(text):,} 글자)")
    else:
        sys.stdout.write(text)
        if text and not text.endswith("\n"):
            sys.stdout.write("\n")


if __name__ == "__main__":
    main()
