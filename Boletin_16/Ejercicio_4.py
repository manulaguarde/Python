""" Queremos hacer el juego de piedra, papel o tijera. El usuario juega contra el ordenador y tiene
que decirnos si gana, pierde o empata. Gana el primero (ordenador o humano) que consigue
tres victorias. Hazlo de forma modular"""

import random



def batalla(ordenador, usuario):
    piedra = 0
    papel = 0
    tijera = 0
    if ordenador=="piedra"==usuario:
        piedra=1
    if ordenador=="papel"==usuario:
        papel=1
    if ordenador=="tijera"==usuario:
        tijera=1

    if usuario>ordenador:




piePapOTij=("piedra","papel","tijera")

ordenador=piePapOTij[random.randint(0,2)]
usuario=input("piedra, papel o tijera: ")


