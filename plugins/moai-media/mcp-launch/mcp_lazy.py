# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""정적 목록은 즉시 반환하고 첫 tools/call에서만 실제 MCP 서버를 시작한다.

stdio 전용이며 공유 데몬이나 호출 재시도를 사용하지 않는다. POSIX에서는 자신이
만든 프로세스 그룹을 정리한다. Windows는 taskkill /T /F를 사용한다. SIGKILL,
스스로 그룹을 이탈한 자식, Windows에서 부모보다 먼저 고아가 된 자식은 보장 밖이다.
"""
from __future__ import annotations

import argparse
import json
import math
import os
from pathlib import Path
import queue
import signal
import subprocess
import sys
import threading
import time
import uuid


def reader(stream, events, source):
    """Windows 파이프에서도 select 없이 읽는다. 줄 크기에 제한을 두지 않는다."""
    try:
        for line in stream:
            events.put((source, line))
    except (OSError, UnicodeError):
        pass
    finally:
        events.put((source, None))


class Writer:
    """파이프가 가득 차도 종료 이벤트 처리를 막지 않는 순서 보존 writer."""
    def __init__(self, stream, events, source):
        self.queue = queue.Queue()
        self.fd = os.dup(stream.fileno())
        self.events, self.source = events, source
        self.thread = threading.Thread(target=self.run, daemon=True)
        self.thread.start()

    def send(self, message):
        self.queue.put((json.dumps(message, ensure_ascii=False, allow_nan=False) + "\n").encode("utf-8"))

    def run(self):
        try:
            while (data := self.queue.get()) is not None:
                remaining = memoryview(data)
                while remaining:
                    remaining = remaining[os.write(self.fd, remaining):]
        except OSError:
            self.events.put((self.source, None))
        finally:
            os.close(self.fd)

    def finish(self, grace):
        self.queue.put(None)
        self.thread.join(timeout=grace)
        return not self.thread.is_alive()


def stop_child(child, grace=1.0):
    if child is None:
        return
    try:
        child.stdin.close()
    except (OSError, ValueError):
        pass
    try:
        child.wait(timeout=grace)
    except subprocess.TimeoutExpired:
        pass
    if os.name == "nt":
        if child.poll() is None:
            try:
                subprocess.run(["taskkill", "/PID", str(child.pid), "/T", "/F"],
                               stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=grace + 2)
            except (OSError, subprocess.TimeoutExpired):
                child.kill()
    else:
        # uv가 먼저 종료돼도 같은 그룹의 서버·손자 프로세스까지 정리한다.
        for sig in (signal.SIGTERM, signal.SIGKILL):
            try:
                os.killpg(child.pid, sig)
            except ProcessLookupError:
                break
            if sig == signal.SIGTERM:
                time.sleep(grace)
                child.poll()  # 종료된 그룹 리더를 회수한 뒤 남은 자식을 정리한다.
    try:
        child.wait(timeout=grace + 2)
    except subprocess.TimeoutExpired:
        child.kill()
        child.wait(timeout=2)


def valid_id(value):
    return value is None or type(value) in (int, str)


def reject_constant(_):
    raise ValueError("JSON의 비유한 수는 허용하지 않습니다.")


class Proxy:
    def __init__(self, catalog, command, timeout, grace):
        self.catalog, self.command = catalog, command
        self.timeout, self.grace = timeout, grace
        self.events = queue.Queue()
        self.child = None
        self.state = "cold"
        self.params = None
        self.initialized = False
        self.pending = {}
        self.buffered = []
        self.internal_id = None
        self.deadline = 0
        self.parent = os.getppid()
        self.host_writer = None
        self.backend_writer = None

    @staticmethod
    def send(stream, message):
        stream.write(json.dumps(message, ensure_ascii=False, allow_nan=False) + "\n")
        stream.flush()

    def error(self, ident, code, text):
        self.host_writer.send({"jsonrpc": "2.0", "id": ident, "error": {"code": code, "message": text}})

    def result(self, ident, result):
        self.host_writer.send({"jsonrpc": "2.0", "id": ident, "result": result})

    def internal(self, method, params=None):
        self.internal_id = str(uuid.uuid4())
        self.backend_writer.send({"jsonrpc": "2.0", "id": self.internal_id,
                                     "method": method, "params": params or {}})

    def start(self):
        self.child = subprocess.Popen(self.command, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                      stderr=None, text=True, encoding="utf-8", bufsize=1,
                                      start_new_session=os.name != "nt",
                                      creationflags=subprocess.CREATE_NEW_PROCESS_GROUP if os.name == "nt" else 0)
        self.state = "initializing"
        self.deadline = time.monotonic() + self.timeout
        self.backend_writer = Writer(self.child.stdin, self.events, "backend-write")
        threading.Thread(target=reader, args=(self.child.stdout, self.events, "backend"), daemon=True).start()
        self.internal("initialize", self.params)

    def client(self, message):
        if (not isinstance(message, dict) or message.get("jsonrpc") != "2.0"
                or ("id" in message and not valid_id(message["id"]))):
            self.error(None, -32600, "잘못된 JSON-RPC 요청입니다.")
            return
        ident, method = message.get("id"), message.get("method")
        if method is None:
            if self.state == "ready" and "id" in message and (("result" in message) != ("error" in message)):
                self.backend_writer.send(message)
            else:
                self.error(None, -32600, "잘못된 JSON-RPC 응답입니다.")
            return
        if not isinstance(method, str) or not isinstance(message.get("params", {}), dict):
            self.error(ident, -32600, "잘못된 JSON-RPC 요청입니다.")
            return
        params = message.get("params", {})
        if "id" not in message:
            if method == "notifications/initialized" and self.params:
                self.initialized = True
            elif self.state == "ready":
                self.backend_writer.send(message)
            elif method == "notifications/cancelled":
                cancelled = params.get("requestId")
                if not valid_id(cancelled):
                    return
                self.buffered = [m for m in self.buffered if m["id"] != cancelled]
                if cancelled in self.pending:
                    self.pending.pop(cancelled)
                    self.error(cancelled, -32800, "호출이 취소되었습니다.")
            return
        if ident in self.pending:
            self.error(ident, -32600, "진행 중인 요청 ID가 중복되었습니다.")
        elif method == "initialize":
            info, caps, version = params.get("clientInfo"), params.get("capabilities"), params.get("protocolVersion")
            if self.params is not None or not isinstance(version, str) or not isinstance(caps, dict) or not (
                isinstance(info, dict) and isinstance(info.get("name"), str) and isinstance(info.get("version"), str)
            ):
                self.error(ident, -32602, "잘못된 initialize 매개변수입니다.")
                return
            result = dict(self.catalog["initialize"])
            if version in self.catalog["supported_protocol_versions"]:
                result["protocolVersion"] = version
            self.params = dict(params, protocolVersion=result["protocolVersion"])
            self.result(ident, result)
        elif method == "ping":
            self.result(ident, {})
        elif not self.initialized:
            self.error(ident, -32000, "initialize와 initialized가 필요합니다.")
        elif self.state == "ready":
            self.pending[ident] = message
            self.backend_writer.send(message)
        elif method in self.catalog["discovery"]:
            if params.get("cursor") is not None:
                self.error(ident, -32602, "정적 목록에는 다음 페이지가 없습니다.")
            else:
                self.result(ident, self.catalog["discovery"][method])
        elif method == "tools/call":
            tools = self.catalog["discovery"]["tools/list"]["tools"]
            if not any(t["name"] == params.get("name") for t in tools) or not isinstance(params.get("arguments", {}), dict):
                self.error(ident, -32602, "알 수 없는 도구 또는 잘못된 인수입니다.")
                return
            self.pending[ident] = message
            self.buffered.append(message)
            if self.state == "cold":
                self.start()
        else:
            self.error(ident, -32601, "지원하지 않는 메서드입니다.")

    def backend(self, message):
        if (not isinstance(message, dict) or message.get("jsonrpc") != "2.0"
                or ("id" in message and not valid_id(message["id"]))):
            raise ValueError("잘못된 백엔드 메시지")
        if self.state != "ready":
            if message.get("id") != self.internal_id:
                # 초기화 중 로그·진행 알림은 전달하되 내부 응답은 호스트에 노출하지 않는다.
                if "method" in message:
                    self.host_writer.send(message)
                return
            expected = (dict(self.catalog["initialize"], protocolVersion=self.params["protocolVersion"])
                        if self.state == "initializing" else self.catalog["discovery"]["tools/list"])
            if message.get("result") != expected:
                raise ValueError("백엔드와 목록 스냅샷 불일치")
            if self.state == "initializing":
                self.backend_writer.send({"jsonrpc": "2.0", "method": "notifications/initialized"})
                self.state = "listing"
                self.internal("tools/list")
            else:
                self.state = "ready"
                for buffered in self.buffered:
                    self.backend_writer.send(buffered)
                self.buffered.clear()
            return
        if "method" not in message:
            self.pending.pop(message.get("id"), None)
        self.host_writer.send(message)

    def run(self):
        self.host_writer = Writer(sys.stdout, self.events, "host-write")
        threading.Thread(target=reader, args=(sys.stdin, self.events, "client"), daemon=True).start()
        for sig in (signal.SIGINT, signal.SIGTERM):
            signal.signal(sig, lambda *_: self.events.put(("stop", None)))
        status = 0
        try:
            while True:
                if self.state in ("initializing", "listing") and time.monotonic() > self.deadline:
                    raise TimeoutError("백엔드 초기화 제한 초과")
                if os.name != "nt" and os.getppid() != self.parent:
                    break
                try:
                    source, line = self.events.get(timeout=0.1)
                except queue.Empty:
                    continue
                if line is None:
                    if source in ("backend", "backend-write", "host-write"):
                        raise RuntimeError("백엔드 연결 종료")
                    break
                try:
                    message = json.loads(line, parse_constant=reject_constant)
                except ValueError:
                    if source == "client":
                        self.error(None, -32700, "JSON을 해석할 수 없습니다.")
                        continue
                    raise
                (self.client if source == "client" else self.backend)(message)
        except (OSError, ValueError, RuntimeError, TimeoutError):
            status = 1
        finally:
            try:
                for ident in self.pending:
                    self.error(ident, -32000, "백엔드 연결이 종료되었습니다. 호출은 자동 재시도하지 않습니다.")
            except (OSError, ValueError):
                status = 1
            if self.backend_writer:
                self.backend_writer.finish(self.grace)
            stop_child(self.child, self.grace)
            if not self.host_writer.finish(self.grace):
                status = 1
        return status


def main():
    for stream in (sys.stdin, sys.stdout, sys.stderr):
        stream.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--catalog", type=Path, required=True)
    parser.add_argument("--startup-timeout", type=float, default=30)
    parser.add_argument("--shutdown-grace", type=float, default=1)
    parser.add_argument("command", nargs=argparse.REMAINDER)
    args = parser.parse_args()
    command = args.command[1:] if args.command[:1] == ["--"] else args.command
    try:
        catalog = json.loads(args.catalog.read_text(encoding="utf-8"))
        versions = catalog["supported_protocol_versions"]
        if not (catalog["format"] == 1 and isinstance(versions, list) and versions
                and all(isinstance(v, str) for v in versions)
                and catalog["initialize"]["protocolVersion"] in versions
                and isinstance(catalog["initialize"]["capabilities"], dict)
                and isinstance(catalog["initialize"]["serverInfo"], dict)
                and isinstance(catalog["discovery"]["tools/list"]["tools"], list)
                and all(isinstance(t.get("name"), str) for t in catalog["discovery"]["tools/list"]["tools"])
                and command and all(math.isfinite(v) and v > 0 for v in (args.startup_timeout, args.shutdown_grace))):
            raise ValueError("잘못된 프록시 설정")
    except (OSError, ValueError, KeyError, TypeError, AttributeError):
        print("MCP 프록시 설정 또는 목록 스냅샷이 잘못되었습니다.", file=sys.stderr)
        return 2
    return Proxy(catalog, command, args.startup_timeout, args.shutdown_grace).run()


if __name__ == "__main__":
    raise SystemExit(main())
