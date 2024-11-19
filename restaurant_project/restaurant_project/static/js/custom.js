// Form Validation
document.addEventListener('DOMContentLoaded', function() {
    const forms = document.querySelectorAll('.needs-validation');

    Array.from(forms).forEach(form => {
        form.addEventListener('submit', event => {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        }, false);
    });

    // Initialize all tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Initialize all popovers
    const popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    popoverTriggerList.map(function (popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl);
    });
});

// Reservation Date Validation
function validateReservationDate() {
    const dateInput = document.getElementById('reservation-date');
    const today = new Date();
    const selectedDate = new Date(dateInput.value);
    
    if (selectedDate < today) {
        dateInput.setCustomValidity('Lütfen gelecek bir tarih seçin');
    } else {
        dateInput.setCustomValidity('');
    }
}

// Cart Functions
const cart = {
    items: [],
    
    addItem(item) {
        this.items.push(item);
        this.updateCartUI();
        this.saveCart();
    },
    
    removeItem(itemId) {
        this.items = this.items.filter(item => item.id !== itemId);
        this.updateCartUI();
        this.saveCart();
    },
    
    updateCartUI() {
        const cartCount = document.getElementById('cart-count');
        if (cartCount) {
            cartCount.textContent = this.items.length;
        }
    },
    
    saveCart() {
        localStorage.setItem('cart', JSON.stringify(this.items));
    },
    
    loadCart() {
        const savedCart = localStorage.getItem('cart');
        if (savedCart) {
            this.items = JSON.parse(savedCart);
            this.updateCartUI();
        }
    }
};

// Load cart on page load
cart.loadCart();

// Ajax Form Submission
function submitFormAjax(formId, successCallback) {
    const form = document.getElementById(formId);
    if (!form) return;

    form.addEventListener('submit', function(e) {
        e.preventDefault();

        const formData = new FormData(form);
        const data = Object.fromEntries(formData);

        fetch(form.action, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(data => {
            if (successCallback) {
                successCallback(data);
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Bir hata oluştu. Lütfen tekrar deneyin.');
        });
    });
}