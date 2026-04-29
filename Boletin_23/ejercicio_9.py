def alumno_nerd(notas):
    for nota in notas:
        if float(nota) < 5:
            return False
    return True

def muestra_notas(fichero):
    alumnos_aprobados=[]
    notas_alumnos=[]
    debe_ra1=[]
    debe_ra2 = []
    debe_ra3 = []
    debe_ra4 = []
    debe_ra5 = []
    modulo=fichero.replace('.txt','')
    try:
        with open(fichero, 'r') as f:
            for line in f:
                line=line.strip()
                line=line.replace('\n','')
                alumno, notas = line.split(": ")
                lista_notas = notas.split(", ")
                if alumno_nerd(lista_notas):
                    alumnos_aprobados.append(alumno)
                else:
                    i=1
                    for nota in lista_notas:
                        if float(nota) < 5:
                            if i==1:
                                debe_ra1.append(alumno)
                            if i==2:
                                debe_ra2.append(alumno)
                            if i==3:
                                debe_ra3.append(alumno)
                            if i==4:
                                debe_ra4.append(alumno)
                            if i==5:
                                debe_ra5.append(alumno)
                        i+=1

                """alumnos.append(alumno)
                lista_notas=notas.split(", ")
                notas_alumnos.append(lista_notas)"""
            print(f"Modulo: {modulo}")
            print("Alumnos con todo aprobado:")
            for alumno in alumnos_aprobados:
                print(alumno)
            print("Resultados de aprendizaje y alumnos suspensos:")
            print("RA1:",end="")
            for alumno in debe_ra1:
                print(alumno, end=", ")
            print()
            print("RA2:",end="")
            for alumno in debe_ra2:
                print(alumno, end=", ")
            print()
            print("RA3:",end="")
            for alumno in debe_ra3:
                print(alumno, end=", ")
            print()
            print("RA4:",end="")
            for alumno in debe_ra4:
                print(alumno, end=", ")
            print()
            print("RA5:",end="")
            for alumno in debe_ra5:
                print(alumno, end=", ")



    except:
        print("Error al abrir el archivo")

muestra_notas("Redes.txt")