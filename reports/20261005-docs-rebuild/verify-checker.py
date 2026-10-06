"""격리된 사본에서 깨진 링크와 잘못된 예제 수치를 탐지하는지 확인한다."""
import importlib.util,json,shutil,tempfile
from pathlib import Path
project=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location("docs",project/"scripts/check-docs.py")
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
results={}
with tempfile.TemporaryDirectory(prefix="moai-docs-oracle-") as tmp:
    root=Path(tmp)/"build";shutil.copytree("/tmp/moai-docs-20261005-final",root)
    page=root/"index.html";page.write_text(page.read_text()+'<a href="/missing-oracle-page/">test</a>')
    errors=module.check(root,project)["errors"]
    results["missing_link_detected"]=any("/missing-oracle-page/" in e for e in errors)
    fixture=Path(tmp)/"project";shutil.copytree(project/"www/content",fixture/"www/content");shutil.copytree(project/"www/static/downloads",fixture/"www/static/downloads")
    sample=fixture/"www/content/cookbook/templates/excel.md"
    sample.write_text(sample.read_text().replace("세 항목 합계는 25,000원", "세 항목 합계는 26,000원"))
    errors=module.check(Path("/tmp/moai-docs-20261005-final"),fixture)["errors"]
    results["wrong_example_total_detected"]=any("templates/excel.md: example arithmetic mismatch" in e for e in errors)
assert all(results.values()),results
(project/"reports/20261005-docs-rebuild/checker-negative.json").write_text(json.dumps(results,indent=2)+"\n")
print(json.dumps(results))
