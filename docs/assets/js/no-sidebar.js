document.querySelectorAll('.sidebar').forEach(el => {
  if (!el.textContent.trim()) el.remove();
});
