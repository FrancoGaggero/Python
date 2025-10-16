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
    {"nombre": "Franco", "edad": 20},
    {"nombre": "Flor", "edad": 22},
    {"nombre": "Gero", "edad": 19},
    {"nombre": "Abril", "edad": 23}
]
USUARIOS_EJEMPLO = ["Franco", "Flor", "Gero", "Abril"]

# ===================================
# RUTAS DE USUARIOS
# ===================================

@users_bp.route('/')
def index():
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
        return redirect(url_for('users.index'))
    
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

@users_bp.route('/panel')
def panel():
    """Panel administrativo de usuarios con funcionalidades CRUD"""
    return render_template('panel_usuarios.html')

@users_bp.route('/perfil')
def perfil():
    """Vista de perfil personal del usuario logueado"""
    return render_template('perfil_usuarios.html')