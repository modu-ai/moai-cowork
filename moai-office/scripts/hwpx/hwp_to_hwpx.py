# Based on seocholaw HWPX utilities (MIT License)
"""
HWP -> HWPX 변환 스크립트 (최선 노력 변환)

구형 HWP 바이너리 파일을 HWPX(ZIP+OWPML XML) 형식으로 변환합니다.
완전한 서식 보존은 한컴오피스가 필요합니다.
이 스크립트는 텍스트 콘텐츠와 기본 구조만 변환합니다.

사용법:
    python hwp_to_hwpx.py input.hwp
    python hwp_to_hwpx.py input.hwp --output output.hwpx
    python hwp_to_hwpx.py input.hwp --verbose

의존성 (선택):
    pip install olefile  # 정확한 텍스트 추출에 필요
"""

from __future__ import annotations

import argparse
import sys
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Optional

# hwp_text_extract 모듈에서 텍스트 추출 재사용
sys.path.insert(0, str(Path(__file__).parent))
try:
    from hwp_text_extract import extract_text as _extract_hwp_text
except ImportError:
    def _extract_hwp_text(path: str, encoding: str = "cp949") -> str:  # type: ignore[misc]
        """hwp_text_extract 모듈 없이 텍스트 추출 불가."""
        raise ImportError("hwp_text_extract.py 가 같은 디렉토리에 있어야 합니다.")


# ---------------------------------------------------------------------------
# OWPML XML 빌더
# ---------------------------------------------------------------------------

def _escape_xml(text: str) -> str:
    """XML 특수문자를 이스케이프합니다."""
    return (
        text.replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;")
            .replace("'", "&apos;")
    )


def _build_section_xml(paragraphs: list[str]) -> str:
    """본문 단락 목록으로 section0.xml을 생성합니다."""
    para_parts: list[str] = []
    for para in paragraphs:
        escaped = _escape_xml(para)
        para_parts.append(
            f"    <hp:p>\n"
            f"        <hp:run>\n"
            f"            <hp:t>{escaped}</hp:t>\n"
            f"        </hp:run>\n"
            f"    </hp:p>"
        )
    body = "\n".join(para_parts)
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<hp:sec xmlns:hp="http://www.hancom.co.kr/hwpml/2016/HwpDoc">\n'
        f"{body}\n"
        "</hp:sec>"
    )


def _build_header_xml(title: str = "") -> str:
    """기본 header.xml을 생성합니다."""
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<hp:head xmlns:hp="http://www.hancom.co.kr/hwpml/2016/HwpDoc">\n'
        "    <hp:docSetting>\n"
        '        <hp:paperSize width="59528" height="84188"/>\n'
        '        <hp:paperMargin left="8504" right="8504" top="5668" bottom="4252"\n'
        '                        header="4252" footer="4252" gutter="0"/>\n'
        "    </hp:docSetting>\n"
        "    <hp:fontfaces>\n"
        '        <hp:fontface lang="Korean" name="맑은 고딕"/>\n'
        '        <hp:fontface lang="Latin" name="Arial"/>\n'
        "    </hp:fontfaces>\n"
        "</hp:head>"
    )


def _build_container_xml() -> str:
    """META-INF/container.xml을 생성합니다."""
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<container xmlns="urn:oasis:names:tc:opendocument:xmlns:container">\n'
        "    <rootfiles>\n"
        '        <rootfile full-path="Contents/content.hpf"'
        ' media-type="application/hwp+zip"/>\n'
        "    </rootfiles>\n"
        "</container>"
    )


def _build_content_hpf(section_count: int = 1) -> str:
    """Contents/content.hpf OPF 매니페스트를 생성합니다."""
    items = "\n".join(
        f'        <item id="section{i}" href="section{i}.xml"'
        f' media-type="application/xml"/>'
        for i in range(section_count)
    )
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<package xmlns="http://www.idpf.org/2007/opf" version="3.0">\n'
        "    <manifest>\n"
        '        <item id="header" href="header.xml" media-type="application/xml"/>\n'
        f"{items}\n"
        "    </manifest>\n"
        "    <spine>\n"
        + "\n".join(
            f'        <itemref idref="section{i}"/>' for i in range(section_count)
        )
        + "\n    </spine>\n"
        "</package>"
    )


# ---------------------------------------------------------------------------
# 변환 메인 로직
# ---------------------------------------------------------------------------

def convert(hwp_path: str, output_path: Optional[str] = None, verbose: bool = False) -> str:
    """HWP 파일을 HWPX로 변환합니다.

    Args:
        hwp_path: 입력 .hwp 파일 경로
        output_path: 출력 .hwpx 파일 경로 (None이면 자동 생성)
        verbose: 진행 상황 출력 여부

    Returns:
        생성된 .hwpx 파일 경로
    """
    src = Path(hwp_path)
    if not src.exists():
        print(f"오류: 파일을 찾을 수 없습니다: {hwp_path}", file=sys.stderr)
        sys.exit(1)

    dst = Path(output_path) if output_path else src.with_suffix(".hwpx")

    if verbose:
        print(f"입력: {src}")
        print(f"출력: {dst}")
        print("텍스트 추출 중...")

    # 텍스트 추출
    raw_text = _extract_hwp_text(str(src))
    paragraphs = [line for line in raw_text.splitlines() if line.strip()]

    if verbose:
        print(f"추출된 단락 수: {len(paragraphs)}")
        print("HWPX 빌드 중...")

    # HWPX ZIP 생성
    section_xml = _build_section_xml(paragraphs)
    header_xml = _build_header_xml(title=src.stem)
    container_xml = _build_container_xml()
    content_hpf = _build_content_hpf(section_count=1)

    with zipfile.ZipFile(str(dst), "w", zipfile.ZIP_DEFLATED) as zf:
        # mimetype은 압축 없이 첫 번째 엔트리로 추가 (HWPX 규격)
        zf.writestr(
            zipfile.ZipInfo("mimetype"),
            "application/hwp+zip",
        )
        zf.writestr("META-INF/container.xml", container_xml)
        zf.writestr("Contents/content.hpf", content_hpf)
        zf.writestr("Contents/header.xml", header_xml)
        zf.writestr("Contents/section0.xml", section_xml)

    size = dst.stat().st_size
    if verbose:
        print(f"변환 완료: {dst} ({size:,} bytes)")
        print()
        print("주의: 이 변환은 최선 노력(best-effort) 방식입니다.")
        print("  - 텍스트 콘텐츠만 보존됩니다.")
        print("  - 표, 이미지, 서식 등은 손실될 수 있습니다.")
        print("  - 완전한 변환은 한컴오피스를 사용하세요.")
    else:
        print(f"변환 완료: {dst}")

    return str(dst)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="HWP -> HWPX 변환기 (최선 노력 텍스트 보존)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("hwp", help="입력 .hwp 파일 경로")
    parser.add_argument("--output", "-o", default=None, help="출력 .hwpx 파일 경로")
    parser.add_argument("--verbose", "-v", action="store_true", help="상세 출력")

    args = parser.parse_args()
    convert(args.hwp, args.output, args.verbose)


if __name__ == "__main__":
    main()
