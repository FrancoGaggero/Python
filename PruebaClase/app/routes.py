"""
CleanSA - Sistema de Gestión
Rutas principales para la aplicación de productos higiénicos
"""

from flask import Blueprint, render_template, request, redirect, url_for

# ===================================
# DATOS DE EJEMPLO (SIN BASE DE DATOS)
# ===================================

NOMBRE_USUARIO = "Franco"
ALUMNOS_EJEMPLO = [
    {"nombre": "Juan", "edad": 20},
    {"nombre": "Ana", "edad": 22},
    {"nombre": "Luis", "edad": 19},
    {"nombre": "Franco", "edad": 23}
]
USUARIOS_EJEMPLO = ["Juan", "Ana", "Luis", "Franco"]

# ===================================
# BLUEPRINT PRINCIPAL
# ===================================

main = Blueprint('main', __name__)

# ===================================
# RUTAS PRINCIPALES
# ===================================

@main.route('/')
def home():
    """Página principal de CleanSA"""
    return render_template('index.html')

@main.route('/about')
def about():
    """Página de información sobre CleanSA"""
    return render_template('about.html')

# ===================================
# GESTIÓN DE USUARIOS
# ===================================

@main.route('/usuarios')
def user():
    """Listar usuarios del sistema"""
    return render_template(
        'usuarios.html', 
        usuarios=USUARIOS_EJEMPLO, 
        nombre=NOMBRE_USUARIO, 
        alumnos=ALUMNOS_EJEMPLO
    )

@main.route('/add_user', methods=['POST'])
def add_user():
    """Agregar nuevo usuario al sistema"""
    nombre_usuario = request.form.get('nombre_usuario')
    if nombre_usuario and nombre_usuario.strip():
        USUARIOS_EJEMPLO.append(nombre_usuario.strip())
    return redirect(url_for('main.user'))

# ===================================
# GESTIÓN DE EMPLEADOS
# ===================================

@main.route('/empleados')
def empleados():
    """Listar empleados de CleanSA"""
    # Datos falsos de empleados para demo
    empleados_falsos = [
        {"id": 1, "nombre": "Ana García", "puesto": "Gerente de Ventas", "email": "ana@cleansa.com"},
        {"id": 2, "nombre": "Carlos López", "puesto": "Técnico de Laboratorio", "email": "carlos@cleansa.com"},
        {"id": 3, "nombre": "María Rodríguez", "puesto": "Coordinadora de Logística", "email": "maria@cleansa.com"}
    ]
    
    return render_template('empleados.html', empleados=empleados_falsos)

# ===================================
# GESTIÓN DE PRODUCTOS
# ===================================

@main.route('/productos')
def productos():
    """Listar productos del catálogo CleanSA"""
    # Datos falsos de productos para demo
    productos_falsos = [
        {"id": 1, "nombre": "Detergente Premium", "precio": 850.00, "stock": 150},
        {"id": 2, "nombre": "Lavandina Concentrada", "precio": 1200.50, "stock": 200},
        {"id": 3, "nombre": "Jabón Antibacterial", "precio": 420.00, "stock": 300}
    ]
    
    return render_template('productos.html', productos=productos_falsos)



