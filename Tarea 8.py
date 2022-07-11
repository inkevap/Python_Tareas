class Vehiculo():
    color= "verde"
    ruedas = 4
    puertas= 0
    def __init__(self):
        print("soy el constructor de vehiculo")

class Coche(Vehiculo):
    velocidad = "250km"
    Cilindrada = 2

Ferrari = Coche()
Ferrari.puertas = 2
print(f"Ferrari de color {Ferrari.color} tiene {Ferrari.ruedas} ruedas, {Ferrari.puertas} puertas, su velocidad maxima es {Ferrari.velocidad} y tiene {Ferrari.Cilindrada} de cilindrada.")
