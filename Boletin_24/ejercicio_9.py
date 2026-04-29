edades=[]
trabajador_con_edad=""
fichero="destino.txt"
try:
    with open(fichero,"rt",encoding='latin-1') as cursor:
        for line in cursor:
            line = line.strip()
            lista=line.split(";")
            nombre=lista[0].split(", ")
            #edades.append(input(f"{nombre[1]} {nombre[0]}. Cuál es su edad?: "))
            edad=input(f"{nombre[1]} {nombre[0]}. Cuál es su edad?: ")
            while int(edad)<18 or int(edad)>67:
                print("la edad no puede ser menor a 18 o mayor que 67 años, vuelva a ingresar")
                edad = input(f"{nombre[1]} {nombre[0]}. Cuál es su edad?: ")
            trabajador_con_edad += line+";"+edad+"\n"

    with open(fichero,"wt") as cursor:
        cursor.write(trabajador_con_edad)

except FileNotFoundError:
    print("No se encuentra el archivo")


