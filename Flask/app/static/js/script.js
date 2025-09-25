// Script básico para la aplicación Flask
// Se ejecuta cuando el DOM está completamente cargado

document.addEventListener('DOMContentLoaded', function() {
    // Obtener nombre para saludo por prompt
    let nombre = prompt("Por favor, ingresa tu nombre:");
    if (!nombre) {
        nombre = "Invitado";
    }
    let mensaje = `¡Bienvenido a Flask, ${nombre}!`;
    document.getElementById("saludo").textContent = mensaje;


    localStorage.setItem('usuario', nombre);
    document.getElementById("saludo").textContent = `¡Bienvenido de nuevo, ${nombre}!`;


    // Evento para el botón "En desarrollo"
    document.getElementById("noBtn").addEventListener("click", function(){
        // Quitar cualquier animación previa
        this.classList.remove("animate-shake");
        
        // Forzar el reflow para que la eliminación de clase tome efecto
        void this.offsetWidth;

        this.classList.add("animate-shake");
        //limpiar clase 
        setTimeout(() => {
            this.classList.remove("animate-shake");
        }, 600); // 600ms coincide con la duración de la animación CSS
    });

    // Array de fondos para el botón de cambiar color
    const fondos = [
        "bg-red-500",
        "bg-blue-500",
        "bg-green-500",
        "bg-yellow-400",
        "bg-purple-500",
        "bg-pink-500",
        "bg-indigo-500",
        "bg-teal-500",
        "bg-orange-500",
        "bg-cyan-500",
        "bg-lime-500",
        "bg-rose-500",
        "bg-violet-500",
        "bg-fuchsia-500",
        "bg-emerald-500",
        "bg-black-500",
        "#ffffff",
        "#000000"
    ];

    // Evento para el botón cambiando el color de fondo del saludo
    document.getElementById("colorBtn").addEventListener("click", function(){
        const saludo = document.getElementById("saludo");
        // Quita las clases de gradiente originales si están presentes
        saludo.classList.remove("bg-gradient-to-r", "from-blue-500", "to-purple-600");
        // Quita cualquier fondo sólido anterior
        fondos.forEach(fondo => saludo.classList.remove(fondo));
        // Elige una clase aleatoria
        const fondoAleatorio = fondos[Math.floor(Math.random() * fondos.length)];
        saludo.classList.add(fondoAleatorio);
    });

    console.log('Flask app cargada correctamente');
});
