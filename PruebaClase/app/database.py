"""
CleanSA - Módulo de Base de Datos
Funciones centralizadas para manejo de la base de datos
"""

import sqlite3
import os
from typing import Optional

# ===================================
# CONFIGURACIÓN DE BASE DE DATOS
# ===================================

# Obtener la ruta absoluta del directorio padre (donde está cleansa.db)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_NAME = os.path.join(BASE_DIR, 'cleansa.db')

def get_db_connection() -> sqlite3.Connection:
    """
    Establece conexión a la base de datos CleanSA
    
    Returns:
        sqlite3.Connection: Conexión a la base de datos
        
    Raises:
        sqlite3.Error: Si hay problemas de conexión
    """
    try:
        print(f"Conectando a la base de datos en: {DB_NAME}")  # Debug
        conn = sqlite3.connect(DB_NAME)
        conn.row_factory = sqlite3.Row  # Acceder a las columnas por nombre
        return conn
    except sqlite3.Error as e:
        print(f"Error conectando a la base de datos: {e}")
        raise

def execute_query(query: str, params: tuple = ()) -> Optional[list]:
    """
    Ejecuta una consulta SELECT y devuelve los resultados
    
    Args:
        query (str): Consulta SQL
        params (tuple): Parámetros para la consulta
        
    Returns:
        list: Resultados de la consulta o None si hay error
    """
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.execute(query, params)
        results = cursor.fetchall()
        return results
    except sqlite3.Error as e:
        print(f"Error ejecutando consulta: {e}")
        return None
    finally:
        if conn:
            conn.close()

def execute_modify(query: str, params: tuple = ()) -> bool:
    """
    Ejecuta una consulta INSERT, UPDATE o DELETE
    
    Args:
        query (str): Consulta SQL
        params (tuple): Parámetros para la consulta
        
    Returns:
        bool: True si fue exitoso, False si hubo error
    """
    conn = None
    try:
        conn = get_db_connection()
        conn.execute(query, params)
        conn.commit()
        return True
    except sqlite3.Error as e:
        print(f"Error modificando datos: {e}")
        if conn:
            conn.rollback()
        return False
    finally:
        if conn:
            conn.close()

# ===================================
# FUNCIONES ESPECÍFICAS PARA CLEANSA
# ===================================

def get_all_products():
    """Obtiene todos los productos del catálogo"""
    try:
        result = execute_query("SELECT * FROM productos ORDER BY nombre")
        print(f"Productos encontrados: {len(result) if result else 0}")  # Debug
        
        # Limpiar valores None para evitar errores en templates
        if result:
            productos_limpios = []
            for producto in result:
                # Convertir Row a diccionario para poder modificarlo
                producto_dict = dict(producto)
                
                # Limpiar campos que pueden ser None
                if producto_dict['descripcion'] is None:
                    producto_dict['descripcion'] = ''
                if producto_dict['stock_minimo'] is None:
                    producto_dict['stock_minimo'] = 5
                if producto_dict['activo'] is None:
                    producto_dict['activo'] = 1
                    
                productos_limpios.append(producto_dict)
            
            return productos_limpios
        
        return result
        
    except Exception as e:
        print(f"Error obteniendo productos: {e}")
        return []

def get_all_employees():
    """Obtiene todos los empleados"""
    return execute_query("SELECT * FROM empleados")

def get_product_by_id(product_id: int):
    """Obtiene un producto específico por ID"""
    return execute_query("SELECT * FROM productos WHERE id = ?", (product_id,))

def get_employee_by_id(employee_id: int):
    """Obtiene un empleado específico por ID"""
    return execute_query("SELECT * FROM empleados WHERE id = ?", (employee_id,))