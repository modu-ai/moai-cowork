#!/usr/bin/env python3
"""
build_images_only_pptx.py — 이미지 디렉토리에서 PPTX 프레젠테이션 생성

사용 예시:
    python build_images_only_pptx.py --images ./slides --output presentation.pptx
    python build_images_only_pptx.py --images ./slides --output deck.pptx --ratio 4:3
    python build_images_only_pptx.py --images ./slides --output deck.pptx --title "분기 보고서" --subtitle "2026 Q1"

의존성:
    pip install python-pptx Pillow

지원 이미지 형식: .jpg, .jpeg, .png, .gif, .bmp, .tiff, .webp
슬라이드 순서: 파일명 기준 알파벳순 정렬
"""

import argparse
import json
import os
import sys
from pathlib import Path

try:
    from pptx import Presentation
    from pptx.util import Inches, Pt, Emu
    from pptx.enum.text import PP_ALIGN
    from pptx.dml.color import RGBColor
except ImportError:
    print("오류: python-pptx가 설치되지 않았습니다. 'pip install python-pptx'를 실행하세요.")
    sys.exit(1)

try:
    from PIL import Image
except ImportError:
    Image = None


# 지원 이미지 확장자
SUPPORTED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".tif", ".webp"}

# 한국어 폰트 우선순위
KOREAN_FONTS = ["Pretendard", "Noto Sans KR", "맑은 고딕", "Apple SD Gothic Neo", "나눔고딕", "돋움"]

# 슬라이드 비율 설정
SLIDE_RATIOS = {
    "16:9": (Inches(13.33), Inches(7.5)),
    "4:3":  (Inches(10),    Inches(7.5)),
    "16:10": (Inches(10), Inches(6.25)),
    "A4":   (Inches(10.83), Inches(7.5)),
}


def find_images(directory: Path) -> list[Path]:
    """디렉토리에서 지원 이미지 파일을 정렬된 순서로 반환."""
    images = [
        f for f in directory.iterdir()
        if f.is_file() and f.suffix.lower() in SUPPORTED_EXTENSIONS
    ]
    return sorted(images, key=lambda p: p.name)


def get_image_dimensions(image_path: Path) -> tuple[int, int] | None:
    """PIL이 있으면 이미지 크기 반환, 없으면 None."""
    if Image is None:
        return None
    try:
        with Image.open(image_path) as img:
            return img.size  # (width, height)
    except Exception:
        return None


def add_title_slide(prs: Presentation, title: str, subtitle: str, font_name: str) -> None:
    """제목 슬라이드 추가."""
    slide_layout = prs.slide_layouts[0]  # 제목 슬라이드 레이아웃
    slide = prs.slides.add_slide(slide_layout)

    slide_width = prs.slide_width
    slide_height = prs.slide_height

    # 기존 플레이스홀더 제거
    for shape in slide.placeholders:
        sp = shape._element
        sp.getparent().remove(sp)

    # 제목 텍스트 박스
    title_box = slide.shapes.add_textbox(
        Inches(1), Inches(2.5),
        slide_width - Inches(2), Inches(1.5)
    )
    tf = title_box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    run = p.add_run()
    run.text = title
    run.font.size = Pt(40)
    run.font.bold = True
    run.font.name = font_name
    run.font.color.rgb = RGBColor(0x1A, 0x1A, 0x1A)

    # 부제목 텍스트 박스
    if subtitle:
        sub_box = slide.shapes.add_textbox(
            Inches(1), Inches(4.2),
            slide_width - Inches(2), Inches(1)
        )
        tf2 = sub_box.text_frame
        p2 = tf2.paragraphs[0]
        p2.alignment = PP_ALIGN.CENTER
        run2 = p2.add_run()
        run2.text = subtitle
        run2.font.size = Pt(24)
        run2.font.name = font_name
        run2.font.color.rgb = RGBColor(0x55, 0x55, 0x55)


def add_image_slide(
    prs: Presentation,
    image_path: Path,
    slide_title: str | None = None,
    font_name: str = "Pretendard",
) -> None:
    """이미지 슬라이드 추가. 이미지를 슬라이드에 꽉 채움."""
    blank_layout = prs.slide_layouts[6]  # 빈 레이아웃
    slide = prs.slides.add_slide(blank_layout)

    slide_width = prs.slide_width
    slide_height = prs.slide_height

    # 슬라이드 제목이 있으면 이미지 영역 축소
    if slide_title:
        title_height = Inches(0.6)
        img_top = title_height
        img_height = slide_height - title_height
    else:
        img_top = Emu(0)
        img_height = slide_height

    # 이미지 비율 유지하며 배치
    dims = get_image_dimensions(image_path)
    if dims:
        img_w, img_h = dims
        ratio = img_w / img_h
        slide_ratio = slide_width / img_height

        if ratio > slide_ratio:
            # 가로 기준 맞춤
            pic_width = slide_width
            pic_height = Emu(int(slide_width / ratio))
            pic_left = Emu(0)
            pic_top = img_top + Emu(int((img_height - pic_height) / 2))
        else:
            # 세로 기준 맞춤
            pic_height = img_height
            pic_width = Emu(int(img_height * ratio))
            pic_left = Emu(int((slide_width - pic_width) / 2))
            pic_top = img_top
    else:
        # PIL 없음: 전체 채움
        pic_left = Emu(0)
        pic_top = img_top
        pic_width = slide_width
        pic_height = img_height

    slide.shapes.add_picture(str(image_path), pic_left, pic_top, pic_width, pic_height)

    # 슬라이드 제목 오버레이
    if slide_title:
        title_box = slide.shapes.add_textbox(
            Inches(0.2), Emu(0),
            slide_width - Inches(0.4), title_height
        )
        tf = title_box.text_frame
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.LEFT
        run = p.add_run()
        run.text = slide_title
        run.font.size = Pt(18)
        run.font.bold = True
        run.font.name = font_name
        run.font.color.rgb = RGBColor(0x1A, 0x1A, 0x1A)


def build_pptx(
    images_dir: str,
    output_path: str,
    ratio: str = "16:9",
    title: str | None = None,
    subtitle: str | None = None,
    slide_meta: dict | None = None,
    font_name: str = "Pretendard",
) -> None:
    """
    이미지 디렉토리에서 PPTX 생성.

    Args:
        images_dir: 이미지 파일이 있는 디렉토리 경로
        output_path: 출력 PPTX 파일 경로
        ratio: 슬라이드 비율 ("16:9", "4:3", "16:10", "A4")
        title: 제목 슬라이드 제목 (None이면 제목 슬라이드 생략)
        subtitle: 제목 슬라이드 부제목
        slide_meta: 슬라이드별 메타데이터 {"filename": {"title": "..."}} 형태
        font_name: 사용할 폰트명
    """
    images_path = Path(images_dir)
    if not images_path.exists():
        raise FileNotFoundError(f"이미지 디렉토리를 찾을 수 없습니다: {images_dir}")

    images = find_images(images_path)
    if not images:
        raise ValueError(f"지원 이미지 파일이 없습니다: {images_dir}")

    # 슬라이드 크기 설정
    if ratio not in SLIDE_RATIOS:
        raise ValueError(f"지원하지 않는 비율: {ratio}. 지원: {list(SLIDE_RATIOS.keys())}")

    slide_width, slide_height = SLIDE_RATIOS[ratio]

    prs = Presentation()
    prs.slide_width = slide_width
    prs.slide_height = slide_height

    # 제목 슬라이드 추가
    if title:
        add_title_slide(prs, title, subtitle or "", font_name)

    # 이미지 슬라이드 추가
    meta = slide_meta or {}
    for img_path in images:
        slide_title = meta.get(img_path.name, {}).get("title") if meta else None
        add_image_slide(prs, img_path, slide_title, font_name)
        print(f"  추가: {img_path.name}")

    # 저장
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    prs.save(str(output))
    print(f"\n저장 완료: {output} ({len(prs.slides)}슬라이드)")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="이미지 디렉토리에서 PPTX 프레젠테이션 생성",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("--images", required=True, help="이미지 디렉토리 경로")
    parser.add_argument("--output", required=True, help="출력 PPTX 파일 경로")
    parser.add_argument("--ratio", default="16:9", choices=list(SLIDE_RATIOS.keys()), help="슬라이드 비율 (기본: 16:9)")
    parser.add_argument("--title", help="제목 슬라이드 제목")
    parser.add_argument("--subtitle", help="제목 슬라이드 부제목")
    parser.add_argument("--meta", help="슬라이드 메타데이터 JSON 파일 경로 (슬라이드별 제목 등)")
    parser.add_argument("--font", default="Pretendard", help="폰트명 (기본: Pretendard)")

    args = parser.parse_args()

    # 메타데이터 파일 로드
    slide_meta = None
    if args.meta:
        meta_path = Path(args.meta)
        if not meta_path.exists():
            print(f"경고: 메타데이터 파일을 찾을 수 없습니다: {args.meta}")
        else:
            with open(meta_path, encoding="utf-8") as f:
                slide_meta = json.load(f)

    print(f"이미지 디렉토리: {args.images}")
    print(f"출력 파일: {args.output}")
    print(f"슬라이드 비율: {args.ratio}")

    try:
        build_pptx(
            images_dir=args.images,
            output_path=args.output,
            ratio=args.ratio,
            title=args.title,
            subtitle=args.subtitle,
            slide_meta=slide_meta,
            font_name=args.font,
        )
    except (FileNotFoundError, ValueError) as e:
        print(f"오류: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
