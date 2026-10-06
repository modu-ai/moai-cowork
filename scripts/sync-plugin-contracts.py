#!/usr/bin/env python3
"""호환 매니페스트에서 portable 패키지와 PM 추천 카탈로그를 생성한다."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re

import yaml

ROOT = Path(__file__).resolve().parents[1]
PLUGINS = ROOT / "plugins"
SCHEMA = "https://agent-plugins.org/schemas/1.0.0/"
IDENTITY = ("name", "version", "description", "author", "homepage", "repository", "license", "keywords")


def portable_mcp(plugin: Path, manifest: dict) -> dict:
    source = manifest.get("mcpServers", {})
    if isinstance(source, str):
        path = (plugin / source).resolve()
        if not path.is_relative_to(plugin.resolve()):
            raise ValueError(f"패키지 밖 MCP 경로: {plugin.name}")
        source = json.loads(path.read_text(encoding="utf-8")).get("mcpServers", {})
    servers = {}
    for name, entry in source.items():
        entry = {k: v for k, v in entry.items() if k != "$comment"}
        cfg = dict(entry)
        # 호환 호스트의 client timeout은 공통 MCP 스키마에 없는 설정이다.
        cfg.pop("timeout", None)
        if cfg.get("command"):
            cfg["type"] = "stdio"
            cfg["cwd"] = "./" if cfg.get("cwd") == "." else cfg.get("cwd", "./")
            cfg["args"] = [a.replace("${CLAUDE_PLUGIN_ROOT}", "${PLUGIN_ROOT}") for a in cfg.get("args", [])]
        elif cfg.get("url"):
            cfg["type"] = "sse" if cfg.get("type") == "sse" else "streamable-http"
        else:
            raise ValueError(f"MCP 전송 방식 없음: {plugin.name}:{name}")
        servers[name] = cfg
    return {"$schema": SCHEMA + "mcp.schema.json", "mcpServers": servers}


def generated() -> dict[Path, dict]:
    outputs = {}
    catalog = {"schema_version": 1, "source": "modu-ai/moai-cowork", "usage": "recommendation_only", "plugins": [], "skills": []}
    for plugin in sorted(PLUGINS.glob("moai-*")):
        codex = json.loads((plugin / ".codex-plugin/plugin.json").read_text(encoding="utf-8"))
        manifest = {"$schema": SCHEMA + "plugin.schema.json", **{k: codex[k] for k in IDENTITY if k in codex}}
        extension = {k: codex[k] for k in ("interface", "apps", "hooks") if k in codex}
        manifest["extensions"] = {"com.openai": extension}
        outputs[plugin / "plugin.json"] = manifest
        outputs[plugin / "mcp.json"] = portable_mcp(plugin, codex)
        catalog["plugins"].append({"name": plugin.name, "version": codex["version"], "description": codex["description"]})
        for skill in sorted(plugin.glob("skills/*/SKILL.md")):
            raw = skill.read_bytes()
            match = re.match(r"^---\s*\n(.*?)\n---", raw.decode(), re.S)
            if not match:
                raise ValueError(f"frontmatter 없음: {skill}")
            meta = yaml.safe_load(match[1])
            catalog["skills"].append({"id": plugin.name + ":" + meta["name"], "version": meta["metadata"]["version"],
                                      "description": meta["description"], "invocation_scope": meta.get("metadata", {}).get("invocation-scope", "user-or-workflow"), "digest": "sha256:" + hashlib.sha256(raw).hexdigest()})
    outputs[PLUGINS / "moai-pm/skills/project/references/skill-catalog.json"] = catalog
    return outputs


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    problems = []
    outputs = generated()
    for path, value in outputs.items():
        expected = json.dumps(value, ensure_ascii=False, indent=2) + "\n"
        if args.check:
            if not path.is_file() or path.read_text(encoding="utf-8") != expected:
                problems.append(str(path.relative_to(ROOT)))
        else:
            path.write_text(expected, encoding="utf-8")
    for problem in problems:
        print(f"정합 오류: {problem}")
    print(f"portable 패키지·PM 카탈로그 검사: 오류 {len(problems)}건" if args.check else f"portable 패키지 {sum(p.name == 'plugin.json' for p in outputs)}개·PM 추천 카탈로그 생성")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
