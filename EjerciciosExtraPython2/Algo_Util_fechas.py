meses = [
    "enero", "febrero", "marzo", "abril", "mayo", "junio",
    "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"
]

from datetime import datetime

hoy = datetime.now()
print(hoy)
print(meses[hoy.month - 1])