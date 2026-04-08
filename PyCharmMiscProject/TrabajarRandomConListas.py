import random

lista=["Manuel", "pepe", "Luis", "Maria"]
lita2=[]

print(random.choice(lista))#elijo un elemento al azar de la lista
lista2=random.sample(lista,3)#elijo 3  elemntos al azar de la lista sin repetir
random.shuffle(lista)#reordena la lista al azar
print(lista)

print(lista2)

