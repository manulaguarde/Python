def dar_la_vueta(fichero1,fichero2):
    try:
        lineas_al_reves=[]
        with open(fichero1,"rt") as f:
            for linea in f:
                linea=linea.strip()
                al_reves=linea[::-1]
                lineas_al_reves.append(al_reves)
        with open( fichero2,"at") as f2:
            i=len(lineas_al_reves)
            while i>0:
                f2.write(lineas_al_reves[i-1]+"\n")
                i-=1
    except:
        print("Fichero no encontrado")

dar_la_vueta("fich_normal.txt","fich_al_reves.txt")