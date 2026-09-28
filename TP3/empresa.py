from producto import Producto
from empleado import Empleado

class Empresa:
    # Constructores
    def __init__(self,razonSocial):
        self._razonSocial = razonSocial
        self._productos = []
        self._empleados = []

    # Comandos
    def establecerRazonSocial(self, razonSocial):
        self._razonSocial = razonSocial

    def agregarProducto(self, producto):
        self._productos.append(producto)

    def removerProducto(self,producto):
        if producto in self._productos: 
            self._productos.remove(producto)
            
    def altaEmpleado(self, empleado):
        # 1. Obtener todos los legajos existentes
        legajos = [emp.obtenerNumeroLegajo() for emp in self._empleados]

        # 2. Calcular el siguiente número de legajo
        if legajos:
            nuevo_legajo = max(legajos) + 1
        else:
            nuevo_legajo = 1  # Primer legajo de la empresa

        # 3. Asignar el nuevo legajo y el estado de ALTA al empleado
        empleado.establecerNumeroLegajo(nuevo_legajo)
        empleado.establecerEstado(Empleado.ESTADO_ALTA)

        # 4. Agregar el empleado a la lista
        self._empleados.append(empleado)
            
    def bajaEmpleado(self, empleado):
        if empleado in self._empleados:
            empleado.establecerEstado(empleado.ESTADO_BAJA)

    # Consultas
    def obtenerRazonSocial(self):
        return self._razonSocial

    def obtenerProductos(self):
        return self._productos

    def obtenerEmpleadosDeAlta(self):
        empleados_alta = []
        for emp in self._empleados:
            if emp.obtenerEstado() == emp.ESTADO_ALTA:
                empleados_alta.append(emp)
        return empleados_alta

    def obtenerEmpleadosHitorico(self):
        return self._empleados

    


