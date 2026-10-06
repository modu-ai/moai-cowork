"""실제 브라우저 측정값과 현재 시안 파일을 검증한다."""
from pathlib import Path
from collections import Counter
from html.parser import HTMLParser
import hashlib, json, re, urllib.request

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[1]
P = ROOT / 'www/design-system/eink-proposal'
read = lambda name: json.loads((OUT / name).read_text())
sha = lambda path: hashlib.sha256(path.read_bytes()).hexdigest()

def luminance(value):
    rgb = [float(x) / 255 for x in re.findall(r'[\d.]+', value)[:3]]
    assert len(rgb) == 3
    return sum((x / 12.92 if x <= .04045 else ((x + .055) / 1.055) ** 2.4) * w
               for x, w in zip(rgb, [.2126, .7152, .0722]))

class Inspect(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.refs, self.remote = [], [], []
        self.foreign = self.svg = 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a: self.ids.append(a['id'])
        for key in ['aria-labelledby', 'aria-describedby', 'aria-controls']:
            self.refs.extend(a.get(key, '').split())
        if tag in ['script', 'img', 'link'] and a.get('src', a.get('href', '')).startswith('http'):
            self.remote.append(a)
        self.svg += tag == 'svg'
        self.foreign += tag == 'foreignobject'

html = (P / 'index.html').read_text()
parser = Inspect()
parser.feed(html)
assert not parser.remote and not parser.foreign
assert not [i for i, n in Counter(parser.ids).items() if n > 1]
assert all(i in parser.ids for i in parser.refs)
assert all(x not in html for x in ['@@', '한국어 개념 설명', '본문을 요약한 개념도'])
layouts = read('browser-layouts.json')
assert len(layouts) == 12
assert {x['requestedWidth'] for x in layouts} == {390, 768, 1440}
assert {x['view'] for x in layouts} == {'home', 'lesson', 'diagrams', 'components'}
fonts, ratios = [], []
for case in layouts:
    assert case['fontLoaded'] == 'true'
    assert all(f.startswith(chr(34) + 'Pretendard Variable' + chr(34)) for f in case['families'])
    assert case['body_width'] <= case['width'] + 1
    assert case['contentWidth'] >= min(350, case['width'] - 40)
    assert not case['clips'] and not case['duplicate_ids']
    for text in case['texts']:
        size = float(text['font'].removesuffix('px'))
        if text.get('viewBox'):
            size *= text['svg_width'] / float(text['viewBox'].split()[2])
        assert size >= 15.99, (case['view'], text)
        fonts.append(size)
        fg, bg = luminance(text['color']), luminance(text['background'])
        ratio = (max(fg, bg) + .05) / (min(fg, bg) + .05)
        assert ratio >= 4.5, (case['view'], text, ratio)
        ratios.append(ratio)
baseline = read('untouched-baseline.json')
drift = [name for name, digest in baseline.items() if sha(ROOT / name) != digest]
assert not drift, drift
assert not read('console-errors.json')
assert json.loads((P / 'tokens.json').read_text())['colors'] == json.loads((OUT / 'before/tokens.json').read_text())['colors']
assert all(sha(P / 'assets' / name) == digest for name, digest in read('preserved-images.json').items())
assert all('NeoDunggeunmo' not in (P / name).read_text() for name in ['prototype.css', 'prototype.js', 'mermaid.config.json', 'index.html'])
http = []
for name in ['index.html', 'assets/parallel-pixel-ko.png', 'assets/context-pixel-ko.png',
             'assets/fonts/PretendardVariable.woff2', 'assets/fonts/Pretendard-LICENSE.txt']:
    with urllib.request.urlopen('http://127.0.0.1:1314/' + name) as response:
        assert response.status == 200 and response.read() == (P / name).read_bytes()
        http.append({'path': name, 'status': 200, 'bytes_match': True})
result = {'layouts': 12, 'measured_texts': len(fonts), 'minimum_font_px': round(min(fonts), 2),
          'minimum_contrast': round(min(ratios), 2), 'page_overflow': 0, 'svg_text_clips': 0,
          'minimum_mobile_content_width': min(x['contentWidth'] for x in layouts),
          'duplicate_ids': 0, 'broken_aria_references': 0, 'inline_svg': parser.svg,
          'pixel_images': 2, 'pretendard_loaded': True, 'remote_render_assets': 0,
          'original_files_unchanged': len(baseline), 'http': http}
(OUT / 'verification.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(result, ensure_ascii=False))
