
#TIP PRO (te puede salvar)

#Si quieres diccionarios en vez de tuplas:

cursor = conexion.cursor(dictionary=True)
#¿Qué cambia?

#Ahora:

cursor.execute("SELECT first_name, last_name FROM actor")

for fila in cursor.fetchall():
    print(fila)

# Obtienes:

#{'first_name': 'PENELOPE', 'last_name': 'GUINESS'}