Numero = int(input("Ingrese un numero: "))
factores = []
def esprimo(numero):
    global factores
    for y in reversed(range(numero)):
        if y == 0:
            continue
        if numero % y == 0:
            factores.append(y)
    if len(factores) < 2:
        return True
    else:
        return False
valor = esprimo(Numero)
resultado= "no es primo" if not valor  else "es primo"
print(f"El numero que usted ha ingresa {resultado} porque tiene estos factores: {factores}")