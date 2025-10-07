#!/usr/bin/env python3
"""
Script de prueba para verificar productos en la base de datos
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.database import get_all_products

try:
    print("=== PRUEBA DE PRODUCTOS ===")
    productos = get_all_products()
    
    print(f"Tipo de datos: {type(productos)}")
    print(f"Cantidad de productos: {len(productos) if productos else 0}")
    
    if productos:
        print(f"Primer producto (raw): {productos[0]}")
        print(f"Tipo del primer producto: {type(productos[0])}")
        
        # Intentar acceder por índice
        try:
            print(f"Por índice [1]: {productos[0][1]}")
        except Exception as e:
            print(f"Error accediendo por índice: {e}")
        
        # Intentar acceder por nombre de columna
        try:
            print(f"Por nombre 'nombre': {productos[0]['nombre']}")
        except Exception as e:
            print(f"Error accediendo por nombre: {e}")
            
        # Mostrar todos los productos
        print("\n=== LISTA DE PRODUCTOS ===")
        for i, producto in enumerate(productos):
            print(f"{i+1}. {producto}")
    else:
        print("❌ No se encontraron productos")
        
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()