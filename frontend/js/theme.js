function toggleTheme() {
  const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
  const newTheme = isDark ? 'light' : 'dark';
  document.documentElement.setAttribute('data-theme', newTheme);
  localStorage.setItem('bams_theme', newTheme);
  const icon = document.getElementById('theme-icon');
  const lbl = document.getElementById('theme-label');
  if(icon) icon.textContent = newTheme === 'dark' ? '☀️' : '🌙';
  if(lbl) lbl.textContent = newTheme === 'dark' ? 'Light' : 'Dark';
}
(function initTheme() {
  const saved = localStorage.getItem('bams_theme') || 'light';
  document.documentElement.setAttribute('data-theme', saved);
  window.addEventListener('DOMContentLoaded', () => {
      const icon = document.getElementById('theme-icon');
      const lbl = document.getElementById('theme-label');
      if (icon) icon.textContent = saved === 'dark' ? '☀️' : '🌙';
      if (lbl) lbl.textContent = saved === 'dark' ? 'Light' : 'Dark';
  });
})();
