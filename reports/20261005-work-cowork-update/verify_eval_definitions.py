"""모델을 호출하지 않고 평가 정의와 합성 fixture를 확인한다."""
from pathlib import Path
import json
import subprocess
import tempfile

from PIL import Image
import yaml

ROOT = Path(__file__).resolve().parents[2]
paths = sorted(ROOT.glob("plugins/*/evals/**/case.yaml"))
for path in paths:
    case = yaml.safe_load(path.read_text(encoding="utf-8"))
    assert case["schema_version"] == "1.1" and case["name"] and case["execution"]["prompt"]
    assert case["graders"] and all(g["type"] in {"tool_used", "llm"} for g in case["graders"])
script = ROOT / "plugins/moai-seller/skills/commerce-detail-page-image/tests/scaffold.sh"
with tempfile.TemporaryDirectory() as tmp:
    subprocess.run(["bash", str(script)], cwd=tmp, check=True, timeout=10)
    files = sorted((Path(tmp) / "fixtures/sections").glob("*.png"))
    assert len(files) == 13
    for path in files:
        with Image.open(path) as image:
            assert image.size == (1, 1)
            image.verify()
result = {"definitions_parsed": len(paths), "png_fixtures_verified": len(files),
          "native_claude_eval_runs": 0, "scope": "offline_yaml_and_fixture_checks"}
(Path(__file__).parent / "eval-definition-evidence.json").write_text(
    json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, ensure_ascii=False))
