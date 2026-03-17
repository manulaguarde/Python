from Conductor import Conductor
from Coche import Coche
from Moto import Moto

conductor1=Conductor("José María Morales","123456789e",1967,1986,10)
conductor2=Conductor("Ines Perado","987654321f",2008,2025,8)

coche1=Coche("6310NXB",2024,conductor1)
moto1=Moto("6309NXB",2025,conductor2)

print(coche1.mostrar_vehiculo())
print(moto1.mostrar_vehiculo())
