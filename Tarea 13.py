import pickle #importamos pickle para almacenar datos

class Vehiculo:
    modelo = ""
    llantas = 0
    color = ""

    def __init__(self,modelo, llantas, color):
        self.modelo = modelo
        self.llantas = llantas
        self.color = color

    def __str__(self):
        return f"Soy un vehiculo modelo {self.modelo} de {self.llantas} llantas y de color {self.color}."


def crear_archivo(nombre_archivo):#creamos una funcion que nos permita crear ficheros
    file = open(nombre_archivo, "wb")
    print(f"El archivo {nombre_archivo} ha sido creado.")
    file.close()
    return nombre_archivo

def guardar_archivo(nombre_archivo,guardar):#creamos una funcion que nos permita guardar en ficheros ya creados
    file = open(nombre_archivo,"wb")
    pickle.dump(guardar,file)
    file.close()

def cargar_archivo(nombre_archivo): #creamos una funcion para cargar ficheros guardados
    file = open(nombre_archivo, "rb")
    variable = pickle.load(file)
    file.close()
    return variable

carro = Vehiculo(2022,4,"verde")
datos = crear_archivo("data.bin")
guardar_archivo(datos,carro)
moto = cargar_archivo(datos)
print(f"Carro: {carro} y Moto: {moto}")


