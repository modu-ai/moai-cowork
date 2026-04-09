# Based on seocholaw HWPX utilities (MIT License)
"""
HWPX 패킹 스크립트 (디렉토리 -> .hwpx ZIP)

HWPX 구조 디렉토리를 .hwpx ZIP 파일로 패킹합니다.
mimetype 파일은 HWPX 규격에 따라 첫 번째 엔트리로, 비압축으로 저장됩니다.

예상 디렉토리 구조:
    source_dir/
    ├── mimetype
    ├── META-INF/
    │   ├── container.xml
    │   └── manifest.xml
    └── Contents/
        ├── content.hpf
        ├── header.xml
        └── section0.xml

사용법:
    python pack.py ./my_hwpx_dir output.hwpx
    python pack.py ./my_hwpx_dir --output output.hwpx
    python pack.py ./my_hwpx_dir --output output.hwpx --compression deflate
"""

from __future__ import annotations

import argparse
import os
import sys
import zipfile
from pathlib import Path
from typing import Optional


# 압축 방식 매핑
COMPRESSION_MAP: dict[str, int] = {
    "store": zipfile.ZIP_STORED,
    "deflate": zipfile.ZIP_DEFLATED,
}

# mimetype은 항상 비압축으로 저장 (HWPX 규격)
MIMETYPE_FILENAME = "mimetype"


def pack(
    source_dir: str,
    output_path: Optional[str] = None,
    compression: str = "deflate",
    verbose: bool = False,
) -> str:
    """디렉토리를 HWPX ZIP 파일로 패킹합니다.

    Args:
        source_dir: HWPX 구조가 담긴 소스 디렉토리
        output_path: 출력 .hwpx 파일 경로 (None이면 자동 생성)
        compression: 압축 방식 ("store" | "deflate")
        verbose: 진행 상황 출력 여부

    Returns:
        생성된 .hwpx 파일 경로
    """
    src = Path(source_dir).resolve()
    if not src.is_dir():
        print(f"오류: 디렉토리가 아닙니다: {source_dir}", file=sys.stderr)
        sys.exit(1)

    if output_path is None:
        output_path = str(src.parent / f"{src.name}.hwpx")
    dst = Path(output_path)

    compress_type = COMPRESSION_MAP.get(compression, zipfile.ZIP_DEFLATED)

    # 전체 파일 수집 (상대 경로 기준)
    all_files: list[tuple[Path, str]] = []  # (절대경로, ZIP 내 경로)
    for root_str, dirs, files in os.walk(str(src)):
        root_path = Path(root_str)
        for filename in sorted(files):
            abs_path = root_path / filename
            rel_path = abs_path.relative_to(src)
            all_files.append((abs_path, str(rel_path).replace(os.sep, "/")))

    # mimetype 파일을 앞으로 분리
    mimetype_entry: Optional[tuple[Path, str]] = None
    other_entries: list[tuple[Path, str]] = []
    for abs_path, rel_path in all_files:
        if rel_path == MIMETYPE_FILENAME:
            mimetype_entry = (abs_path, rel_path)
        else:
            other_entries.append((abs_path, rel_path))

    if verbose:
        print(f"소스 디렉토리: {src}")
        print(f"출력 파일: {dst}")
        print(f"압축 방식: {compression}")
        print(f"파일 수: {len(all_files)}개")
        if not mimetype_entry:
            print("경고: mimetype 파일을 찾을 수 없습니다.", file=sys.stderr)

    with zipfile.ZipFile(str(dst), "w", compress_type) as zf:
        # mimetype을 첫 번째 엔트리로, 반드시 비압축 저장
        if mimetype_entry:
            abs_path, rel_path = mimetype_entry
            zf.write(str(abs_path), rel_path, compress_type=zipfile.ZIP_STORED)
            if verbose:
                print(f"  [STORED] {rel_path}")

        # 나머지 파일 패킹
        for abs_path, rel_path in other_entries:
            zf.write(str(abs_path), rel_path, compress_type=compress_type)
            if verbose:
                size = abs_path.stat().st_size
                print(f"  [{compression.upper()}] {rel_path} ({size:,} bytes)")

    final_size = dst.stat().st_size
    print(f"패킹 완료: {dst} ({final_size:,} bytes, {len(all_files)}개 파일)")
    return str(dst)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="디렉토리를 HWPX ZIP 파일로 패킹",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("source_dir", help="HWPX 구조 디렉토리 경로")
    parser.add_argument("output", nargs="?", default=None, help="출력 .hwpx 파일 경로")
    parser.add_argument("--output", "-o", dest="output_flag", default=None,
                        help="출력 .hwpx 파일 경로 (플래그 형식)")
    parser.add_argument(
        "--compression", "-c",
        choices=["store", "deflate"],
        default="deflate",
        help="압축 방식 (기본: deflate)",
    )
    parser.add_argument("--verbose", "-v", action="store_true", help="상세 출력")

    args = parser.parse_args()
    output_path = args.output or args.output_flag
    pack(args.source_dir, output_path, args.compression, args.verbose)


if __name__ == "__main__":
    main()
