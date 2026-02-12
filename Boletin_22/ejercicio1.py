from datetime import date,datetime

liga=[["Real Betis CF",0,0,0,0,0,0,0],
      ["Atlético de Madrid",0,0,0,0,0,0,0],
      ["Sevilla",0,0,0,0,0,0,0],
      ["Barcelona FC",0,0,0,0,0,0,0],
      ["Rayo Vallecano",0,0,0,0,0,0,0],
      ["Real Madrid FC",0,0,0,0,0,0,0],]
def resultadosPartido():
    pass
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
    for equipo in liga:
        print(f"{equipo[0]:<25}|{equipo[1]:>5}|{equipo[2]:>4}|{equipo[3]:>4}|{equipo[4]:>4}|{equipo[5]:>4}|{equipo[6]:>4}|{equipo[7]:>4}")
verClasificacion(liga)