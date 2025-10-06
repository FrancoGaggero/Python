"""
Gestion de Usuarios - Blueprint de Usuarios
Rutas para gestionar usuarios y clientes del sistema
"""
from flask import Blueprint, render_template, request, redirect, url_for
import sqlite3

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

# ===================================
# RUTAS DE AUTENTICACIÓN
# ===================================



@auth_bp.route('/')
def index():
    return render_template('login.html')









