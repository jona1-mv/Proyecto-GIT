from tkinter import *

# Función para agregar números y operadores
def click(valor):
    entrada.insert(END, valor)

# Función para calcular el resultado
def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, END)
        entrada.insert(0, resultado)
    except:
        entrada.delete(0, END)
        entrada.insert(0, "Error")

# Función para limpiar la pantalla
def limpiar():
    entrada.delete(0, END)

# Ventana principal
ventana = Tk()
ventana.title("Calculadora")
ventana.geometry("300x400")

# Pantalla
entrada = Entry(ventana, font=("Arial", 18), justify="right")
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Botones
botones = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3)
]

for (texto, fila, columna) in botones:
    if texto == '=':
        Button(ventana, text=texto, width=8, height=3,
               command=calcular).grid(row=fila, column=columna)
    else:
        Button(ventana, text=texto, width=8, height=3,
               command=lambda t=texto: click(t)).grid(row=fila, column=columna)

# Botón limpiar
Button(ventana, text="C", width=35, height=2,
       command=limpiar).grid(row=5, column=0, columnspan=4)

ventana.mainloop()
