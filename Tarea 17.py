import tkinter as tk

#Creamos la ventana en donde iran nuestros widgets
window = tk.Tk()

#configuramos las dimensiones de cada fila y columna de la ventana principal
window.rowconfigure(0,weight=1)
window.columnconfigure(0,weight=1)

#Creamos la variable donde se almacenaran las opciones de
#nuestra listbox
lang = ["Español","Ingles","Frances","Portugues"]

#Creamos los objetos con sus correspondientes parametros
list = tk.StringVar(value=lang)
frame = tk.Frame(window)
listbox =tk.Listbox(frame,listvariable=list,height=4)
label = tk.Label(window,text="Lista de idiomas")

#configuramos las dimensiones de cada fila y columna del frame
frame.rowconfigure(0,weight=1)
frame.rowconfigure(1,weight=1)
frame.rowconfigure(2,weight=1)
frame.columnconfigure(0,weight=1)
frame.columnconfigure(1,weight=1)
frame.columnconfigure(2,weight=1)


#Ubicamos los objetos usando grid
listbox.grid(row=1, column=1)
frame.grid(row=0, column=0, sticky="news")
label.grid(row=1, column=0)

window.mainloop()