from producto import Producto
from empleado import Empleado

class Empresa:
    # Constructores
    def __init__(self,razonSocial):
        self.__razonSocial = razonSocial
        self.__productos = []
        self.__empleados = []

    # Comandos
    def establecerRazonSocial(self, razonSocial):
        self.__razonSocial = razonSocial

    def agregarProducto(self, producto):
        self.__productos.append(producto)

    def removerProducto(self,producto):
        if producto in self.__productos: 
            self.__productos.remove(producto)
            
    def altaEmpleado(self, empleado):
        # 1. Obtener todos los legajos existentes
        legajos = []
        for emp in self.__empleados:
            legajos.append(emp.obtenerNumeroLegajo())

        # 2. Calcular el siguiente número de legajo
        if legajos:
            nuevo_legajo = max(legajos) + 1
        else:
            nuevo_legajo = 1  # Primer legajo de la empresa

        # 3. Asignar el nuevo legajo y el estado de ALTA al empleado
        empleado.establecerNumeroLegajo(nuevo_legajo)
        empleado.establecerEstado(Empleado.ESTADO_ALTA)

        # 4. Agregar el empleado a la lista
        self.__empleados.append(empleado)
            
    def bajaEmpleado(self, empleado):
        if empleado in self.__empleados:
            empleado.establecerEstado(empleado.ESTADO_BAJA)

    # Consultas
    def obtenerRazonSocial(self):
        return self.__razonSocial

    def obtenerProductos(self):
        return self.__productos

    def obtenerEmpleadosDeAlta(self):
        empleados_alta = []
        for emp in self.__empleados:
            if emp.obtenerEstado() == emp.ESTADO_ALTA:
                empleados_alta.append(emp)
        return empleados_alta

    def obtenerEmpleadosHistorico(self):
        return self.__empleados

    def __str__(self):
        prods = (
            "\n".join([f"  - {p}" for p in self.obtenerProductos()])
            if self.obtenerProductos()
            else "  (Sin productos)"
        )

        emps = (
            "\n".join([f"  - {e}" for e in self.obtenerEmpleadosDeAlta()])
            if self.obtenerEmpleadosDeAlta()
            else "  (Sin empleados)"
        )


        return f"Nombre de la empresa: {self.__razonSocial}\n Empleados:\n{emps}\n Producos:\n{prods}"

    def __eq__(self,otro):
        if isinstance(otro,Empresa):
                    return self.__razonSocial == otro.__razonSocial
        return False

