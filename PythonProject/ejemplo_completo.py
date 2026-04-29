import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sakila"
)

cursor = conexion.cursor()

# Insertar actor
cursor.execute(
    "INSERT INTO actor (first_name, last_name) VALUES (%s, %s)",
    ("LUIS", "GOMEZ")
)
conexion.commit()

# Consultar actores que empiezan por A
cursor.execute("SELECT * FROM actor WHERE first_name LIKE 'A%'")

for actor in cursor.fetchall():
    print(actor)

# Actualizar actor
cursor.execute(
    "UPDATE actor SET first_name = %s WHERE actor_id = %s",
    ("PEDRO", 1)
)
conexion.commit()

# Borrar actor
cursor.execute(
    "DELETE FROM actor WHERE actor_id = %s",
    (1,)
)
conexion.commit()