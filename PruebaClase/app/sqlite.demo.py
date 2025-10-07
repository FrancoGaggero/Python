"""
CleanSA - Base de Datos SQLite
Sistema de gestión para empresa de productos higiénicos
Configuración e inicialización de tablas
"""

import sqlite3

# ===================================
# CONFIGURACIÓN DE BASE DE DATOS
# ===================================



# Conexión a la base de datos (o creación si no existe)
conn = sqlite3.connect('cleansa.db')
cursor = conn.cursor()

# ===================================
# TABLAS DE CATÁLOGO - GESTIÓN DE PRODUCTOS
# ===================================

 

# Tabla: PRODUCTOS - Catálogo de productos CleanSA
cursor.execute('''
CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    descripcion TEXT,
    precio REAL NOT NULL,
    stock INTEGER NOT NULL DEFAULT 0,
    stock_minimo INTEGER DEFAULT 5,
    activo BOOLEAN DEFAULT 1,
    fecha_creacion DATE DEFAULT CURRENT_DATE
)
''')

# ===================================
# DATOS INICIALES - PRODUCTOS DE MUESTRA
# ===================================

 

# Lista de productos iniciales para CleanSA
productos = [
    {"nombre": "Lavandina Concentrada", "precio": 1200.50, "stock": 150},
    {"nombre": "Detergente Líquido Premium", "precio": 850.75, "stock": 200},
    {"nombre": "Jabón Líquido Antibacterial", "precio": 420.00, "stock": 300},
    {"nombre": "Esponja Multiuso", "precio": 150.00, "stock": 500},
    {"nombre": "Limpiador Multiuso", "precio": 680.00, "stock": 120},
]

# Insertar productos con manejo de duplicados
cursor.executemany('''
    INSERT OR IGNORE INTO productos (nombre, precio, stock) 
    VALUES (?, ?, ?)
''', [(prod["nombre"], prod["precio"], prod["stock"]) for prod in productos])

conn.commit()




# ===================================
# TABLAS DE CONFIGURACIÓN - TIPOS Y CATEGORÍAS
# ===================================



# Tabla: TIPOS DE USUARIO - Roles del sistema (Admin, Cliente)
cursor.execute('''
CREATE TABLE IF NOT EXISTS tipos_usuario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL
)
''')

# ===================================
# DATOS INICIALES - TIPOS DE USUARIO
# ===================================



# Definir roles del sistema CleanSA
tipos_usuario = [
    {"nombre": "admin"},
    {"nombre": "cliente"}
]

# Insertar tipos de usuario
cursor.executemany('''
    INSERT OR IGNORE INTO tipos_usuario (nombre) 
    VALUES (?)
''', [(tipo["nombre"],) for tipo in tipos_usuario])

conn.commit()


# ===================================
# TABLAS DE USUARIOS Y CLIENTES
# ===================================



# Tabla: USUARIOS - Clientes y usuarios del sistema
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    contrasena TEXT NOT NULL,
    tipo_usuario_id INTEGER,
    FOREIGN KEY (tipo_usuario_id) REFERENCES tipos_usuario(id)
)
''')

usuarios = [
    {"nombre": "Franco", "email": "franco@.com", "contrasena": "franco", "tipo_usuario_id": 1},
    {"nombre": "Abril", "email": "abril@.com", "contrasena": "abril", "tipo_usuario_id": 2}
]

# Insertar usuarios
cursor.executemany('''
    INSERT OR IGNORE INTO usuarios (nombre, email, contrasena, tipo_usuario_id) 
    VALUES (?, ?, ?, ?)
''', [(user["nombre"], user["email"], user["contrasena"], user["tipo_usuario_id"]) for user in usuarios])

conn.commit()


# ===================================
# TABLAS DE CATÁLOGO - CATEGORÍAS DE PRODUCTOS
# ===================================



# Tabla: CATEGORÍAS DE PRODUCTOS - Clasificación de productos
cursor.execute('''
CREATE TABLE IF NOT EXISTS categorias_producto (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    descripcion TEXT,
    activo BOOLEAN DEFAULT 1
)
''')

# ===================================
# DATOS INICIALES - CATEGORÍAS DE PRODUCTOS
# ===================================



# Categorías específicas para productos de limpieza CleanSA
categorias_productos = [
    {"nombre": "Limpieza Hogar", "descripcion": "Productos para limpieza doméstica"},
    {"nombre": "Higiene Personal", "descripcion": "Productos de cuidado personal"},
    {"nombre": "Lavandería", "descripcion": "Productos para lavar ropa"},
    {"nombre": "Desinfección", "descripcion": "Productos antibacteriales"},
    {"nombre": "Eco-Friendly", "descripcion": "Productos biodegradables"}
]

# Insertar categorías de productos
cursor.executemany('''
    INSERT OR IGNORE INTO categorias_producto (nombre, descripcion) 
    VALUES (?, ?)
''', [(cat["nombre"], cat["descripcion"]) for cat in categorias_productos])

conn.commit()


# ===================================
# FINALIZACIÓN Y CONFIRMACIÓN
# ===================================

# Confirmar todos los cambios
conn.commit()
 
# Cerrar conexión a la base de datos
conn.close()