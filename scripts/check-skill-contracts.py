#!/usr/bin/env python3
"""스킬 표준·공통 패키지·PM 생성 계약을 오프라인으로 검사한다."""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import re

from jsonschema import Draft202012Validator, validators
from skills_ref import validate
import yaml

ROOT = Path(__file__).resolve().parents[1]


def load(path: Path):
    spec = importlib.util.spec_from_file_location(path.stem, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    errors = []
    skills = sorted(ROOT.glob("plugins/*/skills/*/SKILL.md"))
    for skill in skills:
        errors.extend(f"{skill.relative_to(ROOT)}: {e}" for e in validate(skill.parent))
    packages = sorted(ROOT.glob("plugins/moai-*/plugin.json"))
    for manifest in packages:
        for name in ("plugin", "mcp"):
            schema = json.loads((ROOT / f"scripts/schemas/{name}.schema.json").read_text(encoding="utf-8"))
            validator = validators.validator_for(schema)
            validator.check_schema(schema)
            data = json.loads((manifest.parent / f"{name}.json").read_text(encoding="utf-8"))
            errors.extend(f"{manifest.parent.name}/{name}.json: {e.message}" for e in validator(schema).iter_errors(data))
    generated = load(ROOT / "scripts/sync-plugin-contracts.py").generated()
    for path, value in generated.items():
        if not path.is_file() or json.loads(path.read_text(encoding="utf-8")) != value:
            errors.append(f"생성 정합 오류: {path.relative_to(ROOT)}")
    qualified = {row["id"] for row in generated[ROOT / "plugins/moai-pm/skills/project/references/skill-catalog.json"]["skills"]}
    for base in (ROOT / "plugins", ROOT / "www/content"):
        for path in base.rglob("*.md"):
            if {"archive", "archives"} & set(path.parts):
                continue
            text = path.read_text(encoding="utf-8")
            for match in re.finditer(r"(?<![a-z0-9-])moai-[a-z0-9-]+:[a-z0-9-]+(?![a-z0-9-])", text):
                sid = match.group()
                if not sid.endswith("-") and not text[match.end():].startswith("*") and sid not in qualified:
                    errors.append(f"알 수 없는 스킬 참조: {path.relative_to(ROOT)}: {sid}")
    project = ROOT / "plugins/moai-pm/skills/project"
    schema = json.loads((project / "references/templates/config.schema.json").read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    example = json.loads((project / "references/templates/config.example.json").read_text(encoding="utf-8"))
    errors.extend(f"PM 설정 예시: {e.message}" for e in Draft202012Validator(schema).iter_errors(example))
    errors.extend(load(project / "scripts/project_contract.py").validate(example, ROOT))
    template = (project / "references/templates/AGENTS.md.tmpl").read_text(encoding="utf-8")
    headings = re.findall(r"^## .*\(HARD\)$", template, re.M)
    main_skill = (project / "SKILL.md").read_text(encoding="utf-8")
    if len(headings) != 8 or any(f"`{h}`" not in main_skill for h in headings):
        errors.append("PM HARD 블록의 개수 또는 정본 제목이 일치하지 않습니다")
    for skill in skills:
        front = yaml.safe_load(skill.read_text(encoding="utf-8").split("---", 2)[1])
        if not isinstance(front.get("metadata", {}).get("version"), str):
            errors.append(f"metadata.version 문자열 없음: {skill.relative_to(ROOT)}")
    print(json.dumps({"skills": len(skills), "packages": len(packages), "errors": errors,
                      "scope": "offline_contracts_only"}, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
