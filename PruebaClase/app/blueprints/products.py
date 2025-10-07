"""
CleanSA - Blueprint de Productos
Gestión del catálogo de productos higiénicos
"""

from flask import Blueprint, render_template

# ===================================
# BLUEPRINT DE PRODUCTOS
# ===================================

products_bp = Blueprint('products', __name__, url_prefix='/products')

# ===================================
# DATOS DE EJEMPLO TEMPORALES
# ===================================

# Lista simple de productos para empezar
PRODUCTOS_EJEMPLO = [
    {
        'id': 1,
        'nombre': 'Lavandina Concentrada',
        'descripcion': 'Lavandina para limpieza profunda',
        'precio': 1200.50,
        'stock': 150
    },
    {
        'id': 2,
        'nombre': 'Detergente Líquido Premium', 
        'descripcion': 'Detergente para ropa delicada',
        'precio': 850.75,
        'stock': 200
    },
    {
        'id': 3,
        'nombre': 'Jabón Antibacterial',
        'descripcion': 'Jabón líquido antibacterial',
        'precio': 420.00,
        'stock': 300
    }
]

# ===================================
# RUTAS SIMPLES
# ===================================

@products_bp.route('/')
def list_products():
    """Mostrar productos - versión simple"""
    print(f"Mostrando {len(PRODUCTOS_EJEMPLO)} productos")
    return render_template('productos.html', productos=PRODUCTOS_EJEMPLO)