"""
CleanSA - Base de Datos SQLite
Sistema de gestión para empresa de productos higiénicos
Configuración e inicialización de tablas
"""

import sqlite3

# ===================================
# CONFIGURACIÓN DE BASE DE DATOS
# ===================================

print("🏢 Inicializando base de datos CleanSA...")

# Conexión a la base de datos (o creación si no existe)
conn = sqlite3.connect('cleansa.db')
cursor = conn.cursor()

# ===================================
# TABLAS DE CATÁLOGO - GESTIÓN DE PRODUCTOS
# ===================================

print("🧴 Creando tabla de productos...")

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

print("📦 Insertando productos de ejemplo...")

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
print("✅ Productos insertados correctamente")



# ===================================
# TABLAS DE USUARIOS Y CLIENTES
# ===================================

print("👤 Creando tablas de usuarios...")

# Tabla: USUARIOS - Clientes y usuarios del sistema
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    contrasena TEXT NOT NULL,
    fecha_registro DATE DEFAULT CURRENT_DATE,
    activo BOOLEAN DEFAULT 1
)
''')

# ===================================
# TABLAS DE CONFIGURACIÓN - TIPOS Y CATEGORÍAS
# ===================================

print("⚙️ Creando tablas de configuración...")

# Tabla: TIPOS DE USUARIO - Roles del sistema (Admin, Cliente, Empleado)
cursor.execute('''
CREATE TABLE IF NOT EXISTS tipos_usuario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    descripcion TEXT,
    permisos TEXT
)
''')

# ===================================
# DATOS INICIALES - TIPOS DE USUARIO
# ===================================

print("🔐 Insertando tipos de usuario...")

# Definir roles del sistema CleanSA
tipos_usuario = [
    {"nombre": "admin", "descripcion": "Administrador del sistema", "permisos": "all"},
    {"nombre": "cliente", "descripcion": "Cliente/Comprador", "permisos": "read"}
]

# Insertar tipos de usuario
cursor.executemany('''
    INSERT OR IGNORE INTO tipos_usuario (nombre, descripcion, permisos) 
    VALUES (?, ?, ?)
''', [(tipo["nombre"], tipo["descripcion"], tipo["permisos"]) for tipo in tipos_usuario])

conn.commit()
print("✅ Tipos de usuario configurados")

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

print("📂 Insertando categorías de productos...")

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
print("✅ Categorías de productos configuradas")

# ===================================
# FINALIZACIÓN Y CONFIRMACIÓN
# ===================================

# Confirmar todos los cambios
conn.commit()

print("\n" + "="*50)
print("✅ Base de datos CleanSA inicializada correctamente!")
print("📋 Tablas creadas:")
print("   • usuarios - Clientes y usuarios del sistema") 
print("   • productos - Catálogo de productos")
print("   • categorias_producto - Clasificación de productos")
print("   • tipos_usuario - Roles del sistema")
print("🎉 ¡Sistema listo para usar!")
print("="*50)

# Cerrar conexión a la base de datos
conn.close()