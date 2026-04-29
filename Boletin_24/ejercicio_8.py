origen="origen.txt"
destino="destino.txt"

try:
    with open(origen, "rt",encoding='utf-8') as r:
        for line in r:
            dato = True
            line=line.strip()
            lineas=line.split(";")
            if len(lineas)!=3:
                dato=False
            else:
                nombre=lineas[0].split(", ")
                if len(nombre)!=2:
                    dato=False
                else:
                    if not nombre[0].isalpha() and not nombre[1].isalpha():
                        dato=False
                    trabajo=lineas[1].replace(" ", "")
                    if not trabajo.isalnum():
                        dato=False
                    salario=lineas[2].replace(".", "")
                    if not salario.isdigit():
                        dato=False
                    if dato:
                        with open(destino, "at") as w:
                            w.write(line+"\n")
except:
    print("El fichero no existe")