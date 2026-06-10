import os
import glob
import re

def rebrand():
    frontend_dir = os.path.dirname(os.path.abspath(__file__))
    html_files = glob.glob(os.path.join(frontend_dir, '*.html')) + glob.glob(os.path.join(frontend_dir, 'admin', '*.html'))
    
    logo_svg_root = """<a href="index.html" class="logo-container" style="display:flex;align-items:center;gap:10px;text-decoration:none;">
  <div style="width:38px;height:38px;border-radius:9px;background:#C9A84C;display:flex;align-items:center;justify-content:center;flex-shrink:0;">
    <svg width="22" height="22" viewBox="0 0 22 22" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
      <rect x="2" y="14" width="4" height="6" rx="1" fill="#0A0A0A"/>
      <rect x="9" y="9" width="4" height="11" rx="1" fill="#0A0A0A"/>
      <rect x="16" y="4" width="4" height="16" rx="1" fill="#0A0A0A"/>
      <rect x="2" y="13" width="18" height="1.5" rx="0.5" fill="#0A0A0A" opacity="0.4"/>
    </svg>
  </div>
  <span style="font-size:21px;font-weight:700;font-family:'Georgia',serif;letter-spacing:0.5px;color:#C9A84C;line-height:1;">Easy <span style="color:#FFD700;">pAy</span></span>
</a>"""

    logo_svg_admin = logo_svg_root.replace('"index.html"', '"../index.html"')

    for filepath in html_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        is_admin = 'admin' in filepath.replace('\\', '/')

        # 1. Title tags
        content = re.sub(r'<title>(.*?)BAMS(.*?)</title>', r'<title>\1Easy pAy\2</title>', content)
        
        # 2 & 6. Logo replacements
        # We need to target any <a> or <div> with class="logo-container" or class="sidebar-brand" that contains the old logo
        # We can just look for the typical `<a href="index.html" class="logo-container"...>...</a>` block
        # Since it can span multiple lines, we'll use a regex that matches the opening tag to the closing </a>
        # but only if it contains 'BAMS' or SVG
        
        # Replace <a ... class="logo-container"...>...</a>
        content = re.sub(r'<a[^>]*class="[^"]*logo-container[^"]*"[^>]*>.*?</a>', logo_svg_admin if is_admin else logo_svg_root, content, flags=re.DOTALL)
        
        # Replace sidebar brand logo
        # Let's replace the brand text and any SVG inside <div class="sidebar-brand">
        content = re.sub(r'<div class="sidebar-brand">.*?</div>', f'<div class="sidebar-brand">\n        {logo_svg_admin if is_admin else logo_svg_root}\n    </div>', content, flags=re.DOTALL)
        
        # 8. Remove broken img tags
        content = re.sub(r'<img src="images/logo\.png"[^>]*>', '', content)
        content = re.sub(r'<img src="\.\./images/logo\.png"[^>]*>', '', content)

        # 4 & 5. Text replacements
        content = content.replace('Banking Account Management System', 'Easy pAy — Banking Management System')
        content = content.replace('Welcome to BAMS', 'Welcome to Easy pAy')
        content = content.replace('BAMS has been', 'Easy pAy has been')
        content = content.replace('BAMS Admin', 'Easy pAy Admin')
        
        # Replace generic BAMS (avoiding BAMS2026...)
        content = re.sub(r'BAMS(?![0-9])', 'Easy pAy', content)
        
        # Footer specifics
        content = content.replace('© 2026 Easy pAy — Banking Management System. All rights reserved.', '© 2026 Easy pAy. All rights reserved.')
        content = content.replace('© 2026 Easy pAy. All rights reserved.', '© 2026 Easy pAy. All rights reserved.') # identity mapping if already replaced
        
        # Let's add the footer tagline if there's a typical footer text
        # Usually: <p class="text-muted">Modern banking for the digital age.</p>
        # We will replace known old taglines with the new one.
        content = content.replace('Modern banking for the digital age.', 'Providing secure and innovative banking solutions since 2026. Your trust is our foundation.')

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
            
    print(f"Processed {len(html_files)} HTML files.")

    # 3. CSS Updates
    css_path = os.path.join(frontend_dir, 'css', 'style.css')
    if os.path.exists(css_path):
        with open(css_path, 'r', encoding='utf-8') as f:
            css = f.read()
            
        css += '''\n
/* --- Easy pAy Rebranding Overrides --- */
.navbar, header.navbar { background: #0A0A0A !important; }
[data-theme="dark"] .navbar { background: #000000 !important; }
.nav-link { color: #8B949E; }
.nav-link:hover, .nav-link.active { color: #C9A84C; }
'''
        with open(css_path, 'w', encoding='utf-8') as f:
            f.write(css)
        print("Updated style.css")
        
rebrand()
