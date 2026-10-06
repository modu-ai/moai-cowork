"""프로젝트 설정·의존성·쓰기 소유권·지침 예산을 검사한다. 업무를 실행하지 않는다."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re

SKILL_ID = re.compile(r"^moai-[a-z0-9-]+:[a-z0-9-]+$")
STATES = {"pending", "running", "blocked", "completed", "failed"}


def digest(data: bytes) -> str:
    return "sha256:" + hashlib.sha256(data).hexdigest()


def safe_path(value: str) -> bool:
    normalized = value.replace("\\", "/")
    return bool(normalized) and not normalized.startswith("/") and not re.match(r"^[A-Za-z]:", normalized) and ".." not in PurePosixPath(normalized).parts


def overlaps(left: str, right: str) -> bool:
    """같은 경로·부모 경로·glob의 고정 접두어를 공유하면 직렬화한다."""
    def prefix(value: str) -> str:
        value = PurePosixPath(value.replace("\\", "/")).as_posix().casefold()
        fixed = re.split(r"[?*\[]", value, maxsplit=1)[0]
        if fixed != value:
            fixed = fixed.rsplit("/", 1)[0] if "/" in fixed else ""
        return "" if fixed == "." else fixed.strip("/")
    a, b = prefix(left), prefix(right)
    return not a or not b or a == b or a.startswith(b + "/") or b.startswith(a + "/")


def validate(config: dict, root: Path | None = None) -> list[str]:
    errors = []
    if config.get("schema_version") != 2:
        errors.append("schema_version: 기존 값을 보존하며 버전 2 계약으로 이관해야 합니다")
    for field in ("project", "host", "skills_available", "workflows", "context"):
        expected = list if field == "workflows" else dict
        if not isinstance(config.get(field), expected):
            errors.append(f"{field}: {expected.__name__} 값이 필요합니다")
    if errors:
        return errors
    if any(not isinstance(config["project"].get(k), str) or not config["project"][k].strip() for k in ("name", "purpose")):
        errors.append("project: 이름과 목적이 필요합니다")
    if config.get("sensitivity") not in ("public", "sensitive", "unknown"):
        errors.append("sensitivity: public/sensitive/unknown 중 하나가 필요합니다")
    context = config["context"]
    if not isinstance(context.get("answers"), dict) or not isinstance(context.get("questions"), list):
        errors.append("context: answers 객체와 questions 배열이 필요합니다")
    else:
        for key, answer in context["answers"].items():
            if not isinstance(answer, dict) or "value" not in answer or not answer.get("source"):
                errors.append(f"context.answers.{key}: 실제 값과 출처가 필요합니다")
        for question in context["questions"]:
            if not isinstance(question, dict) or not question.get("id") or question.get("status") not in ("waiting", "answered", "deferred", "not_applicable"):
                errors.append("context.questions: id와 질문 상태가 필요합니다")
    host = config["host"]
    limit = host.get("max_concurrent", 1)
    if type(limit) is not int or limit < 1:
        errors.append("host.max_concurrent: 양의 정수가 필요합니다")
    elif limit > 1 and not (host.get("subagents") is True and host.get("delegation_authorized") is True):
        errors.append("병렬 에이전트: 관찰한 기능과 분업 권한이 필요합니다")
    steps = config["workflows"]
    if any(not isinstance(s, dict) for s in steps):
        return errors + ["workflows: 각 단계는 객체여야 합니다"]
    ids = [s.get("id") for s in steps]
    if any(not isinstance(i, str) or not i for i in ids) or len(set(ids)) != len(ids):
        return errors + ["workflows: 단계 id는 비어 있지 않고 고유해야 합니다"]
    graph = {s["id"]: s for s in steps}
    experts = config.get("experts", {})
    if not isinstance(experts, dict):
        return errors + ["experts: 전문가 계약 객체가 필요합니다"]
    for name, expert in experts.items():
        if not isinstance(expert, dict) or not isinstance(expert.get("role"), str) or not expert["role"].strip():
            errors.append(f"experts.{name}: 전문 역할 계약이 필요합니다")
            continue
        for field in ("skills", "inputs", "outputs", "write_set", "verification", "missing_context"):
            value = expert.get(field)
            if not isinstance(value, list) or any(not isinstance(v, str) for v in value):
                errors.append(f"experts.{name}.{field}: 문자열 배열이 필요합니다")
        if not isinstance(expert.get("skills"), list) or not isinstance(expert.get("write_set"), list):
            continue
        for skill in expert["skills"]:
            if not isinstance(skill, str) or not SKILL_ID.fullmatch(skill) or skill not in config["skills_available"]:
                errors.append(f"experts.{name}: 스킬 소속과 현재 인벤토리가 필요합니다")
        for path in expert["write_set"]:
            if not isinstance(path, str) or not safe_path(path):
                errors.append(f"experts.{name}: 작업 폴더 안의 쓰기 소유권이 필요합니다")
    for step in steps:
        sid = step["id"]
        for field in ("depends_on", "skills", "write_set", "outputs", "evidence"):
            value = step.get(field, [])
            if not isinstance(value, list) or any(not isinstance(v, str) for v in value):
                errors.append(f"{sid}.{field}: 문자열 배열이 필요합니다")
        if any(e.startswith(sid + ".") for e in errors):
            continue
        if step.get("status") not in tuple(STATES):
            errors.append(f"{sid}: 단계 상태가 필요합니다")
        if "agent" in step and (not isinstance(step["agent"], str) or (step["agent"] != "parent" and step["agent"] not in experts)):
            errors.append(f"{sid}: 전문가 계약을 찾을 수 없습니다: {step['agent']}")
        elif step.get("agent", "parent") != "parent":
            expert = experts[step["agent"]]
            if isinstance(expert, dict) and isinstance(expert.get("skills"), list):
                if any(skill not in expert["skills"] for skill in step.get("skills", [])):
                    errors.append(f"{sid}: 전문가에게 배정하지 않은 스킬입니다")
        if step.get("operation") not in ("read", "write", "external_write"):
            errors.append(f"{sid}: read/write/external_write operation이 필요합니다")
        if not step.get("completion_criteria"):
            errors.append(f"{sid}: 관찰 가능한 완료 기준이 필요합니다")
        for dep in step.get("depends_on", []):
            if dep not in graph or dep == sid:
                errors.append(f"{sid}: 유효하지 않은 선행 단계 {dep}")
        for skill in step.get("skills", []):
            entry = config["skills_available"].get(skill)
            if not SKILL_ID.fullmatch(skill) or not isinstance(entry, dict):
                errors.append(f"{sid}: 스킬 소속을 확인할 수 없습니다: {skill}")
            elif step.get("status") != "blocked" and entry.get("status") not in ("exposed", "callable"):
                errors.append(f"{sid}: 현재 호스트에 노출되지 않은 스킬: {skill}")
        writes = step.get("write_set", [])
        if step.get("operation") == "read" and writes:
            errors.append(f"{sid}: 읽기 단계에 쓰기 경로가 있습니다")
        if step.get("operation") == "write" and not writes:
            errors.append(f"{sid}: 쓰기 소유권이 필요합니다")
        for value in writes + step.get("outputs", []):
            if not safe_path(value):
                errors.append(f"{sid}: 작업 폴더 밖의 쓰기/산출물 경로: {value}")
            elif root is not None:
                fixed = re.split(r"[?*\[]", value.replace("\\", "/"), maxsplit=1)[0]
                if not (root / fixed).resolve().is_relative_to(root.resolve()):
                    errors.append(f"{sid}: 심볼릭 링크로 작업 폴더를 벗어나는 경로: {value}")
        if step.get("operation") == "external_write" and step.get("status") != "blocked":
            if not step.get("account_ref") or step.get("authorization") != "granted":
                errors.append(f"{sid}: 대상 계정과 기존 요청에서 확인한 변경 권한이 필요합니다")
        if step.get("status") == "completed" and not step.get("evidence"):
            errors.append(f"{sid}: 완료 증거 없이 completed로 표시할 수 없습니다")
    if errors:
        return errors
    for step in steps:
        if step["status"] == "completed" and any(graph[d]["status"] != "completed" for d in step.get("depends_on", [])):
            errors.append(f"{step['id']}: 선행 단계가 완료되지 않았습니다")
    remaining = set(graph)
    while remaining:
        ready = {sid for sid in remaining if not (set(graph[sid].get("depends_on", [])) & remaining)}
        if not ready:
            errors.append("workflows: 순환 의존성이 있습니다")
            break
        remaining -= ready
    return errors


def plan(config: dict) -> dict:
    errors = validate(config)
    if errors:
        raise ValueError("; ".join(errors))
    steps = {s["id"]: s for s in config["workflows"]}
    done = {sid for sid, s in steps.items() if s["status"] == "completed"}
    pending = {sid for sid, s in steps.items() if s["status"] == "pending"}
    batches = []
    while pending:
        batch = []
        for sid in sorted(pending):
            step = steps[sid]
            if not set(step.get("depends_on", [])) <= done:
                continue
            # 외부 변경은 실제 상태 재조회가 필요하므로 한 번에 한 단계만 계획한다.
            conflict = any(step["operation"] == "external_write" or steps[b]["operation"] == "external_write" or
                           any(overlaps(a, c) for a in step.get("write_set", []) for c in steps[b].get("write_set", [])) for b in batch)
            if not conflict:
                batch.append(sid)
            if len(batch) >= config["host"].get("max_concurrent", 1):
                break
        if not batch:
            break
        batches.append(batch)
        pending -= set(batch)
        done |= set(batch)
    blocked = sorted(pending | {sid for sid, s in steps.items() if s["status"] in {"blocked", "failed", "running"}})
    return {"batches": batches, "blocked_or_incomplete": blocked, "executed": False}


def instruction_budget(files: list[Path], limit: int) -> dict:
    if limit < 1:
        raise ValueError("지침 byte 한도는 양수여야 합니다")
    sizes = [{"path": str(p), "bytes": p.stat().st_size} for p in files]
    total = sum(s["bytes"] for s in sizes)
    return {"files": sizes, "total_bytes": total, "limit_bytes": limit, "passed": total <= limit}


def rollback_content(current: bytes, expected_after: str, before: bytes) -> bytes:
    """파일을 쓰지 않는다. 현재 내용이 자신이 쓴 값과 같을 때만 복구 내용을 반환한다."""
    if digest(current) != expected_after:
        raise ValueError("후속 편집이 있어 자동 롤백을 보류합니다")
    return before


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("validate", "plan", "budget"))
    parser.add_argument("--config", type=Path)
    parser.add_argument("--root", type=Path)
    parser.add_argument("--files", type=Path, nargs="+")
    parser.add_argument("--limit", type=int, default=32768, help="관찰한 호스트 지침 한도; Codex 기본값 32768")
    args = parser.parse_args()
    try:
        if args.mode == "budget":
            if not args.files:
                parser.error("budget에는 실제 발견된 지침 체인의 --files가 필요합니다")
            result = instruction_budget(args.files, args.limit)
            code = 0 if result["passed"] else 1
        else:
            if not args.config:
                parser.error("--config가 필요합니다")
            config = json.loads(args.config.read_text(encoding="utf-8"))
            if not isinstance(config, dict):
                raise ValueError("설정 정본은 JSON 객체여야 합니다")
            errors = validate(config, args.root)
            result = {"errors": errors} if errors or args.mode == "validate" else plan(config)
            code = 1 if errors else 0
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return code
    except (ValueError, OSError) as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
