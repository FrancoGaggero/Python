import sqlite3


# Conexión a la base de datos (o creación si no existe)
conn = sqlite3.connect('cleansa.db')
cursor = conn.cursor()

# Crear una tabla
cursor.execute('''
CREATE TABLE IF NOT EXISTS empleados (
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    puesto TEXT NOT NULL,
    salario REAL NOT NULL
)
''')


 #insertar multiples datos 
empleados = [
    {"nombre": "ana", "puesto": "Diseñadora","salario" : 45000},
    {"nombre": "abril", "puesto": "Diseñadora","salario" : 45000},
    {"nombre": "franco", "puesto": "desarrollador","salario" : 45000},
]

cursor.executemany("INSERT INTO empleados (nombre, puesto, salario) VALUES (?, ?, ?)", 
[(emp["nombre"], emp ["puesto"], emp ["salario"]) for emp in empleados])

conn.commit()





conn.close()