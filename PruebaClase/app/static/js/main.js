// JavaScript simple para index.html
document.addEventListener('DOMContentLoaded', function() {
    
    console.log('Página cargada');
           
    // Efecto para las tarjetas
    anime({
        targets: '.nav-card',
        translateY: [30, 0],
        opacity: [0, 1],
        duration: 800,
        delay: anime.stagger(250),
        easing: 'easeOutQuart'
    });
    
    // Efecto para el título principal
    anime({
        targets: '#main-title',
        scale: [0.8, 1],
        opacity: [0, 1],
        duration: 1000,
        easing: 'easeOutQuart'
    });

    // Efecto para el hero section
    anime({
        targets: '#hero-section',
        opacity: [0, 1],
        translateY: [-50, 0],
        duration: 1200,
        easing: 'easeOutCubic',
        delay: 300
    });

    // Efecto para los items de servicios al pasar el mouse
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

    // Efecto para elemento con ID 'first' (si existe)
    const firstElement = document.getElementById('first');
    if (firstElement) {
        // Crear efecto de texto animado letra por letra
        const text = firstElement.textContent;
        firstElement.innerHTML = '';
        
        // Dividir el texto en spans individuales para cada letra
        for (let i = 0; i < text.length; i++) {
            const span = document.createElement('span');
            span.textContent = text[i] === ' ' ? '\u00A0' : text[i]; // Preservar espacios
            span.style.display = 'inline-block';
            span.style.opacity = '0';
            firstElement.appendChild(span);
        }
        
        // Animar cada letra
        anime({
            targets: '#first span',
            opacity: [0, 1],
            y: [ { to: '-2.75rem', ease: 'outExpo', duration: 400 },
            { to: 0, ease: 'outBounce', duration: 300, delay: 100 },
            ],  
            rotateZ: [-180, 1],
            duration: 250,
            delay: anime.stagger(80),
            easing: 'easeOutElastic(1, .8)',
            loop: true,
            direction: 'alternate',
            loopDelay: 1000
        });
    }
});