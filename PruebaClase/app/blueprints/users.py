"""
CleanSA - Blueprint de Usuarios
Gestión de usuarios y clientes del sistema
"""

from flask import Blueprint, render_template, request, redirect, url_for

# ===================================
# BLUEPRINT DE USUARIOS
# ===================================

users_bp = Blueprint('users', __name__, url_prefix='/admin/users')

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
# RUTAS DE USUARIOS
# ===================================

@users_bp.route('/')
def list_users():
    """Listar usuarios del sistema"""
    return render_template(
        'usuarios.html', 
        usuarios=USUARIOS_EJEMPLO, 
        nombre=NOMBRE_USUARIO, 
        alumnos=ALUMNOS_EJEMPLO
    )

@users_bp.route('/add', methods=['GET', 'POST'])
def add_user():
    """Agregar nuevo usuario al sistema"""
    if request.method == 'POST':
        nombre_usuario = request.form.get('nombre_usuario')
        if nombre_usuario and nombre_usuario.strip():
            USUARIOS_EJEMPLO.append(nombre_usuario.strip())
        return redirect(url_for('users.list_users'))
    
    # TODO: Implementar formulario GET
    return "Formulario para agregar usuario (por implementar)"

@users_bp.route('/<int:user_id>')
def view_user(user_id):
    """Ver detalles de un usuario específico"""
    # TODO: Implementar vista de usuario individual
    return f"Detalles del usuario {user_id} (por implementar)"

@users_bp.route('/<int:user_id>/edit')
def edit_user(user_id):
    """Formulario para editar usuario existente"""
    # TODO: Implementar formulario de edición
    return f"Editar usuario {user_id} (por implementar)"