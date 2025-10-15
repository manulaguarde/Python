"""1. Escribir un programa donde se muestren los 10 primeros números enteros

2. Escribir un programa donde se muestren los 50 primeros números pares

3. Escribir un programa donde se muestren los 5 primeros números múltiplos de uno dado por
el usuario (se introducirá por teclado)

4. Escribir un programa donde se muestren todos los números divisibles por 7 menores a
10000

5. Escribir un programa que pida por teclado un número al usuario y diga si es par o impar"""

# 1

"""for i in range (1,10):
    print (i)
print ("FIN")"""

#2

"""for i in range (0,51,2):
    print (i)
print ("FIN")"""

#3

num = int(input("Introduce un numero "))
i = num
resultado=num%i
for i in range (i,5, resultado):

    if(resultado == 0 ):
        print (i)



#4
"""
i=10000
for i in range(i,1,-1):
    resultado = i % 7

    if resultado==0 :
        print(i)
"""

#5
"""num = int(input("Introduce un numero"))

if (num%2==0):
    print (num, "es par")
else:
    print (num, "no es par")"""
