from gen_savings import HEAD, NAVBAR, FOOTER, write_file

current_info = HEAD.format(title="Current Account") + NAVBAR + """
<main>
    <section class="service-hero" style="background:#0A0A0A;color:#fff;">
        <div class="container">
            <div class="breadcrumb" style="color:#8B949E;"><a href="index.html" style="color:#C9A84C;">Home</a> &rarr; <a href="services.html" style="color:#C9A84C;">Services</a> &rarr; Current Account</div>
            <h1 style="color:#C9A84C;">Current Account</h1>
            <p class="tagline" style="color:#ccc;">Power your business with unlimited transactions</p>
        </div>
    </section>
    
    <section class="section-padding bg-light">
        <div class="container">
            <h2 class="text-center mb-xl">Business Features</h2>
            <div class="features-grid">
                <div class="feature-card text-center"><h3>Unlimited Transactions</h3><p class="text-muted">No cap on the number of monthly transactions.</p></div>
                <div class="feature-card text-center"><h3>Overdraft Facility</h3><p class="text-muted">Easy access to credit lines when you need working capital.</p></div>
                <div class="feature-card text-center"><h3>Business Net Banking</h3><p class="text-muted">Advanced corporate dashboard with role-based access.</p></div>
                <div class="feature-card text-center"><h3>Relationship Manager</h3><p class="text-muted">Dedicated RM for all your corporate banking needs.</p></div>
                <div class="feature-card text-center"><h3>GST Invoice Integration</h3><p class="text-muted">Automated GST billing and seamless accounting sync.</p></div>
                <div class="feature-card text-center"><h3>Bulk Payment Support</h3><p class="text-muted">Upload CSVs to process salaries and vendor payments instantly.</p></div>
            </div>
        </div>
    </section>

    <section class="section-padding">
        <div class="container" style="max-width: 900px;">
            <h2 class="text-center mb-lg">Account Variants</h2>
            <table class="rates-table mb-xl">
                <thead><tr><th>Feature</th><th>Basic</th><th>Business Pro</th><th>Corporate</th></tr></thead>
                <tbody>
                    <tr><td>Monthly Limit</td><td>Unlimited</td><td>Unlimited</td><td>Unlimited</td></tr>
                    <tr><td>Overdraft</td><td>Upto ₹5L</td><td>Upto ₹25L</td><td>Upto ₹1Cr</td></tr>
                    <tr><td>Min Balance</td><td>₹10,000</td><td>₹25,000</td><td>₹1,00,000</td></tr>
                    <tr><td>Annual Fee</td><td>₹500</td><td>₹1500</td><td>₹5000</td></tr>
                </tbody>
            </table>

            <h2 class="text-center mb-lg mt-xl">Eligibility</h2>
            <div class="card bg-light">
                <ul style="line-height:2;color:var(--text-muted);font-size:1.05rem;">
                    <li>Available for Sole Proprietorships, Partnerships, LLPs, Private and Public Limited Companies.</li>
                    <li>Valid business registration documents and PAN required.</li>
                    <li>Minimum age of authorized signatory must be 21 years.</li>
                </ul>
            </div>
        </div>
    </section>

    <section class="section-padding text-center bg-light">
        <div class="container">
            <h2 class="mb-md">Ready to Scale Your Business?</h2>
            <a href="apply-current.html" class="btn btn-primary" style="font-size: 1.2rem; padding: 15px 40px;">Apply Now</a>
        </div>
    </section>
</main>
""" + FOOTER + "\n<script src=\"js/theme.js\"></script>\n</body></html>"

write_file('current-account.html', current_info)

apply_current = HEAD.format(title="Apply Current Account") + NAVBAR + """
<main class="section-padding bg-light">
    <div class="container container-narrow">
        <div class="card" id="application-form-card">
            <h2 class="text-center mb-md">Open Current Account</h2>
            
            <div class="step-bar mb-xl">
                <div class="step-item active" id="step-btn-1">1. Business Info</div>
                <div class="step-item" id="step-btn-2">2. Authorized Person</div>
                <div class="step-item" id="step-btn-3">3. Account Type</div>
                <div class="step-item" id="step-btn-4">4. Review</div>
            </div>

            <form id="currentForm">
                <!-- STEP 1 -->
                <div class="form-step active" id="step1">
                    <div class="form-group"><label>Business Name</label><input type="text" id="ca_bizname" required></div>
                    <div class="form-grid">
                        <div class="form-group"><label>Business Type</label>
                            <select id="ca_biztype" required>
                                <option value="Sole Proprietorship">Sole Proprietorship</option>
                                <option value="Partnership">Partnership</option>
                                <option value="Private Limited">Private Limited</option>
                                <option value="LLP">LLP</option>
                                <option value="Public Limited">Public Limited</option>
                                <option value="Trust">Trust</option>
                                <option value="NGO">NGO</option>
                            </select>
                        </div>
                        <div class="form-group"><label>Date of Incorporation</label><input type="date" id="ca_incorp" required></div>
                    </div>
                    <div class="form-grid">
                        <div class="form-group">
                            <label>GST Number (Optional)</label>
                            <input type="text" id="ca_gst" placeholder="15-character format">
                            <small id="gst-error" style="color:red;display:none;">15-character GST format: 22AAAAA0000A1Z5</small>
                        </div>
                        <div class="form-group"><label>Business PAN Number</label><input type="text" id="ca_pan" required style="text-transform:uppercase;"></div>
                    </div>
                    <div class="form-group"><label>Registered Address</label><textarea id="ca_address" required></textarea></div>
                    <div class="form-grid">
                        <div class="form-group"><label>State</label><select id="ca_state" required><option value="Delhi">Delhi</option><option value="Maharashtra">Maharashtra</option></select></div>
                        <div class="form-group"><label>City</label><input type="text" id="ca_city" required></div>
                    </div>
                    <div class="form-grid">
                        <div class="form-group"><label>Business Phone</label><input type="tel" id="ca_phone" pattern="[0-9]{10}" required></div>
                        <div class="form-group"><label>Business Email</label><input type="email" id="ca_email" required></div>
                    </div>
                    <div class="form-group mt-sm">
                        <label>Annual Turnover Range</label>
                        <div style="display:flex;gap:15px;margin-top:10px;flex-wrap:wrap;">
                            <label><input type="radio" name="ca_turnover" value="Below ₹10L" checked> Below ₹10L</label>
                            <label><input type="radio" name="ca_turnover" value="₹10L–₹1Cr"> ₹10L–₹1Cr</label>
                            <label><input type="radio" name="ca_turnover" value="₹1Cr–₹10Cr"> ₹1Cr–₹10Cr</label>
                            <label><input type="radio" name="ca_turnover" value="Above ₹10Cr"> Above ₹10Cr</label>
                        </div>
                    </div>
                    <div class="text-right mt-lg"><button type="button" class="btn btn-primary next-btn" onclick="nextStep(2)">Next &rarr;</button></div>
                </div>

                <!-- STEP 2 -->
                <div class="form-step" id="step2" style="display:none;">
                    <div class="form-group"><label>Full Name of Authorized Person</label><input type="text" id="ca_auth_name" required></div>
                    <div class="form-grid">
                        <div class="form-group"><label>Designation</label>
                            <select id="ca_auth_desig">
                                <option value="Director">Director</option>
                                <option value="Partner">Partner</option>
                                <option value="Proprietor">Proprietor</option>
                                <option value="Trustee">Trustee</option>
                            </select>
                        </div>
                        <div class="form-group"><label>Personal PAN</label><input type="text" id="ca_auth_pan" required style="text-transform:uppercase;"></div>
                    </div>
                    <div class="form-group"><label>Personal Aadhaar</label><input type="number" id="ca_auth_aadhaar" required></div>
                    <div class="form-grid">
                        <div class="form-group"><label>Mobile Number</label><input type="tel" id="ca_auth_mobile" required></div>
                        <div class="form-group"><label>Email</label><input type="email" id="ca_auth_email" required></div>
                    </div>
                    <div class="form-group"><label>Signature Upload</label><input type="file" accept="image/*" required></div>
                    <div class="text-between mt-lg">
                        <button type="button" class="btn btn-outline" onclick="prevStep(1)">&larr; Back</button>
                        <button type="button" class="btn btn-primary next-btn" onclick="nextStep(3)">Next &rarr;</button>
                    </div>
                </div>

                <!-- STEP 3 -->
                <div class="form-step" id="step3" style="display:none;">
                    <div class="form-group">
                        <label>Account Variant</label>
                        <div class="radio-card-grid mt-sm">
                            <label class="radio-card-label">
                                <input type="radio" name="ca_variant" value="Basic" onchange="updateMin()" checked>
                                <div class="radio-card-content">
                                    <h4 style="color:var(--primary);">Basic</h4><p class="text-muted" style="font-size:0.8rem;">₹10,000 min</p>
                                </div>
                            </label>
                            <label class="radio-card-label">
                                <input type="radio" name="ca_variant" value="Business Pro" onchange="updateMin()">
                                <div class="radio-card-content">
                                    <h4 style="color:var(--primary);">Business Pro</h4><p class="text-muted" style="font-size:0.8rem;">₹25,000 min</p>
                                </div>
                            </label>
                            <label class="radio-card-label">
                                <input type="radio" name="ca_variant" value="Corporate" onchange="updateMin()">
                                <div class="radio-card-content">
                                    <h4 style="color:var(--primary);">Corporate</h4><p class="text-muted" style="font-size:0.8rem;">₹1,00,000 min</p>
                                </div>
                            </label>
                        </div>
                    </div>
                    <div class="form-group">
                        <label>Opening Deposit</label>
                        <input type="number" id="ca_deposit" min="10000" value="10000" required>
                        <small id="ca_min_hint" class="text-muted">Minimum requirement: ₹10,000</small>
                    </div>
                    <div class="form-group">
                        <label>Overdraft Required?</label>
                        <select id="ca_od_req" onchange="document.getElementById('od_amt_div').style.display = this.value==='Yes' ? 'block':'none'">
                            <option value="No">No</option>
                            <option value="Yes">Yes</option>
                        </select>
                    </div>
                    <div class="form-group" id="od_amt_div" style="display:none;">
                        <label>Overdraft Limit Required</label>
                        <select id="ca_od_limit">
                            <option value="₹1L">₹1L</option><option value="₹5L">₹5L</option><option value="₹10L">₹10L</option><option value="₹25L">₹25L</option><option value="₹1Cr">₹1Cr</option>
                        </select>
                    </div>
                    <div style="display:flex;flex-direction:column;gap:10px;margin-top:20px;">
                        <label><input type="checkbox" id="ca_chk" checked> Need Cheque Book?</label>
                        <label><input type="checkbox" id="ca_nb" checked> Need Net Banking Access?</label>
                        <label><input type="checkbox" id="ca_rm"> Need Relationship Manager?</label>
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
                        <div class="calc-row"><span>Business Name:</span> <strong id="rev_biz"></strong></div>
                        <div class="calc-row"><span>Type:</span> <strong id="rev_type"></strong></div>
                        <div class="calc-row"><span>GST:</span> <strong id="rev_gst"></strong></div>
                        <div class="calc-row"><span>Authorized Person:</span> <strong id="rev_auth"></strong></div>
                        <hr style="margin:10px 0;border-color:var(--border-color);">
                        <div class="calc-row"><span>Account Variant:</span> <strong id="rev_var"></strong></div>
                        <div class="calc-row"><span>Opening Deposit:</span> <strong id="rev_dep" style="color:var(--accent);"></strong></div>
                        <div class="calc-row"><span>Overdraft:</span> <strong id="rev_od"></strong></div>
                    </div>
                    <div class="form-group mt-md">
                        <label style="font-weight:normal; display:flex; gap:10px;">
                            <input type="checkbox" id="ca_agree" required>
                            <span>I certify that the business details are authentic and I am authorized to open this account.</span>
                        </label>
                    </div>
                    <div class="text-between mt-lg">
                        <button type="button" class="btn btn-outline" onclick="prevStep(3)">&larr; Back</button>
                        <button type="submit" class="btn btn-accent" id="submitBtn">Open Current Account</button>
                    </div>
                </div>
            </form>
        </div>
    </div>
</main>
<script>
function updateMin() {
    const val = document.querySelector('input[name="ca_variant"]:checked').value;
    const dep = document.getElementById('ca_deposit');
    const hint = document.getElementById('ca_min_hint');
    if(val === 'Basic') { dep.min = 10000; dep.value = 10000; hint.textContent = 'Minimum requirement: ₹10,000'; }
    if(val === 'Business Pro') { dep.min = 25000; dep.value = 25000; hint.textContent = 'Minimum requirement: ₹25,000'; }
    if(val === 'Corporate') { dep.min = 100000; dep.value = 100000; hint.textContent = 'Minimum requirement: ₹1,00,000'; }
}

function nextStep(step) {
    if(step === 2) {
        const gst = document.getElementById('ca_gst').value;
        if(gst && !/^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{1}[1-9A-Z]{1}Z[0-9A-Z]{1}$/.test(gst)){
            document.getElementById('gst-error').style.display='block'; return;
        } else { document.getElementById('gst-error').style.display='none'; }
    }
    if(step === 4) {
        document.getElementById('rev_biz').textContent = document.getElementById('ca_bizname').value;
        document.getElementById('rev_type').textContent = document.getElementById('ca_biztype').value;
        document.getElementById('rev_gst').textContent = document.getElementById('ca_gst').value || 'N/A';
        document.getElementById('rev_auth').textContent = document.getElementById('ca_auth_name').value + ' (' + document.getElementById('ca_auth_desig').value + ')';
        document.getElementById('rev_var').textContent = document.querySelector('input[name="ca_variant"]:checked').value;
        document.getElementById('rev_dep').textContent = '₹' + document.getElementById('ca_deposit').value;
        const od = document.getElementById('ca_od_req').value;
        document.getElementById('rev_od').textContent = od === 'Yes' ? document.getElementById('ca_od_limit').value : 'Not Required';
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

document.getElementById('currentForm').addEventListener('submit', (e) => {
    e.preventDefault();
    if(!document.getElementById('ca_agree').checked) return alert('Please agree to T&C');
    document.getElementById('submitBtn').disabled = true;
    document.getElementById('submitBtn').textContent = 'Processing...';
    
    const accNo = "EPCA" + new Date().getFullYear() + Math.floor(10000 + Math.random() * 90000);
    const biz = document.getElementById('ca_bizname').value;
    
    saveApplication('current', {
        accNo, bizName: biz,
        type: document.getElementById('ca_biztype').value,
        variant: document.querySelector('input[name="ca_variant"]:checked').value,
        authName: document.getElementById('ca_auth_name').value,
        deposit: document.getElementById('ca_deposit').value,
        status: 'Pending Verification'
    });
    
    setTimeout(() => {
        window.location.href = `current-success.html?acc=${accNo}&biz=${encodeURIComponent(biz)}`;
    }, 1500);
});
</script>
""" + FOOTER + "\n<script src=\"js/theme.js\"></script>\n</body></html>"

write_file('apply-current.html', apply_current)

current_success = HEAD.format(title="Current Application Submitted") + NAVBAR + """
<main class="section-padding bg-light">
    <div class="success-container card">
        <div class="success-icon" style="color:var(--accent);">✓</div>
        <h1 class="mb-sm" style="color:var(--text-main);">Application Submitted!</h1>
        <p class="text-muted mb-lg" style="font-size:1.1rem;"><strong id="succ_biz" style="color:var(--primary);"></strong></p>
        
        <div class="ref-box" style="display:inline-block; margin: 20px auto;">
            <p style="font-size:0.9rem; color:var(--text-muted); font-family:Inter,sans-serif; margin-bottom:5px;">Account Reference Number</p>
            <div id="succ_acc"></div>
        </div>

        <h3 class="text-left mb-md mt-xl">Processing Timeline</h3>
        <div class="status-stepper text-left" style="flex-wrap:wrap; gap:10px;">
            <div style="color:var(--accent);font-weight:bold;flex:1;min-width:120px;">1. Verification<br>(2-3 days)</div>
            <div style="flex:1;min-width:120px;">2. Activation</div>
            <div style="flex:1;min-width:120px;">3. Net Banking Setup</div>
            <div style="flex:1;min-width:120px;">4. RM Welcome Call</div>
        </div>

        <div style="display:flex; gap:15px; justify-content:center; margin-top:40px;">
            <button class="btn btn-primary" onclick="alert('Application tracking feature coming soon!')">Track Application</button>
            <a href="services.html" class="btn btn-outline">Back to Services</a>
        </div>
    </div>
</main>
<script>
    const params = new URLSearchParams(window.location.search);
    document.getElementById('succ_biz').textContent = params.get('biz') || 'Your Business';
    document.getElementById('succ_acc').textContent = params.get('acc') || 'EPCA202600000';
</script>
""" + FOOTER + "\n<script src=\"js/theme.js\"></script>\n</body></html>"

write_file('current-success.html', current_success)
print("Current flow generated.")
