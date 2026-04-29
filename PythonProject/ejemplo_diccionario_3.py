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
    actores[actor_id] = [nombre, apellido]

print(actores)

#-----------------------------------------

#ejemplo con join
cursor.execute("""
    SELECT a.actor_id, a.first_name, a.last_name, f.title
    FROM actor a
    JOIN film_actor fa ON a.actor_id = fa.actor_id
    JOIN film f ON fa.film_id = f.film_id
""")

actores = {}

for actor_id, nombre, apellido, pelicula in cursor.fetchall():
    nombre_completo = nombre + " " + apellido

    if nombre_completo not in actores:
        actores[nombre_completo] = [pelicula]
    else:
        actores[nombre_completo].append(pelicula)

print(actores)