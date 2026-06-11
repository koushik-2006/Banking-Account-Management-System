document.addEventListener('DOMContentLoaded', () => {
    console.log('BAMS Frontend Initialized');

    // Quick Banking Widget
    const widgetHTML = `
        <div class="quick-widget" id="quickWidget">
            <button class="widget-toggle" id="widgetToggle">⚡</button>
            <div class="widget-menu" id="widgetMenu">
                <button class="widget-item" onclick="alert('Balance: $12,450.00')">💰 Balance</button>
                <button class="widget-item" onclick="location.href='transfer.html'">💸 Transfer</button>
                <button class="widget-item" onclick="location.href='notifications.html'">🔔 Alerts</button>
                <button class="widget-item" onclick="alert('Emergency Block requested!')">🚫 Block Card</button>
            </div>
        </div>
    `;

    if (document.body.classList.contains('dashboard-body')) {
        document.body.insertAdjacentHTML('beforeend', widgetHTML);

        const toggle = document.getElementById('widgetToggle');
        const menu = document.getElementById('widgetMenu');

        toggle.addEventListener('click', () => {
            menu.classList.toggle('active');
        });

        // Keyboard Shortcuts
        document.addEventListener('keydown', (e) => {
            if (e.altKey && e.key === 't') {
                location.href = 'transfer.html';
            }
            if (e.altKey && e.key === 's') {
                alert('Mini Statement: \n1. Amazon -$14.99\n2. Salary +$5000\n3. Rent -$1200');
            }
        });
    }

    // Smooth Scroll
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });

    // Contact Form Validation
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', (e) => {
            e.preventDefault();
            alert('Thank you for contacting BAMS! We will respond shortly.');
            contactForm.reset();
        });
    }

    // Help Ticket Form
    const helpTicketForm = document.getElementById('helpTicketForm');
    if (helpTicketForm) {
        helpTicketForm.addEventListener('submit', (e) => {
            e.preventDefault();
            alert('Help ticket submitted successfully. Ticket ID: #BAMS-' + Math.floor(Math.random() * 10000));
            helpTicketForm.reset();
        });
    }
});

// Authentication & Session Management
function getAuthState() {
    return JSON.parse(localStorage.getItem('bams_user') || 'null');
}

window.handleLogout = function() {
    localStorage.removeItem('bams_user');
    window.location.href = 'login.html';
};

function updateNavbarAuth() {
    const user = getAuthState();
    const navAuth = document.querySelector('.nav-auth-buttons') || document.querySelector('.nav-actions');
    
    if (user && navAuth) {
        navAuth.innerHTML = `
            <a href="dashboard.html" class="btn btn-outline-nav" style="border:none;">Dashboard</a>
            <a href="profile.html" class="btn btn-outline-nav" style="border:none;">Profile</a>
            <button onclick="handleLogout()" class="btn btn-primary-nav" style="cursor:pointer;">Logout</button>
        `;
    }
}

function protectRoutes() {
    const protectedRoutes = [
        'dashboard.html', 
        'profile.html', 
        'transactions.html', 
        'transfer.html', 
        'notifications.html', 
        'my-applications.html'
    ];
    
    const currentPath = window.location.pathname.split('/').pop();
    
    if (protectedRoutes.includes(currentPath) && !getAuthState()) {
        window.location.href = 'login.html';
    }
}

// Execute authentication checks
protectRoutes();
document.addEventListener('DOMContentLoaded', () => {
    updateNavbarAuth();
    syncProfileName();
});

// Dynamic Profile Synchronization
function syncProfileName() {
    const user = getAuthState();
    if (user && user.name) {
        const fullName = user.name;
        
        // 1. Dashboard Welcome Section and Sidebar Name
        const welcomeEls = document.querySelectorAll('.user-welcome-name, .sidebar-user-name, #welcome-name');
        welcomeEls.forEach(el => el.textContent = fullName);
        
        // 2. Profile Full Name explicitly defined by classes
        const fullNameEls = document.querySelectorAll('.user-full-name, #user-full-name');
        fullNameEls.forEach(el => {
            if (el.tagName === 'INPUT') {
                el.value = fullName;
            } else {
                el.textContent = fullName;
            }
        });

        // 3. User Dropdown or Topbar User Profile
        const topbarName = document.querySelector('.topbar-info .user-name');
        if (topbarName) topbarName.textContent = fullName;

        // 4. Any customer name field showing a hardcoded name (e.g. First Name / Last Name split in profile.html)
        const labels = document.querySelectorAll('label');
        labels.forEach(label => {
            const labelText = label.textContent.trim();
            const input = label.nextElementSibling;
            
            if (input && input.tagName === 'INPUT') {
                if (labelText === 'Last Name' && input.value === 'User') {
                    const nameParts = fullName.split(' ');
                    input.value = nameParts.length > 1 ? nameParts.slice(1).join(' ') : '';
                } else if (labelText === 'First Name') {
                    input.value = fullName.split(' ')[0];
                }
            }
        });
    }
}
