"""6. Queremos hacer un programa que lea un fichero con los datos de una agenda y nos diga si el
formato es correcto. La estructura del fichero es como sigue:
José María
Morales Vázquez
53
Rosa
Gómez
34
Dónde, como se ve, cada registro de la agenda está formado por tres líneas: la primera con el
nombre, la segunda con el apellido y la tercera con la edad. Nuestro programa debería de decirnos si
el formato del fichero es correcto según estas pautas o no lo es (lógicamente, lo que podemos
comprobar es que hay dos líneas de texto no numéricas seguidas de un entero y rechazar cualquier
otra cosa como incorrecta)"""

def compruebaFichero(lista):
    for i in range(len(lista)):
        if (i+1)%3==0:
            if not lista[i].isdigit():
                return False
        else:
            if lista[i].isdigit():
                return False

    return True

try:
    with open("C:/ProyectosGit/EjerciciosPython/Boletin_23/agenda.txt") as cursor:
        lista=cursor.readlines()
        lista2=[]
        for info in lista:
            info=info.replace("\n","")
            lista2.append(info)
        print(lista2)
        if compruebaFichero(lista2):
            print("El fichero es correcto")
        else:
            print("El fichero no es correcto")


except:
    print("No es posible leer el fichero")