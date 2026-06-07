fd_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Apply for Fixed Deposit | BAMS</title>
    <link rel="stylesheet" href="css/variables.css">
    <link rel="stylesheet" href="css/style.css">
    <link rel="shortcut icon" href="images/favicon.png" type="image/x-icon">
    <style>
        .breadcrumb { padding: 15px 0; font-size: 14px; color: var(--text-muted); }
        .breadcrumb a { color: var(--primary); text-decoration: none; }
        .breadcrumb a:hover { text-decoration: underline; }
        .live-calculator { background: #E8F4FD; padding: 20px; border-radius: 8px; border-left: 4px solid var(--primary); margin-top: 20px; }
        .calc-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 15px; margin-top: 15px; }
        .calc-item { background: #fff; padding: 15px; border-radius: 8px; text-align: center; box-shadow: 0 2px 5px rgba(0,0,0,0.05); }
        .calc-value { font-size: 1.5rem; font-weight: 700; color: var(--primary); margin-top: 5px; }
        .calc-label { font-size: 0.85rem; color: var(--text-muted); text-transform: uppercase; letter-spacing: 1px; }
        .summary-card { background: var(--bg-main); padding: 20px; border-radius: 8px; border: 1px solid #eee; margin-bottom: 20px; }
        .summary-item { display: flex; justify-content: space-between; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 5px; }
    </style>
</head>
<body>
    <header class="navbar">
        <div class="container nav-container">
            <a href="index.html" class="logo-container" style="display:flex;align-items:center;gap:8px;text-decoration:none;">
              <svg width="36" height="36" viewBox="0 0 36 36" fill="none" xmlns="http://www.w3.org/2000/svg">
                <rect width="36" height="36" rx="8" fill="#0A2342"/>
                <rect x="6" y="20" width="5" height="10" fill="#C9A84C"/>
                <rect x="13" y="14" width="5" height="16" fill="#C9A84C"/>
                <rect x="20" y="8" width="5" height="22" fill="#C9A84C"/>
                <rect x="6" y="18" width="22" height="2" fill="#F0C040"/>
              </svg>
              <span style="font-size:20px;font-weight:700;color:#0A2342;letter-spacing:1px;">BAMS</span>
            </a>
            <div class="nav-auth-buttons" style="display:flex; gap:10px; align-items:center;">
                <a href="login.html" class="btn btn-outline-nav">Login</a>
                <a href="register.html" class="btn btn-primary-nav">Open Account</a>
            </div>
        </div>
    </header>

    <main class="section-padding" style="min-height: 80vh;">
        <div class="container container-narrow">
            <div class="breadcrumb">
                <a href="index.html">Home</a> &rarr; <a href="services.html">Services</a> &rarr; Fixed Deposit
            </div>
            <div class="card registration-card">
                <div class="text-center mb-lg">
                    <h1 class="section-title">Open a Fixed Deposit</h1>
                    <p class="text-muted">Grow your savings with guaranteed returns.</p>
                </div>

                <div class="progress-bar-container">
                    <p class="text-center mb-md" style="font-weight: 600; color: var(--primary);">Step <span id="currentStepText">1</span> of 2</p>
                    <div class="progress-container">
                        <div class="progress-bar" id="progressBar" style="background-color: var(--accent); width: 0%;"></div>
                        <div class="progress-steps">
                            <div class="step active" data-step="1">1</div>
                            <div class="step" data-step="2">2</div>
                        </div>
                    </div>
                </div>

                <form id="applyForm" class="multi-step-form">
                    <!-- Step 1: Configuration -->
                    <div class="form-step active" id="step1">
                        <h2 class="form-step-title">Step 1: FD Configuration</h2>
                        <div class="form-group">
                            <label>Principal Amount (₹)</label>
                            <input type="number" id="principal" min="1000" value="10000" required>
                        </div>
                        <div class="form-group mt-md">
                            <label>Tenure: <span id="tenureLabel" style="color:var(--primary); font-weight:bold;">1 Year</span></label>
                            <input type="range" id="tenure" min="1" max="120" value="12" style="width:100%; accent-color: var(--accent);">
                        </div>
                        <div class="form-group mt-md">
                            <label>Interest Payout</label>
                            <div style="display: flex; gap: 15px; margin-top: 5px;">
                                <label><input type="radio" name="payout" value="Monthly"> Monthly</label>
                                <label><input type="radio" name="payout" value="Quarterly"> Quarterly</label>
                                <label><input type="radio" name="payout" value="On Maturity" checked> On Maturity</label>
                            </div>
                        </div>
                        <div class="form-group mt-md">
                            <label style="font-weight: 600; display: flex; align-items: center; gap: 10px;">
                                <input type="checkbox" id="seniorToggle" style="width:20px;height:20px;accent-color:var(--primary);">
                                Senior Citizen (+0.5% extra rate)
                            </label>
                        </div>
                        
                        <!-- Live Calculator -->
                        <div class="live-calculator">
                            <h3 style="font-size: 1.1rem; color: var(--primary); margin-bottom: 5px;">Live Returns Calculator</h3>
                            <p style="font-size: 0.85rem; color: var(--text-muted);">Estimates are based on current rates.</p>
                            <div class="calc-grid">
                                <div class="calc-item">
                                    <div class="calc-label">Interest Rate</div>
                                    <div class="calc-value" id="calcRate">6.5%</div>
                                </div>
                                <div class="calc-item">
                                    <div class="calc-label">Interest Earned</div>
                                    <div class="calc-value" id="calcInterest">₹650</div>
                                </div>
                                <div class="calc-item">
                                    <div class="calc-label">Maturity Amount</div>
                                    <div class="calc-value" id="calcMaturity">₹10,650</div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Step 2: Review & Submit -->
                    <div class="form-step" id="step2">
                        <h2 class="form-step-title">Step 2: Review FD Details</h2>
                        <div class="summary-card" id="summaryCard"></div>
                        <div class="form-group" style="margin-top: 20px;">
                            <label style="font-weight: 400; display: flex; align-items: center; gap: 8px;">
                                <input type="checkbox" required> I agree to the <a href="policies.html" class="text-link">Terms & Conditions</a>
                            </label>
                        </div>
                    </div>

                    <!-- Navigation Buttons -->
                    <div class="form-navigation mt-xl">
                        <button type="button" class="btn btn-outline" id="prevBtn" style="visibility: hidden;">Back</button>
                        <button type="button" class="btn btn-primary" id="nextBtn">Next</button>
                        <button type="submit" class="btn btn-accent" id="submitBtn" style="display: none;">Confirm Booking</button>
                    </div>
                </form>
            </div>
        </div>
    </main>

    <!-- Success Modal -->
    <div id="successModal" class="modal-overlay" style="display: none;">
        <div class="modal-card">
            <div class="modal-icon">✅</div>
            <h2 class="mb-md">FD Booked Successfully!</h2>
            <p class="text-muted mb-lg">Your Fixed Deposit has been initiated.</p>
            <div style="background: var(--bg-main); padding: var(--space-md); border-radius: var(--radius-md); margin-bottom: var(--space-lg);">
                <p style="font-size: 0.9rem; margin-bottom: 5px;">FD Reference Number:</p>
                <strong style="font-size: 1.5rem; color: var(--primary);" id="fdRefNumber">FD2026XXXX</strong>
            </div>
            <p style="font-size: 0.9rem; color: var(--accent);">Redirecting to dashboard...</p>
        </div>
    </div>

    <footer class="footer">
        <div class="container text-center">
            <div style="margin-bottom: 10px;">
                <a href="index.html" style="color:white; margin:0 10px; text-decoration:none;">Home</a> |
                <a href="services.html" style="color:white; margin:0 10px; text-decoration:none;">Services</a> |
                <a href="about.html" style="color:white; margin:0 10px; text-decoration:none;">About</a> |
                <a href="contact.html" style="color:white; margin:0 10px; text-decoration:none;">Contact</a> |
                <a href="faq.html" style="color:white; margin:0 10px; text-decoration:none;">FAQ</a> |
                <a href="policies.html" style="color:white; margin:0 10px; text-decoration:none;">Privacy Policy</a> |
                <a href="policies.html" style="color:white; margin:0 10px; text-decoration:none;">Terms & Conditions</a>
            </div>
            <p>&copy; 2026 Banking Account Management System. All rights reserved.</p>
            <a href="admin/login.html" style="font-size:11px;color:#555;opacity:0.4;text-decoration:none;">Admin</a>
        </div>
    </footer>

    <script>
        const form = document.getElementById('applyForm');
        const steps = document.querySelectorAll('.form-step');
        const progressSteps = document.querySelectorAll('.step');
        const progressBar = document.getElementById('progressBar');
        const currentStepText = document.getElementById('currentStepText');
        const prevBtn = document.getElementById('prevBtn');
        const nextBtn = document.getElementById('nextBtn');
        const submitBtn = document.getElementById('submitBtn');
        let currentStep = 0;

        // Calculator Logic
        const principalEl = document.getElementById('principal');
        const tenureEl = document.getElementById('tenure');
        const tenureLabel = document.getElementById('tenureLabel');
        const seniorToggle = document.getElementById('seniorToggle');
        const calcRate = document.getElementById('calcRate');
        const calcInterest = document.getElementById('calcInterest');
        const calcMaturity = document.getElementById('calcMaturity');

        function formatCurrency(num) { return '₹' + num.toLocaleString('en-IN', {maximumFractionDigits:0}); }

        function updateCalculator() {
            let months = parseInt(tenureEl.value);
            let label = months < 12 ? months + ' Months' : (months/12).toFixed(1).replace('.0','') + ' Years';
            if(months < 1) { label = '7 Days'; months = 0.25; }
            tenureLabel.textContent = label;

            let principal = parseFloat(principalEl.value) || 0;
            let baseRate = 5.0;
            if(months >= 12) baseRate = 6.5;
            if(months >= 36) baseRate = 7.0;
            if(seniorToggle.checked) baseRate += 0.5;

            let interest = principal * (baseRate/100) * (months/12);
            let maturity = principal + interest;

            calcRate.textContent = baseRate.toFixed(1) + '%';
            calcInterest.textContent = formatCurrency(interest);
            calcMaturity.textContent = formatCurrency(maturity);
        }

        principalEl.addEventListener('input', updateCalculator);
        tenureEl.addEventListener('input', updateCalculator);
        seniorToggle.addEventListener('change', updateCalculator);
        updateCalculator();

        function checkValidation() {
            const inputs = steps[currentStep].querySelectorAll('input, select');
            let valid = true;
            inputs.forEach(input => {
                if(!input.checkValidity()) {
                    input.reportValidity();
                    valid = false;
                }
            });
            return valid;
        }

        function populateSummary() {
            const principal = principalEl.value;
            const tenure = tenureLabel.textContent;
            const payout = document.querySelector('input[name="payout"]:checked').value;
            const rate = calcRate.textContent;
            const maturity = calcMaturity.textContent;
            
            document.getElementById('summaryCard').innerHTML = `
                <div class="summary-item"><span>Principal Amount:</span> <strong>₹${parseFloat(principal).toLocaleString('en-IN')}</strong></div>
                <div class="summary-item"><span>Tenure:</span> <strong>${tenure}</strong></div>
                <div class="summary-item"><span>Interest Rate:</span> <strong>${rate}</strong></div>
                <div class="summary-item"><span>Payout:</span> <strong>${payout}</strong></div>
                <div class="summary-item" style="border-bottom:none;"><span>Est. Maturity:</span> <strong style="color:var(--primary);">${maturity}</strong></div>
            `;
        }

        function updateForm() {
            steps.forEach((step, index) => step.classList.toggle('active', index === currentStep));
            progressSteps.forEach((step, index) => step.classList.toggle('active', index <= currentStep));
            progressBar.style.width = ((currentStep / (steps.length - 1)) * 100) + '%';
            currentStepText.textContent = currentStep + 1;

            prevBtn.style.visibility = (currentStep === 0) ? 'hidden' : 'visible';
            if (currentStep === steps.length - 1) {
                nextBtn.style.display = 'none';
                submitBtn.style.display = 'inline-block';
                populateSummary();
            } else {
                nextBtn.style.display = 'inline-block';
                submitBtn.style.display = 'none';
            }
        }

        nextBtn.addEventListener('click', () => {
            if (checkValidation()) {
                currentStep++;
                updateForm();
            }
        });

        prevBtn.addEventListener('click', () => {
            currentStep--;
            updateForm();
        });

        form.addEventListener('submit', (e) => {
            e.preventDefault();
            if(!checkValidation()) return;
            
            const randomDigits = Math.floor(1000 + Math.random() * 9000);
            const refNo = `FD2026${randomDigits}`;

            const applicationData = {
                type: 'Fixed Deposit',
                reference: refNo,
                amount: principalEl.value,
                tenure: tenureLabel.textContent,
                rate: calcRate.textContent,
                maturity: calcMaturity.textContent,
                dateApplied: new Date().toISOString(),
                status: 'Pending'
            };
            
            const user = JSON.parse(localStorage.getItem('bams_user'));
            const applicant = user ? user.name : 'Guest User';
            
            const apps = JSON.parse(localStorage.getItem('bams_fd_apps') || '[]');
            apps.push({...applicationData, applicant: applicant});
            localStorage.setItem('bams_fd_apps', JSON.stringify(apps));
            
            document.getElementById('fdRefNumber').textContent = refNo;
            document.getElementById('successModal').style.display = 'flex';
            setTimeout(() => { window.location.href = 'dashboard.html'; }, 3000);
        });

        window.addEventListener('DOMContentLoaded', () => {
            const user = JSON.parse(localStorage.getItem('bams_user') || 'null');
            if (user) {
                const navAuth = document.querySelector('.nav-auth-buttons');
                if (navAuth) {
                    navAuth.innerHTML = `<a href="dashboard.html" class="btn btn-outline-nav">Dashboard</a>`;
                }
            }
        });
    </script>
</body>
</html>"""
with open("apply-fd.html", "w", encoding="utf-8") as f:
    f.write(fd_html)
print("Created apply-fd.html")
