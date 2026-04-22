"""5. Tenemos un fichero llamado estadisticas.txt. El formato del fichero es el siguiente (pero el
contenido puede variar, lógicamente):
Hombre
1.73
Mujer
1.68
Mujer
1.83
Realiza un programa que lea el contenido de ese fichero y muestre el número de hombres, el
número de mujeres y la altura media (con dos decimales) de todos sin hacer distinción de sexo.
Por ejemplo, para el fichero del ejemplo anterior, la salida del programa sería esta:
Hombres: 1.
Mujeres: 2.
Estatura media: 1.75
El formato del fichero se supone correcto y comprobado y nunca va dar problemas"""

try:
    cursor=open("/home/alumno/estadisticas.txt")
    hombres=0
    mujeres=0
    estatura_media=0
    for linea in cursor:
        linea=linea.replace("\n","")
        if linea == "Hombre":
            hombres+=1
        if linea == "Mujer":
            mujeres+=1
        if linea.isdecimal():
            estatura_media+=float(linea)
    print(f"Hombres: {hombres}")
    print(f"Mujeres: {mujeres}")
    print(f"Estatura media: {estatura_media}")
except:
    print("El fichero no se encuentra")