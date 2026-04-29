try:
    serie = int(input("Ingresa un numero: "))
    with open("fibonacci.txt","wt") as f:
        if serie<2:
            print("El número debe ser mayor a 2")
        else:
            a=0
            b=1
            sucecion=f"{a}, {b}, "
            for i in range(serie-2):
                c=a+b
                if i!=serie-3 :
                    sucecion+=f"{c}, "
                else:
                    sucecion+=f"{c}"
                a=b
                b=c
            f.write(sucecion)
except ValueError:
    print("Debe ser un número")
except FileNotFoundError:
    print("Fichero no encontrado")
except:
    print("Error al intentar escribir el fichero")