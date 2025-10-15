"""
21. Escribir un programa que pida por teclado un número al usuario y calcule si es primo o no

22. Escribir un programa que genere un número primo aleatorio entre el 10.000.000 y el
50.000.000

23. Escribir un programa que te escriba todos los números primos que hay entre el 1 y el 100

24. Modifica el programa anterior para que sea el usuario quién introduzca dos números y se nos
muestre los primos que hay entre ambos

25. Escribir un programa que reciba por teclado un número y muestre sucesivamente el
resultado de ir dividiéndolo por dos sucesivamente hasta llegar a un número igual o menor a
1. Caso de ser necesario los resultados se mostrarán con dos decimales. Un ejemplo de una
ejecución correcta después de introducir el número 34 ser´ía esta:
Haz introducido el número 34
17
8.5
4.25
2.12
1.06
0.53
"""
import random

"""#21
num = int(input("Ingrese un numero: "))
i=1
j=1
for i in range (num,i,-1):
    if (num%i==0):
        j+=1
        #print(i)
if (j==2):
    print(num,"es primo")
else:
    print(num,"no es primo")"""

#22
#num = random.randint(10000000,50000000)
i=1
num=1
primo=0
while(primo!=num):
    num = random.randint(10, 50)
    j=0
    for i in range (1,num):
        if(num%i==0):
            j+=1
    if(j==2):
        primo=num
print(num)
