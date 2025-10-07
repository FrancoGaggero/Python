#!/usr/bin/env python3
"""
Script para probar que los productos funcionan sin errores
"""

from flask import Flask, render_template
import sys
import os

# Agregar el directorio actual al path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.database import get_all_products

app = Flask(__name__, template_folder='app/templates')

@app.route('/test-productos')
def test_productos():
    try:
        productos = get_all_products() or []
        print(f"✅ Productos obtenidos: {len(productos)}")
        
        # Probar render del template
        html = render_template('productos.html', productos=productos)
        print(f"✅ Template renderizado correctamente ({len(html)} caracteres)")
        
        return html
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return f"Error: {e}"

if __name__ == '__main__':
    print("=== PRUEBA DE PRODUCTOS ===")
    
    # Probar función de base de datos
    try:
        productos = get_all_products()
        print(f"Productos: {len(productos) if productos else 0}")
        
        if productos:
            print("Primer producto:", productos[0])
    except Exception as e:
        print(f"Error en base de datos: {e}")
    
    # Iniciar servidor de prueba
    print("\nIniciando servidor de prueba en http://127.0.0.1:5000/test-productos")
    app.run(debug=True, port=5000)