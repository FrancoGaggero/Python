"""
CleanSA - Blueprint de Autenticación
Rutas para gestionar login y autenticación del sistema
"""
from flask import Blueprint, render_template, request, redirect, url_for

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

# ===================================
# RUTAS DE AUTENTICACIÓN
# ===================================



@auth_bp.route('/')
def index():
    return render_template('login.html')

@auth_bp.route('/login')
def login():
    """Página de login"""
    return render_template('login.html')


@auth_bp.route('/singin')
def singin():
    """Página de registro de nuevo usuario"""
    return render_template('singin.html')






