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


@auth_bp.route('/singin')
def singin():
    """Página de registro de nuevo usuario"""
    return render_template('singin.html')


@auth_bp.route('/logout')
def logout():
    """Cerrar sesión del usuario"""
    return redirect(url_for('main.home'))



