document.addEventListener('DOMContentLoaded', function() {
    let lastScrollY = window.scrollY;
    const header = document.querySelector('header');
    
    window.addEventListener('scroll', () => {
        const currentScrollY = window.scrollY;
        
        if (currentScrollY > lastScrollY) {
            // Scrolling down
            header.style.transform = 'translate(-50%, -100%)';
        } else {
            // Scrolling up
            header.style.transform = 'translate(-50%, 0)';
        }
        
        lastScrollY = currentScrollY;
    });
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
