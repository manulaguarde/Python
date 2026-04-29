num=int(input("Ingresa el número de la tabla que quieres ver"))
fichero=f"tabla-{num}.txt"
try:
    with open(fichero,"rt") as f:
        print(f.read())
except:
    print(f"Fichero de la tabla del {num} no encontrado")