from producto import Producto
from empleado import Empleado
from empresa import Empresa

empresa_1 = Empresa("CompuMundoHiperMegaRed")
empresa_2 = Empresa("La Mueblería")

empleado_1 = Empleado("Clark","Kent")
empleado_2 = Empleado("Peter","Parker")
empleado_3 = Empleado("Bruce","Baner")

producto_1 = Producto("PC")
producto_2 = Producto("Notebook")

empresa_1.altaEmpleado(empleado_1)
empresa_1.altaEmpleado(empleado_2)
empresa_1.altaEmpleado(empleado_3)

empresa_1.agregarProducto(producto_1)
empresa_1.agregarProducto(producto_2)

empleado_4 = Empleado("Tony","Stark")
empleado_5 = Empleado("Bruce","Wayne")
empleado_6 = Empleado("Scott","Lang")

producto_3 = Producto("Mesa")
producto_4 = Producto("Silla")

empresa_2.altaEmpleado(empleado_4)
empresa_2.altaEmpleado(empleado_5)
empresa_2.bajaEmpleado(empleado_6)

empresa_2.agregarProducto(producto_3)
empresa_2.agregarProducto(producto_4)

empresa_1.bajaEmpleado(empleado_1)
empresa_1.bajaEmpleado(empleado_2)

print(empresa_1)
print("#############################################")
print(empresa_2)