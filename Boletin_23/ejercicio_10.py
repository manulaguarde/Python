try:
    with open("fichero.txt") as cursor:
        lineas = [l.strip() for l in cursor if l.strip()]
        datos_validos=0
        datos_invalidos=0
        lista_valida=[]
        for dato in lineas:
            dato_num=dato.replace(".","")
            if dato_num.isdigit():
                datos_validos+=1
                lista_valida.append(float(dato))
            else:
                datos_invalidos+=1

        print(f"Número de datos válidos: {datos_validos}")
        print(f"Número de datos inválidos: {datos_invalidos}")
        print("Mínimo:", min(lista_valida))
        print("Máximo:", max(lista_valida))
        print("Media aritmética:",sum(lista_valida)/len(lista_valida))
except:
    print("Fichero no encontrado")