import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sakila"
)

cursor = conexion.cursor()

#1. SELECT en Python
cursor.execute("SELECT * FROM actor")

resultados = cursor.fetchall()

for fila in resultados:
    print(fila)


#SELECT con WHERE
cursor.execute("SELECT * FROM actor WHERE first_name = 'PENELOPE'")

#MEJOR (evitar errores / SQL injection)
sql = "SELECT * FROM actor WHERE first_name = %s"
valor = ("PENELOPE",) #en una tupla

cursor.execute(sql, valor)



#2. INSERT en Python
sql = "INSERT INTO actor (first_name, last_name) VALUES (%s, %s)"
valores = ("JUAN", "PEREZ")

cursor.execute(sql, valores)
conexion.commit()

#SIEMPRE:

conexion.commit()

#3. UPDATE en Python
sql = "UPDATE actor SET first_name = %s WHERE actor_id = %s"
valores = ("CARLOS", 1)

cursor.execute(sql, valores)
conexion.commit()

#4. DELETE en Python
sql = "DELETE FROM actor WHERE actor_id = %s"
valores = (1,)

cursor.execute(sql, valores)
conexion.commit()

#5. ORDER BY + LIMIT
cursor.execute("SELECT * FROM film ORDER BY length DESC LIMIT 5")

for fila in cursor.fetchall():
    print(fila)

#6. FUNCIONES (COUNT, AVG…)
cursor.execute("SELECT COUNT(*) FROM film")
print(cursor.fetchone())

cursor.execute("SELECT AVG(length) FROM film")
print(cursor.fetchone())

#7. GROUP BY
cursor.execute("""
    SELECT rating, COUNT(*)
    FROM film
    GROUP BY rating
""")

for fila in cursor.fetchall():
    print(fila)

#8. JOIN (MUY IMPORTANTE)
cursor.execute("""
    SELECT a.first_name, a.last_name, f.title
    FROM actor a
    JOIN film_actor fa ON a.actor_id = fa.actor_id
    JOIN film f ON fa.film_id = f.film_id
""")

for fila in cursor.fetchall():
    print(fila)