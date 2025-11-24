"""Vamos a hacer una implementación del juego del buscaminas y lo primero es preparar el
tablero. Genera un array de dos dimensiones de 5 filas por 5 columnas. El tablero
tendrá 5 minas que se colocaran de forma aleatoria en cinco posiciones del array. Las
minas se representarán con un 1 y las posiciones sin mina con un 0."""

import random

tablero=[]

for i in range(5):
    fila=[]
    for j in range(5):
        fila.append(0)
    tablero.append(fila)

for _ in range(5):   # repetimos 5 veces
    fila_random = random.randint(0, 4)
    col_random = random.randint(0, 4)

    while tablero[fila_random][col_random] == 1:
        fila_random = random.randint(0, 4)
        col_random = random.randint(0, 4)

    tablero[fila_random][col_random] = 1

for fila in tablero:
    for numero in fila:
        print(str(numero),end=" ")
    print()


