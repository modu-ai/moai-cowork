#!/usr/bin/env python3
"""기존 YAML 사례를 Claude의 공식 eval 형식으로 연결한다. 모델은 호출하지 않는다."""
import argparse
import json
from pathlib import Path
import re

import yaml

ROOT = Path(__file__).resolve().parents[1]


def generated():
    outputs = {}
    index = []
    for source in sorted(ROOT.glob("plugins/*/skills/*/tests/test-cases.yaml")):
        suite = yaml.safe_load(source.read_text(encoding="utf-8"))
        cases = suite.get("test_cases", suite.get("cases", suite.get("tests", [])))
        plugin, skill = source.parts[-5], source.parts[-3]
        for number, case in enumerate(cases, 1):
            sid = str(case.get("id", case.get("name", number)))
            name = skill + "--" + re.sub(r"[^a-zA-Z0-9_-]", "-", sid)
            row = {"name": name, "source": str(source.relative_to(ROOT)), "case_id": sid,
                   "execution_status": "NOT-RUN"}
            value = case.get("prompt", case.get("input"))
            if value is None:
                row["gap"] = "실행 입력·fixture가 없는 기대 결과 정의"
                index.append(row)
                continue
            prompt = value if isinstance(value, str) else json.dumps(value, ensure_ascii=False, indent=2)
            criteria = {k: v for k, v in case.items() if k not in {"id", "name", "description", "input", "prompt", "eval_context"}}
            for key in ("rubric", "rubric_anchors", "anti_patterns"):
                if key in suite:
                    criteria[key] = suite[key]
            rubric = """입력 사실·제약과 아래 사례의 기대 결과를 대조한다. 모든 적용 가능한 조건을 만족하면 PASS, 하나라도 위반하면 FAIL이다. false 값은 해당 동작·주장이 없어야 한다는 뜻이다. 정보·도구·fixture가 부족하면 모델이 이를 명시했는지 확인하되, 원래 조건을 충족하지 못한 실행을 임의로 PASS로 바꾸지 않는다. 단어가 있다는 이유만으로 사실성·산술·법적 판단·의미 보존을 통과시키지 않는다. 원격 호출·파일 생성·독립 검수의 주장은 실제 trace와 산출물로 확인한다.\n\n"""
            rubric += json.dumps(criteria, ensure_ascii=False, indent=2)
            data = {"schema_version": "1.1", "name": name, "description": case.get("description", case.get("name", name)),
                    "runs": 1, "tags": ["generated", skill],
                    "execution": {"prompt": "다음 프로젝트 업무를 수행해 주세요. 미확인 정보는 만들지 말고 필요한 맥락을 요청하세요.\n\n" + prompt,
                                  "allowed_tools": ["Read", "Glob", "Grep", "Skill"], "max_turns": 12, "timeout_seconds": 180},
                    "graders": [{"name": "skill-fired", "type": "tool_used", "tool": "Skill",
                                 "input_match": '"skill"\\s*:\\s*"(?:[\\w-]+:)?' + re.escape(skill) + '"'},
                                {"name": "quality", "type": "llm", "focus": "trace", "criteria": rubric}]}
            outputs[ROOT / "plugins" / plugin / "evals/generated" / name / "case.yaml"] = yaml.safe_dump(data, allow_unicode=True, sort_keys=False)
            context = case.get("eval_context", {})
            if context.get("scaffold_script"):
                script = source.parent / context["scaffold_script"]
                if script.parent.resolve() != source.parent.resolve():
                    raise ValueError(f"사례 폴더 밖 scaffold: {script}")
                case_dir = ROOT / "plugins" / plugin / "evals/generated" / name
                outputs[case_dir / script.name] = script.read_text(encoding="utf-8")
                data["context"] = {"scaffold_script": script.name}
                data["execution"]["allowed_tools"] = context.get("allowed_tools", data["execution"]["allowed_tools"])
                outputs[case_dir / "case.yaml"] = yaml.safe_dump(data, allow_unicode=True, sort_keys=False)
            row["eval"] = str((ROOT / "plugins" / plugin / "evals/generated" / name / "case.yaml").relative_to(ROOT))
            index.append(row)
    outputs[ROOT / "scripts/skill-evals-index.json"] = json.dumps(index, ensure_ascii=False, indent=2) + "\n"
    return outputs, index


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    outputs, index = generated()
    errors = []
    for path, value in outputs.items():
        if args.check:
            if not path.is_file() or path.read_text(encoding="utf-8") != value:
                errors.append(str(path.relative_to(ROOT)))
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(value, encoding="utf-8")
    print(json.dumps({"cases": len(index), "runnable_definitions": sum("eval" in r for r in index),
                      "fixture_gaps": sum("gap" in r for r in index), "errors": errors,
                      "model_runs": 0}, ensure_ascii=False))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
