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

document.addEventListener('DOMContentLoaded', function() {
    // Add to cart functionality
    document.querySelectorAll('.add-to-cart').forEach(button => {
        button.addEventListener('click', async function() {
            const productId = this.dataset.product;
            try {
                const response = await fetch('/add-to-cart/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': getCookie('csrftoken')
                    },
                    body: JSON.stringify({
                        product_id: productId
                    })
                });
                const data = await response.json();
                updateCartCount(data.cart_count);
                showMessage('Product added to cart!', 'success');
            } catch (error) {
                showMessage('Error adding product to cart', 'error');
            }
        });
    });

    // Update quantity functionality
    document.querySelectorAll('.update-quantity').forEach(button => {
        button.addEventListener('click', async function() {
            const itemId = this.dataset.item;
            const action = this.dataset.action;
            try {
                const response = await fetch('/update-cart/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': getCookie('csrftoken')
                    },
                    body: JSON.stringify({
                        item_id: itemId,
                        action: action
                    })
                });
                const data = await response.json();
                if (data.success) {
                    location.reload();
                }
            } catch (error) {
                showMessage('Error updating cart', 'error');
            }
        });
    });

    // Helper function to get CSRF token
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    // Helper function to show messages
    function showMessage(message, type) {
        // Implement your message display logic here
    }
}); 
