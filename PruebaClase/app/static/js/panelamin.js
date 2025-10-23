document.addEventListener("DOMContentLoaded", function() {

    
    prompt("DOM loaded - Panel Admin");

    const tareas = [];
    const tareaInput = document.getElementById("tareaInput");
    const agregarBtn = document.getElementById("agregarBtn");
    const listaTareas = document.getElementById("listaTareas");
    const contadorTareas = document.getElementById("contadorTareas");


        // Función para agregar tarea
    function agregarTarea() {
        const tareaInput = document.getElementById("tareaInput");
        
        
        const texto = tareaInput.value.trim();
        if (texto) {
            // Crear objeto tarea con texto y estado de completado
            const nuevaTarea = {
                texto: texto,
                completada: false
            };
            tareas.push(nuevaTarea);
            tareaInput.value = "";
            mostrarTareas();
            guardarTareas();
            console.log(`Tarea agregada: "${texto}"`);
        }
    }

    // Función para marcar todas las tareas como completadas
    function marcarTodasCompletadas() {
        tareas.forEach(tarea => tarea.completada = true);
        mostrarTareas();
        guardarTareas();
    }

    // Función para desmarcar todas las tareas
    function desmarcarTodas() {
        tareas.forEach(tarea => tarea.completada = false);
        mostrarTareas();
        guardarTareas();
    }

    // Función para eliminar tareas completadas
    function eliminarCompletadas() {
        const tareasAntesCount = tareas.length;
        tareas.splice(0, tareas.length, ...tareas.filter(tarea => !tarea.completada));
        const tareasEliminadas = tareasAntesCount - tareas.length;
        
        if (tareasEliminadas > 0) {
            console.log(`${tareasEliminadas} tarea(s) completada(s) eliminada(s)`);
            mostrarTareas();
            guardarTareas();
        }
    }

    // Función para configurar event listeners de las tareas
    function configurarEventListenersTareas() {
        const tareaInput = document.getElementById("tareaInput");
        const agregarBtn = document.getElementById("agregarBtn");
        
        console.log("Configurando event listeners...");
        console.log("tareaInput encontrado:", !!tareaInput);
        console.log("agregarBtn encontrado:", !!agregarBtn);
        
        if (tareaInput && agregarBtn) {
            // Limpiar listeners anteriores si existen
            agregarBtn.replaceWith(agregarBtn.cloneNode(true));
            const nuevoAgregarBtn = document.getElementById("agregarBtn");
            
            // Event listener para el botón
            nuevoAgregarBtn.addEventListener("click", agregarTarea);

            // Event listener para Enter en el input
            tareaInput.addEventListener("keypress", function(e) {
                if (e.key === "Enter") {
                    agregarTarea();
                }
            });
            
            console.log("Event listeners de tareas configurados exitosamente");
        } else {
            console.warn("No se pudieron encontrar los elementos de tareas");
        }
    }


    ////Funcion mostrar tareas 
    function mostrarTareas() {
        const listaTareas = document.getElementById("listaTareas");
        const contadorTareas = document.getElementById("contadorTareas");
        
        if (!listaTareas) {
            console.warn("Elemento listaTareas no encontrado");
            return;
        }
        
        listaTareas.innerHTML = "";
        tareas.forEach(function(tarea, index) {
            const li = document.createElement("li");
            li.className = `flex justify-between items-center p-3 rounded-lg shadow-sm cursor-move transition-all duration-200 hover:shadow-md ${
                tarea.completada 
                    ? 'bg-green-50 border border-green-200' 
                    : 'bg-white border border-gray-200'
            }`;
            
            // ATRIBUTOS PARA DRAG & DROP
            li.draggable = true;
            li.dataset.index = index;
            
            // ICONO DE DRAG
            const dragIcon = document.createElement("span");
            dragIcon.innerHTML = "⋮⋮";
            dragIcon.className = "text-gray-400 text-lg mr-3 cursor-move";
            
            // CHECKBOX PARA MARCAR COMO COMPLETADA
            const checkbox = document.createElement("input");
            checkbox.type = "checkbox";
            checkbox.checked = tarea.completada;
            checkbox.className = "w-4 h-4 text-orange-500 bg-gray-100 border-gray-300 rounded focus:ring-orange-500 focus:ring-2 mr-3";
            checkbox.onchange = function() {
                tarea.completada = this.checked;
                mostrarTareas();
                guardarTareas();
            };
            
            const tareaTexto = document.createElement("span");
            tareaTexto.textContent = tarea.texto;
            tareaTexto.className = `flex-1 ${
                tarea.completada 
                    ? 'text-gray-500 line-through' 
                    : 'text-gray-800'
            }`;
            
            const btnEliminar = document.createElement("button");
            btnEliminar.textContent = "Eliminar";
            btnEliminar.className = "bg-red-500 hover:bg-red-600 text-white px-3 py-1 rounded text-sm transition-colors";
            btnEliminar.onclick = function(){
                tareas.splice(index, 1);
                mostrarTareas();
                guardarTareas();
            };
            
            // ESTRUCTURA: [icono] [checkbox] [texto] [botón]
            li.appendChild(dragIcon);
            li.appendChild(checkbox);
            li.appendChild(tareaTexto);
            li.appendChild(btnEliminar);
            listaTareas.appendChild(li);
        });
        
        // Actualizar contador con tareas completadas y pendientes
        const tareasCompletadas = tareas.filter(tarea => tarea.completada).length;
        const tareasPendientes = tareas.length - tareasCompletadas;
        
        if (contadorTareas) {
            contadorTareas.textContent = 
                `Total: ${tareas.length} | Pendientes: ${tareasPendientes} | Completadas: ${tareasCompletadas}`;
        }

        agregarEventosDragAndDrop();
    }


    ////DRAG Y DROP PARA REORDENAR TAREAS
    let arrastrandoElemento = null;
    let indiceArrastrando = null;

    ///Agregar event listenes a la lista
    function agregarEventosDragAndDrop() {
        const items = listaTareas.querySelectorAll('li[draggable="true"]');

        items.forEach(item => {

            ///EVENTO : cuando emepzamos a arrastrar
            item.addEventListener('dragstart', function(e) {
                arrastrandoElemento = this;
                indiceArrastrando = parseInt(this.dataset.index);

                console.log(`Arrastrando tarea ${indiceArrastrando}: "${tareas[indiceArrastrando].texto}"`);

                ////Estilo visual al arrastrar
                this.style.opacity = '0.5';
                this.style.transform = 'rotate(5deg)';

                ///Guardar datos en el Evento
                e.dataTransfer.effectAllowed = 'move';
                e.dataTransfer.setData('text/html',this.outerHTML);

            });


            //// EVENTO: cuando dejamos de arrastrar
            item.addEventListener('dragend', function(e){
                console.log('Arrastre finalizado');

                //restaurar estilos
                this.style.opacity = '1';
                this.style.transform = 'rotate(0deg)';

                arrastrandoElemento = null;
                indiceArrastrando = null;


            });

            //// EVENTO: cuando un elemento arrastrable entra en el area de otro
            item.addEventListener('dragover', function(e) {

                e.preventDefault(); // Necesario para permitir el drop

                //Estilo visual Hover
                this.style.borderTop = '3px solid #3b82f6'; // azul
                this.style.marginTop = '1px';
            });

            //// EVENTO: cuando un elemento arrastrable sale del area de otro
            item.addEventListener('dragleave', function(e) {
                //restaurar estilos
                this.style.borderTop = '';
                this.style.marginTop = '0';
            });

            //// EVENTO: cuando soltamos el elemento arrastrado
            item.addEventListener('drop', function(e) {
                e.preventDefault();

                if (arrastrandoElemento && arrastrandoElemento !== this) {

                    const targetIndex = parseInt(this.dataset.index);
                    console.log(`Soltando tarea ${indiceArrastrando} sobre tarea ${targetIndex}`);

                    ///reordenar el array
                    reordenarTareas(indiceArrastrando, targetIndex);
                }

                ///limpiar estilos
                this.style.borderTop = '';
                this.style.marginTop = '0';
            });
        });
    }



    function reordenarTareas(fromIndex, toIndex) {
        // Guardar la tarea que estamos moviendo
        const tareaMovida = tareas[fromIndex];
        
        // Remover la tarea de su posición original
        tareas.splice(fromIndex, 1);
        
        // Insertar en la nueva posición
        tareas.splice(toIndex, 0, tareaMovida);
        
        console.log('Array reordenado:', tareas);
        
        // Actualizar la interfaz y guardar
        mostrarTareas();
        guardarTareas();
    }



});