(() => {
  'use strict';
  const slides = [...document.querySelectorAll('.slide')];
  const byId = new Map(slides.map((slide, index) => [slide.dataset.slide, index]));
  const $ = selector => document.querySelector(selector);
  const sourceDialog = $('#source-dialog'), outlineDialog = $('#outline-dialog');
  const dialogs = [sourceDialog, outlineDialog];
  let index = 0, mode = 'present', returnFocus = null;

  function parseLocation() {
    const [requestedMode, id] = location.hash.slice(1).split('/');
    mode = requestedMode === 'read' ? 'read' : 'present';
    index = byId.has(id) ? byId.get(id) : 0;
  }
  function updateLocation(push = false) {
    const hash = `#${mode}/${slides[index].dataset.slide}`;
    if (location.hash !== hash) history[push ? 'pushState' : 'replaceState'](null, '', hash);
  }
  function render({focus = false, scroll = false} = {}) {
    document.body.dataset.mode = mode;
    slides.forEach((slide, i) => { slide.hidden = mode === 'present' && i !== index; });
    document.querySelectorAll('[data-mode-switch]').forEach(button => button.setAttribute('aria-pressed', String(button.dataset.modeSwitch === mode)));
    $('#previous').disabled = index === 0;
    $('#next').disabled = index === slides.length - 1;
    $('#next').textContent = index === slides.length - 1 ? 'End' : 'Next';
    $('#page-status').textContent = `${String(index + 1).padStart(2, '0')} / ${slides.length}`;
    $('#live-status').textContent = `Slide ${index + 1} of ${slides.length}. ${slides[index].dataset.title}`;
    document.querySelectorAll('[data-chapter-jump]').forEach(button => {
      const active = button.dataset.chapterJump === slides[index].dataset.chapter;
      button.classList.toggle('current', active);
      if (active) button.setAttribute('aria-current', 'step');
      else button.removeAttribute('aria-current');
    });
    document.querySelectorAll('[data-slide-jump]').forEach(link => {
      if (link.dataset.slideJump === slides[index].dataset.slide) link.setAttribute('aria-current', 'page');
      else link.removeAttribute('aria-current');
    });
    if (focus) slides[index].querySelector('.slide-title').focus({preventScroll: true});
    if (scroll) (mode === 'read' ? slides[index] : document.querySelector('.app-main')).scrollIntoView({block: 'start', behavior: 'instant'});
  }
  function go(newIndex) {
    index = Math.max(0, Math.min(newIndex, slides.length - 1));
    updateLocation(true);
    render({focus: true, scroll: true});
  }
  function openDialog(dialog, trigger) {
    returnFocus = trigger;
    dialog.showModal();
    dialog.querySelector('[data-close-dialog]').focus();
  }
  dialogs.forEach(dialog => dialog.addEventListener('close', () => {
    if (returnFocus?.isConnected && !returnFocus.closest('[hidden]')) returnFocus.focus({preventScroll: true});
  }));
  $('#next').addEventListener('click', () => go(index + 1));
  $('#previous').addEventListener('click', () => go(index - 1));
  document.querySelectorAll('[data-mode-switch]').forEach(button => button.addEventListener('click', () => {
    mode = button.dataset.modeSwitch;
    updateLocation(true);
    render({scroll: true});
  }));
  document.querySelectorAll('[data-chapter-jump]').forEach(button => button.addEventListener('click', () => {
    go(slides.findIndex(slide => slide.dataset.chapter === button.dataset.chapterJump));
  }));
  $('#outline-toggle').addEventListener('click', event => openDialog(outlineDialog, event.currentTarget));
  document.querySelectorAll('[data-close-dialog]').forEach(button => button.addEventListener('click', () => button.closest('dialog').close()));
  document.querySelectorAll('[data-slide-jump]').forEach(link => link.addEventListener('click', event => {
    event.preventDefault();
    returnFocus = null;
    outlineDialog.close();
    go(byId.get(link.dataset.slideJump));
  }));
  document.querySelectorAll('[data-show-source]').forEach(button => button.addEventListener('click', () => {
    const slide = slides[byId.get(button.dataset.showSource)];
    $('#source-heading').textContent = slide.dataset.title;
    $('#source-body').replaceChildren($('#notes-' + slide.dataset.slide).content.cloneNode(true));
    openDialog(sourceDialog, button);
  }));
  async function fullscreen() {
    try {
      if (document.fullscreenElement) await document.exitFullscreen();
      else await document.documentElement.requestFullscreen();
      $('#fullscreen-message').textContent = '';
    } catch {
      $('#fullscreen-message').textContent = 'Use your browser’s fullscreen command.';
    }
  }
  $('#fullscreen-toggle').addEventListener('click', fullscreen);
  document.addEventListener('fullscreenchange', () => {
    const active = Boolean(document.fullscreenElement);
    $('#fullscreen-toggle').textContent = active ? 'Exit fullscreen' : 'Fullscreen';
    $('#fullscreen-toggle').setAttribute('aria-pressed', String(active));
  });
  document.addEventListener('keydown', event => {
    if (mode !== 'present' || dialogs.some(dialog => dialog.open) || event.ctrlKey || event.metaKey || event.altKey || event.shiftKey) return;
    if (event.target.closest('input,textarea,select,[contenteditable=true],.table-wrap')) return;
    if (event.target.closest('button,a,summary') && [' ', 'Enter'].includes(event.key)) return;
    if (['ArrowRight', 'PageDown', ' '].includes(event.key)) { event.preventDefault(); go(index + 1); }
    else if (['ArrowLeft', 'PageUp'].includes(event.key)) { event.preventDefault(); go(index - 1); }
    else if (event.key === 'Home') { event.preventDefault(); go(0); }
    else if (event.key === 'End') { event.preventDefault(); go(slides.length - 1); }
    else if (event.key.toLowerCase() === 'f') fullscreen();
  });
  function restoreLocation() { parseLocation(); render({focus: true, scroll: true}); }
  window.addEventListener('popstate', restoreLocation);
  window.addEventListener('hashchange', restoreLocation);
  window.addEventListener('beforeprint', () => slides.forEach(slide => { slide.hidden = false; }));
  window.addEventListener('afterprint', () => render());
  parseLocation();
  updateLocation();
  render();
})();
