from Cliente import Cliente
from Sucursal import Sucursal
from Cuenta import Cuenta

s1 = Sucursal("Calle A", "Madrid", 55)
s2 = Sucursal("Calle B", "Sevilla", 4444)

c1 = Cliente("Jose", "Morales", "123", "666", s1)
c2 = Cliente("Ana", "Lopez", "456", "777", s2)

cuenta1 = Cuenta("123456789012", 200.55, s1, c1)
cuenta2 = Cuenta("987654321021", 123.40, s2, c1)
cuenta3 = Cuenta("112233445566", 21.00, s2, c1, c2)

print(c1.listar_clientes())
print()
print(s2.listar_sucursales())