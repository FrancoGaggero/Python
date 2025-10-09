import sqlite3

# Conexión o creación de la base
conn = sqlite3.connect('empresa.db')
cursor = conn.cursor()

#print("Base de datos creada y conectada exitosamente.")


#Para ejecutar la consultas usamos "cursor.execute(consulta_sql)"

# Crear tabla (si no existe)
cursor.execute('''
CREATE TABLE IF NOT EXISTS empleados (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    puesto TEXT NOT NULL,
    salario REAL
)
''')

# Insertar datos
cursor.execute("INSERT INTO empleados (nombre, puesto, salario) VALUES (?, ?, ?)",
            ("Ghami", "Profesor", 700000))


# Insertar múltiples datos
empleados = [{"nombre": "Ana", "puesto": "Ingeniera", "salario": 800000},
            {"nombre": "Luis", "puesto": "Diseñador", "salario": 600000},
            {"nombre": "Marta", "puesto": "Gerente", "salario": 900000}]

cursor.executemany("INSERT INTO empleados (nombre, puesto, salario) VALUES (?, ?, ?)", 
                [(emp["nombre"], emp["puesto"], emp["salario"]) for emp in empleados])

conn.commit() #Con commit se guardan los cambios en la base de datos

# Leer datos
cursor.execute("SELECT * FROM empleados")
empleados = cursor.fetchall()

print("Listado de empleados:")
for e in empleados:
    print(e)
    
    
# Actualizar datos

cursor.execute("UPDATE empleados SET salario = ? WHERE nombre = ?", (750000, "Ghami"))
#Acá estamos actualizando el salario del empleado llamado "Ghami" a 750000
conn.commit()

# Eliminar datos
cursor.execute("DELETE FROM empleados WHERE nombre = ?", ("Luis",))
conn.commit()

# Cerrar conexión
conn.close()
