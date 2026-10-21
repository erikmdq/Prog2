import abc


class Animal(abc.ABC):

    def __init__(self, id, nombre, id_cuidador_principal):
        self.__id = id
        self.__nombre = nombre
        self.__id_cuidador_principal = id_cuidador_principal

    def establecer_id(self, id):
        self.__id = id

    def establecer_nombre(self, nombre):
        self.__nombre = nombre

    def establecer_id_cuidador_principal(self, id_cuidador_principal):
        self.__id_cuidador_principal = id_cuidador_principal

    def obtener_id(self):
        return self.__id

    def obtener_nombre(self):
        return self.__nombre

    def obtener_id_cuidador_principal(self):
        return self.__id_cuidador_principal
