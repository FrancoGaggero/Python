"""
CleanSA - Blueprint de Empleados
Gestión del personal de CleanSA
"""

from flask import Blueprint, render_template
from ..database import get_all_employees, get_employee_by_id

# ===================================
# BLUEPRINT DE EMPLEADOS
# ===================================

employees_bp = Blueprint('employees', __name__, url_prefix='/admin/employees')

# ===================================
# RUTAS DE EMPLEADOS
# ===================================

@employees_bp.route('/')
def list_employees():
    """Listar todos los empleados de CleanSA"""
    empleados = get_all_employees() or []
    return render_template('empleados.html', empleados=empleados)

@employees_bp.route('/add')
def add_employee():
    """Formulario para agregar nuevo empleado"""
    # TODO: Implementar formulario de creación
    return "Formulario para agregar empleado (por implementar)"

@employees_bp.route('/<int:employee_id>')
def view_employee(employee_id):
    """Ver detalles de un empleado específico"""
    # TODO: Implementar vista de empleado individual
    return f"Detalles del empleado {employee_id} (por implementar)"

@employees_bp.route('/<int:employee_id>/edit')
def edit_employee(employee_id):
    """Formulario para editar empleado existente"""
    # TODO: Implementar formulario de edición
    return f"Editar empleado {employee_id} (por implementar)"