soluciones=[]
respuesta=[]
respuestas=[]
diccionario={}
try:
    with open("/home/alumno/ejercicio6Python_ficheros/soluciones.txt","rt") as cursor:
        contenido=cursor.read()
        contenido=contenido.replace("\n","")
        soluciones=contenido.split(", ")


except:
    print("Fichero no encontrado")

try:
    with open("/home/alumno/ejercicio6Python_ficheros/respuestas.txt","rt") as cursor:
        for linea in cursor:
            linea=linea.replace("\n","")
            respuesta=linea.split(": ")
            letra=respuesta[1].split(", ")
            #print(letra)
            #print(respuesta)
            respuestas.append(respuesta)
            diccionario[respuesta[0]]=respuesta[1]
except:
    print("Fichero no encontrado")

#print(respuestas)
print(diccionario)

try:
    with open("/home/alumno/ejercicio6Python_ficheros/notas.txt","wt") as cursor:
        aciertos=0
        errores=0
        

except:
    print("Hubo un problema al intentar escribir el fichero")