import os
import re
from gen_savings import HEAD, NAVBAR, FOOTER, write_file

my_apps = HEAD.format(title="My Applications") + NAVBAR + """
<main class="section-padding bg-light">
    <div class="container">
        <h2 class="mb-md">My Applications</h2>
        
        <div class="card" style="padding:0; overflow:hidden;">
            <div style="background:var(--bg-main); padding:15px 20px; border-bottom:1px solid var(--border-color); display:flex; gap:15px; border-top-left-radius:var(--radius-lg); border-top-right-radius:var(--radius-lg);">
                <button class="btn btn-outline active" onclick="filterApps('All', this)">All</button>
                <button class="btn btn-outline" onclick="filterApps('Pending', this)">Pending</button>
                <button class="btn btn-outline" onclick="filterApps('Approved', this)">Approved / Active</button>
            </div>
            
            <div class="table-responsive" style="padding:20px;">
                <table class="rates-table" id="appsTable" style="margin:0;">
                    <thead>
                        <tr>
                            <th>Reference No</th>
                            <th>Service</th>
                            <th>Date Applied</th>
                            <th>Status</th>
                            <th>Action</th>
                        </tr>
                    </thead>
                    <tbody id="appsBody">
                        <!-- JS injected -->
                    </tbody>
                </table>
                <div id="noAppsMsg" style="display:none; text-align:center; padding:40px; color:var(--text-muted);">
                    No applications found.
                </div>
            </div>
        </div>
    </div>
</main>

<script>
requireLogin('My Applications', 'my-applications.html');
const user = getUser();

const services = [
    { key: 'bams_savings_apps', name: 'Savings Account' },
    { key: 'bams_current_apps', name: 'Current Account' },
    { key: 'bams_fd_apps', name: 'Fixed Deposit' },
    { key: 'bams_loan_apps', name: 'Personal Loan' },
    { key: 'bams_homeloan_apps', name: 'Home Loan' },
    { key: 'bams_card_apps', name: 'Credit Card' }
];

let allApps = [];

if (user) {
    services.forEach(svc => {
        const arr = JSON.parse(localStorage.getItem(svc.key) || '[]');
        arr.forEach(app => {
            // Filter apps that belong to this user via email or accNo
            if(app.email === user.email || app.accNo === user.accountNumber || app.authName === user.name) {
                allApps.push({
                    ref: app.accNo || app.fdRef || app.loanRef || app.hlRef || app.ccRef || 'Unknown',
                    service: svc.name,
                    date: new Date(app.date || new Date()).toLocaleDateString('en-IN'),
                    status: app.status || 'Pending',
                    rawStatus: app.status || 'Pending'
                });
            }
        });
    });
    // Sort newest first
    allApps.sort((a,b) => new Date(b.date) - new Date(a.date));
}

function renderApps(filter) {
    const tb = document.getElementById('appsBody');
    tb.innerHTML = '';
    
    const filtered = allApps.filter(app => {
        if(filter === 'All') return true;
        if(filter === 'Pending' && (app.rawStatus.includes('Pending') || app.rawStatus.includes('Applied'))) return true;
        if(filter === 'Approved' && (app.rawStatus.includes('Approved') || app.rawStatus.includes('Active'))) return true;
        return false;
    });
    
    if(filtered.length === 0) {
        document.getElementById('noAppsMsg').style.display = 'block';
        document.getElementById('appsTable').style.display = 'none';
    } else {
        document.getElementById('noAppsMsg').style.display = 'none';
        document.getElementById('appsTable').style.display = 'table';
        
        filtered.forEach(app => {
            let badgeClass = 'status-badge status-pending';
            if(app.rawStatus.includes('Approved') || app.rawStatus.includes('Active')) badgeClass = 'status-badge status-active';
            if(app.rawStatus.includes('Rejected')) badgeClass = 'status-badge status-blocked';
            
            tb.innerHTML += `
                <tr>
                    <td><strong style="color:var(--primary);">${app.ref}</strong></td>
                    <td>${app.service}</td>
                    <td>${app.date}</td>
                    <td><span class="${badgeClass}">${app.status}</span></td>
                    <td><button class="btn btn-outline" style="padding:5px 10px;font-size:0.8rem;">View</button></td>
                </tr>
            `;
        });
    }
}

function filterApps(filter, btn) {
    document.querySelectorAll('.btn-outline').forEach(el => el.classList.remove('active'));
    btn.classList.add('active');
    renderApps(filter);
}

renderApps('All');
</script>
""" + FOOTER + "\n<script src=\"js/theme.js\"></script>\n</body></html>"

write_file('my-applications.html', my_apps)

print("my-applications.html generated.")
