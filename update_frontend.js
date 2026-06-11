const fs = require('fs');
const path = require('path');

const files = [
  'login.html', 'register.html', 'dashboard.html', 'account.html', 'transfer.html',
  'loans.html', 'cards.html', 'fixed-deposits.html', 'apply-savings.html', 'apply-current.html'
];
const adminFiles = [
  'admin/dashboard.html', 'admin/db-viewer.html', 'admin/users.html', 'admin/loans.html', 'admin/cards.html'
];

function injectScript(filePath, isAdmin = false) {
  if (!fs.existsSync(filePath)) return;
  let content = fs.readFileSync(filePath, 'utf-8');
  const scriptTag = isAdmin ? '<script src="../js/api.js"></script>' : '<script src="js/api.js"></script>';
  if (!content.includes('api.js')) {
    content = content.replace('</head>', `    ${scriptTag}\n</head>`);
    fs.writeFileSync(filePath, content);
  }
}

// 1. Inject API script to all pages
files.forEach(f => injectScript(path.join('frontend', f), false));
adminFiles.forEach(f => injectScript(path.join('frontend', f), true));

// 2. Update login.html logic
const loginPath = path.join('frontend', 'login.html');
if (fs.existsSync(loginPath)) {
  let loginHtml = fs.readFileSync(loginPath, 'utf-8');
  
  // Replace the old submit logic with API logic
  const oldSubmitLogicRegex = /document\.getElementById\('login-form'\)\.addEventListener\('submit',[\s\S]*?\}\);/;
  const newLoginLogic = `document.getElementById('login-form').addEventListener('submit', async (e) => {
  e.preventDefault();
  const btn = document.getElementById('login-btn');
  const msg = document.getElementById('login-message');
  btn.disabled = true; btn.textContent = 'Signing in...';
  try {
    const res = await EasyPayAPI.login({ accountNumber: document.getElementById('account-number').value.trim(), password: document.getElementById('password').value });
    if (res.success) {
      localStorage.setItem('bams_user', JSON.stringify(res.data));
      msg.className = 'msg-box msg-success'; msg.textContent = '✓ ' + res.message; msg.style.display='block';
      const redirect = localStorage.getItem('bams_redirect_after_login') || 'dashboard.html';
      localStorage.removeItem('bams_redirect_after_login');
      setTimeout(() => window.location.href = redirect, 1000);
    } else {
      msg.className = 'msg-box msg-error'; msg.textContent = '✗ ' + res.message; msg.style.display='block';
      btn.disabled = false; btn.textContent = 'Login';
    }
  } catch {
    msg.className = 'msg-box msg-error'; msg.textContent = '⚠ Cannot connect to server. Is Spring Boot running on port 8080?'; msg.style.display='block';
    btn.disabled = false; btn.textContent = 'Login';
  }
});`;
  if (loginHtml.match(oldSubmitLogicRegex)) {
    loginHtml = loginHtml.replace(oldSubmitLogicRegex, newLoginLogic);
  } else {
    // Append it before </body> if no match
    loginHtml = loginHtml.replace('</body>', `<script>\n${newLoginLogic}\n</script>\n</body>`);
  }
  fs.writeFileSync(loginPath, loginHtml);
}

// 3. Update dashboard.html logic
const dashPath = path.join('frontend', 'dashboard.html');
if (fs.existsSync(dashPath)) {
  let dashHtml = fs.readFileSync(dashPath, 'utf-8');
  const oldLoadRegex = /function loadDashboard\(\)[\s\S]*?loadDashboard\(\);/g;
  const newDashLogic = `async function loadDashboard() {
  const profile = await EasyPayAPI.getProfile();
  if (!profile.success) { window.location.href = 'login.html'; return; }
  const u = profile.data;
  document.querySelectorAll('[data-user="firstName"]').forEach(el => el.textContent = u.fullName.split(' ')[0]);
  document.querySelectorAll('[data-user="balance"]').forEach(el => el.textContent = '₹' + Number(u.balance).toLocaleString('en-IN', {minimumFractionDigits:2}));
  document.querySelectorAll('[data-user="accountNumber"]').forEach(el => el.textContent = u.accountNumber);
  document.querySelectorAll('[data-user="accountType"]').forEach(el => el.textContent = u.accountType + ' Account');
  const txRes = await EasyPayAPI.getTransactions();
  if (txRes.success) {
      if (typeof renderTransactionTable === 'function') {
          renderTransactionTable(txRes.data);
      }
  }
}
loadDashboard();`;
  if (dashHtml.match(oldLoadRegex)) {
    dashHtml = dashHtml.replace(oldLoadRegex, newDashLogic);
  } else {
    dashHtml = dashHtml.replace('</body>', `<script>\n${newDashLogic}\n</script>\n</body>`);
  }
  fs.writeFileSync(dashPath, dashHtml);
}

console.log('Frontend updated with API logic.');
