"""



"""
import tkinter as tk
import pprint as p

window = tk.Tk()

def funcion():
    Opciones.set ("x")

for x in range(0,4):
    window.columnconfigure(x, weight=1)
    window.rowconfigure(x,weight=1)
Opciones = tk.StringVar()
opcion1 = tk.Radiobutton(
    window,
    text= "opcion 1",
    variable = Opciones,
    value = 1,
    tristatevalue=0

)
opcion3 = tk.Radiobutton(
    window,
    text= "opcion 3",
    variable = Opciones,
    value = 3,
    tristatevalue=0
)
opcion2 = tk.Radiobutton(
    window,
    text= "opcion 2",
    variable = Opciones,
    value = 2,
    tristatevalue=0
)
reiniciar = tk.Button(
    window,
    text="Reiniciar Todo",
    command= funcion
)

opcion1.grid(column=0, row=1)
opcion2.grid(column=0, row=2)
opcion3.grid(column=0, row=3)
reiniciar.grid(column=2, row=2)


window.mainloop()
