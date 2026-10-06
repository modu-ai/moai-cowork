"""실행 중인 로컬 문서의 HTTP 응답과 정적 파일을 대조한다."""
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import sys
from urllib.error import HTTPError
from urllib.parse import quote, unquote, urlsplit
from urllib.request import urlopen

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
BUILD = Path(sys.argv[1]).resolve()
BASE = 'http://127.0.0.1:1313'

class References(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls = []
    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        self.urls += [attrs[k] for k in ('src', 'href') if attrs.get(k)]
        self.urls += [v.strip().split()[0] for v in attrs.get('srcset', '').split(',') if v.strip()]

targets = {}
for file in BUILD.rglob('*.html'):
    rel = '/' + str(file.relative_to(BUILD))
    route = rel.removesuffix('index.html') if rel.endswith('/index.html') else rel
    targets[route] = {'kind': 'html', 'file': file}
    parser = References()
    parser.feed(file.read_text())
    for ref in parser.urls:
        parts = urlsplit(ref)
        if parts.scheme and parts.hostname != 'cowork.mo.ai.kr':
            continue
        if not parts.path.startswith('/'):
            continue
        path = unquote(parts.path)
        candidate = BUILD / path.lstrip('/')
        if candidate.is_file() and candidate.suffix != '.html':
            targets[path] = {'kind': 'asset', 'file': candidate}
for name in ('search.json', 'sitemap.xml'):
    targets['/' + name] = {'kind': 'asset', 'file': BUILD / name}

observations = []
errors = []
for path, target in sorted(targets.items()):
    try:
        with urlopen(BASE + quote(path, safe='/'), timeout=5) as response:
            data = response.read()
            result = {'path': path, 'kind': target['kind'], 'status': response.status,
                      'bytes': len(data), 'content_type': response.headers.get_content_type()}
            if response.status != 200 or not data:
                errors.append(f'{path}: HTTP {response.status}, {len(data)} bytes')
            if target['kind'] == 'asset':
                result['sha256_matches_build'] = hashlib.sha256(data).digest() == hashlib.sha256(target['file'].read_bytes()).digest()
                if not result['sha256_matches_build']:
                    errors.append(f'{path}: served bytes differ from build')
            observations.append(result)
    except Exception as error:
        errors.append(f'{path}: {error}')

missing = None
try:
    with urlopen(BASE + '/missing-local-test-page-20261006/', timeout=5) as response:
        missing = {'status': response.status, 'bytes': len(response.read())}
except HTTPError as error:
    missing = {'status': error.code, 'body_prefix': error.read().decode('utf-8', errors='replace')[:160]}
if missing is None or missing['status'] != 404:
    errors.append('unknown route did not return HTTP 404')

result = {'base_url': BASE, 'build': str(BUILD),
          'html_responses': sum(r['kind'] == 'html' for r in observations),
          'asset_responses': sum(r['kind'] == 'asset' for r in observations),
          'checked_responses': len(observations), 'missing_route': missing,
          'errors': errors, 'responses': observations,
          'scope': 'local HTTP responses and static asset bytes; not browser interactions'}
(OUT / 'live-http.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({k: v for k, v in result.items() if k != 'responses'}, ensure_ascii=False, indent=2))
raise SystemExit(bool(errors))
