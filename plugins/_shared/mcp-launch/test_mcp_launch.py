"""런처 자격증명 해석 테스트.

핵심은 '자리표시자가 들어 있던 키는 남기지 않고 지운다' 이다. 남겨두면 제3자 서버가
`${DART_API_KEY}` 라는 문자열을 진짜 키로 믿고, 실패가 "키 없음" 이 아니라 "키 틀림" 으로
보인다.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))

import mcp_launch  # noqa: E402


@pytest.fixture(autouse=True)
def creds_dir(tmp_path, monkeypatch):
    monkeypatch.setattr(mcp_launch, "CREDENTIALS_DIR", tmp_path)
    return tmp_path


def write(creds_dir: Path, service: str, payload) -> None:
    (creds_dir / f"{service}.json").write_text(
        json.dumps(payload) if not isinstance(payload, str) else payload,
        encoding="utf-8",
    )


class TestIsUnset:
    @pytest.mark.parametrize(
        "value", [None, "", "  ", "${DART_API_KEY}", "${user_config.DART_API_KEY}"]
    )
    def test_미설정(self, value):
        assert mcp_launch.is_unset(value) is True

    def test_설정됨(self):
        assert mcp_launch.is_unset("real") is False


class TestReadCredentials:
    def test_파일이_없으면_빈_사전(self):
        assert mcp_launch.read_credentials("없는서비스") == {}

    def test_깨진_JSON_은_빈_사전(self, creds_dir):
        write(creds_dir, "dart", "{ 깨짐")
        assert mcp_launch.read_credentials("dart") == {}

    def test_객체가_아니면_빈_사전(self, creds_dir):
        write(creds_dir, "dart", ["배열"])
        assert mcp_launch.read_credentials("dart") == {}

    def test_읽는다(self, creds_dir):
        write(creds_dir, "dart", {"DART_API_KEY": "k"})
        assert mcp_launch.read_credentials("dart") == {"DART_API_KEY": "k"}


class TestResolveEnv:
    def test_자리표시자를_파일값으로_바꾼다(self, creds_dir, monkeypatch):
        write(creds_dir, "dart", {"DART_API_KEY": "real-key"})
        monkeypatch.setenv("DART_API_KEY", "${DART_API_KEY}")
        env = mcp_launch.resolve_env("dart", ["DART_API_KEY"])
        assert env["DART_API_KEY"] == "real-key"

    def test_진짜_환경변수는_건드리지_않는다(self, creds_dir, monkeypatch):
        write(creds_dir, "dart", {"DART_API_KEY": "from-file"})
        monkeypatch.setenv("DART_API_KEY", "from-env")
        env = mcp_launch.resolve_env("dart", ["DART_API_KEY"])
        assert env["DART_API_KEY"] == "from-env"

    def test_둘_다_없으면_키를_지운다(self, monkeypatch):
        monkeypatch.setenv("DART_API_KEY", "${DART_API_KEY}")
        env = mcp_launch.resolve_env("dart", ["DART_API_KEY"])
        assert "DART_API_KEY" not in env

    def test_빈_환경변수도_파일로_대체된다(self, creds_dir, monkeypatch):
        # Claude 의 ${user_config.KEY} 는 미입력 시 빈 문자열이 된다.
        write(creds_dir, "dart", {"DART_API_KEY": "real-key"})
        monkeypatch.setenv("DART_API_KEY", "")
        assert mcp_launch.resolve_env("dart", ["DART_API_KEY"])["DART_API_KEY"] == "real-key"

    def test_다른_환경변수는_보존된다(self, monkeypatch):
        monkeypatch.setenv("PATH", "/somewhere")
        env = mcp_launch.resolve_env("dart", ["DART_API_KEY"])
        assert env["PATH"] == "/somewhere"

    def test_여러_키를_한번에(self, creds_dir, monkeypatch):
        write(creds_dir, "el", {"A": "a", "B": "b"})
        monkeypatch.setenv("A", "${A}")
        monkeypatch.delenv("B", raising=False)
        env = mcp_launch.resolve_env("el", ["A", "B"])
        assert (env["A"], env["B"]) == ("a", "b")


def test_명령이_없으면_거부한다(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["mcp_launch.py", "--service", "dart", "--keys", "K"])
    with pytest.raises(SystemExit):
        mcp_launch.main()


def test_끝까지_실행된다(creds_dir, monkeypatch, tmp_path):
    """자격증명을 채우고 자식 명령까지 전달한다."""
    write(creds_dir, "dart", {"DART_API_KEY": "real-key"})
    seen = {}

    def fake_launch(argv, env, *, windows):
        seen["argv"] = argv
        seen["key"] = env.get("DART_API_KEY")
        return 0

    monkeypatch.setattr(mcp_launch, "launch_command", fake_launch)
    monkeypatch.setenv("DART_API_KEY", "${DART_API_KEY}")
    monkeypatch.setattr(
        sys,
        "argv",
        ["mcp_launch.py", "--service", "dart", "--keys", "DART_API_KEY", "--", "npx", "-y", "x"],
    )
    assert mcp_launch.main() == 0
    assert seen["argv"] == ["npx", "-y", "x"]
    assert seen["key"] == "real-key"


def test_자식의_구분자는_보존한다(monkeypatch):
    seen = {}

    def fake_launch(argv, env, *, windows):
        seen["argv"] = argv
        return 0

    monkeypatch.setattr(mcp_launch, "launch_command", fake_launch)
    monkeypatch.setattr(
        sys,
        "argv",
        ["mcp_launch.py", "--service", "dart", "--keys", "DART_API_KEY", "--", "npx", "-y", "tool", "--", "--child-option"],
    )
    assert mcp_launch.main() == 0
    assert seen["argv"] == ["npx", "-y", "tool", "--", "--child-option"]


def test_posix_자식으로_대체한다(monkeypatch):
    seen = {}

    def fake_exec(file, argv, env):
        seen["argv"] = argv
        raise OSError("stop")

    monkeypatch.setattr(mcp_launch.os, "execvpe", fake_exec)
    assert mcp_launch.launch_command(["npx", "-y", "tool"], {}, windows=False) == 127
    assert seen["argv"] == ["npx", "-y", "tool"]


def test_windows_cmd_런처를_찾고_종료코드를_전달한다(monkeypatch):
    seen = {}

    def fake_which(name, *, path):
        seen["which"] = (name, path)
        return "C:\\tools\\npx.cmd"

    def fake_run(argv, *, env, check):
        seen["argv"] = argv
        seen["env"] = env
        return SimpleNamespace(returncode=7)

    monkeypatch.setattr(mcp_launch.shutil, "which", fake_which)
    monkeypatch.setattr(mcp_launch.subprocess, "run", fake_run)
    env = {"PATH": "C:\\tools"}
    assert mcp_launch.launch_command(["npx", "-y", "tool"], env, windows=True) == 7
    assert seen == {"which": ("npx", "C:\\tools"), "argv": ["C:\\tools\\npx.cmd", "-y", "tool"], "env": env}


def test_배포된_플러그인_런처가_공용본과_같다():
    plugins = Path(__file__).resolve().parents[2]
    source = (plugins / "_shared/mcp-launch/mcp_launch.py").read_bytes()
    for name in ("moai-accountant", "moai-analyst", "moai-coworker", "moai-media"):
        assert (plugins / name / "mcp-launch/mcp_launch.py").read_bytes() == source


@pytest.mark.parametrize("service,keys", [("../secret", "K"), ("dart", "BAD.NAME"), ("dart", ",")])
def test_잘못된_이름은_거부한다(monkeypatch, service, keys):
    monkeypatch.setattr(sys, "argv", ["mcp_launch.py", "--service", service, "--keys", keys, "--", "npx"])
    with pytest.raises(SystemExit) as error:
        mcp_launch.main()
    assert error.value.code == 2
