"""이 작업에서 저장한 실제 브라우저 관측값과 현재 산출물을 대조한다."""
from pathlib import Path
import csv
import hashlib
import io
import json

P = Path(__file__).resolve().parent
ROOT = P.parents[1]
def read(name):
    return json.loads((P / name).read_text())

site = read('site-check.json')
assert site['errors'] == [] and site['html_files'] == 288
mobile = read('browser-mobile.json')
desktop = read('browser-diagrams.json')
tablet = read('browser-tablet.json')
assert len(mobile) == 288 and len(desktop) == 47 and len(tablet) == 22
for record in mobile + desktop + tablet:
    assert record['body_width'] == record['width'], record['url']
    assert not record['clips'] and not record['duplicate_ids'], record['url']
    assert record['font_loaded'] == 'true', record['url']
    assert record['bg'] == 'rgb(233, 233, 229)', record['url']
    assert all(block['state'] == 'true' and block['svg'] and not block['foreign'] for block in record['blocks'])
    assert all(not item['broken'] for item in record['ids'])
assert all(not item['cropped'] for item in read('browser-text-crops.json'))
leaf = read('browser-leaf-contrast.json')
assert len(leaf) == 12 and all(not item['low'] for item in leaf)
home = read('home-final.json')
assert home['paragraph'] == '18px' and home['accent'] == 'rgb(32, 32, 32)'
assert home['button'] == 'rgb(244, 244, 239)' and home['width'] == home['scroll']
interactions = read('interactions.json')
assert interactions['copy_exact'] and interactions['answer_open']
assert interactions['menu_open'] == 'true' and interactions['menu_closed'] == 'false'
assert interactions['figure']['scroll'] > 0 and interactions['search_results'] > 0
rows = list(csv.DictReader(io.StringIO(interactions['download_csv'])))
assert len(rows) == 6
http = read('http-assets.json')
assert all(x['status'] == 200 and x['build_match'] for x in http)
archive = read('archived-assets.json')
assert len(archive) == 189
for item in archive:
    assert not (ROOT / item['old']).exists()
    assert hashlib.sha256((ROOT / item['archive']).read_bytes()).hexdigest() == item['sha256']
for page in (ROOT / 'www/content').rglob('*.md'):
    assert '/infographics/pages/' not in page.read_text()
    assert '<!-- page-infographic:' not in page.read_text()
result = {
    'built_pages': 288, 'mobile_pages': 288, 'desktop_diagram_pages': 47, 'tablet_pages': 22,
    'page_overflow': 0, 'svg_text_clips': 0, 'body_text_crops': 0, 'duplicate_ids': 0,
    'broken_svg_aria': 0, 'leaf_contrast_pages': len(leaf),
    'leaf_texts': sum(x['texts'] for x in leaf),
    'min_leaf_contrast': round(min(x['min_contrast'] for x in leaf), 2),
    'copy_exact': True, 'download_rows': len(rows), 'search_results': interactions['search_results'],
    'http_200_and_build_match': len(http), 'archived_assets_unchanged': len(archive),
    'removed_card_blocks': read('content-changes.json')['removed_card_blocks'],
}
(P / 'verification.json').write_text(json.dumps(result, ensure_ascii=False, indent=2))
print(json.dumps(result, ensure_ascii=False))
