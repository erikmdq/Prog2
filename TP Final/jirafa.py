import animal


class Jirafa(animal.Animal):

    def __init__(self, id, nombre, id_cuidador_principal, largo_cuello):
        super().__init__(id, nombre, id_cuidador_principal)
        self.__largo_cuello = largo_cuello

    def establecer_largo_cuello(self, largo_cuello):
        self.__largo_cuello = largo_cuello

    def obtener_largo_cuello(self):
        return self.__largo_cuello
