meses = [
    "enero", "febrero", "marzo", "abril", "mayo", "junio",
    "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"
]

from datetime import datetime

hoy = datetime.now()
print(hoy)
print(meses[hoy.month - 1])

#fString

precio = 12.56789
print(f"{precio:.2f}")   # 12.57

numero = 7
print(f"{numero:03}")   # 007

from datetime import datetime

hoy = datetime.now()
print(f"Hoy es {hoy:%d/%m/%Y}")
print(f"{hoy:%A %d de %B de %Y}")

empleados = {
    "123A": ("Ana López", 2350.456, 5),
    "456B": ("Carlos Ruiz", 1800.5, 12),
    "789C": ("María Gómez", 3200.7, 2)
}

for dni, datos in empleados.items():
    #Muy útil!!!!
    nombre, salario, años = datos

    categoria = "Veterano" if años > 5 else "Junior"

    print(f"{nombre:<15} | {salario:>10,.2f} € | {categoria}")

#diccionarios

persona = {
    "nombre": "Ana",
    "edad": 25,
    "ciudad": "Madrid"
}
print(persona.get("telefono", "No existe"))

alumnos = {}

for i in range(4):
    nombre = input("Nombre del alumno: ")
    notas = []

    for j in range(3):
        nota = float(input("Nota: "))
        notas.append(nota)

    alumnos[nombre] = notas

mayor_media = 0
mejor_alumno = ""
aprobados = 0

for nombre, notas in alumnos.items():
    media = sum(notas) / len(notas)
    print(f"{nombre} tiene media {media:.2f}")

    if media > mayor_media:
        mayor_media = media
        mejor_alumno = nombre

    if media >= 5:
        aprobados += 1

print(f"Mejor alumno: {mejor_alumno}")
print(f"Aprobados: {aprobados}")

#CONJUNTOS
numeros = {1, 2, 2, 3, 3, 3}
print(numeros)
#Eliminar en conjuntos
numeros.discard(3)  # no da error si no existe
#con pop se puede pero es aleatorio

#para ordenar en un conjunto
for n in sorted(numeros):
    print(n)

ingles = set(range(1, 21))
frances = set(range(13, 28))

solo_ingles = ingles - frances
solo_frances = frances - ingles
ambos = ingles & frances
al_menos_uno = ingles | frances

total = 30
ninguno = total - len(al_menos_uno)


A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

if 3 in A:
    print("Está en el conjunto")