# POO 

#IMportar la clase estudiante
Estudiante = __import__('Estudiante').Estudiante


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

# Crear una instancia de la clase Estudiante
#estudiante1 = Estudiante("Franco", 23)

def mostrarEstudiante(estudiante):
    print("Nombre:", estudiante.get_nombre())
    print("Edad:", estudiante.get_edad())



def mostrar_menu():
    print("\n" + "="*40)
    print("         MENÚ PRINCIPAL")
    print("="*40)
    print("1. Ingresar Estudiante")
    print("2. Ver estudiante") 
    print("3. Salir")
    print("="*40)

# Mostrar el menú principal
while True:
    mostrar_menu()
    try:    
        opcion = int(input("Selecciona una opción (1-3): "))
        validar_numero_positivo(opcion)
    except ValueError:
        print("Por favor, ingresa un número válido.")
        continue
    if opcion < 1 or opcion > 3:
        print("Opción inválida. Por favor, elige una opción entre 1 y 3.")
        continue
        
    match opcion:
        case 1 :
            nombre = input("Ingrese el nombre del estudiante: ")
            validar_dato(nombre)  # Validar que el nombre no esté vacío

            edad = int(input("Ingrese la edad del estudiante: "))
            validar_numero_positivo(edad)

            estudiante1 = Estudiante(nombre, edad)
        case 2 :
            print("\n--- Datos del Estudiante ---")
            try:
                mostrarEstudiante(estudiante1)
            except NameError:
                print("No se ha ingresado ningún estudiante aún. Por favor, ingresa un estudiante primero.")

        case 3 :
            print("Saliendo del programa...")
            break


    
    









