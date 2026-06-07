import os
import glob
import re

base_dir = r"c:\Users\koush\OneDrive\Desktop\Banking-Account-Management-System\frontend"

# 1. Update variables.css
variables_css_path = os.path.join(base_dir, "css", "variables.css")
with open(variables_css_path, "r", encoding="utf-8") as f:
    vars_content = f.read()

theme_vars = """
:root {
  --bg-page: #F5F7FA;
  --bg-card: #FFFFFF;
  --bg-navbar: #0A2342;
  --text-primary: #1A1A2E;
  --text-secondary: #4B5563;
  --input-bg: #FFFFFF;
}

[data-theme="dark"] {
  --bg-page: #0D1117;
  --bg-card: #161B22;
  --bg-navbar: #010409;
  --text-primary: #E6EDF3;
  --text-secondary: #8B949E;
  --border-color: #30363D;
  --input-bg: #21262D;
  --shadow-md: 0 4px 6px -1px rgba(0,0,0,0.4);
  --accent: #C9A84C;
  --accent-light: #F0C040;
}
"""
if "[data-theme=\"dark\"]" not in vars_content:
    with open(variables_css_path, "a", encoding="utf-8") as f:
        f.write("\n" + theme_vars)

# 2. Update style.css
style_css_path = os.path.join(base_dir, "css", "style.css")
with open(style_css_path, "r", encoding="utf-8") as f:
    style_content = f.read()

theme_styles = """
/* --- THEME OVERRIDES --- */
body { background: var(--bg-page); color: var(--text-primary); transition: background 0.3s, color 0.3s; }
.navbar { background: var(--bg-navbar); }
.card, .registration-card, .summary-card, .calc-item { background: var(--bg-card); border-color: var(--border-color); color: var(--text-primary); }
input, select, textarea { background: var(--input-bg); color: var(--text-primary); border-color: var(--border-color); }
.sidebar { background: #010409; }
.content-area { background: var(--bg-page); }
table th { background: var(--bg-card); color: var(--text-secondary); }
table td { border-color: var(--border-color); color: var(--text-primary); }
.modal-content, .modal-card { background: var(--bg-card); color: var(--text-primary); }
.footer { background: #010409; }

/* --- DARK MODE EXCLUSIVES --- */
[data-theme="dark"] .hero-section, [data-theme="dark"] .hero { background: #0D1117; }
[data-theme="dark"] .stats-bar { background: #010409; }
[data-theme="dark"] .service-card { background: #161B22; border-color: #30363D; }
[data-theme="dark"] .service-card:hover { border-color: #C9A84C; box-shadow: 0 0 0 1px #C9A84C; }
[data-theme="dark"] .testimonial-card { background: #161B22; }
[data-theme="dark"] .btn-outline { border-color: #C9A84C; color: #C9A84C; }
[data-theme="dark"] .btn-outline:hover { background: #C9A84C; color: #0D1117; }
[data-theme="dark"] .sidebar-link:hover { background: rgba(201,168,76,0.1); color: #C9A84C; }
[data-theme="dark"] .dashboard-metric-card { background: #161B22; border-color: #30363D; }
[data-theme="dark"] .progress-bar { background: #30363D; }
[data-theme="dark"] input:focus { border-color: #C9A84C; box-shadow: 0 0 0 3px rgba(201,168,76,0.15); }
[data-theme="dark"] .badge-pending { background: rgba(201,168,76,0.15); color: #F0C040; }
[data-theme="dark"] .badge-success { background: rgba(34,197,94,0.1); color: #4ADE80; }
[data-theme="dark"] table tr:hover { background: rgba(201,168,76,0.05); }
[data-theme="dark"] .btn-outline-nav { border-color: #C9A84C; color: #C9A84C; }
[data-theme="dark"] .btn-outline-nav:hover { background: #C9A84C; color: #010409; }
[data-theme="dark"] .breadcrumb { color: var(--text-secondary); }
"""
if "THEME OVERRIDES" not in style_content:
    with open(style_css_path, "a", encoding="utf-8") as f:
        f.write("\n" + theme_styles)

# 3. Create theme.js
theme_js_path = os.path.join(base_dir, "js", "theme.js")
theme_js_content = """function toggleTheme() {
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
"""
with open(theme_js_path, "w", encoding="utf-8") as f:
    f.write(theme_js_content)

# 4. Process all HTML files
html_files = glob.glob(os.path.join(base_dir, "*.html")) + glob.glob(os.path.join(base_dir, "admin", "*.html"))

button_html = """<button id="theme-toggle" onclick="toggleTheme()" aria-label="Toggle dark mode" style="background:none;border:1.5px solid rgba(201,168,76,0.5);border-radius:20px;padding:5px 12px;cursor:pointer;display:flex;align-items:center;gap:6px;color:#C9A84C;font-size:13px;transition:all 0.2s">
  <span id="theme-icon">🌙</span>
  <span id="theme-label">Dark</span>
</button>"""

for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    modified = False
    
    # Inject button before nav-auth-buttons or nav-actions
    if 'id="theme-toggle"' not in content:
        if '<div class="nav-auth-buttons"' in content:
            content = content.replace('<div class="nav-auth-buttons"', button_html + '\n            <div class="nav-auth-buttons"')
            modified = True
        elif '<div class="nav-actions"' in content:
            content = content.replace('<div class="nav-actions"', button_html + '\n            <div class="nav-actions"')
            modified = True
            
    # Inject script before </body>
    if 'theme.js' not in content:
        # Check if in admin
        if 'admin' in file_path.replace("\\", "/"):
            script_tag = '<script src="../js/theme.js"></script>\n</body>'
        else:
            script_tag = '<script src="js/theme.js"></script>\n</body>'
            
        content = content.replace('</body>', script_tag)
        modified = True
        
    if modified:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

print("Applied dark mode to all files.")
