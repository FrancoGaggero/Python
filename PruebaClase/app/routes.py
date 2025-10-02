from flask import Blueprint, render_template, request, redirect, url_for

main = Blueprint('main', __name__)


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


##falta crear rutas para agregar usuarios



