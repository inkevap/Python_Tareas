from Operaciones import *

b = int(input("Ingrese un numero: "))
a = int(input("Ingrese un numero mayor al anterior: "))
while a < b:
    "El numero que ha ingresado es menor."
    a = int(input("Ingrese un numero mayor al anterior: "))

print(f"la multiplicacion de {a} por {b} es {multiplicacion.multiplicado(a,b)}")
print(f"la division de {a} entre {b} es {division.dividido(a,b)}")
print(f"la resta de {b} a {a} es {resta.resta(a,b)}")
print(f"la suma de {b} a {a} es {suma.suma(a,b)}")

