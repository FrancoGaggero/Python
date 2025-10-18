
"""
CleanSA - Aplicación Flask Principal
Sistema de gestión para empresa de productos higiénicos
"""

from flask import Flask

def create_app():
    """
    Crea y configura la aplicación Flask CleanSA
    
    
        Flask: Instancia de la aplicación configurada
    """
    app = Flask(__name__)
    
    # ===================================
    # CONFIGURACIÓN BÁSICA
    # ===================================
    
    app.config['SECRET_KEY'] = 'cleansa-secret-key-development'
    
    
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














