import glob
import re
import os

portal_files = ['dashboard.html', 'account.html', 'profile.html', 'transactions.html', 'transfer.html', 'loans.html', 'cards.html', 'fixed-deposits.html', 'notifications.html', 'beneficiary.html', 'deposit.html', 'withdraw.html']

for file in portal_files:
    if not os.path.exists(file):
        continue
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Inject auth-guard.js
    if 'auth-guard.js' not in content:
        content = content.replace('<script src="js/app.js"></script>', '<script src="js/auth-guard.js"></script>\n    <script src="js/app.js"></script>')
        content = content.replace('<script src="../js/app.js"></script>', '<script src="../js/auth-guard.js"></script>\n    <script src="../js/app.js"></script>')

    # 1. Welcome back Koushik
    content = re.sub(r'Welcome back, <span id="userName">Koushik</span>', r'Welcome back, <span data-user="firstName"></span>', content)
    content = re.sub(r'Welcome back, Koushik', r'Welcome back, <span data-user="firstName"></span>', content)
    
    # 2. Balance card - looking for ₹1,24,500.00 or similar
    content = re.sub(r'₹[0-9,]+\.[0-9]{2}', r'<span data-user="balance">Loading...</span>', content, count=1) # only replace the first occurrence (main balance)

    # 3. Account number
    content = re.sub(r'>Acc: 00987654321<', r'>Acc: <span data-user="accountNumber"></span><', content)
    content = re.sub(r'>00987654321<', r'><span data-user="accountNumber"></span><', content)
    
    # 4. Account type
    content = re.sub(r'>Savings Account<', r'><span data-user="accountType"></span><', content)

    # 5. Full name
    content = re.sub(r'>KOUSHIK USER<', r'><span data-user="fullName"></span><', content)
    content = re.sub(r'<h2>Koushik</h2>', r'<h2><span data-user="fullName"></span></h2>', content)
    content = re.sub(r'<input type="text" value="Koushik" readonly>', r'<input type="text" data-user="fullName" readonly>', content)
    
    # 6. Email
    content = re.sub(r'>koushik@example\.com<', r'><span data-user="email"></span><', content)
    content = re.sub(r'<input type="email" value="koushik@example\.com">', r'<input type="email" data-user="email">', content)

    # 7. Avatar Initials
    # Usually it's a div like <div class="avatar-initials">KU</div>
    content = re.sub(r'>KU<', r'><span data-user="avatarInitials"></span><', content)
    
    # 8. Status badge
    content = re.sub(r'<span class="status-badge status-active">Active</span>', r'<span class="status-badge status-active" data-user="status">Active</span>', content)

    # Replace Logout button redirect
    content = re.sub(r'<a href="login\.html" class="sidebar-link[^>]*>.*?Logout</a>', r'<a href="#" onclick="localStorage.removeItem(\'bams_user\');window.location.href=\'login.html\'" class="sidebar-link"><span class="icon">🚪</span> Logout</a>', content)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print('Applied data-user attributes to all portal files.')
