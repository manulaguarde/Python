try:
    with open("/home/alumno/contabilidad.txt","rt") as cursor:
        ingresos=0
        gastos=0
        for linea in cursor:
            lista=linea.split(": ")
            if float(lista[1]) > 0:
                ingresos+=float(lista[1])
            else:
                gastos+=float(lista[1])

    with open("/home/alumno/resultado.txt","wt") as cursor2:
        cursor2.write(f"Ingresos: {ingresos:.2f}\n")
        cursor2.write(f"Gastos: {gastos:.2f}\n")
except:
    print("Fichero no encontrado")