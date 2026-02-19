from datetime import date
liga={"Real Betis CF":[0,0,0,0,0,0,0],
      "Atlético de Madrid":[0,0,0,0,0,0,0],
      "Sevilla":[0,0,0,0,0,0,0],
      "Barcelona FC":[0,0,0,0,0,0,0],
      "Rayo Vallecano":[0,0,0,0,0,0,0],
      "Real Madrid FC":[0,0,0,0,0,0,0]}

def verClasificacion(liga):
    lineas="-----------------------------------------------------------------"
    longitud=len(lineas)
    hoy=date.today()
    fecha=hoy.strftime("%d-%m-%y")
    cabecera=f"Competicion: La Liga eaSports - Clasificación a día {fecha}"
    print("-----------------------------------------------------------------")
    print(" ",cabecera)
    print("-----------------------------------------------------------------")
    print(f" {'EQUIPO':<24}|{'Pts':^5}|{'PJ':^4}|{'PG':^4}|{'PE':^4}|{'PP':^4}|{'GF':^4}|{'GC':^4}")
    print("-----------------------------------------------------------------")
    for equipo, valores in liga.items():
        print(f"{equipo:<25}|{valores[0]:>5}|{valores[1]:>4}|{valores[2]:>4}|{valores[3]:>4}|{valores[4]:>4}|{valores[5]:>4}|{valores[6]:>4}")
verClasificacion(liga)

