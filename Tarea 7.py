Year = int(input("Ingrese el numero de un año: "))

def esBisiesto(year):
    if (not(year % 4 ) and (year % 100)) or  (not(year % 4) and not(year % 100 ) and not(year % 400)):
        return "Es bisiesto"
    else:
        return "no es bisiesto"

print(f"El año {Year} {esBisiesto(Year)}")