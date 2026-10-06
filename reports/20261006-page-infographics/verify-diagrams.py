"""페이지 계획·SVG 원본·빌드·검사기의 누락 탐지를 확인한다."""
from pathlib import Path
import hashlib
import importlib.util
import json
import re
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
BUILD = Path(sys.argv[1]).resolve()
plan = json.loads((OUT / 'page-plan.json').read_text())
assets = json.loads((OUT / 'assets.json').read_text())
specs = json.loads((OUT / 'diagram-specs.json').read_text())
facts = json.loads((OUT / 'example-facts.json').read_text())
errors = []
ns = {'s': 'http://www.w3.org/2000/svg'}
trees = {}
charts = []
expense_examples = []

def require(condition, message):
    if not condition:
        errors.append(message)

def compact(value):
    return re.sub(r'\s+', '', value)

for fact in facts:
    body = compact((ROOT / fact['path']).read_text())
    for field, value in fact.items():
        if field not in ('path', 'title'):
            require(compact(value) in body, f'{fact["path"]}: extracted {field} differs from source')
    key = 'example-' + fact['path'].removeprefix('www/content/').removesuffix('.md').replace('/', '-')
    require(compact(specs[key]['example']['input']) == compact(fact['example']), f'{key}: input differs from extracted source')
    require(compact(specs[key]['example']['expected']) == compact(fact['expected']), f'{key}: result differs from extracted source')

for asset in assets:
    path = ROOT / asset['path']
    content = path.read_bytes()
    require(hashlib.sha256(content).hexdigest() == asset['sha256'], f'{path.name}: SHA mismatch')
    tree = ET.fromstring(content)
    trees[asset['key']] = tree
    require(bool(tree.findtext('s:title', namespaces=ns)), f'{path.name}: title missing')
    require(bool(tree.findtext('s:desc', namespaces=ns)), f'{path.name}: description missing')
    require(not any(e.tag.split('}')[-1] in ('script', 'foreignObject') for e in tree.iter()), f'{path.name}: active content')
    require((BUILD / 'infographics/pages' / path.name).read_bytes() == content, f'{path.name}: built copy differs')

for key, spec in specs.items():
    variants = [trees[key], trees[key + '-mobile']]
    texts = [compact(''.join(t.itertext())) for t in variants]
    require(texts[0] == texts[1], f'{key}: desktop/mobile text differs')
    example = spec.get('example', {})
    match = re.search(r'A지역 문의 (\d+)건, 응답 완료 (\d+)건\. B지역 문의 (\d+)건, 응답 완료 (\d+)건', example.get('input', ''))
    if match:
        a, ac, b, bc = map(int, match.groups())
        percentages = [ac / a * 100, bc / b * 100, (ac + bc) / (a + b) * 100]
        for tree in variants:
            labels = [e.text for e in tree.findall('.//s:text', ns)]
            require(all(f'{p:g}%' in labels for p in percentages), f'{key}: chart labels mismatch')
            bars = [float(e.attrib['width']) for e in tree.findall('.//s:rect', ns) if e.get('x') == '250' and e.get('height') == '30' and e.get('fill') != '#e6ede8']
            require(len(bars) == 3 and all(abs(w - 390 * p / 100) < 0.0001 for w, p in zip(bars, percentages)), f'{key}: bar proportions mismatch')
        charts.append({'concept': key, 'percentages': percentages})
    match = re.search(r'교재 ([\d,]+)원, 인쇄 ([\d,]+)원, 소모품 ([\d,]+)원', example.get('input', ''))
    if match:
        total = sum(int(n.replace(',', '')) for n in match.groups())
        for tree in variants:
            labels = [e.text for e in tree.findall('.//s:text', ns)]
            require(f'= {total:,}원' in labels, f'{key}: expense total mismatch')
        expense_examples.append({'concept': key, 'total': total})

unchanged = []
added = []
for row in plan:
    path = ROOT / 'www/content' / row['path']
    body = path.read_text()
    if row['action'] == '추가':
        marker = '<!-- page-infographic: ' + row['asset'] + ' -->'
        require(body.count(marker) == 1, f'{row["path"]}: marker count')
        require(f']({row["asset"]})' in body, f'{row["path"]}: image absent')
        require(body.count('<!--more-->') == 1, f'{row["path"]}: explicit summary boundary absent')
        added.append(row['path'])
    else:
        require(hashlib.sha256(path.read_bytes()).hexdigest() == row['source_sha256'], f'{row["path"]}: unplanned change')
        unchanged.append(row['path'])
require(len(plan) == len(list((ROOT / 'www/content').rglob('*.md'))) == 171, 'page inventory differs')
old = Path('/tmp/moai-docs-20261005-final')
old_urls = {str(p.relative_to(old)) for p in old.rglob('*.html')}
new_urls = {str(p.relative_to(BUILD)) for p in BUILD.rglob('*.html')}
missing_urls = sorted(old_urls - new_urls)
require(len(old_urls) == 288 and not missing_urls, 'previous build URLs missing or baseline absent')
require(not (BUILD / 'infographics/pages/render-check.html').exists(), 'temporary probe in build')
picture_pages = {}
for path in BUILD.rglob('*.html'):
    sources = re.findall(r'srcset="(/infographics/pages/[^\"]+-mobile\.svg)"', path.read_text())
    if sources:
        picture_pages[str(path.relative_to(BUILD))] = sources
require(len(picture_pages) == 108 and sum(map(len, picture_pages.values())) == 108, 'expected one responsive picture on each of 108 pages')
require(not any(k.startswith('tags/') for k in picture_pages), 'new diagrams repeated in tag excerpts')

module_spec = importlib.util.spec_from_file_location('docscheck', ROOT / 'scripts/check-docs.py')
module = importlib.util.module_from_spec(module_spec)
module_spec.loader.exec_module(module)
parser = module.Page()
parser.feed('<source srcset="/small.svg 1x, /large.svg 2x">')
require(parser.refs == [('source', 'srcset', '/small.svg'), ('source', 'srcset', '/large.svg')], 'srcset candidates missed')
# 이번 작업의 임시 빌드에서만 모바일 이미지를 누락시킨 뒤 반드시 복구한다.
mobile = BUILD / 'infographics/pages/questions-mobile.svg'
original = mobile.read_bytes()
try:
    mobile.unlink()
    negative = module.check(BUILD, ROOT)
    detected = [e for e in negative['errors'] if 'questions-mobile.svg' in e]
    require(bool(detected), 'missing mobile source was not detected')
finally:
    mobile.write_bytes(original)

result = {'pages_planned': len(plan), 'pages_added': len(added), 'pages_unchanged': len(unchanged),
          'concepts': len(specs), 'svg_files': len(assets), 'variant_texts_equal': True if not errors else None,
          'worked_examples_grounded_in_current_source': len(facts),
          'previous_html_urls': len(old_urls), 'final_html_urls': len(new_urls), 'missing_previous_urls': missing_urls,
          'responsive_picture_pages': len(picture_pages), 'responsive_pictures': sum(map(len, picture_pages.values())),
          'unique_responsive_concepts': len({s for sources in picture_pages.values() for s in sources}),
          'chart_examples': charts, 'expense_examples': expense_examples,
          'missing_mobile_source_errors_observed': detected, 'errors': errors,
          'scope': 'this worktree source and the specified temporary Hugo build'}
(OUT / 'artifact-check.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(result, ensure_ascii=False, indent=2))
raise SystemExit(bool(errors))
