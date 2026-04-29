#ejercicio 1
texto = "  Python es Genial para Programar  "
texto=texto.strip().lower().replace("genial","potente")
print(texto)

#ejercicio 2
cadena="hola que tal"
diccionario_vocales={"a":0,"e":0,"i":0,"o":0,"u":0}
for caracter in cadena:
    if caracter in diccionario_vocales:
        diccionario_vocales[caracter]+=1

print(diccionario_vocales)

#ejercicio 3
frase = "python java python c++ java python"

cuenta_palabras={}
lista=frase.split(" ")
for palabra in lista:
    if palabra not in cuenta_palabras:
        cuenta_palabras[palabra]=1
    else:
        cuenta_palabras[palabra]+=1

print(cuenta_palabras)

#ejercicio 4
def convierte_capitalize(lista):
    nombres_capitalize=[]
    for nombre in lista:
        nombres_capitalize.append(nombre.capitalize())

    return nombres_capitalize

nombres = ["ana", "juan", "pedro", "maria"]
print(convierte_capitalize(nombres))

#ejercicio 5
lista=["manzana","ananas","uva","pera","Banana","Sandía","Espinaca"]
vocales="aeiouAEIOU"
for dato in lista:
    if len(dato)>5:
        if dato[0].lower() in vocales:
            print(dato)

#ejercicio 6
numeros = [1, 2, 2, 3, 4, 4, 4, 5]
num_repetidos={}
for num in numeros:
    if num not in num_repetidos:
        num_repetidos[num]=1
    else:
        num_repetidos[num]+=1

print(num_repetidos)

#ejercicio 7
alumnos = {
    "Ana": [7, 8, 9],
    "Juan": [5, 6, 4],
    "Maria": [10, 9, 9]
}

media_alumno={}
for alumno,notas in alumnos.items():
    media_alumno[alumno]=round(sum(notas)/len(notas),2)

print(media_alumno)

#ejercicio 8
try:
    with open("texto.txt","rt") as cursor:
        contar_palabras={}
        for linea in cursor:
            linea=linea.strip()
            palabras=linea.split(" ")
            for palabra in palabras:
                if palabra not in contar_palabras:
                    contar_palabras[palabra]=1
                else:
                    contar_palabras[palabra]+=1
    with open("resultado.txt","wt") as cursor:
        for palabra,cantidad in contar_palabras.items():
            cursor.write(palabra+": "+str(cantidad)+"\n")
except FileNotFoundError:
    print("archivo no encontrado")

#ejercicio 9 y 10

def muestra_mas_pesonas_por_ciudad(diccionario):
    ciudades=list(diccionario.keys())
    ciudad_mas_grande=ciudades[0]
    for ciudad, habitantes in diccionario.items():
        if len(habitantes)>len(diccionario[ciudad_mas_grande]):
            ciudad_mas_grande=ciudad

    return ciudad_mas_grande

try:
    with open("usuarios.txt","rt") as cursor:
        usuarios_por_ciudad={}
        for linea in cursor:
            linea=linea.strip()
            palabras=linea.split(";")
            if palabras[2] not in usuarios_por_ciudad:
                usuarios_por_ciudad[palabras[2]]=[palabras[0]]
            else:
                usuarios_por_ciudad[palabras[2]].append(palabras[0])
        print(f"La ciudad con más habitantes es: {muestra_mas_pesonas_por_ciudad(usuarios_por_ciudad)}")
except FileNotFoundError:
    print("archivo no encontrado")