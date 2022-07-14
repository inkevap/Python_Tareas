paises = input("ingresa una lista de paises separados por coma:\n")

paises = paises.title().split(",")
for x in range(len(paises)):
    paises[x] = paises[x].strip(" ")
paises = sorted(list(set(paises)))
print(", ".join(paises))
