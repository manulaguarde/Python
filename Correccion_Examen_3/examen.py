import random
jugadores={}
numJugadores=456
columnas=12

def inicializaJuego(jugadores,numJugadores):
    for i in range (numJugadores):
        jugador=i+1
        jugadores[jugador]="vivo"

def eliminaJugador(jugadores,cant):
    if len(jugadores)>cant:
        for i in range (cant):
            eliminado=random.choice(list(jugadores.keys()))
            jugadores.pop(eliminado,None)
        if len(jugadores)==1:
            print("Queda un solo jugador!")
        else:
            print(f"Se han eliminado {cant} jugadores, quedan solamente {len(jugadores)}" )
    else:
        print("No quedan tantos jugadores para eliminar")

def visualizarTablero(jugadores, columnas):
    print("-------------------------------------------------------------------")
    print(f"quedan {len(jugadores)} jugadores")
    print("--------------------------------------------------------------------")
    k=1
    for i in range (35):
        for j in range(columnas+1):
            if jugadores[k]=="vivo":
                print(f"{k:03}",end=" ")
            else:
                print(f"---",end=" ")

            k+=1
        print()

inicializaJuego(jugadores,numJugadores)
#print(jugadores)
visualizarTablero(jugadores, columnas)
eliminaJugador(jugadores,150)
print(len(jugadores))
eliminaJugador(jugadores,150)
print(len(jugadores))
visualizarTablero(jugadores, columnas)
eliminaJugador(jugadores,200)
print(len(jugadores))
eliminaJugador(jugadores,105)