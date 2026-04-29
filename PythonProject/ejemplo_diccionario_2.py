import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sakila"
)

cursor = conexion.cursor()

cursor.execute("SELECT actor_id, first_name, last_name FROM actor")

actores = {}

for actor_id, nombre, apellido in cursor.fetchall():
    actores[actor_id] = nombre + " " + apellido

print(actores)

#-------------------------------------------

diccionario = {
    "id": 1,
    "nombre": "ricardo",
    "apellido": "ramirez",
    "edad": 17
}

#USO DE GET

diccionario.get("ciudad", "No existe")

#------------------------------------------

conteo = {}

palabra = "python"
#Sin .get():
if palabra not in conteo:
    conteo[palabra] = 1
else:
    conteo[palabra] += 1
    
#Con .get():
conteo[palabra] = conteo.get(palabra, 0) + 1

#lista[0]["edad"] <- para acceder a la edad de un diccionario dentro de una lista de diccionarios