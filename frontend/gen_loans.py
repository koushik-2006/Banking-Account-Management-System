from gen_savings import HEAD, NAVBAR, FOOTER, write_file

# ================= PERSONAL LOAN =================
pl_info = HEAD.format(title="Personal Loan") + NAVBAR + """
<main>
    <section class="service-hero" style="background:#5B21B6;color:#fff;">
        <div class="container">
            <div class="breadcrumb" style="color:#C4B5FD;"><a href="index.html" style="color:#C9A84C;">Home</a> &rarr; <a href="services.html" style="color:#C9A84C;">Services</a> &rarr; Personal Loan</div>
            <h1 style="color:#C9A84C;">Personal Loan</h1>
            <p class="tagline" style="color:#DDD6FE;">Get funds up to ₹25 Lakhs in 48 hours</p>
        </div>
    </section>
    
    <section class="section-padding bg-light">
        <div class="container" style="max-width: 800px;">
            <h2 class="text-center mb-lg">Loan Slabs & Rates</h2>
            <table class="rates-table mb-xl">
                <thead><tr><th>Loan Amount</th><th>Tenure</th><th>Rate (p.a.)</th><th>Processing Fee</th></tr></thead>
                <tbody>
                    <tr><td>₹50K - ₹2L</td><td>12-24 mo</td><td>10.5%</td><td>1.0%</td></tr>
                    <tr><td>₹2L - ₹5L</td><td>12-36 mo</td><td>11.0%</td><td>1.0%</td></tr>
                    <tr><td>₹5L - ₹10L</td><td>12-48 mo</td><td>11.5%</td><td>1.5%</td></tr>
                    <tr><td>₹10L - ₹25L</td><td>12-60 mo</td><td>12.0%</td><td>2.0%</td></tr>
                </tbody>
            </table>
            <div class="card bg-light">
                <h3 class="mb-sm">Eligibility</h3>
                <ul style="line-height:2;color:var(--text-muted);font-size:1.05rem;">
                    <li>Age 21-60 years</li>
                    <li>Salaried or Self-employed individuals</li>
                    <li>Minimum monthly income of ₹20,000</li>
                    <li>CIBIL score of 650 or above</li>
                </ul>
            </div>
            <div class="features-grid mt-xl">
                <div class="feature-card text-center"><h3>Instant Approval</h3></div>
                <div class="feature-card text-center"><h3>No Collateral</h3></div>
                <div class="feature-card text-center"><h3>Flexible Tenure</h3></div>
                <div class="feature-card text-center"><h3>Part Prepayment</h3></div>
            </div>
        </div>
    </section>

    <section class="section-padding text-center">
        <div class="container">
            <h2 class="mb-md">Achieve your personal goals today</h2>
            <a href="apply-personal-loan.html" class="btn btn-primary" style="font-size: 1.2rem; padding: 15px 40px;">Apply Now</a>
        </div>
    </section>
</main>
""" + FOOTER + "\n<script src=\"js/theme.js\"></script>\n</body></html>"

write_file('personal-loan.html', pl_info)

apply_pl = HEAD.format(title="Apply Personal Loan") + NAVBAR + """
<main class="section-padding bg-light">
    <div class="container container-narrow">
        <div id="auth-bar" style="background:var(--bg-main); padding:15px; border-radius:8px; margin-bottom:20px; font-weight:bold; color:var(--text-main); border:1px solid var(--border-color); display:flex; justify-content:space-between; flex-wrap:wrap;">
            <span>Account: <span id="bar_acc" style="color:var(--primary);"></span></span>
            <span>Holder: <span id="bar_name"></span></span>
        </div>

        <div class="card" id="application-form-card">
            <h2 class="text-center mb-md">Apply for Personal Loan</h2>
            
            <div class="step-bar mb-xl">
                <div class="step-item active" id="step-btn-1">1. Loan Details</div>
                <div class="step-item" id="step-btn-2">2. Employment</div>
                <div class="step-item" id="step-btn-3">3. Documents</div>
                <div class="step-item" id="step-btn-4">4. Review</div>
            </div>

            <form id="plForm">
                <!-- STEP 1 -->
                <div class="form-step active" id="step1">
                    <div class="form-group text-center">
                        <label>Loan Amount Required</label>
                        <h2 id="slider_val" style="color:var(--primary);margin:10px 0;">₹5,00,000</h2>
                        <input type="range" id="pl_amt" min="50000" max="2500000" step="10000" value="500000" style="width:100%;" oninput="calcEMI()">
                    </div>
                    
                    <div class="form-group">
                        <label>Purpose of Loan</label>
                        <select id="pl_purpose">
                            <option value="Medical Emergency">Medical Emergency</option>
                            <option value="Home Renovation">Home Renovation</option>
                            <option value="Education">Education</option>
                            <option value="Travel">Travel</option>
                            <option value="Wedding">Wedding</option>
                            <option value="Debt Consolidation">Debt Consolidation</option>
                            <option value="Business">Business</option>
                            <option value="Other">Other</option>
                        </select>
                    </div>

                    <div class="form-group mt-lg">
                        <label>Loan Tenure</label>
                        <div class="radio-card-grid mt-sm">
                            <label class="radio-card-label"><input type="radio" name="pl_tenure" value="12" onchange="calcEMI()"><div class="radio-card-content"><h4>1 Year</h4></div></label>
                            <label class="radio-card-label"><input type="radio" name="pl_tenure" value="24" onchange="calcEMI()"><div class="radio-card-content"><h4>2 Years</h4></div></label>
                            <label class="radio-card-label"><input type="radio" name="pl_tenure" value="36" onchange="calcEMI()" checked><div class="radio-card-content"><h4>3 Years</h4></div></label>
                            <label class="radio-card-label"><input type="radio" name="pl_tenure" value="48" onchange="calcEMI()"><div class="radio-card-content"><h4>4 Years</h4></div></label>
                            <label class="radio-card-label"><input type="radio" name="pl_tenure" value="60" onchange="calcEMI()"><div class="radio-card-content"><h4>5 Years</h4></div></label>
                        </div>
                    </div>

                    <div class="calc-box">
                        <h3 class="mb-sm text-center">Live EMI Calculator</h3>
                        <div class="calc-row"><span>Interest Rate:</span> <strong id="calc_rate"></strong></div>
                        <div class="calc-row"><span>Monthly EMI:</span> <strong id="calc_emi" style="color:var(--accent);font-size:1.5rem;"></strong></div>
                        <hr style="border-color:var(--accent);">
                        <div class="calc-row"><span>Total Interest:</span> <strong id="calc_int"></strong></div>
                        <div class="calc-row"><span>Processing Fee:</span> <strong id="calc_fee"></strong></div>
                        <div class="calc-row"><span>Total Repayment:</span> <strong id="calc_tot"></strong></div>
                    </div>
                    <div class="text-right mt-lg"><button type="button" class="btn btn-primary next-btn" onclick="nextStep(2)">Next &rarr;</button></div>
                </div>

                <!-- STEP 2 -->
                <div class="form-step" id="step2" style="display:none;">
                    <div class="form-group">
                        <label>Employment Type</label>
                        <div style="display:flex;gap:15px;margin-top:10px;">
                            <label><input type="radio" name="pl_emp" value="Salaried" checked> Salaried</label>
                            <label><input type="radio" name="pl_emp" value="Self-Employed"> Self-Employed</label>
                            <label><input type="radio" name="pl_emp" value="Business Owner"> Business Owner</label>
                        </div>
                    </div>
                    <div class="form-group"><label>Company / Business Name</label><input type="text" id="pl_comp" required></div>
                    <div class="form-group"><label>Designation</label><input type="text" id="pl_desig"></div>
                    <div class="form-grid">
                        <div class="form-group">
                            <label>Monthly Income (₹)</label>
                            <input type="number" id="pl_inc" required>
                            <small id="inc-warn" style="color:red;display:none;">Minimum income required is ₹20,000/month</small>
                        </div>
                        <div class="form-group"><label>Years at Current Job</label><input type="number" id="pl_yrs" min="1" required></div>
                    </div>
                    <div class="text-between mt-lg">
                        <button type="button" class="btn btn-outline" onclick="prevStep(1)">&larr; Back</button>
                        <button type="button" class="btn btn-primary next-btn" onclick="nextStep(3)">Next &rarr;</button>
                    </div>
                </div>

                <!-- STEP 3 -->
                <div class="form-step" id="step3" style="display:none;">
                    <p class="text-muted text-center mb-md">Documents are stored locally for demo. In production, these are securely uploaded.</p>
                    <div id="doc-list" style="display:flex;flex-direction:column;gap:15px;">
                        <!-- JS populated -->
                    </div>
                    <p class="text-center mt-md"><strong id="doc-count">0 of 5 documents uploaded</strong></p>
                    <div class="text-between mt-lg">
                        <button type="button" class="btn btn-outline" onclick="prevStep(2)">&larr; Back</button>
                        <button type="button" class="btn btn-primary next-btn" onclick="nextStep(4)">Review &rarr;</button>
                    </div>
                </div>

                <!-- STEP 4 -->
                <div class="form-step" id="step4" style="display:none;">
                    <div class="calc-box">
                        <h3 class="mb-sm">Loan Summary</h3>
                        <div class="calc-row"><span>Amount:</span> <strong id="rev_amt" style="color:var(--accent);"></strong></div>
                        <div class="calc-row"><span>EMI:</span> <strong id="rev_emi"></strong></div>
                        <div class="calc-row"><span>Tenure:</span> <strong id="rev_ten"></strong></div>
                        <div class="calc-row"><span>Rate:</span> <strong id="rev_rate"></strong></div>
                        <div class="calc-row"><span>Income:</span> <strong id="rev_inc"></strong></div>
                    </div>
                    <h3 class="mt-lg mb-sm">EMI Schedule (First 3 Months)</h3>
                    <table class="rates-table" style="font-size:0.85rem;" id="amort_table">
                        <thead><tr><th>Month</th><th>EMI</th><th>Principal</th><th>Interest</th><th>Balance</th></tr></thead>
                        <tbody></tbody>
                    </table>

                    <div class="form-group mt-md">
                        <label style="font-weight:normal; display:flex; gap:10px;">
                            <input type="checkbox" id="pl_agree" required>
                            <span>I declare all information is correct and authorize CIBIL check.</span>
                        </label>
                    </div>
                    <div class="text-between mt-lg">
                        <button type="button" class="btn btn-outline" onclick="prevStep(3)">&larr; Back</button>
                        <button type="submit" class="btn btn-accent" id="submitBtn">Apply for Loan</button>
                    </div>
                </div>
            </form>
        </div>
    </div>
</main>
<script>
requireLogin('Personal Loan', 'apply-personal-loan.html');
const user = getUser();
if(user) {
    document.getElementById('bar_acc').textContent = user.accountNumber;
    document.getElementById('bar_name').textContent = user.name;
}

const docs = ["Latest Salary Slip", "3 Months Bank Statement", "Aadhaar Card (Front/Back)", "PAN Card", "Passport Photo"];
const docList = document.getElementById('doc-list');
docs.forEach((doc, idx) => {
    docList.innerHTML += `
        <div style="padding:15px; border:1px solid var(--border-color); border-radius:8px; display:flex; justify-content:space-between; align-items:center; background:#fff;">
            <div>
                <strong>${doc}</strong>
                <div id="stat_${idx}" style="font-size:0.8rem;color:var(--text-muted);margin-top:5px;">Not uploaded</div>
            </div>
            <input type="file" onchange="updDoc(${idx}, this)" style="max-width:200px;">
        </div>
    `;
});
let upCount = 0;
function updDoc(idx, input) {
    if(input.files.length > 0) {
        document.getElementById(`stat_${idx}`).innerHTML = `<span style="color:green;">✓ Uploaded</span> (${input.files[0].name})`;
        upCount++;
    } else {
        document.getElementById(`stat_${idx}`).textContent = 'Not uploaded';
        upCount--;
    }
    document.getElementById('doc-count').textContent = `${upCount} of 5 documents uploaded`;
}

let c = {};
function calcEMI() {
    const p = Number(document.getElementById('pl_amt').value);
    document.getElementById('slider_val').textContent = '₹' + p.toLocaleString('en-IN');
    const m = Number(document.querySelector('input[name="pl_tenure"]:checked').value);
    
    let rate = 12.0, feeP = 2.0;
    if(p <= 200000) { rate = 10.5; feeP = 1.0; }
    else if(p <= 500000) { rate = 11.0; feeP = 1.0; }
    else if(p <= 1000000) { rate = 11.5; feeP = 1.5; }
    
    const r = rate / 12 / 100;
    const emi = p * r * Math.pow(1+r, m) / (Math.pow(1+r, m) - 1);
    const total = emi * m;
    const interest = total - p;
    const fee = p * (feeP/100);
    
    c = { p, m, rate, emi, total, interest, fee };
    document.getElementById('calc_rate').textContent = rate + '% p.a';
    document.getElementById('calc_emi').textContent = '₹' + Math.round(emi).toLocaleString('en-IN');
    document.getElementById('calc_int').textContent = '₹' + Math.round(interest).toLocaleString('en-IN');
    document.getElementById('calc_fee').textContent = '₹' + Math.round(fee).toLocaleString('en-IN') + ` (${feeP}%)`;
    document.getElementById('calc_tot').textContent = '₹' + Math.round(total).toLocaleString('en-IN');
}

function nextStep(step) {
    if(step === 3) {
        const inc = document.getElementById('pl_inc').value;
        if(!inc) return alert('Enter income');
        if(inc < 20000) { document.getElementById('inc-warn').style.display='block'; return; }
        document.getElementById('inc-warn').style.display='none';
    }
    if(step === 4) {
        document.getElementById('rev_amt').textContent = '₹' + c.p.toLocaleString('en-IN');
        document.getElementById('rev_emi').textContent = '₹' + Math.round(c.emi).toLocaleString('en-IN');
        document.getElementById('rev_ten').textContent = c.m + ' Months';
        document.getElementById('rev_rate').textContent = c.rate + '%';
        document.getElementById('rev_inc').textContent = '₹' + Number(document.getElementById('pl_inc').value).toLocaleString();
        
        const tb = document.querySelector('#amort_table tbody');
        tb.innerHTML = '';
        let bal = c.p;
        const r = c.rate/12/100;
        for(let i=1; i<=3; i++) {
            let intP = bal * r;
            let prinP = c.emi - intP;
            bal -= prinP;
            tb.innerHTML += `<tr><td>${i}</td><td>₹${Math.round(c.emi).toLocaleString()}</td><td>₹${Math.round(prinP).toLocaleString()}</td><td>₹${Math.round(intP).toLocaleString()}</td><td>₹${Math.round(bal).toLocaleString()}</td></tr>`;
        }
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

document.getElementById('plForm').addEventListener('submit', (e) => {
    e.preventDefault();
    if(!document.getElementById('pl_agree').checked) return alert('Please agree');
    
    const btn = document.getElementById('submitBtn');
    btn.disabled = true;
    btn.textContent = 'Processing...';
    
    const loanRef = generateRef('LN');
    saveApplication('loan', {
        loanRef,
        accNo: user.accountNumber,
        amount: c.p,
        emi: Math.round(c.emi),
        tenure: c.m,
        rate: c.rate,
        status: 'Applied'
    });
    
    setTimeout(() => {
        window.location.href = `loan-success.html?ref=${loanRef}`;
    }, 1500);
});
calcEMI();
</script>
""" + FOOTER + "\n<script src=\"js/theme.js\"></script>\n</body></html>"

write_file('apply-personal-loan.html', apply_pl)

pl_success = HEAD.format(title="Loan Submitted") + NAVBAR + """
<main class="section-padding bg-light">
    <div class="success-container card">
        <div class="success-icon" style="color:var(--accent);">📄</div>
        <h1 class="mb-sm" style="color:var(--text-main);">Application Submitted!</h1>
        <div class="ref-box" style="display:inline-block; margin: 20px auto;">
            <p style="font-size:0.9rem; color:var(--text-muted); font-family:Inter,sans-serif; margin-bottom:5px;">Loan Reference Number</p>
            <div id="succ_ref"></div>
        </div>

        <div class="status-stepper text-left mt-lg" style="flex-wrap:wrap;">
            <div style="color:var(--accent);font-weight:bold;flex:1;">1. Applied<br>✓</div>
            <div style="flex:1;">2. Under Review</div>
            <div style="flex:1;">3. Verification</div>
            <div style="flex:1;">4. Approved</div>
        </div>

        <p class="text-muted mt-xl">Our loan officer will contact you within 24-48 hours.</p>

        <div style="display:flex; gap:15px; justify-content:center; margin-top:30px;">
            <button class="btn btn-primary" onclick="alert('Status tracker coming soon.')">Track Application</button>
            <a href="dashboard.html" class="btn btn-outline">Go to Dashboard</a>
        </div>
    </div>
</main>
<script>
    const params = new URLSearchParams(window.location.search);
    document.getElementById('succ_ref').textContent = params.get('ref') || 'LN202600000';
</script>
""" + FOOTER + "\n<script src=\"js/theme.js\"></script>\n</body></html>"

write_file('loan-success.html', pl_success)

# ================= HOME LOAN =================
hl_info = HEAD.format(title="Home Loan") + NAVBAR + """
<main>
    <section class="service-hero" style="background:#064E3B;color:#fff;">
        <div class="container">
            <div class="breadcrumb" style="color:#A7F3D0;"><a href="index.html" style="color:#C9A84C;">Home</a> &rarr; <a href="services.html" style="color:#C9A84C;">Services</a> &rarr; Home Loan</div>
            <h1 style="color:#C9A84C;">Home Loan</h1>
            <p class="tagline" style="color:#D1FAE5;">Finance your dream home with rates starting at 8.5%</p>
        </div>
    </section>
    
    <section class="section-padding bg-light">
        <div class="container">
            <div class="features-grid">
                <div class="feature-card text-center"><h3>Up to ₹5 Crore</h3></div>
                <div class="feature-card text-center"><h3>30-Year Tenure</h3></div>
                <div class="feature-card text-center"><h3>Tax Benefits</h3></div>
                <div class="feature-card text-center"><h3>Balance Transfer</h3></div>
            </div>
            
            <table class="rates-table mb-xl mt-xl">
                <thead><tr><th>Category</th><th>Interest Rate (p.a.)</th></tr></thead>
                <tbody>
                    <tr><td>Salaried</td><td>8.50% - 9.25%</td></tr>
                    <tr><td>Self-employed</td><td>8.75% - 9.50%</td></tr>
                    <tr><td>Pre-approved</td><td>8.40%</td></tr>
                </tbody>
            </table>
            
            <div class="card bg-light text-center">
                <h3 style="color:var(--primary);">Tax Benefits</h3>
                <p class="text-muted mt-sm">Deduction up to ₹2 Lakhs on interest (Sec 24) + ₹1.5 Lakhs on principal (Sec 80C).</p>
            </div>
        </div>
    </section>

    <section class="section-padding text-center">
        <a href="apply-home-loan.html" class="btn btn-primary" style="font-size: 1.2rem; padding: 15px 40px;">Apply Now</a>
    </section>
</main>
""" + FOOTER + "\n<script src=\"js/theme.js\"></script>\n</body></html>"

write_file('home-loan.html', hl_info)

apply_hl = HEAD.format(title="Apply Home Loan") + NAVBAR + """
<main class="section-padding bg-light">
    <div class="container container-narrow">
        <div class="card" id="application-form-card">
            <h2 class="text-center mb-md">Apply for Home Loan</h2>
            
            <div class="step-bar mb-xl">
                <div class="step-item active" id="step-btn-1">1. Property</div>
                <div class="step-item" id="step-btn-2">2. Co-applicant</div>
                <div class="step-item" id="step-btn-3">3. Income</div>
                <div class="step-item" id="step-btn-4">4. Review</div>
            </div>

            <form id="hlForm">
                <!-- STEP 1 -->
                <div class="form-step active" id="step1">
                    <div class="form-group">
                        <label>Property Type</label>
                        <div class="radio-card-grid mt-sm">
                            <label class="radio-card-label"><input type="radio" name="hl_type" value="Apartment" checked><div class="radio-card-content">🏢 Apartment</div></label>
                            <label class="radio-card-label"><input type="radio" name="hl_type" value="House"><div class="radio-card-content">🏠 Independent House</div></label>
                            <label class="radio-card-label"><input type="radio" name="hl_type" value="Plot"><div class="radio-card-content">📦 Plot</div></label>
                        </div>
                    </div>
                    
                    <div class="form-grid">
                        <div class="form-group"><label>Property Value (₹)</label><input type="number" id="hl_val" value="5000000" oninput="calcHL()"></div>
                        <div class="form-group"><label>Down Payment (₹)</label><input type="number" id="hl_down" value="1000000" oninput="calcHL()"></div>
                    </div>
                    <div class="form-group">
                        <label>Loan Tenure</label>
                        <select id="hl_tenure" onchange="calcHL()">
                            <option value="5">5 Years</option><option value="10">10 Years</option><option value="15">15 Years</option><option value="20" selected>20 Years</option><option value="25">25 Years</option><option value="30">30 Years</option>
                        </select>
                    </div>

                    <div class="calc-box">
                        <div class="calc-row"><span>Required Loan:</span> <strong id="calc_req"></strong></div>
                        <div class="calc-row"><span>Rate:</span> <strong id="calc_rate">8.50%</strong></div>
                        <div class="calc-row"><span>Monthly EMI:</span> <strong id="calc_emi" style="color:var(--accent);font-size:1.5rem;"></strong></div>
                        <hr>
                        <div class="calc-row"><span>LTV Ratio:</span> <strong id="calc_ltv"></strong></div>
                        <small id="ltv-warn" style="color:red;display:none;">LTV exceeds 80%. Consider increasing down payment.</small>
                    </div>
                    <div class="text-right mt-lg"><button type="button" class="btn btn-primary next-btn" onclick="nextStep(2)">Next &rarr;</button></div>
                </div>

                <!-- STEP 2 -->
                <div class="form-step" id="step2" style="display:none;">
                    <div class="form-group">
                        <label>Do you have a co-applicant?</label>
                        <select id="hl_co_req" onchange="document.getElementById('co_div').style.display = this.value==='Yes'?'block':'none'">
                            <option value="No">No</option><option value="Yes">Yes</option>
                        </select>
                    </div>
                    <div id="co_div" style="display:none;background:var(--bg-main);padding:15px;border-radius:8px;border:1px solid var(--border-color);">
                        <p class="text-muted text-center mb-md">Adding a co-applicant increases loan eligibility.</p>
                        <div class="form-group"><label>Co-applicant Name</label><input type="text"></div>
                        <div class="form-group"><label>Relation</label><input type="text"></div>
                        <div class="form-group"><label>Monthly Income</label><input type="number"></div>
                    </div>
                    <div class="text-between mt-lg">
                        <button type="button" class="btn btn-outline" onclick="prevStep(1)">&larr; Back</button>
                        <button type="button" class="btn btn-primary next-btn" onclick="nextStep(3)">Next &rarr;</button>
                    </div>
                </div>

                <!-- STEP 3 -->
                <div class="form-step" id="step3" style="display:none;">
                    <div class="form-group">
                        <label>Monthly Income (₹)</label>
                        <input type="number" id="hl_inc" required oninput="calcFOIR()">
                        <small id="inc-warn" style="color:red;display:none;">Minimum ₹30,000 required.</small>
                    </div>
                    <div class="form-group">
                        <label>Existing EMIs per month (₹)</label>
                        <input type="number" id="hl_ext" value="0" oninput="calcFOIR()">
                    </div>
                    <div class="calc-box" style="border-color:orange;">
                        <div class="calc-row"><span>FOIR (Obligations to Income):</span> <strong id="calc_foir">0%</strong></div>
                        <small id="foir-warn" style="color:red;display:none;">FOIR exceeds 65%. Loan approval may be difficult.</small>
                    </div>
                    <div class="text-between mt-lg">
                        <button type="button" class="btn btn-outline" onclick="prevStep(2)">&larr; Back</button>
                        <button type="button" class="btn btn-primary next-btn" onclick="nextStep(4)">Review &rarr;</button>
                    </div>
                </div>

                <!-- STEP 4 -->
                <div class="form-step" id="step4" style="display:none;">
                    <div class="calc-box">
                        <h3 class="mb-sm">Review Summary</h3>
                        <div class="calc-row"><span>Property Value:</span> <strong id="rev_val"></strong></div>
                        <div class="calc-row"><span>Loan Amount:</span> <strong id="rev_amt" style="color:var(--accent);"></strong></div>
                        <div class="calc-row"><span>Tenure:</span> <strong id="rev_ten"></strong></div>
                        <div class="calc-row"><span>EMI:</span> <strong id="rev_emi"></strong></div>
                    </div>
                    <div class="form-group mt-md"><label style="font-weight:normal; display:flex; gap:10px;"><input type="checkbox" id="hl_agree" required><span>I declare all information is correct.</span></label></div>
                    <div class="text-between mt-lg">
                        <button type="button" class="btn btn-outline" onclick="prevStep(3)">&larr; Back</button>
                        <button type="submit" class="btn btn-accent" id="submitBtn">Submit Application</button>
                    </div>
                </div>
            </form>
        </div>
    </div>
</main>
<script>
requireLogin('Home Loan', 'apply-home-loan.html');

let c = {};
function calcHL() {
    const val = Number(document.getElementById('hl_val').value) || 0;
    const down = Number(document.getElementById('hl_down').value) || 0;
    const p = val - down;
    const y = Number(document.getElementById('hl_tenure').value);
    const m = y * 12;
    const rate = 8.5;
    
    document.getElementById('calc_req').textContent = '₹' + p.toLocaleString('en-IN');
    
    if(p <= 0 || val <= 0) return;
    
    const r = rate / 12 / 100;
    const emi = p * r * Math.pow(1+r, m) / (Math.pow(1+r, m) - 1);
    const ltv = (p / val) * 100;
    
    c = { p, emi, ltv, y, val };
    
    document.getElementById('calc_emi').textContent = '₹' + Math.round(emi).toLocaleString('en-IN');
    document.getElementById('calc_ltv').textContent = ltv.toFixed(1) + '%';
    document.getElementById('ltv-warn').style.display = ltv > 80 ? 'block' : 'none';
    calcFOIR();
}

function calcFOIR() {
    const inc = Number(document.getElementById('hl_inc').value) || 1;
    const ext = Number(document.getElementById('hl_ext').value) || 0;
    const foir = ((ext + (c.emi || 0)) / inc) * 100;
    document.getElementById('calc_foir').textContent = foir.toFixed(1) + '%';
    document.getElementById('foir-warn').style.display = foir > 65 ? 'block' : 'none';
}

function nextStep(step) {
    if(step === 4) {
        document.getElementById('rev_val').textContent = '₹' + c.val.toLocaleString('en-IN');
        document.getElementById('rev_amt').textContent = '₹' + c.p.toLocaleString('en-IN');
        document.getElementById('rev_ten').textContent = c.y + ' Years';
        document.getElementById('rev_emi').textContent = '₹' + Math.round(c.emi).toLocaleString('en-IN');
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

document.getElementById('hlForm').addEventListener('submit', (e) => {
    e.preventDefault();
    if(!document.getElementById('hl_agree').checked) return alert('Please agree');
    document.getElementById('submitBtn').disabled = true;
    
    const hlRef = generateRef('HL');
    saveApplication('homeloan', {
        hlRef,
        amount: c.p,
        emi: Math.round(c.emi),
        tenure: c.y,
        status: 'Applied'
    });
    
    setTimeout(() => { window.location.href = `homeloan-success.html?ref=${hlRef}`; }, 1500);
});
calcHL();
</script>
""" + FOOTER + "\n<script src=\"js/theme.js\"></script>\n</body></html>"

write_file('apply-home-loan.html', apply_hl)

hl_success = HEAD.format(title="Home Loan Submitted") + NAVBAR + """
<main class="section-padding bg-light">
    <div class="success-container card">
        <div class="success-icon" style="color:var(--accent);">🏡</div>
        <h1 class="mb-sm" style="color:var(--text-main);">Application Received!</h1>
        <div class="ref-box" style="display:inline-block; margin: 20px auto;">
            <p style="font-size:0.9rem; color:var(--text-muted); font-family:Inter,sans-serif; margin-bottom:5px;">Home Loan Reference</p>
            <div id="succ_ref"></div>
        </div>
        <p class="text-muted mt-md mb-xl">Processing time: 7-10 working days.</p>
        <div style="display:flex; gap:15px; justify-content:center;">
            <a href="dashboard.html" class="btn btn-primary">Dashboard</a>
        </div>
    </div>
</main>
<script>
    document.getElementById('succ_ref').textContent = new URLSearchParams(window.location.search).get('ref') || 'HL202600000';
</script>
""" + FOOTER + "\n<script src=\"js/theme.js\"></script>\n</body></html>"

write_file('homeloan-success.html', hl_success)
print("Loans flow generated.")
