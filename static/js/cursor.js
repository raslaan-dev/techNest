document.addEventListener('DOMContentLoaded', () => {
    // First ensure cursor element exists
    let cursor = document.querySelector('.cursor');
    if (!cursor) {
        cursor = document.createElement('div');
        cursor.classList.add('cursor');
        document.body.appendChild(cursor);
    }

    // Force initial styles
    cursor.style.cssText = `
        position: fixed;
        width: 30px;
        height: 30px;
        border: 2px solid #ffffff;
        border-radius: 50%;
        pointer-events: none;
        z-index: 999999;
        mix-blend-mode: difference;
        transition: transform 0.3s ease;
        transform: translate(-50%, -50%);
        display: block;
        opacity: 1;
    `;

    document.body.style.cursor = 'none';

    let mouseX = 0, mouseY = 0;
    let cursorX = 0, cursorY = 0;
    const delay = 0.15; // Adjust this value for the desired delay

    // Update mouse position on mousemove
    document.addEventListener('mousemove', e => {
        mouseX = e.clientX;
        mouseY = e.clientY;
    });

    function animateCursor() {
        // Smooth transition calculation
        cursorX += (mouseX - cursorX) * delay;
        cursorY += (mouseY - cursorY) * delay;

        // Position the cursor
        cursor.style.left = `${cursorX}px`;
        cursor.style.top = `${cursorY}px`;

        requestAnimationFrame(animateCursor);
    }

    animateCursor();

    // Enhanced hover effects
    document.querySelectorAll('a, button').forEach(element => {
        element.addEventListener('mouseenter', () => cursor.classList.add('grow'));
        element.addEventListener('mouseleave', () => cursor.classList.remove('grow'));
    });
});
