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

# Lista expandida de productos para el panel administrativo
PRODUCTOS_EJEMPLO = [
    {
        'id': 1,
        'nombre': 'Lavandina Concentrada CleanSA',
        'descripcion': 'Lavandina profesional para limpieza profunda y desinfección',
        'precio': 1200.50,
        'stock': 150
    },
    {
        'id': 2,
        'nombre': 'Detergente Líquido Premium', 
        'descripcion': 'Detergente concentrado para ropa delicada y colores',
        'precio': 850.75,
        'stock': 200
    },
    {
        'id': 3,
        'nombre': 'Jabón Antibacterial',
        'descripcion': 'Jabón líquido antibacterial con fragancia natural',
        'precio': 420.00,
        'stock': 300
    },
    {
        'id': 4,
        'nombre': 'Limpiador Multiuso Eco-Friendly',
        'descripcion': 'Limpiador biodegradable para todas las superficies',
        'precio': 680.00,
        'stock': 85
    },
    {
        'id': 5,
        'nombre': 'Desinfectante Industrial',
        'descripcion': 'Desinfectante de grado hospitalario para áreas críticas',
        'precio': 2150.00,
        'stock': 45
    },
    {
        'id': 6,
        'nombre': 'Esponjas Multiuso (Pack x12)',
        'descripcion': 'Pack de esponjas resistentes para limpieza doméstica',
        'precio': 320.00,
        'stock': 0
    },
    {
        'id': 7,
        'nombre': 'Shampoo Alfombras CleanSA',
        'descripcion': 'Shampoo especial para limpieza profunda de alfombras',
        'precio': 1850.75,
        'stock': 120
    },
    {
        'id': 8,
        'nombre': 'Detergente en Polvo Familiar',
        'descripcion': 'Detergente en polvo concentrado para lavado familiar',
        'precio': 950.00,
        'stock': 3
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

@products_bp.route('/panel')
def panel():
    """Panel administrativo de productos con funcionalidades CRUD"""
    return render_template('panel_productos.html', productos=PRODUCTOS_EJEMPLO)