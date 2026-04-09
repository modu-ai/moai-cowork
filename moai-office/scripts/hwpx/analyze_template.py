# Based on seocholaw HWPX utilities (MIT License)
"""
HWPX 템플릿 분석 스크립트

.hwpx 파일(ZIP+XML 구조)을 열어 섹션, 스타일, 플레이스홀더,
폰트, 페이지 설정 등 템플릿 구조를 요약해 출력합니다.

사용법:
    python analyze_template.py template.hwpx
    python analyze_template.py template.hwpx --json
    python analyze_template.py template.hwpx --output report.txt
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any


# OWPML 네임스페이스
NAMESPACES: dict[str, str] = {
    "hp": "http://www.hancom.co.kr/hwpml/2016/HwpDoc",
    "hc": "http://www.hancom.co.kr/hwpml/2016/HwpChar",
    "hs": "http://www.hancom.co.kr/hwpml/2016/HwpStyle",
    "hpf": "http://www.idpf.org/2007/opf",
}

# 플레이스홀더 패턴 ({{변수명}} 또는 {변수명})
PLACEHOLDER_RE = re.compile(r"\{\{?\s*(\w+)\s*\}?\}")


def _ns(tag: str, ns: str = "hp") -> str:
    """네임스페이스 프리픽스를 확장합니다."""
    return f"{{{NAMESPACES[ns]}}}{tag}"


def list_zip_entries(zf: zipfile.ZipFile) -> list[str]:
    """ZIP 내부 파일 목록을 반환합니다."""
    return sorted(zf.namelist())


def parse_header(zf: zipfile.ZipFile) -> dict[str, Any]:
    """header.xml 에서 폰트/페이지 설정을 파싱합니다."""
    result: dict[str, Any] = {"fonts": [], "page_setup": {}}
    try:
        data = zf.read("Contents/header.xml")
    except KeyError:
        return result

    try:
        root = ET.fromstring(data)
    except ET.ParseError:
        return result

    # 폰트 수집
    for ff in root.iter(_ns("fontface")):
        lang = ff.get("lang", "")
        name = ff.get("name", "")
        if name:
            result["fonts"].append({"lang": lang, "name": name})

    # 용지 크기/여백
    paper = root.find(f".//{_ns('paperSize')}")
    if paper is not None:
        result["page_setup"]["paper_size"] = {
            "width": paper.get("width"),
            "height": paper.get("height"),
        }
    margin = root.find(f".//{_ns('paperMargin')}")
    if margin is not None:
        result["page_setup"]["margin"] = dict(margin.attrib)

    return result


def parse_styles(zf: zipfile.ZipFile) -> list[str]:
    """header.xml 의 스타일 이름 목록을 반환합니다."""
    styles: list[str] = []
    try:
        data = zf.read("Contents/header.xml")
    except KeyError:
        return styles

    try:
        root = ET.fromstring(data)
    except ET.ParseError:
        return styles

    for style in root.iter(_ns("style")):
        name = style.get("name") or style.get("val")
        if name and name not in styles:
            styles.append(name)

    return styles


def parse_sections(zf: zipfile.ZipFile) -> list[dict[str, Any]]:
    """section*.xml 파일들을 파싱하여 섹션 정보를 반환합니다."""
    sections: list[dict[str, Any]] = []
    section_files = [n for n in zf.namelist() if re.match(r"Contents/section\d+\.xml", n)]
    section_files.sort()

    for sf in section_files:
        try:
            data = zf.read(sf)
            root = ET.fromstring(data)
        except (KeyError, ET.ParseError):
            sections.append({"file": sf, "paragraphs": 0, "error": True})
            continue

        # 단락 수 집계
        para_count = sum(1 for _ in root.iter(_ns("p")))

        # 플레이스홀더 탐색
        placeholders: list[str] = []
        for t_elem in root.iter(_ns("t")):
            if t_elem.text:
                for m in PLACEHOLDER_RE.finditer(t_elem.text):
                    ph = m.group(1)
                    if ph not in placeholders:
                        placeholders.append(ph)

        sections.append({
            "file": sf,
            "paragraphs": para_count,
            "placeholders": placeholders,
        })

    return sections


def analyze(hwpx_path: str) -> dict[str, Any]:
    """HWPX 파일을 분석하고 구조 요약 딕셔너리를 반환합니다."""
    path = Path(hwpx_path)
    if not path.exists():
        print(f"오류: 파일을 찾을 수 없습니다: {hwpx_path}", file=sys.stderr)
        sys.exit(1)

    if not zipfile.is_zipfile(str(path)):
        print(f"오류: 유효한 ZIP/HWPX 파일이 아닙니다: {hwpx_path}", file=sys.stderr)
        sys.exit(1)

    result: dict[str, Any] = {
        "file": str(path.resolve()),
        "size_bytes": path.stat().st_size,
        "entries": [],
        "sections": [],
        "styles": [],
        "fonts": [],
        "page_setup": {},
        "all_placeholders": [],
    }

    with zipfile.ZipFile(str(path), "r") as zf:
        result["entries"] = list_zip_entries(zf)
        header_info = parse_header(zf)
        result["fonts"] = header_info["fonts"]
        result["page_setup"] = header_info["page_setup"]
        result["styles"] = parse_styles(zf)
        result["sections"] = parse_sections(zf)

    # 전체 플레이스홀더 통합
    all_ph: list[str] = []
    for sec in result["sections"]:
        for ph in sec.get("placeholders", []):
            if ph not in all_ph:
                all_ph.append(ph)
    result["all_placeholders"] = all_ph

    return result


def print_text_report(info: dict[str, Any]) -> None:
    """분석 결과를 사람이 읽기 쉬운 텍스트로 출력합니다."""
    print(f"=== HWPX 템플릿 분석 보고서 ===")
    print(f"파일: {info['file']}")
    print(f"크기: {info['size_bytes']:,} bytes")
    print()

    print(f"[ZIP 엔트리] ({len(info['entries'])}개)")
    for e in info["entries"]:
        print(f"  - {e}")
    print()

    print(f"[섹션] ({len(info['sections'])}개)")
    for sec in info["sections"]:
        ph_str = ", ".join(sec.get("placeholders", [])) or "(없음)"
        print(f"  {sec['file']}: 단락 {sec.get('paragraphs', 0)}개, 플레이스홀더: {ph_str}")
    print()

    print(f"[스타일] ({len(info['styles'])}개)")
    for s in info["styles"]:
        print(f"  - {s}")
    print()

    print(f"[폰트] ({len(info['fonts'])}개)")
    for f in info["fonts"]:
        print(f"  - {f['lang']}: {f['name']}")
    print()

    ps = info.get("page_setup", {})
    if ps:
        print("[페이지 설정]")
        if "paper_size" in ps:
            sz = ps["paper_size"]
            print(f"  용지: {sz.get('width')} x {sz.get('height')} (HWPX 단위)")
        if "margin" in ps:
            m = ps["margin"]
            print(f"  여백: 좌{m.get('left')} 우{m.get('right')} 상{m.get('top')} 하{m.get('bottom')}")
        print()

    print(f"[플레이스홀더 전체] ({len(info['all_placeholders'])}개)")
    if info["all_placeholders"]:
        print("  " + ", ".join(info["all_placeholders"]))
    else:
        print("  (없음)")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="HWPX 템플릿 파일 구조 분석기",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("hwpx", help="분석할 .hwpx 파일 경로")
    parser.add_argument("--json", action="store_true", help="JSON 형식으로 출력")
    parser.add_argument("--output", "-o", default=None, help="결과를 파일로 저장")

    args = parser.parse_args()
    info = analyze(args.hwpx)

    if args.json:
        text = json.dumps(info, ensure_ascii=False, indent=2)
    else:
        import io
        buf = io.StringIO()
        _orig = sys.stdout
        sys.stdout = buf
        print_text_report(info)
        sys.stdout = _orig
        text = buf.getvalue()

    if args.output:
        Path(args.output).write_text(text, encoding="utf-8")
        print(f"결과 저장 완료: {args.output}")
    else:
        print(text)


if __name__ == "__main__":
    main()
