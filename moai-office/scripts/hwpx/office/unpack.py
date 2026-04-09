# Based on seocholaw HWPX utilities (MIT License)
"""
HWPX 언패킹 스크립트 (.hwpx ZIP -> 디렉토리)

HWPX ZIP 파일을 디렉토리 구조로 언패킹합니다.
편집 후 pack.py로 다시 패킹할 수 있습니다.

사용법:
    python unpack.py document.hwpx
    python unpack.py document.hwpx --output ./my_hwpx_dir
    python unpack.py document.hwpx --output ./my_hwpx_dir --overwrite

언패킹 결과:
    my_hwpx_dir/
    ├── mimetype
    ├── META-INF/
    │   ├── container.xml
    │   └── manifest.xml  (있는 경우)
    └── Contents/
        ├── content.hpf
        ├── header.xml
        └── section0.xml
"""

from __future__ import annotations

import argparse
import sys
import zipfile
from pathlib import Path
from typing import Optional


def unpack(
    hwpx_path: str,
    output_dir: Optional[str] = None,
    overwrite: bool = False,
    verbose: bool = False,
) -> str:
    """HWPX 파일을 디렉토리로 언패킹합니다.

    Args:
        hwpx_path: .hwpx 파일 경로
        output_dir: 출력 디렉토리 (None이면 파일명 기반 자동 생성)
        overwrite: True이면 기존 디렉토리 덮어쓰기
        verbose: 진행 상황 출력 여부

    Returns:
        언패킹된 디렉토리 경로
    """
    src = Path(hwpx_path)
    if not src.exists():
        print(f"오류: 파일을 찾을 수 없습니다: {hwpx_path}", file=sys.stderr)
        sys.exit(1)

    if not zipfile.is_zipfile(str(src)):
        print(f"오류: 유효한 HWPX(ZIP) 파일이 아닙니다: {hwpx_path}", file=sys.stderr)
        sys.exit(1)

    # 출력 디렉토리 결정
    if output_dir is None:
        dst = src.parent / src.stem
    else:
        dst = Path(output_dir)

    if dst.exists() and not overwrite:
        print(
            f"오류: 출력 디렉토리가 이미 존재합니다: {dst}\n"
            "  --overwrite 옵션을 사용하면 덮어쓸 수 있습니다.",
            file=sys.stderr,
        )
        sys.exit(1)

    if verbose:
        print(f"입력: {src}")
        print(f"출력: {dst}")

    # 언패킹 수행
    extracted: list[str] = []
    with zipfile.ZipFile(str(src), "r") as zf:
        entries = zf.namelist()
        for entry in entries:
            # 경로 트래버설 공격 방지 (절대경로, ../ 포함 엔트리 무시)
            entry_path = Path(entry)
            if entry_path.is_absolute() or ".." in entry_path.parts:
                print(f"경고: 안전하지 않은 경로 스킵: {entry}", file=sys.stderr)
                continue

            target = dst / entry_path
            if entry.endswith("/"):
                # 디렉토리 엔트리
                target.mkdir(parents=True, exist_ok=True)
            else:
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(zf.read(entry))
                extracted.append(entry)
                if verbose:
                    info = zf.getinfo(entry)
                    print(f"  {entry} ({info.file_size:,} bytes)")

    print(f"언패킹 완료: {dst} ({len(extracted)}개 파일)")
    return str(dst)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="HWPX ZIP 파일을 디렉토리로 언패킹",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("hwpx", help="언패킹할 .hwpx 파일 경로")
    parser.add_argument("--output", "-o", default=None,
                        help="출력 디렉토리 경로 (기본: 파일명과 동일한 폴더명)")
    parser.add_argument("--overwrite", action="store_true",
                        help="출력 디렉토리가 이미 존재하면 덮어쓰기")
    parser.add_argument("--verbose", "-v", action="store_true", help="상세 출력")

    args = parser.parse_args()
    unpack(args.hwpx, args.output, args.overwrite, args.verbose)


if __name__ == "__main__":
    main()
