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
