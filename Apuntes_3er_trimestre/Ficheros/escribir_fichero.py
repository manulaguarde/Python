#ESCRITURA EN FICHEROS

#podemos tener dos opciones w (write) o a (append)
#w inicializa el fichero (borra todo si existe) y lo crea si no existe
#a se posiciona al final del cursor (al final del contenido) pero no borra el contenido que ya estaba

try:
    with open("/home/alumno/fichero.txt","wt") as cursor:
        lista=["uno\n","dos\n","tres\n","\ncuatro"]
        cursor.writelines(lista) #me escribe el contenido de una lísta en el fichero

except:
    print("Error trabajando con el fichero")