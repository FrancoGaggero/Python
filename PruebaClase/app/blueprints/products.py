"""
CleanSA - Blueprint de Productos
Gestión del catálogo de productos higiénicos
"""

from flask import Blueprint, render_template, jsonify
from models import Producto, Categoria, database

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
        
        # Fallback con productos de ejemplo si hay error
        productos_ejemplo = [
            {
                'id': 1,
                'nombre': 'Detergente Multiuso',
                'precio': 15.99,
                'stock': 50,
                'categoria': 'Limpieza General',
                'peligroso': False
            },
            {
                'id': 2,
                'nombre': 'Desinfectante Pisos',
                'precio': 18.50,
                'stock': 30,
                'categoria': 'Desinfectantes',
                'peligroso': True
            }
        ]
        return render_template('productos.html', 
                             productos=productos_ejemplo, 
                             categorias={})

@products_bp.route('/panel')
def panel():
    """Panel administrativo de productos con funcionalidades CRUD"""
    try:
        productos = Producto.query.all()
        categorias = Categoria.query.all()
        
        return render_template('panel_productos.html', 
                             productos=productos,
                             categorias=categorias)
    except Exception as e:
        
        return render_template('panel_productos.html', 
                             productos=[],
                             categorias=[])

@products_bp.route('/api/productos')
def api_productos():
    """API endpoint para obtener productos en formato JSON"""
    try:
        productos = Producto.query.all()
        productos_data = []
        
        for producto in productos:
            categoria = Categoria.query.get(producto.fk_categoria)
            productos_data.append({
                'id': producto.id,
                'nombre': producto.nombre,
                'precio': producto.precio,
                'stock': producto.stock,
                'categoria': categoria.nombre if categoria else 'Sin categoría',
                'peligroso': producto.peligroso
            })
        
        return jsonify({
            'success': True,
            'productos': productos_data,
            'total': len(productos_data)
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'productos': []
        }), 500