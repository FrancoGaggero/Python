
// Manejo del modal de productos en el panel de administración
document.addEventListener('DOMContentLoaded', function() {
    const modal = document.getElementById('productoModal');
    const openModalBtn = document.getElementById('openModalBtn');
    const closeModalBtn = document.getElementById('closeModalBtn');
    const cancelModalBtn = document.getElementById('cancelModalBtn');

    // Función para abrir el modal
    function openModal() {
        modal.classList.remove('hidden');
        // Hacer focus en el primer input cuando se abre el modal
        const firstInput = modal.querySelector('input[type="text"]');
        if (firstInput) {
            setTimeout(() => firstInput.focus(), 100);
        }
    }

    // Función para cerrar el modal
    function closeModal() {
        modal.classList.add('hidden');
        // Limpiar el formulario al cerrar
        const form = modal.querySelector('form');
        if (form) {
            form.reset();
        }
    }

    // Event listeners
    if (openModalBtn) {
        openModalBtn.addEventListener('click', openModal);
    }

    if (closeModalBtn) {
        closeModalBtn.addEventListener('click', closeModal);
    }

    if (cancelModalBtn) {
        cancelModalBtn.addEventListener('click', closeModal);
    }

    // Cerrar modal al hacer clic fuera de él
    modal.addEventListener('click', function(e) {
        if (e.target === modal) {
            closeModal();
        }
    });

    // Cerrar modal con la tecla Escape
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && !modal.classList.contains('hidden')) {
            closeModal();
        }
    });

    // Manejo del formulario
    const form = modal.querySelector('form');
    if (form) {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
           
            
            // Por ahora solo cerramos el modal
            closeModal();
            
            // Mostrar mensaje de éxito (temporal)
            alert('Producto guardado correctamente');
        });
    }
});