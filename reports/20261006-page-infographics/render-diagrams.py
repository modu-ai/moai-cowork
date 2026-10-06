"""확인한 본문 근거로 SVG를 제작하고 계획된 위치에 그림과 설명을 넣는다."""
from pathlib import Path
import hashlib,html,json,re,unicodedata
from xml.etree import ElementTree as ET

ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent
DEST=ROOT/'www/static/infographics/pages'
DEST.mkdir(parents=True,exist_ok=True)
specs=json.loads((OUT/'diagram-specs.json').read_text())
plan=json.loads((OUT/'page-plan.json').read_text())

def clean(text):
    text=text.strip().replace('**','').replace('만들어 줘.','작성합니다.').replace('진행해 줘.','진행합니다.')
    def particle(m):
        c=m.group(1);closed=(ord(c)-0xac00)%28!=0
        return c+('을' if closed else '를')
    return re.sub(r'([가-힣])[을를](?=\s)',particle,text)

def width(s):
    return sum(1 if unicodedata.east_asian_width(c) in ('W','F') else .62 for c in s)

def wrap(s,limit):
    lines=[];line=''
    for word in clean(s).split():
        addition=(' ' if line else '')+word
        if width(line+addition)<=limit:line+=addition;continue
        if line:lines.append(line);line=''
        for c in word:
            if width(line+c)>limit:lines.append(line);line=''
            line+=c
    if line:lines.append(line)
    return lines or ['']

COLORS=[('#edf5f0','#285942'),('#ecf3fc','#245a86'),('#fff5e7','#8a540a'),('#f3effa','#654395')]

def draw(key,spec,mobile=False):
    parts=[];layout=[]
    def rect(x,y,w,h,fill,stroke='none',radius=20):
        parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" stroke="{stroke}"/>')
    def text(lines,x,y,size=27,color='#243c31',weight=400,step=38):
        if isinstance(lines,str):lines=[lines]
        for i,line in enumerate(lines):
            parts.append(f'<text x="{x}" y="{y+i*step}" font-size="{size}" fill="{color}" font-weight="{weight}">{html.escape(line)}</text>')
            layout.append({'text':line,'x':x,'y':y+i*step,'size':size,'right_estimate':round(x+width(line)*size,2)})
    text('MoAI-Cowork · 한국어 개념 설명',48,43,18,'#516e60',600)
    title=wrap(spec['title'],18)
    text(title,48,102,38,'#173d2b',800,50)
    top=153+(len(title)-1)*50
    text('업무 순서  ① → ② → ③ → ④' if spec['mode']=='flow' else '비슷해 보여도 서로 다른 네 가지',48,top,23,'#536f61',500)
    y=top+30
    columns=1 if mobile else 2
    for row in range(4//columns):
        heights=[];cards=[]
        for i in range(row*columns,row*columns+columns):
            heading,body=spec['cards'][i];hl=wrap(heading,18 if mobile else 11.8);bl=wrap(body,18 if mobile else 11.8)
            height=(100+len(hl)*48+len(bl)*48) if mobile else (80+len(hl)*39+len(bl)*37)
            heights.append(height);cards.append((i,hl,bl))
        height=max(heights)
        for col,(i,hl,bl) in enumerate(cards):
            x=48+col*368;fill,color=COLORS[i];rect(x,y,704 if mobile else 336,height,fill,'#d6e2d9')
            rect(x+20,y+20,42,36,color,radius=10)
            text(str(i+1).zfill(2),x+28,y+45,22,'white',700)
            text(hl,x+22,y+94,36 if mobile else 28,color,700,48 if mobile else 39)
            text(bl,x+22,y+94+len(hl)*(48 if mobile else 39)+12,36 if mobile else 26,'#253d33',400,48 if mobile else 37)
        y+=height+20
    if spec.get('example'):
        data=re.search(r'A지역 문의 (\d+)건, 응답 완료 (\d+)건\. B지역 문의 (\d+)건, 응답 완료 (\d+)건',spec['example']['input'])
        amounts=re.search(r'교재 ([\d,]+)원, 인쇄 ([\d,]+)원, 소모품 ([\d,]+)원',spec['example']['input'])
        if data:
            a,ac,b,bc=map(int,data.groups())
            text('비율은 건수를 합쳐서 계산',48,y+32,29,'#173d2b',700);y+=62
            for label,done,total,color in [('A지역',ac,a,'#245a86'),('B지역',bc,b,'#654395'),('전체',ac+bc,a+b,'#285942')]:
                percent=done/total*100
                text(f'{label} {done}/{total}',48,y+29,26,color,600)
                rect(250,y+7,390,30,'#e6ede8',radius=6)
                rect(250,y+7,390*percent/100,30,color,radius=6)
                text(f'{percent:g}%',658,y+31,28,color,700)
                y+=69
            text('전체 완료율 = 완료 합계 ÷ 문의 합계 × 100',48,y+22,24,'#253d33',600);y+=62
        elif amounts:
            values=[int(n.replace(',','')) for n in amounts.groups()]
            text('세 항목을 더한 가상 지출 합계',48,y+32,29,'#173d2b',700);y+=66
            text(' + '.join(f'{n:,}' for n in values),70,y+25,31,'#245a86',700);y+=55
            rect(48,y,704,84,'#edf5f0','#d6e2d9',16)
            text(f'= {sum(values):,}원',70,y+55,35,'#285942',800);y+=112
        text('가상 예제로 읽어 보기',48,y+31,29,'#173d2b',700);y+=52
        for label,value in [('제공 자료',spec['example']['input']),('예상 결과',spec['example']['expected'])]:
            lines=wrap(value,18 if mobile else 25);height=80+len(lines)*(48 if mobile else 37)
            rect(48,y,704,height,'#f8faf8','#d6e2d9',16)
            text(label,70,y+42,23,'#285942',700)
            text(lines,70,y+86,36 if mobile else 26,'#253d33',400,48 if mobile else 37);y+=height+16
    note=wrap(spec['note'],20 if mobile else 25)
    height=78+len(note)*(44 if mobile else 36)
    rect(48,y,704,height,'#fff8ec','#ead7b7',16)
    text('주의할 혼동' if spec.get('example') else '기억할 기준',70,y+38,23,'#80520e',700)
    text(note,70,y+80,32 if mobile else 25,'#67491c',400,44 if mobile else 36)
    y+=height+38
    text('본문을 요약한 개념도 · 실제 앱 화면이나 실행 결과가 아닙니다.',48,y,19,'#536f61',400)
    bottom=y+32
    # 마지막 줄 기준으로 영역이 늘어난다. 텍스트와 배경이 겹치지 않도록 높이를 계산한다.
    desc=' / '.join(h+': '+clean(b) for h,b in spec['cards'])
    svg=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 {bottom}" width="800" height="{bottom}" role="img" aria-labelledby="title desc"><title id="title">{html.escape(spec["title"])}</title><desc id="desc">{html.escape(desc)}</desc><rect width="800" height="{bottom}" fill="#ffffff"/><g font-family="Apple SD Gothic Neo, Malgun Gothic, Noto Sans KR, sans-serif">'+''.join(parts)+'</g></svg>\n'
    ET.fromstring(svg)
    assert all(item['right_estimate']<=766 for item in layout),(key,'text width')
    file_key=key+('-mobile' if mobile else '')
    path=DEST/(file_key+'.svg')
    if path.exists():
        previous=json.loads((OUT/'assets.json').read_text())
        previous_hash=next(a['sha256'] for a in previous if a['key']==file_key)
        assert hashlib.sha256(path.read_bytes()).hexdigest()==previous_hash,f'제작 후 다른 편집 발견: {path}'
    path.write_text(svg)
    return {'key':file_key,'concept':key,'mobile':mobile,'path':str(path.relative_to(ROOT)),'height':bottom,'bytes':len(svg.encode()),'sha256':hashlib.sha256(svg.encode()).hexdigest(),'lines':layout}

assets=[draw(k,s,mobile) for k,s in specs.items() for mobile in (False,True)]
changed=[]
for row in plan:
    if row['action']!='추가':continue
    path=ROOT/'www/content'/row['path'];body=path.read_text();marker='<!-- page-infographic: '+row['asset']+' -->'
    if marker in body:changed.append(row['path']);continue
    assert hashlib.sha256(body.encode()).hexdigest()==row['source_sha256'],f'계획 후 원본 변경: {path}'
    key=Path(row['asset']).stem;spec=specs[key]
    alt=spec['title']+' · '+(' → ' if spec['mode']=='flow' else ' / ').join(c[0] for c in spec['cards'])
    explanation=('그림의 순서대로 ' if spec['mode']=='flow' else '그림은 ')+(' → ' if spec['mode']=='flow' else ', ').join(c[0] for c in spec['cards'])+('를 확인합니다.' if spec['mode']=='flow' else '를 구분합니다.')
    explanation=clean(explanation)+' '+('아래 예제는 가상 자료이며 실제 실행 결과가 아닙니다.' if spec.get('example') else '각 항목의 자세한 설명과 실제 확인 방법은 본문에서 이어집니다.')
    block='\n<!--more-->\n\n'+marker+'\n\n## 그림으로 먼저 이해하기\n\n!['+alt+']('+row['asset']+')\n\n'+explanation+'\n\n'
    # 첫 요청·실습보다 앞, 첫 설명 다음에 넣어 문서를 읽는 기준을 먼저 보여 준다.
    match=re.search(r'^## ',body,re.M)
    if match and body[match.start():].startswith('## 이번 수업에서 배울 내용\n'):
        next_heading=re.search(r'^## ',body[match.end():],re.M)
        assert next_heading,'학습 목표 다음에 설명 절이 필요합니다.'
        match_start=match.end()+next_heading.start()
    else:match_start=match.start() if match else None
    if match:position=match_start
    else:
        fm=re.match(r'^---\n.*?\n---\n',body,re.S);assert fm
        position=fm.end()
    path.write_text(body[:position]+block+body[position:]);changed.append(row['path'])
(OUT/'assets.json').write_text(json.dumps(assets,ensure_ascii=False,indent=2)+'\n')
(OUT/'inserted-pages.json').write_text(json.dumps(changed,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'concepts':len(specs),'svg_files':len(assets),'inserted_pages':len(changed),'xml_errors':0,'estimated_text_overflow':0},ensure_ascii=False))
