"""Tenemos una lista con cadenas de texto que, previsiblemente, deberían de ser fechas en formato
dd/mm/yy. Por ejemplo esta:
[“13/02/25”, “hola carmela”, “12 34 56”, “14/06/2026”, “bra, bra”,
“56/13/26”]
La lista puede ser esa o cualquier otra. Usa excepciones para separar las que se trata de fechas correctas de
las que no lo son y muéstrales en consola. Por ejemplo así:
Fechas correctas:
“13/02/25”
“14/06/2026”
Fechas incorrectas:
“hola carmela”
“12 34 56”
“bra, bra”,
“56/13/26”"""

from datetime import date,datetime

lista=["13/02/25", "hola carmela", "12 34 56", "14/06/2026", "bra,bra" ,"56/13/26"]

def compruebaFechas():
    for fecha in lista:
        try:
            convierteAFecha=datetime.strptime(fecha,"%d/%m/%Y")
            print(convierteAFecha)
        except:
            print(fecha)



#fecha=input("Ingresa una fecha en formato dd/mm/aaaa o /aa")
compruebaFechas()