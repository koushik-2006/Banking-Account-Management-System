const API_BASE = 'http://localhost:8080/api';

function getToken() {
  const user = JSON.parse(localStorage.getItem('bams_user') || 'null');
  return user?.token || null;
}

function authHeaders() {
  return { 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + getToken() };
}

const EasyPayAPI = {
  register: (data) => fetch(API_BASE + '/auth/register', { method: 'POST', headers: {'Content-Type':'application/json'}, body: JSON.stringify(data) }).then(r => r.json()),
  login: (data) => fetch(API_BASE + '/auth/login', { method: 'POST', headers: {'Content-Type':'application/json'}, body: JSON.stringify(data) }).then(r => r.json()),
  getProfile: () => fetch(API_BASE + '/user/profile', { headers: authHeaders() }).then(r => r.json()),
  getTransactions: () => fetch(API_BASE + '/user/transactions', { headers: authHeaders() }).then(r => r.json()),
  getBalance: () => fetch(API_BASE + '/user/balance', { headers: authHeaders() }).then(r => r.json()),
  transfer: (data) => fetch(API_BASE + '/user/transfer', { method: 'POST', headers: authHeaders(), body: JSON.stringify(data) }).then(r => r.json()),
  applyLoan: (data) => fetch(API_BASE + '/user/apply-loan', { method: 'POST', headers: authHeaders(), body: JSON.stringify(data) }).then(r => r.json()),
  applyFD: (data) => fetch(API_BASE + '/user/apply-fd', { method: 'POST', headers: authHeaders(), body: JSON.stringify(data) }).then(r => r.json()),
  applyCard: (data) => fetch(API_BASE + '/user/apply-card', { method: 'POST', headers: authHeaders(), body: JSON.stringify(data) }).then(r => r.json()),
  getLoans: () => fetch(API_BASE + '/user/loans', { headers: authHeaders() }).then(r => r.json()),
  getFDs: () => fetch(API_BASE + '/user/fds', { headers: authHeaders() }).then(r => r.json()),
  getCards: () => fetch(API_BASE + '/user/cards', { headers: authHeaders() }).then(r => r.json()),
  adminGetUsers: () => fetch(API_BASE + '/admin/users', { headers: authHeaders() }).then(r => r.json()),
  adminGetStats: () => fetch(API_BASE + '/admin/stats', { headers: authHeaders() }).then(r => r.json()),
  adminUpdateLoan: (id, data) => fetch(API_BASE + '/admin/loans/' + id + '/decision', { method: 'PATCH', headers: authHeaders(), body: JSON.stringify(data) }).then(r => r.json()),
};
