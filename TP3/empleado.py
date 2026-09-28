class Empleado:
    # Instancias de la clase
    ESTADO_ALTA = 1
    ESTADO_BAJA = 2
    # Constructores
    def __init__ (self,nombres,apellidos):
        self._numeroLegajo = 0
        self._nombres = nombres
        self._apellidos = apellidos
        self._estado = Empleado.ESTADO_ALTA

    # Comandos
    def establecerNumeroLegajo(self, numero):
        self._numeroLegajo = numero

    def establecerNombres(self, nombres):
        self._nombres = nombres

    def establecerApellidos(self, apellidos):
        self._apellidos = apellidos

    def establecerEstado(self, estado):
        self._estado = estado

    # Consultas
    def obtenerNumeroLegajo(self):
        return self._numeroLegajo
    
    def obtenerNombres(self):
        return self._nombres

    def obtenerApellidos(self):
        return self._apellidos

    def obtenerEstado(self):
        return self._estado

    


    

    