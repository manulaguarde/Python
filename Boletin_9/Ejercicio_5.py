"""Escribir un programa que guarde en un diccionario los precios de las frutas de la siguiente tabla:
Fruta     Precio (€/Kg)
Aguacate  4.35
Mandarina 2.60
Kiwi      3.75
Naranja   1.80
NOTA: El diccionario debes de crearlo en el código del programa con los datos listados en la tabla
Tú programa debe de preguntar al usuario por una fruta y un número de kilos y mostrar por pantalla el
precio de ese número de kilos de fruta con dos decimales. El número de kilos debe de admitir
decimales. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello. Captura
las posibles excepciones.
El programa finalizará cuando se escriba la palabra fin (de forma insensible a mayúsculas y/o
minúsuculas)
EJEMPLO DE EJECUCIÓN:
¿Qué fruta quieres comprar? Sandía
Lo siento mucho pero no vendemos esa fruta
¿Qué fruta quieres comprar? Kiwi
¿Cuantos kilos quieres? ff
No has introducido bien la cantidad que quieres
¿Qué fruta quieres comprar? Mandarina
¿Cuantos kilos quieres? 4.75
4.75 de Mandarina cuestan 12.35 €
¿Qué fruta quieres comprar? fin
"""

tienda={"Aguacate": 4.35,
        "Mandarina": 2.60,
        "Kiwi": 3.75,
        "Naranja" :1.80 }


fruta="hola"


while fruta.lower() != "fin":
    fruta = input("¿Qué fruta quieres comprar? ")
    if fruta in tienda:
        try:
            kilos=float(input("Cuantos kilos quieres? "))
        except ValueError:
            print("No has introducido bien la cantidad que quieres")
        else:
            print(f"{kilos} de {fruta} cuentan {round(kilos*tienda[fruta],2)}€")
    elif fruta.lower() != "fin":
        print("Lo siento mucho pero no vendemos esa fruta")