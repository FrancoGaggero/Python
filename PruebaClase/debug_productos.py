#!/usr/bin/env python3
import sqlite3

conn = sqlite3.connect('cleansa.db')
cursor = conn.cursor()

# Obtener estructura de la tabla productos
cursor.execute("PRAGMA table_info(productos)")
columnas = cursor.fetchall()
print("=== ESTRUCTURA TABLA PRODUCTOS ===")
for col in columnas:
    print(f"- {col[1]} ({col[2]}) - NULL: {'Sí' if col[3] == 0 else 'No'}")

print("\n=== DATOS DE PRODUCTOS ===")
cursor.execute("SELECT * FROM productos")
productos = cursor.fetchall()

for i, producto in enumerate(productos):
    print(f"\nProducto {i+1}:")
    for j, valor in enumerate(producto):
        col_name = columnas[j][1]
        print(f"  {col_name}: {valor} ({type(valor).__name__})")

# Verificar específicamente valores None
print("\n=== VERIFICANDO VALORES NONE ===")
cursor.execute("SELECT COUNT(*) FROM productos WHERE descripcion IS NULL")
desc_null = cursor.fetchone()[0]
print(f"Productos con descripcion NULL: {desc_null}")

cursor.execute("SELECT COUNT(*) FROM productos WHERE precio IS NULL")
precio_null = cursor.fetchone()[0]
print(f"Productos con precio NULL: {precio_null}")

cursor.execute("SELECT COUNT(*) FROM productos WHERE stock IS NULL")
stock_null = cursor.fetchone()[0]
print(f"Productos con stock NULL: {stock_null}")

conn.close()