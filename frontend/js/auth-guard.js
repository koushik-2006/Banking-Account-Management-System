const BASE_URL = 'http://localhost:8080/api';

async function initDashboard() {
  const user = JSON.parse(localStorage.getItem('bams_user') || 'null');
  if (!user) {
    window.location.href = 'login.html';
    return;
  }

  try {
    const res = await fetch(BASE_URL + '/user/profile', {
      headers: { 'Authorization': 'Bearer ' + user.token }
    });

    if (res.status === 401) {
      localStorage.removeItem('bams_user');
      window.location.href = 'login.html';
      return;
    }

    const data = await res.json();
    if (data.success) {
      updateUserUI(data);
    } else {
      updateUserUI(user);
    }
  } catch (err) {
    updateUserUI(user);
  }
}

function updateUserUI(data) {
  const firstName = (data.fullName || data.name || 'User').split(' ')[0];
  const formatCurrency = (n) => '₹' + Number(n || 0).toLocaleString('en-IN', {minimumFractionDigits: 2});

  document.querySelectorAll('[data-user="firstName"]').forEach(el => el.textContent = firstName);
  document.querySelectorAll('[data-user="fullName"]').forEach(el => {
    if(el.tagName === 'INPUT') el.value = data.fullName || data.name || '';
    else el.textContent = data.fullName || data.name || '';
  });
  document.querySelectorAll('[data-user="email"]').forEach(el => {
    if(el.tagName === 'INPUT') el.value = data.email || '';
    else el.textContent = data.email || '';
  });
  document.querySelectorAll('[data-user="accountNumber"]').forEach(el => el.textContent = data.accountNumber || '');
  document.querySelectorAll('[data-user="accountType"]').forEach(el => el.textContent = (data.accountType || 'Savings') + ' Account');
  document.querySelectorAll('[data-user="balance"]').forEach(el => el.textContent = formatCurrency(data.balance));
  document.querySelectorAll('[data-user="status"]').forEach(el => {
    el.textContent = data.accountStatus || 'Active';
    el.className = 'status-badge status-' + (data.accountStatus || 'Active').toLowerCase();
  });

  if (data.picture) {
    document.querySelectorAll('[data-user="avatar"]').forEach(el => {
      if (el.tagName === 'IMG') el.src = data.picture;
    });
  } else {
    document.querySelectorAll('[data-user="avatarInitials"]').forEach(el => {
      el.textContent = (data.fullName || data.name || 'U').split(' ').map(w => w[0]).join('').toUpperCase().slice(0,2);
    });
  }
}

initDashboard();
