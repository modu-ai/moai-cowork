"""HWPX 파일 생성 도구

텍스트 내용으로 새 HWPX 파일을 생성합니다.

Usage:
    python create_hwpx.py --output <output.hwpx> --title "제목" --body "본문"
    python create_hwpx.py --output <output.hwpx> --paragraphs "단락1" "단락2" "단락3"
    python create_hwpx.py --output <output.hwpx> --input-file content.txt

Examples:
    python create_hwpx.py --output report.hwpx --title "월간 보고서" --body "내용입니다."
    python create_hwpx.py --output letter.hwpx --paragraphs "안녕하세요." "본문입니다." "감사합니다."
    python create_hwpx.py --output doc.hwpx --input-file paragraphs.txt
"""

import argparse
import sys
import zipfile
from pathlib import Path
from xml.sax.saxutils import escape


# OWPML 네임스페이스
HP = 'http://www.hancom.co.kr/hwpml/2011/paragraph'
HS = 'http://www.hancom.co.kr/hwpml/2011/section'
HH = 'http://www.hancom.co.kr/hwpml/2011/head'
HC = 'http://www.hancom.co.kr/hwpml/2011/core'
HV = 'urn:hancom:office:hwpml:version'
ODF = 'urn:oasis:names:tc:opendocument:xmlns:manifest:1.0'


def build_paragraph_xml(text: str, is_title: bool = False) -> str:
    """단일 단락의 XML을 생성합니다."""
    safe_text = escape(text)
    char_pr_id = "1" if is_title else "0"
    para_pr_id = "1" if is_title else "0"
    return f'''    <hp:p paraPrIDRef="{para_pr_id}" styleIDRef="0">
      <hp:run charPrIDRef="{char_pr_id}">
        <hp:t>{safe_text}</hp:t>
      </hp:run>
    </hp:p>'''


def create_hwpx(
    output_path: str,
    paragraphs: list[str],
    title: str = "",
    font_hangul: str = "함초롬돋움",
    font_latin: str = "함초롬돋움",
    font_size: int = 1000,
    title_font_size: int = 1600,
    page_width: int = 59528,
    page_height: int = 84188,
    margin_left: int = 4252,
    margin_right: int = 4252,
    margin_top: int = 5669,
    margin_bottom: int = 4252,
    margin_header: int = 4252,
    margin_footer: int = 4252,
) -> tuple[bool, str]:
    """HWPX 파일을 생성합니다.

    Args:
        output_path: 출력 파일 경로
        paragraphs: 단락 텍스트 목록
        title: 제목 (별도 서식 적용)
        font_hangul: 한글 기본 글꼴명
        font_latin: 영문 기본 글꼴명
        font_size: 본문 글꼴 크기 (1/100 pt, 기본 1000 = 10pt)
        title_font_size: 제목 글꼴 크기 (1/100 pt, 기본 1600 = 16pt)
        page_width: 용지 너비 (hwpunit, A4: 59528)
        page_height: 용지 높이 (hwpunit, A4: 84188)

    Returns:
        (success, message)
    """
    if not paragraphs and not title:
        return False, "Error: 최소 한 개의 단락이 필요합니다"

    out = Path(output_path)
    if out.suffix.lower() != '.hwpx':
        return False, "Error: 출력 파일은 .hwpx 확장자여야 합니다"

    # 제목 + 본문 단락 XML 생성
    para_parts = []
    if title:
        para_parts.append(build_paragraph_xml(title, is_title=True))
    for p in paragraphs:
        para_parts.append(build_paragraph_xml(p, is_title=False))
    para_xml = '\n'.join(para_parts)

    mimetype = 'application/hwp+zip'

    version_xml = f'''<?xml version="1.0" encoding="UTF-8"?>
<hv:HWPVersion xmlns:hv="{HV}"
  major="1" minor="1" micro="0" buildNumber="0"/>'''

    manifest_xml = f'''<?xml version="1.0" encoding="UTF-8"?>
<odf:manifest xmlns:odf="{ODF}">
  <odf:file-entry odf:full-path="/" odf:media-type="application/hwp+zip"/>
  <odf:file-entry odf:full-path="version.xml" odf:media-type="text/xml"/>
  <odf:file-entry odf:full-path="Contents/content.hpf" odf:media-type="text/xml"/>
  <odf:file-entry odf:full-path="Contents/header.xml" odf:media-type="text/xml"/>
  <odf:file-entry odf:full-path="Contents/section0.xml" odf:media-type="text/xml"/>
</odf:manifest>'''

    content_hpf = f'''<?xml version="1.0" encoding="UTF-8"?>
<hc:package xmlns:hc="{HC}">
  <hc:head href="Contents/header.xml"/>
  <hc:body>
    <hc:section href="Contents/section0.xml"/>
  </hc:body>
</hc:package>'''

    header_xml = f'''<?xml version="1.0" encoding="UTF-8"?>
<hh:head xmlns:hh="{HH}" xmlns:hp="{HP}">
  <hh:beginNum page="1" footnote="1" endnote="1"/>
  <hh:refList>
    <hh:fontfaces>
      <hh:fontface lang="HANGUL">
        <hp:font id="0" face="{escape(font_hangul)}" type="TTF"/>
      </hh:fontface>
      <hh:fontface lang="LATIN">
        <hp:font id="0" face="{escape(font_latin)}" type="TTF"/>
      </hh:fontface>
      <hh:fontface lang="HANJA">
        <hp:font id="0" face="{escape(font_hangul)}" type="TTF"/>
      </hh:fontface>
    </hh:fontfaces>
    <hh:borderFills>
      <hh:borderFill id="1">
        <hh:slash type="NONE"/>
        <hh:backSlash type="NONE"/>
        <hh:leftBorder type="NONE" width="0.1mm" color="#000000"/>
        <hh:rightBorder type="NONE" width="0.1mm" color="#000000"/>
        <hh:topBorder type="NONE" width="0.1mm" color="#000000"/>
        <hh:bottomBorder type="NONE" width="0.1mm" color="#000000"/>
      </hh:borderFill>
    </hh:borderFills>
    <hh:charProperties>
      <hh:charPr id="0" height="{font_size}" textColor="#000000">
        <hp:fontRef hangul="0" latin="0" hanja="0"/>
        <hp:ratio hangul="100" latin="100" hanja="100"/>
        <hp:spacing hangul="0" latin="0" hanja="0"/>
        <hp:relSz hangul="100" latin="100" hanja="100"/>
        <hp:offset hangul="0" latin="0" hanja="0"/>
        <hp:italic/>
        <hp:bold/>
        <hp:underline type="NONE"/>
        <hp:strikeout type="NONE"/>
        <hp:outline type="NONE"/>
        <hp:shadow type="NONE"/>
        <hp:emboss type="NONE"/>
        <hp:engrave type="NONE"/>
      </hh:charPr>
      <hh:charPr id="1" height="{title_font_size}" textColor="#000000">
        <hp:fontRef hangul="0" latin="0" hanja="0"/>
        <hp:ratio hangul="100" latin="100" hanja="100"/>
        <hp:spacing hangul="0" latin="0" hanja="0"/>
        <hp:relSz hangul="100" latin="100" hanja="100"/>
        <hp:offset hangul="0" latin="0" hanja="0"/>
        <hp:italic/>
        <hp:bold value="true"/>
        <hp:underline type="NONE"/>
        <hp:strikeout type="NONE"/>
        <hp:outline type="NONE"/>
        <hp:shadow type="NONE"/>
        <hp:emboss type="NONE"/>
        <hp:engrave type="NONE"/>
      </hh:charPr>
    </hh:charProperties>
    <hh:tabProperties>
      <hh:tabPr id="0" autoTabLeft="0" autoTabRight="0"/>
    </hh:tabProperties>
    <hh:paraProperties>
      <hh:paraPr id="0" align="BOTH">
        <hp:margin indent="0" left="0" right="0"/>
        <hp:spacing lineSpacing="160" before="0" after="0" lineSpacingType="PERCENT"/>
      </hh:paraPr>
      <hh:paraPr id="1" align="CENTER">
        <hp:margin indent="0" left="0" right="0"/>
        <hp:spacing lineSpacing="160" before="0" after="200" lineSpacingType="PERCENT"/>
      </hh:paraPr>
    </hh:paraProperties>
    <hh:styles>
      <hh:style id="0" type="PARA" name="Normal" paraPrIDRef="0" charPrIDRef="0"/>
    </hh:styles>
  </hh:refList>
</hh:head>'''

    section_xml = f'''<?xml version="1.0" encoding="UTF-8"?>
<hs:sec xmlns:hs="{HS}" xmlns:hp="{HP}">
  <hp:secPr textDirection="HORIZONTAL" spaceColumns="1134">
    <hp:pageSize width="{page_width}" height="{page_height}"/>
    <hp:pageMar left="{margin_left}" right="{margin_right}" top="{margin_top}" bottom="{margin_bottom}" header="{margin_header}" footer="{margin_footer}"/>
  </hp:secPr>
{para_xml}
</hs:sec>'''

    try:
        out.parent.mkdir(parents=True, exist_ok=True)

        with zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED) as zf:
            # mimetype은 첫 번째, 비압축 (ODF 관례)
            zf.writestr('mimetype', mimetype, compress_type=zipfile.ZIP_STORED)
            zf.writestr('version.xml', version_xml)
            zf.writestr('META-INF/manifest.xml', manifest_xml)
            zf.writestr('Contents/content.hpf', content_hpf)
            zf.writestr('Contents/header.xml', header_xml)
            zf.writestr('Contents/section0.xml', section_xml)

        size_kb = out.stat().st_size / 1024
        total_paras = len(paragraphs) + (1 if title else 0)
        return True, (
            f"Created {output_path}\n"
            f"  {total_paras}개 단락, {size_kb:.1f} KB"
        )

    except Exception as e:
        return False, f"Error: 파일 생성 실패 - {e}"


def main():
    parser = argparse.ArgumentParser(description="새 HWPX 파일을 생성합니다")
    parser.add_argument("--output", "-o", required=True, help="출력 HWPX 파일 경로")
    parser.add_argument("--title", help="문서 제목 (첫 번째 단락, 볼드+16pt)")
    parser.add_argument("--body", help="본문 텍스트")
    parser.add_argument("--paragraphs", nargs="+", help="단락 목록")
    parser.add_argument("--input-file", help="단락이 줄로 구분된 텍스트 파일")
    parser.add_argument("--font", default="함초롬돋움", help="기본 글꼴 (기본: 함초롬돋움)")
    parser.add_argument("--font-size", type=int, default=1000,
                        help="글꼴 크기 (1/100 pt, 기본: 1000=10pt)")

    args = parser.parse_args()

    # 단락 수집
    paragraphs = []

    if args.body:
        paragraphs.append(args.body)

    if args.paragraphs:
        paragraphs.extend(args.paragraphs)

    if args.input_file:
        try:
            with open(args.input_file, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line:
                        paragraphs.append(line)
        except FileNotFoundError:
            print(f"Error: {args.input_file} 파일을 찾을 수 없습니다", file=sys.stderr)
            sys.exit(1)

    if not paragraphs and not args.title:
        print("Error: --title, --body, --paragraphs, --input-file 중 하나 이상 지정하세요",
              file=sys.stderr)
        sys.exit(1)

    success, message = create_hwpx(
        args.output,
        paragraphs,
        title=args.title or "",
        font_hangul=args.font,
        font_latin=args.font,
        font_size=args.font_size,
    )
    print(message)

    if not success:
        sys.exit(1)


if __name__ == "__main__":
    main()
