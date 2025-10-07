#!/usr/bin/env python3
import sqlite3

# Verificar tablas en la base de datos del directorio principal
conn1 = sqlite3.connect('cleansa.db')
cursor1 = conn1.cursor()
cursor1.execute("SELECT name FROM sqlite_master WHERE type='table'")
tablas_raiz = [row[0] for row in cursor1.fetchall()]
print("Tablas en cleansa.db (raíz):", tablas_raiz)

if 'productos' in tablas_raiz:
    cursor1.execute("SELECT COUNT(*) FROM productos")
    count = cursor1.fetchone()[0]
    print(f"Productos en raíz: {count}")
    
    if count > 0:
        cursor1.execute("SELECT * FROM productos LIMIT 3")
        productos = cursor1.fetchall()
        print("Primeros 3 productos:", productos)

conn1.close()

# Verificar tablas en la base de datos del directorio app
try:
    conn2 = sqlite3.connect('app/cleansa.db')
    cursor2 = conn2.cursor()
    cursor2.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tablas_app = [row[0] for row in cursor2.fetchall()]
    print("Tablas en app/cleansa.db:", tablas_app)
    
    if 'productos' in tablas_app:
        cursor2.execute("SELECT COUNT(*) FROM productos")
        count = cursor2.fetchone()[0]
        print(f"Productos en app: {count}")
    
    conn2.close()
except Exception as e:
    print(f"Error con app/cleansa.db: {e}")