(() => {
  Promise.all([
    document.fonts.load('400 16px "Pretendard Variable"', '한글 자료 ABC'),
    document.fonts.load('700 16px "Pretendard Variable"', '한글 자료 ABC')
  ]).then(fonts => {
    document.documentElement.dataset.fontsLoaded = String(fonts.every(list => list.length > 0));
  }).catch(error => {
    document.documentElement.dataset.fontsLoaded = 'false';
    console.error('Pretendard 글꼴을 불러오지 못했습니다.', error);
  });
  const views = [...document.querySelectorAll('[data-view]')];
  const links = [...document.querySelectorAll('[data-view-link]')];

  const showView = () => {
    const name = location.hash.slice(1).split('?')[0] || 'home';
    const anchor = document.getElementById(name);
    const target = views.find(v => v.dataset.view === name) || anchor?.closest('[data-view]') || (anchor ? views.find(v => !v.hidden) : views[0]);
    views.forEach(v => { v.hidden = v !== target; });
    links.forEach(a => {
      if (a.dataset.viewLink === target.dataset.view) a.setAttribute('aria-current', 'page');
      else a.removeAttribute('aria-current');
    });
    document.querySelector('[data-toc]').hidden = target.dataset.view !== 'lesson';
    document.title = target.querySelector('h1').innerText.replace(/\s+/g, ' ') + ' · 킨들 시안';
    if (anchor) anchor.scrollIntoView();
    else window.scrollTo(0, 0);
  };
  document.querySelectorAll('[role=tablist]').forEach(list => {
    const tabs = [...list.querySelectorAll('[role=tab]')];
    const select = (tab, focus = false) => {
      tabs.forEach(b => {
        const active = b === tab;
        b.setAttribute('aria-selected', String(active));
        b.tabIndex = active ? 0 : -1;
        document.getElementById(b.getAttribute('aria-controls')).hidden = !active;
      });
      if (focus) tab.focus();
    };
    tabs.forEach((tab, i) => {
      tab.addEventListener('click', () => select(tab));
      tab.addEventListener('keydown', e => {
        const next = {ArrowRight: tabs[(i + 1) % tabs.length], ArrowLeft: tabs[(i - 1 + tabs.length) % tabs.length], Home: tabs[0], End: tabs[tabs.length - 1]}[e.key];
        if (next) { e.preventDefault(); select(next, true); }
      });
    });
  });
  document.querySelector('[data-copy]').addEventListener('click', async e => {
    const button = e.currentTarget;
    try {
      await navigator.clipboard.writeText(document.querySelector('[data-request]').textContent);
      button.textContent = '복사됨';
    } catch { button.textContent = '복사하지 못함'; }
  });
  document.querySelector('[data-form]').addEventListener('submit', e => {
    e.preventDefault();
    const data = new FormData(e.currentTarget);
    document.querySelector('[data-form-result]').textContent = data.get('review') ? `${data.get('goal') || '업무'} · ${data.get('app')} · 결과 검토 포함` : '결과 검토 항목도 확인해 주세요.';
  });
  window.addEventListener('hashchange', showView);
  showView();
})();
