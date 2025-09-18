#Primer paso: importar la libreria
import tkinter as tkin
from tkinter import messagebox

def saludar(etiqueta):
    etiqueta.config(text="Hola desde Tkinter en la pantalla\n")
    print("Hola desde Tkinter en consola")

    
def main():
    ventana = tkin.Tk()
    ventana.title("Mi Ventana Tkinter")
    ventana.geometry("300x200")
    ventana.configure(bg= "lightgrey")
    
    #Ahora usaremos algunos widgets
    etiqueta = tkin.Label(ventana, text="Hola, Tkinter")
    etiqueta.pack(pady= 5)  # Agrega el widget a la ventana
    
    boton = tkin.Button(ventana, text="Saludar", command=lambda: saludar(etiqueta), width=10)
    #Se utiliza lambda para pasar parametros a la funcion y que no se ejecute al crear el boton
    boton.pack()
    boton.pack(pady=5) # Agregamos el boton a la ventana
    
    def mostrar_mensaje():
        messagebox.showinfo("Título", "Esto es una información")
        messagebox.showerror("Error", "Hubo un problema")
    
    
    boton = tkin.Button(ventana, text="Clic acá", command=mostrar_mensaje, width=10)
    boton.pack(pady=5) # Agregamos el boton a la ventana
    
    etiqueta_nombre = tkin.Label(ventana, text="Nombre:", bg="lightgrey")
    etiqueta_nombre.pack(pady=2)
    entrada = tkin.Entry(ventana)
    entrada.pack(pady=5)
     # Agregamos la entrada de texto a la ventana
    
    ventana.mainloop()# Inicia el loop de la ventana


if __name__ == "__main__":
    main()















