"""Read every tracked file; emit reproducible structural inventory, not a runtime verdict."""
from pathlib import Path
import ast
import collections
import hashlib
import json
import re
import subprocess
import sys
import tomllib
import yaml

ROOT = Path('/Users/goos/.codex/worktrees/b0aa/moai-cowork')
OUT = Path(__file__).parent
names = subprocess.check_output(['git', '-C', str(ROOT), 'ls-files', '-z']).decode().split('\0')
files = []
texts = {}
errors = []
syntax = collections.Counter()
for name in sorted(n for n in names if n):
    path = ROOT / name
    if not path.is_file():
        errors.append({'path': name, 'kind': 'missing-tracked-file'})
        continue
    raw = path.read_bytes()
    row = {'path': name, 'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()}
    try:
        value = raw.decode('utf-8')
        if '\0' in value:
            raise UnicodeError()
        texts[name] = value
        row['text'] = True
        row['lines'] = len(value.splitlines())
    except UnicodeError:
        row['text'] = False
    files.append(row)
    if name not in texts:
        continue
    try:
        if path.suffix == '.py':
            ast.parse(texts[name], filename=name)
            syntax['python'] += 1
        elif path.suffix == '.json':
            json.loads(texts[name])
            syntax['json'] += 1
        elif path.suffix == '.toml':
            tomllib.loads(texts[name])
            syntax['toml'] += 1
        elif path.suffix in ('.yaml', '.yml'):
            list(yaml.safe_load_all(texts[name]))
            syntax['yaml'] += 1
    except Exception as exc:
        errors.append({'path': name, 'kind': 'parse', 'message': str(exc)})

skills = []
agents = []
frontmatter_errors = []
for name, body in texts.items():
    if not (name.endswith('/SKILL.md') or ('/agents/' in name and name.endswith('.md'))):
        continue
    try:
        match = re.match(r'^---\s*\n(.*?)\n---\s*\n', body, re.S)
        metadata = yaml.safe_load(match[1]) if match else {}
        metadata = metadata or {}
        for key in ('name', 'description'):
            if not metadata.get(key):
                frontmatter_errors.append({'path': name, 'field': key})
    except Exception as exc:
        metadata = {}
        frontmatter_errors.append({'path': name, 'message': str(exc)})
    row = {'path': name, 'metadata': metadata, 'lines': len(body.splitlines()),
           'bytes': len(body.encode()), 'headings': re.findall(r'^#{1,4} .+', body, re.M),
           'has_workflow': bool(re.search(r'workflow|워크플로우|Phase|단계|프로세스', body, re.I)),
           'has_input': bool(re.search(r'입력|맥락|질문|context|input', body, re.I)),
           'has_verification': bool(re.search(r'검증|검수|품질|verify|validation|quality|audit', body, re.I)),
           'has_claude_tool_names': bool(re.search(r'AskUserQuestion|\bSkill\(|\bAgent\(|TaskCreate', body))}
    (skills if name.endswith('/SKILL.md') else agents).append(row)

skill_ids = set()
for row in skills:
    parts = Path(row['path']).parts
    if parts[0] == 'plugins':
        skill_ids.add(parts[1] + ':' + parts[3])
reference_candidates = []
for name, body in texts.items():
    if not name.startswith(('plugins/', 'README', 'www/content/')):
        continue
    for lineno, line in enumerate(body.splitlines(), 1):
        for ref in re.findall(r'\bmoai-[a-z0-9-]+:[a-z0-9-]+', line):
            if ref not in skill_ids:
                reference_candidates.append({'path': name, 'line': lineno, 'ref': ref})
link_candidates = []
for name, body in texts.items():
    if not name.startswith('plugins/') or not name.endswith('.md'):
        continue
    for match in re.finditer(r'\[[^\]\n]+\]\(([^)\s]+)\)', body):
        target = match[1].split('#')[0]
        if not target or re.match(r'^[a-zA-Z][\w+.-]*:', target) or target.startswith(('/', '{', '$')):
            continue
        if not (ROOT / name).parent.joinpath(target).exists():
            link_candidates.append({'path': name, 'line': body[:match.start()].count('\n') + 1, 'target': target})

tools = []
for name, body in texts.items():
    if '/mcp-servers/' not in name or not name.endswith('.py') or '/tests/' in name:
        continue
    tree = ast.parse(body, filename=name)
    for node in ast.walk(tree):
        if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        for decorator in node.decorator_list:
            text = ast.get_source_segment(body, decorator) or ''
            if re.match(r'mcp\.tool\(', text):
                tools.append({'path': name, 'line': node.lineno, 'name': node.name,
                              'decorator': text, 'docstring': ast.get_docstring(node),
                              'has_annotations': 'annotations' in text})
plugins = []
for plugin in sorted((ROOT / 'plugins').glob('moai-*')):
    claude = json.loads((plugin / '.claude-plugin/plugin.json').read_text())
    codex = json.loads((plugin / '.codex-plugin/plugin.json').read_text())
    mcp = json.loads((plugin / '.mcp.json').read_text()) if (plugin / '.mcp.json').exists() else {}
    plugins.append({'name': plugin.name, 'claude_manifest': claude, 'codex_manifest': codex,
                    'claude_mcp': mcp, 'skills': sum(s['path'].startswith('plugins/' + plugin.name + '/') for s in skills),
                    'agents': sum(a['path'].startswith('plugins/' + plugin.name + '/') for a in agents)})
summary = {'root': str(ROOT), 'head': subprocess.check_output(['git', '-C', str(ROOT), 'rev-parse', 'HEAD']).decode().strip(),
           'tracked_files': len(files), 'text_files': len(texts), 'binary_files': len(files) - len(texts),
           'tracked_bytes': sum(f['bytes'] for f in files), 'syntax_checked': dict(syntax),
           'plugin_skills': sum(s['path'].startswith('plugins/') for s in skills), 'repository_skills': len(skills),
           'plugin_agents': len(agents), 'mcp_tool_definitions': len(tools),
           'mcp_tools_without_annotations': sum(not t['has_annotations'] for t in tools),
           'parse_errors': len(errors), 'frontmatter_errors': len(frontmatter_errors),
           'unresolved_skill_reference_candidates': len(reference_candidates),
           'broken_markdown_link_candidates': len(link_candidates)}
for filename, data in [('inventory.json', files), ('skills-agents.json', {'skills': skills, 'agents': agents}),
                       ('plugins.json', plugins), ('mcp-tools.json', tools),
                       ('scan-results.json', {'summary': summary, 'errors': errors, 'frontmatter_errors': frontmatter_errors,
                                              'reference_candidates': reference_candidates, 'link_candidates': link_candidates})]:
    (OUT / filename).write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(summary, ensure_ascii=False, indent=2))
print('Pattern hits are candidates; confirm semantics before reporting defects.')
