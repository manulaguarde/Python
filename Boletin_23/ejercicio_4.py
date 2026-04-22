"""Crea una función que se llame compararFicheros y que reciba como argumento el nombre de dos
ficheros de texto. La función debería de devolver un valor booleano indicando si el contenido de
ambos ficheros es exactamente el mismo o no.
Ejemplo de ejecución:
if compararFicheros(“fichero1.txt”, “fichero2.txt”):
print(“El contenido de los ficheros es el mismo”)
else:
print(“El contenido de los ficheros no es el mismo”)"""

def compararFicheros(fich1,fich2):
    cursor1=open(fich1)
    cursor2=open(fich2)
    fichero1=cursor1.read()
    fichero2=cursor2.read()
    if fichero1 == fichero2:
        return True

    return False


try:
    if compararFicheros("/home/alumno/fiasdf.txt","/home/alumno/fichero1.txt"):
        print("El contenido de los ficheros es el mismo")
    else:
        print("El contenido de los ficheros no es el mismo")
except:
    print("Alguno de los ficheros no se encuentra")