"""
Módulo de operaciones matemáticas
Contiene la lógica de cálculos separada de las rutas
"""

def sumar(numero1, numero2):
    """
    Suma dos números
    Args:
        numero1 (str): Primer número como string
        numero2 (str): Segundo número como string
    Returns:
        tuple: (resultado, error)
    """
    try:
        num1 = float(numero1)
        num2 = float(numero2)
        resultado = num1 + num2
        return resultado, None
    except ValueError:
        return None, "Por favor ingresa números válidos"

def restar(numero1, numero2):
    """Resta dos números"""
    try:
        num1 = float(numero1)
        num2 = float(numero2)
        resultado = num1 - num2
        return resultado, None
    except ValueError:
        return None, "Por favor ingresa números válidos"

def multiplicar(numero1, numero2):
    """Multiplica dos números"""
    try:
        num1 = float(numero1)
        num2 = float(numero2)
        resultado = num1 * num2
        return resultado, None
    except ValueError:
        return None, "Por favor ingresa números válidos"

def dividir(numero1, numero2):
    """Divide dos números"""
    try:
        num1 = float(numero1)
        num2 = float(numero2)
        
        if num2 == 0:
            return None, "No se puede dividir por cero"
            
        resultado = num1 / num2
        return resultado, None
    except ValueError:
        return None, "Por favor ingresa números válidos"

def calcular(numero1, numero2, operacion):
    """
    Función principal que maneja todas las operaciones
    Args:
        numero1 (str): Primer número
        numero2 (str): Segundo número  
        operacion (str): Tipo de operación ('suma', 'resta', 'multiplicacion', 'division')
    Returns:
        tuple: (resultado, error, simbolo)
    """
    operaciones = {
        'suma': (sumar, '+'),
        'resta': (restar, '-'),
        'multiplicacion': (multiplicar, '×'),
        'division': (dividir, '÷')
    }
    
    if operacion not in operaciones:
        return None, "Operación no válida", None
    
    funcion, simbolo = operaciones[operacion]
    resultado, error = funcion(numero1, numero2)
    
    return resultado, error, simbolo