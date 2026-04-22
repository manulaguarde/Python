try:
    cursor=open("/home/alumno/fichero2.txt","rt")
    profesores=[]
    alumnos=[]
    for linea in cursor:
        contenido=linea.split(": ")
        contenido[1]=contenido[1].replace("\n","") #esta forma es más segura para quitar el último carácter porque si está lo elimina, sino está, no sucede nada
        if contenido[0]=="Alumno":
            #alumnos.append(contenido[1][:-1]) #eliminamos el último carácter ("\n") pero nos tenémos que asegurar que todas las líneas tengan ese carácter
            alumnos.append(contenido[1])

        else:
            #profesores.append(contenido[1][:-1])
            profesores.append(contenido[1])
    cursor.close()
    print(profesores)
    print(alumnos)
except:
    print("Error al abrir fichero")