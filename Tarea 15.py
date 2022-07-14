from functools import reduce

def funcion(lista):
   lista = list(filter(lambda x: x % 2 == 1,lista))
   print(f"Numeros impares: {lista}")
   lista = reduce(lambda x,y: x+y, lista)
   print(f"Sumatoria de los elementos: {lista}")

ejemplo = list(range(1,6))
print(ejemplo)
funcion(ejemplo)