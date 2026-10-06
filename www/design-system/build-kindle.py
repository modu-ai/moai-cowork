"""확정한 시안의 토큰·글꼴·Mermaid 설정을 문서 사이트에 반영한다."""
from pathlib import Path
import hashlib
import json
import re
import shutil

DS = Path(__file__).resolve().parent
WWW = DS.parent
SOURCE = DS / 'eink-proposal'
tokens = json.loads((SOURCE / 'tokens.json').read_text())
colors = tokens['colors']
font = tokens['typography']['sans']
static = WWW / 'static'
(static / 'fonts').mkdir(exist_ok=True)
for name in ['PretendardVariable.woff2', 'Pretendard-LICENSE.txt']:
    shutil.copyfile(SOURCE / 'assets/fonts' / name, static / 'fonts' / name)

# 기존 컴포넌트는 변수 이름을 유지하고 현재 토큰을 사용한다.
roles = {
    'color-primary': 'ink', 'color-primary-hover': 'muted', 'color-primary-active': 'ink',
    'color-ink': 'ink', 'color-bg': 'paper', 'color-surface': 'surface',
    'fg-1': 'ink', 'fg-2': 'muted', 'fg-3': 'muted', 'fg-on-primary': 'inverse',
    'border-1': 'line', 'border-2': 'line', 'border-strong': 'strong-line',
    'color-success': 'ink', 'color-warning': 'ink', 'color-danger': 'ink', 'color-info': 'ink',
    'gradient-signature': 'ink', 'gradient-signature-soft': 'soft', 'gradient-signature-dark': 'ink',
    'terminal-bg': 'surface', 'terminal-fg': 'ink', 'terminal-dim': 'muted',
    'terminal-sigil': 'ink', 'terminal-border': 'line', 'header-bg': 'paper',
}
css = '/* 확정 기준: design-system/eink-proposal/tokens.json. build-kindle.py로 생성. */\n'
css += '@font-face{font-family:"Pretendard Variable";src:url("fonts/PretendardVariable.woff2") format("woff2");font-weight:45 920;font-style:normal;font-display:swap}\n:root{\n'
css += ''.join(f'  --{name}:{value};\n' for name, value in colors.items())
css += ''.join(f'  --{name}:var(--{role});\n' for name, role in roles.items())
css += ''.join(f'  --font-{role}:{font};\n' for role in ['sans', 'serif', 'mono', 'latin', 'display'])
css += ''.join(f'  --radius-{name}:0;\n' for name in ['none','sm','md','lg','xl','2xl','card','pill','full'])
css += ''.join(f'  --shadow-{name}:none;\n' for name in ['xs','sm','md','lg','xl','signature'])
css += ''.join(f'  --duration-{name}:0ms;\n' for name in ['instant','fast','normal','slow','page'])
css += '  --shell-sidebar:240px;--shell-toc:176px;--shell-gap:32px;--container-page:1344px;--container-gutter:24px;\n}\n'
(static / 'moai-kindle-tokens.css').write_text(css)

# 테마 번들의 엔진과 청크는 보존하고 초기화 부분만 현재 설정으로 바꾼다.
bundle_path = WWW / 'themes/hugo-geekdoc/static/js/mermaid-0dbf3612.bundle.min.js'
bundle = bundle_path.read_text()
marker = 'document.addEventListener("DOMContentLoaded",()=>{const r=t.namespace'
assert bundle.count(marker) == 1, 'Mermaid 번들의 시작 코드가 바뀌었습니다. 재검토가 필요합니다.'
config = json.loads((SOURCE / 'mermaid.config.json').read_text())
bootstrap = r'''const kindleRender=async()=>{
try{
const faces=await document.fonts.load('16px "Pretendard Variable"','프로젝트 자료 ABC');
if(!faces.length)throw new Error('Pretendard 글꼴을 불러오지 못했습니다.');
or.initialize(CONFIG);
for(const block of document.querySelectorAll('.kindle-mermaid')){
  let source=block.textContent.replace(/%%\{[\s\S]*?\}%%/g,'');
  source=source.replace(/((?:fill|stroke|color)\s*:)\s*#[a-f\d]{3,8}/gi,(all,key)=>key+(key.startsWith('fill')?'#f4f4ef':key.startsWith('stroke')?'#707070':'#202020'));
  try{
    const result=await or.render('kindle-'+crypto.randomUUID(),source);
    block.innerHTML=result.svg;
    const svg=block.querySelector('svg');
    const box=svg.viewBox.baseVal;
    svg.style.width=box.width+'px';svg.style.maxWidth='none';svg.style.height='auto';
    block.dataset.rendered='true';
    result.bindFunctions?.(block);
  }catch(error){block.dataset.rendered='error';console.error('[문서 도식]',error);}
}
}catch(error){console.error('[문서 도식 초기화]',error);}
};
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',kindleRender,{once:true});else kindleRender();
})();})();'''
config['startOnLoad'] = False
bootstrap = bootstrap.replace('CONFIG', json.dumps(config, ensure_ascii=False, separators=(',', ':')))
generated = bundle[:bundle.index(marker)] + bootstrap
(static / 'js').mkdir(exist_ok=True)
(static / 'js/moai-mermaid.bundle.js').write_text(generated)
provenance = {'engine_source': str(bundle_path.relative_to(WWW)), 'engine_sha256': hashlib.sha256(bundle.encode()).hexdigest(),
              'config_sha256': hashlib.sha256((SOURCE / 'mermaid.config.json').read_bytes()).hexdigest(),
              'bundle_sha256': hashlib.sha256(generated.encode()).hexdigest(), 'font_sha256': hashlib.sha256((static / 'fonts/PretendardVariable.woff2').read_bytes()).hexdigest()}
(DS / 'kindle-provenance.json').write_text(json.dumps(provenance, indent=2))
print('kindle_assets: tokens, local Pretendard, Mermaid bootstrap generated')
