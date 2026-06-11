const fs = require('fs');

let indexHtml = fs.readFileSync('index.html', 'utf-8');
const aboutHtml = fs.readFileSync('about.html', 'utf-8');
const contactHtml = fs.readFileSync('contact.html', 'utf-8');
const faqHtml = fs.readFileSync('faq.html', 'utf-8');

// 1. Update Navbar Links in index.html
indexHtml = indexHtml.replace(/<nav class="nav-links">[\s\S]*?<\/nav>/, `<nav class="nav-links">
                <a href="#home" class="nav-link active">Home</a>
                <a href="#services" class="nav-link">Services</a>
                <a href="#about" class="nav-link">About</a>
                <a href="#contact" class="nav-link">Contact</a>
                <a href="#faq" class="nav-link">Help</a>
            </nav>`);

// 2. Add id="home" to hero section
indexHtml = indexHtml.replace(/<section class="hero section-padding">/, '<section id="home" class="hero section-padding">');

// 3. Extract sections
const aboutMatch = aboutHtml.match(/<!-- About Hero -->([\s\S]*?)<!-- Footer -->/);
let aboutContent = aboutMatch ? aboutMatch[1] : '';
aboutContent = aboutContent.replace(/<section class="about-hero/, '<section id="about" class="about-hero');

const contactMatch = contactHtml.match(/<!-- Contact Hero -->([\s\S]*?)<!-- Footer -->/);
let contactContent = contactMatch ? contactMatch[1] : '';
contactContent = contactContent.replace(/<section class="contact-hero/, '<section id="contact" class="contact-hero');

const faqMatch = faqHtml.match(/<!-- FAQ Hero -->([\s\S]*?)<!-- Footer -->/);
let faqContent = faqMatch ? faqMatch[1] : '';
faqContent = faqContent.replace(/<section class="faq-hero/, '<section id="faq" class="faq-hero');

// 4. Update Footer
const newFooter = `<!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-grid">
                <div class="footer-col-1">
                    <a href="#home" class="footer-logo">Easy pAy</a>
                    <p class="footer-desc">Providing secure and innovative banking solutions since 2026. Your trust is
                        our foundation.</p>
                </div>
                <div class="footer-col-2">
                    <h4 class="footer-title">Quick Links</h4>
                    <ul class="footer-links">
                        <li><a href="#home">Home</a></li>
                        <li><a href="#services">Services</a></li>
                        <li><a href="#about">About Us</a></li>
                        <li><a href="#contact">Contact</a></li>
                        <li><a href="#faq">FAQ</a></li>
                    </ul>
                </div>
                <div class="footer-col-3">
                    <h4 class="footer-title">Support</h4>
                    <ul class="footer-links">
                        <li><a href="#faq">Help Center</a></li>
                        <li><a href="policies.html">Privacy Policy</a></li>
                        <li><a href="policies.html">Terms & Conditions</a></li>
                        <li><a href="#branch-locator">Branch Locator</a></li>
                    </ul>
                </div>
                <div class="footer-col-4">
                    <h4 class="footer-title">Newsletter</h4>
                    <p class="footer-desc">Subscribe for the latest updates and offers.</p>
                    <form class="newsletter-form">
                        <input type="email" placeholder="Your Email" class="footer-input">
                        <button type="button" class="btn btn-accent" onclick="if(this.previousElementSibling.value) { alert('Thank you for subscribing!'); this.previousElementSibling.value=''; } else { alert('Please enter your email.'); }">Subscribe</button>
                    </form>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2026 Easy pAy. All rights reserved.</p>
                <p>Designed with ❤️ for modern banking.</p>
            </div>
        </div>
    </footer>`;

const replacementBlock = `${aboutContent}\n${contactContent}\n${faqContent}\n${newFooter}`;
indexHtml = indexHtml.replace(/<!-- Footer -->[\s\S]*?<\/footer>/, replacementBlock);

// 5. Extract and Append Scripts
const faqScriptMatch = faqHtml.match(/<script>\s*\/\/ Simple FAQ Search([\s\S]*?)<\/script>\s*<script>/);
const faqScript = faqScriptMatch ? `<script>\n        // Simple FAQ Search${faqScriptMatch[1]}</script>\n` : '';

const contactScriptMatch = contactHtml.match(/<script>\s*const branches =([\s\S]*?)<\/script>\s*<\/body>/);
const contactScript = contactScriptMatch ? `<script>\nconst branches =${contactScriptMatch[1]}</script>\n` : '';

const smoothScrollScript = `
    <script>
        // Smooth scroll for nav links
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if(target) {
                    target.scrollIntoView({
                        behavior: 'smooth'
                    });
                }
            });
        });
    </script>
`;

indexHtml = indexHtml.replace('</body>', `${smoothScrollScript}${faqScript}${contactScript}</body>`);

fs.writeFileSync('index.html', indexHtml);
console.log('SPA generated successfully with Regex.');
