from flask import Blueprint, render_template, request, redirect, url_for
import sqlite3



#funcion de conexion a la base de datos que retora la connexion
def get_db_connection():
    conn = sqlite3.connect('cleansa.db')
    conn.row_factory = sqlite3.Row #acceder a las columanas por el nombre
    return conn


main = Blueprint('main', __name__)

@main.route("/empleados")
def empleados():
    conn = get_db_connection()
    empleados = conn.execute('SELECT * FROM empleados').fetchall()
    conn.close()
    return render_template('empleados.html', empleados=empleados)


nombre = "Franco"
alumnos = [
        {"nombre": "Juan", "edad": 20},
        {"nombre": "Ana", "edad": 22},
        {"nombre": "Luis", "edad": 19},
        {"nombre": "Franco", "edad": 23}
    ]
usuario = ["Juan", "Ana", "Luis","franco"]

@main.route('/')
def home ():
    return render_template ('pruebaclase.html')


@main.route('/about')
def about():
    return render_template ('about.html')

@main.route('/usuarios')
def user():
    return render_template('usuarios.html', usuarios=usuario, nombre=nombre, alumnos=alumnos)


@main.route('/add_user', methods=['POST'])
def add_user():
    nombre_usuario = request.form.get('nombre_usuario')
    if nombre_usuario:
        usuario.append(nombre_usuario)
    return redirect(url_for('main.user'))

##falta crear rutas para agregar usuarios



