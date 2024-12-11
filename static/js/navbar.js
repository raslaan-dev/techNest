let lastScrollTop = 0;
const navbar = document.querySelector('header');
const navbarHeight = navbar.offsetHeight;
let ticking = false;

window.addEventListener('scroll', () => {
    let scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    
    if (!ticking) {
        window.requestAnimationFrame(() => {
            if (scrollTop > lastScrollTop && scrollTop > 100) {
                // Scrolling down - hide navbar completely
                navbar.style.transform = `translate(-50%, -${navbarHeight + 20}px)`; // Added extra 20px to ensure it's hidden
            } else {
                // Scrolling up - show navbar
                navbar.style.transform = 'translate(-50%, 0)';
            }
            
            lastScrollTop = scrollTop;
            ticking = false;
        });
        
        ticking = true;
    }
});

// Mobile menu functionality
const mobileMenuButton = document.querySelector('[aria-label="Menu"]');
const mobileMenu = document.getElementById('mobile-menu');
const overlay = document.getElementById('mobile-menu-overlay');

function toggleMobileMenu() {
    const isOpen = mobileMenu.classList.contains('translate-x-0');
    mobileMenu.classList.toggle('translate-x-0');
    mobileMenu.classList.toggle('translate-x-full');
    overlay.classList.toggle('hidden');
    document.body.classList.toggle('overflow-hidden');
}

mobileMenuButton?.addEventListener('click', toggleMobileMenu);
overlay?.addEventListener('click', toggleMobileMenu); 