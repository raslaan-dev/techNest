// Initialize cart count
let itemCount = 0;

// Function to update cart count
function updateCartCount(count) {
    const cartCount = document.querySelector('.cart-count');
    if (cartCount) {
        cartCount.textContent = count;
    }
}

// Example: Update cart count (you can call this function whenever items are added/removed)
updateCartCount(itemCount);

// Example: Add to cart functionality
document.querySelectorAll('.add-to-cart').forEach(button => {
    button.addEventListener('click', () => {
        itemCount++;
        updateCartCount(itemCount);
    });
}); 