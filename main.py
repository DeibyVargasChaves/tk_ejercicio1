import tkinter as tk
from tkinter import ttk


def seleccionar():
    opcion_seleccionada = var.get()
    etiqueta_seleccion.config(text="Opción seleccionada: " + opcion_seleccionada)

def reiniciar():
    var.set(None)
    etiqueta_seleccion.config(text="")
    print("Reiniciando...")

window = tk.Tk()

var = tk.StringVar()

selected = tk.StringVar()
r1 = ttk.Radiobutton(window, text='si', variable=var, value='1', command=selected)
r2 = ttk.Radiobutton(window, text='tal vez', variable=var, value='2', command=selected)
r3 = ttk.Radiobutton(window, text='no', variable=var, value='3', command=selected)
etiqueta_seleccion = tk.Label(window, text="")
boton_reiniciar = tk.Button(window, text="reiniciar", command=reiniciar)

r1.grid(column=0, row=0, pady=5, padx=5)
r2.grid(column=0, row=1, pady=5, padx=5)
r3.grid(column=0, row=2, pady=5, padx=5)
etiqueta_seleccion.grid(column=0, row=3, pady=5, padx=5)
boton_reiniciar.grid(column=0, row=4, pady=5, padx=5)

window.mainloop()

