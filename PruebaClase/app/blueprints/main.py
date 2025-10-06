"""
CleanSA - Blueprint Principal
Rutas principales del sitio web (home, about, etc.)
"""

from flask import Blueprint, render_template

# ===================================
# BLUEPRINT PRINCIPAL
# ===================================

main_bp = Blueprint('main', __name__)

# ===================================
# RUTAS PRINCIPALES
# ===================================

@main_bp.route('/')
def home():
    """Página principal de CleanSA"""
    return render_template('index.html')

@main_bp.route('/about')
def about():
    """Página de información sobre CleanSA"""
    return render_template('about.html')

@main_bp.route('/test')
def test():
    """Página de prueba para Anime.js"""
    return render_template('test.html')