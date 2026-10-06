"""실제 다운로드 자료와 학습 목표 순서 검사기의 누락 탐지를 검증한다."""
import csv
import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import sys
from tempfile import TemporaryDirectory

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
BUILD = Path(sys.argv[1]).resolve()
download = OUT / 'downloaded-문의.csv'
source = ROOT / 'www/static/downloads/classroom/문의.csv'
same = hashlib.sha256(download.read_bytes()).digest() == hashlib.sha256(source.read_bytes()).digest()
rows = list(csv.DictReader(download.open(encoding='utf-8-sig')))
types = {kind: sum(r['유형'] == kind for r in rows) for kind in ('배송', '반품', '결제')}
assert same and len(rows) == 6 and types == {'배송': 3, '반품': 2, '결제': 1}

spec = importlib.util.spec_from_file_location('docscheck', ROOT / 'scripts/check-docs.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
with TemporaryDirectory(prefix='moai-docs-order-') as temp:
    clone = Path(temp)
    shutil.copytree(ROOT / 'www/content', clone / 'www/content')
    (clone / 'www/static/downloads/classroom').mkdir(parents=True)
    shutil.copyfile(source, clone / 'www/static/downloads/classroom/문의.csv')
    page = clone / 'www/content/learn/03-first-result.md'
    body = page.read_text()
    frontmatter_end = body.index('\n---\n', 4) + len('\n---\n')
    page.write_text(body[:frontmatter_end] + '\n## 그림이 목표보다 먼저 나오는 회귀\n\n' + body[frontmatter_end:])
    result = module.check(BUILD, clone)
    detected = [e for e in result['errors'] if 'learning goal must precede' in e]
    assert detected == ['03-first-result.md: learning goal must precede other sections'], result['errors']

result = {'download_matches_source': same, 'download_rows': len(rows), 'types': types,
          'lesson_order_regression_detected': detected, 'errors': [],
          'scope': 'downloaded virtual class fixture and an automatically removed temporary source copy'}
(OUT / 'fixture-check.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(result, ensure_ascii=False, indent=2))
