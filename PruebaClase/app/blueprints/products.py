"""
CleanSA - Blueprint de Productos
Gestión del catálogo de productos higiénicos
"""

from flask import Blueprint, render_template
from models import Producto, Categoria

# ===================================
# BLUEPRINT DE PRODUCTOS
# ===================================

products_bp = Blueprint('products', __name__, url_prefix='/products')

# ===================================
# RUTAS DE PRODUCTOS
# ===================================

@products_bp.route('/')
def list_products():
    """Mostrar productos desde la base de datos"""
    try:
        # Obtener todos los productos de la base de datos
        productos = Producto.query.all()
        
        # Obtener categorías para mostrar información completa
        categorias = {cat.id: cat.nombre for cat in Categoria.query.all()}
        
        return render_template('productos.html', 
                             productos=productos, 
                             categorias=categorias)
    except Exception as e:
        
        
        return render_template('productos.html', 
                             productos=[], 
                             categorias={})

@products_bp.route('/panel')
def panel():
    """Panel administrativo de productos con funcionalidades CRUD"""
    try:
        productos = Producto.query.all()
        categorias_list = Categoria.query.all()
        
        # Convertir categorías a diccionario para fácil acceso en template
        categorias = {cat.id: cat.nombre for cat in categorias_list}
        
        print(f"✅ Panel cargado: {len(productos)} productos, {len(categorias)} categorías")
        
        return render_template('panel_productos.html', 
                             productos=productos,
                             categorias=categorias)
    except Exception as e:
        print(f"❌ Error al cargar panel de productos: {e}")
        return render_template('panel_productos.html', 
                             productos=[],
                             categorias={})