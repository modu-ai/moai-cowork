"""HWPX 양식 채우기 도구 (python-hwpx 기반)

기존 HWPX 양식 파일을 열어 표 셀의 값을 채우고 저장합니다.
원본 레이아웃(표 구조, 서식, 페이지 설정)을 100% 보존합니다.

의존성: pip install python-hwpx

Usage:
    # 라벨 기반 채우기 (fill_by_path)
    python fill_template.py --template 양식.hwpx --output 결과.hwpx \\
        --fill "과제명 > right=AgentOS" "주관기관 > right=모두의AI"

    # JSON 데이터 파일로 채우기
    python fill_template.py --template 양식.hwpx --output 결과.hwpx \\
        --data values.json

    # 플레이스홀더 치환 (ZIP 레벨)
    python fill_template.py --template 양식.hwpx --output 결과.hwpx \\
        --replace "{과제명}=AgentOS" "{주관기관}=모두의AI"

    # 양식 분석 (라벨 목록 출력)
    python fill_template.py --template 양식.hwpx --analyze
"""

import argparse
import json
import sys
import zipfile
from pathlib import Path

# python-hwpx 의존성
try:
    from hwpx import HwpxDocument
    # lxml 호환 패치
    try:
        import lxml.etree as _lxml_ET
        import hwpx.oxml.document as _oxdoc
        _oxdoc.ET = _lxml_ET
    except ImportError:
        pass
    HAS_HWPX = True
except ImportError:
    HAS_HWPX = False


def analyze_template(template_path: str) -> tuple[bool, str]:
    """양식의 표 구조와 라벨 목록을 분석합니다."""
    if not HAS_HWPX:
        return False, "Error: python-hwpx가 필요합니다. pip install python-hwpx"

    try:
        doc = HwpxDocument.open(template_path)

        lines = [f"=== 양식 분석: {template_path} ===\n"]

        # 표 목록
        table_map = doc.get_table_map()
        tables = table_map.get("tables", []) if isinstance(table_map, dict) else table_map
        lines.append(f"표 수: {len(tables)}개\n")
        for i, t in enumerate(tables):
            rows = t.get("rows", "?") if isinstance(t, dict) else "?"
            cols = t.get("cols", "?") if isinstance(t, dict) else "?"
            header = t.get("header_text", "") if isinstance(t, dict) else ""
            preview = f" — {header}" if header else ""
            lines.append(f"  T{i}: {rows}x{cols}{preview}")

        # 단락 수
        paras = doc.paragraphs if isinstance(doc.paragraphs, list) else list(doc.paragraphs)
        lines.append(f"\n단락 수: {len(paras)}개\n")

        # 라벨 셀 탐색 (일반적인 양식 라벨 패턴)
        lines.append("=== 감지된 라벨 셀 ===\n")
        common_labels = [
            "과제명", "주관기관", "성명", "소속", "직위", "연락처",
            "사업자번호", "대표자", "주소", "사업비", "총사업비",
            "연구기간", "참여인원", "이메일", "전화번호",
        ]
        found = []
        for label in common_labels:
            result = doc.find_cell_by_label(label)
            if result and result.get("count", 0) > 0:
                found.append(label)
                lines.append(f"  '{label}' — {result['count']}건")

        if not found:
            lines.append("  (일반 라벨 미감지 — 표 셀 내용을 직접 확인하세요)")

        # 텍스트 미리보기
        lines.append("\n=== 본문 미리보기 (첫 20줄) ===\n")
        text = doc.export_text()
        for i, line in enumerate(text.split("\n")[:20]):
            if line.strip():
                lines.append(f"  {i+1}: {line.strip()[:80]}")

        doc.close()
        return True, "\n".join(lines)

    except Exception as e:
        return False, f"Error: 분석 실패 — {e}"


def fill_by_labels(
    template_path: str,
    output_path: str,
    fill_data: dict[str, str],
) -> tuple[bool, str]:
    """라벨 기반으로 양식 표 셀을 채웁니다 (fill_by_path)."""
    if not HAS_HWPX:
        return False, "Error: python-hwpx가 필요합니다. pip install python-hwpx"

    try:
        doc = HwpxDocument.open(template_path)
        doc.fill_by_path(fill_data)

        out = Path(output_path)
        out.parent.mkdir(parents=True, exist_ok=True)
        doc.save_to_path(str(out))
        doc.close()

        size_kb = out.stat().st_size / 1024
        return True, (
            f"Created {output_path}\n"
            f"  {len(fill_data)}개 셀 채움, {size_kb:.1f} KB\n"
            f"  원본 레이아웃 보존"
        )
    except Exception as e:
        return False, f"Error: 양식 채우기 실패 — {e}"


def replace_placeholders(
    template_path: str,
    output_path: str,
    replacements: dict[str, str],
) -> tuple[bool, str]:
    """ZIP 레벨에서 플레이스홀더를 치환합니다 (서식 100% 보존)."""
    try:
        from xml.sax.saxutils import escape

        template = Path(template_path)
        out = Path(output_path)
        out.parent.mkdir(parents=True, exist_ok=True)

        count = 0
        with zipfile.ZipFile(template, 'r') as zin:
            with zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED) as zout:
                for item in zin.infolist():
                    data = zin.read(item.filename)

                    # mimetype은 비압축
                    if item.filename == 'mimetype':
                        zout.writestr(item, data, compress_type=zipfile.ZIP_STORED)
                        continue

                    # XML 파일만 치환 대상
                    if item.filename.endswith(('.xml', '.hpf')):
                        text = data.decode('utf-8')
                        for old, new in replacements.items():
                            if old in text:
                                text = text.replace(old, escape(new))
                                count += 1
                        zout.writestr(item, text.encode('utf-8'))
                    else:
                        zout.writestr(item, data)

        size_kb = out.stat().st_size / 1024
        return True, (
            f"Created {output_path}\n"
            f"  {count}건 치환, {size_kb:.1f} KB\n"
            f"  ZIP 레벨 치환 — 서식 100% 보존"
        )
    except Exception as e:
        return False, f"Error: 치환 실패 — {e}"


def main():
    parser = argparse.ArgumentParser(
        description="HWPX 양식을 채우거나 분석합니다 (원본 레이아웃 보존)"
    )
    parser.add_argument("--template", "-t", required=True,
                        help="원본 HWPX 양식 파일")
    parser.add_argument("--output", "-o",
                        help="출력 HWPX 파일 경로")
    parser.add_argument("--analyze", action="store_true",
                        help="양식 구조 분석 (표/라벨/단락 목록)")
    parser.add_argument("--fill", nargs="+",
                        help='라벨 기반 채우기: "라벨 > right=값"')
    parser.add_argument("--replace", nargs="+",
                        help='플레이스홀더 치환: "{플레이스홀더}=값"')
    parser.add_argument("--data",
                        help="JSON 데이터 파일 (fill_by_path용)")

    args = parser.parse_args()

    # 분석 모드
    if args.analyze:
        success, msg = analyze_template(args.template)
        print(msg)
        sys.exit(0 if success else 1)

    # 출력 필수
    if not args.output:
        print("Error: --output 필요 (--analyze 제외)", file=sys.stderr)
        sys.exit(1)

    # 라벨 기반 채우기
    if args.fill:
        data = {}
        for item in args.fill:
            if "=" in item:
                k, v = item.split("=", 1)
                data[k.strip()] = v.strip()
        success, msg = fill_by_labels(args.template, args.output, data)
        print(msg)
        sys.exit(0 if success else 1)

    # JSON 데이터
    if args.data:
        try:
            with open(args.data, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except Exception as e:
            print(f"Error: JSON 파일 읽기 실패 — {e}", file=sys.stderr)
            sys.exit(1)
        success, msg = fill_by_labels(args.template, args.output, data)
        print(msg)
        sys.exit(0 if success else 1)

    # 플레이스홀더 치환
    if args.replace:
        replacements = {}
        for item in args.replace:
            if "=" in item:
                k, v = item.split("=", 1)
                replacements[k.strip()] = v.strip()
        success, msg = replace_placeholders(args.template, args.output, replacements)
        print(msg)
        sys.exit(0 if success else 1)

    print("Error: --analyze, --fill, --replace, --data 중 하나 지정", file=sys.stderr)
    sys.exit(1)


if __name__ == "__main__":
    main()
