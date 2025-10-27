"""10. Escribe un programa que valide si un NIF español introducido por teclado es correcto.
La longitud exacta de la cadena ha de ser de 9 caractéres. Los ocho primeros han de
ser números comprendidos entre el 0 y el 9 y el último una letra que puede estar
escrita en mayúsculas o minúsculas.
"""
"""
nif=input("Introduce su NIF ")

longitud=len(nif)
numeros=nif[:8]
letra=nif[8:]
letraMayus=letra.upper()

if longitud==9:
    if numeros.isdigit()==True:        
        if letraMayus.isalpha()==True:
            print("el NIF ingresado es correcto")
        else:
            print("el NIF ingresado es incorrecto")
    else:
        print("el NIF ingresado es incorrecto")
else:
    print("el NIF ingresado es incorrecto")
"""
"""11. Mejorar el programa anterior para que detecte si se trata de un NIF o un NIE y nos
comunique, además de si es válido de que tipo es.
Un NIE es una cadena de 9 caractéres que siempre empieza por X,Y o Z y a
continuación vienen 7 cifras y una letra final. Las letras inicial y final pueden estar
escritas con mayúsculas o con minúsculas
"""
"""
nifNie=input("Introduce su NIF/NIE ")
longitud=len(nifNie)
numerosnif = nifNie[:8]
numerosnie = nifNie[1:8]
letraFinal = nifNie[8:]
letraIncio = nifNie[0]
letraFinalMayus = letraFinal.upper()
letraIncioMayus = letraIncio.upper()


if longitud==9:
    if numerosnif.isdigit()==True:
        if letraFinalMayus.isalpha()==True:
            print("el NIF ingresado es correcto")
        else:
            print("el NIF ingresado es incorrecto")
    elif numerosnie.isdigit()==True:
        if letraFinalMayus.isalpha()==True:
            if letraIncioMayus=="X" or letraIncioMayus=="Y" or letraIncioMayus=="Z":
                print("el NIE ingresado es correcto")
            else:
                print("el NIE ingresado es incorrecto")
        else:
            print("el NIE ingresado es incorrecto")
    else:
        print("el NIF/NIE ingresado es incorrecto")
else:
    print("el NIF/NIE ingresado es incorrecto")
"""
"""14. Modifica el programa que validaba si un NIF era correcto comprobando si la letra que
incorpora lo es."""

nif=input("Introduce su NIF ")

longitud=len(nif)
numeros = nif[:8]
letra = nif[8:]
letraMayus = letra.upper()
if longitud==9:
    if numeros.isdigit()==True:
        num1=int (numeros[0])
        num2=int (numeros[1])
        num3=int (numeros[2])
        num4=int (numeros[3])
        num5=int (numeros[4])
        num6=int (numeros[5])
        num7=int (numeros[6])
        num8=int (numeros[7])
        suma=num1+num2+num3+num4+num5+num6+num7
        resto=suma%23
        restoTexto=str (resto)
        if letraMayus.isalpha()==True:

            print("el NIF ingresado es correcto")
        else:
            print("el NIF ingresado es incorrecto")
    else:
        print("el NIF ingresado es incorrecto")
else:
    print("el NIF ingresado es incorrecto")