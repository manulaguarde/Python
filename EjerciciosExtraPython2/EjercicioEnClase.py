"""Quiero obtener un listado con nombre de pila y el siguiente formato:
 Ines Rosales (20)
 José María Morales (55)
 Pepe potamo (44)"""
clientes={"Potamo,Pepe":44, "Morales,José María":55,"Rsosales,Inés":20}

"""nombres=clientes.keys()
nombresPila=[]
for nombre in nombres:
    nomYap=nombre.split(",")
    nombresPila.append(nomYap[1])
    nombresPila.append(nomYap[0])
    nombresPila.append(clientes[nombre])
    nombresPila.append(f"{nomYap[1]} {nomYap[0]} ({clientes[nombre]})")"""


lista = []

for nombre_completo in clientes:
    print(nombre_completo)
    #apellido, nombre=nombre_completo.split(",")
    nombre = nombre_completo.split(",")
    edad = clientes[nombre_completo]
    lista.append((nombre[1], nombre[0], edad))  # primero nombre

lista.sort()  # ordena por el primer elemento de la tupla

for nombre, apellido, edad in lista:
    print(f"{nombre} {apellido} ({edad})")