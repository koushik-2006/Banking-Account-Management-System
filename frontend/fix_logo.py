import glob
import re
import os

svg_logo_root = """<a href="index.html" class="logo-container" style="display:flex;align-items:center;gap:8px;text-decoration:none;">
  <svg width="36" height="36" viewBox="0 0 36 36" fill="none" xmlns="http://www.w3.org/2000/svg">
    <rect width="36" height="36" rx="8" fill="#0A2342"/>
    <rect x="6" y="20" width="5" height="10" fill="#C9A84C"/>
    <rect x="13" y="14" width="5" height="16" fill="#C9A84C"/>
    <rect x="20" y="8" width="5" height="22" fill="#C9A84C"/>
    <rect x="6" y="18" width="22" height="2" fill="#F0C040"/>
  </svg>
  <span style="font-size:20px;font-weight:700;color:#0A2342;letter-spacing:1px;">BAMS</span>
</a>"""

svg_logo_admin = svg_logo_root.replace('href="index.html"', 'href="../index.html"')

def fix_logos(directory, is_admin=False):
    for filepath in glob.glob(os.path.join(directory, '*.html')):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Regex to match the old logo container:
        # <a href="index.html" class="logo-container">
        #     <img src="images/logo.png" alt="BAMS Logo">
        #     <span>BAMS</span>
        # </a>
        # This regex will match across multiple lines
        pattern = r'<a[^>]*class="logo-container"[^>]*>[\s\S]*?</a>'
        
        replacement = svg_logo_admin if is_admin else svg_logo_root
        
        new_content, count = re.subn(pattern, replacement, content)
        
        if count > 0:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {count} logo(s) in {filepath}")

# Process frontend root
fix_logos('.')

# Process admin directory if it exists
if os.path.exists('admin'):
    fix_logos('admin', is_admin=True)

