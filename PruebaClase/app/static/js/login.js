/**
 * CleanSA Login Page Animations
 * Utilizando Anime.js para crear animaciones fluidas y profesionales
 */

// Configuracion de animaciones
const animationConfig = {
    duration: 800,
    easing: 'easeOutElastic(1, .8)',
    delay: function(el, i) { return i * 100; }
};

// Inicializacion cuando el DOM este listo
document.addEventListener('DOMContentLoaded', function() {
    initializeAnimations();
    setupInteractions();
    setupFormValidation();
});

/**
 * Inicializa todas las animaciones de entrada
 */
function initializeAnimations() {
    // Ocultar elementos inicialmente
    hideInitialElements();
    
    // Secuencia de animaciones de entrada
    setTimeout(() => animateHeader(), 200);
    setTimeout(() => animateForm(), 600);
    setTimeout(() => animateFooter(), 1000);
    setTimeout(() => animateBackground(), 1200);
}

/**
 * Oculta elementos para la animacion inicial
 */
function hideInitialElements() {
    const elements = [
        '#login-header',
        '#login-form',
        '#footer-info',
        '.floating-element'
    ];
    
    elements.forEach(selector => {
        const el = document.querySelector(selector);
        if (el) {
            el.style.opacity = '0';
            el.style.transform = 'translateY(30px)';
        }
    });
    
    // Ocultar campos del formulario individualmente
    const formFields = document.querySelectorAll('.form-field');
    formFields.forEach(field => {
        field.style.opacity = '0';
        field.style.transform = 'translateX(-20px)';
    });
}

/**
 * Anima el header con el logo
 */
function animateHeader() {
    // Animacion del logo
    anime({
        targets: '#logo-icon',
        scale: [0, 1],
        rotate: [0, 360],
        duration: 1000,
        easing: 'easeOutElastic(1, .8)',
        complete: function() {
            // Efecto de pulsacion sutil
            anime({
                targets: '#logo-icon',
                scale: [1, 1.05, 1],
                duration: 2000,
                loop: true,
                direction: 'alternate',
                easing: 'easeInOutSine'
            });
        }
    });
    
    // Animacion del header completo
    anime({
        targets: '#login-header',
        opacity: [0, 1],
        translateY: [30, 0],
        duration: 800,
        easing: 'easeOutCubic'
    });
    
    // Animacion del titulo
    anime({
        targets: '#logo-title',
        opacity: [0, 1],
        translateY: [20, 0],
        duration: 800,
        delay: 200,
        easing: 'easeOutCubic'
    });
    
    // Animacion del subtitulo
    anime({
        targets: '#logo-subtitle',
        opacity: [0, 1],
        translateY: [20, 0],
        duration: 800,
        delay: 400,
        easing: 'easeOutCubic'
    });
}
