cuenta = __import__('cuenta').cuenta


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


#ingresar nombre titrular
nombre = input("Ingrese el nombre del titular de la cuenta: ")
validar_dato(nombre)  # Validar que el nombre no esté vacío

usuario = cuenta(nombre,0)






def mostrar_menu():
    print("\n" + "="*40)
    print("         MENÚ PRINCIPAL")
    print("="*40)
    print("1. Ver Saldo")
    print("2. Depositar")
    print("3. Retirar")
    print("4. Ver movimientos")
    print("5. Salir")
    print("="*40)





while True:
    mostrar_menu()
    try:    
        opcion = int(input(f"Hola {nombre} Selecciona una opción (1-5): "))
        validar_numero_positivo(opcion)
    except ValueError:
        print("Por favor, ingresa un número válido.")
        continue
    if opcion < 1 or opcion > 5:
        print("Opción inválida. Por favor, elige una opción entre 1 y 5.")
        continue
        
    match opcion:
        case 1:
            usuario.verMonto()

        case 2:
            usuario.depositar(int(input("Ingrese el monto a depositar: $")))

        case 3:
            usuario.retirar(int(input("Ingrese el monto a retirar: $")))   
        case 4:
            usuario.verMovimientos()
        case 5:
            print("Saliendo del programa. ¡Hasta luego!")
            break

    if opcion != 4:
        input("Presiona Enter para continuar...")