# Based on seocholaw HWPX utilities (MIT License)
"""
HWPX 파일 구조 검증 스크립트

HWPX 파일의 ZIP 무결성, 필수 XML 파일 존재 여부,
OWPML 네임스페이스, mimetype 항목을 검사합니다.

사용법:
    python validate.py document.hwpx
    python validate.py document.hwpx --strict
    python validate.py document.hwpx --json

종료 코드:
    0 = PASS
    1 = FAIL
"""

from __future__ import annotations

import argparse
import json
import sys
import zipfile
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional


# HWPX 필수 파일 목록
REQUIRED_FILES: list[str] = [
    "mimetype",
    "META-INF/container.xml",
    "Contents/header.xml",
]

# 최소 1개의 섹션 파일 필요
MIN_SECTION_REQUIRED = True

# OWPML 네임스페이스 (검증 기준)
OWPML_NS = "http://www.hancom.co.kr/hwpml/2016/HwpDoc"
EXPECTED_MIMETYPE = "application/hwp+zip"


@dataclass
class CheckResult:
    """개별 검사 항목 결과."""
    name: str
    passed: bool
    message: str
    severity: str = "error"  # error | warning | info


@dataclass
class ValidationReport:
    """전체 검증 보고서."""
    file: str
    checks: list[CheckResult] = field(default_factory=list)

    @property
    def passed(self) -> bool:
        return all(c.passed for c in self.checks if c.severity == "error")

    @property
    def error_count(self) -> int:
        return sum(1 for c in self.checks if not c.passed and c.severity == "error")

    @property
    def warning_count(self) -> int:
        return sum(1 for c in self.checks if not c.passed and c.severity == "warning")


def _check_zip_integrity(path: str) -> CheckResult:
    """ZIP 파일 무결성을 검사합니다."""
    if not zipfile.is_zipfile(path):
        return CheckResult("ZIP 무결성", False, "ZIP 파일 시그니처 없음 또는 손상됨")
    try:
        with zipfile.ZipFile(path, "r") as zf:
            bad = zf.testzip()
            if bad:
                return CheckResult("ZIP 무결성", False, f"손상된 엔트리: {bad}")
    except zipfile.BadZipFile as e:
        return CheckResult("ZIP 무결성", False, str(e))
    return CheckResult("ZIP 무결성", True, "ZIP 구조 정상")


def _check_mimetype(zf: zipfile.ZipFile) -> CheckResult:
    """mimetype 엔트리의 값과 압축 방식을 검사합니다."""
    if "mimetype" not in zf.namelist():
        return CheckResult("mimetype", False, "mimetype 파일이 없습니다")

    info = zf.getinfo("mimetype")
    # mimetype은 압축 없이 저장되어야 함
    compression_ok = info.compress_type == zipfile.ZIP_STORED

    try:
        value = zf.read("mimetype").decode("ascii", errors="replace").strip()
    except Exception as e:
        return CheckResult("mimetype", False, f"읽기 오류: {e}")

    if value != EXPECTED_MIMETYPE:
        return CheckResult(
            "mimetype",
            False,
            f"예상값: '{EXPECTED_MIMETYPE}', 실제값: '{value}'",
        )
    if not compression_ok:
        return CheckResult(
            "mimetype",
            False,
            "mimetype은 비압축(ZIP_STORED)이어야 합니다",
            severity="warning",
        )
    return CheckResult("mimetype", True, f"'{value}' (비압축)")


def _check_required_files(zf: zipfile.ZipFile) -> list[CheckResult]:
    """필수 파일 존재 여부를 검사합니다."""
    results: list[CheckResult] = []
    entries = set(zf.namelist())
    for req in REQUIRED_FILES:
        if req in entries:
            results.append(CheckResult(f"필수파일:{req}", True, "존재함"))
        else:
            results.append(CheckResult(f"필수파일:{req}", False, f"'{req}' 파일이 없습니다"))
    return results


def _check_section_files(zf: zipfile.ZipFile) -> CheckResult:
    """최소 1개의 섹션 파일이 있는지 검사합니다."""
    import re
    sections = [n for n in zf.namelist() if re.match(r"Contents/section\d+\.xml", n)]
    if sections:
        return CheckResult("섹션 파일", True, f"{len(sections)}개 발견: {', '.join(sorted(sections))}")
    return CheckResult("섹션 파일", False, "Contents/section*.xml 파일이 없습니다")


def _check_owpml_namespace(zf: zipfile.ZipFile) -> CheckResult:
    """header.xml 또는 section0.xml에서 OWPML 네임스페이스를 확인합니다."""
    candidates = ["Contents/header.xml", "Contents/section0.xml"]
    for candidate in candidates:
        try:
            data = zf.read(candidate)
            root = ET.fromstring(data)
            # ElementTree는 네임스페이스를 {uri}tag 형식으로 반환
            if OWPML_NS in root.tag or any(OWPML_NS in k for k in root.attrib):
                return CheckResult("OWPML 네임스페이스", True, f"{candidate}에서 확인")
            # 자식 노드 탐색
            for elem in root.iter():
                if OWPML_NS in elem.tag:
                    return CheckResult("OWPML 네임스페이스", True, f"{candidate}에서 확인")
        except (KeyError, ET.ParseError):
            continue

    return CheckResult(
        "OWPML 네임스페이스",
        False,
        f"'{OWPML_NS}' 네임스페이스를 찾을 수 없습니다",
        severity="warning",
    )


def _check_xml_wellformed(zf: zipfile.ZipFile) -> list[CheckResult]:
    """모든 XML 파일의 형식이 올바른지 검사합니다."""
    results: list[CheckResult] = []
    xml_files = [n for n in zf.namelist() if n.endswith(".xml") or n.endswith(".hpf")]
    for xf in xml_files:
        try:
            data = zf.read(xf)
            ET.fromstring(data)
            results.append(CheckResult(f"XML형식:{xf}", True, "올바른 XML"))
        except ET.ParseError as e:
            results.append(CheckResult(f"XML형식:{xf}", False, f"파싱 오류: {e}"))
        except KeyError:
            results.append(CheckResult(f"XML형식:{xf}", False, "읽기 불가"))
    return results


def validate(hwpx_path: str, strict: bool = False) -> ValidationReport:
    """HWPX 파일을 검증하고 보고서를 반환합니다.

    Args:
        hwpx_path: .hwpx 파일 경로
        strict: True이면 XML 형식 검사도 수행

    Returns:
        ValidationReport 인스턴스
    """
    report = ValidationReport(file=hwpx_path)

    # 파일 존재 확인
    path = Path(hwpx_path)
    if not path.exists():
        report.checks.append(CheckResult("파일 존재", False, f"파일을 찾을 수 없습니다: {hwpx_path}"))
        return report
    report.checks.append(CheckResult("파일 존재", True, f"{path.stat().st_size:,} bytes"))

    # ZIP 무결성
    zip_check = _check_zip_integrity(hwpx_path)
    report.checks.append(zip_check)
    if not zip_check.passed:
        return report  # ZIP 손상 시 이후 검사 불가

    with zipfile.ZipFile(hwpx_path, "r") as zf:
        report.checks.append(_check_mimetype(zf))
        report.checks.extend(_check_required_files(zf))
        report.checks.append(_check_section_files(zf))
        report.checks.append(_check_owpml_namespace(zf))
        if strict:
            report.checks.extend(_check_xml_wellformed(zf))

    return report


def print_report(report: ValidationReport) -> None:
    """검증 보고서를 텍스트로 출력합니다."""
    status = "PASS" if report.passed else "FAIL"
    print(f"=== HWPX 검증 결과: {status} ===")
    print(f"파일: {report.file}")
    print(f"오류: {report.error_count}개 | 경고: {report.warning_count}개")
    print()
    for check in report.checks:
        icon = "✓" if check.passed else ("!" if check.severity == "warning" else "✗")
        print(f"  [{icon}] {check.name}: {check.message}")
    print()
    print(f"결과: {status}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="HWPX 파일 구조 검증기",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("hwpx", help="검증할 .hwpx 파일 경로")
    parser.add_argument("--strict", action="store_true", help="XML 형식 검사 포함")
    parser.add_argument("--json", action="store_true", help="JSON 형식으로 출력")

    args = parser.parse_args()
    report = validate(args.hwpx, strict=args.strict)

    if args.json:
        data = {
            "file": report.file,
            "passed": report.passed,
            "error_count": report.error_count,
            "warning_count": report.warning_count,
            "checks": [
                {
                    "name": c.name,
                    "passed": c.passed,
                    "message": c.message,
                    "severity": c.severity,
                }
                for c in report.checks
            ],
        }
        print(json.dumps(data, ensure_ascii=False, indent=2))
    else:
        print_report(report)

    sys.exit(0 if report.passed else 1)


if __name__ == "__main__":
    main()
