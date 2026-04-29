import mysql.connector
try:
    #nos conectamos a la BD
    conexion= mysql.connector.connect(host="localhost",user="admin",password="1234",database="sakila")
    print("Conexion realizada correctamente")

    #vamos a hacer un select de la tabla actor
    #necesitamos crear un cursor que nos permite realizar operaciones sobre las base de datos
    cursor=conexion.cursor()

    #para ejecutar un query
    """cursor.execute("select * from actor where first_name='AUDREY'")

    #para ver los datos que recupera el cursor de la query lo hacemos con un bucle
    for fila in cursor:
        print(fila[2]) #nos va devolviendo tuplas, no podemos modificarlas, solo podemos leerlas

    #otra forma, para recuperar cuantos datos me devuelve es esta manera
    tupla=cursor.fetchall() #mete todos lo datos en una tupla, osea una tupla de tuplas
    print(len(tupla)) #y ver cuantos datos tengo
    for linea in tupla:
        print (linea)"""

    #eliminar dato de una base de datos
    codigo=16047
    cursor.execute("delete from payment where payment_id="+str(codigo))

    #row count es una variable que se actualiza despues de haber afectado la base de datos y nos devuelve las rows (lineas afectadas)
    print("El comando ha afectado a ",cursor.rowcount, "registros")



    #cerramos el cursor
    cursor.close()

    # los cambios se guardan con un commit. todos los cambios que no le haga un commit no se modifican en la base de datos
    conexion.commit()

    #una vez que terminamos cerramos la conexion
    conexion.close()
except mysql.connector.Error as error: #esto nos devuelve un mensaje del error concreto
    print(error)