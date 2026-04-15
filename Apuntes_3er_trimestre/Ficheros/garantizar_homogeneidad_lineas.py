try:
    cursor=open("/home/alumno/fichero2.txt","rt")
    profesores=[]
    alumnos=[]
    for linea in cursor:
        contenido=linea.split(":")
        contenido[1]=contenido[1].replace("\n","")
        contenido[0]=contenido[0].strip()
        contenido[1]=contenido[1].strip()
        if contenido[0]=="Alumno":
            alumnos.append(contenido[1])
        elif contenido[0]=="Profesor":
            profesores.append(contenido[1])
    cursor.close()
    print(profesores)
    print(alumnos)
except:
    print("Error al abrir fichero")