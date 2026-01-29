print("Inicio del programa")
esCorrecto=False
"""while not esCorrecto:
    try:
        entrada = input("Introduce tu sueldo")
        sueldo= float(entrada)
        esCorrecto=True
    except ValueError:
        print("Sueldo ingresado no valido, vuelve a ingresar")
        esCorrecto=False

print(sueldo)"""

try:
    while not esCorrecto:
        entrada=input("Introduce tu sueldo")
        sueldo=float(entrada)
        esCorrecto=True
except ValueError:
    print("Sueldo ingresado no valido, vuelve a ingresar")

