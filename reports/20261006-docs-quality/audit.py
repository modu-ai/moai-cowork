"""현재 문서의 구조·참조·그림 유형을 전 페이지에 대해 기록한다.
본문의 정확성 전체나 실제 앱의 설치·실행 성공을 판정하는 도구는 아니다.
"""
from pathlib import Path
import collections
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
baseline = {r['path']: r for r in json.loads((OUT/'baseline.json').read_text())}
items = []
for p in sorted((ROOT/'www/content').rglob('*.md')):
    text = p.read_text()
    key = str(p.relative_to(ROOT))
    digest = hashlib.sha256(p.read_bytes()).hexdigest()
    skills = set(re.findall(r'`(moai-[a-z-]+):([a-z0-9-]+)`', text))
    missing = [a+':'+b for a, b in sorted(skills)
               if not (ROOT/'plugins'/a/'skills'/b/'SKILL.md').exists()]
    concepts = re.findall(r'\{\{< concept-diagram ([\w-]+)', text)
    pictures = re.findall(r'!\[([^]]*)\]\(([^)]+)\)', text)
    historical = '/archive/' in key
    worked = '## 가상 예제로 더 이해하기' in text
    if concepts:
        treatment = '관계·분기·순서를 도식으로 설명'
    elif 'rate-chart' in text:
        treatment = '건수·비율 계산 도표 유지'
    elif '/screenshots/' in text:
        treatment = '실제 화면 사진과 단계 설명'
    elif worked:
        treatment = '원문과 모범 결과 표로 비교'
    else:
        treatment = '본문·목록·표로 설명'
    if '/releases/' in key:
        treatment = '과거 기록 보존·현재 사용 경로와 구분'
    relative = p.relative_to(ROOT/'www/content')
    section = relative.parts[0] if len(relative.parts)>1 else 'root'
    items.append({
        'path': key, 'title': re.search(r'^title: (.+)', text, re.M).group(1).strip('"'),
        'section': section, 'chars': len(text), 'sha256': digest,
        'changed_this_turn': key not in baseline or digest != baseline[key]['sha256'],
        'new_page': key not in baseline, 'headings': re.findall(r'^#{2,3} .+', text, re.M),
        'concepts': concepts, 'images': pictures, 'visual_treatment': treatment,
        'worked_example': worked, 'model_result_table': '### 직접 비교할 모범 결과' in text,
        'skill_refs': len(skills), 'missing_skills': missing, 'historical': historical,
    })
summary = {
    'baseline_pages': len(baseline), 'current_pages': len(items),
    'changed_pages': sum(i['changed_this_turn'] for i in items),
    'new_pages': sum(i['new_page'] for i in items),
    'sections': dict(collections.Counter(i['section'] for i in items)),
    'worked_pages': sum(i['worked_example'] for i in items),
    'new_output_tables': sum(i['model_result_table'] for i in items),
    'historical_missing_skill_pages': sum(bool(i['missing_skills']) and i['historical'] for i in items),
    'active_missing_skills': [dict(path=i['path'], missing=i['missing_skills']) for i in items
                              if i['missing_skills'] and not i['historical']],
    'concept_instances': sum(len(i['concepts']) for i in items),
}
for name, data in [('page-audit.json', items), ('audit-summary.json', summary)]:
    (OUT/name).write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n')
lines = ['# 페이지별 조사와 처리 목록', '',
         '모든 Markdown의 본문·목차·그림·스킬 참조를 읽어 구조를 기록했습니다. 이 목록은 구조 조사와 편집 처리의 기록이며, 모든 외부 제품 기능을 실행 검증했다는 뜻은 아닙니다.', '',
         '| 문서 | 처리 | 그림·설명 방식 |', '|---|---|---|']
for i in items:
    action = '추가' if i['new_page'] else ('수정' if i['changed_this_turn'] else '유지')
    lines.append(f"| [{i['title']}]({ROOT/i['path']}) | {action} | {i['visual_treatment']} |")
(OUT/'page-audit.md').write_text('\n'.join(lines)+'\n')
print(json.dumps(summary, ensure_ascii=False, indent=2))
