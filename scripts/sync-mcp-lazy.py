#!/usr/bin/env python3
"""실제 SDK stdio 응답으로 자체 MCP 서버의 지연 시작 목록을 생성한다.

기본 실행은 생성·복제, --check는 백엔드를 실행하지 않는 정합 검사,
--verify는 잠긴 의존성으로 실제 SDK 응답까지 비교한다. --server로 범위를 좁힌다.
스냅샷은 도구만 제공하고 목록 변경·구독을 지원하지 않는 서버에 한해 생성한다.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import queue
import subprocess
import sys
import tempfile
import threading
import time
import tomllib
import uuid

ROOT = Path(__file__).resolve().parent.parent
CANONICAL = ROOT / "plugins" / "_shared" / "mcp-lazy" / "mcp_lazy.py"
SERVERS = {"moai-mcp-ip", "moai-mcp-openai", "moai-mcp-threads-poster",
           "moai-mcp-smartstore", "moai-mcp-imweb", "moai-mcp-cafe24"}
LISTS = {"tools/list": "tools", "resources/list": "resources",
         "resources/templates/list": "resourceTemplates", "prompts/list": "prompts"}


def source_digest(server):
    """OS 체크아웃의 CRLF 차이는 제외하고 런타임 소스·의존성을 묶는다."""
    paths = [server / "pyproject.toml", server / "uv.lock", *server.glob("src/**/*.py")]
    digest = hashlib.sha256()
    for path in sorted(paths):
        data = path.read_bytes().replace(b"\r\n", b"\n")
        digest.update(path.relative_to(server).as_posix().encode("utf-8") + b"\0")
        digest.update(str(len(data)).encode("ascii") + b"\0" + data)
    return digest.hexdigest()


def validate_catalog(catalog):
    """정적 도구 목록으로 안전하게 응답할 수 있는 범위인지 검사한다."""
    if catalog.get("format") != 1:
        raise ValueError("지원하지 않는 목록 형식")
    initialize = catalog["initialize"]
    versions = catalog["supported_protocol_versions"]
    if not versions or not all(isinstance(v, str) for v in versions) or initialize["protocolVersion"] not in versions:
        raise ValueError("SDK 프로토콜 버전 정보 불일치")
    caps = initialize["capabilities"]
    for name, value in caps.items():
        if name not in {"tools", "resources", "prompts", "experimental"} and value is not None:
            raise ValueError("도구 전용 서버가 아님")
        if name == "experimental" and value:
            raise ValueError("실험 기능은 지연 시작 대상이 아님")
        if isinstance(value, dict) and (value.get("listChanged") or value.get("subscribe")):
            raise ValueError("동적 목록 또는 구독 지원 서버")
    for method, field in LISTS.items():
        result = catalog["discovery"][method]
        if not isinstance(result.get(field), list) or result.get("nextCursor") is not None:
            raise ValueError("페이지가 있거나 잘못된 목록")
        if method != "tools/list" and result[field]:
            raise ValueError("리소스·프롬프트를 제공하는 서버")
    tools = catalog["discovery"]["tools/list"]["tools"]
    names = [tool["name"] for tool in tools]
    if not tools or len(names) != len(set(names)) or not all(isinstance(name, str) for name in names):
        raise ValueError("도구 이름이 비었거나 중복됨")


def proxy_helpers():
    spec = importlib.util.spec_from_file_location("mcp_lazy", CANONICAL)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def isolated_env(home):
    # 자격증명 변수·MOAI 경로·PYTHONPATH를 상속하지 않는다.
    keys = {"PATH", "SYSTEMROOT", "WINDIR", "COMSPEC", "PATHEXT", "TEMP", "TMP", "LANG", "LC_ALL",
            "UV_CACHE_DIR", "UV_PYTHON_INSTALL_DIR"}
    env = {key: value for key, value in os.environ.items() if key.upper() in keys}
    env.update({key: str(home) for key in ("HOME", "USERPROFILE", "APPDATA", "LOCALAPPDATA",
                                          "XDG_CONFIG_HOME", "XDG_CACHE_HOME")})
    env["PYTHONIOENCODING"] = "utf-8"
    env["UV_NO_PROGRESS"] = "1"
    return env


class Session:
    def __init__(self, command, env, timeout, helper):
        self.helper, self.timeout = helper, timeout
        self.events = queue.Queue()
        self.child = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                      stderr=None, text=True, encoding="utf-8", bufsize=1, env=env,
                                      start_new_session=os.name != "nt",
                                      creationflags=subprocess.CREATE_NEW_PROCESS_GROUP if os.name == "nt" else 0)
        threading.Thread(target=helper.reader, args=(self.child.stdout, self.events, "sdk"), daemon=True).start()

    def receive(self):
        _, line = self.events.get(timeout=self.timeout)
        if line is None:
            raise ValueError("SDK 연결 종료")
        return json.loads(line)

    def request(self, method, params=None):
        ident = str(uuid.uuid4())
        self.helper.Proxy.send(self.child.stdin, {"jsonrpc": "2.0", "id": ident,
                                                  "method": method, "params": params or {}})
        deadline = time.monotonic() + self.timeout
        while time.monotonic() < deadline:
            reply = self.receive()
            if reply.get("id") == ident:
                if "error" in reply:
                    raise ValueError(f"SDK 요청 실패: {method}")
                return reply["result"]
            if "id" in reply or reply.get("method", "").endswith("list_changed"):
                raise ValueError("동적 SDK 동작은 지연 시작 대상이 아님")
        raise TimeoutError("SDK 응답 제한 초과")

    def close(self):
        self.helper.stop_child(self.child)
        self.child.stdout.close()


def snapshot(server, python, timeout):
    project = tomllib.loads((server / "pyproject.toml").read_text(encoding="utf-8"))["project"]
    name = project["name"]
    if name not in project["scripts"]:
        raise ValueError("프로젝트 이름과 일치하는 진입점 없음")
    helper = proxy_helpers()
    uv = ["uv", "run", "--locked", "--python", python, "--directory", str(server)]
    with tempfile.TemporaryDirectory(prefix="moai-catalog-") as directory:
        env = isolated_env(Path(directory))
        metadata = Session(uv + ["python", "-c",
            "import json,importlib.metadata; from mcp.shared.version import SUPPORTED_PROTOCOL_VERSIONS; "
            "from mcp.types import LATEST_PROTOCOL_VERSION; "
            "print(json.dumps({'versions':SUPPORTED_PROTOCOL_VERSIONS,'latest':LATEST_PROTOCOL_VERSION,"
            "'sdk_version':importlib.metadata.version('mcp')}),flush=True)"], env, timeout, helper)
        try:
            versions = metadata.receive()
        finally:
            metadata.close()
        session = Session(uv + [name], env, timeout, helper)
        try:
            initialize = session.request("initialize", {
                "protocolVersion": versions["latest"], "capabilities": {},
                "clientInfo": {"name": "moai-catalog", "version": "1"}})
            helper.Proxy.send(session.child.stdin, {"jsonrpc": "2.0", "method": "notifications/initialized"})
            discovery = {method: session.request(method) for method in LISTS}
            if discovery["tools/list"] != session.request("tools/list"):
                raise ValueError("반복 조회한 도구 목록이 달라짐")
        finally:
            session.close()
    catalog = {"format": 1, "source_digest": source_digest(server), "sdk_version": versions["sdk_version"],
               "supported_protocol_versions": versions["versions"], "initialize": initialize, "discovery": discovery}
    validate_catalog(catalog)
    return catalog


def main():
    for stream in (sys.stdout, sys.stderr):
        stream.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--verify", action="store_true")
    parser.add_argument("--server", choices=sorted(SERVERS))
    parser.add_argument("--python", default=sys.executable if sys.version_info[:2] == (3, 11) else "3.11",
                        help="SDK 스냅샷용 Python 버전 또는 경로")
    parser.add_argument("--timeout", type=float, default=120)
    args = parser.parse_args()
    servers = [p.parent for p in sorted(ROOT.glob("plugins/*/mcp-servers/*/pyproject.toml"))
               if p.parent.name in SERVERS and (not args.server or p.parent.name == args.server)]
    if len(servers) != (1 if args.server else len(SERVERS)):
        parser.error("자체 MCP 서버 구성이 예상과 다릅니다.")
    failed = False
    for server in servers:
        try:
            path = server / "mcp-catalog.json"
            if args.check or args.verify:
                current = json.loads(path.read_text(encoding="utf-8"))
                validate_catalog(current)
                if current["source_digest"] != source_digest(server):
                    raise ValueError("소스·lockfile 변경 후 목록을 생성하지 않음")
                if args.verify and current != snapshot(server, args.python, args.timeout):
                    raise ValueError("실제 SDK 응답과 스냅샷 불일치")
            else:
                path.write_text(json.dumps(snapshot(server, args.python, args.timeout), ensure_ascii=False,
                                           indent=2) + "\n", encoding="utf-8", newline="\n")
            print(f"정합: {server.name}" if args.check or args.verify else f"생성: {server.name}")
        except (OSError, ValueError, KeyError, TypeError, queue.Empty, subprocess.SubprocessError) as exc:
            print(f"불일치: {server.name}: {exc}", file=sys.stderr)
            failed = True
    owners = sorted({server.parent.parent for server in servers})
    canonical = CANONICAL.read_text(encoding="utf-8")
    for owner in owners:
        target = owner / "mcp-launch" / CANONICAL.name
        if args.check or args.verify:
            if not target.is_file() or target.read_text(encoding="utf-8") != canonical:
                print(f"프록시 복제본 불일치: {target.relative_to(ROOT)}", file=sys.stderr)
                failed = True
        elif not failed:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(canonical, encoding="utf-8", newline="\n")
    return int(failed)


if __name__ == "__main__":
    raise SystemExit(main())
