function requireLogin(serviceName, returnUrl) {
    const user = JSON.parse(localStorage.getItem('bams_user') || 'null');
    if (!user || !user.token) {
        localStorage.setItem('redirect_after_login', returnUrl);
        window.location.href = 'login.html';
    }
}

function saveApplication(type, data) {
    const key = `bams_${type}_apps`;
    const apps = JSON.parse(localStorage.getItem(key) || '[]');
    data.date = new Date().toISOString();
    apps.push(data);
    localStorage.setItem(key, JSON.stringify(apps));
}

function generateRef(prefix) {
    return prefix + new Date().getFullYear() + Math.floor(100000 + Math.random() * 900000);
}

function getUser() {
    return JSON.parse(localStorage.getItem('bams_user') || 'null');
}
