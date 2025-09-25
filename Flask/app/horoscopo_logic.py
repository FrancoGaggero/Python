

from datetime import datetime


#Lista de diccionarios
SIGNOS_ZODIACALES = [
    {
        "nombre": "Aries",
        "inicio": (3, 21),  # 21 de marzo
        "fin": (4, 19),     # 19 de abril
        "elemento": "Fuego",
        "emoji": "♈",
        "descripcion": "Enérgico, valiente y pionero"
    },
    {
        "nombre": "Tauro",
        "inicio": (4, 20),  # 20 de abril
        "fin": (5, 20),     # 20 de mayo
        "elemento": "Tierra",
        "emoji": "♉",
        "descripcion": "Práctico, confiable y determinado"
    },
    {
        "nombre": "Géminis",
        "inicio": (5, 21),  # 21 de mayo
        "fin": (6, 20),     # 20 de junio
        "elemento": "Aire",
        "emoji": "♊",
        "descripcion": "Comunicativo, adaptable y curioso"
    },
    {
        "nombre": "Cáncer",
        "inicio": (6, 21),  # 21 de junio
        "fin": (7, 22),     # 22 de julio
        "elemento": "Agua",
        "emoji": "♋",
        "descripcion": "Emocional, intuitivo y protector"
    },
    {
        "nombre": "Leo",
        "inicio": (7, 23),  # 23 de julio
        "fin": (8, 22),     # 22 de agosto
        "elemento": "Fuego",
        "emoji": "♌",
        "descripcion": "Creativo, generoso y líder natural"
    },
    {
        "nombre": "Virgo",
        "inicio": (8, 23),  # 23 de agosto
        "fin": (9, 22),     # 22 de septiembre
        "elemento": "Tierra",
        "emoji": "♍",
        "descripcion": "Analítico, perfeccionista y servicial"
    },
    {
        "nombre": "Libra",
        "inicio": (9, 23),  # 23 de septiembre
        "fin": (10, 22),    # 22 de octubre
        "elemento": "Aire",
        "emoji": "♎",
        "descripcion": "Equilibrado, diplomático y justo"
    },
    {
        "nombre": "Escorpio",
        "inicio": (10, 23), # 23 de octubre
        "fin": (11, 21),    # 21 de noviembre
        "elemento": "Agua",
        "emoji": "♏",
        "descripcion": "Intenso, misterioso y transformador"
    },
    {
        "nombre": "Sagitario",
        "inicio": (11, 22), # 22 de noviembre
        "fin": (12, 21),    # 21 de diciembre
        "elemento": "Fuego",
        "emoji": "♐",
        "descripcion": "Aventurero, optimista y filosófico"
    },
    {
        "nombre": "Capricornio",
        "inicio": (12, 22), # 22 de diciembre
        "fin": (1, 19),     # 19 de enero
        "elemento": "Tierra",
        "emoji": "♑",
        "descripcion": "Ambicioso, disciplinado y responsable"
    },
    {
        "nombre": "Acuario",
        "inicio": (1, 20),  # 20 de enero
        "fin": (2, 18),     # 18 de febrero
        "elemento": "Aire",
        "emoji": "♒",
        "descripcion": "Innovador, independiente y humanitario"
    },
    {
        "nombre": "Piscis",
        "inicio": (2, 19),  # 19 de febrero
        "fin": (3, 20),     # 20 de marzo
        "elemento": "Agua",
        "emoji": "♓",
        "descripcion": "Intuitivo, compasivo y artístico"
    }
]

# TODO: Implementar estas funciones (¡TU TURNO!)

def obtener_signo(fecha_nacimiento):

    try:
        
        # Convertir string a datetime
        fecha = datetime.strptime(fecha_nacimiento, '%Y-%m-%d')
        mes = fecha.month
        dia = fecha.day
        
        
        # Buscar el signo correspondiente
        for signo in SIGNOS_ZODIACALES:
            inicio_mes, inicio_dia = signo['inicio']
            fin_mes, fin_dia = signo['fin']
            
            
            
            # Caso especial para Capricornio (cruza el año)
            if inicio_mes > fin_mes:  # Capricornio: diciembre a enero
                if (mes == inicio_mes and dia >= inicio_dia) or (mes == fin_mes and dia <= fin_dia):
                    
                    return signo
            else:
                # Casos normales
                if mes == inicio_mes and mes == fin_mes:
                    # Mismo mes
                    if inicio_dia <= dia <= fin_dia:
                        
                        return signo
                elif mes == inicio_mes and dia >= inicio_dia:
                    # Mes de inicio
                    
                    return signo
                elif mes == fin_mes and dia <= fin_dia:
                    # Mes de fin
                    
                    return signo
        
        print("DEBUG: No se encontró signo")
        return None
        
    except ValueError as e:
        print(f"DEBUG: Error de formato: {e}")
        return None

def validar_fecha(fecha_string):
    
    try:
        fecha = datetime.strptime(fecha_string, '%Y-%m-%d')
        
        # Verificar que no sea fecha futura
        if fecha > datetime.now():
            return (False, None, "La fecha no puede ser futura")
            
        # Verificar que sea una fecha razonable (no muy antigua)
        if fecha.year < 1900:
            return (False, None, "La fecha es demasiado antigua")
            
        return (True, fecha, None)
        
    except ValueError:
        return (False, None, "Formato de fecha inválido. Use YYYY-MM-DD")

def formatear_informacion_signo(signo_info):

    if not signo_info:
        return "No se pudo determinar el signo zodiacal"
        
    return f"{signo_info['emoji']} {signo_info['nombre']} - Elemento: {signo_info['elemento']} - {signo_info['descripcion']}"

# Función de ayuda para debuggear (ya implementada)
def mostrar_todos_los_signos():
    """Función para ver todos los signos - útil para debugging"""
    for signo in SIGNOS_ZODIACALES:
        print(f"{signo['emoji']} {signo['nombre']} ({signo['elemento']}) - {signo['inicio']} a {signo['fin']}")

# Test básico (descomenta para probar)
if __name__ == "__main__":
    print("🔮 Horóscopo Logic - Testing")
    print("=" * 40)
    mostrar_todos_los_signos()
