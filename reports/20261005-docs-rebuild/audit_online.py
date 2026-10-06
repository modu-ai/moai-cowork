"""Bounded, read-only crawl of the public documentation site."""
import concurrent.futures
import hashlib
import json
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlsplit
from urllib.request import Request, urlopen

BASE = 'https://cowork.mo.ai.kr/'
OUT = Path(__file__).parent

class Page(HTMLParser):
    def __init__(self):
        super().__init__(); self.links = []; self.text = []; self.main = 0; self.title = False; self.heading = False; self.h1 = []
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'article': self.main += 1
        if tag == 'h1': self.heading = True
        if tag == 'a' and a.get('href'): self.links.append(a['href'])
    def handle_endtag(self, tag):
        if tag == 'article': self.main = max(0, self.main - 1)
        if tag == 'h1': self.heading = False
    def handle_data(self, data):
        if self.main and data.strip(): self.text.append(data.strip())
        if self.heading: self.h1.append(data.strip())

def fetch(url):
    try:
        with urlopen(Request(url, headers={'User-Agent': 'MoAI-Docs-Audit/1.0'}), timeout=20) as response:
            raw = response.read(); content_type = response.headers.get('Content-Type', '')
            parser = Page(); parser.feed(raw.decode('utf-8', errors='replace'))
            return {'url': url, 'final_url': response.url, 'status': response.status, 'type': content_type,
                    'sha256': hashlib.sha256(raw).hexdigest(), 'h1': parser.h1, 'text': '\n'.join(parser.text), 'links': parser.links}
    except Exception as exc:
        return {'url': url, 'error': str(exc), 'links': []}

def main():
    pending = {BASE}; seen = set(); rows = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        while pending and len(seen) < 350:
            batch = sorted(pending - seen)[:350-len(seen)]; pending = set(); seen.update(batch)
            for row in pool.map(fetch, batch):
                rows.append(row)
                for link in row['links']:
                    u = urlsplit(urljoin(row['url'], link))
                    if u.netloc != urlsplit(BASE).netloc or u.query: continue
                    if '.' in u.path.rsplit('/', 1)[-1]: continue
                    target = BASE.rstrip('/') + (u.path or '/')
                    if target not in seen: pending.add(target)
    (OUT/'online-pages-before.json').write_text(json.dumps(rows, ensure_ascii=False, indent=2)+'\n')
    summary = {'pages_requested': len(rows), 'success': sum(r.get('status') == 200 for r in rows),
               'errors': [{'url':r['url'],'error':r.get('error')} for r in rows if r.get('status') != 200],
               'remaining_at_bound': sorted(pending - seen), 'base': BASE}
    (OUT/'online-summary-before.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps(summary, ensure_ascii=False))

if __name__ == '__main__': main()
