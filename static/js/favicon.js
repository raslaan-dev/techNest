const icons = [
    '/static/img/black_solid.png', 
    '/static/img/purple_solid.png', 
    '/static/img/white_solid.png',
];
let index = 0;

function updateFavicon() {
    const faviconElement = document.getElementById('favicon');
    if (faviconElement) {
        // Pre-load the image to verify it exists
        const img = new Image();
        img.onload = function() {
            faviconElement.href = icons[index];
            index = (index + 1) % icons.length;
        };
        img.onerror = function() {
            console.error(`Failed to load favicon: ${icons[index]}`);
            // Skip to next image if current one fails
            index = (index + 1) % icons.length;
        };
        img.src = icons[index];
    }
}

// Reduce interval to make it easier to debug
setInterval(updateFavicon, 400);

