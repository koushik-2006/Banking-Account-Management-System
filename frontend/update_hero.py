import re

new_hero_image = """<div class="hero-image">
    <div id="hero-slideshow" style="position:relative; width:100%; height:380px; overflow:hidden;" onmouseenter="stopTimer()" onmouseleave="startTimer()">
        
        <!-- Slide 1: Mobile Dashboard -->
        <div class="hero-slide" style="position:absolute; top:0; left:0; width:100%; height:100%; opacity:1; transition:opacity 0.7s ease;">
            <svg viewBox="0 0 480 360" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
                <rect width="480" height="360" fill="transparent" />
                <!-- Smartphone -->
                <rect x="190" y="90" width="100" height="180" rx="15" fill="#0A2342" />
                <rect x="195" y="100" width="90" height="160" rx="8" fill="#FFFFFF" />
                <!-- Wifi -->
                <path d="M 265 110 Q 270 105 275 110" fill="none" stroke="#0A2342" stroke-width="1.5"/>
                <path d="M 267 113 Q 270 110 273 113" fill="none" stroke="#0A2342" stroke-width="1.5"/>
                <!-- Account Balance -->
                <text x="205" y="130" font-family="sans-serif" font-size="8" fill="#0A2342">Account Balance</text>
                <text x="205" y="145" font-family="sans-serif" font-size="14" font-weight="bold" fill="#C9A84C">₹1,24,500</text>
                <!-- Mini bar chart -->
                <rect x="210" y="210" width="10" height="20" fill="#C9A84C" />
                <rect x="225" y="190" width="10" height="40" fill="#C9A84C" />
                <rect x="240" y="200" width="10" height="30" fill="#C9A84C" />
                <rect x="255" y="170" width="10" height="60" fill="#C9A84C" />
                <!-- Floating coins with sparkle -->
                <circle cx="150" cy="150" r="12" fill="#C9A84C" />
                <text x="146" y="154" font-family="sans-serif" font-size="10" fill="#FFFFFF">₹</text>
                <path d="M 150 130 L 150 134 M 150 166 L 150 170 M 130 150 L 134 150 M 166 150 L 170 150" stroke="#C9A84C" stroke-width="1.5" />
                
                <circle cx="120" cy="200" r="10" fill="#C9A84C" />
                <text x="117" y="203" font-family="sans-serif" font-size="8" fill="#FFFFFF">₹</text>
                <path d="M 120 185 L 120 188 M 105 200 L 108 200" stroke="#C9A84C" stroke-width="1" />
                
                <circle cx="160" cy="240" r="15" fill="#C9A84C" />
                <text x="155" y="245" font-family="sans-serif" font-size="12" fill="#FFFFFF">₹</text>
            </svg>
        </div>
        
        <!-- Slide 2: Instant Fund Transfer -->
        <div class="hero-slide" style="position:absolute; top:0; left:0; width:100%; height:100%; opacity:0; transition:opacity 0.7s ease;">
            <svg viewBox="0 0 480 360" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
                <rect width="480" height="360" fill="transparent" />
                <!-- Left Bank -->
                <rect x="80" y="180" width="60" height="80" fill="#0A2342" />
                <polygon points="110,140 70,180 150,180" fill="#0A2342" />
                <rect x="90" y="200" width="10" height="60" fill="#E8F4FD" />
                <rect x="120" y="200" width="10" height="60" fill="#E8F4FD" />
                <!-- Right Bank -->
                <rect x="340" y="180" width="60" height="80" fill="#0A2342" />
                <polygon points="370,140 330,180 410,180" fill="#0A2342" />
                <rect x="350" y="200" width="10" height="60" fill="#E8F4FD" />
                <rect x="380" y="200" width="10" height="60" fill="#E8F4FD" />
                <!-- Arrow -->
                <path d="M 150 180 Q 240 100 330 180" fill="none" stroke="#C9A84C" stroke-width="12" />
                <polygon points="335,185 315,170 330,160" fill="#C9A84C" />
                <!-- Lightning -->
                <polygon points="240,110 230,130 240,130 235,150 250,125 240,125" fill="#FFFFFF" />
                <!-- Coins -->
                <circle cx="180" cy="150" r="6" fill="#C9A84C" />
                <circle cx="210" cy="130" r="6" fill="#C9A84C" />
                <circle cx="240" cy="120" r="6" fill="#C9A84C" />
                <circle cx="270" cy="130" r="6" fill="#C9A84C" />
                <circle cx="300" cy="150" r="6" fill="#C9A84C" />
                <!-- Badge -->
                <rect x="160" y="60" width="160" height="30" rx="15" fill="#FFFFFF" stroke="#C9A84C" stroke-width="2"/>
                <text x="240" y="80" font-family="sans-serif" font-size="14" font-weight="bold" fill="#0A2342" text-anchor="middle">₹50,000 Transferred</text>
            </svg>
        </div>

        <!-- Slide 3: FD Growth Tree -->
        <div class="hero-slide" style="position:absolute; top:0; left:0; width:100%; height:100%; opacity:0; transition:opacity 0.7s ease;">
            <svg viewBox="0 0 480 360" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
                <rect width="480" height="360" fill="transparent" />
                <!-- Line Chart behind -->
                <path d="M 120 280 L 180 240 L 260 250 L 360 120" fill="none" stroke="#FFFFFF" stroke-width="4" stroke-dasharray="8 4" />
                <!-- Terracotta Pot -->
                <polygon points="220,300 260,300 270,260 210,260" fill="#0A2342" />
                <!-- Tree Trunk -->
                <path d="M 240 260 Q 230 180 240 120" fill="none" stroke="#0A2342" stroke-width="8" />
                <!-- Branches -->
                <path d="M 238 200 Q 200 170 210 140" fill="none" stroke="#0A2342" stroke-width="5" />
                <path d="M 242 160 Q 280 130 290 100" fill="none" stroke="#0A2342" stroke-width="5" />
                <!-- Gold Circular Leaves -->
                <circle cx="240" cy="120" r="25" fill="#C9A84C" />
                <circle cx="210" cy="140" r="20" fill="#C9A84C" />
                <circle cx="290" cy="100" r="30" fill="#C9A84C" />
                <circle cx="260" cy="140" r="20" fill="#C9A84C" />
                <circle cx="220" cy="180" r="15" fill="#C9A84C" />
                <text x="290" y="105" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0A2342" text-anchor="middle">7.5% p.a.</text>
                <!-- Hand holding coin -->
                <path d="M 100 200 L 160 200" fill="none" stroke="#0A2342" stroke-width="15" stroke-linecap="round" />
                <circle cx="160" cy="190" r="12" fill="#C9A84C" />
                <text x="160" y="194" font-family="sans-serif" font-size="10" fill="#FFFFFF" text-anchor="middle">₹</text>
            </svg>
        </div>

        <!-- Slide 4: Credit Card Showcase -->
        <div class="hero-slide" style="position:absolute; top:0; left:0; width:100%; height:100%; opacity:0; transition:opacity 0.7s ease;">
            <svg viewBox="0 0 480 360" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
                <rect width="480" height="360" fill="transparent" />
                <!-- Card -->
                <rect x="80" y="80" width="320" height="200" rx="15" fill="#0A2342" />
                <rect x="80" y="110" width="320" height="30" fill="#C9A84C" />
                <!-- Sparkles -->
                <path d="M 60 60 L 65 75 L 80 80 L 65 85 L 60 100 L 55 85 L 40 80 L 55 75 Z" fill="#C9A84C" />
                <path d="M 400 280 L 405 290 L 415 295 L 405 300 L 400 310 L 395 300 L 385 295 L 395 290 Z" fill="#C9A84C" />
                <!-- Chip -->
                <rect x="110" y="160" width="40" height="30" rx="4" fill="#C9A84C" />
                <line x1="110" y1="170" x2="150" y2="170" stroke="#0A2342" stroke-width="1.5" />
                <line x1="110" y1="180" x2="150" y2="180" stroke="#0A2342" stroke-width="1.5" />
                <!-- Masked Number -->
                <text x="110" y="230" font-family="sans-serif" font-size="20" letter-spacing="4" fill="#FFFFFF">•••• •••• •••• 4242</text>
                <!-- VISA -->
                <text x="330" y="250" font-family="sans-serif" font-size="24" font-weight="bold" font-style="italic" fill="#FFFFFF">VISA</text>
                <!-- Contactless -->
                <path d="M 350 160 Q 360 170 350 180" fill="none" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round" />
                <path d="M 360 155 Q 375 170 360 185" fill="none" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round" />
                <path d="M 370 150 Q 390 170 370 190" fill="none" stroke="#FFFFFF" stroke-width="4" stroke-linecap="round" />
            </svg>
        </div>

        <!-- Slide 5: Security Shield -->
        <div class="hero-slide" style="position:absolute; top:0; left:0; width:100%; height:100%; opacity:0; transition:opacity 0.7s ease;">
            <svg viewBox="0 0 480 360" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
                <rect width="480" height="360" fill="transparent" />
                <!-- Binary Background -->
                <text x="50" y="80" font-family="monospace" font-size="14" fill="#E8F4FD" opacity="0.6">01011001 01101010</text>
                <text x="350" y="150" font-family="monospace" font-size="14" fill="#E8F4FD" opacity="0.6">11001011</text>
                <text x="80" y="250" font-family="monospace" font-size="14" fill="#E8F4FD" opacity="0.6">101101</text>
                <!-- Hex Shield -->
                <polygon points="240,50 330,100 330,220 240,290 150,220 150,100" fill="#0A2342" stroke="#0A2342" stroke-width="10" stroke-linejoin="round"/>
                <polygon points="240,65 315,110 315,210 240,270 165,210 165,110" fill="#C9A84C" />
                <!-- Padlock -->
                <rect x="210" y="170" width="60" height="45" rx="5" fill="#FFFFFF" />
                <path d="M 225 170 L 225 150 Q 240 120 255 150 L 255 170" fill="none" stroke="#FFFFFF" stroke-width="10" stroke-linecap="round" />
                <circle cx="240" cy="190" r="5" fill="#0A2342" />
                <rect x="238" y="190" width="4" height="12" fill="#0A2342" />
                <!-- Checkmarks -->
                <g fill="#28A745">
                    <circle cx="150" cy="100" r="15"/>
                    <circle cx="330" cy="100" r="15"/>
                    <circle cx="120" cy="160" r="15"/>
                    <circle cx="360" cy="160" r="15"/>
                    <circle cx="150" cy="220" r="15"/>
                    <circle cx="330" cy="220" r="15"/>
                </g>
                <g stroke="#FFFFFF" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" fill="none">
                    <polyline points="145,100 148,105 155,95"/>
                    <polyline points="325,100 328,105 335,95"/>
                    <polyline points="115,160 118,165 125,155"/>
                    <polyline points="355,160 358,165 365,155"/>
                    <polyline points="145,220 148,225 155,215"/>
                    <polyline points="325,220 328,225 335,215"/>
                </g>
                <!-- Badge -->
                <rect x="160" y="310" width="160" height="26" rx="13" fill="#FFFFFF" stroke="#0A2342" stroke-width="2" />
                <text x="240" y="328" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0A2342" text-anchor="middle">256-bit Encrypted</text>
            </svg>
        </div>

        <!-- Slide 6: Loan Approval -->
        <div class="hero-slide" style="position:absolute; top:0; left:0; width:100%; height:100%; opacity:0; transition:opacity 0.7s ease;">
            <svg viewBox="0 0 480 360" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
                <rect width="480" height="360" fill="transparent" />
                <!-- House Silhouette -->
                <polygon points="150,150 240,70 330,150" fill="#0A2342" />
                <rect x="170" y="150" width="140" height="100" fill="#0A2342" />
                <!-- Door -->
                <rect x="220" y="190" width="40" height="60" fill="#E8F4FD" />
                <!-- Windows -->
                <rect x="185" y="170" width="25" height="25" fill="#E8F4FD" />
                <rect x="270" y="170" width="25" height="25" fill="#E8F4FD" />
                <!-- Approval Stamp -->
                <circle cx="330" cy="100" r="35" fill="none" stroke="#C9A84C" stroke-width="4" />
                <text x="330" y="105" font-family="sans-serif" font-size="12" font-weight="bold" fill="#C9A84C" text-anchor="middle" transform="rotate(-15 330 100)">APPROVED</text>
                <!-- Document -->
                <rect x="90" y="100" width="60" height="80" fill="#FFFFFF" stroke="#0A2342" stroke-width="2"/>
                <line x1="100" y1="120" x2="140" y2="120" stroke="#0A2342" stroke-width="2" />
                <line x1="100" y1="135" x2="130" y2="135" stroke="#0A2342" stroke-width="2" />
                <line x1="100" y1="150" x2="140" y2="150" stroke="#0A2342" stroke-width="2" />
                <polyline points="100,120 105,125 115,110" fill="none" stroke="#28A745" stroke-width="3" />
                <polyline points="100,135 105,140 115,125" fill="none" stroke="#28A745" stroke-width="3" />
                <polyline points="100,150 105,155 115,140" fill="none" stroke="#28A745" stroke-width="3" />
                <!-- EMI Badge -->
                <rect x="190" y="270" width="100" height="30" rx="5" fill="#C9A84C" />
                <text x="240" y="290" font-family="sans-serif" font-size="14" font-weight="bold" fill="#FFFFFF" text-anchor="middle">₹8,500/mo</text>
            </svg>
        </div>

        <!-- Slide 7: Digital Banking App -->
        <div class="hero-slide" style="position:absolute; top:0; left:0; width:100%; height:100%; opacity:0; transition:opacity 0.7s ease;">
            <svg viewBox="0 0 480 360" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
                <rect width="480" height="360" fill="transparent" />
                <!-- Laptop -->
                <rect x="120" y="100" width="240" height="150" rx="10" fill="#0A2342" />
                <rect x="130" y="110" width="220" height="130" fill="#FFFFFF" />
                <polygon points="100,250 380,250 390,260 90,260" fill="#0A2342" />
                <!-- Sidebar -->
                <rect x="130" y="110" width="40" height="130" fill="#E8F4FD" />
                <!-- Metric Cards -->
                <rect x="180" y="120" width="70" height="30" rx="4" fill="#C9A84C" />
                <rect x="260" y="120" width="70" height="30" rx="4" fill="#E8F4FD" />
                <!-- Line Chart -->
                <rect x="180" y="160" width="150" height="70" fill="#E8F4FD" />
                <polyline points="180,230 200,210 230,220 270,180 330,200" fill="none" stroke="#0A2342" stroke-width="3" />
                <!-- Cloud -->
                <path d="M 380 90 Q 370 70 390 70 Q 410 70 410 90 Q 430 90 420 110 L 380 110 Z" fill="#E8F4FD" />
                <!-- Badge -->
                <rect x="200" y="60" width="100" height="24" rx="12" fill="#C9A84C" />
                <text x="250" y="77" font-family="sans-serif" font-size="12" font-weight="bold" fill="#FFFFFF" text-anchor="middle">24/7 Banking</text>
            </svg>
        </div>

        <!-- Slide 8: Rewards & Cashback -->
        <div class="hero-slide" style="position:absolute; top:0; left:0; width:100%; height:100%; opacity:0; transition:opacity 0.7s ease;">
            <svg viewBox="0 0 480 360" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
                <rect width="480" height="360" fill="transparent" />
                <!-- Angled Credit Card -->
                <g transform="translate(240, 180) rotate(-15) translate(-240, -180)">
                    <rect x="160" y="110" width="160" height="100" rx="10" fill="#0A2342" />
                    <rect x="160" y="130" width="160" height="20" fill="#E8F4FD" />
                    <text x="180" y="190" font-family="sans-serif" font-size="16" fill="#C9A84C" font-weight="bold">2% Cashback</text>
                </g>
                <!-- Gold Stars -->
                <path id="star" d="M 10 0 L 13 6 L 20 7 L 15 12 L 16 19 L 10 16 L 4 19 L 5 12 L 0 7 L 7 6 Z" fill="#C9A84C" />
                <use href="#star" x="120" y="80" />
                <use href="#star" x="320" y="60" />
                <use href="#star" x="100" y="180" />
                <use href="#star" x="380" y="150" />
                <use href="#star" x="160" y="240" />
                <use href="#star" x="340" y="260" />
                <use href="#star" x="220" y="50" transform="scale(1.5)" />
                <use href="#star" x="280" y="280" />
                <use href="#star" x="80" y="120" />
                <use href="#star" x="400" y="210" />
                <!-- Badge -->
                <rect x="140" y="300" width="200" height="30" rx="15" fill="#C9A84C" />
                <text x="240" y="320" font-family="sans-serif" font-size="14" font-weight="bold" fill="#0A2342" text-anchor="middle">500+ Reward Partners</text>
            </svg>
        </div>

        <button onclick="goTo(current-1)" style="position:absolute;left:10px;top:50%;transform:translateY(-50%);z-index:10;background:rgba(10,35,66,0.5);color:#E6F1FB;border:none;border-radius:50%;width:36px;height:36px;cursor:pointer;font-size:18px;">&#10094;</button>
        <button onclick="goTo(current+1)" style="position:absolute;right:10px;top:50%;transform:translateY(-50%);z-index:10;background:rgba(10,35,66,0.5);color:#E6F1FB;border:none;border-radius:50%;width:36px;height:36px;cursor:pointer;font-size:18px;">&#10095;</button>

        <div style="position:absolute; bottom:15px; left:50%; transform:translateX(-50%); display:flex; gap:8px; z-index:10;">
            <div class="slide-dot" style="width:10px; height:10px; border-radius:50%; background:#C9A84C; cursor:pointer;" onclick="goTo(0)"></div>
            <div class="slide-dot" style="width:10px; height:10px; border-radius:50%; background:#ccc; cursor:pointer;" onclick="goTo(1)"></div>
            <div class="slide-dot" style="width:10px; height:10px; border-radius:50%; background:#ccc; cursor:pointer;" onclick="goTo(2)"></div>
            <div class="slide-dot" style="width:10px; height:10px; border-radius:50%; background:#ccc; cursor:pointer;" onclick="goTo(3)"></div>
            <div class="slide-dot" style="width:10px; height:10px; border-radius:50%; background:#ccc; cursor:pointer;" onclick="goTo(4)"></div>
            <div class="slide-dot" style="width:10px; height:10px; border-radius:50%; background:#ccc; cursor:pointer;" onclick="goTo(5)"></div>
            <div class="slide-dot" style="width:10px; height:10px; border-radius:50%; background:#ccc; cursor:pointer;" onclick="goTo(6)"></div>
            <div class="slide-dot" style="width:10px; height:10px; border-radius:50%; background:#ccc; cursor:pointer;" onclick="goTo(7)"></div>
        </div>
    </div>
    <script>
        let current = 0, slides, dots, timer;
        function init() {
          slides = document.querySelectorAll('.hero-slide');
          dots = document.querySelectorAll('.slide-dot');
          startTimer();
        }
        function goTo(n) {
          slides[current].style.opacity = '0';
          dots[current].style.background = '#ccc';
          current = (n + slides.length) % slides.length;
          slides[current].style.opacity = '1';
          dots[current].style.background = '#C9A84C';
        }
        function startTimer() { timer = setInterval(() => goTo(current + 1), 3500); }
        function stopTimer() { clearInterval(timer); }
        document.addEventListener('DOMContentLoaded', init);
    </script>
</div>"""

import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace everything from <div class="hero-image"> to the closing </div> of that block
# The block ends right before <!-- Statistics Section -->
# So we can match <div class="hero-image">.*?</div>\s*<!-- Statistics Section -->
pattern = re.compile(r'<div class="hero-image">.*?</div>(?=\s*<!-- Statistics Section -->)', re.DOTALL)
new_content = pattern.sub(new_hero_image, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated index.html hero section.")
