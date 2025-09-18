
#Desafio semana 4


# validaciones de datos 
#validar input no vacio
def validar_dato(mensaje):
    while mensaje == "":
        mensaje = input("Vuelve a ingresar el mensaje: ")
    return mensaje

#validar numero positivo
def validar_numero_positivo(numero):
    while numero <= 0 or not isinstance(numero, int):
        print("El número debe ser positivo. Intenta de nuevo.")
        numero = int(input("Ingresa un número positivo: "))
    return numero

# String to lower
def to_lower(texto):
    return texto.lower()

# Precio positivo y no vacío
def validar_precio(mensaje="Ingresa el precio del producto: $"):

    while True:
        entrada = input(mensaje).strip()  #elimina espacios en blanco
        
        # Verificar si está vacío
        if entrada == "":
            print("Error: El precio no puede estar vacío. Debes ingresar un valor.")
            continue
            
        # Verificar si es un número válido
        try:
            precio = float(entrada)  # Acepta decimales y enteros
        except ValueError:
            print("Error: Debes ingresar un número válido (ejemplo: 150 o 150.50).")
            continue
            
        # Verificar si es positivo
        if precio <= 0:
            print("Error: El precio debe ser mayor que 0.")
            continue
            
        return precio

# Función para validar nombre de producto (no vacío)
def validar_nombre_producto(mensaje="Ingresa el nombre del producto: "):

    while True:
        entrada = input(mensaje).strip()
        
        if entrada == "":
            print("Error: El nombre del producto no puede estar vacío.")
            continue
            
        return entrada.lower()  # Devuelve en minúsculas




#(ya se que la consigna pedia listas pero queria probar como quedaba con diccionarios :D)
#Diccionario de productos con sus precios
productos = {"calzado": 1500, "remera": 800, "pantalon": 1200, "bolso": 2000, "gorra": 500, "paleta": 300, "pelotas": 400, "mochila": 2500}

# Funciones del menu
def agregar_producto(producto, precio):
    productos[producto] = precio
    print(f"Producto {producto} agregado a la lista con un precio de {precio}.")

def eliminar_producto(producto):
    if producto.lower() in productos:
        del productos[producto.lower()]
        print(f"producto {producto} eliminado de la lista.")
    else:
        print(f"El producto {producto} no se encuentra en la lista.")

def mostrar_productos():
    print("Productos en la lista:")
    for producto, precio in productos.items():
        print(f"- {producto}: ${precio}")

def valor_inventario():
    total = sum(productos.values())
    print(f"El valor total del inventario es: ${total}")    

def mostrar_menu():
    print("\n" + "="*40)
    print("         MENÚ PRINCIPAL")
    print("="*40)
    print("1. Agregar producto")
    print("2. Eliminar producto") 
    print("3. Mostrar productos")
    print("4. Valor del inventario")
    print("5. Salir")
    print("="*40)




#############################
# Bucle principal del menu
while True:
    mostrar_menu()
    
    # Obtener opcion del usuario con validación
    try:
        menuPrincipal = int(input("Elige una opción (1-5): "))
        validar_numero_positivo(menuPrincipal)
    except ValueError:
        print("Por favor, ingresa un número válido.")
        continue
    
    # Validar que la opción esté en el rango correcto
    if menuPrincipal < 1 or menuPrincipal > 5:
        print("Opción inválida. Por favor, elige una opción entre 1 y 5.")
        continue
    
    # Procesar la opción seleccionada en menuPrincipal
    match menuPrincipal:
        case 1:
            print("\n--- AGREGAR PRODUCTO ---")
            
            nuevoProducto = validar_nombre_producto("Ingresa el nombre del producto a agregar: ")
            
            
            nuevoPrecio = validar_precio("Ingresa el precio del producto: $")
            
            agregar_producto(nuevoProducto, nuevoPrecio)
            
        case 2:
            print("\n--- ELIMINAR PRODUCTO ---")

            productoEliminar = validar_nombre_producto(f"Ingresa el nombre del producto a eliminar: {list(productos.keys())}")
            eliminar_producto(productoEliminar)
            
        case 3:
            print("\n--- PRODUCTOS DISPONIBLES ---")
            mostrar_productos()
            
        case 4:
            print("\n--- VALOR DEL INVENTARIO ---")
            valor_inventario()
            
        case 5:
            print("\n¡Gracias por usar el sistema! Saliendo del programa...")
            break  
    
    #Mensaje para poder leer mensaje 
    if menuPrincipal != 5:
        input("\nPresiona Enter para continuar...")