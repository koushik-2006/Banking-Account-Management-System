import os

NAVBAR = """<header class="navbar">
    <div class="container nav-container">
        <a href="index.html" class="logo-container" style="display:flex;align-items:center;gap:10px;text-decoration:none;">
            <div style="width:38px;height:38px;border-radius:9px;background:#C9A84C;display:flex;align-items:center;justify-content:center;flex-shrink:0;">
                <svg width="22" height="22" viewBox="0 0 22 22" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
                    <rect x="2" y="14" width="4" height="6" rx="1" fill="#0A0A0A"/>
                    <rect x="9" y="9" width="4" height="11" rx="1" fill="#0A0A0A"/>
                    <rect x="16" y="4" width="4" height="16" rx="1" fill="#0A0A0A"/>
                    <rect x="2" y="13" width="18" height="1.5" rx="0.5" fill="#0A0A0A" opacity="0.4"/>
                </svg>
            </div>
            <span style="font-size:21px;font-weight:700;font-family:'Georgia',serif;letter-spacing:0.5px;color:#C9A84C;line-height:1;">Easy <span style="color:#FFD700;">pAy</span></span>
        </a>
        <nav class="nav-links">
            <a href="index.html" class="nav-link">Home</a>
            <a href="services.html" class="nav-link active">Services</a>
            <a href="about.html" class="nav-link">About</a>
            <a href="contact.html" class="nav-link">Contact</a>
            <a href="faq.html" class="nav-link">Help</a>
        </nav>
        <button id="theme-toggle" onclick="toggleTheme()" aria-label="Toggle dark mode" style="background:none;border:1.5px solid rgba(201,168,76,0.5);border-radius:20px;padding:5px 12px;cursor:pointer;display:flex;align-items:center;gap:6px;color:#C9A84C;font-size:13px;transition:all 0.2s">
            <span id="theme-icon">🌙</span>
            <span id="theme-label">Dark</span>
        </button>
        <div class="nav-auth-buttons" style="display:flex; gap:10px; align-items:center;">
            <a href="login.html" class="btn btn-outline-nav">Login</a>
            <a href="register.html" class="btn btn-primary-nav">Open Account</a>
        </div>
    </div>
</header>
"""

FOOTER = """<footer class="footer">
    <div class="container text-center">
        <p>&copy; 2026 Easy pAy. All rights reserved.</p>
        <p class="text-muted" style="margin-top:10px;font-size:0.9rem;">Providing secure and innovative banking solutions since 2026. Your trust is our foundation.</p>
    </div>
</footer>
"""

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Easy pAy</title>
    <link rel="stylesheet" href="css/variables.css">
    <link rel="stylesheet" href="css/style.css">
    <link rel="stylesheet" href="css/service-pages.css">
    <script src="js/flow-guard.js"></script>
</head>
<body>
"""

def write_file(filename, content):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

# ================= SAVINGS ACCOUNT FLOW =================

savings_info = HEAD.format(title="Savings Account") + NAVBAR + """
<main>
    <section class="service-hero">
        <div class="container">
            <div class="breadcrumb"><a href="index.html">Home</a> &rarr; <a href="services.html">Services</a> &rarr; Savings Account</div>
            <h1>Savings Account</h1>
            <p class="tagline">Grow your savings with guaranteed security and high interest.</p>
            <div style="background: rgba(201, 168, 76, 0.1); padding: 15px; border-radius: 8px; margin: 20px auto; max-width: 800px; color: var(--primary); font-weight: bold; font-size: 1.1rem; border: 1px solid var(--accent);">
                4.5% Interest Rate | Zero Balance Option | Free Debit Card | Instant Account Opening
            </div>
        </div>
    </section>
    
    <section class="section-padding bg-light">
        <div class="container">
            <h2 class="text-center mb-xl">Key Features</h2>
            <div class="features-grid">
                <div class="feature-card text-center">
                    <div class="icon">📈</div>
                    <h3>4.5% Annual Interest</h3>
                    <p class="text-muted">Competitive rates calculated daily and credited quarterly on your savings balance.</p>
                </div>
                <div class="feature-card text-center">
                    <div class="icon">🚫</div>
                    <h3>Zero Monthly Fees</h3>
                    <p class="text-muted">No hidden charges or minimum maintenance fees for your core account.</p>
                </div>
                <div class="feature-card text-center">
                    <div class="icon">💳</div>
                    <h3>Free Debit Card</h3>
                    <p class="text-muted">Complimentary RuPay/Visa debit card with a ₹50,000 daily withdrawal limit.</p>
                </div>
                <div class="feature-card text-center">
                    <div class="icon">📱</div>
                    <h3>Mobile Banking</h3>
                    <p class="text-muted">24/7 banking via the Easy pAy mobile app. Manage funds securely on the go.</p>
                </div>
                <div class="feature-card text-center">
                    <div class="icon">👨‍👩‍👧</div>
                    <h3>Nomination Facility</h3>
                    <p class="text-muted">Secure your savings for your loved ones with an easy online nomination process.</p>
                </div>
                <div class="feature-card text-center">
                    <div class="icon">⚡</div>
                    <h3>Instant Account</h3>
                    <p class="text-muted">Experience same-day account activation immediately after digital KYC approval.</p>
                </div>
            </div>
        </div>
    </section>

    <section class="section-padding">
        <div class="container" style="max-width: 800px;">
            <h2 class="text-center mb-lg">Eligibility & Documents</h2>
            <table class="rates-table mb-xl">
                <tr><th>Age Requirement</th><td>18+ years (Resident Indian)</td></tr>
                <tr><th>Minimum Deposit</th><td>₹0 (Zero balance account allowed)</td></tr>
                <tr><th>Mandatory Documents</th><td>Aadhaar Card, PAN Card, Passport Size Photo</td></tr>
            </table>

            <h2 class="text-center mb-lg">Interest Rates</h2>
            <table class="rates-table">
                <thead><tr><th>Balance Slab</th><th>Interest Rate (p.a.)</th></tr></thead>
                <tbody>
                    <tr><td>Up to ₹1 Lakh</td><td>3.50%</td></tr>
                    <tr><td>₹1 Lakh to ₹10 Lakhs</td><td>4.00%</td></tr>
                    <tr><td>Above ₹10 Lakhs</td><td>4.50%</td></tr>
                </tbody>
            </table>
        </div>
    </section>

    <section class="section-padding text-center bg-light">
        <div class="container">
            <h2 class="mb-md">Ready to Open Your Account?</h2>
            <p class="text-muted mb-lg">Join thousands of customers banking with Easy pAy today.</p>
            <a href="apply-savings.html" class="btn btn-primary" style="font-size: 1.2rem; padding: 15px 40px;">Apply Now</a>
        </div>
    </section>
</main>
""" + FOOTER + "\n<script src=\"js/theme.js\"></script>\n</body></html>"

write_file('savings-account.html', savings_info)

apply_savings = HEAD.format(title="Apply Savings Account") + NAVBAR + """
<main class="section-padding bg-light">
    <div class="container container-narrow">
        <div id="login-warning" style="display:none; background: var(--bg-card); border: 2px solid var(--accent); padding: 20px; border-radius: 8px; text-align: center; margin-bottom: 30px;">
            <h3 style="color: var(--primary);">You already have an account!</h3>
            <p class="text-muted" style="margin: 10px 0;">If you want to open a Fixed Deposit or apply for a Loan, please visit your dashboard.</p>
            <a href="dashboard.html" class="btn btn-accent">Go to Dashboard</a>
        </div>

        <div class="card" id="application-form-card">
            <h2 class="text-center mb-md">Open Savings Account</h2>
            
            <div class="step-bar mb-xl">
                <div class="step-item active" id="step-btn-1">1. Personal</div>
                <div class="step-item" id="step-btn-2">2. KYC</div>
                <div class="step-item" id="step-btn-3">3. Preferences</div>
                <div class="step-item" id="step-btn-4">4. Review</div>
            </div>

            <form id="savingsForm">
                <!-- STEP 1 -->
                <div class="form-step active" id="step1">
                    <div class="form-group"><label>Full Name</label><input type="text" id="sa_name" required></div>
                    <div class="form-grid">
                        <div class="form-group">
                            <label>Date of Birth</label>
                            <input type="date" id="sa_dob" required>
                            <small id="dob-error" style="color:red;display:none;">Minimum age is 18 years</small>
                        </div>
                        <div class="form-group">
                            <label>Gender</label>
                            <div style="display:flex;gap:15px;margin-top:10px;">
                                <label><input type="radio" name="sa_gender" value="Male" checked> Male</label>
                                <label><input type="radio" name="sa_gender" value="Female"> Female</label>
                                <label><input type="radio" name="sa_gender" value="Other"> Other</label>
                            </div>
                        </div>
                    </div>
                    <div class="form-grid">
                        <div class="form-group"><label>Phone Number</label><input type="tel" id="sa_phone" pattern="[0-9]{10}" placeholder="10 digits" required></div>
                        <div class="form-group"><label>Email Address</label><input type="email" id="sa_email" required></div>
                    </div>
                    <div class="form-group"><label>Address</label><textarea id="sa_address" rows="3" required></textarea></div>
                    <div class="form-grid">
                        <div class="form-group"><label>State</label>
                            <select id="sa_state" required>
                                <option value="">Select State</option>
                                <option value="Delhi">Delhi</option>
                                <option value="Maharashtra">Maharashtra</option>
                                <option value="Karnataka">Karnataka</option>
                                <option value="Tamil Nadu">Tamil Nadu</option>
                            </select>
                        </div>
                        <div class="form-group"><label>City</label><input type="text" id="sa_city" required></div>
                    </div>
                    <div class="text-right mt-lg"><button type="button" class="btn btn-primary next-btn" onclick="nextStep(2)">Next &rarr;</button></div>
                </div>

                <!-- STEP 2 -->
                <div class="form-step" id="step2" style="display:none;">
                    <div class="form-grid">
                        <div class="form-group">
                            <label>Aadhaar Number</label>
                            <input type="number" id="sa_aadhaar" placeholder="12 digits" required>
                            <small id="aadhaar-error" style="color:red;display:none;">Must be exactly 12 digits</small>
                        </div>
                        <div class="form-group">
                            <label>PAN Number</label>
                            <input type="text" id="sa_pan" placeholder="ABCDE1234F" style="text-transform:uppercase;" required>
                            <small id="pan-error" style="color:red;display:none;">Invalid format</small>
                        </div>
                    </div>
                    <div class="form-group"><label>Occupation</label>
                        <select id="sa_occ" required>
                            <option value="Salaried">Salaried</option>
                            <option value="Self-Employed">Self-Employed</option>
                            <option value="Student">Student</option>
                            <option value="Retired">Retired</option>
                            <option value="Other">Other</option>
                        </select>
                    </div>
                    <div class="form-grid">
                        <div class="form-group"><label>Nominee Name</label><input type="text" id="sa_nom_name" required></div>
                        <div class="form-group"><label>Nominee Relation</label>
                            <select id="sa_nom_rel" required>
                                <option value="Spouse">Spouse</option>
                                <option value="Parent">Parent</option>
                                <option value="Child">Child</option>
                                <option value="Sibling">Sibling</option>
                                <option value="Friend">Friend</option>
                            </select>
                        </div>
                    </div>
                    <div class="form-group"><label>Nominee DOB</label><input type="date" id="sa_nom_dob" required></div>
                    <div class="text-between mt-lg">
                        <button type="button" class="btn btn-outline" onclick="prevStep(1)">&larr; Back</button>
                        <button type="button" class="btn btn-primary next-btn" onclick="nextStep(3)">Next &rarr;</button>
                    </div>
                </div>

                <!-- STEP 3 -->
                <div class="form-step" id="step3" style="display:none;">
                    <div class="form-group">
                        <label>Initial Deposit Amount (₹)</label>
                        <input type="number" id="sa_deposit" min="0" value="0" required>
                        <small class="text-muted">Minimum ₹0 — zero balance account allowed</small>
                    </div>
                    <div class="form-group">
                        <label>Account Mode Preference</label>
                        <div style="display:flex;gap:15px;margin-top:10px;">
                            <label><input type="radio" name="sa_mode" value="Single" checked> Single</label>
                            <label><input type="radio" name="sa_mode" value="Joint"> Joint</label>
                        </div>
                    </div>
                    <div class="form-group">
                        <label>Preferred Branch</label>
                        <select id="sa_branch">
                            <option value="Online">Online / Digital Branch</option>
                            <option value="Main Branch">Main Branch</option>
                            <option value="City Branch">City Branch</option>
                        </select>
                    </div>
                    
                    <div class="form-group mt-lg">
                        <label>Select Debit Card Type</label>
                        <div class="radio-card-grid mt-sm">
                            <label class="radio-card-label">
                                <input type="radio" name="sa_card" value="RuPay Classic" checked>
                                <div class="radio-card-content">
                                    <h4 style="color:var(--primary);">RuPay Classic</h4>
                                    <p class="text-muted" style="font-size:0.8rem;margin:5px 0;">₹0 Annual Fee</p>
                                    <p class="text-muted" style="font-size:0.8rem;">₹25,000/day limit</p>
                                </div>
                            </label>
                            <label class="radio-card-label">
                                <input type="radio" name="sa_card" value="RuPay Platinum">
                                <div class="radio-card-content">
                                    <h4 style="color:var(--primary);">RuPay Platinum</h4>
                                    <p class="text-muted" style="font-size:0.8rem;margin:5px 0;">₹200/year Fee</p>
                                    <p class="text-muted" style="font-size:0.8rem;">₹1,00,000/day limit</p>
                                </div>
                            </label>
                            <label class="radio-card-label">
                                <input type="radio" name="sa_card" value="Visa International">
                                <div class="radio-card-content">
                                    <h4 style="color:var(--primary);">Visa Intl</h4>
                                    <p class="text-muted" style="font-size:0.8rem;margin:5px 0;">₹500/year Fee</p>
                                    <p class="text-muted" style="font-size:0.8rem;">₹1,50,000/day limit</p>
                                </div>
                            </label>
                        </div>
                    </div>
                    <div class="text-between mt-lg">
                        <button type="button" class="btn btn-outline" onclick="prevStep(2)">&larr; Back</button>
                        <button type="button" class="btn btn-primary next-btn" onclick="nextStep(4)">Review &rarr;</button>
                    </div>
                </div>

                <!-- STEP 4 -->
                <div class="form-step" id="step4" style="display:none;">
                    <div class="calc-box">
                        <h3 class="mb-sm">Application Summary</h3>
                        <div class="calc-row"><span>Name:</span> <strong id="rev_name"></strong></div>
                        <div class="calc-row"><span>Phone:</span> <strong id="rev_phone"></strong></div>
                        <div class="calc-row"><span>Email:</span> <strong id="rev_email"></strong></div>
                        <div class="calc-row"><span>City, State:</span> <strong id="rev_loc"></strong></div>
                        <div class="calc-row"><span>PAN:</span> <strong id="rev_pan"></strong></div>
                        <hr style="margin:10px 0;border-color:var(--border-color);">
                        <div class="calc-row"><span>Initial Deposit:</span> <strong id="rev_dep" style="color:var(--accent);"></strong></div>
                        <div class="calc-row"><span>Debit Card:</span> <strong id="rev_card"></strong></div>
                        <div class="calc-row"><span>Nominee:</span> <strong id="rev_nom"></strong></div>
                    </div>
                    <div class="form-group mt-md">
                        <label style="font-weight:normal; display:flex; gap:10px;">
                            <input type="checkbox" id="sa_agree" required>
                            <span>I confirm all details are correct and agree to Easy pAy Terms & Conditions</span>
                        </label>
                    </div>
                    <div class="text-between mt-lg">
                        <button type="button" class="btn btn-outline" onclick="prevStep(3)">&larr; Back</button>
                        <button type="submit" class="btn btn-accent" id="submitBtn">Create My Account</button>
                    </div>
                </div>
            </form>
        </div>
    </div>
</main>
<script>
if (getUser()) {
    document.getElementById('login-warning').style.display = 'block';
}

function nextStep(step) {
    if(step === 2) {
        const dob = document.getElementById('sa_dob').value;
        if(!dob) return alert('Please enter DOB');
        const age = (new Date() - new Date(dob)) / (365.25 * 24 * 60 * 60 * 1000);
        if(age < 18) {
            document.getElementById('dob-error').style.display='block';
            return;
        }
        document.getElementById('dob-error').style.display='none';
    }
    if(step === 3) {
        const aadhaar = document.getElementById('sa_aadhaar').value;
        const pan = document.getElementById('sa_pan').value.toUpperCase();
        let err = false;
        if(!/^[2-9]{1}[0-9]{11}$/.test(aadhaar)) { document.getElementById('aadhaar-error').style.display='block'; err=true; } else { document.getElementById('aadhaar-error').style.display='none'; }
        if(!/^[A-Z]{5}[0-9]{4}[A-Z]{1}$/.test(pan)) { document.getElementById('pan-error').style.display='block'; err=true; } else { document.getElementById('pan-error').style.display='none'; }
        if(err) return;
    }
    if(step === 4) {
        document.getElementById('rev_name').textContent = document.getElementById('sa_name').value;
        document.getElementById('rev_phone').textContent = document.getElementById('sa_phone').value;
        document.getElementById('rev_email').textContent = document.getElementById('sa_email').value;
        document.getElementById('rev_loc').textContent = document.getElementById('sa_city').value + ', ' + document.getElementById('sa_state').value;
        document.getElementById('rev_pan').textContent = document.getElementById('sa_pan').value.toUpperCase();
        document.getElementById('rev_dep').textContent = '₹' + document.getElementById('sa_deposit').value;
        document.getElementById('rev_card').textContent = document.querySelector('input[name="sa_card"]:checked').value;
        document.getElementById('rev_nom').textContent = document.getElementById('sa_nom_name').value + ' (' + document.getElementById('sa_nom_rel').value + ')';
    }
    document.querySelectorAll('.form-step').forEach(el => el.style.display = 'none');
    document.querySelectorAll('.step-item').forEach((el, idx) => el.classList.toggle('active', idx < step));
    document.getElementById('step' + step).style.display = 'block';
}

function prevStep(step) {
    document.querySelectorAll('.form-step').forEach(el => el.style.display = 'none');
    document.querySelectorAll('.step-item').forEach((el, idx) => el.classList.toggle('active', idx < step));
    document.getElementById('step' + step).style.display = 'block';
}

document.getElementById('savingsForm').addEventListener('submit', (e) => {
    e.preventDefault();
    if(!document.getElementById('sa_agree').checked) return alert('Please agree to T&C');
    document.getElementById('submitBtn').disabled = true;
    document.getElementById('submitBtn').textContent = 'Processing...';
    
    const accNo = "EP" + new Date().getFullYear() + Math.floor(1000000 + Math.random() * 9000000);
    const custId = "CID" + Math.floor(100000 + Math.random() * 900000);
    const name = document.getElementById('sa_name').value;
    const email = document.getElementById('sa_email').value;
    const initialDeposit = document.getElementById('sa_deposit').value;
    
    localStorage.setItem('bams_user', JSON.stringify({
        name: name, email: email, accountNumber: accNo, accountType: 'Savings', balance: initialDeposit, custId: custId
    }));
    
    saveApplication('savings', {
        accNo, custId, name, email,
        pan: document.getElementById('sa_pan').value.toUpperCase(),
        deposit: initialDeposit,
        card: document.querySelector('input[name="sa_card"]:checked').value,
        status: 'Approved'
    });
    
    setTimeout(() => {
        window.location.href = 'savings-success.html';
    }, 1500);
});
</script>
""" + FOOTER + "\n<script src=\"js/theme.js\"></script>\n</body></html>"

write_file('apply-savings.html', apply_savings)

savings_success = HEAD.format(title="Savings Account Created") + NAVBAR + """
<main class="section-padding bg-light">
    <div class="success-container card">
        <div class="success-icon">✅</div>
        <h1 class="mb-sm" style="color:var(--text-main);">Account Created Successfully!</h1>
        <p class="text-muted mb-lg" style="font-size:1.1rem;">Welcome to Easy pAy, <strong id="succ_name"></strong>!</p>
        
        <div style="display:flex; gap:20px; justify-content:center; flex-wrap:wrap;">
            <div class="ref-box" style="flex:1; min-width:200px;">
                <p style="font-size:0.9rem; color:var(--text-muted); font-family:Inter,sans-serif;">Account Number</p>
                <div id="succ_acc" style="margin-top:10px;"></div>
            </div>
            <div class="ref-box" style="flex:1; min-width:200px; border-color:var(--border-color); color:var(--text-main);">
                <p style="font-size:0.9rem; color:var(--text-muted); font-family:Inter,sans-serif;">Customer ID</p>
                <div id="succ_cid" style="margin-top:10px;"></div>
            </div>
        </div>
        
        <div style="background:#FFFBEB; border:1px solid #FCD34D; color:#92400E; padding:15px; border-radius:8px; margin-bottom:30px; font-size:0.95rem;">
            ⚠️ <strong>Please save your Account Number.</strong> You will need it to log in to your dashboard.
        </div>

        <h3 class="text-left mb-md">What happens next?</h3>
        <div class="status-stepper text-left">
            <div style="color:var(--accent);font-weight:bold;">1. KYC Verification<br>(Done)</div>
            <div style="color:var(--accent);font-weight:bold;">2. Account Active<br>(Done)</div>
            <div>3. Debit Card Dispatch<br>(3-5 days)</div>
            <div>4. Welcome Kit<br>(7-10 days)</div>
        </div>

        <div style="display:flex; gap:15px; justify-content:center; margin-top:30px;">
            <a href="login.html" class="btn btn-primary">Go to Dashboard</a>
            <button class="btn btn-outline" onclick="downloadDetails()">Download Account Details</button>
        </div>
        <p class="text-muted mt-lg" style="font-size:0.85rem;">Need Help? Contact support@easypay.com</p>
    </div>
</main>
<script>
    const u = getUser();
    if(u) {
        document.getElementById('succ_name').textContent = u.name;
        document.getElementById('succ_acc').textContent = u.accountNumber;
        document.getElementById('succ_cid').textContent = u.custId;
    }
    
    function downloadDetails() {
        if(!u) return;
        const text = `EASY PAY - ACCOUNT DETAILS\\n\\nName: ${u.name}\\nAccount Number: ${u.accountNumber}\\nCustomer ID: ${u.custId}\\nAccount Type: Savings\\n\\nPlease keep this secure. Do not share your password.`;
        const blob = new Blob([text], {type: "text/plain"});
        const a = document.createElement("a");
        a.href = URL.createObjectURL(blob);
        a.download = "EasyPay_AccountDetails.txt";
        a.click();
    }
</script>
""" + FOOTER + "\n<script src=\"js/theme.js\"></script>\n</body></html>"

write_file('savings-success.html', savings_success)
print("Savings flow generated.")
