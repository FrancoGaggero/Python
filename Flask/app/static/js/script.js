// Script básico para la aplicación Flask
document.addEventListener('DOMContentLoaded', function() {
    console.log('Flask app cargada correctamente');
    
    // Mensaje de bienvenida simple
    const saludoElement = document.getElementById('saludo');
    if (saludoElement) {
        saludoElement.textContent = '¡Bienvenido a Flask!';
    }
});
