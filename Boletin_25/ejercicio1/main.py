from Pokemon import Pokemon
from Equipo import Equipo

poke1=Pokemon("1","pikachu",2,4,50,80,"electrico")
poke2=Pokemon("2","charmander",2,4,50,80,"fuego","volador")
poke3=Pokemon("3","square",2,4,50,80,"agua")

equipo1=Equipo("equipo Rocket","Ash",poke1,poke2,poke3)
print(equipo1.verEquipo())