class Producto:
    def __init__(self,nombre):
        self.__nombre = nombre

    def obtener_nombre(self):
        return self.__nombre
        
    # Método de texo
    def __str__(self):
        return f"Producto: {self.__nombre}"

    # Método de equivalencia
    def __eq__(self,otro):
        if isinstance(otro, Producto):
            return self.__nombre == otro.__nombre
        return False

    




