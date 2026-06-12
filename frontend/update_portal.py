import glob
import re

portal_files = ['dashboard.html', 'account.html', 'profile.html', 'transactions.html', 'transfer.html', 'loans.html', 'cards.html', 'fixed-deposits.html', 'notifications.html', 'beneficiary.html', 'deposit.html', 'withdraw.html']

script_to_add = """
function loadUserSession() {
  const user = JSON.parse(localStorage.getItem('bams_user') || 'null');
  if (!user) {
    window.location.href = 'login.html';
    return;
  }
  const firstName = user.name ? user.name.split(' ')[0] : 'User';
  const welcomeEls = document.querySelectorAll('.user-welcome-name, .sidebar-user-name, #welcome-name');
  welcomeEls.forEach(el => el.textContent = firstName);
  const fullNameEls = document.querySelectorAll('.user-full-name, #user-full-name');
  fullNameEls.forEach(el => {
    if (el.tagName === 'INPUT') el.value = user.name || 'Account Holder';
    else el.textContent = user.name || 'Account Holder';
  });
  const emailEls = document.querySelectorAll('.user-email, #user-email');
  emailEls.forEach(el => {
    if (el.tagName === 'INPUT') el.value = user.email || '';
    else el.textContent = user.email || '';
  });
  if (user.picture) {
    const avatarEls = document.querySelectorAll('.user-avatar, #user-avatar');
    avatarEls.forEach(el => { if(el.tagName === 'IMG') el.src = user.picture; });
  }
  const accountNo = user.accountNumber || 'BAMS2026' + Math.floor(1000 + Math.random()*9000);
  const accEls = document.querySelectorAll('.user-account-no, #user-account-no');
  accEls.forEach(el => el.textContent = accountNo);
}
loadUserSession();
"""

for file in portal_files:
    if file not in glob.glob('*.html'):
        continue
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Add JS
    if 'loadUserSession()' not in content:
        content = content.replace('<script src="js/app.js"></script>', '<script>\n' + script_to_add + '</script>\n    <script src="js/app.js"></script>')

    # 2. Replace Logout button (fixed redirect logic to index.html instead of ../index.html because these are already in the root frontend directory alongside index.html)
    content = re.sub(r'<a href="login\.html" class="sidebar-link[^>]*>.*?Logout</a>', r'<a href="#" onclick="localStorage.removeItem('bams_user'); window.location.href='index.html';" class="sidebar-link logout-link"><span class="icon">🚪</span> Logout</a>', content)

    # 3. Welcome back Koushik
    content = re.sub(r'Welcome back, <span id="userName">Koushik</span>', r'Welcome back, <span class="user-welcome-name"></span>', content)
    content = re.sub(r'Welcome back, Koushik', r'Welcome back, <span class="user-welcome-name"></span>', content)

    # 4. Profile name & email
    content = re.sub(r'<h2>Koushik</h2>', r'<h2 class="user-full-name"></h2>', content)
    content = re.sub(r'<input type="text" value="Koushik" readonly>', r'<input type="text" class="user-full-name" readonly>', content)
    content = re.sub(r'<input type="email" value="koushik@example\.com">', r'<input type="email" class="user-email">', content)
    content = re.sub(r'>koushik@example\.com<', r'><span class="user-email"></span><', content)

    # 5. Acc number
    content = re.sub(r'<span class="acc-number">Acc: 00987654321</span>', r'<span class="acc-number">Acc: <span class="user-account-no"></span></span>', content)
    content = re.sub(r'>00987654321<', r'><span class="user-account-no"></span><', content)

    # 6. KOUSHIK USER
    content = re.sub(r'KOUSHIK USER', r'<span class="user-full-name"></span>', content)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print('Portal files updated.')
