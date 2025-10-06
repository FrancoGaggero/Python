"""
CleanSA - Módulo de Base de Datos
Funciones centralizadas para manejo de la base de datos
"""

import sqlite3
from typing import Optional

# ===================================
# CONFIGURACIÓN DE BASE DE DATOS
# ===================================

DB_NAME = 'cleansa.db'

def get_db_connection() -> sqlite3.Connection:
    """
    Establece conexión a la base de datos CleanSA
    
    Returns:
        sqlite3.Connection: Conexión a la base de datos
        
    Raises:
        sqlite3.Error: Si hay problemas de conexión
    """
    try:
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
    return execute_query("SELECT * FROM productos")

def get_all_employees():
    """Obtiene todos los empleados"""
    return execute_query("SELECT * FROM empleados")

def get_product_by_id(product_id: int):
    """Obtiene un producto específico por ID"""
    return execute_query("SELECT * FROM productos WHERE id = ?", (product_id,))

def get_employee_by_id(employee_id: int):
    """Obtiene un empleado específico por ID"""
    return execute_query("SELECT * FROM empleados WHERE id = ?", (employee_id,))