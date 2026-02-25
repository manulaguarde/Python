"""EJERCICIO CON FORMATO DE EXAMEN
Escribir un programa que reciba un texto y devuelva un diccionario o una estructura similar donde las
palabras del texto serán las claves y el número de veces que aparece cada una de ellas su valor.
Considera que la frase que introducimos no tiene signos de puntuación, que el único separador entre
palabras son los espacios y no tengas en cuenta las tildes ni mayúsculas. Es decir: “qué” se
considera una palabra diferente de “que” y “Como” es distinta de “como”.
El texto debe de introducirse desde el teclado
EJEMPLO DE EJECUCIÓN:
Introduce tu texto: Como quieres que te quiera si el que quiero que me quiera no me quiere
como quiero que me quiera
Diccionario: {'Como': 1, 'quieres': 1, 'que': 4, 'te': 1, 'quiera': 3, 'si': 1, 'el': 1, 'quiero': 2, 'me': 3,
'no': 1, 'quiere': 1, 'como': 1}
"""

texto=input("Introduce tu texto: ")
textoLista=texto.split()
textoConjunto=set(textoLista)
textoSinrepetir=list(textoConjunto)
contadorLista=[]
diccionario={}
for palabra in textoSinrepetir:
    contador = 0
    for palab in textoLista:
        if palab == palabra:
            contador += 1
    contadorLista.append(contador)

for i in range (len(contadorLista)):
    diccionario[textoSinrepetir[i]] = contadorLista[i]

for palabra in diccionario:
    print(palabra, diccionario[palabra])


