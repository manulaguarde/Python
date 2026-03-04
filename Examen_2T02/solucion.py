import random

def inicializaJuego(diccionario, num):
    for i in range(1,num+1):
        diccionario[i] = ACTIVO

def numJugadoresActivos(diccionario):
    num = len(diccionario)
    activos = 0
    for i in range(1, num+1):
        if diccionario[i] == ACTIVO:
            activos+=1
    return activos

def verJugadores(diccionario,cols):
    num = len(diccionario)
    activos = numJugadoresActivos(diccionario)
    print("-------" * cols)
    if activos == 1:
        print(f"Jugadores activos: {activos:d}. El juego ha terminado")
    else:
        print(f"Jugadores activos: {activos:d}")
    print("-------" * cols)
    for i in range(1, num+1):
        if diccionario[i] == INACTIVO:
            print("  ---  ", end="")
        else:
            print(f"  {i:03d}  ", end="")
        if i % cols == 0:
            print()
    print("-------" * cols)

def eliminarJugadores(diccionario,eliminados):
    num = 0
    activos = numJugadoresActivos(diccionario)
    if activos<= eliminados:
        print(f"¡No puedo eliminar a {eliminados:d} jugadores! Ahora mismo quedan {activos:d} activos. ¡Nos quedamos sin ganador!")
    else:
        print(f"Vamos a eliminar a {eliminados:d} jugadores.")
        while num < eliminados:
            azar = random.randint(1,456)
            if diccionario[azar] == ACTIVO:
                diccionario[azar] = INACTIVO
                num+=1
        if activos-eliminados == 1:
            print(f"Queda un solo jugador activo. ¡Ya tenemos ganador!")
        else:
            print(f"Quedan {activos-eliminados:d} jugadores activos")

# se valorará mas si lo haces con un diccionario
jugadores = {}
# pero si te sientes mas seguro puedes hacerlo con una lista
#jugadores=[]
# número de jugadores
numJugadores = 456
# columnas del tablero de jugadores
columnas = 12

ACTIVO = True
INACTIVO = False

# inicializa los datos de tu lista o de tu diccionario
inicializaJuego(jugadores, numJugadores)
# muestra el tablero con los jugadores en consola deberían de aparecer los 456
# ya que aún no hay ningún eliminado
verJugadores(jugadores, columnas)
# elimina 150 jugadores al azar
eliminarJugadores(jugadores, 200)
# mostramos de nuevo el tablero. ahora ya hay jugadores eliminados
verJugadores(jugadores, columnas)
# elimina 200 jugadores al azareliminarJugadores(jugadores, 200)
eliminarJugadores(jugadores, 150)
# trata de eliminar otros 200 jugadores al azar, pero no puede porque no quedan tantos
eliminarJugadores(jugadores, 200)
#elimina 105 jugadores. Ya sólo queda 1. Tenemos ganador
eliminarJugadores(jugadores, 105)
# muestra por última vez el tablero de jugadores. Sólo puede quedar uno
verJugadores(jugadores, columnas)


