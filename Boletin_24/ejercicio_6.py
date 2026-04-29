soluciones=[]
respuestas=[]
alumnos=[]
try:
    with open("C:/ProyectosGit/EjerciciosPython/Boletin_24/soluciones.txt","rt") as cursor:
        contenido=cursor.read()
        contenido=contenido.replace("\n","")
        soluciones=contenido.split(", ")


except:
    print("Fichero no encontrado")

try:
    with open("C:/ProyectosGit/EjerciciosPython/Boletin_24/respuestas.txt","rt") as cursor:
        for linea in cursor:
            linea=linea.replace("\n","")
            lista_linea=linea.split(": ")
            alumnos.append(lista_linea[0])
            letra=lista_linea[1].split(", ")
            respuestas.append(letra)

except:
    print("Fichero no encontrado")


notas=[]
for respuesta in respuestas:
    aciertos=0
    errores=0
    for i in range (len(respuesta)):
        print(respuesta[i], soluciones[i])
        if respuesta[i] == soluciones[i]:
            aciertos+=1
        else:
            errores+=0.30
    notas.append(aciertos-errores)

try:
    with open("C:/ProyectosGit/EjerciciosPython/Boletin_24/notas.txt","at") as cursor:
        for i in range (len(notas)):
            cursor.write(f"{alumnos[i]}: {notas[i]}\n")
except:
    print("Hubo un problema al intentar escribir el fichero")