class Estudiante:

    def __init__(self , nombre,edad):
        self.nombre = nombre
        self.edad = edad





    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_edad(self):
        return self.edad
    
    def set_edad(self, edad):
        self.edad = edad

    def saludar(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."




def validar_dato(dato): 
    if not dato.strip():  
        raise ValueError("El dato no puede estar vacío.") 
    return dato

