"""
CleanSA - Blueprint de Autenticación
Rutas para gestionar login y autenticación del sistema
"""
from flask import Blueprint, render_template, request, redirect, url_for
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from models import Usuario, database

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


# ===================================
# RUTAS DE AUTENTICACIÓN
# ===================================



@auth_bp.route('/')
def index():
    return render_template('login.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """Página de login"""
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = Usuario.query.filter_by(nombre=username).first()
        
        
        if user and Bcrypt().check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('main.home'))
        else:
            return render_template('login.html', error="Credenciales inválidas")
    return render_template('login.html')


@auth_bp.route('/singin' , methods=['GET', 'POST'])
def singin():
    """Página de registro de nuevo usuario"""
    if request.method == "POST":
        nombre = request.form.get('nombre')
        apellido = request.form.get('apellido')
        password = request.form.get('password')
        dni = request.form.get('dni')
        direccion = request.form.get('direccion')
        tipo = request.form.get('tipo') == 'true'
        
        hashed_password = Bcrypt().generate_password_hash(password).decode('utf-8')
        
        new_user = Usuario(
            nombre=nombre,
            apellido=apellido,
            password=hashed_password,
            dni=dni,
            direccion=direccion,
            fk_tipousuario=2,  # Asignar tipo Cliente por defecto
            tipo=tipo
        )
        
        database.session.add(new_user)
        database.session.commit()
        
        return redirect(url_for('auth.login'))
    
    return render_template('singin.html')





@auth_bp.route('/logout')
@login_required
def logout():
    """Cerrar sesión del usuario"""
    logout_user()
    return redirect(url_for('main.home'))



