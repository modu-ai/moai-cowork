"""Run the Agent Skills reference validator; report every plugin skill."""
from pathlib import Path
import collections
import importlib.metadata
import json
import subprocess
from skills_ref import validate

ROOT = Path('/Users/goos/.codex/worktrees/b0aa/moai-cowork')
OUT = Path(__file__).parent
rows = [{'path': str(p.relative_to(ROOT)), 'errors': validate(p.parent)}
        for p in sorted(ROOT.glob('plugins/*/skills/*/SKILL.md'))]
summary = {'validator_version': importlib.metadata.version('skills-ref'),
           'checked': len(rows), 'passed': sum(not r['errors'] for r in rows),
           'failed': sum(bool(r['errors']) for r in rows),
           'error_classes': dict(collections.Counter(e for r in rows for e in r['errors']))}
result = {'head': subprocess.check_output(['git', '-C', str(ROOT), 'rev-parse', 'HEAD'], text=True).strip(),
          'command': 'uv run --no-project --python 3.11 --with skills-ref==0.1.1 python reports/20261005-work-cowork-update/validate_skills.py',
          'summary': summary, 'skills': rows}
(OUT / 'skills-ref-validation.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(summary, ensure_ascii=False, indent=2))
# Nonzero signals validation failure; findings are fully written before exiting.
raise SystemExit(1 if summary['failed'] else 0)
