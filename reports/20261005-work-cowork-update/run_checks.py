"""Bounded local checks; all subprocess output is saved with its baseline."""
from pathlib import Path
import concurrent.futures
import json
import os
import subprocess
import tempfile

ROOT = Path('/Users/goos/.codex/worktrees/b0aa/moai-cowork')
OUT = Path(__file__).parent
TEMP = Path(tempfile.mkdtemp(prefix='moai-cowork-audit-'))
head = subprocess.check_output(['git', '-C', str(ROOT), 'rev-parse', 'HEAD']).decode().strip()
jobs = [
    ('plugin-wiring', ['python3', 'scripts/check-plugin-runtimes.py'], ROOT),
    ('core-sync', ['python3', 'scripts/sync-mcp-core.py', '--check'], ROOT),
    ('launcher', ['uv', 'run', '--no-project', '--python', '3.11', '--with', 'pytest', 'pytest', '-q', '-p', 'no:cacheprovider', 'plugins/_shared/mcp-launch/test_mcp_launch.py'], ROOT),
    ('korean-humanize', ['uv', 'run', '--no-project', '--python', '3.11', 'python', '-m', 'unittest', 'discover', '-s', 'plugins/moai-writer/skills/korean-humanize/tests', '-p', 'test_*.py', '-q'], ROOT),
]
jobs.extend([
    ('skill-contracts', ['uv', 'run', '--no-project', '--python', '3.11', '--with', 'skills-ref==0.1.1', '--with', 'jsonschema==4.25.1', '--with', 'pyyaml==6.0.3', 'python', 'scripts/check-skill-contracts.py'], ROOT),
    ('dev-skills-sync', ['python3', 'scripts/sync-dev-skills.py', '--check'], ROOT),
    ('evals-sync', ['uv', 'run', '--no-project', '--with', 'pyyaml==6.0.3', 'python', 'scripts/sync-skill-evals.py', '--check'], ROOT),
    ('pm-contract', ['uv', 'run', '--no-project', '--python', '3.11', 'python', '-m', 'unittest', 'discover', '-s', 'plugins/moai-pm/skills/project/tests', '-q'], ROOT),
])
for project in sorted((ROOT / 'plugins').rglob('pyproject.toml')):
    path = project.parent
    if not (path / 'tests').is_dir():
        continue
    dev = ['--extra', 'dev'] if path.name == 'moai-mcp-smartstore' else ['--group', 'dev']
    jobs.append((path.name, ['uv', 'run', '--python', '3.11', *dev, 'pytest', '-q', '-p', 'no:cacheprovider'], path))

def run(job):
    label, command, cwd = job
    env = dict(os.environ)
    env['UV_PROJECT_ENVIRONMENT'] = str(TEMP / label / 'venv')
    env['PYTHONDONTWRITEBYTECODE'] = '1'
    for key in list(env):
        if key.endswith(('_API_KEY', '_ACCESS_TOKEN', '_REFRESH_TOKEN', '_CLIENT_SECRET', '_CLIENT_ID', '_CREDENTIALS_FILE', '_TOKEN_FILE', '_MALL_ID')):
            env.pop(key)
    try:
        result = subprocess.run(command, cwd=cwd, env=env, capture_output=True, text=True, timeout=180)
        output = result.stdout + result.stderr
        code = result.returncode
    except subprocess.TimeoutExpired as exc:
        output = 'TIMEOUT after 180 seconds\n' + str(exc.stdout or '') + str(exc.stderr or '')
        code = 124
    (OUT / (label + '.log')).write_text(output)
    row = {'label': label, 'command': command, 'cwd': str(cwd), 'head': head, 'exit_code': code,
           'output_file': label + '.log', 'tail': '\n'.join(output.splitlines()[-8:])}
    print(json.dumps(row, ensure_ascii=False), flush=True)
    return row

with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
    results = list(pool.map(run, jobs))
(OUT / 'checks.json').write_text(json.dumps(results, ensure_ascii=False, indent=2) + '\n')
(OUT / 'environment-root.txt').write_text(str(TEMP) + '\n')
print('RESULT', len(results), 'checks;', sum(r['exit_code'] == 0 for r in results), 'passed', flush=True)
