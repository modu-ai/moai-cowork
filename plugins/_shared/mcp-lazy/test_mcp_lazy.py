"""실제 stdio 프로세스로 지연 시작·메시지 보존·종료를 검증한다."""
from __future__ import annotations

import importlib.util
import json
import os
from pathlib import Path
import queue
import signal
import subprocess
import sys
import threading
import time

import pytest

PROXY = Path(__file__).with_name("mcp_lazy.py")
VERSION = "2025-11-25"
TOOLS = {"tools": [{"name": "echo", "description": "원문 반환", "inputSchema": {"type": "object"}}]}
INIT = {"protocolVersion": VERSION, "capabilities": {"tools": {"listChanged": False}},
        "serverInfo": {"name": "fake", "version": "1"}, "instructions": "fake instructions"}
DISCOVERY = {"tools/list": TOOLS, "resources/list": {"resources": []},
             "resources/templates/list": {"resourceTemplates": []}, "prompts/list": {"prompts": []}}
BACKEND = r'''
import json, os, subprocess, sys, time
from pathlib import Path
marker, mode = sys.argv[1:]
with open(marker, "a") as f:
    f.write(str(os.getpid()) + "\n")
def send(message):
    print(json.dumps(message), flush=True)
init = json.loads(os.environ["FAKE_INIT"])
tools = json.loads(os.environ["FAKE_TOOLS"])
child = None
if mode == "descendant":
    child = subprocess.Popen([sys.executable, "-c", "import time; time.sleep(120)"])
    Path(marker + ".child").write_text(str(child.pid))
for line in sys.stdin:
    msg = json.loads(line)
    with open(marker + ".messages", "a") as f:
        f.write(line)
    method = msg.get("method")
    if method == "initialize":
        if mode == "slow": time.sleep(0.3)
        if mode == "timeout": time.sleep(120)
        result = dict(init, protocolVersion=msg["params"]["protocolVersion"])
        if mode == "version": result["protocolVersion"] = "future-invalid"
        if mode == "capabilities": result["capabilities"] = {}
        send({"jsonrpc": "2.0", "id": msg["id"], "result": result})
    elif method == "tools/list":
        result = {"tools": []} if mode == "schema" else tools
        send({"jsonrpc": "2.0", "id": msg["id"], "result": result})
    elif method == "tools/call":
        Path(marker + ".called").write_text("called")
        if mode == "crash": sys.exit(7)
        if mode in ("hang", "descendant"): time.sleep(120)
        if mode == "huge":
            send({"jsonrpc": "2.0", "id": msg["id"], "result": {"content": [{"type": "image", "data": "a" * 2000000, "mimeType": "image/png"}]}})
            continue
        token = msg.get("params", {}).get("_meta", {}).get("progressToken")
        if token is not None:
            send({"jsonrpc": "2.0", "method": "notifications/progress", "params": {"progressToken": token, "progress": 1}})
        send({"jsonrpc": "2.0", "id": msg["id"], "result": {"content": [{"type": "text", "text": json.dumps(msg["params"])}]}})
    elif method == "client-roundtrip":
        send({"jsonrpc": "2.0", "id": "backend-question", "method": "ping"})
    elif msg.get("id") == "backend-question":
        send({"jsonrpc": "2.0", "method": "notifications/roundtrip", "params": msg})
'''


class Host:
    def __init__(self, tmp_path, mode="normal", timeout=2, read_output=True):
        self.read_output = read_output
        self.marker = tmp_path / "starts"
        backend = tmp_path / "backend.py"
        backend.write_text(BACKEND, encoding="utf-8")
        catalog = tmp_path / "catalog.json"
        catalog.write_text(json.dumps({"format": 1, "supported_protocol_versions": ["2024-11-05", VERSION],
                                      "initialize": INIT, "discovery": DISCOVERY}), encoding="utf-8")
        env = dict(os.environ, FAKE_INIT=json.dumps(INIT), FAKE_TOOLS=json.dumps(TOOLS))
        self.process = subprocess.Popen(
            [sys.executable, str(PROXY), "--catalog", str(catalog), "--startup-timeout", str(timeout),
             "--shutdown-grace", "0.1", "--", sys.executable, str(backend), str(self.marker), mode],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding="utf-8", env=env,
        )
        self.messages = queue.Queue()
        def read():
            for line in self.process.stdout:
                self.messages.put(json.loads(line))
        if read_output:
            threading.Thread(target=read, daemon=True).start()

    def send(self, message):
        self.process.stdin.write(json.dumps(message) + "\n")
        self.process.stdin.flush()

    def receive(self):
        if not self.read_output:
            return json.loads(self.process.stdout.readline())
        try:
            return self.messages.get(timeout=4)
        except queue.Empty:
            if self.process.poll() is not None:
                pytest.fail(self.process.stderr.read())
            raise

    def request(self, ident, method, params=None):
        self.send({"jsonrpc": "2.0", "id": ident, "method": method, "params": params or {}})

    def initialize(self, version=VERSION):
        self.request(0, "initialize", {"protocolVersion": version, "capabilities": {"sampling": {}},
                                       "clientInfo": {"name": "test-host", "version": "7"}})
        reply = self.receive()
        self.send({"jsonrpc": "2.0", "method": "notifications/initialized"})
        return reply

    def call(self, ident=1, meta=None):
        params = {"name": "echo", "arguments": {"message": "안녕"}}
        if meta: params["_meta"] = meta
        self.request(ident, "tools/call", params)

    def close(self):
        if self.process.stdin and not self.process.stdin.closed:
            self.process.stdin.close()
        try:
            self.process.wait(timeout=4)
        except subprocess.TimeoutExpired:
            self.process.kill()
            self.process.wait(timeout=2)
        # 실패한 검증에서도 이 테스트가 띄운 서버·손자를 정리한다.
        if self.marker.exists():
            for pid in map(int, self.marker.read_text().splitlines()):
                if os.name == "nt":
                    subprocess.run(["taskkill", "/PID", str(pid), "/T", "/F"],
                                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=3)
                else:
                    try:
                        os.killpg(pid, signal.SIGKILL)
                    except ProcessLookupError:
                        pass
        self.process.stdout.close()
        self.process.stderr.close()


@pytest.fixture
def host(tmp_path):
    hosts = []
    def make(mode="normal", timeout=2, **kwargs):
        path = tmp_path / str(len(hosts))
        path.mkdir()
        instance = Host(path, mode, timeout, **kwargs)
        hosts.append(instance)
        return instance
    yield make
    for instance in hosts:
        instance.close()


def test_discovery_and_ping_do_not_spawn_backend(host):
    h = host()
    assert h.initialize()["result"] == INIT
    for i, (method, expected) in enumerate(DISCOVERY.items(), 1):
        h.request(i, method)
        assert h.receive() == {"jsonrpc": "2.0", "id": i, "result": expected}
    h.request(10, "ping")
    assert h.receive()["result"] == {}
    assert not h.marker.exists()


def test_first_overlapping_calls_start_once_replay_original_init_and_preserve_progress(host):
    h = host("slow")
    h.initialize()
    h.call(1, {"progressToken": "progress-1", "trace": {"keep": True}})
    h.call(2)
    replies = [h.receive() for _ in range(3)]
    assert replies[0]["params"]["progressToken"] == "progress-1"
    results = {r["id"]: r for r in replies if "id" in r}
    assert set(results) == {1, 2}
    assert json.loads(results[1]["result"]["content"][0]["text"])["_meta"]["trace"] == {"keep": True}
    assert len(h.marker.read_text().splitlines()) == 1
    messages = [json.loads(s) for s in Path(str(h.marker) + ".messages").read_text().splitlines()]
    assert messages[0]["params"]["clientInfo"] == {"name": "test-host", "version": "7"}
    assert messages[0]["params"]["capabilities"] == {"sampling": {}}
    assert isinstance(messages[0]["id"], str)
    assert [m["method"] for m in messages[:3]] == ["initialize", "notifications/initialized", "tools/list"]


def test_cancel_before_ready_removes_queued_call_without_starting_for_cancel(host):
    h = host("slow")
    h.initialize()
    h.send({"jsonrpc": "2.0", "method": "notifications/cancelled", "params": {"requestId": 99}})
    h.request(9, "ping")
    assert h.receive()["id"] == 9
    assert not h.marker.exists()
    h.call(1)
    h.send({"jsonrpc": "2.0", "method": "notifications/cancelled", "params": {"requestId": 1}})
    h.call(2)
    replies = [h.receive(), h.receive()]
    assert {m["id"] for m in replies} == {1, 2}
    assert next(m for m in replies if m["id"] == 1)["error"]["code"] == -32800
    messages = Path(str(h.marker) + ".messages").read_text()
    assert '"id": 1,' not in messages


def test_invalid_boolean_cancel_id_does_not_cancel_integer_call(host):
    h = host("slow")
    h.initialize()
    h.call(1)
    h.send({"jsonrpc": "2.0", "method": "notifications/cancelled", "params": {"requestId": True}})
    assert h.receive()["id"] == 1


def test_backend_failure_explicitly_fails_pending_without_replay(host):
    h = host("crash")
    h.initialize()
    h.call(1)
    h.call(2)
    assert all("error" in h.receive() for _ in range(2))
    assert h.process.wait(timeout=4) != 0
    assert len(h.marker.read_text().splitlines()) == 1


@pytest.mark.parametrize("mode", ["version", "capabilities", "schema", "timeout"])
def test_snapshot_mismatch_and_startup_timeout_do_not_execute_calls(host, mode):
    h = host(mode, timeout=0.4)
    h.initialize()
    h.call()
    assert "error" in h.receive()
    assert h.process.wait(timeout=4) != 0
    assert '"tools/call"' not in Path(str(h.marker) + ".messages").read_text()


def test_invalid_requests_unsupported_version_and_unknown_tool(host):
    h = host()
    h.process.stdin.write("not-json\n[]\n")
    h.process.stdin.flush()
    assert h.receive()["error"]["code"] == -32700
    assert h.receive()["error"]["code"] == -32600
    h.request(8, "initialize", {"protocolVersion": 123})
    assert h.receive()["error"]["code"] == -32602
    assert h.initialize("future-unknown")["result"]["protocolVersion"] == VERSION
    h.request(2, "tools/call", {"name": "unknown"})
    assert "error" in h.receive()
    assert not h.marker.exists()


def test_ready_proxy_forwards_server_requests_and_client_responses(host):
    h = host()
    h.initialize()
    h.call()
    h.receive()
    h.request(2, "client-roundtrip")
    assert h.receive()["id"] == "backend-question"
    response = {"jsonrpc": "2.0", "id": "backend-question", "result": {}}
    h.send(response)
    assert h.receive()["params"] == response


def wait_started(h, suffix=""):
    path = Path(str(h.marker) + suffix)
    deadline = time.monotonic() + 4
    while not path.exists() and time.monotonic() < deadline:
        time.sleep(0.01)
    assert path.exists()
    return int(path.read_text().strip())


def wait_called(h):
    deadline = time.monotonic() + 4
    while not Path(str(h.marker) + ".called").exists() and time.monotonic() < deadline:
        time.sleep(0.01)
    assert Path(str(h.marker) + ".called").exists()


def assert_dead(pid):
    deadline = time.monotonic() + 4
    while time.monotonic() < deadline:
        if os.name == "nt":
            import ctypes
            kernel = ctypes.WinDLL("kernel32", use_last_error=True)
            kernel.OpenProcess.restype = ctypes.c_void_p
            kernel.WaitForSingleObject.argtypes = [ctypes.c_void_p, ctypes.c_ulong]
            kernel.CloseHandle.argtypes = [ctypes.c_void_p]
            handle = kernel.OpenProcess(0x00100000, False, pid)
            if not handle:
                if ctypes.get_last_error() == 87:
                    return
                raise ctypes.WinError(ctypes.get_last_error())
            try:
                if kernel.WaitForSingleObject(handle, 0) == 0:
                    return
            finally:
                kernel.CloseHandle(handle)
        else:
            try:
                os.kill(pid, 0)
            except ProcessLookupError:
                return
        time.sleep(0.02)
    pytest.fail(f"프로세스가 종료되지 않음: {pid}")


def test_host_eof_while_tool_hangs_cleans_child(host):
    h = host("hang")
    h.initialize()
    h.call()
    pid = wait_started(h)
    h.process.stdin.close()
    h.process.wait(timeout=4)
    assert_dead(pid)


def blocked_backend_writer(host):
    h = host("hang")
    h.initialize()
    h.call(1)
    pid = wait_started(h)
    wait_called(h)
    h.request(2, "tools/call", {"name": "echo", "arguments": {"payload": "x" * 2_000_000}})
    time.sleep(0.1)
    return h, pid


def test_host_eof_during_backend_write_backpressure_cleans_child_and_fails_pending(host):
    h, pid = blocked_backend_writer(host)
    h.process.stdin.close()
    assert h.process.wait(timeout=3) == 0
    assert_dead(pid)
    replies = [h.receive(), h.receive()]
    assert {r["id"] for r in replies} == {1, 2}
    assert all("error" in r for r in replies)


@pytest.mark.skipif(os.name == "nt", reason="POSIX 종료 신호 검증")
@pytest.mark.parametrize("sig", [signal.SIGTERM, signal.SIGINT])
def test_signal_during_backend_write_backpressure_cleans_child(host, sig):
    h, pid = blocked_backend_writer(host)
    h.process.send_signal(sig)
    assert h.process.wait(timeout=3) == 0
    assert_dead(pid)
    assert "Fatal Python error" not in h.process.stderr.read()


@pytest.mark.skipif(os.name == "nt", reason="POSIX 종료 신호 검증")
def test_signal_during_host_stdout_backpressure_cleans_child(host):
    h = host("huge", read_output=False)
    h.initialize()
    h.call()
    pid = wait_started(h)
    wait_called(h)
    time.sleep(0.1)
    h.process.send_signal(signal.SIGTERM)
    h.process.wait(timeout=3)
    assert_dead(pid)
    assert "Fatal Python error" not in h.process.stderr.read()


@pytest.mark.skipif(os.name == "nt", reason="POSIX 프로세스 그룹 신호 검증")
@pytest.mark.parametrize("sig", [signal.SIGTERM, signal.SIGINT])
def test_signal_reaps_own_backend_and_descendants(host, sig):
    h = host("descendant")
    h.initialize()
    h.call()
    pid = wait_started(h)
    child_pid = wait_started(h, ".child")
    h.process.send_signal(sig)
    code = h.process.wait(timeout=4)
    stderr = h.process.stderr.read()
    assert code == 0, stderr
    assert "Fatal Python error" not in stderr
    assert_dead(pid)
    assert_dead(child_pid)


def test_large_tool_payload_is_not_truncated(host):
    h = host()
    h.initialize()
    value = "a" * 2_000_000
    h.request(1, "tools/call", {"name": "echo", "arguments": {"image": value}})
    assert json.loads(h.receive()["result"]["content"][0]["text"])["arguments"]["image"] == value


def generator_module():
    path = PROXY.parents[3] / "scripts" / "sync-mcp-lazy.py"
    spec = importlib.util.spec_from_file_location("sync_mcp_lazy", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_generator_digest_normalizes_crlf_and_detects_source_or_lock_change(tmp_path):
    generator = generator_module()
    source = tmp_path / "src" / "package.py"
    source.parent.mkdir()
    source.write_bytes(b"value = 1\n")
    (tmp_path / "pyproject.toml").write_text("[project]\n", encoding="utf-8")
    lock = tmp_path / "uv.lock"
    lock.write_bytes(b"version = 1\n")
    digest = generator.source_digest(tmp_path)
    source.write_bytes(b"value = 1\r\n")
    assert generator.source_digest(tmp_path) == digest
    source.write_bytes(b"value = 2\n")
    assert generator.source_digest(tmp_path) != digest
    source.write_bytes(b"value = 1\n")
    lock.write_bytes(b"version = 2\n")
    assert generator.source_digest(tmp_path) != digest


def test_generator_rejects_dynamic_or_nonempty_resource_discovery():
    generator = generator_module()
    catalog = {"format": 1, "initialize": INIT, "discovery": DISCOVERY,
               "supported_protocol_versions": [VERSION]}
    generator.validate_catalog(catalog)
    for mutation in (
        {"initialize": dict(INIT, capabilities={"tools": {"listChanged": True}})},
        {"discovery": dict(DISCOVERY, **{"resources/list": {"resources": [{"uri": "x"}]}})},
        {"discovery": dict(DISCOVERY, **{"tools/list": dict(TOOLS, nextCursor="next")})},
    ):
        with pytest.raises(ValueError):
            generator.validate_catalog(dict(catalog, **mutation))
