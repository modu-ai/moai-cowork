// 문서 복사 버튼의 실패 표시와 프롬프트 제거를 DOM 모형으로 확인한다.
const fs = require('node:fs');
const vm = require('node:vm');
const assert = require('node:assert/strict');
const html = fs.readFileSync('www/layouts/partials/foot.html', 'utf8');
const scripts = [...html.matchAll(/<script>([\s\S]*?)<\/script>/g)];
const source = scripts.at(-1)[1];
async function run(mode) {
  let click, copiedText;
  const attrs = {}, classes = new Set(), label = {textContent:'복사'};
  const icon = {setAttribute(){},removeAttribute(){}};
  const button = {
    setAttribute(k,v){attrs[k]=v;},removeAttribute(k){delete attrs[k];},
    querySelector(q){return q==='.copy-label'?label:icon;},
    classList:{add(k){classes.add(k);},remove(k){classes.delete(k);}},
    closest(){return {querySelector(){return {innerText:'$ echo hello\n$ pwd\n'};}};},
    addEventListener(_, fn){click=fn;}
  };
  const document = {
    readyState:'complete',querySelectorAll(){return [button];},
    body:{appendChild(){},removeChild(){}},
    createElement(){return {style:{},setAttribute(){},select(){copiedText=this.value;}};},
    execCommand(){return mode==='fallback-success';}
  };
  const navigator = mode.startsWith('clipboard') ? {clipboard:{writeText(text){copiedText=text;return mode==='clipboard-success'?Promise.resolve():Promise.reject(new Error('denied'));}}} : {};
  vm.runInNewContext(source,{document,navigator,setTimeout(){}});
  click(); await Promise.resolve(); await Promise.resolve();
  assert.equal(copiedText,'echo hello\npwd');
  const success=mode.endsWith('success');
  assert.equal(classes.has('copied'),success);
  assert.equal(label.textContent,success?'복사됨':'직접 복사');
  if(!success) assert.match(attrs['aria-label'],/자동 복사 불가/);
  return {mode,observedLabel:label.textContent,promptRemoved:true};
}
(async()=>{
  const rows=[];
  for(const mode of ['clipboard-success','clipboard-denied','fallback-success','fallback-denied']) rows.push(await run(mode));
  fs.writeFileSync('reports/20261005-docs-rebuild/copy-logic-check.json',JSON.stringify({scope:'DOM model, not operating-system clipboard',cases:rows},null,2)+'\n');
  console.log(JSON.stringify(rows));
})();
