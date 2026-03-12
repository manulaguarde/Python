from pokemon import Pokemon, PokemonLegendario #del archivo pokemon importamos la clase Pokemon y la clase PokemonLegendario

poke1=Pokemon(13,"Pikachu","Eléctrico")
#print(poke1.nombre)
poke2=Pokemon(56,"Charmander","Fuego","Volador")

poke1.verPokemon()
poke2.verPokemon()
Pokemon.coleccion()
poke3=PokemonLegendario(150,"MewTwo","Psíquico")
poke3.verPokemon()