"""Inspect registered MCP tools without invoking remote tool operations."""
from pathlib import Path
import json
import os
import subprocess

ROOT = Path('/Users/goos/.codex/worktrees/b0aa/moai-cowork')
ENV_ROOT = Path('/var/folders/kt/nq2q81cn4gx3y41r7x47ggmr0000gn/T/moai-cowork-audit-cbsj5su2')
OUT = Path(__file__).parent
SERVERS = ('moai-mcp-ip', 'moai-mcp-openai', 'moai-mcp-smartstore',
           'moai-mcp-imweb', 'moai-mcp-cafe24', 'moai-mcp-threads-poster')
env = {k: v for k, v in os.environ.items()
       if not k.endswith(('_API_KEY', '_ACCESS_TOKEN', '_REFRESH_TOKEN', '_CLIENT_SECRET'))}
env['PYTHONDONTWRITEBYTECODE'] = '1'
head = subprocess.check_output(['git', '-C', str(ROOT), 'rev-parse', 'HEAD'], text=True).strip()
records = []
for server in SERVERS:
    module = server.replace('-', '_')
    script = (f'import asyncio,json; from {module}.server import mcp; '
              'print(json.dumps([t.model_dump(mode="json") '
              'for t in asyncio.run(mcp.list_tools())],ensure_ascii=False))')
    command = [str(ENV_ROOT / server / 'venv/bin/python'), '-c', script]
    result = subprocess.run(command, cwd=ROOT, env=env, text=True, capture_output=True, timeout=20)
    if result.returncode:
        raise RuntimeError(f'{server}: exit {result.returncode}: {result.stderr[-1000:]}')
    registered = json.loads(result.stdout)
    (OUT / f'{server}-tool-schemas.json').write_text(json.dumps(registered, ensure_ascii=False, indent=2) + '\n')
    records.append({'server': server, 'command': command, 'cwd': str(ROOT), 'head': head,
                    'exit_code': result.returncode, 'registered_tools': len(registered),
                    'without_annotations': sum(t.get('annotations') is None for t in registered),
                    'input_schema_utf8_bytes': sum(len(json.dumps(t['inputSchema'], ensure_ascii=False).encode()) for t in registered)})
(OUT / 'runtime-probe-evidence.json').write_text(json.dumps(records, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'registered_tools': sum(r['registered_tools'] for r in records),
                  'without_annotations': sum(r['without_annotations'] for r in records),
                  'servers': len(records)}, ensure_ascii=False))
