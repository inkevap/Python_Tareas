numero_inicial = int(input("Ingresa un numero: "))
numero_final = int(input("Ingresa un numero mayor al anterior: "))
numeros_impares = []
while numero_final <= numero_inicial:
    print("El numero que has ingresado es menor al primer numero")
    numero_final = int(input("Ingresa un numero mayor al anterior: "))

for numero_actual in range(numero_inicial,numero_final):
    if numero_actual % 2 == 1:
        numeros_impares.append(numero_actual)

print("Numeros impares entre %s " % numero_inicial + "y %s" % numero_final)
print(numeros_impares)