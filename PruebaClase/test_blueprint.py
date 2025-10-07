#!/usr/bin/env python3
"""
Script simple para probar el blueprint de productos
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.blueprints.products import obtener_productos

print("=== PRUEBA DEL BLUEPRINT DE PRODUCTOS ===")

try:
    productos = obtener_productos()
    
    if productos:
        print(f"✅ Se cargaron {len(productos)} productos:")
        for i, producto in enumerate(productos[:3], 1):  # Mostrar solo los primeros 3
            print(f"{i}. {producto['nombre']} - ${producto['precio']} - Stock: {producto['stock']}")
        
        if len(productos) > 3:
            print(f"   ... y {len(productos) - 3} productos más")
    else:
        print("❌ No se encontraron productos")
        
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()