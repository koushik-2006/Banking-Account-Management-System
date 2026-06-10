import re
import os

def update_footer(html):
    new_footer = """<div class="footer-col-2">
                    <h4 class="footer-title">Our Services</h4>
                    <ul class="footer-links">
                        <li><a href="savings-account.html">Savings Account</a></li>
                        <li><a href="current-account.html">Current Account</a></li>
                        <li><a href="fixed-deposit.html">Fixed Deposit</a></li>
                        <li><a href="personal-loan.html">Personal Loan</a></li>
                        <li><a href="home-loan.html">Home Loan</a></li>
                        <li><a href="credit-card.html">Credit Card</a></li>
                    </ul>
                </div>"""
    # Replace the Quick Links column
    html = re.sub(r'<div class="footer-col-2">.*?<h4 class="footer-title">Quick Links</h4>.*?</div>', new_footer, html, flags=re.DOTALL)
    return html

# 1 & 2. UPDATE services.html and index.html Apply Links
for filename in ['services.html', 'index.html']:
    if not os.path.exists(filename): continue
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Savings Account
    content = re.sub(r'<h3>Savings Account</h3>(.*?)<a href="[^"]+" class="btn btn-primary" style="flex: 1;">Apply Now</a>', 
                     r'<h3>Savings Account</h3>\1<a href="apply-savings.html" class="btn btn-primary" style="flex: 1;">Apply Now</a>', content, flags=re.DOTALL)
    
    # Current Account
    content = re.sub(r'<h3>Current Account</h3>(.*?)<a href="[^"]+" class="btn btn-primary" style="flex: 1;">Apply Now</a>', 
                     r'<h3>Current Account</h3>\1<a href="apply-current.html" class="btn btn-primary" style="flex: 1;">Apply Now</a>', content, flags=re.DOTALL)
    
    # Fixed Deposit
    content = re.sub(r'<h3>Fixed Deposit</h3>(.*?)<a href="[^"]+" class="btn btn-primary" style="flex: 1;">Apply Now</a>', 
                     r'<h3>Fixed Deposit</h3>\1<a href="apply-fd.html" class="btn btn-primary" style="flex: 1;">Apply Now</a>', content, flags=re.DOTALL)
    
    # Personal Loan
    content = re.sub(r'<h3>Personal Loan</h3>(.*?)<a href="[^"]+" class="btn btn-primary" style="flex: 1;">Apply Now</a>', 
                     r'<h3>Personal Loan</h3>\1<a href="apply-personal-loan.html" class="btn btn-primary" style="flex: 1;">Apply Now</a>', content, flags=re.DOTALL)
                     
    # Home Loan
    content = re.sub(r'<h3>Home Loan</h3>(.*?)<a href="[^"]+" class="btn btn-primary" style="flex: 1;">Apply Now</a>', 
                     r'<h3>Home Loan</h3>\1<a href="apply-home-loan.html" class="btn btn-primary" style="flex: 1;">Apply Now</a>', content, flags=re.DOTALL)
                     
    # Credit Card
    content = re.sub(r'<h3>Credit Card</h3>(.*?)<a href="[^"]+" class="btn btn-primary" style="flex: 1;">Apply Now</a>', 
                     r'<h3>Credit Card</h3>\1<a href="apply-credit-card.html" class="btn btn-primary" style="flex: 1;">Apply Now</a>', content, flags=re.DOTALL)

    content = update_footer(content)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

# 3. UPDATE dashboard.html
with open('dashboard.html', 'r', encoding='utf-8') as f:
    dash = f.read()

# Add to sidebar
my_app_link = '<a href="my-applications.html" class="sidebar-link"><span class="icon">📄</span> My Applications</a>\n            <hr class="sidebar-divider">'
if 'My Applications' not in dash:
    dash = dash.replace('<hr class="sidebar-divider">', my_app_link)

# Add quick apply section
quick_apply = """
<!-- Quick Apply Section -->
<div class="card" style="margin-top:20px;">
    <h3 class="card-title">Apply for Services</h3>
    <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(150px, 1fr)); gap:15px; margin-top:15px;">
        <a href="apply-fd.html" style="text-decoration:none; background:var(--bg-main); padding:15px; border-radius:8px; border:1px solid var(--border-color); text-align:center; color:var(--text-main); font-weight:bold; transition:0.2s;">
            <div style="font-size:1.5rem; margin-bottom:5px;">💎</div> Fixed Deposit
        </a>
        <a href="apply-personal-loan.html" style="text-decoration:none; background:var(--bg-main); padding:15px; border-radius:8px; border:1px solid var(--border-color); text-align:center; color:var(--text-main); font-weight:bold; transition:0.2s;">
            <div style="font-size:1.5rem; margin-bottom:5px;">💰</div> Personal Loan
        </a>
        <a href="apply-home-loan.html" style="text-decoration:none; background:var(--bg-main); padding:15px; border-radius:8px; border:1px solid var(--border-color); text-align:center; color:var(--text-main); font-weight:bold; transition:0.2s;">
            <div style="font-size:1.5rem; margin-bottom:5px;">🏠</div> Home Loan
        </a>
        <a href="apply-credit-card.html" style="text-decoration:none; background:var(--bg-main); padding:15px; border-radius:8px; border:1px solid var(--border-color); text-align:center; color:var(--text-main); font-weight:bold; transition:0.2s;">
            <div style="font-size:1.5rem; margin-bottom:5px;">💳</div> Credit Card
        </a>
        <a href="transfer.html" style="text-decoration:none; background:var(--bg-main); padding:15px; border-radius:8px; border:1px solid var(--border-color); text-align:center; color:var(--text-main); font-weight:bold; transition:0.2s;">
            <div style="font-size:1.5rem; margin-bottom:5px;">🔄</div> Transfer
        </a>
        <a href="transactions.html" style="text-decoration:none; background:var(--bg-main); padding:15px; border-radius:8px; border:1px solid var(--border-color); text-align:center; color:var(--text-main); font-weight:bold; transition:0.2s;">
            <div style="font-size:1.5rem; margin-bottom:5px;">📊</div> Statement
        </a>
    </div>
</div>
"""
if 'Apply for Services' not in dash:
    dash = dash.replace('<!-- Dashboard Content -->', '<!-- Dashboard Content -->\n        <div class="dashboard-content">\n            ' + quick_apply)

with open('dashboard.html', 'w', encoding='utf-8') as f:
    f.write(dash)

# 4. UPDATE admin/applications.html
admin_app = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Manage Applications | Admin | Easy pAy</title>
    <link rel="stylesheet" href="../css/variables.css">
    <link rel="stylesheet" href="../css/style.css">
    <link rel="stylesheet" href="../css/service-pages.css">
</head>
<body class="dashboard-body">
    <aside class="sidebar" id="sidebar" style="background:#000;">
        <div class="sidebar-header">
            <h2 style="color:var(--primary);">Admin Panel</h2>
        </div>
        <nav class="sidebar-nav">
            <a href="index.html" class="sidebar-link">📊 Overview</a>
            <a href="applications.html" class="sidebar-link active">📄 Applications</a>
            <a href="../login.html" class="sidebar-link logout-link">🚪 Logout</a>
        </nav>
    </aside>

    <main class="dashboard-main" style="padding:20px;">
        <h1 class="mb-md">Manage Applications</h1>
        <div class="card" style="padding:0;">
            <div style="background:var(--bg-main); padding:15px; display:flex; gap:10px; border-bottom:1px solid var(--border-color);">
                <button class="btn btn-outline active" onclick="loadTab('bams_savings_apps', this)">Savings</button>
                <button class="btn btn-outline" onclick="loadTab('bams_current_apps', this)">Current</button>
                <button class="btn btn-outline" onclick="loadTab('bams_fd_apps', this)">Fixed Deposits</button>
                <button class="btn btn-outline" onclick="loadTab('bams_loan_apps', this)">Personal Loans</button>
                <button class="btn btn-outline" onclick="loadTab('bams_homeloan_apps', this)">Home Loans</button>
                <button class="btn btn-outline" onclick="loadTab('bams_card_apps', this)">Credit Cards</button>
            </div>
            <div class="table-responsive" style="padding:20px;">
                <table class="rates-table" style="margin:0;">
                    <thead><tr><th>Ref No</th><th>Applicant</th><th>Details</th><th>Date</th><th>Status</th><th>Action</th></tr></thead>
                    <tbody id="adminBody"></tbody>
                </table>
            </div>
        </div>
    </main>
    <script>
    let currentKey = 'bams_savings_apps';
    function loadTab(key, btn) {
        document.querySelectorAll('.btn-outline').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        currentKey = key;
        renderAdmin();
    }
    
    function renderAdmin() {
        const apps = JSON.parse(localStorage.getItem(currentKey) || '[]');
        const tb = document.getElementById('adminBody');
        tb.innerHTML = '';
        apps.reverse().forEach((app, index) => {
            const ref = app.accNo || app.fdRef || app.loanRef || app.hlRef || app.ccRef || 'Unknown';
            const name = app.name || app.bizName || app.authName || 'User';
            const det = app.deposit ? '₹'+app.deposit : (app.amount ? '₹'+app.amount : (app.cardType || 'N/A'));
            const d = new Date(app.date || new Date()).toLocaleDateString();
            const stat = app.status || 'Pending';
            
            let badge = 'status-pending';
            if(stat.includes('Approv') || stat.includes('Active')) badge = 'status-active';
            if(stat.includes('Reject')) badge = 'status-blocked';
            
            let btnHtml = '';
            if(!stat.includes('Approv') && !stat.includes('Active')) {
                // Reverse index because we reversed the array to show newest first.
                const origIdx = apps.length - 1 - index;
                btnHtml = `<button class="btn btn-accent" style="padding:4px 8px;font-size:0.8rem;" onclick="approveApp('${currentKey}', ${origIdx})">Approve</button>`;
            }
            
            tb.innerHTML += `<tr>
                <td><strong>${ref}</strong></td>
                <td>${name}</td>
                <td>${det}</td>
                <td>${d}</td>
                <td><span class="status-badge ${badge}">${stat}</span></td>
                <td>${btnHtml}</td>
            </tr>`;
        });
    }
    
    function approveApp(key, index) {
        const apps = JSON.parse(localStorage.getItem(key) || '[]');
        const app = apps[index];
        app.status = 'Approved';
        localStorage.setItem(key, JSON.stringify(apps));
        
        // If savings/current, activate account
        if(key === 'bams_savings_apps' || key === 'bams_current_apps') {
            const users = JSON.parse(localStorage.getItem('bams_users') || '[]');
            // Try to find the user in DB - for demo we just update the logged in user if it matches
            const u = JSON.parse(localStorage.getItem('bams_user'));
            if(u && u.accountNumber === app.accNo) {
                u.accountStatus = 'Active';
                localStorage.setItem('bams_user', JSON.stringify(u));
            }
        }
        renderAdmin();
    }
    renderAdmin();
    </script>
</body>
</html>
"""
os.makedirs('admin', exist_ok=True)
with open('admin/applications.html', 'w', encoding='utf-8') as f:
    f.write(admin_app)

print("Wiring complete.")
