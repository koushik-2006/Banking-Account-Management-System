import glob
import re

portal_files = [f for f in glob.glob('*.html') if '<aside class="sidebar"' in open(f, encoding='utf-8').read()]

print(f'Found {len(portal_files)} portal files: {portal_files}')

for f in portal_files:
    content = open(f, encoding='utf-8').read()
    
    welcome_match = re.search(r'Welcome back,.*?(?=<)', content)
    if welcome_match:
        print(f'{f}: {welcome_match.group()}')
    
    acc_match = re.search(r'Acc: \d+', content)
    if acc_match:
        print(f'{f}: {acc_match.group()}')
        
    if 'Koushik' in content or 'KOUSHIK' in content:
        print(f'{f} contains Koushik')
