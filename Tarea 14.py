paises_usuario = " Guatemala, Belice, El salvador, España, Brazil, Guatemala, Belice"
#paises_usuario = input("ingresa una lista de paises, separados por coma. ")

paises_usuario = sorted(list(set(paises_usuario.rstrip(" ").lstrip(" ").split(","))))


print(paises_usuario)
