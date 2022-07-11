
class Alumno():
    nombre = ""
    nota = 0

    def __init__(self,nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def cambiar_nota(self,nota):
        self.nota = nota

    def renombrar(self,nombre):
        self.nombre = nombre

    def esAprobado(self):
        if self.nota > 60:
            print(f"{self.nombre} ha sido aprobado con una nota de {self.nota}.")


Alumno1 = Alumno("Maro",49)
Alumno1.renombrar("Oscar")
Alumno1.cambiar_nota(65)
Alumno1.esAprobado()


