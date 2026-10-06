#!/usr/bin/env python3
"""Hugo가 만든 문서의 로컬 링크·앵커·이미지·검색·실습 자료를 검사한다."""
from __future__ import annotations
import argparse
import csv
from html.parser import HTMLParser
import json
from pathlib import Path
import re
from urllib.parse import unquote, urljoin, urlsplit
import xml.etree.ElementTree as ET

class Page(HTMLParser):
    def __init__(self):
        super().__init__(); self.refs=[]; self.ids=set(); self.images=[]
    def handle_starttag(self, tag, attributes):
        attrs=dict(attributes)
        if attrs.get('id'): self.ids.add(attrs['id'])
        for attr in ('href','src'):
            if attrs.get(attr): self.refs.append((tag,attr,attrs[attr]))
        if attrs.get('srcset') and not attrs['srcset'].startswith('data:'):
            for candidate in attrs['srcset'].split(','):
                if candidate.strip(): self.refs.append((tag,'srcset',candidate.strip().split()[0]))
        if tag=='img': self.images.append(attrs)

def check(root: Path, project: Path):
    root=root.resolve();project=project.resolve()
    errors=[]; pages={}; checked=0; fragments=0; images=0
    for path in sorted(root.rglob('*.html')):
        p=Page();p.feed(path.read_text()); pages[path.resolve()]=p
    def target(url):
        path=root/unquote(urlsplit(url).path).lstrip('/')
        if path.is_dir(): path/= 'index.html'
        return path.resolve()
    for path,p in pages.items():
        rel=path.relative_to(root);base='https://cowork.mo.ai.kr/'+str(rel)
        if rel.name=='index.html':base=base[:-10]
        for tag,attr,ref in p.refs:
            if urlsplit(ref).scheme in ('data','mailto','tel','javascript'):continue
            url=urljoin(base,ref);part=urlsplit(url)
            if part.hostname!='cowork.mo.ai.kr':continue
            checked+=1;t=target(url)
            if not t.is_relative_to(root):errors.append(f'{rel}: outside build root {ref}');continue
            if not t.is_file():errors.append(f'{rel}: missing {ref}');continue
            if part.fragment and t in pages:
                fragments+=1
                if unquote(part.fragment) not in pages[t].ids:errors.append(f'{rel}: missing anchor {ref}')
        for img in p.images:
            images+=1
            if not img.get('alt','').strip():errors.append(f'{rel}: image alt missing {img.get("src")}')
    search=json.loads((root/'search.json').read_text())
    if isinstance(search,dict):search=search.get('items',search.get('pages',[]))
    for row in search:
        if not target(row['href']).is_file():errors.append(f'search target missing: {row["href"]}')
    sitemap=ET.parse(root/'sitemap.xml')
    locs=[x.text for x in sitemap.iter() if x.tag.endswith('}loc')]
    for loc in locs:
        if not target(loc).is_file():errors.append(f'sitemap target missing: {loc}')
    sitemap_targets={target(loc) for loc in locs}
    for row in search:
        if target(row['href']) not in sitemap_targets:errors.append(f'search page absent from sitemap: {row["href"]}')
    if (root/'index.html') not in sitemap_targets:errors.append('home absent from sitemap')
    if len(locs)<len(list((project/'www/content').rglob('*.md'))):errors.append('sitemap omits content pages')
    rows=list(csv.DictReader((project/'www/static/downloads/classroom/문의.csv').open(encoding='utf-8-sig')))
    counts={name:sum(r['유형']==name for r in rows) for name in ('배송','반품','결제')}
    if len(rows)!=6 or counts!={'배송':3,'반품':2,'결제':1}:errors.append('classroom CSV mismatch')
    arithmetic=[]
    for source in sorted((project/'www/content').rglob('*.md')):
        body=source.read_text()
        cases=[
            (r'가상 자료: A지역 문의 (\d+)건, 응답 완료 (\d+)건\. B지역 문의 (\d+)건, 응답 완료 (\d+)건',r'전체 문의 (\d+)건, 완료 (\d+)건, 전체 완료율 (\d+)%',lambda v:[v[0]+v[2],v[1]+v[3],(v[1]+v[3])/(v[0]+v[2])*100]),
            (r'가상 지출표: 교재 ([\d,]+)원, 인쇄 ([\d,]+)원, 소모품 ([\d,]+)원',r'세 항목 합계는 ([\d,]+)원',lambda v:[sum(v)]),
            (r'가상 계획: 판매량 (\d+)개, 개당 판매가 ([\d,]+)원, 개당 변동비 ([\d,]+)원, 고정비 ([\d,]+)원',r'매출 ([\d,]+)원, 변동비 ([\d,]+)원, 고정비 ([\d,]+)원입니다\. 이 가정만의 차액은 ([\d,]+)원',lambda v:[v[0]*v[1],v[0]*v[2],v[3],v[0]*(v[1]-v[2])-v[3]])
        ]
        for inputs,outputs,calculate in cases:
            match=re.search(inputs,body)
            if not match:continue
            values=[int(n.replace(',','')) for n in match.groups()]
            answer=re.search(outputs,body)
            expected=calculate(values)
            actual=[int(n.replace(',','')) for n in answer.groups()] if answer else None
            rel=str(source.relative_to(project));arithmetic.append({'path':rel,'expected':expected,'actual':actual})
            if actual!=expected:errors.append(f'{rel}: example arithmetic mismatch')
    if not arithmetic:errors.append('no worked arithmetic examples checked')
    lessons=sorted((project/'www/content/learn').glob('0*.md'))
    for lesson in lessons:
        body=lesson.read_text()
        headings=re.findall(r'^## (.+)$',body,re.M)
        if not headings or headings[0]!='이번 수업에서 배울 내용':errors.append(f'{lesson.name}: learning goal must precede other sections')
        for token in ('## 이번 수업에서 배울 내용','## 확인 문제','<details>'):
            if token not in body:errors.append(f'{lesson.name}: missing lesson element {token}')
    if len(lessons)!=6:errors.append('expected six lessons')
    result={'html_files':len(pages),'internal_references':checked,'fragment_references':fragments,'images':images,'search_entries':len(search),'sitemap_entries':len(locs),'classroom_rows':len(rows),'classroom_types':counts,'worked_arithmetic':arithmetic,'lessons':len(lessons),'errors':sorted(set(errors)),'scope':'built_site_local_references_and_fixtures_only'}
    return result

def main():
    args=argparse.ArgumentParser();args.add_argument('build',type=Path);args.add_argument('--report',type=Path);opt=args.parse_args()
    result=check(opt.build.resolve(),Path(__file__).resolve().parents[1])
    if opt.report:opt.report.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False,indent=2));return bool(result['errors'])
if __name__=='__main__':raise SystemExit(main())
