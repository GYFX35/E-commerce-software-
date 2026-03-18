// Simple Shopping Cart Logic for E-Commerce MVP

document.addEventListener('DOMContentLoaded', () => {
    let cart = JSON.parse(localStorage.getItem('cart')) || [];
    updateCartUI();

    // Add to Cart from products page or index
    document.querySelectorAll('.add-to-cart').forEach(button => {
        button.addEventListener('click', (e) => {
            const id = e.target.dataset.id;
            const name = e.target.dataset.name;
            const price = parseFloat(e.target.dataset.price);
            addToCart(id, name, price);
            alert(`${name} added to cart!`);
        });
    });

    // Add to Cart from product detail page
    const detailAddToCartBtn = document.querySelector('.add-to-cart-detail');
    if (detailAddToCartBtn) {
        detailAddToCartBtn.addEventListener('click', () => {
            const id = new URLSearchParams(window.location.search).get('id') || '1';
            const name = document.getElementById('product-name').textContent;
            const priceText = document.getElementById('product-price').textContent;
            const price = parseFloat(priceText.replace('$', ''));
            const quantity = parseInt(document.getElementById('quantity').value) || 1;

            for(let i=0; i<quantity; i++) {
                addToCart(id, name, price, false); // Add multiple if quantity > 1
            }
            updateCartUI();
            alert(`${name} added to cart!`);
        });
    }

    // Cart Page Specific Logic
    if (window.location.pathname.includes('cart.html')) {
        renderCartItems();
    }

    // Checkout Page Specific Logic
    if (window.location.pathname.includes('checkout.html')) {
        renderCheckoutSummary();
        const checkoutForm = document.getElementById('checkout-form');
        if (checkoutForm) {
            checkoutForm.addEventListener('submit', (e) => {
                e.preventDefault();
                alert('Thank you for your order! Your purchase is being processed.');
                localStorage.removeItem('cart');
                window.location.href = 'index.html';
            });
        }
    }

    function addToCart(id, name, price, update = true) {
        const existingItem = cart.find(item => item.id === id);
        if (existingItem) {
            existingItem.quantity += 1;
        } else {
            cart.push({ id, name, price, quantity: 1 });
        }
        localStorage.setItem('cart', JSON.stringify(cart));
        if (update) updateCartUI();
    }

    function updateCartUI() {
        const cartCount = document.getElementById('cart-count');
        const checkoutCartCount = document.getElementById('checkout-cart-count');
        const totalItems = cart.reduce((total, item) => total + item.quantity, 0);

        if (cartCount) cartCount.textContent = totalItems;
        if (checkoutCartCount) checkoutCartCount.textContent = totalItems;
    }

    function renderCartItems() {
        const cartTableBody = document.getElementById('cart-items');
        const subtotalEl = document.getElementById('cart-subtotal');
        const totalEl = document.getElementById('cart-total');

        if (!cartTableBody) return;

        cartTableBody.innerHTML = '';
        let subtotal = 0;

        if (cart.length === 0) {
            cartTableBody.innerHTML = '<tr><td colspan="5" class="text-center py-5">Your cart is empty. <a href="products.html">Start shopping!</a></td></tr>';
            const checkoutBtn = document.getElementById('checkout-btn');
            if(checkoutBtn) checkoutBtn.classList.add('disabled');
        } else {
            cart.forEach(item => {
                const itemTotal = item.price * item.quantity;
                subtotal += itemTotal;

                const tr = document.createElement('tr');
                tr.innerHTML = `
                    <td><strong>${item.name}</strong></td>
                    <td>$${item.price.toFixed(2)}</td>
                    <td>
                        <input type="number" class="form-control quantity-input" data-id="${item.id}" value="${item.quantity}" min="1" style="width: 70px;">
                    </td>
                    <td>$${itemTotal.toFixed(2)}</td>
                    <td>
                        <button class="btn btn-sm btn-danger remove-item" data-id="${item.id}"><i class="fas fa-trash"></i></button>
                    </td>
                `;
                cartTableBody.appendChild(tr);
            });
        }

        if (subtotalEl) subtotalEl.textContent = `$${subtotal.toFixed(2)}`;
        if (totalEl) totalEl.textContent = `$${subtotal.toFixed(2)}`;

        // Add event listeners for removal and quantity change
        document.querySelectorAll('.remove-item').forEach(btn => {
            btn.addEventListener('click', (e) => {
                const id = e.currentTarget.dataset.id;
                cart = cart.filter(item => item.id !== id);
                localStorage.setItem('cart', JSON.stringify(cart));
                renderCartItems();
                updateCartUI();
            });
        });

        document.querySelectorAll('.quantity-input').forEach(input => {
            input.addEventListener('change', (e) => {
                const id = e.target.dataset.id;
                const newQty = parseInt(e.target.value);
                if (newQty > 0) {
                    const item = cart.find(item => item.id === id);
                    if (item) item.quantity = newQty;
                    localStorage.setItem('cart', JSON.stringify(cart));
                    renderCartItems();
                    updateCartUI();
                }
            });
        });
    }

    function renderCheckoutSummary() {
        const checkoutList = document.getElementById('checkout-cart-items');
        const totalEl = document.getElementById('checkout-total');

        if (!checkoutList) return;

        checkoutList.innerHTML = '';
        let total = 0;

        cart.forEach(item => {
            const itemTotal = item.price * item.quantity;
            total += itemTotal;

            const li = document.createElement('li');
            li.className = 'list-group-item d-flex justify-content-between lh-sm';
            li.innerHTML = `
                <div>
                    <h6 class="my-0">${item.name}</h6>
                    <small class="text-muted">Quantity: ${item.quantity}</small>
                </div>
                <span class="text-muted">$${itemTotal.toFixed(2)}</span>
            `;
            checkoutList.appendChild(li);
        });

        if (totalEl) totalEl.textContent = `$${total.toFixed(2)}`;
    }

    // Simple Product Detail Page Handler (MVP)
    if (window.location.pathname.includes('product-detail.html')) {
        const urlParams = new URLSearchParams(window.location.search);
        const productId = urlParams.get('id');

        // Mock Product Data
        const products = {
            '1': { name: 'Smartphone X Pro', price: '$999.00', desc: 'The most advanced smartphone for the modern professional.' },
            '2': { name: 'Wireless Headphones', price: '$199.00', desc: 'Crystal clear audio with long-lasting battery life.' },
            '3': { name: 'Smart Watch 5', price: '$299.00', desc: 'Track your fitness and stay connected on the go.' },
            '4': { name: 'Laptop Pro 14', price: '$1299.00', desc: 'High performance laptop for demanding tasks.' }
        };

        if (productId && products[productId]) {
            document.getElementById('product-name').textContent = products[productId].name;
            document.getElementById('product-price').textContent = products[productId].price;
            document.getElementById('product-description').textContent = products[productId].desc;
        }
    }
});
