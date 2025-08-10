document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('a.headerlink').forEach(link => {
    link.setAttribute('aria-label', 'Permalink');
    link.textContent = '#';
  });
  document.querySelectorAll('img:not([alt])').forEach(img => {
    img.setAttribute('alt', '');
  });
});
