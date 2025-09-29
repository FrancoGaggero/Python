
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

#Variables
nombre = "Franco"
alumnos = [
        {"nombre": "Juan", "edad": 20},
        {"nombre": "Ana", "edad": 22},
        {"nombre": "Luis", "edad": 19},
        {"nombre": "Franco", "edad": 23}
    ]
usuario = ["Juan", "Ana", "Luis","franco"]

@app.route('/')
def index():
    return render_template ('pruebaclase.html')

@app.route('/user')
def user():
    return render_template('usuarios.html', usuarios=usuario, nombre=nombre, alumnos=alumnos)
 
@app.route('/add_user', methods=['POST'])
def add_user():
    nuevo = request.form['nombre']
    edad = request.form['edad']
    alumnos.append({"nombre": nuevo, "edad": int(edad)})
    return redirect(url_for('user'))



if __name__ == '__main__':
    app.run(debug=True)