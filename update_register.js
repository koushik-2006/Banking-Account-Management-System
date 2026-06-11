const fs = require('fs');

const registerFiles = ['frontend/register.html', 'frontend/apply-savings.html'];

registerFiles.forEach(file => {
    if (fs.existsSync(file)) {
        let content = fs.readFileSync(file, 'utf-8');
        
        // Find the place where the old pending user is saved
        const oldLogic = `localStorage.setItem('easypay_pending_user'`;
        
        if (content.includes(oldLogic)) {
            const apiLogic = `
          // Replaced by node script
          const reqData = {
              fullName: document.getElementById('fullName').value.trim() + ' ' + document.getElementById('lastName').value.trim(),
              email: document.getElementById('email').value.trim(),
              phone: document.getElementById('mobile').value.trim(),
              password: document.getElementById('password').value,
              gender: document.getElementById('gender') ? document.getElementById('gender').value : 'Not specified',
              dateOfBirth: document.getElementById('dob').value,
              address: document.getElementById('street').value + ', ' + document.getElementById('city').value + ' - ' + document.getElementById('pincode').value,
              accountType: 'Savings',
              initialDeposit: 0.00
          };

          const btn = document.querySelector('button[onclick="submitApplication()"]');
          if(btn) { btn.disabled = true; btn.textContent = 'Processing...'; }

          try {
              const res = await EasyPayAPI.register(reqData);
              if (res.success) {
                  localStorage.setItem('easypay_pending_user', JSON.stringify({
                      accNo: res.data.accountNumber,
                      name: reqData.fullName,
                      email: reqData.email
                  }));
                  window.location.href = 'policies.html';
              } else {
                  alert("Registration Failed: " + res.message);
                  if(btn) { btn.disabled = false; btn.textContent = 'Submit Application'; }
              }
          } catch(err) {
              alert("Server Error. Please make sure backend is running.");
              if(btn) { btn.disabled = false; btn.textContent = 'Submit Application'; }
          }
          // End API logic`;

            content = content.replace(/localStorage\.setItem\('easypay_pending_user'[\s\S]*?window\.location\.href\s*=\s*'policies\.html';/g, apiLogic);
            
            // Also we need to make submitApplication async
            content = content.replace(/function submitApplication\(\)\s*\{/, 'async function submitApplication() {');
            
            fs.writeFileSync(file, content);
        }
    }
});
console.log("Updated register.html and apply-savings.html");
