from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
import re
import urllib.parse
import urllib.request

P = Path(__file__).resolve().parent
BUILD = Path('/tmp/moai-kindle-rollout-final-20261006')
expected = {}
for file in BUILD.rglob('*'):
    if not file.is_file():
        continue
    relative = str(file.relative_to(BUILD))
    if file.suffix == '.html':
        url = '/' + relative.removesuffix('index.html')
    elif file.suffix in ['.css', '.js', '.woff2'] or any('/' + part + '/' in '/' + relative for part in ['infographics', 'screenshots', 'downloads']):
        url = '/' + relative
    else:
        continue
    expected[url] = file

def check(url):
    with urllib.request.urlopen('http://127.0.0.1:1313' + urllib.parse.quote(url, safe='/%'), timeout=20) as response:
        data = response.read()
        status = response.status
    source = expected[url].read_bytes()
    if expected[url].suffix == '.html':
        # 서버의 개발용 livereload 주입과 공백 차이만 제외한다.
        rendered = re.sub(r'\s*<script src="/livereload\.js[^\"]*"[^>]*></script>', '', data.decode('utf-8'))
        same = re.sub(r'\s+', ' ', rendered) == re.sub(r'\s+', ' ', source.decode('utf-8'))
    else:
        same = data == source
    return {'url': url, 'status': status, 'build_match': same, 'sha256': hashlib.sha256(data).hexdigest()}

with ThreadPoolExecutor(max_workers=6) as pool:
    rows = list(pool.map(check, sorted(expected)))
(P / 'http-assets.json').write_text(json.dumps(rows, ensure_ascii=False, indent=2))
print(json.dumps({'checked': len(rows), 'HTTP_200': sum(x['status'] == 200 for x in rows), 'build_matches': sum(x['build_match'] for x in rows), 'mismatches': [x['url'] for x in rows if not x['build_match']]}, ensure_ascii=False))
assert all(x['status'] == 200 and x['build_match'] for x in rows)
