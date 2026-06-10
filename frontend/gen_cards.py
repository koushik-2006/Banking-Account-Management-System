from gen_savings import HEAD, NAVBAR, FOOTER, write_file

cc_info = HEAD.format(title="Credit Cards") + NAVBAR + """
<main>
    <section class="service-hero" style="background:#0F172A;color:#fff;">
        <div class="container">
            <div class="breadcrumb" style="color:#94A3B8;"><a href="index.html" style="color:#C9A84C;">Home</a> &rarr; <a href="services.html" style="color:#C9A84C;">Services</a> &rarr; Credit Cards</div>
            <h1 style="color:#C9A84C;">Credit Cards</h1>
            <p class="tagline" style="color:#CBD5E1;">Enjoy exclusive rewards, cashback, and global acceptance.</p>
        </div>
    </section>
    
    <section class="section-padding bg-light">
        <div class="container">
            <div class="features-grid">
                <!-- SILVER -->
                <div class="card" style="background:linear-gradient(135deg, #1e293b, #0f172a); color:white; border:none;">
                    <h2 style="color:#94A3B8;margin-bottom:15px;">SILVER CARD</h2>
                    <ul style="line-height:2;font-size:0.9rem;margin-bottom:20px;">
                        <li><strong>Limit:</strong> Up to ₹1,50,000</li>
                        <li><strong>Cashback:</strong> 1% on all spends</li>
                        <li><strong>Annual Fee:</strong> ₹500 (waived on ₹1L spend)</li>
                        <li><strong>Perks:</strong> Fuel surcharge waiver, EMI purchases</li>
                    </ul>
                </div>
                <!-- GOLD -->
                <div class="card" style="background:linear-gradient(135deg, #422006, #713f12); color:white; border:2px solid #C9A84C;">
                    <h2 style="color:#C9A84C;margin-bottom:15px;">GOLD CARD</h2>
                    <ul style="line-height:2;font-size:0.9rem;margin-bottom:20px;">
                        <li><strong>Limit:</strong> Up to ₹5,00,000</li>
                        <li><strong>Cashback:</strong> 1.5% shopping, 2% dining</li>
                        <li><strong>Annual Fee:</strong> ₹1,000 (waived on ₹2.5L spend)</li>
                        <li><strong>Perks:</strong> 2 domestic lounge visits/year</li>
                    </ul>
                </div>
                <!-- PLATINUM -->
                <div class="card" style="background:linear-gradient(135deg, #171717, #0a0a0a); color:white; border:1px solid #333;">
                    <h2 style="color:#d4d4d4;margin-bottom:15px;">PLATINUM CARD</h2>
                    <ul style="line-height:2;font-size:0.9rem;margin-bottom:20px;">
                        <li><strong>Limit:</strong> Up to ₹15,00,000</li>
                        <li><strong>Cashback:</strong> 2% all, 3% travel & dining</li>
                        <li><strong>Annual Fee:</strong> ₹2,500 (waived on ₹5L spend)</li>
                        <li><strong>Perks:</strong> 4 intl lounge visits, Concierge</li>
                    </ul>
                </div>
            </div>
            <div class="text-center mt-xl">
                <a href="apply-credit-card.html" class="btn btn-primary" style="font-size: 1.2rem; padding: 15px 40px;">Apply Now</a>
            </div>
        </div>
    </section>
</main>
""" + FOOTER + "\n<script src=\"js/theme.js\"></script>\n</body></html>"

write_file('credit-card.html', cc_info)

apply_cc = HEAD.format(title="Apply Credit Card") + NAVBAR + """
<main class="section-padding bg-light">
    <div class="container container-narrow">
        <div class="card" id="application-form-card">
            <h2 class="text-center mb-md">Apply for Credit Card</h2>
            
            <div class="step-bar mb-xl">
                <div class="step-item active" id="step-btn-1">1. Card Selection</div>
                <div class="step-item" id="step-btn-2">2. Personal & Income</div>
                <div class="step-item" id="step-btn-3">3. Review</div>
            </div>

            <form id="ccForm">
                <!-- STEP 1 -->
                <div class="form-step active" id="step1">
                    <div class="form-group">
                        <label>Monthly Income (₹)</label>
                        <input type="number" id="cc_inc" required oninput="calcEligibility()">
                        <small class="text-muted">Eligibility depends on income.</small>
                    </div>

                    <div class="form-group mt-lg">
                        <label>Select Card Type</label>
                        <div class="radio-card-grid mt-sm">
                            <label class="radio-card-label" id="lbl_silver">
                                <input type="radio" name="cc_type" value="Silver" onchange="updatePreview()" checked>
                                <div class="radio-card-content" style="background:#1e293b;color:white;border:none;"><h4>SILVER</h4></div>
                            </label>
                            <label class="radio-card-label" id="lbl_gold">
                                <input type="radio" name="cc_type" value="Gold" onchange="updatePreview()">
                                <div class="radio-card-content" style="background:#713f12;color:white;border:none;"><h4>GOLD</h4></div>
                            </label>
                            <label class="radio-card-label" id="lbl_plat">
                                <input type="radio" name="cc_type" value="Platinum" onchange="updatePreview()">
                                <div class="radio-card-content" style="background:#0a0a0a;color:white;border:none;"><h4>PLATINUM</h4></div>
                            </label>
                        </div>
                    </div>

                    <!-- CSS Card Preview -->
                    <div id="card_preview" style="width:320px;height:200px;border-radius:15px;margin:20px auto;padding:20px;color:white;position:relative;background:#1e293b;box-shadow:0 10px 20px rgba(0,0,0,0.2);transition:all 0.3s;">
                        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:30px;">
                            <strong style="color:#C9A84C;font-family:Georgia,serif;">Easy <span style="color:#FFD700;">pAy</span></strong>
                            <span id="prev_badge" style="font-size:0.8rem;letter-spacing:1px;color:#94A3B8;">SILVER</span>
                        </div>
                        <div style="font-family:monospace;font-size:1.4rem;letter-spacing:3px;margin-bottom:15px;">●●●● ●●●● ●●●● ####</div>
                        <div style="display:flex;justify-content:space-between;align-items:flex-end;">
                            <div>
                                <div style="font-size:0.6rem;opacity:0.8;">VALID THRU</div>
                                <div style="font-family:monospace;">MM/YY</div>
                                <div id="prev_name" style="margin-top:10px;text-transform:uppercase;font-size:0.9rem;letter-spacing:1px;">CARD HOLDER</div>
                            </div>
                            <div style="font-style:italic;font-weight:bold;font-size:1.2rem;">VISA</div>
                        </div>
                    </div>

                    <div class="text-right mt-lg"><button type="button" class="btn btn-primary next-btn" onclick="nextStep(2)">Next &rarr;</button></div>
                </div>

                <!-- STEP 2 -->
                <div class="form-step" id="step2" style="display:none;">
                    <div class="form-group"><label>Billing Address</label><textarea id="cc_addr" required></textarea></div>
                    <div class="form-group">
                        <label>Existing Credit Cards?</label>
                        <select id="cc_ext_has" onchange="document.getElementById('ext_div').style.display=this.value==='Yes'?'block':'none';calcEligibility();">
                            <option value="No">No</option><option value="Yes">Yes</option>
                        </select>
                    </div>
                    <div class="form-group" id="ext_div" style="display:none;">
                        <label>Total Existing Credit Limit (₹)</label>
                        <input type="number" id="cc_ext_lim" value="0" oninput="calcEligibility()">
                    </div>
                    
                    <div class="calc-box">
                        <div class="calc-row text-center" style="display:block;"><span>Estimated Credit Limit:</span> <strong id="calc_lim" style="color:var(--accent);font-size:1.5rem;display:block;margin-top:10px;">₹0</strong></div>
                    </div>

                    <div class="text-between mt-lg">
                        <button type="button" class="btn btn-outline" onclick="prevStep(1)">&larr; Back</button>
                        <button type="button" class="btn btn-primary next-btn" onclick="nextStep(3)">Next &rarr;</button>
                    </div>
                </div>

                <!-- STEP 3 -->
                <div class="form-step" id="step3" style="display:none;">
                    <div class="calc-box">
                        <h3 class="mb-sm">Review Summary</h3>
                        <div class="calc-row"><span>Card Type:</span> <strong id="rev_type"></strong></div>
                        <div class="calc-row"><span>Estimated Limit:</span> <strong id="rev_lim" style="color:var(--accent);"></strong></div>
                    </div>
                    <div class="form-group mt-md"><label style="font-weight:normal; display:flex; gap:10px;"><input type="checkbox" id="cc_agree" required><span>I declare all information is correct.</span></label></div>
                    <div class="text-between mt-lg">
                        <button type="button" class="btn btn-outline" onclick="prevStep(2)">&larr; Back</button>
                        <button type="submit" class="btn btn-accent" id="submitBtn">Apply for Card</button>
                    </div>
                </div>
            </form>
        </div>
    </div>
</main>
<script>
requireLogin('Credit Card', 'apply-credit-card.html');
const user = getUser();
if(user) {
    document.getElementById('prev_name').textContent = user.name;
}

let estLim = 0;
function calcEligibility() {
    const inc = Number(document.getElementById('cc_inc').value) || 0;
    
    // Eligibility UI
    const rG = document.getElementById('lbl_gold');
    const rP = document.getElementById('lbl_plat');
    
    if(inc < 20000) {
        rG.style.opacity = '0.3'; rG.style.pointerEvents = 'none';
        rP.style.opacity = '0.3'; rP.style.pointerEvents = 'none';
        document.querySelector('input[value="Silver"]').checked = true;
    } else if(inc <= 50000) {
        rG.style.opacity = '1'; rG.style.pointerEvents = 'auto';
        rP.style.opacity = '0.3'; rP.style.pointerEvents = 'none';
        if(document.querySelector('input[name="cc_type"]:checked').value === 'Platinum') {
            document.querySelector('input[value="Gold"]').checked = true;
        }
    } else {
        rG.style.opacity = '1'; rG.style.pointerEvents = 'auto';
        rP.style.opacity = '1'; rP.style.pointerEvents = 'auto';
    }
    updatePreview();

    // Limit Calc
    const cType = document.querySelector('input[name="cc_type"]:checked').value;
    const extHas = document.getElementById('cc_ext_has').value;
    const extLim = extHas === 'Yes' ? (Number(document.getElementById('cc_ext_lim').value) || 0) : 0;
    
    let base = inc * 3;
    if(cType === 'Gold') base = inc * 5;
    if(cType === 'Platinum') base = inc * 8;
    
    let avail = base - extLim;
    const capped = { Silver: 150000, Gold: 500000, Platinum: 1500000 };
    estLim = Math.max(0, Math.min(avail, capped[cType]));
    
    document.getElementById('calc_lim').textContent = '₹' + estLim.toLocaleString('en-IN');
}

function updatePreview() {
    const t = document.querySelector('input[name="cc_type"]:checked').value;
    const p = document.getElementById('card_preview');
    const b = document.getElementById('prev_badge');
    if(t === 'Silver') { p.style.background = '#1e293b'; b.textContent = 'SILVER'; b.style.color = '#94A3B8'; }
    if(t === 'Gold') { p.style.background = '#713f12'; b.textContent = 'GOLD'; b.style.color = '#FFD700'; }
    if(t === 'Platinum') { p.style.background = '#0a0a0a'; b.textContent = 'PLATINUM'; b.style.color = '#d4d4d4'; }
}

function nextStep(step) {
    if(step === 2) {
        if(!document.getElementById('cc_inc').value) return alert('Enter income');
    }
    if(step === 3) {
        document.getElementById('rev_type').textContent = document.querySelector('input[name="cc_type"]:checked').value;
        document.getElementById('rev_lim').textContent = '₹' + estLim.toLocaleString('en-IN');
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

document.getElementById('ccForm').addEventListener('submit', (e) => {
    e.preventDefault();
    if(!document.getElementById('cc_agree').checked) return alert('Please agree');
    document.getElementById('submitBtn').disabled = true;
    
    const ccRef = generateRef('CC');
    const last4 = Math.floor(1000 + Math.random() * 9000);
    const expiry = `${String(new Date().getMonth()+1).padStart(2,'0')}/${new Date().getFullYear()+3 - 2000}`;
    
    saveApplication('card', {
        ccRef,
        cardType: document.querySelector('input[name="cc_type"]:checked').value,
        creditLimit: estLim,
        last4, expiry,
        status: 'Pending'
    });
    
    setTimeout(() => { window.location.href = `card-success.html?ref=${ccRef}&type=${document.querySelector('input[name="cc_type"]:checked').value}`; }, 1500);
});
updatePreview();
</script>
""" + FOOTER + "\n<script src=\"js/theme.js\"></script>\n</body></html>"

write_file('apply-credit-card.html', apply_cc)

cc_success = HEAD.format(title="Credit Card Submitted") + NAVBAR + """
<main class="section-padding bg-light">
    <div class="success-container card">
        <h1 class="mb-sm" style="color:var(--text-main);">Application Submitted!</h1>
        <div class="ref-box" style="display:inline-block; margin: 20px auto;">
            <p style="font-size:0.9rem; color:var(--text-muted); font-family:Inter,sans-serif; margin-bottom:5px;">Reference Number</p>
            <div id="succ_ref"></div>
        </div>
        
        <!-- VIRTUAL CARD PREVIEW -->
        <div id="card_preview" style="width:320px;height:200px;border-radius:15px;margin:20px auto;padding:20px;color:white;position:relative;background:#1e293b;box-shadow:0 10px 20px rgba(0,0,0,0.2);text-align:left;">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:30px;">
                <strong style="color:#C9A84C;font-family:Georgia,serif;">Easy <span style="color:#FFD700;">pAy</span></strong>
                <span id="prev_badge" style="font-size:0.8rem;letter-spacing:1px;color:#94A3B8;">SILVER</span>
            </div>
            <div style="font-family:monospace;font-size:1.4rem;letter-spacing:3px;margin-bottom:15px;opacity:0.5;">●●●● ●●●● ●●●● ●●●●</div>
            <div style="display:flex;justify-content:space-between;align-items:flex-end;">
                <div>
                    <div style="font-size:0.6rem;opacity:0.8;">VALID THRU</div>
                    <div style="font-family:monospace;">--/--</div>
                    <div style="margin-top:10px;font-size:0.9rem;letter-spacing:1px;background:#fcd34d;color:#92400e;padding:2px 5px;border-radius:4px;font-weight:bold;">PENDING APPROVAL</div>
                </div>
            </div>
        </div>

        <p class="text-muted mt-md mb-xl">Your card details will be revealed once approved.<br>Estimated processing: 3-5 working days.</p>
        <div style="display:flex; gap:15px; justify-content:center;">
            <a href="dashboard.html" class="btn btn-outline">Dashboard</a>
        </div>
    </div>
</main>
<script>
    const params = new URLSearchParams(window.location.search);
    document.getElementById('succ_ref').textContent = params.get('ref') || 'CC202600000';
    const t = params.get('type') || 'Silver';
    const p = document.getElementById('card_preview');
    const b = document.getElementById('prev_badge');
    if(t === 'Silver') { p.style.background = '#1e293b'; b.textContent = 'SILVER'; b.style.color = '#94A3B8'; }
    if(t === 'Gold') { p.style.background = '#713f12'; b.textContent = 'GOLD'; b.style.color = '#FFD700'; }
    if(t === 'Platinum') { p.style.background = '#0a0a0a'; b.textContent = 'PLATINUM'; b.style.color = '#d4d4d4'; }
</script>
""" + FOOTER + "\n<script src=\"js/theme.js\"></script>\n</body></html>"

write_file('card-success.html', cc_success)
print("Cards flow generated.")
