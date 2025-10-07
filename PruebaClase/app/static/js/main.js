// JavaScript simple para index.html
document.addEventListener('DOMContentLoaded', function() {
    
    console.log('Página cargada');
        // Efecto simple para el hero-section
        anime({
            targets: '#hero-section',
            translateY: [-50, 0],
            opacity: [0, 1],
            duration: 1000,
            easing: 'easeOutExpo',
            complete: function() {
                // Llamar a la animación flotante después de que termine la entrada
                floatingText();
            }
        });
        
        // Efecto para las tarjetas
        anime({
            targets: '.nav-card',
            translateY: [30, 0],
            opacity: [0, 1],
            duration: 800,
            delay: anime.stagger(250),
            easing: 'easeOutQuart'
        });
        
        anime({
            targets: '#main-title',
            scale: [0.8, 1],
            opacity: [0, 1],
            duration: 1000,
            easing: 'easeOutQuart'
        })

        ///efecto para los items de servicios al pasar el mouse
        const items = document.querySelectorAll('.item');
        items.forEach(item => {
            item.addEventListener('mouseenter', () => {
                anime({
                    targets: item,
                    scale: 1.1,
                    duration: 300,
                    easing: 'easeOutQuart'
                });
            });
            item.addEventListener('mouseleave', () => {
                anime({
                    targets: item,
                    scale: 1.0,
                    duration: 300,
                    easing: 'easeOutQuart'
                });
            });
        });
        
    
    
    
    
    // Función de animación flotante
    function floatingText() {
        anime({
            targets: '#hero-section h2, #hero-section p',
            translateY: [0, -10, 0],
            duration: 3000,
            easing: 'easeInOutSine',
            loop: true,
            direction: 'alternate'
        });
    }
    
});











