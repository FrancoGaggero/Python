"""
CleanSA - Blueprint de Productos
Gestión del catálogo de productos higiénicos
"""

from flask import Blueprint, render_template
from ..database import get_all_products, get_product_by_id

# ===================================
# BLUEPRINT DE PRODUCTOS
# ===================================

products_bp = Blueprint('products', __name__, url_prefix='/admin/products')

# ===================================
# RUTAS DE PRODUCTOS
# ===================================

@products_bp.route('/')
def list_products():
    """Listar todos los productos del catálogo CleanSA"""
    productos = get_all_products() or []
    return render_template('productos.html', productos=productos)

@products_bp.route('/add')
def add_product():
    """Formulario para agregar nuevo producto"""
    # TODO: Implementar formulario de creación
    return "Formulario para agregar producto (por implementar)"

@products_bp.route('/<int:product_id>')
def view_product(product_id):
    """Ver detalles de un producto específico"""
    # TODO: Implementar vista de producto individual
    return f"Detalles del producto {product_id} (por implementar)"

@products_bp.route('/<int:product_id>/edit')
def edit_product(product_id):
    """Formulario para editar producto existente"""
    # TODO: Implementar formulario de edición
    return f"Editar producto {product_id} (por implementar)"