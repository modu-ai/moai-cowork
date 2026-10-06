"""모델 호출 없이 프로젝트 실행 계약의 안전 조건을 검증한다."""
import importlib.util
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location("project_contract", Path(__file__).parents[1] / "scripts/project_contract.py")
contract = importlib.util.module_from_spec(spec)
spec.loader.exec_module(contract)


def stage(sid, depends=None, writes=None):
    return {"id": sid, "depends_on": depends or [], "skills": ["moai-pm:project"],
            "operation": "write" if writes else "read", "write_set": writes or [],
            "outputs": [], "status": "pending", "evidence": [], "completion_criteria": "입력과 결과를 대조한다"}


def config():
    return {"schema_version": 2, "project": {"name": "강의", "purpose": "교육 자료 제작"},
            "host": {"max_concurrent": 2, "subagents": True, "delegation_authorized": True},
            "sensitivity": "unknown", "context": {"answers": {"audience": {"value": "초보자", "source": "사용자 요청"}}, "questions": []},
            "skills_available": {"moai-pm:project": {"status": "exposed"}},
            "workflows": [stage("research"), stage("design"), stage("join", ["research", "design"], ["output/report.md"])]}


class ContractTests(unittest.TestCase):
    def test_expert_binding_must_exist(self):
        c = config(); c["workflows"][0]["agent"] = "expert-research"
        self.assertTrue(contract.validate(c))
        c["experts"] = {"expert-research": {"role": "조사", "skills": ["moai-pm:project"],
                                             "inputs": [], "outputs": [], "write_set": [],
                                             "verification": ["입력 대조"], "missing_context": []}}
        self.assertEqual(contract.validate(c), [])
        c["workflows"][0]["agent"] = {}
        self.assertTrue(contract.validate(c))

    def test_expert_cannot_use_unassigned_skill(self):
        c = config(); c["workflows"][0]["agent"] = "expert"
        c["experts"] = {"expert": {"role": "검수", "skills": [], "inputs": [], "outputs": [],
                                    "write_set": [], "verification": ["정독"], "missing_context": []}}
        self.assertTrue(any("배정하지" in e for e in contract.validate(c)))

    def test_invalid_enum_types_return_errors(self):
        c = config(); c["sensitivity"] = []
        self.assertTrue(contract.validate(c))
        c = config(); c["workflows"][0]["operation"] = {}
        self.assertTrue(contract.validate(c))

    def test_parallel_and_join(self):
        c = config()
        self.assertEqual(contract.validate(c), [])
        self.assertEqual(contract.plan(c)["batches"], [["design", "research"], ["join"]])
        self.assertFalse(contract.plan(c)["executed"])

    def test_overlapping_writes_are_serial(self):
        c = config()
        c["workflows"] = [stage("a", writes=["output/**"]), stage("b", writes=["output/report.md"])]
        self.assertEqual(contract.plan(c)["batches"], [["a"], ["b"]])

    def test_windows_paths_collide(self):
        self.assertTrue(contract.overlaps("output\\report.md", "output/report.md"))

    def test_normalized_and_case_insensitive_ownership_collide(self):
        self.assertTrue(contract.overlaps("./output/./Report.md", "output/report.md"))
        self.assertTrue(contract.overlaps(".", "output/report.md"))

    def test_cycle_and_unknown_dependency(self):
        c = config()
        c["workflows"][0]["depends_on"] = ["join"]
        self.assertTrue(any("순환" in e for e in contract.validate(c)))
        c["workflows"][0]["depends_on"] = ["missing"]
        self.assertTrue(contract.validate(c))

    def test_foreign_paths_rejected(self):
        for path in ("../report.md", "/tmp/report.md", "C:\\report.md", "output/../../secret"):
            c = config(); c["workflows"] = [stage("a", writes=[path])]
            self.assertTrue(contract.validate(c), path)

    def test_symlink_escape_rejected(self):
        with tempfile.TemporaryDirectory() as d, tempfile.TemporaryDirectory() as outside:
            root = Path(d)
            try:
                (root / "output").symlink_to(outside, target_is_directory=True)
            except OSError:
                self.skipTest("이 플랫폼에서 symlink 생성 권한 없음")
            c = config()
            self.assertTrue(any("심볼릭" in e for e in contract.validate(c, root)))

    def test_catalog_is_not_callable(self):
        c = config(); c["skills_available"]["moai-pm:project"]["status"] = "catalog"
        self.assertTrue(contract.validate(c))
        for s in c["workflows"]:
            s["status"] = "blocked"
        self.assertEqual(contract.validate(c), [])

    def test_failed_parent_blocks_join(self):
        c = config(); c["workflows"][0]["status"] = "failed"
        self.assertEqual(contract.plan(c)["batches"], [["design"]])
        self.assertEqual(contract.plan(c)["blocked_or_incomplete"], ["join", "research"])

    def test_no_claimed_completion_without_evidence(self):
        c = config(); c["workflows"][0]["status"] = "completed"
        self.assertTrue(contract.validate(c))
        c["workflows"][2].update(status="completed", evidence=["실행 로그"])
        self.assertTrue(contract.validate(c))

    def test_no_parallel_without_observed_permission(self):
        c = config(); c["host"]["delegation_authorized"] = False
        self.assertTrue(contract.validate(c))
        c["host"]["max_concurrent"] = 1
        self.assertEqual(contract.validate(c), [])

    def test_external_account_and_permission(self):
        c = config(); c["workflows"] = [stage("publish")]
        c["workflows"][0]["operation"] = "external_write"
        self.assertTrue(contract.validate(c))
        c["workflows"][0].update(account_ref="test-store", authorization="granted")
        self.assertEqual(contract.validate(c), [])

    def test_answer_provenance_required(self):
        c = config(); del c["context"]["answers"]["audience"]["source"]
        self.assertTrue(contract.validate(c))

    def test_invalid_dependency_type_does_not_crash(self):
        c = config(); c["workflows"][0]["depends_on"] = [{}]
        self.assertTrue(contract.validate(c))

    def test_budget_counts_utf8_and_whole_chain(self):
        with tempfile.TemporaryDirectory() as d:
            files = [Path(d) / n for n in ("parent.md", "child.md")]
            for p in files:
                p.write_text("한글", encoding="utf-8")
            result = contract.instruction_budget(files, 10)
            self.assertEqual(result["total_bytes"], 12)
            self.assertFalse(result["passed"])

    def test_rollback_preserves_later_edits(self):
        before, after = b"original", b"generated"
        self.assertEqual(contract.rollback_content(after, contract.digest(after), before), before)
        with self.assertRaises(ValueError):
            contract.rollback_content(b"user edit", contract.digest(after), before)


if __name__ == "__main__":
    unittest.main()
