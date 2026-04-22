"""2. Escribe una función que nos cuente el número de líneas y de caracteres que hay en un fichero. La
llamada a la función debería de ser como esta:
estadisticas(“fichero1.txt”)
Suponiendo que el contenido del fichero sea este:
uno
dos y dos
tres
La salida por consola de tu programa debería de ser la siguiente:
Número de líneas: 4
Líneas en blanco: 1
Cantidad de caracteres sin contar los espacios: 14
Cantidad de espacios: 2"""

def estadisticas(fichero):

    try:
        cursor = open(fichero)
        num_lineas=0
        lineas_en_blanco=0
        cant_caracteres=0
        cant_espacios=0
        for lineas in cursor:
            lineas=lineas.strip()
            lineas=lineas.replace("\n","")
            num_lineas+=1
            if lineas=="":
                lineas_en_blanco+=1
            for caracter in lineas:
                if caracter!=" ":
                    cant_caracteres+=1
                else:
                    cant_espacios+=1

        print(f"Número de líneas: {num_lineas}")
        print(f"Líneas en blanco: {lineas_en_blanco}")
        print(f"Cantidad de carácteres sin contar los espacios: {cant_caracteres}")
        print(f"Cantidad de espacios: {cant_espacios}")
    except:
        print("Fichero no encontrado")


estadisticas("/home/alumno/fichero1.txt")