class Empleado:
    # Instancias de la clase
    ESTADO_ALTA = 1
    ESTADO_BAJA = 2
    # Constructores
    def __init__ (self,nombres,apellidos):
        self.__numeroLegajo = 0
        self.__nombres = nombres
        self.__apellidos = apellidos
        self.__estado = Empleado.ESTADO_ALTA

    # Comandos
    def establecerNumeroLegajo(self, numero):
        self.__numeroLegajo = numero

    def establecerNombres(self, nombres):
        self.__nombres = nombres

    def establecerApellidos(self, apellidos):
        self.__apellidos = apellidos

    def establecerEstado(self, estado):
        self.__estado = estado

    # Consultas
    def obtenerNumeroLegajo(self):
        return self.__numeroLegajo
    
    def obtenerNombres(self):
        return self.__nombres

    def obtenerApellidos(self):
        return self.__apellidos

    def obtenerEstado(self):
        return self.__estado

    
    def __str__(self):
        estado = "ALTA" if self.__estado == Empleado.ESTADO_ALTA else "BAJA"
        return f"Empleado Legajo N° {self.__numeroLegajo}: {self.__nombres} {self.__apellidos} [{estado}]"

    def __eq__(self,otro):
        if isinstance(otro,Empleado):
            return self.__numero_Legajo == otro.__numero_Legajo
        return False
