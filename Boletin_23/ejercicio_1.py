"""1. Escribe un programa que reciba por teclado el nombre de un fichero y una palabra. Tú programa
debería de decirnos cuantas líneas tiene el fichero y cuantas veces aparece esa palabra repetida en
el fichero.
Ejemplo de ejecución (los caracteres en negrita son los que se han introducido de forma interactiva
desde el teclado):
Introduce el nombre del fichero: compra.txt
El fichero compra.txt no existe
Introduce el nombre del fichero: /home/josemaria/compra.txt
Introduce la palabra a buscar: pera
El fichero tiene 7 líneas
La palabra pera aparece 2 veces"""


fichero=input("Ingresa el nombre del fichero")
palabra=input("Ingresa la palabra a buscar")

try:
    cursor=open(fichero)
    lineas=0
    cont_palabras=0
    for linea in cursor:
        lineas+=1
        if palabra==linea:
            cont_palabras+=1

    print(f"El fichero tiene {lineas} líneas")
    print(f"La palabra {palabra} aparece 2 veces")
except:
    print(f"El fichero {fichero} no existe")









