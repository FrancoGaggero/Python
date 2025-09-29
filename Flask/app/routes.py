from flask import Blueprint, render_template, request
from .calculadora_logic import calcular
from .horoscopo_logic import obtener_signo, validar_fecha, formatear_informacion_signo

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/horoscopo', methods=['GET', 'POST'])





def horoscopo():
    
    resultado = None
    error = None
    fecha_nacimiento = ""

    if request.method == 'POST':
        fecha_nacimiento = request.form.get('fecha_nacimiento', '')
        print(f"DEBUG: Fecha recibida: '{fecha_nacimiento}'")
        
        if fecha_nacimiento:
            # Validar la fechaa
            es_valida, fecha_obj, mensaje_error = validar_fecha(fecha_nacimiento)
            print(f"DEBUG: Validación - es_valida: {es_valida}, error: {mensaje_error}")
            
            if es_valida:
                # traigo el signo
                signo_info = obtener_signo(fecha_nacimiento)
                print(f"DEBUG: Signo obtenido: {signo_info}")
                if signo_info:
                    resultado = formatear_informacion_signo(signo_info)
                    print(f"DEBUG: Resultado formateado: {resultado}")
                else:
                    error = "No se pudo determinar el signo zodiacal"
            else:
                error = mensaje_error
        else:
            error = "Por favor ingrese una fecha"

    return render_template('horoscopo.html', 
                         horoscopo=resultado, 
                         error=error, 
                         fecha_nacimiento=fecha_nacimiento)


@main.route('/calculadora', methods=['GET', 'POST'])
def calculadora():
    
    resultado = None
    numero1 = ""
    numero2 = ""
    error = None
    operacion = "suma"  # por defecto
    simbolo = "+"
    
    if request.method == 'POST':
        # Obtener datos de formulario
        numero1 = request.form.get('numero1', '')
        numero2 = request.form.get('numero2', '')
        operacion = request.form.get('operacion', 'suma')
        
        # Usar la lógica oopr separado
        resultado, error, simbolo = calcular(numero1, numero2, operacion)
    
    return render_template('calculadora.html', 
                         resultado=resultado, 
                         numero1=numero1, 
                         numero2=numero2,
                         error=error,
                         operacion=operacion,
                         simbolo=simbolo)