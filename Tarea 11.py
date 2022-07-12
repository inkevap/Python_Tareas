import time as t # importamos el modulo tiempo para obtener la hora

_,_,_,hora,minutos,_,_,_,_ = t.localtime() # Guardamos las variables del tiempo hora y minuto y descartamos el resto

if hora >= 19: # comprobamos si es la hora de salir
    print("Es hora de parar de trabajar")
else:
    print(f"Aun faltan {18-hora} horas con {59-minutos} minutos para parar de trabajar.")