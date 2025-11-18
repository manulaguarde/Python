"""Escribir un programa que nos pida una cadena por teclado y luego cuente cuantas
palabras hay en ella con cuatro o más vocales diferentes. Por ejemplo, si introducimos
la frase “Crisis constitucional por culpa del murcielago guineoecuatorial” Nos debería de
decir que 3. Tendrías que tener en cuenta que las vocales pueden ir en mayúsculas o no
y son la misma letra. Presupón que ninguna vocal va acentuada de ninguna forma."""

frase=input("Introduce una frase: ").lower()
listaFrase=frase.split()
vocalesDiferentes=[0]
vocales= "aeiou"
contador=0
for palabra in listaFrase:
    for vocal in palabra:
        if vocal not in vocalesDiferentes:
            if vocal in vocales:
                vocalesDiferentes.append(vocal)
                if len(vocalesDiferentes)>3:
                    contador+=1
print(contador)


