"""3. Escribir un programa que acceda a un fichero (el nombre del fichero se introducirá por teclado) y
muestre por pantalla el número de palabras que contiene. El único separador válido entre palabras
es el espacio, pero podría ser que hubiese mas de un espacio seguido separando dos palabras."""

fichero=input("Introduce el nombre del fichero")

try:
    cursor=open(fichero)
    cont_palabras=0
    for linea in cursor:
        linea=linea.replace("  ","")
        linea=linea.replace("\n","")
        palabras=linea.split(" ")
        #cont_palabras+=len(palabras)
        for palabra in palabras:
            if palabra != "":
                cont_palabras+=1
    print(f"El total de palabras del fichero es {cont_palabras}")
except:
    print("El fichero no se encuentra")