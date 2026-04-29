num=int(input("Introduce el número de la tabala que quieres generar"))
fichero="tabla-"+str(num)+".txt"
try:
    with open(fichero,"at") as f:
        for i in range(11):
            rsldo=num*i
            f.write(f"{num}X{i}={rsldo}\n")

except:
    print("No se encuentra el fichero")