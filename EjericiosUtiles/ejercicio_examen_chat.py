def titulo_mas_largo(lista_peliculas):
    titulos_largos = []
    vocales="aeiouáéíóú"

    for pelicula in lista_peliculas:
        contador_vocales = 0
        if len(pelicula["titulo"])>10:
            for letra in pelicula["titulo"]:
                if letra in vocales:
                    contador_vocales+=1
            if contador_vocales>0:
                titulos_largos.append(pelicula["titulo"])

    return titulos_largos


    return titulos_largos

def menor_nota(lista_peliculas):
    nota=10
    tupla=()
    for pelicula in lista_peliculas:
        if float(pelicula["nota"])<nota:
            nota=float(pelicula["nota"])
            tupla=(pelicula["titulo"],pelicula["nota"])
    return tupla

def mayor_nota(lista_peliculas):
    nota=0
    tupla=()
    for pelicula in lista_peliculas:
        if float(pelicula["nota"])>nota:
            nota = float(pelicula["nota"])
            tupla=(pelicula["titulo"],pelicula["nota"])
    return tupla

def calcula_nota_media_por_pelicula(lista_peliculas,generos):
    notas_por_genero={}
    for genero in generos.keys():
        suma_nota=0
        contador=0
        for pelicula in lista_peliculas:
            if genero == pelicula["genero"]:
                suma_nota += float(pelicula["nota"])
                contador +=1
        notas_por_genero[genero]=round(suma_nota/contador,2)

def nota_media_global(lista_peliculas):
    notas=[]
    for pelicula in lista_peliculas:
        notas.append(float(pelicula["nota"]))

    return sum(notas)/len(notas)

lista_de_peliculas=[]
try:
    with open("peliculas.txt","rt") as cursor:


        for linea in cursor:
            linea = linea.strip()
            lista=linea.split(";")
            lista_de_peliculas.append({"id":lista[0],
                                       "titulo":lista[1],
                                       "genero":lista[2],
                                       "nota":lista[3]})

except FileNotFoundError:
    print("archivo no encontrado")

generos={}
for pelicula in lista_de_peliculas:
    if pelicula["genero"] not in generos.keys():
        generos[pelicula["genero"]]=[pelicula["titulo"]]
    else:
        generos[pelicula["genero"]].append(pelicula["titulo"])



try:
    with open("resumen.txt","at") as cursor:
        mejor_pelicula=mayor_nota(lista_de_peliculas)
        peor_pelicula=menor_nota(lista_de_peliculas)
        media=nota_media_global(lista_de_peliculas)
        cursor.write(f"Número total de películas: {len(lista_de_peliculas)}\n")
        cursor.write(f"Mejor película: {mejor_pelicula[0]}\n")
        cursor.write(f"Peor película: {peor_pelicula[0]}\n")
        cursor.write(f"Nota media global: {round(media,2)}")
except:
    print("No se ha podido encontrar el archivo")

try:
    with open("rating.txt","at") as cursor:
        notas=[]
        for pelicula in lista_de_peliculas:
            notas.append(float(pelicula["nota"]))

        notas_ordenadas=sorted(notas,reverse=True)
        cursor.write("Raiting de mas puntuada a menos puntuada:\n")
        for nota in notas_ordenadas:
            for pelicula in lista_de_peliculas:
                if nota == float(pelicula["nota"]):
                    cursor.write(pelicula["titulo"]+"\n")

except:
    print("No se ha podido encontrar el archivo")