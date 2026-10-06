"""실제 브라우저가 기록한 좌표·글꼴·색으로 시안 검증 결과를 계산한다."""
from pathlib import Path
from collections import Counter
from html.parser import HTMLParser
import hashlib, json, re

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[1]
P = ROOT / 'www/design-system/eink-proposal'

def read(name):
    return json.loads((OUT / name).read_text())

def rgb(value):
    result = [float(x) for x in re.findall(r'[\d.]+', value)[:3]]
    assert len(result) == 3, ('색 측정 누락', value)
    return result

def luminance(color):
    color = [x / 255 for x in color]
    color = [x / 12.92 if x <= .04045 else ((x + .055) / 1.055) ** 2.4 for x in color]
    return sum(x * w for x, w in zip(color, [.2126, .7152, .0722]))

class Inspector(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.references, self.external_assets = [], [], []
        self.svg = self.foreign_objects = 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a: self.ids.append(a['id'])
        for key in ['aria-labelledby', 'aria-describedby', 'aria-controls']:
            if key in a: self.references.extend(a[key].split())
        if tag in ['script', 'img', 'link'] and ('src' in a or 'href' in a):
            self.external_assets.append(a.get('src', a.get('href')))
        if tag == 'svg': self.svg += 1
        if tag == 'foreignobject': self.foreign_objects += 1

html = (P / 'index.html').read_text()
parser = Inspector()
parser.feed(html)
layouts = read('browser-layouts.json')
failures, fonts, contrast, main_fonts, svg_fonts = [], [], [], [], []
for layout in layouts:
    if layout['width'] != layout['body_width']: failures.append({'type': '페이지 넘침', 'layout': layout['view']})
    failures.extend(layout['clips'])
    failures.extend({'type': '중복 ID', 'id': i} for i in layout['duplicate_ids'])
    for text in layout['texts']:
        scale = (text['svg_width'] / float(text['viewBox'].split()[2])) if text.get('svg_width') else 1
        size = float(text['font'].replace('px', '')) * scale
        fg, bg = rgb(text['color']), rgb(text['background'])
        a, b = luminance(fg), luminance(bg)
        ratio = (max(a, b) + .05) / (min(a, b) + .05)
        fonts.append(size)
        contrast.append(ratio)
        if text['tag'].lower() == 'text': svg_fonts.append(size)
        if text['tag'].lower() in ['p', 'li', 'td', 'th', 'label', 'summary'] and not text.get('viewBox'): main_fonts.append(size)
        if size < 13.9 or ratio < 4.5 or len(set(fg)) != 1:
            failures.append({'type': '글자', 'view': layout['view'], 'text': text['text'], 'font': size, 'contrast': ratio, 'color': fg})

tokens = json.loads((P / 'tokens.json').read_text())
assert all(v[1:3] == v[3:5] == v[5:7] for v in tokens['colors'].values())
assert all(x not in html for x in ['한국어 개념 설명', '본문을 요약한 개념도'])
assert not parser.external_assets
assert not parser.foreign_objects
assert not [i for i, n in Counter(parser.ids).items() if n > 1]
assert all(i in parser.ids for i in parser.references)
assert len(layouts) == 24 and {x['style'] for x in layouts} == {'paper', 'reader'}
assert {x['view'] for x in layouts} == {'home', 'lesson', 'diagrams', 'components'}
assert {x['viewport']['width'] for x in layouts} == {390, 768, 1280}

interactions = read('interactions.json')
assert interactions['tabs_arrow'] and interactions['copy_matches'] and interactions['quiz_open']
assert interactions['form_result'] == '주간 보고서 초안 · Claude Cowork · 결과 검토 포함'
source_drift = []
for page in read('pages.json'):
    if hashlib.sha256((ROOT / page['path']).read_bytes()).hexdigest() != page['sha256']: source_drift.append(page['path'])
assert not source_drift, '감사 후 본문 변경: ' + ', '.join(source_drift)
assert not failures, json.dumps(failures, ensure_ascii=False)

summary = {'layouts': len(layouts), 'styles': 2, 'views': 4, 'viewport_widths': [390, 768, 1280],
           'measured_texts': len(fonts), 'minimum_font_px': round(min(fonts), 2),
           'minimum_main_font_px': round(min(main_fonts), 2), 'minimum_svg_font_px': round(min(svg_fonts), 2),
           'minimum_contrast': round(min(contrast), 2), 'text_or_node_clips': 0,
           'page_overflow': 0, 'duplicate_ids': 0, 'broken_aria_references': 0,
           'external_render_assets': 0, 'foreign_objects': 0, 'inline_svg': parser.svg,
           'copy_matches': True, 'keyboard_tabs': True, 'form_confirmation': True, 'quiz_toggle': True,
           'original_page_drift': source_drift, 'failures': failures}
(OUT / 'verification.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(summary, ensure_ascii=False))
