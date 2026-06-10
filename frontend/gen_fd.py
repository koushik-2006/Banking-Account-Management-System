from gen_savings import HEAD, NAVBAR, FOOTER, write_file

fd_info = HEAD.format(title="Fixed Deposit") + NAVBAR + """
<main>
    <section class="service-hero" style="background:#1B3D6E;color:#fff;">
        <div class="container">
            <div class="breadcrumb" style="color:#A0C4FF;"><a href="index.html" style="color:#C9A84C;">Home</a> &rarr; <a href="services.html" style="color:#C9A84C;">Services</a> &rarr; Fixed Deposit</div>
            <h1 style="color:#C9A84C;">Fixed Deposit</h1>
            <p class="tagline" style="color:#E8F4FD;">Secure your future with guaranteed returns up to 8.00%</p>
        </div>
    </section>
    
    <section class="section-padding bg-light">
        <div class="container">
            <div class="features-grid">
                <div class="feature-card text-center"><h3>Guaranteed Returns</h3><p class="text-muted">Market fluctuations don't affect your FD returns.</p></div>
                <div class="feature-card text-center"><h3>Flexible Tenure</h3><p class="text-muted">Choose any tenure from 7 days to 10 years.</p></div>
                <div class="feature-card text-center"><h3>Auto-Renewal</h3><p class="text-muted">Hassle-free automatic renewal upon maturity.</p></div>
                <div class="feature-card text-center"><h3>Premature Withdrawal</h3><p class="text-muted">Access your funds instantly in case of emergencies.</p></div>
                <div class="feature-card text-center"><h3>Loan Against FD</h3><p class="text-muted">Get an overdraft up to 90% of your FD value.</p></div>
            </div>
        </div>
    </section>

    <section class="section-padding">
        <div class="container" style="max-width: 800px;">
            <h2 class="text-center mb-lg">Fixed Deposit Interest Rates</h2>
            <table class="rates-table mb-xl">
                <thead><tr><th>Tenure</th><th>General Rate (p.a.)</th><th>Senior Citizen (p.a.)</th></tr></thead>
                <tbody>
                    <tr><td>7 - 29 days</td><td>3.00%</td><td>3.50%</td></tr>
                    <tr><td>30 - 90 days</td><td>4.00%</td><td>4.50%</td></tr>
                    <tr><td>91 - 180 days</td><td>5.50%</td><td>6.00%</td></tr>
                    <tr><td>6 months - 1 year</td><td>6.50%</td><td>7.00%</td></tr>
                    <tr><td>1 year - 2 years</td><td>7.00%</td><td>7.50%</td></tr>
                    <tr><td>2 years - 3 years</td><td>7.25%</td><td>7.75%</td></tr>
                    <tr><td>3 years - 5 years</td><td>7.50%</td><td>8.00%</td></tr>
                </tbody>
            </table>
        </div>
    </section>

    <section class="section-padding text-center bg-light">
        <div class="container">
            <h2 class="mb-md">Ready to Grow Your Wealth?</h2>
            <a href="apply-fd.html" class="btn btn-primary" style="font-size: 1.2rem; padding: 15px 40px;">Apply Now</a>
        </div>
    </section>
</main>
""" + FOOTER + "\n<script src=\"js/theme.js\"></script>\n</body></html>"

write_file('fixed-deposit.html', fd_info)

apply_fd = HEAD.format(title="Apply Fixed Deposit") + NAVBAR + """
<main class="section-padding bg-light">
    <div class="container container-narrow">
        <div id="auth-bar" style="background:var(--bg-main); padding:15px; border-radius:8px; margin-bottom:20px; font-weight:bold; color:var(--text-main); border:1px solid var(--border-color); display:flex; justify-content:space-between; flex-wrap:wrap;">
            <span>Account: <span id="bar_acc" style="color:var(--primary);"></span></span>
            <span>Holder: <span id="bar_name"></span></span>
            <span>Balance: <span id="bar_bal" style="color:var(--accent);"></span></span>
        </div>

        <div class="card" id="application-form-card">
            <h2 class="text-center mb-md">Open Fixed Deposit</h2>
            
            <div class="step-bar mb-xl">
                <div class="step-item active" id="step-btn-1">1. FD Configuration</div>
                <div class="step-item" id="step-btn-2">2. Review & Confirm</div>
            </div>

            <form id="fdForm">
                <!-- STEP 1 -->
                <div class="form-step active" id="step1">
                    <div class="form-group">
                        <label>FD Amount (₹)</label>
                        <input type="number" id="fd_amount" min="1000" required oninput="calcPreview()">
                        <small id="bal-error" style="color:red;display:none;">Insufficient balance.</small>
                    </div>

                    <div class="form-group" style="display:flex; align-items:center; gap:10px;">
                        <label style="margin:0;">Are you a Senior Citizen?</label>
                        <select id="fd_senior" onchange="calcPreview()" style="width:100px;">
                            <option value="No">No</option>
                            <option value="Yes">Yes</option>
                        </select>
                    </div>

                    <div class="form-group mt-lg">
                        <label>FD Tenure</label>
                        <div class="radio-card-grid mt-sm">
                            <label class="radio-card-label"><input type="radio" name="fd_tenure" value="6" onchange="calcPreview()" checked><div class="radio-card-content"><h4 style="color:var(--primary);">6 Months</h4><p class="text-muted" style="font-size:0.8rem;">6.50% / 7.00%</p></div></label>
                            <label class="radio-card-label"><input type="radio" name="fd_tenure" value="12" onchange="calcPreview()"><div class="radio-card-content"><h4 style="color:var(--primary);">1 Year</h4><p class="text-muted" style="font-size:0.8rem;">7.00% / 7.50%</p></div></label>
                            <label class="radio-card-label"><input type="radio" name="fd_tenure" value="24" onchange="calcPreview()"><div class="radio-card-content"><h4 style="color:var(--primary);">2 Years</h4><p class="text-muted" style="font-size:0.8rem;">7.25% / 7.75%</p></div></label>
                            <label class="radio-card-label"><input type="radio" name="fd_tenure" value="36" onchange="calcPreview()"><div class="radio-card-content"><h4 style="color:var(--primary);">3 Years</h4><p class="text-muted" style="font-size:0.8rem;">7.50% / 8.00%</p></div></label>
                            <label class="radio-card-label"><input type="radio" name="fd_tenure" value="60" onchange="calcPreview()"><div class="radio-card-content"><h4 style="color:var(--primary);">5 Years</h4><p class="text-muted" style="font-size:0.8rem;">7.50% / 8.00%</p></div></label>
                        </div>
                    </div>

                    <div class="form-group">
                        <label>Interest Payout Mode</label>
                        <div style="display:flex;gap:15px;margin-top:10px;">
                            <label><input type="radio" name="fd_payout" value="maturity" onchange="calcPreview()" checked> At Maturity (Reinvested)</label>
                            <label><input type="radio" name="fd_payout" value="monthly" onchange="calcPreview()"> Monthly Payout</label>
                        </div>
                    </div>

                    <div class="calc-box">
                        <h3 class="mb-sm text-center">FD Calculation Preview</h3>
                        <div class="calc-row"><span>Principal Amount:</span> <strong id="calc_prin">₹0</strong></div>
                        <div class="calc-row"><span>Interest Rate:</span> <strong id="calc_rate">0.00% p.a</strong></div>
                        <div class="calc-row"><span>Interest Earned:</span> <strong id="calc_int" style="color:green;">₹0</strong></div>
                        <hr style="border-color:var(--accent);">
                        <div class="calc-row" style="font-size:1.2rem; margin-top:10px;"><span>Maturity Amount:</span> <strong id="calc_mat" style="color:var(--accent);">₹0</strong></div>
                        <div class="calc-row" style="margin-top:5px;"><span>Maturity Date:</span> <strong id="calc_date"></strong></div>
                    </div>

                    <div class="text-right mt-lg"><button type="button" class="btn btn-primary next-btn" onclick="nextStep(2)">Review FD &rarr;</button></div>
                </div>

                <!-- STEP 2 -->
                <div class="form-step" id="step2" style="display:none;">
                    <div class="calc-box" style="border-color:var(--primary);">
                        <h3 class="mb-sm">Review & Confirm</h3>
                        <div class="calc-row"><span>Debiting Account:</span> <strong id="rev_acc"></strong></div>
                        <div class="calc-row"><span>FD Amount:</span> <strong id="rev_amt" style="color:red;"></strong></div>
                        <div class="calc-row"><span>Tenure:</span> <strong id="rev_tenure"></strong></div>
                        <div class="calc-row"><span>Rate:</span> <strong id="rev_rate"></strong></div>
                        <div class="calc-row"><span>Payout Mode:</span> <strong id="rev_payout"></strong></div>
                        <div class="calc-row"><span>Maturity Amount:</span> <strong id="rev_mat" style="color:var(--accent);"></strong></div>
                    </div>
                    
                    <div style="background:#FFFBEB; border:1px solid #FCD34D; color:#92400E; padding:15px; border-radius:8px; margin-top:20px; font-size:0.95rem;">
                        <strong id="deduct_notice"></strong>
                    </div>

                    <div class="form-group mt-md">
                        <label style="font-weight:normal; display:flex; gap:10px;">
                            <input type="checkbox" id="fd_agree" required>
                            <span>I confirm the FD details and authorize the bank to debit my savings account.</span>
                        </label>
                    </div>
                    <div class="text-between mt-lg">
                        <button type="button" class="btn btn-outline" onclick="prevStep(1)">&larr; Back</button>
                        <button type="submit" class="btn btn-accent" id="submitBtn">Create Fixed Deposit</button>
                    </div>
                </div>
            </form>
        </div>
    </div>
</main>
<script>
requireLogin('Fixed Deposit', 'apply-fd.html');
const user = getUser();
if(user) {
    document.getElementById('bar_acc').textContent = user.accountNumber;
    document.getElementById('bar_name').textContent = user.name;
    document.getElementById('bar_bal').textContent = '₹' + Number(user.balance).toLocaleString();
    document.getElementById('rev_acc').textContent = user.accountNumber;
}

let currentCalculation = {};

function calcPreview() {
    const amount = Number(document.getElementById('fd_amount').value);
    const err = document.getElementById('bal-error');
    if(user && amount > Number(user.balance)) {
        err.style.display = 'block';
        err.textContent = `Insufficient balance. Your balance is ₹${user.balance}`;
    } else { err.style.display = 'none'; }

    const months = Number(document.querySelector('input[name="fd_tenure"]:checked').value);
    const isSenior = document.getElementById('fd_senior').value === 'Yes';
    const payout = document.querySelector('input[name="fd_payout"]:checked').value;
    
    let rate = 0;
    if(months <= 6) rate = isSenior ? 7.00 : 6.50;
    else if(months <= 12) rate = isSenior ? 7.50 : 7.00;
    else if(months <= 24) rate = isSenior ? 7.75 : 7.25;
    else rate = isSenior ? 8.00 : 7.50;

    const r = rate / 100;
    const years = months / 12;
    let maturity, interest;
    
    if (payout === 'maturity') {
        maturity = amount * Math.pow(1 + r/4, 4 * years); // quarterly compound
    } else {
        maturity = amount + (amount * r * years); // simple
    }
    interest = maturity - amount;
    
    const matDate = new Date();
    matDate.setMonth(matDate.getMonth() + months);
    
    currentCalculation = {
        amount, rate, months, payout,
        maturity: maturity.toFixed(2), 
        interest: interest.toFixed(2), 
        maturityDate: matDate.toLocaleDateString('en-IN')
    };

    document.getElementById('calc_prin').textContent = '₹' + amount.toLocaleString();
    document.getElementById('calc_rate').textContent = rate.toFixed(2) + '% p.a';
    document.getElementById('calc_int').textContent = '₹' + Number(currentCalculation.interest).toLocaleString();
    document.getElementById('calc_mat').textContent = '₹' + Number(currentCalculation.maturity).toLocaleString();
    document.getElementById('calc_date').textContent = currentCalculation.maturityDate;
}

function nextStep(step) {
    if(step === 2) {
        if(!document.getElementById('fd_amount').value) return alert('Enter amount');
        if(user && Number(document.getElementById('fd_amount').value) > Number(user.balance)) return;
        
        document.getElementById('rev_amt').textContent = '₹' + currentCalculation.amount.toLocaleString();
        document.getElementById('rev_tenure').textContent = currentCalculation.months + ' Months';
        document.getElementById('rev_rate').textContent = currentCalculation.rate.toFixed(2) + '% p.a';
        document.getElementById('rev_payout').textContent = currentCalculation.payout === 'maturity' ? 'At Maturity' : 'Monthly';
        document.getElementById('rev_mat').textContent = '₹' + Number(currentCalculation.maturity).toLocaleString();
        document.getElementById('deduct_notice').textContent = `₹${currentCalculation.amount.toLocaleString()} will be debited from your savings account ${user.accountNumber}`;
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

document.getElementById('fdForm').addEventListener('submit', (e) => {
    e.preventDefault();
    if(!document.getElementById('fd_agree').checked) return alert('Please agree');
    
    document.getElementById('submitBtn').disabled = true;
    document.getElementById('submitBtn').textContent = 'Processing...';
    
    // Deduct balance
    user.balance = Number(user.balance) - currentCalculation.amount;
    localStorage.setItem('bams_user', JSON.stringify(user));

    const fdRef = generateRef('FD');
    saveApplication('fd', {
        fdRef,
        accNo: user.accountNumber,
        amount: currentCalculation.amount,
        tenure: currentCalculation.months,
        rate: currentCalculation.rate,
        maturityDate: currentCalculation.maturityDate,
        maturityAmount: currentCalculation.maturity,
        payout: currentCalculation.payout,
        status: 'Active'
    });
    
    setTimeout(() => {
        window.location.href = `fd-success.html?ref=${fdRef}`;
    }, 1500);
});
calcPreview();
</script>
""" + FOOTER + "\n<script src=\"js/theme.js\"></script>\n</body></html>"

write_file('apply-fd.html', apply_fd)

fd_success = HEAD.format(title="FD Created") + NAVBAR + """
<main class="section-padding bg-light">
    <div class="success-container card">
        <div class="success-icon" style="color:var(--accent);">🏦</div>
        <h1 class="mb-sm" style="color:var(--text-main);">Fixed Deposit Created!</h1>
        <div class="ref-box" style="display:inline-block; margin: 20px auto;">
            <p style="font-size:0.9rem; color:var(--text-muted); font-family:Inter,sans-serif; margin-bottom:5px;">FD Reference Number</p>
            <div id="succ_ref"></div>
        </div>

        <div style="background:#E8F4FD; border:1px solid #3B82F6; color:#1E3A8A; padding:15px; border-radius:8px; margin-bottom:30px; font-size:0.95rem;">
            Amount has been successfully debited from your savings account.
        </div>

        <div style="display:flex; gap:15px; justify-content:center; margin-top:40px;">
            <a href="dashboard.html" class="btn btn-primary">View in Dashboard</a>
            <a href="services.html" class="btn btn-outline">Back to Services</a>
        </div>
    </div>
</main>
<script>
    const params = new URLSearchParams(window.location.search);
    document.getElementById('succ_ref').textContent = params.get('ref') || 'FD202600000';
</script>
""" + FOOTER + "\n<script src=\"js/theme.js\"></script>\n</body></html>"

write_file('fd-success.html', fd_success)
print("FD flow generated.")
