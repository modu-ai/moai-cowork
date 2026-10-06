"""토큰·컴포넌트·실제 렌더링한 Mermaid SVG로 독립 시안을 만든다."""
from pathlib import Path
import argparse, hashlib, html, json, re

P = Path(__file__).resolve().parent
WWW = P.parents[1]
parser = argparse.ArgumentParser()
parser.add_argument('--prepare-render', action='store_true')
args = parser.parse_args()
if args.prepare_render:
    config = json.loads((P / 'mermaid.config.json').read_text())
    directive = '%%{init: ' + json.dumps(config, ensure_ascii=False) + '}%%\n'
    blocks = ['<section data-diagram="' + s.stem + '"><pre class="mermaid">' + html.escape(directive + s.read_text()) + '</pre></section>' for s in sorted((P / 'diagrams').glob('*.mmd'))]
    (P / '_render.html').write_text('<!doctype html><html lang="ko"><meta charset="utf-8"><title>Mermaid 시안 렌더링</title>' + ''.join(blocks) + '<script src="js/mermaid-0dbf3612.bundle.min.js"></script></html>')
    if not (P / 'js').exists():
        (P / 'js').symlink_to(WWW / 'themes/hugo-geekdoc/static/js', target_is_directory=True)
    print('render_setup: 5 sources; repository Mermaid bundle; localhost only')
    raise SystemExit(0)

tokens = json.loads((P / 'tokens.json').read_text())
css_tokens = ':root{' + ''.join('--' + k + ':' + v + ';' for k, v in tokens['colors'].items())
css_tokens += ''.join('--' + k + ':' + tokens['typography'][k] + ';' for k in ['sans', 'serif', 'mono'])
css_tokens += '--radius:' + str(tokens['radius']) + 'px;}'
rendered = json.loads((P / 'rendered-diagrams.json').read_text())
assert len(rendered) == 5 and all(x['svg'] and x['title'] and x['description'] for x in rendered)
svg_map = {x['key']: x['svg'] for x in rendered}
provenance = json.loads((P / 'render-provenance.json').read_text())
for s in (P / 'diagrams').glob('*.mmd'):
    assert hashlib.sha256(s.read_bytes()).hexdigest() == provenance['source_hashes'][s.name], '도식 원본을 바꾼 뒤에는 실제 렌더링을 다시 해야 합니다.'
assert hashlib.sha256((P / 'mermaid.config.json').read_bytes()).hexdigest() == provenance['config_hash']

def svg_instance(key, instance):
    svg = svg_map[key]
    ids = dict.fromkeys(re.findall(r'\bid="([^"]+)"', svg))
    mapping = {old: 'eink-' + instance + '-' + old for old in ids}
    for old in sorted(mapping, key=len, reverse=True):
        svg = svg.replace('id="' + old + '"', 'id="' + mapping[old] + '"').replace('#' + old, '#' + mapping[old])
    svg = re.sub(r'(aria-(?:labelledby|describedby)=")([^"]+)(")', lambda m: m.group(1) + ' '.join(mapping.get(t, t) for t in m.group(2).split()) + m.group(3), svg)
    width = float(re.search(r'viewBox="[^\"]*? ([\d.]+) [\d.]+"', svg).group(1))
    opening = re.match(r'<svg[^>]*>', svg).group(0)
    replacement = re.sub(r'\sstyle="[^"]*"', '', opening)[:-1] + ' style="width:' + str(width) + 'px;max-width:none;height:auto">'
    svg = replacement + svg[len(opening):]
    # SVG마다 자체 viewBox의 1:1 크기를 유지한다. 작은 화면에서는 도식 영역 안에서만 이동한다.
    return svg

chart = '<svg class="chart" viewBox="0 0 640 280" role="img" aria-labelledby="chart-title chart-desc"><title id="chart-title">지역별 완료율: A 80%, B 50%, 전체 68%</title><desc id="chart-desc">가상 자료. A지역 24/30건, B지역 10/20건, 전체 34/50건. 전체 완료율은 문의 건수를 합쳐 계산한다.</desc><defs><pattern id="hatch" width="6" height="6" patternUnits="userSpaceOnUse"><path d="M-1 1L1-1M0 6L6 0M5 7L7 5" stroke="#707070" stroke-width="1"/></pattern></defs><rect width="640" height="280" fill="#ffffff"/>'
for i, (label, percent, fill) in enumerate([('A지역', 80, '#202020'), ('B지역', 50, 'url(#hatch)'), ('전체', 68, '#b8b8b8')]):
    y = 35 + i * 66
    chart += f'<text x="20" y="{y+24}" font-size="18" fill="#202020">{label}</text><rect x="100" y="{y}" width="400" height="32" fill="#ffffff" stroke="#707070"/><rect x="100" y="{y}" width="{percent*4}" height="32" fill="{fill}"/><text x="520" y="{y+24}" font-size="18" fill="#202020">{percent}%</text>'
chart += '<g fill="#575757" font-size="16"><text x="100" y="255">0</text><text x="285" y="255">50</text><text x="470" y="255">100%</text></g></svg>'
chart = '<div class="table-wrap" role="region" aria-label="지역별 완료율" tabindex="0">' + chart + '</div>'
template = (P / 'prototype.template.html').read_text()
parts = {'tokens': css_tokens, 'css': (P / 'prototype.css').read_text(), 'js': (P / 'prototype.js').read_text(), 'chart': chart}
for key in svg_map: parts[key] = svg_instance(key, key)
parts['parallel-gallery'] = svg_instance('parallel', 'parallel-gallery')
for key, value in parts.items(): template = template.replace('@@' + key + '@@', value)
assert '@@' not in template
(P / 'index.html').write_text(template)
print(json.dumps({'prototype': str(P / 'index.html'), 'bytes': len(template.encode()), 'inline_mermaid': 6, 'unique_mermaid': 5, 'inline_charts': 1, 'external_render_dependencies': 0}, ensure_ascii=False))
