"""En este ejercicio tendréis que crear una tabla llamada Alumnos que constará de tres columnas:
la columna id de tipo entero, la columna nombre que será de tipo texto y la columna apellido que
también será de tipo texto.
Una vez creada la tabla, tenéis que insertarle datos, como mínimo tenéis que insertar 8 alumnos a la tabla.
Por último, tienes que realizar una búsqueda de un alumno por nombre y mostrar los datos por consola."""
# Importamos las librerias que vamos a usar
import sqlite3

# Nos conectamos a una base de datos y creamos un cursor
conn = sqlite3.connect("fichero.db")
cursor = conn.cursor()

# Creamos la tabla con sus respectivas columnas
Tabla = """ CREATE TABLE IF NOT EXISTS alumnos (
            id PRIMARY KEY,
            nombre text NOT NULL,
            apellido text NOT NULL
        );"""
cursor.execute(Tabla)

# Insertamos SOLO LOS PRIMEROS 8 alumnos a la base de datos
Alumnos = [[1, "Pedro", "Barbena"], [2, "Jose", "Montes"], [3, "Fred", "Cardenas"],
           [4, "Gaby", "Rangel"], [5, "David", "Cartagena"], [6, "Oscar", "Galvan"],
           [7, "Sofia", "Ruiz"], [8, "Elder", "Romano"], [9, "Maria", "Vasquez"], [10, "Carolina", "Cantor"]]


for x in range(0, 8):  # <-------- Solo insertamos los primeros 8 alumnos
    Query = f"""SELECT * FROM alumnos WHERE id={Alumnos[x][0]}
    AND nombre='{Alumnos[x][1]}' AND apellido='{Alumnos[x][2]}'"""
    if cursor.execute(Query).fetchone() is None:  # <-------- Verificamos que el alumno no existe en la base de datos
        Query = "INSERT INTO alumnos(id, nombre, apellido) VALUES(?,?,?)"
        cursor.execute(Query, (Alumnos[x][0], Alumnos[x][1], Alumnos[x][2]))
    else:
        print(f"id: {Alumnos[x][0]}, nombre: {Alumnos[x][1]}, apellido:{Alumnos[x][2]} ya se encuentra en la base")


# Verificamos que los usuarios se encuentren en la base de datos
for x in range(len(Alumnos)):
    Query = f"SELECT * FROM alumnos WHERE id={Alumnos[x][0]}" \
            f" AND nombre='{Alumnos[x][1]}' AND apellido='{Alumnos[x][2]}'"
    rows = cursor.execute(Query)
    if rows.fetchone() is not None:
        print(f"El alumno {Alumnos[x][1]} {Alumnos[x][2]} de ID {Alumnos[x][0]} se encuentra en la base")
    else:
        print(f"El alumno {Alumnos[x][1]} {Alumnos[x][2]} de ID {Alumnos[x][0]} NO se encuentra en la base")

# Cerramos el cursor y la conexion con la base de datos
cursor.close()
conn.commit()  # <------ Guardamos todos los cambios a la base de datos
conn.close()
