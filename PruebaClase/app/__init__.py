
"""
CleanSA - Aplicación Flask Principal
Sistema de gestión para empresa de productos higiénicos
"""

from flask import Flask, request, redirect, url_for, render_template
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from flask_sqlalchemy import SQLAlchemy

# Initialize the database object
database = SQLAlchemy()

def create_app():
 
    
    # ===================================
    # CONFIGURACIÓN BÁSICA
    # ===================================
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'supersecretkey'
    bcrypt = Bcrypt()
    # Inicializamos Bcrypt y LoginManager
    bcrypt.init_app(app) #Inicializar Bcrypt con la app
    login_manager = LoginManager()
    login_manager.init_app(app) # Integrando login con la app Flask

    # ===================================
    # CONFIGURACIÓN BÁSICA DE BASE DE DATOS
    # ===================================
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pruebabbdd.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False    
    database.init_app(app)
    
    # ===================================
    # REGISTRO DE BLUEPRINTS
    # ===================================
    
    # Importar todos los blueprints
    from .blueprints import ALL_BLUEPRINTS
    
    # Registrar cada blueprint en la aplicación
    for blueprint in ALL_BLUEPRINTS:
        app.register_blueprint(blueprint)
    
    # ===================================
    # MANEJADORES DE ERRORES
    # ===================================
    
    @app.errorhandler(404)
    def not_found(error):
        return "Página no encontrada - CleanSA", 404
    
    @app.errorhandler(500)
    def internal_error(error):
        return "Error interno del servidor - CleanSA", 500
    
    return app














