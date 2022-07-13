
def crear_archivo(nombre_archivo):
    file = open(nombre_archivo, "w")
    print(f"El archivo {nombre_archivo} ha sido creado.")
    file.close()
    return nombre_archivo

def escribir_en_archivo(archivo,texto):
    f =open(archivo, "a")
    f.write(texto+"\n")
    f.close

def leer_archivo(archivo):
    f =open(archivo,)
    print(f.readlines())
    f.close

Archivo = crear_archivo("texto.txt")
escribir_en_archivo(Archivo,"El archivo ha sido satisfactoriamente creado.")
escribir_en_archivo(Archivo,"El texto ha sido escrito.")
leer_archivo(Archivo)

