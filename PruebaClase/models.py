from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

database = SQLAlchemy()

class Usuario (database.Model, UserMixin):
    __tablename__ = 'usuarios'  
    id = database.Column(database.Integer, primary_key=True)
    nombre = database.Column(database.String(100), nullable=False)
    apellido = database.Column(database.String(100), nullable=False)
    password = database.Column(database.String(200), nullable=False)
    dni = database.Column(database.Integer, nullable=False)
    direccion = database.Column(database.String(100), nullable=False)
    tipousuario = database.Column(database.Boolean, nullable=False)
    tipo = database.Column(database.Boolean, nullable=False)

class Categoria (database.Model):
    __tablename__ = 'categorias'  
    id = database.Column(database.Integer, primary_key=True)
    nombre = database.Column(database.String(100), nullable=False)

class Producto (database.Model):
    __tablename__ = 'productos'  
    id = database.Column(database.Integer, primary_key=True)
    nombre = database.Column(database.String(100), nullable=False)
    precio = database.Column(database.Float, nullable=False)
    stock = database.Column(database.Integer, nullable=False)
    fk_categoria = database.Column(database.Integer,database.ForeignKey('categorias.id'), nullable=False)
    peligroso = database.Column(database.Boolean, nullable=False)

class Carrito (database.Model):
    __tablename__ = 'carritos'  
    id = database.Column(database.Integer, primary_key=True)
    fecha = database.Column(database.Date, nullable=False)
    estado = database.Column(database.String(100), nullable=False)
    total = database.Column(database.Float, nullable=False)
    codigo_envio = database.Column(database.Integer, nullable=False)
    fk_cliente = database.Column(database.Integer,database.ForeignKey('usuarios.id'), nullable=False)


class Carrito_detalle (database.Model):
    __tablename__ = 'carrito_detalles'  
    id = database.Column(database.Integer, primary_key=True)
    fk_carrito = database.Column(database.Integer,database.ForeignKey('carritos.id'), nullable=False)
    fk_producto = database.Column(database.Integer, database.ForeignKey('productos.id'), nullable=False)
    total_producto = database.Column(database.Float,nullable=False)
    cantidad = database.Column(database.Integer,nullable=False)



class Envio (database.Model):
    __tablename__ = 'envios'  
    id = database.Column(database.Integer, primary_key=True)
    fk_carrito = database.Column(database.Integer,database.ForeignKey('carritos.id'), nullable=False)
    fecha_entrega = database.Column(database.Date, nullable=False)
    direccion = database.Column(database.String(100), nullable=False)

