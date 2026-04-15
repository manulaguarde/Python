try:
    cursor=open("/home/alumno/fichero.txt","rt")
    espacios=0
    for linea in cursor:
        espacios+=linea.count(" ")
    cursor.close()
    print("Total espacios:",espacios)
except:
    print("Error al leer fichero")