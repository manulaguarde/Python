#DICCIONARIOS
#Los diccionarios tampoco tienen orden, podemos distinguir dos elementos con un papel diferente
#Un elemento es lo que se llama clave (key) y el otro valor (value)
#La clave es lo que nos permite hacer una busqueda rapida. Nos ahorra recorrer los elementos uno a uno

#La clave no se puede repertir - Si pongo una clave repetida me la sobreescribe, no la duplica

#el elemento distintivo son las llaves {} podemos crearlos de estas formas:

diccionario={}

diccionario2= dict()

print(diccionario)
print(diccionario2)

#Crear diccionario con contenido:
liga= {'equipo1':34, 'equipo2':45, 'equipo3':14,} #tanto la clave como el valor puede ser cualquier tipo (int, str, lista, char, etc)

print(liga)

#Como puedo recuperar valores en los diccionarios
print(liga['equipo1']) #como en las listas para recuperar un índice pero con la clave no el índice, y recupero el valor
print(liga.get('equipo2')) #tambien existe el método get, si no se encuentra la clave devuelve "none" por defecto

print(liga.get('equipo22','esa clave no existe')) #el metodo get permite escribir un mensaje en caso de que no exista la clave


    #la clave es el equipo                    el valor es la lista
liga2={'equipo1':[0,0,0,0,0,0,0,0], 'equipo2':[0,0,0,0,0,0,0,0], 'equipo3':[0,0,0,0,0,0,0,0]}

#Como recorreer un diccionario (recordamos que no tienen orden)
#tengo distintas maneras de recorrerlos, para recuperar solo claves, para recuperar solo valores, y para recuperar ambos

for elemento in liga: #así solo recupero las claves del diccionario
    print(elemento)

for elemento in liga: #asi recupero los valores
    print(liga[elemento])

for clave, valor in liga.items(): #asi recupero ambos, clave y valor
    print(clave,"puntos: ", valor)



