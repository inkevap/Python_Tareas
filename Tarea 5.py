import math
Altura = int(input("ingrese la altura del triangulo a calcular: "))
Base = int(input("ingrese la base del triangulo a calcular: "))
Radio = int(input("ingrese el radio del circulo a calcular: "))

def area_triangulo(altura=0,base=0):
    resultado = (base * altura)/2
    return resultado

def area_circulo(radio = 0):
    resultado = 2*math.pi*(radio**2)
    return resultado

print(f"El area de su triangulo es: {area_triangulo(Altura,Base)}:")
print(f"El area de su circulo es: {area_circulo(Radio)}:")
