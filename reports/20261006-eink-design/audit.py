"""현재 본문 전체와 도식 자산을 읽어 재표현 계획을 기록한다. 원본은 수정하지 않는다."""
from pathlib import Path
from collections import Counter
import hashlib, json, re
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
specs = json.loads((ROOT / 'reports/20261006-page-infographics/diagram-specs.json').read_text())
reasons = {
    'questions': ('Mermaid 분기', '필수 맥락이 없을 때 보류하고 질문하는 분기와 독립 작업 경로를 표시한다.'),
    'pm-setup': ('Mermaid 흐름', '질문 → 역할·스킬 매핑 → 지침 저장 → 실제 참조 확인의 의존 관계를 표시한다.'),
    'reuse': ('Mermaid 순환', '검토 결과를 지침에 반영하고 다시 실행하는 반복 경로를 표시한다.'),
    'permissions': ('Mermaid 관계', '프로젝트와 허용한 폴더의 경계, 읽기와 별도 결과 저장을 표시한다.'),
    'handoff': ('Mermaid 인계', '이전 작업의 결과·미정 항목이 다음 작업의 입력이 되는 인계를 표시한다.'),
    'limits': ('Mermaid 분기·합류', '작업을 분리하되 선행 결과가 필요한 작업은 합류 뒤에 시작하도록 표시한다.'),
    'troubleshooting': ('Mermaid 분기', '설치·노출·인증·실행 중 어느 단계가 막혔는지 조건별로 표시한다.'),
    'credentials': ('Mermaid 관계', '사용자·서비스·인증 저장 범위의 대응 관계를 표시한다. 비밀 값은 넣지 않는다.'),
    'server-modes': ('Mermaid 관계', '실행 위치와 연결 방식을 서로 다른 축으로 표시한다.'),
}
png_notes = {
    'coworker-concept': ('HTML 목록', '역할 이름 목록은 검색·링크가 가능한 HTML 목록으로 표현한다.'),
    'core-concepts': ('HTML 용어 표', '네 용어의 짧은 정의를 본문 표로 통합한다.'),
    'install-3steps': ('HTML 체크리스트', '설치 단계는 실제 UI 캡처와 체크리스트로 안내한다.'),
    'quickstart-5min': ('HTML 실습 안내', '지침 설정과 첫 요청은 실행 가능한 본문으로 안내한다.'),
    'docsite-map': ('HTML 탐색 목록', '문서 탐색은 클릭 가능한 목차가 적합하다.'),
    'coworker-family-map': ('HTML 역할 목록', '분야 분류와 역할 이름을 링크 가능한 목록으로 표현한다.'),
    'skill-chain-flow': ('Mermaid 흐름', '생성·변환·검수의 선후 관계를 명확한 화살표로 다시 그린다.'),
    'team-pattern': ('Mermaid 분기·합류', '담당자별 입력·출력과 합류 조건을 추가해 다시 그린다.'),
    'attribution-flow': ('HTML 기준 표', '권리·출처 확인 기준을 근거 링크가 있는 표로 표현한다.'),
    'install-manage-flow': ('HTML 체크리스트', '단순 직선 단계는 체크리스트와 실제 화면으로 안내한다.'),
    'mcp-bridge': ('Mermaid 관계', '앱·연결·외부 서비스의 경계와 실제 지원 확인을 표시한다.'),
    'skill-chaining-pattern': ('Mermaid 흐름', '도메인 방법 → 결과 형식 → 검토 기준이 어디에 적용되는지 다시 그린다.'),
    'project-flow': ('Mermaid 흐름', '맥락 질문과 기능 확인에서 지침 생성·참조 확인으로 이어지는 관계를 그린다.'),
    'project-context-ko': ('Mermaid 관계', '앱 프로젝트와 허용한 로컬 폴더의 경계를 분리한다. 긴 설명은 HTML로 옮긴다.'),
    'project-concepts-ko': ('Mermaid 관계', '지침·스킬·역할·패키지·외부 연결의 관계를 간결하게 다시 그린다.'),
    'expert-workflow-ko': ('Mermaid 분기·합류', '분석 뒤 작성 작업의 분기와 검토 전 합류를 남기고 설명은 본문으로 옮긴다.'),
    'first-workflow-ko': ('Mermaid 순환', '결과 검토 → 수정 요청의 되돌아가는 경로를 남긴다.'),
}

pages = []
for path in sorted((ROOT / 'www/content').rglob('*.md')):
    text = path.read_text()
    title = re.search(r'^title:\s*["\']?(.*?)["\']?\s*$', text, re.M)
    refs = sorted(set(re.findall(r'/infographics/[\w./-]+\.(?:svg|png)', text)))
    mermaids = re.findall(r'```mermaid\s*\n(.*?)```', text, re.S)
    pages.append({'path': str(path.relative_to(ROOT)), 'title': title.group(1) if title else path.stem,
                  'bytes_read': len(text.encode()), 'sha256': hashlib.sha256(text.encode()).hexdigest(),
                  'assets': refs, 'existing_mermaid': [
                      {'source': block, 'sha256': hashlib.sha256(block.encode()).hexdigest(),
                       'action': '구조 유지·무채색 적용',
                       'explicit_colors': re.findall(r'#[0-9a-fA-F]{3,8}\b', block)} for block in mermaids]})

concepts = []
for key, spec in specs.items():
    if key in reasons:
        action, why = reasons[key]
    elif spec.get('example') and re.search(r'A지역 문의 \d+건, 응답 완료 \d+건\. B지역 문의 \d+건, 응답 완료 \d+건', spec['example']['input']):
        action, why = 'SVG 차트 + HTML 표', '네 칸 설명은 본문으로 통합하고 분모가 다른 완료율만 눈금·값이 있는 차트로 남긴다.'
    elif spec.get('example'):
        action, why = 'HTML 본문 통합', '준비 자료·작업·검토·결과 설명과 예제는 선택·복사 가능한 본문으로 통합하고 중복 그림을 제거한다.'
    else:
        action, why = 'HTML 본문 통합', '짧은 정의·비교·단순 순서는 기존 본문의 표·목록으로 통합하고 중복 그림을 제거한다.'
    refs = ['/infographics/pages/' + key + '.svg', '/infographics/pages/' + key + '-mobile.svg']
    concepts.append({'key': key, 'title': spec['title'], 'action': action, 'reason': why,
                     'pages': [p['path'] for p in pages if set(refs) & set(p['assets'])], 'assets': refs})

assets = []
for path in sorted((ROOT / 'www/static/infographics').rglob('*')):
    if not path.is_file(): continue
    data = path.read_bytes()
    ref = '/' + str(path.relative_to(ROOT / 'www/static'))
    referenced = [p['path'] for p in pages if ref in p['assets']]
    row = {'path': str(path.relative_to(ROOT)), 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(), 'pages': referenced}
    if path.suffix == '.svg':
        svg = ET.fromstring(data)
        key = path.stem.removesuffix('-mobile')
        target = next(c for c in concepts if c['key'] == key)
        row.update({'concept': key, 'action': target['action'], 'reason': target['reason'],
                    'text_nodes': len(svg.findall('.//{*}text')), 'path_nodes': len(svg.findall('.//{*}path')),
                    'line_nodes': len(svg.findall('.//{*}line')), 'marker_nodes': len(svg.findall('.//{*}marker')),
                    'has_redundant_header': '한국어 개념 설명' in data.decode(),
                    'has_redundant_footer': '본문을 요약한 개념도' in data.decode()})
    else:
        action, reason = png_notes[path.stem]
        row.update({'action': action if referenced else '미참조 보관·재사용 보류',
                    'reason': reason, 'visual_inspected': True, 'proposed_if_reused': action})
    assets.append(row)

lookup = {'/' + a['path'].split('www/static/', 1)[1]: a for a in assets}
page_plan = []
for page in pages:
    row = dict(page)
    row['proposed_actions'] = sorted({lookup[a]['action'] for a in page['assets']})
    if page['existing_mermaid']: row['proposed_actions'].append('기존 Mermaid 구조 유지·무채색 적용')
    if not row['proposed_actions']: row['proposed_actions'] = ['공통 사이트 디자인 적용 · 그림 자동 추가 없음']
    page_plan.append(row)

summary = {'pages_read': len(pages), 'current_pages': sum('/releases/' not in p['path'] for p in pages),
           'concepts': len(concepts), 'asset_files': len(assets), 'formats': dict(Counter(Path(a['path']).suffix for a in assets)),
           'concept_actions': dict(Counter(c['action'].split(' ')[0] for c in concepts)),
           'asset_actions': dict(Counter(a['action'].split(' ')[0] for a in assets)),
           'unreferenced_png': [a['path'] for a in assets if a['path'].endswith('.png') and not a['pages']],
           'existing_mermaid_blocks': sum(len(p['existing_mermaid']) for p in pages),
           'svg_redundant_header': sum(a.get('has_redundant_header', False) for a in assets),
           'svg_redundant_footer': sum(a.get('has_redundant_footer', False) for a in assets),
           'source_mutations': 0}
for name, data in [('pages', pages), ('assets', assets), ('concepts', concepts), ('summary', summary), ('page-plan', page_plan)]:
    (OUT / (name + '.json')).write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
table = ['# 인포그래픽 재표현 계획', '', '원본을 일괄 변경하기 전 검토할 계획이다. 같은 개념의 PC·모바일 파일은 한 묶음으로 센다.', '',
         '| 개념 | 제안 | 이유 | 사용 페이지 |', '|---|---|---|---|']
for c in concepts:
    table.append('| ' + ' | '.join([c['title'], c['action'], c['reason'], '<br>'.join(c['pages'])]) + ' |')
table += ['', '## 기존 PNG', '', '| 파일 | 현재 사용 | 제안 | 이유 |', '|---|---|---|---|']
for a in assets:
    if a['path'].endswith('.png'):
        table.append('| ' + ' | '.join([Path(a['path']).name, str(len(a['pages'])) + '개 페이지', a['action'], a['reason']]) + ' |')
(OUT / 'inventory.md').write_text('\n'.join(table) + '\n')
print(json.dumps(summary, ensure_ascii=False))
