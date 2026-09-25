"""TokenStore — 영속화와 폴백."""

from __future__ import annotations

import json
import threading

from moai_mcp_core import tokenstore
from moai_mcp_core.tokenstore import TokenStore


def test_저장한_토큰을_다시_읽는다(tmp_path):
    store = TokenStore("youtube", path=tmp_path / "youtube-tokens.json")
    assert store.save({"access_token": "abc", "refresh_token": "xyz"}) is True

    reloaded = TokenStore("youtube", path=tmp_path / "youtube-tokens.json")
    assert reloaded.load() == {"access_token": "abc", "refresh_token": "xyz"}


def test_갱신_잠금은_다른_클라이언트의_진입을_기다린다(tmp_path):
    path = tmp_path / "shared.json"
    first = TokenStore("shared", path=path)
    second = TokenStore("shared", path=path)
    started = threading.Event()
    entered = threading.Event()
    errors = []

    def wait_for_lock():
        started.set()
        try:
            with second.refresh_lock(timeout=2):
                entered.set()
        except Exception as exc:
            errors.append(exc)

    thread = threading.Thread(target=wait_for_lock)
    with first.refresh_lock():
        thread.start()
        assert started.wait(1)
        assert not entered.wait(0.1)
    thread.join(2)
    assert not thread.is_alive()
    assert not errors
    assert entered.is_set()


def test_파일이_없으면_빈_딕셔너리(tmp_path):
    store = TokenStore("youtube", path=tmp_path / "없는파일.json")
    assert store.load() == {}


def test_손상된_파일은_없는_것으로_취급한다(tmp_path):
    path = tmp_path / "broken.json"
    path.write_text("{이건 JSON이 아니다", encoding="utf-8")

    store = TokenStore("youtube", path=path)
    assert store.load() == {}
    # 그리고 저장은 정상 동작해야 한다 — 손상 파일이 영구 장애가 되면 안 된다.
    assert store.save({"access_token": "새것"}) is True
    assert json.loads(path.read_text(encoding="utf-8"))["access_token"] == "새것"


def test_쓰기_불가_경로면_인메모리로_폴백한다(tmp_path):
    # 파일을 디렉터리 자리에 놓아 mkdir 를 실패시킨다.
    blocker = tmp_path / "blocked"
    blocker.write_text("파일", encoding="utf-8")

    store = TokenStore("youtube", path=blocker / "tokens.json")
    assert store.save({"access_token": "메모리"}) is False
    assert store.persistent is False
    # 폴백 상태에서도 값은 살아 있어야 한다 — 서버가 계속 돌아가야 하므로.
    assert store.load() == {"access_token": "메모리"}


def test_환경변수로_경로를_덮어쓴다(tmp_path, monkeypatch):
    target = tmp_path / "커스텀.json"
    monkeypatch.setenv("YOUTUBE_TOKEN_FILE", str(target))

    store = TokenStore("youtube", env_var="YOUTUBE_TOKEN_FILE")
    assert store.path == target
    store.save({"access_token": "a"})
    assert target.exists()


def test_한글_값도_그대로_보존한다(tmp_path):
    path = tmp_path / "tokens.json"
    store = TokenStore("youtube", path=path)
    store.save({"채널명": "모두의 코워크"})

    raw = path.read_text(encoding="utf-8")
    assert "모두의 코워크" in raw  # ensure_ascii 이스케이프가 아니라 그대로여야 한다
    assert store.load()["채널명"] == "모두의 코워크"


def test_clear_는_파일이_없어도_실패하지_않는다(tmp_path):
    store = TokenStore("youtube", path=tmp_path / "tokens.json")
    store.clear()  # 파일 없음
    store.save({"a": 1})
    store.clear()
    assert store.load() == {}


def test_동시_저장은_각자_고유한_임시_파일을_쓴다(tmp_path, monkeypatch):
    path = tmp_path / "shared-tokens.json"
    barrier = threading.Barrier(2)
    original_replace = tokenstore.os.replace
    sources: list[str] = []
    first_calls: set[int] = set()
    lock = threading.Lock()

    def replace(src, dst):
        with lock:
            sources.append(str(src))
            thread_id = threading.get_ident()
            first_call = thread_id not in first_calls
            first_calls.add(thread_id)
        if first_call:
            barrier.wait(timeout=5)
        return original_replace(src, dst)

    monkeypatch.setattr(tokenstore.os, "replace", replace)
    results: list[bool | None] = [None, None]

    def save(index: int) -> None:
        results[index] = TokenStore("shared", path=path).save({"refresh_token": str(index)})

    threads = [threading.Thread(target=save, args=(index,)) for index in range(2)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    assert results == [True, True]
    assert len(set(sources)) == 2
    assert TokenStore("shared", path=path).load()["refresh_token"] in {"0", "1"}


def test_일시적인_windows_공유_위반은_다시_시도한다(tmp_path, monkeypatch):
    path = tmp_path / "tokens.json"
    original_replace = tokenstore.os.replace
    calls = 0

    def replace(src, dst):
        nonlocal calls
        calls += 1
        if calls == 1:
            error = PermissionError("temporary sharing violation")
            error.winerror = 32
            raise error
        return original_replace(src, dst)

    monkeypatch.setattr(tokenstore.os, "replace", replace)
    monkeypatch.setattr(tokenstore.time, "sleep", lambda _: None)

    store = TokenStore("shared", path=path)
    assert store.save({"refresh_token": "새 토큰"}) is True
    assert calls == 2
    assert TokenStore("shared", path=path).load()["refresh_token"] == "새 토큰"
