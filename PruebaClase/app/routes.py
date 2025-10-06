"""
CleanSA - Sistema de Gestión
Rutas principales para la aplicación de productos higiénicos
"""

from flask import Blueprint, render_template, request, redirect, url_for
import sqlite3

# ===================================
# CONFIGURACIÓN DE BASE DE DATOS
# ===================================

def get_db_connection():
    """
    Establece conexión a la base de datos CleanSA
    Returns:
        sqlite3.Connection: Conexión a la base de datos
    """
    conn = sqlite3.connect('cleansa.db')
    conn.row_factory = sqlite3.Row  # Acceder a las columnas por nombre
    return conn

# ===================================
# DATOS DE EJEMPLO (TEMPORAL)
# ===================================

# TODO: Migrar a base de datos cuando sea necesario
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
    conn = get_db_connection()
    try:
        empleados = conn.execute('SELECT * FROM empleados').fetchall()
    except sqlite3.Error as e:
        # TODO: Implementar logging adecuado
        print(f"Error al obtener empleados: {e}")
        empleados = []
    finally:
        conn.close()
    
    return render_template('empleados.html', empleados=empleados)

# ===================================
# GESTIÓN DE PRODUCTOS
# ===================================

@main.route('/productos')
def productos():
    """Listar productos del catálogo CleanSA"""
    conn = get_db_connection()
    try:
        productos = conn.execute('SELECT * FROM productos').fetchall()
    except sqlite3.Error as e:
        # TODO: Implementar logging adecuado
        print(f"Error al obtener productos: {e}")
        productos = []
    finally:
        conn.close()
    
    return render_template('productos.html', productos=productos)



