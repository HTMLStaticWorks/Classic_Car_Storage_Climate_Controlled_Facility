document.addEventListener('DOMContentLoaded', () => {
    // 1. Active State Highlight
    const currentPath = window.location.pathname;
    let pageName = currentPath.split('/').pop();
    if (!pageName) pageName = 'index.html';
    
    const navLinks = document.querySelectorAll('.main-nav .nav-link');
    navLinks.forEach(link => {
        link.classList.remove('active');
        const linkHref = link.getAttribute('href');
        if (linkHref === pageName) {
            link.classList.add('active');
        }
    });

    // 2. Theme Toggle
    const themeToggleBtns = document.querySelectorAll('.theme-toggle-btn');
    const htmlElement = document.documentElement;
    
    // Check local storage
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
        htmlElement.setAttribute('data-theme', savedTheme);
        updateThemeIcon(savedTheme);
    }

    if (themeToggleBtns.length > 0) {
        themeToggleBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                const currentTheme = htmlElement.getAttribute('data-theme');
                const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
                
                htmlElement.setAttribute('data-theme', newTheme);
                localStorage.setItem('theme', newTheme);
                updateThemeIcon(newTheme);
            });
        });
    }

    function updateThemeIcon(theme) {
        themeToggleBtns.forEach(btn => {
            if (theme === 'dark') {
                btn.innerHTML = '<i class="bi bi-sun"></i>';
            } else {
                btn.innerHTML = '<i class="bi bi-moon"></i>';
            }
        });
    }

    // 3. RTL Toggle
    const rtlToggleBtns = document.querySelectorAll('.rtl-toggle-btn');
    
    const savedDir = localStorage.getItem('dir');
    if (savedDir) {
        htmlElement.setAttribute('dir', savedDir);
    }

    if (rtlToggleBtns.length > 0) {
        rtlToggleBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                const currentDir = htmlElement.getAttribute('dir');
                const newDir = currentDir === 'rtl' ? 'ltr' : 'rtl';
                
                htmlElement.setAttribute('dir', newDir);
                localStorage.setItem('dir', newDir);
            });
        });
    }

    // 4. Initialize AOS if available
    if (typeof AOS !== 'undefined') {
        AOS.init({
            duration: 800,
            easing: 'ease-in-out',
            once: true,
            offset: 50
        });
    }

    // 5. Header Scroll Effect (Premium Glassmorphism)
    const header = document.querySelector('.site-header');
    if (header) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 50) {
                header.classList.add('scrolled');
            } else {
                header.classList.remove('scrolled');
            }
        });
    }

    // 6. Premium Animated Counters
    const counters = document.querySelectorAll('.counter-val');
    if (counters.length > 0) {
        const counterObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const target = parseInt(entry.target.getAttribute('data-target'));
                    const duration = 2000;
                    const step = target / (duration / 16);
                    let current = 0;
                    
                    const updateCounter = () => {
                        current += step;
                        if (current < target) {
                            entry.target.innerText = Math.ceil(current).toLocaleString();
                            requestAnimationFrame(updateCounter);
                        } else {
                            entry.target.innerText = target.toLocaleString();
                        }
                    };
                    updateCounter();
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.5 });
        
        counters.forEach(counter => counterObserver.observe(counter));
    }

    // 7. Mobile Menu Toggle
    const mobileToggleBtn = document.querySelector('.mobile-toggle');
    const mainNav = document.querySelector('.main-nav');
    if (mobileToggleBtn && mainNav) {
        mobileToggleBtn.addEventListener('click', () => {
            mainNav.classList.toggle('show');
            
            // Toggle icon between hamburger and close
            const icon = mobileToggleBtn.querySelector('i');
            if (icon) {
                if (mainNav.classList.contains('show')) {
                    icon.classList.remove('bi-list');
                    icon.classList.add('bi-x-lg');
                } else {
                    icon.classList.remove('bi-x-lg');
                    icon.classList.add('bi-list');
                }
            }
        });
    }

    // 8. Back to Top Button
    const backToTopBtn = document.querySelector('.back-to-top');
    if (backToTopBtn) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 300) {
                backToTopBtn.classList.add('active');
            } else {
                backToTopBtn.classList.remove('active');
            }
        });
        
        backToTopBtn.addEventListener('click', (e) => {
            e.preventDefault();
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }

    // 9. Interactive Chamber Telemetry Switcher
    const chamberTabs = document.querySelectorAll('.chamber-tab-card');
    const chamberImg = document.getElementById('chamberVehicleImg');
    const chamberBayName = document.getElementById('chamberBayName');
    const chamberModeStatus = document.getElementById('chamberModeStatus');
    const telTemp = document.getElementById('telTemp');
    const telHum = document.getElementById('telHum');
    const telVolt = document.getElementById('telVolt');
    const telAir = document.getElementById('telAir');

    const chamberData = {
        'climate': {
            bay: 'BAY #07-OMEGA',
            status: 'ATMOSPHERIC LOCK ACTIVE',
            img: 'https://images.unsplash.com/photo-1617788138017-80ad40651399?auto=format&fit=crop&w=900&q=80',
            temp: '68.2°F',
            hum: '50.1% RH',
            volt: '13.6V',
            air: '99.98%'
        },
        'security': {
            bay: 'VAULT SECTOR 04-APEX',
            status: 'BIOMETRIC & LASER ARMED',
            img: 'https://images.unsplash.com/photo-1503376780353-7e6692767b70?auto=format&fit=crop&w=900&q=80',
            temp: '68.0°F',
            hum: '49.8% RH',
            volt: '13.4V',
            air: '100.0%'
        },
        'power': {
            bay: 'TRICKLE STATION #12',
            status: 'CTEK FLOAT OPTIMIZED',
            img: 'https://images.unsplash.com/photo-1552519507-da3b142c6e3d?auto=format&fit=crop&w=900&q=80',
            temp: '68.5°F',
            hum: '50.0% RH',
            volt: '13.8V',
            air: '99.95%'
        },
        'telemetry': {
            bay: 'COCKPIT TELEMETRY LIVE',
            status: '4K OPTICS STREAMING',
            img: 'https://images.unsplash.com/photo-1492144534655-ae79c964c9d7?auto=format&fit=crop&w=900&q=80',
            temp: '68.1°F',
            hum: '50.3% RH',
            volt: '13.7V',
            air: '99.99%'
        }
    };

    if (chamberTabs.length > 0) {
        chamberTabs.forEach(tab => {
            tab.addEventListener('click', () => {
                chamberTabs.forEach(t => t.classList.remove('active'));
                tab.classList.add('active');
                
                const mode = tab.getAttribute('data-chamber-mode');
                const data = chamberData[mode];
                if (data && chamberImg) {
                    chamberImg.style.opacity = '0.3';
                    setTimeout(() => {
                        chamberImg.src = data.img;
                        if (chamberBayName) chamberBayName.textContent = data.bay;
                        if (chamberModeStatus) chamberModeStatus.textContent = data.status;
                        if (telTemp) telTemp.textContent = data.temp;
                        if (telHum) telHum.textContent = data.hum;
                        if (telVolt) telVolt.textContent = data.volt;
                        if (telAir) telAir.textContent = data.air;
                        chamberImg.style.opacity = '1';
                    }, 200);
                }
            });
        });
    }
});
