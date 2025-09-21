/**
 * Main JavaScript file for Flask Login Application
 * Contains all interactive functionality for the login form
 */

// Wait for DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    initializeAnimations();
    initializeFormValidation();
    initializeMessageSystem();
    console.log('Login form initialized successfully');
});

/**
 * Toggle password visibility in the password input field
 */
function togglePassword() {
    const passwordInput = document.getElementById('password');
    const eyeIcon = document.getElementById('eye-icon');
    
    if (!passwordInput || !eyeIcon) {
        console.error('Password input or eye icon not found');
        return;
    }
    
    if (passwordInput.type === 'password') {
        passwordInput.type = 'text';
        eyeIcon.innerHTML = `
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13.875 18.825A10.05 10.05 0 0112 19c-4.478 0-8.268-2.943-9.543-7a9.97 9.97 0 011.563-3.029m5.858.908a3 3 0 114.243 4.243M9.878 9.878l4.242 4.242M9.878 9.878L8.464 8.464M21.536 21.536L2.464 2.464"></path>
        `;
    } else {
        passwordInput.type = 'password';
        eyeIcon.innerHTML = `
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path>
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"></path>
        `;
    }
}

/**
 * Initialize CSS animations by injecting styles into the document head
 */
function initializeAnimations() {
    const animationStyles = `
        <style>
            @keyframes fadeIn {
                from { 
                    opacity: 0; 
                    transform: translateY(-10px); 
                }
                to { 
                    opacity: 1; 
                    transform: translateY(0); 
                }
            }
            
            @keyframes slideUp {
                from { 
                    opacity: 0; 
                    transform: translateY(20px); 
                }
                to { 
                    opacity: 1; 
                    transform: translateY(0); 
                }
            }
            
            .animate-fade-in {
                animation: fadeIn 0.5s ease-in-out;
            }
            
            .animate-slide-up {
                animation: slideUp 0.5s ease-out;
            }
            
            /* Smooth transitions for form elements */
            .form-input {
                transition: all 0.2s ease-in-out;
            }
            
            .form-input:focus {
                transform: translateY(-1px);
                box-shadow: 0 4px 12px rgba(59, 130, 246, 0.15);
            }
            
            /* Button hover effects */
            .btn-primary {
                transition: all 0.2s ease-in-out;
            }
            
            .btn-primary:hover {
                transform: translateY(-1px);
                box-shadow: 0 8px 25px rgba(59, 130, 246, 0.3);
            }
        </style>
    `;
    
    document.head.insertAdjacentHTML('beforeend', animationStyles);
}

/**
 * Initialize form validation and enhancement
 */
function initializeFormValidation() {
    const form = document.querySelector('form');
    const emailInput = document.getElementById('email');
    const passwordInput = document.getElementById('password');
    
    if (!form) return;
    
    // Add form classes for styling
    if (emailInput) {
        emailInput.classList.add('form-input');
    }
    
    if (passwordInput) {
        passwordInput.classList.add('form-input');
    }
    
    // Add form submission handler
    form.addEventListener('submit', function(e) {
        if (!validateForm()) {
            e.preventDefault();
            return false;
        }
        
        // Show loading state
        showLoadingState();
    });
    
    // Add real-time validation
    if (emailInput) {
        emailInput.addEventListener('blur', validateEmail);
        emailInput.addEventListener('input', clearEmailError);
    }
    
    if (passwordInput) {
        passwordInput.addEventListener('blur', validatePassword);
        passwordInput.addEventListener('input', clearPasswordError);
    }
}

/**
 * Validate the entire form
 */
function validateForm() {
    const isEmailValid = validateEmail();
    const isPasswordValid = validatePassword();
    
    return isEmailValid && isPasswordValid;
}

/**
 * Validate email field
 */
function validateEmail() {
    const emailInput = document.getElementById('email');
    if (!emailInput) return true;
    
    const email = emailInput.value.trim();
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    
    if (!email) {
        showFieldError(emailInput, 'El correo electrónico es obligatorio');
        return false;
    }
    
    if (!emailRegex.test(email)) {
        showFieldError(emailInput, 'Por favor ingresa un correo electrónico válido');
        return false;
    }
    
    clearFieldError(emailInput);
    return true;
}

/**
 * Validate password field
 */
function validatePassword() {
    const passwordInput = document.getElementById('password');
    if (!passwordInput) return true;
    
    const password = passwordInput.value;
    
    if (!password) {
        showFieldError(passwordInput, 'La contraseña es obligatoria');
        return false;
    }
    
    if (password.length < 6) {
        showFieldError(passwordInput, 'La contraseña debe tener al menos 6 caracteres');
        return false;
    }
    
    clearFieldError(passwordInput);
    return true;
}

/**
 * Show error message for a specific field
 */
function showFieldError(input, message) {
    clearFieldError(input);
    
    input.classList.add('border-red-500', 'focus:ring-red-500', 'focus:border-red-500');
    input.classList.remove('border-gray-300', 'focus:ring-blue-500', 'focus:border-blue-500');
    
    const errorDiv = document.createElement('div');
    errorDiv.className = 'mt-1 text-sm text-red-600 field-error';
    errorDiv.textContent = message;
    
    input.parentNode.appendChild(errorDiv);
}

/**
 * Clear error message for a specific field
 */
function clearFieldError(input) {
    input.classList.remove('border-red-500', 'focus:ring-red-500', 'focus:border-red-500');
    input.classList.add('border-gray-300', 'focus:ring-blue-500', 'focus:border-blue-500');
    
    const existingError = input.parentNode.querySelector('.field-error');
    if (existingError) {
        existingError.remove();
    }
}

/**
 * Clear email error on input
 */
function clearEmailError() {
    const emailInput = document.getElementById('email');
    if (emailInput) {
        clearFieldError(emailInput);
    }
}

/**
 * Clear password error on input
 */
function clearPasswordError() {
    const passwordInput = document.getElementById('password');
    if (passwordInput) {
        clearFieldError(passwordInput);
    }
}

/**
 * Show loading state on form submission
 */
function showLoadingState() {
    const submitButton = document.querySelector('button[type="submit"]');
    if (!submitButton) return;
    
    const originalText = submitButton.innerHTML;
    
    submitButton.disabled = true;
    submitButton.innerHTML = `
        <svg class="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
            <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
            <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
        </svg>
        Iniciando sesión...
    `;
    
    // Reset button after 5 seconds (fallback)
    setTimeout(() => {
        if (submitButton.disabled) {
            submitButton.disabled = false;
            submitButton.innerHTML = originalText;
        }
    }, 5000);
}

/**
 * Initialize message system for displaying notifications
 */
function initializeMessageSystem() {
    // This function can be expanded to handle dynamic messages
    // For now, it's prepared for future Flask integration
}

/**
 * Show a message to the user
 * @param {string} message - The message to display
 * @param {string} type - The type of message ('success', 'error', 'info')
 */
function showMessage(message, type = 'info') {
    const messageArea = document.getElementById('message-area');
    const messageText = document.getElementById('message-text');
    
    if (!messageArea || !messageText) {
        console.warn('Message area not found');
        return;
    }
    
    // Clear existing classes
    messageArea.className = 'mb-4 p-4 rounded-lg';
    
    // Add appropriate classes based on type
    switch (type) {
        case 'success':
            messageArea.classList.add('bg-green-100', 'border', 'border-green-400', 'text-green-700');
            break;
        case 'error':
            messageArea.classList.add('bg-red-100', 'border', 'border-red-400', 'text-red-700');
            break;
        default:
            messageArea.classList.add('bg-blue-100', 'border', 'border-blue-400', 'text-blue-700');
    }
    
    messageText.textContent = message;
    messageArea.classList.remove('hidden');
    
    // Auto-hide after 5 seconds
    setTimeout(() => {
        hideMessage();
    }, 5000);
}

/**
 * Hide the message area
 */
function hideMessage() {
    const messageArea = document.getElementById('message-area');
    if (messageArea) {
        messageArea.classList.add('hidden');
    }
}

// Make functions available globally
window.togglePassword = togglePassword;
window.showMessage = showMessage;
window.hideMessage = hideMessage;